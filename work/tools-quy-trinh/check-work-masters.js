const fs=require('fs'),vm=require('vm'),assert=require('assert');
let html=fs.readFileSync(process.argv[2]||__dirname+'/view.html','utf8');
const r=JSON.parse(html.match(/<script id="tqt-composite-processes"[^>]*>([\s\S]*?)<\/script>/)[1]).catalog;
const engineCode=Buffer.from(html.match(/<script id="tqt-record-control"[^>]*>([\s\S]*?)<\/script>/)[1]).toString();
html=null;/release/.test('release'); // Release large HTML/RegExp input; all real records/history remain intact.
// Fixture mutations never edit execution-history entries. Share their full read-only
// source instead of repeatedly serializing historical evidence; current records and
// checkpoint entries are read-only; replacing an array stays local to the fixture.
// Fingerprints before each fixture and after the suite catch unintended source edits.
function historyFingerprint(a){const h=require('crypto').createHash('sha256');for(const key of ['history','checkpoint_checks']){h.update(key);for(const row of a[key]||[])h.update(JSON.stringify(row)).update('\n');}return h.digest('hex');}
const sourceHistoryFingerprint=historyFingerprint(r.application_preview.record);
function cloneFixture(x){
 assert.equal(historyFingerprint(r.application_preview.record),sourceHistoryFingerprint,'FIXTURE_MUTATED_SOURCE_HISTORY');
 if(!x?.application_preview?.record)return JSON.parse(JSON.stringify(x));
 const a=x.application_preview.record,out=JSON.parse(JSON.stringify({...x,application_preview:{...x.application_preview,record:{...a,history:[],checkpoint_checks:[]}}}));
 out.application_preview.record.history=a.history;out.application_preview.record.checkpoint_checks=a.checkpoint_checks;assert.equal(historyFingerprint(r.application_preview.record),sourceHistoryFingerprint,'FIXTURE_MUTATED_SOURCE_HISTORY');return out;
}
const adapter=process.argv[3];if(adapter)vm.runInThisContext(fs.readFileSync(adapter,'utf8'));
function validate(r){
 const s=r.work_schedule, defs=r.work_master_designs.records, by=new Map(s.records.map(x=>[x.record_id,x]));
 assert.equal(s.master_code,'CAT-227*');assert.equal(by.size,s.records.length);assert.equal(new Set(s.records.map(x=>x.order)).size,s.records.length);
 assert.equal(new Set(defs.map(x=>x.code)).size,defs.length);
 for(const d of defs){assert(r.work_form.record_control.masters.some(m=>m.code===d.code&&m.name===d.name));assert.equal(d.parent,'UI.MASTER');assert.equal(d.state,'DESIGN_ONLY');assert(new Set(d.fields.map(f=>f.key)).size===d.fields.length);for(const col of d.columns)assert(d.fields.some(f=>f.key===col.key));}
 const visiting=new Set(),done=new Set();function visit(id){assert(by.has(id),'missing dependency');assert(!visiting.has(id),'cycle');if(done.has(id))return;visiting.add(id);for(const dep of by.get(id).depends_on)visit(dep);visiting.delete(id);done.add(id);}for(const id of by.keys())visit(id);
 assert.equal(s.display_code,'DEF 00.1');assert.equal(s.display_order,0.1);assert.equal(s.master_identity.key,s.master_code);
 for(const x of s.records){assert(['T0','T0.5','T1','T2','T3'].includes(x.target_tier));assert(s.lifecycle.states[x.lifecycle_state]);for(const k of ['actual_start','actual_finish','planned_start','planned_finish']){assert(x[k]===null||/^\d{4}-\d{2}-\d{2}(T.*)?$/.test(x[k]));}assert(!x.actual_finish||x.actual_start&&x.actual_finish>=x.actual_start);}
 const a=r.application_preview.record;
 for(const x of s.records){assert(x.record_id&&x.process_code==='MOW-TH-005'&&x.process_version===r.records.find(p=>p.code===x.process_code).version);if(x.application_id){assert(x.application_id===a.application_id&&x.target_code===a.target_code&&x.target_version===a.target_version);assert(x.application_ref===r.application_preview.source_ref);assert(x.application_refs.includes(x.application_id));assert.equal(x.state_source,'catalog.application_preview.record');}else{assert(!x.application_ref);assert(!x.completion_evidence);}}
 return true;
}
validate(r);let rejected=0;
for(const change of [x=>x.work_schedule.records.push(x.work_schedule.records[0]),x=>x.work_schedule.records[1].order=1,x=>x.work_schedule.records[0].depends_on=['TQT-VIEC-002'],x=>x.work_schedule.records[1].depends_on=['UNKNOWN'],x=>x.work_schedule.records[0].application_id='OTHER',x=>x.work_schedule.records[0].target_version='OLD',x=>x.work_schedule.records[0].application_ref='OTHER',x=>x.work_master_designs.records[0].code='MISSING',x=>x.work_master_designs.records[0].columns.push({key:'unknown'}),x=>x.work_schedule.records[1].completion_evidence='FAKE',x=>x.work_schedule.records[0].target_tier='CTCM',x=>x.work_schedule.records[0].lifecycle_state='UNKNOWN',x=>x.work_schedule.records[0].actual_finish='2026-01-01',x=>x.work_schedule.display_code='DEF001']){const c=cloneFixture(r);change(c);assert.throws(()=>validate(c));rejected++;}
if(adapter){const A=globalThis.TQT_WORK_MASTER;r.source_url='https://example.test/view.html';const list=A.scheduleRows(r);assert.equal(list.length,2);assert(list[0].dossier_url.endsWith('#tqt-recording-list'));assert.equal(list[1].dossier_url,null);assert.equal(list[1].state,'Ghi danh');for(const d of r.work_master_designs.records){const cfg=A.configure({}, {tqt:r,masterCode:d.code,sample:false});assert.equal(cfg.mother,'DEF');assert(cfg.definitionColumns.length);const sample=A.configure({}, {tqt:r,masterCode:d.code,sample:true});assert.equal(sample.items.length,1);assert(sample.items[0].form_schema.fields.length);assert(sample.items[0].code.startsWith('MAU-'));}assert.equal(A.indexRows(r).length,r.work_master_designs.records.length);
 assert.equal(A.indexRows(r)[0].code,'DEF 00.1');assert.equal(A.indexRows(r)[0].humanNo,'0.1');
 assert.deepEqual(A.summary(list),{total:2,unfinished:2,done:0,blocked:1,closed:0});
 assert.deepEqual(A.summary([]),{total:0,unfinished:0,done:0,blocked:0,closed:0});
 assert.equal(A.definition(r,'DEF00.1').code,'CAT-227*');
 const bad=cloneFixture(r);bad.work_schedule.records[0].target_version='wrong';assert.throws(()=>A.scheduleRows(bad));
 const fake=cloneFixture(r);fake.application_preview.record.state='XONG';assert.equal(A.scheduleRows(fake)[0].done,false);
 const cfg=A.configure({}, {tqt:r,masterCode:'DEF00.1',sample:false});assert.equal(cfg.filterFields.length,4);assert(cfg.statusOptions.includes('Đã cho nghỉ'));assert.equal(cfg.items[0].metadata.actual_start,r.work_schedule.records[0].actual_start||r.application_preview.record.execution_walk?.started_at?.slice(0,10)||'Chưa ghi');assert.equal(cfg.items[1].metadata.actual_start,'Chưa ghi');
}
console.log(JSON.stringify({masters:r.work_master_designs.records.length,planned_jobs:r.work_schedule.records.length,negative_cases:rejected,scope:'DESIGN_ONLY',pg:'NOT_RUN'}));

if(adapter){
 vm.runInThisContext(engineCode);
 const A=globalThis.TQT_WORK_MASTER,copy=cloneFixture,d=A.dossier(r,r.work_schedule.records[0]);
 assert.equal(d.checkpoints.length,7);assert.equal(d.groups.length,11);assert.equal(d.groups.reduce((n,g)=>n+g.rows.length,0),34);
 assert.equal(d.checkpoints.filter(x=>x.current)[0].id,d.a.current_checkpoint);assert.equal(d.checkpoints.filter(x=>x.done).length,d.audit.verifiedCheckpoints.length);assert.equal(d.done,d.groups.filter(x=>x.done).length);
 const waiting=A.dossier(r,r.work_schedule.records[1]);assert.equal(waiting.a,null);assert(waiting.groups.every(g=>!g.done&&g.condition==='Chưa gắn hồ sơ'));assert(waiting.checkpoints.every(x=>!x.done&&!x.current));
 {const partial=copy(r),recordedPlan=copy(partial.application_preview.record.record_checks.find(x=>x.requirement_code==='PLAN'));
 const storedPlan=partial.application_preview.record.trial_records.find(x=>x.requirement_code==='PLAN');assert(storedPlan,'PLAN fixture needs its stored row');assert.equal(recordedPlan.master_record_id,storedPlan.id);assert.equal(recordedPlan.record_version,storedPlan.record_version);assert.equal(recordedPlan.checked_payload_token,tqtCanonical(storedPlan));
 for(const x of partial.application_preview.record.record_checks.filter(x=>['PLAN','RESULT-P01','RESULT-P02','RESULT-P03','RESULT-P04','RESULT-P05','BLOCKED'].includes(x.requirement_code)))Object.assign(x,{record_state:'NOT_RECORDED',check_state:'NOT_CHECKED',readback_state:'NOT_TESTED'});const p=partial.application_preview.record.record_checks.find(x=>x.requirement_code==='PLAN');
 // Keep the real stored identity/version/token; change only this fixture's verification state.
 Object.assign(p,recordedPlan,{record_state:'RECORDED',check_state:'NOT_CHECKED',readback_state:'NOT_TESTED'});
 const g=A.dossier(partial,partial.work_schedule.records[0]).groups.find(g=>g.id==='RG04');assert.equal(g.written,1);assert(!g.done);assert(g.active.length>1);
 Object.assign(p,recordedPlan,{readback_state:'PASS',check_state:'MATCHED'});
 assert.equal(A.dossier(partial,partial.work_schedule.records[0]).groups.find(g=>g.id==='RG04').verified,1);
 p.application_id='WRONG';assert.equal(A.dossier(partial,partial.work_schedule.records[0]).groups.find(g=>g.id==='RG04').verified,0);}
 {const foreign=copy(r);foreign.work_schedule.records[0].process_version='WRONG';assert.throws(()=>A.dossier(foreign,foreign.work_schedule.records[0]));}
 {const unlinked=copy(r);unlinked.work_schedule.records[0].application_id='MISSING';assert.throws(()=>A.dossier(unlinked,unlinked.work_schedule.records[0]));}
 {const second=copy(r),other=cloneFixture(second).application_preview.record;other.application_id='TEST-SECOND';other.target_code='TEST-TARGET';other.record_checks=[];second.work_schedule.applications=[other];Object.assign(second.work_schedule.records[1],{application_id:other.application_id,target_code:other.target_code,target_version:other.target_version});
 const distinct=A.dossier(second,second.work_schedule.records[1]);assert.equal(distinct.a.application_id,'TEST-SECOND');assert.equal(distinct.written,0);assert.equal(distinct.done,0);assert(distinct.audit.errors.length);}
 const cfg=A.configure({}, {tqt:r,masterCode:'DEF00.1',sample:false});const view=cfg.detailRenderer(cfg,cfg.items[0]);assert(view.fullWidth&&view.interactive);assert.equal((view.html.match(/type="checkbox"/g)||[]).length,18);assert.equal((view.html.match(/type="checkbox" disabled/g)||[]).length,18);assert.equal((view.html.match(/ checked /g)||[]).length,d.checkpoints.filter(x=>x.done).length+d.groups.filter(x=>x.done).length); // UI must follow actual evidence, not a frozen empty fixture.
 console.log('dossier: 7 checkpoints, 11 groups, 34 obligations; partial/foreign/unlinked/second job cases passed');
}

const coverage=r.work_master_designs.coverage, all=new Set([...r.work_master_designs.records.map(x=>x.code),'ML-DEF-004','ML-DEF-005','ML-DEF-013']);
assert.equal(coverage.rows.length,9);assert.equal(coverage.new_ui_codes.length,8);
for(const row of coverage.rows)for(const code of row.masters)assert(all.has(code),'Unresolved Master '+code);
for(const code of coverage.new_ui_codes){const d=r.work_master_designs.records.find(x=>x.code===code);assert(d);assert(d.fields.length>=12);assert(d.pg_design.primary_key);assert(d.pg_design.natural_key);assert.equal(d.pg_design.status,'LOGICAL_DESIGN_ONLY');}
assert.equal(r.work_form.record_control.guidance.length,11);
console.log('coverage: 7 checkpoints + exception/operations; 8 new UI references resolved; 11 groups preserved');

if(adapter){const rows=globalThis.TQT_WORK_MASTER.sourceRows(r,'CAT-206*');assert.equal(rows.length,r.application_preview.record.information_contract.rows.length);assert(rows.every(x=>x.meaning&&x.contract_version&&x.acceptance_refs.length));const cfg=globalThis.TQT_WORK_MASTER.configure({}, {tqt:r,masterCode:'CAT-206*',sample:false});assert.equal(cfg.items.length,rows.length);assert(cfg.items[0].form_schema.fields.some(x=>x.key==='meaning'));const detail=cfg.detailRenderer(cfg,cfg.items[0]);assert(detail.html.includes(rows[0].meaning));assert(detail.html.includes('Mã hợp đồng'));assert(detail.html.includes('Số lượng'));assert(detail.html.includes(rows[0].contract_id));console.log('CAT206 applied contracts visible; field meaning/version/case links preserved');}

// P30: test the actual merged list, including the former DOT duplicate.
if(adapter&&process.argv[4]){
 const path=require('path'),registryText=fs.readFileSync(process.argv[4],'utf8'),registry=JSON.parse(registryText.match(/DEFINITION_MASTER_REGISTRY=(\[.*?\]);/s)[1]);
 const A=globalThis.TQT_WORK_MASTER,copy=cloneFixture;
 const primary=registry.map(x=>({...x,code:x.masterId,name:x.masterName,definitionValues:['—','','','','','','']}));
 const extra=[{code:'CAT-248*',name:'Master Config',url:'./config-master-v1.html',definitionValues:[]}].concat(A.indexRows(r));
 const joined=A.reconcileIndex(r,primary,extra),dot=joined.filter(x=>x.code==='ML-DEF-024');
 assert.equal(joined.length,47);assert.equal(dot.length,1);assert.equal(dot[0].name,'Master DOT');assert.equal(dot[0].definitionValues[0],6+(r.tool_registry.audit_projection?.dot_inventory.length||0)+(r.tool_registry.audit_projection?.script_inventory?.length||0));assert.deepEqual(dot[0].aliases,['CAT-006']);assert.equal(dot[0].url,'./definition-master-v1.html?stt=24');
 assert.deepEqual(A.sourceRows(r,'CAT-006'),A.sourceRows(r,'ML-DEF-024'));assert.equal(A.definition(r,'ML-DEF-024').code,'CAT-006');
 const original=copy(r);original.master_identity.bindings=[];assert.throws(()=>A.reconcileIndex(original,primary,extra),/POSSIBLE_DUPLICATE_MASTER/);
 for(const item of [{code:'NEW',name:'Danh mục DOT'},{code:'NEW',name:'Different name',source_key:'catalog.tool_registry'},{code:'NEW',name:'Different name',entity_key:'DOT'},{code:'NEW',name:'Different name',url:dot[0].url},primary[0]])assert.throws(()=>A.reconcileIndex(r,primary,[...extra,item]));
 const amb=copy(r);amb.master_identity.bindings.push(copy(amb.master_identity.bindings[0]));assert.throws(()=>A.reconcileIndex(amb,primary,extra),/AMBIGUOUS_ALIAS/);
 assert.throws(()=>A.reconcileIndex(r,primary.filter(x=>x.code!=='ML-DEF-024'),extra),/CANONICAL_MASTER_MISSING/);
 assert.notEqual(A.identityName('Master View'),A.identityName('Master List View'));
 // Exercise production list composition, not a test-only reconstruction.
 const sandbox={window:{addEventListener(){},UI_CHILD_CONTEXT:{type:'DEFMASTER_INDEX',tqt:copy(r)},MASTER_CONFIG:{},DEFINITION_MASTER_REGISTRY:registry,DEFINITION_MASTER_DATA:{},TQT_WORK_MASTER:A,MMIM_CHAINS:{reviewDefaultId:'TEST'},CONFIG_MASTER_SCHEMA:{columns:[]},CONFIG_MASTER_DATA:[]},document:{addEventListener(){},querySelectorAll(){return []},getElementById(){return null}},console};
 vm.runInNewContext(fs.readFileSync(path.join(path.dirname(adapter),'ui-child-content-v1.js'),'utf8'),sandbox);sandbox.window.configureChildMaster();assert.equal(sandbox.window.MASTER_CONFIG.items.length,47);
 sandbox.window.UI_CHILD_CONTEXT.tqt.master_identity.bindings=[];sandbox.window.configureChildMaster();assert.equal(sandbox.window.MASTER_CONFIG.items.length,0);assert(sandbox.window.MASTER_CONFIG.sub.includes('POSSIBLE_DUPLICATE_MASTER'));
 // Legacy URL keeps detail/sample parameters and redirects to the existing Master.
 let redirected='';vm.runInNewContext(fs.readFileSync(path.join(path.dirname(adapter),'ui-child-from-parent-v1.js'),'utf8'),{URL,URLSearchParams,location:{pathname:'/ui/process-work-master-v1.html',search:'?master=CAT-006&mau=1&chi-tiet=TEST',href:'https://example.test/ui/process-work-master-v1.html?master=CAT-006&mau=1&chi-tiet=TEST',replace:u=>redirected=u}});const url=new URL(redirected);assert.equal(url.searchParams.get('stt'),'24');assert.equal(url.searchParams.get('chi-tiet'),'TEST');assert.equal(url.searchParams.get('mau'),'1');assert(!url.searchParams.has('master'));
 console.log('P30 merged-index guard: 48 inputs -> 47 Masters, one DOT/6 tools, duplicate cases rejected, real UI fails closed, old URL preserved');
}

if(adapter){const A=globalThis.TQT_WORK_MASTER;const rows=A.toolRows(r);assert.equal(new Set(rows.map(x=>x.record_id)).size,rows.length);assert(rows.filter(x=>x.id.startsWith('DOT.')).every(x=>x.state==='Đã tìm thấy · chưa kiểm chạy'));assert(rows.find(x=>x.id==='TQT-CHECK-004').state.includes('1 tệp'));const matrix=A.reuseMatrix(r);assert(matrix.some(x=>!x.tools.length));assert(matrix.some(x=>x.tool_ids.includes('jev-reference:evaluate')));const bad=cloneFixture(r);bad.tool_registry.reuse_needs[0].tool_ids=['UNKNOWN'];assert.throws(()=>A.reuseMatrix(bad));const cfg=A.configureTools({}, {tqt:r},{masterId:'ML-DEF-023',masterName:'Master Tool'},[{id:'TOOL-TEST',name:'Test legacy'}]);assert.equal(cfg.items.length,1+r.tool_registry.provider_tools.length);assert(cfg.items.some(x=>x.code==='jev-reference:evaluate'));assert(cfg.detailRenderer(cfg,cfg.items[1]).html.includes('Bằng chứng'));console.log('P33 inventory/proof states, provider reuse, missing coverage and detail validated');}

if(adapter){const old=cloneFixture(r);old.tool_registry.records[0].sha256='0'.repeat(64);assert(globalThis.TQT_WORK_MASTER.toolRows(old)[0].state.includes('phiên trước'));console.log('P33 stale tool source is not shown as current TEST proof');}

// P34: lifecycle and consensus are distinct from TEST results and inventory.
if(adapter){
 const A=globalThis.TQT_WORK_MASTER,copy=cloneFixture,id=r.tool_registry.records[0].id;
 const fixture=()=>{const q=copy(r),tool=q.tool_registry.records[0];q.tool_registry.audit_projection.last_checks=[{id,sha256:tool.sha256,exit_code:0,evidence_ref:'TEST:receipt',job_id:'TEST-RUN'}];q.tool_registry.reviews=[];delete q.tool_registry.lifecycle_policy.owner_execution_exception;return q;};
 const row=q=>A.toolRows(q).find(x=>x.record_id===id);
 const sign=(q,vendor)=>{const x=row(q),m=q.tool_registry.memory.find(x=>x.tool_id===id);q.tool_registry.reviews.push({review_id:'TEST-'+vendor,target_code:id,vendor,reviewer:vendor+' TEST reviewer',reviewed_at:'2026-10-12T00:00:00Z',binding:x.binding,scope:m.acceptance_scope,evidence_ref:'TEST:platform-receipt',authority_ref:'TEST:verified-identity',receipt_verified:true,decision:'APPROVE'});};
 let q=fixture();assert.equal(row(q).lifecycle_code,'TESTED');sign(q,'OpenAI');assert.equal(row(q).lifecycle_code,'TESTED');sign(q,'Anthropic');assert.equal(row(q).lifecycle_code,'USABLE');
 for(const change of [x=>x.tool_registry.records[0].preconditions='changed contract without revision bump',x=>x.tool_registry.records[0].sha256='0'.repeat(64),x=>x.tool_registry.memory[0].contract_revision='NEXT',x=>x.tool_registry.memory[0].acceptance_scope='different scope',x=>x.tool_registry.reviews[1].scope='different scope',x=>x.tool_registry.reviews[1].vendor='OpenAI',x=>x.tool_registry.reviews[1].receipt_verified=false,x=>x.tool_registry.reviews[1].evidence_ref='',x=>x.tool_registry.reviews[1].reviewed_at='invalid',x=>x.tool_registry.reviews[1].authority_ref='',x=>x.tool_registry.audit_projection.last_checks[0].exit_code=1,x=>x.tool_registry.audit_projection.last_checks[0].evidence_ref='']){let n=copy(q);change(n);assert.notEqual(row(n).lifecycle_code,'USABLE');}
 let exceptionCase=fixture();sign(exceptionCase,'OpenAI');exceptionCase.tool_registry.lifecycle_policy.owner_execution_exception={active:true,tool_ids:[id],scope:exceptionCase.tool_registry.memory[0].acceptance_scope,evidence_ref:'TEST:Owner directive'};assert.equal(row(exceptionCase).lifecycle_code,'USABLE');assert.equal(row(exceptionCase).claude_review,'Chưa duyệt');exceptionCase.tool_registry.lifecycle_policy.owner_execution_exception.tool_ids=[];assert.equal(row(exceptionCase).lifecycle_code,'TESTED');
 let n=copy(q);n.tool_registry.reviews.push({...n.tool_registry.reviews[1],review_id:'TEST-REVOKED',decision:'REJECT'});assert.notEqual(row(n).lifecycle_code,'USABLE');
 n=copy(q);n.tool_registry.memory[0].retired_at='2026-10-12T01:00:00Z';assert.equal(row(n).lifecycle_code,'RETIRED');
 const dep=fixture(),dt=dep.tool_registry.records.find(x=>x.id==='TQT-CHECK-005');dep.tool_registry.audit_projection.last_checks.push({id:dt.id,sha256:dt.sha256,exit_code:0,evidence_ref:'TEST:deps',ui_inputs:copy(dt.ui_inputs)});let dr=A.toolRows(dep).find(x=>x.record_id===dt.id);assert.equal(dr.lifecycle_code,'TESTED');const oldBinding=dr.binding;dt.ui_inputs['process-work-master-v1.js']='0'.repeat(64);dr=A.toolRows(dep).find(x=>x.record_id===dt.id);assert.equal(dr.lifecycle_code,'RETEST');assert.notEqual(dr.binding,oldBinding);
 const known=new Set([...A.toolRows(r),...A.providerRows(r)].map(x=>x.record_id));const memory=r.tool_registry.memory;assert.equal(new Set(memory.map(x=>x.tool_id)).size,memory.length);assert(memory.every(x=>known.has(x.tool_id)||/^TOOL-CTCM-00[1-9]$/.test(x.tool_id)));
 for(const col of A.sharedToolColumns(r))assert(col.help&&col.label);assert.deepEqual(A.sharedToolColumns(r).slice(-2).map(x=>x.key),['gpt_review','claude_review']);assert.deepEqual(A.definition(r,'CAT-006').layout.order.slice(-2),['gpt_review','claude_review']);
 for(const vendor of ['OpenAI','Anthropic'])assert(A.providerRows(r).every(x=>x.lifecycle_code!=='USABLE')); // capability name is not a pinned runtime test.
 assert.equal(A.relatedRows(r,'CAT-015').length,r.tool_registry.audit_projection.last_checks.length+(r.application_preview.record.execution_walk?.steps.length||0)+(r.application_preview.record.test_cases?.length||0));assert.equal(A.relatedRows(r,'CAT-025').length,r.tool_registry.reviews.length+(r.application_preview.record.decisions||[]).length+(r.application_preview.record.start_confirmation?.state==='CONFIRMED'?1:0));assert.equal(A.relatedRows(r,'CAT-016').length,r.tool_registry.changes.length+r.application_preview.record.trial_records.filter(x=>x.requirement_code==='CHANGE').length);assert.equal(A.relatedRows(r,'CAT-229*')[0].state,r.tool_registry.walkthrough.finished_at?'Đã trả kết quả':'Đang làm');assert.equal(A.relatedRows(r,'CAT-069?').length,(r.tool_registry.walkthrough?.findings.length||0)+(r.application_preview.record.execution_walk?.findings.length||0));
 for(const code of ['CAT-012','CAT-015','CAT-016','CAT-025','CAT-229*','CAT-069?']){const cfg=A.configure({}, {tqt:r,masterCode:code,sample:false});assert.equal(cfg.recordCountLabel,String(A.relatedRows(r,code).length));}
 const definitions=A.relatedRows(r,'CAT-012'),results=A.relatedRows(r,'CAT-015');assert.equal(new Set(definitions.map(x=>x.record_id)).size,definitions.length);for(const result of results)assert(definitions.some(x=>x.case_code===result.case_code&&x.suite_code===result.suite_code),'RESULT_CASE_NOT_REGISTERED');for(const entry of definitions.filter(x=>x.record_kind==='CASE'))assert(r.tool_registry.records.some(x=>x.case_set===entry.suite_code),'CASE_SUITE_NOT_REGISTERED');
 const sigs=r.tool_registry.reviews;assert.equal(new Set(sigs.map(x=>x.review_id)).size,sigs.length);for(const x of sigs){assert(known.has(x.target_code));assert(['OpenAI','Anthropic'].includes(x.vendor));assert(x.evidence_ref&&x.authority_ref&&x.scope&&x.binding);assert(!x.evidence_ref.startsWith('TEST:'));}
 for(const x of r.tool_registry.changes){assert(known.has(x.target_code));assert(x.previous_version!==x.next_version);assert(x.actor&&x.changed_at&&x.evidence_ref);}
 console.log('P34: 12 invalid-approval/version/test mutations + revocation/retirement blocked; 6 existing Masters read their sources; two vendor columns last; no synthetic receipt saved');
}

if(adapter&&r.application_preview.record.execution_walk){const A=globalThis.TQT_WORK_MASTER,a=r.application_preview.record;for(const code of ['CAT-012','CAT-015','CAT-069?','CAT-229*'])assert(A.relatedRows(r,code).some(x=>x.application_id===a.application_id));const n=cloneFixture(r);n.application_preview.record.checkpoint_checks=[];assert.equal(A.dossier(n,n.work_schedule.records[0]).checkpoints.filter(x=>x.done).length,0);console.log('P35: real work visible in existing Masters; removing checkpoint evidence clears progress');}

if(adapter&&r.application_preview.record.execution_walk){const rows=globalThis.TQT_WORK_MASTER.relatedRows(r,'CAT-069?').filter(x=>x.application_id===r.application_preview.record.application_id);assert(rows.length);for(const row of rows)assert(row.next&&row.owner&&row.state&&!['OPEN','FIXED'].includes(row.state),'REAL_FINDING_NEXT_AND_STATUS');console.log('P35 UI readback: real findings expose next action, owner and human-readable state');}

if(adapter){
 const A=globalThis.TQT_WORK_MASTER,n=cloneFixture(r),a=n.application_preview.record,c=a.information_contract;
 a.execution_walk={run_id:'MOW001-P99-REAL',actor:'HOST-MUST-NOT-BECOME-REVIEWER',steps:[{checkpoint:'CP01',action:'PASS only mentioned in planned action',state:'NOT_EXECUTED'}]};a.test_cases=[];
 const rows=code=>A.relatedRows(n,code),work=()=>rows('CAT-229*').find(x=>x.application_id===a.application_id),audit=()=>rows('CAT-015').find(x=>x.record_kind==='CHECKPOINT_AUDIT');
 assert.equal(work().round_id,'P99');assert.equal(work().attempt_no,'Chưa ghi');
 a.execution_walk.round_id='P100';a.execution_walk.attempt_no=2;assert.equal(work().round_id,'P100');assert.equal(work().attempt_no,2);
 delete a.execution_walk.round_id;delete a.execution_walk.attempt_no;a.execution_walk.run_id='unclassified';assert.equal(work().round_id,'Chưa ghi');
 assert.equal(audit().actual,'Chưa kiểm');assert.equal(audit().expected,'Chưa kiểm');assert.equal(audit().result,'Chưa kiểm');assert.equal(audit().checked_by,'Chưa ghi');assert.equal(audit().source_state,'NOT_EXECUTED');
 Object.assign(a.execution_walk.steps[0],{expected:'required observation',actual:'observed separately',result:'PASS',reviewer_id:'REVIEWER',evidence_ref:'test-only:readback'});
 assert.equal(audit().actual,'observed separately');assert.equal(audit().expected,'required observation');assert.equal(audit().checked_by,'REVIEWER');assert.equal(audit().evidence_ref,'test-only:readback');
 assert.equal(rows('CAT-015').filter(x=>x.record_kind==='PRODUCT_TEST_RESULT').length,0);
 const criterion=c.criteria[0];a.test_cases=[{id:'TEST-PROJECTION-ONLY',application_id:a.application_id,target_version:a.target_version,scope:a.scope,contract_binding:{id:c.id,version:c.version},criterion_id:criterion.id,expected:criterion.expected,actual:'Observed fixture, not real acceptance',reviewer_id:'TEST-REVIEWER',result:'PASS',evidence_ref:'test-only:projection'}];
 const product=()=>rows('CAT-015').find(x=>x.record_kind==='PRODUCT_TEST_RESULT');
 assert.equal(product().actual,a.test_cases[0].actual);assert.equal(product().checked_by,'TEST-REVIEWER');assert.equal(product().evidence_ref,'test-only:projection');
 assert(rows('CAT-012').some(x=>x.record_kind==='PRODUCT_CRITERION'&&x.case_code===product().case_code&&x.suite_code===product().suite_code&&x.expected===criterion.expected));
 a.test_cases[0].target_version='old';assert.equal(product().target_version,'old');assert(product().validity.includes('Khác hoặc thiếu'));
 a.test_cases[0].target_version=a.target_version;a.test_cases[0].criterion_id='UNKNOWN';assert(product().validity.includes('Chưa tìm thấy'));
 delete a.execution_walk;assert.equal(rows('CAT-015').filter(x=>x.record_kind==='PRODUCT_TEST_RESULT').length,1);assert.equal(rows('CAT-012').filter(x=>x.record_kind==='PRODUCT_CRITERION').length,c.criteria.length);
 console.log('P36: projection preserves observed results, reviewers and versions; no action-to-result inference; existing product criteria/results visible');
}

assert.equal(historyFingerprint(r.application_preview.record),sourceHistoryFingerprint,'FIXTURE_MUTATED_SOURCE_HISTORY');

// P37: the dossier itself must expose answers and distinguish an unopened next job.
if(adapter&&r.application_preview.resolved_questions){
 const A=globalThis.TQT_WORK_MASTER,a=r.application_preview.record,projection=r.application_preview;
 function verifyQuestions(p){const qs=p.resolved_questions,ids=a.preparation_review.answers.map(x=>x.question_id);assert.equal(p.question_source_version,p.source_version,'QUESTION_SOURCE_VERSION');assert.equal(qs.length,ids.length,'QUESTION_COVERAGE');assert.equal(new Set(qs.map(x=>x.question_id)).size,ids.length,'QUESTION_DUPLICATE');for(const id of ids){const x=qs.find(x=>x.question_id===id);assert(x&&x.question?.trim()&&x.answer?.trim()&&x.source_ref&&x.scope,'QUESTION_CONTENT:'+id);}}
 verifyQuestions(projection);assert.throws(()=>verifyQuestions({...projection,question_source_version:'OLD'}));assert.throws(()=>verifyQuestions({...projection,resolved_questions:projection.resolved_questions.slice(1)}));assert.throws(()=>verifyQuestions({...projection,resolved_questions:projection.resolved_questions.map((x,i)=>i?x:{...x,answer:''})}));
 const s=a.server_receipt,policy=r.server_trust_policy,crypto=require('crypto');assert(s&&s.key_id===policy.policy_id);const key=crypto.createPublicKey({key:Buffer.concat([Buffer.from('302a300506032b6570032100','hex'),Buffer.from(policy.public_key_base64,'base64')]),format:'der',type:'spki'});assert(crypto.verify(null,Buffer.from(s.payload),key,Buffer.from(s.signature,'base64')),'SERVER_SIGNATURE');tqtRegisterServerTrust(r,JSON.parse(s.payload));
 const list=A.scheduleRows(r),own=A.dossierView(r,{metadata:list[0]}).html,waiting=A.dossierView(r,{metadata:list[1]}).html;
 assert(own.includes('câu hỏi và câu trả lời'));assert(own.includes('Kho tệp G1: đã kiểm quyền ghi–đọc'));assert(!own.includes('Chưa khai nguồn lưu'));assert(waiting.includes('chưa mở hồ sơ thực hiện'));assert(waiting.includes('Chưa có hồ sơ để đối chiếu các mục'));assert(!waiting.includes('11 mục chưa phát sinh nhánh'));assert(waiting.includes('chi-tiet=TQT-VIEC-001'));assert(!waiting.includes('Quyết định và xác nhận nhận G1'));
 if(['XONG','DA_BAN_GIAO'].includes(a.state)){assert(tqtRecordAudit(r).canFinish,'CLOSED_WITHOUT_FINAL_GATE');assert(list[0].done,'COMPLETION_NOT_VISIBLE');assert(own.includes(a.decisions.find(x=>x.id===a.release.decision_ref).owner_quote),'OWNER_DECISION_NOT_VISIBLE');assert.equal(A.summary(list).done,1);assert.equal(A.summary(list).unfinished,1);}
 console.log('P37: question coverage/version/content, signed G1 file scope, actual closure and unopened successor visible; negative mutations rejected');
}
if(adapter&&r.application_preview.resolved_questions){
 const A=globalThis.TQT_WORK_MASTER,a=r.application_preview.record;
 for(const x of a.decisions||[])assert(A.relatedRows(r,'CAT-025').some(y=>y.record_id===x.id&&y.application_id===a.application_id),'OWNER_DECISION_MISSING_FROM_MASTER');
 for(const x of a.receipts||[])assert(A.relatedRows(r,'CAT-232*').some(y=>y.record_id===x.id&&y.recipient===x.recipient),'ACK_MISSING_FROM_MASTER');
 for(const [i,x] of a.history.entries()){const row=A.relatedRows(r,'CAT-233*')[i];assert.equal(row.occurred_at,x.at||x.date||'Chưa ghi');assert.equal(row.event_type,x.event||x.type||x.action||'HISTORY');}
 assert.equal(A.relatedRows(r,'CAT-233*').filter(x=>x.application_id===a.application_id).length,a.history.length,'HISTORY_MISSING_FROM_MASTER');
 assert(A.relatedRows(r,'CAT-016').some(x=>x.application_id===a.application_id),'CHANGE_MISSING_FROM_MASTER');
 assert.equal(A.relatedRows(r,'CAT-244*').length,(a.branch_records||[]).filter(x=>x.kind==='CANCELLED').length,'CONDITIONAL_BRANCH_FABRICATED');
 for(const code of ['CAT-025','CAT-232*','CAT-233*','CAT-016','CAT-244*']){const c=A.configure({}, {tqt:r,masterCode:code,sample:false});assert(c.principle.includes('Bản chiếu từ hồ sơ kho tệp hiện có'));assert(!c.principle.includes('Chưa khai nguồn lưu'));}
 console.log('P37: all actual Owner decisions, receipts, history and changes projected to existing Masters; no fabricated cancellation');
}
