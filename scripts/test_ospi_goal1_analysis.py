#!/usr/bin/env python3
"""Invariant checks for Goal 1 derived outputs."""
from pathlib import Path
import pandas as pd

D=Path("ospi_riverview/derived")
obs=pd.read_csv(D/"goal1_observations.csv")
cmp=pd.read_csv(D/"goal1_wa_comparisons.csv")
chg=pd.read_csv(D/"goal1_district_changes.csv")

assert set(obs.value_state.unique()) <= {"numeric","suppressed","missing","non_numeric"}
assert obs.loc[obs.value_state!="numeric","numeric_value"].isna().all(), "non-numeric source values became numbers"
assert (cmp.district_value-cmp.state_value-cmp.district_minus_state).abs().fillna(0).lt(1e-10).all()
assert (chg.numeric_value-chg.previous_value-chg.absolute_change).abs().fillna(0).lt(1e-10).all()
assert obs.source_dataset_id.astype(str).str.len().gt(0).all(), "lost source dataset provenance"
assert len(cmp) > 0, "no district/state matches; comparison dimensions likely include organization identity"
expected={"assessment","growth","graduation","sqss"}
missing=expected-set(cmp.source_family.unique())
assert not missing, f"missing expected district/state comparison families: {sorted(missing)}"
print(f"Goal 1 invariants OK: {len(obs):,} observations, {len(cmp):,} WA comparisons, {len(chg):,} changes")
