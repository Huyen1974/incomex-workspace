// TEST-ONLY interactive composition. One fixture and one state; no business API or authority.
(() => {
 const F=window.GATE2_FIXTURE, $=id=>document.getElementById(id), clone=x=>JSON.parse(JSON.stringify(x));
 const esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 let S;
 const row=(a,b)=>`<div class="row"><span>${esc(a)}</span>${esc(b)}</div>`;
 const block=(title,body)=>`<section class="n2-block"><h3>${esc(title)}</h3>${body}</section>`;
 const ref=x=>`<div class="trace-ref">${esc(x)}</div>`;
 function record(event,actor='observer',detail='') {
  S.trace.push({n:S.trace.length+1,at:new Date().toISOString(),event,actor,detail,stage:F.stages[S.stage].id,pattern:S.pattern,object:S.context.object_ref,package:S.context.package_ref,scope:S.context.scope,version:S.context.definition_version,revision:S.context.draft_revision,release:S.context.release_ref,instance:S.context.instance_ref,attempt:S.attempt,blocked:!!S.error});
 }
 function reset() {
  const n=F.negatives.find(x=>x.id===$('scenario').value);
  S={stage:n?n.at:0,pattern:F.stages[n?n.at:0].pattern,context:clone(F.context),error:n||null,scenario:n?n.id:'HAPPY',search:'',duration:38,note:'Đã ghi nhận',feedback:'Bổ sung hướng dẫn khi nhập ghi chú',attempt:1,trace:[],human:0,hmitl:0,nav:0,searches:0,machine:0,repair:0};
  if(S.stage>=8)S.context.draft_revision=2;
  S.test=S.stage>=10?{revision:2}:null;S.approval=S.stage>=11?{revision:2,scope:'publish+activate'}:null;S.released=S.stage>=12?{version:1,revision:2}:null;
  if(n?.id==='N03'){S.test={revision:1};S.approval=null;}if(n?.id==='N07')S.approval=null;
  record('start-scenario','test_operator',S.scenario);render();
 }
 function repair() {
  const n=S.error;if(!n)return;
  if(n.human==='machine')S.machine++;else S.human++;
  if(n.id==='N03'||n.id==='N06'){S.context.draft_revision++;S.test=null;S.approval=null;S.stage=8;}
  if(n.id==='N02')S.stage=4;
  if(n.id==='N07'){S.stage=10;S.approval=null;}
  if(n.id==='N08')S.attempt=2;
  S.repair++;S.error=null;S.pattern=F.stages[S.stage].pattern;record('negative-resolved',n.human,n.id+': '+n.resume);render();
 }
 function advance() {
  const stage=F.stages[S.stage];if(S.error||stage.actor==='terminal')return;
  if(stage.actor==='HMITL'){
   const input=$('runtime-duration');if(!input||!input.checkValidity())return input?.reportValidity();
   S.duration=Number(input.value);S.note=$('runtime-note').value;S.hmitl++;
  }else if(stage.actor==='machine')S.machine++;else S.human++;
  if(stage.id==='intent')S.intent=$('intent')?.value||F.intent;
  if(stage.id==='feedback')S.feedback=$('feedback')?.value||S.feedback;
  record('stage-completed',stage.actor,stage.title);
  if(stage.id==='declaration')S.context.draft_revision=Math.max(2,S.context.draft_revision);
  if(stage.id==='test')S.test={revision:S.context.draft_revision};
  if(stage.id==='approval')S.approval={revision:S.context.draft_revision,scope:'publish+activate'};
  if(stage.id==='release')S.released={version:S.context.definition_version,revision:S.context.draft_revision};
  if(stage.id==='improve'){S.context.definition_version=2;S.context.draft_revision++;S.test=null;S.approval=null;}
  S.stage++;S.pattern=F.stages[S.stage].pattern;record('stage-entered','machine_navigation');render();
 }
 function library() {
  let objects=F.objects.filter(x=>!S.search||(x.name+' '+x.family+' '+x.meaning).toLowerCase().includes(S.search.toLowerCase()));
  return block('Nguyên liệu đã tìm trong phạm vi TEST',`<p class="subtle">Nguồn fixture đầy đủ trong lượt happy; không phải kết quả tìm toàn hệ production. Exact không có nghĩa mọi quyền/lifecycle đều đã phù hợp.</p><label>Tìm thủ công (tùy chọn) <input id="catalog-search" value="${esc(S.search)}" placeholder="Tên / family / nghĩa"></label><div class="ml-scroll"><table class="ml-tbl"><thead><tr><th>Nguyên liệu</th><th>Family · version</th><th>Kết quả</th><th>Nghĩa / dùng tại</th></tr></thead><tbody>${objects.map(x=>`<tr><td><strong>${esc(x.name)}</strong>${ref(x.id)}</td><td>${esc(x.family)} · v${x.version}</td><td>${x.status==='missing'&&S.stage<6?'Thiếu — request owner':esc(x.match==='none'?'Đã bổ sung qua request':x.match)}</td><td>${esc(x.meaning)}${ref('Where-used: '+x.where_used.join(', '))}</td></tr>`).join('')}</tbody></table></div>`);
 }
 function review() {
  const ready=S.test?.revision===S.context.draft_revision&&!S.error, released=S.released?.version===S.context.definition_version;
  const form=`<div class="form-preview"><label>Thời lượng dự kiến (phút)<input type="number" value="38" readonly></label>${S.context.draft_revision>=2?'<label>Ghi chú<textarea readonly>Field dùng lại, thêm qua khai báo revision 2</textarea></label>':''}<div class="subtle">Ngày tạo, actor và revision là system fields. Đây là preview, không gửi nghiệp vụ.</div></div>`;
  return `<div class="grid"><div>${block('Ý tưởng → bản khai',S.stage===0?`<label for="intent">Ý tưởng nghiệp vụ</label><textarea id="intent">${esc(F.intent)}</textarea>`:`<p>${esc(S.intent||F.intent)}</p>${ref('MOW → HMITL MOT.capture → AUTO MOT.summary → MOUT.duration')}`)}${block('MOIT dùng chung · preview',form)}</div><aside>${block('1 · Có được phát hành không?',`<span class="pill ${ready?'':'warn'}">${released?'Đã phát hành TEST':S.context.definition_version===2?'Version2 DRAFT · chưa test/duyệt':ready?'Đủ kiểm để xin duyệt TEST':'Chưa đủ điều kiện TEST'}</span>${row('Bản đang rà','v'+S.context.definition_version+' · revision '+S.context.draft_revision)}${row('Quyền/D04','D04 WAITING OWNER trước Gate3 / real pilot')}`)}${block('2 · Đã nối đủ để chạy chưa?',row('Input','Field.so_phut + MOIT.duration')+row('Trigger','Submitted business event')+row('Condition',S.stage>=6?'Condition >60 phút v1':'Thiếu → request owner Condition')+row('Người','Năm nghĩa tách riêng; source TEST'))}${block('3 · Chạy xong biết tốt/xấu bằng gì?',row('MOUT','Kết quả tổng hợp + effect receipt')+row('Kết thúc','Output đủ + điều kiện + audit')+row('Help','Áp dụng releasev1; drift khi xem v2'))}</aside></div>`;
 }
 function expert() {
  return `<div class="grid">${block('Owner editor · Condition',row('Owner','TEST.owner.condition')+row('Định nghĩa','TEST.COND.over60 · version1')+row('Đầu vào','field.so_phut · integer · minute')+row('Biểu thức khai báo','operator > · threshold 60')+row('Write scope','Chỉ Condition definition; không sửa global Field')+`<p class="subtle">Gate3 chọn DSL/operator trong cơ chế có sẵn trước code. Không nhúng biểu thức SQL tự do vào Nuxt.</p>`)}${block('Gói cha vẫn được giữ',row('Package',S.context.package_ref)+row('Parent',S.context.object_ref)+row('Slot','condition.after-capture')+row('Request','TEST.REQ.condition-001')+row('Return',S.context.return_context)+`<div class="flow"><span>Field owner</span><b>→</b><span>Condition owner</span><b>→</b><span>MOW binding</span></div>`)}</div>`;
 }
 function runtime() {
  const st=S.stage<13?'Chờ occurrence':S.stage===13?'Chờ HMITL':S.stage===14?'AUTO queued / running TEST':S.stage===15?'Đối chiếu output TEST':'Completed TEST';
  return `<div class="grid"><div>${block('HMITL · việc của người thực hiện',row('Executor',F.people.executor)+`<div class="form-preview"><label for="runtime-duration">Thời lượng thực tế (phút)</label><input id="runtime-duration" type="number" min="0" step="1" required value="${S.duration}" ${S.stage===13&&!S.error?'':'readonly'}><label for="runtime-note">Ghi chú thực tế</label><textarea id="runtime-note" ${S.stage===13&&!S.error?'':'readonly'}>${esc(S.note)}</textarea></div>`)}${block('MOUT · kết quả / tham chiếu',row('Input đã nộp',S.stage>=14?S.duration+' minute':'Chưa nộp')+row('Kết quả',S.stage>=15&&!S.error?'Có receipt TEST / kiểm slot output':'Chưa hoàn tất')+row('Trạng thái',st))}</div><aside>${block('AUTO · monitor',`<span class="pill ${S.error?'warn':''}">${esc(st)}</span>${row('Capability','guarded-write@1 · TEST')}${row('Release pin',S.context.release_ref)}${row('Instance',S.context.instance_ref)}${row('Attempt','TEST.ATTEMPT.auto-00'+S.attempt)}<p class="subtle">AUTO không có nút Done. Nút diễn tập bên dưới chỉ chuyển fixture để kiểm thiết kế. Worker lab chạy riêng, có logs thật.</p>`)}${block('Năm vai, năm nghĩa',Object.entries(F.people).map(([a,b])=>row(a,b)).join(''))}</aside></div>`;
 }
 function lifecycle() {
  const rev=S.context.draft_revision, test=S.test?.revision===rev&&!S.error?'PASS TEST cho revision '+rev:S.test?'STALE: evidence revision '+S.test.revision:'Chưa chạy cho revision '+rev;
  return `<div class="grid"><div>${block('Readiness · diff · impact · test',row('Packet',S.context.package_ref+' / revision '+rev)+row('Diff',rev>=2?'Thêm binding Condition + Field Ghi chú':'Draft: một Condition còn thiếu')+row('Impact','MOW binding, MOIT preview, MOT input; Field meaning không đổi')+row('Evidence',test)+row('Nguồn','TEST.SUITE.duration-v1 / dependency digest rev'+rev))}${block('Approval → publish → activate',row('Approval ingredient',S.stage>=6?'TEST.DEC.condition-v1 accepted':'Chưa có')+row('Approval workflow',S.approval?.revision===rev?'TEST.DEC.mow-rev'+S.approval.revision+' · publish+activate':'Chưa có decision hợp lệ cho bản đang rà')+row('Published release',S.released?S.context.release_ref+' / revision '+S.released.revision:'Chưa phát hành')+row('Active binding',S.released?'TEST.BINDING.duration → releasev1 (không phải draftv2)':'Chưa kích hoạt')+row('Gate2','PM ACCEPT · DESIGN ONLY · chưa PM ACCEPT'))}</div><aside>${block('Request / owner / resume',row('Request','TEST.REQ.condition-001')+row('Owner','TEST.owner.condition')+row('State',S.stage>=6?'produced → revalidated → resumed':'pending / missing ingredient')+row('Return',S.context.return_context))}${block('Help và phản hồi',row('Help','TEST.GUIDE.duration-v1 · applies_to releasev1')+row('Drift',S.context.definition_version>1?'Cảnh báo: Helpv1 chưa nhận applies_to v2':'Khớp fixture releasev1')+row('Feedback → cải tiến',S.context.definition_version>1?'TEST.FEEDBACK.duration-001 → MOW v2 DRAFT':'Tự gắn trace khi gửi')+`<label for="feedback">Ý kiến cải tiến</label><textarea id="feedback">${esc(S.feedback)}</textarea>${ref('Tự gắn object / scope / revision / instance / release; không nhập raw ID.')}`)}</aside></div>`;
 }
 function render() {
  const st=F.stages[S.stage],c=S.context;
  $('context').innerHTML=`<div><strong>${esc(c.name)}</strong><span data-context="object">${esc(c.object_ref)}</span> · ${esc(c.family)}<div data-context="package">${esc(c.package_ref)}</div></div><div><strong>v${c.definition_version} · revision ${c.draft_revision}</strong><span data-context="scope">${esc(c.scope)}</span><div>Owner: ${esc(c.owner)}</div></div><div><strong>Quay lại đúng gói</strong><span>${esc(c.return_context)}</span><div class="subtle">${S.stage>=13?'Instance giữ':'Kế hoạch pin'} ${esc(c.release_ref)}</div></div>`;
  $('patterns').innerHTML=Object.entries(F.patterns).map(([k,v])=>`<button data-pattern="${k}" aria-pressed="${S.pattern===k}">${k} · ${esc(v)}</button>`).join('');
  document.querySelectorAll('[data-pattern]').forEach(b=>b.onclick=()=>{S.pattern=b.dataset.pattern;S.nav++;record('optional-navigation','observer');render();});
  $('stage-position').textContent=`${S.scenario} · BƯỚC ${S.stage+1}/${F.stages.length}`;$('stage-title').textContent=st.title;$('machine-responsibility').textContent=st.machine;$('actor-tag').innerHTML=`<span class="pill">${esc(st.actor==='machine'?'Máy · mô phỏng':st.actor)}</span>`;
  $('content').innerHTML=({P01:library,P02:review,P03:expert,P04:runtime,P05:lifecycle})[S.pattern]();
  const search=$('catalog-search');if(search)search.onchange=()=>{S.search=search.value;S.searches++;record('manual-search','observer');render();};
  $('error').hidden=!S.error;
  if(S.error)$('error').innerHTML=`<h3>${esc(S.error.id+' · '+S.error.state)}</h3><p>${esc(S.error.finding)}</p><p><b>Máy:</b> ${esc(S.error.machine)}</p><p><b>Resume:</b> ${esc(S.error.resume)}</p><button id="repair" class="n2-btn">${esc(S.error.repair)}</button>`;
  if($('repair'))$('repair').onclick=repair;
  $('advance').textContent=st.action;$('advance').disabled=!!S.error||st.actor==='terminal';
  $('action-explanation').textContent=S.error?'Bước tiếp bị chặn. Xem nguyên nhân và đường phục hồi ở trên.':st.actor==='machine'?'Điều khiển kiểm thử mô phỏng một tool stage. Đường sản phẩm đích phải do máy tự chạy.':st.actor==='HMITL'?'Một thao tác nghiệp vụ của người được giao; không phải điều phối máy.':'Quyết định người có lý do; không tạo authority hoặc trạng thái production.';
  const metrics={'Quyết định H1–H5':S.human,'Nộp HMITL':S.hmitl,'Chuyển màn tùy chọn':S.nav,'Tìm tay':S.searches,'Nhập raw ID':0,'Nhập lại máy biết':0,'Tool stage mô phỏng':S.machine,'Mất context':S.trace.filter(t=>t.object!==F.context.object_ref||t.package!==F.context.package_ref||t.scope!==F.context.scope).length};
  $('metrics').innerHTML=Object.entries(metrics).map(([k,v])=>`<div class="metric"><b>${v}</b>${esc(k)}</div>`).join('');
  $('trace-json').textContent=JSON.stringify({scenario:S.scenario,context:c,metrics,stage:st.id,negative:S.error?.id||null,recovered:S.repair,trace:S.trace},null,2);
 }
 $('scenario').innerHTML='<option value="HAPPY">Happy path · từ ý tưởng đến cải tiến</option>'+F.negatives.map(n=>`<option value="${n.id}">${n.id} · ${esc(n.title)}</option>`).join('');
 $('reset').onclick=reset;$('advance').onclick=advance;reset();
})();
