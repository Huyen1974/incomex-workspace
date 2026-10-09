"""Design consistency only; unresolved readiness is reported, not accepted as runtime readiness."""
import copy,json,re,sys
from pathlib import Path
s=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name('view.html')).read_text()
c=json.loads(re.search(r'<script id="tqt-composite-processes"[^>]*>(.*?)</script>',s,re.S)[1])
def validate(c):
 r=c['catalog'];allp=r['records']+r['normal_processes'];by={x['code']:x for x in allp};assert len(by)==len(allp)
 for p in allp:
  assert p['object_type']=='MOW';assert all(p['guide'].get(k) for k in ['purpose','when','avoid','done'])
 for b in r['instruction_owners']:assert b['process'] in by and ('id="'+b['anchor']+'"') in s
 for p in r['records']:
  for ref in p['child_refs']:assert ref['code'] in by and ref['version']==by[ref['code']]['version'] and ref['relation'] in ['candidate','conditional_call']
 w=by['MOW-TH-005']['workflow'];assert w['selection']['cardinality']==1 and 'MOW-TH-005' in w['selection']['exclude']
 steps=w['steps'];assert len({st['code'] for st in steps})==len(steps)
 for st in steps:
  assert st['object_type']=='MOT' and st['owner']=='MOW-TH-005' and st['version']==by['MOW-TH-005']['version']
  b=st['binding'];assert b['kind'] in ['process','external_process','selected_process','selected_contract','issue_handler']
  if b['kind'] in ['process','issue_handler']:assert b['code'] in by and b['version']==by[b['code']]['version']
  if b['kind']=='external_process':assert b['source'] and b['source_version'] and b['runtime_version'] is None
  if b['kind']=='selected_process':assert b['field']=='selected_process' and 'MOW-TH-005' in b['exclude']
 assert w['branches']['S4_PASS']=='S6' and w['branches']['S4_FAIL']=='S5' and w['branches']['S6_ACK']=='XONG'
 assert all(w['branches'][k].startswith('DỪNG') for k in ['BLOCKED','REJECTED','CANCELLED'])
 tasks=[t for p in r['normal_processes'] for t in p['tasks']]
 assert len({t['code'] for t in tasks+steps})==len(tasks)+len(steps)
 assert by['MOW-TH-005']['chainId']=='CH-001' and by['MOW-TH-005']['version']=='1.0-design'
 assert r['trial_contract']['owner']=='MOW-TH-005' and r['trial_contract']['mode']=='DESIGN_TRIAL'
 assert all(k in r['trial_contract']['required'] for k in ['application_id','target_code','target_version','recipient','return_to','acceptance'])
 for p in r['normal_processes']:
  assert p['tasks']
  for i,t in enumerate(p['tasks']):
   assert t['owner']==p['code'] and t['object_type']=='MOT' and t['version']==p['version'] and t['order']==i+1
   assert t['next']==(p['tasks'][i+1]['code'] if i+1<len(p['tasks']) else 'RETURN_TO_CALLER')
   assert t['contract_ref']=='#tqt-trial-contract'
   ref=t['instruction_ref']
   if ref.startswith('#'):assert ('id="'+ref[1:]+'"') in s
   else:
    src=p.get('steps') or next(x['steps'] for x in c['processes'][0]['supplements'] if x['id']==p['code'])
    assert ref.endswith('.steps['+str(i)+']') and i<len(src) and src[i]
 return True
validate(c)
mutations=[lambda d:d['catalog']['records'][4]['workflow']['selection'].update(cardinality=4),lambda d:d['catalog']['records'][4]['workflow']['selection'].update(exclude=[]),lambda d:d['catalog']['instruction_owners'][0].update(process='MISSING'),lambda d:d['catalog']['records'][4]['workflow']['steps'][1]['binding'].update(code='MISSING'),lambda d:d['catalog']['records'][4]['workflow']['steps'][1]['binding'].update(version='WRONG'),lambda d:d['catalog']['records'][4]['workflow']['branches'].update(REJECTED='XONG'),lambda d:d['catalog']['records'][4]['workflow']['steps'][1].update(owner='MOW-TH-001'),lambda d:d['catalog']['normal_processes'][0].update(object_type='NEW_TYPE')]
mutations += [lambda d:d['catalog']['normal_processes'][0]['tasks'][0].update(owner='WRONG'),lambda d:d['catalog']['normal_processes'][0]['tasks'][0].update(next='RETURN_TO_CALLER'),lambda d:d['catalog']['normal_processes'][0]['tasks'][0].update(instruction_ref='#MISSING'),lambda d:d['catalog']['normal_processes'][0]['tasks'][0].update(version='WRONG'),lambda d:d['catalog']['trial_contract'].update(required=[]),lambda d:d['catalog']['records'][4].update(chainId=None)]
for f in mutations:
 d=copy.deepcopy(c);f(d)
 try:validate(d)
 except AssertionError:pass
 else:raise AssertionError('invalid declaration accepted')
print(json.dumps({'positive':1,'negative':len(mutations),'procedures':len(c['catalog']['records'])+len(c['catalog']['normal_processes']),'owned_instruction_sections':len(c['catalog']['instruction_owners']),'design_MOTs':6+sum(len(p['tasks']) for p in c['catalog']['normal_processes']),'production_ready':False,'open':c['catalog']['consistency_review']['open']},ensure_ascii=False))
