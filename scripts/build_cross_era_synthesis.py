#!/usr/bin/env python3
"""Rebuild the bounded cross-era synthesis from committed reviews, without new collection."""
import argparse,hashlib,json
from collections import Counter
from decimal import Decimal
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(path):return json.loads((ROOT/path).read_text())
def digest(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
INPUTS=['data/strategic-plans/early-objective-matrix.json','data/strategic-plans/middle-objective-matrix.json','data/strategic-plans/transition-objective-matrix.json','data/strategic-plans/iteration-inventory.json','data/strategic-plans/current-objective-register.json','data/synthesis/master-evaluation-matrix.json','data/strategic-plans/transition-diagnostics.json']
# Thematic membership is curated; membership is never proof of task identity or supersession.
FAMILIES={
'curriculum_assessment':(['EARLY-01','EARLY-02','EARLY-03','EARLY-06','EARLY-14','MIDDLE-02','MIDDLE-04','MIDDLE-05','MIDDLE-13','TRANS-OBJ-01','CROSS-CURRENT-1A'],'Sustained responsibility','Standards, curriculum and assessment recur, while instruments, intervention models and targets change.'),
'equity_interventions':(['EARLY-04','EARLY-15','MIDDLE-03','MIDDLE-13','TRANS-OBJ-02','CROSS-CURRENT-1B'],'Evolving challenge','General interventions and at-risk growth evolve into named focal-group gaps and specific learning/service tools. No exact all-era gap series or causal credit.'),
'department_technology':(['EARLY-05','MIDDLE-01','MIDDLE-04','MIDDLE-14','TRANS-OBJ-03','CROSS-CURRENT-1A'],'Evolving challenge','Integration themes recur; device/classroom/website tasks and later AI/data tools are different outputs.'),
'finance_allocation':(['EARLY-08','EARLY-16','MIDDLE-06','MIDDLE-15','TRANS-OBJ-04','CROSS-CURRENT-2A'],'Sustained responsibility','Financial stewardship persists; equitable allocation becomes explicit. Reserve targets and balance/denominator definitions change.'),
'capital_projects':(['MIDDLE-07','MIDDLE-16','TRANS-OBJ-04'],'Evolving challenge','Property/boundary/capital tasks and later bond presentation are related but not identical. No specific current capital-objective completion is inferred.'),
'safety_operations':(['EARLY-09','EARLY-17','MIDDLE-08','MIDDLE-17','TRANS-OBJ-05','CROSS-CURRENT-2B'],'Sustained responsibility','Plan reviews, emergency readiness and later access/technology projects recur; adoption or partial equipment work is not complete training/fidelity.'),
'governance_policy':(['EARLY-07','EARLY-10','EARLY-18','EARLY-21','MIDDLE-09'],'Sustained responsibility','Governance includes distinct policy review and evaluation-system tasks. Later omission of a dedicated objective does not prove completion, abandonment or failure.'),
'hr_recruitment':(['EARLY-11','EARLY-19','MIDDLE-10','MIDDLE-18','TRANS-OBJ-06','CROSS-CURRENT-3A'],'Evolving challenge','HR subplans and recruitment themes evolve into diversity/workforce-match tasks. Unmatched historical workforce and turnover categories cannot certify current match.'),
'staff_learning':(['EARLY-11','EARLY-19','MIDDLE-10','MIDDLE-18','TRANS-OBJ-06','CROSS-CURRENT-3B'],'Sustained responsibility','Onboarding/training recur within earlier HR objectives and a later separate professional-learning objective; events do not establish universal application.'),
'communications_outreach':(['EARLY-12','EARLY-13','EARLY-20','MIDDLE-11','MIDDLE-12','MIDDLE-19','TRANS-OBJ-07','CROSS-CURRENT-3C'],'Evolving challenge','Communications subplans/outreach evolve into social media, translation, audit recommendations and analytics. Reused codes and changed measures prevent automatic attainment transfer.')}

def build():
    matrix=[]
    for family,path in [('early',INPUTS[0]),('middle',INPUTS[1]),('transition',INPUTS[2])]:
        data=read(path)
        for i,r in enumerate(data['objectives']):
            version=r.get('iteration') or ('2015–2020 July2016 revision' if r.get('snapshot')=='2016' else '2015–2020 year-five2019–2020' if r.get('snapshot')=='2019' else '2020–2025 year-one2020–2021')
            source_ids=r.get('source_ids') or [r['source_id']]
            matrix.append({'assertion_id':r['assertion_id'],'kind':'evaluation','version':version,'row_unit':'version-specific objective','code':r.get('objective_code',r.get('code')),'title_raw':r.get('objective_text',r.get('title_raw')),'source_ids':source_ids,'source_locators':r.get('source_locators') or [{'source_id':source_ids[0],'pdf_pages':r['definition_pdf_pages']}],'origin':{'file':path,'json_pointer':f'/objectives/{i}'},'implementation_original':r['implementation'],'fidelity_original':r.get('implementation_fidelity',r.get('fidelity')),'attainment_original':r.get('goal_attainment',r.get('attainment')),'evidence_scope':'Partial observed Board register; full objective census unknown' if family=='early' else 'Confirmed reviewed snapshot; not every annual version','original_evaluation':r})
    current=read(INPUTS[4]);domains=read(INPUTS[5])['rows'];domain_by_id={r['assertion_id']:r for r in domains}
    for i,r in enumerate(current['objectives']):
        matrix.append({'assertion_id':'CROSS-CURRENT-'+r['code'],'kind':'evaluation','version':'2022–2027 September2024 revised snapshot with later bounded domain evidence','row_unit':'version-specific objective; domain component judgments retained','code':r['code'],'title_raw':r['title_raw'],'source_ids':[current['source_id']],'source_locators':[{'source_id':current['source_id'],'pdf_pages':[r['pdf_page']]}],'origin':{'file':INPUTS[4],'json_pointer':f'/objectives/{i}'},'implementation_original':'Cannot determine full objective; see component scopes','fidelity_original':'Cannot determine full objective','attainment_original':'Cannot determine','evidence_scope':'Current snapshot definition plus completed bounded domain review; no combined rating invented','component_findings':[domain_by_id[s] for s in r['domain_assertion_ids']]})
    ids={r['assertion_id'] for r in matrix};crosswalk=[]
    for i,(name,(members,classification,basis)) in enumerate(FAMILIES.items(),1):
        assert set(members)<=ids
        crosswalk.append({'assertion_id':f'CROSS-FAMILY-{i:02d}','kind':'evaluation','family':name,'objective_assertion_ids':members,'relationship':'Thematic continuity or evolving scope; exact retained/revised/replaced task lineage not independently established across every gap','recurrence':classification,'basis':basis,'limitations':'Many-to-many membership is not an independent evidence count, task identity, execution failure or authority finding.'})
    for r in matrix:r['family_ids']=[x['assertion_id'] for x in crosswalk if r['assertion_id'] in x['objective_assertion_ids']]
    assert all(r['family_ids'] for r in matrix)
    candidates=[]
    inventory=read(INPUTS[3])
    for r in inventory['iterations']:
        ident=r['iteration_id']
        wanted=([x['assertion_id'] for x in matrix if x['version'].startswith('2012')] if ident=='ITER-2012' else [x['assertion_id'] for x in matrix if x['version'].startswith('2013')] if ident=='ITER-2013' else [x['assertion_id'] for x in matrix if x['version']=='2015–2020 July2016 revision'] if ident=='ITER-2015' else [x['assertion_id'] for x in matrix if x['version']=='2015–2020 year-five2019–2020'] if ident=='ITER-2019' else [x['assertion_id'] for x in matrix if x['version']=='2020–2025 year-one2020–2021'] if ident=='ITER-2020' else [x['assertion_id'] for x in matrix if x['assertion_id'].startswith('CROSS-CURRENT-')] if ident=='ITER-2022' else [])
        candidates.append({'assertion_id':'CROSS-COVERAGE-'+ident.removeprefix('ITER-'),'iteration_id':ident,'period':r['effective_years'],'inventory_status':r['status'],'source_ids':r['source_ids'],'authority':r['authority'],'result':'Bounded version-specific review' if wanted else 'Insufficient evidence closeout; no objective register/rating invented','objective_assertion_ids':wanted,'objective_count':len(wanted) if wanted else None,'full_register_complete':False if ident in ['ITER-2012','ITER-2013'] or not wanted else 'Complete only for recovered snapshot; not all annual versions','reopen_only_for':'Original authoritative register/adoption/version record plus material matched implementation/outcome evidence; no exhaustive speculative crawl.'})
    # Compare three distinct dimensions, never average incompatible groups or suppressed cells.
    diagnostics=read(INPUTS[6]);snapshots=diagnostics['assessment_snapshots'];pairs=[]
    for group in ['All Students','English Language Learners','Low-Income','Students with Disabilities','Homeless']:
        a=next(x for x in snapshots if x['period']=='2021-22' and x['group']==group and x['subject']=='ELA');b=next(x for x in snapshots if x['period']=='2024-25' and x['group']==group and x['subject']=='ELA')
        def delta(key):return str(Decimal(b[key])-Decimal(a[key])) if a[key] is not None and b[key] is not None else None
        level=delta('district_percent');gap=delta('gap_vs_all_students_pp') if group!='All Students' else None;wa=delta('district_minus_wa_pp')
        pairs.append({'assertion_id':'CROSS-ELA-'+str(len(pairs)+1),'kind':'derived result','group':group,'subject':'ELA','periods':['2021-22','2024-25'],'input_assertion_id':'TRANS-DERIVED-01','input_file':INPUTS[6],'source_values':[a,b],'district_level_change_pp':level,'gap_change_pp':gap,'wa_advantage_change_pp':wa,'focal_level_improved':Decimal(level)>0 if level is not None else None,'gap_narrowed':Decimal(gap)>0 if gap is not None else None,'wa_advantage_improved':Decimal(wa)>0 if wa is not None else None,'limitations':'Descriptive repeated cross-sections with source rounding/coverage/denominator/methodology limits. All Students includes focal groups. Not a certified continuous all-era trend or causal estimate.'})
    recurrence=[{'assertion_id':'CROSS-REC-01','classification':'Sustained responsibility','scope':'Financial stewardship, safety readiness, policy/learning responsibilities','supporting_ids':['CROSS-FAMILY-04','CROSS-FAMILY-06','CROSS-FAMILY-07','CROSS-FAMILY-09'],'finding':'Dated recurring work supports sustained responsibilities, not repeated failure.'},
    {'assertion_id':'CROSS-REC-02','classification':'Evolving challenge','scope':'Equity interventions, technology, HR recruitment, communications and reserve target changes','supporting_ids':['CROSS-FAMILY-02','CROSS-FAMILY-03','CROSS-FAMILY-08','CROSS-FAMILY-10','TRANS-CROSSWALK-01'],'finding':'Definitions, tasks and scope change; exact supersession and all task dispositions remain unresolved.'},
    {'assertion_id':'CROSS-REC-03','classification':'Measurement failure','scope':'Public evaluation trace, not assertion that district has no internal data','supporting_ids':['SYN-10','TRANS-CONFLICT-01','TRANS-REGISTER-01','MIDDLE-CONFLICT-01','FIN-02','FIN-03','FIN-05','COMM-09'],'finding':'Documented conflicting titles/tasks/deadlines, target definitions and irreproducible stated analytics obstruct independent evaluation.'},
    {'assertion_id':'CROSS-REC-04','classification':'Resolved or institutionalized (qualified issue only)','scope':'Specific FY2017 Title I audit finding','supporting_ids':['SYN-03','FIN-08','FIN-11'],'finding':'Management Fully Corrected and subsequent auditor Title I testing/no reported finding support narrow correction. Not permanent institutionalization, all controls certified or final repayment proved.'},
    {'assertion_id':'CROSS-REC-05','classification':'Persistent unresolved problem — not established as an unqualified all-era trend','scope':'Focal-group academic disparities','supporting_ids':['MIDDLE-DERIVED-01','TRANS-DERIVED-01','G1-D1','G1-D2','G1-D3'],'finding':'Repeated available snapshots show disparities; denominator/coverage/republication limits and suppressed contexts prevent a certified continuous all-era gap series or causal persistence claim.'},
    {'assertion_id':'CROSS-REC-06','classification':'Recurrent implementation failure — not established','scope':'All reviewed eras','supporting_ids':['CROSS-REC-01','CROSS-REC-02','MIDDLE-BOND-01','TRANS-TARGET-03'],'finding':'Two narrower outcome/criterion shortfalls and repeated task titles do not provide repeated execution/fidelity failure for the same intervention.'}]
    input_hashes={p:digest(p) for p in INPUTS}
    edges=[]
    for old,new,relation,note in [
        ('EARLY-02','EARLY-14','Annual target deadline changed','Spring2013 versus spring2014; original assessment baseline/endpoint not established.'),
        ('MIDDLE-07','MIDDLE-16','Capital scope revised','Property/boundary steps versus prioritized projects; disappearance not proof of failed or completed boundary work.'),
        ('MIDDLE-10','MIDDLE-18','Named HR subplan changed','2013–2018 becomes2018–2023; new label does not certify prior-plan attainment.'),
        ('MIDDLE-13','TRANS-OBJ-01','Curriculum scope expanded','Related curriculum/support objective, different tasks and2025 goal metrics.'),
        ('TRANS-OBJ-01','CROSS-CURRENT-1A','Title continuity; task scope revised','Aligned curriculum title recurs;2024 AI, i-Ready, curriculum-cycle and fidelity tasks are not identical2021 work.'),
        ('TRANS-OBJ-02','CROSS-CURRENT-1B','Title continuity with terminology/task changes','English Language becomes Multilingual services; service/population definitions not silently assumed identical.'),
        ('TRANS-OBJ-04','CROSS-CURRENT-2A','Allocation-title continuity; financial targets changed','9% year-one task,14%2025 aspiration and current7% task have distinct scopes/definitions.'),
        ('TRANS-OBJ-05','CROSS-CURRENT-2B','Title continuity; operations scope revised','2021 camera/emergency/reopening tasks versus2024 access/RFID/common-practice tasks.'),
        ('TRANS-OBJ-06','CROSS-CURRENT-3A','HR scope reorganized','Broad HR subplan/practices versus diverse recruitment/workforce match.'),
        ('TRANS-OBJ-06','CROSS-CURRENT-3B','HR learning becomes separate objective','One older HR objective connects thematically to two current objectives, not two independent successes.'),
        ('TRANS-OBJ-07','CROSS-CURRENT-3C','Communication title theme moved to another code','Current3B is professional learning; old3B communications maps thematically to current3C.'),
        ('EARLY-10','MIDDLE-09','Recurring policy-review responsibility','Later absence of dedicated objective does not establish retirement or completion.')]:
        edges.append({'assertion_id':'CROSS-LINK-'+str(len(edges)+1).zfill(2),'from_assertion_id':old,'to_assertion_id':new,'relationship':relation,'basis':note,'authority_limit':'No full chain of annual adoption/revision/task-disposition records; no automatic completion or attainment transfer.'})
    index=[]
    for path,array in [(INPUTS[0],'objectives'),(INPUTS[1],'objectives'),(INPUTS[1],'narrow_assertions'),(INPUTS[2],'objectives'),(INPUTS[2],'goal_targets'),(INPUTS[2],'transition_observations'),(INPUTS[5],'rows')]:
        for i,r in enumerate(read(path)[array]):index.append({'assertion_id':r['assertion_id'],'file':path,'json_pointer':f'/{array}/{i}','sha256':digest(path),'kind':r.get('kind',r.get('layer','evaluation'))})
    for path in ['data/strategic-plans/middle-outcome-diagnostics.json','data/strategic-plans/transition-diagnostics.json','data/strategic-plans/early-turnover-changes.json','data/strategic-plans/transition-crosswalk.json','data/strategic-plans/current-objective-register.json','data/strategic-plans/transition-ospi-values.json','data/strategic-plans/transition-task-register.json']:
        d=read(path);index.append({'assertion_id':d.get('assertion_id','EARLY-DERIVED-01'),'file':path,'json_pointer':'','sha256':digest(path),'kind':d.get('kind','derived result')})
    # Existing domain assertion labels remain traceable through their bounded reports.
    known_index={x['assertion_id'] for x in index}
    for domain in domains:
        for label in domain['supporting_assertion_ids']:
            labels=[label]
            if label=='G1-B1/G1-B2':labels+=['G1-B1','G1-B2']
            for ident in labels:
                if ident in known_index:continue
                path=domain['evidence_document']
                if ident not in (ROOT/path).read_text() and not (ident.startswith('G1-B') and 'G1-B1' in (ROOT/path).read_text()):raise ValueError('Missing domain label: '+ident)
                index.append({'assertion_id':ident,'file':path,'locator':'Assertion label in domain report; source values/pages/calculation methods retained there','sha256':digest(path),'kind':'existing domain assertion; see report'})
                known_index.add(ident)
    for ident,path in [('FIN-05','docs/evaluations/goal-2-finance-evidence-synthesis.md'),('SYN-10','docs/evaluations/final-synthesis.md'),('TRANS-CONFLICT-01','docs/evaluations/plan-2020-2025.md'),('MIDDLE-CONFLICT-01','docs/evaluations/middle-plan-iterations.md')]:
        assert ident in (ROOT/path).read_text()
        index.append({'assertion_id':ident,'file':path,'locator':'Assertion label','sha256':digest(path),'kind':'evaluation or source conflict; see report'})
    for array,values in [('objective_matrix',matrix),('coverage',candidates),('crosswalk',crosswalk),('version_links',edges),('recurrence',recurrence),('outcome_dimension_comparison',pairs)]:
        for i,r in enumerate(values):
            if r['assertion_id'].startswith('CROSS-'):index.append({'assertion_id':r['assertion_id'],'file':'data/synthesis/cross-era-evaluation.json','json_pointer':f'/{array}/{i}','kind':r.get('kind','evaluation'),'generated_by':'scripts/build_cross_era_synthesis.py; input hashes above'})
    index.append({'assertion_id':'CROSS-SYNTHESIS-01','file':'data/synthesis/cross-era-evaluation.json','json_pointer':'','kind':'evaluation','generated_by':'scripts/build_cross_era_synthesis.py; input hashes above'})
    sources=[];preservation=[]
    for path in sorted((ROOT/'data/manifests').glob('*.json')):
        rel=str(path.relative_to(ROOT));d=read(rel)
        if not isinstance(d,list):continue
        eligible=[x for x in d if isinstance(x,dict) and 'evidence_id' in x and 'url' in x]
        if not eligible:continue
        counter=Counter(x.get('internet_archive',{}).get('status','not_recorded') for x in eligible)
        preservation.append({'manifest':rel,'sha256':digest(rel),'records':len(eligible),'capture_verified':counter['capture_verified'],'statuses':dict(counter)})
        for i,s in enumerate(d):
            if not isinstance(s,dict) or 'evidence_id' not in s or 'url' not in s:continue
            sources.append({'source_id':s['evidence_id'],'manifest':rel,'json_pointer':f'/{i}','url':s['url'],'sha256':s.get('sha256'),'format':s.get('format'),'capture_status':s.get('internet_archive',{}).get('status','not_recorded'),'limitation':'Manifest record, not independent evidence. Link attempts with no PDF hash remain link attempts.'})
    return {'schema_version':1,'assertion_id':'CROSS-SYNTHESIS-01','kind':'evaluation','as_of':'2026-10-01','scope':'12 inventoried candidates;47 historical version-specific objective rows and7 current snapshot objectives. Seven existing domain rows are retained separately, with FY2017 audit issue contextual rather than a current objective. No composite score.','reproduction':{'script':'scripts/build_cross_era_synthesis.py','input_sha256':input_hashes,'acquisition':'No new sources or archive submissions in this synthesis.'},'coverage':candidates,'objective_matrix':matrix,'current_domain_findings':domains,'crosswalk':crosswalk,'version_links':edges,'recurrence':recurrence,'outcome_dimension_comparison':pairs,'narrow_findings':{'historical_bond_criterion':'MIDDLE-BOND-01: Not met; not all communication tasks failed.','historical_ela_state_benchmark':'TRANS-TARGET-03: Not met state-assessment component; district assessment/replacement unresolved.','current_revised_policy':'SYN-02: FY2025 revised-policy numerical tests Met; distinct from prior uncommitted strategic targets.','audit_correction':'SYN-03: Qualified correction of specific FY2017 issue; no whole-plan attainment.'},'assertion_index':index,'source_index':sources,'preservation':{'counting_rule':'Manifest records, not unique independent sources; shared/reused byte hashes and link attempts retained. Artifact11111512770 in run36744065183 provenance lives in selected OSPI values; workflow retention finite.','manifests':preservation,'total_records':sum(x['records'] for x in preservation),'verified_capture_records':sum(x['capture_verified'] for x in preservation)},'stopping_rule':'Each known candidate has a bounded review or insufficient-evidence closeout. Reopen only for a material authoritative register/version/definition/fidelity or outcome artifact. No background work, forecast waiting, generalized new pipeline or invented zeros.'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();text=json.dumps(build(),indent=2)+'\n'
    if a.output:a.output.write_text(text)
    else:print(text,end='')
