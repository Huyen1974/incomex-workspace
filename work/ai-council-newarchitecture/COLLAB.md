# COLLAB — ai-council-newarchitecture
Tên việc: Hội đồng AI — kế hoạch động, thực thi song song

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: CHƯA XÁC NHẬN — Owner 30/10/2026 yêu cầu lập task để cùng thảo luận từng bước. Ghi lại yêu cầu dưới đây; chưa chốt A0 và chưa chỉ định Host riêng. Đề xuất GPT Chat làm Host, chờ Owner xác nhận. Chưa READY/RUN.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-30 10:06 +07 · GPT Chat · khởi tạo
- 🎯 Mục tiêu: “quá trình điều chỉnh kế hoạch diễn ra song song với quá trình code” — giảm thời gian chờ hội đồng và sai giả định đầu vào.
- 🏁 Xong khi: Owner duyệt khái niệm, cách tạo task/cập nhật kế hoạch qua PR, phân vai và phép đo thử.
- 📍 Tiến độ: [■ Ghi nhận] → [□ Khái niệm] → [□ Quy trình] → [□ Vai trò] → [□ Thử].
- ✅ Đã xong: lập hồ sơ yêu cầu ban đầu.
- ■ Đang làm: — · 0 RUN active.
- ⬜ Còn lại: xác nhận A0/Host; thảo luận từng phần A–E.
- ➡ Kế tiếp: 😊 Owner xác nhận mục tiêu và Host; Host mở thảo luận phần A; Reviewer/Agent khảo sát khi đã có phạm vi. NEXT_TRIGGER=OWNER_CONFIRM_A0_AND_HOST.
- ⛔ Không làm/để sau: chưa sửa luật AGENTS, chưa tạo PROMPT/RUN, chưa tác động code, VPS hoặc production.

### 1. Mục tiêu
1. “Vẫn chốt các mục tiêu lớn”
2. “Đưa ra các mục tiêu nhỏ hơn để phù hợp cho agent làm 1 lần (tối đa ~3-4 tiếng)”
3. “Trong mục tiêu nhỏ: có các check point.”
4. “Agent thực hiện, các agent khác vẫn có thể bổ sung mục tiêu nhỏ, chec point trong quá trình làm => quá trình điều chỉnh kế hoạch diễn ra song song với quá trình code. Việc báo cáo ngắn theo checkpoint là giúp, toàn bộ hội đồng có thông tin cập nhật để kịp thời điều chỉnh kế hoạch, giám sát.”
5. “Các Agent được tham gia khảo sát từ đầu. Agent thực hiện cũng là người đề xuất cập nhật kế hoạch nhiều nhất (vì nó nắm được ngữ cảnh tốt nhất).”
6. “Việc đề xuất đưa vào PR, Host liên tục rà soát bổ sung kế hoạch tiếp theo, các giám sát có thể liên tục hoạt động.”

### 2. Thế nào là hoàn thành
“Định nghĩa từng việc khái niệm. Cần làm gì với từng khái niệm, quy trình tạo 1 task mới thế nào? Quy trình cập nhật kế hoạch thế nào? Ai làm gì? Cùng nhau làm việc này cho rõ ràng để thay đổi cách làm với hy vọng là tiến độ nhanh hơn” — Owner 30/10/2026.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
**Các phần sẽ cùng thảo luận, chưa phải kế hoạch được duyệt:**
- **A. Khái niệm:** Task, mục tiêu nhỏ (mỗi lượt ≤3–4 giờ), checkpoint, PR; PASS và bằng chứng.
- **B. Tạo task:** khảo sát từ đầu; thông tin tối thiểu và điều kiện bắt đầu.
- **C. Kế hoạch động:** agent đề xuất qua PR trong khi code; Host cập nhật phần tiếp theo, không sửa ngang RUN đang chạy.
- **D. Vai trò:** Owner, Host, reviewer, worker; quyền tự bổ sung/sửa checkpoint và cổng dừng.
- **E. Thử và đo:** so thời gian chờ, RUN lỗi đầu vào, thời gian đạt mục tiêu với quy trình cũ.

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| gpt-chat (đề xuất) | OpenAI / GPT | ChatGPT Chat | Host (chưa duyệt) | Owner giao trực tiếp |
| claude-chat (đề xuất) | Anthropic / Claude | Claude Chat | Reviewer (đề xuất) | Owner chuyển tay / CHƯA ĐO |
| codex (đề xuất) | OpenAI / Codex | Codex Desktop/CLI | Worker + khảo sát (đề xuất) | Owner chuyển tay / CHƯA ĐO |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: —

Giữ GitHub làm SSOT; đối chiếu AGENTS.md và ai-council-karpathy để không xây trùng. Chưa tạo file, task con, prompt hay RUN khác. Chỉ chuyển bước sau khi Owner chốt phạm vi.

### Vòng trước
- Chưa có.
