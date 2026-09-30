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
# Missing/suppressed measure cells must remain observations; neither may become zero.
assert not ((obs.value_state.isin(["missing","suppressed"])) & obs.numeric_value.notna()).any()
assert (cmp.district_value-cmp.state_value-cmp.district_minus_state).abs().fillna(0).lt(1e-10).all()
assert (chg.numeric_value-chg.previous_value-chg.absolute_change).abs().fillna(0).lt(1e-10).all()
assert obs.source_dataset_id.astype(str).str.len().gt(0).all(), "lost source dataset provenance"
# School-level rows may carry Riverview as their parent DistrictName, but must
# never be treated as district observations.
district_rows=obs[obs.scope.eq("district")]
assert not district_rows.organization_level.astype(str).str.casefold().eq("school").any(), "school rows entered district scope"

# A period-labelled derived row may not carry a different SchoolYear in its dimensions.
def year_ok(row):
    import re
    m=re.fullmatch(r"(\d{4})-(\d{2})",str(row.source_period))
    if not m: return True
    hit=re.search(r"(?:^| \| )schoolyear=([^|]+)",str(row.dimension_key),re.I)
    if not hit: return True
    start=int(m.group(1)); end=2000+int(m.group(2))
    return hit.group(1).strip() in {str(row.source_period),f"{start}-{end}",str(end)}
assert obs.apply(year_ok,axis=1).all(), "derived observations contain SchoolYear outside source_period"
assert len(cmp) > 0, "no district/state matches; comparison dimensions likely include organization identity"
expected={"assessment","growth","graduation","sqss"}
missing=expected-set(cmp.source_family.unique())
assert not missing, f"missing expected district/state comparison families: {sorted(missing)}"
print(f"Goal 1 invariants OK: {len(obs):,} observations, {len(cmp):,} WA comparisons, {len(chg):,} changes")
