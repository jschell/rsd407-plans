#!/usr/bin/env python3
"""Extract the hash-verified2020–2025 year-one plan without reconciling source conflicts."""
import argparse,hashlib,json,re,subprocess,tempfile
from pathlib import Path
HASH='f454eb2b71f8689c541e9a99aae4b1e7af50457f0556e7682f98272d2ff8c9ce'
RANGES={'1A':[23,24],'1B':[25,26],'1C':[27,28],'2A':[31],'2B':[32],'3A':[35,36],'3B':[37,38]}
COUNTS=[6,6,3,3,4,5,7]
def clean(s):return '\n'.join(x for x in s.splitlines() if not re.match(r'^(Riverview School District|Strategic Plan\s*$|\s*Page \d+\s*$)',x))
def build(path):
    if hashlib.sha256(path.read_bytes()).hexdigest()!=HASH:raise ValueError('PDF hash mismatch')
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'text';subprocess.run(['pdftotext','-layout',str(path),str(p)],check=True);pages=p.read_text().split('\f')
    timeline=[]
    for n in [47,48]:
        text=pages[n-1];hits=list(re.finditer(r'^\s*([123]/[A-Z]/\d+)\s',text,re.M))
        for i,h in enumerate(hits):
            block=text[h.start():hits[i+1].start() if i+1<len(hits) else len(text)]
            timeline.append({'code_raw':h.group(1),'source_page':n,'row_raw':clean(block).strip(),'completion_mark_raw':'X' if re.search(r'\bX\b',block) else None})
    objectives=[]
    for (code,nums),count in zip(RANGES.items(),COUNTS):
        text='\n'.join(clean(pages[n-1]) for n in nums);tasktext=text.split('TASKS:',1)[1].split('RESOURCES:',1)[0];hits=list(re.finditer(r'^\s*(\d+)\.\s+',tasktext,re.M));tasks=[]
        for i,h in enumerate(hits):
            number=int(h.group(1));block=tasktext[h.start():hits[i+1].start() if i+1<len(hits) else len(tasktext)].strip();key=f'{code[0]}/{code[1]}/{number}';row=next((x for x in timeline if x['code_raw']==key),None)
            tasks.append({'number':number,'definition_and_deadline_raw':block,'timeline_row':row,'status':'unmarked; completion unknown' if row else 'not found in timeline; completion unknown'})
        assert len(tasks)==count
        objectives.append({'code':code,'title_raw':text.split('TITLE:',1)[1].split('PROGRESS MEASUREMENT:',1)[0].strip(),'progress_raw':text.split('PROGRESS MEASUREMENT:',1)[1].split('TASKS:',1)[0].strip(),'definition_pdf_pages':nums,'tasks':tasks,'resources_and_roi_raw':text.split('RESOURCES:',1)[1].split('RESPONSIBILITIES:',1)[0].strip(),'responsibilities_raw':text.split('RESPONSIBILITIES:',1)[1].strip()})
    metrics=[]
    for goal,n in [(1,21),(2,29),(3,33)]:
        text=clean(pages[n-1]);head='2025 GOAL METRICS' if goal==1 else 'GOAL METRICS:';block=text.split(head,1)[1].split('SUPPORTING OBJECTIVES:',1)[0]
        if goal==3:block=block.split('The Communications Department',1)[0]
        for line in re.split(r'\n\s*[•\uf0b7]\s*',block):
            if line.strip():metrics.append({'goal':goal,'source_page':n,'text_raw':line.strip()})
    return {'assertion_id':'TRANS-REGISTER-01','kind':'observation','source_id':'RSD407-TRANS-PLAN2020','sha256':HASH,'period':'2020–2025; year one2020–2021','approval_record_raw':clean(pages[45]).strip(),'timeline_updated_raw':'2/9/2021','objectives':objectives,'task_count':sum(len(o['tasks']) for o in objectives),'timeline_rows':len(timeline),'timeline_marks':sum(x['completion_mark_raw']=='X' for x in timeline),'goal_metrics_and_notes':metrics,'limitations':['Source-stated School Board approval2/9/21 p46, separate motion unrecovered. Metadata creation2021-02-09 is not full-cycle status.','34 body tasks versus33 timeline rows;1/B/6 Equity Plan absent from timeline. Blank completion cells unknown, not failures.','3/B/2 body alumni site/ongoing versus timeline Ambassadors Program/March15;3/B/5 body translated documents/June15 versus timeline Communications audit/May15. Same codes do not establish same task.','3/A/1 bodyFebruary15(*normally November) versus timelineNovember15,2021. Preserve both.','3A summaryp20/p33 HR subplan title differs from bodyp35 broad Human Resources/Communication title;3B summary/supporting-title variants also preserved in evaluation.']}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('pdf',type=Path);a=p.parse_args();print(json.dumps(build(a.pdf),indent=2))
