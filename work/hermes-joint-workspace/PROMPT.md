# PROMPT — HJW.3B · Public Webhook Bridge + Secret + Kuma + Closeout

RUN_ID: HJW-3B-20260925-01
STATUS: DRAFT — KHÔNG MUTATION cho tới khi Reviewer ACCEPT và Host ghi READY@ đúng SHA cuối chạm file này

Executor_Surface: Claude Code CLI MỚI trên Mac
Runtime_Write_Path: SSH/root-operator tới VPS; Hermes runtime/config trên VPS là SSOT
Report_Write_Path: chỉ cập nhật file hiện hữu `work/hermes-joint-workspace/COLLAB.md` + `view.html`; evidence nhạy cảm append vào hồ sơ root-only hiện hữu
Work: `work/hermes-joint-workspace/`

## HJW.3B DELTA — PHẦN DUY NHẤT EXECUTOR MỚI ĐƯỢC MUTATION

Baseline đã chạy: `HJW-3-20260924-01` tại `PROMPT@23f49c0ac5ca5fe9436cc0b77166224bebd0d55e`.
Evidence root-only hiện hữu: `/opt/incomex/work/hermes-joint-workspace/HJW-3-20260924-01/`.
**Không làm lại G1/G2/STOP/local webhook đã PASS ở P26.**

### Mục tiêu còn lại
1. Quan sát/đối chiếu T5/T6 self-wake đã được Host arm bằng `ASSIGN@HJW-H3-T5-01`; không trigger tay.
2. Public webhook qua **UNIX socket bridge**, webhook bản thân vẫn bind `127.0.0.1:8644`.
3. Một secret riêng `HERMES_WEBHOOK_SECRET` qua secret-path root-managed hiện hữu.
4. Harden nginx + external tests + canary.
5. Kuma monitor qua hạ tầng Kuma hiện hữu.
6. Hoàn tất T10/KQ.

### Read-gate phiên CLI MỚI
Đọc:
`AGENTS.md → root COLLAB.md → HJW COLLAB.md (P26/P27/P28 + dòng hiện hành) → PROMPT.md phần HJW.3B này → EVIDENCE.md + rollback.sh`.

Phải xác nhận baseline:
- G1: `hjw_gate.py`, fault-injection + fixture 11/11 PASS.
- G2: `ws-dispatch` 2′, handoff/run-watch 15′, idle 0 LLM.
- STOP-DISPATCH + STOP-AUTO baseline PASS.
- local WebhookAdapter tests P26 giữ nguyên.
- Agent Gateway 7 tool sống; `AGENT_DATA_*` vẫn vắng.
- T5: nếu assignment đã done thì đọc P29 + ledger/Telegram; nếu open/claimed thì **không can thiệp/không cron run tay**.
- trước mutation: re-read HEAD/version/worktree; conflict/outcome UNKNOWN => read-back/reconcile, không overwrite.

### T5/T6
T5 chỉ PASS khi cron tự wake LLM Hermes, assignment tự chuyển trạng thái, Git author = `agent-gw/hermes`, Telegram/raw delivery **exactly 3 non-empty lines STATUS/COMMIT/NEXT**, và executions ledger chứng minh model turn thật.
T6: lấy model/provider/reasoning + token/cost thật nếu có; không suy giá.

### Bridge — UNIX socket ONLY
Host ruling P28 + JEV `gen-dec-1790288556-2qqAifoGz8UcJn8fJnW4` chọn UNIX_SOCKET 0.98.

Trước mutation:
- `docker inspect incomex-nginx`: Mounts/User/Networks/config source.
- xác định nginx worker UID/GID + userns.
- tìm host directory đã bind-mount vào nginx phù hợp cho socket.
- kiểm pattern `systemd-socket-proxyd` hiện hữu.

Ưu tiên:
- một cặp systemd socket/service tối thiểu: **UNIX socket → 127.0.0.1:8644**;
- socket mode tối đa 0660, owner/group chỉ đủ cho nginx worker;
- nginx `proxy_pass` qua UNIX socket;
- **không TCP listener mới**.

Nếu chưa có mount phù hợp nhưng config hiện hữu hỗ trợ:
- **TRƯỚC KHI recreate nginx**, bắt buộc xác định và lưu **run-spec đầy đủ** đã sinh ra container `incomex-nginx` hiện tại: compose file/project hoặc unit/source-of-truth tương đương, image/digest, command/entrypoint, env refs, mounts, networks, published ports, restart policy và các tham số cần thiết để tái tạo **nguyên trạng**. Phải chứng minh dry-read rằng container có thể được dựng lại từ đúng spec này; **không xác định được nguồn tạo/run-spec ⇒ DỪNG, không recreate**.
- chụp pre-recreate acceptance riêng cho các đường public đang sống: **Owner View, Directus, Nuxt, `/api/mcp*` của Agent Data và route GPT hiện hành**; lưu status/đích kiểm cụ thể để so sau.
- được phép thêm đúng **một bind-mount thư mục socket** vào nginx trong chính run-spec đã xác định;
- chuẩn bị rollback **từ run-spec gốc** trước mutation; Telegram Owner trước recreate.
- recreate **chỉ nginx đúng một lần**; sau recreate phải kiểm lại **đích danh từng đường public ở trên** + container state/config/mount/network. Bất kỳ đường nào lệch ⇒ rollback ngay bằng run-spec gốc và DỪNG.
- **Không gộp recreate với nginx reload.** Recreate xong phải verify sạch trước; chỉ khi sang bước sửa nginx route sau đó mới `nginx -t` + reload và verify riêng lần nữa, để tách nguyên nhân lỗi.

UDS không khả thi an toàn => `DỪNG UDS_BRIDGE_NOT_FEASIBLE`.
**CẤM fallback TCP 172.18.0.1 trong RUN này.**

### Secret webhook
Được phép tạo đúng một secret `HERMES_WEBHOOK_SECRET` trong Secret Manager/project hiện hữu:
- random mạnh, không stdout/log/chat/repo;
- không project/service mới;
- config chỉ dùng `${HERMES_WEBHOOK_SECRET}`;
- user Hermes không có GSM credential;
- thiếu secret => fail closed, không plaintext fallback.

**Chuỗi materialize bắt buộc — tái dùng đúng thứ tự đã PASS ở HJW.2B1:**
1. sửa **source** `/usr/local/sbin/hermes-key-fetch` hiện hữu để nạp optional `HERMES_WEBHOOK_SECRET`; kiểm syntax/source trước khi chạy;
2. **root chạy trực tiếp source command/script đó để regenerate `/run/hermes/or.env`**; **TUYỆT ĐỐI KHÔNG `systemctl restart hermes-key.service`** và không restart oneshot/unit nạp key, vì unit đó có dependency có thể bounce cả serve+gateway;
3. chỉ kiểm **tên biến/presence**, không in giá trị: `HERMES_WEBHOOK_SECRET` phải có; `AGENT_DATA_*` vẫn phải vắng trong file env;
4. sau khi config webhook đã sẵn sàng, restart **`hermes-serve` trước → verify health → `hermes-gateway` sau → verify Telegram/health**;
5. sau restart, chứng minh lại bằng `/proc/<MainPID>/environ` của **cả serve và gateway**: `AGENT_DATA_*` = 0; narrow Agent Gateway key vẫn hiện diện đúng cơ chế; `hermes-safe-update health` PASS;
6. rollback secret/script cũng theo cùng thứ tự: restore source → root regenerate trực tiếp env → kiểm names → restart serve → gateway → health. **Không restart `hermes-key.service`.**

Nếu script source/syntax/regenerate fail hoặc env mất biến bắt buộc ⇒ DỪNG trước restart; không để `EnvironmentFile=` hỏng làm Hermes chết.
Nếu auto-mode chặn Secret-Store write => DỪNG đúng approval gate, không lách.

### Webhook/nginx production
Webhook:
- `platforms.webhook.extra.host=127.0.0.1`, port 8644;
- profile `default`, route `incomex-dispatch`, `cron_job=ws-dispatch`;
- fixed literal template; cấm interpolation từ body/header/query/payload;
- HMAC V2; body ≤16KB; adapter rate 30/phút/route.

Nginx exact public route:
- POST only; reject query string;
- ≤30 req/min/source, burst≤5; body≤16KB;
- strict `X-Request-ID` hex/uuid-style 16–64;
- no args/body/secret in logs;
- reject/strip legacy V1/GitHub/GitLab/Svix/Linear signature families;
- preserve only exact Hermes V2 headers + sanitized delivery id/content type;
- `nginx -t` + Telegram Owner trước reload.

External test bắt buộc: wrong/missing/expired V2 reject; **V1 và GitHub-style hợp lệ cũng phải reject**; query/id invalid reject; duplicate same id no second run; rate counts thật; valid V2/no assignment => gate false 0 LLM.

Residual chấp nhận: replay request hợp lệ trong freshness window bằng delivery-id mới vẫn có thể “đánh chuông”, nhưng scheduler claim + rate-limit giới hạn tác hại. Ghi đúng, **không gọi replay-proof**.

### Canary
Sau public route: canary unique không được xuất hiện ở prompt/context, model output, Telegram, application/gateway/nginx logs acceptance.
Query bị reject; ID sanitized; access log no args.
Leak bất kỳ mặt nào => rollback public route + DỪNG.
Mỗi route webhook thêm/sửa về sau phải chạy lại canary.

### Kuma
Được phép tạo đúng một monitor Hermes trong Kuma hiện hữu; token root-only; gắn vào push script/service/timer root-owned hiện hữu.
Không tạo service/timer mới nếu cơ chế hiện hữu dùng được; nếu bắt buộc unit mới => `DỪNG KUMA_NEW_UNIT_REQUIRED`.
Test alert ≤10 phút rồi restore.

### Rollback/KQ
Không rollback G1/G2/HJW.2C trừ khi causal.
KQ chỉ XONG nếu đủ: T5+T6; UDS/socket proof; V1/GitHub rejection; canary sạch public; idle 0 LLM; STOP/HARD-STOP; Kuma alert; valid V2 tới cùng dispatcher/claim; rollback documented.

**CẤM:** repo task/project/file mới; TCP bridge 172.18.0.1; raw public 8644/8642/9119; direct full Hermes API public; legacy signature public; GSM credential cho user Hermes; plaintext secret; manual trigger giả T5; rerun G1/G2 nếu không regression.

## BASELINE HJW.3 BÊN DƯỚI — CHỈ THAM KHẢO, KHÔNG LÀM LẠI

## 0. Owner direction / kiến trúc bắt buộc

Owner 24/09 nhắc lại: **thế mạnh Hermes là chạy VPS 24/7 và qua API nên có thể được gọi từ bên ngoài, bất cứ lúc nào; phải kết nối ở mức tốt nhất để dùng cho các việc tiếp theo.**

Không biến Hermes thành một chatbot chỉ đọc/ghi repo. HJW.3 phải nghiệm thu vòng:
**trigger ngoài / lịch / Telegram → lọc máy 0-token → wake đúng lúc → Hermes LLM đọc SSOT → claim/làm bằng Agent Gateway → Git attribution → báo Telegram → ledger/monitor/stop/retry.**

Kiến trúc Host chốt:
1. **Telegram Owner** = cửa người→Hermes đã có.
2. **Git assignment + cron/script-gate** = backstop 24/7, 0-token khi không có việc.
3. **Built-in Hermes webhook** = cửa máy→máy từ Internet, đặt sau nginx HTTPS hiện hữu, HMAC + replay protection + filter + idempotency + rate-limit; webhook **chỉ fire đúng cron job dispatcher**, không cho payload ngoài trở thành prompt tự do.
4. **Hermes API Server trực tiếp** giữ loopback/trusted-only trong HJW.3. Không public OpenAI-compatible API đầy đủ cho tới khi có profile/toolset/API key riêng đủ hẹp; API Server có blast radius lớn hơn webhook dispatcher.
5. Tất cả trigger hội tụ vào **một dispatcher/assignment contract**, không tạo SSOT thứ hai.

JEV Host: `gen-dec-1790241698-LNju0s9zxYbOrssd8idg` → WEBHOOK_PLUS_CRON 0.74.

## 1. Bằng chứng đã PASS — KHÔNG LÀM LẠI

Chấp nhận từ HJW.2C + SELF01:
- Agent Data auth patch + generic Agent Gateway PASS.
- Hermes narrow credential/profile PASS; master Agent Data key không quay lại Hermes.
- Hermes thấy đúng 7 workspace tool; read toàn root `workspace`, write chỉ HJW; root khác DENY.
- trusted Git author = `agent-gw/hermes`; revoke/restore + reversible write PASS.
- P18 = **LLM Hermes thật** đã tự đọc AGENTS/COLLAB, tự dùng MCP, tự ghi P18 và đóng assignment; Claude P19 xác minh author thật.
- `workspace_result_read` không cần mở: file dài dùng `start_char`; search/log có cursor riêng.
- T1 đọc, T3 cross/version evidence, T4 identity/attribution coi là PASS evidence; không chạy lại trừ regression.
- A9 đã map riêng `agent-gw/hermes → Hermes`.

## 2. Read-gate trước mutation

1. Đọc `AGENTS.md → root COLLAB.md → HJW COLLAB.md → PROMPT.md`; kiểm A0 và READY full SHA.
2. Kiểm Agent Data/Hermes sau mọi thay đổi song song:
   - Agent Data healthy; current HEAD/worktree ghi lại;
   - source/current runtime vẫn có `/mcp-agent` generic + Hermes profile;
   - từ Hermes live session/relay: `tools/list` vẫn đúng 7;
   - `AGENT_DATA_*` vẫn vắng ở serve+gateway;
   - `hermes-safe-update health` PASS.
   Nếu contract 2C bị regression bởi phiên khác ⇒ DỪNG trước HJW.3 mutation.
3. Inventory thực tế:
   - Hermes version + `hermes cron --help/status/list/doctor`;
   - existing `~/.hermes/scripts/` và cron jobs; **reuse trước khi tạo**;
   - webhook platform hiện trạng; port/listener conflict;
   - API Server bind/auth hiện trạng (dự kiến loopback);
   - Telegram connected + allowed Owner;
   - nginx public HTTPS config hiện hữu;
   - Kuma monitor/push path hiện hữu;
   - safe-update timer/lock và các restart gần đây.
4. Nếu chỉ gặp timeout/refused/502/503 do phiên khác restart service: giữ checkpoint, không mutation, retry backoff tối đa ~5 phút như OP-NOTE; không tự chữa bằng restart ngoài PROMPT.

## 3. Assembly First / quyền tạo runtime tối thiểu

- **CẤM tạo repo task/project/file mới.**
- Ưu tiên config/feature có sẵn của Hermes/nginx/Kuma.
- Owner 24/09 đã yêu cầu kết nối 24/7/API ở mức tốt nhất: RUN này được phép tạo **tối đa một runtime dispatcher script** dưới `~/.hermes/scripts/` nếu inventory chứng minh không có script hiện hữu tái dùng được. Tên + hash + owner/mode phải ghi evidence.
- Không tạo server/service public mới. Webhook là adapter có sẵn trong `hermes-gateway`, bind loopback; public qua nginx hiện hữu.
- Không tạo GitHub webhook thứ hai trong RUN này. Git assignment dùng cron/backstop; generic webhook dành cho external systems hiện tại/tương lai.
- Không cấp thêm workspace tool; không mở `workspace_result_read`, exec/task/terminal cho profile Agent Gateway Hermes.

## 4. G1 — Một dispatcher 24/7, fail-closed

### G1.1 Assignment SSOT
Dùng đúng:
`ASSIGN@<ID> · to=Hermes · role=<Reviewer|Agent|Host> · scope=<path> · state=<open|claimed|blocked|done> [· run=<RUN_ID>]`

Luật:
- `COLLAB.md` tại Git HEAD xác định là SSOT; derived view không quyết định quyền.
- Reviewer: không cần RUN nhưng chỉ đúng scope.
- Agent: chỉ wake/làm khi có `run=<RUN_ID>`, PROMPT hiện hành có READY@ đúng SHA và assignment do Owner/GPT Host mở.
- Host: chỉ khi Owner giao.
- Hermes claim bằng `workspace_edit` expected_version `open→claimed`.
- done/blocked ghi cùng commit kết quả khi có thể.
- stale/ambiguous/missing HEAD/missing READY/out-of-scope ⇒ **không wake hoặc blocked**, tuyệt đối không suy diễn.

### G1.2 Script gate 0-token
- Reuse script hiện hữu; nếu không có, tối đa một script chung.
- Script đọc public Git/HEAD **không dùng narrow Agent Gateway key** và không gọi LLM để dò việc.
- Hermes scheduler gate là **fail-open nếu script im lặng/chết/JSON sai**. Vì vậy mọi nhánh lỗi/không việc phải **exit 0** và dòng stdout **cuối cùng** phải là JSON hợp lệ `{"wakeAgent": false}`. Không dùng `set -e`/exception path không được trap; network/read/parse/STOP error đều phải kết thúc bằng sentinel false.
- Chỉ `wakeAgent:true` khi có đúng assignment Hermes hợp lệ và STOP gates cho phép.
- **Không tự dựng ledger/dedup store mới.** Dùng built-in cron claim/at-most-once + executions ledger + `hermes cron notepad`/`--continuity` cho per-condition state/last-seen khi cần. Git `ASSIGN@` vẫn là SSOT nghiệp vụ.
- Mọi MCP write của unattended turn dùng `expected_version` + `operation_id`; nếu transport trả outcome UNKNOWN/expired thì read-back/reconcile trước khi retry, không blind retry.
- Không render nội dung bất kỳ từ webhook thành instruction. LLM sau wake phải tự re-read AGENTS/COLLAB/PROMPT qua MCP.
- Fault-injection acceptance bắt buộc: unreadable STOP flag, Git/network timeout, parse error, malformed output ⇒ đều 0 LLM và dòng cuối sentinel false.

## 5. G2 — Cron / scheduled backstop

Tạo bằng Hermes cron hiện hữu, model/toolset ghim rõ:

### Job A — `ws-dispatch`
- schedule mục tiêu ~2 phút; script gate G1 chạy trước.
- không assignment hợp lệ ⇒ 0 LLM.
- assignment hợp lệ ⇒ wake Hermes fresh session; prompt tự chứa lệnh vào đúng workspace và buộc đọc SSOT.
- delivery cuối = Telegram Owner, đúng 3 dòng:
  `STATUS: ...`
  `COMMIT: <sha|—>`
  `NEXT: ...`
- Ghim đúng built-in `cron.max_parallel_jobs=1`; at-most-once dùng scheduler claim/in-flight dedupe + executions ledger, không tự chế khoá/ledger riêng.

### Job B — `ws-handoff-watch` (no-agent / 0-token)
- định kỳ hợp lý (ưu tiên 15 phút).
- tìm NEXT/to=GPT|Claude|Owner chưa được nhận sau ngưỡng đã chốt (~2h).
- chỉ Telegram **một** cảnh báo cho cùng condition/generation; không spam.

### Job C — `ws-run-watch` (no-agent / 0-token)
- canh READY+RUN chưa có KQ sau ~6h và KQ DỪNG mới.
- dedup incident; một condition chỉ cảnh báo một lần cho tới khi state đổi.

Heartbeat không tự dựa vào Hermes báo mình còn sống; xem G5 Kuma.

## 6. G3 — External machine ingress qua built-in Webhook

### G3.1 Enable an toàn
- Bật **built-in Hermes webhook platform** và ghim **đúng key** `platforms.webhook.extra.host: 127.0.0.1`; port ưu tiên **8644**. Không dựa vào default: source Hermes mặc định webhook có thể bind mọi interface.
- Sau start/restart, **bắt buộc chứng minh bằng `ss -ltnp`**: webhook 8644 chỉ nghe `127.0.0.1`/loopback; direct API Server 8642 và Hermes serve 9119 cũng chỉ loopback. Bất kỳ `0.0.0.0`/`::` trên các cổng này, hoặc không chứng minh được socket ⇒ **DỪNG trước public test**.
- Đồng thời audit nginx: **không có route public cũ trỏ tới direct API Server `/v1/*`/8642 hoặc serve 9119**. Chỉ route webhook hẹp mới được public trong RUN này.
- Secret nằm trong root-managed env material hiện hữu, config chỉ dùng env substitution; **không plaintext**.
- Public HTTPS đi qua **nginx hiện hữu**, path riêng hẹp; không publish raw port.
- Rate limit phải **ghi số tường minh ở cả hai tầng**: Hermes webhook adapter `rate_limit: 30` request/phút/route; nginx public webhook hiệu dụng tối đa **30 request/phút/source**, burst tối đa **5**. Reuse zone hiện hữu nếu rate của zone ≤30/phút; nếu zone nhanh hơn thì tạo/chỉnh route-specific limit trong nginx hiện hữu, không server mới.
- nginx: TLS hiện hữu, body limit, rate-limit; `nginx -t` trước reload.
- Telegram Owner một dòng trước restart/reload ảnh hưởng gateway/nginx.

### G3.2 Một route generic “đánh chuông”, không prompt injection
- Route external = `incomex-dispatch`, chạy dưới **profile Hermes hiện hành `default`** trong HJW.3. Agent tương lai phải có profile/route namespace/job/credential riêng; không dùng route Hermes chung.
- Generic **HMAC V2** + timestamp/replay protection; không dùng V1.
- filter allowlist event/source; max body ≤ Hermes default hoặc thấp hơn.
- idempotency/delivery id bắt buộc ở test; cache webhook chỉ là lớp đầu, **scheduler claim mới là chốt dedupe bền**.
- route dùng **`cron_job: ws-dispatch`**, không start independent agent session.
- **Template route phải là literal fixed text**, ví dụ “External wake signal received; re-read Git SSOT and act only on a valid assignment.” **CẤM mọi biến/template lấy từ body/header/query/payload.** Route name/profile/event allowlist là config cố định; không render user-supplied text.
- Dù Hermes internally tạo `event_context/extra_prompt`, context của route này không được chứa nội dung payload ngoài; dispatcher khi chạy luôn re-read Git SSOT để quyết định có assignment hay không.
- **Negative canary test bắt buộc:** gửi request HMAC hợp lệ có body/header/query chứa chuỗi duy nhất + instruction giả (ví dụ `HJW_CANARY_IGNORE_PREVIOUS_<nonce>`). Chứng minh canary **không xuất hiện** trong run prompt/context, model output, Telegram delivery hoặc application log của lượt; xuất hiện ở bất kỳ nơi nào ⇒ **DỪNG/rollback webhook route**.
- unknown event/filter miss/invalid signature/expired timestamp/duplicate ⇒ 0 LLM.

### G3.3 External acceptance
Từ máy ngoài VPS (ưu tiên chính Mac/Claude Code):
1. missing/wrong signature ⇒ reject, 0 run;
2. expired V2 timestamp ⇒ reject;
3. valid signed event, không assignment ⇒ accepted/ignored nhưng 0 LLM;
4. same delivery id gửi lại ⇒ dedup, không run thứ hai;
5. rate-limit burst ⇒ với adapter 30/phút/route + nginx ≤30/phút/source (burst ≤5), vượt ngưỡng phải có 429; ghi số request/401/2xx/429 thực tế, gateway/master routes khác không ảnh hưởng;
6. valid event + một assignment HJW test đã Host arm ⇒ fire **chính ws-dispatch**, claim đúng một lần, không duplicate.

## 7. G4 — Telegram Owner / T5 thật

T5 chỉ PASS khi **không người gọi trực tiếp phiên Hermes để làm việc**.

Sau hạ tầng G1–G3 PASS, Host sẽ arm một assignment test trong HJW. Agent Claude Code **không tự tạo assignment thay Host** nếu chưa có dòng arm sẵn.

Acceptance:
- assignment `state=open` tồn tại trên Git;
- hoặc webhook hợp lệ fire ws-dispatch, hoặc cron backstop tự phát hiện;
- Hermes **tự thức**;
- LLM Hermes tự đọc AGENTS → HJW COLLAB → prompt/assignment;
- claim `open→claimed`;
- dùng chính 7 MCP tools để làm một việc reviewer an toàn trong HJW;
- commit author phải là `agent-gw/hermes`;
- state→done/blocked;
- Job prompt phải ép **exactly 3 non-empty lines, không code fence/không lời mở đầu-kết**:
  `STATUS: ...`
  `COMMIT: <sha|—>`
  `NEXT: ...`
- Nghiệm thu trên **tin nhắn Telegram thực tế Owner nhận** (hoặc delivery log raw tương đương), không dùng model output nội bộ làm bằng chứng. Thừa/thiếu dòng hoặc thêm prose ⇒ T5 FAIL.
Không được harness/shell làm thay LLM.

Đo:
- webhook path: event→claim latency;
- cron-only path: assignment→claim latency; mục tiêu ≤5 phút với 2-min backstop.

## 8. G5 — STOP + heartbeat độc lập

### STOP-AUTO
- Normal operator stop không trao root cho Hermes.
- Dùng trạng thái/flag vận hành đã thiết kế để mọi scheduled HJW wake trả false; pause cron nếu phù hợp.
- Resume không được chạy bù duplicate.

### STOP-DISPATCH
- Root-owned flag ngoài quyền ghi user Hermes nhưng **phải world-readable** cho user/process Hermes (ví dụ root:root mode 0644; không writable bởi Hermes). Mọi HJW script gate phải kiểm.
- **Không đọc/stat được flag = coi như STOP đang BẬT**. Mọi lỗi permission/I/O/parse ở bước STOP phải fail-closed: dòng stdout cuối `{"wakeAgent": false}` + exit 0.
- flag ON ⇒ cron + webhook-triggered dispatcher đều 0 agent run.
- Hermes không tự gỡ/sửa flag. Acceptance phải test flag ON, flag unreadable/error giả lập và flag OFF.

### HARD-STOP
- Đường root/operator dừng gateway/service khi compromise; không giao Hermes tự tắt chính mình.
- Test rõ run mới bị chặn và state của run in-flight.

### Kuma
- Reuse Kuma root-owned monitor/path hiện hữu.
- monitor Hermes/gateway independent of Hermes credential.
- chứng minh khi Hermes/gateway chết, Owner nhận Telegram ≤10 phút.
- token Kuma không đưa cho Hermes.

## 9. G6 — T2/T6 và cost/observability

### T2
Không tạo fixture mới. Dùng assignment reviewer/Agent an toàn trên file hiện hữu HJW để chứng minh:
- read current version;
- write scoped;
- stale expected_version bị reject hoặc evidence version guard hiện hữu được tái dùng;
- conflict ⇒ read lại/hòa giải, không overwrite;
- no out-of-scope commit.

### T6
Cho ít nhất một LLM turn auto-wake thật:
- ghi model/provider/reasoning profile;
- token usage/cost nếu Hermes execution ledger/API response hiện có hỗ trợ;
- nếu chỉ có token mà không có giá chính xác, báo token + model, không tự suy giá.
**D10 giữ nguyên:** budget/hard cap ngoài scope, T6 chỉ đo.

### Observability
- `hermes cron status/runs/incidents/doctor`;
- executions ledger;
- nginx webhook logs chỉ metadata, không body/secret;
- Git author + assignment lifecycle;
- Telegram incident dedup;
- current config hash/before-after + rollback.

## 10. Direct API Server — giữ capability nhưng không public trong RUN này

- Xác nhận local API Server health/auth và **chứng minh socket thật bằng `ss -ltnp`**: API 8642 và serve 9119 chỉ loopback; không chỉ tin default/config.
- Audit nginx để chứng minh **không có route public cũ** trỏ tới 8642/9119 hoặc `/v1/*`.
- **Không thêm nginx public route cho `/v1/*` trong HJW.3.**
- Lý do: direct API Server mang Hermes agent/toolset rộng hơn dispatcher webhook.
- NEXT sau HJW.3 có thể mở direct external API bằng **profile/toolset/API key riêng**, có concurrency/idempotency/rate-limit và acceptance riêng. Không dùng default profile public.

## 11. T10 acceptance matrix

PASS chỉ khi:
1. 15 phút không assignment/event ⇒ dispatcher 0 LLM; no wake thừa.
2. Git assignment open ⇒ cron tự wake/claim ≤5 phút.
3. external valid signed webhook + assignment ⇒ immediate fire cùng dispatcher; duplicate không duplicate run.
4. invalid/expired/filter-miss webhook ⇒ 0 LLM; signed negative-canary payload không xuất hiện ở prompt/context/output/log.
5. two triggers chen nhau ⇒ một claim/run.
6. blocked condition ⇒ Git state + Telegram Owner; không auto-approve.
7. handoff watcher và RUN watcher dedup, không spam.
8. STOP-AUTO/STOP-DISPATCH ⇒ 0 run mới; resume không chạy bù trùng.
9. HARD-STOP service boundary hoạt động; rollback rõ.
10. Kuma báo khi Hermes/gateway chết ≤10 phút.
11. auto LLM turn ghi bằng `agent-gw/hermes`, write ngoài HJW vẫn DENY.
12. Telegram completion **tin nhắn thực tế** đúng chính xác 3 dòng STATUS/COMMIT/NEXT, không prose thêm.
13. T6 model/token/cost evidence có mức thật, không đoán.
14. `ss -ltnp` chứng minh webhook 8644 + API 8642 + serve 9119 chỉ loopback; nginx không expose direct API/serve; direct API Server not newly public.
15. Agent Data 7-tool Hermes contract + existing GPT/Claude clients không regression.

## 12. Rollback

- Webhook fail: disable webhook route/platform + nginx route; cron backstop vẫn chạy.
- Cron job fail: pause/remove đúng HJW jobs; Agent Gateway/Telegram manual vẫn giữ.
- Dispatcher script fail: rollback hash/script, job fail-closed `wakeAgent:false`.
- Hermes config fail: restore exact config before + restart serve→gateway theo thứ tự đã nghiệm thu.
- Secret fail: revoke external webhook secret; không rotate unrelated secrets.
- Không rollback Agent Gateway HJW.2C nếu không phải nguyên nhân.

## 13. Báo cáo

Chỉ cập nhật file hiện hữu:
- `COLLAB.md`: KQ + assignment test + latencies + PASS/FAIL T2/T5/T6/T10.
- `view.html`: Owner summary: các cửa vào 24/7, stop controls, known limits.
- evidence nhạy cảm: append hồ sơ root-only hiện hữu.

Ghi rõ:
- cron jobs + cadence;
- public webhook path ở mức không lộ secret;
- signature mode;
- external test result;
- self-wake commit author;
- Telegram result;
- no-wake window;
- model/token/cost;
- Kuma test;
- rollback state.

## CẤM

- Không tạo task/project/repo file mới.
- Không public raw port 8644/9119.
- Không public default/full Hermes API Server.
- Không đưa webhook payload tự do trực tiếp vào LLM prompt.
- Không thêm GitHub webhook thứ hai trong RUN này.
- Không cấp Hermes sudo/root/GSM broad access/master Agent Data key.
- Không mở thêm workspace tools.
- Không auto-approve production/root action từ unattended turn.
- Không để webhook/cron bypass READY/RUN cho role=Agent.
- Không thay Owner/Founders contract.
- Không tự onboard agent thứ hai trong RUN này.

## AP-CLOSE

- `KQ@HJW-3-20260924-01 XONG` chỉ khi T2/T5/T6/T10 và rollback/observability PASS.
- DỪNG nếu: gateway 2C regression; webhook không thể bind loopback + expose qua existing nginx an toàn; secret phải plaintext; script gate có nhánh lỗi wake=true; direct external payload có thể thành arbitrary instruction; assignment/READY/RUN không enforce; no-agent window vẫn gọi LLM; STOP/HARD-STOP/Kuma không chứng minh được; hoặc rollback không sạch.
- Agent báo XONG không đồng nghĩa DONE; Host + Reviewer nghiệm thu.
