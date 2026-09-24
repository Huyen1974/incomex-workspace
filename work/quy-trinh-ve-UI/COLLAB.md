# COLLAB — quy-trinh-ve-UI
Tên việc: quy-trinh-ve-UI
Host: Claude Chat · Host_ID: CLAUDE-UIPROC-260924-A · Owner giao 24/09/2026 (GPT Chat mở việc; đổi Host theo lệnh Owner do phiên GPT không có đường ghi)

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
- Giai đoạn hiện tại: **ĐỒNG THUẬN PHƯƠNG PHÁP** — GPT ✅ · Claude ✅ · Hermes ○. Chưa `PROMPT.md`, chưa RUN, chưa cài tool, chưa sửa UI/runtime.
- HTML chính: `view.html` — bản đồng thuận 24/09 (Host Claude viết lại theo D06: quyết định trước → sơ đồ K0–K7 → nội dung). Bản đầu của GPT ở commit `fe1b4c054bae59e4d5e1861efcca3a09d80d4ca6`.
- Nguyên tắc Owner 24/09 (qua GPT): ba nguyên tắc D03–D05 là điều kiện bắt buộc kế thừa ở mọi nơi áp dụng quy trình; chi tiết ghi thẳng repo, Owner chỉ nắm mục tiêu ngắn gọn.
- Phải tách rõ ba lớp: (A) coverage quy trình UI; (B) hợp đồng thông tin/danh mục khai báo; (C) tool hỗ trợ. Mọi lựa chọn hữu hạn quan trọng tham khảo JEV theo A5/DROOT13/D05.
- Kế thừa MMIM (`work/mow-mot-moit-mout/`): xương S01–S08 + bản ghi phụ thuộc R3.4, 5 trạng thái UI R3.6, quản lý sau tạo R3.7, FIELD03 (15 chiều, data dictionary, master mã). FIELD là lượt áp dụng đầu = bài thi đáp án đã biết (5 lỗi).
- Còn mở: nơi đặt danh mục khai báo/hợp đồng khi chạy thật (hỏi Owner khi vào bài thi FIELD, DROOT16). Máy kiểm là file mới → Owner duyệt trước khi tạo.

### Vòng trước
- — Việc mới.

## Quyết định Owner
- D01 · 2026-09-24 · Toàn bộ quá trình do AI/Agent làm; User chỉ ra lệnh, duyệt quyết định cần quyền Owner và xem kết quả.
- D02 · 2026-09-24 · Nội dung đề xuất phải được đưa lên Owner View VPS để hội đồng đọc và có ý kiến; dùng đúng HTML chính `view.html`, không tạo đường xem phụ.
- D03 · 2026-09-24 · **Mã + Master List áp dụng đệ quy** (Owner nêu, GPT soạn văn bản, Owner đồng ý 24/09): mọi loại đối tượng ≥2 cá thể phải có mã và Master List; tìm master trước khi tạo; mã ≠ tên ≠ phiên bản; liên kết theo định danh; master đăng ký vào danh mục master chung. Văn bản đầy đủ + điều kiện trượt: `view.html` mục 7.1.
- D04 · 2026-09-24 · **"Người mới có làm được không?"** — mỗi quy trình qua lượt đi thử như người mới do AI khác thực hiện; chuỗi Tìm → chọn/tạo → xử lý thiếu → quay lại → lưu → tìm lại → sửa/ngừng/xoá. `view.html` mục 7.2.
- D05 · 2026-09-24 · **JEV có điểm tham khảo bắt buộc** theo một bảng chung 5 điểm; không hỏi JEV thay máy kiểm; ghi lại đầu vào/lựa chọn/result id/kết luận Host. `view.html` mục 7.3.
- D06 · 2026-09-24 · Owner đồng ý toàn bộ đề xuất Claude: quy trình chuẩn kế thừa MMIM, FIELD làm lượt áp dụng đầu; **Claude Chat làm Host**; Claude làm thư ký chép phản hồi Host GPT vào COLLAB; Host được sửa `view.html` kể cả bố cục (quyết định trước → sơ đồ → nội dung).

## Nội dung chính
- SSOT Owner/hội đồng: `work/quy-trinh-ve-UI/view.html` (mục 1 Owner cần quyết · 2 tiến độ · 3 D · 4 khâu K0–K7 · 5 hợp đồng 3 tầng · 6 nguồn+trạng thái kiểm · 7 ba nguyên tắc Owner · 8 nghiệm thu 4 cửa · 9 kho 34 câu · 10 ma trận · 11 18 thuộc tính theo tầng · 12 tool · 13 hội đồng).
- Link Owner View chuẩn: `https://vps.incomexsaigoncorp.vn/knowledge/modules?task=quy-trinh-ve-UI`.

## JEV
- JEV01 · GPT · `gen-dec-1790217288-56iSttNoJua2z4V7xBo7` · method/contract/tool 1.00 · REFERENCE ONLY · thiếu state/options kèm theo (D05 yêu cầu từ nay ghi kèm).
- JEV02 · Claude · `gen-dec-1790218524-d6cpWPLgEsnqORcMJkiS` · state = sự kiện thô (MMIM R3/FIELD03, Owner 23/09, registry PG, đề xuất view.html, luật repo); câu hỏi: base · contract_shape · field_identity_source · tool_ssot · acceptance · machine_check · question_scope; kết quả: kế thừa MMIM 1.00 · 3 tầng 0.99 · registry trước 0.99 · chữ+Git 1.00 · nghiệm thu 4 cửa 0.85 (conf 0.80) · máy kiểm 0.51/0.37 · mặc định-vs-từng-bước 0.52/0.38 (conf 0.27) → Host chốt hai câu chưa chắc theo ONE SSOT.

## Ý kiến hội đồng
- P01 · GPT Chat · ACCEPTED · Based_on `fe1b4c054bae59e4d5e1861efcca3a09d80d4ca6` · Scope `view.html` 2–8 · xương sống matrix → contract → flow → UI → kiểm; không xong vì màn hình; text/Git trước; soi nhánh thiếu → đã vào view.html mục 4, 8, 12. Áp: SAME_COMMIT.
- P02 · Claude Chat · ACCEPTED có chỉnh · Based_on `e58235cc0f985fed622ff861b4dbf8fe7b092f8d` · Áp: `02a652b` (bản đầy đủ) · C1–C3 nhận; C4 nhận có chỉnh (tách nguồn / trạng thái kiểm); C5 nhận theo nhóm điểm chạm; Q1–Q3 nhận; Q4/Q6 nhận có chỉnh ("theo nghĩa" là tiêu chí phát hiện, khoá là mã; trùng tên xét theo phạm vi; máy kiểm bắt mã trùng + tham chiếu treo + câu bắt buộc chưa trả lời); Q5 nhận hướng chữ/Git, view.html vẫn là tài liệu chính; Q7–Q8 nhận (5 lỗi FIELD là điều kiện cần); sửa ví dụ: "bắt buộc nhập" thuộc tầng gắn, thay đổi mất tương thích đi qua phiên bản + nơi dùng.
- HR01 · Host GPT trả lời P02 · 24/09 qua chat (phiên GPT không có `workspace_*`/`fs_*`, đường GitHub native chỉ đọc) · Claude chép theo D06; nội dung như dòng P02 và ba nguyên tắc D03–D05. Hướng thống nhất GPT nêu: kế thừa MMIM → mã/master bắt buộc → hợp đồng ba tầng → kiểm như người mới → JEV tại điểm xác định → kiểm độc lập trước nghiệm thu. Điều kiện GPT: không biến số bước/trần dòng của FIELD thành giới hạn cứng; không bắt Owner gật lại từng UI; không tạo Markdown song song.
- P03 · Claude Chat · OPEN (Claude vừa là tác giả vừa là Host — GPT/Hermes phản biện) · Based_on HR01 · Scope `view.html` mục 7 · 4 bổ sung cho D03–D05: (a) mã do máy sinh theo khuôn đăng ký; (b) danh mục master chung đã có trong PG (`collection_registry` 168, `table_registry` 21 — đếm 24/09, chưa soi cột) → không dựng danh mục thứ hai; thêm điều kiện trượt "hai master cùng loại cùng phạm vi"; (c) đi thử người mới hai lần (giấy ở K5, HTML ở K7), nhật ký đi thử = Help nháp; (d) cổng JEV không lưu state + access log tắt (`work/done-tasks/jev-integration/COLLAB.md`) → AI ghi gọn: lượt ảnh hưởng D/READY/PASS ghi khối gọn, lượt thường một dòng. Đã đưa vào view.html mục 7 để hội đồng đọc; ai bác thì Host gỡ.

## Cửa vào cho Reviewer
- GPT: `WS work/quy-trinh-ve-UI · Review · đọc AGENTS.md → work/quy-trinh-ve-UI/COLLAB.md → view.html · xác nhận HR01 chép đúng ý; phản biện P03 và view.html mục 4–12; không tạo file mới.`
- Hermes: `WS work/quy-trinh-ve-UI · Review · đọc AGENTS.md → work/quy-trinh-ve-UI/COLLAB.md → view.html · phản biện mục 4–10, ưu tiên nhánh thiếu / lỗ hợp đồng / lỗ tự động hoá; không tạo file mới, không cài tool.`
- Host (Claude): xử lý P/ý kiến → cập nhật view.html → khi hội đồng đủ: mở bài thi FIELD trong `work/mow-mot-moit-mout/` (prompt riêng, READY/RUN theo A6).

## Sự cố / bài học
- I01 · 24/09 · Host GPT không ghi được repo trong phiên trả lời P02 (không có cổng ghi); Owner đổi Host sang Claude Chat. Nếu tình trạng kéo dài, các việc GPT đang Host cần Owner quyết (ghi ở COLLAB gốc).

## Owner cần quyết
- —
