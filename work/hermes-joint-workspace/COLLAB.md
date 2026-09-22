# COLLAB — Hermes Joint Workspace

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Mục tiêu (mở rộng 2026-09-21 theo chỉ đạo Owner: “cần 1 thành viên chạy API để các nhiệm vụ khép kín vòng”): Hermes là thành viên hội đồng cùng GPT và Claude, **chạy API 24/7 trên VPS**: tự thức khi repo có việc tới lượt mình, làm đúng vai được giao, ghi qua đường đã audit với dấu `[Hermes]`, và tự báo Owner khi gặp việc vượt quyền — để vòng công việc khép kín mà Owner không phải trực máy.
- Nhiệm vụ/phạm vi: nối Hermes qua Agent Data đang có; không mở đường ghi Git thứ ba, không đưa tài khoản GitHub Owner lên VPS, không cấp sudo rộng; tái dùng chuông GitHub webhook + backstop 15′ đang chạy (DROOT07) để đánh thức Hermes, không dựng chuông mới.
- Tiêu chí xong: T1–T6 (đọc · ghi · chống ghi đè · chéo GPT/Claude) + T7 tự thức khi repo đổi mà không ai nhắn + T8 gặp việc vượt quyền thì ghi blocker và báo Owner, không tự vượt — PASS bằng chạy thật; sau đó mới cập nhật luật gốc hội đồng 3 thành viên.
- Xác nhận User: **ĐÃ XÁC NHẬN** — Owner 21/09/2026 ủng hộ mục tiêu Hermes chạy API khép kín vòng, yêu cầu tự động nhưng phải tối ưu tài nguyên/thời gian/token và tách HJW thành việc riêng xử lý dứt điểm.

Hội đồng: GPT · Claude · Hermes (Owner quyết 2026-09-20, ghi ở COLLAB gốc DROOT02). Trước mắt làm việc: GPT + Claude; Hermes vào khi HJW.3 PASS.
Host: GPT Chat · Host_ID: GPT-HJW-260922-A · Owner chuyển Host 2026-09-22
HTML chính: `view.html`

## Dòng hiện hành
HJW | Hermes thành viên hội đồng chạy API, khép kín vòng | việc 2/5 | A0 ĐÃ XÁC NHẬN | NEXT: Claude phản biện P02 → GPT Host chốt PROMPT HJW.2 | BLOCK: —

## Quyết định Owner
- D01 · 2026-09-20 · Mục tiêu: Hermes tham gia workspace đầy đủ như một thành viên. Được làm gì hay không là do lệnh điều hành, như GPT/Claude; không dựng rào kỹ thuật riêng cho Hermes.
- D02 · 2026-09-20 · Hội đồng gồm 3 thành viên: GPT · Claude · Hermes.
- D03 · 2026-09-20 · Kênh: Agent Data (`workspace_*`, cùng cửa Claude Code đang dùng) vì Hermes nằm trên VPS. Không đưa tài khoản GitHub của Owner lên VPS; không mở cửa ghi thứ ba (giữ D12).
- D04 · 2026-09-20 · Cách làm: tham gia · an toàn · tận dụng tối đa cái đang có · hạn chế xây mới · nhanh nhất, không sa đà.
- D05 · 2026-09-21 · Owner xác nhận mục tiêu mở rộng: Hermes chạy API 24/7 để khép kín vòng, nhưng **tự động phải tiết kiệm**. GitHub push/webhook không được mặc định đánh thức LLM Hermes cho mọi thay đổi; phải có bộ lọc deterministic trước, chỉ wake Hermes khi tín hiệu/assignment máy đọc xác định việc tới lượt Hermes. Backstop dùng cùng logic chống trùng.
- D06 · 2026-09-21 · Tách việc dứt điểm: JEV.B1 OpenAI hoàn tất + nghiệm thu trước; sau đó `work/hermes-joint-workspace/` mới RUN riêng. Không một RUN/PROMPT gộp hai task.
- D07 · 2026-09-22 · Owner chuyển Host của HJW sang **GPT Chat**; Host_ID hiện hành `GPT-HJW-260922-A`. Việc chuyển Host không đổi A0, D01–D06 hay phạm vi kỹ thuật đã chốt.

## Kế hoạch
- HJW.1 | Mở việc + nhận ý kiến GPT (P01) | ✓ 21/09
- HJW.2 | Một PROMPT cho Claude Code, làm một lần. **Chỉ cấu hình phía Hermes, không sửa backend Agent Data ⇒ không phải chờ R03 CLOSED.** (a) Khai Agent Data vào `mcp_servers` của Hermes, ưu tiên relay nội bộ. (b) Một skill mỏng dạy Hermes luật hội đồng: đọc AGENTS → A0 → vai; Reviewer chỉ ghi P, không tự chạy thử/triển khai khi prompt không giao; mọi ghi qua đường audit; tiền tố `[Hermes]`. (c) Nối chuông: sau bước dựng snapshot của webhook/backstop DROOT07, **lọc tất định** — chỉ đánh thức Hermes khi `COLLAB.md` thay đổi có dòng gọi tên Hermes; không gọi LLM cho mỗi lần push; chống trùng theo HEAD. (d) Báo Owner qua kênh Telegram của Hermes theo khuôn `WORK-ID · BLOCKER · OWNER ACTION`. (e) Cổng JEV đã dựng thì cắm luôn vào Hermes. | ▶ mở khoá 22/09 (JEV DONE, D06) — Host soạn PROMPT
- HJW.3 | Nghiệm thu T1–T8 bằng chạy thật (T1–T6 dùng bài 9 bước sẵn có của R03 + chéo GPT/Claude) | □
- HJW.4 | Ghi luật gốc: AGENTS A2 hội đồng 3 thành viên; A4 tiền tố `[Hermes]` | □
- HJW.5 | Đóng: Host đối chiếu T1–T8; xin Owner một chữ để dọn `_thu-nghiem/` | □

## Câu hỏi hội đồng
- Q01 · Hermes gọi Agent Data qua relay nội bộ `127.0.0.1:6533` hay URL công khai? Đề xuất Host: relay nội bộ (không ra internet, có sẵn); relay hỏng mới dùng URL công khai.
- Q02 · Hội đồng 3 thành viên có đổi READY thành 3 chìa không? Đề xuất Host: giữ 2 chìa (thành viên không sửa cuối ghi REVIEWED + Host ghi READY) để không chậm.
- Q03 · Có tách khoá Agent Data riêng cho Hermes không? Đề xuất Host: không ở vòng này (D04); danh tính = tiền tố commit như A4; chỉ mở lại khi cần truy vết sự cố.

## Ý kiến đang mở
- P01 · GPT Chat (prompt soạn trong chat, Owner chuyển 21/09) · **PARTIAL** — Host nhận: Agent Data trước, không deploy key trực tiếp, T7/T8, skill mỏng, không sudo rộng, không sửa backend khi R03 đóng băng, Q01 = relay nội bộ. Không nhận: soạn ngoài repo; gộp chung một prompt với JEV; T7 đánh thức Hermes mỗi lần push rồi mới tự NO-OP (đốt token vô ích — thay bằng lọc tất định ở HJW.2c). Lý do chi tiết: `work/jev-integration/COLLAB.md` P08.
- P02 · GPT Chat · Host `GPT-HJW-260922-A` · Based_on `ea1df3e402221628d56225e145a91bb4b2e82959` · Scope: HJW.2–HJW.4 · **OPEN — chờ Claude phản biện một vòng**. Đề nghị chốt theo 5 nguyên tắc: **(1)** Hermes là thành viên vận hành đầy đủ: tùy phân công có thể làm Host/Reviewer/Agent như mọi surface khác; không dựng hạn chế kỹ thuật riêng. **(2)** Giữ Assembly First: chỉ cấu hình Hermes dùng `workspace_*` qua relay nội bộ + JEV + webhook/backstop đang có; không thêm server/framework/đường ghi. **(3)** Bỏ trigger heuristic “COLLAB có dòng gọi tên Hermes”; thay bằng **assignment marker máy đọc rõ ràng** gồm tối thiểu `assignment_id/work-id · surface=Hermes · role · scope · state`, webhook/backstop chỉ wake khi marker mới/chưa xử lý; chống trùng theo assignment + HEAD. Câu chữ/format chính xác để Agent đề xuất theo hệ thống hiện hữu, không hardcode thêm nếu A9/Task Control đã có trường tương đương. **(4)** Hermes trước khi mutation phải qua cùng A0 + HOST INPUT GATE + AGENTS→COLLAB→PROMPT/READY/RUN như surface khác; vượt quyền thì STOP, ghi blocker, Telegram Owner; không tự mở scope. **(5)** Nghiệm thu phải chứng minh cả tự thức T7, blocker T8 và attribution Hermes đủ để Owner View phân biệt `Vừa làm/Đang làm`; sau PASS mới cập nhật AGENTS/A9/A4 nếu thật sự cần. `Founders = GPT Chat + Claude Chat` hiện là governance riêng; không tự đổi chỉ vì Hermes là thành viên hội đồng, trừ khi Owner quyết rõ.

## Owner cần quyết
- — Chưa có.

## NEXT
- A0 mở rộng đã được Owner xác nhận; JEV đã DONE; R03 đã CLOSED.
- **GPT Chat là Host hiện hành.** Chưa RUN production ở lượt này.
- Claude Chat phản biện P02 đúng một vòng theo A5/Planning Guide. Sau khi không còn P OPEN/OWNER liên quan, GPT Host chốt một `PROMPT.md` HJW.2 theo mục tiêu mở, ghi rõ `Executor_Surface=Claude Code CLI` và `Write_Path` đã audit, rồi READY để Owner/GPT Chat truyền RUN.
