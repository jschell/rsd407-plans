#!/usr/bin/env python3
"""Recalculate middle-era outcome diagnostics from preserved source values."""
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def number(value):
    try:
        result = Decimal(value)
        return result if result.is_finite() else None
    except (InvalidOperation, TypeError, ValueError):
        return None

def derive():
    data = json.loads((ROOT / 'data/strategic-plans/middle-ospi-values.json').read_text())
    growth = data['growth']
    keyed = {(x['schoolyear'], x['organizationlevel'], x['gradelevel'], x['subject']): x for x in growth}
    comparisons = []
    for x in growth:
        if x['organizationlevel'] != 'District' or x['schoolyear'] != '2018-19':
            continue
        baseline = keyed.get(('2014-15', 'District', x['gradelevel'], x['subject']))
        early = keyed.get(('2015-16', 'District', x['gradelevel'], x['subject']))
        state = keyed.get(('2018-19', 'State', x['gradelevel'], x['subject']))
        endpoint = number(x['mediansgp'])
        b = number(baseline['mediansgp']) if baseline else None
        e = number(early['mediansgp']) if early else None
        w = number(state['mediansgp']) if state else None
        comparisons.append({'grade': x['gradelevel'], 'subject': x['subject'],
                            'baseline_2014_15_raw': baseline['mediansgp'] if baseline else None,
                            'early_2015_16_raw': early['mediansgp'] if early else None,
                            'endpoint_2018_19_raw': x['mediansgp'],
                            'wa_endpoint_raw': state['mediansgp'] if state else None,
                            'change_from_baseline': str(endpoint-b) if endpoint is not None and b is not None else None,
                            'change_from_early_year': str(endpoint-e) if endpoint is not None and e is not None else None,
                            'endpoint_minus_wa': str(endpoint-w) if endpoint is not None and w is not None else None})
    assessment = data['assessment']
    akey = {(x['organizationlevel'], x['studentgroup'], x['testsubject'], x['testadministration']): x for x in assessment}
    snapshots = []
    for x in assessment:
        if x['organizationlevel'] != 'District':
            continue
        state = akey.get(('State', x['studentgroup'], x['testsubject'], x['testadministration']))
        allstudents = akey.get(('District', 'All Students', x['testsubject'], x['testadministration']))
        value = number(x['percent_consistent_grade'])
        wa = number(state['percent_consistent_grade']) if state else None
        allvalue = number(allstudents['percent_consistent_grade']) if allstudents else None
        snapshots.append({'subject': x['testsubject'], 'test': x['testadministration'], 'student_group': x['studentgroup'],
                          'district_raw': x['percent_consistent_grade'], 'wa_raw': state['percent_consistent_grade'] if state else None,
                          'district_percent': str(value*100) if value is not None else None,
                          'wa_percent': str(wa*100) if wa is not None else None,
                          'district_minus_wa_percentage_points': str((value-wa)*100) if value is not None and wa is not None else None,
                          'gap_vs_district_all_percentage_points': str((value-allvalue)*100) if value is not None and allvalue is not None else None})
    finance = json.loads((ROOT / 'data/strategic-plans/middle-finance-values.json').read_text())
    reserve = []
    for x in finance['reserves']:
        value = Decimal(x['unassigned_balance_raw']) / Decimal(x['actual_expenditures_raw']) * 100
        reserve.append({**x, 'unassigned_pct_actual_expenditures': str(value.quantize(Decimal('0.0001'))),
                        'above_5pct_diagnostic': value >= Decimal('5'), 'above_9pct_diagnostic': value >= Decimal('9')})
    return {'assertion_id': 'MIDDLE-DERIVED-01', 'kind': 'derived result', 'method': 'Decimal arithmetic; exact grade/subject/period/scope pairing; no imputation or averaged SGP',
            'growth': comparisons, 'assessment_2018_19': snapshots, 'reserves': reserve,
            'limitations': ['SGP changes compare same-grade repeated cross-sections, not the same pupils or absolute attainment.',
                           '2018–2019 assessment is an in-cycle snapshot, not a 2015 baseline or full spring2020 endpoint.',
                           'Focal groups compared with all students, which includes the focal group; not a non-focal contrast.',
                           'Reserve diagnostics use audited unassigned balance/actual expenditures; plan uncommitted terminology and denominator are not fully reconciled. No whole-plan compliance inference.']}

if __name__ == '__main__':
    print(json.dumps(derive(), indent=2))
