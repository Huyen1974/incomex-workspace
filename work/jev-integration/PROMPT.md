# PROMPT — JEV.B2 · Claude (Chat · Cowork · Claude Code) · RUN_ID `JEV-B2-CLAUDE-20260922-01`

- Host Bước 2: **Claude Chat** · Host_ID `CLAUDE-JEV-B2-260922-A` (Owner giao 2026-09-22). Host việc JEV nói chung vẫn là GPT Chat.
- Executor_Surface: **Claude Code CLI trên Mac của Owner**. SSH root VPS (`ssh contabo`) chỉ để ĐỌC/kiểm; lượt này không sửa gì trên VPS.
- Write_Path: `workspace_*` cho mọi ghi repo. Cấm git native.
- Đọc trước: `AGENTS.md` → `work/jev-integration/COLLAB.md` (A0, D01–D10, P15–P16, KQ JEV-OPENAI-ACC) → file này → `SKILL.md` → `CLIENT-ACCEPTANCE.md` (§0, §D, §E, §F3, §H).

## 0. Mục tiêu lượt này
Claude Chat, Cowork và Claude Code tham khảo JEV **tự nhiên** như phía OpenAI đã đạt: gặp quyết định có biên thì tự gọi `evaluate`; việc không hợp thì không gọi; không truyền `model`; có `answers`; JEV chỉ là tham khảo. Đồng thời đưa `SKILL.md` mới (description ≤200 ký tự, dùng chung hai hãng) về các bản đã cài phía OpenAI và chứng minh Codex không lùi.

## 1. Cấm / giới hạn
- Không sửa VPS, `jev-gw`, nginx, GSM, provider/model/version, Config Guard.
- Không đổi đăng ký plugin/app ChatGPT; không sửa `~/.codex/config.toml` (cờ thử chỉ truyền bằng `-c`).
- Không đụng `work/hermes-joint-workspace/` và luật nền.
- Chỉ ghi đè đúng các file skill nêu ở §3 A1; ghi sha trước/sau vào KQ. Không xoá/ghi đè cấu hình khác.
- URL JEV là secret: chỉ đi clipboard/connector/cấu hình client; không in ra màn hình, không vào repo/log/KQ; so bằng sha256.
- Thất bại ⇒ DỪNG, giữ nguyên, ghi `KQ@JEV-B2-CLAUDE-20260922-01 DỪNG` kèm lý do.

## 2. Cổng chỉ-đọc (FAIL ⇒ DỪNG trước mọi thay đổi)
1. READY trong `COLLAB.md` khớp full SHA commit cuối chạm file này; read-gate `workspace_*` PASS.
2. Health JEV: kết quả health gần nhất ≤15 phút là UP (journal `jev-gw-health` hoặc Kuma #19) — chỉ đọc.
3. `SKILL.md` repo: frontmatter hợp lệ, `name: jev-reference`, description ≤200 ký tự (đếm NFC).
4. Liệt kê các bản skill đang cài trên Mac + sha256: Codex user skill `~/.agents/skills/jev-reference/SKILL.md`; bản trong thư mục plugin ChatGPT (nếu có); `~/.claude/skills/` (nếu có).
5. `claude --version`; `claude mcp list` (chỉ tên server, không in URL); `~/.claude/CLAUDE.md` có nhắc JEV không (ghi có/không — để biết phép thử có sạch).

## 3. Phần A — chuẩn bị (tự làm)
- A1. Đồng bộ skill = đúng nội dung `SKILL.md` repo tại commit READY: Codex user skill; bản trong thư mục plugin ChatGPT trên Mac (nếu có); tạo `~/.claude/skills/jev-reference/SKILL.md`.
- A2. Codex không lùi: chạy lại K1 (natural) + K2 (negative) của `CLIENT-ACCEPTANCE.md` đúng cách lượt JEV-OPENAI-ACC (`codex exec` phiên mới, `--sandbox read-only`, cờ `-c` như cũ). PASS: K1 có call `evaluate`, không có khoá `model`, có `answers`; K2 không call.
- A3. Đóng gói `~/Desktop/jev-reference.zip` = thư mục `jev-reference/` chứa `SKILL.md` (để Owner upload lên claude.ai).
- A4. Chép URL JEV v2 vào clipboard Mac (lấy từ GSM như lượt trước; không in).
- A5. **DỪNG CHỜ OWNER** — báo đúng một dòng: `Chuẩn bị xong · Codex K1/K2 <PASS|FAIL> · zip trên Desktop · URL trong clipboard · mời anh cắm trên claude.ai rồi nhắn "đã cắm"`. Không làm Phần B trước khi Owner nhắn "đã cắm".

## 4. Phần B — sau khi Owner nhắn "đã cắm"
- B1. Claude Code thấy connector tài khoản `JEV Reference` trong `claude mcp list` ⇒ dùng. Không thấy ⇒ `claude mcp add --transport http --scope user jev-reference <URL>`, URL lấy từ GSM qua pipe (D10); kiểm file cấu hình chỉ user đọc được. Ghi cách đã dùng.
- B2. Smoke CC0/CC1/CC2 theo §H3. CC1 phải tự gọi; CC2 không gọi. CC1 không gọi mà CC0 gọi ⇒ `SKILL_NOT_TRIGGERED` ⇒ DỪNG, không tự sửa `SKILL.md`.
- B3. 10+10 theo §H3: mỗi ca một process `claude -p` mới, `--output-format stream-json`; cwd là thư mục mẫu sạch (3 README.md, không `CLAUDE.md`); chỉ cho công cụ đọc + tool JEV (không Edit/Write/Bash ghi; MCP có tool ghi tắt bằng cờ dòng lệnh trong lượt thử, không sửa config); prompt đúng bản đã điền dữ liệu của lượt Codex, có tiền tố “Không sửa file.”. Hash cây thư mục trước/sau mỗi ca.
- B4. Chấm từ trace, không tin lời model kể: ca nào có `tool_use` JEV `evaluate`; arguments quét đệ quy không có khoá `model`; tool result có `answers`. Ghi thêm model trả về (telemetry) và số lượt gọi mỗi ca.
- B5. Ghi KQ vào `COLLAB.md` qua `workspace_*` theo khuôn §F3 cho Claude Code, kèm dòng Codex K1/K2 re-smoke và cách B1 đã dùng. Claude Chat/Cowork do Host chấm; Agent không chấm thay.

## 5. PASS / báo cáo
- Codex K1/K2 PASS; Claude Code `POSITIVE_TRIGGER ≥7/10`, `FALSE_TRIGGER ≤2/10`, `MODEL_ARG_ABSENT` 100%, `ANSWERS` 100% trên call thành công.
- Kết thúc: `KQ@JEV-B2-CLAUDE-20260922-01 XONG|DỪNG` trong `COLLAB.md`; báo Owner một dòng.
