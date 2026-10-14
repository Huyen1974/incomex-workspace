# PROMPT — GJW-G1C-JEV-MAC-G2-COUNCIL-20261014-01
RUN_ID: GJW-G1C-JEV-MAC-G2-COUNCIL-20261014-01
Status: DRAFT · CHƯA READY/CHƯA RUN. Claude Chat Reviewer rà một lượt và ACCEPT đúng SHA; GPT Host phát READY. Không chạy trước READY.
Task: work/gemini-join-workflow · Host GPT Chat · Reviewer Claude Chat · Executor Claude Code CLI Mac (hỗ trợ kỹ thuật); Gemini qua agy là ghế Google độc lập · AUTO0.
Write_Path: GitHub workspace chỉ bằng gateway fs_*/workspace_* có expected_version; config Mac chỉ local chuẩn + backup; VPS JEV chỉ bằng DOT/script-wrapper quản lý và GSM/Config Guard dưới VPS-GHI.

## MỤC TIÊU — MỘT LƯỢT, KHÔNG LÀM LẠI G1B
Kết quả giữ nguyên: google-main đã xác thực và ghi P10, agent-data/KB đọc-ghi PASS, 6 danh tính sống, agy đã login Keychain và ghim Gemini 3.8 Flash High, VPS-GHI đã trả. Không đổi agent-data/secret GSM đang sống. Chủ việc muốn ưu tiên Gemini tham gia hội đồng, tạm hoãn Kuma/biên nhận Telegram R4. Hai việc kỹ thuật còn sát đích: (1) tạo đường JEV riêng cho Google, không mượn secret chung; (2) chống drift của cấu hình MCP trên Mac. Cuối cùng chính Gemini đưa ý kiến phản biện G3, ghi P riêng qua google-main.

## CỔNG VÀ NHỊP (AGENTS A6, DROOT30/31/48/54)
Đọc AGENTS.md → COLLAB gốc (VPS-GHI) → work/gemini-join-workflow/COLLAB.md (§0, P09–P11) → PROMPT này. Verify last-touch SHA = Reviewer ACCEPT = GPT READY, không STOP, không STARTED task chưa KQ. Read-gate PASS mới ghi STARTED@RUN_ID bằng gateway. Mỗi bước ghi một dòng tiến độ và cuối lượt KQ XONG hoặc DỪNG. Không giữ phiên/khóa chờ giờ, không chạm task khác.

| Bước | Ai | Điểm chốt / SLA | Bằng chứng và khi lỗi |
|---|---|---|---|
| S0 read-gate | Claude Code | một lượt ≤5 phút | READY, VPS-GHI, JEV và Mac config đã có; fail báo Host + KQ |
| S1 JEV Google | Claude Code | một lượt ≤25 phút, không chờ lock | credential độc lập, tool evaluate thật, client cũ còn PASS; không đạt ghi GAP |
| S2 Mac guard | Claude Code | ≤10 phút | hash, quyền 0600, backup, preflight lúc agy được gọi; GAP minh bạch nếu chưa cưỡng chế |
| S3 Hội đồng Google | chính Gemini qua agy | ≤15 phút | Gemini phản biện độc lập, P tự ghi tác giả google-main; không đạt không tính ghế |
| S4 post & dọn | Claude Code | ≤10 phút | Điều 30/31 theo footprint, KQ, rollback, 0 tiến trình/khóa; PARTIAL nêu nợ |

## S1 · JEV — một thẻ riêng, dùng máy chủ sẵn có
- S0 đo nhẹ endpoint JEV hiện hữu: jev-gw + jev-gw-key-fetch + mcp-proxy named-server. Không tạo JEV service thứ hai. Ưu tiên cấu hình thêm một named-server/path-secret chỉ cho Google, lấy từ GSM, giữ credential legacy nguyên trạng. Nếu thiếu hỗ trợ cấu hình, chỉ sửa đúng chỗ trong key-fetch hiện có bằng DOT/script-wrapper đã quản lý, có dry-run/verify/rollback + backup. Không dùng chung/lộ khóa JEV đang cấp cho ghế khác.
- Trước mutation VPS: xác nhận VPS-GHI trống theo root mới nhất, lấy đúng khóa qua gateway CAS, Guard pre, snapshot known-good. Dừng nếu lock bận, làm phần Mac/G2 có thể làm rồi ghi KQ DỪNG; không giữ RUN đợi. Chỉ restart riêng jev-gw tối đa một lần **nếu thật sự cần** (Owner Q02 đã chấp thuận có điều kiện), không restart agent-data/PG/nginx/Graph/HJW hay bất kỳ service khác.
- Thử legacy JEV trước/sau, Google riêng PASS, key sai bị từ chối. Kết nối MCP JEV vào config agy thật trên Mac qua đúng transport, backup/0600. Dùng tool discovery/schema thật để gọi JEV evaluate một câu hỏi hữu hạn (ví dụ ưu tiên CLI/email/Chrome cho G3) và ghi mã biên nhận/kết quả. Không bịa tham số. Nhả VPS-GHI ngay khi xong. Nếu kỹ thuật không cho phép thêm secret riêng qua đúng đường quản lý: JEV = GAP, không phá máy, tiếp tục S2/S3 và nêu delta nhỏ nhất.

## S2 · Bảo vệ cấu hình Antigravity trên Mac
- Không dời/xóa cấu hình, không in token/SSH key, không tạo service/cron/LaunchAgent, không bật Turbo/bypass permission. Giữ config agent-data/KB đã đạt.
- So lại agy mcp list, Keychain login/model, hash của ~/.gemini/config/mcp_config.json, quyền 0600 và backup INDEX của G1B. Ưu tiên hook/preflight native đã có để **mỗi lần gọi agy trong workflow** xác minh file/config quan trọng và từ chối nếu drift; nếu thiếu dùng wrapper nhỏ nhất có quản lý và rollback. Ghi rõ giới hạn phạm vi: preflight lúc gọi ≠ giám sát 24/7. Không âm thầm sửa config lệch.

## S3 · Một lượt Hội đồng thực của google-main
- Claude Code chỉ kích hoạt CLI chính thức: agy -p theo mô hình thuộc Gemini, trỏ P11 và C3/G3 trong COLLAB task. Gemini tự đọc SSOT và phản biện độc lập hướng gọi vào CLI/email, Browser Subagent Chrome và ba rủi ro trước khi dùng làm courier; tham khảo JEV nếu S1 PASS, nếu chưa thì nêu GAP. Không truy cập HJW runtime, không điều khiển Chrome thật (để G3).
- Chính Gemini viết P tiếp theo trong task, ghi model, UTC, phân tích và JEV call/result hoặc GAP, qua workspace gateway với danh tính google-main và expected_version. Chứng minh commit Git author gemini-agy [auth:google-main] + JSON agy output thật. Claude Code không viết thay Google. Đây là thử ghế Google có nội dung khác hãng; Host nghiệm thu rồi mới công nhận G2.

## S4 · Bảo vệ, kết quả, trả máy
- Kiểm Điều 30 (JEV old/new + repo/KB/6 identity vẫn PASS, sai key bị chặn), Điều 31 (Guard/Config trước-sau, Mac preflight), self-check và rollback trên footprint thật. Đèn #21/#22 từ trước hoặc biên nhận Telegram R4 thiếu ⇒ ghi PARTIAL rõ, KHÔNG tuyên PASS giả hoặc làm Kuma ở task này (Owner hoãn). Nếu có thể phát receipt qua đúng cổng hiện hữu thì ghi message_id; không phát bằng đường bypass.
- Ghi P/KQ, số lần restart, paths/hashes nhưng không secrets, NEXT_TRIGGER một dòng. Dọn đồ chính RUN tạo, trả VPS-GHI cùng lượt. Nếu Gemini P riêng có author/model/công việc thật thì đánh dấu G2-CANARY PASS (dù JEV còn GAP), Host quyết công nhận ghế; G3 chưa chạy. Không tự sửa AGENTS A9 — alias UI do Founders xử lý, không chặn thử hội đồng.
