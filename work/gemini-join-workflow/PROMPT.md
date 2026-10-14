# PROMPT — GJW-G1-ANTIGRAVITY-SELF-SETUP-20261014-01
RUN_ID: GJW-G1-ANTIGRAVITY-SELF-SETUP-20261014-01
Status: DRAFT — Reviewer Claude Chat đã sửa thẳng theo P03 (A6/DROOT53). GPT Host đặt READY đúng SHA commit cuối chạm tệp này; chưa READY ⇒ không chạy.
Task: work/gemini-join-workflow
Host: GPT Chat · Reviewer: Claude Chat · Executor: Antigravity (app hoặc `agy`) trên MacBook Owner, chạy bằng mô hình họ Gemini · Dự phòng: Claude Code CLI CHỈ cho từng mục BLOCKED_CAPABILITY · Automation_Level: AUTO0
Đọc repo: GitHub công khai, chỉ đọc. Ghi repo: chỉ qua gateway Incomex `fs_*`/`workspace_*` bằng danh tính Google riêng của bạn.

## MỤC TIÊU
Bạn là Google Antigravity/Gemini, EXECUTOR CHÍNH. Tự khảo sát và tự nối chính bạn vào repo, VPS MCP, KB và JEV bằng danh tính Google riêng, để từ G2 ngồi ghế Google trong hội đồng.
Owner 14/10/2026: «nguyên tắc là chúng ta đưa ra khuôn khổ và giao nó tự thực hiện. Cái gì không tự thực hiện được thì chúng ta mới hỗ trợ.» ⇒ Bạn tự làm mọi thứ nằm trong KHUÔN KHỔ dưới đây. Chỉ chuyển Claude Code phần có bằng chứng bạn không làm được.

## KHUÔN KHỔ QUYỀN — đọc trước lệnh đầu tiên
🟢 TỰ LÀM NGAY
- Đọc repo, tài liệu Google, cấu hình Antigravity trên Mac — chỉ metadata, không đọc/in giá trị bí mật.
- SSH vào VPS CHỈ ĐỂ ĐỌC và nhẹ: `nice`/`ionice`, không quét cả đĩa, không thử tải, không chiếm dòng `VPS-GHI` (DROOT54 d).
- Cấu hình của chính bạn trên Mac: sao lưu trước; THÊM mục mới, không sửa/xoá mục cũ; tệp chứa khoá `chmod 600`.
- Gọi `agy -p`, công cụ MCP chỉ đọc, KB, JEV.

🟡 TỰ LÀM KHI ĐỦ MỌI ĐIỀU KIỆN — thiếu một ⇒ không làm, ghi BLOCKED_CAPABILITY
- Tạo đúng MỘT danh tính cho ghế Google, theo thứ tự ưu tiên:
  (1) gateway có sẵn OAuth/đăng ký client cho MCP client ⇒ đăng nhập theo đường đó, KHÔNG đổi gì trên VPS;
  (2) nếu không: 1 secret mới trong GSM (tên rõ, không in) + đăng ký vào cơ chế khoá/profile CÓ SẴN của gateway qua đường chính thức (`incomex-config-apply-v0`/Config Guard). Điều kiện: dòng `VPS-GHI` ở COLLAB gốc là `trống` và lượt này đã giữ khoá đúng luật gốc; không sửa mã; không restart/reload/recreate container, nginx hay service; đèn Guard trước/sau không thêm đỏ; có rollback; trả khoá cùng lượt.
- Ghi repo: chỉ bằng danh tính Google vừa có, qua `fs_*`/`workspace_*`, có expected_version.

🔴 KHÔNG LÀM, kể cả khi có quyền kỹ thuật
- Xoá/dời tệp; stop/restart/reload service, container, nginx, cron, systemd; sửa Compose hay mã nguồn; ghi PG/Directus; đụng Guard/Kuma/Telegram/backup Drive.
- Ghi repo bằng SSH, git trên VPS, deploy key, hay khoá/danh tính của ghế khác (sai tác giả); `git push` từ Mac.
- In/dán bí mật vào chat, log, repo, tệp công khai.
- Gọi API trả phí; mở cổng public; webhook/email ingress; dịch vụ nền/LaunchAgent/polling (thuộc G3).
- Đụng việc khác: HJW (cờ courier spike P313 còn mở), Graph, VPSC, TQT.
- Chạy lượt này bằng mô hình không thuộc họ Gemini; chế độ bỏ qua quyền (`--yolo`, dangerously-skip-permissions).

Bảo vệ trước khi SSH: đặt chính sách lệnh terminal của Antigravity sao cho mọi lệnh 🔴 bị chặn hoặc phải hỏi; ghi lại đã đặt gì vào KQ.

## S0 — TỰ KHẢO SÁT (chỉ đọc, fail-closed)
1. Đọc AGENTS.md, README.md, work/README.md, COLLAB.md của việc này (§0, Bảng, ô 1–3, P01–P03) và đoạn HJW về dòng yêu cầu đưa thư (COURIER_REQUEST). Kiểm có READY đúng SHA tệp này; không có ⇒ dừng.
2. Bề mặt: Antigravity app/`agy` — phiên bản, cách đăng nhập, gói + hạn mức, danh sách mô hình (`agy models` nếu có), mô hình đang chạy chính lượt này; Argon có hay không (chỉ ghi khi đo được).
3. SSH: alias trong `~/.ssh/config`, user, dấu vân tay khoá đang dùng; khoá đó có dùng chung với Claude Code/Owner không; user có phải root không. Không đổi cấu hình SSH.
4. Cấu hình cũ: 4 tệp `~/.gemini` (`config/mcp_config.json`, `antigravity-cli/mcp_config.json`, `settings.json`, `antigravity.json`) và `.agents/mcp_config.json` nếu có — chỉ metadata: tên server, kiểu xác thực, còn công cụ nào đọc chúng. Lưu ý `config/mcp_config.json` vừa là tệp cũ vừa là tệp dùng chung của IDE + `agy`: được THÊM mục, không sửa/xoá mục cũ. Gemini CLI đã ngừng cho tài khoản cá nhân từ 18/06/2026, còn đường Enterprise/API.
5. Gateway: mỗi client hiện có danh tính riêng thế nào (claude-mcp, route ChatGPT, Agent Gateway/Hermes, KB, JEV); có OAuth/đăng ký client không; có cơ chế THÊM danh tính mà không sửa mã/không restart không. Không có đường nào ⇒ BLOCKED_CAPABILITY kèm delta nhỏ nhất.
6. Ma trận bằng chứng: bề mặt · máy · phiên bản · mô hình · đăng nhập · MCP transport · tool bind được · repo/KB/JEV · chiều vào (Hermes/VPS → Google) · chiều ra (Google → MCP) · hạn mức — mỗi ô một mức VERIFIED_LOCAL | DOC_ONLY | UNKNOWN | UNAVAILABLE.
7. Đèn: đọc `logs/bang-den.json` (gốc code) hoặc `vps_status` trước mọi bước có ghi.

## S1 — TỰ NỐI (đúng khuôn khổ)
1. Danh tính Google (🟡). Có ⇒ THÊM mục MCP mới vào `~/.gemini/config/mcp_config.json` (tên mới, `serverUrl`, khoá đọc từ GSM, không in); mục cũ khoá chết giữ nguyên, có cờ tắt thì tắt, không xoá.
2. Chứng minh từng cổng qua chính bề mặt Google: `fs_read` AGENTS.md · `workspace_read` một tệp · KB search · JEV `evaluate` — ghi kết quả hay lỗi thật.
3. `agy -p "<một câu>" --output-format json` (hoặc stream-json): chứng minh status, mã phiên, usage, mô hình họ Gemini.
4. Ghi P04 (kết quả) vào COLLAB việc này bằng danh tính Google — chính là bằng chứng ghi thật. Thử âm: ghi ngoài `work/gemini-join-workflow/` ⇒ phải bị từ chối; gateway không có phạm vi theo đường dẫn ⇒ ghi UNAVAILABLE + đề xuất, không tính là trượt.
5. Remote Control: chỉ khảo sát, chưa bật (G3).

## GHI TRẠNG THÁI — DROOT31/50/54
- Lúc bắt đầu chưa có đường ghi riêng ⇒ in khối `STARTED` (RUN_ID, giờ UTC, executor, mô hình) trong chat; Owner chuyển Host GPT ghi hộ. Có đường ghi rồi thì tự ghi tiến độ/KQ ngay dưới P04.
- Nhánh 🟡(2) cần khoá `VPS-GHI` mà chưa có đường ghi ⇒ in đúng MỘT dòng xin khoá trong chat; chỉ làm sau khi Host ghi khoá cho RUN này. Không ngồi chờ: kết thúc lượt bằng KQ DỪNG + NEXT_TRIGGER nếu chưa có khoá.
- Hết mỗi bước S0/S1: một dòng `<RUN_ID> · bước k/N · <đã xong gì> · <UTC> · dự kiến xong <UTC>`.
- Đồ lượt này có thể tạo (DROOT54 c): bản sao lưu cấu hình Mac (giữ, ghi đường dẫn) · thư mục tạm `$TMPDIR/gjw-g1-*` (xoá trước KQ) · phiên `agy -p` (kết thúc ngay) · trên VPS chỉ đúng 1 mục danh tính nếu nhánh 🟡(2) chạy (giữ, có rollback). Không tiến trình nền, không cổng mở.
- Kết thúc: `KQ@GJW-G1-ANTIGRAVITY-SELF-SETUP-20261014-01 XONG|DỪNG` · `Dọn: <đã gỡ>/<đã tạo> · còn lại: …` · trả `VPS-GHI: trống` nếu đã giữ · 0 tiến trình nền.

## KẾT QUẢ (P04)
Ma trận S0.6 · SSH (vân tay, user, dùng chung hay riêng) · chính sách terminal đã đặt · trước/sau cấu hình (hash, không bí mật) · mô hình + kiểu đăng nhập + hạn mức · kết quả repo/KB/JEV/`agy` · thử âm · đèn trước/sau · danh sách BLOCKED_CAPABILITY (mỗi mục: bằng chứng · delta nhỏ nhất · việc gợi ý cho Claude Code).
XONG khi: S1.2 đủ 4 cổng thật + S1.3 đạt + P04 ghi bằng danh tính Google + đèn không thêm đỏ. Thiếu ⇒ DỪNG, giữ phần đã đạt, không phá gì.
Không mở G2/G3, không thay Hermes, không bật tự động. Xong thì trả Host GPT nghiệm thu; Claude Chat (khác hãng) rà KQ.
