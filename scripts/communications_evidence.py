#!/usr/bin/env python3
"""Reproduce screenshot arithmetic, without asserting time-window comparability."""
import json
from decimal import Decimal
from pathlib import Path
root = Path(__file__).resolve().parents[1]
snapshot = json.loads((root / 'data/communications/observations.json').read_text())['website_snapshots']
results = {'evidence_id': 'COMM-09', 'source_id': snapshot['source_id'],
           'pages': [snapshot['earlier_page'], snapshot['later_page'], snapshot['claim_page']],
           'limitation': snapshot['comparability'], 'metrics': {}}
for name in ['site_sessions', 'unique_visitors', 'new_visitors', 'returning_visitors']:
    values = snapshot[name]
    earlier, later = Decimal(values['earlier_scaled']), Decimal(values['later_scaled'])
    results['metrics'][name] = {
        'earlier': str(earlier), 'later': str(later), 'rounded_source': values['rounded'],
        'baseline_denominator_growth_percent': str(((later - earlier) / earlier * 100).quantize(Decimal('.01'))),
        'ending_denominator_share_percent': str(((later - earlier) / later * 100).quantize(Decimal('.01')))}
print(json.dumps(results, indent=2))
