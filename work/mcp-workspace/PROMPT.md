# PROMPT — MCPW B2A · LEGACY MASTER WRITE ENFORCE

RUN_ID: MCPW-B2A-LEGACY-ENFORCE-20261001-01
Host: GPT Chat · GPT-MCPW-250925-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: `work/mcp-workspace/COLLAB.md` qua `workspace_*` bằng profile `claude-code`.
Runtime: VPS1 production.
STATUS: chạy theo READY Host phát ở task COLLAB; READY phải = commit last-touch của PROMPT này.

## 0. Mục tiêu duy nhất

Khép phần `ENFORCE_DEFERRED` của B1 bằng cách đổi `legacy_master` từ `compat` sang `enforce` ngay khi đủ cổng bằng chứng §1 — **không chờ theo giờ** (DROOT32, P64).

RUN này KHÔNG làm execution ledger. KHÔNG restart/recreate agent-data/claude-mcp/nginx. KHÔNG B2B/Pha C.

Kế thừa:
- B1 KQ `52436cc24e5ff100dd8402dad6b16b069a30d789` XONG · ENFORCE_DEFERRED;
- Reviewer P60 `8cb01359eab876834b8920fc8a9a3b06873f4cfd` ACCEPT;
- profile server-side đã có: `gpt-web` · `claude-chat` · `claude-code` · `codex`; Hermes không đổi;
- legacy read-only consumers được phép còn tồn tại; legacy **write** phải bị chặn sau RUN.
- consumer **có khả năng ghi nhưng đang không ghi** (`WRITE_DORMANT`, §3) sau RUN thành chỉ-đọc theo quyết định Owner **O-B2A-1** (task COLLAB); Host chỉ phát READY sau khi Owner gật. B2B cấp profile riêng cho consumer nào cần ghi lại.

## 1. Khi nào được START

Cổng bằng chứng, đo live **một lần**, không chờ giờ (DROOT32). START ngay khi đủ cả 4:
1. **Người ghi đã biết đã chuyển khoá:** journal `legacy_master_write` (mọi lượt gọi tool ghi qua khoá chung, kể cả lượt lỗi — journal ghi ở cổng trước khi chạy) từ deploy B1 chỉ gồm app Codex cũ, đã cutover sang profile `codex`.
2. **Không người ghi lạ:** không có `legacy_master_write` nào sau lượt cuối đã biết (30/09 08:19:05Z); journal liền mạch, không gap/UNKNOWN.
3. **G4C không cần khoá chung để ghi:** commit G4C mang `auth:claude-code`.
4. **Rollback sẵn:** `b1-ctl.sh legacy compat` qua cùng apply path, không restart.

Thiếu điều nào ⇒ KHÔNG ghi STARTED, KHÔNG mutation, trả `NOT_READY · <điều thiếu> · <bằng chứng>`.

## 2. Read/collision gate

Đọc:
AGENTS.md → root COLLAB DROOT09/19/22/25/28/29/30/31/32 → MCPW COLLAB §0 + N1–N9 + KQ B1 + P57/P58/P60/P61/P63/P64 + O-B2A-1 → PROMPT này.

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
- không có `legacy_master_write` mới kể từ lượt đo ở §1;
- exact last `legacy_master_write` timestamp/route/src/tool;
- profile writes gần nhất của gpt-web/claude-chat/claude-code/codex;
- **quét tĩnh người ghi tiềm năng** (journal không thấy job tuần/chạy tay; làm một lần, ~1 phút): root/user crontab, systemd timers, DOT/script trong `/opt/incomex` đọc khoá chung từ `.env` rồi gọi tool ghi, config MCP trên Mac (Claude Desktop, Antigravity, khác). Đã biết: MCP cục bộ Claude Desktop (có tool ghi) · DOT `dot/iu-cutter-*/upload_kb.py` (`upload_document`) · Antigravity giữ khoá trước SEC-CRED (VPSUP §8A) · Kuma/Guard/claude-kb chỉ đọc;
- phân loại từng consumer: `READ_ONLY` · `WRITE_DORMANT` (có khả năng ghi, chạy tay/hiếm, 0 lượt sau 30/09 08:19:05Z) · `WRITE_SCHEDULED` (cron/timer/tự động có gọi tool ghi);
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
- bằng chứng 4 điều §1;
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
