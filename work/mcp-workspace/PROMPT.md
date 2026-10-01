# PROMPT — MCPW B2A · LEGACY MASTER WRITE ENFORCE

RUN_ID: MCPW-B2A-LEGACY-ENFORCE-20261001-01
Host: GPT Chat · GPT-MCPW-250925-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: `work/mcp-workspace/COLLAB.md` qua `workspace_*` bằng profile `claude-code`.
Runtime: VPS1 production.
STATUS: chạy theo READY Host phát ở task COLLAB; READY phải = commit last-touch của PROMPT này.

## 0. Mục tiêu duy nhất

Khép phần `ENFORCE_DEFERRED` của B1 bằng cách đổi `legacy_master` từ `compat` sang `enforce` **chỉ sau khi máy chứng minh không có legacy write trong 24 giờ liên tục**.

RUN này KHÔNG làm execution ledger. KHÔNG restart/recreate agent-data/claude-mcp/nginx. KHÔNG B2B/Pha C.

Kế thừa:
- B1 KQ `52436cc24e5ff100dd8402dad6b16b069a30d789` XONG · ENFORCE_DEFERRED;
- Reviewer P60 `8cb01359eab876834b8920fc8a9a3b06873f4cfd` ACCEPT;
- profile server-side đã có: `gpt-web` · `claude-chat` · `claude-code` · `codex`; Hermes không đổi;
- legacy read-only consumers được phép còn tồn tại; legacy **write** phải bị chặn sau RUN.
- consumer **có khả năng ghi nhưng đang không ghi** (`WRITE_DORMANT`, §3) sau RUN thành chỉ-đọc theo quyết định Owner **O-B2A-1** (task COLLAB); Host chỉ phát READY sau khi Owner gật. B2B cấp profile riêng cho consumer nào cần ghi lại.

## 1. Khi nào được START

Không launch RUN này chỉ dựa vào giờ dự kiến.

Executor chỉ được START khi read-gate xác minh từ journal máy:
- tìm **sự kiện `legacy_master_write` gần nhất** — mọi lượt gọi tool ghi qua khoá chung, kể cả lượt sau đó lỗi (journal ghi ở cổng, trước khi chạy tool);
- từ lượt đó tới thời điểm kiểm đã đủ **>=24h liên tục**;
- trong cửa sổ đó `legacy_master_write=0`;
- journal không có gap/UNKNOWN làm mất khả năng kết luận.

Mốc B1 báo cáo chỉ để định hướng: lượt cuối ~30/09 08:19Z ⇒ sớm nhất khoảng 01/10 08:20Z (15:20 +07). **Journal live quyết định, không phải mốc này.**

Nếu chưa đủ 24h hoặc journal không đủ tin cậy:
- KHÔNG ghi STARTED;
- KHÔNG mutation;
- trả `NOT_YET_LEGACY_24H · last_write=<UTC> · eligible_after=<UTC>`.

## 2. Read/collision gate

Đọc:
AGENTS.md → root COLLAB DROOT09/19/22/25/28/29/30/31 → MCPW COLLAB §0 + N1–N9 + KQ B1 + P57/P58/P60/P61/P63 + O-B2A-1 → PROMPT này.

Kiểm live:
- PROMPT last-touch = READY hiện hành;
- không có STARTED/KQ/STOP_REQUESTED/HOLD/READY mới cho B2A;
- B1 terminal sạch;
- `legacy_master=compat`;
- Config Guard hiện hành CLEAN;
- agent-data/claude-mcp/nginx healthy;
- G4C VPSUP có thể đang STARTED trên VPS2: **không chặn B2A** vì RUN này không restart/recreate và không chạm VPS2/Directus/PG/Nuxt/Qdrant/DNS.

Chỉ sau khi §1 PASS, ghi:
`STARTED@MCPW-B2A-LEGACY-ENFORCE-20261001-01 <UTC> · executor=Claude Code CLI`.

## 3. PRE — đo lại ngay trước mutation

Ngay trước mutation áp DROOT30 và đo lại:
- legacy write trong trailing 24h = 0;
- exact last `legacy_master_write` timestamp/route/src/tool;
- profile writes gần nhất của gpt-web/claude-chat/claude-code/codex;
- **quét tĩnh người ghi tiềm năng** (cửa sổ 24h không thấy job tuần/chạy tay): root/user crontab, systemd timers, DOT/script trong `/opt/incomex` đọc khoá chung từ `.env` rồi gọi tool ghi, config MCP trên Mac (Claude Desktop, Antigravity, khác). Đã biết: MCP cục bộ Claude Desktop (có tool ghi) · DOT `dot/iu-cutter-*/upload_kb.py` (`upload_document`) · Antigravity giữ khoá trước SEC-CRED (VPSUP §8A) · Kuma/Guard/claude-kb chỉ đọc;
- phân loại từng consumer: `READ_ONLY` · `WRITE_DORMANT` (có khả năng ghi, chạy tay/hiếm, 0 lượt trong cửa sổ §1) · `WRITE_SCHEDULED` (cron/timer/tự động có gọi tool ghi);
- có `WRITE_SCHEDULED` ⇒ DỪNG trước enforce, ghi exact consumer/evidence (nó sẽ hỏng ngầm theo lịch);
- `WRITE_DORMANT` **không** chặn RUN: sau enforce thành chỉ-đọc theo O-B2A-1, liệt kê đủ trong KQ.

Không yêu cầu map lịch sử 7 ngày; chỉ dùng forward evidence theo P57/P60.

## 4. Mutation duy nhất

Đổi `legacy_master: compat → enforce` bằng **Config Guard/apply path hiện hữu**, có RUN_ID/reason/audit.

Yêu cầu:
- một config switch;
- không restart/recreate;
- không sửa tool/schema/serverInfo;
- không xoá legacy credential;
- không rotate GSM;
- rollback = switch `enforce → compat` qua cùng apply path.

## 5. Acceptance

Sau switch:

1. `legacy_master=enforce` live + Config Guard CLEAN.
2. Legacy **read** bằng khoá chung vẫn hoạt động cho read-only tool contract.
3. Legacy **write** bị DENY **trước side effect**; dùng probe vô hại/invalid write path để không tạo commit/rác.
4. `gpt-web`, `claude-chat`, `claude-code`, `codex` vẫn read được đúng contract; profile write path của Host/Reviewer/Claude Code không bị khóa.
5. Claude Code KQ phải ghi bằng `workspace_*` và commit author = `claude-code [auth:claude-code]`.
6. Hermes profile/tool/write scope/AUTO/STOP unchanged.
7. Tool contract 37/23 + schema/serverInfo unchanged.
8. Guard/Config Guard POST CLEAN; ngoài scope = 0.
9. Không restart/recreate bất kỳ production service nào.
10. Không ghi `work/vps1-up-grade/`; không mutation VPS2/Directus/PG/Nuxt/Qdrant/DNS.
11. Biển báo root (dòng MCPW, cùng commit KQ): khoá chung chỉ còn đọc; tên các `WRITE_DORMANT`; cách mở lại tạm = `legacy compat` qua cùng apply path khi Owner nói một câu.

## 6. Rollback proof

Trước KQ:
- chứng minh switch có thể trả `enforce → compat` bằng cơ chế hiện hữu mà không restart;
- không cần lật production về compat nếu acceptance PASS;
- lưu exact old/new + audit + reason/RUN_ID.

Nếu sau enforce profile write hợp lệ bị khóa hoặc read-only legacy bị hỏng ngoài dự kiến:
- rollback ngay về `compat`;
- KQ DỪNG với evidence;
- không tự sửa rộng hơn.

## 7. KQ

PASS:
`KQ@MCPW-B2A-LEGACY-ENFORCE-20261001-01 XONG`

KQ phải nêu:
- last legacy write UTC;
- trailing window thực đo;
- switch audit;
- legacy read PASS / legacy write DENY;
- 4 profile smoke;
- bảng consumer `READ_ONLY/WRITE_DORMANT/WRITE_SCHEDULED` + nguồn bằng chứng;
- contract hash;
- Guard/Config Guard;
- rollback proof.

## 8. NEXT

Sau B2A XONG:
- Host + Claude nghiệm thu nhanh;
- B2B = execution ledger / START-FINISH / NEXT theo P39/N1–N9; trong lượt deploy agent-data của B2B cấp profile riêng cho các `WRITE_DORMANT` cần ghi lại (MCP cục bộ Claude Desktop, DOT upload KB);
- B2B deploy/restart agent-data chỉ sau khi VPSUP G4C terminal hoặc DROOT30 chứng minh không còn collision runtime;
- sau B2B mới Pha C lease/fencing.

Không tự chạy B2B/C trong RUN này.
