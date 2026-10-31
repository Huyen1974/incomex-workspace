# COLLAB — ai-council-newarchitecture
Tên việc: Hội đồng AI — kế hoạch động, thực thi song song
HTML chính: view.html

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner 30/10/2026 lập task; 14:57 chỉ đạo «không bàn nữa mà làm»: chốt 5 việc Owner quyết + quy trình Mục tiêu lớn → Mục tiêu nhỏ → Checkpoint (§1 mục 9), sửa thẳng bản thiết kế, GPT góp thêm rồi chạy thử. Host: GPT Chat (đề xuất, Owner chưa chỉ định riêng). Chưa đổi AGENTS.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-31 08:07 +07 · GPT Host · rà N4 Đầu vào, N10 giữ ĐỀ XUẤT
- 🎯 Mục tiêu: Owner chỉ quyết 5 việc; còn lại AI chạy theo Mục tiêu lớn (L) → Đầu vào chung (Đ) → Mục tiêu nhỏ (N) → Checkpoint (C) với từ điển + form khai chung, agent khảo sát và đề xuất nhiều nhất, hội đồng tập trung giám sát.
- 🏁 Xong khi: từ điển + form + thao tác ở [view.html](view.html) chạy thử đạt trên ≥ 1 việc thật, đo chỉ số ([mục 8](view.html#muc-8)); lỗ gặp khi thử đã vá vào form.
- 📍 Tiến độ: [✅ N1 bản V2.1] → [■ N4 Bảng mục tiêu] → [□ N2 GPT rà, sửa thẳng] → [□ N3 thử trên Sổ PG] → [□ Sửa AGENTS theo kết quả thử].
- ✅ Đã xong: N1 — [view.html](view.html) V2.1: **giữ đủ định nghĩa, vai, cấu trúc, quy trình V1 của GPT** (nhãn V1) + bổ sung: từ điển có cột «không phải», form L/Đ/N/C/Báo cáo, 17 thao tác (ai · ghi đâu · làm thế nào), lượt agent 8 bước, khi nào hỏi Owner, 10 lỗ hở, bảng V2 khác V1. §4 bên dưới đã viết theo form. N4.C2: [Bảng mục tiêu](view.html#ban-do-muc-tieu) thay hình minh hoạ — «Hỏi gì → nhìn đâu» + 4 bảng (Mục tiêu lớn · Đầu vào · Mục tiêu nhỏ × Checkpoint · Báo cáo), dưới mỗi bảng ghi ai thêm, thêm thế nào; thêm thao tác 3.18 chuyển checkpoint chưa xong sang N sau.
- ■ Đang làm: N4 · GPT Host đã đối chiếu 5 bổ sung của Claude, hiệu chỉnh 3 điểm (Đ6 vào Quyền, Đ18 chưa kiểm ≠ thiếu, N10 dùng nguồn hiện hữu trước). N4 chưa nghiệm thu toàn phần, 0 RUN kỹ thuật.
- ⬜ Còn lại: N4 chốt bảng + quy tắc vẽ; N2 GPT rà (gồm cả bảng); N3 thử trên Sổ PG; N5 trang Task tự vẽ (đề xuất); sửa AGENTS sau khi thử đạt.
- ➡ Kế tiếp: Claude/Owner đối chiếu N4 sau hiệu chỉnh nhỏ; N10 đồng ý mục đích nhưng vẫn ĐỀ XUẤT, chưa GO đo máy chủ; GPT chốt N2 rồi thử N3 theo cổng hiện hành. NEXT_TRIGGER=CLAUDE_OWNER_VERIFY_N4_INPUT_AND_N10.
- 😊 Owner cần quyết (không gấp): mục tiêu lớn 3 (+) «Sửa luật AGENTS theo cách làm mới» — đề xuất: GẬT, làm sau khi chạy thử đạt.
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
16. Owner 30/10/2026 16:10 (viết lại đúng ý): phải có mục 2, mục 3 — chỉ có mục 1 thì AI đọc dễ hiểu nhầm. Tình trạng cần thêm: đã duyệt (nhất là với mục tiêu lớn), xong một phần (vàng), đã làm xong và Host duyệt (Host duyệt phải có ý kiến AI khác hãng trước — quy tắc nói sau, giờ chỉ cần nhìn thấy tình trạng); đề xuất bổ sung mục tiêu lớn/nhỏ/checkpoint bằng dấu + (xanh) hoặc − (đỏ) ở cột mục tiêu. Đổi tên cột thành «Mục tiêu / Nhiệm vụ». Hướng dẫn tầng viết ngắn: 1 = mục tiêu lớn (số nguyên) · 1.1 = mục tiêu nhỏ (một chấm) · 1.1.1 = checkpoint (hai chấm).
17. Owner 30/10/2026 16:16 (viết lại đúng ý): khen cách «đề xuất = vòng, đã duyệt = chấm» — giữ. Dấu + / − đang nặng, làm nhẹ cho hài hoà với các chấm. Mục 2, mục 3 cũng phải có chi tiết (xổ ra mục tiêu nhỏ, checkpoint) như mục 1 thì AI mới hiểu. Phần chú thích gọi là «Cách đọc bảng», thu gọn lại — chỉ cho người mới. Nhiều thông tin nhưng nhìn phải gọn.
18. Owner 30/10/2026 16:22 (viết lại đúng ý): chấm tình trạng to hơn một chút vì có hai loại (vòng và chấm đặc). Xám cũng có vòng: vòng xám = mới đề xuất, chưa duyệt; Host duyệt xong mới thành chấm xám (đã duyệt, chưa làm). Mọi chấm phải tròn (không ô van) và cùng kích thước.
19. Owner 30/10/2026 16:32 (viết lại đúng ý): vòng ở cột tình trạng phải mảnh như vòng ở «Cách đọc bảng» (nhẹ nhàng hơn). Cột Báo cáo để mờ, không cần màu. Tên các cột dùng cơ chế «?» như cả hệ thống: giải thích + hướng dẫn. Thêm 3 cột ký tên: Host, Thực hiện, Council — Host tự ký, người thực hiện tự ký, thành viên council tự điền tên mình vào (không được xoá tên người khác).
20. Owner 30/10/2026 16:34: bỏ dòng «Vòng = chưa duyệt · Chấm = đã duyệt» trong «Cách đọc bảng» — thừa.
21. Owner 30/10/2026 16:54 (viết lại đúng ý): có lẽ tạm bỏ 3 cột Host · Thực hiện · Council — làm bảng phức tạp mà không giải quyết được vấn đề. Cạnh cột Báo cáo cần cột Lịch sử: biết ai đã làm gì với từng việc, ít nhất tới mục tiêu nhỏ, chi tiết tới checkpoint càng tốt. Thông tin này repo đã có — chuyển sang đây hoặc link tới đó; chỉ cần AI đọc được, không phức tạp cho User. Phải quy định thành cột cố định để không mỗi lần làm một kiểu. Owner hỏi ý kiến giải pháp kỹ thuật.
22. Owner 30/10/2026 17:08 (viết lại đúng ý): lịch sử commit không thay được — phải có một bảng ký tên, mọi thứ quy chuẩn; bảng này không hiện hết trên ma trận. Vai trò (Host, phản biện, thực hiện, giám sát, nhắc việc, giám sát toàn hệ: có ai trốn việc, có chỗ nào thiếu chữ ký mà vẫn được thông qua) có thể đổi nên không định nghĩa cứng mà bàn cơ chế ai đọc cũng hiểu. Ba biến số: (1) vị trí công việc — nhiệm vụ cố định; (2) bổ nhiệm AI vào vị trí — ít đổi, theo từng việc; (3) thực thi từng việc cụ thể — đổi nhiều nhất. Ví dụ cơ chế: AI đề xuất phải ký «đã đề xuất» thì Host mới biết để duyệt (Host chỉ duyệt khi có ít nhất 1 chữ ký khác hãng); giám sát thấy council không vào → gọi nhắc việc → nhắc vài lần không được → gọi User. Hiện làm hạ tầng (sẵn sàng cho mọi quy trình); quy trình bàn sau vì hay đổi. Liên quan: phiên khác đang làm cơ chế AI phải xưng danh khi ghi. Owner hỏi ý kiến cách tổ chức kỹ thuật trước.
23. Owner 30/10/2026 17:14 (viết lại đúng ý): bảng ký ghi ở đâu — PG hay GitHub? Không muốn mỗi lần viết tay; cần cách đồng bộ tương đối. Hỏi chuẩn ngành IT đang làm việc này thế nào để làm căn cứ thiết kế; AI đề xuất.
24. Owner 30/10/2026 17:23 (viết lại đúng ý): chốt vẫn trên GitHub. Ký dùng cơ chế ghi danh sắp xong (muốn ghi phải ghi danh, lấy vé tạm) — ghi gì hệ thống cũng bắt được danh; chưa ghi = chưa có, kể cả đã làm mà chưa ghi. Việc đầu tiên: bỏ 3 cột Host · Thực hiện · Council, thay bằng 1 cột «Tiến trình» (thống kê AI nào đã làm gì), bấm vào thì ra một nơi khác; thống kê theo mục tiêu nhỏ/lớn thế nào chưa rõ — AI đọc là chính nên dùng thứ tiêu chuẩn có sẵn, không cần thiết kế riêng. Làm cột và giải thích trước, Owner hướng dẫn tiếp.
25. Owner 30/10/2026 20:32 (viết lại đúng ý): cột Tiến trình chiếm nhiều chỗ — ưu tiên bề rộng tối đa cho cột Mục tiêu và cột Thế nào là hoàn thành (thông tin thật sẽ rất dài), cột khác không méo nhưng không phí chỗ. Ma trận mục tiêu (từ «Cách đọc bảng» tới dòng «Bấm dòng có ›…») là một miếng độc lập. Phía trên cần miếng đầu tiên «Thông tin đầu vào» — vì từng có nhiều tuần cả Claude và GPT thiết kế, điều hành trên giả định PG cũ trong khi hệ thống đã dùng PG/Directus mới. Cần quy định: ghi thông tin gì, khi nào, ai ghi (Host, hội đồng, agent) — đủ mà không phức tạp, mọi AI hiểu thống nhất; «?» là hướng dẫn. AI cho ý kiến rồi làm luôn form.
26. Owner 30/10/2026 20:44 (viết lại đúng ý): Claude hiểu nhầm ý mục 25. Đầu vào = để làm được mục tiêu, hiện ta đang có gì — ngữ cảnh để triển khai, đủ để ra quyết định (ví dụ nấu cơm cần: gạo, điện, nồi cơm điện, nước, số người ăn, giờ cần cơm chín). Hiện mỗi AI khi làm, khi đánh giá lại đều phải tự kiểm lại thông tin, mà vẫn có lúc quên cái cơ bản nhất (vd PG đang ở phiên bản nào). Cần ý kiến chuyên môn: nên thống kê những gì, quy định thế nào để mọi AI hiểu thống nhất — không phải chỉ liệt kê sự kiện.
27. Owner 30/10/2026 20:55 (viết lại đúng ý): ghi thành quy định theo chuẩn ngành để mọi AI hiểu giống nhau, đúng cái cần hiểu, không thừa, nhất quán trong mọi việc; GPT có ý kiến sau. Nguyên tắc: làm việc gì cũng có điều kiện đầu vào và mục tiêu đầu ra — mục tiêu đã chốt, giờ quy định đầu vào. Có form và hướng dẫn tốt thì agent nào cũng điền được, thành tự động. Đồng ý một phần do máy làm, nhưng phải nghĩ cho mọi loại việc; với từng việc chỉ là trả lời các câu hỏi — làm sẵn form + hướng dẫn, agent khảo sát và điền. Phần nào cũng có ô ghi chú/bổ sung cho thứ không theo chuẩn.

28. Owner 30/10/2026 21:23 (GPT Chat): «có những việc thiếu => plan lập tức phải bổ sung mục tiêu con về chuẩn bị nguồn»; không được bắt tay làm ngay rồi tắc mới báo thất bại. Giao GPT sửa trực tiếp phần Thông tin đầu vào, giữ khung Claude đã làm; sau ví dụ và thử nghiệm, đóng gói thành pack chuẩn dùng lại khi mở task mới (chưa triển khai pack).
29. Owner 30/10/2026 22:06: «Cần bổ sung gì thì bạn bổ sung luôn, giờ là hiệu chỉnh cho nên cần chú ý tránh kiểu dỡ ra viết lại»; bổ sung tinh chỉnh thì cứ bổ sung thẳng cho nhanh.

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
- L2 · Quy tắc khi nào hỏi Owner · DUYỆT · Owner nói: «những việc đi vào luẩn quẩn … nên hoàn thiện dần quy tắc này để khi nào cần phải xin ý kiến của User» — 30/10 14:57 · Xong khi: mọi lần Owner phải can thiệp đều thành quy tắc (view.html mục 5) · mục tiêu nhỏ: N6, N7 (ma trận mục 2).
- L3 · + Sửa luật AGENTS theo cách làm mới · ĐỀ XUẤT (claude-chat, từ lộ trình «Sửa AGENTS sau khi thử đạt») · Xong khi: AGENTS ghi đúng cách làm đã chạy thử đạt · chờ Owner gật (thao tác 3.3) · mục tiêu nhỏ (+ đề xuất cùng L3): N8, N9 (ma trận mục 3).

#### Đầu vào chung
> 🤖 Biển: Đầu vào chung 8 mục. **Mục 2/3/4** trả lời CẦN gì → HIỆN CÓ gì; mục 1/5/6/8 ghi bối cảnh/quyết định/ghi chú, không ép theo khuôn Cần→Có. Nếu dòng chỉ phục vụ một N, ghi `cho: Nx`; không ghi = chung. Ghi nguồn, thời điểm kiểm và trạng thái ● đủ/đã kiểm · ○ chưa kiểm · 🟡 cần kiểm lại · 🔴 thiếu/sai. Thiếu nguồn ở mục nào thì đánh dấu **tại mục đó**; mục 7 chỉ dành cho điều chưa xếp được nhóm. Thiếu thiết yếu cho Nx ⇒ đề xuất N chuẩn bị/khảo sát trước Nx, gắn `Nx cần trước: N chuẩn bị · Đx`, không tạo trùng. **Chưa được duyệt N ≠ thiếu nguồn**; không đánh đỏ khi chưa kiểm. Host duyệt N chuẩn bị trước RUN; chỉ chặn N phụ thuộc, việc độc lập tiếp tục. Dữ liệu động/quyền kiểm khi dùng; không khảo sát lại toàn bộ mỗi lượt. Sai: giữ dòng cũ có dẫn sang Đ mới, Git lưu dấu vết. Chi tiết: [view.html › Thông tin đầu vào](view.html#dau-vao).
- 1 Dùng cho ai · khi nào · bao nhiêu
  - Đ7 · Owner và mọi AI hội đồng; áp cho mọi việc trên trang Task (11 việc) · nguồn: Owner 30/10 14:57 · trang Task · kiểm: 30/10 · Claude · ●
  - Đ8 · Hạn: Owner chưa nêu · nguồn: — · kiểm: — · ○
- 2 Nguyên liệu có sẵn
  - Đ9 · Bản V1 của GPT (commit d79a12af) và bản V2 view.html · nguồn: repo · work/ai-council-newarchitecture · kiểm: 30/10 · Claude · ●
  - Đ1 · Số đo 15–30/10: máy làm 2–11% thời gian; lượt agent trung vị 17 phút; chờ giữa lượt 7–11 giờ; 18/63 lượt DỪNG · nguồn: git log repo · kiểm: 30/10 · Claude · ●
  - Đ10 · Khuôn «?» và ma trận đã làm ở Công thức (ban-duyet.html) để dùng lại · nguồn: repo · work/mow-mot-moit-mout · kiểm: 30/10 · Claude · ●
- 3 Dụng cụ
  - Đ11 · GitHub repo incomex-workspace (nơi gốc của hội đồng) · nguồn: AGENTS.md · kiểm: 30/10 · Claude · ●
  - Đ3 · Cổng ghi repo từ chối khi sai phiên bản (expected_version) ⇒ khoá chống ghi đè · nguồn: công cụ fs_edit · đã dùng thật · kiểm: 30/10 · Claude · ●
  - Đ2 · Trang Task hiện từ §3 đến trước «Vòng trước» ⇒ §4 Kế hoạch hiện được, không sửa mã · nguồn: sync.py · parse_objective_parts · kiểm: 30/10 · Claude · ●
  - Đ12 · PG, Directus: không dùng cho việc này · nguồn: Đ4 · kiểm: 30/10 · Claude · không cần
- 4 Quyền và đường vào
  - Đ6 · Cần: cơ chế ghi danh khi bước triển khai yêu cầu xưng danh. Hiện: phiên khác đang làm, chưa xác minh chạy thật; chỉ kiểm trước N phụ thuộc, không chặn thiết kế form hiện tại · nguồn: Owner 30/10 17:23 · kiểm: chưa đo live · ○
  - Đ13 · claude-chat, gpt-chat ghi thư mục việc qua cổng ghi repo; Owner không phải bấm gì · nguồn: đã ghi thật 30/10 · kiểm: 30/10 · Claude · ●
- 5 Ràng buộc
  - Đ14 · Một tài liệu: chỉ sửa view.html và COLLAB.md, không đẻ file mới · nguồn: luật chung của Owner · kiểm: 30/10 · Claude · ●
  - Đ15 · Không sửa AGENTS, production, VPS khi chưa chạy thử đạt · nguồn: Owner 30/10 14:57 · mục 3 ma trận · kiểm: 30/10 · Claude · ●
  - Đ16 · Đọc kỹ bản cũ trước khi sửa phần người khác viết · nguồn: Owner 30/10 15:07 · kiểm: 30/10 · Claude · ●
- 6 Đã chốt
  - Đ17 · Owner chỉ quyết 5 việc; còn lại hội đồng tự chạy · nguồn: Owner 30/10 14:57 · kiểm: 30/10 · Owner · ●
  - Đ4 · Hội đồng và kế hoạch ở GitHub; trang Task chỉ đọc lại; PG không tham gia · nguồn: Owner 30/10 15:29, 17:23 · kiểm: 30/10 · Owner · ●
  - Đ5 · Ký = ghi danh khi ghi lên repo; chưa ghi = chưa có · nguồn: Owner 30/10 17:23 · kiểm: 30/10 · Owner · ●
- 7 Còn thiếu
  - Đ18 · cho: N3 · Cần: xác minh nguồn dữ liệu, môi trường và quyền để thử Sổ PG. Hiện: N3.C1 chưa khảo sát/ghi đủ bằng chứng trong task này (CHƯA KIỂM); N3 còn ĐỀ XUẤT là cổng duyệt, không phải thiếu nguồn. Bước kế: N3.C1 rà đầu vào; phát hiện thiếu thật mới ghi đỏ tại mục 2/3/4 và thêm N chuẩn bị trước N3 · nguồn: ma trận 1.4, N3.C1 · kiểm: 2026-10-31 · GPT Host đối chiếu repo · ○
- 8 Ghi chú, bổ sung
  - Đ19 · Bảng mục tiêu cũ (4 bảng) giữ lại tới khi ma trận được chốt · nguồn: Owner 30/10 15:48 · kiểm: 30/10 · Claude · ●

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
- C2 🟡 Chỉnh theo góp ý Owner · Đạt khi: Owner đồng ý mẫu · bằng chứng: 15:29 đổi sang dữ liệu thật (c9f00c1a); 15:35 thay hình bằng Bảng mục tiêu trả lời 6 câu Owner + thêm thao tác 3.18 (af7d908e, 64d716a7); 15:48 mẫu Ma trận mục tiêu 5 cột, 3 tầng xổ, 4 màu (ad8c53bf); 15:54 dạng cây kiểu Apple: 3 cỡ chữ, thụt lề + đường cây, chấm 9px, chấm thẳng một cột đã đo (9e4a5da9, 3a03b9df, 9fc1913b); 16:10 mục 2–3, 6 tình trạng, +/−, cột «Mục tiêu / Nhiệm vụ», chú thích 1 / 1.1 / 1.1.1 (9452bc4c); 16:16 +/− thành vòng mảnh, mục 2–3 có mục tiêu nhỏ + checkpoint, «Cách đọc bảng» thu gọn (aeb9b34c); 16:22 mọi chấm/vòng 12px tròn đều (đo 60/60 chấm 12.00×12.00, một cột), vòng xám = mới đề xuất → chấm xám = Host duyệt · chưa làm, chú thích xếp theo vòng đời (c241bfd9) · 30/10 16:26 · claude-chat
- C3 ⬜ Ghi quy tắc vẽ «trường form → hình/màu» (để máy vẽ tự động ở N5) · Đạt khi: mỗi trạng thái N, C, Đ có đúng một cách vẽ
- C4 − ⬜ Bỏ Bảng mục tiêu cũ (4 bảng, view.html #ban-do-muc-tieu) · Đạt khi: ma trận được Owner chốt — trước đó giữ nguyên (Owner 15:48 «đừng xóa vội») · ĐỀ XUẤT BỎ, chờ Owner
- Ghi chú: N4 chèn trước N2 (thao tác 3.5 + 3.8) để GPT rà luôn cả bản đồ · claude-chat 30/10
- Ghi chú: dữ liệu mẫu «Sổ PG Tự quản» khiến Owner hiểu là chuyển hội đồng vào PG (15:29) ⇒ đổi sang dữ liệu thật §4 của chính việc này, commit c9f00c1a · claude-chat 30/10
- Ghi chú: claude-chat rà bản GPT sửa Đầu vào (commit 7fef7a8d) · 30/10 21:56 · ĐÃ ÁP 22:11 theo Owner 22:06 (commit dc15cd45): 1 quy tắc 2 · 2 quy tắc 3 + «?» mục 7, Đ6 sang mục 3 · 3 «cho: Nx», Đ18 cho N3 · 4 xong nhờ 1 (dòng đủ chỉ cần «có: …») · 5 thêm N10 ĐỀ XUẤT, ma trận 1.6
  - Đồng ý: Cần → Có → Đủ chưa; thiếu → thêm N chuẩn bị NGAY trước N phụ thuộc; chưa kiểm ≠ thiếu; chỉ chặn phần phụ thuộc; bỏ hạn 7 ngày cứng.
  - Đề xuất 1 · «Cần → Có» chỉ áp cho mục 2, 3, 4 (nguồn lực). Mục 1, 5, 6 là bối cảnh — ghi thẳng như cũ; ép «Cần/Có» vào đó làm câu rối.
  - Đề xuất 2 · Dòng thiếu nằm ngay ở mục của nó (vd thiếu quyền → đỏ ở mục 4), không dồn về mục 7. Dồn về 7 thì mục 2/3/4 luôn xanh, nhìn không biết tắc ở đâu. Mục 7 chỉ cho thứ chưa xếp được mục nào. Sửa cả quy tắc 3 («đỏ ở mục 7»).
  - Đề xuất 3 · Thêm trường «Cho: Nx» vào mỗi dòng Đ (cả Task → «chung»). Quy tắc 6, 7 nói «chặn Nx phụ thuộc» mà dòng Đ chưa có chỗ ghi phụ thuộc N nào → không áp được.
  - Đề xuất 4 · Đồng bộ dữ liệu: chỉ Đ6, Đ18 theo khuôn mới; Đ1–Đ17 và form mẫu mục 2.2 vẫn khuôn cũ → viết lại cùng một khuôn.
  - Đề xuất 5 · Giữ đề xuất «Hệ thống hiện tại» (máy tự ghi phiên bản PG, Directus, máy chủ — Owner 20:55 đồng ý một phần do máy): ghi thành N ĐỀ XUẤT dưới L1, chờ Owner gật vì phải chạy công cụ trên máy chủ. Bản sửa của GPT bỏ mất chỗ ghi đề xuất này.

- Ghi chú: GPT Host 2026-10-31 rà 5 ý Claude: đồng ý khuôn 2/3/4, thiếu tại nguồn, «cho: Nx», dữ liệu mẫu và N10 theo hướng tái sử dụng; hiệu chỉnh Đ6 thuộc nhóm quyền, Đ18 chưa được đo không thể tô đỏ, N10 giữ ĐỀ XUẤT, chưa GO máy chủ. Không sửa Ma trận mục tiêu.

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

#### N10 · + Hệ thống hiện tại do máy tự ghi · ĐỀ XUẤT
- Thuộc: L1 · Cần trước: — · Người làm: (Host chọn) · Ước: 2h
- Xong khi: mục 3 Đầu vào trỏ tới một nguồn hiện trạng có phiên bản, tình trạng và giờ kiểm đáng tin; ưu tiên dùng sổ/nguồn đo hiện có, không dựng nơi lưu thứ hai hoặc chép tay.
- Được làm: 👁 khảo sát chỉ đọc các nguồn đã có; ⚙ chạy công cụ đo trên máy chủ hoặc tạo cơ chế tự ghi cần phê duyệt riêng, chưa GO
- Đề xuất: claude-chat 30/10 22:11 (Owner 20:55 đồng ý một phần do máy) · Duyệt: —
- C1 ⬜ Rà nguồn hiện trạng sẵn có trước · Đạt khi: mỗi mục cần đo có nguồn tin cậy và thời điểm kiểm; chỉ liệt kê phần thật sự thiếu
- C2 ⬜ Kiểm bằng đường chỉ đọc đã duyệt; chỉ đề xuất máy đo bổ sung nếu thiếu thật · Đạt khi: không giả phiên bản từ ký ức, không dựng service mới mặc định
- C3 ⬜ Nối vào đầu vào · Đạt khi: mục 3 dẫn tới, không chép tay
- Ghi chú: GPT Host 31/10 chấp nhận mục đích N10, **chưa duyệt thi hành**; N10 không là điều kiện bắt buộc của N2/N3. Giữ ĐỀ XUẤT, chỉ chạy máy chủ khi đủ thẩm quyền.

#### N6 · Ghi các trường hợp phải hỏi Owner · XONG
- Thuộc: L2 · Người làm: claude-chat · Ước: (đã làm trong N1)
- Xong khi: mỗi trường hợp phải hỏi Owner viết rõ có / không (view.html mục 5).
- Được làm: 👁 · ✍ work/ai-council-newarchitecture/
- Đề xuất: Owner 30/10 14:57 · Duyệt: Owner trực tiếp
- C1 🟢 Đổi mục tiêu lớn → luôn hỏi Owner · bằng chứng: view.html 5.1, commit e5e755d1 · 30/10 15:20 · claude-chat
- C2 🟢 Phá huỷ · quyền · tiền → luôn hỏi Owner · bằng chứng: view.html 5.2, commit e5e755d1 · 30/10 15:20 · claude-chat
- C3 🟢 Luẩn quẩn: 2 lượt chưa thống nhất, hoặc một N DỪNG 2 lần → hỏi Owner · bằng chứng: view.html 5.3, commit e5e755d1 · 30/10 15:20 · claude-chat
- C4 🟢 Hội đồng không dám quyết → ghi rõ rủi ro gì rồi hỏi · bằng chứng: view.html 5.4, commit e5e755d1 · 30/10 15:20 · claude-chat
- Nghiệm thu: (GPT làm ở N2)

#### N7 · + Thêm quy tắc sau mỗi lần Owner can thiệp · ĐỀ XUẤT
- Thuộc: L2 · Người làm: (Host chọn) · Ước: 30 phút mỗi lần
- Xong khi: mỗi lần Owner phải can thiệp có một dòng quy tắc mới ở view.html 5.5.
- Được làm: 👁 · ✍ work/ai-council-newarchitecture/
- Đề xuất: claude-chat 30/10 · Duyệt: —
- C1 + ⬜ Lần 30/10 15:07 (sửa tài liệu người khác khi chưa đọc) → quy tắc «đọc kỹ bản cũ trước khi sửa của người khác» · Đạt khi: có dòng 5.x trong mục 5
- Ghi chú:

#### N8 · + Đối chiếu AGENTS với cách làm mới · ĐỀ XUẤT (cùng L3)
- Thuộc: L3 · Cần trước: N3 · Người làm: (Host chọn) · Ước: 1h
- Xong khi: liệt kê đủ chỗ AGENTS phải sửa; chưa sửa AGENTS.
- Được làm: 👁 AGENTS.md · ✍ work/ai-council-newarchitecture/
- Đề xuất: claude-chat 30/10 · Duyệt: —
- C1 ⬜ Duyệt từng lượt → duyệt mục tiêu nhỏ · Đạt khi: có dòng sửa
- C2 ⬜ Ý kiến AI khác hãng → lúc duyệt N và lúc nghiệm thu · Đạt khi: có dòng sửa
- C3 ⬜ Host tự kiểm đầu vào → agent khảo sát · Đạt khi: có dòng sửa
- Ghi chú:

#### N9 · + Ghi luật mới vào AGENTS · ĐỀ XUẤT (cùng L3)
- Thuộc: L3 · Cần trước: N8 · Người làm: (Host chọn) · Ước: 1h
- Xong khi: AGENTS khớp cách làm đã chạy thử đạt.
- Được làm: 👁 · ✍ nhánh sửa AGENTS · ⛔ tự merge — chờ Owner gật
- Đề xuất: claude-chat 30/10 · Duyệt: —
- C1 ⬜ Viết bản sửa · Đạt khi: có bản sửa trên nhánh
- C2 ⬜ AI khác hãng rà · Đạt khi: có ý kiến đồng ý
- C3 ⬜ Owner gật · Đạt khi: Owner đồng ý
- Ghi chú:

### Vòng trước
- C3 · 30/10 16:00 · Claude Chat · Owner 15:07 nhắc: bản V2 lần đầu đã xoá định nghĩa/quy trình V1 của GPT khi chưa đọc kỹ. Đã khôi phục đủ V1 (nhãn V1) và ghi mọi chỗ V2 khác V1 vào [Bảng 9](view.html#muc-9) để GPT rà.
- C2 · 30/10 15:25 · Claude Chat · theo Owner 14:57 bỏ phần bàn, viết thẳng V2 (N1 XONG). Khái niệm «Giấy phép» của C1 đã nhập vào trường «Được làm» của N — không còn là khái niệm riêng.
- C1 · 30/10 15:10 · Claude Chat (khác hãng Host) · phản biện V1 tại [view.html#muc-v](view.html#muc-v). Kết luận: V1 đúng hướng nhưng còn giữ «Host duyệt từng mục tiêu nhỏ/READY từng lượt» là chỗ tắc đo được; đề xuất thêm **Giấy phép**, 5 khái niệm (Mục tiêu · Giấy phép · Lượt · Checkpoint · Cổng). Chưa có hiệu lực; Host chốt.
