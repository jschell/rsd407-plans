#!/usr/bin/env python3
"""Reproduce percentage-point changes in the Board-reported early turnover data."""
import json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = json.loads((ROOT / 'data/strategic-plans/early-turnover-values.json').read_text())
results = []
for row in source['values']:
    baseline = Decimal(row['baseline_raw'])
    endpoint = Decimal(row['endpoint_raw'])
    change = endpoint - baseline
    results.append({**row, 'change_percentage_points': str(change),
                    'direction': 'decreased' if change < 0 else 'increased' if change > 0 else 'unchanged'})
print(json.dumps({'assertion_id': 'EARLY-DERIVED-01', 'kind': 'derived result',
                  'source_id': source['source_id'], 'pdf_page': source['page'],
                  'method': 'reported endpoint percent minus baseline percent; Decimal arithmetic',
                  'baseline_period': source['baseline_period'],
                  'endpoint_period': source['endpoint_period'],
                  'limitations': source['limitations'], 'values': results}, indent=2))
