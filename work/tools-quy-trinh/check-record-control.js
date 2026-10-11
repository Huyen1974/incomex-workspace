/* Tests the same design projection as Overview. No PostgreSQL writes. */
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync(process.argv[2]||__dirname+'/view.html','utf8');
const script=id=>{const m=html.match(new RegExp('<script id="'+id+'"[^>]*>([\\s\\S]*?)</script>'));assert(m,id);return m[1];};
const R=JSON.parse(script('tqt-composite-processes')).catalog;
vm.runInThisContext(script('tqt-record-control'));
const audit=globalThis.tqtRecordAudit,clone=x=>JSON.parse(JSON.stringify(x));let tests=0;
if(process.argv.includes('--complete-fixture')){fs.writeFileSync(1,JSON.stringify(fixture()));process.exit(0);}
if(process.argv.includes('--audit')){const r=JSON.parse(fs.readFileSync(0,'utf8'));const a=audit(r);fs.writeFileSync(1,JSON.stringify({errors:a.errors,counts:a.counts,verifiedCheckpoints:a.verifiedCheckpoints,canStart:a.canStart,canFinish:a.canFinish}));process.exit(0);}

if(process.argv.includes('--validate-transition')){
 const i=process.argv.indexOf('--validate-transition');
 try{const before=JSON.parse(fs.readFileSync(process.argv[i+1],'utf8')).application_D24,after=JSON.parse(fs.readFileSync(process.argv[i+2],'utf8')).application_D24;const result=globalThis.tqtValidateTransition(before,after);fs.writeFileSync(1,JSON.stringify(result));process.exit(result.state==='PASS'?0:1);}catch(e){fs.writeFileSync(1,JSON.stringify({state:'FAIL',errors:[e.message]}));process.exit(1);}
}
const check=(r,id)=>r.application_preview.record.record_checks.find(x=>x.requirement_code===id),row=(a,id)=>a.rows.find(x=>x.code===id);
function unrecorded(r){delete r.trial_storage_contract;delete r.application_preview.record.trial_store;for(const x of r.application_preview.record.record_checks)if(x.store_state==='TRIAL')Object.assign(x,{store_state:'UNVERIFIED',record_state:'NOT_RECORDED',check_state:'NOT_CHECKED',master_record_id:null,record_ref:null,record_version:null});return r;}
function test(name,change,verify){const r=unrecorded(clone(R));change(r);try{verify(audit(r),r);}catch(e){throw Error(name+': '+e.message);}tests++;}
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
test('duplicate check rejected',r=>r.application_preview.record.record_checks.push(clone(check(r,'PLAN'))),a=>assert(a.errors.length));
test('written without key rejected',r=>check(r,'PLAN').record_state='RECORDED',a=>{assert(!row(a,'PLAN').written);assert(a.errors.length);});
test('written independent of comparison',written,a=>{assert(row(a,'PLAN').written);assert(!row(a,'PLAN').verified);assert.equal(row(a,'PLAN').checkState,'NOT_CHECKED');});
test('matched with evidence',matched,a=>assert(row(a,'PLAN').verified));
for(const key of ['master_record_id','record_ref','record_version','evidence_ref','checked_by','checked_at'])test('missing '+key,r=>{matched(r);check(r,'PLAN')[key]=null;},a=>{assert(!row(a,'PLAN').verified);assert.equal(row(a,'PLAN').checkState,'NEEDS_FIX');});
test('repair does not erase recording',r=>{matched(r);check(r,'PLAN').check_state='NEEDS_FIX';},a=>{assert(row(a,'PLAN').written);assert(!row(a,'PLAN').verified);});
test('future output not due',r=>{},a=>assert(!row(a,'RESULT-P03').due));
test('output becomes due',r=>r.application_preview.record.current_checkpoint='CP04',a=>assert(row(a,'RESULT-P03').due));
test('new output needs declaration',r=>r.application_preview.record.plan.push({id:'P06'}),a=>assert(a.errors.some(x=>x.includes('P06'))));
test('field cannot be omitted',r=>r.application_preview.record.record_requirements=r.application_preview.record.record_requirements.filter(x=>x.code!=='FIELD-identity'),a=>assert(a.errors.some(x=>x.includes('identity'))));
test('foreign check rejected',r=>{const c=clone(check(r,'PLAN'));c.requirement_code='UNKNOWN';r.application_preview.record.record_checks.push(c);},a=>assert(a.errors.length));
test('wrong option rejected',r=>check(r,'PLAN').check_state='GREEN',a=>assert(a.errors.length));
test('cannot jump to last checkpoint',r=>r.application_preview.record.checkpoint_checks=[{checkpoint:'CP07',application_id:r.application_preview.record.application_id,process_version:r.application_preview.record.process_version,target_version:r.application_preview.record.target_version,result:'PASS',validity:'CURRENT',evidence_ref:'test-only'}],a=>assert.equal(a.verifiedCheckpoints.length,0));
assert.deepEqual(R.work_form.record_control.state_options.check_state.map(x=>x.label),['Chưa đối chiếu','Đã đối chiếu','Cần sửa lại']);
assert.deepEqual(R.work_form.record_control.state_options.record_state.map(x=>x.label),['Chưa ghi','Đã ghi']);
for(const m of html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g))if(!/application\/json/.test(m[1])&&m[2].trim())new vm.Script(m[2]);
console.log(JSON.stringify({tests,scope:'DESIGN_PROJECTION_ONLY',counts:audit(R).counts,pg:'NOT_RUN'}));
// Regression walk: complete synthetic evidence, then break one boundary at a time.
function fixture(){
 const r=unrecorded(clone(R)),a=r.application_preview.record;a.current_checkpoint='CP07';
 for(const m of r.work_form.record_control.masters)m.source_state='VERIFIED';
 for(const x of a.record_checks)Object.assign(x,{record_state:'RECORDED',check_state:'MATCHED',master_record_id:'SIM-'+x.requirement_code,record_ref:'test-only:'+x.requirement_code,record_version:'1',checked_record_version:'1',readback_state:'PASS',access_state:'PASS',process_code:a.process_code,process_version:a.process_version,target_code:a.target_code,evidence_ref:'test-only:readback',checked_by:'TEST',checked_at:'2026-10-11T00:00:00Z'});
 a.questions_complete=true;a.requirements_checked=true;
 for(const x of a.declarations)Object.assign(x,{result:'PASS',validity:'CURRENT',evidence_refs:['test-only:declaration']});
 Object.assign(a.preparation_review,{output_contracts_reviewed:true,branches_reviewed:true,evidence_ref:'test-only:coverage'});
 Object.assign(a.start_confirmation,{state:'CONFIRMED',evidence_ref:'test-only:start'});
 const payload={application_id:a.application_id,target_version:a.target_version,evidence_ref:'test-only:payload',actor:'TEST',at:'2026-10-11T00:00:00Z'};
 a.plan_results=a.plan.map(p=>{p.status='DONE';return {...payload,id:'SIM-'+p.id,plan_id:p.id,output_ref:'test-only:output',output_version:'1'};});
 a.contract_binding=globalThis.tqtContractPin(a);
 a.information_contract.review={state:'PASS',reviewer_id:'TEST-INDEPENDENT',evidence_ref:'test-only:independent',at:'2026-10-11T00:00:00Z',contract_binding:a.contract_binding};
 a.start_confirmation.contract_binding=a.contract_binding;
 for(const x of a.plan_results)x.contract_binding=a.contract_binding;
 const canonical=v=>JSON.stringify(v,(_,x)=>x&&typeof x==='object'&&!Array.isArray(x)?Object.fromEntries(Object.keys(x).sort().map(k=>[k,x[k]])):x);
 for(const ep of a.trial_endpoints){const {access_check,...spec}=ep;ep.access_check={state:'PASS',read:'PASS',write:'PASS',evidence_ref:'test-only:endpoint',spec_token:canonical(spec)};}
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
function mutation(name,change,verify){const r=clone(complete);change(r);try{verify(audit(r),r);}catch(e){throw Error(name+': '+e.message);}tests++;}
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
mutation('duplicate checkpoint revision rejected',r=>r.application_preview.record.checkpoint_checks.push(clone(r.application_preview.record.checkpoint_checks[0])),a=>assert.equal(a.verifiedCheckpoints.length,0));
console.log(JSON.stringify({tests,regression:'QTTH05_WALK',synthetic_full_walk:7,live_application:audit(R).verifiedCheckpoints.length,pg:'NOT_RUN'}));

// Real persisted trial declarations: existence/readback are separate from semantic approval.
const baseTrial=audit(R);assert.equal(baseTrial.counts.written,13);assert.equal(baseTrial.verifiedCheckpoints.length,0);assert(!baseTrial.canStart);
let trialCases=1;
for(const mutate of [
 r=>r.application_preview.record.declarations.shift(),
 r=>r.application_preview.record.declarations.push(clone(r.application_preview.record.declarations[0])),
 r=>r.application_preview.record.declarations[0].schema_version='2.0',
 r=>r.application_preview.record.declarations[0].record_version='2',
 r=>r.application_preview.record.declarations[0].surprise='unregistered column',
 r=>r.application_preview.record.trial_store.source_ref='another file',
 r=>delete r.application_preview.record.trial_store,
 r=>check(r,'FIELD-identity').store_state='UNVERIFIED',
 r=>r.application_preview.record.trial_store.production=true,
 r=>r.application_preview.record.scope_stage='G2',
 r=>check(r,'FIELD-identity').record_ref='fake:row',
 r=>check(r,'FIELD-identity').master_record_id='another row'
]){const r=clone(R);mutate(r);assert(!row(audit(r),'FIELD-identity').written);trialCases++;}
const readTrial=clone(R),ar=readTrial.application_preview.record,dr=ar.declarations[0],xr=check(readTrial,'FIELD-identity');
Object.assign(xr,{check_state:'MATCHED',readback_state:'PASS',process_code:ar.process_code,process_version:ar.process_version,target_code:ar.target_code,checked_record_version:dr.record_version,evidence_ref:'test-only:readback',checked_by:'TEST',checked_at:'2026-10-11T00:00:00Z',checked_payload_token:JSON.stringify(dr, Object.keys(dr).sort())});
assert(row(audit(readTrial),'FIELD-identity').verified);trialCases++;
dr.answer+=' changed';assert(!row(audit(readTrial),'FIELD-identity').verified);trialCases++;
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
 ['new contract version',r=>r.application_preview.record.information_contract.version='2'],
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
]){const r=clone(complete);change(r);assert(!audit(r).canFinish,name);contractCases++;}
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
]){const r=clone(R);mutate(r);const x=audit(r);assert(!x.canStart&&!x.canFinish);assert(x.errors.length||!x.contract.reviewed);contractCases++;}
const previous=clone(R.application_preview.record),validate=globalThis.tqtValidateTransition;
assert.equal(validate(previous,clone(previous)).state,'PASS');contractCases++;
for(const change of [
 a=>a.declarations[0].answer+=' changed without revision',
 a=>a.declarations[0].record_version='2',
 a=>a.declaration_history.push({...a.declarations[0],answer:'fabricated'}),
 a=>a.declarations.pop(),
 a=>a.information_contract.rows[0].meaning='changed',
 a=>a.information_contract.history.push({fake:true})
]){const after=clone(previous);change(after);assert.equal(validate(previous,after).state,'FAIL');contractCases++;}
const next=clone(previous);next.declaration_history.push(clone(previous.declarations[0]));next.declarations[0].answer+=' changed';next.declarations[0].record_version='2';
assert.equal(validate(previous,next).state,'PASS');contractCases++;
const rewrite=clone(next);rewrite.declaration_history[0].answer='rewrite old';assert.equal(validate(next,rewrite).state,'FAIL');contractCases++;
const newContract=clone(previous),prior=clone(previous.information_contract);delete prior.history;newContract.information_contract.history.push(prior);newContract.information_contract.version='2';newContract.information_contract.rows.forEach(x=>x.contract_version='2');
assert.equal(validate(previous,newContract).state,'PASS');contractCases++;
const changed=clone(complete);changed.application_preview.record.information_contract.rows[0].meaning+=' revised';assert.deepEqual(audit(changed).verifiedCheckpoints,['CP01']);contractCases++;
console.log(JSON.stringify({information_contract_cases:contractCases,actual_contract_rows:R.application_preview.record.information_contract.rows.length,actual_criteria:R.application_preview.record.information_contract.criteria.length,synthetic_full_walk:audit(complete).verifiedCheckpoints.length,real_checkpoints:audit(R).verifiedCheckpoints.length,server_write_hook:'NOT_ENFORCED',pg:'NOT_RUN'}));
