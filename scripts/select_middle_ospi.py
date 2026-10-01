#!/usr/bin/env python3
"""Select preserved middle-era OSPI inputs from the hash-verified workflow ZIP."""
import pathlib,csv,json,hashlib,argparse,zipfile,io,itertools
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--artifact',type=pathlib.Path,required=True)
args=parser.parse_args()
EXPECTED='a20428371aa7a9ed24d8fa6b48c57adde7025562fc798199dc022d07604a29f3'
if hashlib.sha256(args.artifact.read_bytes()).hexdigest()!=EXPECTED:
 raise ValueError('Workflow artifact SHA-256 mismatch')
archive=zipfile.ZipFile(args.artifact)

spec=[('growth','normalized/growth_2014-15_to_2018-19_ufi5-ki2f.csv','ufi5-ki2f'),('assessment','normalized/assessment_2018-19_4h5k-di3v.csv','4h5k-di3v')];output={};prov=[]
for family,name,id in spec:
 matches=[n for n in archive.namelist() if n.endswith('/'+name) or n==name]
 if len(matches)!=1:raise ValueError('Expected one CSV member: '+name)
 member=archive.read(matches[0]);rows=list(csv.DictReader(io.StringIO(member.decode('utf-8'))));selected=[]
 for x in rows:
  if x['organizationlevel'] not in ['District','State']:continue
  if x['organizationlevel']=='District' and x['districtorganizationid']!='100222':continue
  if family=='growth':
   if x['studentgroup']!='All Students':continue
   keys=['source_dataset_id','schoolyear','organizationlevel','districtname','studentgrouptype','studentgroup','gradelevel','subject','mediansgp','studentcount','dataasof','suppression']
  else:
   if x['gradelevel']!='All Grades' or x['studentgroup'] not in ['All Students','English Language Learners','Low-Income','Students with Disabilities'] or x['dat']!='None' or x['test_administration_group']!='General':continue
   keys=['source_dataset_id','schoolyear','organizationlevel','districtname','studentgrouptype','studentgroup','gradelevel','testsubject','testadministration','test_administration_group','dat','count_of_students_tested','percent_consistent_grade','dataasof']
  selected.append({k:x.get(k) for k in keys})
 output[family]=selected;prov.append({'evidence_id':'OSPI-MIDDLE-'+family.upper(),'dataset_id':id,'url':'https://data.wa.gov/resource/'+id+'.json','artifact_member':name,'artifact_member_sha256':hashlib.sha256(member).hexdigest(),'selected_rows':len(selected),'selection':'District org100222 or State; growth All Students; assessment All Grades/General/datNone/All Students and three focal groups; all matching years retained.'})
output['provenance']={'artifact_id':11111512770,'run_id':36744065183,'run_url':'https://github.com/jschell/rsd407-plans/actions/runs/36744065183','artifact_sha256':'a20428371aa7a9ed24d8fa6b48c57adde7025562fc798199dc022d07604a29f3','artifact_reverified_at':'2026-10-01','original_acquired_at':'2026-09-30T16:27:34.722754+00:00','sources':prov,'limitation':'Artifact retention finite. Committed selected source values permit recalculation; future pulls require new provenance and may differ. No spring2020 assessment or2015 achievement baseline acquired in this pass.'}
seen={(x['organizationlevel'],x['studentgroup'],x['testsubject']) for x in output['assessment']}
expected=set(itertools.product(['District','State'],['All Students','English Language Learners','Low-Income','Students with Disabilities'],['ELA','Math','Science']))
output['coverage']={'growth_rows':len(output['growth']),'assessment_rows':len(output['assessment']),'missing_assessment_contexts':[dict(zip(['organizationlevel','studentgroup','testsubject'],x)) for x in sorted(expected-seen)],'interpretation':'No matching selected record for this context; unknown, never zero. No claim about why it is absent.'}
print(json.dumps(output,indent=2))
