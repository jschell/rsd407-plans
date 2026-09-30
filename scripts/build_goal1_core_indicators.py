#!/usr/bin/env python3
"""Select interpretable Goal 1 indicators from validated OSPI observations."""
from pathlib import Path
import pandas as pd
import re

D=Path("ospi_riverview/derived")
obs=pd.read_csv(D/"goal1_observations.csv",dtype=str,keep_default_na=False)
obs["numeric_value"]=pd.to_numeric(obs.numeric_value,errors="coerce")

def k(x): return re.sub("[^a-z0-9]","",str(x).lower())

# Outcome measures used for Goal 1 interpretation. Counts remain in the generic
# evidence table but are not themselves treated as performance outcomes.
def outcome_metric(family,metric):
    m=k(metric)
    if family=="assessment": return m.startswith("percent")
    if family=="growth": return m=="mediansgp" or m.startswith("percent")
    if family=="graduation": return m=="graduationrate"
    if family=="sqss": return m=="percent" or m.endswith("coursepercent")
    if family=="el": return m.endswith("dat") and ("percent" in m or "progress" in m or "profic" in m)
    return False

core=obs[[outcome_metric(f,m) for f,m in zip(obs.source_family,obs.metric)]].copy()
core.to_csv(D/"goal1_core_indicators.csv",index=False)

# Exact district/state comparisons for outcome measures.
num=core[core.value_state.eq("numeric")].copy()
keys=["source_family","source_period","dimension_key","metric"]
dist=num[num.scope.eq("district")].groupby(keys).numeric_value.agg(["count","first"]).reset_index()
wa=num[num.scope.eq("state")].groupby(keys).numeric_value.agg(["count","first"]).reset_index()
cmp=dist.merge(wa,on=keys,suffixes=("_district","_wa"))
cmp=cmp[(cmp.count_district==1)&(cmp.count_wa==1)].copy()
cmp["district_minus_wa"]=cmp.first_district-cmp.first_wa
cmp.rename(columns={"first_district":"district_value","first_wa":"wa_value"},inplace=True)
cmp=cmp[keys+["district_value","wa_value","district_minus_wa"]]
cmp.to_csv(D/"goal1_core_wa_comparisons.csv",index=False)

# Longitudinal district outcome changes. Exact dimension/metric identity only.
trend=num[num.scope.eq("district")][keys+["numeric_value"]].copy()
trend["year"]=pd.to_numeric(trend.source_period.str.extract(r"^(\d{4})")[0],errors="coerce")
trend=trend.dropna(subset=["year"]).sort_values(["source_family","dimension_key","metric","year"])
g=trend.groupby(["source_family","dimension_key","metric"],dropna=False)
trend["previous_period"]=g.source_period.shift()
trend["previous_value"]=g.numeric_value.shift()
trend["absolute_change"]=trend.numeric_value-trend.previous_value
trend=trend.dropna(subset=["previous_value"])
trend.to_csv(D/"goal1_core_changes.csv",index=False)

report=pd.DataFrame([
 {"check":"core_observations","value":len(core)},
 {"check":"core_numeric","value":int(core.value_state.eq("numeric").sum())},
 {"check":"core_suppressed","value":int(core.value_state.eq("suppressed").sum())},
 {"check":"core_wa_comparisons","value":len(cmp)},
 {"check":"core_changes","value":len(trend)},
])
report.to_csv(D/"goal1_core_report.csv",index=False)
print(report.to_string(index=False))
