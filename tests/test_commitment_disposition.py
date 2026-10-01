import copy
import importlib.util
import json
import unittest
from unittest.mock import patch
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('tracker', ROOT / 'scripts/build_commitment_disposition.py')
tracker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tracker)

class DispositionTests(unittest.TestCase):
    def setUp(self):
        self.data = tracker.build()
        self.rows = {r['origin_assertion_id']: r for r in self.data['rows']}

    def test_complete_inventory_and_original_results(self):
        self.assertEqual(len(self.rows), 69)
        cross = tracker.read(tracker.INPUTS[0])
        for r in cross['objective_matrix']:
            self.assertEqual(self.rows[r['assertion_id']]['attainment'], r['attainment_original'])
        for r in tracker.read(tracker.INPUTS[1])['goal_targets']:
            self.assertEqual(self.rows[r['assertion_id']]['attainment'], r['result'])
        self.assertEqual(self.rows['MIDDLE-BOND-01']['attainment'], 'Not met')
        self.assertIn('Documented criterion miss; disposition/closure unresolved', self.rows['TRANS-TARGET-03']['flags'])

    def test_absence_is_bounded_to_complete_objective_lists(self):
        absent = [r['origin_assertion_id'] for r in self.rows.values()
                  if r['disposition_review']['observed_disposition'] == 'Absent from reviewed successor']
        self.assertEqual(set(absent), {'MIDDLE-09', 'TRANS-OBJ-03'})
        r = copy.deepcopy(self.rows['MIDDLE-09']['disposition_review'])
        r['successor_objective_list_complete'] = False
        with self.assertRaises(AssertionError): tracker.validate_review('MIDDLE-09', r, set(self.rows))

    def test_objective_list_does_not_establish_metric_absence(self):
        r = copy.deepcopy(self.rows['TRANS-TARGET-03']['disposition_review'])
        self.assertEqual(r['observed_disposition'], 'Unknown')
        r['observed_disposition'] = 'Absent from reviewed successor'
        with self.assertRaises(AssertionError): tracker.validate_review('TRANS-TARGET-03', r, set(self.rows))

    def test_closure_and_formal_retirement_require_evidence(self):
        r = copy.deepcopy(self.rows['MIDDLE-BOND-01']['disposition_review'])
        r['follow_up_state'] = 'Closed'
        with self.assertRaises(AssertionError): tracker.validate_review('MIDDLE-BOND-01', r, set(self.rows))
        r.pop('follow_up_state'); r['formal_disposition'] = 'Explicitly retired'
        with self.assertRaises(AssertionError): tracker.validate_review('MIDDLE-BOND-01', r, set(self.rows))

    def test_changed_successor_does_not_close_original_miss(self):
        r = self.rows['MIDDLE-BOND-01']
        self.assertEqual(r['disposition_review']['related_successor_ids'], ['TRANS-TARGET-09'])
        self.assertEqual(r['attainment'], 'Not met')
        self.assertEqual(r['follow_up_state'], 'Open')
        self.assertTrue(all(r['disposition_review']['formal_disposition'] == 'Unknown' for r in self.rows.values()))

    def test_documented_retirement_preserves_missed_result(self):
        policy = tracker.read(tracker.INPUTS[3])
        policy['reviews']['MIDDLE-BOND-01'].update(
            formal_disposition='Explicitly retired', formal_decision_source_ids=['RSD407-ITER-2019'],
            formal_decision_date='2026-10-01', follow_up_state='Closed',
            closure_evidence_ids=['MIDDLE-BOND-01'], closure_basis='Synthetic test of disposition closure only')
        original_read = tracker.read
        with patch.object(tracker, 'read', side_effect=lambda p: policy if p == tracker.INPUTS[3] else original_read(p)):
            changed = next(r for r in tracker.build()['rows'] if r['origin_assertion_id'] == 'MIDDLE-BOND-01')
        self.assertEqual(changed['attainment'], 'Not met')
        self.assertTrue(changed['retired_after_miss'])
        self.assertEqual(changed['follow_up_state'], 'Closed')

    def test_generated_output_matches_committed_copy(self):
        self.assertEqual(self.data, tracker.read('data/strategic-plans/commitment-disposition-register.json'))
        self.assertEqual(tracker.report(self.data), (ROOT / 'docs/evaluations/commitment-disposition.md').read_text())

if __name__ == '__main__': unittest.main()
