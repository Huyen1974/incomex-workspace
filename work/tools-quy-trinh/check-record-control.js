/* Checks the same pure projection used by Overview. No browser or PostgreSQL mutation. */
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const file=process.argv[2]||__dirname+'/view.html',html=fs.readFileSync(file,'utf8');
const script=id=>{const m=html.match(new RegExp('<script id="'+id+'"[^>]*>([\\s\\S]*?)</script>'));assert(m,id);return m[1];};
const data=JSON.parse(script('tqt-composite-processes')),R=data.catalog;
vm.runInThisContext(script('tqt-record-control'));
const audit=globalThis.tqtRecordAudit,clone=x=>JSON.parse(JSON.stringify(x));let tests=0;
function test(name,change,verify){const r=clone(R);change(r);verify(audit(r),r);tests++;}
const row=(a,id)=>a.rows.find(x=>x.code===id);
const check=(r,id)=>r.application_preview.record.record_checks.find(x=>x.requirement_code===id);
assert.equal(new Set(R.records[4].workflow.checkpoints.map(x=>x.id)).size,7);
for(let i=0;i<7;i++){const cp=R.records[4].workflow.checkpoints[i];assert.equal(cp.order,i+1);assert.equal(cp.predecessor,i?'CP0'+i:null);}
test('current preparation has no verified milestones',r=>{},a=>{assert.equal(a.current,'CP02');assert.equal(a.verifiedCheckpoints.length,0);assert(!a.coverage);assert(!a.destinationReady);assert.equal(a.errors.length,0);});
test('omitted check row cannot disappear',r=>r.application_preview.record.record_checks.shift(),a=>assert.equal(row(a,'MOW').status,'CHECK_MISSING'));
test('unknown destination differs missing register',r=>r.work_form.record_control.definitions[0].source=null,a=>assert.equal(row(a,'MOW').store,'UNMAPPED'));
test('confirmed missing register',r=>check(r,'MOW').store_state='MISSING',a=>assert.equal(row(a,'MOW').store,'MISSING'));
test('unverified master is not evidence that record absent',r=>{},a=>assert.equal(row(a,'MOW').status,'UNKNOWN_RECORD'));
test('declared answer not accepted as checked',r=>{},a=>{assert.equal(row(a,'FIELD-identity').status,'WRITTEN');assert(!row(a,'FIELD-identity').verified);});
test('due missing answer detected',r=>r.application_preview.record.declarations[0].answer='',a=>assert.equal(row(a,'FIELD-identity').status,'MISSING_RECORD'));
test('future output not called missing',r=>{},a=>assert.equal(row(a,'RESULT-P03').status,'NOT_DUE'));
test('due output absent detected',r=>r.application_preview.record.current_checkpoint='CP04',a=>assert.equal(row(a,'RESULT-P03').status,'MISSING_RECORD'));
test('PREPARE result P01 due before start',r=>{},a=>assert.equal(row(a,'RESULT-P01').status,'MISSING_RECORD'));
test('conditional branch absent is not missing',r=>{},a=>assert.equal(row(a,'ISSUE').status,'NOT_DUE'));
test('wrong application',r=>check(r,'PLAN').application_id='OTHER',a=>assert.equal(row(a,'PLAN').status,'CHECK_MISSING'));
test('wrong target version',r=>check(r,'PLAN').target_version='OLD',a=>assert.equal(row(a,'PLAN').status,'CHECK_MISSING'));
test('duplicate check',r=>r.application_preview.record.record_checks.push(clone(check(r,'PLAN'))),a=>assert.equal(row(a,'PLAN').status,'CHECK_MISSING'));
test('PASS without proof',r=>check(r,'PLAN').readback_state='PASS',a=>assert(!row(a,'PLAN').verified));
test('register readable is not writable',r=>{},a=>assert(!a.destinationReady));
test('new plan output requires destination',r=>r.application_preview.record.plan.push({id:'P06',output:'New output'}),a=>assert(a.errors.some(x=>x.includes('P06'))));
test('deleted expected field detected',r=>r.work_form.record_control.definitions=r.work_form.record_control.definitions.filter(x=>x.code!=='FIELD-identity'),a=>assert(a.errors.some(x=>x.includes('identity'))));
test('unknown check requirement',r=>{const c=clone(check(r,'PLAN'));c.requirement_code='X';r.application_preview.record.record_checks.push(c);},a=>assert(a.errors.length));
test('later checkpoint cannot skip predecessors',r=>r.application_preview.record.checkpoint_checks=[{checkpoint:'CP07',application_id:r.application_preview.record.application_id,process_version:r.application_preview.record.process_version,target_version:r.application_preview.record.target_version,result:'PASS',validity:'CURRENT',evidence_ref:'test-only'}],a=>assert.equal(a.verifiedCheckpoints.length,0));
test('correctly evidenced record',r=>Object.assign(check(r,'PLAN'),{record_ref:'test-only:plan',record_version:'1',readback_state:'PASS',evidence_ref:'test-only:evidence',checked_by:'test-actor',checked_at:'2026-10-11T00:00:00Z'}),a=>assert(row(a,'PLAN').verified));
test('missing record version invalidates pass',r=>Object.assign(check(r,'PLAN'),{record_ref:'test-only:plan',readback_state:'PASS',evidence_ref:'test-only:evidence',checked_by:'test-actor',checked_at:'2026-10-11T00:00:00Z'}),a=>assert(!row(a,'PLAN').verified));
// A standalone render must parse; every embedded executable script is checked, not run against fake DOM.
for(const m of html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)){if(!/application\/json/.test(m[1])&&m[2].trim())new vm.Script(m[2]);}
console.log(JSON.stringify({tests,scope:'DECLARED_RECORDS_SIMULATION_ONLY',current:audit(R).current,counts:audit(R).counts,coverage:audit(R).coverage,pg:'NOT_RUN'}));
