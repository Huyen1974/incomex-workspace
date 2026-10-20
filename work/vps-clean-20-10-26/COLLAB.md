# COLLAB — vps-clean-20-10-26

Host: GPT Chat · Host_ID: gpt-chat/openai-main · Owner chỉ định trực tiếp ngày 20/10/2026
Nguồn chứng cứ: root COLLAB.md §PROOT11 và PROOT04; work/done-tasks/vps-clean-20-9-26/ (đã đóng, chỉ kế thừa kết quả).

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner trực tiếp GPT Chat ngày 20/10/2026, yêu cầu mở phiên work/vps-clean-20-10-26, cho phép lựa chọn tạo task mới và giao GPT tiếp tục làm Host.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-20 11:55 +07 · Claude Chat · P02
- 🎯 Mục tiêu: dọn lỗi/rác phát sinh, giảm chi phí tính toán, rà lại kiến trúc và số lượng cổng kiểm soát để VPS an toàn nhưng không lãng phí tài nguyên.
- 🏁 Xong khi: việc không cần thiết được xác định/tắt an toàn; các phần cần dùng, Điều 30/31, backup và cảnh báo vẫn hoạt động; chi phí và lỗi có số đo; kiểm tra hằng ngày tận dụng cơ chế hiện hữu.
- 📍 Tiến độ: ■ R1 đo nền PROOT11 (READY + GPT ACCEPT cùng SHA, Owner giao Codex) → ⬜ quyết TOP 10 → ⬜ R2 xử lý mục được duyệt → ⬜ cơ chế rà soát thường xuyên chi phí thấp.
- ✅ Đã xong: VPSC đợt 9/2026 CLOSED_SCOPE P115 ngày 15/10; PROOT11 R1 đã được GPT rà, chấp thuận khảo sát CHỈ ĐỌC; Claude Reviewer P02 đồng thuận P01 và xác nhận R1 đủ điều kiện giao Codex; chưa có KQ R1.
- ■ Đang làm: — · 0 RUN active trong task này; PROOT11 R1 ngoài task đang ở cổng OWNER_PASTE, không coi READY là STARTED.
- ⬜ Còn lại: số đo R1; phân loại GIỮ/GỘP/GIÃN/TẮT; Owner gật TOP 10; Claude Code sửa có bảo vệ; kiểm hậu quả/rollback; dùng kết quả đo để tối ưu nhịp rà hằng ngày.
- ➡ Kế tiếp: Owner chuyển nguyên prompt PROOT11-R1 cho Codex; GPT Host nhận KQ và yêu cầu Claude Chat phản biện một vòng; Owner duyệt từng mục có mutation. NEXT_TRIGGER=PROOT11_R1_KQ.
- ⛔ Không làm/để sau: không mở lại task cũ đã đóng; không thêm cron/Guard/monitor mặc định; không xoá hay dừng dịch vụ trước khi có phép và bằng chứng; không sửa các task khác thay chủ; không ép KPI AI tự đặt.

### 1. Mục tiêu
Owner 20/10/2026, nguyên văn: «Chúng ta mở một phiên mới để tiếp tục dọn rẹp VPS. Trong quá trình triển khai thì các cái rác nó tiếp tục sinh ra các lỗi và nhu cầu cần phải tối ưu cái tài nguyên tính toán của máy chủ để dành nhiệm vụ cho những cái việc cần thiết. Cho nên là ngoài việc dọn rác thường xuyên đánh giá xem có chương trình nào lỗi thì việc liên tục nhìn lại để tái cấu trúc máy chủ, xây dựng những cái số lượng các cái cổng kiểm soát một cách hợp lý chứ không xây dựng bừa bãi, rồi kiến trúc máy chủ làm sao vừa đảm bảo an toàn nhưng mà phải tối ưu cái tài nguyên tính toán. Cũng là một cái việc từ trước đến giờ chưa đặt ra bởi vì là quy mô còn nhỏ. Bây giờ chúng ta phải tiếp tục rà soát và kiểm tra thường xuyên những việc đó hàng ngày.»

Owner 20/10/2026: «Bạn tiếp tục làm host cho việc này. Hoặc tạo 1 task mới trên Repo.»

Owner 20/10/2026 10:27 +07 (nói với Claude Chat, đã sửa lỗi gõ; bản gốc tại root §PROOT11): «Hiện nay các cơ chế bảo vệ đã lên khoảng 75, nếu tiếp tục sẽ còn lên nhiều nữa. Tôi không phản đối việc tăng cơ chế bảo vệ, nhưng dù đã cố dọn server thường xuyên tôi vẫn thấy hơi chậm. Cảnh báo là tốt nhưng phải vừa đủ. Các hệ thống cảnh báo qua Telegram và giám sát server có tốn nhiều tài nguyên không? Những chương trình gì đang chạy ngầm định kỳ làm tiêu hao tài nguyên? Đâu là điểm cân bằng giữa quản lý chặt, giám sát chặt và tối ưu tài nguyên? Còn lỗi gì chưa dọn hết hoặc mới phát sinh làm tốn tài nguyên tính toán không? Phải tiếp tục dọn server song song với phát triển chương trình, vì cứ viết mã là sinh rác; nhiều cấu trúc cũ không hợp lý đã phải làm lại — chỗ nào chưa tắt hết mã sẽ gây nặng không cần thiết. Chương trình nào chạy liên tục thì xem config thế nào cho hợp lý.»

### 2. Thế nào là hoàn thành
VPS được kiểm kê, dọn lỗi/rác và tối ưu tài nguyên theo bằng chứng; các cơ chế kiểm soát, Guard Điều 30/31, cảnh báo và backup còn đủ tác dụng với chi phí phù hợp; không gây lỗi mới cho phần đang dùng. Có phương án rà hằng ngày dựa trên bộ canh hiện có, nêu rõ người chịu trách nhiệm và đầu ra. Mỗi lượt khảo sát/sửa phải đóng KQ sạch; không giữ RUN hay tăng thêm cơ chế chạy nền chỉ để theo dõi việc.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
1. R1 dùng nguyên lượt khảo sát chỉ đọc đã được Claude soạn tại root §PROOT11, READY và ACCEPT cùng SHA 9fd9f14d9efa2dc4c91d54c40dda49c45d025e29; RUN_ID PROOT11-R1-VPS-LOAD-AUDIT-20261020-01. Không chạy khảo sát khác và không đụng VPS trước khi có KQ. Báo cáo gốc R1 theo đúng vị trí root/BAO-CAO đã chỉ trong R1.7; task này trỏ về chứng cứ, không nhân đôi dữ liệu.
2. GPT Host nhận R1: tổng hợp 5 câu Owner, ma trận chi phí thực, nguồn chậm/lỗi, mức trùng lặp của Guard/Kuma/cron/healthcheck/flow/trigger, và TOP 10 theo tiết kiệm × an toàn × khả năng đảo. Số chưa đo ghi CHƯA ĐO, không tự đặt KPI cứng.
3. Claude Chat Reviewer phản biện một vòng; GPT chốt R2. Owner chọn từng hành động có tác động; Claude Code CLI chỉ thực thi sau READY/RUN thủ công, giữ VPS-GHI, dùng đường apply-v0 và bảo vệ Đ30/31, kiểm PRE/POST/rollback. Đối tượng xoá phải Drive-first + checksum/khả năng khôi phục + Owner đồng ý.
4. Tối ưu kiến trúc (chấm theo đúng Thước cân bằng TC1–TC7 đã ký ở root §PROOT11 — không soạn thước thứ hai; ngưỡng Owner chốt khi có số): phân chủ từng kiểm tra, nhận diện một chức năng bị canh nhiều lần, đánh giá nhịp theo thời gian hỏng/chịu lỗi và chi phí thật, đề xuất GIỮ/GIÃN/GỘP/TẮT. Không tạo lớp canh mới nếu cơ chế cũ làm được; không làm giảm coverage Đ30/31/backup/Telegram.
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

## P02 · Claude Chat Reviewer · 20/10/2026 11:55 +07 · B4 Owner · ĐỒNG THUẬN P01
- Based_on: P01 (`4132f2b3`), root §PROOT11 READY + ACCEPT `9fd9f14d9efa2dc4c91d54c40dda49c45d025e29`, chat Owner↔Claude 20/10 10:27. JEV `gen-dec-1792471565-BK9WJBMZhc46DIZa1Bfk`: R1 giao được 0,91 · task mới được Owner cho phép 0,77 · gom về một nhà sau R1 0,90.
- **Đồng thuận:** (1) R1 giao Codex ngay: READY + ACCEPT cùng SHA; 4 commit sau `9fd9f14` chỉ chạm dòng Graph, khối R1 nguyên vẹn. (2) Task mới hợp lệ vì Owner cho phép (§1); giữ VPSC 9/2026 đóng. (3) «Tối ưu kiến trúc vận hành» là lời Owner (§1: tái cấu trúc, số cổng kiểm soát hợp lý), không phải mục tiêu AI tự thêm.
- **4 điểm giám sát (Host áp khi nhận KQ R1):**
  - G1 · Một nhà: nhận KQ R1 xong, Host chuyển R2 nháp + tóm tắt KQ + TOP 10 về task này; root §PROOT11 rút còn một dòng con trỏ (làm SAU R1 để không phá READY). Bảng R1 ghi ở BAO-CAO VPSC cũ là ngoại lệ cuối cùng vì đã ký; từ R2, mọi số đo và quyết định chỉ ghi ở task này.
  - G2 · Một thước: §3.4 chấm bằng TC1–TC7 đã ký; cần đổi thước thì xin Owner một câu, không âm thầm sửa.
  - G3 · «Rà hằng ngày» (§2, §3.5) = máy báo trong bản tin 08:00/Kuma/Guard sẵn có, không phải AI ngồi chờ hay hẹn giờ quay lại; thêm job/cron/monitor nào cũng phải Owner gật và khai nhịp + chi phí (TC5).
  - G4 · TOP 10 không xếp theo số lượng mà theo tài nguyên tiết kiệm đo được × an toàn × đảo được (đồng ý P01); mục nào chưa đo được tiết kiệm thì không vào R2.
- **Claude đã vá thêm:** root `## Đang làm` thiếu dòng task này → đã thêm; §1 thiếu lời Owner 10:27 (5 câu hỏi, «cảnh báo vừa đủ») → đã thêm. Không đổi R1, không thêm điều kiện cho R1. `NEXT_TRIGGER=PROOT11_R1_KQ`
