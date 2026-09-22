# R9 · actual design walkthrough

**11/11 lượt hoàn tất trong prototype**: happy +10 negative. Đây là CUA browser actions trên workshop local, không phải backend runtime/authority test. Final run source đã sửa lỗi ban đầu suy approval từ stage; bản cuối giữ test/approval theo revision riêng và releasev1 khác draftv2.

## Happy path

| Bước | View | Người / máy | Máy cần làm | Evidence |
|---|---|---|---|---|
| 1 · Ý tưởng của con người | P02 | H1 | Máy nhận scope/outcome và tạo package; không yêu cầu ID. | [DOM bước1](../browser/workshop/happy-final-run-step-0.txt) |
| 2 · Tìm và đối chiếu nguyên liệu | P01 | machine | Catalog exact + near, completeness và where-used; chưa đủ nguồn thì không kết luận none. | [DOM bước2](../browser/workshop/happy-final-run-step-1.txt) |
| 3 · Lập bản nháp và nhận diện thiếu | P02 | machine | Dùng Field/Form/Trigger/NTGV đã có; một Condition >60 phút chưa tồn tại. | [DOM bước3](../browser/workshop/happy-final-run-step-2.txt) |
| 4 · Yêu cầu bổ sung Condition | P05 | machine | Request giữ package, slot, owner và return context; chưa gửi cho người thật. | [DOM bước4](../browser/workshop/happy-final-run-step-3.txt) |
| 5 · Rà chuyên môn tại owner Condition | P03 | H3 | Owner kiểm subject, unit, operator và threshold; không sửa Field global từ MOW. | [DOM bước5](../browser/workshop/happy-final-run-step-4.txt) |
| 6 · Duyệt nguyên liệu mới | P05 | H4 | Quyết định TEST chỉ cho Condition; không đồng thời duyệt MOW. | [DOM bước6](../browser/workshop/happy-final-run-step-5.txt) |
| 7 · Máy tiếp nhận và quay lại gói | P02 | machine | Read-back produced_ref/version, revalidate slot và dependency revision. | [DOM bước7](../browser/workshop/happy-final-run-step-6.txt) |
| 8 · Khai báo và đọc lại revision 2 | P02 | machine | Thêm Ghi chú đã có bằng declaration; cùng renderer, owner và package. | [DOM bước8](../browser/workshop/happy-final-run-step-7.txt) |
| 9 · Diff, tác động và readiness | P05 | machine | Một nguồn findings theo package/revision/dependency digest; không số mẫu không nguồn. | [DOM bước9](../browser/workshop/happy-final-run-step-8.txt) |
| 10 · Chạy bộ kiểm của bản nháp | P05 | machine | Kết quả TEST có suite/revision/digest. Không dùng test revision cũ cấp quyền release. | [DOM bước10](../browser/workshop/happy-final-run-step-9.txt) |
| 11 · Xin duyệt đúng bản và đúng quyền | P05 | H4 | Scope quyết định TEST ghi rõ cả publish và activate trên revision2; không cấp quyền thật. | [DOM bước11](../browser/workshop/happy-final-run-step-10.txt) |
| 12 · Phát hành rồi gắn active binding | P05 | machine | Release closure v1 bất biến trong fixture; active binding riêng, audit đọc lại. | [DOM bước12](../browser/workshop/happy-final-run-step-11.txt) |
| 13 · Occurrence sinh instance | P04 | machine | Occurrence khác Trigger Definition; instance pin release v1. Dedupe theo occurrence. | [DOM bước13](../browser/workshop/happy-final-run-step-12.txt) |
| 14 · Người thực hiện ghi nhận thời lượng | P04 | HMITL | Nhập nghiệp vụ có chủ đích; actor/time/version là máy điền và server target kiểm. | [DOM bước14](../browser/workshop/happy-final-run-step-13.txt) |
| 15 · Worker xử lý AUTO | P04 | machine | Không có AUTO Done. Worker dùng capability/pinned input; native queue owns retry/ack. | [DOM bước15](../browser/workshop/happy-final-run-step-14.txt) |
| 16 · Kiểm output và kết thúc | P04 | machine | Có receipt và MOUT đọc lại; missing output không được kết thúc. | [DOM bước16](../browser/workshop/happy-final-run-step-15.txt) |
| 17 · Góp ý từ đúng ngữ cảnh | P05 | H1 | Feedback tự gắn context/instance/release; không yêu cầu dán trace hay ID. | [DOM bước17](../browser/workshop/happy-final-run-step-16.txt) |
| 18 · Lập version cải tiến | P02 | machine | Version2 DRAFT liên feedback; instance cũ vẫn pin releasev1. Chưa duyệt version2. | [DOM bước18](../browser/workshop/happy-final-run-step-17.txt) |

## Negative / resume

| Case | View | Chặn / việc máy | Quyết định người | Resume | Actual evidence |
|---|---|---|---|---|---|
| N01 · Tìm chưa đủ / nghĩa mơ hồ | P01 | INCOMPLETE_SEARCH / AMBIGUOUS; Máy thử lại nguồn có quyền, so subject/unit; nếu vẫn còn hai nghĩa hợp lệ thì hỏi H2 shortlist. | H2 · Chọn nghĩa minute sau khi nguồn đã đủ (H2 · TEST) | Giữ intent/package; quay lại search có completeness và lý do chọn. | [blocked](../browser/workshop/N01-blocked.txt), [resume](../browser/workshop/N01-resumed.txt), [to end](../browser/workshop/N01-final.json) |
| N02 · Thiếu nguyên liệu | P05 | MISSING_INGREDIENT; Máy tạo/đọc request cùng fingerprint, route owner; chờ produced version rồi revalidate. | machine · Diễn sửa lỗi: theo request và mở owner editor | Đi P03→H4 nguyên liệu→resume, không nhập lại ý tưởng. | [blocked](../browser/workshop/N02-blocked.txt), [resume](../browser/workshop/N02-resumed.txt), [to end](../browser/workshop/N02-final.json) |
| N03 · Bản cũ / xung đột | P05 | STALE_REVISION / 409; Máy đọc bản hiện hành, tạo diff; chỉ auto-merge phần không xung đột đã có policy. | H3 · Đối chiếu thay đổi và nhận revision mới (H3 · TEST) | Về readiness→test→approval trên revision mới; không overwrite mù. | [blocked](../browser/workshop/N03-blocked.txt), [resume](../browser/workshop/N03-resumed.txt), [to end](../browser/workshop/N03-final.json) |
| N04 · Caller không đủ quyền | P05 | FORBIDDEN / 403; Tạo handoff request tới owner; giữ package read-only cho caller, recheck sau quyết định quyền riêng. | H4 · Diễn Owner đủ quyền tiếp nhận (H4 · TEST) | Đúng owner review cùng package; quyết định TEST không cấp quyền thật. | [blocked](../browser/workshop/N04-blocked.txt), [resume](../browser/workshop/N04-resumed.txt), [to end](../browser/workshop/N04-final.json) |
| N05 · Thiếu assignee / ủy quyền hết hạn | P04 | BLOCKED_ASSIGNMENT; Máy re-resolve từ NTGV/People; người có quyền xử lý reassign nếu nguồn vẫn thiếu. | H5 · Diễn reassign hợp lệ từ nguồn người (H5 · TEST) | Resume cùng task/instance, history executor trước còn; D04 vẫn chờ Owner thật. | [blocked](../browser/workshop/N05-blocked.txt), [resume](../browser/workshop/N05-resumed.txt), [to end](../browser/workshop/N05-final.json) |
| N06 · Kiểm thử không đạt | P05 | TEST_FAILED; Finding route owner-editor, sửa declaration rồi chạy lại suite cho revision mới. | machine · Diễn sửa lỗi: sửa khai báo và kiểm lại | Về readiness và test; exact digest mới trước approval. | [blocked](../browser/workshop/N06-blocked.txt), [resume](../browser/workshop/N06-resumed.txt), [to end](../browser/workshop/N06-final.json) |
| N07 · Duyệt bị từ chối / hết hạn | P05 | APPROVAL_DENIED_OR_EXPIRED; Giữ draft/review packet, recheck revision/test và xin decision mới khi đủ điều kiện. | H4 · Xem lại và duyệt đúng bản (H4 · TEST) | Quay approval→publish; không tự dùng chữ approved cũ. | [blocked](../browser/workshop/N07-blocked.txt), [resume](../browser/workshop/N07-resumed.txt), [to end](../browser/workshop/N07-final.json) |
| N08 · AUTO lỗi / retry | P04 | AUTO_RETRY_WAIT; Native queue retry bounded same logical effect key; nếu effect unknown phải reconcile trước retry. | machine · Diễn native retry đã đối chiếu receipt | Cùng instance/release, attempt2 riêng; không nút AUTO Done. | [blocked](../browser/workshop/N08-blocked.txt), [resume](../browser/workshop/N08-resumed.txt), [to end](../browser/workshop/N08-final.json) |
| N09 · Thiếu output | P04 | OUTPUT_INCOMPLETE; Máy đối chiếu output slot, tìm lại receipt; còn thiếu thì owner exception, không giả done. | H5 · Diễn giải quyết output thiếu (H5 · TEST) | Resume output check cùng instance rồi end; giữ evidence thiếu ban đầu. | [blocked](../browser/workshop/N09-blocked.txt), [resume](../browser/workshop/N09-resumed.txt), [to end](../browser/workshop/N09-final.json) |
| N10 · Deactivate / retire còn where-used | P02 | RETIRE_BLOCKED_WHERE_USED; Máy lập impact plan: deprecate/replacement cho future bindings, bảo toàn current instance/history. | H4 · Chấp nhận deprecate cho lần dùng mới (H4 · TEST) | Return improvement draft; không thay pin instancev1, không xóa vật cũ. | [blocked](../browser/workshop/N10-blocked.txt), [resume](../browser/workshop/N10-resumed.txt), [to end](../browser/workshop/N10-final.json) |

## Số đo và cách hiểu

Happy final run: **5 quyết định H1–H5**, **1 lần nộp nghiệp vụ HMITL**, **0 navigation bắt buộc**, **0 tìm tay**, **0 raw ID**, **0 nhập lại cấu hình máy biết**, **12 tool stages mô phỏng**, **0 context loss**.18 nút advance trong final run sinh18semantic actions;5 quyết định gồm ý tưởngH1, nghĩa ConditionH3, approval nguyên liệuH4, approval workflowH4 và ý tưởng cải tiếnH1. Khởi động/reset/selection của người test là thao tác harness riêng. Không tính input nghiệp vụ thật là lỗi tự động authoring.

10 negative bắt đầu tại checkpoint có fixture tiền điều kiện; metric của mỗi negative là phần từ checkpoint đến end, không cộng thành cả quy trình hoặc dùng để tính % tiết kiệm. Source snapshot và raw trace giữ các bước giả lập; không có actual Agent tool invocation ở workshop.5 lần navigation tùy chọn được kiểm riêng trong pattern-context-results.json, cùng object/package/scope. Tất cả patterns đọc một state; fixture.json là bản evidence của fixture.js, không thêm nguồn truth runtime.

Lượt đầu có một click không tiến và projection V2 chưa rõ; raw evidence giữ, self-review fix ghi riêng. Final happy18clicks và10branch reruns đạt, không lấy lượt lỗi làm final. Không phải test thời gian người thật; chưa có98%, chưa chứng minh khả năng AI đầu-cuối hay kết quả O1–O3.

## Reuse / giới hạn hiển thị

CSS Master/Nháp2 trích nguyên rule,5pattern bám accepted role map;3câu hỏi Nháp2 giữ. Không chạy nguyên master-list.js vì chứa TREE/mock truth khác; không clone5apps. JS composition/state là workshop code mới có kê riêng. Runtime UI live lab tái dùng Form/DirectusTable với session thật nằm ở ../platform và ../browser/ui-*. Workshop không thay proof đó. [Mở workshop](../workshop/index.html).
