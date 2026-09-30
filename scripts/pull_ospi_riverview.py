#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,os,platform,re,sys,time,zipfile
from datetime import datetime,timezone
import pandas as pd, requests

BASE="https://data.wa.gov"; CATALOG="https://api.us.socrata.com/api/catalog/v1"
ORG_ID="100222"; DISTRICT_CODE="17407"; DISTRICT_NAME="Riverview School District"
OUT=Path("ospi_riverview"); RAW=OUT/"raw"; NORM=OUT/"normalized"
RAW.mkdir(parents=True,exist_ok=True); NORM.mkdir(parents=True,exist_ok=True)
HEADERS={"User-Agent":"rsd407-plans-ospi-collector/1.0"}
if os.getenv("SOCRATA_APP_TOKEN"): HEADERS["X-App-Token"]=os.environ["SOCRATA_APP_TOKEN"]

KNOWN={
("assessment","2018-19"):"4h5k-di3v",("assessment","2021-22"):"85v8-iyrc",("assessment","2022-23"):"yah4-nq3t",("assessment","2023-24"):"5i5h-c5pk",("assessment","2024-25"):"h5d9-vgwi",
("growth","2014-15_to_2018-19"):"ufi5-ki2f",
("graduation","2021-22"):"i23g-ymbg",("graduation","2022-23"):"kigx-4b2d",("graduation","2023-24"):"76iv-8ed4",("graduation","2024-25"):"isxb-523t",
("sqss","2018-19"):"2zsf-krin",("sqss","2021-22"):"tfs4-sdfn",("sqss","2022-23"):"hs5t-6yez",("sqss","2023-24"):"q9gf-prrp",("sqss","2024-25"):"f7j6-nk2h",
("el","2022-23"):"43ir-hnt6",("el","2023-24"):"qrns-2pnm",("el","2024-25"):"2mv4-s52p",
("enrollment","2022-23"):"dij7-mbxg",("enrollment","2023-24"):"q4ba-s3jc",("enrollment","2024-25"):"2rwv-gs2e",("wsif","2024_run"):"8v2t-vz3j"}
REQUIRED=[
("assessment","2018-19"),("assessment","2021-22"),("assessment","2022-23"),("assessment","2023-24"),("assessment","2024-25"),
("growth","2014-15_to_2018-19"),("growth","2022-23"),("growth","2023-24"),("growth","2024-25"),
("graduation","2018-19"),("graduation","2021-22"),("graduation","2022-23"),("graduation","2023-24"),("graduation","2024-25"),
("sqss","2018-19"),("sqss","2021-22"),("sqss","2022-23"),("sqss","2023-24"),("sqss","2024-25"),
("el","2021-22"),("el","2022-23"),("el","2023-24"),("el","2024-25"),
("enrollment","2018-19"),("enrollment","2021-22"),("enrollment","2022-23"),("enrollment","2023-24"),("enrollment","2024-25"),("wsif","2024_run")]
TERMS={"assessment":"Report Card Assessment Data {y}","growth":"Report Card Growth {y}","graduation":"Report Card Graduation {y}","sqss":"Report Card SQSS {y}","el":"Report Card English Learner Assessment {y}","enrollment":"Report Card Enrollment {y}","wsif":"Washington School Improvement Framework 2024"}

def log(msg):
    print(msg, flush=True)

def get(url,params=None):
    err=None
    for n in range(5):
        try:
            r=requests.get(url,params=params,headers=HEADERS,timeout=120)
            if 400 <= r.status_code < 500 and r.status_code != 429:
                r.raise_for_status()
            r.raise_for_status()
            return r
        except requests.HTTPError as e:
            err=e
            status=e.response.status_code if e.response is not None else None
            if status is not None and 400 <= status < 500 and status != 429:
                log(f"        request failed without retry: HTTP {status} — {url}")
                raise
            wait=min(2**n,16)
            log(f"        request attempt {n+1}/5 failed: HTTP {status or '?'}; retrying in {wait}s")
            time.sleep(wait)
        except requests.RequestException as e:
            err=e
            wait=min(2**n,16)
            log(f"        request attempt {n+1}/5 failed: {type(e).__name__}: {e}; retrying in {wait}s")
            time.sleep(wait)
    raise RuntimeError(f"GET failed {url}: {err}")

def discover(fam,period):
    q=TERMS[fam].format(y=period.replace("_run","").replace("_to_"," to "))
    data=get(CATALOG,{"search_context":"data.wa.gov","q":q,"limit":30}).json()
    needle={"assessment":"assessment","growth":"growth","graduation":"graduation","sqss":"sqss","el":"english learner","enrollment":"enrollment","wsif":"school improvement"}[fam]
    for x in data.get("results",[]):
        r=x.get("resource",{}); name=r.get("name","")
        if r.get("id") and needle in name.lower(): return r["id"],name
    return None,None

def schema_probe(did):
    """Fetch one row to learn the API field names without downloading the dataset."""
    rows=get(f"{BASE}/resource/{did}.json",{"$limit":1}).json()
    return pd.DataFrame(rows)

def soql_literal(value):
    return "'" + str(value).replace("'", "''") + "'"

def build_scope_where(sample):
    """Build a conservative server-side scope from fields proven present."""
    clauses=[]
    c=col(sample,"DistrictOrganizationId")
    if c: clauses.append(f"{c}={soql_literal(ORG_ID)}")
    c=col(sample,"DistrictCode")
    if c: clauses.append(f"{c}={soql_literal(DISTRICT_CODE)}")
    c=col(sample,"DistrictName")
    if c: clauses.append(f"lower({c})={soql_literal(DISTRICT_NAME.lower())}")
    c=col(sample,"OrganizationLevel")
    if c: clauses.append(f"lower({c})='state'")
    return " OR ".join(dict.fromkeys(clauses))

def fetch(did,where=None):
    rows=[]; off=0
    while True:
        started=time.monotonic()
        params={"$limit":50000,"$offset":off}
        if where: params["$where"]=where
        part=get(f"{BASE}/resource/{did}.json",params).json(); rows+=part
        log(f"        page {off//50000+1}: {len(part):,} rows ({time.monotonic()-started:.1f}s; {len(rows):,} total)")
        if len(part)<50000:return pd.DataFrame(rows)
        off+=50000

def key(x):return re.sub("[^a-z0-9]","",str(x).lower())
def col(df,*names):
    m={key(c):c for c in df.columns}
    return next((m[key(n)] for n in names if key(n) in m),None)

def scope(df):
    masks=[]
    for name,val in [("DistrictOrganizationId",ORG_ID),("DistrictCode",DISTRICT_CODE),("DistrictName",DISTRICT_NAME)]:
        c=col(df,name)
        if c:masks.append(df[c].astype(str).str.replace(r"\.0$","",regex=True).str.casefold().eq(val.casefold()))
    c=col(df,"OrganizationLevel")
    if c:masks.append(df[c].astype(str).str.casefold().eq("state"))
    if not masks:return df.iloc[0:0].copy()
    m=masks[0]
    for x in masks[1:]:m|=x
    return df[m].copy()

def digest(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return h.hexdigest()

report=[]; files=[]; acquisitions=[]
log(f"Starting OSPI collection: {len(REQUIRED)} required dataset-periods")
run_started=time.monotonic()
for idx,(fam,period) in enumerate(REQUIRED,1):
    item_started=time.monotonic()
    did=KNOWN.get((fam,period)); title=""
    log(f"[{idx:02d}/{len(REQUIRED)}] {fam} {period}" + (f" — known dataset {did}" if did else " — discovering dataset"))
    try:
        if not did:
            did,title=discover(fam,period)
            log(f"        discovery result: {did or 'NOT FOUND'}" + (f" — {title}" if title else ""))
        if not did:
            report.append([fam,period,"","NOT_FOUND",0,0,""])
            log(f"        NOT_FOUND ({time.monotonic()-item_started:.1f}s)")
            continue
        try:
            title=get(f"{BASE}/api/views/{did}").json().get("name",title)
        except requests.HTTPError as e:
            status=e.response.status_code if e.response is not None else "unknown"
            log(f"        metadata unavailable (HTTP {status}); continuing with dataset ID {did}")
            title=title or f"OSPI dataset {did}"
        sample=schema_probe(did)
        where=build_scope_where(sample)
        if not where:
            raise ValueError(f"cannot construct verified server scope; source columns={list(sample.columns)}")
        log(f"        server filter: {where}")
        full=fetch(did,where)
        acquisitions.append({"family":fam,"period":period,"dataset_id":did,"endpoint":f"{BASE}/resource/{did}.json","where":where,"method":"socrata-soql-filtered-json","local_scope_validation":True})
        # A plausible title/row count is not sufficient: verify the source
        # actually contains the requested school year before accepting it.
        if period != "2024_run" and "_to_" not in period:
            yc=col(full,"SchoolYear")
            if yc:
                years=set(full[yc].dropna().astype(str).str.strip())
                if period not in years:
                    raise ValueError(f"dataset period mismatch: requested {period}; source SchoolYear values={sorted(years)[:12]}")
        sub=scope(full)
        if len(sub)==0:
            log(f"        zero scoped rows; source columns: {', '.join(map(str,full.columns))}")
        log(f"        scope filter: {len(full):,} source rows -> {len(sub):,} Riverview/WA rows")
        c=col(sub,"DistrictName"); riv=int(sub[c].astype(str).str.casefold().eq(DISTRICT_NAME.casefold()).sum()) if c else 0
        raw=RAW/f"{fam}_{period}_{did}.csv";sub.to_csv(raw,index=False)
        norm=sub.copy()
        for n,v in reversed([("source_family",fam),("source_period",period),("source_dataset_id",did),("source_dataset_title",title)]):norm.insert(0,n,v)
        np=NORM/f"{fam}_{period}_{did}.csv";norm.to_csv(np,index=False)
        status="OK" if len(sub) and riv else "VALIDATION_WARNING"
        report.append([fam,period,did,status,len(sub),riv,title])
        files.extend([{"path":str(raw),"sha256":digest(raw)},{"path":str(np),"sha256":digest(np)}])
        log(f"        {status} — Riverview rows: {riv:,} — {time.monotonic()-item_started:.1f}s")
    except Exception as e:
        report.append([fam,period,did or "","FETCH_FAILED",0,0,str(e)])
        log(f"        FETCH_FAILED — {type(e).__name__}: {e} — {time.monotonic()-item_started:.1f}s")

rep=pd.DataFrame(report,columns=["family","period","dataset_id","status","scoped_rows","riverview_rows","note"])
rep.to_csv(OUT/"collection_report.csv",index=False)
manifest={"schema_version":1,"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"github_sha":os.getenv("GITHUB_SHA"),"github_run_id":os.getenv("GITHUB_RUN_ID"),"python":platform.python_version(),"district":{"name":DISTRICT_NAME,"organization_id":ORG_ID,"district_code":DISTRICT_CODE},"source_hosts":[BASE,CATALOG],"acquisitions":acquisitions,"artifacts":files,"collection_report_sha256":digest(OUT/"collection_report.csv")}
(OUT/"run_manifest.json").write_text(json.dumps(manifest,indent=2))
with zipfile.ZipFile("ospi_riverview.zip","w",zipfile.ZIP_DEFLATED) as z:
    for f in OUT.rglob("*"):
        if f.is_file():z.write(f,f)
ok=int((rep.status=="OK").sum())
log("")
log(rep.to_string(index=False))
log(f"Validated {ok}/{len(REQUIRED)} in {time.monotonic()-run_started:.1f}s")
sys.exit(0 if ok==len(REQUIRED) else 2)
