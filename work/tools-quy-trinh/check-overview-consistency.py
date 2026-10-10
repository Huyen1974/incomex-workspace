"""Validate design declarations and stored application; does not enforce production execution."""
import copy,hashlib,json,re,sys
from pathlib import Path
path=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name('view.html'))
s=path.read_text();c=json.loads(re.search(r'<script id="tqt-composite-processes"[^>]*>(.*?)</script>',s,re.S)[1])
REQUIRED={'application_id','process_code','process_version','target_code','target_version','scope','scope_stage','input_refs','actor','reviewer','recipient','output_ref','issue_register_ref','acceptance','return_to','plan_ref','start_confirmation'}
SELECT={'code','version','scope','inputs','actor','reviewer','recipient','acceptance','authority'}
BRANCH={'S1_OK':'S2','S2_OK':'S3','S3_RETURN':'S4','S4_PASS':'S6','S4_FAIL':'S5','S6_ACK':'XONG','NO_PROCESS':'S5','MISSING_INPUT':'S5'}
def resolve(d,ref):
 if ref.startswith('#'):
  assert ('id="'+ref[1:]+'"') in s;return
 m=re.fullmatch(r'catalog\.normal_processes\[code=([^\]]+)\]\.steps\[(\d+)\]',ref)
 if m:rows=[p for p in d['catalog']['normal_processes'] if p['code']==m[1]]
 else:
  m=re.fullmatch(r'processes\[0\]\.supplements\[id=([^\]]+)\]\.steps\[(\d+)\]',ref);assert m,ref
  rows=[p for p in d['processes'][0]['supplements'] if p['id']==m[1]]
 assert len(rows)==1 and int(m[2])<len(rows[0]['steps']) and rows[0]['steps'][int(m[2])]
def validate_application(a,r):
 assert REQUIRED<=set(a) and all(a[k] for k in REQUIRED)
 assert a['process_code']=='MOW-TH-005' and a['process_version']==r['records'][4]['version']
 assert SELECT<=set(a['selected_process']) and all(a['selected_process'][k] for k in SELECT)
 by={p['code']:p for p in r['records']+r['normal_processes']};sel=a['selected_process'];assert sel['code'] in by and sel['code']!='MOW-TH-005' and sel['version']==by[sel['code']]['version']
 assert a['state'] in r['work_form']['states']
 fields={f['key'] for f in r['work_form']['fields']};answers={x['key']:x for x in a['declarations']};assert len(answers)==len(a['declarations']) and set(answers)==fields
 assert all(x['owner'] and x['answer'] and x['result'] in ['NOT_TESTED','PASS','FAIL','BLOCKED','NA'] and x['validity'] in ['CURRENT','RECHECK'] for x in answers.values())
 seen=set()
 for p in a['plan']:
  assert p['id'] not in seen and set(p['depends_on'])<=seen and p['process'] in by and p['actor'] and p['output'];seen.add(p['id'])
 if a['state'] in ['SAN_SANG','DANG_LAM','DANG_KIEM','CHO_DUYET','DA_BAN_GIAO','XONG']:
  sc=a['start_confirmation'];assert sc['state']=='CONFIRMED' and sc['actor'] and sc['evidence_ref'] and sc['plan_version']==a['plan_version']
  assert a['questions_complete'] and a['requirements_checked']
  for key in r['records'][4]['workflow']['start_gate']['requires']:
   if key=='start_confirmation':continue
   ans=answers[key];assert ans['result']=='PASS' and ans['validity']=='CURRENT' and ans['evidence_refs']
 if a['state'] in ['CHO_DUYET','DA_BAN_GIAO','XONG']:
  assert a['test_result']=='PASS' and all(a['connection_tests'][k]=='PASS' for k in ['in','out'])
  assert all(p['status']=='DONE' or (p['status']=='NA' and p.get('reason')) for p in a['plan'] if p['process']!='MOW-TH-005')
 if a['state'] in ['DA_BAN_GIAO','XONG']:
  assert a['release']['state']=='APPROVED' and a['release']['decision_ref'] and a['release']['ack_ref']
 if a['scope_stage']=='G1':assert not a['deployed'] and a['excluded_stages']==['G2','G3'] and a['release']['scope']=='G1_DESIGN_ONLY'
 if a['state']=='BI_CHAN':assert a['reason'] and a['next_owner'] and a['next_trigger']
def validate(d):
 r=d['catalog'];allp=r['records']+r['normal_processes'];by={x['code']:x for x in allp};assert len(by)==len(allp)
 for p in allp:assert p['object_type']=='MOW' and all(p['guide'].get(k) for k in ['purpose','when','avoid','done'])
 for b in r['instruction_owners']:assert b['process'] in by and ('id="'+b['anchor']+'"') in s
 for p in r['records']:
  for ref in p['child_refs']:assert ref['code'] in by and ref['version']==by[ref['code']]['version'] and ref['relation'] in ['candidate','conditional_call']
 w=by['MOW-TH-005']['workflow'];assert w['selection']['cardinality']==1 and 'MOW-TH-005' in w['selection']['exclude'];assert SELECT<=set(w['selection']['required'])
 assert REQUIRED<=set(r['trial_contract']['required']) and 'issue_ref' not in r['trial_contract']['required']
 assert all(w['branches'].get(k)==v for k,v in BRANCH.items())
 assert all(w['branches'][k].startswith('DỪNG') for k in ['BLOCKED','REJECTED','CANCELLED'])
 assert w['start_gate']['before']=='S3' and {'identity','connections_in','connections_out','prerequisites','execution_conditions','plan','records','roles','acceptance','questions','start_confirmation'}<=set(w['start_gate']['requires'])
 steps=w['steps'];assert len(steps)==6
 for st in steps:
  assert st['object_type']=='MOT' and st['owner']=='MOW-TH-005' and st['version']==by['MOW-TH-005']['version']
  b=st['binding'];assert b['kind'] in ['process','external_process','selected_process','selected_contract','issue_handler']
  if b['kind'] in ['process','issue_handler']:assert b['code'] in by and b['version']==by[b['code']]['version']
  if b['kind']=='external_process':assert b['source'] and b['source_version'] and b['runtime_version'] is None
  if b['kind']=='selected_process':assert b['field']=='selected_process' and 'MOW-TH-005' in b['exclude']
  if b['kind']=='selected_contract':assert b['field'] in ['selected_process.acceptance','selected_process.recipient']
 assert steps[3]['binding']['field']=='selected_process.acceptance' and steps[5]['binding']['field']=='selected_process.recipient'
 tasks=[t for p in r['normal_processes'] for t in p['tasks']]+steps+[by['MOW-TH-003']['publication']]
 assert len({t['code'] for t in tasks})==len(tasks)
 for p in r['normal_processes']:
  assert p['tasks']
  for i,t in enumerate(p['tasks']):
   assert t['owner']==p['code'] and t['object_type']=='MOT' and t['version']==p['version'] and t['order']==i+1
   assert t['next']==(p['tasks'][i+1]['code'] if i+1<len(p['tasks']) else 'RETURN_TO_CALLER') and t['contract_ref']=='#tqt-trial-contract';resolve(d,t['instruction_ref'])
 resolve(d,by['MOW-TH-003']['publication']['instruction_ref'])
 assert r['trial_contract']['owner']=='MOW-TH-005' and r['trial_contract']['mode']=='DESIGN_TRIAL'
 f=r['work_form'];assert f['owner']=='MOW-TH-005' and f['version']==by['MOW-TH-005']['version'] and len({x['key'] for x in f['fields']})==len(f['fields'])
 assert all(x['mot'] in {st['code'] for st in steps} for x in f['fields'])
 a=r['application_preview']['record'];validate_application(a,r)
 assert hashlib.sha256(json.dumps(a,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()==r['application_preview']['record_sha256']
 return True
validate(c)
mutations=[
 lambda d:d['catalog']['records'][4]['workflow']['selection'].update(cardinality=4),
 lambda d:d['catalog']['records'][4]['workflow']['selection'].update(exclude=[]),
 lambda d:d['catalog']['instruction_owners'][0].update(process='MISSING'),
 lambda d:d['catalog']['records'][4]['workflow']['steps'][1]['binding'].update(code='MISSING'),
 lambda d:d['catalog']['records'][4]['workflow']['steps'][1]['binding'].update(version='WRONG'),
 lambda d:d['catalog']['records'][4]['workflow']['branches'].update(REJECTED='XONG'),
 lambda d:d['catalog']['records'][4]['workflow']['steps'][1].update(owner='MOW-TH-001'),
 lambda d:d['catalog']['normal_processes'][0].update(object_type='NEW_TYPE'),
 lambda d:d['catalog']['normal_processes'][0]['tasks'][0].update(owner='WRONG'),
 lambda d:d['catalog']['normal_processes'][0]['tasks'][0].update(next='RETURN_TO_CALLER'),
 lambda d:d['catalog']['normal_processes'][0]['tasks'][0].update(instruction_ref='#MISSING'),
 lambda d:d['catalog']['normal_processes'][0]['tasks'][0].update(version='WRONG'),
 lambda d:d['catalog']['trial_contract'].update(required=[]),
 lambda d:d['catalog']['records'][4]['workflow']['branches'].update(S1_OK='XONG'),
 lambda d:d['catalog']['records'][4]['workflow']['steps'][3]['binding'].update(field='selected_process.not_exists'),
 lambda d:d['catalog']['trial_contract'].update(required=[x for x in REQUIRED if x not in ['process_version','actor','reviewer']]),
 lambda d:d['catalog']['normal_processes'][-3]['tasks'][0].update(instruction_ref='does.not.exist.steps[0]'),
 lambda d:d['catalog']['normal_processes'][-3]['tasks'][0].update(instruction_ref='processes[0].supplements[code=TQT-TH-001-PG].steps[0]'),
 lambda d:d['catalog']['records'][4]['workflow']['start_gate'].update(requires=[]),
 lambda d:d['catalog']['records'][4]['workflow']['branches'].update(S2_OK='S6'),
 lambda d:d['catalog']['trial_contract']['required'].append('issue_ref')]
for f in mutations:
 d=copy.deepcopy(c);f(d)
 try:validate(d)
 except (AssertionError,KeyError,IndexError,StopIteration):pass
 else:raise AssertionError('invalid declaration accepted')
# Application tests bypass preview hash so they exercise gates, not merely hash mismatch.
appmut=[lambda a:a.update(state='DANG_LAM'),lambda a:a.update(state='XONG'),lambda a:a.update(deployed=True),lambda a:a.update(actor=''),lambda a:a.update(issue_register_ref=''),lambda a:a['selected_process'].update(code='MOW-TH-005'),lambda a:a['plan'][0].update(depends_on=['P05']),lambda a:a['release'].update(scope='PRODUCTION')]
for fn in appmut:
 a=copy.deepcopy(c['catalog']['application_preview']['record']);fn(a)
 try:validate_application(a,c['catalog'])
 except (AssertionError,KeyError):pass
 else:raise AssertionError('invalid application accepted')
# Synthetic positive path, then remove evidence at each boundary.
ready=copy.deepcopy(c['catalog']['application_preview']['record'])
ready.update(state='SAN_SANG',questions_complete=True,requirements_checked=True)
ready['start_confirmation'].update(state='CONFIRMED',evidence_ref='SIM:confirmation')
for row in ready['declarations']:row.update(result='PASS',evidence_refs=['SIM:verified'])
validate_application(ready,c['catalog'])
closed=copy.deepcopy(ready);closed.update(state='XONG',test_result='PASS')
closed['connection_tests']={'in':'PASS','out':'PASS'}
for p in closed['plan']:p.update(status='DONE',result='PASS')
closed['release'].update(state='APPROVED',decision_ref='SIM:decision',ack_ref='SIM:ack')
validate_application(closed,c['catalog'])
late=[lambda a:a['release'].update(ack_ref=None),lambda a:a['connection_tests'].update(out='FAIL'),lambda a:a['start_confirmation'].update(plan_version='OLD'),lambda a:a['plan'][1].update(status='TODO'),lambda a:a['declarations'][0].update(validity='RECHECK')]
for fn in late:
 a=copy.deepcopy(closed);fn(a)
 try:validate_application(a,c['catalog'])
 except AssertionError:pass
 else:raise AssertionError('premature completion accepted')
source_check='LOCAL_PROJECTION_ONLY'
source=Path(__file__).parent.parent/'mow-mot-moit-mout'/'UI-REVIEW-MOW001.json'
if source.exists():
 actual=json.loads(source.read_text())['application_D24'];assert actual==c['catalog']['application_preview']['record'];source_check='MATCH_EXISTING_PRODUCT_RECEIPT'
a=c['catalog']['application_preview']['record'];r=c['catalog'];answers={x['key']:x for x in a['declarations']};labels={f['key']:f['label'] for f in r['work_form']['fields']}
missing=[]
for key in r['records'][4]['workflow']['start_gate']['requires']:
 if key=='start_confirmation':
  if a['start_confirmation']['state']!='CONFIRMED':missing.append({'field':key,'need':'Xác nhận kế hoạch đúng phiên trước S3','owner':a['start_confirmation']['actor']})
 elif answers[key]['result']!='PASS' or answers[key]['validity']!='CURRENT' or not answers[key]['evidence_refs']:
  missing.append({'field':key,'need':labels[key]+' — cần kiểm và ghi căn cứ','owner':answers[key]['owner']})
candidate=copy.deepcopy(a);candidate['state']='SAN_SANG'
try:validate_application(candidate,r);can_start=True
except (AssertionError,KeyError,IndexError):can_start=False
if not can_start and not missing:missing.append({'field':'application','need':'Khai báo, bộ câu hoặc xác nhận kế hoạch chưa hợp lệ; rà phiếu theo cổng S2','owner':a['actor']})
print(json.dumps({'positive':3,'negative':len(mutations)+len(appmut)+len(late),'procedures':len(c['catalog']['records'])+len(c['catalog']['normal_processes']),'source_check':source_check,'application_state':a['state'],'can_start':can_start,'needs_before_start':missing,'next':a['next'],'production_ready':False},ensure_ascii=False))
