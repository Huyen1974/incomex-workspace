# PROMPT — GJW-G1C-JEV-MAC-G2-COUNCIL-20261014-01
RUN_ID: GJW-G1C-JEV-MAC-G2-COUNCIL-20261014-01
Status: DRAFT · CHƯA READY/CHƯA RUN. Claude Chat Reviewer đã sửa thẳng S1 theo P12 (A6/DROOT53) và ACCEPT đúng SHA; GPT Host phát READY. Không chạy trước READY.
Task: work/gemini-join-workflow · Host GPT Chat · Reviewer Claude Chat · Executor Claude Code CLI Mac (hỗ trợ kỹ thuật); Gemini qua agy là ghế Google độc lập · AUTO0.
Write_Path: GitHub workspace chỉ bằng gateway fs_*/workspace_* có expected_version; config Mac chỉ local chuẩn + backup; VPS: 0 ghi, 0 restart, không lấy VPS-GHI (JEV dùng path-secret chung đã có).

## MỤC TIÊU — MỘT LƯỢT, KHÔNG LÀM LẠI G1B
Kết quả giữ nguyên: google-main đã xác thực và ghi P10, agent-data/KB đọc-ghi PASS, 6 danh tính sống, agy đã login Keychain và ghim Gemini 3.8 Flash High, VPS-GHI đã trả. Không đổi agent-data/secret GSM đang sống. Chủ việc muốn ưu tiên Gemini tham gia hội đồng, tạm hoãn Kuma/biên nhận Telegram R4. Hai việc kỹ thuật còn sát đích: (1) nối JEV cho Google bằng path-secret JEV chung như Claude/GPT đang dùng — JEV là tài nguyên chung, không phải danh tính ghế (Owner: «sử dụng chung các tài nguyên như tham khảo Jev»); (2) chống drift của cấu hình MCP trên Mac. Cuối cùng chính Gemini đưa ý kiến phản biện G3, ghi P riêng qua google-main.

## CỔNG VÀ NHỊP (AGENTS A6, DROOT30/31/48/54)
Đọc AGENTS.md → COLLAB gốc (VPS-GHI) → work/gemini-join-workflow/COLLAB.md (§0, P09–P11) → PROMPT này. Verify last-touch SHA = Reviewer ACCEPT = GPT READY, không STOP, không STARTED task chưa KQ. Read-gate PASS mới ghi STARTED@RUN_ID bằng gateway. Mỗi bước ghi một dòng tiến độ và cuối lượt KQ XONG hoặc DỪNG. Không giữ phiên/khóa chờ giờ, không chạm task khác.

| Bước | Ai | Điểm chốt / SLA | Bằng chứng và khi lỗi |
|---|---|---|---|
| S0 read-gate | Claude Code | một lượt ≤5 phút | READY, VPS-GHI, JEV và Mac config đã có; fail báo Host + KQ |
| S1 JEV Google | Claude Code | ≤10 phút, chỉ Mac | path-secret chung từ GSM vào config agy 0600; Gemini gọi evaluate thật; không đạt ghi GAP |
| S2 Mac guard | Claude Code | ≤10 phút | hash, quyền 0600, backup, preflight lúc agy được gọi; GAP minh bạch nếu chưa cưỡng chế |
| S3 Hội đồng Google | chính Gemini qua agy | ≤15 phút | Gemini phản biện độc lập, P tự ghi tác giả google-main; không đạt không tính ghế |
| S4 post & dọn | Claude Code | ≤10 phút | Điều 30/31 theo footprint, KQ, rollback, 0 tiến trình/khóa; PARTIAL nêu nợ |

## S1 · JEV — dùng chung như Claude/GPT, 0 thay đổi VPS
- Sự thật: cổng `jev-gw` (mcp-proxy named server) chỉ có MỘT path-secret `jev-mcp-path-secret` trong GSM; connector Claude, GPT và Claude Code trên Mac đều dùng nó; log JEV không ghi danh tính client. Danh tính ghế của Google (ghi repo/VPS) đã riêng = `google-main`. ⇒ KHÔNG tạo khoá JEV riêng, KHÔNG sửa jev-gw/mcp-proxy/key-fetch, KHÔNG restart, KHÔNG lấy VPS-GHI.
- Đọc `jev-mcp-path-secret` từ GSM đúng cách Claude Code vẫn đọc trên Mac (không in). Thêm server JEV (đúng URL `/jev-mcp/<secret>/mcp` mà connector Claude/GPT đang dùng) vào `~/.gemini/config/mcp_config.json`: sao lưu trước, 0600, giữ nguyên mục agent-data/KB đã đạt; `agy mcp list` thấy JEV.
- Chính Gemini gọi `evaluate` một câu hữu hạn qua `agy -p` (tool discovery thật, không bịa tham số), ghi mã `gen-dec-…`. Lỗi ⇒ ghi lỗi thật + GAP, vẫn làm S2/S3. Khoá JEV riêng từng ghế chỉ làm khi Owner yêu cầu (việc khác).

## S2 · Bảo vệ cấu hình Antigravity trên Mac
- Không dời/xóa cấu hình, không in token/SSH key, không tạo service/cron/LaunchAgent, không bật Turbo/bypass permission. Giữ config agent-data/KB đã đạt.
- So lại agy mcp list, Keychain login/model, hash của ~/.gemini/config/mcp_config.json, quyền 0600 và backup INDEX của G1B. Ưu tiên hook/preflight native đã có để **mỗi lần gọi agy trong workflow** xác minh file/config quan trọng và từ chối nếu drift; nếu thiếu dùng wrapper nhỏ nhất có quản lý và rollback. Ghi rõ giới hạn phạm vi: preflight lúc gọi ≠ giám sát 24/7. Không âm thầm sửa config lệch.

## S3 · Một lượt Hội đồng thực của google-main
- Claude Code chỉ kích hoạt CLI chính thức: agy -p theo mô hình thuộc Gemini, trỏ P11 và C3/G3 trong COLLAB task. Gemini tự đọc SSOT và phản biện độc lập hướng gọi vào CLI/email, Browser Subagent Chrome và ba rủi ro trước khi dùng làm courier; tham khảo JEV nếu S1 PASS, nếu chưa thì nêu GAP. Không truy cập HJW runtime, không điều khiển Chrome thật (để G3).
- Chính Gemini viết P tiếp theo trong task, ghi model, UTC, phân tích và JEV call/result hoặc GAP, qua workspace gateway với danh tính google-main và expected_version. Chứng minh commit Git author gemini-agy [auth:google-main] + JSON agy output thật. Claude Code không viết thay Google. Đây là thử ghế Google có nội dung khác hãng; Host nghiệm thu rồi mới công nhận G2.

## S4 · Bảo vệ, kết quả, trả máy
- Kiểm Điều 30 (JEV qua Google PASS + repo/KB/6 identity vẫn PASS, sai key bị chặn), Điều 31 (Guard/Config trước-sau, Mac preflight), self-check và rollback trên footprint thật. Đèn #21/#22 từ trước hoặc biên nhận Telegram R4 thiếu ⇒ ghi PARTIAL rõ, KHÔNG tuyên PASS giả hoặc làm Kuma ở task này (Owner hoãn). Nếu có thể phát receipt qua đúng cổng hiện hữu thì ghi message_id; không phát bằng đường bypass.
- Ghi P/KQ, số lần restart, paths/hashes nhưng không secrets, NEXT_TRIGGER một dòng. Dọn đồ chính RUN tạo; lượt này 0 ghi VPS nên không giữ VPS-GHI. Nếu Gemini P riêng có author/model/công việc thật thì đánh dấu G2-CANARY PASS (dù JEV còn GAP), Host quyết công nhận ghế; G3 chưa chạy. Không tự sửa AGENTS A9 — alias UI do Founders xử lý, không chặn thử hội đồng.
