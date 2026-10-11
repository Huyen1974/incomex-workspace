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
if(adapter){const A=globalThis.TQT_WORK_MASTER;r.source_url='https://example.test/view.html';const list=A.scheduleRows(r);assert.equal(list.length,2);assert(list[0].dossier_url.endsWith('#tqt-recording-list'));assert.equal(list[1].dossier_url,null);assert.equal(list[1].state,'Ghi danh');for(const d of r.work_master_designs.records){const cfg=A.configure({}, {tqt:r,masterCode:d.code,sample:false});assert.equal(cfg.mother,'DEF');assert(cfg.definitionColumns.length);const sample=A.configure({}, {tqt:r,masterCode:d.code,sample:true});assert.equal(sample.items.length,1);assert(sample.items[0].form_schema.fields.length);assert(sample.items[0].code.startsWith('MAU-'));}assert.equal(A.indexRows(r).length,9);
 assert.equal(A.indexRows(r)[0].code,'DEF 00.1');assert.equal(A.indexRows(r)[0].humanNo,'0.1');
 assert.deepEqual(A.summary(list),{total:2,unfinished:2,done:0,blocked:1,closed:0});
 assert.deepEqual(A.summary([]),{total:0,unfinished:0,done:0,blocked:0,closed:0});
 assert.equal(A.definition(r,'DEF00.1').code,'CAT-227*');
 const bad=JSON.parse(JSON.stringify(r));bad.work_schedule.records[0].target_version='wrong';assert.throws(()=>A.scheduleRows(bad));
 const fake=JSON.parse(JSON.stringify(r));fake.application_preview.record.state='XONG';assert.equal(A.scheduleRows(fake)[0].done,false);
 const cfg=A.configure({}, {tqt:r,masterCode:'DEF00.1',sample:false});assert.equal(cfg.filterFields.length,4);assert(cfg.statusOptions.includes('Đã cho nghỉ'));assert(cfg.items.every(x=>x.metadata.actual_start==='Chưa ghi'));
}
console.log(JSON.stringify({masters:r.work_master_designs.records.length,planned_jobs:r.work_schedule.records.length,negative_cases:rejected,scope:'DESIGN_ONLY',pg:'NOT_RUN'}));
