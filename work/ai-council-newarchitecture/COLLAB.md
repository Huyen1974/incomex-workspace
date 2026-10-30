# COLLAB — ai-council-newarchitecture
Tên việc: Hội đồng AI — kế hoạch động, thực thi song song
HTML chính: view.html

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner 30/10/2026 lập task; 14:57 chỉ đạo «không bàn nữa mà làm»: chốt 5 việc Owner quyết + quy trình Mục tiêu lớn → Mục tiêu nhỏ → Checkpoint (§1 mục 9), sửa thẳng bản thiết kế, GPT góp thêm rồi chạy thử. Host: GPT Chat (đề xuất, Owner chưa chỉ định riêng). Chưa đổi AGENTS.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-30 17:10 +07 · Claude Chat · N4 ĐANG LÀM: Ma trận mục tiêu dạng cây kiểu Apple chờ Owner hướng dẫn
- 🎯 Mục tiêu: Owner chỉ quyết 5 việc; còn lại AI chạy theo Mục tiêu lớn (L) → Đầu vào chung (Đ) → Mục tiêu nhỏ (N) → Checkpoint (C) với từ điển + form khai chung, agent khảo sát và đề xuất nhiều nhất, hội đồng tập trung giám sát.
- 🏁 Xong khi: từ điển + form + thao tác ở [view.html](view.html) chạy thử đạt trên ≥ 1 việc thật, đo chỉ số ([mục 8](view.html#muc-8)); lỗ gặp khi thử đã vá vào form.
- 📍 Tiến độ: [✅ N1 bản V2.1] → [■ N4 Bảng mục tiêu] → [□ N2 GPT rà, sửa thẳng] → [□ N3 thử trên Sổ PG] → [□ Sửa AGENTS theo kết quả thử].
- ✅ Đã xong: N1 — [view.html](view.html) V2.1: **giữ đủ định nghĩa, vai, cấu trúc, quy trình V1 của GPT** (nhãn V1) + bổ sung: từ điển có cột «không phải», form L/Đ/N/C/Báo cáo, 17 thao tác (ai · ghi đâu · làm thế nào), lượt agent 8 bước, khi nào hỏi Owner, 10 lỗ hở, bảng V2 khác V1. §4 bên dưới đã viết theo form. N4.C2: [Bảng mục tiêu](view.html#ban-do-muc-tieu) thay hình minh hoạ — «Hỏi gì → nhìn đâu» + 4 bảng (Mục tiêu lớn · Đầu vào · Mục tiêu nhỏ × Checkpoint · Báo cáo), dưới mỗi bảng ghi ai thêm, thêm thế nào; thêm thao tác 3.18 chuyển checkpoint chưa xong sang N sau.
- ■ Đang làm: N4 · claude-chat · chỉnh Bảng mục tiêu cùng Owner.
- ⬜ Còn lại: N4 chốt bảng + quy tắc vẽ; N2 GPT rà (gồm cả bảng); N3 thử trên Sổ PG; N5 trang Task tự vẽ (đề xuất); sửa AGENTS sau khi thử đạt.
- ➡ Kế tiếp: Owner xem mẫu [Ma trận mục tiêu](view.html#ma-tran-muc-tieu) (5 cột, bấm xổ 3 tầng) và hướng dẫn chỉnh; claude-chat sửa thẳng. Bảng mục tiêu cũ giữ bên dưới. Sau đó gpt-chat làm N2. NEXT_TRIGGER=OWNER_ADJUST_GOAL_MAP_SAMPLE.
- 😊 Owner cần quyết: không — chỉ góp ý chỉnh mẫu.
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
10. Owner 30/10/2026 15:02: phải giữ các định nghĩa để bất cứ AI nào vào cũng hiểu nó là cái gì và hiểu thống nhất — không định nghĩa từ ngữ thì mỗi AI hiểu một kiểu.
11. Owner 30/10/2026 15:07: định nghĩa viết trước đó (V1) có lý của nó — khái niệm lạ như mục tiêu lớn, mục tiêu nhỏ, checkpoint… không làm rõ thì AI không hiểu để làm. **Không xóa sạch; phải đọc cái cũ đang làm gì trước khi sửa; không hiểu mà sửa của người khác là rất tệ.**
12. Owner 30/10/2026 15:23 (viết lại đúng ý): sản phẩm cuối cùng là **một hình vẽ trực quan, ít chữ** cho một mục tiêu lớn (Mục tiêu lớn / danh sách đầu vào / mục tiêu con / checkpoint) — cả người và AI nhìn vào là hiểu tiến trình đang thế nào. Dữ liệu phải đổ vào và hiện cho Owner và mọi AI cùng đọc. Theo cách đã làm được ở phần Công thức (mow-mot-moit-mout): ngắn, ít chữ — rác AI tạo ra đều bắt đầu từ nhiều chữ. Vẽ một mẫu bảng ít chữ + hình họa, đặt ở đầu phần Cấu trúc và quy trình, rồi cùng điều chỉnh. (Phần định nghĩa là danh sách, giữ như cũ.)
13. Owner 30/10/2026 15:35 (viết lại đúng ý): hình vẽ trước «vẽ cho vui», không trả lời được câu hỏi làm việc thật. Bảng phải trả lời được, ví dụ: (1) đầu vào có liệt kê không, là những gì, nhìn thế nào; (2) mục tiêu lớn nhìn ở đâu; (3) hội đồng đang chia bao nhiêu mục tiêu nhỏ, mỗi cái bao nhiêu checkpoint, nhìn ở đâu; (4) AI muốn thêm mục tiêu nhỏ nhìn ở đâu, thêm thế nào; Owner muốn thêm mục tiêu lớn nhìn ở đâu, chỉ đạo ai thêm; (5) chuyển checkpoint còn thiếu sang mục tiêu nhỏ tiếp theo thế nào; (6) format mục tiêu lớn, mục tiêu nhỏ, checkpoint, báo cáo gồm gì. Phải hình dung câu chuyện thực tế sẽ diễn ra, làm để làm việc chứ không phải cho vui; đơn giản là tốt.
14. Owner 30/10/2026 15:48: bảng trước phức tạp quá — làm **một bảng ma trận**, chưa xóa bảng cũ. Bảng mục tiêu lớn có các cột: STT · Mục tiêu · Thế nào là hoàn thành · Tình trạng (chỉ 4 màu, rê vào màu thì hiện chữ) · Báo cáo (link bản báo cáo nếu có). Bấm mục tiêu lớn thì xổ ra mục tiêu nhỏ, cũng từng đó cột; bấm mục tiêu nhỏ thì xổ ra checkpoint. Thiết kế mẫu trước, Owner sẽ hướng dẫn; tư duy phải ngắn gọn.
15. Owner 30/10/2026 15:54: nhìn phải thấy ngay là cây (treeview) — cái nào mục tiêu lớn, mục tiêu nhỏ, checkpoint; chữ to/nhỏ theo tầng; tình trạng chỉ cần một chấm màu nhỏ theo chuẩn Apple; thiết kế có hàng lối.

### 2. Thế nào là hoàn thành
“Định nghĩa từng việc khái niệm. Cần làm gì với từng khái niệm, quy trình tạo 1 task mới thế nào? Quy trình cập nhật kế hoạch thế nào? Ai làm gì? Cùng nhau làm việc này cho rõ ràng để thay đổi cách làm với hy vọng là tiến độ nhanh hơn” — Owner 30/10/2026.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
**Bản thiết kế:** [view.html](view.html) — V2, sửa thẳng tại đó; COLLAB chỉ giữ mục tiêu, trạng thái, kế hoạch (§4) và con trỏ.
- [0. Từ điển](view.html#muc-0) · [1. Cấu trúc và quy trình (V1)](view.html#muc-1) · [2. Form khai](view.html#muc-2) · [3. 17 thao tác](view.html#muc-3) · [4. Một lượt của agent](view.html#muc-4)
- [5. Khi nào hỏi Owner](view.html#muc-5) · [6. Giám sát](view.html#muc-6) · [7. Lỗ hở đã rà](view.html#muc-7) · [8. Chạy thử và đo](view.html#muc-8) · [9. V2 khác V1](view.html#muc-9)

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| gpt-chat (đề xuất) | OpenAI / GPT | ChatGPT Chat | Host (chưa duyệt) | Owner giao trực tiếp |
| claude-chat (đề xuất) | Anthropic / Claude | Claude Chat | Reviewer (đề xuất) | Owner chuyển tay / CHƯA ĐO |
| codex (đề xuất) | OpenAI / Codex | Codex Desktop/CLI | Worker + khảo sát (đề xuất) | Owner chuyển tay / CHƯA ĐO |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: —

Giữ GitHub làm SSOT; đối chiếu AGENTS.md và ai-council-karpathy để không xây trùng. Chưa tạo file, task con, prompt hay RUN khác. Chỉ chuyển bước sau khi Owner chốt phạm vi.

### 4. Kế hoạch — mục tiêu nhỏ (N) và checkpoint (C)
> 🤖 Biển: từ ngữ theo [Từ điển](view.html#muc-0); form và thao tác ở [view.html mục 2–4](view.html#muc-2). Thứ tự làm = từ trên xuống. Agent chọn N đầu tiên có DUYỆT đúng ghế mình; tích C ngay khi xong, mỗi C một commit. Không sửa N người khác đang làm — ghi vào «Ghi chú».

L1 = §1 + §2 ở trên (Owner).

#### Đầu vào chung
- Đ1 · Số đo 15–30/10: máy làm 2–11% thời gian, lượt agent trung vị 17 phút, chờ giữa lượt 7–11 giờ, DỪNG 18/63 · nguồn: git log repo (Claude Chat đếm 30/10) · chắc: vừa (phân loại lý do DỪNG là ước lượng)
- Đ2 · Trang Task hiện mọi thứ từ §3 đến trước `### Vòng trước` trong ô «Chi tiết cần đạt» ⇒ §4 Kế hoạch hiện được, không cần sửa mã · nguồn: docker/nuxt-repo/scripts/hvu-b2/sync.py parse_objective_parts · chắc: cao
- Đ3 · Cổng ghi repo từ chối ghi khi sai expected_version ⇒ dùng làm khoá chống ghi đè · nguồn: mô tả công cụ fs_edit · chắc: cao
- Đ4 · Hội đồng và kế hoạch (§4) nằm trên GitHub repo incomex-workspace; trang Task trên VPS chỉ đọc từ GitHub và vẽ lại; PG không tham gia việc này. «Sổ PG Tự quản» là mục tiêu của việc khác (nhap-directus-for-workflow), chỉ dùng làm ví dụ form · nguồn: AGENTS.md (GitHub là SSOT), sync.py trang Task · chắc: cao

#### N1 · Viết bản V2: form L/N/C + thao tác + lượt agent · XONG
- Thuộc: L1 · Người làm: claude-chat · Ước: 1h
- Xong khi: view.html có 3 form, bảng thao tác ghi rõ ai · ghi đâu · làm thế nào, lượt agent từng bước, quy tắc hỏi Owner, lỗ hở đã rà.
- Được làm: 👁 · ✍ work/ai-council-newarchitecture/
- Đề xuất: Owner 30/10 14:57 · Duyệt: Owner trực tiếp
- C1 🟢 3 form L/N/C có ví dụ thật (Sổ PG) · bằng chứng: view.html mục 1, commit e5e755d1 · 30/10 15:20 · claude-chat
- C2 🟢 15 thao tác ai · ghi đâu · làm thế nào · bằng chứng: view.html Bảng 2 · 30/10 15:20 · claude-chat
- C3 🟢 Lượt agent 8 bước từ ghế người làm · bằng chứng: view.html mục 3 · 30/10 15:20 · claude-chat
- C4 🟢 9 lỗ hở → xử lý · bằng chứng: view.html Bảng 6 · 30/10 15:20 · claude-chat
- C5 🟢 Từ điển: mỗi từ dùng trong form/thao tác có «là gì» + «không phải» (Owner 15:02) · bằng chứng: view.html mục 0, commit 7a4c8ac9 · 30/10 15:40 · claude-chat
- C6 🟢 Khôi phục đủ V1 (Owner 15:07): 10 định nghĩa, 6 vai, 3 luồng, quy trình 6 bước, 3 mức thay đổi, cơ chế ghi, rào thực thi — gắn nhãn V1; bổ sung Đầu vào chung (Đ), Báo cáo, KHÔNG CHỌN; chỗ khác V1 liệt kê Bảng 9 · bằng chứng: view.html commit 4be69bf2 · 30/10 16:00 · claude-chat
- Báo cáo · 30/10 16:00 · claude-chat
  - Đạt: C1–C6 🟢
  - Chứng cứ: view.html commit 4be69bf2
  - Còn thiếu: chưa thử thật (N3)
  - Đầu vào đã cập nhật: Đ1–Đ3 (mới)
  - Đề xuất tiếp: N2, N3 (đã ghi)
- Lỗi đã sửa trong N1: bản V2 lần đầu (e5e755d1) xoá phần V1 khi chưa đọc kỹ — Owner nhắc 15:07, đã khôi phục ở C6.
- Nghiệm thu: (GPT làm ở N2)

#### N4 · Bảng mục tiêu · ĐANG LÀM · claude-chat · 30/10 16:10
- Thuộc: L1 · Cần trước: N1 · Người làm: claude-chat · Ước: 1h
- Xong khi: Owner nhìn mẫu là hiểu tiến trình của một mục tiêu lớn; mỗi hình/màu ứng đúng một trường của form §4 (vẽ được từ dữ liệu, không thêm chữ ngoài form); Owner đồng ý mẫu.
- Được làm: 👁 · ✍ work/ai-council-newarchitecture/
- Đề xuất: Owner 30/10 15:23 · Duyệt: Owner trực tiếp
- C1 🟢 Vẽ mẫu theo khuôn Công thức: dòng công thức, chú thích hình = loại / màu = trạng thái, thẻ mục tiêu lớn có thanh tiến độ, ô đầu vào, chuỗi mục tiêu nhỏ + chấm checkpoint · bằng chứng: view.html #ban-do-muc-tieu, commit b543f6fb; đã xem ở 1100px và 400px · 30/10 16:15 · claude-chat
- C2 🟡 Chỉnh theo góp ý Owner · Đạt khi: Owner đồng ý mẫu · bằng chứng: 15:29 đổi sang dữ liệu thật (c9f00c1a); 15:35 thay hình bằng Bảng mục tiêu trả lời 6 câu Owner + thêm thao tác 3.18 (af7d908e, 64d716a7); 15:48 mẫu Ma trận mục tiêu 5 cột, 3 tầng xổ, 4 màu (ad8c53bf); 15:54 dạng cây kiểu Apple: 3 cỡ chữ, thụt lề + đường cây, chấm 9px, chấm thẳng một cột đã đo (9e4a5da9, 3a03b9df, 9fc1913b) · 30/10 16:50 · claude-chat
- C3 ⬜ Ghi quy tắc vẽ «trường form → hình/màu» (để máy vẽ tự động ở N5) · Đạt khi: mỗi trạng thái N, C, Đ có đúng một cách vẽ
- Ghi chú: N4 chèn trước N2 (thao tác 3.5 + 3.8) để GPT rà luôn cả bản đồ · claude-chat 30/10
- Ghi chú: dữ liệu mẫu «Sổ PG Tự quản» khiến Owner hiểu là chuyển hội đồng vào PG (15:29) ⇒ đổi sang dữ liệu thật §4 của chính việc này, commit c9f00c1a · claude-chat 30/10

#### N2 · GPT rà V2 từ ghế agent, sửa thẳng, chốt bản thử · DUYỆT
- Thuộc: L1 · Cần trước: N4 · Người làm: gpt-chat · Ước: 1h
- Xong khi: view.html là bản Host chốt để thử; mỗi chỗ GPT sửa có 1 dòng «Ghi chú» dưới đây; không còn điểm bất đồng mở với Claude.
- Được làm: 👁 · ✍ work/ai-council-newarchitecture/
- Đề xuất: claude-chat 30/10 · Duyệt: Owner 30/10 14:57 («GPT đóng góp thêm rồi đưa vào thử nghiệm»)
- C1 ⬜ Đối chiếu phần nhãn V1 với bản V1 gốc (commit d79a12af): đủ ý, không bị hiểu sai; rà 5 dòng Bảng 9 (V2 khác V1) · Đạt khi: mỗi dòng Bảng 9 có «đồng ý» hoặc đã sửa
- C2 ⬜ Rà Từ điển + 17 thao tác + 8 bước lượt agent: mỗi từ một nghĩa, mỗi bước agent làm được mà không phải hỏi · Đạt khi: không còn từ/bước mơ hồ
- C3 ⬜ Sửa thẳng view.html chỗ chưa ổn · Đạt khi: mỗi chỗ đổi có 1 dòng Ghi chú
- C4 ⬜ Nghiệm thu N1 (thao tác 3.16) · Đạt khi: dòng «Nghiệm thu» của N1 đã điền
- Ghi chú:

#### N3 · Thử trên phần còn lại của Sổ PG · ĐỀ XUẤT
- Thuộc: L1 · Cần trước: N2 · Người làm: claude-code (agent) · gpt-chat (Host Sổ PG) · Ước: 3h
- Xong khi: §4 Kế hoạch của work/nhap-directus-for-workflow viết theo form; ≥ 1 lượt agent ≥ 2 giờ chạy bằng lệnh một dòng; đo chỉ số ([view.html mục 8](view.html#muc-8)) so với số cũ.
- Được làm: 👁 · ✍ work/nhap-directus-for-workflow/ (§4) · ⚙ chỉ theo từng N đã DUYỆT bên Sổ PG
- Đề xuất: claude-chat 30/10 · Duyệt: —
- C1 ⬜ Host Sổ PG chuyển việc còn lại thành L1 + N theo form · Đạt khi: §4 bên Sổ PG có ≥ 2 N DUYỆT
- C2 ⬜ Lượt agent đầu tiên bằng lệnh một dòng · Đạt khi: ≥ 1 N XONG, C tích đủ bằng chứng
- C3 ⬜ Đo chỉ số, ghi lỗ mới vào view.html Bảng 7 · Đạt khi: Bảng 8 có cột kết quả thử
- Ghi chú:

#### N5 · Trang Task tự vẽ Bản đồ mục tiêu từ §4 · ĐỀ XUẤT
- Thuộc: L1 · Cần trước: N4 · Người làm: (Host chọn — claude-code hoặc codex) · Ước: 3h
- Xong khi: trang Task đọc §4 của mọi việc và vẽ đúng mẫu N4; sửa §4 xong mở trang Task thấy hình đổi theo; việc thiếu §4 hiện «chưa có kế hoạch».
- Được làm: 👁 · ✍ nhánh + PR mã trang Task (scripts/hvu-b2) · merge/deploy theo KST
- Đề xuất: claude-chat 30/10 · Duyệt: —
- C1 ⬜ Bộ đọc §4 ra dữ liệu L/Đ/N/C · Đạt khi: đọc đúng §4 của việc này
- C2 ⬜ Vẽ theo quy tắc N4.C3 · Đạt khi: ảnh chụp khớp mẫu
- C3 ⬜ PR xanh, KST merge · Đạt khi: trang Task thật hiện hình
- Ghi chú:

### Vòng trước
- C3 · 30/10 16:00 · Claude Chat · Owner 15:07 nhắc: bản V2 lần đầu đã xoá định nghĩa/quy trình V1 của GPT khi chưa đọc kỹ. Đã khôi phục đủ V1 (nhãn V1) và ghi mọi chỗ V2 khác V1 vào [Bảng 9](view.html#muc-9) để GPT rà.
- C2 · 30/10 15:25 · Claude Chat · theo Owner 14:57 bỏ phần bàn, viết thẳng V2 (N1 XONG). Khái niệm «Giấy phép» của C1 đã nhập vào trường «Được làm» của N — không còn là khái niệm riêng.
- C1 · 30/10 15:10 · Claude Chat (khác hãng Host) · phản biện V1 tại [view.html#muc-v](view.html#muc-v). Kết luận: V1 đúng hướng nhưng còn giữ «Host duyệt từng mục tiêu nhỏ/READY từng lượt» là chỗ tắc đo được; đề xuất thêm **Giấy phép**, 5 khái niệm (Mục tiêu · Giấy phép · Lượt · Checkpoint · Cổng). Chưa có hiệu lực; Host chốt.
