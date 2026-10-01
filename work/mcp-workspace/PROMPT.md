# PROMPT — MCPW B2B · LIFECYCLE LEDGER + PRIVATE WRITERS + REST ENFORCE

RUN_ID: MCPW-B2B-LIFECYCLE-REST-20261001-01
Host: GPT Chat · GPT-MCPW-250925-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: `work/mcp-workspace/COLLAB.md` qua `workspace_*` bằng profile `claude-code`.
Runtime: VPS1 production.
STATUS: chỉ chạy khi READY Host hiện hành trỏ đúng commit last-touch PROMPT này VÀ gate §1 PASS.

## 0. Mục tiêu duy nhất

Khép B2 bằng một lượt deploy ngắn trên agent-data:
1. cấp private profile/credential cho mọi consumer còn cần WRITE;
2. chặn legacy master WRITE trên cả MCP **và REST**;
3. triển khai lifecycle ledger tối thiểu trên agent-data cho START/FINISH/AWAITING_REPORT/LOST + review-kind + NEXT derivation;
4. chỉ **một lần restart/recreate agent-data** nếu implementation bắt buộc.

Không làm Pha C lease/fencing. Không chạy G5. Không chạm VPS2/Directus/PG/Nuxt/Qdrant/DNS ngoài read-only collision check. **Không sửa/restart claude-mcp** (§3.0). Directus giữ nguyên (§2.3).

Kế thừa bắt buộc:
- B1 identity: `52436cc`, Reviewer P60 ACCEPT.
- B2A: `c4f5902`, Host P66 + Reviewer P67 ACCEPT.
- `legacy_master=enforce` trên MCP và phải giữ như vậy.
- DROOT30/31/32; N1–N9; P39 thiết kế B hiện hành.
- tool contract: agent-data 37, claude-mcp 23; không đổi schema/tool count.
- GitHub vẫn SSOT/write authority; lifecycle/interaction dùng state VPS, không thêm GitHub hot-path.

## 1. START gate — ngắn, không chờ máy móc

START chỉ khi tất cả PASS:

1. **G4C soak đã FINAL sạch** trên `work/vps1-up-grade`:
   - không còn trạng thái soak đang chạy/chờ;
   - không có FAIL/HOLD/rollback đang xử lý;
   - G5 chưa STARTED.
   Thời gian soak tự thân là bằng chứng ổn định; không thêm cửa chờ khác sau FINAL.
2. B2A vẫn terminal sạch, `legacy_master=enforce`, Guard/Config Guard hiện hành không có blocker.
3. agent-data/claude-mcp/nginx healthy; workspace fresh; PROMPT last-touch = READY hiện hành.
4. Không có STARTED/KQ/STOP_REQUESTED/HOLD mới cho RUN B2B; không RUN nào khác đang STARTED mà mutation agent-data/claude-mcp/nginx (RUN chỉ-đọc như DNS-RES DNS0 không chặn).
5. Có rollback cụ thể cho source/config/image trước first mutation.

Thiếu điều nào ⇒ không ghi STARTED, không mutation, trả `NOT_READY · <điều thiếu>`.

Sau gate PASS mới ghi:
`STARTED@MCPW-B2B-LIFECYCLE-REST-20261001-01 <UTC> · executor=Claude Code CLI`.

## 2. PRE — map writer trước khi khóa REST

Làm một lần, trực tiếp, không đặt cửa chờ theo giờ.

### 2.1 Kê đầy đủ consumer WRITE

Dùng code/config/log hiện hành để lập bảng:
`consumer · channel(MCP/REST) · endpoint/tool · scheduled/manual · credential hiện tại · private profile mới · cách test`.

Bắt buộc bao phủ ít nhất:
- Directus Flow production: Reviewer đã đo PG — **29 flow active** POST/DELETE agent-data `/documents` (+`/chat`), 28 lấy khoá chung từ env Directus, gọi nội bộ `AGENT_DATA_URL=http://agent-data:8000` — xử lý theo §2.3;
- `dot-api-health.sh` và mọi cron/timer REST writer;
- DOT `upload_kb.py`;
- MCP cục bộ Claude Desktop `lcl-agent-data`;
- script/DOT khác tìm thấy trong `/opt/incomex`, cron, systemd timer, config Mac;
- GitHub Actions trong repo mã gọi `https://…/api` bằng khoá chung (vd `agent-data-repo/.github/workflows/vector-audit.yml` `POST /kb/audit-sync`, `data-lifecycle.yml` chạy đêm, `nuxt-repo/.github/workflows/sync-check.yml`): kiểm còn chạy không (`gh run list`) và có ghi không;
- các profile đã có: gpt-web · claude-chat · claude-code · codex · Hermes.

Không suy từ tên. Đối chiếu static config + log/audit route thật.

**Không được bật REST enforce trước khi mọi writer hợp lệ cần tiếp tục ghi đã có private credential/profile và đường test.**

### 2.2 Private profiles

Tái dùng `agent_profiles`/secret include/nginx/config path hiện hữu. Không tạo server/port/tool mới.

Cấp private profile tối thiểu cho:
- MCP cục bộ Claude Desktop trên Mac;
- DOT `upload_kb.py`;
- mọi REST writer tự động đang sống **trừ Directus** (health job, GitHub Actions còn chạy, consumer khác tìm được).

Nguyên tắc:
- server quyết actor theo credential; không tin `clientInfo`/UA;
- không in/copy secret vào repo, terminal report hay KQ;
- repo public: không ghi IP Owner; dùng nhãn `Mac Owner`;
- read-only consumer có thể tiếp tục legacy read nếu thiết kế hiện hữu cho phép.

Nếu còn writer đang sống không chuyển được trong lượt (vd không đặt được secret GitHub) ⇒ **không bật REST enforce cho đường đó**, ghi `REST_ENFORCE_DEFERRED` + danh sách; profile + sổ vẫn deploy (độc lập). Không khoá mù, không dừng cả RUN vì REST.

### 2.3 Directus — không đụng trong B2B

Directus sẽ được VPSUP dựng lại ở cutover production; đổi env/restart Directus bây giờ = thêm một lần restart dịch vụ production và đụng VPSUP. Vì vậy:
- giữ nguyên Directus, flow và env;
- REST legacy WRITE chỉ bị DENY khi đến qua **cạnh public** (nginx `/api/`); gọi nội bộ mạng docker từ Directus vẫn được, server gắn nhãn `directus-flow`. Nhận diện bằng tín hiệu server-side ngoài không giả được (vd TCP peer = container nginx ⇒ public; hoặc header do nginx ghi đè ở cạnh), không dùng header client tự gửi;
- khoá riêng cho Directus thành hạng mục bắt buộc của cutover production VPSUP (ghi trong KQ để Host chuyển).
Không tách được public/nội bộ một cách tin cậy ⇒ `REST_ENFORCE_DEFERRED` như §2.2.

## 3. Lifecycle ledger — tối thiểu, reuse-first

### 3.0 Phạm vi chặn (DENY) — hẹp, không khoá hội đồng

- **Chặn** chỉ áp cho profile executor `claude-code`, `codex` khi mutation root repo (workspace git): cần execution ACTIVE (auto-START ở lần chạm đầu `work/<task>/` có RUN ISSUED). Đã ACTIVE thì được ghi cả root `COLLAB.md` trong cùng session (biển báo root trong KQ).
- **Chỉ ghi sổ, không chặn:** Host/Reviewer `gpt-web`/`claude-chat` (kind=review, mọi file kể cả `PROMPT.md`, root `COLLAB.md`); Hermes (đã có cổng Telegram); ghi KB/REST; root `ui`.
- **claude-mcp không đổi trong B2B** (0 restart): hoạt động Claude Chat lấy từ git (author `claude-chat`) cho NEXT/Owner View. Fail-closed của claude-mcp chuyển Pha C.

### 3.1 Single writer

Tái dùng `queue.sqlite` hiện hữu của agent-data:
- SQLite WAL;
- synchronous FULL;
- BEGIN IMMEDIATE cho claim/state transition cần atomic;
- chỉ agent-data ghi ledger.
Không DB/service/port mới. `claude-mcp` không mount/write SQLite và không đổi trong B2B (§3.0).

### 3.2 Execution model

Execution record tối thiểu:
`execution_id · actor_profile · server_session_id · work_id · RUN_ID/assignment_id · role · kind · scope · generation · state · started_at · last_activity_at · ended_at · end_reason · report_ref`.

- `execution_id` do VPS sinh.
- key auto-claim theo P39: `(actor_profile, server_session_id)`.
- lần gọi đầu tiên chạm đúng `work/<task>/` có RUN ISSUED/READY hợp lệ ⇒ durable START trước side effect.
- trong phạm vi chặn §3.0: mutation bắt buộc có execution ACTIVE cùng session/work/RUN/scope;
- tool không có path của executor chỉ gắn khi session có đúng một execution ACTIVE; 0 hoặc >1 ⇒ DENY trước side effect.
- START + first event commit trước side effect.
- không suy “đang nghĩ” từ im lặng.

### 3.3 Trạng thái cuối

Chuẩn hóa tối thiểu:
- `REPORTED`: report/KQ/P hợp lệ đã gắn artifact/commit thật;
- `AWAITING_REPORT`: execution kỹ thuật kết thúc nhưng chưa có report hợp lệ;
- `LOST`: crash/recover/session mất/hết điều kiện sống mà không terminal hợp lệ;
- nội bộ có thể giữ `STARTED/ACTIVE/FINISHING`, nhưng một execution kết thúc phải quy về đúng một terminal state phía trên.

Recover sau restart phải biến execution treo cũ thành LOST/INTERRUPTED theo thiết kế, không tự coi DONE.

### 3.4 Review-kind

Host/Reviewer không có RUN executor vẫn ghi review bình thường:
- mutation của Host/Reviewer (mọi file, kể cả `PROMPT.md`, root `COLLAB.md`) ⇒ ghi sổ `kind=review`, không bao giờ DENY; role lấy từ task, không suy từ route;
- commit/report review thành công ⇒ REPORTED;
- route identity `claude-chat` chỉ là actor route, không tự suy role Reviewer.

Claude Code executor bắt buộc ghi repo qua `workspace_*` profile `claude-code`; không dùng `fs_*` để ghi repo.

### 3.5 NEXT derivation

Tái dùng A9/Owner View/state hiện hữu. Không tạo pipeline mới.

Từ lifecycle + task signals, máy phải có đúng một NEXT tối thiểu cho mỗi task mở:
`surface/role tiếp theo · hành động · lý do`.

- không có execution/report hợp lệ ⇒ không gọi DONE;
- AWAITING_REPORT/LOST phải hiện rõ, không giả “đang làm”;
- Hermes dispatch/control path hiện hữu được tái dùng, AUTO không tự bật;
- không thay A9 bằng cơ chế thứ hai nếu không cần.

## 4. REST legacy write enforcement

Sau khi §2 private cutover PASS:

- áp cùng nguyên tắc B2A cho REST write endpoint của agent-data: legacy master READ được giữ nếu hợp đồng hiện hành cần; legacy master WRITE phải DENY **trước side effect** khi đến qua cạnh public (nội bộ Directus theo §2.3);
- bao phủ các endpoint ghi thực tế dưới `/api/`, gồm documents/KB/webhook/chat endpoint nào có mutation theo code live;
- private profile hợp lệ vẫn WRITE được;
- random/unknown credential 401;
- không đổi public tool/schema contract 37/23.

Không hard-code danh sách endpoint chỉ từ báo cáo B2A; derive từ router/source live và test theo nhóm mutation.

## 5. Residual nhỏ cùng lượt

- sửa quyền `~/.claude.json` về 0600 nếu còn 0644, không in nội dung/secret;
- backup/config chứa khoá chung: chỉ `chmod 0600`; **không xoá, không xoay khoá** (phá huỷ/xoay khoá = Owner quyết riêng);
- planned-change window + Config Guard rebaseline qua apply path hiện hữu trước nhịp Guard để tránh false alarm;
- không thêm cleanup ngoài scope.

## 6. Deploy

Ưu tiên một candidate image/config đã test trên bản sao/fixture.

Production:
1. DROOT30 ngay trước mutation;
2. private writer cutover/config;
3. deploy code/config lifecycle + REST gate;
4. **chỉ một lần restart/recreate agent-data** nếu cần;
5. smoke ngay;
6. nếu critical acceptance fail ⇒ rollback source/config/image + private writer routing về known-good, giữ B2A MCP enforce nếu rollback độc lập cho phép.

Không restart claude-mcp/Directus/nginx (nginx `reload` được nếu cần cho §2.3). Nếu phát hiện bắt buộc restart thêm service ngoài agent-data ⇒ STOP trước mutation đó và báo Host.

## 7. Acceptance tối thiểu

### A. Writer/REST
1. bảng writer có nguồn bằng chứng; 0 writer tự động hợp lệ còn phụ thuộc legacy WRITE;
2. Directus nội bộ vẫn ghi được, nhãn `directus-flow` (probe nội bộ bằng đối số sai ⇒ lỗi kiểm dữ liệu, không phải DENIED; không tạo dữ liệu Directus); cùng khoá chung qua cạnh public ⇒ DENY;
3. `dot-api-health.sh` + GitHub Actions còn chạy: private PASS hoặc nằm trong `REST_ENFORCE_DEFERRED`;
4. MCP local Claude Desktop + DOT upload KB private write path PASS bằng probe không tạo rác;
5. legacy REST WRITE bị DENY trước side effect trên mọi nhóm endpoint mutation;
6. legacy READ cần thiết vẫn PASS.

### B. Identity/contract
7. gpt-web · claude-chat · claude-code · codex · Hermes không regression;
8. spoof `clientInfo` không đổi actor;
9. agent-data 37 / claude-mcp 23 + schema/serverInfo unchanged.

### C. Lifecycle
10. first scoped touch → START durable trước side effect;
11. START → report hợp lệ → REPORTED;
12. technical finish thiếu report → AWAITING_REPORT;
13. crash/recover fixture → LOST, không DONE;
14. duplicate/retry/event replay không double-count;
15. 0 orphan trong tập test; cursor/replay đúng;
16. `gpt-web` sửa `PROMPT.md` + root `COLLAB.md` không bị chặn; Hermes/KB/`ui` chỉ ghi sổ;
17. session có 0/>1 execution mà gọi pathless mutation ⇒ DENY;
18. claude-mcp không đổi (image/StartedAt trước = sau); fail-closed claude-mcp chuyển Pha C;
19. NEXT derivation trên fixture cho đúng một “ai · làm gì”; LOST/AWAITING_REPORT không bị hiển thị DONE.

### D. Guard/rollback
20. Config Guard CLEAN; Guard POST PASS; ngoài scope = 0;
21. mutant/negative control của REST gate + lifecycle gate phải FAIL;
22. rollback proof exact cho image/config/private routing;
23. runtime identity before→after: image/hash/StartedAt/config được ghi;
24. không chạm VPS2/G5; G5 vẫn chưa STARTED trong RUN này.

Không đặt soak mới nếu test trực tiếp + rollback đã đủ bằng chứng (DROOT32). Chỉ nếu restart/lifecycle cần quan sát theo thời gian mới giao watcher VPS hiện hữu và nêu rõ bằng chứng cần sinh.

## 8. KQ

PASS:
`KQ@MCPW-B2B-LIFECYCLE-REST-20261001-01 XONG`

KQ ngắn nhưng phải có:
- G4C FINAL gate;
- writer map + profile labels (không secret/IP Owner);
- source/config/image before→after + restart count;
- REST legacy deny/private writer PASS;
- Directus nội bộ + hạng mục chuyển VPSUP; `REST_ENFORCE_DEFERRED` (nếu có);
- lifecycle state tests + reconciliation;
- NEXT fixture;
- contract 37/23;
- Guard/Config Guard;
- rollback proof;
- residual thật còn lại.

FAIL:
`KQ@MCPW-B2B-LIFECYCLE-REST-20261001-01 DỪNG · <reason>`

## 9. NEXT

Sau B2B:
- Host + Claude nghiệm thu theo N9 E1–E6;
- nếu ACCEPT: Pha C scoped lease/fencing;
- nhánh VPSUP: chỉ khi B2B terminal/clean thì Host mới cho G5 RUN; khoá riêng cho Directus vào checklist cutover production VPSUP.

Không tự chạy Pha C hay G5 trong RUN này.
