#!/usr/bin/env python3
"""Build reproducible Goal 1 analytical tables from normalized OSPI extracts.

This script never rewrites source extracts. It emits tidy observations plus
deterministic comparisons while preserving non-numeric/suppressed source values.
"""
from pathlib import Path
import re
import pandas as pd

ROOT=Path("ospi_riverview")
NORM=ROOT/"normalized"
DERIVED=ROOT/"derived"
DERIVED.mkdir(parents=True,exist_ok=True)

ID_HINTS=("id","code","year","grade","level","name","group","race","ethnic","gender","sex","test","subject","measure","indicator","cohort","type","status","notes","label","dataasof")
ORG_FIELDS={"organizationlevel","orglevel","organizationname","organizationid","county","esdname","esdorganizationid","districtname","districtcode","districtorganizationid","schoolname","schoolcode","schoolorganizationid","currentschooltype","schooltype"}
SUPPRESS=re.compile(r"(suppress|privacy|small|n/?a|not available|not reported|<\s*\d+|\*)",re.I)

def key(x): return re.sub("[^a-z0-9]","",str(x).lower())

def classify_scope(row):
    vals={key(k):str(v).strip().casefold() for k,v in row.items() if pd.notna(v)}
    level=vals.get("organizationlevel",vals.get("orglevel",""))
    dname=vals.get("districtname","")
    oname=vals.get("organizationname","")
    if level=="state": return "state"
    if dname=="riverview school district" or (level=="district" and oname=="riverview school district"):
        return "district"
    return "school_or_other"

def numeric_candidate(series,name):
    k=key(name)
    if any(h in k for h in ID_HINTS): return False
    cleaned=series.dropna().astype(str).str.strip()
    if cleaned.empty: return False
    parsed=pd.to_numeric(cleaned.str.replace("%","",regex=False).str.replace(",","",regex=False),errors="coerce")
    return parsed.notna().mean() >= 0.70

rows=[]
for path in sorted(NORM.glob("*.csv")):
    df=pd.read_csv(path,dtype=str,keep_default_na=False)
    if df.empty: continue
    source_cols=[c for c in df.columns if c.startswith("source_")]
    candidates=[c for c in df.columns if c not in source_cols and numeric_candidate(df[c],c)]
    dimensions=[c for c in df.columns if c not in source_cols and c not in candidates]
    for _,r in df.iterrows():
        scope=classify_scope(r)
        # Organization identity belongs in scope, not in the analytical match key.
        # Otherwise a State Total row can never match the corresponding district row.
        dim={c:r[c] for c in dimensions if key(c) not in ORG_FIELDS and str(r[c]).strip()!=""}
        dim_key=" | ".join(f"{c}={dim[c]}" for c in sorted(dim,key=key))
        org_level=r.get("organizationlevel",r.get("orglevel",""))
        school_name=r.get("schoolname","")
        organization_name=r.get("organizationname","")
        for metric in candidates:
            raw=str(r[metric]).strip()
            if not raw: state="missing"; value=None
            elif SUPPRESS.search(raw): state="suppressed"; value=None
            else:
                value=pd.to_numeric(raw.replace("%","").replace(",",""),errors="coerce")
                state="numeric" if pd.notna(value) else "non_numeric"
                value=float(value) if state=="numeric" else None
            rows.append({
                "source_family":r.get("source_family",""),
                "source_period":r.get("source_period",""),
                "source_dataset_id":r.get("source_dataset_id",""),
                "scope":scope,
                "organization_level":org_level,
                "school_name":school_name,
                "organization_name":organization_name,
                "dimension_key":dim_key,
                "metric":metric,
                "source_value":raw,
                "value_state":state,
                "numeric_value":value,
            })

obs=pd.DataFrame(rows)
obs.to_csv(DERIVED/"goal1_observations.csv",index=False)

# WA-relative comparisons are valid only for identical family/period/dimension/metric
# keys with exactly one district and one state numeric observation.
numeric=obs[obs.value_state.eq("numeric")].copy()
keys=["source_family","source_period","dimension_key","metric"]
district=numeric[numeric.scope.eq("district")].groupby(keys,dropna=False).numeric_value.agg(["count","first"]).reset_index()
state=numeric[numeric.scope.eq("state")].groupby(keys,dropna=False).numeric_value.agg(["count","first"]).reset_index()
cmp=district.merge(state,on=keys,suffixes=("_district","_state"))
cmp=cmp[(cmp.count_district==1)&(cmp.count_state==1)].copy()
cmp["district_minus_state"]=cmp.first_district-cmp.first_state
cmp.rename(columns={"first_district":"district_value","first_state":"state_value"},inplace=True)
cmp[keys+["district_value","state_value","district_minus_state"]].to_csv(DERIVED/"goal1_wa_comparisons.csv",index=False)

# Longitudinal change uses exact dimension+metric matches and adjacent available periods.
trend=numeric[numeric.scope.eq("district")][keys+["numeric_value"]].copy()
trend["period_start"]=trend.source_period.str.extract(r"^(\d{4})")[0]
trend["period_start"]=pd.to_numeric(trend.period_start,errors="coerce")
trend=trend.dropna(subset=["period_start"]).sort_values(["source_family","dimension_key","metric","period_start"])
trend["previous_period"]=trend.groupby(["source_family","dimension_key","metric"]).source_period.shift()
trend["previous_value"]=trend.groupby(["source_family","dimension_key","metric"]).numeric_value.shift()
trend["absolute_change"]=trend.numeric_value-trend.previous_value
trend.dropna(subset=["previous_value"])[["source_family","source_period","previous_period","dimension_key","metric","numeric_value","previous_value","absolute_change"]].to_csv(DERIVED/"goal1_district_changes.csv",index=False)

summary=pd.DataFrame([
    {"check":"observation_rows","value":len(obs)},
    {"check":"numeric_rows","value":int(obs.value_state.eq("numeric").sum())},
    {"check":"suppressed_rows","value":int(obs.value_state.eq("suppressed").sum())},
    {"check":"missing_rows","value":int(obs.value_state.eq("missing").sum())},
    {"check":"wa_comparisons","value":len(cmp)},
])
summary.to_csv(DERIVED/"goal1_analysis_report.csv",index=False)
print(summary.to_string(index=False))
