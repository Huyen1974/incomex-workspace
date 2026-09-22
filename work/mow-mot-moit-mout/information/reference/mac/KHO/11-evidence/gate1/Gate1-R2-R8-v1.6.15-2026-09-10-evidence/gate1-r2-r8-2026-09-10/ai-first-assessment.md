# AI-first assessment — toàn Gate1

**Hiện tại có:** nhiều phần bố cục/component tốt và một số trang đọc dữ liệu thật. **Chưa có:** default path đã nối đủ để người chỉ quyết nghĩa/quyền/ngoại lệ. Người hiện vẫn phải điều phối nhiều builder và khai lặp các cấu hình máy có thể lấy từ metadata. Không candidate nào được chứng minh DEFAULT AI-FIRST FIT toàn vòng; không đặt tỷ lệ 98%.

H1 = Intent; H2 = semantic ambiguity; H3 = expert judgement; H4 = authority/approval; H5 = exception. Đây là giới hạn quyết định trong authoring; nhập dữ liệu thực địa ở HMITL có thể là việc nghiệp vụ thật, không phải mọi lần nhập đều cần loại bỏ.

| Pattern/family | Phân loại | Manual lặp hiện thấy | Có cần H1–H5? / xử lý Gate2 |
|---|---|---|---|
| P01 mọi library | AI-FIRST WITH GATE2 GAPS | Tìm nhiều Master, chọn cây 7 tầng nhiều lần, mở detail rồi gặp ngõ cụt | Máy giải context và catalog search trước. H2 chỉ khi candidates còn khác nghĩa; không hỏi Owner vì UI chưa map table. G01/G02. |
| P02 mọi Definition | AI-FIRST WITH GATE2 GAPS | Người tự đọc nhiều status/config để tự suy đủ hay chưa | Reuse Nháp2 3 câu, máy tổng hợp từ same revision. Người H1–H4 ở quyết định material. G03/G04/G05. |
| P03 MOW/MOT | MANUAL-FIRST / EXPERT ONLY | Tự kéo graph, khai từng bước, collection, trigger, conditions, people | Agent compile/reuse/bind; H2/H3 ca nghĩa/nhánh chưa rõ, H4 quyền. Default không qua xưởng. G01–G06. |
| P03 MOIT/MOUT | MANUAL-FIRST / EXPERT ONLY | Chọn lại cột/FK/layout, gõ physical name, đặt lịch/người nhận | AI khai refs/layout/query theo profile; người xác nhận nghĩa, miền đọc, kết quả mong đợi. H2/H3/H4, không catalog field-by-field. S01 trước renderer mới. |
| P01/P03 Field/Table/Trigger/Condition | AI-FIRST WITH GATE2 GAPS cho library; editor mẫu EXPERT ONLY | Người tạo nguyên liệu vì không tìm thấy; mỗi builder có picker riêng | SEARCH_INCOMPLETE phải hiện đúng, lookup/reuse/version/variant trước CREATE_NEW; H2 cho mơ hồ, H4 admission, expert schema thuộc P03. G01/G02/G04. |
| P03 NTGV + People | MANUAL-FIRST / EXPERT ONLY | Điền người/role/rule ở nhiều nơi, tự kiểm tình trạng duyệt | Resolver từ nguồn People/Role/Delegation; người chỉ H2/H4/H5. D04 cần nghĩa trách nhiệm trước. G05/G06. |
| P04 HMITL | AI-FIRST WITH GATE2 GAPS | Mở việc đúng người/context; nhập dữ liệu/quan sát thật; tự theo dõi bước kế trong mock | Phần nhập thực địa có thể cần human; tìm task/nhớ luật/đẩy bước kế không cần human làm tay. G01/G03/G06/G07. |
| P04 AUTO | AI-FIRST WITH GATE2 GAPS | Canvas/cards giống công việc người, chưa attempt/error/result monitor | Worker chạy tự động; human chỉ H5 ngoại lệ được route. Không fake Done. G07. |
| P05 lifecycle/Help | AI-FIRST WITH GATE2 GAPS | Người nhập test/approval status, copy Guidance, chỉnh JS matrix | Máy test/record/refetch; H3 expected nghiệp vụ mới, H4 chữ ký/quyền, H5 ngoại lệ. Guidance một nguồn có applies-to/version. G04/G05/G08. |

Điều kiện xác nhận sau này: cùng declaration sau Agent write phải xuất hiện ở UI đúng object/version/revision; missing-resume quay về đúng chỗ; explicit conflict và quyền; đo active human effort riêng thời gian chờ. Gate0 proof có lát cắt giúp tái dùng nhưng không thay formal Pilot Gate5/6.
