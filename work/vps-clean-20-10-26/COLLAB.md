# COLLAB — vps-clean-20-10-26

Host: GPT Chat · Host_ID: gpt-chat/openai-main · Owner chỉ định trực tiếp ngày 20/10/2026
Nguồn chứng cứ: root COLLAB.md §PROOT11 và PROOT04; work/done-tasks/vps-clean-20-9-26/ (đã đóng, chỉ kế thừa kết quả).

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner trực tiếp GPT Chat ngày 20/10/2026, yêu cầu mở phiên work/vps-clean-20-10-26, cho phép lựa chọn tạo task mới và giao GPT tiếp tục làm Host.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-20 10:51 +07 · GPT Chat · P01
- 🎯 Mục tiêu: dọn lỗi/rác phát sinh, giảm chi phí tính toán, rà lại kiến trúc và số lượng cổng kiểm soát để VPS an toàn nhưng không lãng phí tài nguyên.
- 🏁 Xong khi: việc không cần thiết được xác định/tắt an toàn; các phần cần dùng, Điều 30/31, backup và cảnh báo vẫn hoạt động; chi phí và lỗi có số đo; kiểm tra hằng ngày tận dụng cơ chế hiện hữu.
- 📍 Tiến độ: ■ R1 đo nền PROOT11 (READY + GPT ACCEPT cùng SHA, Owner giao Codex) → ⬜ quyết TOP 10 → ⬜ R2 xử lý mục được duyệt → ⬜ cơ chế rà soát thường xuyên chi phí thấp.
- ✅ Đã xong: VPSC đợt 9/2026 CLOSED_SCOPE P115 ngày 15/10; PROOT11 R1 đã được GPT rà, chấp thuận khảo sát CHỈ ĐỌC; chưa có KQ R1.
- ■ Đang làm: — · 0 RUN active trong task này; PROOT11 R1 ngoài task đang ở cổng OWNER_PASTE, không coi READY là STARTED.
- ⬜ Còn lại: số đo R1; phân loại GIỮ/GỘP/GIÃN/TẮT; Owner gật TOP 10; Claude Code sửa có bảo vệ; kiểm hậu quả/rollback; dùng kết quả đo để tối ưu nhịp rà hằng ngày.
- ➡ Kế tiếp: Owner chuyển nguyên prompt PROOT11-R1 cho Codex; GPT Host nhận KQ và yêu cầu Claude Chat phản biện một vòng; Owner duyệt từng mục có mutation. NEXT_TRIGGER=PROOT11_R1_KQ.
- ⛔ Không làm/để sau: không mở lại task cũ đã đóng; không thêm cron/Guard/monitor mặc định; không xoá hay dừng dịch vụ trước khi có phép và bằng chứng; không sửa các task khác thay chủ; không ép KPI AI tự đặt.

### 1. Mục tiêu
Owner 20/10/2026, nguyên văn: «Chúng ta mở một phiên mới để tiếp tục dọn rẹp VPS. Trong quá trình triển khai thì các cái rác nó tiếp tục sinh ra các lỗi và nhu cầu cần phải tối ưu cái tài nguyên tính toán của máy chủ để dành nhiệm vụ cho những cái việc cần thiết. Cho nên là ngoài việc dọn rác thường xuyên đánh giá xem có chương trình nào lỗi thì việc liên tục nhìn lại để tái cấu trúc máy chủ, xây dựng những cái số lượng các cái cổng kiểm soát một cách hợp lý chứ không xây dựng bừa bãi, rồi kiến trúc máy chủ làm sao vừa đảm bảo an toàn nhưng mà phải tối ưu cái tài nguyên tính toán. Cũng là một cái việc từ trước đến giờ chưa đặt ra bởi vì là quy mô còn nhỏ. Bây giờ chúng ta phải tiếp tục rà soát và kiểm tra thường xuyên những việc đó hàng ngày.»

Owner 20/10/2026: «Bạn tiếp tục làm host cho việc này. Hoặc tạo 1 task mới trên Repo.»

### 2. Thế nào là hoàn thành
VPS được kiểm kê, dọn lỗi/rác và tối ưu tài nguyên theo bằng chứng; các cơ chế kiểm soát, Guard Điều 30/31, cảnh báo và backup còn đủ tác dụng với chi phí phù hợp; không gây lỗi mới cho phần đang dùng. Có phương án rà hằng ngày dựa trên bộ canh hiện có, nêu rõ người chịu trách nhiệm và đầu ra. Mỗi lượt khảo sát/sửa phải đóng KQ sạch; không giữ RUN hay tăng thêm cơ chế chạy nền chỉ để theo dõi việc.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
1. R1 dùng nguyên lượt khảo sát chỉ đọc đã được Claude soạn tại root §PROOT11, READY và ACCEPT cùng SHA 9fd9f14d9efa2dc4c91d54c40dda49c45d025e29; RUN_ID PROOT11-R1-VPS-LOAD-AUDIT-20261020-01. Không chạy khảo sát khác và không đụng VPS trước khi có KQ. Báo cáo gốc R1 theo đúng vị trí root/BAO-CAO đã chỉ trong R1.7; task này trỏ về chứng cứ, không nhân đôi dữ liệu.
2. GPT Host nhận R1: tổng hợp 5 câu Owner, ma trận chi phí thực, nguồn chậm/lỗi, mức trùng lặp của Guard/Kuma/cron/healthcheck/flow/trigger, và TOP 10 theo tiết kiệm × an toàn × khả năng đảo. Số chưa đo ghi CHƯA ĐO, không tự đặt KPI cứng.
3. Claude Chat Reviewer phản biện một vòng; GPT chốt R2. Owner chọn từng hành động có tác động; Claude Code CLI chỉ thực thi sau READY/RUN thủ công, giữ VPS-GHI, dùng đường apply-v0 và bảo vệ Đ30/31, kiểm PRE/POST/rollback. Đối tượng xoá phải Drive-first + checksum/khả năng khôi phục + Owner đồng ý.
4. Tối ưu kiến trúc: phân chủ từng kiểm tra, nhận diện một chức năng bị canh nhiều lần, đánh giá nhịp theo thời gian hỏng/chịu lỗi và chi phí thật, đề xuất GIỮ/GIÃN/GỘP/TẮT. Không tạo lớp canh mới nếu cơ chế cũ làm được; không làm giảm coverage Đ30/31/backup/Telegram.
5. Rà hằng ngày trước hết dùng Kuma/Guard/Config Guard, storage-watch và bản tin 08:00 đã tồn tại; đo được gì, thiếu gì thì ghi vào sổ hiện hành. Đề xuất nâng cấp bản tin sau khi kiểm chi phí, Owner duyệt trước khi bổ sung job/cron/monitor. Không giữ AI/terminal chờ giữa các ngày.
6. Ranh giới: VPSC 9/2026 đóng ở P115, là kho bằng chứng cũ. Task mới xử lý vệ sinh, tối ưu tài nguyên và lỗi nhỏ của việc đã đóng; lỗi lớn hoặc liên quan nghiệp vụ task đang hoạt động chuyển về Host đúng việc. Các thay đổi có phá huỷ/mất dữ liệu hoặc ảnh hưởng thiết kế quyền Owner quyết.

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| gpt-chat | OpenAI / GPT | GPT Chat (phiên này) | Host | Owner trao đổi trực tiếp qua chat |
| claude-chat | Anthropic / Claude | Claude Chat | Reviewer | Owner chuyển tay giữa hai phiên |
| codex | OpenAI / Codex | Codex | Worker (R1) | Owner dán prompt R1 |
| claude-code-cli | Anthropic / Claude | Claude Code CLI | Worker (R2) | Owner dán PROMPT được READY |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: Owner duyệt từng mutation có nguy cơ; R1 chỉ đọc, R2 chưa READY.

### Vòng trước
Không có vòng của task này. work/done-tasks/vps-clean-20-9-26/COLLAB.md P115 là đợt cũ CLOSED_SCOPE, chỉ dẫn chứng. Root §PROOT11 là lượt R1 đã chuẩn bị trước khi mở task.

## P01 · GPT Chat Host · 20/10/2026 · mở task nối tiếp không phá READY
- Based_on: AGENTS.md (A0/MT3/MT4/DROOT54–55), root §PROOT11 R1.0–R1.8, PROOT04, VPSC P115.
- Quyết định: tách nhiệm vụ dài hạn ra task mới vì task 9/2026 đã đóng; giữ nguyên R1 root để Codex chạy ngay khi Owner giao, không phát thêm RUN hay cập nhật VPS.
- R1 đã được GPT Chat Reviewer độc lập ký ACCEPT trên root đúng SHA. Sau khi R1 trả KQ, GPT Chat là Host chính task mới, Claude Chat Reviewer khác hãng; các bước sau phải đối chiếu mục tiêu này và dữ liệu mới.
