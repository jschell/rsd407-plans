#!/usr/bin/env python3
"""Build the evidence-bounded commitment disposition tracker; no network access."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
INPUTS = ['data/synthesis/cross-era-evaluation.json',
          'data/strategic-plans/transition-objective-matrix.json',
          'data/strategic-plans/middle-objective-matrix.json',
          'data/strategic-plans/commitment-disposition-reviews.json']
DISPOSITIONS = {'Retained', 'Revised', 'Replaced', 'Explicitly retired',
                'Absent from reviewed successor', 'Unknown'}

def read(path):
    return json.loads((ROOT / path).read_text())

def validate_review(ident, review, known):
    assert review['observed_disposition'] in DISPOSITIONS, ident
    assert review['formal_disposition'] in DISPOSITIONS, ident
    assert set(review['related_successor_ids']) <= known, ident
    assert set(review['successor_snapshot_objective_ids']) <= known, ident
    if review['observed_disposition'] == 'Absent from reviewed successor':
        assert review['successor_objective_list_complete'], ident
        assert review.get('successor_target_list_complete', True), ident
        assert review['successor_snapshot_objective_ids'], ident
        assert not review['related_successor_ids'], ident
    if review['formal_disposition'] != 'Unknown':
        assert review['formal_decision_source_ids'] and review['formal_decision_date'], ident
    if review.get('follow_up_state', 'Open') == 'Closed':
        assert review['closure_evidence_ids'] and review.get('closure_basis'), ident
    assert review.get('follow_up_state', 'Open') in {'Open', 'Closed'}, ident

def build():
    cross, transition, middle, policy = [read(p) for p in INPUTS]
    imported = []
    for i, r in enumerate(cross['objective_matrix']):
        original = r.get('original_evaluation', {})
        imported.append({'origin_assertion_id': r['assertion_id'], 'unit': 'Version-specific objective',
                         'version': r['version'], 'code': r['code'], 'commitment_raw': r['title_raw'],
                         'attainment': r['attainment_original'], 'implementation': r['implementation_original'],
                         'deadline_raw': original.get('deadline'),
                         'deadline_reference': original.get('target_and_deadline_reference', original.get('register_reference', original.get('register_file'))),
                         'baseline_raw': original.get('baseline'), 'source_locators': r['source_locators'],
                         'result_basis': original.get('attainment_basis', original.get('rationale', r['evidence_scope'])),
                         'origin': {'file': INPUTS[0], 'json_pointer': f'/objective_matrix/{i}'}})
    for i, r in enumerate(transition['goal_targets']):
        imported.append({'origin_assertion_id': r['assertion_id'], 'unit': 'Original goal metric',
                         'version': '2020–2025 year-one specification', 'code': f"Goal{r['goal']}",
                         'commitment_raw': r['target_raw'], 'attainment': r['result'], 'implementation': None,
                         'deadline_raw': '2022 school year' if r['assertion_id'] == 'TRANS-TARGET-13' else '2025',
                         'deadline_reference': 'Original wording retained in commitment_raw', 'baseline_raw': None,
                         'source_locators': [{'source_id': r['source_id'], 'pdf_pages': [r['pdf_page']]}],
                         'result_basis': r['basis'], 'origin': {'file': INPUTS[1], 'json_pointer': f'/goal_targets/{i}'}})
    r = middle['narrow_assertions'][0]
    assert r['assertion_id'] == 'MIDDLE-BOND-01'
    imported.append({'origin_assertion_id': r['assertion_id'], 'unit': 'Original success criterion',
                     'version': '2019–2020 year-five specification', 'code': '3B bond criterion',
                     'commitment_raw': r['criterion_raw'], 'attainment': r['result'], 'implementation': None,
                     'deadline_raw': 'February2020', 'deadline_reference': r['target_source'], 'baseline_raw': None,
                     'source_locators': [{'source_id': 'RSD407-ITER-2019', 'pdf_pages': [31]}],
                     'outcome_source_ids': r['source_ids'], 'result_basis': r['limitation'],
                     'origin': {'file': INPUTS[2], 'json_pointer': '/narrow_assertions/0'}})
    known = {r['origin_assertion_id'] for r in imported}
    assert set(policy['reviews']) == known
    rows = []
    for r in imported:
        ident = r['origin_assertion_id']; review = policy['reviews'][ident]
        validate_review(ident, review, known)
        source_ids = {s['source_id'] for s in cross['source_index']}
        assertion_ids = {s['assertion_id'] for s in cross['assertion_index']} | known
        assert set(review['formal_decision_source_ids']) <= source_ids, ident
        assert set(review['closure_evidence_ids']) <= source_ids | assertion_ids, ident
        flags = []
        historical = not ident.startswith('CROSS-CURRENT-')
        if review['observed_disposition'] == 'Absent from reviewed successor':
            flags.append('Unverified attainment; dedicated objective absent from reviewed successor')
        elif historical and review['observed_disposition'] == 'Revised':
            flags.append('Original commitment not conclusively closed; successor scope or criterion changed')
        elif historical:
            flags.append('Original commitment closure and successor disposition unresolved')
        if r['attainment'].startswith('Not met'):
            flags.append('Documented criterion miss; disposition/closure unresolved' if review.get('follow_up_state', 'Open') == 'Open' else 'Historical criterion miss preserved after documented closure')
        if not historical: flags.append('Current objective; no later complete register comparison')
        rows.append(dict(r, assertion_id='DISP-' + ident, kind='evaluation', disposition_review=review,
                         related_successor_origins=[next(x['origin'] for x in imported if x['origin_assertion_id'] == sid)
                                                   for sid in review['related_successor_ids']],
                         review_origin={'file': INPUTS[3], 'json_pointer': '/reviews/' + ident},
                         unverified_and_absent=r['attainment'].startswith('Cannot determine') and review['observed_disposition'] == 'Absent from reviewed successor',
                         missed_and_absent=r['attainment'].startswith('Not met') and review['observed_disposition'] == 'Absent from reviewed successor',
                         retired_after_miss=r['attainment'].startswith('Not met') and review['formal_disposition'] == 'Explicitly retired',
                         flags=flags, follow_up_state=review.get('follow_up_state', 'Open'),
                         closure_basis=review.get('closure_basis'),
                         evidence_needed='Original endpoint/coverage/result for the original commitment; authoritative revision, continuation or retirement decision with date and rationale. For an absence finding, intervening annual versions and formal task disposition are particularly material.'))
    return {'schema_version': 1, 'assertion_id': 'DISP-REGISTER-01', 'kind': 'evaluation', 'as_of': '2026-10-01',
            'scope': '54 version-specific objectives,14 original2020–2025 metrics and1 historical bond criterion. Overlapping units, not69 independent goals or a complete task census.',
            'input_sha256': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in INPUTS},
            'rules': ['Absence requires a complete relevant successor list; partial Board reports cannot prove disappearance.',
                      'A complete objective list is not a complete goal-metric list.',
                      'Observed thematic revision is distinct from formally adopted replacement or retirement.',
                      'Closure requires cited evidence and rationale; no automatic closure from deadline passage, related work or an X mark.',
                      'Confirmed retirement does not change an original Not met result into Met.',
                      'Open means an evidence question, not a finding of overdue work, failed execution or intentional abandonment.'],
            'counts': {'units': dict(Counter(r['unit'] for r in rows)),
                       'observed_disposition': dict(Counter(r['disposition_review']['observed_disposition'] for r in rows)),
                       'attainment': dict(Counter(r['attainment'] for r in rows))}, 'rows': rows}

def report(data):
    lines = ['# Commitment attainment and disposition tracker', '',
             '**DISP-REGISTER-01 — evaluation.** A commitment can disappear or change before its result is conclusively verified. This register tracks the original attainment judgment separately from what appears in a later reviewed plan and from any documented formal decision.', '',
             'It contains **54 version-specific objectives,14 original goal metrics and one bond-success criterion**. These overlapping units are not69 independent goals and are not a complete historical task census. Two criterion results are Not met; other attainment remains Cannot determine. Every entry retains its original assertion, source/page locator, raw commitment/deadline, comparison scope and evidence needed for closure.', '',
             '[Machine-readable register](../../data/strategic-plans/commitment-disposition-register.json) · [Curated disposition reviews](../../data/strategic-plans/commitment-disposition-reviews.json) · [Cross-era evaluation](cross-era-synthesis.md)', '',
             '## Cases requiring particular attention', '',
             '| Original assertion | Attainment | Later observation | What remains unresolved |',
             '| --- | --- | --- | --- |']
    for ident in ['MIDDLE-09', 'TRANS-OBJ-03', 'MIDDLE-07', 'MIDDLE-10', 'MIDDLE-BOND-01', 'TRANS-TARGET-03']:
        r = next(r for r in data['rows'] if r['origin_assertion_id'] == ident)
        review = r['disposition_review']
        lines.append(f"| {ident} | {r['attainment']} | {review['observed_disposition']} | {review['basis']} Formal decision/closure remains unverified. |")
    lines += ['', 'For MIDDLE-09, the dedicated policy-review objective is absent from the complete year-five objective list, while retrospective policy activity is still reported. For TRANS-OBJ-03, the dedicated department-integration objective is absent from the complete September2024 list, while related activities remain within other objectives. Neither observation proves abandonment or formal retirement.', '',
              'For the bond, the later criterion asks to present a bond rather than achieve a successful election. The original miss remains visible. For the ELA benchmark, current objective titles do not establish whether its original85% target was retained, revised or retired: an objective register is not a complete successor metric register.', '',
              '## How to read the tracker', '',
              '- **Attainment:** the existing result for the original specification, unchanged by successor wording.',
              '- **Observed disposition:** Retained, Revised, Replaced, Explicitly retired, Absent from reviewed successor, or Unknown. Initial Revised rows denote observed related scope changes, not verified Board replacement.',
              '- **Formal disposition:** requires a dated authoritative decision and source. All initial formal dispositions remain Unknown.',
              '- **Follow-up state:** Open or Closed, independently of attainment. Open means unresolved evidence, not overdue or failed execution. Current objectives have no later complete comparison and remain within the2027 cycle.',
              '- **Closure:** requires cited supporting evidence and an explanation. A documented retirement may resolve disposition while preserving a historical Not met or unverified attainment finding.', '',
              'No exact carry-forward finding is manufactured from reused codes, shared themes or a missing partial annual report. Original target-level closure remains unknown where the available successor inputs contain only objective definitions.', '',
              'The machine register has separate query flags: `unverified_and_absent`, `missed_and_absent` and `retired_after_miss`. The initial evidence supports two unverified dedicated-objective omissions; it establishes no formal retirement after a miss. That is a bounded evidence finding, not proof that no such retirement occurred. Unknown successor disposition remains Unknown, not a zero or a confirmed carry-forward.', '',
              '## All tracked commitments', '',
              'Each DISP ID is stable and resolves to one machine-register row. The origin IDs resolve through the existing cross-era assertion/source index. Full original wording and comparison pointers are preserved in JSON.', '',
              '| Tracker / origin ID | Version / code | Attainment | Observed disposition |',
              '| --- | --- | --- | --- |']
    for r in data['rows']:
        lines.append(f"| {r['assertion_id']} | {r['version']} / {r['code']} | {r['attainment']} | {r['disposition_review']['observed_disposition']} |")
    lines += ['', '## Update and reproduce', '',
              '1. Identify the origin assertion and inspect its source, reporting period and original deadline. Do not replace original wording with a successor target.',
              '2. Update its entry in `data/strategic-plans/commitment-disposition-reviews.json` with the compared complete/partial register, related successor IDs, basis and supporting evidence. An exact retained/replaced/retired claim requires appropriate evidence; title similarity is insufficient.',
              '3. For a formal decision, record its source IDs, decision date and rationale in the basis. For closure, add `closure_evidence_ids`, `closure_basis` and `follow_up_state: Closed`. Retain the original outcome. If new evidence changes attainment, update the originating evaluation and dependent synthesis first.',
              '4. Regenerate and review both tracker outputs. Commit corrections with their evidence and explanation; do not reopen generalized collection solely because an entry is Open.', '',
              '```sh', 'python scripts/build_commitment_disposition.py', 'python -m unittest discover -s tests -p test_commitment_disposition.py', '```', '',
              'The standard-library builder performs no source acquisition. `--output-dir /tmp/rsd407-disposition` writes a comparison copy of both outputs; compare each against the committed file. Input hashes identify the exact evidence/review versions. [Research guide](../research-guide.md) explains underlying source reproduction and preservation.', '']
    return '\n'.join(lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args(); data = build()
    targets = [(ROOT / 'data/strategic-plans/commitment-disposition-register.json', json.dumps(data, indent=2) + '\n'),
               (ROOT / 'docs/evaluations/commitment-disposition.md', report(data))]
    for path, content in targets:
        path = args.output_dir / path.name if args.output_dir else path
        path.parent.mkdir(parents=True, exist_ok=True); path.write_text(content)
