# COLLAB — quy-trinh-ve-ui
Tên việc: Quy trình vẽ UI

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner giao trực tiếp ngày 24/09/2026 trong ChatGPT.

### 1. Mục tiêu
1. Chốt được quy trình vẽ UI chuẩn, đảm bảo không bị thiếu. Liệt kê các câu hỏi chuẩn phải trả lời từng bước và phải có câu trả lời chính xác mới là hoàn thành.
2. Chốt được quy trình liệt kê hợp đồng thông tin => để tạo được danh mục hợp đồng thông tin, danh mục khai báo.
3. Chốt được tool làm việc này. Tool có thể cài thêm nếu cần (ưu tiên nguồn mở, nhẹ). Nhớ dùng Jev để tham khảo các khâu.

### 2. Thế nào là hoàn thành
- Chốt được đủ 3 nội dung trên thành một quy trình có thể dùng lặp lại cho mọi UI.
- Mỗi bước UI có checklist/câu hỏi bắt buộc và điều kiện PASS rõ ràng; thiếu hoặc trả lời chưa chính xác thì chưa được coi là xong.
- Có quy trình sinh và kiểm danh mục hợp đồng thông tin/danh mục khai báo.
- Có tool/workflow được chọn sau khi so sánh; nếu cần cài thêm thì phải Owner duyệt trước.
- Hội đồng GPT · Claude · Hermes đã có ý kiến; bất đồng còn lại được đưa Owner quyết.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Việc này đang ở giai đoạn **THẢO LUẬN/CHỐT PHƯƠNG PHÁP**. Chưa tạo `PROMPT.md`, chưa RUN Agent, chưa cài tool, chưa sửa UI/runtime.
- Chỉ dùng `COLLAB.md` hiện tại làm nơi thảo luận/chốt; **không tự tạo thêm file/draft/view/URL/tool project** nếu Owner chưa duyệt.
- Phải tách rõ ba lớp: (A) coverage quy trình UI; (B) hợp đồng thông tin/danh mục khai báo; (C) tool hỗ trợ.
- Mọi lựa chọn hữu hạn quan trọng nên tham khảo JEV theo AGENTS A5/DROOT13; JEV chỉ là bằng chứng phụ.

### Vòng trước
- — Việc mới.

## 1. Phạm vi cần hội đồng chốt

### UI.1 — Quy trình vẽ UI chuẩn, không bỏ sót
Mục tiêu là không bắt đầu từ “vẽ màn hình”, mà phải quét đủ nghiệp vụ trước. Hội đồng cần chốt một **UI Step Contract** dùng chung. Bản nháp câu hỏi bắt buộc cho MỖI bước:

1. Mục tiêu của bước này là gì?
2. Actor/role nào được làm?
3. Người dùng đi vào bước này từ đâu?
4. Điều kiện nào phải có trước khi vào?
5. Người dùng bấm/chọn ở đâu để bắt đầu?
6. UI phải hiển thị những thông tin gì?
7. Người dùng phải nhập/chọn những thông tin gì?
8. Mỗi thông tin lấy từ đâu: nhập tay, kế thừa, tra cứu, tự tính hay gọi đối tượng khác?
9. Trường nào bắt buộc/tùy chọn; format/ràng buộc/validation là gì?
10. Có gọi đối tượng/công cụ/quy trình khác không? Gọi tại đâu trong UI?
11. Nếu đối tượng cần gọi **chưa tồn tại** thì đi vào quy trình tạo mới nào?
12. Quy trình tạo mới phụ thuộc đó đã có chưa? Nếu chưa có thì xử lý/gate thế nào?
13. Tạo xong đối tượng phụ thuộc thì quay lại đúng bước đang làm dở bằng cách nào; dữ liệu đang nhập có được giữ không?
14. Bấm Lưu/Xác nhận thì hệ thống ghi những gì?
15. Lưu vào đâu; ID/version/trạng thái sau lưu là gì?
16. Thành công xong thì người dùng đi đâu/nhìn thấy gì?
17. Muốn sửa đối tượng đã tạo thì bắt đầu ở đâu, bấm đâu, sửa được trường nào?
18. Muốn xóa/archive thì bắt đầu ở đâu; điều kiện, cảnh báo, ảnh hưởng và quyền là gì?
19. Có cần khôi phục/undo không; nếu có thì từ đâu?
20. Hủy/quay lại/đóng giữa chừng xử lý dữ liệu chưa lưu thế nào?
21. Lỗi validation, lỗi hệ thống, mất kết nối, dữ liệu trùng/xung đột được xử lý thế nào?
22. Permission/RBAC khác nhau làm UI thay đổi ra sao?
23. Đối tượng này đang được dùng ở đâu (where-used); sửa/xóa ảnh hưởng cái gì?
24. Cần audit/history/version/concurrency ra sao?
25. Bước này được kiểm thử và đánh PASS bằng điều kiện quan sát được nào?

**Gate đề xuất:** một bước chỉ được coi là “đã thiết kế” khi tất cả câu hỏi áp dụng đều có câu trả lời `EVIDENCED/DECIDED`; câu nào chưa áp dụng phải ghi `N/A + lý do`, không để trống.

### UI.2 — Coverage vòng đời và luồng gọi chéo
Trước wireframe cần một ma trận tối thiểu theo đối tượng × hành động:
- List/Search
- View detail
- Create
- Select/use
- Create-while-selecting
- Edit
- Delete/Archive
- Restore/Undo nếu có
- Cancel/Back
- Error/Empty/Duplicate/Conflict
- Permission
- Where-used/impact

Mỗi ô phải trỏ tới Step Contract tương ứng hoặc ghi `N/A + lý do`. Mục tiêu: nhìn ma trận là biết còn luồng nào chưa thiết kế.

### IC.1 — Quy trình liệt kê “hợp đồng thông tin”
Hội đồng cần chốt đơn vị chuẩn cho mỗi transition/bước. Bản nháp Information Contract tối thiểu:

1. Contract ID.
2. From step/object.
3. To step/object.
4. Trigger.
5. Input data/field.
6. Kiểu dữ liệu/format/unit.
7. Source/SSOT.
8. Required/optional/default.
9. Validation/business rule.
10. Identifier/key/version.
11. Output sinh ra.
12. Destination/storage.
13. Consumer/used-by.
14. Owner/quyền ghi.
15. Error/fallback/retry.
16. Create-if-missing dependency.
17. Compatibility/migration khi thay đổi schema.
18. Audit/history/retention nếu áp dụng.

**Đầu ra cần chốt:** từ các contract sinh được:
- Danh mục hợp đồng thông tin.
- Danh mục trường/khai báo chuẩn, loại bỏ trùng tên nhưng khác nghĩa.
- Bảng where-used để biết một field/contract đang được UI/quy trình nào dùng.

### TOOL.1 — Tiêu chí chọn tool
Chưa chọn tool cuối. Hội đồng phải so theo cùng tiêu chí:
- Nguồn mở là ưu tiên.
- Nhẹ, cài/vận hành đơn giản.
- Git-friendly/diff được hoặc ít nhất export text chuẩn.
- AI đọc/sửa được.
- Hỗ trợ flow/state/diagram và bảng coverage.
- Không ép vẽ hình trước khi nghiệp vụ đủ.
- Có thể link ID giữa matrix ↔ contract ↔ flow ↔ UI.
- Dễ rollback/version.
- Không tạo thêm hạ tầng/phụ thuộc nặng nếu Markdown/text hiện tại đã đủ.

Ứng viên cần khảo sát sau khi hội đồng chốt tiêu chí: workflow text/diagram-as-code (ví dụ Mermaid/PlantUML hoặc tương đương nhẹ), editor trực quan nhẹ nếu thật sự cần, BPMN chỉ khi luồng nghiệp vụ đòi hỏi. **Không cài gì ở bước thảo luận này.**

## 2. JEV tham khảo ban đầu
- JEV01 · model `typesafe/jev-1.13-20260917` · result id `gen-dec-1790217288-56iSttNoJua2z4V7xBo7`.
- `method = matrix_contract_flow` · confidence `1.00`: ma trận coverage + UI Step Contract + flow/state trước, wireframe sau.
- `information_contract = contract_matrix` · confidence `1.00`: contract theo transition, có input/source/validation/output/destination/owner/error/version/used-by.
- `tool_phase1 = text_diagram_git` · confidence `1.00`: giai đoạn 1 ưu tiên text/diagram-as-code trong Git; chưa cần Figma/BPMN/custom app.
- Trạng thái: **REFERENCE ONLY**, chờ hội đồng phản biện; không coi JEV là quyết định.

## 3. Ý kiến hội đồng

- P01 · GPT Chat · OPEN · Based_on `03ed2d8ccfc08721e76418fad810661b03614fab` + chỉ đạo Owner 24/09/2026 · Scope: UI.1/UI.2/IC.1/TOOL.1.
  - Đề nghị lấy **coverage matrix → Step Contract → Information Contract → flow/state → wireframe/UI → test lại coverage** làm thứ tự chuẩn.
  - Không cho phép đánh “xong UI” chỉ vì đã có màn hình đẹp/chạy được; phải PASS coverage + contract.
  - Tool nên phục vụ quy trình, không để công cụ quyết định quy trình. Giai đoạn đầu ưu tiên text/Git; chỉ thêm editor trực quan khi đã chứng minh nhu cầu.
  - Cần Claude và Hermes cố tình tìm các nhánh còn thiếu, đặc biệt: nested-create, quay lại giữ trạng thái, edit/delete ảnh hưởng where-used, quyền, lỗi/concurrency, version/schema migration.

## 4. Câu hỏi giao hội đồng phản biện
1. Bộ 25 câu UI Step Contract trên còn thiếu tình huống tiêu chuẩn nào?
2. Ma trận vòng đời đã đủ để “quét không sót” chưa; cần thêm chiều actor/state/channel/device nào?
3. Information Contract nên quản lý theo transition như IC.1 hay phải có thêm object/field contract riêng? Cách nào tránh trùng lặp?
4. Từ Information Contract sinh “danh mục khai báo” theo quy tắc nào để không có hai field cùng nghĩa/tên khác hoặc cùng tên/nghĩa khác?
5. Tool nào phù hợp nhất với tiêu chí nhẹ + nguồn mở + Git/AI-friendly? Tool nào chỉ nên là lớp xem, không phải SSOT?
6. Có nên quy định một máy kiểm coverage tự động (lint/checklist) hay giai đoạn đầu chỉ cần template + review?
7. Điều kiện nghiệm thu cuối của cả quy trình là gì để một AI khác có thể kiểm độc lập PASS/FAIL?

## 5. Cửa vào cho Reviewer
- Claude: `WS work/quy-trinh-ve-ui · Review · đọc AGENTS.md → work/quy-trinh-ve-ui/COLLAB.md · phản biện P01 + trả lời Q1–Q7; không tạo file mới, không cài tool.`
- Hermes: `WS work/quy-trinh-ve-ui · Review · đọc AGENTS.md → work/quy-trinh-ve-ui/COLLAB.md · phản biện P01 + trả lời Q1–Q7; ưu tiên phát hiện missing branches/contract gaps; không tạo file mới, không cài tool.`
- GPT: sau khi có phản hồi Claude/Hermes, tổng hợp ACCEPT/PARTIAL/REJECTED; điểm còn vênh chuyển OWNER theo A5.

## Owner cần quyết
- —
