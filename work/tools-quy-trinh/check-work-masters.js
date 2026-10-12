const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync(process.argv[2]||__dirname+'/view.html','utf8'),r=JSON.parse(html.match(/<script id="tqt-composite-processes"[^>]*>([\s\S]*?)<\/script>/)[1]).catalog;
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
for(const change of [x=>x.work_schedule.records.push(x.work_schedule.records[0]),x=>x.work_schedule.records[1].order=1,x=>x.work_schedule.records[0].depends_on=['TQT-VIEC-002'],x=>x.work_schedule.records[1].depends_on=['UNKNOWN'],x=>x.work_schedule.records[0].application_id='OTHER',x=>x.work_schedule.records[0].target_version='OLD',x=>x.work_schedule.records[0].application_ref='OTHER',x=>x.work_master_designs.records[0].code='MISSING',x=>x.work_master_designs.records[0].columns.push({key:'unknown'}),x=>x.work_schedule.records[1].completion_evidence='FAKE',x=>x.work_schedule.records[0].target_tier='CTCM',x=>x.work_schedule.records[0].lifecycle_state='UNKNOWN',x=>x.work_schedule.records[0].actual_finish='2026-01-01',x=>x.work_schedule.display_code='DEF001']){const c=JSON.parse(JSON.stringify(r));change(c);assert.throws(()=>validate(c));rejected++;}
if(adapter){const A=globalThis.TQT_WORK_MASTER;r.source_url='https://example.test/view.html';const list=A.scheduleRows(r);assert.equal(list.length,2);assert(list[0].dossier_url.endsWith('#tqt-recording-list'));assert.equal(list[1].dossier_url,null);assert.equal(list[1].state,'Ghi danh');for(const d of r.work_master_designs.records){const cfg=A.configure({}, {tqt:r,masterCode:d.code,sample:false});assert.equal(cfg.mother,'DEF');assert(cfg.definitionColumns.length);const sample=A.configure({}, {tqt:r,masterCode:d.code,sample:true});assert.equal(sample.items.length,1);assert(sample.items[0].form_schema.fields.length);assert(sample.items[0].code.startsWith('MAU-'));}assert.equal(A.indexRows(r).length,r.work_master_designs.records.length);
 assert.equal(A.indexRows(r)[0].code,'DEF 00.1');assert.equal(A.indexRows(r)[0].humanNo,'0.1');
 assert.deepEqual(A.summary(list),{total:2,unfinished:2,done:0,blocked:1,closed:0});
 assert.deepEqual(A.summary([]),{total:0,unfinished:0,done:0,blocked:0,closed:0});
 assert.equal(A.definition(r,'DEF00.1').code,'CAT-227*');
 const bad=JSON.parse(JSON.stringify(r));bad.work_schedule.records[0].target_version='wrong';assert.throws(()=>A.scheduleRows(bad));
 const fake=JSON.parse(JSON.stringify(r));fake.application_preview.record.state='XONG';assert.equal(A.scheduleRows(fake)[0].done,false);
 const cfg=A.configure({}, {tqt:r,masterCode:'DEF00.1',sample:false});assert.equal(cfg.filterFields.length,4);assert(cfg.statusOptions.includes('Đã cho nghỉ'));assert(cfg.items.every(x=>x.metadata.actual_start==='Chưa ghi'));
}
console.log(JSON.stringify({masters:r.work_master_designs.records.length,planned_jobs:r.work_schedule.records.length,negative_cases:rejected,scope:'DESIGN_ONLY',pg:'NOT_RUN'}));

if(adapter){
 vm.runInThisContext(html.match(/<script id="tqt-record-control"[^>]*>([\s\S]*?)<\/script>/)[1]);
 const A=globalThis.TQT_WORK_MASTER,copy=x=>JSON.parse(JSON.stringify(x)),d=A.dossier(r,r.work_schedule.records[0]);
 assert.equal(d.checkpoints.length,7);assert.equal(d.groups.length,11);assert.equal(d.groups.reduce((n,g)=>n+g.rows.length,0),34);
 assert.equal(d.checkpoints.filter(x=>x.current)[0].id,'CP02');assert.equal(d.checkpoints.filter(x=>x.done).length,0);assert.equal(d.done,0);
 const waiting=A.dossier(r,r.work_schedule.records[1]);assert.equal(waiting.a,null);assert(waiting.groups.every(g=>!g.done&&g.condition==='Chưa gắn hồ sơ'));assert(waiting.checkpoints.every(x=>!x.done&&!x.current));
 const partial=copy(r),p=partial.application_preview.record.record_checks.find(x=>x.requirement_code==='PLAN');
 Object.assign(p,{record_state:'RECORDED',master_record_id:'TEST',record_ref:'test:record',record_version:'1'});
 const g=A.dossier(partial,partial.work_schedule.records[0]).groups.find(g=>g.id==='RG04');assert.equal(g.written,1);assert(!g.done);assert(g.active.length>1);
 Object.assign(p,{process_code:partial.application_preview.record.process_code,process_version:partial.application_preview.record.process_version,target_code:partial.application_preview.record.target_code,readback_state:'PASS',checked_record_version:'1'});p.check_state='MATCHED';p.evidence_ref='test:evidence';p.checked_by='TEST';p.checked_at='2026-10-11T00:00:00Z';
 assert.equal(A.dossier(partial,partial.work_schedule.records[0]).groups.find(g=>g.id==='RG04').verified,1);
 p.application_id='WRONG';assert.equal(A.dossier(partial,partial.work_schedule.records[0]).groups.find(g=>g.id==='RG04').verified,0);
 const foreign=copy(r);foreign.work_schedule.records[0].process_version='WRONG';assert.throws(()=>A.dossier(foreign,foreign.work_schedule.records[0]));
 const unlinked=copy(r);unlinked.work_schedule.records[0].application_id='MISSING';assert.throws(()=>A.dossier(unlinked,unlinked.work_schedule.records[0]));
 const second=copy(r),other=copy(second.application_preview.record);other.application_id='TEST-SECOND';other.target_code='TEST-TARGET';other.record_checks=[];second.work_schedule.applications=[other];Object.assign(second.work_schedule.records[1],{application_id:other.application_id,target_code:other.target_code,target_version:other.target_version});
 const distinct=A.dossier(second,second.work_schedule.records[1]);assert.equal(distinct.a.application_id,'TEST-SECOND');assert.equal(distinct.written,0);assert.equal(distinct.done,0);assert(distinct.audit.errors.length);
 const cfg=A.configure({}, {tqt:r,masterCode:'DEF00.1',sample:false});const view=cfg.detailRenderer(cfg,cfg.items[0]);assert(view.fullWidth&&view.interactive);assert.equal((view.html.match(/type="checkbox"/g)||[]).length,18);assert.equal((view.html.match(/type="checkbox" disabled/g)||[]).length,18);assert.equal((view.html.match(/ checked /g)||[]).length,0); // No independent checkpoint/group approval yet.
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
 const A=globalThis.TQT_WORK_MASTER,copy=x=>JSON.parse(JSON.stringify(x));
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

if(adapter){const A=globalThis.TQT_WORK_MASTER;const rows=A.toolRows(r);assert.equal(new Set(rows.map(x=>x.record_id)).size,rows.length);assert(rows.filter(x=>x.id.startsWith('DOT.')).every(x=>x.state==='Đã tìm thấy · chưa kiểm chạy'));assert(rows.find(x=>x.id==='TQT-CHECK-004').state.includes('1 tệp'));const matrix=A.reuseMatrix(r);assert(matrix.some(x=>!x.tools.length));assert(matrix.some(x=>x.tool_ids.includes('jev-reference:evaluate')));const bad=JSON.parse(JSON.stringify(r));bad.tool_registry.reuse_needs[0].tool_ids=['UNKNOWN'];assert.throws(()=>A.reuseMatrix(bad));const cfg=A.configureTools({}, {tqt:r},{masterId:'ML-DEF-023',masterName:'Master Tool'},[{id:'TOOL-TEST',name:'Test legacy'}]);assert.equal(cfg.items.length,1+r.tool_registry.provider_tools.length);assert(cfg.items.some(x=>x.code==='jev-reference:evaluate'));assert(cfg.detailRenderer(cfg,cfg.items[1]).html.includes('Bằng chứng'));console.log('P33 inventory/proof states, provider reuse, missing coverage and detail validated');}

if(adapter){const old=JSON.parse(JSON.stringify(r));old.tool_registry.records[0].sha256='0'.repeat(64);assert(globalThis.TQT_WORK_MASTER.toolRows(old)[0].state.includes('phiên trước'));console.log('P33 stale tool source is not shown as current TEST proof');}

// P34: lifecycle and consensus are distinct from TEST results and inventory.
if(adapter){
 const A=globalThis.TQT_WORK_MASTER,copy=x=>JSON.parse(JSON.stringify(x)),id=r.tool_registry.records[0].id;
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
 assert.equal(A.relatedRows(r,'CAT-015').length,r.tool_registry.audit_projection.last_checks.length);assert.equal(A.relatedRows(r,'CAT-025').length,r.tool_registry.reviews.length);assert.equal(A.relatedRows(r,'CAT-016').length,r.tool_registry.changes.length);assert.equal(A.relatedRows(r,'CAT-229*')[0].state,r.tool_registry.walkthrough.finished_at?'Đã trả kết quả':'Đang làm');assert.equal(A.relatedRows(r,'CAT-069?').length,4);
 for(const code of ['CAT-012','CAT-015','CAT-016','CAT-025','CAT-229*','CAT-069?']){const cfg=A.configure({}, {tqt:r,masterCode:code,sample:false});assert.equal(cfg.recordCountLabel,String(A.relatedRows(r,code).length));}
 const sigs=r.tool_registry.reviews;assert.equal(new Set(sigs.map(x=>x.review_id)).size,sigs.length);for(const x of sigs){assert(known.has(x.target_code));assert(['OpenAI','Anthropic'].includes(x.vendor));assert(x.evidence_ref&&x.authority_ref&&x.scope&&x.binding);assert(!x.evidence_ref.startsWith('TEST:'));}
 for(const x of r.tool_registry.changes){assert(known.has(x.target_code));assert(x.previous_version!==x.next_version);assert(x.actor&&x.changed_at&&x.evidence_ref);}
 console.log('P34: 12 invalid-approval/version/test mutations + revocation/retirement blocked; 6 existing Masters read their sources; two vendor columns last; no synthetic receipt saved');
}
