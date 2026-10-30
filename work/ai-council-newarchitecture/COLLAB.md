# COLLAB — ai-council-newarchitecture
Tên việc: Hội đồng AI — kế hoạch động, thực thi song song
HTML chính: view.html

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner 30/10/2026 lập task; 14:57 chỉ đạo «không bàn nữa mà làm»: chốt 5 việc Owner quyết + quy trình Mục tiêu lớn → Mục tiêu nhỏ → Checkpoint (§1 mục 9), sửa thẳng bản thiết kế, GPT góp thêm rồi chạy thử. Host: GPT Chat (đề xuất, Owner chưa chỉ định riêng). Chưa đổi AGENTS.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-30 15:25 +07 · Claude Chat · N1 XONG (bản V2), N2 giao GPT
- 🎯 Mục tiêu: Owner chỉ quyết 5 việc; còn lại AI chạy theo Mục tiêu lớn (L) → Mục tiêu nhỏ (N) → Checkpoint (C) với form khai chung, agent khảo sát và đề xuất nhiều nhất, hội đồng tập trung giám sát.
- 🏁 Xong khi: form + 15 thao tác ở [view.html](view.html) chạy thử đạt trên ≥ 1 việc thật, đo 4 chỉ số ([mục 7](view.html#muc-7)); lỗ gặp khi thử đã vá vào form.
- 📍 Tiến độ: [✅ N1 bản V2] → [■ N2 GPT rà, sửa thẳng] → [□ N3 thử trên Sổ PG] → [□ Sửa AGENTS theo kết quả thử].
- ✅ Đã xong: N1 — [view.html](view.html) bản V2: 3 form L/N/C, 15 thao tác (ai · ghi đâu · làm thế nào), lượt agent 8 bước, khi nào hỏi Owner, 9 lỗ hở đã rà, 4 chỉ số đo. Gộp V1 GPT + C1 Claude (bản cũ: commit c309bb96). §4 bên dưới đã viết theo form.
- ■ Đang làm: — · 0 RUN active.
- ⬜ Còn lại: N2 GPT rà từ ghế agent, sửa thẳng; N3 thử trên Sổ PG; sửa AGENTS sau khi thử đạt.
- ➡ Kế tiếp: **gpt-chat làm N2** theo §4 (sửa thẳng view.html, ghi chú mỗi chỗ đổi). NEXT_TRIGGER=GPT_N2_REVIEW_V2_DIRECT_EDIT.
- 😊 Owner cần quyết: không.
- ⛔ Không làm/để sau: chưa sửa luật AGENTS, chưa tác động code, VPS hoặc production.

### 1. Mục tiêu
1. “Vẫn chốt các mục tiêu lớn”
2. “Đưa ra các mục tiêu nhỏ hơn để phù hợp cho agent làm 1 lần (tối đa ~3-4 tiếng)”
3. “Trong mục tiêu nhỏ: có các check point.”
4. “Agent thực hiện, các agent khác vẫn có thể bổ sung mục tiêu nhỏ, chec point trong quá trình làm => quá trình điều chỉnh kế hoạch diễn ra song song với quá trình code. Việc báo cáo ngắn theo checkpoint là giúp, toàn bộ hội đồng có thông tin cập nhật để kịp thời điều chỉnh kế hoạch, giám sát.”
5. “Các Agent được tham gia khảo sát từ đầu. Agent thực hiện cũng là người đề xuất cập nhật kế hoạch nhiều nhất (vì nó nắm được ngữ cảnh tốt nhất).”
6. “Việc đề xuất đưa vào PR, Host liên tục rà soát bổ sung kế hoạch tiếp theo, các giám sát có thể liên tục hoạt động.”
7. “Đẩy các Agent thực thi tham gia nhiều hơn vào quá trình khảo sát, đưa ra mục tiêu con, và đưa ra check point. GPT chat, DOT, Claude chat/work sẽ giảm khối lượng công việc xuống (tập trung vào vấn đề giám sát).” — Owner bổ sung 30/10/2026.
8. Owner 30/10/2026 14:43 (gửi Claude Chat, viết lại đúng ý): công việc tiến triển quá lâu — thời gian thực sự viết mã thấp, gần hết thời gian dành cho hội đồng đánh giá; thiếu vai agent như Claude Code đánh giá từ đầu (agent có công cụ đọc nhanh nhất, hiểu việc nhất). Bằng chứng: các sổ ghi «PG đang có gì» loanh quanh cả tuần không xong; cứ thế thì 10 năm mới xong cỗ máy chế tạo quy trình. Tỷ lệ prompt thất bại vẫn cao. Owner muốn **thay đổi cách tiếp cận**.
9. Owner 30/10/2026 14:57 (viết lại đúng ý): **Không bàn nữa, phải làm.** Owner chỉ quyết 5 việc: (1) mục tiêu lớn; (2) bổ sung, hiệu chỉnh mục tiêu lớn; (3) việc hội đồng không dám quyết; (4) việc luẩn quẩn 2–3 vòng không thoát — hoàn thiện dần quy tắc khi nào phải hỏi Owner; (5) giám sát qua GPT live/DOT/Duet…, thấy không ổn thì chỉ đạo bổ sung qua các bề mặt đó. Nguyên tắc: có mục tiêu lớn + hiểu sơ bộ đầu vào thì mọi AI đều đưa ra được mục tiêu nhỏ, rồi checkpoint. Cần: (a) **form khai** cho mục tiêu lớn, mục tiêu nhỏ, checkpoint — hướng dẫn ngắn, mọi AI hiểu và làm giống nhau; (b) chỉ rõ từng thao tác **làm thế nào, ghi vào đâu**: thêm mục tiêu lớn, thêm mục tiêu nhỏ, đổi thứ tự mục tiêu nhỏ, thêm checkpoint, đổi thứ tự checkpoint; (c) **đứng ở vị trí agent phải làm** để kiểm hướng dẫn có làm được không; (d) rà kỹ quy trình cho ít hở rồi chạy thử, hoàn thiện dần, làm nhanh; (e) sửa thẳng vào tài liệu, GPT góp thêm, rồi đưa vào thử nghiệm.

### 2. Thế nào là hoàn thành
“Định nghĩa từng việc khái niệm. Cần làm gì với từng khái niệm, quy trình tạo 1 task mới thế nào? Quy trình cập nhật kế hoạch thế nào? Ai làm gì? Cùng nhau làm việc này cho rõ ràng để thay đổi cách làm với hy vọng là tiến độ nhanh hơn” — Owner 30/10/2026.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
**Bản thiết kế:** [view.html](view.html) — V2, sửa thẳng tại đó; COLLAB chỉ giữ mục tiêu, trạng thái, kế hoạch (§4) và con trỏ.
- [1. Ba form khai L/N/C](view.html#muc-1) · [2. 15 thao tác](view.html#muc-2) · [3. Một lượt của agent](view.html#muc-3)
- [4. Khi nào hỏi Owner](view.html#muc-4) · [5. Giám sát](view.html#muc-5) · [6. Lỗ hở đã rà](view.html#muc-6) · [7. Chạy thử và đo](view.html#muc-7)

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| gpt-chat (đề xuất) | OpenAI / GPT | ChatGPT Chat | Host (chưa duyệt) | Owner giao trực tiếp |
| claude-chat (đề xuất) | Anthropic / Claude | Claude Chat | Reviewer (đề xuất) | Owner chuyển tay / CHƯA ĐO |
| codex (đề xuất) | OpenAI / Codex | Codex Desktop/CLI | Worker + khảo sát (đề xuất) | Owner chuyển tay / CHƯA ĐO |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: —

Giữ GitHub làm SSOT; đối chiếu AGENTS.md và ai-council-karpathy để không xây trùng. Chưa tạo file, task con, prompt hay RUN khác. Chỉ chuyển bước sau khi Owner chốt phạm vi.

### 4. Kế hoạch — mục tiêu nhỏ (N) và checkpoint (C)
> 🤖 Biển: form và thao tác ở [view.html mục 1–3](view.html#muc-1). Thứ tự làm = từ trên xuống. Agent chọn N đầu tiên có DUYỆT đúng ghế mình; tích C ngay khi xong, mỗi C một commit. Không sửa N người khác đang làm — ghi vào «Ghi chú».

L1 = §1 + §2 ở trên (Owner).

#### N1 · Viết bản V2: form L/N/C + thao tác + lượt agent · XONG
- Thuộc: L1 · Người làm: claude-chat · Ước: 1h
- Xong khi: view.html có 3 form, bảng thao tác ghi rõ ai · ghi đâu · làm thế nào, lượt agent từng bước, quy tắc hỏi Owner, lỗ hở đã rà.
- Được làm: 👁 · ✍ work/ai-council-newarchitecture/
- Đề xuất: Owner 30/10 14:57 · Duyệt: Owner trực tiếp
- C1 🟢 3 form L/N/C có ví dụ thật (Sổ PG) · bằng chứng: view.html mục 1, commit e5e755d1 · 30/10 15:20 · claude-chat
- C2 🟢 15 thao tác ai · ghi đâu · làm thế nào · bằng chứng: view.html Bảng 2 · 30/10 15:20 · claude-chat
- C3 🟢 Lượt agent 8 bước từ ghế người làm · bằng chứng: view.html mục 3 · 30/10 15:20 · claude-chat
- C4 🟢 9 lỗ hở → xử lý · bằng chứng: view.html Bảng 6 · 30/10 15:20 · claude-chat
- Nghiệm thu: (GPT làm ở N2)

#### N2 · GPT rà V2 từ ghế agent, sửa thẳng, chốt bản thử · DUYỆT
- Thuộc: L1 · Cần trước: N1 · Người làm: gpt-chat · Ước: 1h
- Xong khi: view.html là bản Host chốt để thử; mỗi chỗ GPT sửa có 1 dòng «Ghi chú» dưới đây; không còn điểm bất đồng mở với Claude.
- Được làm: 👁 · ✍ work/ai-council-newarchitecture/
- Đề xuất: claude-chat 30/10 · Duyệt: Owner 30/10 14:57 («GPT đóng góp thêm rồi đưa vào thử nghiệm»)
- C1 ⬜ Rà 15 thao tác + 8 bước lượt agent: mỗi bước agent làm được mà không phải hỏi · Đạt khi: không còn bước mơ hồ
- C2 ⬜ Sửa thẳng view.html chỗ chưa ổn · Đạt khi: mỗi chỗ đổi có 1 dòng Ghi chú
- C3 ⬜ Nghiệm thu N1 (2.14) · Đạt khi: dòng «Nghiệm thu» của N1 đã điền
- Ghi chú:

#### N3 · Thử trên phần còn lại của Sổ PG · ĐỀ XUẤT
- Thuộc: L1 · Cần trước: N2 · Người làm: claude-code (agent) · gpt-chat (Host Sổ PG) · Ước: 3h
- Xong khi: §4 Kế hoạch của work/nhap-directus-for-workflow viết theo form; ≥ 1 lượt agent ≥ 2 giờ chạy bằng lệnh một dòng; đo 4 chỉ số ([view.html mục 7](view.html#muc-7)) so với số cũ.
- Được làm: 👁 · ✍ work/nhap-directus-for-workflow/ (§4) · ⚙ chỉ theo từng N đã DUYỆT bên Sổ PG
- Đề xuất: claude-chat 30/10 · Duyệt: —
- C1 ⬜ Host Sổ PG chuyển việc còn lại thành L1 + N theo form · Đạt khi: §4 bên Sổ PG có ≥ 2 N DUYỆT
- C2 ⬜ Lượt agent đầu tiên bằng lệnh một dòng · Đạt khi: ≥ 1 N XONG, C tích đủ bằng chứng
- C3 ⬜ Đo 4 chỉ số, ghi lỗ mới vào view.html Bảng 6 · Đạt khi: Bảng 7 có cột kết quả thử
- Ghi chú:

### Vòng trước
- C2 · 30/10 15:25 · Claude Chat · theo Owner 14:57 bỏ phần bàn, viết thẳng V2 (N1 XONG). Khái niệm «Giấy phép» của C1 đã nhập vào trường «Được làm» của N — không còn là khái niệm riêng.
- C1 · 30/10 15:10 · Claude Chat (khác hãng Host) · phản biện V1 tại [view.html#muc-v](view.html#muc-v). Kết luận: V1 đúng hướng nhưng còn giữ «Host duyệt từng mục tiêu nhỏ/READY từng lượt» là chỗ tắc đo được; đề xuất thêm **Giấy phép**, 5 khái niệm (Mục tiêu · Giấy phép · Lượt · Checkpoint · Cổng). Chưa có hiệu lực; Host chốt.
