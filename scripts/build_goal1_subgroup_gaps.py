#!/usr/bin/env python3
"""Derive exact-context Goal 1 subgroup gaps from OSPI core indicators."""
from pathlib import Path
import re
import pandas as pd

D=Path("ospi_riverview/derived")
core=pd.read_csv(D/"goal1_core_indicators.csv",dtype=str,keep_default_na=False)
core["numeric_value"]=pd.to_numeric(core.numeric_value,errors="coerce")

def parse_dims(s):
    out={}
    for part in str(s).split(" | "):
        if "=" in part:
            k,v=part.split("=",1); out[k]=v
    return out

# OSPI families use several labels for the student-group dimension.
GROUP_NAMES={"studentgroup","studentgroupname","studentgroupcategory","studentgroupvalue","group","demographicgroup"}
GROUP_CONTEXT_FIELDS=GROUP_NAMES | {"studentgrouptype","grouptype","demographictype","studentgrouping"}
def find_group(d):
    for k,v in d.items():
        if re.sub("[^a-z0-9]","",k.lower()) in GROUP_NAMES:
            return k,v
    return None,None

records=[]
for i,r in core.iterrows():
    d=parse_dims(r.dimension_key)
    gfield,gvalue=find_group(d)
    if not gfield or not gvalue: continue
    base={k:v for k,v in d.items() if re.sub("[^a-z0-9]","",k.lower()) not in GROUP_CONTEXT_FIELDS}
    context=" | ".join(f"{k}={base[k]}" for k in sorted(base,key=lambda x:re.sub("[^a-z0-9]","",x.lower())))
    records.append({**r.to_dict(),"group_field":gfield,"student_group":gvalue,"gap_context":context})

g=pd.DataFrame(records)
if g.empty:
    raise SystemExit("No student-group dimensions found in core indicators")

def norm(v): return re.sub("[^a-z0-9]","",str(v).lower())
g["group_norm"]=g.student_group.map(norm)
# OSPI uses several aggregate labels across Report Card families/releases.
# Normalize punctuation/case and accept only explicit aggregate labels.
all_labels={"allstudents","allstudent","all","allstudentscombined","allstudentgroups","allstudentsgroup","total"}
keys=["source_family","source_period","scope","organization_level","school_name","organization_name","gap_context","metric"]
num=g[g.value_state.eq("numeric")].copy()
baseline_rows=num[num.group_norm.isin(all_labels)].copy()
print("student-group labels:", sorted(g.student_group.drop_duplicates().astype(str).tolist())[:80])
print("aggregate baseline rows:", len(baseline_rows))
baseline=baseline_rows.groupby(keys).numeric_value.agg(["count","first"]).reset_index()
sub=num[~num.group_norm.isin(all_labels)].copy()
gaps=sub.merge(baseline,on=keys,suffixes=("","_all"))
gaps=gaps[gaps["count"].eq(1)].copy()
gaps["gap_vs_all"]=gaps.numeric_value-gaps["first"]
gaps.rename(columns={"numeric_value":"subgroup_value","first":"all_students_value"},inplace=True)
keep=keys+["student_group","subgroup_value","all_students_value","gap_vs_all","source_dataset_id"]
gaps[keep].to_csv(D/"goal1_subgroup_gaps.csv",index=False)

# Track change in a subgroup gap only across identical context/metric/group.
trend=gaps[keep].copy()
trend["year"]=pd.to_numeric(trend.source_period.str.extract(r"^(\d{4})")[0],errors="coerce")
trend=trend.dropna(subset=["year"]).sort_values(["source_family","scope","organization_level","school_name","organization_name","gap_context","metric","student_group","year"])
tk=["source_family","scope","organization_level","school_name","organization_name","gap_context","metric","student_group"]
grp=trend.groupby(tk,dropna=False)
trend["previous_period"]=grp.source_period.shift()
trend["previous_gap"]=grp.gap_vs_all.shift()
trend["gap_change"]=trend.gap_vs_all-trend.previous_gap
trend=trend.dropna(subset=["previous_gap"])
trend.to_csv(D/"goal1_subgroup_gap_changes.csv",index=False)

report=pd.DataFrame([
 {"check":"group_observations","value":len(g)},
 {"check":"subgroup_gaps","value":len(gaps)},
 {"check":"gap_changes","value":len(trend)},
 {"check":"gap_families","value":gaps.source_family.nunique()},
])
report.to_csv(D/"goal1_subgroup_gap_report.csv",index=False)
print(report.to_string(index=False))
if len(num) and len(gaps)==0:
    raise SystemExit("Group-bearing numeric observations exist but no exact-context subgroup gaps were formed")
