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
    print('Verified 10 PDFs against the committed source manifest')

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
    for r in rows:
        balance, expenditure = Decimal(r['total_balance']), Decimal(r['expenditures'])
        if expenditure <= 0 or balance < 0:
            raise ValueError('Invalid finance input')
        item = {'evidence_id': r['evidence_id'], 'period': r['period'], 'basis': r['basis'],
                'total_balance_pct_of_expenditures': str((100 * balance / expenditure).quantize(Decimal('.0001')))}
        if previous is not None and r['basis'] == 'audited actual':
            item['change_in_total_balance'] = str(balance - previous)
        if r['basis'] == 'audited actual':
            previous = balance
        result.append(item)
    fy25 = rows[2]
    expenditure = Decimal(fy25['expenditures'])
    reserve = Decimal(fy25['policy_reserve_amount_rounded'])
    diagnostics = {
        'evidence_id': fy25['evidence_id'],
        'actual_expenditure_5pct': str(expenditure * Decimal('.05')),
        'actual_expenditure_7pct': str(expenditure * Decimal('.07')),
        'listed_reserve_pct_of_actual_expenditure': str((100 * reserve / expenditure).quantize(Decimal('.0001'))),
        'policy_compliance_determination': 'Cannot determine: effective policy and applicable budget denominator unresolved'}
    output = {'reserves': result, 'fy2025_policy_diagnostic': diagnostics}
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
