# Structured review — 41/41 candidates R2–R8
Phụ lục evidence theo SSOT; mọi vai trò ngoài D03 là đề nghị PM. Writes ghi từ source, không khẳng định đã chạy. Source local không mặc nhiên deployed. [8 gap groups](gap-compression.md).

## C01 · Toàn hệ / browse
R2–R8 · U01 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-hub.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Toàn hệ / browse |
| Role đề nghị | LIBRARY/MASTER |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | MASTER_CONFIG inline; master-list.js và drawer dùng chung |
| Writes | Không thấy business write; chỉ DOM/list local |
| ID/version/revision/context | Mã/7 tầng mẫu; không canonical version/revision |
| Human path | Tìm/list/filter rồi mở review |
| Agent path | Agent có thể dùng catalog API riêng; Hub chưa refetch cùng canonical object |
| Ownership | Hub chỉ entry, không sở hữu Definition 4 Mẹ |
| Reuse/where-used/diff/readiness | Có cùng list/drawer; thống kê mẫu và MOIT menu còn lệch Master thật |
| Gap groups | G01 G02 G03 G04 G05 G08 |
| Disposition | MERGE CAPABILITY INTO PATTERN P01; giữ entry tổng, không một implementation Master mới |
| Evidence | [source/9d4433ffff-master-hub.html](source/9d4433ffff-master-hub.html); [source/81a7037bea-mot-render-v1.js](source/81a7037bea-mot-render-v1.js); [source/d85481bd7b-mvx-v3.js](source/d85481bd7b-mvx-v3.js); [source/27e5baf791-master-drawer-view-v1.js](source/27e5baf791-master-drawer-view-v1.js); [source/30e162474e-master-list.js](source/30e162474e-master-list.js); [source/7d4b138746-eco-nav.js](source/7d4b138746-eco-nav.js); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [browser/C01-hub.png](browser/C01-hub.png); [browser/C01-hub.txt](browser/C01-hub.txt) |

## C02 · MOT Definition / library, inspect
R2 · U05 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-master-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOT Definition / library, inspect |
| Role đề nghị | LIBRARY/MASTER |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | 7 inline items TSK-0001…7; drawer tự fallback sampleForm/sampleReport |
| Writes | List/filter/chi-tiet local; edit chỉ điều hướng |
| ID/version/revision/context | chi-tiet=TSK-0001 giữ code; edit=TSK-0001 đến Studio vẫn là xưởng chung; không version/revision/returnContext |
| Human path | Tìm → inspect input/output → editor chuyên trách |
| Agent path | Không declaration read-back; editor không resolve edit param thành Definition |
| Ownership | MOT inspect MOIT/MOUT phù hợp; list gọi vai 3 forwarder nhưng drawer gọi làm thay; chưa enforce owner |
| Reuse/where-used/diff/readiness | Drawer schema mẫu dù nhãn Form/Báo cáo thật; role completeness local |
| Gap groups | G01 G02 G03 G04 G05 G08 G06 |
| Disposition | KEEP CANONICAL ROLE đề nghị library P01; review ghép P02; không nhận app nguyên trạng |
| Evidence | [source/f840698247-mot-master-v1.html](source/f840698247-mot-master-v1.html); [source/81a7037bea-mot-render-v1.js](source/81a7037bea-mot-render-v1.js); [source/27e5baf791-master-drawer-view-v1.js](source/27e5baf791-master-drawer-view-v1.js); [source/30e162474e-master-list.js](source/30e162474e-master-list.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/f419abc5ec-mot-gopy-filter-v1.js](source/f419abc5ec-mot-gopy-filter-v1.js); [browser/C02-detail-dom.txt](browser/C02-detail-dom.txt); [browser/C02-detail.png](browser/C02-detail.png); [browser/C02-detail.txt](browser/C02-detail.txt); [browser/C02-editor-handoff-dom.txt](browser/C02-editor-handoff-dom.txt); [browser/C02-editor-handoff.png](browser/C02-editor-handoff.png); [browser/C02-editor-handoff.txt](browser/C02-editor-handoff.txt); [browser/C02-initial.json](browser/C02-initial.json); [browser/C02-initial.png](browser/C02-initial.png); [browser/C02-initial.txt](browser/C02-initial.txt) |

## C03 · MOT T1 / task contract và ingredient binding
R2,R4,R6,R7 · U06, U14, U17, U19, U27 · https://vps.incomexsaigoncorp.vn/admin-new-modt?tang=T1&che-do=de-xuat

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOT T1 / task contract và ingredient binding |
| Role đề nghị | EXPERT EDITOR |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | Inline MODULES/collection.field/people sample; NTGV_RULE_TABLE_V1 |
| Writes | Đề xuất NTGV sessionStorage; Test đổi DOM; chưa canonical API |
| ID/version/revision/context | tang/mode chỉ UI; mappings mẫu, chưa ID/version/revision; deep-link không đảm bảo focus |
| Human path | Khai nhiều module/field/condition/role bằng tay; chỉ expert sau AI đề nghị |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | Gộp nội dung chưa đảm bảo edit về MOT/MOIT/MOUT/Field owner; cần phân ranh Field và physical column |
| Reuse/where-used/diff/readiness | Có similar-field UI nhưng mẫu; trạng thái Chưa kết nối; test không evidence |
| Gap groups | G01 G02 G03 G04 G05 G08 G06 |
| Disposition | KEEP EXPERT P03, không primary authoring |
| Evidence | [source/839d16634c-admin-new-modt](source/839d16634c-admin-new-modt); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/4cebec5b2f-mow-t1-work-standard-v1.js](source/4cebec5b2f-mow-t1-work-standard-v1.js); [source/a7f08313d4-ntgv-rule-table-v1.js](source/a7f08313d4-ntgv-rule-table-v1.js); [source/edce88572c-mvx-v3.js](source/edce88572c-mvx-v3.js); [source/2e812fe4dd-eco-nav.js](source/2e812fe4dd-eco-nav.js); [source/4cdcaf8e9f-mow-canvas-url-v1.js](source/4cdcaf8e9f-mow-canvas-url-v1.js); [browser/C03-initial.json](browser/C03-initial.json); [browser/C03-initial.png](browser/C03-initial.png); [browser/C03-initial.txt](browser/C03-initial.txt) |

## C04 · MOT contract / lắp task
R2,R5 · U06, U15, U16 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/modt-builder-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOT contract / lắp task |
| Role đề nghị | EXPERT EDITOR |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | M config + entry-engine/entry-savemode; KIT/DB choices mẫu |
| Writes | cast=alert demo đăng ký task_registry; preview local |
| ID/version/revision/context | Khuôn JSON local/target_collection; không canonical revision |
| Human path | Chọn bảng, fields, report, trigger/condition, people rồi đúc |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | MOT lắp refs; builder tự khai input/report/rules vượt owner nếu dùng làm truth |
| Reuse/where-used/diff/readiness | Có config/preview; không registry search/where-used/diff/test thật |
| Gap groups | G01 G02 G03 G04 G05 G08 |
| Disposition | MERGE CAPABILITY INTO P03 task contract; không duy trì editor ngang New MODT |
| Evidence | [source/07b1ea508b-modt-builder-v1.html](source/07b1ea508b-modt-builder-v1.html); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/018f9a2b6b-eco-nav.js](source/018f9a2b6b-eco-nav.js); [source/5d3168f73e-entry-engine.js](source/5d3168f73e-entry-engine.js); [source/9dc6e96d95-modit-entry-enhance.js](source/9dc6e96d95-modit-entry-enhance.js); [source/be01069c97-entry-savemode.js](source/be01069c97-entry-savemode.js); [source/b5a3d592d9-guide-dock.js](source/b5a3d592d9-guide-dock.js); [browser/C04-initial.json](browser/C04-initial.json); [browser/C04-initial.png](browser/C04-initial.png); [browser/C04-initial.txt](browser/C04-initial.txt) |

## C05 · Task Instance / làm việc
R2,R8 · U07, U24, U25 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-dashboard-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Task Instance / làm việc |
| Role đề nghị | RUNTIME WORKSPACE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | MOT_DATA.tasks inline; default MOT-2599, các form/reference mẫu |
| Writes | complete chỉ M.cur.state=done + toast rồi mở item kế; revise đặt open; không PG/handoff ACK |
| ID/version/revision/context | Có local task id/code; không workflow_instance/attempt/effect key/pinned version |
| Human path | HMITL chọn việc, nhập MOIT, xem MOUT/Help, kết quả; không bấm Done trong review |
| Agent path | Không AUTO worker/Agent read-back trong candidate; Guard/worker Gate0 là evidence riêng |
| Ownership | Không được coi M.cur.state là runtime truth; edit instance không sửa Definition; AUTO phải riêng |
| Reuse/where-used/diff/readiness | Có workbench/list/guidance/feedback panel; số đếm và luồng tiếp chỉ local |
| Gap groups | G01 G03 G06 G07 G08 |
| Disposition | KEEP CANONICAL ROLE đề nghị P04 HMITL pattern, không runtime PASS |
| Evidence | [source/44e46628e9-mot-dashboard-v1.html](source/44e46628e9-mot-dashboard-v1.html); [source/81a7037bea-mot-render-v1.js](source/81a7037bea-mot-render-v1.js); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/2e812fe4dd-eco-nav.js](source/2e812fe4dd-eco-nav.js); [source/00bcb3a336-mot-data-v1.js](source/00bcb3a336-mot-data-v1.js); [source/4b57e42e43-mot-app-v1.js](source/4b57e42e43-mot-app-v1.js); [source/e761c3a34b-mot-improve-bar-v1.js](source/e761c3a34b-mot-improve-bar-v1.js); [source/781f760cd0-mot-help-v1.js](source/781f760cd0-mot-help-v1.js); [source/cd92fef08f-mot-enhance.js](source/cd92fef08f-mot-enhance.js); [browser/C05-help-dom.txt](browser/C05-help-dom.txt); [browser/C05-help.png](browser/C05-help.png); [browser/C05-help.txt](browser/C05-help.txt); [browser/C05-initial.json](browser/C05-initial.json); [browser/C05-initial.png](browser/C05-initial.png); [browser/C05-initial.txt](browser/C05-initial.txt); [browser/C05-ready-dom.txt](browser/C05-ready-dom.txt); [browser/C05-ready.png](browser/C05-ready.png); [browser/C05-ready.txt](browser/C05-ready.txt) |

## C06 · MOIT Definition / library
R3 · U08 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/moit-master-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOIT Definition / library |
| Role đề nghị | LIBRARY/MASTER |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | 7 inline form items; shared drawer fallback schema vòng1 |
| Writes | Không canonical write; edit link MOIT form |
| ID/version/revision/context | Mã MOIT-F-0001; không immutable version/revision; drawer schema fallback |
| Human path | Tìm/filter/inspect rồi owner layout editor |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | Thư viện MOIT đúng role; không cho Form field layout sở hữu Field meaning |
| Reuse/where-used/diff/readiness | Dùng lại master-list; drawer sample không phải form_registry read |
| Gap groups | G01 G02 G03 G04 G05 G08 |
| Disposition | KEEP CANONICAL ROLE đề nghị P01 cho MOIT |
| Evidence | [source/5233fc8aad-moit-master-v1.html](source/5233fc8aad-moit-master-v1.html); [source/81a7037bea-mot-render-v1.js](source/81a7037bea-mot-render-v1.js); [source/27e5baf791-master-drawer-view-v1.js](source/27e5baf791-master-drawer-view-v1.js); [source/30e162474e-master-list.js](source/30e162474e-master-list.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [browser/C06-detail-dom.txt](browser/C06-detail-dom.txt); [browser/C06-detail.png](browser/C06-detail.png); [browser/C06-detail.txt](browser/C06-detail.txt); [browser/C06-initial.json](browser/C06-initial.json); [browser/C06-initial.png](browser/C06-initial.png); [browser/C06-initial.txt](browser/C06-initial.txt) |

## C07 · MOIT Definition / layout
R3,R4 · U09, U14 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/moit-form-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOIT Definition / layout |
| Role đề nghị | EXPERT EDITOR |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | KIT F01–F10/E01/E02 + local layout/options/Guidance |
| Writes | Lưu form=alert demo; form preview không chứng minh submit canonical |
| ID/version/revision/context | MOIT-FORM-0001 local khác Master MOIT-F-0001; chưa resolve same context |
| Human path | Kéo trường, required/order/layout, viết hướng dẫn; chỉ H2/H3 khi nghĩa chưa rõ |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | MOIT layout/order/required tại form; không tự sửa meaning/constraints global Field |
| Reuse/where-used/diff/readiness | Preview sống trong page; thiếu read/refetch declaration chung |
| Gap groups | G01 G02 G03 G04 G05 G08 |
| Disposition | KEEP EXPERT P03 layout; generic renderer S01 ưu tiên |
| Evidence | [source/b41bf4c11e-moit-form-v1.html](source/b41bf4c11e-moit-form-v1.html); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/b5a3d592d9-guide-dock.js](source/b5a3d592d9-guide-dock.js); [browser/C07-initial.json](browser/C07-initial.json); [browser/C07-initial.png](browser/C07-initial.png); [browser/C07-initial.txt](browser/C07-initial.txt) |

## C08 · MOIT / cấu hình nhập và binding
R3,R5 · U10, U15, U16 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/moit-builder-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOIT / cấu hình nhập và binding |
| Role đề nghị | EXPERT EDITOR |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | M/entry-engine fields, conditions, people mẫu; table-first phase agent |
| Writes | cast alert demo input_form_registry; direct/queue là local config |
| ID/version/revision/context | Physical target_collection/value_fields, chưa business Field identity/version |
| Human path | Chọn bảng/cột/FK, điều kiện, lịch, người, đúc |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | Trộn form layout, Trigger/Condition Definition, NTGV và task spawning; cần owner-aware refs |
| Reuse/where-used/diff/readiness | Có declaration preview; không native catalog lookup/admission thật |
| Gap groups | G01 G02 G03 G04 G05 G08 G06 |
| Disposition | MERGE CAPABILITY INTO P03; layout về C07, binding riêng cùng context; không giữ 2 truth |
| Evidence | [source/67925058e9-moit-builder-v1.html](source/67925058e9-moit-builder-v1.html); [source/7d4b138746-eco-nav.js](source/7d4b138746-eco-nav.js); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/5d3168f73e-entry-engine.js](source/5d3168f73e-entry-engine.js); [source/be01069c97-entry-savemode.js](source/be01069c97-entry-savemode.js); [source/79ed183bb9-modit-entry-enhance.js](source/79ed183bb9-modit-entry-enhance.js); [browser/C08-initial.json](browser/C08-initial.json); [browser/C08-initial.png](browser/C08-initial.png); [browser/C08-initial.txt](browser/C08-initial.txt) |

## C09 · MOUT Definition / library
R3 · U11 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mout-home-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOUT Definition / library |
| Role đề nghị | LIBRARY/MASTER |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | 10 inline RPT items; master drawer fallback report_schema mẫu |
| Writes | Không canonical write; điều hướng builder |
| ID/version/revision/context | RPT-0001 + slug; không revision/exact report declaration |
| Human path | Tìm/filter/inspect báo cáo rồi mở owner editor |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | MOUT sở hữu read/report definition; runtime task chỉ consume |
| Reuse/where-used/diff/readiness | Master/list tái dùng; chữ Báo cáo thật vẫn render mẫu |
| Gap groups | G01 G02 G03 G04 G05 G08 |
| Disposition | KEEP CANONICAL ROLE đề nghị P01 cho MOUT |
| Evidence | [source/701533bd11-mout-home-v1.html](source/701533bd11-mout-home-v1.html); [source/81a7037bea-mot-render-v1.js](source/81a7037bea-mot-render-v1.js); [source/27e5baf791-master-drawer-view-v1.js](source/27e5baf791-master-drawer-view-v1.js); [source/30e162474e-master-list.js](source/30e162474e-master-list.js); [source/7d4b138746-eco-nav.js](source/7d4b138746-eco-nav.js); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [browser/C09-detail-dom.txt](browser/C09-detail-dom.txt); [browser/C09-detail.png](browser/C09-detail.png); [browser/C09-detail.txt](browser/C09-detail.txt); [browser/C09-initial.json](browser/C09-initial.json); [browser/C09-initial.png](browser/C09-initial.png); [browser/C09-initial.txt](browser/C09-initial.txt) |

## C10 · MOUT / report Definition
R3 · U12 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mout-builder-v3.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOUT / report Definition |
| Role đề nghị | EXPERT EDITOR |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | ENT/FIELDS/CT mẫu sinh physical path; M cols + dataset tại JS |
| Writes | cast chỉ hiện URL giả lập /r/slug, lịch/phân phối DOM; export CSV/XLS local; không registry/save/API |
| ID/version/revision/context | slug và physical path không canonical ID; không version/revision |
| Human path | Chọn cột, AND tối đa5, lọc/lịch/tổng/nhận; chuyên gia kiểm query/meaning |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | Report filter không global Condition; lịch/sending cần runtime/binding chủ quản |
| Reuse/where-used/diff/readiness | Có layout/preview/export; không true source query permission/diff |
| Gap groups | G01 G02 G03 G04 G05 G08 |
| Disposition | KEEP EXPERT P03 MOUT; merge MODUT connection capability |
| Evidence | [source/464cc6ddb6-mout-builder-v3.html](source/464cc6ddb6-mout-builder-v3.html); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [browser/C10-initial.json](browser/C10-initial.json); [browser/C10-initial.png](browser/C10-initial.png); [browser/C10-initial.txt](browser/C10-initial.txt) |

## C11 · MOUT / source binding + phân phối
R3,R5 · U13, U15, U16 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/modut-builder-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOUT / source binding + phân phối |
| Role đề nghị | EXPERT EDITOR |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | 4 report choices + collections/functions/recipient mẫu |
| Writes | cast alert demo output_table_registry; không scheduler/API |
| ID/version/revision/context | Report code chọn local, không pinned source/version; technical function names mẫu |
| Human path | Chọn nguồn, hàm, lịch, recipients rồi đúc |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | MOUT read binding khác task assignment; không DOT function mới chỉ vì bảng chọn mẫu |
| Reuse/where-used/diff/readiness | Hướng dẫn 2 mặt miền dữ liệu hữu ích; readiness chưa nối |
| Gap groups | G01 G02 G03 G04 G05 G06 G08 |
| Disposition | MERGE CAPABILITY INTO P03 MOUT owner editor, không thêm app default |
| Evidence | [source/ad54770c9d-modut-builder-v1.html](source/ad54770c9d-modut-builder-v1.html); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/b5a3d592d9-guide-dock.js](source/b5a3d592d9-guide-dock.js); [browser/C11-initial.json](browser/C11-initial.json); [browser/C11-initial.png](browser/C11-initial.png); [browser/C11-initial.txt](browser/C11-initial.txt) |

## C12 · NTGV / review approval
R6,R7 · U17, U22 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/duyet-ntgv-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | NTGV / review approval |
| Role đề nghị | PRIMARY REVIEW |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | NTGV01 sample + sessionStorage ntgv.approval.*; shared rule-table |
| Writes | Select approval đổi sessionStorage; Help nói DB/cờ pháp lý chưa có evidence |
| ID/version/revision/context | NTGV01 local code; không revision signer/authority/receipt; 0 count nhưng có1row |
| Human path | Đọc NẾU/THÌ; duyệt chưa được bấm trong review |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | NTGV definition khác People; forwarder chưa định nghĩa trách nhiệm; legal gate chỉ claim Help |
| Reuse/where-used/diff/readiness | Có layout rule table và Help theo cột; không approval truth |
| Gap groups | G01 G04 G05 G06 G08 |
| Disposition | MERGE CAPABILITY INTO P02/P05; không NTGV approval engine riêng |
| Evidence | [source/16997da12c-duyet-ntgv-v1.html](source/16997da12c-duyet-ntgv-v1.html); [source/81a7037bea-mot-render-v1.js](source/81a7037bea-mot-render-v1.js); [source/27e5baf791-master-drawer-view-v1.js](source/27e5baf791-master-drawer-view-v1.js); [source/30e162474e-master-list.js](source/30e162474e-master-list.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/f419abc5ec-mot-gopy-filter-v1.js](source/f419abc5ec-mot-gopy-filter-v1.js); [source/a7f08313d4-ntgv-rule-table-v1.js](source/a7f08313d4-ntgv-rule-table-v1.js); [browser/C12-help-dom.txt](browser/C12-help-dom.txt); [browser/C12-help.png](browser/C12-help.png); [browser/C12-help.txt](browser/C12-help.txt); [browser/C12-initial.json](browser/C12-initial.json); [browser/C12-initial.png](browser/C12-initial.png); [browser/C12-initial.txt](browser/C12-initial.txt) |

## C13 · Table/Field meaning / phân loại danh từ Lark
R4 · U18 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-danh-tu-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Table/Field meaning / phân loại danh từ Lark |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | 120 danh từ khai trongHTML; nguồn ngữ nghĩa nhập một lần |
| Writes | GIỮ/GỘP/BỎ persist localStorage; export file local |
| ID/version/revision/context | Số danh từ không canonical business ID/version; quyết định local không admission |
| Human path | Owner xem nghĩa và nhóm; H2/H3 ca khó, không ép chốt120mục hay quota50 bảng |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | Concept ≠ table; một noun không bắt buộc một bảng; không dùng page làm schema truth |
| Reuse/where-used/diff/readiness | Giữ rationale/alias/grouping; thiếu kho hiện hành/where-used/merge kiểm chứng |
| Gap groups | G01 G02 G04 G08 |
| Disposition | KEEP REFERENCE; MERGE meaning review into P02; không schema manager |
| Evidence | [source/abb18bf094-mow-danh-tu-v1.html](source/abb18bf094-mow-danh-tu-v1.html); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [browser/C13-initial.json](browser/C13-initial.json); [browser/C13-initial.png](browser/C13-initial.png); [browser/C13-initial.txt](browser/C13-initial.txt) |

## C14 · QA UI kỹ thuật / kiểm contract bề mặt
R7 · U21 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/qa-runner.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | QA UI kỹ thuật / kiểm contract bề mặt |
| Role đề nghị | EXPERT EDITOR |
| Implementation truth | source-only/unproven — live page cố ý không mở vì auto-run |
| Reads | qa-contracts.js + pages/iframe + UI contract sources |
| Writes | runAll có tự load và thao tác iframe; chotMoc tạo fingerprint hướng dẫn sửa file; KHÔNG thực thi |
| ID/version/revision/context | File hash/region baseline; không business release/expected-source authority |
| Human path | Kỹ thuật viên QA khi được giao; không human business-test entry |
| Agent path | Agent có thể dùng harness sau scope test được phép; lượt này chỉ đọc source |
| Ownership | UI regression ≠ business Test/approval/publish; không lấy green UI test thành release readiness |
| Reuse/where-used/diff/readiness | Có test names/DOM checks; thiếu expected version/provenance/negative business suite |
| Gap groups | G04 G05 G08 |
| Disposition | KEEP EXPERT kỹ thuật; business evidence render qua P05 |
| Evidence | [source/e092c3b211-qa-runner.html](source/e092c3b211-qa-runner.html); [source/15a0961275-qa-contracts.js](source/15a0961275-qa-contracts.js) |

## C15 · Feedback / improvement history
R7 · U26 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-gopy-list-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Feedback / improvement history |
| Role đề nghị | LIBRARY/MASTER |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | 8 góp ý từ mow-gopy-data-v1.js |
| Writes | Status/filter/drawer local; chưa nối bảng thật |
| ID/version/revision/context | GY/TK/RUN step mã mẫu; chưa actor/server/time/version authority |
| Human path | Một ô góp ý; xem list/details/status; H1/H5, không tự approval |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | Feedback là input Proposal; không trực tiếp sửa Definition đang ban hành |
| Reuse/where-used/diff/readiness | Có context thiết kế/bước-lượt và trạng thái mẫu; không causal measurement |
| Gap groups | G01 G03 G05 G08 |
| Disposition | MERGE CAPABILITY INTO P01/P05; giữ một sổ góp ý chung |
| Evidence | [source/0d0c767343-mow-gopy-list-v1.html](source/0d0c767343-mow-gopy-list-v1.html); [source/81a7037bea-mot-render-v1.js](source/81a7037bea-mot-render-v1.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/2ecc58896f-mow-gopy-data-v1.js](source/2ecc58896f-mow-gopy-data-v1.js); [source/0f1dbeef27-mow-gopy-list-v1.js](source/0f1dbeef27-mow-gopy-list-v1.js); [browser/C15-initial.json](browser/C15-initial.json); [browser/C15-initial.png](browser/C15-initial.png); [browser/C15-initial.txt](browser/C15-initial.txt) |

## C16 · Onboarding / idea→system
R7 · U28 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/bat-dau-o-day.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Onboarding / idea→system |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | HTML hướng dẫn 02/09; link New MODT/T1 cũ |
| Writes | Không business write; text/config hoặc export local |
| ID/version/revision/context | Mốc02/09; không runtime revision |
| Human path | Đọc hướng dẫn, không mặc định click qua chuỗi16 bước |
| Agent path | Agent đọc tham khảo có provenance; không dùng mô tả làm lệnh chạy/authority |
| Ownership | Phân biệt công cụ/quy trình chuyên môn hữu ích; Task = người có hạn bỏ sót AUTO |
| Reuse/where-used/diff/readiness | CHƯA CÓ là nhãn lịch sử, MOIT library thực tế đã có |
| Gap groups | G03 G07 G08 |
| Disposition | KEEP REFERENCE; nội dung áp dụng qua P05 Help có revision |
| Evidence | [source/693de0ed58-bat-dau-o-day.html](source/693de0ed58-bat-dau-o-day.html); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [browser/C16-initial.json](browser/C16-initial.json); [browser/C16-initial.png](browser/C16-initial.png); [browser/C16-initial.txt](browser/C16-initial.txt) |

## C17 · Factory process / two channels
R7 · U28 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/quy-trinh-he-thong.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Factory process / two channels |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | HTML khảo sát02/09 |
| Writes | Không business write; text/config hoặc export local |
| ID/version/revision/context | Không contract runtime/version pointer |
| Human path | Hiểu ý tưởng→tool; đường Agent được nêu kênh chính |
| Agent path | Agent đọc tham khảo có provenance; không dùng mô tả làm lệnh chạy/authority |
| Ownership | Ghi thẳng PG theo formatUI không thay quyền/guard; UI không canonical contract owner |
| Reuse/where-used/diff/readiness | Có kênh Agent/human; wording tự dựng bảng còn lệch reuse-first |
| Gap groups | G01 G02 G03 G05 G08 |
| Disposition | KEEP REFERENCE; nội dung áp dụng qua P05 Help có revision |
| Evidence | [source/5b5df4bc22-quy-trinh-he-thong.html](source/5b5df4bc22-quy-trinh-he-thong.html); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [browser/C17-initial.json](browser/C17-initial.json); [browser/C17-initial.png](browser/C17-initial.png); [browser/C17-initial.txt](browser/C17-initial.txt) |

## C18 · MOT onboarding /16steps
R2,R7 · U28 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-process-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOT onboarding /16steps |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | HTML khảo sát02/09, linkstới NewMODT/Studio |
| Writes | Không business write; text/config hoặc export local |
| ID/version/revision/context | 16 bước/0 chạy thật là snapshot cũ không scorehiện tại |
| Human path | Đọc checklist legacy; không bắt human tự điều phối toolchain |
| Agent path | Agent đọc tham khảo có provenance; không dùng mô tả làm lệnh chạy/authority |
| Ownership | Ba vai chuyển tiếp và làm thay bị gọi lẫn; Test không actualevidence |
| Reuse/where-used/diff/readiness | Giữ danh sách câu hỏi/ngõ cụt; sửa drift trạng thái Proof G0 |
| Gap groups | G03 G04 G06 G08 |
| Disposition | KEEP REFERENCE; nội dung áp dụng qua P05 Help có revision |
| Evidence | [source/3ad13eab35-mot-process-v1.html](source/3ad13eab35-mot-process-v1.html); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [browser/C18-initial.json](browser/C18-initial.json); [browser/C18-initial.png](browser/C18-initial.png); [browser/C18-initial.txt](browser/C18-initial.txt) |

## C19 · Widget library / mẫu task
R2,R3,R7 · U28, U06, U09 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-studio-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Widget library / mẫu task |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | MOTStudio JS+mot-render-v1.js samples F01–F10/E01/E02 |
| Writes | Không business write; text/config hoặc export local |
| ID/version/revision/context | edit=TSK-0001 ở URL nhưng body vẫn widgetcatalog; không revision |
| Human path | Thử loại ô và bố cục; expertreference |
| Agent path | Agent đọc tham khảo có provenance; không dùng mô tả làm lệnh chạy/authority |
| Ownership | F01 ở đây widget type, không business Field code; tránh đồng nhất |
| Reuse/where-used/diff/readiness | Dùng lại ý tưởng widgets, kiểm S01 đã đáp ứng trước customJS |
| Gap groups | G01 G03 G08 |
| Disposition | KEEP REFERENCE widget catalog; MERGE needed renderer capability into existing S01 |
| Evidence | [source/bc09b43c22-mot-studio-v1.html](source/bc09b43c22-mot-studio-v1.html); [source/81a7037bea-mot-render-v1.js](source/81a7037bea-mot-render-v1.js); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/2e812fe4dd-eco-nav.js](source/2e812fe4dd-eco-nav.js); [source/f14d6575c3-mot-studio-v1.js](source/f14d6575c3-mot-studio-v1.js); [browser/C19-initial.json](browser/C19-initial.json); [browser/C19-initial.png](browser/C19-initial.png); [browser/C19-initial.txt](browser/C19-initial.txt) |

## C20 · MOIT dataflow reference
R3,R7 · U10, U28 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/moit-dataflow-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOIT dataflow reference |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | HTML kiến trúc field_registry/input_form_registry/binding_registry |
| Writes | Không business write; text/config hoặc export local |
| ID/version/revision/context | Claim schema tồn tại không chứng minh shape/compatibility current |
| Human path | Đọc đường nhập→guard; không bắt user mapping physicaltable |
| Agent path | Agent đọc tham khảo có provenance; không dùng mô tả làm lệnh chạy/authority |
| Ownership | Field owner=GOV-MOIT trong tài liệu cần đối chiếu Field owner riêng; cấmNuxt tuyệt đối lệch transport |
| Reuse/where-used/diff/readiness | Có idea declaration→render; coi khung nguồn legacy, không tự dựng MOITForm mới |
| Gap groups | G01 G02 G03 G05 G08 |
| Disposition | KEEP REFERENCE; nội dung áp dụng qua P05 Help có revision |
| Evidence | [source/512df5c44e-moit-dataflow-v1.html](source/512df5c44e-moit-dataflow-v1.html); [source/7d4b138746-eco-nav.js](source/7d4b138746-eco-nav.js); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [browser/C20-initial.json](browser/C20-initial.json); [browser/C20-initial.png](browser/C20-initial.png); [browser/C20-initial.txt](browser/C20-initial.txt) |

## C21 · MOUT / alias v2 cũ
R3 · U12 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mout-builder-v2.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOUT / alias v2 cũ |
| Role đề nghị | RETIRE-CANDIDATE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | HTML meta-refresh sang C10 v3; browser xác nhận cùng target |
| Writes | Không business write tại alias |
| ID/version/revision/context | Giữ redirect; không cho biết consumer traffic/old query preservation |
| Human path | Link cũ tự vào v3 |
| Agent path | Không Agent authoring riêng |
| Ownership | Không truth riêng vì đã redirect; quyền vẫn theo target chưa chứng minh |
| Reuse/where-used/diff/readiness | Không capability riêng còn lại; metadata legacy trong nav matchset |
| Gap groups | G01 G08 |
| Disposition | RETIRE-CANDIDATE alias only; retain redirect tới sau consumer audit Gate7 |
| Evidence | [source/021be6a568-mout-builder-v2.html](source/021be6a568-mout-builder-v2.html); [browser/C21-initial.json](browser/C21-initial.json); [browser/C21-initial.png](browser/C21-initial.png); [browser/C21-initial.txt](browser/C21-initial.txt) |

## C22 · MOUT / alias DOT-table concept cũ
R3 · U13 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mout-dot-table-v1.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOUT / alias DOT-table concept cũ |
| Role đề nghị | RETIRE-CANDIDATE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | HTML meta-refresh sang C10 v3; browser xác nhận cùng target |
| Writes | Không business write tại alias |
| ID/version/revision/context | Giữ redirect; không cho biết consumer traffic/old query preservation |
| Human path | Link cũ tự vào v3 |
| Agent path | Không Agent authoring riêng |
| Ownership | Không truth riêng vì đã redirect; quyền vẫn theo target chưa chứng minh |
| Reuse/where-used/diff/readiness | Không capability riêng còn lại; metadata legacy trong nav matchset |
| Gap groups | G01 G08 |
| Disposition | RETIRE-CANDIDATE alias only; retain redirect tới sau consumer audit Gate7 |
| Evidence | [source/26cc3078b8-mout-dot-table-v1.html](source/26cc3078b8-mout-dot-table-v1.html); [browser/C22-initial.json](browser/C22-initial.json); [browser/C22-initial.png](browser/C22-initial.png); [browser/C22-initial.txt](browser/C22-initial.txt) |

## C23 · T1 hanging-card visual reference
R2,R7 · U06, U28 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-tang1-v1.html?che-do=de-xuat

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | T1 hanging-card visual reference |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | HTML static card; comment trỏ MOW_T1_WORK_STANDARD_V1 |
| Writes | Không business write; text/config hoặc export local |
| ID/version/revision/context | che-do=de-xuat không biến page thành editor; không task code |
| Human path | Chỉ xem thẩm mỹ Owner đã chọn |
| Agent path | Agent đọc tham khảo có provenance; không dùng mô tả làm lệnh chạy/authority |
| Ownership | Không copy page để tạoTask; task data phải qua standard/owner |
| Reuse/where-used/diff/readiness | Giữ hình dáng/card links; onboarding link sai kỳ vọng authoring |
| Gap groups | G01 G07 G08 |
| Disposition | KEEP REFERENCE; nội dung áp dụng qua P05 Help có revision |
| Evidence | [source/5560fa4210-mow-tang1-v1.html](source/5560fa4210-mow-tang1-v1.html); [browser/C23-initial.json](browser/C23-initial.json); [browser/C23-initial.png](browser/C23-initial.png); [browser/C23-initial.txt](browser/C23-initial.txt) |

## C24 · Guide / kiến trúc cũ
R7 · U28, U20 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/guide.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Guide / kiến trúc cũ |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | Guide+system-manifest v5.3+guide-extra |
| Writes | Không business write; text/config hoặc export local |
| ID/version/revision/context | Ngày/manifest không accepted SSOT v1.6.14 |
| Human path | Tra Help; không theo runtime Kestra cũ |
| Agent path | Agent đọc tham khảo có provenance; không dùng mô tả làm lệnh chạy/authority |
| Ownership | DOT/Kestra bắt buộc trong Help không thay current bounded pg-boss/guard candidates |
| Reuse/where-used/diff/readiness | Giữ guide entry; cần owner/source/version/applies-to mới |
| Gap groups | G03 G05 G07 G08 |
| Disposition | KEEP REFERENCE; nội dung áp dụng qua P05 Help có revision |
| Evidence | [source/e86fb01573-guide.html](source/e86fb01573-guide.html); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/044753bc60-system-manifest.js](source/044753bc60-system-manifest.js); [source/86cd069f67-guide-extra.js](source/86cd069f67-guide-extra.js); [browser/C24-initial.json](browser/C24-initial.json); [browser/C24-initial.png](browser/C24-initial.png); [browser/C24-initial.txt](browser/C24-initial.txt) |

## C25 · UI contract catalog / schema hypotheses
R4,R7 · U18, U28 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/he-thong-thiet-ke.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | UI contract catalog / schema hypotheses |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | system-manifest v5.3, 23 bảng/228 cột yêu cầuUI |
| Writes | Không business write; text/config hoặc export local |
| ID/version/revision/context | Snapshot02/07; con số không PG actual |
| Human path | Expert tra hợp đồng cũ |
| Agent path | Agent đọc tham khảo có provenance; không dùng mô tả làm lệnh chạy/authority |
| Ownership | UI yêu cầu data không được tạo23 bảng mới bỏ catalog-first |
| Reuse/where-used/diff/readiness | Có contract/schema map + exportJSON/MD; cần reuse mapping |
| Gap groups | G01 G02 G04 G08 |
| Disposition | KEEP REFERENCE; nội dung áp dụng qua P05 Help có revision |
| Evidence | [source/6009b7696a-he-thong-thiet-ke.html](source/6009b7696a-he-thong-thiet-ke.html); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/044753bc60-system-manifest.js](source/044753bc60-system-manifest.js); [browser/C25-initial.json](browser/C25-initial.json); [browser/C25-initial.png](browser/C25-initial.png); [browser/C25-initial.txt](browser/C25-initial.txt) |

## C26 · Readiness / connection matrix
R4,R7 · U18, U28 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/he-thong-dau-noi.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Readiness / connection matrix |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | system-manifest + binding-status.js seed30/06 |
| Writes | Không business write; text/config hoặc export local |
| ID/version/revision/context | 0/23/2of23 chỉ seed, không runtime health |
| Human path | Đọc matrix; không sửa JS làm readiness truth |
| Agent path | Agent đọc tham khảo có provenance; không dùng mô tả làm lệnh chạy/authority |
| Ownership | Statusfile không canonical evidence; PG catalog có table không bằng đấu nối PASS |
| Reuse/where-used/diff/readiness | 4 nấc khai/PG/nối/test là presentation dùng được |
| Gap groups | G01 G04 G08 |
| Disposition | KEEP REFERENCE; nội dung áp dụng qua P05 Help có revision |
| Evidence | [source/1d95b8d91b-he-thong-dau-noi.html](source/1d95b8d91b-he-thong-dau-noi.html); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [browser/C26-initial.json](browser/C26-initial.json); [browser/C26-initial.png](browser/C26-initial.png); [browser/C26-initial.txt](browser/C26-initial.txt) |

## C27 · Governance matrix / draft design preview
R7 · U20, U28 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/constitution-new-index.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Governance matrix / draft design preview |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | Inline mock/config, readiness simulation/workflow contract |
| Writes | Không business write; text/config hoặc export local |
| ID/version/revision/context | DRAFT NON-AUTHORIZING; cell_id4chiều không canonicalrecord |
| Human path | Expert inspect eligibility/missing; không duyệt thật |
| Agent path | Agent đọc tham khảo có provenance; không dùng mô tả làm lệnh chạy/authority |
| Ownership | Matrix positioning ≠ orgtree; stamp mock không cấp authority |
| Reuse/where-used/diff/readiness | Có thiếu/lỗi/unknown và candidate/promote concept; không chọnframeworkmới |
| Gap groups | G01 G04 G05 G08 |
| Disposition | KEEP REFERENCE; nội dung áp dụng qua P05 Help có revision |
| Evidence | [source/ee5af11f61-constitution-new-index.html](source/ee5af11f61-constitution-new-index.html); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/7b43bf3a25-eco-nav.js](source/7b43bf3a25-eco-nav.js); [browser/C27-initial.json](browser/C27-initial.json); [browser/C27-initial.png](browser/C27-initial.png); [browser/C27-initial.txt](browser/C27-initial.txt) |

## C28 · Reuse/meaning alignment / feedback
R7 · U26, U28 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/quy-trinh-sua-re.html

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Reuse/meaning alignment / feedback |
| Role đề nghị | LEGACY/REFERENCE |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | concept-ledger.js + ui-contracts.js; queue matched/candidate/review |
| Writes | Không business write; text/config hoặc export local |
| ID/version/revision/context | Concept code JS; file-based counters không PG revision |
| Human path | Người chốt ca khó H2/H3; Agent khử trùng/find reuse |
| Agent path | Agent đọc tham khảo có provenance; không dùng mô tả làm lệnh chạy/authority |
| Ownership | Businessmeaningowner chốt; JS ledger không thành registry truth thứ hai |
| Reuse/where-used/diff/readiness | Có aliases, near_concepts, where-used đếm từUIcontracts; tốtchoP01/P02 |
| Gap groups | G01 G02 G04 G08 |
| Disposition | KEEP REFERENCE; nội dung áp dụng qua P05 Help có revision |
| Evidence | [source/015e21352a-quy-trinh-sua-re.html](source/015e21352a-quy-trinh-sua-re.html); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [browser/C28-initial.json](browser/C28-initial.json); [browser/C28-initial.png](browser/C28-initial.png); [browser/C28-initial.txt](browser/C28-initial.txt) |

## C29 · Catalog / Field, Table, Trigger inventory
R4,R5,R7 · U14, U15, U16, U18, U20 · https://vps.incomexsaigoncorp.vn/knowledge/registries

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Catalog / Field, Table, Trigger inventory |
| Role đề nghị | LIBRARY/MASTER |
| Implementation truth | partial — dữ liệu danh mục có hiển thị; canonical business lookup chưa đủ |
| Reads | Nuxt SSR data + local source meta_catalog/registry composition/health; 3 drilldowns read metadata |
| Writes | Không write thực hiện; page/list chủ yếu read |
| ID/version/revision/context | Catalog code + collection route; không semantic version/revision; summary count không phải lookup coverage |
| Human path | Browse/search→detail; Trigger/directus_fields/Field Standards đều báo chưa có bảng registry |
| Agent path | Có native catalog read API để reuse; user-facing request/resume chưa có |
| Ownership | Technical meta_catalog khác Field meaning/Trigger Definition; không tạo mới vì detail thiếu |
| Reuse/where-used/diff/readiness | Có counts/health; drilldown 107/1497/11 items nhưng không render records |
| Gap groups | G01 G02 G04 G08 |
| Disposition | KEEP CANONICAL ROLE đề nghị P01 dựa generic catalog/table; bổ sung mapping, không catalog mới |
| Evidence | [source/6bfadd7ce2-registries](source/6bfadd7ce2-registries); [source/9a04a213b6-DkEoWw5i.js](source/9a04a213b6-DkEoWw5i.js); [browser/C29-directus-fields-dom.txt](browser/C29-directus-fields-dom.txt); [browser/C29-directus-fields.png](browser/C29-directus-fields.png); [browser/C29-directus-fields.txt](browser/C29-directus-fields.txt); [browser/C29-drilldown-links.json](browser/C29-drilldown-links.json); [browser/C29-field-standard-dom.txt](browser/C29-field-standard-dom.txt); [browser/C29-field-standard.png](browser/C29-field-standard.png); [browser/C29-field-standard.txt](browser/C29-field-standard.txt); [browser/C29-initial.json](browser/C29-initial.json); [browser/C29-initial.png](browser/C29-initial.png); [browser/C29-initial.txt](browser/C29-initial.txt); [browser/C29-trigger-dom.txt](browser/C29-trigger-dom.txt); [browser/C29-trigger.png](browser/C29-trigger.png); [browser/C29-trigger.txt](browser/C29-trigger.txt); [native-source/web/pages/knowledge/registries/index.vue](native-source/web/pages/knowledge/registries/index.vue); [native-source/web/pages/knowledge/registries/all/index.vue](native-source/web/pages/knowledge/registries/all/index.vue) |

## C30 · Multi-entity catalog / search
R4,R5 · U14, U15, U16, U18 · https://vps.incomexsaigoncorp.vn/knowledge/registries/all

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Multi-entity catalog / search |
| Role đề nghị | LIBRARY/MASTER |
| Implementation truth | partial — SSR list 1023 items; full coverage chưa chứng minh |
| Reads | meta_catalog rồi collection reads theo source local; 45 loại UI |
| Writes | Không business write observed |
| ID/version/revision/context | Entity type/code; metadata không exact business version set |
| Human path | Tìm/filter generic across collections |
| Agent path | Tái dùng Directus read/filter; không mặc định list giới hạn = searched all |
| Ownership | Không trộn loài/catalog vớicanonical Definition ownership |
| Reuse/where-used/diff/readiness | Có generic list; source cap/per-collection/loại mapping cần bounded coverage |
| Gap groups | G01 G02 G04 |
| Disposition | MERGE CAPABILITY INTO P01; không list implementation mỗi Registry |
| Evidence | [source/2ee3682f9f-all](source/2ee3682f9f-all); [source/9a04a213b6-DkEoWw5i.js](source/9a04a213b6-DkEoWw5i.js); [browser/C30-initial.json](browser/C30-initial.json); [browser/C30-initial.png](browser/C30-initial.png); [browser/C30-initial.txt](browser/C30-initial.txt); [native-source/web/pages/knowledge/registries/all/index.vue](native-source/web/pages/knowledge/registries/all/index.vue) |

## C31 · Workflow category/Definition browse (không instance)
R8,R7 · U24, U23 · https://vps.incomexsaigoncorp.vn/knowledge/workflows

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Workflow category/Definition browse (không instance) |
| Role đề nghị | LIBRARY/MASTER |
| Implementation truth | partial — deployed category UI khác local workflows list source |
| Reads | Deployed SSR C1-GEN/C1-PC/C1-TTC; local tbl_workflow_list chỉ là evidence asset có sẵn |
| Writes | Không write thực hiện; category navigation |
| ID/version/revision/context | Category codes không phải workflow_instance/attempt/version pins |
| Human path | Mở khu nghiệp vụ rồi workflow |
| Agent path | Native workflow catalog đọc có thể reuse; runtime read-back chưa chứng minh |
| Ownership | Definition category khác Workflow Instance; không dùng làm monitor |
| Reuse/where-used/diff/readiness | Có entry phân khu; chưa có attempt/handoff/health runtime |
| Gap groups | G01 G02 G07 G08 |
| Disposition | KEEP REFERENCE native category entry; MERGE P01, không runtime workspace |
| Evidence | [source/68dd68004a-workflows](source/68dd68004a-workflows); [source/9a04a213b6-DkEoWw5i.js](source/9a04a213b6-DkEoWw5i.js); [browser/C31-initial.json](browser/C31-initial.json); [browser/C31-initial.png](browser/C31-initial.png); [browser/C31-initial.txt](browser/C31-initial.txt); [native-source/web/pages/knowledge/workflows/index.vue](native-source/web/pages/knowledge/workflows/index.vue) |

## C32 · Legacy technical tasks / list
R2,R8 · U07, U24, U25 · https://vps.incomexsaigoncorp.vn/knowledge/current-tasks

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Legacy technical tasks / list |
| Role đề nghị | CONTEXTUAL VIEW |
| Implementation truth | partial — deployed tasks dữ liệu hiện có; target business Task Instance chưa chứng minh |
| Reads | tbl_tasks_list/useDirectusTable; tasks technical collaboration |
| Writes | Không write trong review; useTasks có create/update/comment source nhưng không chạy |
| ID/version/revision/context | Task row ID/status; không workflow_instance/attempt/pinned set |
| Human path | Lọc tìm task kỹ thuật |
| Agent path | Native Directus tasks read; không claimed Factory Task runtime |
| Ownership | tasks legacy khác Task Instance target; không migrate/merge dựa cùng tên |
| Reuse/where-used/diff/readiness | Table filter/sort reusable; không HMITL/AUTO view contract |
| Gap groups | G01 G03 G07 |
| Disposition | KEEP REFERENCE existing technical tasks, reuse generic list P01/P04 |
| Evidence | [source/92352215eb-current-tasks](source/92352215eb-current-tasks); [source/9a04a213b6-DkEoWw5i.js](source/9a04a213b6-DkEoWw5i.js); [browser/C32-initial.json](browser/C32-initial.json); [browser/C32-initial.png](browser/C32-initial.png); [browser/C32-initial.txt](browser/C32-initial.txt); [native-source/web/pages/knowledge/current-tasks/index.vue](native-source/web/pages/knowledge/current-tasks/index.vue); [native-source/web/composables/useTasks.ts](native-source/web/composables/useTasks.ts) |

## C33 · Knowledge document review / approval
R7 · U22, U23 · https://vps.incomexsaigoncorp.vn/approval-desk

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Knowledge document review / approval |
| Role đề nghị | FALLBACK |
| Implementation truth | partial/source risk — live 2 buttons; write authority chưa thử |
| Reads | Deployed UI matches compact Approval Desk; local source có approval routes trùng, knowledge_documents iframe |
| Writes | Source compact approve updateItem knowledge_documents.status=published; documentId fallback 1; requestChange alert. Không click |
| ID/version/revision/context | route.params.id fallback 1; không exact revision/expected hash/signer decision |
| Human path | Đọc iframe/review; không bấm approve trong lượt |
| Agent path | Không generic approval receipt contract; Agent không quyền tự ký |
| Ownership | Knowledge document publish không hệ approval cross-object; approve≠publish cần tách |
| Reuse/where-used/diff/readiness | Có iframe/hai source variants, chưa shared test/diff/authority gate |
| Gap groups | G01 G04 G05 G08 |
| Disposition | KEEP FALLBACK knowledge-specific; MERGE safe review capability P05; không adopt handler |
| Evidence | [source/d0d2e55397-approval-desk](source/d0d2e55397-approval-desk); [source/9a04a213b6-DkEoWw5i.js](source/9a04a213b6-DkEoWw5i.js); [browser/C33-initial.json](browser/C33-initial.json); [browser/C33-initial.png](browser/C33-initial.png); [browser/C33-initial.txt](browser/C33-initial.txt); [native-source/web/pages/approval-desk.vue](native-source/web/pages/approval-desk.vue); [native-source/web/pages/approval-desk/index.vue](native-source/web/pages/approval-desk/index.vue); [native-source/web/components/shared/ApprovalWidget.vue](native-source/web/components/shared/ApprovalWidget.vue) |

## C34 · Report library / technical reports
R3 · U11, U13 · https://vps.incomexsaigoncorp.vn/reports

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Report library / technical reports |
| Role đề nghị | LIBRARY/MASTER |
| Implementation truth | partial — actual SSR 6 reports and counters; MOUT canonical integration chưa chứng minh |
| Reads | table_registry tbl_report_home + /api/reports/live + Directus count |
| Writes | Read/list; no write duringreview |
| ID/version/revision/context | table_id/route/loài; chưa pinnedMOUTrevision |
| Human path | Browse/search/openreadreport |
| Agent path | Existing generic table/dataread reuse trướcMOUTcustomrenderer |
| Ownership | Technicalreport contracts không tự là businessMOUTdefinition |
| Reuse/where-used/diff/readiness | Declaredcolumns/rowlink/count pattern cónativepath; thiếuquery/context policy/version |
| Gap groups | G01 G02 G03 G05 |
| Disposition | KEEP CANONICAL ROLE đề nghị reuse renderer P01/P03; giữ reports consumer |
| Evidence | [source/39f11da0d1-reports](source/39f11da0d1-reports); [source/9a04a213b6-DkEoWw5i.js](source/9a04a213b6-DkEoWw5i.js); [browser/C34-initial.json](browser/C34-initial.json); [browser/C34-initial.png](browser/C34-initial.png); [browser/C34-initial.txt](browser/C34-initial.txt); [native-source/web/pages/reports/index.vue](native-source/web/pages/reports/index.vue); [native-source/web/components/shared/DirectusTable.vue](native-source/web/components/shared/DirectusTable.vue); [native-source/web/composables/useDirectusTable.ts](native-source/web/composables/useDirectusTable.ts) |

## C35 · Guidance library
R7 · U20, U28 · https://vps.incomexsaigoncorp.vn/help

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Guidance library |
| Role đề nghị | LIBRARY/MASTER |
| Implementation truth | partial — deployed 2 collections/3 articles; object-version Guidance chưa chứng minh |
| Reads | HelpCollectionsIndex read help_collections; GlobalSearch help_articles |
| Writes | Không write thực hiện |
| ID/version/revision/context | Help collection/articles không applies-to target object/revision/current SSOT |
| Human path | Search/read guide khi cần |
| Agent path | Reuse content API; Agent maintain proposal theo quyền, chưa read-back Guidance gắn với object |
| Ownership | Guidance owner khác workflow owner; không copy text mỗi MOIT/MOT |
| Reuse/where-used/diff/readiness | Search/browse existing; thiếu context/version freshness |
| Gap groups | G01 G02 G08 |
| Disposition | KEEP CANONICAL ROLE đề nghị P01 Guidance/P05 context Help |
| Evidence | [source/4e56f965b0-help](source/4e56f965b0-help); [source/9a04a213b6-DkEoWw5i.js](source/9a04a213b6-DkEoWw5i.js); [browser/C35-initial.json](browser/C35-initial.json); [browser/C35-initial.png](browser/C35-initial.png); [browser/C35-initial.txt](browser/C35-initial.txt); [native-source/web/pages/help/index.vue](native-source/web/pages/help/index.vue); [native-source/web/components/help/CollectionsIndex.vue](native-source/web/components/help/CollectionsIndex.vue) |

## C36 · People / authoritative source
R6 · U19 · https://vps.incomexsaigoncorp.vn/admin/users

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | People / authoritative source |
| Role đề nghị | FALLBACK |
| Implementation truth | source-only/unproven — live Directus login redirect rồi lỗi 404 |
| Reads | Deployed Directus UI; Nuxt source cùng path chỉ asset candidate, không source đang phục vụ |
| Writes | Không login/change/write; không khẳng định mutation route local đang deployed |
| ID/version/revision/context | Redirect/admin/login?redirect=/users; không record context verified |
| Human path | Không truy cập được màn record trong session này |
| Agent path | Dùng API đã được phân quyền ở Gate sau; không bypass auth |
| Ownership | People/auth source cần map employee/role/delegation; knowledge folder không phải org tree |
| Reuse/where-used/diff/readiness | Source shows possible native read; access/delivery mapping chưa chứng minh |
| Gap groups | G01 G05 G06 G08 |
| Disposition | KEEP FALLBACK; chưa adopt URL current; input Gate2 route/auth design |
| Evidence | [source/8d803d0104-users](source/8d803d0104-users); [source/9fa9201061-index.DZKk-X6d.entry.js](source/9fa9201061-index.DZKk-X6d.entry.js); [browser/C36-initial.json](browser/C36-initial.json); [browser/C36-initial.png](browser/C36-initial.png); [browser/C36-initial.txt](browser/C36-initial.txt); [browser/C36-ready-dom.txt](browser/C36-ready-dom.txt); [browser/C36-ready.png](browser/C36-ready.png); [browser/C36-ready.txt](browser/C36-ready.txt); [native-source/web/pages/admin/users.vue](native-source/web/pages/admin/users.vue) |

## C37 · Knowledge tree admin
R7 · U20 · https://vps.incomexsaigoncorp.vn/admin/knowledge-tree

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Knowledge tree admin |
| Role đề nghị | FALLBACK |
| Implementation truth | source-only/unproven — live Directus login redirect rồi lỗi 404 |
| Reads | Deployed Directus UI; Nuxt source cùng path chỉ asset candidate, không source đang phục vụ |
| Writes | Không login/change/write; không khẳng định mutation route local đang deployed |
| ID/version/revision/context | Redirect/admin/login?redirect=/knowledge-tree; không record context verified |
| Human path | Không truy cập được màn record trong session này |
| Agent path | Dùng API đã được phân quyền ở Gate sau; không bypass auth |
| Ownership | knowledge_documents hierarchy khác organizational 7 tầng |
| Reuse/where-used/diff/readiness | Source shows possible native read; access/delivery mapping chưa chứng minh |
| Gap groups | G01 G05 G06 G08 |
| Disposition | KEEP FALLBACK; chưa adopt URL current; input Gate2 route/auth design |
| Evidence | [source/1d9e888f3e-knowledge-tree](source/1d9e888f3e-knowledge-tree); [source/9fa9201061-index.DZKk-X6d.entry.js](source/9fa9201061-index.DZKk-X6d.entry.js); [browser/C37-initial.json](browser/C37-initial.json); [browser/C37-initial.png](browser/C37-initial.png); [browser/C37-initial.txt](browser/C37-initial.txt); [browser/C37-ready-dom.txt](browser/C37-ready-dom.txt); [browser/C37-ready.png](browser/C37-ready.png); [browser/C37-ready.txt](browser/C37-ready.txt); [native-source/web/pages/admin/knowledge-tree.vue](native-source/web/pages/admin/knowledge-tree.vue) |

## C38 · Knowledge folder tree / browse
R7 · U20 · https://vps.incomexsaigoncorp.vn/knowledge-tree

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Knowledge folder tree / browse |
| Role đề nghị | CONTEXTUAL VIEW |
| Implementation truth | partial — live knowledge_documents tree, không nguồn tổ chức |
| Reads | useKnowledgeTreeLazy→knowledge_documents / parent_document_id |
| Writes | Source createFolder/moveNode qua Directus; không click new/move |
| ID/version/revision/context | Document ID/parent; không org-node authority/effective version |
| Human path | Browse Knowledge folders; không cấu hình org 7 tầng |
| Agent path | Native API read có thể reuse; khác context resolver |
| Ownership | Knowledge classification khác organization và assembly tier; không gộp 3 cây |
| Reuse/where-used/diff/readiness | Lazy tree pattern tái dùng; còn mapping nguồn tổ chức |
| Gap groups | G01 G06 G08 |
| Disposition | KEEP CANONICAL ROLE cho Knowledge; MERGE tree presentation selectively |
| Evidence | [source/c337f9a6de-knowledge-tree](source/c337f9a6de-knowledge-tree); [source/9a04a213b6-DkEoWw5i.js](source/9a04a213b6-DkEoWw5i.js); [browser/C38-initial.json](browser/C38-initial.json); [browser/C38-initial.png](browser/C38-initial.png); [browser/C38-initial.txt](browser/C38-initial.txt); [native-source/web/pages/knowledge-tree/index.vue](native-source/web/pages/knowledge-tree/index.vue); [native-source/web/composables/useKnowledgeTree.ts](native-source/web/composables/useKnowledgeTree.ts) |

## C39 · NTGV / rule and people resolution
R6 · U17, U19 · https://vps.incomexsaigoncorp.vn/admin-new-modt?tang=T1&cau-hinh=nguyen-tac-giao-viec

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | NTGV / rule and people resolution |
| Role đề nghị | EXPERT EDITOR |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | Cùng source New MODT C03, NTGV01 mẫu + MODULE assignment / executor / delegate / report |
| Writes | trạng thái đề xuất trong sessionStorage; không có truy vấn People/Delegation thật |
| ID/version/revision/context | cau-hinh=nguyen-tac-giao-viec URL không canonical rule ID/revision/authority; bối cảnh T1 mẫu |
| Human path | NẾU 3 conditions/AND/OR→executor/report/forwarder; expert review |
| Agent path | Không có Agent write/read-back cùng canonical revision được chứng minh tại candidate; Gate2 cần contract dùng chung, không Agent sửa JS cho mỗi object. |
| Ownership | Actual D04: NTGV forwarder vs MODULE Người làm thay / ủy quyền vs drawer delegate; ảnh hưởng trách nhiệm |
| Reuse/where-used/diff/readiness | BLOCK thiếu executor / WARN các vai khác chỉ Help; không có resolved actor record |
| Gap groups | G01 G02 G04 G05 G06 G08 |
| Disposition | KEEP EXPERT NTGV owner P03; D04 OWNER DECISION REQUIRED |
| Evidence | [source/38a341a89e-admin-new-modt](source/38a341a89e-admin-new-modt); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/4cebec5b2f-mow-t1-work-standard-v1.js](source/4cebec5b2f-mow-t1-work-standard-v1.js); [source/a7f08313d4-ntgv-rule-table-v1.js](source/a7f08313d4-ntgv-rule-table-v1.js); [source/edce88572c-mvx-v3.js](source/edce88572c-mvx-v3.js); [source/2e812fe4dd-eco-nav.js](source/2e812fe4dd-eco-nav.js); [source/4cdcaf8e9f-mow-canvas-url-v1.js](source/4cdcaf8e9f-mow-canvas-url-v1.js); [browser/C39-initial.json](browser/C39-initial.json); [browser/C39-initial.png](browser/C39-initial.png); [browser/C39-initial.txt](browser/C39-initial.txt) |

## C40 · Workflow runtime graph / context
R8 · U24, U25 · https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html?tang=T2&che-do=van-hanh

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | Workflow runtime graph / context |
| Role đề nghị | CONTEXTUAL VIEW |
| Implementation truth | mock/static/local — không canonical-connected |
| Reads | NV/T nodes, người và due dates khai inline; MVX/mow work standard |
| Writes | Không thấy runtime write; modes/edits JS local |
| ID/version/revision/context | T2/van-hanh URL; không Workflow Instance ID/Task Instance ID/Attempt/pinned set |
| Human path | Inspect topology/progress/branch; không default manual authoring |
| Agent path | Chưa có AUTO event/result stream connected |
| Ownership | Instance view không được sửa Definition; ranh giới graph context với owner editor chưa chứng minh |
| Reuse/where-used/diff/readiness | Graph presentation reuse theo R1/D03; không occurrence/attempt/retry trace |
| Gap groups | G01 G05 G06 G07 |
| Disposition | KEEP CANONICAL ROLE contextual P04/P03 theo D03; không runtime PASS |
| Evidence | [source/9d1f3e1a85-mow-unified-canvas-v2.html](source/9d1f3e1a85-mow-unified-canvas-v2.html); [source/c0368304de-eco-nav.js](source/c0368304de-eco-nav.js); [source/6b762669d0-eco-nav.js](source/6b762669d0-eco-nav.js); [source/4cebec5b2f-mow-t1-work-standard-v1.js](source/4cebec5b2f-mow-t1-work-standard-v1.js); [source/edce88572c-mvx-v3.js](source/edce88572c-mvx-v3.js); [source/2e812fe4dd-eco-nav.js](source/2e812fe4dd-eco-nav.js); [source/4cdcaf8e9f-mow-canvas-url-v1.js](source/4cdcaf8e9f-mow-canvas-url-v1.js); [browser/C40-initial.json](browser/C40-initial.json); [browser/C40-initial.png](browser/C40-initial.png); [browser/C40-initial.txt](browser/C40-initial.txt) |

## S01 · MOIT form / MOUT table generic rendering
R3 · U09, U10, U11, U12, U13 · source group

| Câu hỏi | Kết quả |
|---|---|
| Object / stage | MOIT form / MOUT table generic rendering |
| Role đề nghị | CONTEXTUAL VIEW |
| Implementation truth | partial — đường đọc UForm đã có trong deployed source + fixture bounded đã PM nhận tại Gate0; target integration chưa chứng minh |
| Reads | Form block→UForm→FormCustom.ts schema; SharedDirectusTable → table_registry + Directus/gateway |
| Writes | Current UForm createItem inbox; Gate0 lab có generic adapter/guard writes riêng. DirectusTable chỉ đọc. Không thực hiện write mới |
| ID/version/revision/context | Form.id/inboxformref; G0 pins/expected hash chỉ trong fixture; còn thiếu mapping canonical MOIT/version |
| Human path | Generic form input và read report; người review nghĩa/quyền; không bắt mapping fields bằng tay |
| Agent path | Agent declaration thêm note/refetch đã PM nhận + 36 UI hashes không đổi trong bounded proof; mở rộng contract target thuộc Gate3/4 |
| Ownership | Renderer không sở hữu Field meaning/NTGV; UForm có email validation hardcoded và query prefill, cần giới hạn theo profile |
| Reuse/where-used/diff/readiness | Tài sản reuse có evidence mạnh; không tự thêm component MOITForm; table composition hiện có |
| Gap groups | G01 G03 G04 G05 G07 |
| Disposition | KEEP CANONICAL ROLE generic renderer; reuse Gate0 adapter sau TARGET compatibility/rehearsal |
| Evidence | [native-source/web/components/blocks/Form.vue](native-source/web/components/blocks/Form.vue); [native-source/web/components/base/UForm.vue](native-source/web/components/base/UForm.vue); [native-source/web/components/base/FormCustom.ts](native-source/web/components/base/FormCustom.ts); [native-source/web/components/shared/DirectusTable.vue](native-source/web/components/shared/DirectusTable.vue); [native-source/web/composables/useDirectusTable.ts](native-source/web/composables/useDirectusTable.ts); [accepted/Gate0/README.md](accepted/Gate0/README.md); [accepted/Gate0/code-inventory.md](accepted/Gate0/code-inventory.md) |
