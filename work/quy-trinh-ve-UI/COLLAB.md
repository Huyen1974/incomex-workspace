# COLLAB — quy-trinh-ve-UI
Tên việc: quy-trinh-ve-UI

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner giao trực tiếp và bổ sung ngày 24/09/2026 trong ChatGPT.

### 1. Mục tiêu
1. Chốt được quy trình vẽ UI chuẩn, đảm bảo không bị thiếu. Liệt kê các câu hỏi chuẩn phải trả lời từng bước và phải có câu trả lời chính xác mới là hoàn thành.
2. Chốt được quy trình liệt kê hợp đồng thông tin => để tạo được danh mục hợp đồng thông tin, danh mục khai báo.
3. Chốt được tool làm việc này. Tool có thể cài thêm nếu cần (ưu tiên nguồn mở, nhẹ). Nhớ dùng Jev để tham khảo các khâu.
4. Toàn bộ quá trình này do AI và Agent thực hiện; User chỉ ra lệnh, duyệt các quyết định cần quyền Owner và xem kết quả.

### 2. Thế nào là hoàn thành
- Chốt được đủ 3 nội dung chuyên môn trên thành một quy trình có thể dùng lặp lại cho mọi UI.
- Mỗi bước UI có checklist/câu hỏi bắt buộc và điều kiện PASS rõ ràng; thiếu hoặc trả lời chưa chính xác thì chưa được coi là xong.
- Có quy trình sinh và kiểm danh mục hợp đồng thông tin/danh mục khai báo.
- Có tool/workflow được chọn sau khi so sánh; nếu cần cài thêm thì phải Owner duyệt trước.
- Quy trình đủ tự động để AI/Agent tự khảo sát → lập danh mục → thiết kế → kiểm tra → sửa; không yêu cầu User thao tác chi tiết.
- Hội đồng GPT · Claude · Hermes đã có ý kiến; bất đồng còn lại được đưa Owner quyết.
- Nội dung chính Owner/hội đồng đọc được trên Owner View chuẩn của VPS.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Giai đoạn hiện tại: **THẢO LUẬN/CHỐT PHƯƠNG PHÁP**. Chưa tạo `PROMPT.md`, chưa RUN Agent, chưa cài tool, chưa sửa UI/runtime.
- HTML chính: `view.html` — chứa toàn bộ nội dung đề xuất để Owner và hội đồng đọc/phản biện. Tạo theo lệnh Owner yêu cầu đưa nội dung lên VPS; commit `fe1b4c054bae59e4d5e1861efcca3a09d80d4ca6`.
- `COLLAB.md` chỉ giữ mục tiêu, quyết định, ý kiến, trạng thái và con trỏ; không giữ bản nội dung song song.
- Không tự tạo thêm file/draft/view/URL/tool project ngoài `view.html` + `COLLAB.md` nếu Owner chưa duyệt.
- Phải tách rõ ba lớp: (A) coverage quy trình UI; (B) hợp đồng thông tin/danh mục khai báo; (C) tool hỗ trợ.
- Mọi lựa chọn hữu hạn quan trọng nên tham khảo JEV theo AGENTS A5/DROOT13; JEV chỉ là bằng chứng phụ.

### Vòng trước
- — Việc mới.

## Quyết định Owner
- D01 · 2026-09-24 · Toàn bộ quá trình do AI/Agent làm; User chỉ ra lệnh, duyệt quyết định cần quyền Owner và xem kết quả.
- D02 · 2026-09-24 · Nội dung đề xuất phải được đưa lên Owner View VPS để hội đồng đọc và có ý kiến; dùng đúng HTML chính `view.html`, không tạo đường xem phụ.

## Nội dung chính
- SSOT Owner/hội đồng: `work/quy-trinh-ve-UI/view.html`.
- Nội dung hiện có: quy trình 7 bước; UI Step Contract 25 câu; coverage matrix; Information Contract 18 thuộc tính; tiêu chí chọn tool; JEV tham khảo; 8 câu hỏi phản biện hội đồng.
- Link Owner View chuẩn: `https://vps.incomexsaigoncorp.vn/knowledge/modules?task=quy-trinh-ve-UI`.

## JEV tham khảo ban đầu
- JEV01 · model `typesafe/jev-1.13-20260917` · result id `gen-dec-1790217288-56iSttNoJua2z4V7xBo7`.
- `method = matrix_contract_flow` · confidence `1.00`.
- `information_contract = contract_matrix` · confidence `1.00`.
- `tool_phase1 = text_diagram_git` · confidence `1.00`.
- Trạng thái: **REFERENCE ONLY**, chờ hội đồng phản biện; không coi JEV là quyết định.

## Ý kiến hội đồng
- P01 · GPT Chat · OPEN · Based_on `fe1b4c054bae59e4d5e1861efcca3a09d80d4ca6` · Scope: `view.html` mục 2–8.
  - Đề nghị lấy **coverage matrix → Step Contract → Information Contract → flow/state → wireframe/UI → independent check** làm xương sống.
  - Không đánh “xong UI” chỉ vì có màn hình; phải PASS coverage + contract.
  - Tool phục vụ quy trình; giai đoạn đầu ưu tiên text/Git, chỉ thêm editor trực quan nếu chứng minh cần.
  - Reviewer phải cố tình tìm missing branches: nested-create, quay lại giữ trạng thái, edit/delete + where-used, quyền, lỗi/concurrency, version/schema migration và checkpoint để AI tự làm hết.

## Cửa vào cho Reviewer
- Claude: `WS work/quy-trinh-ve-UI · Review · đọc AGENTS.md → work/quy-trinh-ve-UI/COLLAB.md → view.html · phản biện P01 và trả lời 8 câu ở mục 8; không tạo file mới, không cài tool.`
- Hermes: `WS work/quy-trinh-ve-UI · Review · đọc AGENTS.md → work/quy-trinh-ve-UI/COLLAB.md → view.html · phản biện P01 và trả lời 8 câu ở mục 8; ưu tiên missing branches/contract gaps/automation gaps; không tạo file mới, không cài tool.`
- GPT: sau phản hồi Claude/Hermes, tổng hợp ACCEPT/PARTIAL/REJECTED; điểm còn vênh chuyển OWNER theo A5.

## Owner cần quyết
- —
