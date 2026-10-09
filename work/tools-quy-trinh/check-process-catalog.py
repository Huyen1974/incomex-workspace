"""Check coded procedure references and the design checkpoint gate; no PG access."""
import copy,json,re,subprocess,sys,shutil
from pathlib import Path
args=[x for x in sys.argv[1:] if x!='--references-only']
s=Path(args[0] if args else Path(__file__).with_name('view.html')).read_text()
def block(i):return re.search(r'<script id="'+i+r'"[^>]*>([\s\S]*?)</script>',s)[1]
c=json.loads(block('tqt-composite-processes'));r=c['catalog']
def validate(c):
 r=c['catalog'];rows=r['records']+r['normal_processes']+r['resources'];by={x['code']:x for x in rows};assert len(rows)==len(by),'duplicate code'
 refs=[x for p in r['records'] for x in p['child_refs']]+[x for p in c['processes'] for st in p['stages'] for t in st['steps'] for x in t['uses']]
 for x in refs:assert x['code'] in by and by[x['code']]['version']==x['version'],'missing code/version'
 for p in r['records']:assert p['name'] and p['goal'] and p['child_refs']
 for st in ['1.4','2.3','3.2']:
  t=next(t for p in c['processes'] for z in p['stages'] for t in z['steps'] if t['id']==st);assert any(x['code']=='MOW-TH-002' for x in t['uses'])
 return len(refs)
n=validate(c)
for field,value in [('code','MISSING'),('version','wrong')]:
 bad=copy.deepcopy(c);bad['catalog']['records'][0]['child_refs'][0][field]=value
 try:validate(bad)
 except AssertionError:pass
 else:raise AssertionError('accepted broken reference')
if '--references-only' in sys.argv:
 print(json.dumps({'aggregate':len(r['records']),'normal':len(r['normal_processes']),'coded_references':n,'bad_reference_cases':2,'checkpoint_cases':'NOT_RUN: references-only','scope':'DESIGN_ONLY'}));sys.exit(0)
if not shutil.which('node'):sys.exit('Node.js required for checkpoint tests; use --references-only for reference validation only.')
js=block('tqt-checkpoint-rule')+'\nconst f=module.exports.tqtCheckpoint,p='+json.dumps(c['checkpoint_policy'])+''';
const assert=require('assert');let n=0;const plan={scope:'A',version:'1',required:['Q1']},e={id:'Q1',scope:'A',version:'1',context:'DESIGN',current:true,result:'PASS',level:3,validity:'CURRENT',evidence:'EV1'};
const t=(st,pl,ev,fa,w)=>{assert.equal(f(p,st,pl,ev,fa).status,w);n++};
t('G1',plan,[e],{},'DAT');t('G1',{...plan,required:[]},[],{},'CHUA');for(const z of [{scope:'B'},{version:'2'},{level:2},{result:'FAIL'},{result:'BLOCKED'},{result:'NOT_TESTED'},{validity:'STALE'},{evidence:''},{result:'NA'}])t('G1',plan,[{...e,...z}],{},'CHUA');t('G1',plan,[{...e,result:'NA',reason:'N/A',approved_by:'Host'}],{},'DAT');t('G1',plan,[e,e],{},'CHUA');let tech={...e,level:4,context:'TECHNICAL'},facts={real_environment:true,restore_pass:true,recipient_ready:true};t('G2',plan,[tech],facts,'DAT');t('G3',plan,[tech],facts,'CHUA');const op={...tech,context:'OPERATIONS'},of={observation_met:true,logs_reviewed:true,feedback_reviewed:true,handoff_ack:true};t('G3',plan,[op],of,'DAT');for(const k of Object.keys(of))t('G3',plan,[op],{...of,[k]:false},'CHUA');console.log('checkpoint cases',n);
'''
subprocess.run(['node','-e',js],check=True)
print(json.dumps({'aggregate':len(r['records']),'normal':len(r['normal_processes']),'coded_references':n,'bad_reference_cases':2,'scope':'DESIGN_ONLY'}))
