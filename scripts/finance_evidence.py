#!/usr/bin/env python3
"""Verify preserved sources, retrieve without overwriting, and calculate finance measures."""
import argparse
import hashlib
import json
import re
from decimal import Decimal
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads((ROOT / path).read_text())

def verify(destination):
    for s in read('data/manifests/finance-sources.json'):
        b = (destination / s['expected_filename']).read_bytes()
        if len(b) != s['byte_count'] or hashlib.sha256(b).hexdigest() != s['sha256']:
            raise ValueError('Source changed: ' + s['evidence_id'])
    print(f"Verified {len(read('data/manifests/finance-sources.json'))} PDFs against the committed source manifest")

def retrieve(destination, archived=False):
    destination.mkdir(parents=True, exist_ok=True)
    # Exclusive creation prevents overwriting any prior download.
    for s in read('data/manifests/finance-sources.json'):
        path = destination / s['expected_filename']
        url = s['url']
        if archived:
            archive = s.get('internet_archive', {})
            if archive.get('status') != 'capture_verified':
                raise ValueError('No verified archive: ' + s['evidence_id'])
            url = re.sub(r'/web/(\d+)/', r'/web/\1id_/', archive['capture_url'])
        with urlopen(url, timeout=60) as response:
            b = response.read()
        if not b.startswith(b'%PDF-'):
            raise ValueError('Not a PDF: ' + s['evidence_id'])
        with path.open('xb') as stream:
            stream.write(b)
        actual = hashlib.sha256(b).hexdigest()
        if actual != s['sha256']:
            raise ValueError('Upstream differs from preserved snapshot: ' + s['evidence_id'])
        print('Matched ' + s['evidence_id'])

def calculate():
    rows = read('data/finance/observations.json')['reserves']
    result = []
    previous = None
    previous_year = None
    for r in rows:
        balance, expenditure = Decimal(r['total_balance']), Decimal(r['expenditures'])
        if expenditure <= 0 or balance < 0:
            raise ValueError('Invalid finance input')
        item = {'evidence_id': r['evidence_id'], 'period': r['period'], 'basis': r['basis'],
                'total_balance_pct_of_expenditures': str((100 * balance / expenditure).quantize(Decimal('.0001')))}
        if previous is not None and r['basis'] == 'audited actual':
            item['change_in_total_balance'] = str(balance - previous)
            item['comparison_to_fiscal_year'] = previous_year
            item['comparison_is_consecutive'] = int(r['period'][:4]) == previous_year
        if r['basis'] == 'audited actual':
            previous = balance
            previous_year = int(r['period'][:4]) + 1
        result.append(item)
    fy25 = next(r for r in rows if r['period'] == '2024-25')
    expenditure = Decimal(fy25['expenditures'])
    reserve = Decimal(fy25['policy_reserve_amount_rounded'])
    diagnostics = {
        'evidence_id': fy25['evidence_id'],
        'actual_expenditure_5pct': str(expenditure * Decimal('.05')),
        'actual_expenditure_7pct': str(expenditure * Decimal('.07')),
        'listed_reserve_pct_of_actual_expenditure': str((100 * reserve / expenditure).quantize(Decimal('.0001'))),
        'numeric_target_determination': 'FY2025 balances exceed published May 2025 Policy 6000 numeric targets; audited note reserve-row inconsistency remains' }
    policy = read('data/finance/observations.json')['policy_6000']
    diagnostics.update({
        'policy_evidence_id': policy['evidence_id'],
        'total_target_amount': str(expenditure * Decimal(policy['total_balance_pct']) / 100),
        'unassigned_target_amount': str(expenditure * Decimal(policy['unassigned_balance_pct']) / 100),
        'unassigned_pct_of_actual_expenditures': str((100 * Decimal(fy25['unassigned_balance']) / expenditure).quantize(Decimal('.0001'))),
        'total_target_met': Decimal(fy25['total_balance']) >= expenditure * Decimal('.05'),
        'unassigned_target_met': Decimal(fy25['unassigned_balance']) >= expenditure * Decimal('.025')})
    budgets = []
    for b in read('data/finance/observations.json')['budget_denominators']:
        budgets.append({**b, 'seven_pct_amount': str(Decimal(b['expenditures']) * Decimal('.07')),
                        'qualification': b.get('qualification', '') + ' Historical comparator; motion does not specify fiscal year or denominator.'})
    output = {'reserves': result, 'fy2025_policy_diagnostic': diagnostics, 'historical_budget_comparators': budgets}
    print(json.dumps(output, indent=2))
    return output

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['verify', 'calculate', 'retrieve'])
    parser.add_argument('--destination', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--archive', action='store_true', help='Retrieve hash-verified archive instead of publisher URL')
    args = parser.parse_args()
    if args.action == 'verify':
        if args.destination is None:
            parser.error('verify requires --destination')
        verify(args.destination)
    elif args.action == 'retrieve':
        if args.destination is None:
            parser.error('retrieve requires --destination')
        retrieve(args.destination, args.archive)
    else:
        output = calculate()
        if args.output:
            args.output.write_text(json.dumps(output, indent=2) + '\n')
