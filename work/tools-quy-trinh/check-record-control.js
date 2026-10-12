/* Tests the same design projection as Overview. No PostgreSQL writes. */
const fs=require('fs'),vm=require('vm'),assert=require('assert');
// Heavy real-packet readers run before the parent loads its full catalog.
let realTransitionPreflight=null;
if(!process.argv.slice(2).some(x=>x.startsWith('--'))){runPreparationReaderCases();realTransitionPreflight=runRealTransitionPreflight();}
// The lock launcher needs no application/catalog. Acquire the OS lock before
// starting the TEST receiver so an idle launcher never duplicates the full source.
// Kernel flock survives filename persistence and is released on process death. Never unlink it.
if(process.argv.includes('--test-handoff')&&process.argv[process.argv.indexOf('--test-handoff')+1]==='consume'&&!process.argv.includes('--held-lock')){
 const code=`import os,sys,fcntl,json
f=open(sys.argv[1],'a+')
try: fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
except BlockingIOError:
 print(json.dumps({'state':'BLOCKED','error':'CONCURRENT_WRITE','issue_master':'CAT-069?','owner':'TEST','return_to':'P01'}));sys.exit(0)
os.set_inheritable(f.fileno(),True)
os.execv(sys.argv[2],sys.argv[2:])`;
 const dir=process.argv[process.argv.indexOf('--test-handoff')+2],x=require('child_process').spawnSync('python3',['-c',code,require('path').join(dir,'receive.lock'),process.execPath,...process.execArgv,__filename,...process.argv.slice(2),'--held-lock'],{encoding:'utf8',maxBuffer:2e6});
 if(x.stdout)process.stdout.write(x.stdout);if(x.stderr)process.stderr.write(x.stderr);process.exit(x.status===null?1:x.status);
}
const testMode=['--test-handoff','--test-design'].find(flag=>process.argv.includes(flag));
let testContext=null;
if(testMode){
 const allowed=new Set([testMode,'--held-lock']);assert(process.argv.slice(2).filter(x=>x.startsWith('--')).every(x=>allowed.has(x)),'TEST_MODE_FLAGS');
 const path=require('path'),dir=process.argv[process.argv.indexOf(testMode)+2],file=path.join(dir,'test-context.json');
 if(fs.existsSync(file)){
  const context=JSON.parse(fs.readFileSync(file,'utf8')),policy=JSON.parse(fs.readFileSync(path.join(dir,'policy.json'),'utf8'));
  assert.equal(context.environment,'ISOLATED_TEST');assert.equal(policy.environment,'TEST');assert.equal(context.schema,'TQT-HANDOFF-TEST-CONTEXT/1');
  const engine=fs.readFileSync(path.join(dir,'test-engine.js'),'utf8');assert.equal(require('crypto').createHash('sha256').update(engine).digest('hex'),context.engine_sha256,'TEST_ENGINE_HASH');
  testContext={catalog:context.catalog,engine};
 }
}
let html=testContext?null:fs.readFileSync(process.argv[2]||__dirname+'/view.html','utf8');
const script=id=>{const m=html.match(new RegExp('<script id="'+id+'"[^>]*>([\\s\\S]*?)</script>'));assert(m,id);return m[1];};
const engineSource=testContext?testContext.engine:Buffer.from(script('tqt-record-control'),'utf8').toString('utf8');
// The audit catalog arrives intact on stdin. Do not parse another full copy from HTML.
const auditMode=process.argv.includes('--audit');
if(auditMode){html=null;/release/.test('release');}
const R=testContext?testContext.catalog:auditMode?JSON.parse(fs.readFileSync(0,'utf8')):JSON.parse(script('tqt-composite-processes')).catalog;
const persistedApplicationSHA=require('crypto').createHash('sha256').update(JSON.stringify(R.application_preview.record)).digest('hex');
vm.runInThisContext(engineSource);
// Reuse CHECK004 for lossless storage conversion; never write source in place.
if(process.argv.includes('--compact-history')||process.argv.includes('--expand-history')){
 const path=require('path'),crypto=require('crypto'),mode=process.argv.includes('--compact-history')?'--compact-history':'--expand-history',at=process.argv.indexOf(mode),file=path.resolve(process.argv[at+1]||'');html=null;R.application_preview.record=null;/release/.test('release');
 const raw=fs.readFileSync(file),doc=JSON.parse(raw),before=doc.application_D24;if(!before?.application_id)throw Error('APPLICATION_REQUIRED');
 const original=tqtExpandApplication(before);doc.application_D24=mode==='--compact-history'?tqtPackApplication(before):tqtExpandApplication(before);const restored=tqtExpandApplication(doc.application_D24);if(!require('util').isDeepStrictEqual(original,restored))throw Error('HISTORY_ROUNDTRIP_MISMATCH');
 const bytes=Buffer.from(JSON.stringify(doc,null,2)+'\n'),outIndex=process.argv.indexOf('--output'),execute=process.argv.includes('--execute');
 if(execute){if(outIndex<0)throw Error('OUTPUT_REQUIRED');const output=path.resolve(process.argv[outIndex+1]);if(output===file)throw Error('NO_IN_PLACE_WRITE');fs.writeFileSync(output,bytes,{flag:'wx',mode:0o600});}else if(outIndex>=0)throw Error('EXECUTE_REQUIRED');
 console.log(JSON.stringify({state:execute?'CANDIDATE_WRITTEN':'DRY_RUN',mode,input_sha256:crypto.createHash('sha256').update(raw).digest('hex'),output_sha256:crypto.createHash('sha256').update(bytes).digest('hex'),input_bytes:raw.length,output_bytes:bytes.length,logical_equality:'ALL_FIELDS_EXACT',roundtrip:'EXACT',history_events:before.history.length,checkpoint_revisions:before.checkpoint_checks.length,nodes:Object.keys(doc.application_D24.history_store?.nodes||{}).length,pg:'NOT_RUN',note:'Candidate only. Submit via existing guarded transaction; rollback with --expand-history, same exact logical evidence.'}));return;
}
// Existing validators/readers receive the same full logical evidence, shared immutable past blocks.
R.application_preview.record=tqtExpandApplication(R.application_preview.record);

// P36: CLI verifies the same server signature before caching public read evidence.
function loadServerReceipt(r){const a=r.application_preview.record,p=r.server_trust_policy,s=a.server_receipt;if(!s)return false;const c=require('crypto');if(!p||s.algorithm!=='Ed25519'||s.key_id!==p.policy_id)throw Error('SERVER_RECEIPT_KEY');const key=c.createPublicKey({key:Buffer.concat([Buffer.from('302a300506032b6570032100','hex'),Buffer.from(p.public_key_base64,'base64')]),format:'der',type:'spki'});if(!c.verify(null,Buffer.from(s.payload),key,Buffer.from(s.signature,'base64')))throw Error('SERVER_RECEIPT_SIGNATURE');globalThis.tqtRegisterServerTrust(r,JSON.parse(s.payload));return true;}
if(process.argv.includes('--server-context')){try{const input=JSON.parse(fs.readFileSync(0,'utf8'));console.log(JSON.stringify({state:'PASS',context:globalThis.tqtServerContext(R,input)}));}catch(e){console.log(JSON.stringify({state:'FAIL',errors:[e.message]}));process.exitCode=1;}return;}
if(!process.argv.includes('--write-gate'))loadServerReceipt(R);
function runHistoryCases(){
 const base=R.application_preview.record,packed=tqtPackApplication(base),copy=x=>JSON.parse(JSON.stringify(x));let count=0;
 const equal=(a,b)=>assert(require('util').isDeepStrictEqual(a,b));equal(tqtExpandApplication(packed),base);count++;
 equal(tqtPackApplication(packed),packed);count++;
 assert.equal(tqtValidateTransition(base,packed).state,'PASS');count++;assert.equal(tqtValidateTransition(packed,base).state,'PASS');count++;
 const actual=tqtRecordAudit(R),packedAudit=tqtRecordAudit({...R,application_preview:{...R.application_preview,record:packed}});equal(packedAudit.verifiedCheckpoints,actual.verifiedCheckpoints);equal(packedAudit.counts,actual.counts);assert.equal(packedAudit.canFinish,actual.canFinish);count++;
 for(const mutate of [
  x=>delete x.history_store,
  x=>x.history_store.format='UNKNOWN',
  x=>delete x.history_store.nodes[Object.keys(x.history_store.nodes)[0]],
  x=>x.history_store.nodes[Object.keys(x.history_store.nodes)[0]]=['v','changed'],
  x=>x.history[2].previous_evidence.$history='0'.repeat(64),
  x=>x.history_store.nodes[tqtSHA256(JSON.stringify(['v','orphan']))]=['v','orphan'],
  x=>x.checkpoint_checks[0].dependency_key={$history:'0'.repeat(64)}
 ]){const x=copy(packed);mutate(x);assert.throws(()=>tqtExpandApplication(x));assert.equal(tqtValidateTransition(packed,x).state,'FAIL');assert.equal(tqtRecordAudit({...R,application_preview:{...R.application_preview,record:x}}).canFinish,false);count++;}
 // Re-hashing forged content does not authorize rewriting history.
 const forged=copy(packed);forged.history[0].actor='FORGED';assert(tqtValidateTransition(packed,forged).errors.includes('EXECUTION_HISTORY_REWRITTEN'));count++;
 const dropped={...base,history:base.history.slice(0,-1)};assert.equal(tqtValidateTransition(packed,tqtPackApplication(dropped)).state,'FAIL');count++;
 const altered={...base,checkpoint_checks:base.checkpoint_checks.map((x,i)=>i?x:{...x,dependency_key:x.dependency_key+'forged'})};assert.equal(tqtValidateTransition(packed,tqtPackApplication(altered)).state,'FAIL');count++;
 const stripped={...base,current_checkpoint:'CP01'};assert(tqtValidateTransition(packed,stripped).errors.includes('HISTORY_PACK_REQUIRED'));count++;
 const special={application_id:'TEST',history:[{previous_evidence:JSON.parse('{"__proto__":{"polluted":true},"x":"Tiếng Việt"}')}],checkpoint_checks:[]};equal(tqtExpandApplication(tqtPackApplication(special)),special);assert.equal({}.polluted,undefined);count++;
 return {state:'PASS',cases:count,history_events:base.history.length,checkpoint_revisions:base.checkpoint_checks.length,logical_equality:'ALL_FIELDS_EXACT',verified_checkpoints:actual.verifiedCheckpoints,compact_bytes:Buffer.byteLength(JSON.stringify(packed)),pg:'NOT_RUN'};
}
if(process.argv.includes('--check-history')){console.log(JSON.stringify(runHistoryCases()));return;}

const testTrust={endpoint_receipts:[],principals:[]};
const audit=r=>globalThis.tqtRecordAudit(r,r===R?undefined:testTrust),clone=x=>JSON.parse(JSON.stringify(x));let tests=0;
if(!process.argv.slice(2).some(x=>x.startsWith('--')))console.log('P38 history storage: '+JSON.stringify(runHistoryCases()));
function designFixture(r,result){const a=r.application_preview.record,p=r.work_master_designs.records.find(x=>x.code==='CAT-206*').validation.profiles[0];return {application_id:a.application_id,target_version:a.target_version,scope:a.scope,plan_id:result.plan_id,output_version:result.output_version,contract_binding:globalThis.tqtContractPin(a),mots:Object.entries(p.mots).map(([code,x])=>({code,fields:clone(x.fields.filter(f=>f.contract_role==='PRODUCT_SPEC')),controls:x.design_requirements.controls,states:x.design_requirements.states,branches:x.design_requirements.branches,rule_refs:[p.rule_source.ref+'@'+p.rule_source.version],open_items:[]}))};}
// Isolated TEST protocol only. The receiver is a separate process and opens the persisted packet itself.
function sliceCommand(){
 const path=require('path'),crypto=require('crypto'),dir=process.argv[process.argv.indexOf('--test-handoff')+2],mode=process.argv[process.argv.indexOf('--test-handoff')+1],a=R.application_preview.record;
 const file=n=>path.join(dir,n),digest=x=>crypto.createHash('sha256').update(x).digest('hex'),json=n=>JSON.parse(fs.readFileSync(file(n),'utf8'));
 if(!fs.statSync(dir).isDirectory()||json('policy.json').environment!=='TEST')throw Error('TEST_DIRECTORY_REQUIRED');
 if(mode==='produce'){
  const result={id:'TEST-P01',application_id:a.application_id,target_version:a.target_version,plan_id:'P01',contract_binding:globalThis.tqtContractPin(a),output_ref:'test-only:prepared-answers',output_version:'1',evidence_ref:'test-only:file-readback',actor:a.actor,at:new Date().toISOString(),scope:a.scope,data:{answers:a.declarations.map(d=>({key:d.key,answer:d.answer})),source_refs:a.input_refs}};
  const validation=globalThis.tqtPayloadAudit(R,'P01',result);if(validation.state!=='PASS')throw Error(validation.errors.join(','));const packet=JSON.stringify({environment:'TEST',recipient_plan_id:'P02',payload:result});fs.writeFileSync(file('packet.json'),packet,{flag:'wx'});return {state:'WRITTEN',sha256:digest(packet)};
 }
 if(!process.argv.includes('--held-lock'))throw Error('OS_LOCK_REQUIRED');
 if(process.env.TQT_TEST_KILL_AFTER_LOCK==='1')process.kill(process.pid,'SIGKILL');
 {
  const persist=next=>{const fd=fs.openSync(file('state.next.json'),'w',0o600);try{fs.writeFileSync(fd,JSON.stringify(next));fs.fsyncSync(fd);}finally{fs.closeSync(fd);}fs.renameSync(file('state.next.json'),file('state.json'));const dd=fs.openSync(dir,'r');try{fs.fsyncSync(dd);}finally{fs.closeSync(dd);}};
  const repair=state=>{const old=fs.existsSync(file('events.jsonl'))?fs.readFileSync(file('events.jsonl'),'utf8').trim().split('\n').filter(Boolean).map(JSON.parse):[];for(const event of state.events||[])if(!old.some(x=>x.event_id===event.event_id)){fs.appendFileSync(file('events.jsonl'),JSON.stringify(event)+'\n');}const fd=fs.openSync(file('events.jsonl'),'a');try{fs.fsyncSync(fd);}finally{fs.closeSync(fd);}};
  const policy=json('policy.json'),state=json('state.json'),bytes=fs.readFileSync(file('packet.json'),'utf8'),packet=JSON.parse(bytes),p=packet.payload,hash=digest(bytes);
  const reject=error=>{const result={state:'BLOCKED',error,issue_master:'CAT-069?',owner:a.actor,return_to:'P01'};fs.appendFileSync(file('events.jsonl'),JSON.stringify(result)+'\n');return result;};
  if(policy.receiver!=='P02'||packet.recipient_plan_id!=='P02'||packet.environment!=='TEST')return reject('WRONG_RECIPIENT');
  if(!policy.read_allowed)return reject('READ_FORBIDDEN');
  if(!policy.write_allowed)return reject('WRITE_FORBIDDEN');
  if(state.cancelled)return reject('CANCELLED');
  if(p.output_version!==policy.expected_output_version)return reject('STALE_OUTPUT');
  const result=globalThis.tqtPayloadAudit(R,'P01',p);if(result.state!=='PASS')return reject(result.errors.join(','));
  if(state.received){if(state.received.sha256!==hash)return reject('DUPLICATE_KEY_DIFFERENT_CONTENT');repair(state);return {state:'ACK',replayed:true,receipt_id:state.received.id,effect_count:state.effects.length};}
  if(state.revision!==policy.expected_state_revision)return reject('CONCURRENT_REVISION');
  const h=a.information_contract.handoffs.find(h=>h.plan_id==='P02'),received=Object.fromEntries(h.input_fields.map(k=>[k,p[h.mapping[k]]]));
  if(received.data.answers.length!==a.declarations.length||received.data.answers.some((x,i)=>x.key!==a.declarations[i].key||x.answer!==a.declarations[i].answer)||JSON.stringify(received.data.source_refs)!==JSON.stringify(a.input_refs))return reject('PREPARED_DATA_MISMATCH');
  const receipt={id:'TEST-RECEIPT-P01-P02',sha256:hash,plan_id:'P02',used_scope:received.scope,answer_keys:received.data.answers.map(x=>x.key)};
  const next={...state,revision:state.revision+1,received:receipt,effects:[...state.effects,{id:'TEST-EFFECT-P02',input_sha256:hash}],events:[...(state.events||[]),{event_id:receipt.id+':'+hash,state:'RECEIVED',receipt_id:receipt.id}]};persist(next);
  if(process.env.TQT_TEST_LOG_FAILURE==='1')throw Error('INJECTED_EVENT_LOG_FAILURE');
  repair(next);
  if(policy.drop_ack_once)return {state:'ACK_LOST',effect_count:next.effects.length};
  return {state:'ACK',replayed:false,receipt_id:receipt.id,effect_count:next.effects.length,sha256:hash,used_scope:received.scope,answer_count:received.data.answers.length};
 }
}
if(process.argv.includes('--test-handoff')){try{console.log(JSON.stringify(sliceCommand()));}catch(e){console.log(JSON.stringify({state:'BLOCKED',error:e.message}));process.exitCode=1;}return;}

// Same CAT-206 validator: producer stores designs, receiver opens their bound bytes.
function designCommand(){
 const path=require('path'),dir=fs.realpathSync(process.argv[process.argv.indexOf('--test-design')+2]),mode=process.argv[process.argv.indexOf('--test-design')+1],a=R.application_preview.record;
 const read=n=>JSON.parse(fs.readFileSync(path.join(dir,n),'utf8')),write=(n,x)=>fs.writeFileSync(path.join(dir,n),JSON.stringify(x)),policy=read('policy.json');
 if(policy.environment!=='TEST')throw Error('TEST_DIRECTORY_REQUIRED');
 if(mode==='produce'){
  if(!read('state.json').received)throw Error('P01_NOT_RECEIVED');
  const outputs=['P02','P03'].map(plan_id=>{const result={id:'TEST-'+plan_id,application_id:a.application_id,target_version:a.target_version,plan_id,contract_binding:globalThis.tqtContractPin(a),output_ref:'test-only:design-'+plan_id,output_version:'1',evidence_ref:'test-only:design-readback',actor:a.plan.find(x=>x.id===plan_id).actor,at:new Date().toISOString(),scope:a.scope};const artifact=designFixture(R,result),name=plan_id+'.json';write(name,artifact);result.artifact={path:name,sha256:globalThis.tqtSHA256(globalThis.tqtCanonical(artifact))};return result;});
  write('design-packet.json',{environment:'TEST',recipient:'P04',outputs});return {state:'WRITTEN',count:outputs.length};
 }
 const packet=read('design-packet.json');if(packet.environment!=='TEST'||packet.recipient!=='P04'||packet.outputs.length!==2)throw Error('DESIGN_WRONG_RECIPIENT');
 const reads=[];
 for(const plan of ['P02','P03']){const xs=packet.outputs.filter(x=>x.plan_id===plan);if(xs.length!==1)throw Error('DESIGN_OUTPUT_COVERAGE');const result=xs[0],check=globalThis.tqtPayloadAudit(R,plan,result);if(check.state!=='PASS')throw Error(check.errors.join(','));
  const target=path.resolve(dir,result.artifact.path);if(!target.startsWith(dir+path.sep)||fs.realpathSync(target)!==target)throw Error('ARTIFACT_OUTSIDE_STORE');
  const artifact=JSON.parse(fs.readFileSync(target,'utf8')),audit=globalThis.tqtDesignAudit(R,result,artifact);if(audit.state!=='PASS')throw Error(audit.errors.join(','));reads.push({plan_id:plan,sha256:audit.sha256,output_version:result.output_version});}
 write('P04-receipt.json',{environment:'TEST',state:'READ_AND_CHECKED',reads});return {state:'ACK',reads};
}
if(process.argv.includes('--test-design')){try{console.log(JSON.stringify(designCommand()));}catch(e){console.log(JSON.stringify({state:'BLOCKED',error:e.message}));}return;}


// P36: real receiver opens designs in the existing protected document, never a TEST fixture.
if(process.argv.includes('--read-designs')){html=null;/release/.test('release');R.application_preview.record=null;const raw=fs.readFileSync(process.argv[process.argv.indexOf('--read-designs')+1]),P=JSON.parse(raw),a=tqtExpandApplication(P.application_D24);R.application_preview.record=a;loadServerReceipt(R);const reads=[];for(const plan of ['P02','P03']){const rows=a.plan_results.filter(x=>x.plan_id===plan);if(rows.length!==1)throw Error('DESIGN_OUTPUT_COVERAGE');const result=rows[0],prefix=R.application_preview.source_ref+'/design_artifacts/';if(result.artifact?.path!==prefix+plan)throw Error('DESIGN_ARTIFACT_POINTER');const handoff=tqtPayloadAudit(R,plan,result),artifact=a.design_artifacts?.[plan],check=tqtDesignAudit(R,result,artifact);if(handoff.state!=='PASS'||check.state!=='PASS')throw Error(JSON.stringify({handoff,check}));reads.push({plan_id:plan,artifact_ref:result.artifact.path,sha256:check.sha256,output_version:result.output_version,mots:artifact.mots.map(x=>({code:x.code,fields:x.fields.length,controls:x.controls,states:x.states,branches:x.branches,open_items:x.open_items})),design_scope:artifact.design_scope||null});}console.log(JSON.stringify({state:'READ_AND_CHECKED',environment:'REAL_DESIGN_READBACK',application_id:a.application_id,target_version:a.target_version,source_sha256:require('crypto').createHash('sha256').update(raw).digest('hex'),reads,product_acceptance:false,pg:'NOT_RUN'}));return;}

// P36: reusable UI model checks with the same logical product contract. No UI/network/PG writes.
if(process.argv.includes('--check-g1-ui')){
 const path=require('path'),crypto=require('crypto'),dir=path.resolve(process.argv[process.argv.indexOf('--check-g1-ui')+1]||''),files=['field-flow-model-v1.js','field-flow-v1.js','mow-ui-walkthrough-v1.js'];
 const sources=files.map(name=>{const p=path.join(dir,name);if(fs.realpathSync(p)!==p||!fs.statSync(p).isFile())throw Error('UI_SOURCE_NOT_REGULAR');const bytes=fs.readFileSync(p);return {name,path:p,sha256:crypto.createHash('sha256').update(bytes).digest('hex'),bytes:bytes.length,text:bytes.toString('utf8')};});
 const cases=[],test=(id,expected,fn)=>{try{const actual=fn();cases.push({id,state:'PASS',expected,actual:actual===undefined?'Assertions matched':actual});}catch(e){cases.push({id,state:'FAIL',expected,actual:e.message});}},json=x=>JSON.parse(JSON.stringify(x));
 for(const file of sources)new vm.Script(file.text,{filename:file.name});
 const sandbox={module:{exports:{}},console:{log(){}}};vm.runInNewContext(sources[0].text,sandbox,{timeout:3000,filename:sources[0].name});const F=sandbox.module.exports;
 const rows=[{id:'EXAMPLE-1',name:'Field 1',type:'FIELD',detail:'text',path:'demo'},{id:'EXAMPLE-2',name:'Field 2',type:'FIELD',detail:'text',path:'demo'}];
 const bind=(mode='example')=>F.bind(F.create(mode),{requestId:'CHECK004-G1-UI',caller:{id:'UI-CHECK-CALLER',return_to:'same-page',target_version:F.VERSION},scope:{sources:['ML-DEF-008'],permission_context:{mode}}});
 const make=(mode='example')=>F.change(bind(mode),{query:'Field',description:'G1 design check'});let good;
 const contract=(state,packet)=>{const a=tqtProductOutputAudit(R,json(packet),json(F.request(state)),json(state.evaluationContext));assert.equal(a.state,'PASS',a.errors.join(','));};
 for(const [scenario,expected] of [['found','found'],['not_found','not_found'],['incomplete','incomplete'],['unconfigured','incomplete'],['empty','not_found'],['error','incomplete'],['forbidden','incomplete']])test('CONCLUSION_'+scenario,expected,()=>{let state={...make(),scenario};const x=F.exampleResponse(state,rows);state=F.receive(state,x.response,x.context);const packet=F.packet(state);assert.equal(packet.conclusion,expected);assert.equal(F.validateReturn(state,packet).length,0);contract(state,packet);if(scenario==='found'){assert.equal(packet.candidates.length,2);good=state;}return {conclusion:packet.conclusion,candidates:packet.candidates.length,mode:packet.mode};});
 test('INVALID_FINAL_DATA','Reject nulls/bad timestamp',()=>{const packet=F.packet(good);packet.generatedAt='tomorrow';assert(F.validateReturn(good,packet).length);packet.generatedAt=null;assert(F.validateReturn(good,packet).length);});
 test('WRONG_CALLER','Reject other recipient',()=>{const packet=F.packet(good);packet.return_to.caller.id='other';assert(F.validateReturn(good,packet).includes('WRONG_RECIPIENT'));});
 test('STALE_CANDIDATE','Reject previous revision inside candidate',()=>{const packet=F.packet(good);packet.candidates[0].evaluation.requestRevision--;assert(F.validateReturn(good,packet).length);});
 test('STALE_AGGREGATE','Reject previous rule in total evaluation',()=>{const packet=F.packet(good);packet.evaluation.ruleVersion='old';assert(F.validateReturn(good,packet).length);});
 test('CHANGED_INPUT','Invalidate result/evaluation/receipt',()=>{const state=F.change(F.confirm(good),{query:'new'});assert.equal(state.revision,good.revision+1);for(const k of ['response','receipt','evaluationContext'])assert.equal(state[k],null);});
 test('CLEAR_MONOTONIC_REVISION','Do not reset revision to an old value',()=>{const state=F.change(good,{query:'',description:''});assert(state.revision>good.revision);assert(!F.valid(state));});
 test('NO_SELECTION_REQUIREMENT','Return complete suitable set without checkbox',()=>{assert.equal(good.selected,null);assert(F.canConfirm(good));assert.equal(F.confirm(good).receipt.candidates.length,2);});
 test('EXACT_ACK_AND_IDEMPOTENT_RETURN','Same packet retained; forged ACK ignored',()=>{const a=F.confirm(good),b=F.confirm(a);assert.equal(F.canonical(a.receipt),F.canonical(b.receipt));assert.equal(F.acknowledge(a,{requestId:a.requestId,revision:a.revision,caller:a.caller,packet_token:'wrong'}).ack,null);assert(F.acknowledge(a,{requestId:a.requestId,revision:a.revision,caller:a.caller,packet_token:F.canonical(a.receipt)}).ack);});
 test('LIVE_CANCEL_AND_LATE_RESULT','Cancellation preserves caller and rejects late response',()=>{const state=F.cancel(make('live')),packet=F.packet(state);assert.equal(packet.conclusion,'cancelled');contract(state,packet);assert.equal(F.receive(state,{},{}),state);});
 test('NO_LIVE_EXAMPLE_PROOF','Live cannot make example data or successful result without adapter',()=>{const state=make('live');assert.throws(()=>F.exampleResponse(state,rows),/EXAMPLE_ONLY/);assert.equal(F.packet(state),null);assert(!F.canConfirm(state));});
 test('MALFORMED_CANDIDATES','Invalid object rejected without crashing',()=>{const state=make(),x=F.exampleResponse(state,[]);x.response.candidates={bad:true};assert(F.responseErrors(state,x.response,x.context).includes('INVALID_RESPONSE_FIELDS'));});
 test('DESCRIPTION_ONLY','Description is valid intent; live remains unconnected',()=>{const state=F.change(bind('live'),{description:'Field đầu vào MOIT'});assert(F.valid(state));assert.equal(tqtProductInputAudit(R,'1.1',json(F.request(state))).state,'PASS');assert.equal(F.packet(state),null);});
 test('EMPTY_FILTERS','Empty object/blank strings are not intent; meaningful filter is',()=>{let state=bind();assert(!F.valid(state));assert.equal(tqtProductInputAudit(R,'1.1',json(F.request(state))).state,'FAIL');state=F.change(state,{state:'   ',branch:'',specific:''});assert(!F.valid(state));state=F.change(state,{state:'ACTIVE'});assert(F.valid(state));assert.equal(tqtProductInputAudit(R,'1.1',json(F.request(state))).state,'PASS');});
 test('CANCEL_BEFORE_INPUT','No query needed for identified cancellation',()=>{const state=F.cancel(bind('live')),packet=F.packet(state);assert.equal(packet.conclusion,'cancelled');contract(state,packet);});
 for(const mot of ['1.1','1.2'])test('CANCEL_CANNOT_BYPASS_INTENT_'+mot,'Reject cancellation outside interface',()=>{const request=json(F.request(bind()));request.cancellation={requestId:request.requestId,revision:request.revision,caller:request.caller,scope:request.scope,target_version:request.caller.target_version};const result=tqtProductInputAudit(R,mot,request);assert.equal(result.state,'FAIL');assert(result.errors.includes('CANCELLATION_OUTSIDE_INTERFACE'));});
 test('SOURCE_READ_ONLY','All three source hashes unchanged after checks',()=>{for(const file of sources)assert.equal(crypto.createHash('sha256').update(fs.readFileSync(file.path)).digest('hex'),file.sha256);return sources.map(({name,sha256})=>({name,sha256}));});
 const failures=cases.filter(x=>x.state!=='PASS'),target=R.application_preview.record.target_version,wrapper=sources.find(x=>x.name==='mow-ui-walkthrough-v1.js');
 console.log(JSON.stringify({schema:'TQT-CHECK-004/G1-UI-1',state:failures.length?'FAIL':'PASS',environment:'ISOLATED_MODEL_CHECK',application_id:R.application_preview.record.application_id,contract_binding:{id:R.application_preview.record.information_contract.id,version:R.application_preview.record.information_contract.version},target_version:target,target_hash_matches:target.endsWith('@'+wrapper.sha256),build_version:F.VERSION,sources:sources.map(({name,sha256,bytes})=>({name,sha256,bytes})),cases,total:cases.length,passed:cases.length-failures.length,failed:failures.length,source_integrity:'UNCHANGED_DURING_CHECK',browser_verification:'NOT_PERFORMED',product_acceptance:false,mow001_checkpoint_change:false,pg:'NOT_RUN'}));if(failures.length)process.exitCode=1;return;
}

// Read a persisted preparation packet using the same contracts; never manufactures answers or acceptance.
if(process.argv.includes('--read-preparation')){const crypto=require('crypto'),q=JSON.parse(script('tqt-question-matrix'));html=null;/release/.test('release');R.application_preview.record=null;const raw=fs.readFileSync(process.argv[process.argv.indexOf('--read-preparation')+1]),P=JSON.parse(raw),a=tqtExpandApplication(P.application_D24);R.application_preview.record=a;if(a.target_code!=='MOW-NHC-001'||a.scope_stage!=='G1')throw Error('UNSUPPORTED_PREPARATION_SCOPE');const groups=new Set(['STEP','CHILD','LAYER','CHAIN','B1','B1.1','B1.2','B1.3','FIELD','CTCM','UI','TEST','CONFIG']),needed=q.questions.filter(x=>groups.has(x.owner)).map(x=>x.id),answers=a.preparation_review.answers;const missing=needed.filter(id=>answers.filter(x=>x.question_id===id).length!==1);const refs=answers.map(x=>x.answer_ref?P.process_trial_20261009.answers[Number(x.answer_ref.split('/').pop())]:x);if(answers.length!==needed.length||missing.length||answers.some((x,i)=>x.answer_ref&&(x.answer_ref!=='work/mow-mot-moit-mout/UI-REVIEW-MOW001.json#/process_trial_20261009/answers/'+Number(x.answer_ref.split('/').pop())||refs[i]?.question_id!==x.question_id))||refs.some(x=>!x||(!x.answer&&!x.answers?.every(y=>y.answer)))||tqtSHA256(tqtCanonical(q))!==a.preparation_review.question_matrix_sha256)throw Error('PREPARATION_ANSWERS_INCOMPLETE');const result=a.plan_results.find(x=>x.plan_id==='P01'),check=tqtPayloadAudit(R,'P01',result);if(check.state!=='PASS')throw Error(JSON.stringify(check));const records=a.trial_records.filter(x=>['PLAN','COVERAGE'].includes(x.requirement_code));if(records.length!==2||new Set(records.map(x=>x.requirement_code)).size!==2)throw Error('PREPARATION_RECORD_SET');for(const x of records){if(x.application_id!==a.application_id||x.payload.source_ref!==R.application_preview.source_ref+'/'+(x.requirement_code==='PLAN'?'plan':'preparation_review'))throw Error('PREPARATION_RECORD_SOURCE');preparationSnapshot(a,x);}console.log(JSON.stringify({environment:'PREPARATION_READBACK',state:'READ_AND_VALIDATED',application_id:a.application_id,target_version:a.target_version,source_sha256:crypto.createHash('sha256').update(raw).digest('hex'),P01_sha256:tqtSHA256(tqtCanonical(result)),declarations:a.declarations.length,required_questions:needed.length,answered:answers.length,inherited:answers.filter(x=>x.answer_ref).length,added:answers.filter(x=>x.answer).length,missing,record_refs:records.map(x=>x.id),snapshot_checks:records.map(x=>({requirement_code:x.requirement_code,...preparationSnapshot(a,x)})),handoff:check,reader:'read-only preparation input for P02; execution provenance comes from caller receipt',product_acceptance:false,pg:'NOT_RUN'}));process.exit(0);}
// Called by the authenticated gateway before committing. stdin is captured under its root lock.
if(process.argv.includes('--write-gate')){
 try{const {before,after,trusted_context}=JSON.parse(fs.readFileSync(0,'utf8')),a=tqtExpandApplication(after.application_D24),transition=globalThis.tqtValidateTransition(before.application_D24,after.application_D24),r=clone(R);r.application_preview.record=a;const audit=globalThis.tqtRecordAudit(r,trusted_context),errors=[...transition.errors,...audit.errors];
  const schemas=R.work_master_designs.records.find(x=>x.code==='CAT-206*').validation.schemas;
  for(const d of a.declarations||[])errors.push(...globalThis.tqtSchemaErrors(schemas,'declaration',d));
  for(const result of a.plan_results||[])errors.push(...globalThis.tqtPayloadAudit(r,result.plan_id,result).errors);
  for(const row of a.trial_records||[])errors.push(...globalThis.tqtSchemaErrors(schemas,'trial_record',row));
  const latestChecks=new Map();for(const c of a.checkpoint_checks||[])if(!latestChecks.has(c.checkpoint)||c.revision>latestChecks.get(c.checkpoint).revision)latestChecks.set(c.checkpoint,c);for(const c of latestChecks.values())if(c.result==='PASS'&&c.validity==='CURRENT'&&!audit.verifiedCheckpoints.includes(c.checkpoint))errors.push('UNPROVED_CHECKPOINT:'+c.checkpoint);
  const out={state:errors.length?'FAIL':'PASS',errors,verified_checkpoints:audit.verifiedCheckpoints};console.log(JSON.stringify(out));process.exit(errors.length?1:0);
 }catch(e){console.log(JSON.stringify({state:'FAIL',errors:[e.message]}));process.exit(1);}
}

if(process.argv.includes('--complete-fixture')){fs.writeFileSync(1,JSON.stringify(fixture()));process.exit(0);}
if(process.argv.includes('--audit')){const r=R;loadServerReceipt(r);const a=globalThis.tqtRecordAudit(r);fs.writeFileSync(1,JSON.stringify({errors:a.errors,counts:a.counts,verifiedCheckpoints:a.verifiedCheckpoints,canStart:a.canStart,canFinish:a.canFinish}));process.exit(0);}

if(process.argv.includes('--validate-transition')){
 const i=process.argv.indexOf('--validate-transition');
 try{const before=JSON.parse(fs.readFileSync(process.argv[i+1],'utf8')).application_D24,after=JSON.parse(fs.readFileSync(process.argv[i+2],'utf8')).application_D24;const result=globalThis.tqtValidateTransition(before,after);fs.writeFileSync(1,JSON.stringify(result));process.exit(result.state==='PASS'?0:1);}catch(e){fs.writeFileSync(1,JSON.stringify({state:'FAIL',errors:[e.message]}));process.exit(1);}
}
// Test inputs are JSON data. Clone every object/array while sharing immutable
// strings, avoiding a serialized second copy of large historical evidence tokens.
function cloneFixtureData(x){if(Array.isArray(x))return x.map(cloneFixtureData);if(x&&typeof x==='object')return Object.fromEntries(Object.entries(x).map(([key,value])=>[key,cloneFixtureData(value)]));return x;}
const check=(r,id)=>r.application_preview.record.record_checks.find(x=>x.requirement_code===id),row=(a,id)=>a.rows.find(x=>x.code===id);
function unrecorded(r){const a=r.application_preview.record;a.checkpoint_checks=[];for(const x of a.record_checks)Object.assign(x,{record_state:'NOT_RECORDED',check_state:'NOT_CHECKED',master_record_id:null,record_ref:null,record_version:null,readback_state:'NOT_TESTED',access_state:'NOT_TESTED'});delete r.trial_storage_contract;delete r.application_preview.record.trial_store;for(const x of r.application_preview.record.record_checks)if(x.store_state==='TRIAL')Object.assign(x,{store_state:'UNVERIFIED',record_state:'NOT_RECORDED',check_state:'NOT_CHECKED',master_record_id:null,record_ref:null,record_version:null});return r;}
// Only synthetic boundary fixtures replace the accumulated execution/checkpoint history.
// R, real readback and real transition checks below retain the complete persisted source.
// Full-source read fixtures share only immutable historical entries; no data is trimmed.
function copyReadFixture(source){const a=source.application_preview.record,r=cloneFixtureData({...source,application_preview:{...source.application_preview,record:{...a,history:[],checkpoint_checks:[]}}});r.application_preview.record.history=a.history;r.application_preview.record.checkpoint_checks=a.checkpoint_checks;return r;}
// These transition cases edit only declarations/contracts or append history. Copy
// exactly those mutable branches; retain every earlier execution/checkpoint entry.
function copyTransitionFixture(a){return {...a,declarations:cloneFixtureData(a.declarations),declaration_history:cloneFixtureData(a.declaration_history),information_contract:cloneFixtureData(a.information_contract),history:[...a.history]};}
function sourceHistoryFingerprint(){const h=require('crypto').createHash('sha256'),a=R.application_preview.record;for(const key of ['history','checkpoint_checks']){h.update(key);for(const row of a[key]||[])h.update(JSON.stringify(row)).update('\n');}return h.digest('hex');}
const fullSourceHistoryFingerprint=sourceHistoryFingerprint();
function syntheticSeed(){const {server_receipt,...a}=R.application_preview.record;return {...R,application_preview:{...R.application_preview,record:{...a,history:[{event:'TEST_SEED',environment:'ISOLATED_TEST',actor:'TEST',at:'2026-10-11T00:00:00Z',evidence_ref:'test-only:synthetic-history'}],checkpoint_checks:[]}}};}
function test(name,change,verify){const r=unrecorded(cloneFixtureData(syntheticSeed()));change(r);try{verify(audit(r),r);}catch(e){throw Error(name+': '+e.message);}tests++;}
const written=r=>Object.assign(check(r,'PLAN'),{record_state:'RECORDED',master_record_id:'TEST-RECORD',record_ref:'test-only:record',record_version:'1'});
const matched=r=>{written(r);Object.assign(check(r,'PLAN'),{check_state:'MATCHED',process_code:r.application_preview.record.process_code,process_version:r.application_preview.record.process_version,target_code:r.application_preview.record.target_code,readback_state:'PASS',checked_record_version:'1',evidence_ref:'test-only:proof',checked_by:'test-actor',checked_at:'2026-10-11T00:00:00Z'});};
test('guidance separate from work',r=>{},(a,r)=>{assert(!r.work_form.record_control.definitions);assert(!JSON.stringify(r.work_form.record_control.guidance).includes('MOW001'));assert(r.application_preview.record.record_requirements.length);});
test('preparation is not Master entry',r=>{},a=>{assert.equal(a.counts.written,0);assert.equal(a.counts.verified,0);assert.equal(a.errors.length,0);assert.equal(a.verifiedCheckpoints.length,0);assert(!a.destinationReady);});
test('no check cannot disappear',r=>r.application_preview.record.record_checks.shift(),a=>{assert.equal(row(a,'MOW').checkState,'NEEDS_FIX');assert(a.errors.length);});
test('unknown Master is visible',r=>r.application_preview.record.record_requirements[0].master_code='UNKNOWN',a=>{assert(!row(a,'MOW').master);assert(a.errors.length);});
test('unknown guide rejected',r=>r.application_preview.record.record_requirements[0].guidance_id='UNKNOWN',a=>assert(a.errors.length));
test('wrong application rejected',r=>check(r,'PLAN').application_id='OTHER',a=>assert.equal(row(a,'PLAN').checkState,'NEEDS_FIX'));
test('wrong version rejected',r=>{matched(r);check(r,'PLAN').target_version='OLD';},a=>{assert(!row(a,'PLAN').verified);assert.equal(row(a,'PLAN').checkState,'NEEDS_FIX');});
test('wrong Master rejected',r=>{matched(r);check(r,'PLAN').master_code='CAT-015';},a=>assert(!row(a,'PLAN').verified));
test('duplicate check rejected',r=>r.application_preview.record.record_checks.push(cloneFixtureData(check(r,'PLAN'))),a=>assert(a.errors.length));
test('written without key rejected',r=>check(r,'PLAN').record_state='RECORDED',a=>{assert(!row(a,'PLAN').written);assert(a.errors.length);});
test('written independent of comparison',written,a=>{assert(row(a,'PLAN').written);assert(!row(a,'PLAN').verified);assert.equal(row(a,'PLAN').checkState,'NOT_CHECKED');});
test('matched with evidence',matched,a=>assert(row(a,'PLAN').verified));
for(const key of ['master_record_id','record_ref','record_version','evidence_ref','checked_by','checked_at'])test('missing '+key,r=>{matched(r);check(r,'PLAN')[key]=null;},a=>{assert(!row(a,'PLAN').verified);assert.equal(row(a,'PLAN').checkState,'NEEDS_FIX');});
test('repair does not erase recording',r=>{matched(r);check(r,'PLAN').check_state='NEEDS_FIX';},a=>{assert(row(a,'PLAN').written);assert(!row(a,'PLAN').verified);});
test('future output not due',r=>r.application_preview.record.current_checkpoint='CP01',a=>assert(!row(a,'RESULT-P03').due));
test('output becomes due',r=>r.application_preview.record.current_checkpoint='CP04',a=>assert(row(a,'RESULT-P03').due));
test('new output needs declaration',r=>r.application_preview.record.plan.push({id:'P06'}),a=>assert(a.errors.some(x=>x.includes('P06'))));
test('field cannot be omitted',r=>r.application_preview.record.record_requirements=r.application_preview.record.record_requirements.filter(x=>x.code!=='FIELD-identity'),a=>assert(a.errors.some(x=>x.includes('identity'))));
test('foreign check rejected',r=>{const c=cloneFixtureData(check(r,'PLAN'));c.requirement_code='UNKNOWN';r.application_preview.record.record_checks.push(c);},a=>assert(a.errors.length));
test('wrong option rejected',r=>check(r,'PLAN').check_state='GREEN',a=>assert(a.errors.length));
test('cannot jump to last checkpoint',r=>r.application_preview.record.checkpoint_checks=[{checkpoint:'CP07',application_id:r.application_preview.record.application_id,process_version:r.application_preview.record.process_version,target_version:r.application_preview.record.target_version,result:'PASS',validity:'CURRENT',evidence_ref:'test-only'}],a=>assert.equal(a.verifiedCheckpoints.length,0));
assert.deepEqual(R.work_form.record_control.state_options.check_state.map(x=>x.label),['Chưa đối chiếu','Đã đối chiếu','Cần sửa lại']);
assert.deepEqual(R.work_form.record_control.state_options.record_state.map(x=>x.label),['Chưa ghi','Đã ghi']);
for(const m of html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g))if(!/application\/json/.test(m[1])&&m[2].trim())new vm.Script(m[2]);
// CLI modes above already returned; the full parsed R remains authoritative.
html=null;/release/.test('release');
console.log(JSON.stringify({tests,scope:'DESIGN_PROJECTION_ONLY',counts:audit(R).counts,pg:'NOT_RUN'}));
// Regression walk: complete synthetic evidence, then break one boundary at a time.
function fixture(){
 const r=unrecorded(cloneFixtureData(syntheticSeed())),a=r.application_preview.record;a.current_checkpoint='CP07';
 a.assignments={state:'ASSIGNED',reviewer_id:'TEST-INDEPENDENT',authority_ref:'test-only:authority'};a.plan.find(p=>p.id==='P04').actor='TEST-INDEPENDENT';a.information_contract.handoffs.find(h=>h.plan_id==='P03').recipient='TEST-INDEPENDENT';
 testTrust.principals=[{id:'TEST-INDEPENDENT',application_id:a.application_id,target_version:a.target_version,roles:['REVIEWER']}];
 for(const m of r.work_form.record_control.masters)m.source_state='VERIFIED';
 for(const x of a.record_checks)Object.assign(x,{record_state:'RECORDED',check_state:'MATCHED',master_record_id:'SIM-'+x.requirement_code,record_ref:'test-only:'+x.requirement_code,record_version:'1',checked_record_version:'1',readback_state:'PASS',access_state:'PASS',process_code:a.process_code,process_version:a.process_version,target_code:a.target_code,evidence_ref:'test-only:readback',checked_by:'TEST',checked_at:'2026-10-11T00:00:00Z'});
 a.questions_complete=true;a.requirements_checked=true;
 for(const x of a.declarations)Object.assign(x,{result:'PASS',validity:'CURRENT',evidence_refs:['test-only:declaration']});
 Object.assign(a.preparation_review,{output_contracts_reviewed:true,branches_reviewed:true,evidence_ref:'test-only:coverage'});
 Object.assign(a.start_confirmation,{state:'CONFIRMED',evidence_ref:'test-only:start'});
 const payload={application_id:a.application_id,target_version:a.target_version,evidence_ref:'test-only:payload',actor:a.actor,at:'2026-10-11T00:00:00Z'};
 a.plan_results=a.plan.map(p=>{p.status='DONE';return {...payload,id:'SIM-'+p.id,plan_id:p.id,actor:p.actor,scope:a.scope,output_ref:'test-only:output',output_version:'1'};});
 a.contract_binding=globalThis.tqtContractPin(a);
 a.information_contract.review={state:'PASS',reviewer_id:'TEST-INDEPENDENT',evidence_ref:'test-only:independent',at:'2026-10-11T00:00:00Z',contract_binding:a.contract_binding};
 a.start_confirmation.contract_binding=a.contract_binding;
 testTrust.design_reads=[];
 for(const x of a.plan_results){x.contract_binding=a.contract_binding;if(['P02','P03'].includes(x.plan_id)){const artifact=designFixture(r,x);x.artifact={path:'test-only:design-'+x.plan_id,sha256:globalThis.tqtSHA256(globalThis.tqtCanonical(artifact))};testTrust.design_reads.push({payload_token:globalThis.tqtCanonical(x),artifact});}if(x.plan_id==='P01')x.data={answers:a.declarations.map(d=>({key:d.key,answer:d.answer})),source_refs:a.input_refs};const h=a.information_contract.handoffs.find(h=>h.plan_id===x.plan_id),ch=a.record_checks.find(ch=>ch.requirement_code==='RESULT-'+x.plan_id);Object.assign(ch,{master_record_id:x.id,record_ref:h.output_ref,record_version:x.output_version,checked_payload_token:globalThis.tqtCanonical(x)});}
 const canonical=v=>JSON.stringify(v,(_,x)=>x&&typeof x==='object'&&!Array.isArray(x)?Object.fromEntries(Object.keys(x).sort().map(k=>[k,x[k]])):x);
 testTrust.endpoint_receipts=[];
 for(const ep of a.trial_endpoints){const {access_check,...spec}=ep;ep.access_check={state:'PASS',read:'PASS',write:'PASS',evidence_ref:'test-only:endpoint',spec_token:canonical(spec)};testTrust.endpoint_receipts.push({...ep.access_check,application_id:a.application_id,target_version:a.target_version,requirement_code:ep.requirement_code});}
 payload.contract_binding=a.contract_binding;
 payload.product_binding=a.plan_results.filter(x=>['P02','P03'].includes(x.plan_id)).map(x=>({plan_id:x.plan_id,output_ref:x.output_ref,output_version:x.output_version}));
 a.test_result='PASS';a.connection_tests={in:'PASS',out:'PASS'};a.test_cases=a.information_contract.criteria.map(c=>({...payload,id:'SIM-'+c.id,criterion_id:c.id,expected:c.expected,actual:'TEST fixture conforms',reviewer_id:'TEST-INDEPENDENT',result:'PASS'}));
 Object.assign(a.release,{state:'APPROVED',decision_ref:'SIM-DECISION',ack_ref:'SIM-ACK'});
 a.decisions=[{...payload,id:'SIM-DECISION',outcome:'APPROVED',scope:a.release.scope,actor:a.approver,authority_ref:'test-only:authority'}];
 a.receipts=[{...payload,id:'SIM-ACK',decision_id:'SIM-DECISION',recipient:a.recipient}];
 a.checkpoint_checks=[];
 for(const cp of r.records.find(x=>x.code===a.process_code).workflow.checkpoints){const state=audit(r).checkpointStates.find(x=>x.id===cp.id);a.checkpoint_checks.push({checkpoint:cp.id,revision:1,application_id:a.application_id,process_code:a.process_code,process_version:a.process_version,target_code:a.target_code,target_version:a.target_version,result:'PASS',validity:'CURRENT',checked_by:'TEST',checked_at:'2026-10-11T00:00:00Z',evidence_ref:'test-only:checkpoint',dependency_key:state.dependency_key});}
 return r;
}
const complete=fixture();assert.equal(audit(complete).verifiedCheckpoints.length,7);tests++;
function mutation(name,change,verify){const r=cloneFixtureData(complete);change(r);try{verify(audit(r),r);}catch(e){throw Error(name+': '+e.message);}tests++;}
for(const code of ['MOW','MOT-1.1','MOT-1.2','MOT-1.3','START','DECISION','ACK','COVERAGE','HISTORY','ISSUE','BLOCKED','CANCELLED','NA','CHANGE'])mutation('deleted '+code,r=>{const a=r.application_preview.record;a.record_requirements=a.record_requirements.filter(x=>x.code!==code);a.record_checks=a.record_checks.filter(x=>x.requirement_code!==code);},a=>{assert(a.errors.length);assert(!a.canFinish);});
mutation('wrong process version',r=>r.application_preview.record.process_version='old',a=>assert(!a.canStart));
mutation('readback FAIL cannot MATCH',r=>check(r,'PLAN').readback_state='FAIL',a=>assert.equal(row(a,'PLAN').checkState,'NEEDS_FIX'));
mutation('readback NOT_TESTED cannot MATCH',r=>check(r,'PLAN').readback_state='NOT_TESTED',a=>assert(!row(a,'PLAN').verified));
mutation('record version stale',r=>check(r,'PLAN').record_version='2',a=>assert(!row(a,'PLAN').verified));
mutation('missing checkpoint checker',r=>r.application_preview.record.checkpoint_checks[2].checked_by=null,a=>assert(!a.canStart));
mutation('changed plan invalidates from preparation',r=>r.application_preview.record.plan[2].output+=' changed',a=>assert.deepEqual(a.verifiedCheckpoints,['CP01']));
mutation('new issue keeps first three',r=>{r.application_preview.record.issue_ref='TEST-ISSUE';check(r,'ISSUE').check_state='NOT_CHECKED';},a=>assert.deepEqual(a.verifiedCheckpoints,['CP01','CP02','CP03']));
mutation('future mismatch keeps early proof',r=>check(r,'TEST').readback_state='FAIL',a=>assert.deepEqual(a.verifiedCheckpoints,['CP01','CP02','CP03','CP04']));
mutation('dormant cancellation destination ignored',r=>r.work_form.record_control.masters.find(x=>x.code==='CAT-244*').source_state='MISSING',a=>assert(a.canFinish));
mutation('activated cancellation blocks relevant step',r=>{r.work_form.record_control.masters.find(x=>x.code==='CAT-244*').source_state='MISSING';r.application_preview.record.branch_records.push({kind:'CANCELLED'});},a=>assert.deepEqual(a.verifiedCheckpoints,['CP01','CP02','CP03']));
mutation('approval wrong actor',r=>r.application_preview.record.decisions[0].actor='OTHER',a=>assert(!a.verifiedCheckpoints.includes('CP06')));
mutation('approval wrong scope',r=>r.application_preview.record.decisions[0].scope='PRODUCTION',a=>assert(!a.canFinish));
mutation('approval wrong target version',r=>r.application_preview.record.decisions[0].target_version='old',a=>assert(!a.canFinish));
mutation('receipt wrong recipient',r=>r.application_preview.record.receipts[0].recipient='OTHER',a=>assert(!a.canFinish));
mutation('receipt wrong decision',r=>r.application_preview.record.receipts[0].decision_id='OTHER',a=>assert(!a.canFinish));
mutation('receipt deleted keeps first six',r=>r.application_preview.record.receipts=[],a=>assert.equal(a.verifiedCheckpoints.length,6));
mutation('latest failed revision keeps history',r=>{const a=r.application_preview.record;a.checkpoint_checks.push({...a.checkpoint_checks[4],revision:2,result:'FAIL'});},a=>{assert.equal(a.verifiedCheckpoints.length,4);assert.equal(a.checkpointStates[4].history.length,2);});
mutation('duplicate checkpoint revision rejected',r=>r.application_preview.record.checkpoint_checks.push(cloneFixtureData(r.application_preview.record.checkpoint_checks[0])),a=>assert.equal(a.verifiedCheckpoints.length,0));
console.log(JSON.stringify({tests,regression:'QTTH05_WALK',synthetic_full_walk:7,live_application:audit(R).verifiedCheckpoints.length,pg:'NOT_RUN'}));

// Real persisted trial declarations: existence/readback are separate from semantic approval.
const baseTrial=audit(R);assert.equal(baseTrial.rows.filter(x=>x.code.startsWith('FIELD-')&&x.written).length,R.work_form.fields.length);assert.deepEqual(baseTrial.errors,[]); // Real progress is not frozen at 0/7.
{const noProof=copyReadFixture(R);noProof.application_preview.record.checkpoint_checks=[];assert.equal(audit(noProof).verifiedCheckpoints.length,0);} // Evidence, not labels, grants progress.
let trialCases=1;
for(const mutate of [
 r=>r.application_preview.record.declarations.shift(),
 r=>r.application_preview.record.declarations.push(cloneFixtureData(r.application_preview.record.declarations[0])),
 r=>r.application_preview.record.declarations[0].schema_version='2.0',
 r=>r.application_preview.record.declarations[0].record_version=String(Number(r.application_preview.record.declarations[0].record_version)+1),
 r=>r.application_preview.record.declarations[0].surprise='unregistered column',
 r=>r.application_preview.record.trial_store.source_ref='another file',
 r=>delete r.application_preview.record.trial_store,
 r=>check(r,'FIELD-identity').store_state='UNVERIFIED',
 r=>r.application_preview.record.trial_store.production=true,
 r=>r.application_preview.record.scope_stage='G2',
 r=>check(r,'FIELD-identity').record_ref='fake:row',
 r=>check(r,'FIELD-identity').master_record_id='another row'
]){const r=copyReadFixture(R);mutate(r);assert(!row(audit(r),'FIELD-identity').written);trialCases++;}
{const readTrial=copyReadFixture(R),ar=readTrial.application_preview.record,dr=ar.declarations[0],xr=check(readTrial,'FIELD-identity');
Object.assign(xr,{check_state:'MATCHED',readback_state:'PASS',process_code:ar.process_code,process_version:ar.process_version,target_code:ar.target_code,checked_record_version:dr.record_version,evidence_ref:'test-only:readback',checked_by:'TEST',checked_at:'2026-10-11T00:00:00Z',checked_payload_token:JSON.stringify(dr, Object.keys(dr).sort())});
assert(row(audit(readTrial),'FIELD-identity').verified);trialCases++;
dr.answer+=' changed';assert(!row(audit(readTrial),'FIELD-identity').verified);trialCases++;
}
console.log(JSON.stringify({trial_cases:trialCases,persisted_declarations:baseTrial.counts.written,checkpoints:baseTrial.verifiedCheckpoints.length,scope:'TRIAL_NOT_PG'}));

// PR13: information must survive every handoff; a PASS flag never replaces the applied contract.
let contractCases=0;
for(const [name,change] of [
 ['missing Master',r=>r.work_form.record_control.masters=r.work_form.record_control.masters.filter(x=>x.code!=='CAT-206*')],
 ['missing contract',r=>delete r.application_preview.record.information_contract],
 ['missing MOT outputs',r=>r.application_preview.record.information_contract.rows=r.application_preview.record.information_contract.rows.filter(x=>x.mot_code!=='1.2')],
 ['changed meaning same version',r=>r.application_preview.record.information_contract.rows[0].meaning+=' changed'],
 ['changed cardinality',r=>r.application_preview.record.information_contract.rows[0].cardinality='0..n'],
 ['wrong destination',r=>r.application_preview.record.information_contract.rows[0].destination_master='CAT-025'],
 ['new contract version',r=>r.application_preview.record.information_contract.version='999'],
 ['missing plan interface',r=>r.application_preview.record.information_contract.handoffs.pop()],
 ['missing predefined cases',r=>r.application_preview.record.information_contract.criteria=[]],
 ['self review',r=>r.application_preview.record.information_contract.review.reviewer_id=r.application_preview.record.actor],
 ['missing endpoint',r=>r.application_preview.record.trial_endpoints.pop()],
 ['unproved write access',r=>r.application_preview.record.trial_endpoints[0].access_check.write='NOT_TESTED'],
 ['changed endpoint spec',r=>r.application_preview.record.trial_endpoints[0].path='fake'],
 ['wrong work binding',r=>r.application_preview.record.plan_results[2].contract_binding.version='old'],
 ['wrong test binding',r=>r.application_preview.record.test_cases[0].contract_binding.version='old'],
 ['uncovered criterion',r=>r.application_preview.record.test_cases.pop()],
 ['invented expected value',r=>r.application_preview.record.test_cases[0].expected='Anything is fine'],
 ['no actual observation',r=>delete r.application_preview.record.test_cases[0].actual],
 ['worker self-tests',r=>r.application_preview.record.test_cases[0].reviewer_id=r.application_preview.record.actor],
 ['wrong reviewed product',r=>r.application_preview.record.test_cases[0].product_binding[0].output_version='wrong'],
 ['wrong approval contract',r=>r.application_preview.record.decisions[0].contract_binding.version='old'],
 ['wrong approved product',r=>r.application_preview.record.decisions[0].product_binding[0].output_version='wrong'],
 ['wrong receipt contract',r=>r.application_preview.record.receipts[0].contract_binding.version='old'],
 ['wrong received product',r=>r.application_preview.record.receipts[0].product_binding[0].output_version='wrong']
]){const r=cloneFixtureData(complete);change(r);assert(!audit(r).canFinish,name);contractCases++;}
for(const mutate of [
 r=>r.application_preview.record.record_checks=r.application_preview.record.record_checks.filter(x=>x.requirement_code!=='FIELD-identity'),
 r=>r.application_preview.record.record_checks=null,
 r=>r.application_preview.record.record_checks.push(null),
 r=>r.application_preview.record.record_checks='bad',
 r=>r.application_preview.record.declarations[0]=null,
 r=>r.application_preview.record.record_requirements[0]=null,
 r=>r.application_preview.record.information_contract.rows=[null],
 r=>r.application_preview.record.information_contract.criteria='bad',
 r=>r.application_preview.record.trial_endpoints=[null]
]){const r=copyReadFixture(R);mutate(r);const x=audit(r);assert(!x.canStart&&!x.canFinish);assert(x.errors.length||!x.contract.reviewed);contractCases++;}
const validate=globalThis.tqtValidateTransition;
// Run full real-history comparisons in a receiver process with only the engine
// and complete application. Avoid retaining a second full HTML/catalog beside it.
function realTransitionCases(previous){let contractCases=0;const validate=globalThis.tqtValidateTransition;

assert.equal(validate(previous,copyTransitionFixture(previous)).state,'PASS');contractCases++;
for(const change of [
 a=>a.declarations[0].answer+=' changed without revision',
 a=>a.declarations[0].record_version=String(Number(a.declarations[0].record_version)+1),
 a=>a.declaration_history.push({...a.declarations[0],answer:'fabricated'}),
 a=>a.declarations.pop(),
 a=>a.information_contract.rows[0].meaning='changed',
 a=>a.information_contract.history.push({fake:true})
]){const after=copyTransitionFixture(previous);change(after);assert.equal(validate(previous,after).state,'FAIL');contractCases++;}
const next=copyTransitionFixture(previous);next.declaration_history.push(cloneFixtureData(previous.declarations[0]));next.declarations[0].answer+=' changed';next.declarations[0].record_version=String(Number(previous.declarations[0].record_version)+1);
assert.equal(validate(previous,next).state,'PASS');contractCases++;
const rewrite=copyTransitionFixture(next);rewrite.declaration_history[0].answer='rewrite old';assert.equal(validate(next,rewrite).state,'FAIL');contractCases++;
const newContract=copyTransitionFixture(previous),prior=cloneFixtureData(previous.information_contract);delete prior.history;newContract.information_contract.history.push(prior);newContract.information_contract.version=String(Number(previous.information_contract.version)+1);newContract.information_contract.rows.forEach(x=>x.contract_version=newContract.information_contract.version);
assert.equal(validate(previous,newContract).state,'PASS');contractCases++;

 return {cases:contractCases,unchanged:'PASS',history:'FULL_SOURCE_NOT_TRIMMED'};
}
function runRealTransitionPreflight(){const os=require('os'),path=require('path'),cp=require('child_process'),crypto=require('crypto'),dir=fs.mkdtempSync(path.join(os.tmpdir(),'tqt-real-transition-TEST-'));
 try{
 // A short-lived producer copies the full actual application and exact engine.
 // It exits before the history receiver starts, while main has not loaded R yet.
 const prepare=String.raw`const fs=require('fs'),path=require('path'),crypto=require('crypto');let html=fs.readFileSync(process.argv[1],'utf8');const script=id=>html.match(new RegExp('<script id="'+id+'"[^>]*>([\\s\\S]*?)</script>'))[1];const engine=Buffer.from(script('tqt-record-control')).toString(),record=JSON.parse(script('tqt-composite-processes')).catalog.application_preview.record;html=null;/release/.test('release');const source=JSON.stringify(record);fs.writeFileSync(path.join(process.argv[2],'application.json'),source);fs.writeFileSync(path.join(process.argv[2],'engine.js'),engine);console.log(JSON.stringify({source_sha256:crypto.createHash('sha256').update(source).digest('hex'),engine_sha256:crypto.createHash('sha256').update(engine).digest('hex')}));`;
 const made=cp.spawnSync(process.execPath,[...process.execArgv,'-e',prepare,process.argv[2]||__dirname+'/view.html',dir],{encoding:'utf8',maxBuffer:2e6});assert.equal(made.status,0,made.stderr);const copied=JSON.parse(made.stdout);
 const code=`const fs=require('fs'),vm=require('vm'),assert=require('assert'),crypto=require('crypto');${cloneFixtureData.toString()};${copyTransitionFixture.toString()};vm.runInThisContext(fs.readFileSync(process.argv[1],'utf8'));let raw=fs.readFileSync(process.argv[2]);const source_sha256=crypto.createHash('sha256').update(raw).digest('hex'),document=JSON.parse(raw);raw=null;const result=(${realTransitionCases.toString()})(document);console.log(JSON.stringify({...result,source_sha256}));`;
 const result=cp.spawnSync(process.execPath,[...process.execArgv,'-e',code,path.join(dir,'engine.js'),path.join(dir,'application.json')],{encoding:'utf8',maxBuffer:2e6});assert.equal(result.status,0,result.stderr);const proof=JSON.parse(result.stdout);assert.equal(proof.source_sha256,copied.source_sha256);return {...proof,engine_sha256:copied.engine_sha256};
 }finally{fs.rmSync(dir,{recursive:true,force:true});}
}
const realTransitionEvidence=realTransitionPreflight;
assert.equal(realTransitionEvidence.source_sha256,persistedApplicationSHA,'FULL_REAL_TRANSITION_SOURCE');
assert.equal(realTransitionEvidence.engine_sha256,require('crypto').createHash('sha256').update(engineSource).digest('hex'),'FULL_REAL_TRANSITION_ENGINE');
contractCases+=realTransitionEvidence.cases;

{const changed=cloneFixtureData(complete);changed.application_preview.record.information_contract.rows[0].meaning+=' revised';assert.deepEqual(audit(changed).verifiedCheckpoints,['CP01']);contractCases++;}
console.log(JSON.stringify({information_contract_cases:contractCases,actual_contract_rows:R.application_preview.record.information_contract.rows.length,actual_criteria:R.application_preview.record.information_contract.criteria.length,synthetic_full_walk:audit(complete).verifiedCheckpoints.length,real_checkpoints:audit(R).verifiedCheckpoints.length,server_write_hook:'NOT_PROBED_BY_THIS_SUITE',pg:'NOT_RUN'}));

// PR14: acceptance is measured at each boundary, not only by final checkpoint state.
let pr14Cases=0;const cc=x=>globalThis.tqtCanonical(x);
for(const [name,change] of [
 ['all product fields removed',a=>a.information_contract.rows=a.information_contract.rows.filter(x=>x.contract_role!=='PRODUCT_SPEC')],
 ['request identity removed',a=>a.information_contract.rows=a.information_contract.rows.filter(x=>x.field_code!=='requestId')],
 ['interface graph removed',a=>a.information_contract.product_interfaces=[]],
 ...['application_id','target_code','target_version','process_code','process_version','mot_version','rule_version','data_type','source_path','destination_field','nullable','cardinality','unit'].map(k=>[k,a=>a.information_contract.rows[2][k]='UNKNOWN']),
 ...['input_ref','output_ref','recipient','input_schema','output_schema'].map(k=>['handoff '+k,a=>a.information_contract.handoffs[1][k]='OTHER']),
 ['unknown output field',a=>a.information_contract.handoffs[0].output_fields=['FAKE']],
 ['missing mapping',a=>delete a.information_contract.handoffs[1].mapping.scope]
]){const r=copyReadFixture(R);change(r.application_preview.record);assert(!audit(r).contract.ready,name);pr14Cases++;}
for(const planId of ['P01','P02','P03','P04','P05']){
 const r=cloneFixtureData(complete),a=r.application_preview.record,x=a.plan_results.find(x=>x.plan_id===planId);delete x.scope;
 assert.equal(globalThis.tqtPayloadAudit(r,planId,x).state,'FAIL');assert(!audit(r).canFinish);pr14Cases++;
}
for(const [name,change] of [
 ['missing preparation',a=>a.plan_results=a.plan_results.filter(x=>x.plan_id!=='P01')],
 ['wrong preparation record ID',a=>a.plan_results[0].id='OTHER'],
 ['wrong preparation payload',a=>a.plan_results[0].scope='OTHER'],
 ['no execution history',a=>a.history=[]],
 ['unassigned independent reviewer',a=>a.assignments.reviewer_id=null],
 ['self assigned reviewer',a=>a.assignments.reviewer_id=a.actor]
]){const r=cloneFixtureData(complete);change(r.application_preview.record);assert(!audit(r).canStart,name);pr14Cases++;}
// Access statements inside a submitted document confer no trust by themselves.
assert(!globalThis.tqtRecordAudit(complete).canStart);pr14Cases++;
for(const field of ['schema_ref','key_fields']){const r=cloneFixtureData(complete),ep=r.application_preview.record.trial_endpoints[0];ep[field]=field==='schema_ref'?'catalog.NO_SUCH_SCHEMA':['NO_SUCH_KEY'];const {access_check,...spec}=ep;ep.access_check.spec_token=cc(spec);const trusted=cloneFixtureData(testTrust);trusted.endpoint_receipts[0].spec_token=cc(spec);assert(!globalThis.tqtRecordAudit(r,trusted).canStart);pr14Cases++;}
// These TEST transition mutations replace arrays or edit a row's scalar field.
// Share immutable large strings, copy every row that a mutation can edit.
function copyEvidenceFixture(a){const out={...a};for(const key of ['history','checkpoint_checks','record_checks','plan_results','decisions','receipts','test_cases','trial_records'])out[key]=(a[key]||[]).map(row=>({...row}));return out;}
{const beforeEvidence=complete.application_preview.record;
for(const change of [a=>a.history=[],a=>a.checkpoint_checks=[],a=>a.checkpoint_checks[0].result='FAIL',a=>a.record_checks=[],a=>a.plan_results[0].output_ref='other',a=>a.decisions=[],a=>a.receipts=[],a=>a.test_cases=[],a=>a.trial_records.push({id:'NEW'})]){const after=copyEvidenceFixture(beforeEvidence);change(after);assert.equal(validate(beforeEvidence,after).state,'FAIL');pr14Cases++;}
const revised=copyEvidenceFixture(beforeEvidence);revised.plan_results[0].output_version='2';revised.plan_results[0].output_ref='test-only:new-product';revised.evidence_revision=Number(beforeEvidence.evidence_revision||1)+1;revised.history.push({event:'EVIDENCE_REVISION',revision:revised.evidence_revision,actor:'TEST',reason:'Retain exact earlier evidence',at:'2026-10-11T00:00:00Z',previous_evidence:globalThis.tqtEvidenceMaterial(beforeEvidence)});assert.equal(validate(beforeEvidence,revised).state,'PASS');assert(!audit({...complete,application_preview:{...complete.application_preview,record:revised}}).canStart);pr14Cases++;
}
assert.equal(realTransitionEvidence.unchanged,'PASS');assert.equal(realTransitionEvidence.history,'FULL_SOURCE_NOT_TRIMMED');pr14Cases++;
console.log(JSON.stringify({pr14_boundary_cases:pr14Cases,synthetic_trusted_context_only:true,untrusted_self_attestation_blocked:true,real_checkpoints:audit(R).verifiedCheckpoints.length}));
// Child packet/design tests use the exact schema, contract, plan and declaration
// values they consume, not unrelated execution/checkpoint history. Real R stays full.
function writeHandoffTestContext(dir){
 const path=require('path'),a=R.application_preview.record,keys=['application_id','target_code','target_version','process_code','process_version','scope','scope_stage','actor','plan','declarations','input_refs','information_contract'];
 const catalog={application_preview:{source_ref:R.application_preview.source_ref,record:Object.fromEntries(keys.map(key=>[key,a[key]]))},work_form:{fields:R.work_form.fields},work_master_designs:{records:[R.work_master_designs.records.find(x=>x.code==='CAT-206*')]}};
 assert.deepEqual(tqtContractPin(catalog.application_preview.record),tqtContractPin(a));
 const context={schema:'TQT-HANDOFF-TEST-CONTEXT/1',environment:'ISOLATED_TEST',engine_sha256:require('crypto').createHash('sha256').update(engineSource).digest('hex'),catalog};
 fs.writeFileSync(path.join(dir,'test-context.json'),JSON.stringify(context));fs.writeFileSync(path.join(dir,'test-engine.js'),engineSource);
}
async function fileHandoffSlice(){
 const os=require('os'),path=require('path'),cp=require('child_process'),crypto=require('crypto'),tmp=fs.mkdtempSync(path.join(os.tmpdir(),'tqt-handoff-TEST-'));
 const write=(n,x)=>fs.writeFileSync(path.join(tmp,n),JSON.stringify(x)),read=n=>JSON.parse(fs.readFileSync(path.join(tmp,n),'utf8'));
 const policy={environment:'TEST',receiver:'P02',expected_output_version:'1',expected_state_revision:0,read_allowed:true,write_allowed:true};
 const call=mode=>{const p=cp.spawnSync(process.execPath,[...process.execArgv,__filename,process.argv[2]||__dirname+'/view.html','--test-handoff',mode,tmp],{encoding:'utf8',maxBuffer:2e6});assert.equal(p.status,0,p.stderr);return JSON.parse(p.stdout);};
 let cases=0;try{
  writeHandoffTestContext(tmp);
  write('policy.json',policy);write('state.json',{revision:0,cancelled:false,received:null,effects:[]});const produced=call('produce'),packet=read('packet.json');
  const accepted=call('consume');assert.equal(accepted.state,'ACK');assert.equal(accepted.sha256,produced.sha256);assert.equal(accepted.answer_count,R.application_preview.record.declarations.length);cases++;
  assert.equal(call('consume').replayed,true);assert.equal(read('state.json').effects.length,1);cases++;
  const reset=()=>{write('state.json',{revision:0,cancelled:false,received:null,effects:[]});write('policy.json',policy);write('packet.json',packet);};
  for(const mutate of [p=>delete p.payload.scope,p=>p.payload.scope=12,p=>p.payload.target_version='OLD',p=>p.payload.application_id='OTHER',p=>p.payload.output_version='2',p=>p.recipient_plan_id='OTHER',p=>p.payload.data.answers[0].answer='Invented',p=>delete p.payload.data]){reset();const p=cloneFixtureData(packet);mutate(p);write('packet.json',p);const x=call('consume');assert.equal(x.state,'BLOCKED');assert.equal(x.return_to,'P01');assert.equal(read('state.json').effects.length,0);cases++;}
  for(const change of [{read_allowed:false},{write_allowed:false}]){reset();write('policy.json',{...policy,...change});assert.equal(call('consume').state,'BLOCKED');cases++;}
  reset();write('state.json',{revision:0,cancelled:true,received:null,effects:[]});assert.equal(call('consume').error,'CANCELLED');cases++;
  reset();write('state.json',{revision:1,cancelled:false,received:null,effects:[]});assert.equal(call('consume').error,'CONCURRENT_REVISION');cases++;
  reset();write('policy.json',{...policy,drop_ack_once:true});assert.equal(call('consume').state,'ACK_LOST');assert.equal(call('consume').replayed,true);assert.equal(read('state.json').effects.length,1);cases++;
  reset();const parallel=()=>new Promise((resolve,reject)=>{const p=cp.spawn(process.execPath,[...process.execArgv,__filename,process.argv[2]||__dirname+'/view.html','--test-handoff','consume',tmp]);let out='';p.stdout.on('data',d=>out+=d);p.on('error',reject);p.on('close',code=>code?reject(Error(out)):resolve(JSON.parse(out)));});
  const both=await Promise.all([parallel(),parallel()]);assert(both.some(x=>x.state==='ACK'));assert(both.every(x=>x.state==='ACK'||x.error==='CONCURRENT_WRITE'));assert.equal(read('state.json').effects.length,1);cases++;
  const changed=cloneFixtureData(packet);changed.payload.at='2026-10-11T00:00:00Z';write('packet.json',changed);assert.equal(call('consume').error,'DUPLICATE_KEY_DIFFERENT_CONTENT');cases++;
  const events=fs.readFileSync(path.join(tmp,'events.jsonl'),'utf8').trim().split('\n').map(JSON.parse);assert(events.some(x=>x.state==='BLOCKED'&&x.issue_master==='CAT-069?'&&x.owner&&x.return_to==='P01'));
  console.log(JSON.stringify({pr14_file_handoff:{cases,state:'PASS',producer:'separate process; creates packet from declarations',consumer:'separate process; opens persisted packet and uses scope/answers',producer_sha256:produced.sha256,readback_sha256:accepted.sha256,concurrent_effect_count:read('state.json').effects.length,environment:'ISOLATED_TEST_NOT_MOW001_COMPLETION',real_endpoint_permissions:'NOT_PROVED',pg:'NOT_RUN'}}));
 }finally{fs.rmSync(tmp,{recursive:true,force:true});}
}
fileHandoffSlice().catch(e=>{console.error(e);process.exitCode=1;});
// Logical product-input schemas and cancellation identity; no backend or PG execution.
{
 const input={requestId:'TEST-REQ',revision:1,caller:{id:'TEST-CALLER',return_to:'TEST-INBOX',target_version:'TEST-V1'},query:'Find field',description:null,scope:{sources:['TEST'],permission_context:{}},filters:{}};
 input.cancellation={requestId:input.requestId,revision:1,caller:cloneFixtureData(input.caller),scope:cloneFixtureData(input.scope),target_version:'TEST-V1',state:'cancelled',reason:'TEST cancel',cancelledAt:'2026-10-11T00:00:00Z'};
 assert.equal(globalThis.tqtProductInputAudit(R,'1.3',input).state,'PASS');let cases=1;
 for(const change of [x=>delete x.cancellation,x=>delete x.cancellation.reason,x=>x.cancellation.revision=2,x=>x.cancellation.caller.id='OTHER',x=>x.cancellation.scope.sources=['OTHER'],x=>x.cancellation.target_version='OLD',x=>x.cancellation.cancelledAt='not a date']){const x=cloneFixtureData(input);change(x);assert.equal(globalThis.tqtProductInputAudit(R,'1.3',x).state,'FAIL');cases++;}
 const changed=copyReadFixture(R);changed.work_master_designs.records.find(x=>x.code==='CAT-206*').validation.schemas.positive_integer.minimum=0;assert(!audit(changed).contract.ready);cases++;
 for(const text of ['', 'abc', 'Hợp đồng thông tin', 'x'.repeat(10000)])assert.equal(globalThis.tqtSHA256(text),require('crypto').createHash('sha256').update(text).digest('hex'));
 console.log(JSON.stringify({pr14_product_input_cases:cases,sha256_crosscheck_vectors:4}));
}
{
 const request={requestId:'TEST',revision:1,caller:{id:'CALLER',return_to:'INBOX',target_version:'TEST'},query:'Find',description:null,scope:{sources:['TEST'],permission_context:{}},filters:{}};
 const response={requestId:'TEST',revision:1,retrievalStatus:'success',candidates:[],evaluation:{status:'red',reasons:[],missingInformation:[],requestRevision:1,ruleVersion:'TEST'},source:{ref:'TEST-SOURCE',version:'1'},scope:cloneFixtureData(request.scope),version:'1',mode:'example',retrievedAt:'2026-10-11T00:00:00Z'};
 const cancellation={requestId:'TEST',revision:1,caller:cloneFixtureData(request.caller),scope:cloneFixtureData(request.scope),target_version:'TEST',state:'cancelled',reason:'User cancelled TEST',cancelledAt:'2026-10-11T00:00:00Z'};
 const context={requestId:request.requestId,revision:request.revision,scope:cloneFixtureData(request.scope),ruleVersion:'TEST',sources:{'TEST-SOURCE':'1'}};
 for(const [from,to,parts] of [['CALLER','1.1',{request}],['1.1','1.2',{request,response}],['1.1','1.3',{request,response}],['1.2','1.3',{request,response}],['1.2','1.3',{request,cancellation}]])assert.equal(globalThis.tqtMapProductHandoff(R,from,to,parts,context).state,'PASS');
 assert.equal(globalThis.tqtMapProductHandoff(R,'1.1','1.3',{request}).state,'FAIL');
 assert.equal(globalThis.tqtMapProductHandoff(R,'1.2','1.3',{request,response,cancellation}).state,'FAIL');
 assert.equal(globalThis.tqtMapProductHandoff(R,'1.1','1.3',{request,response:{...response,revision:2}}).state,'FAIL');
 console.log(JSON.stringify({pr14_product_mapping_cases:8,scope:'LOGICAL_PACKETS_NOT_BACKEND_EXECUTION'}));
}
// PR15: real values, nested evaluation freshness, persisted design and crash recovery.
{
 const request={requestId:'TEST-PR15',revision:2,caller:{id:'CALLER',return_to:'INBOX',target_version:'TEST'},query:'Field',description:null,scope:{sources:['TEST-SOURCE'],permission_context:{}},filters:{}};
 const context={requestId:request.requestId,revision:2,scope:cloneFixtureData(request.scope),ruleVersion:'RULE-2',sources:{'TEST-SOURCE':'2'}};
 const evaluation={status:'green',reasons:['current'],missingInformation:[],requestRevision:2,ruleVersion:'RULE-2'};
 const response={requestId:request.requestId,revision:2,retrievalStatus:'success',candidates:[{id:'FIELD',name:'Field',metadata:{},sourceRef:'TEST-SOURCE',sourceVersion:'2',evaluation:cloneFixtureData(evaluation)}],evaluation,source:{ref:'TEST-SOURCE',version:'2'},scope:cloneFixtureData(request.scope),version:'2',mode:'example',retrievedAt:'2026-10-12T00:00:00Z'};
 const result={...cloneFixtureData(response),return_to:{caller:cloneFixtureData(request.caller),requestId:request.requestId,revision:2},conclusion:'found',reasons:[],missingInformation:[],ruleVersion:'RULE-2',generatedAt:'2026-10-12T00:00:01Z'};
 let cases=0;const map=x=>globalThis.tqtMapProductHandoff(R,'1.3','CALLER',{request,result:x},context);assert.equal(map(result).state,'PASS');assert.equal(map(result).payload.retrievalStatus,'success');cases++;
 for(const change of [x=>Object.keys(x).forEach(k=>x[k]=null),x=>x.conclusion='UNDEFINED',x=>x.generatedAt='yesterday',x=>x.generatedAt='2026-02-30T00:00:00Z',x=>x.candidates=[null],x=>x.revision='2',x=>x.requestId='OTHER',x=>x.revision=1,x=>x.return_to.caller.id='OTHER',x=>x.return_to.revision=1,x=>x.scope.sources=['OTHER'],x=>delete x.retrievedAt,x=>x.evaluation.requestRevision=1,x=>x.candidates[0].evaluation.requestRevision=1,x=>x.evaluation.ruleVersion='OLD',x=>x.candidates[0].evaluation.ruleVersion='OLD',x=>x.source.version='1',x=>x.candidates[0].sourceVersion='1',x=>x.conclusion='not_found']){const x=cloneFixtureData(result);change(x);assert.equal(map(x).state,'FAIL');cases++;}
 for(const change of [x=>x.evaluation.requestRevision=1,x=>x.candidates[0].evaluation.requestRevision=1,x=>x.evaluation.ruleVersion='OLD',x=>x.candidates[0].sourceVersion='1']){const x=cloneFixtureData(response);change(x);assert.equal(globalThis.tqtProductInputAudit(R,'1.3',{...request,incoming_response:x},context).state,'FAIL');cases++;}
 assert.equal(globalThis.tqtProductInputAudit(R,'1.3',{...request,incoming_response:response}).state,'FAIL');cases++;
 const cancelled={...cloneFixtureData(result),retrievalStatus:'cancelled',conclusion:'cancelled',candidates:[],evaluation:{...evaluation,status:'not_evaluated'}};assert.equal(map(cancelled).state,'PASS');cases++;
 console.log(JSON.stringify({pr15_product_boundaries:{cases,state:'PASS'}}));
}
{
 const os=require('os'),path=require('path'),cp=require('child_process'),tmp=fs.mkdtempSync(path.join(os.tmpdir(),'tqt-pr15-TEST-')),p=n=>path.join(tmp,n),write=(n,x)=>fs.writeFileSync(p(n),JSON.stringify(x)),read=n=>JSON.parse(fs.readFileSync(p(n),'utf8'));
 const call=(kind,mode,env={})=>{const x=cp.spawnSync(process.execPath,[...process.execArgv,__filename,process.argv[2]||__dirname+'/view.html',kind,mode,tmp],{encoding:'utf8',maxBuffer:4e6,env:{...process.env,...env}});return {status:x.status,result:x.stdout?JSON.parse(x.stdout):null};};
 let cases=0;try{
  writeHandoffTestContext(tmp);
  write('policy.json',{environment:'TEST',receiver:'P02',expected_output_version:'1',expected_state_revision:0,read_allowed:true,write_allowed:true});write('state.json',{revision:0,cancelled:false,received:null,effects:[]});assert.equal(call('--test-handoff','produce').result.state,'WRITTEN');
  assert.notEqual(call('--test-handoff','consume',{TQT_TEST_KILL_AFTER_LOCK:'1'}).status,0);assert.equal(read('state.json').effects.length,0);assert.equal(call('--test-handoff','consume').result.state,'ACK');cases++;
  write('state.json',{revision:0,cancelled:false,received:null,effects:[]});fs.unlinkSync(p('events.jsonl'));
  assert.equal(call('--test-handoff','consume',{TQT_TEST_LOG_FAILURE:'1'}).result.state,'BLOCKED');assert.equal(read('state.json').effects.length,1);assert(!fs.existsSync(p('events.jsonl')));assert.equal(call('--test-handoff','consume').result.replayed,true);assert.equal(read('state.json').effects.length,1);assert.equal(fs.readFileSync(p('events.jsonl'),'utf8').trim().split('\n').length,1);cases++;
  assert.equal(call('--test-design','produce').result.state,'WRITTEN');assert.equal(call('--test-design','consume').result.state,'ACK');const packet=read('design-packet.json'),original=read('P03.json');cases++;
  fs.renameSync(p('P03.json'),p('P03.saved'));assert.equal(call('--test-design','consume').result.state,'BLOCKED');fs.renameSync(p('P03.saved'),p('P03.json'));cases++;
  for(const change of [x=>x.mots=[],x=>x.output_version='OLD',x=>x.contract_binding.version='OLD',x=>x.mots[0].fields.pop(),x=>x.mots[1].states=[],x=>x.mots[2].branches=[],x=>x.mots[0].controls=[],x=>x.mots[0].fields[0].data_type='fake',x=>x.mots[0].open_items=['UNRESOLVED']]){
   const x=cloneFixtureData(original);change(x);write('P03.json',x);const forged=cloneFixtureData(packet);forged.outputs[1].artifact.sha256=globalThis.tqtSHA256(globalThis.tqtCanonical(x));write('design-packet.json',forged);assert.equal(call('--test-design','consume').result.state,'BLOCKED');cases++;}
  write('P03.json',original);write('design-packet.json',packet);const bad=cloneFixtureData(packet);bad.outputs[0].actor='NOT_ASSIGNED';write('design-packet.json',bad);assert.equal(call('--test-design','consume').result.state,'BLOCKED');cases++;
  write('design-packet.json',packet);assert.equal(call('--test-design','consume').result.state,'ACK');cases++;
  console.log(JSON.stringify({pr15_persisted_design_and_recovery:{cases,state:'PASS',read_plans:read('P04-receipt.json').reads.map(x=>x.plan_id),effects:read('state.json').effects.length,real_endpoint_permissions:'NOT_PROVED',mow001_progress:'TEST_DOES_NOT_ADVANCE_REAL_CHECKPOINTS'}}));
 }finally{fs.rmSync(tmp,{recursive:true,force:true});}
}

// PLAN stores the preparation snapshot. Execution status/result can advance without
// changing the plan definition (same rule as checkpoint dependency material).
// A historical fallback must match the exact stored hash AND current plan/version.
function preparationSnapshot(a,row){
 const current=row.requirement_code==='PLAN'?a.plan:a.preparation_review;
 if(tqtSHA256(tqtCanonical(current))===row.payload.sha256)return {source:'current'};
 if(row.requirement_code==='PLAN'){
  const material=plan=>plan.map(({status,result,...definition})=>definition);
  for(let i=a.history.length-1;i>=0;i--){const old=a.history[i].previous_evidence;
   if(old?.plan_version===a.plan_version&&Array.isArray(old.plan)&&tqtSHA256(tqtCanonical(old.plan))===row.payload.sha256&&tqtCanonical(material(old.plan))===tqtCanonical(material(a.plan)))return {source:'history/'+i+'/previous_evidence/plan',current_definition_matches:true,rule:'Only execution status/result may differ; all plan definition fields and version must match'};
  }
 }
 throw Error('STORED_RECORD_HASH_MISMATCH:'+row.requirement_code);
}

// P35 reusable real-packet reader, with invalid packets isolated in temporary TEST files.
function runPreparationReaderCases(){
 const path=require('path'),os=require('os'),cp=require('child_process'),dir=fs.mkdtempSync(path.join(os.tmpdir(),'TQT-P01-TEST-')),source=path.join(__dirname,'../mow-mot-moit-mout/UI-REVIEW-MOW001.json');let cases=0;
 try{for(const mutate of [null,p=>p.application_D24.preparation_review.answers.pop(),p=>p.application_D24.preparation_review.answers[0].answer_ref='fake:source/0',p=>p.application_D24.plan_results[0].data.answers[0].answer='wrong',p=>p.application_D24.trial_records=[],p=>p.application_D24.trial_records[0].payload.source_ref='fake:plan',p=>p.application_D24.preparation_review.question_matrix_sha256='0'.repeat(64),p=>p.application_D24.plan[1].actor='WRONG_ACTOR',p=>p.application_D24.plan_version='OLD',p=>p.application_D24.trial_records.find(x=>x.requirement_code==='PLAN').payload.sha256='0'.repeat(64)]){const f=path.join(dir,'packet.json');if(!mutate)fs.copyFileSync(source,f);else{
 // Create the complete mutated packet in a short-lived worker; release it before
 // the real reader loads both full source and packet. Never trim stored history.
 const code="const fs=require('fs'),p=JSON.parse(fs.readFileSync(process.argv[1],'utf8'));("+mutate.toString()+")(p);fs.writeFileSync(process.argv[2],JSON.stringify(p));";
 const made=cp.spawnSync(process.execPath,[...process.execArgv,'-e',code,source,f],{encoding:'utf8',timeout:120000,maxBuffer:2e6});assert.equal(made.status,0,'P01_FIXTURE_CREATION: '+made.stderr);
 }const res=cp.spawnSync(process.execPath,[...process.execArgv,__filename,process.argv[2]||__dirname+'/view.html','--read-preparation',f],{encoding:'utf8',timeout:120000,maxBuffer:2e6});assert.equal(res.status===0,!mutate,'P01_READER_BOUNDARY case='+cases+' status='+res.status+' signal='+res.signal+' stderr='+res.stderr.slice(-1500));cases++;}console.log(JSON.stringify({p35_preparation_reader:{cases,state:'PASS',scope:'TEST packets validate reader; real checkpoint requires authenticated persisted-source receipt'}}));}finally{fs.rmSync(dir,{recursive:true,force:true});}
}
// P36 TEST-only boundary cases. No fixture is persisted as MOW001 progress.
{
 const c=require('crypto'),r=fixture(),a=r.application_preview.record;let cases=0;
 const keys=c.generateKeyPairSync('ed25519'),publicKey=keys.publicKey.export({format:'der',type:'spki'}).subarray(-32).toString('base64');
 r.server_trust_policy={...R.server_trust_policy,policy_id:'TEST-P36',public_key_base64:publicKey,reviewer_id:'TEST-INDEPENDENT',reviewer_evidence_ref:'test-only:reviewer'};
 a.plan_results=a.plan_results.filter(x=>x.plan_id==='P01');for(const p of a.plan)if(p.id!=='P01')Object.assign(p,{status:'TODO',result:'NOT_TESTED'});
 for(const m of r.work_form.record_control.masters)m.source_state='UNVERIFIED';
 for(const d of a.record_requirements.filter(x=>x.checkpoint>='CP04'))Object.assign(a.record_checks.find(x=>x.requirement_code===d.code),{record_state:'NOT_RECORDED',check_state:'NOT_CHECKED',store_state:'TRIAL',master_record_id:null,record_ref:null,record_version:null,readback_state:'NOT_TESTED'});
 a.trial_records=[];a.checkpoint_checks=[];a.current_checkpoint='CP03';
 const input={document:{application_D24:a},previous:null,policy:r.server_trust_policy,principal:'TEST-WRITER',acl:{readers:['TEST-WRITER','TEST-READER'],writers:['TEST-WRITER']},source_sha256:'0'.repeat(64)};
 const ctx=tqtServerContext(r,input);for(const ep of a.trial_endpoints){const proof=ctx.endpoint_receipts.find(x=>x.requirement_code===ep.requirement_code);ep.access_check={state:'PASS',read:'PASS',write:'PASS',evidence_ref:proof.evidence_ref,spec_token:proof.spec_token};}
 for(const id of ['CP01','CP02','CP03']){const s=tqtRecordAudit(r,ctx).checkpointStates.find(x=>x.id===id);assert(s.eligible,'future outputs must not prevent '+id);a.checkpoint_checks.push({checkpoint:id,revision:1,application_id:a.application_id,process_code:a.process_code,process_version:a.process_version,target_code:a.target_code,target_version:a.target_version,result:'PASS',validity:'CURRENT',checked_by:'TEST',checked_at:new Date().toISOString(),evidence_ref:'test-only:p36',dependency_key:s.dependency_key});}
 assert.deepEqual(tqtRecordAudit(r,ctx).verifiedCheckpoints,['CP01','CP02','CP03']);cases++;
 assert(!tqtRecordAudit(r,{}).canStart);cases++;
 assert(!tqtRecordAudit(r,ctx).checkpointStates.find(x=>x.id==='CP04').eligible);cases++;
 const bad=cloneFixtureData(r);Object.assign(bad.application_preview.record.record_checks.find(x=>x.requirement_code==='RESULT-P02'),{record_state:'RECORDED',check_state:'MATCHED',record_ref:'fake',master_record_id:'fake',record_version:'1'});assert(tqtRecordAudit(bad,ctx).errors.some(x=>x.includes('RESULT-P02')));cases++;
 for(const mutate of [x=>x.principal='TEST-READER',x=>x.acl.writers=[],x=>x.policy.policy_id='OTHER',x=>x.document.application_D24.target_version='OTHER',x=>x.document.application_D24.trial_endpoints[0].selector='OTHER',x=>x.document.application_D24.trial_endpoints.pop(),x=>x.document.application_D24.trial_endpoints[0].key_fields=['FAKE'],x=>x.document.application_D24.trial_records=[{id:'BAD'}]]){const x=cloneFixtureData(input);mutate(x);assert.throws(()=>tqtServerContext(r,x));cases++;}
 const payload=JSON.stringify(ctx),receipt={algorithm:'Ed25519',key_id:'TEST-P36',payload,signature:c.sign(null,Buffer.from(payload),keys.privateKey).toString('base64')};a.server_receipt=receipt;assert(loadServerReceipt(r));cases++;
 for(const mutate of [x=>x.application_preview.record.server_receipt.payload+=' ',x=>x.application_preview.record.server_receipt.key_id='OTHER',x=>x.application_preview.record.plan_version='OTHER',x=>x.server_trust_policy.public_key_base64=Buffer.alloc(32).toString('base64')]){const x=cloneFixtureData(r);mutate(x);assert.throws(()=>loadServerReceipt(x));cases++;}
 // Changing the ACL changes the receipt reference even if a previous signature remains historical evidence.
 const changed=cloneFixtureData(input);changed.acl.readers.push('TEST-NEW');assert.notEqual(tqtServerContext(r,changed).endpoint_receipts[0].evidence_ref,ctx.endpoint_receipts[0].evidence_ref);cases++;
 // A read of old bytes never certifies changed after-image artifact bytes.
 const designed=fixture(),da=designed.application_preview.record;designed.server_trust_policy={...r.server_trust_policy,application_id:da.application_id,target_version:da.target_version};da.design_artifacts={};for(const result of da.plan_results.filter(x=>['P02','P03'].includes(x.plan_id))){const artifact=designFixture(designed,result);da.design_artifacts[result.plan_id]=artifact;result.artifact={path:designed.application_preview.source_ref+'/design_artifacts/'+result.plan_id,sha256:tqtSHA256(tqtCanonical(artifact))};}
 const di={...cloneFixtureData(input),policy:designed.server_trust_policy,document:{application_D24:da},previous:{application_D24:cloneFixtureData(da)},previous_sha256:'1'.repeat(64)};const good=tqtServerContext(designed,di);assert.equal(good.design_reads.length,2);assert(good.design_reads.every(x=>x.source_sha256===di.previous_sha256));cases++;
 di.document.application_D24.design_artifacts.P02.mots=[];const changedDesign=tqtServerContext(designed,di);assert(!changedDesign.design_reads.some(x=>JSON.parse(x.payload_token).plan_id==='P02'));cases++;
 console.log(JSON.stringify({p36_server_evidence:{cases,state:'PASS',future_output_before_start:'NOT_REQUIRED',production_progress:'NOT_CHANGED_BY_TEST',pg:'NOT_RUN'}}));
}

assert.equal(sourceHistoryFingerprint(),fullSourceHistoryFingerprint,'TEST_MUTATED_FULL_SOURCE_HISTORY');
