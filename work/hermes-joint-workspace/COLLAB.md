# COLLAB — Hermes Joint Workspace

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Mục tiêu: đưa Hermes vào workspace như một thành viên của hội đồng cùng GPT và Claude để cùng tham gia công việc theo lệnh điều hành.
- Nhiệm vụ/phạm vi: kết nối Hermes qua Agent Data đang có, nghiệm thu khả năng làm việc chung an toàn; không mở đường ghi thứ ba hay đưa tài khoản GitHub Owner lên VPS.
- Tiêu chí xong: Hermes đọc/ghi/chéo được theo cùng cơ chế đã audit, nghiệm thu T1–T6 đạt rồi mới cập nhật luật gốc về hội đồng 3 thành viên.
- Xác nhận User: **ĐÃ XÁC NHẬN** — Owner giao trực tiếp 2026-09-20; DROOT02 và D01–D04 của việc này.

Hội đồng: GPT · Claude · Hermes (Owner quyết 2026-09-20, ghi ở COLLAB gốc DROOT02). Trước mắt làm việc: GPT + Claude; Hermes vào khi HJW.3 PASS.
Host: Claude Chat · Host_ID: CLAUDE-HJW-260920-A · mở việc theo lệnh Owner 2026-09-20
HTML chính: `view.html`

## Dòng hiện hành
HJW | Hermes vào workspace như một thành viên hội đồng | việc 1/5 | DRAFT | NEXT: GPT Review | BLOCK: —

## Quyết định Owner
- D01 · 2026-09-20 · Mục tiêu: Hermes tham gia workspace đầy đủ như một thành viên. Được làm gì hay không là do lệnh điều hành, như GPT/Claude; không dựng rào kỹ thuật riêng cho Hermes.
- D02 · 2026-09-20 · Hội đồng gồm 3 thành viên: GPT · Claude · Hermes.
- D03 · 2026-09-20 · Kênh: Agent Data (`workspace_*`, cùng cửa Claude Code đang dùng) vì Hermes nằm trên VPS. Không đưa tài khoản GitHub của Owner lên VPS; không mở cửa ghi thứ ba (giữ D12).
- D04 · 2026-09-20 · Cách làm: tham gia · an toàn · tận dụng tối đa cái đang có · hạn chế xây mới · nhanh nhất, không sa đà.

## Kế hoạch
- HJW.1 | Mở việc: mục tiêu, hiện trạng, tiêu chí T1–T6 (`view.html`) | ▶ chờ GPT review
- HJW.2 | Nối — một PROMPT cho Claude Code, làm một lần: đo Hermes/relay/khoá → khai Agent Data vào `mcp_servers` của Hermes → thêm một đoạn nạp luật WS vào AGENTS.md riêng của Hermes | □ bắt đầu khi R03 CLOSED (không chạy song song lượt deploy cuối và giai đoạn đóng băng backend của R03)
- HJW.3 | Nghiệm thu T1–T6: bài 9 bước sẵn có của R03 + chéo GPT/Claude | □
- HJW.4 | Ghi luật gốc: AGENTS A2 hội đồng 3 thành viên; A4 tiền tố `[Hermes]` (gộp `[Claude Code]` đang chờ) | □
- HJW.5 | Đóng: Host đối chiếu T1–T6; xin Owner một chữ để dọn `_thu-nghiem/` | □

## Câu hỏi hội đồng
- Q01 · Hermes gọi Agent Data qua relay nội bộ `127.0.0.1:6533` hay URL công khai? Đề xuất Host: relay nội bộ (không ra internet, có sẵn); relay hỏng mới dùng URL công khai.
- Q02 · Hội đồng 3 thành viên có đổi READY thành 3 chìa không? Đề xuất Host: giữ 2 chìa (thành viên không sửa cuối ghi REVIEWED + Host ghi READY) để không chậm.
- Q03 · Có tách khoá Agent Data riêng cho Hermes không? Đề xuất Host: không ở vòng này (D04); danh tính = tiền tố commit như A4; chỉ mở lại khi cần truy vết sự cố.

## Ý kiến đang mở
- —

## Owner cần quyết
- — Chưa có.

## NEXT
- GPT đọc `AGENTS.md` → file này → `view.html`; tạo Pxx hoặc ghi `GPT REVIEWED · ACCEPT` vào mục Ý kiến đang mở, kèm trả lời Q01–Q03.
- Hết P OPEN và R03 CLOSED: Host soạn `PROMPT.md` trong thư mục này cho HJW.2.
