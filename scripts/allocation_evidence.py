#!/usr/bin/env python3
"""Reproduce the staffing exhibit discrepancy without choosing a corrected value."""
import json
from decimal import Decimal
from pathlib import Path

root = Path(__file__).resolve().parents[1]
observation = json.loads((root / 'data/allocation/observations.json').read_text())['staff_reduction']
line_sum = sum((Decimal(row['reduction_fte']) for row in observation['specialists_line_items']), Decimal('0'))
heading = Decimal(observation['specialists_heading_total_fte'])
print(json.dumps({
    'evidence_id': observation['evidence_id'],
    'pdf_page': observation['pdf_pages']['exhibit_a'],
    'specialists_heading_total_fte': str(heading),
    'specialists_line_item_sum_fte': str(line_sum),
    'line_items_minus_heading_fte': str(line_sum - heading),
    'determination': 'Source discrepancy retained; neither figure is final implemented staffing.'
}, indent=2))
