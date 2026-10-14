const fs=require('fs'),vm=require('vm'),assert=require('assert');
// Shared P60 contract: used by CHECK005 and the UI; no PG or identity authentication.
function controlBinding(value){return JSON.stringify(value);}
function validateControl(work,def,options={}){
 const errors=[],need=(ok,code)=>{if(!ok)errors.push(code);},c=work.control||{},o=c.objective||{},b=controlBinding(o);
 const filled=x=>typeof x==='string'&&!!x.trim();
 if(options.start||options.prepared||options.complete||c.owner_start)need(filled(o.goal)&&filled(o.recipient)&&filled(o.exclusions)&&Array.isArray(o.products)&&o.products.length>0&&o.products.every(x=>filled(x.id)&&filled(x.check_ref))&&Array.isArray(o.criteria)&&o.criteria.length>0&&o.criteria.every(x=>filled(x.id)&&filled(x.measure)&&filled(x.check)), 'OBJECTIVE_FIVE_FIELDS');
 need(new Set((o.criteria||[]).map(x=>x.id)).size===(o.criteria||[]).length,'CRITERION_ID');
 const approved=c.owner_start?.decision==='APPROVE'&&c.owner_start.binding===b&&c.owner_start.actor==='Owner'&&filled(c.owner_start.evidence_ref);
 if(options.start||options.complete)need(approved,'OWNER_START_REQUIRED');
 if(c.locked_objective&&controlBinding(c.locked_objective)!==b)need((c.repairs||[]).some(x=>x.subject==='objective'&&x.after_binding===b&&x.owner_approval?.binding===b&&x.owner_approval?.evidence_ref),'OBJECTIVE_CHANGE_UNAPPROVED');
 if(options.prepared||options.complete)need((o.criteria||[]).every(x=>(c.cases||[]).some(y=>y.criterion_id===x.id&&filled(y.expected)&&filled(y.method))),'CRITERION_CASE_MISSING');
 const events=c.steps||[],latest=new Map();for(const e of events){need(def.step_cards?.[e.step_id],'UNKNOWN_STEP');if(e.state==='DONE'){const card=def.step_cards?.[e.step_id];need(filled(e.evidence_ref),'STEP_EVIDENCE');for(const dep of card?.after||[]){const prev=latest.get(dep),na=(c.applicability||[]).find(x=>x.step_id===dep&&x.state==='NOT_APPLICABLE'&&x.evidence_ref&&x.review_ref);need(prev?.state==='DONE'||na,'STEP_ORDER');}}latest.set(e.step_id,e);}
 for(const m of c.milestones||[])if(m.state==='DONE')need(Array.isArray(m.report)&&controlBinding(m.report)===controlBinding(milestoneReport(work,m)),'MILESTONE_REPORT');
 const criteria=(o.criteria||[]).map(x=>({id:x.id,pass:(c.results||[]).some(y=>y.criterion_id===x.id&&y.result==='PASS'&&y.evidence_ref&&y.objective_binding===b)}));
 const inv=c.field_inventory||{},fieldOK=inv.state==='COMPLETE'&&Array.isArray(inv.ids)&&new Set(inv.ids).size===inv.ids.length&&filled(inv.evidence_ref)&&Number.isInteger(inv.new_design_count)&&inv.new_design_count>=0&&inv.new_design_count<=inv.ids.length;
 const gates=c.required_gates||[],signatureOK=gates.length>0&&gates.every(g=>['OpenAI','Anthropic','Owner'].every(v=>(g.reviews||[]).some(x=>x.vendor===v&&x.decision==='APPROVE'&&x.binding===g.binding&&x.scope===g.scope&&x.reviewer&&x.evidence_ref)));
 const stepsOK=Object.entries(def.step_cards||{}).every(([id,card])=>latest.get(id)?.state==='DONE'||(card.branch&&(c.applicability||[]).some(a=>a.step_id===id&&a.state==='NOT_APPLICABLE'&&a.evidence_ref&&a.review_ref))),milestonesOK=['CP01','CP02','CP03','CP04','CP05','CP06','CP07'].every(id=>(c.milestones||[]).some(m=>m.checkpoint===id&&m.state==='DONE'&&m.server_receipt&&m.report?.length===4));
 const allCriteria=criteria.length>0&&criteria.every(x=>x.pass),passed=approved&&allCriteria&&fieldOK&&signatureOK&&stepsOK&&milestonesOK;
 if(options.complete){need(stepsOK,'ALL_APPLICABLE_STEPS');need(milestonesOK,'SEVEN_UNIQUE_MILESTONES');}
 if(options.complete){need(allCriteria,'CRITERIA_INCOMPLETE');need(fieldOK,'FIELD_INVENTORY_INCOMPLETE');need(signatureOK,'SIGNATURES_INCOMPLETE');need(c.recipient_ack?.evidence_ref&&c.recipient_ack?.binding===b,'RECIPIENT_ACK');need((c.milestones||[]).filter(x=>x.state==='DONE'&&x.server_receipt).length===7,'SEVEN_SERVER_MILESTONES');}
 const card={criteria:{passed:criteria.filter(x=>x.pass).length,total:criteria.length,state:approved&&allCriteria?'GREEN':'RED'},fields:{state:fieldOK?'GREEN':'RED',new_design_count:fieldOK?inv.new_design_count:null,pg:'UNVERIFIED'},signatures:{state:signatureOK?'GREEN':'RED'},done:passed&&errors.length===0&&c.recipient_ack?.binding===b&&!!c.recipient_ack?.evidence_ref&&(c.milestones||[]).filter(x=>x.state==='DONE'&&x.server_receipt).length===7};
 if(c.claimed_card)need(controlBinding(c.claimed_card)===controlBinding(card),'MANUAL_CARD_COLOR');
 return {state:errors.length?'FAIL':'PASS',errors,card,scope:'HOST_CHECK_NOT_SERVER_AUTH'};
}
function validateGovernance(r){
 const errors=[],need=(x,c)=>{if(!x)errors.push(c);},g=r.governance||{},fields=r.field_registry.records,masters=g.masters||[];
 const workIds=(r.work_schedule?.records||[]).map(x=>x.short_id);need(workIds.every(x=>/^CV-\d{3,}$/.test(x||''))&&new Set(workIds).size===workIds.length,'WORK_CODE');need(masters.length===r.work_master_designs.records.length,'MASTER_COVERAGE');need(new Set(masters.map(x=>x.id)).size===masters.length,'MASTER_DUPLICATE');for(const m of masters){need(/^[A-Z]+(?:-[A-Z]+)*-\d+$/.test(m.id),'MASTER_CODE');need(m.source_code&&r.work_master_designs.records.some(x=>x.code===m.source_code),'MASTER_SOURCE');if(m.initial_approval?.state==='APPROVED')need(m.initial_approval.actor==='Owner'&&m.initial_approval.evidence_ref&&m.initial_approval.version,'MASTER_OWNER_APPROVAL');}
 const ids=new Set(),db=new Set(),names=new Set();for(const f of fields){need(/^FLD-\d{4,}$/.test(f.id)&&!ids.has(f.id),'FIELD_ID');ids.add(f.id);need(/^[a-z][a-z0-9_]{0,39}$/.test(f.db_code||'')&&!db.has(f.db_code),'FIELD_DB_CODE');db.add(f.db_code);need(f.name&&f.name.length<=60&&!names.has(f.name),'FIELD_DISPLAY_NAME');names.add(f.name);need(f.description&&f.origin_ref,'FIELD_DESCRIPTION_OR_ORIGIN');if(['CREATED','REUSED','ACCEPTED'].includes(f.lifecycle))need(f.pg_evidence_ref&&f.pg_target&&f.lifecycle_events?.length,'FIELD_PG_PROOF');let prev='DESIGNED';for(const e of f.lifecycle_events||[]){need(e.from===prev&&e.actor&&e.at&&e.evidence_ref,'FIELD_LIFECYCLE');need(({DESIGNED:['NEEDS_CREATE','REUSED','RETIRED'],NEEDS_CREATE:['CREATED','RETIRED'],CREATED:['ACCEPTED','RETIRED'],REUSED:['ACCEPTED','RETIRED'],ACCEPTED:['RETIRED'],RETIRED:[]}[prev]||[]).includes(e.to),'FIELD_LIFECYCLE_ORDER');prev=e.to;}need((f.lifecycle_events||[]).length===0?f.lifecycle==='DESIGNED':prev===f.lifecycle,'FIELD_LIFECYCLE_STATE');}
 const def=r.detailed_workflow;for(const row of def.groups.flatMap(x=>x.rows)){const card=def.step_cards?.[row[0]];need(card&&['action','after','input','actor','tool','done','write','report','error'].every(k=>card[k]!==undefined&&card[k]!==''),'STEP_NINE_ANSWERS');if(card)need(card.after.every(x=>def.step_cards[x]),'STEP_DEPENDENCY');}
 for(const x of g.repairs||[]){need(x.id&&x.subject&&x.before&&x.after&&x.reason&&x.actor&&x.evidence_ref&&x.signature_impact,'REPAIR_FIELDS');if(x.state==='VERIFIED')need(x.reviewer_vendor&&x.reviewer_vendor!==x.actor_vendor&&x.check_ref,'REPAIR_REVIEW');}
 return {state:errors.length?'FAIL':'PASS',errors};
}
function validateControlTransition(before,after,def){const out=validateControl(after,def);const a=before.control?.objective,b=after.control?.objective;if(before.control?.owner_start?.decision==='APPROVE'&&controlBinding(a)!==controlBinding(b)&&!(after.control?.repairs||[]).some(x=>x.subject==='objective'&&x.before_binding===controlBinding(a)&&x.after_binding===controlBinding(b)&&x.owner_approval?.binding===controlBinding(b)&&x.owner_approval?.evidence_ref))out.errors.push('SIGNED_CHANGE_REPAIR');out.state=out.errors.length?'FAIL':'PASS';return out;}
function milestoneReport(work,m){const c=work.control||{},steps=(c.steps||[]).filter(x=>x.step_id?.startsWith(m.checkpoint)),done=steps.filter(x=>x.state==='DONE'),blocked=steps.filter(x=>x.state==='BLOCKED');return ['Đang ở: '+m.checkpoint+' · '+m.state,'Đã xong: '+(done.map(x=>x.step_id).join(', ')||'Chưa có bước ghi xong'),'Tắc: '+(blocked.map(x=>x.step_id+': '+(x.reason||'Thiếu lý do')).join('; ')||'Chưa ghi nhận'),'Tiếp: '+(blocked.map(x=>(x.owner||'Chưa có người')+' / '+(x.next_trigger||'Chưa có điều kiện')).join('; ')||'Kiểm kết quả mốc trước khi chuyển tiếp')];}
function validateGovernanceTransition(before,after){const out=validateGovernance(after),changes=[];if(before.detailed_workflow?.source_sha256!==after.detailed_workflow?.source_sha256)changes.push('MOW-TH-006');if(controlBinding(before.field_registry)!==controlBinding(after.field_registry))changes.push('field_registry');for(const x of after.tool_registry?.records||[]){const old=before.tool_registry?.records.find(y=>y.id===x.id);if(old&&old.sha256!==x.sha256)changes.push(x.id);}for(const id of changes)if(!(after.governance?.repairs||[]).some(x=>x.subject===id&&x.before&&x.after&&x.evidence_ref&&x.signature_impact))out.errors.push('VERSION_CHANGE_WITHOUT_REPAIR:'+id);out.state=out.errors.length?'FAIL':'PASS';return out;}

function humanTime(value){if(typeof value!=='string'||!/^\d{4}-\d\d-\d\dT/.test(value))return value;const date=new Date(value);return Number.isNaN(+date)?value:new Intl.DateTimeFormat('vi-VN',{timeZone:'Asia/Ho_Chi_Minh',dateStyle:'short',timeStyle:'medium'}).format(date)+' (VN)';}

// P52: both CLI and normal checks use Git, never a caller-supplied receipt as proof.
const cp=require('child_process'),pathModule=require('path'),receiptCache=new Map();
function gitReceipt(repo,commit,path,eventId){
 assert(repo&&/^[a-f0-9]{40}$/.test(commit||'')&&path&&!path.startsWith('/')&&!path.split('/').includes('..')&&eventId,'RECEIPT_ARGUMENTS');
 const key=[repo,commit,path,eventId].join('|');if(receiptCache.has(key))return receiptCache.get(key);
 const git=args=>cp.execFileSync('git',['-C',repo,...args],{encoding:'utf8',maxBuffer:32*1024*1024,stdio:['ignore','pipe','pipe']});
 git(['merge-base','--is-ancestor',commit,'HEAD']);
 const raw=git(['show',commit+':'+path]),data=JSON.parse(raw.match(/<script id="tqt-composite-processes"[^>]*>([\s\S]*?)<\/script>/)[1]).catalog;
 const hits=(data.work_schedule.records||[]).flatMap(w=>(w.detail_tracking?.cycle?.milestone_events||[]).filter(e=>e.event_id===eventId));assert.equal(hits.length,1,'COMMITTED_EVENT_NOT_UNIQUE');const e=hits[0];assert(e.application_id&&/^CP0[1-7]$/.test(e.checkpoint)&&['STARTED','KQ'].includes(e.kind),'COMMITTED_EVENT_FIELDS');
 const value={commit,path,event_id:eventId,application_id:e.application_id,checkpoint:e.checkpoint,kind:e.kind,server_committed_at:git(['show','-s','--format=%cI',commit]).trim(),readback_sha256:require('crypto').createHash('sha256').update(raw).digest('hex'),scope:'GIT_COMMIT_TIME_NOT_PER_STEP_DURATION'};receiptCache.set(key,value);return value;
}
function receiptRepository(){
 const file=fs.realpathSync(process.argv[2]||__dirname+'/view.html');
 try{const repo=cp.execFileSync('git',['-C',pathModule.dirname(file),'rev-parse','--show-toplevel'],{encoding:'utf8',stdio:['ignore','pipe','pipe']}).trim(),relative=pathModule.relative(repo,file);cp.execFileSync('git',['-C',repo,'ls-files','--error-unmatch',relative],{stdio:'pipe'});return {repo,path:relative};}catch{return null;}
}
if(process.argv.includes('--commit-receipt')){console.log(JSON.stringify(gitReceipt(...process.argv.slice(process.argv.indexOf('--commit-receipt')+1))));process.exit(0);}
const receiptSource=receiptRepository();

let html=fs.readFileSync(process.argv[2]||__dirname+'/view.html','utf8');
const r=JSON.parse(html.match(/<script id="tqt-composite-processes"[^>]*>([\s\S]*?)<\/script>/)[1]).catalog;
// P51: every dossier is checked; no event suffix or P46-only entrance condition.
// Shared predicate: used unchanged by CHECK005 and the dossier UI.
function assessmentBinding(b,a){return JSON.stringify([b.application_id,b.target_version,b.process_version,b.definition_sha256,a.step_id,a.state,a.evaluated_by,a.execution_mode,a.actor,a.subject_vendor,a.evidence_ref,a.at,a.revision]);}
function validNonApplicable(b,a,def){
 if(!a||a.state!=='NOT_APPLICABLE'||!a.evidence_ref)return false;
 const c=b.cycle||{};
 if(a.evaluated_by==='MACHINE'){const x=c.master_records?.['CAT-229*']?.find(x=>x.record_id===a.evaluation_receipt);return !!(x&&x.application_id===b.application_id&&x.target_version===b.target_version&&x.step_id===a.step_id&&x.state==='SUCCESS'&&x.tool_id&&x.evidence_ref&&Number.isFinite(Date.parse(x.at)));}
 if(def?.execution_policy?.applicability_evaluator?.automation_current!=='NO_COMMAND'||a.evaluated_by!=='AI'||a.execution_mode!=='MANUAL_ASSISTED'||!a.actor||!['OpenAI','Anthropic'].includes(a.subject_vendor)||!Number.isFinite(Date.parse(a.at))||!Number.isInteger(a.revision)||a.revision<1)return false;
 const x=c.master_records?.['CAT-015']?.find(x=>x.record_id===a.review_ref),v=x?.review;
 return !!(x&&x.application_id===b.application_id&&x.target_version===b.target_version&&x.process_version===b.process_version&&x.definition_sha256===b.definition_sha256&&x.step_id==='CP05.03'&&x.decision==='APPROVE'&&x.assessment_binding===assessmentBinding(b,a)&&x.evidence_ref&&Number.isFinite(Date.parse(x.at))&&Date.parse(x.at)>=Date.parse(a.at)&&v?.subject_vendor===a.subject_vendor&&['OpenAI','Anthropic'].includes(v.reviewer_vendor)&&v.reviewer_vendor!==a.subject_vendor&&v.reviewer&&v.reviewer!==a.actor);
}

if(process.argv.includes('--assessment-binding')){const x=JSON.parse(fs.readFileSync(process.argv[process.argv.indexOf('--assessment-binding')+1],'utf8'));console.log(JSON.stringify({assessment_binding:assessmentBinding(x.dossier,x.assessment)}));process.exit(0);}
function validateCompact(b,def,context={}){
 if(!def.execution_policy?.compact_contract)return;
 const c=b.cycle||{},policies=def.step_policies,events=[...new Map((b.events||[]).map(e=>[e.step_id+'|'+(e.item_key||''),e])).values()],fail=(x,m)=>assert(x,m),byId=new Map();
 const receipt=(id,step)=>{const x=c.master_records?.['CAT-229*']?.find(x=>x.record_id===id);return x&&x.application_id===b.application_id&&x.target_version===b.target_version&&x.step_id===step&&x.state==='SUCCESS'&&x.tool_id&&x.evidence_ref&&Number.isFinite(Date.parse(x.at))?x:null;};
 for(const a of c.applicability||[]){fail(policies[a.step_id]&&!byId.has(a.step_id),'APPLICABILITY_ID');byId.set(a.step_id,a);fail(['APPLIES','NOT_APPLICABLE','UNKNOWN'].includes(a.state),'APPLICABILITY_STATE');if(a.state==='NOT_APPLICABLE'){fail(policies[a.step_id].applicability==='CONDITIONAL','MANDATORY_NOT_APPLICABLE');fail(validNonApplicable(b,a,def),'APPLICABILITY_EVIDENCE');}}
 for(const e of events){const p=policies[e.step_id];if(!p)continue;if(e.performed==='DONE'){
  if(p.automation_current==='HAS_COMMAND')fail(e.execution_mode==='AUTOMATED'&&p.command&&p.last_real_run_ref&&receipt(e.tool_run_id,e.step_id),'AUTOMATED_RECEIPT_REQUIRED');
  if(p.automation_current==='NO_COMMAND')fail(e.execution_mode==='MANUAL_ASSISTED','MANUAL_FALLBACK_REQUIRED');
  fail(byId.get(e.step_id)?.state!=='NOT_APPLICABLE','EVENT_ON_INAPPLICABLE_BRANCH');
  if(p.members.length>1){const items=e.obligation_checks||[];fail(items.length===p.members.length&&new Set(items.map(x=>x.step_id)).size===p.members.length&&p.members.every(id=>items.some(x=>x.step_id===id&&x.evidence_ref&&(x.state==='PASS'||(x.state==='NOT_APPLICABLE'&&r.detailed_workflow_history.find(d=>d.version==='0.7-completion-contract')?.groups.flatMap(g=>g.rows).find(row=>row[0]===id)?.[5].startsWith('KHI')&&validNonApplicable(b,x,def))))),'MERGED_OBLIGATIONS_INCOMPLETE');}
 }
 const intervals=(c.milestones||[]).filter(x=>x.checkpoint===(e.step_id==='CP03.12'&&e.return_to?e.return_to:e.step_id).slice(0,4));
 if(intervals.length){const start=Date.parse(e.started_at||e.at),end=Date.parse(e.completed_at||e.at);fail(Number.isFinite(start)&&Number.isFinite(end)&&end>=start,'EVENT_INTERVAL');fail(intervals.some(m=>Date.parse(m.start_receipt?.server_committed_at)<=start&&(!m.end_receipt||end<=Date.parse(m.end_receipt.server_committed_at))),'EVENT_OUTSIDE_MILESTONE');}
 else if(context.require_complete)fail(false,'EVENT_MILESTONE_REQUIRED');
 }
 if(c.resume_from){const e=events.find(e=>e.step_id==='CP03.12'&&e.performed==='DONE');fail(e&&e.previous_run_id===c.resume_from&&e.return_to&&e.source_version===b.target_version&&e.rights_receipt,'RESUME_RECHECK_REQUIRED');const t=Date.parse(e.completed_at||e.at);fail(events.filter(x=>x!==e&&x.run_id===e.run_id).every(x=>Date.parse(x.started_at||x.at)>=t),'RESUME_ORDER');}
 if(context.require_complete)for(const [code,p] of Object.entries(policies)){const rows=events.filter(x=>x.step_id===code),done=rows.length>0&&rows.every(x=>x.performed==='DONE'),na=byId.get(code)?.state==='NOT_APPLICABLE';fail(done||(p.applicability==='CONDITIONAL'&&na),'APPLICABLE_STEP_INCOMPLETE');}
}
function validateFieldRegistry(f,designs){
 assert.equal(f.master_id,'ML-DEF-008');assert.equal(new Set(f.records.map(x=>x.id)).size,f.records.length);
 const expected=designs.flatMap(m=>m.fields.map(x=>m.code+'.'+x.key+(x.required?' (bắt buộc)':''))),actual=f.records.flatMap(x=>x.usage_refs).filter(x=>expected.includes(x));assert.deepEqual(actual.slice().sort(),expected.slice().sort(),'FIELD_USAGE_COVERAGE');assert.equal(f.usage_count,f.records.reduce((n,x)=>n+x.usage_refs.length,0));
 const keys=f.records.map(x=>JSON.stringify([x.key,x.dataType,x.validation,x.semantic_key]));assert.equal(new Set(keys).size,keys.length,'DUPLICATE_FIELD_MEANING');
 assert.equal(f.records.length,f.reused_definition_count+f.new_contract_fields+f.new_registry_fields);
 for(const x of f.records){assert(x.semantic_key&&x.definition_version,'FIELD_IDENTITY');for(const u of x.usage_refs)assert(x.usage_labels?.[u],'FIELD_USE_LABEL');if(['Đã tạo trong PG','Đã kiểm PG'].includes(x.pg_state))assert(x.pg_target&&x.pg_evidence_ref,'FIELD_PG_EVIDENCE');}
 const groups=new Map();for(const x of f.records){const k=JSON.stringify([x.key,x.dataType,x.validation]);if(!groups.has(k))groups.set(k,[]);groups.get(k).push(x.id);}for(const [k,ids] of groups){if(ids.length<2)continue;const decisions=(f.collision_decisions||[]).filter(d=>JSON.stringify([d.key,d.dataType,d.validation])===k);assert.equal(decisions.length,1,'FIELD_COLLISION_DECISION');const d=decisions[0];assert(d.decision==='KEEP'&&d.reason&&d.decided_by,'FIELD_COLLISION_REASON');assert.deepEqual([...d.current_ids].sort(),ids.sort(),'FIELD_COLLISION_MEMBERS');}
 const targets=new Set(f.records.map(x=>x.id));for(const [id,to] of Object.entries(f.old_to_new))assert(targets.has(to),'FIELD_ALIAS_TARGET');
}

function validateDossier(b,def,context={}){
 const fail=(ok,code)=>assert(ok,code),c=b.cycle||{},latest=new Map(),known=new Map(def.groups.flatMap(g=>g.rows.map(x=>[x[0],x]))),ids=new Set(),warnings=[];
 for(const e of b.events||[]){
  fail(e.event_id&&!ids.has(e.event_id),'EVENT_ID');ids.add(e.event_id);
  fail(known.has(e.step_id)&&e.application_id===b.application_id&&e.target_version===b.target_version&&e.process_version===b.process_version&&e.definition_sha256===b.definition_sha256,'EVENT_BINDING');
  fail(e.item_key&&e.actor&&Number.isFinite(Date.parse(e.at))&&Number.isInteger(e.revision)&&e.revision>0,'EVENT_FIELDS');
  const key=e.step_id+'|'+e.item_key,old=latest.get(key);fail(!old||e.revision>old.revision,'REVISION_ORDER');latest.set(key,e);
 }
 const step=id=>[...latest.values()].filter(e=>e.step_id===id);
 for(const e of latest.values()){
  fail(['DONE','BLOCKED','NOT_DONE'].includes(e.performed),'PERFORMED');
  if(e.performed==='DONE')fail(e.actual_action&&(e.evidence_ref||e.result_ref),'DONE_EVIDENCE');
  if(e.performed==='BLOCKED')for(const k of ['reason','issue_ref','owner','return_to','next_trigger'])fail(typeof e[k]==='string'&&e[k].trim(),'BLOCKER_'+k);
  if(e.performed==='NOT_DONE'){
   fail(e.reason&&e.condition_evidence,'SKIP_EVIDENCE');
   if(known.get(e.step_id)[5].startsWith('LUÔN')||e.obligation_due===true)fail(e.exception_approval?.approver&&e.exception_approval?.authority_ref&&e.exception_approval?.evidence_ref&&e.exception_approval?.scope===e.step_id,'MANDATORY_SKIP_APPROVAL');
  }
  if((def.execution_policy?.independent_review_steps||[]).includes(e.step_id)&&e.performed==='DONE')fail(e.review?.subject_actor&&e.review?.reviewer&&e.review.reviewer!==e.review.subject_actor&&e.review.evidence_ref&&e.review.target_version===b.target_version,'INDEPENDENT_REVIEW');
  if((def.execution_policy?.independent_review_steps||[]).includes(e.step_id)&&e.performed==='DONE'){const v=def.execution_policy.consensus_required||[];fail(v.includes(e.review.subject_vendor)&&v.includes(e.review.reviewer_vendor)&&e.review.subject_vendor!==e.review.reviewer_vendor,'INDEPENDENT_REVIEW_VENDOR');}
  if(e.items){fail(Array.isArray(e.items.expected_ids)&&Array.isArray(e.items.checked_ids)&&new Set(e.items.expected_ids).size===e.items.expected_ids.length&&new Set(e.items.checked_ids).size===e.items.checked_ids.length,'ITEM_IDS');fail(e.items.count===e.items.checked_ids.length&&e.items.checked_ids.every(x=>e.items.expected_ids.includes(x)),'ITEM_COUNT');if(e.performed==='DONE')fail(e.items.expected_ids.length===e.items.checked_ids.length&&e.items.evidence_ref&&e.items.source_version,'ITEM_COVERAGE');}
  if(def.execution_policy?.repeat_steps?.includes(e.step_id)&&e.performed==='DONE')fail(e.item_key!=='G1'&&(e.items||e.item_evidence_ref),'REPEAT_MANIFEST');
 }
 if(c.closed_at)fail(step('CP07.08').some(e=>e.performed==='DONE'&&e.evidence_ref),'CLOSED_RUN_STILL_BLOCKED');
 if(c.publication?.readback?.state==='PASS')fail(step(def.legacy_step_map?.['CP04.07']||'CP04.07').some(e=>e.performed==='DONE'&&e.evidence_ref),'READBACK_STILL_BLOCKED');
 if((c.master_records?.['CAT-016']||[]).length)fail(!step('CP04.15').some(e=>e.performed==='NOT_DONE'),'CHANGE_BRANCH_SKIPPED');
 // A correction may inherit measured evidence only along an explicit same-step/item chain.
 for(const e of b.events||[])if(e.correction_of){const p=b.events.find(x=>x.event_id===e.correction_of);fail(p&&p.step_id===e.step_id&&p.item_key===e.item_key&&p.application_id===e.application_id&&p.revision<e.revision,'CORRECTION_BINDING');}
 if(c.history_correction_proof){const h=c.history_correction_proof;fail((b.events||[]).length>=h.prior_events,'HISTORY_LENGTH');fail(require('crypto').createHash('sha256').update(JSON.stringify(b.events.slice(0,h.prior_events))).digest('hex')===h.prior_sha256,'HISTORY_PREFIX_CHANGED');}
 const milestoneIds=new Set();for(const m of c.milestones||[]){
  fail(/^CP0[1-7]$/.test(m.checkpoint)&&m.start_receipt,'MILESTONE_START');
  for(const key of ['start_receipt','end_receipt'])if(m[key]){const receipt=m[key];fail(/^[a-f0-9]{40}$/.test(receipt.commit||'')&&Number.isFinite(Date.parse(receipt.server_committed_at))&&!milestoneIds.has(receipt.event_id),'MILESTONE_RECEIPT_FORMAT');milestoneIds.add(receipt.event_id);if(!receiptSource){warnings.push({code:'UNVERIFIED_RECEIPT',event_id:receipt.event_id});fail(!context.require_complete,'UNVERIFIED_RECEIPT');}else{let trusted;try{trusted=gitReceipt(receiptSource.repo,receipt.commit,receiptSource.path,receipt.event_id);}catch(error){throw Error('INVALID_SERVER_RECEIPT: '+error.message);}fail(trusted.application_id===b.application_id&&trusted.checkpoint===m.checkpoint&&trusted.kind===(key==='start_receipt'?'STARTED':'KQ')&&Date.parse(trusted.server_committed_at)===Date.parse(receipt.server_committed_at)&&(!receipt.path||receipt.path===trusted.path)&&(!receipt.readback_sha256||receipt.readback_sha256===trusted.readback_sha256),'SERVER_RECEIPT_MISMATCH');}}
  if(m.end_receipt)fail(Date.parse(m.end_receipt.server_committed_at)>=Date.parse(m.start_receipt.server_committed_at),'MILESTONE_ORDER');
 }
 if(c.write_authorization){const a=c.write_authorization;fail(a.mode==='HOST_CHECK'&&a.application_id===b.application_id&&a.path&&a.authority_ref&&a.precheck_ref&&a.cas_receipt&&a.readback_ref,'HOST_CHECK_CHAIN');fail(a.server_enforced===false,'HOST_CHECK_NOT_SERVER_GUARD');}
 for(const issue of c.issues||[])auditIssue(issue);
 if(context.require_complete===true){fail(['CP01','CP02','CP03','CP04','CP05','CP06','CP07'].every(cp=>(c.milestones||[]).some(m=>m.checkpoint===cp&&m.end_receipt)),'SEVEN_MILESTONES_REQUIRED');fail(c.owner_decision_ref&&c.recipient_ack_ref,'OWNER_ACK_REQUIRED');}
 validateCompact(b,def,context);
 if(def.execution_policy?.control_contract){const canonical=r.work_schedule.records.find(w=>w.application_id===b.application_id)?.control;fail(!canonical||!b.control||controlBinding(canonical)===controlBinding(b.control),'DUPLICATE_CONTROL_MISMATCH');const v=validateControl({control:{...(canonical||b.control||{}),steps:(b.events||[]).map(e=>({...e,state:e.performed,evidence_ref:e.evidence_ref||e.result_ref}))}},def,{start:(b.events||[]).some(e=>e.step_id>='CP02'),prepared:(b.events||[]).some(e=>e.step_id>='CP03'),complete:context.require_complete});fail(v.state==='PASS',v.errors.join(','));}
 return {state:warnings.length?'UNVERIFIED':'PASS',warnings,scope:'HOST_CHECK_ONLY_NOT_SERVER_ENFORCEMENT',events:(b.events||[]).length,manual_assessments:[...(c.applicability||[]),...[...latest.values()].flatMap(e=>e.obligation_checks||[])].filter(a=>a.execution_mode==='MANUAL_ASSISTED').length};
}
function reviewConsensus(g){
 if(!g)return false;
 return ['OpenAI','Anthropic'].every(v=>{const x=(g.reviews||[]).filter(x=>x.vendor===v).at(-1);return x&&x.decision==='APPROVE'&&x.binding===g.binding&&x.scope===g.scope&&x.reviewer&&x.evidence_ref&&Number.isFinite(Date.parse(x.reviewed_at));});
}
function auditIssue(x){
 assert(['OPEN','VERIFIED','FIXING','VERIFYING','CLOSED','DEFERRED','REJECTED','SUPERSEDED'].includes(x.state),'ISSUE_STATE');assert(x.owner&&x.return_to,'ISSUE_OWNER_RETURN');
 if(x.state==='CLOSED')assert(x.result_ref&&x.origin_readback_ref&&x.verified_by&&x.verified_by!==x.fixed_by,'ISSUE_CLOSE_EVIDENCE');
 if(x.state==='DEFERRED')assert(x.approved_by&&x.decision_ref&&x.next_trigger,'ISSUE_DEFER_APPROVAL');
 if(x.state==='REJECTED')assert(x.reason&&x.evidence_ref,'ISSUE_REJECT_EVIDENCE');
 if(x.state==='SUPERSEDED')assert(x.replacement_ref&&x.obligation_mapping_ref&&x.verified_by,'ISSUE_SUPERSEDED_MAPPING');
 return true;
}

if(process.argv.includes('--validate-dossier')){const f=process.argv[process.argv.indexOf('--validate-dossier')+1],x=JSON.parse(fs.readFileSync(f,'utf8')),b=x.dossier,def=[r.detailed_workflow,...(r.detailed_workflow_history||[])].find(d=>d.version===b.process_version&&d.source_sha256===b.definition_sha256);assert(def,'UNKNOWN_DEFINITION');assert(r.work_schedule.records.some(w=>w.application_id===b.application_id)||def.version===r.detailed_workflow.version,'NEW_APPLICATION_REQUIRES_CURRENT_DEFINITION');console.log(JSON.stringify(validateDossier(b,def,x)));process.exit(0);}
if(process.argv.includes('--milestone-report')){const x=JSON.parse(fs.readFileSync(process.argv[process.argv.indexOf('--milestone-report')+1],'utf8'));console.log(JSON.stringify(milestoneReport(x.work,x.milestone)));process.exit(0);}
if(process.argv.includes('--validate-governance-before')){const text=fs.readFileSync(process.argv[process.argv.indexOf('--validate-governance-before')+1],'utf8'),m=text.match(/<script id="tqt-composite-processes"[^>]*>([\s\S]*?)<\/script>/),before=JSON.parse(m?m[1]:text).catalog;const out=validateGovernanceTransition(before,r);console.log(JSON.stringify(out));process.exit(out.state==='PASS'?0:1);}
if(process.argv.includes('--validate-control')){const input=JSON.parse(fs.readFileSync(process.argv[process.argv.indexOf('--validate-control')+1],'utf8'));const result=input.before?validateControlTransition(input.before,input.work,r.detailed_workflow):validateControl(input.work,r.detailed_workflow,input.options||{});console.log(JSON.stringify(result));process.exit(result.state==='PASS'?0:1);}
if(r.governance){const v=validateGovernance(r);assert.equal(v.state,'PASS',v.errors.join(','));}
const engineCode=Buffer.from(html.match(/<script id="tqt-record-control"[^>]*>([\s\S]*?)<\/script>/)[1]).toString();
html=null;/release/.test('release'); // Release large HTML/RegExp input; all real records/history remain intact.
// Fixture mutations never edit execution-history entries. Share their full read-only
// source instead of repeatedly serializing historical evidence; current records and
// checkpoint entries are read-only; replacing an array stays local to the fixture.
// Fingerprints before each fixture and after the suite catch unintended source edits.
function historyFingerprint(a){const h=require('crypto').createHash('sha256');for(const key of ['history','checkpoint_checks']){h.update(key);for(const row of a[key]||[])h.update(JSON.stringify(row)).update('\n');}return h.digest('hex');}
vm.runInThisContext(engineCode);
r.application_preview.record=tqtExpandApplication(r.application_preview.record);
const sourceHistoryFingerprint=historyFingerprint(r.application_preview.record);
function cloneFixture(x){
 assert.equal(historyFingerprint(r.application_preview.record),sourceHistoryFingerprint,'FIXTURE_MUTATED_SOURCE_HISTORY');
 if(!x?.application_preview?.record)return JSON.parse(JSON.stringify(x));
 const a=x.application_preview.record,out=JSON.parse(JSON.stringify({...x,application_preview:{...x.application_preview,record:{...a,history:[],checkpoint_checks:[]}}}));
 out.application_preview.record.history=a.history;out.application_preview.record.checkpoint_checks=a.checkpoint_checks;assert.equal(historyFingerprint(r.application_preview.record),sourceHistoryFingerprint,'FIXTURE_MUTATED_SOURCE_HISTORY');return out;
}
const adapter=process.argv[3];if(adapter)vm.runInThisContext(fs.readFileSync(adapter,'utf8'));
function auditRecordedCycle(A,data){const normalized={...data,work_schedule:{...data.work_schedule,records:data.work_schedule.records.map(w=>{const b=w.detail_tracking;if(!b?.cycle)return w;return {...w,detail_tracking:{...b,events:(b.events||[]).map(e=>{if(!('duration_ms' in e)){assert.equal(e.timing_basis,'RECORDING_ONLY','MISSING_MEASURED_DURATION');return {...e,duration_ms:0};}return e;})}};})}};return A.cycleAudit(normalized);}
if(adapter&&globalThis.TQT_WORK_MASTER.cycleAudit){const v=auditRecordedCycle(globalThis.TQT_WORK_MASTER,r);assert.equal(v.state,'PASS',JSON.stringify(v));if(process.argv.includes('--cycle-only')){console.log(JSON.stringify(v));process.exit(0);}}
function auditCycleProducts(c){for(const [k,p] of Object.entries(c.products||{})){assert.equal(p.cycle_id,c.run_id,'PRODUCT_CYCLE');assert.equal(require('crypto').createHash('sha256').update(JSON.stringify(p)).digest('hex'),c.product_hashes[k],'PRODUCT_HASH');if(k==='P01')assert.equal(p.read_receipt.answered,50,'P01_ANSWERS');if(['P02','P03'].includes(k)){assert.equal(p.reused_content.mots.length,3,'DESIGN_MOTS');for(const m of p.reused_content.mots)for(const key of ['fields','controls','branches'])assert(Array.isArray(m[key])&&m[key].length,'DESIGN_CONTENT');}}}
for(const w of r.work_schedule.records){const c=w.detail_tracking?.cycle;if(c?.products?.P02?.reused_content){auditCycleProducts(c);const bad=JSON.parse(JSON.stringify(c));bad.products.P02.reused_content.mots[0].fields=[];bad.product_hashes.P02=require('crypto').createHash('sha256').update(JSON.stringify(bad.products.P02)).digest('hex');assert.throws(()=>auditCycleProducts(bad),/DESIGN_CONTENT/);console.log('P46: actual rebuilt products read and verified; missing-fields negative case rejected (TEST)');}}

for(const w of r.work_schedule.records){const b=w.detail_tracking;if(!b?.cycle)continue;const def=[r.detailed_workflow,...(r.detailed_workflow_history||[])].find(d=>d.version===b.process_version&&d.source_sha256===b.definition_sha256);assert(def,'HISTORICAL_DEFINITION');console.log(JSON.stringify({application_id:b.application_id,...validateDossier(b,def)}));if(!b.cycle.history_correction_proof)continue;const bad=JSON.parse(JSON.stringify(b));bad.events[0].actual_action='tampered';assert.throws(()=>validateDossier(bad,def),/HISTORY_PREFIX_CHANGED/);if(adapter){const model=globalThis.TQT_WORK_MASTER.detailModel(r,w),rows=model.groups.flatMap(g=>g.rows);assert(rows.find(x=>x.definition[0]==='CP05.04').actual.elapsed.includes('348'));assert(rows.find(x=>x.definition[0]==='CP05.10').actual.tools.includes('TQT-CHECK-006'));assert.equal(rows.find(x=>x.definition[0]==='CP03.05').actual.confirmation,'Bị chặn');assert(!rows.find(x=>x.definition[0]==='CP02.05').actual.evidence.includes('[{'));const grouped=globalThis.TQT_WORK_MASTER.compactModel(r,w);assert.equal(grouped.groups.flatMap(g=>g.rows).length,r.detailed_workflow.step_count);assert.equal(grouped.groups.flatMap(g=>g.rows).flatMap(x=>x.parts).length,87);assert.equal(grouped.original.count,87);}}
// New application, not a P46 clone: each rule has a positive control and mutation.
{
 const d=JSON.parse(JSON.stringify(r.detailed_workflow_history.find(x=>x.version==='0.9-manual-applicability')||r.detailed_workflow)),id='TEST-P51-NEW',now='2026-10-13T00:00:00Z';
 const e={event_id:'NEW-E1',revision:1,at:now,actor:'TEST executor',application_id:id,target_version:'TEST-v1',process_version:d.version,definition_sha256:d.source_sha256,step_id:'CP01.01',item_key:'request',performed:'DONE',actual_action:'TEST only',evidence_ref:'TEST/evidence'};
 const b={application_id:id,target_version:'TEST-v1',process_version:d.version,definition_sha256:d.source_sha256,events:[e],cycle:{}};
 validateDossier(b,d);assert.throws(()=>validateDossier(b,d,{require_complete:true}),/SEVEN_MILESTONES/);let cases=2;const reject=(mut,code)=>{const x=JSON.parse(JSON.stringify(b));mut(x);assert.throws(()=>validateDossier(x,d),new RegExp(code));cases++;};
 reject(x=>Object.assign(x.events[0],{performed:'BLOCKED',reason:'missing'}),'BLOCKER');
 reject(x=>x.cycle.closed_at=now,'CLOSED_RUN');
 reject(x=>x.cycle.publication={readback:{state:'PASS'}},'READBACK');
 reject(x=>{x.events[0].step_id='CP04.15';Object.assign(x.events[0],{performed:'NOT_DONE',reason:'branch absent',condition_evidence:'TEST'});x.cycle.master_records={'CAT-016':[{record_id:'NEW-CHANGE'}]};},'CHANGE_BRANCH');
 reject(x=>Object.assign(x.events[0],{performed:'NOT_DONE',reason:'skip'}),'SKIP_EVIDENCE');
 reject(x=>Object.assign(x.events[0],{performed:'NOT_DONE',reason:'skip',condition_evidence:'TEST'}),'MANDATORY_SKIP');
 reject(x=>Object.assign(x.events[0],{step_id:'CP03.05',review:{subject_actor:'A',reviewer:'A',evidence_ref:'TEST',target_version:'TEST-v1'}}),'INDEPENDENT_REVIEW');
 reject(x=>x.events[0].items={expected_ids:['a','b'],checked_ids:['a'],count:1,evidence_ref:'TEST',source_version:'1'},'ITEM_COVERAGE');
 reject(x=>Object.assign(x.events[0],{step_id:'CP02.02',item_key:'G1'}),'REPEAT_MANIFEST');
 reject(x=>x.events[0].correction_of='missing','CORRECTION_BINDING');

 reject(x=>x.cycle.write_authorization={mode:'HOST_CHECK'},'HOST_CHECK_CHAIN');

 const issue={state:'CLOSED',owner:'A',return_to:'CP02.13',result_ref:'TEST',origin_readback_ref:'TEST',fixed_by:'A',verified_by:'B'};auditIssue(issue);assert.throws(()=>auditIssue({...issue,verified_by:'A'}));assert.throws(()=>auditIssue({...issue,state:'SUPERSEDED',replacement_ref:'new'}));cases+=3;
 const gate={binding:'TEST-binding',scope:'TEST',reviews:['OpenAI','Anthropic'].map(v=>({vendor:v,decision:'APPROVE',binding:'TEST-binding',scope:'TEST',reviewer:v,evidence_ref:'TEST',reviewed_at:now}))};assert(reviewConsensus(gate));gate.reviews[1].binding='old';assert(!reviewConsensus(gate));gate.reviews=[];assert(!reviewConsensus(gate));cases+=3;
 console.log(JSON.stringify({p51_general_rules:cases,scope:'NEW_APPLICATION_TEST_NOT_REAL_WORK',state:'PASS'}));
}

// P52 retained regression cases: actual temporary Git commits, no VPS/PG writes.
{
 const os=require('os'),p=require('path'),tmp=fs.mkdtempSync(p.join(os.tmpdir(),'tqt-receipt-'));
 try{
  const d=r.detailed_workflow_history.find(x=>x.version==='0.9-manual-applicability'),id='TEST-P52-NEW',date='2026-10-13T00:00:00Z',script=__filename;
  const b={application_id:id,target_version:'TEST-v1',process_version:d.version,definition_sha256:d.source_sha256,events:[],cycle:{milestone_events:[{event_id:'E1',application_id:id,checkpoint:'CP01',kind:'STARTED'}]}};
  const raw='<script id="tqt-composite-processes">'+JSON.stringify({catalog:{detailed_workflow:d,work_schedule:{records:[{detail_tracking:b}]}}})+'</script>',file=p.join(tmp,'view.html'),input=p.join(tmp,'input.json');fs.writeFileSync(file,raw);
  const git=a=>cp.execFileSync('git',['-C',tmp,...a],{encoding:'utf8',stdio:['ignore','pipe','pipe']}).trim();git(['init']);git(['config','user.name','TEST']);git(['config','user.email','test@example.invalid']);git(['add','view.html']);git(['commit','-m','TEST milestone']);const commit=git(['rev-parse','HEAD']);
  const receipt=gitReceipt(tmp,commit,'view.html','E1');b.cycle.milestones=[{checkpoint:'CP01',start_receipt:receipt}];
  function run(dossier,view=file,extra={}){fs.writeFileSync(input,JSON.stringify({dossier,...extra}));return cp.spawnSync(process.execPath,[script,view,'--validate-dossier',input],{encoding:'utf8'});}
  assert.equal(run(b).status,0,'REAL_GIT_RECEIPT');const fake=JSON.parse(JSON.stringify(b));fake.cycle.milestones[0].start_receipt.commit='a'.repeat(40);assert.notEqual(run(fake).status,0,'FORGED_COMMIT');
  const wrong=JSON.parse(JSON.stringify(b));wrong.cycle.milestones[0].start_receipt.server_committed_at=date;assert.notEqual(run(wrong).status,0,'WRONG_TIME');
  const offline=p.join(tmp,'offline');fs.mkdirSync(offline);fs.writeFileSync(p.join(offline,'view.html'),raw);const unverified=run(fake,p.join(offline,'view.html'),{server_receipts:[fake.cycle.milestones[0].start_receipt]});assert.equal(unverified.status,0,unverified.stderr);assert.equal(JSON.parse(unverified.stdout).state,'UNVERIFIED');assert.notEqual(run(fake,p.join(offline,'view.html'),{require_complete:true}).status,0);
  const review={event_id:'R',revision:1,at:date,actor:'TEST',application_id:id,target_version:'TEST-v1',process_version:d.version,definition_sha256:d.source_sha256,step_id:'CP03.05',item_key:'contract',performed:'DONE',actual_action:'TEST',evidence_ref:'TEST',review:{subject_actor:'Codex Host',reviewer:'Codex Reviewer',subject_vendor:'OpenAI',reviewer_vendor:'OpenAI',evidence_ref:'TEST',target_version:'TEST-v1'}};
  const reviewed={...b,events:[review]};assert.notEqual(run(reviewed).status,0,'SAME_VENDOR');review.review.reviewer_vendor='Anthropic';review.review.reviewer='Claude';assert.equal(run(reviewed).status,0,'CROSS_VENDOR');delete review.review.subject_vendor;assert.notEqual(run(reviewed).status,0,'MISSING_VENDOR');
  console.log('P52: 8 Git receipt/offline/forgery/vendor regression cases PASS; TEST only');
 }finally{fs.rmSync(tmp,{recursive:true,force:true});}
}


validateFieldRegistry(r.field_registry,r.work_master_designs.records);
{const bad=JSON.parse(JSON.stringify(r.field_registry));bad.records.push({...bad.records[0],id:'TEST-DUPLICATE',usage_refs:[]});assert.throws(()=>validateFieldRegistry(bad,r.work_master_designs.records),/DUPLICATE_FIELD_MEANING/);}
// Compact workflow regressions are TEST-only; they do not add real work events.
{const def=JSON.parse(JSON.stringify(r.detailed_workflow_history.find(x=>x.version==='0.9-manual-applicability')||r.detailed_workflow)),id='TEST-COMPACT',t='2026-10-13T01:00:00Z',base={application_id:id,target_version:'1',events:[],cycle:{}},event={step_id:'CP01.04',performed:'DONE',at:t,execution_mode:'MANUAL_ASSISTED',obligation_checks:def.step_policies['CP01.04'].members.map(step_id=>({step_id,state:'PASS',evidence_ref:'TEST'}))};
 const copy=x=>JSON.parse(JSON.stringify(x)),b=copy(base);b.events=[event];validateCompact(b,def);let n=1;const rejects=(change,code)=>{const x=copy(b),d=copy(def);change(x,d);assert.throws(()=>validateCompact(x,d),new RegExp(code));n++;};
 rejects(x=>x.events[0].obligation_checks.pop(),'MERGED_OBLIGATIONS');rejects(x=>delete x.events[0].execution_mode,'MANUAL_FALLBACK');
 rejects((x,d)=>{d.step_policies['CP01.04'].automation_current='HAS_COMMAND';d.step_policies['CP01.04'].command='TEST';d.step_policies['CP01.04'].last_real_run_ref='TEST';},'AUTOMATED_RECEIPT');
 rejects(x=>{x.cycle.applicability=[{step_id:'CP04.10',state:'NOT_APPLICABLE',evaluated_by:'MACHINE'}];},'APPLICABILITY_EVIDENCE');
 rejects(x=>{x.cycle.applicability=[{step_id:'CP01.04',state:'NOT_APPLICABLE',evaluated_by:'MACHINE'}];},'MANDATORY_NOT_APPLICABLE');
 rejects(x=>{x.cycle.milestones=[{checkpoint:'CP01',start_receipt:{server_committed_at:'2026-10-13T02:00:00Z'},end_receipt:{server_committed_at:'2026-10-13T03:00:00Z'}}];},'EVENT_OUTSIDE_MILESTONE');
 rejects(x=>x.cycle.resume_from='TEST-OLD','RESUME_RECHECK');
 const x=copy(b);x.cycle.milestones=[{checkpoint:'CP01',start_receipt:{server_committed_at:t},end_receipt:{server_committed_at:t}}];validateCompact(x,def);n++;
 const a=copy(base);a.cycle.applicability=[{step_id:'CP04.10',state:'NOT_APPLICABLE',evaluated_by:'MACHINE',evidence_ref:'TEST',evaluation_receipt:'TEST-R'}];a.cycle.master_records={'CAT-229*':[{record_id:'TEST-R',application_id:id,target_version:'1',step_id:'CP04.10',state:'SUCCESS',tool_id:'TQT-CHECK-005',evidence_ref:'TEST',at:t}]};validateCompact(a,def);n++;a.cycle.applicability[0].state='UNKNOWN';validateCompact(a,def);n++;

 const auto=copy(b),ad=copy(def);ad.step_policies['CP01.04'].automation_current='HAS_COMMAND';ad.step_policies['CP01.04'].command='TEST-command';ad.step_policies['CP01.04'].last_real_run_ref='TEST-proof';auto.events[0].execution_mode='AUTOMATED';auto.events[0].tool_run_id='TEST-AUTO';auto.cycle.master_records={'CAT-229*':[{record_id:'TEST-AUTO',application_id:id,target_version:'1',step_id:'CP01.04',state:'SUCCESS',tool_id:'TQT-CHECK-005',evidence_ref:'TEST',at:t}]};validateCompact(auto,ad);n++;auto.cycle.master_records['CAT-229*'][0].application_id='OTHER';assert.throws(()=>validateCompact(auto,ad),/AUTOMATED_RECEIPT/);n++;
 const tiny=copy(def);tiny.step_policies={'CP01.04':tiny.step_policies['CP01.04']};const revised=copy(x);revised.events.push({...copy(event),performed:'BLOCKED'});assert.throws(()=>validateCompact(revised,tiny,{require_complete:true}),/APPLICABLE_STEP_INCOMPLETE/);n++;
 assert.throws(()=>validateCompact(a,def,{require_complete:true}),/APPLICABLE_STEP_INCOMPLETE/);n++;
 console.log(JSON.stringify({p53_cases:n,state:'PASS',scope:'TEST_NOT_REAL_WORK'}));}

// Existing regression fixtures describe the historical G1 baseline. Validate the live cycle above, then isolate those fixtures from the new run.
const liveCycleBindings=r.work_schedule.records.map(w=>w.detail_tracking);for(const w of r.work_schedule.records){if(w.detail_tracking?.cycle)w.detail_tracking={...w.detail_tracking,cycle:undefined,events:[],mode:'REFERENCE_ONLY',process_version:r.detailed_workflow.version,definition_sha256:r.detailed_workflow.source_sha256};}

function validate(r){
 const s=r.work_schedule, defs=r.work_master_designs.records, by=new Map(s.records.map(x=>[x.record_id,x]));
 assert.equal(s.master_code,'CAT-227*');assert.equal(by.size,s.records.length);assert.equal(new Set(s.records.map(x=>x.order)).size,s.records.length);
 assert.equal(new Set(defs.map(x=>x.code)).size,defs.length);
 for(const d of defs){assert(r.work_form.record_control.masters.some(m=>m.code===d.code&&m.name===d.name));assert.equal(d.parent,'UI.MASTER');assert.equal(d.state,'DESIGN_ONLY');assert(new Set(d.fields.map(f=>f.key)).size===d.fields.length);for(const col of d.columns)assert(d.fields.some(f=>f.key===col.key));}
 const visiting=new Set(),done=new Set();function visit(id){assert(by.has(id),'missing dependency');assert(!visiting.has(id),'cycle');if(done.has(id))return;visiting.add(id);for(const dep of by.get(id).depends_on)visit(dep);visiting.delete(id);done.add(id);}for(const id of by.keys())visit(id);
 assert.equal(s.display_code,'DEF 00.1');assert.equal(s.display_order,0.1);assert.equal(s.master_identity.key,s.master_code);
 for(const x of s.records){assert(['T0','T0.5','T1','T2','T3'].includes(x.target_tier));assert(s.lifecycle.states[x.lifecycle_state]);for(const k of ['actual_start','actual_finish','planned_start','planned_finish']){assert(x[k]===null||/^\d{4}-\d{2}-\d{2}(T.*)?$/.test(x[k]));}assert(!x.actual_finish||x.actual_start&&x.actual_finish>=x.actual_start);}
 const a=r.application_preview.record, pool=[a,...(s.applications||[])], apps=new Map(pool.map(a=>[a.application_id,a]));assert.equal(apps.size,pool.length,'DUPLICATE_APPLICATION');
 for(const x of s.records){assert(x.record_id&&x.process_code==='MOW-TH-005'&&x.process_version===r.records.find(p=>p.code===x.process_code).version);if(x.application_id){const current=apps.get(x.application_id);assert(current&&x.target_code===current.target_code&&x.target_version===current.target_version);assert(current.process_code===x.process_code&&current.process_version===x.process_version);assert(x.application_ref===(current===a?r.application_preview.source_ref:current.source_ref));assert(x.application_refs.includes(x.application_id));assert.equal(x.state_source,current===a?'catalog.application_preview.record':'catalog.work_schedule.applications');}else{assert(!x.application_ref);assert(!x.completion_evidence);}}
 return true;
}
// P40: definitions and dossier rendering, reused CHECK005 (no new DOT).
{
 const crypto=require('crypto'),path=require('path');
 const md=fs.readFileSync(path.join(path.dirname(process.argv[2]||__dirname+'/view.html'),'MOW-TH-006.md'),'utf8');
 const def=r.detailed_workflow;
 assert(!/(hồsơ|ngườirà|71bước|khôngký|chưanghiệmthu)/.test(md),'UNREADABLE_NEW_PROSE');
 assert.equal(def.source_sha256,crypto.createHash('sha256').update(md).digest('hex'),'QT006_SOURCE_DRIFT');
 const parsed=[...md.matchAll(/^### (CP\d+\.\d+) · (.*)$/gm)].map(m=>m.slice(1));
 assert.deepEqual(def.groups.flatMap(g=>g.rows.map(x=>x.slice(0,2))),parsed,'QT006_PROJECTION_DRIFT');assert.equal(parsed.length,def.step_count);assert.equal(new Set(parsed.map(x=>x[0])).size,def.step_count);
 assert.deepEqual(def.groups.map(g=>g.rows.length),[8,18,11,15,8,4,7]);const legacy=r.detailed_workflow_history.find(x=>x.version==='0.7-completion-contract').groups.flatMap(g=>g.rows.map(x=>x[0]));assert.deepEqual(Object.keys(def.legacy_step_map).sort(),legacy.sort());assert(Object.values(def.legacy_step_map).every(id=>parsed.some(x=>x[0]===id)));assert(parsed.findIndex(x=>x[0]==='CP01.02')<parsed.findIndex(x=>x[0]==='CP01.04'));assert.equal(def.execution_policy.independent_review_steps.includes('CP06.04'),false,'OWNER_NOT_VENDOR_REVIEW');
 const pos=id=>parsed.findIndex(x=>x[0]===id);assert(pos('CP02.23')<pos('CP02.21'));assert(pos('CP02.21')<pos('CP03.08'));assert(pos('CP05.10')<pos('CP06.03'));assert.equal(pos('CP07.08'),def.step_count-1);assert.equal(pos('CP07.05'),-1);
 assert.equal(r.records.filter(x=>x.code==='MOW-TH-006').length,1);assert.equal(r.records.find(x=>x.code==='MOW-TH-006').child_refs[0].relation,'operational_detail_for');assert(!r.records.find(x=>x.code==='MOW-TH-005').child_refs.some(x=>x.code==='MOW-TH-006'));
 for(const b of def.master_bindings){const m=r.work_form.record_control.masters.find(x=>x.code===b.code);assert(m&&m.home===b.home&&m.name===b.name);}
 if(adapter){
  const A=globalThis.TQT_WORK_MASTER,w=r.work_schedule.records[0],before=JSON.stringify(w),m=A.detailModel(r,w);assert.equal(m.count,def.step_count);assert.equal(m.done,0);assert.equal(m.mode,'REFERENCE_ONLY');assert.equal(m.errors.length,0);
  const out=A.dossierView(r,{metadata:w}).html;assert(out.indexOf('<details class="tqt-recording-groups"')<out.indexOf('<details class="qt006-dossier"'));assert.equal((out.match(/class="qt006-group"/g)||[]).length,7);assert.equal((out.match(/data-qt006-step=/g)||[]).length,def.step_count);assert(!/<details[^>]*class="(?:qt006-dossier|qt006-group|tqt-recording-groups)"[^>]*\bopen\b/.test(out));assert.equal(JSON.stringify(w),before);
  assert.equal(A.detailModel(r,r.work_schedule.records[1]).mode,'UNOPENED');
  assert(m.groups.flatMap(g=>g.rows).every(x=>x.actual===null),'NO_PREFILLED_ACTUALS');assert(!out.includes('Công cụ dùng lại theo việc cần làm'));assert(out.includes('Tool đã dùng'));assert(!out.includes('Tool dùng lại'));
  const base=JSON.parse(JSON.stringify(w.detail_tracking));let neg=0;
  for(const key of ['application_id','target_version','process_version','definition_sha256']){w.detail_tracking={...base,[key]:'OTHER'};assert(A.detailModel(r,w).errors.length);neg++;}
  for(const step of ['CP01.01','CP05.04']){w.detail_tracking={...base,events:[{event_id:'TEST-FAKE',step_id:step,status:'DONE',adjustment:'NA',item_key:'P02',revision:1,application_id:w.application_id,target_version:w.target_version,process_version:def.version,definition_sha256:def.source_sha256,actor:'TEST',at:'2026-10-13T00:00:00Z'}]};const n=A.detailModel(r,w);assert.equal(n.done,0);assert(n.groups.flatMap(g=>g.rows).find(x=>x.definition[0]===step).status==='Vướng');neg++;}
  const ev={event_id:'P42-FIXTURE',step_id:'CP01.01',item_key:'P01',revision:1,application_id:w.application_id,target_version:w.target_version,process_version:def.version,definition_sha256:def.source_sha256,actor:'TEST',at:'2026-10-13T00:00:00Z',performed:'DONE',actual_action:'Đã kiểm fixture',result_ref:'TEST-only',tool_uses:['EXACT-USED-TOOL']};
  w.detail_tracking={...base,events:[ev]};let row=A.detailModel(r,w).groups[0].rows[0];assert.equal(row.actual.tools,'EXACT-USED-TOOL');assert.equal(row.done,false);
  w.detail_tracking.events=[{...ev,performed:'NOT_DONE',reason:'Nhánh không phát sinh',tool_uses:[]}];row=A.detailModel(r,w).groups[0].rows[0];assert.equal(row.actual.tools,'');assert(row.actual.confirmation.startsWith('Không làm'));assert.equal(row.done,false);
  w.detail_tracking.events=[{...ev,application_id:'OTHER'}];assert.equal(A.detailModel(r,w).groups[0].rows[0].actual,null);
  w.detail_tracking={...base,added_steps:[{id:'BS-001',after_step:'CP01.01',action:'Bước riêng TEST',reason:'Phát sinh thật',completion:'Có bằng chứng'}],events:[]};let extra=A.detailModel(r,w);assert.equal(extra.count,def.step_count+1);assert.equal(extra.groups[0].rows[1].definition[0],'BS-001');assert.equal(extra.groups[0].rows[1].actual,null);
  w.detail_tracking.added_steps[0].id='CP01.99';assert(A.detailModel(r,w).errors.length);
  w.detail_tracking={...base,events:[{...ev,performed:'BLOCKED',reason:'Thiếu đầu vào'}]};assert.equal(A.detailModel(r,w).groups[0].rows[0].actual.confirmation,'Bị chặn');
  w.detail_tracking=base;const helpUI=A.dossierView(r,{metadata:w}).html;assert(helpUI.includes('Hướng dẫn: Tình trạng'));assert(helpUI.includes('Hướng dẫn: CP01.01'));assert(!helpUI.includes('Ô trống = chưa ghi nhận;'));assert(!helpUI.includes('>Quy định ↗</a>'));
  for(const g of r.work_form.record_control.guidance){assert(helpUI.includes('Hướng dẫn: '+g.id));assert(helpUI.includes(g.instruction.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;')));}
  for(const label of ['Xong','Phải ghi gì?','Master List nào?','Đã ghi','Đối chiếu','Còn thiếu / chi tiết'])assert(helpUI.includes('Hướng dẫn: '+label));assert(!helpUI.includes('>Quy định cách ghi ↗</a>'));
  w.detail_tracking=base;assert.equal(JSON.stringify(w),before);console.log(JSON.stringify({qt006_steps:def.step_count,groups:7,negative_cases:neg,state:'READ_ONLY_DOSSIER_VERIFIED',real_execution:'NOT_RUN'}));
 }
}

validate(r);
// P45: a repeat application is checked by identity and source, never by old G1 alone.
{const q=cloneFixture(r), old=q.application_preview.record, w=q.work_schedule.records[0];const fresh={application_id:'TEST-P45-SECOND',target_code:w.target_code,target_version:w.target_version,process_code:w.process_code,process_version:w.process_version,source_ref:'TEST-only/new-application'};q.work_schedule.applications=[fresh];w.application_id=fresh.application_id;w.application_ref=fresh.source_ref;w.application_refs=[old.application_id,fresh.application_id];w.state_source='catalog.work_schedule.applications';validate(q);fresh.target_version='WRONG';assert.throws(()=>validate(q));fresh.target_version=w.target_version;w.application_ref='OLD-PATH';assert.throws(()=>validate(q));w.application_ref=fresh.source_ref;q.work_schedule.applications.push(fresh);assert.throws(()=>validate(q));}
let rejected=0;
for(const change of [x=>x.work_schedule.records.push(x.work_schedule.records[0]),x=>x.work_schedule.records[1].order=1,x=>x.work_schedule.records[0].depends_on=['TQT-VIEC-002'],x=>x.work_schedule.records[1].depends_on=['UNKNOWN'],x=>x.work_schedule.records[0].application_id='OTHER',x=>x.work_schedule.records[0].target_version='OLD',x=>x.work_schedule.records[0].application_ref='OTHER',x=>x.work_master_designs.records[0].code='MISSING',x=>x.work_master_designs.records[0].columns.push({key:'unknown'}),x=>x.work_schedule.records[1].completion_evidence='FAKE',x=>x.work_schedule.records[0].target_tier='CTCM',x=>x.work_schedule.records[0].lifecycle_state='UNKNOWN',x=>x.work_schedule.records[0].actual_finish='2026-01-01',x=>x.work_schedule.display_code='DEF001']){const c=cloneFixture(r);change(c);assert.throws(()=>validate(c));rejected++;}
if(adapter){const A=globalThis.TQT_WORK_MASTER;r.source_url='https://example.test/view.html';const list=A.scheduleRows(r);assert.equal(list.length,2);assert(list[0].dossier_url.endsWith('#tqt-recording-list'));assert.equal(list[1].dossier_url,null);assert.equal(list[1].state,'Ghi danh');for(const d of r.work_master_designs.records){const cfg=A.configure({}, {tqt:r,masterCode:d.code,sample:false});assert.equal(cfg.mother,'DEF');assert(cfg.definitionColumns.length);const sample=A.configure({}, {tqt:r,masterCode:d.code,sample:true});assert.equal(sample.items.length,1);assert(sample.items[0].form_schema.fields.length);assert(sample.items[0].code.startsWith('MAU-'));}assert.equal(A.indexRows(r).length,r.work_master_designs.records.length);
 assert.equal(A.indexRows(r)[0].code,'CAT-227');assert.equal(A.indexRows(r)[0].humanNo,'0.1');
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
 const cfg=A.configure({}, {tqt:r,masterCode:'DEF00.1',sample:false});const view=cfg.detailRenderer(cfg,cfg.items[0]);assert(view.fullWidth&&view.interactive);assert(view.html.includes('.tqt-status-tick:checked{background:#16803c'));assert.equal((view.html.match(/type="checkbox"/g)||[]).length,18);assert.equal((view.html.match(/type="checkbox" disabled/g)||[]).length,18);assert.equal((view.html.match(/ checked /g)||[]).length,d.checkpoints.filter(x=>x.done).length+d.groups.filter(x=>x.done).length); // UI must follow actual evidence, not a frozen empty fixture.
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

// P54: executable completion path, no real application records written.
{const def=JSON.parse(JSON.stringify(r.detailed_workflow_history.find(x=>x.version==='0.9-manual-applicability')||r.detailed_workflow)),t='2026-10-14T01:00:00Z',b={application_id:'TEST-P54',target_version:'TEST-V1',process_version:def.version,definition_sha256:def.source_sha256,events:[],cycle:{applicability:[],master_records:{'CAT-015':[]},milestones:Array.from({length:7},(_,i)=>({checkpoint:'CP0'+(i+1),start_receipt:{server_committed_at:t},end_receipt:{server_committed_at:t}}))}},copy=x=>JSON.parse(JSON.stringify(x));let cases=0;
 function addNA(step){const a={step_id:step,state:'NOT_APPLICABLE',evaluated_by:'AI',execution_mode:'MANUAL_ASSISTED',actor:'Claude Worker',subject_vendor:'Anthropic',evidence_ref:'TEST-condition-'+step,at:t,revision:1,review_ref:'TEST-review-'+step};b.cycle.applicability.push(a);b.cycle.master_records['CAT-015'].push({record_id:a.review_ref,application_id:b.application_id,target_version:b.target_version,process_version:b.process_version,definition_sha256:b.definition_sha256,step_id:'CP05.03',decision:'APPROVE',assessment_binding:assessmentBinding(b,a),evidence_ref:'TEST-reviewed-'+step,at:t,review:{subject_vendor:'Anthropic',reviewer_vendor:'OpenAI',reviewer:'GPT Reviewer'}});}
 for(const [id,p] of Object.entries(def.step_policies)){if(p.applicability==='CONDITIONAL')addNA(id);else b.events.push({step_id:id,performed:'DONE',execution_mode:'MANUAL_ASSISTED',at:t,obligation_checks:p.members.map(step_id=>({step_id,state:'PASS',evidence_ref:'TEST'}))});}
 validateCompact(b,def,{require_complete:true});cases++;
 const fail=(change,pattern='APPLICABILITY_EVIDENCE')=>{const x=copy(b),d=copy(def);change(x,d);assert.throws(()=>validateCompact(x,d,{require_complete:true}),new RegExp(pattern));cases++;};
 fail(x=>x.cycle.master_records['CAT-015'].shift());
 fail(x=>x.cycle.master_records['CAT-015'][0].review.reviewer_vendor='Anthropic');
 fail(x=>x.cycle.master_records['CAT-015'][0].application_id='OTHER');
 fail(x=>x.cycle.applicability[0].evidence_ref='CHANGED');
 fail(x=>x.cycle.master_records['CAT-015'][0].step_id='CP06.04');
 fail((x,d)=>d.execution_policy.applicability_evaluator.automation_current='HAS_COMMAND');
 fail(x=>x.cycle.applicability[0].state='UNKNOWN','APPLICABLE_STEP_INCOMPLETE');
 fail(x=>x.cycle.applicability[0].step_id='CP01.01','MANDATORY_NOT_APPLICABLE');
 if(adapter){const A=globalThis.TQT_WORK_MASTER,a=b.cycle.applicability[0];assert.equal(A.stepApplicability(b,a.step_id,def),'NOT_APPLICABLE');const bad=copy(b);bad.cycle.master_records['CAT-015'][0].assessment_binding='OLD';assert.equal(A.stepApplicability(bad,a.step_id,def),'UNKNOWN');cases+=2;}
 const f=copy(r.field_registry);f.collision_decisions=f.collision_decisions.filter(x=>x.decision!=='KEEP');assert.throws(()=>validateFieldRegistry(f,r.work_master_designs.records),/FIELD_COLLISION_DECISION/);cases++;
 const f2=copy(r.field_registry),x=f2.records.find(x=>x.key==='checkpoint');f2.records.push({...x,id:'TEST-UNDECIDED',semantic_key:'different-meaning',usage_refs:[]});f2.new_registry_fields++;assert.throws(()=>validateFieldRegistry(f2,r.work_master_designs.records),/FIELD_COLLISION_MEMBERS/);cases++;
 console.log(JSON.stringify({p54_cases:cases,steps:71,manual_assessments:b.cycle.applicability.length,completion:'PASS_TEST_ONLY'}));}

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
 assert.equal(A.relatedRows(r,'CAT-015').length,r.tool_registry.audit_projection.last_checks.length+(r.application_preview.record.execution_walk?.steps.length||0)+(r.application_preview.record.test_cases?.length||0));assert.equal(A.relatedRows(r,'CAT-025').length,r.tool_registry.reviews.length+(r.application_preview.record.decisions||[]).length+(r.application_preview.record.start_confirmation?.state==='CONFIRMED'?1:0));assert.equal(A.relatedRows(r,'CAT-016').length,r.tool_registry.changes.length+r.application_preview.record.trial_records.filter(x=>x.requirement_code==='CHANGE').length+(r.governance?.repairs||[]).length);assert.equal(A.relatedRows(r,'CAT-229*')[0].state,r.tool_registry.walkthrough.finished_at?'Đã trả kết quả':'Đang làm');assert.equal(A.relatedRows(r,'CAT-069?').length,(r.tool_registry.walkthrough?.findings.length||0)+(r.tool_registry.walkthrough_runs||[]).reduce((n,x)=>n+(x.findings||[]).length,0)+(r.application_preview.record.execution_walk?.findings.length||0));
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
 const legacyR={...r,work_schedule:{...r.work_schedule,records:r.work_schedule.records.map(w=>({...w,control:undefined}))}};const list=A.scheduleRows(legacyR),own=A.dossierView(legacyR,{metadata:list[0]}).html,waiting=A.dossierView(legacyR,{metadata:list[1]}).html;
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

if(adapter){for(const run of r.tool_registry.walkthrough_runs||[]){const A=globalThis.TQT_WORK_MASTER;assert(A.relatedRows(r,'CAT-229*').some(x=>x.record_id===run.run_id&&x.scope===run.scope));for(const f of run.findings)assert(A.relatedRows(r,'CAT-069?').some(x=>x.record_id===f.id&&x.application_id===run.run_id&&x.scope===run.scope));}}

if(adapter){const A=globalThis.TQT_WORK_MASTER;const q=cloneFixture(r);q.work_schedule.records.forEach((w,i)=>w.detail_tracking=liveCycleBindings[i]);assert.equal(auditRecordedCycle(A,q).state,'PASS');const b=q.work_schedule.records.find(w=>w.detail_tracking?.cycle)?.detail_tracking;if(b){const copy=JSON.parse(JSON.stringify(b));q.work_schedule.records.find(w=>w.detail_tracking?.cycle).detail_tracking=copy;const e=copy.events.find(e=>e.performed==='DONE');if(e){e.completed_at='2000-01-01T00:00:00Z';assert.equal(auditRecordedCycle(A,q).state,'FAIL');}assert(A.dossierView(r,{metadata:r.work_schedule.records[0]}).html.includes('Thời gian hoàn thành'));}}

// P58: every current issue must be projected once, no stale copied state or empty visible cells.
if(adapter){const A=globalThis.TQT_WORK_MASTER;function checkIssues(q){const rows=A.relatedRows(q,'CAT-069?');for(const w of q.work_schedule.records||[])for(const x of w.detail_tracking?.cycle?.issues||[]){const hit=rows.filter(y=>y.record_id===x.id);assert.equal(hit.length,1,'ISSUE_PROJECTION_UNIQUE');assert.equal(hit[0].problem,x.problem,'ISSUE_PROJECTION_PROBLEM');assert.equal(hit[0].next,x.next_action,'ISSUE_PROJECTION_NEXT');assert.equal(hit[0].state_code,x.state,'ISSUE_PROJECTION_STATE');assert(!rows.some(y=>y.record_id!==x.id&&y.record_id.endsWith('-'+x.id)),'ISSUE_PROJECTION_OLD_ALIAS');}for(const x of rows)assert(x.problem&&x.owner&&x.next&&x.state,'ISSUE_VISIBLE_FIELDS');return rows;}
 const live=cloneFixture(r);live.work_schedule.records.forEach((w,i)=>w.detail_tracking=liveCycleBindings[i]);const rows=checkIssues(live);const q=cloneFixture(live),w=q.work_schedule.records.find(x=>x.detail_tracking?.cycle);w.detail_tracking={...w.detail_tracking,cycle:{...w.detail_tracking.cycle,issues:w.detail_tracking.cycle.issues.map(x=>({...x}))}};w.detail_tracking.cycle.issues[0].state='FIXING';w.detail_tracking.cycle.issues[0].next_action='TEST changed at source';checkIssues(q);w.detail_tracking.cycle.issues.push({id:'TEST-P58-NEW',problem:'TEST new issue',owner:'TEST',state:'OPEN',next_action:'TEST next'});assert(checkIssues(q).some(x=>x.record_id==='TEST-P58-NEW'));assert.equal(rows.length+1,A.relatedRows(q,'CAT-069?').length);console.log('P58 issue projection PASS: source edits/new issues propagate; old aliases suppressed; visible fields complete; TEST only');}

// P60: positive controls and corruptions, all TEST-only and no live records changed.
{const copy=x=>JSON.parse(JSON.stringify(x)),def=r.detailed_workflow;let cases=0;
 const base={control:{objective:{goal:'TEST goal',recipient:'TEST recipient',exclusions:'No production',products:[{id:'P',check_ref:'TEST'}],criteria:[{id:'C',measure:'TEST measurable',check:'TEST method'}]},steps:[],milestones:[],required_gates:[]}};
 const b=controlBinding(base.control.objective);base.control.owner_start={actor:'Owner',decision:'APPROVE',binding:b,evidence_ref:'TEST approval'};
 base.control.cases=[{criterion_id:'C',expected:'TEST',method:'TEST'}];
 assert.equal(validateControl(base,def,{start:true,prepared:true}).state,'PASS');cases++;const draft={control:{objective:{}}};assert.equal(validateControl(draft,def).state,'PASS');assert(!validateControl(draft,def).card.done);assert(validateControl(draft,def,{start:true}).errors.includes('OBJECTIVE_FIVE_FIELDS'));cases++;
 const reject=(mut,code)=>{let x=copy(base);mut(x);assert(validateControl(x,def,{start:true,prepared:true}).errors.includes(code),code);cases++;};
 reject(x=>delete x.control.objective.goal,'OBJECTIVE_FIVE_FIELDS');reject(x=>x.control.owner_start=null,'OWNER_START_REQUIRED');reject(x=>x.control.objective.goal='changed','OWNER_START_REQUIRED');reject(x=>x.control.cases=[],'CRITERION_CASE_MISSING');
 reject(x=>x.control.steps=[{step_id:'CP01.02',state:'DONE',evidence_ref:'TEST'}],'STEP_ORDER');reject(x=>x.control.steps=[{step_id:'CP01.01',state:'DONE'}],'STEP_EVIDENCE');reject(x=>x.control.milestones=[{state:'DONE'}],'MILESTONE_REPORT');reject(x=>x.control.claimed_card={done:true},'MANUAL_CARD_COLOR');
 assert(!validateControl(base,def,{complete:true}).card.done);cases++;
 const complete=copy(base);complete.control.results=[{criterion_id:'C',result:'PASS',evidence_ref:'TEST',objective_binding:b}];complete.control.field_inventory={state:'COMPLETE',ids:[],new_design_count:0,evidence_ref:'TEST inventory'};complete.control.required_gates=[{binding:'TEST product',scope:'TEST',reviews:['OpenAI','Anthropic','Owner'].map(v=>({vendor:v,decision:'APPROVE',binding:'TEST product',scope:'TEST',reviewer:v,evidence_ref:'TEST'}))}];complete.control.milestones=Array.from({length:7},(_,i)=>({checkpoint:'CP0'+(i+1),state:'DONE',server_receipt:'TEST-'+i,report:['where','done','block','next']}));complete.control.steps=Object.keys(def.step_cards).map(step_id=>({step_id,state:'DONE',evidence_ref:'TEST'}));complete.control.steps=Object.keys(def.step_cards).map(step_id=>({step_id,state:'DONE',evidence_ref:'TEST'}));complete.control.steps=Object.keys(def.step_cards).map(step_id=>({step_id,state:'DONE',evidence_ref:'TEST'}));complete.control.milestones.forEach(m=>m.report=milestoneReport(complete,m));complete.control.steps=Object.keys(def.step_cards).map(step_id=>({step_id,state:'DONE',evidence_ref:'TEST'}));complete.control.steps=Object.keys(def.step_cards).map(step_id=>({step_id,state:'DONE',evidence_ref:'TEST'}));complete.control.steps=Object.keys(def.step_cards).map(step_id=>({step_id,state:'DONE',evidence_ref:'TEST'}));complete.control.steps=Object.keys(def.step_cards).map(step_id=>({step_id,state:'DONE',evidence_ref:'TEST'}));complete.control.steps=Object.keys(def.step_cards).map(step_id=>({step_id,state:'DONE',evidence_ref:'TEST'}));complete.control.steps=Object.keys(def.step_cards).map(step_id=>({step_id,state:'DONE',evidence_ref:'TEST'}));complete.control.steps=Object.keys(def.step_cards).map(step_id=>({step_id,state:'DONE',evidence_ref:'TEST'}));complete.control.recipient_ack={binding:b,evidence_ref:'TEST'};assert(validateControl(complete,def,{complete:true}).card.done);cases++;
 const missing=copy(complete);missing.control.required_gates[0].reviews.pop();assert(!validateControl(missing,def,{complete:true}).card.done);cases++;
 const changed=copy(base);changed.control.objective.goal='changed';assert(validateControlTransition(base,changed,def).errors.includes('SIGNED_CHANGE_REPAIR'));cases++;
 const bad=(mut,code)=>{const q={governance:copy(r.governance),field_registry:copy(r.field_registry),detailed_workflow:copy(r.detailed_workflow),work_master_designs:r.work_master_designs,work_schedule:copy({records:r.work_schedule.records.map(x=>({short_id:x.short_id}))})};mut(q);assert(validateGovernance(q).errors.includes(code),code);cases++;};
 bad(q=>q.work_schedule.records[1].short_id=q.work_schedule.records[0].short_id,'WORK_CODE');bad(q=>q.governance.masters[0].id='CAT-227*','MASTER_CODE');bad(q=>q.governance.masters.pop(),'MASTER_COVERAGE');bad(q=>q.governance.masters[0].initial_approval={state:'APPROVED'},'MASTER_OWNER_APPROVAL');
 bad(q=>q.field_registry.records[1].db_code=q.field_registry.records[0].db_code,'FIELD_DB_CODE');bad(q=>q.field_registry.records[0].db_code='Bad-Code','FIELD_DB_CODE');bad(q=>q.field_registry.records[1].name=q.field_registry.records[0].name,'FIELD_DISPLAY_NAME');bad(q=>q.field_registry.records[0].description='','FIELD_DESCRIPTION_OR_ORIGIN');bad(q=>q.field_registry.records[0].origin_ref='','FIELD_DESCRIPTION_OR_ORIGIN');bad(q=>q.field_registry.records[0].lifecycle='CREATED','FIELD_PG_PROOF');bad(q=>q.field_registry.records[0].lifecycle_events=[{from:'DESIGNED',to:'ACCEPTED',actor:'TEST',at:'TEST',evidence_ref:'TEST'}],'FIELD_LIFECYCLE_ORDER');bad(q=>delete q.detailed_workflow.step_cards['CP01.01'].input,'STEP_NINE_ANSWERS');bad(q=>delete q.governance.repairs[0].evidence_ref,'REPAIR_FIELDS');
 console.log(JSON.stringify({p60_cases:cases,state:'PASS',scope:'TEST_NOT_QT001_ACCEPTANCE'}));}
