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

Không làm Pha C lease/fencing. Không chạy G5. Không chạm VPS2/Directus/PG/Nuxt/Qdrant/DNS ngoài read-only collision check.

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
4. Không có STARTED/KQ/STOP_REQUESTED/HOLD mới cho RUN B2B.
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
- Directus Flow/automation production gọi agent-data REST POST/DELETE hoặc endpoint ghi liên quan KB;
- `dot-api-health.sh` và mọi cron/timer REST writer;
- DOT `upload_kb.py`;
- MCP cục bộ Claude Desktop `lcl-agent-data`;
- script/DOT khác tìm thấy trong `/opt/incomex`, cron, systemd timer, config Mac;
- các profile đã có: gpt-web · claude-chat · claude-code · codex · Hermes.

Không suy từ tên. Đối chiếu static config + log/audit route thật.

**Không được bật REST enforce trước khi mọi writer hợp lệ cần tiếp tục ghi đã có private credential/profile và đường test.**

### 2.2 Private profiles

Tái dùng `agent_profiles`/secret include/nginx/config path hiện hữu. Không tạo server/port/tool mới.

Cấp private profile tối thiểu cho:
- MCP cục bộ Claude Desktop trên Mac;
- DOT `upload_kb.py`;
- mọi REST writer tự động đang sống (Directus flow, health job, hoặc consumer khác tìm được).

Nguyên tắc:
- server quyết actor theo credential; không tin `clientInfo`/UA;
- không in/copy secret vào repo, terminal report hay KQ;
- repo public: không ghi IP Owner; dùng nhãn `Mac Owner`;
- read-only consumer có thể tiếp tục legacy read nếu thiết kế hiện hữu cho phép.

Nếu phát hiện writer không thể chuyển private profile an toàn trong cùng lượt ⇒ STOP trước REST enforce và báo exact blocker; không khóa mù.

## 3. Lifecycle ledger — tối thiểu, reuse-first

### 3.1 Single writer

Tái dùng `queue.sqlite` hiện hữu của agent-data:
- SQLite WAL;
- synchronous FULL;
- BEGIN IMMEDIATE cho claim/state transition cần atomic;
- chỉ agent-data ghi ledger.
Không DB/service/port mới. `claude-mcp` không mount/write SQLite trực tiếp; nếu cần ghi lifecycle, gọi internal agent-data path trên docker network hiện hữu. Agent-data down ⇒ write từ claude-mcp fail-closed; read path vẫn được giữ khi có thể.

### 3.2 Execution model

Execution record tối thiểu:
`execution_id · actor_profile · server_session_id · work_id · RUN_ID/assignment_id · role · kind · scope · generation · state · started_at · last_activity_at · ended_at · end_reason · report_ref`.

- `execution_id` do VPS sinh.
- key auto-claim theo P39: `(actor_profile, server_session_id)`.
- lần gọi đầu tiên chạm đúng `work/<task>/` có RUN ISSUED/READY hợp lệ ⇒ durable START trước side effect.
- mutation bắt buộc có execution ACTIVE cùng session/work/RUN/scope.
- tool không có path chỉ gắn khi session có đúng một execution ACTIVE; 0 hoặc >1 ⇒ DENY trước side effect.
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
- mutation review vào đúng `work/<task>/COLLAB.md`/surface được giao ⇒ auto START `kind=review`, role lấy từ task, không suy từ route;
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

- áp cùng nguyên tắc B2A cho REST write endpoint của agent-data: legacy master READ được giữ nếu hợp đồng hiện hành cần; legacy master WRITE phải DENY **trước side effect**;
- bao phủ các endpoint ghi thực tế dưới `/api/`, gồm documents/KB/webhook/chat endpoint nào có mutation theo code live;
- private profile hợp lệ vẫn WRITE được;
- random/unknown credential 401;
- không đổi public tool/schema contract 37/23.

Không hard-code danh sách endpoint chỉ từ báo cáo B2A; derive từ router/source live và test theo nhóm mutation.

## 5. Residual nhỏ cùng lượt

- sửa quyền `~/.claude.json` về 0600 nếu còn 0644, không in nội dung/secret;
- xử lý backup/config chứa legacy key theo policy hiện hành mà không xóa đường rollback cần thiết;
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

Không restart claude-mcp/nginx nếu không thật sự bắt buộc; nếu phát hiện bắt buộc restart thêm service ngoài agent-data ⇒ STOP và báo Host trước khi mở rộng.

## 7. Acceptance tối thiểu

### A. Writer/REST
1. bảng writer có nguồn bằng chứng; 0 writer tự động hợp lệ còn phụ thuộc legacy WRITE;
2. Directus production flow/automation writer qua private profile PASS bằng probe an toàn;
3. `dot-api-health.sh`/scheduled REST writer private PASS;
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
16. review-kind Host/Reviewer không bị lifecycle gate chặn;
17. session có 0/>1 execution mà gọi pathless mutation ⇒ DENY;
18. agent-data down ⇒ claude-mcp write fail-closed; read không regression ngoài giới hạn đã biết;
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
- nhánh VPSUP: chỉ khi B2B terminal/clean thì Host mới cho G5 RUN.
T-FINISH / NEXT theo P39/N1–N9; trong lượt deploy agent-data của B2B cấp profile riêng cho các `WRITE_DORMANT` cần ghi lại (MCP cục bộ Claude Desktop, DOT upload KB);
- B2B deploy/restart agent-data chỉ sau khi VPSUP G4C terminal hoặc DROOT30 chứng minh không còn collision runtime;
- sau B2B mới Pha C lease/fencing.

Không tự chạy B2B/C trong RUN này.
