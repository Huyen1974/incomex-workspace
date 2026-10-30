# COLLAB — ai-council-newarchitecture
Tên việc: Hội đồng AI — kế hoạch động, thực thi song song

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: CHƯA XÁC NHẬN — Owner 30/10/2026 yêu cầu lập task để cùng thảo luận từng bước. Ghi lại yêu cầu dưới đây; chưa chốt A0 và chưa chỉ định Host riêng. Đề xuất GPT Chat làm Host, chờ Owner xác nhận. Chưa READY/RUN.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-30 10:40 +07 · GPT Chat · bổ sung mục tiêu 7
- 🎯 Mục tiêu: kế hoạch điều chỉnh song song với code; agent thực thi chủ động khảo sát, đề xuất mục tiêu con/checkpoint; GPT Chat, DOT, Claude Chat/Work tập trung giám sát, giảm thời gian chờ và sai giả định.
- 🏁 Xong khi: Owner chốt đủ 4 phần I–IV và cách kiểm chứng quy trình mới nhanh hơn, ít lỗi hơn.
- 📍 Tiến độ: [✅ Ghi nhận] → [■ Khung I–IV] → [□ Thảo luận từng mục] → [□ Chốt và thử].
- ✅ Đã xong: lập hồ sơ; tạo 4 mục xổ/thu gọn trên GitHub.
- ■ Đang làm: — · 0 RUN active.
- ⬜ Còn lại: xác nhận A0/Host; cùng xây dựng và chốt nội dung I–IV.
- ➡ Kế tiếp: 😊 Owner cùng bàn mục I, xác nhận A0/Host để chốt và điều hành; chưa mở RUN. NEXT_TRIGGER=OWNER_CONFIRM_A0_AND_HOST.
- ⛔ Không làm/để sau: chưa sửa luật AGENTS, chưa tạo PROMPT/RUN, chưa tác động code, VPS hoặc production.

### 1. Mục tiêu
1. “Vẫn chốt các mục tiêu lớn”
2. “Đưa ra các mục tiêu nhỏ hơn để phù hợp cho agent làm 1 lần (tối đa ~3-4 tiếng)”
3. “Trong mục tiêu nhỏ: có các check point.”
4. “Agent thực hiện, các agent khác vẫn có thể bổ sung mục tiêu nhỏ, chec point trong quá trình làm => quá trình điều chỉnh kế hoạch diễn ra song song với quá trình code. Việc báo cáo ngắn theo checkpoint là giúp, toàn bộ hội đồng có thông tin cập nhật để kịp thời điều chỉnh kế hoạch, giám sát.”
5. “Các Agent được tham gia khảo sát từ đầu. Agent thực hiện cũng là người đề xuất cập nhật kế hoạch nhiều nhất (vì nó nắm được ngữ cảnh tốt nhất).”
6. “Việc đề xuất đưa vào PR, Host liên tục rà soát bổ sung kế hoạch tiếp theo, các giám sát có thể liên tục hoạt động.”
7. “Đẩy các Agent thực thi tham gia nhiều hơn vào quá trình khảo sát, đưa ra mục tiêu con, và đưa ra check point. GPT chat, DOT, Claude chat/work sẽ giảm khối lượng công việc xuống (tập trung vào vấn đề giám sát).” — Owner bổ sung 30/10/2026.

### 2. Thế nào là hoàn thành
“Định nghĩa từng việc khái niệm. Cần làm gì với từng khái niệm, quy trình tạo 1 task mới thế nào? Quy trình cập nhật kế hoạch thế nào? Ai làm gì? Cùng nhau làm việc này cho rõ ràng để thay đổi cách làm với hy vọng là tiến độ nhanh hơn” — Owner 30/10/2026.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
**Nội dung thảo luận — chưa chốt.** Bấm tên từng mục để mở/thu gọn. Chưa thêm nội dung chi tiết trước khi cùng Owner bàn.

<details>
<summary><strong>I. Định nghĩa khái niệm</strong></summary>

*Nội dung sẽ bổ sung sau khi thảo luận.*

</details>

<details>
<summary><strong>II. Định nghĩa vai trò</strong></summary>

*Nội dung sẽ bổ sung sau khi thảo luận.*

</details>

<details>
<summary><strong>III. Cấu trúc trong Hội đồng AI</strong></summary>

*Nội dung sẽ bổ sung sau khi thảo luận.*

</details>

<details>
<summary><strong>IV. Quy trình thực hiện</strong></summary>

*Nội dung sẽ bổ sung sau khi thảo luận.*

</details>

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
