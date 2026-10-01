#!/usr/bin/env python3
"""Reproduce transition snapshots from the verified OSPI artifact or preserved inputs."""
import argparse,csv,hashlib,io,json,zipfile
from decimal import Decimal,InvalidOperation
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ZIP_HASH='a20428371aa7a9ed24d8fa6b48c57adde7025562fc798199dc022d07604a29f3'
SPECS=[('2021-22','85v8-iyrc'),('2024-25','h5d9-vgwi')]
GROUPS=['All Students','English Language Learners','Low-Income','Students with Disabilities','Homeless']

def select(path):
    if hashlib.sha256(path.read_bytes()).hexdigest()!=ZIP_HASH:raise ValueError('Artifact SHA-256 mismatch')
    rows=[];members=[];benchmark=[]
    with zipfile.ZipFile(path) as z:
        for period,dataset in SPECS:
            member=f'normalized/assessment_{period}_{dataset}.csv'
            names=[n for n in z.namelist() if n==member or n.endswith('/'+member)]
            if len(names)!=1:raise ValueError('Expected one source CSV')
            b=z.read(names[0]);selected=[]
            for x in csv.DictReader(io.StringIO(b.decode())):
                if period=='2024-25' and x['organizationlevel'] in ['District','State'] and (x['organizationlevel']=='State' or x['districtorganizationid']=='100222') and x['gradelevel']=='03' and x['studentgroup']=='All Students' and x['testsubject']=='ELA' and x['testadministration']=='SBAC':
                    benchmark.append({k:x.get(k) for k in ['source_dataset_id','schoolyear','organizationlevel','districtname','gradelevel','studentgroup','testsubject','testadministration','dat','percent_consistent_grade','count_of_students_expected','count_of_students_expected_1','count_consistent_grade_level','percent_participation','dataasof']})
                if x['organizationlevel'] not in ['District','State']:continue
                if x['organizationlevel']=='District' and x['districtorganizationid']!='100222':continue
                if x['schoolyear']!=period or x['gradelevel']!='All Grades' or x['studentgroup'] not in GROUPS or x['testadministration'] not in ['SBAC','WCAS']:continue
                keys=['source_dataset_id','schoolyear','organizationlevel','districtname','studentgrouptype','studentgroup','gradelevel','testsubject','testadministration','test_administration_group','dat','count_of_students_tested','count_of_students_expected','count_of_students_expected_1','count_consistent_grade_level','percent_consistent_tested','percent_participation','percent_consistent_grade','dataasof']
                selected.append({k:x.get(k) for k in keys})
            assert len(selected)==30
            rows+=selected;members.append({'dataset_id':dataset,'url':f'https://data.wa.gov/resource/{dataset}.json','artifact_member':member,'member_sha256':hashlib.sha256(b).hexdigest(),'selected_snapshot_rows':len(selected),'selected_benchmark_rows':2 if period=='2024-25' else 0})
    return {'assertion_id':'TRANS-OSPI-01','kind':'observation','rows':rows,'grade3_ela_benchmark_rows':benchmark,'provenance':{'artifact_id':11111512770,'run_id':36744065183,'run_url':'https://github.com/jschell/rsd407-plans/actions/runs/36744065183','zip_sha256':ZIP_HASH,'original_acquired_at':'2026-09-30T16:27:34.722754+00:00','sources':members,'selection':'District org100222 or State; exact source period; All Grades; five stated groups; SBAC/WCAS; retain suppression and rounded/percentage source strings.'},'limitations':['2021–2022 is in-period, not original2020 baseline. 2024–2025 overlaps the nominal newer plan.','2021 fractions and2024 percentage strings/rounding retained. Grade coverage and tested populations vary.','Any dat value other than None is conservatively treated as unavailable for calculations, even if a numeric string remains. No imputation.','Workflow artifact retention finite; committed selected values support recalculation.']}

def percent(x):
    if not x or x['dat']!='None':return None
    raw=x['percent_consistent_grade']
    try:
        result=Decimal(raw[:-1]) if raw.endswith('%') else Decimal(raw)*100
        return result if result.is_finite() else None
    except (InvalidOperation,ValueError,TypeError,AttributeError):return None

def derive():
    values=json.loads((ROOT/'data/strategic-plans/transition-ospi-values.json').read_text());rows=values['rows']
    keys=[(x['schoolyear'],x['organizationlevel'],x['studentgroup'],x['testsubject'],x['testadministration']) for x in rows]
    if len(keys)!=len(set(keys)):raise ValueError('Duplicate context')
    keyed=dict(zip(keys,rows));results=[]
    for x in rows:
        if x['organizationlevel']!='District':continue
        y=x['schoolyear'];g=x['studentgroup'];s=x['testsubject'];t=x['testadministration']
        wa=keyed.get((y,'State',g,s,t));allstudents=keyed.get((y,'District','All Students',s,t));v=percent(x);w=percent(wa);a=percent(allstudents)
        results.append({'period':y,'group':g,'subject':s,'test':t,'district_raw':x['percent_consistent_grade'],'district_dat':x['dat'],'district_percent':str(v) if v is not None else None,'wa_raw':wa['percent_consistent_grade'] if wa else None,'district_minus_wa_pp':str(v-w) if v is not None and w is not None else None,'gap_vs_all_students_pp':str(v-a) if v is not None and a is not None else None})
    changes=[]
    for g in GROUPS:
        for s,t in [('ELA','SBAC'),('Math','SBAC'),('Science','WCAS')]:
            b=percent(keyed.get(('2021-22','District',g,s,t)));e=percent(keyed.get(('2024-25','District',g,s,t)))
            changes.append({'group':g,'subject':s,'start_period':'2021-22','end_period':'2024-25','change_pp':str(e-b) if b is not None and e is not None else None})
    finance=json.loads((ROOT/'data/finance/observations.json').read_text())['reserves'];reserves=[]
    for x in finance:
        if x['period'] not in ['2020-21','2021-22','2022-23','2023-24','2024-25']:continue
        reserves.append({**x,'total_balance_pct_actual_expenditures':str((Decimal(x['total_balance'])/Decimal(x['expenditures'])*100).quantize(Decimal('0.0001')))})
    return {'assertion_id':'TRANS-DERIVED-01','kind':'derived result','assessment_snapshots':results,'assessment_changes':changes,'grade3_ela_state_benchmark':{'assertion_id':'TRANS-TARGET-03','target_percent':'85','source_id':'RSD407-TRANS-PLAN2020','source_pdf_page':21,'district_source_row':next(x for x in values['grade3_ela_benchmark_rows'] if x['organizationlevel']=='District'),'observed_percent':str(percent(next(x for x in values['grade3_ela_benchmark_rows'] if x['organizationlevel']=='District'))),'observed_minus_target_pp':str(percent(next(x for x in values['grade3_ela_benchmark_rows'] if x['organizationlevel']=='District'))-Decimal('85')) if percent(next(x for x in values['grade3_ela_benchmark_rows'] if x['organizationlevel']=='District')) is not None else None,'state_assessment_result':('Cannot determine' if percent(next(x for x in values['grade3_ela_benchmark_rows'] if x['organizationlevel']=='District')) is None else 'Met' if percent(next(x for x in values['grade3_ela_benchmark_rows'] if x['organizationlevel']=='District'))>=Decimal('85') else 'Not met'),'limitation':'Tests state-assessment component using2024–2025 All Students grade03 SBAC ELA; district assessment component not acquired. Does not establish continued governing authority after replacement.'},'finance_context':reserves,'limitations':['Changes use repeated district cross-sections, not same-pupil cohorts. Fractions versus rounded percentage source precision differs.','Focal groups compared with All Students which includes them. Suppressed values remain unknown.','No recovered2020 numerical targets, original baseline or replacement date. These are contextual diagnostics, not formal attainment or causal estimates.','Finance uses total balance/actual expenditures, not unassigned or plan-specific uncommitted reserves. No prior or revised2025 reserve threshold is back-projected.','Shared OSPI/finance records are reused, not independent additional evidence or separately counted successes.']}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--artifact',type=Path);args=p.parse_args()
    print(json.dumps(select(args.artifact) if args.artifact else derive(),indent=2))
