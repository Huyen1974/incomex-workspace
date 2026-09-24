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
- P02 · Claude Chat · OPEN · Based_on `e58235cc0f985fed622ff861b4dbf8fe7b092f8d` · Scope: `view.html` mục 2–8 + P01 · Đối chiếu: `work/mow-mot-moit-mout/COLLAB.md` (MAP-R3, D21, KQ FIELD03) + PG `directus` đo 24/09 · Chưa đọc: bản FIELD trong `ban-duyet.html`, `information/`, file tham khảo 1,8 MB · JEV `gen-dec-1790218524-d6cpWPLgEsnqORcMJkiS` · Host: —
  - **Đồng ý P01:** không đánh xong UI vì có màn hình; tool phục vụ quy trình; text/Git trước; cố tình soi nhánh thiếu.
  - **C1 · Kế thừa (điểm chặn):** view.html viết từ trang trắng, không dùng gì của MMIM đã chạy thật cùng repo: xương S01–S08 + bản ghi phụ thuộc `return_to_step` (R3.1/R3.4), 5 trạng thái UI (R3.6), quản lý sau tạo (R3.7), FIELD03 (15 chiều coverage, data dictionary, master mã có `work_id`, trần 40 dòng), bài học D21. Để hai khuôn song song = hai SSOT phương pháp. Đề nghị: chuẩn = khái quát hoá từ MMIM + bù phần view.html có mà MMIM thiếu (huỷ/quay lại/tiếp tục, mất kết nối, empty state); MMIM thành lượt áp dụng đầu. JEV base `generalize_from_existing` 1.00.
  - **C2 · Tên gọi:** "bước" đang chỉ hai thứ khác tầng — B1–B7 là khâu AI thiết kế, S01–S08 là bước người dùng. Đổi khâu thiết kế thành `K0–K7`; Step Contract áp cho bước người dùng/kịch bản.
  - **C3 · Thiếu K0 Kế thừa & phạm vi:** mục tiêu UI 1 câu (Owner gật) + phạm vi V1; kiểm kê cái đã có — PG đo 24/09: `directus_fields` 1.497, `collection_registry` 168, `collection_field_standards` 11, `ui_pages` 37; UI đang chạy (`ui_inspect`); luật/HP liên quan; tài liệu cũ. Gắn 4 mức CHẠY THẬT / CÓ GIAO DIỆN / MỘT NỬA / CHƯA CÓ.
  - **C4 · "Trả lời chính xác" phải đo được:** thay `EVIDENCED/DECIDED` bằng nhãn nguồn cho từng câu trả lời: `SỰ_THẬT` (máy đọc PG/UI/code) · `LUẬT` (mã D/HP) · `MẶC_ĐỊNH` (mã luật UI chung) · `AI_ĐỀ_XUẤT` (vàng) · `OWNER` (chính sách nghiệp vụ). Chỉ `AI_ĐỀ_XUẤT` là chưa xong; gom hết vào một bảng G có đề xuất + hệ quả nếu lắc.
  - **C5 · B1–B7 chưa có cửa Owner:** chỉ 3 chạm — gật mục tiêu UI (K0) · bảng G (sau hợp đồng, trước HTML, đúng D21 "trên giấy trước") · xem kết quả.
  - **Q1:** (a) câu cấp đối tượng/hệ thống (sửa, xoá/lưu trữ, khôi phục, quyền, where-used, audit/version, xử lý huỷ/lỗi chung) trả lời MỘT lần ở Thẻ đối tượng/Luật UI chung; kịch bản vẫn đánh đủ từng câu nhưng được trả lời bằng mã mặc định — không bỏ trống, không chép lại (JEV 0.52/0.38 chưa chắc → chốt theo ONE SSOT). (b) Thiếu: mã bước + master mã (Owner 23/09) · đề xuất→duyệt→áp dụng · tìm trước khi tạo + alias · tạo xong quản lý ở đâu · lưu xong kích hoạt gì (trigger/thông báo/tầng dưới) · nhập/xuất hàng loạt (Excel/Word/in) · deep-link · Help trong UI · trạng thái UI 5 mức.
  - **Q2:** thêm chiều **trạng thái vòng đời** (bắt buộc: sửa/xoá phụ thuộc trạng thái); vai trò = bảng quyền riêng mỗi đối tượng, có cả ô CẤM; kênh/thiết bị = thuộc tính đầu UI (mặc định web máy tính), không nhân ma trận. Hàng sinh máy móc từ CRUD × trạng thái × chính/phụ/lỗi × vai trò (D21); cột = 15 chiều FIELD03 ∪ phần view.html có thêm.
  - **Q3:** chuẩn hoá 3 tầng, mỗi thông tin sống đúng 1 nơi: ① Danh mục khai báo (field: nghĩa, kiểu, đơn vị, validation, alias) ② Thẻ đối tượng (vòng đời, quyền, where-used, ngừng/xoá, audit) ③ Hợp đồng chuyển tiếp (from/to/trigger/key/output/lỗi/`return_to_step` — chỉ tham chiếu mã ①②; dạng "tạo khi thiếu" dùng lại R3.4). 18 thuộc tính giữ đủ nhưng chia về đúng tầng. JEV `normalized_layers` 0.99.
  - **Q4:** khoá = nghĩa, không phải tên: mỗi field một câu định nghĩa + đơn vị + đối tượng chủ; mã ≠ tên ≠ phiên bản; tìm trước trong `directus_fields`/`collection_field_standards` + danh mục + alias; hai mã trùng tên/alias = lỗi máy; nghi cùng nghĩa → JEV phân loại cùng/khác/liên quan → Host; field chưa có trong PG ghi `MỚI` vào bảng G, tạo thật sau qua DOT. JEV `existing_registries_plus_new_flagged` 0.99.
  - **Q5:** SSOT = bảng chữ cột cố định trong Git (để sau nạp PG qua DOT không phải diễn giải lại) + Mermaid cho vòng đời/luồng; HTML chỉ là lớp xem và nguyên mẫu, thử bằng `ui_inspect`/`ui_act` sẵn có. Figma/Penpot/Excalidraw/BPMN không làm SSOT; BPMN chỉ khi có nhánh song song/duyệt nhiều cấp mà Mermaid không tả nổi. Vòng 1 không cài gì; Host kiểm một lần Owner View có vẽ được Mermaid không. JEV `text_in_git_plus_mermaid` 1.00.
  - **Q6:** có, tối thiểu, viết ngay sau khi khuôn qua backtest FIELD và trước đối tượng thứ hai: 3 luật — không ô trống · không mã treo · không trùng tên/alias. Lý do: AI tự báo không đủ tin; máy chấm như nhau với mọi AI. Script chỉ tạo khi Owner duyệt (DROOT16). JEV 0.51/0.37 → Claude chốt.
  - **Q7:** PASS khi đủ 4: máy kiểm 0 lỗi · AI khác lập lại danh sách kịch bản **mù** (không xem bản tác giả) rồi diff, dòng lệch nào cũng có xử lý · **backtest FIELD**: quy trình phải tự bắt lại 4 lỗ Owner nêu 23/09 + lỗi `edit=`/`truong=`, không bắt được là quy trình FAIL · đi thử kiểu người mới không kẹt. Có HTML thì thêm `ui_act` bấm thử kịch bản chính. JEV 0.85.
  - **Q8:** mỗi khâu K0–K7 có cửa ra máy kiểm được + thanh tiến độ một ô đang làm cho từng đối tượng; JEV dùng ở chỗ chọn hữu hạn (ô cần/N-A/ngoài phạm vi · nghi trùng field · nhãn nguồn · chấm coverage), không dùng để nghĩ kịch bản (MMIM D21: JEV chỉ chấm danh sách ta đưa).
  - **JEV01:** ba kết quả 1.00 trên nhãn do chính đề xuất đặt; ghi kèm state/options để kiểm lại được (A5).
  - **Điều kiện Claude ACCEPT:** Host trả lời C1–C5, Q1–Q8 (ACCEPTED/PARTIAL/REJECTED + lý do); view.html thể hiện kế thừa MMIM · K0 · 3 tầng · nhãn nguồn · 3 chạm Owner · 4 điều kiện nghiệm thu. Đổi bố cục view.html theo DROOT17.

## Cửa vào cho Reviewer
- Claude: `WS work/quy-trinh-ve-UI · Review · đọc AGENTS.md → work/quy-trinh-ve-UI/COLLAB.md → view.html · phản biện P01 và trả lời 8 câu ở mục 8; không tạo file mới, không cài tool.`
- Hermes: `WS work/quy-trinh-ve-UI · Review · đọc AGENTS.md → work/quy-trinh-ve-UI/COLLAB.md → view.html · phản biện P01 và trả lời 8 câu ở mục 8; ưu tiên missing branches/contract gaps/automation gaps; không tạo file mới, không cài tool.`
- GPT: sau phản hồi Claude/Hermes, tổng hợp ACCEPT/PARTIAL/REJECTED; điểm còn vênh chuyển OWNER theo A5.

## Owner cần quyết
- —
