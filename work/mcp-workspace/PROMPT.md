# PROMPT — MCPW R2 · MÁY NHẬN RA AI ĐANG LÀM + HERMES ĐỦ THÀNH VIÊN

RUN_ID: MCPW-R2-PRESENCE-HERMES-20261001-01
Host: GPT Chat · GPT-MCPW-250925-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: `work/mcp-workspace/COLLAB.md` qua `workspace_*` profile `claude-code`.
Runtime: VPS1 production + Mac Owner.
STATUS: chỉ chạy khi READY Host trỏ đúng commit cuối chạm PROMPT này và gate §2 PASS.
PROMPT B2B cũ (`MCPW-B2B-LIFECYCLE-REST-20261001-01`) đã KQ DỪNG, superseded — không chạy lại.

## 0. Mục tiêu (Owner 01/10) — chỉ cái này

Có hữu hạn 5 ông làm việc: Claude Code · Codex · GPT Chat · Claude Chat · Hermes. Ông nào vào làm, máy tự nhận ra và ghi lại; không ông nào làm chui. Máy tự bắt, hoặc nhắc agent làm đúng.

Đúng 4 việc (COLLAB §0.3):
1. Claude Code + Codex + SSH — biết bắt đầu · đang làm · kết thúc; gắn đúng việc/RUN.
2. Sổ chung trên VPS — 5 ông cùng một sổ; chỉ ghi, không chặn.
3. Owner View — mỗi việc: ai · từ lúc nào · trạng thái · cảnh báo.
4. Hermes — ghi ý kiến vào việc được giao · vào sổ · đổi config ngoài lượt bị phát hiện.

## 1. Không làm (scope cứng)

NEXT/Bảng giao việc · scoped lease/fencing · bất kỳ DENY nào · REST legacy enforcement · Directus · chuyển writer sang khoá riêng · DNS · `work/vps1-up-grade` · G5/S1/G6/G7 · Hermes AUTO · rebaseline drift của task khác (trừ đúng mục §5 nêu).
Không dùng trạng thái VPSUP làm gate. Không có chờ theo giờ. Tối đa 1 restart/recreate agent-data. Không restart claude-mcp/Directus/nginx.

## 2. START gate — ngắn

1. READY Host = commit cuối chạm PROMPT này; không có STARTED/KQ/STOP_REQUESTED/HOLD mới cho RUN này.
2. Không RUN khác đang STARTED mà mutation cùng tài nguyên: agent-data source/config/image · `nuxt-repo/scripts/hvu-b2/` (lane MMIM) · runtime Hermes/HJW. Có ⇒ chờ đúng RUN đó có KQ, không chờ giờ.
3. agent-data/claude-mcp/nginx healthy; `legacy_master=enforce` (B2A) giữ nguyên.
4. Có lệnh rollback cụ thể trước mutation đầu.
PASS ⇒ ghi `STARTED@MCPW-R2-PRESENCE-HERMES-20261001-01 <UTC> · executor=Claude Code CLI`. DROOT30 trước mutation production đầu tiên.

## 3. Việc 1 — Claude Code + Codex + SSH

**Claude Code (hook chính thức của version đang cài):** `SessionStart` · `UserPromptSubmit` · `PreToolUse` · `PostToolUse` · `Stop` · `SessionEnd`.
- Handler: script nhỏ trên Mac gửi sự kiện tối thiểu về agent-data bằng credential riêng `claude-code` (đọc từ chỗ đã có, 0600; không in). Payload chỉ gồm: `surface · session_id · event · event_id · ts · tool_name · work_id · RUN_ID · ssh=yes/no`. `work_id`/`RUN_ID` trích tại Mac bằng regex từ tool_input (`work/<id>/`, chuỗi RUN_ID). **Không gửi prompt, nội dung, output, secret, IP.**
- Timeout ≤2 s; lỗi mạng không được làm hỏng phiên (đệm file cục bộ, gửi lại sau).
- Đặt hook: managed settings nếu Owner gõ mật khẩu Mac 1 lần; không được thì user settings + ghi residual. **Chốt thật nằm ở VPS:** profile `claude-code`/`codex` có hoạt động qua cổng MCP hoặc SSH mà không có phiên hook tương ứng ⇒ `HOOK_MISSING` (vàng).
- **Nhắc quên KQ:** `Stop` hook hỏi sổ; nếu phiên đã gắn RUN (có `STARTED@<RUN_ID>`) mà chưa có `KQ@<RUN_ID>` ⇒ trả lời nhắc **đúng 1 lần/phiên** (dùng `stop_hook_active` chống lặp). Phiên không gắn RUN thì không nhắc.

**Codex:** đo version CLI/Desktop thật. Có hook/notify chính thức thì dùng cùng khuôn trên. Sửa config Codex phải smoke Codex vẫn chạy + rollback đúng byte (Codex đang được dùng). Thiếu chức năng ⇒ residual; hoạt động của Codex vẫn hiện qua `HOOK_MISSING`. Không dựng framework/monkeypatch.

**SSH:** VPS đọc dòng `Accepted publickey` của sshd (journald). Ghép với sự kiện hook có `ssh=yes` trong ±60 s ⇒ gán đúng phiên. Không ghép được ⇒ `SSH_UNKNOWN` (vàng), không đoán.

## 4. Việc 2 — Sổ chung trên VPS

- Tái dùng mã sổ đã test của B2B (`/opt/incomex/work/mcp-workspace/MCPW-B2B-LIFECYCLE-REST-20261001/stage/` — `lifecycle.py` trên `queue.sqlite`, WAL/FULL/BEGIN IMMEDIATE). Chế độ `audit`; nhánh `enforce` để tắt. **Không mang sang** writer-map REST, REST enforcement, Directus, NEXT, lease.
- Một endpoint nhận sự kiện hook dưới đường `/api/` hiện hữu; actor lấy từ credential server-side, không tin trường actor trong payload; idempotent theo `event_id`. Không đổi contract 37/23.
- Nguồn vào sổ: hook Claude Code/Codex · cuộc gọi cổng agent-data (danh tính B1) · Claude Chat qua claude-mcp (đọc audit của claude-mcp hoặc commit author `claude-chat`; không sửa/restart claude-mcp) · SSH · Hermes (§6).

**Trạng thái — executor (Claude Code/Codex):**
| Trạng thái | Khi nào |
|---|---|
| `ACTIVE` | có sự kiện trong lượt. Sau `Stop` = ACTIVE cờ “chờ người”, **không phải LOST** |
| `REPORTED` | phiên gắn RUN và có `KQ@<RUN_ID>` do chính actor đó ghi |
| `AWAITING_REPORT` | `SessionEnd` (hoặc “chờ người” quá 2 h không SessionEnd) mà phiên gắn RUN chưa có KQ |
| `LOST` | giữa lượt (đã có UserPromptSubmit/PreToolUse, chưa Stop) mà im >10′ và không có tool hợp lệ đang chạy. Sự kiện quay lại ⇒ về ACTIVE + ghi “đã mất tín hiệu X′” |
| `NGOÀI VIỆC` (vàng) | phiên không gắn task/RUN mà có SSH hoặc ghi repo. Không thay đổi gì ⇒ chỉ ghi sổ |

**GPT Chat · Claude Chat · Hermes chat:** chỉ `ACTIVE` theo hoạt động + `REPORTED` khi có commit P/KQ. Không áp LOST/AWAITING (không có tín hiệu kết thúc).

## 5. Việc 3 — Owner View tối thiểu

- Tái dùng đường presence hiện hữu: `nuxt-repo/scripts/hvu-b2/presence.py` (đã đọc `queue.sqlite`). Ưu tiên chỉ sửa presence + phần hiển thị tối thiểu; **tránh sửa `sync.py`** (đang Config Guard DRIFT từ A09R1). Nếu buộc sửa `sync.py`: trước đó kiểm hash live = bản A09R1 đã nghiệm thu D102 (`a64a59eb…`), rồi rebaseline ghi old/new + lý do.
- Mỗi việc hiện: `ai/surface · bắt đầu · hoạt động cuối · trạng thái · cảnh báo`. Thêm một dòng **“Ngoài việc”** cho phiên không gắn task.
- Đỏ: ≥2 phiên **executor** (Claude Code/Codex) ACTIVE cùng work/RUN. Reviewer đọc/ghi P song song **không** đỏ.
- Vàng: `SSH_UNKNOWN` · `HOOK_MISSING` · `NGOÀI VIỆC`. `AWAITING_REPORT`/`LOST` hiện rõ.
- Không redesign dashboard.

## 6. Việc 4 — Hermes

- Giữ công tắc tay trên Telegram; AUTO rỗng.
- Ghi ý kiến vào `work/<task>/COLLAB.md` của đúng task trong thẻ giao việc, qua profile riêng `hermes` (không khoá chung). Mở write scope tối thiểu: chỉ `COLLAB.md` của task được giao; nếu cơ chế chỉ hỗ trợ danh sách tĩnh thì `work/*/COLLAB.md` (không PROMPT, không file khác). Khuôn one-shot nhận đường đích từ thẻ.
- Sổ: việc giao (`executions.db`) + chat tự do (`state.db`: phiên bắt đầu/kết thúc, số tool call; không nội dung) → sổ chung, chỉ đọc.
- Config Guard thêm `~/.hermes/config.yaml` (chỉ hash, không đọc giá trị). Thay đổi ngoài RUN được duyệt ⇒ cảnh báo.

## 7. Deploy · rollback · bảo vệ

- Test candidate trên bản sao/fixture trước production.
- Thứ tự: DROOT30 → agent-data (≤1 restart) → hook Mac → Codex → Hermes scope + importer → Owner View → đăng ký mọi mã/config mới vào Config Guard trong cùng RUN (DROOT29) → smoke.
- Rollback có sẵn trước mutation: image/config agent-data · file hook Mac · config Codex · Hermes scope · Owner View · Guard registry.
- Repo public: không secret, không IP Owner (dùng nhãn `Mac Owner`).

## 8. Nghiệm thu bằng thử thật

Executor tự mở phiên thử (`claude -p`, chỉ đọc fixture, không tạo rác repo):

| Mã | Ca | Đạt khi |
|---|---|---|
| CC1 | phiên Claude Code mới | ACTIVE đúng actor `claude-code` |
| CC2 | chạm `work/<id>` | gắn đúng work (và RUN nếu có) |
| CC3 | lệnh SSH qua phiên / SSH tay ngoài hook | gán đúng phiên / `SSH_UNKNOWN` vàng |
| CC4 | phiên gắn RUN kết thúc thiếu KQ | nhắc đúng 1 lần → `AWAITING_REPORT` |
| CC5 | kill -9 giữa lượt / phiên đang chờ người | `LOST` ≤10′ / **không** LOST |
| CC6 | chính RUN R2 ghi KQ | `REPORTED` |
| CC7 | tắt hook rồi gọi cổng bằng profile `claude-code` | `HOOK_MISSING` vàng |
| CC8 | phiên không gắn task mà SSH | `NGOÀI VIỆC` vàng |
| CX | phiên Codex thật theo version | PASS, hoặc residual vàng — không giả PASS |
| CH | GPT/Claude Chat hoạt động; spoof `clientInfo` | vào sổ đúng actor B1; actor không đổi; contract 37/23 |
| OV | 2 phiên Claude Code cùng work/RUN / reviewer song song | đỏ / không đỏ; Owner View hiện đúng actor · thời điểm · trạng thái |
| HM | thẻ Hermes (Owner bấm 1 lần) · chat tự do · Hermes ghi ý kiến · thêm 1 dòng chú thích vào config rồi trả đúng byte | vào sổ · vào sổ · commit author hermes đúng COLLAB · Guard DRIFT rồi MATCH |
| RG | hồi quy | gateway/P02/B1/B2A/công tắc Hermes giữ nguyên · 0 DENY · 0 đếm trùng · mutant/negative FAIL · rollback exact · ngoài scope 0 · không chạm `work/vps1-up-grade` |

Bước HM cần Owner bấm thẻ 1 lần: báo Owner đúng 1 dòng khi tới bước đó; các ca khác chạy tiếp, không ngồi chờ.

## 9. Residual — không dừng cả RUN

Một surface thiếu hook/chức năng ⇒ `RESIDUAL` + vàng trên Owner View + làm tiếp phần độc lập. Chỉ DỪNG cả RUN khi có regression chung hoặc rollback không bảo đảm.

## 10. KQ

`KQ@MCPW-R2-PRESENCE-HERMES-20261001-01 XONG` hoặc `… DỪNG · <lý do>`.

Mở đầu KQ bằng bảng cho Owner (đọc 30 giây):
| Việc | Kết quả |
|---|---|
| 1 Claude Code · Codex · SSH | 🟢 / 🟡 residual |
| 2 Sổ chung | |
| 3 Owner View | |
| 4 Hermes | |

Sau bảng: bằng chứng từng ca §8 · before→after (image/hash/StartedAt/config) + số lần restart · rollback proof · Guard/Config Guard · residual thật.

NEXT sau R2: Claude nghiệm thu (N9 E1–E6) → Owner nhìn Owner View, gật → đóng MCPW. Không tự mở roadmap bước 2–3.
