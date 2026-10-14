/* Standard QTTH006 projection; source/version/hash from catalog only. */
(function(){
'use strict';
const definition=JSON.parse(document.getElementById('tqt-composite-processes').textContent).catalog.detailed_workflow;
const groups=definition.groups;
const sourceHash=definition.source_sha256;
const headers=['Bước','Việc cần làm','Điều kiện xong','Master cần ghi','Công cụ gợi ý (không phải đã dùng)','Quy tắc / nhánh','Ai làm dự kiến','Tự động hiện tại'];
const css="#over-view #tqt006-overview-guide{margin:22px 0;border:1px solid #cddbd2;border-radius:12px;background:#fff;overflow:hidden}\n#over-view #tqt006-overview-guide .qt006-outer>summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:14px;padding:18px 17px;background:#f0f5ef;color:#23412f}\n#over-view #tqt006-overview-guide summary::-webkit-details-marker{display:none}\n#over-view #tqt006-overview-guide summary{cursor:pointer}\n#over-view #tqt006-overview-guide .qt006-summary-text{display:flex;flex-direction:column;gap:4px}\n#over-view #tqt006-overview-guide .qt006-summary-text strong{font-size:18px}\n#over-view #tqt006-overview-guide .qt006-summary-text small{font-size:12px;font-weight:500}\n#over-view #tqt006-overview-guide .qt006-action{font-size:12px;color:#2d6749;font-weight:700;white-space:nowrap}\n#over-view #tqt006-overview-guide .qt006-body{padding:13px 15px 16px}\n#over-view #tqt006-overview-guide .qt006-body>p{margin:4px 0 12px;line-height:1.6;font-size:13px;color:#344a3e}\n#over-view #tqt006-overview-guide .qt006-small-note{color:#627669!important}\n#over-view #tqt006-overview-guide .qt006-group{border:1px solid #dbe6dc;border-radius:8px;margin:8px 0;background:#fff;overflow:hidden}\n#over-view #tqt006-overview-guide .qt006-group>summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:11px;padding:11px 13px;background:#f6f9f6;color:#254b37;font-size:14px}\n#over-view #tqt006-overview-guide .qt006-group>summary span{font-size:12px;font-weight:600;color:#577261;white-space:nowrap}\n#over-view #tqt006-overview-guide .qt006-scroll{overflow-x:auto;width:100%}\n#over-view #tqt006-overview-guide table{border-collapse:collapse;min-width:850px;width:100%;table-layout:fixed;font-size:12px;line-height:1.48}\n#over-view #tqt006-overview-guide table thead{background:#eaf2ea}\n#over-view #tqt006-overview-guide th,#over-view #tqt006-overview-guide td{border:1px solid #e1e9e2;padding:9px 8px;text-align:left;vertical-align:top;overflow-wrap:anywhere}\n#over-view #tqt006-overview-guide th:nth-child(1){width:8%}#over-view #tqt006-overview-guide th:nth-child(2){width:22%}\n#over-view #tqt006-overview-guide th:nth-child(3){width:17%}#over-view #tqt006-overview-guide th:nth-child(4){width:17%}\n#over-view #tqt006-overview-guide th:nth-child(5){width:14%}#over-view #tqt006-overview-guide th:nth-child(6){width:8%}\n#over-view #tqt006-overview-guide th:nth-child(7){width:7%}#over-view #tqt006-overview-guide th:nth-child(8){width:7%}\n#over-view #tqt006-overview-guide tbody tr:nth-child(even){background:#fafcfa}\n#over-view #tqt006-overview-guide .qt006-id{font:750 12px ui-monospace,monospace}\n#over-view #tqt006-overview-guide code{font-size:12px}\n@media(max-width:600px){#over-view #tqt006-overview-guide{margin:14px 0}#over-view #tqt006-overview-guide .qt006-outer>summary{padding:14px 12px}#over-view #tqt006-overview-guide .qt006-summary-text strong{font-size:15px}#over-view #tqt006-overview-guide .qt006-body{padding:11px 9px}#over-view #tqt006-overview-guide .qt006-group>summary{font-size:12px}}";
const node=(name,cls,text)=>{const el=document.createElement(name);if(cls)el.className=cls;if(text!=null)el.textContent=text;return el};
function create(){
const outer=node('section');outer.id='tqt006-overview-guide';outer.dataset.sourceSha256=sourceHash;outer.dataset.sourceFile='work/tools-quy-trinh/MOW-TH-006.md';
const fold=node('details','qt006-outer');const summary=node('summary');
const title=node('span','qt006-summary-text');title.append(node('strong',null,'3. QTTH 06 · '+definition.step_count+' bước thực hiện'),node('small',null,definition.step_count+' bước · 7 mốc · Quy trình chung, không phải hồ sơ tiến độ'));summary.append(title,node('span','qt006-action','Mở '+definition.step_count+' bước ▾'));fold.append(summary);
const body=node('div','qt006-body');const first=node('details');first.open=true;first.append(node('summary',null,'Đọc trước khi làm'));for(const text of ['1. Viết rõ cách làm và thứ tự.','2. Làm đúng thứ tự phải ra kết quả; tắc thì ghi vấn đề và sửa luật.','3. Làm có bằng chứng, tích xong chỉ từ kết quả đã kiểm.','Bắt đầu: yêu cầu gốc → quyền/phạm vi → mã việc → hồ sơ CAT-227. Năm ô mục tiêu phải có Owner duyệt trước CP02.','Xong: đủ tiêu chí, Field thiết kế, chữ ký đúng phiên, 7 mốc và xác nhận nhận. Khép RUN không thay nghiệm thu sản phẩm.','CHECK005 kiểm hợp đồng; chưa cưỡng chế mọi endpoint máy chủ. Chưa PG, không dùng TEST thay việc thật.'])first.append(node('p',null,text));body.append(first);
const intro=node('p');intro.append(node('strong',null,'QTTH 05'),document.createTextNode(' là các checkpoint tổng hợp. '),node('strong',null,'QTTH 006'),document.createTextNode(' là danh sách thao tác, điều kiện xong, sổ ghi và công cụ. Trạng thái làm thật thuộc '));
const dossier=node('a',null,'hồ sơ từng việc tại CAT-227 ↗');dossier.href='https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/process-work-master-v1.html?master=DEF00.1';dossier.target='_blank';dossier.rel='noopener';intro.append(dossier,document.createTextNode('.'));body.append(intro);
body.append(node('p','qt006-small-note','Quy định chuẩn · '+definition.version+'. Công cụ ở đây là gợi ý dùng lại; hồ sơ chỉ ghi công cụ đã thực sự dùng.'));
for(const g of groups){
 const box=node('details','qt006-group'),head=node('summary');head.append(node('strong',null,g.cp+' · '+g.name),node('span',null,g.rows.length+' bước · Mở xem'));box.append(head);
 const scroller=node('div','qt006-scroll'),table=node('table'),thead=node('thead'),tr=node('tr');
 for(const h of headers){const th=node('th',null,h);th.scope='col';const help=node('details'),sum=node('summary',null,'?');sum.setAttribute('aria-label','Hướng dẫn: '+h);help.append(sum,node('span',null,h==='Tự động hiện tại'?'NO_COMMAND: chưa có lệnh tự làm và ghi trọn bước, AI làm tay có nhãn; không giả biên nhận. HAS_COMMAND: có lệnh và lần chạy thật.':h==='Ai làm dự kiến'?'Vai thực hiện tách khỏi điều kiện áp dụng; reviewer khác hãng, người có quyền duyệt riêng.':'Đây là quy định chuẩn; kết quả thực tế chỉ ghi trong hồ sơ. Nhánh chưa xác định phải hiện ra, chưa được bỏ qua.'));th.append(help);tr.append(th)}thead.append(tr);table.append(thead);
 const tbody=node('tbody');for(const item of g.rows){
  const policy=definition.step_policies?.[item[0]],values=[...item,policy?.actor||'',policy?.automation_current||''];const row=node('tr');for(let i=0;i<values.length;i++){
    const cell=node(i===0?'th':'td',i===0?'qt006-id':null,values[i]);
    if(i===0){cell.scope='row';const card=definition.step_cards?.[item[0]];if(card){const help=node('details'),q=node('summary',null,'?');q.setAttribute('aria-label','Hướng dẫn bước '+item[0]);help.append(q);for(const [key,label] of Object.entries({action:'Làm gì',after:'Sau bước',input:'Đầu vào',actor:'Ai',tool:'Tool',done:'Xong khi',write:'Ghi đâu',report:'Báo khi',error:'Lỗi đi đâu'}))help.append(node('p',null,label+': '+(Array.isArray(card[key])?card[key].join(', ')||'Đầu vào nhánh / yêu cầu gốc':card[key])));cell.append(help);}}
    row.append(cell)
  }
  tbody.append(row)
 }
 table.append(tbody);scroller.append(table);box.append(scroller);body.append(box);
}
const last=node('p','qt006-small-note');last.append(document.createTextNode('Nguồn định nghĩa: '));
const link=node('a',null,'Quy định QTTH 05–06 ↗');link.href='https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=over-view';link.target='_blank';link.rel='noopener';last.append(link,document.createTextNode('. Nếu sửa nguồn quy trình, phải cập nhật bản chiếu/kiểm hash; không sửa độc lập bảng này.'));body.append(last);
fold.append(body);outer.append(fold);return outer;
}
function mount(){
 const root=document.getElementById('tqt-overview-root');if(!root||document.getElementById('tqt006-overview-guide'))return;
 const section=document.getElementById('tqt006-standard-slot');if(!section)return;
 if(!document.getElementById('tqt006-overview-style')){const style=node('style');style.id='tqt006-overview-style';style.textContent=css;document.head.append(style)}
 section.append(create());
}
function ready(){
 const root=document.getElementById('tqt-overview-root');if(!root)return;
 mount();new MutationObserver(mount).observe(root,{childList:true,subtree:true});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',ready,{once:true});else ready();
})();
