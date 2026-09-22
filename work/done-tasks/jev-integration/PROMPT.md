# PROMPT — JEV hậu kiểm cuối: đồng bộ skill mới + thử lại tự động + đồng hồ đếm dùng thật

RUN_ID: JEV-B2-FINAL-CLAUDECODE-20260922-01

- Host: **Claude Chat** · Host_ID `CLAUDE-JEV-B2-260922-A` (Host Bước 2, D10).
- Executor_Surface: **Claude Code CLI trên Mac của Owner**; `ssh contabo` (root VPS) được dùng ở Phần C.
- Write_Path: `workspace_*` cho mọi ghi repo. Cấm git native.
- Đọc trước: `AGENTS.md` → `work/jev-integration/COLLAB.md` (Trạng thái, D05–D10, KQ JEV-B1 / JEV-B2 / VERIFY-01 / VERIFY-02) → file này → `SKILL.md` → `CLIENT-ACCEPTANCE.md` (§D, §E, §F3, §H3).

## 0. Mục tiêu
1. `SKILL.md` mới (sha `916a1c80…`, commit `60fdb01`: “Luôn hỏi JEV … kể cả khi thấy đáp án rõ”, thêm “lọc”) có mặt ở mọi bản cài trên Mac; Claude Code và Codex **không lùi, không hỏi thừa**.
2. Kênh nhắc thường trực cho Claude Code, giống dòng Host đã thêm vào memory claude.ai cho Chat.
3. **Đồng hồ đếm lượt dùng JEV thật** (thực hiện D06): biết Jev có được dùng trong công việc hay không; 14 ngày không ai dùng thì Kuma báo đỏ.

## 1. Cấm / giới hạn
- Không đổi provider/model/version, GSM, path-secret, URL, tool contract. Không sửa đăng ký plugin ChatGPT, `~/.codex/config.toml`, skill trên claude.ai. Không đụng `work/hermes-joint-workspace/`.
- Log đếm **không được** chứa path-secret, `$request`/`$uri`/`$args`, hay nội dung `state`/`questions`.
- Được start/restart chính `jev-gw` và reload nginx sau `nginx -t` PASS; bless Config Guard **chỉ khi diff đúng bằng các dòng RUN này thêm** (như P10). Xoá/dừng/khôi phục khác = Owner quyết.
- Thất bại ⇒ DỪNG, giữ nguyên, ghi `KQ@JEV-B2-FINAL-CLAUDECODE-20260922-01 DỪNG` kèm lý do.

## 2. Cổng chỉ-đọc (FAIL ⇒ DỪNG trước mọi thay đổi)
1. READY khớp full SHA commit cuối chạm file này; read-gate `workspace_*` PASS.
2. Health JEV UP ≤15 phút; Config Guard CLEAN; `nginx -t` OK.
3. `SKILL.md` repo sha `916a1c80…`, description ≤200 ký tự (NFC).
4. Liệt kê bản skill trên Mac + sha: Codex user skill, `~/.claude/skills/jev-reference/`, bản claude.ai đồng bộ trong `~/.claude/skills/synced/…` (phải đã là bản mới vì claude.ai đã `NEW` ở VERIFY-02).
5. Health probe dùng User-Agent/đánh dấu gì; journald giữ log `jev-gw` được bao nhiêu ngày.

## 3. Phần A — đồng bộ + kênh nhắc
- A1. Codex user skill và `~/.claude/skills/jev-reference/SKILL.md` = `SKILL.md` repo tại commit READY; ghi sha trước/sau.
- A2. Thêm **đúng một dòng** vào cuối `~/.claude/CLAUDE.md` (cấp user; tạo file nếu chưa có; ghi sha trước/sau):
  `- Trước khi chốt các quyết định có lựa chọn, xếp hạng, phân loại hoặc lọc thông tin: tham khảo JEV (skill jev-reference) — kết quả JEV chỉ hỗ trợ, bạn tự quyết.`

## 4. Phần B — thử lại tự động (bước 5 của “Quy trình giữ không quên”)
- B1. Codex K1/K2 đúng cách lượt JEV-OPENAI-ACC. PASS: K1 gọi, không `model`, có `answers`; K2 không gọi.
- B2. Claude Code 10+10 đúng cách lượt JEV-B2 (mỗi ca một process `claude -p` mới, `--output-format stream-json`, cwd thư mục mẫu sạch, chỉ công cụ đọc + JEV, các MCP khác tắt bằng cờ). Lần này `~/.claude/CLAUDE.md` có dòng A2 — đó là cấu hình thật, giữ nguyên. Thêm 2 ca, ghi riêng:
  - X1 · `Hai bridge đều chạy được: bridge X strict hơn về Accept header, bridge Y stateless và tương thích rộng hơn với nhiều client. Cần phục vụ nhiều loại client khác nhau. Chọn bridge nào?`
  - X2 · `Nhóm 5 người đều dùng Slack hằng ngày và ít mở email. Gửi báo cáo tuần qua email hay qua Slack thì hợp hơn?`
- PASS: `POSITIVE_TRIGGER ≥8/10` (không lùi) · `FALSE_TRIGGER ≤2/10` · `MODEL_ARG_ABSENT` 100% · `ANSWERS` 100%; X1, X2 mục tiêu là gọi. `FALSE_TRIGGER >2/10` ⇒ DỪNG trước Phần C, báo Host; không tự sửa skill.

## 5. Phần C — đồng hồ đếm dùng thật (D06)
- C1. Chọn tín hiệu có sẵn chính xác nhất, theo thứ tự: (a) dòng log từng request của MCP SDK trong `jev-gw` (dạng “Processing request of type CallToolRequest”) khi nâng mức log bằng cờ/cấu hình có sẵn của `mcp-proxy`; (b) nếu không có (a): access log riêng cho location JEV với `log_format` chỉ gồm thời gian, status, method, User-Agent, request_length. Không tự viết server hay dịch vụ mới.
- C2. Tách lượt health probe khỏi lượt dùng thật (theo đánh dấu có sẵn của probe; chưa có thì cho probe một User-Agent riêng).
- C3. Mở rộng **đúng script health đang có**: mỗi lượt tính số lượt dùng thật 1/7/14 ngày, đẩy lên **Kuma monitor thứ hai “JEV dùng thật (14 ngày)”** theo pattern monitor #19. UP khi 14 ngày có ≥1 lượt thật (msg `real 1d/7d/14d = a/b/c`); DOWN khi đủ 14 ngày dữ liệu mà 0 lượt; chưa đủ 14 ngày thì UP, msg `đang tích luỹ từ <ngày>`.
- C4. Sau khi bật: một lượt gọi thật ⇒ bộ đếm tăng đúng 1; quét log/journal theo giá trị: 0 bản path-secret, không có nội dung `state`/`questions`. `nginx -t` + reload nếu có đổi; restart `jev-gw` nếu đổi mức log; health UP lại; Kuma #19 vẫn UP; bless Config Guard theo §1.

## 6. KQ + báo cáo
- Ghi một khối `## KQ — JEV-B2-FINAL-CLAUDECODE-20260922-01` cuối `COLLAB.md` qua `workspace_*`: sha skill trước/sau · dòng A2 · Codex K1/K2 · Claude Code theo khuôn §F3 + X1/X2 · tín hiệu đếm đã chọn · Kuma monitor mới (tên/số) · số `real` hiện tại · Config Guard.
- Dòng `KQ@JEV-B2-FINAL-CLAUDECODE-20260922-01 XONG|DỪNG`; báo Owner một dòng.
