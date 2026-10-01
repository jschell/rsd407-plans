#!/usr/bin/env python3
"""Rebuild task-register transcription from two hash-verified, locally reviewed PDFs."""
import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RANGES = {'2016': {'1A':[32], '1B':[33], '1C':[34], '1D':[35], '1E':[36], '2A':[38], '2B':[39,40], '2C':[41,42], '2D':[43], '3A':[45], '3B':[46,47], '3C':[48,49]},
          '2019': {'1A':[21,22], '1B':[23], '2A':[25], '2B':[26], '2C':[27,28], '3A':[30], '3B':[31]}}
EXPECTED = {'2016':[5,6,5,6,6,6,8,8,3,6,12,12], '2019':[10,6,4,3,8,5,7]}

def clean(text):
    return '\n'.join(line for line in text.splitlines() if not re.match(r'^(Riverview School District|Strategic Plan\s*$|Revised 7/11/16|\s*Page \d+\s*$)', line))

def build(paths):
    manifest = json.loads((ROOT/'data/manifests/iteration-sources.json').read_text())
    results = []
    for key,path in paths.items():
        sid = 'RSD407-ITER-2015' if key=='2016' else 'RSD407-ITER-2019'
        source = next(x for x in manifest if x['evidence_id']==sid)
        if hashlib.sha256(path.read_bytes()).hexdigest()!=source['sha256']:
            raise ValueError('PDF SHA-256 mismatch: '+sid)
        with tempfile.TemporaryDirectory() as td:
            textfile = Path(td)/'extraction.txt'
            subprocess.run(['pdftotext','-layout',str(path),str(textfile)],check=True)
            pages = textfile.read_text().split('\f')
        timeline = []
        for n in ([55,56,57] if key=='2016' else [40,41,42]):
            text = pages[n-1]
            hits = list(re.finditer(r'^\s*([123]/[A-Z0-9]+/\d+)\s',text,re.M))
            for j,hit in enumerate(hits):
                block = text[hit.start():hits[j+1].start() if j+1<len(hits) else len(text)]
                rawcode = hit.group(1)
                code = '2/B/3' if key=='2019' and rawcode=='2/5/3' else rawcode
                timeline.append({'task_code_raw':rawcode,'task_code_matched':code,'source_page':n,
                                 'row_raw':clean(block).strip(),
                                 'completion_mark_raw':'X' if re.search(r'\bX\b',block) else 'Postponed' if 'Postponed' in block else None,
                                 'interpretation':'reported complete' if re.search(r'\bX\b',block) else 'reported postponed' if 'Postponed' in block else 'unmarked; completion unknown'})
        objectives = []
        for (code,nums),count in zip(RANGES[key].items(),EXPECTED[key]):
            text = '\n'.join(clean(pages[n-1]) for n in nums)
            title = text.split('TITLE:',1)[1].split('PROGRESS MEASUREMENT:',1)[0].strip()
            progress = text.split('PROGRESS MEASUREMENT:',1)[1].split('TASKS',1)[0].strip()
            tasksraw = text.split('TASKS',1)[1].split('RESOURCES:',1)[0].strip()
            hits = list(re.finditer(r'^\s*(\d+)\.\s+',tasksraw,re.M));tasks=[]
            for j,hit in enumerate(hits):
                number = int(hit.group(1));block=tasksraw[hit.start():hits[j+1].start() if j+1<len(hits) else len(tasksraw)].strip()
                dates=[]
                for line in block.splitlines():
                    match = re.search(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December|Ongoing|Monthly|Quarterly|Completed|After audit|Any time)\b',line[55:])
                    if match:dates.append(line[55+match.start():].strip())
                status = next(x for x in timeline if x['task_code_matched']==f'{code[0]}/{code[1]}/{number}')
                tasks.append({'task_number':number,'definition_and_deadline_raw':block,'deadline_lines_raw':dates,
                              'timeline_evidence':status})
            assert len(tasks)==count,(key,code,len(tasks),count)
            owners = text.split('RESPONSIBILITIES:',1)[1].strip() if 'RESPONSIBILITIES:' in text else None
            objectives.append({'objective_code':code,'title_raw':title,'progress_measurement_raw':progress,
                               'definition_pdf_pages':nums,'resources_and_return_expectations_raw':text.split('RESOURCES:',1)[1].split('RESPONSIBILITIES:',1)[0].strip(),
                               'responsibilities_raw':owners,'baseline':None,'tasks':tasks})
        results.append({'snapshot':key,'source_id':sid,'sha256':source['sha256'],
                        'plan_period':'2015–2020','revision':'2016-07-11' if key=='2016' else '2019–2020 year five; PDF metadata created2020-02-19, not certified status date',
                        'objectives':objectives,'task_count':len(timeline),
                        'completed_marks':sum(x['completion_mark_raw']=='X' for x in timeline),
                        'postponed_marks':sum(x['completion_mark_raw']=='Postponed' for x in timeline),
                        'unmarked':sum(x['completion_mark_raw'] is None for x in timeline)})
    return {'schema_version':1,'kind':'observation','extraction':'pdftotext -layout, curated physical page ranges; extracted status cells visually checked; preserve raw wording/deadlines/owners and marks. Blank status is unknown, not zero or failure.',
            'limitations':['2016 copy is a revised snapshot, not untouched June2015 baseline.','Completion marks are district reports; no completion dates or independent fidelity proof.','2019 timeline raw code2/5/3 is matched to2/B/3 using objective page26 wording; typo preserved.','Raw fixed-layout rows retain wrapped text and adjacent timeline labels; original PDF remains authoritative.'], 'snapshots':results}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--snapshot2016',type=Path,required=True)
    parser.add_argument('--yearfive2019',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(build({'2016':args.snapshot2016,'2019':args.yearfive2019}),indent=2))
