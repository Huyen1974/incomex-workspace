# PROMPT — HJW.2C · Generic Agent Gateway + Auth Patch

RUN_ID: HJW-2C-20260924-01
STATUS: DRAFT — KHÔNG RUN cho tới khi Reviewer ACCEPT và Host ghi READY@ đúng SHA cuối chạm file này

Executor_Surface: Claude Code CLI trên Mac
Runtime_Write_Path: SSH/root-operator tới VPS; Agent Data source/runtime trên VPS là SSOT
Report_Write_Path: chỉ cập nhật file hiện hữu `work/hermes-joint-workspace/COLLAB.md` + `view.html` và evidence root-only hiện hữu `CAP-PATH-AUDIT.md`
Work: `work/hermes-joint-workspace/`

## Mục tiêu

Theo Owner 24/09:
1. **Gate 0:** vá tận gốc lớp authentication MCP của Agent Data trước khi bật đường agent mới.
2. Tạo **một Agent Gateway generic** từ Agent Data tới GitHub/workspace cho Hermes và agent tương lai; không tạo route riêng từng agent.
3. Mỗi credential xác định một profile server-side: `agent_id`, tool allowlist, allowed roots, read scope, write scope và trusted attribution.
4. Hermes là profile production đầu tiên. Claude Code/agent khác **chưa migrate trong RUN này**; test phải chứng minh thêm profile sau chỉ cần config + credential, không cần route code mới.
5. Không đưa master `API_KEY` cho Hermes/agent mới; không tin `clientInfo`/User-Agent để cấp quyền hoặc xác định identity.

JEV Host: `gen-dec-1790217958-q1i8W3GQZj6EZBKY6cMG` → GENERIC_AGENT_GATEWAY 1.00.

## Checkpoint / read-gate

- Đọc `AGENTS.md → COLLAB.md → PROMPT.md`; kiểm A0 Owner 24/09 đã xác nhận.
- Kiểm `READY@<SHA>` đúng commit cuối chạm PROMPT trước mutation.
- Đọc `KQ@HJW-2B1-20260923-02 XONG` và evidence root-only hiện hữu `/opt/incomex/work/hermes-joint-workspace/HJW-2B1-20260923-02/CAP-PATH-AUDIT.md`.
- Agent Data phải clean worktree; ghi branch + HEAD trước mutation. VPS source/runtime là SSOT: **không pull/deploy từ GitHub xuống VPS**.
- Xác nhận `incomex-agent-data` healthy và public Agent Data HTTP sống.
- Chụp baseline cho **từng master MCP profile hiện hữu** (`/mcp`, `/mcp-readonly`, `/mcp-gpt`, `/mcp-gpt-full`): `tools/list` names/count + connectorSchemaVersion/hash + serverInfo. Dùng để so exact sau G0/G1.
- Xác nhận HJW.2B1 vẫn đúng: `AGENT_DATA_API_KEY/AGENT_DATA_URL` vắng trong `/run/hermes/or.env` và env của cả `hermes-serve` + `hermes-gateway`. **Không gỡ lại, không cấp lại master key.**
- Pre-flight Hermes: xác định service serve/gateway đang dùng venv nào; trong đúng venv đó phải import được MCP client/`mcp.client.streamable_http`. Không chứng minh được ⇒ DỪNG trước deploy Hermes.
- **TUYỆT ĐỐI KHÔNG TẠO FILE/TASK/PROJECT MỚI.** Chỉ sửa source/config/test file hiện hữu. Nếu bắt buộc cần file mới ⇒ DỪNG xin Owner.
- Không copy exact exploit/auth bypass, secret value, token/hash secret vào repo/chat/public log. Chi tiết vulnerability chỉ ở evidence root-only.
- Không chạm Qdrant/OpenRouter/Telegram/GSM ngoài narrow credential cần cho gateway. Không tạo Google project/service mới.

## G0. AUTH PATCH — BẮT BUỘC PASS TRƯỚC GATEWAY

### G0.1 Caller inventory trước breaking change
- Trước khi đóng legacy `POST /mcp/tools/{tool_name}`, đọc log Agent Data/nginx trong **7 ngày gần nhất** (hoặc toàn bộ retention nếu <7 ngày), chỉ lấy metadata an toàn: thời điểm, route, caller/client/UA đã sanitize, tool name; **không in body/params**.
- Nêu caller thật đang dùng legacy route cho Owner trong evidence root-only + COLLAB mức không nhạy cảm.
- Có caller thật/chưa xác định được caller, hoặc retention quá ngắn khiến không thể đánh giá an toàn ⇒ **DỪNG trước mutation** để Owner quyết.

### G0.2 Vá theo cấu trúc, không vá một dòng
- Đọc exact finding root-only và đối chiếu source.
- Root cause phải được xử lý: auth của route MCP **không được chỉ nằm trong thân handler**.
- Mọi route externally reachable có thể đi tới `_dispatch_mcp_tool` phải khai **auth policy ở route/dependency/common guard trước dispatch**:
  - master MCP routes/legacy ⇒ master auth;
  - generic `/mcp-agent` ⇒ agent-profile auth;
  - không route dispatch nào được “quên auth”.
- Thêm regression/invariant vào **test file hiện hữu**: liệt kê toàn bộ route MCP có thể dispatch tool và fail nếu route không có auth policy declared tương ứng.
- Legacy `POST /mcp/tools/{tool_name}` phải auth trước đọc body/dispatch.
- Bỏ/redact dòng log legacy đang ghi nguyên request params/body; chỉ log metadata an toàn sau auth.
- Missing/invalid credential trả lỗi generic cùng lớp; không phân biệt chi tiết giúp dò credential.
- Không vá bằng đóng toàn service hoặc rotate master key nếu không cần.

### G0.3 Regression + deploy
Bổ sung vào test file hiện hữu:
- missing/invalid master key trên legacy/bypass cũ ⇒ 401/403 trước handler;
- valid master key trên master routes vẫn PASS;
- invariant route-auth PASS;
- log/test output không chứa body/secret/exploit detail.

FAIL ⇒ rollback source, `KQ DỪNG`; **không viết G1**.

Nếu PASS:
- commit G0 riêng trong repo Agent Data từ VPS SSOT;
- trước production restart gửi Owner một dòng Telegram; không gửi được ⇒ DỪNG;
- deploy bằng cơ chế hiện hữu, không tạo service/port/listener;
- smoke: container healthy; baseline master profile tools/schema/serverInfo **khớp exact**; Full All 2/public contract sống; bypass cũ missing/invalid key bị chặn.
Regression đỏ ⇒ rollback G0 runtime/commit rồi DỪNG.

## G1. GENERIC AGENT GATEWAY — một route, nhiều profile

Chỉ bắt đầu sau G0 production PASS.

### G1.1 Profile registry — tái dùng config hiện hữu
- Tái dùng file mà `WORKSPACE_CONFIG` đang trỏ tới; **không tạo config file mới**.
- Thêm registry chung `agent_profiles` (tên field có thể điều chỉnh):
  - `agent_id` canonical;
  - `credential_env` = **tên** env chứa credential, không secret value;
  - `allowed_tools`;
  - `allowed_roots`;
  - read scope;
  - write scope;
  - attribution label nếu cần.
- Secret thật ở secret/env material hiện hữu của Agent Data. Constant-time compare; missing env/config malformed/duplicate match ⇒ fail closed.
- **Không fallback sang master API_KEY** trên Agent Gateway.
- Thêm profile thứ hai trong test chỉ bằng config fixture/env; route code không đổi.

### G1.2 Một route generic + public hardening
- Tạo đúng **một route generic**, ưu tiên `POST /mcp-agent`.
- Không tạo `/mcp-hermes`, `/mcp-claude`…; agent mới chỉ thêm profile + credential/config.
- Reuse protocol/tool schema/filtered-handler logic hiện hữu; không fork MCP implementation.
- Reuse nginx/API port hiện hữu. Không mở port/listener/service mới.
- Nếu public `/api/mcp-agent` cần nginx config: chỉ sửa config hiện hữu, `nginx -t` trước reload.
- Public route phải có rate-limit bằng cơ chế nginx hiện hữu và auth error generic, không phân biệt missing vs wrong credential.
- MCP sampling cho Hermes gateway phải **disabled** trong config client nếu syntax hiện hữu hỗ trợ; pre-flight xác nhận config parse được.

### G1.3 Trusted identity + attribution
- Credential hợp lệ ⇒ server xác định `agent_id` từ profile.
- Với Agent Gateway, effective identity/attribution/presence/Git author lấy từ authenticated profile, **không** từ `clientInfo`/User-Agent/header tự khai.
- Reuse ambient identity hiện hữu (`hvu_signals`/contextvar) nếu phù hợp: route agent đặt trusted identity trước dispatch; `hvu_signals.author_args()` phải thấy identity trusted này.
- Forged `clientInfo` không đổi effective identity.
- Identity/profile context phải tới được choke point scope.
- **Global deny trong HJW.2C cho agent profiles:** `task_*`, `workspace_exec*` và mọi background/queued tool chưa được cấp. Chỉ mở ở RUN tương lai sau khi chứng minh policy/identity được bind qua queue/status/cancel. Không để config profile tự override deny này.

### G1.4 Tool + root + path scope — server-side
- Enforce tool allowlist trước argument validation/dispatch.
- Enforce root/path ở **một choke point chung** của workspace tool dispatch; master callers không có authenticated agent profile thì giữ behavior hiện hành.
- Agent profile lookup từ trusted ambient `agent_id`; mỗi call reload/đọc policy an toàn từ registry hiện hữu hoặc cache có invalidation rõ.
- `allowed_roots` phải được enforce trước root_spec dispatch.
- Read và write scope tách riêng; component-aware prefix.
- Tool có `path/from/to/operations` nested phải kiểm toàn bộ đường liên quan; không chứng minh được ⇒ deny.
- Raw MCP/HTTP không bypass scope.
- Queue/background tools bị deny như G1.3 cho tới khi có binding riêng.

### G1.5 Hermes profile đầu tiên
Production Hermes:
- `allowed_roots = ["workspace"]`.
- **Read = toàn bộ root `workspace`**. Đây là repo workspace dùng chung; read không phải security boundary của RUN này.
- **Write = chỉ `work/hermes-joint-workspace/**`**.
- Tool allowlist đầu: `workspace_list, workspace_read, workspace_search, workspace_stat, workspace_log, workspace_diff, workspace_edit`.
- Không cấp `workspace_write_new`, transaction, move/copy, import/upload/restore, task_*, exec, delete, UI, `vps_status`.
- Hệ quả cố ý: Hermes không tạo file mới; KQ/báo cáo phải cập nhật file hiện hữu.
- `workspace_result_read` **không cấp mặc định trong HJW.2C** vì state/result hiện tại chưa bind authenticated profile. Live test phải đo khả năng đọc file dài bằng `workspace_read` cửa sổ nhỏ + cursor. Nếu không thể đọc đầy đủ mà không dùng result_read ⇒ DỪNG và báo Host; không expose continuation dùng chung không identity-bound.
- Master key Agent Data đã gỡ ở HJW.2B1 và **không quay lại** env Hermes.

### G1.6 Narrow credential Hermes
- Tạo narrow credential đủ mạnh; không in/log.
- Server copy vào secret/env material **hiện hữu** của Agent Data theo `credential_env`.
- Client copy materialize bằng cơ chế root-managed hiện hữu vào `/run/hermes/or.env` dưới tên riêng, ví dụ `HERMES_AGENT_GW_KEY`; không plaintext trong `config.yaml`.
- Không cấp GSM broad access cho Hermes.
- Không tạo persistent secret file mới. Nếu hạ tầng hiện hữu không chứa được credential mà phải tạo file/resource mới chưa được Owner duyệt ⇒ DỪNG.
- Sau materialization, xác nhận bằng **tên biến**: narrow key có mặt; `AGENT_DATA_API_KEY/AGENT_DATA_URL` vẫn vắng. Không in value.

### G1.7 Deploy phía Hermes — bắt buộc
- Sửa `config.yaml` hiện hữu để thêm đúng một `mcp_servers` entry trỏ generic gateway qua relay/public path đã chọn; header lấy từ env expansion narrow key; sampling disabled.
- Trước restart: gửi Owner một dòng Telegram nói serve + gateway/desktop có thể gián đoạn; không gửi được ⇒ DỪNG.
- Restart **`hermes-serve` trước → verify local status**, rồi **`hermes-gateway` → verify Telegram connected**.
- Gọi thật `tools/list` từ Hermes và xác nhận đúng allowlist 7 tool, không có tool cấm/result_read.
- Rollback phía Hermes nếu fail: bỏ entry mcp_servers + narrow key materialization bằng source hiện hữu, regenerate env an toàn, restart serve → gateway; Agent Data G0-good vẫn giữ.
- Không restart `hermes-key.service` nếu unit dependency có thể bounce hai service; dùng source command trực tiếp theo pattern đã nghiệm thu 2B1.

## G2. TEST — dùng file hiện hữu, không tạo fixture mới

### G2.1 Unit/regression
Bổ sung vào **test files hiện hữu**:
1. route-auth invariant cho toàn bộ dispatch-capable MCP routes;
2. hai agent profile giả lập, credential khác nhau; profile thứ hai chỉ thêm config/env;
3. key A không dùng được profile/scope B; invalid/no key fail closed;
4. tool ngoài allowlist không xuất hiện `tools/list` và `tools/call` reject trước dispatch;
5. allowed_roots: `workspace` PASS; `agent-data/ui/docs` DENY;
6. write trong HJW PASS; write ngoài HJW DENY; prefix collision `work/hermes-joint-workspace-x` cũng DENY;
7. forged `clientInfo` không đổi authenticated agent_id/Git attribution;
8. agent profile không thể cấp task_*/exec qua config trong RUN này;
9. master routes baseline tools/schema/serverInfo exact PASS;
10. legacy route log không còn body/params nhạy cảm.

### G2.2 Live Hermes
Sau G0/G1 deploy:
- no/invalid/master key trên `/mcp-agent` ⇒ reject generic;
- narrow Hermes key ⇒ `tools/list` đúng 7 tool;
- đọc `AGENTS.md` và một task khác dưới `work/` PASS;
- thử root khác `agent-data` ⇒ DENY trước content;
- gọi tool cấm ⇒ DENY;
- **long-read measurement:** Hermes đọc toàn bộ `work/hermes-joint-workspace/COLLAB.md` bằng `workspace_read` với cửa sổ nhỏ + cursor, xác nhận tới EOF/total_chars. Không đọc hết được ⇒ DỪNG; không tự cấp result_read.
- **write thật reversible:** dùng `view.html` hiện hữu, không dùng `COLLAB.md`. Trước test lưu hash + bytes local; chọn lúc worktree sạch/vắng writer; báo Owner marker có thể xuất hiện 1–2 commit. Edit marker tối thiểu → kiểm commit attribution authenticated Hermes → revert bằng edit thứ hai. Revert conflict: retry giới hạn; vẫn fail ⇒ khôi phục bytes local theo cơ chế hiện hữu rồi DỪNG. Hash cuối phải bằng hash đầu.
- write ngoài HJW ⇒ DENY, 0 diff;
- forged client name vẫn attribution Hermes;
- revoke/disable Hermes profile/key ⇒ access fail; restore profile/key ⇒ PASS, client khác không ảnh hưởng.

### G2.3 Public/local + backward compatibility
- Test route Hermes qua path thực tế (relay 6533 nếu dùng) và public `/api/mcp-agent`; không mở port mới.
- Public route rate-limit hoạt động mà không làm ảnh hưởng master profiles.
- Run acceptance hiện hữu cho Full All 2/public route.
- So baseline vs after cho từng master profile: tool names/count + schema version/hash + serverInfo phải exact như trước.

## G3. DEPLOY / ROLLBACK

- Agent Data source VPS là SSOT; build/deploy bằng cơ chế hiện hữu. Không force/rebase/pull code từ GitHub xuống.
- G0 và G1 dùng commit riêng.
- Trước mỗi production restart/reload ảnh hưởng service: clean worktree/expected HEAD + Telegram Owner; không gửi được ⇒ DỪNG.
- G1 fail: rollback G1 về G0-good, disable/revoke Hermes profile/key, rollback Hermes mcp entry; **không** trả master key.
- G0 regression: rollback G0 và DỪNG; không gateway.
- Không thay/chạm plugin Full All 2 ngoài regression cần thiết.

## Nghiệm thu bắt buộc

PASS chỉ khi:
- AUTH-STRUCTURAL: mọi dispatch-capable MCP route có declared auth policy; bypass root-only đóng.
- LEGACY-CALLER-CHECK: caller inventory đã làm; không breaking caller chưa duyệt.
- LOG-SAFE: legacy không log raw body/params.
- EXISTING-CLIENTS-PASS: baseline master tools/schema/serverInfo exact + Full All 2 PASS.
- GENERIC: một route code phục vụ ≥2 profile test config.
- PER-AGENT-AUTH: credential riêng, no shared master/fallback.
- TOOL-SCOPE + ROOT-SCOPE + WRITE-SCOPE: server-side, outside denied.
- TRUSTED-IDENTITY: credential → agent_id → attribution; forged clientInfo vô hiệu.
- NO-BACKGROUND-BYPASS: task/exec globally denied cho agent profiles ở RUN này.
- HERMES-FIRST: deploy client, tools/list, full long-read, reversible write + attribution, outside deny PASS.
- REVOCABLE: revoke profile/key fail closed, client khác không ảnh hưởng.
- NO-NEW-FILE: không project/task/source/test/config file mới.
- SECRETS: no plaintext secret/exact exploit detail public.
- SAMPLING-OFF + PUBLIC-RATE-LIMIT: Hermes sampling disabled; public agent route throttled.

## Báo cáo

- Cập nhật **chỉ** `COLLAB.md` và `view.html` hiện hữu.
- Evidence nhạy cảm append vào **CAP-PATH-AUDIT.md hiện hữu root-only**; không tạo evidence file mới.
- Ghi before/after Agent Data commit, G0 caller inventory kết luận, tests, deploy health, schema/hash regression, Hermes live result, rollback/revoke state.
- Nếu PASS: NEXT = onboard agent thứ hai bằng profile/config trong RUN riêng; không tự migrate trong RUN này.

## CẤM

- Không tạo project/task/source/test/config/evidence file/service/port/listener mới.
- Không tạo route riêng từng agent.
- Không dùng shared key cho nhiều agent.
- Không dùng `clientInfo` làm authorization/trusted identity.
- Không đưa master Agent Data key/GSM broad access cho Hermes.
- Không mở Hermes write ngoài HJW.
- Không cấp task_*/exec/background tool cho agent profile trong RUN này.
- Không expose `workspace_result_read` nếu result state chưa bind authenticated profile.
- Không migrate Claude Code/agent khác production trong RUN này.
- Không log/copy secret hoặc exact bypass exploit vào repo/chat.
- Không tự tiếp tục automation Phase 1 sau KQ.

## AP-CLOSE

- `KQ@HJW-2C-20260924-01 XONG` chỉ khi toàn bộ nghiệm thu PASS.
- `DỪNG` nếu: legacy caller chưa được Owner xác nhận; G0 không đóng được structural auth; regression existing client; cần file/service/resource mới chưa được Owner duyệt; không tạo được narrow credential bằng secret path hiện hữu; scope/identity không enforce server-side; Hermes client preflight fail; long-read không đầy đủ; hoặc rollback không sạch.
- Agent báo XONG không đồng nghĩa DONE; Host phải nghiệm thu KQ/evidence.
