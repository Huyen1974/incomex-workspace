# PROMPT — HJW.2C · Generic Agent Gateway + Auth Patch

RUN_ID: HJW-2C-20260924-01
STATUS: DRAFT — KHÔNG RUN cho tới khi Reviewer ACCEPT và Host ghi READY@ đúng SHA cuối chạm file này

Executor_Surface: Claude Code CLI trên Mac
Runtime_Write_Path: SSH/root-operator tới VPS; Agent Data source/runtime trên VPS là SSOT
Report_Write_Path: chỉ cập nhật file hiện hữu `work/hermes-joint-workspace/COLLAB.md` + `view.html` và evidence root-only hiện hữu `CAP-PATH-AUDIT.md`
Work: `work/hermes-joint-workspace/`

## Mục tiêu

Theo Owner 24/09:
1. **Gate 0:** vá lỗ hổng authentication Agent Data đã phát hiện ở HJW.2B1 trước khi bật đường agent mới.
2. Tạo **một Agent Gateway generic** từ Agent Data tới GitHub/workspace cho Hermes và agent tương lai; không tạo route riêng từng agent.
3. Mỗi credential xác định một profile server-side: `agent_id`, tool allowlist, allowed roots, read prefixes, write prefixes và trusted attribution.
4. Hermes là profile production đầu tiên. Claude Code/agent khác **chưa migrate trong RUN này**; nhưng kiến trúc/test phải chứng minh thêm profile sau không cần sửa route code.
5. Không đưa master `API_KEY` cho Hermes/agent mới; không tin `clientInfo` để cấp quyền/đặt identity.

JEV Host: `gen-dec-1790217958-q1i8W3GQZj6EZBKY6cMG` → GENERIC_AGENT_GATEWAY 1.00.

## Checkpoint / read-gate

- Đọc `AGENTS.md → COLLAB.md → PROMPT.md`; kiểm A0 Owner 24/09 đã xác nhận.
- Kiểm `READY@<SHA>` đúng commit cuối chạm PROMPT trước mutation.
- Đọc `KQ@HJW-2B1-20260923-02 XONG` và **evidence root-only hiện hữu** `/opt/incomex/work/hermes-joint-workspace/HJW-2B1-20260923-02/CAP-PATH-AUDIT.md`.
- Agent Data hiện phải clean worktree; ghi branch + HEAD trước mutation. VPS source/runtime là SSOT: **không pull/deploy từ GitHub xuống VPS**.
- Xác nhận container `incomex-agent-data` healthy và public Agent Data HTTP sống.
- **TUYỆT ĐỐI KHÔNG TẠO FILE/TASK/PROJECT MỚI.** Chỉ sửa source/config/test file hiện hữu. Nếu test/rollback bắt buộc cần file mới ⇒ DỪNG xin Owner.
- Không copy chi tiết exploit/auth bypass, secret value, token/hash secret vào repo/chat/public log. Chi tiết vulnerability chỉ ở evidence root-only hiện hữu.
- Không chạm Qdrant/OpenRouter/Telegram/GSM ngoài đúng secret material cần cho narrow agent credential. Không tạo Google project/service mới.

## G0. AUTH PATCH — BẮT BUỘC PASS TRƯỚC GATEWAY

1. Đọc exact finding trong root-only `CAP-PATH-AUDIT.md` và tự đối chiếu source đang chạy.
2. Vá **tối thiểu** đường bypass đã đo; mọi externally reachable path có thể dispatch MCP tool ghi/exec/xoá phải auth **trước dispatch**.
3. Legacy `POST /mcp/tools/{tool_name}` phải yêu cầu auth hợp lệ trước đọc body/dispatch theo mức hợp lý; các route hiện hành `/mcp`, `/mcp-readonly`, `/mcp-gpt`, `/mcp-gpt-full` giữ contract/client hiện có.
4. Không “vá” bằng đóng toàn bộ service hoặc đổi master key nếu không cần.
5. Bổ sung regression vào **test file hiện hữu**:
   - missing/invalid key trên bypass cũ và legacy write-capable path ⇒ 401/403, handler không chạy;
   - valid master key trên route hiện hành vẫn PASS;
   - không leak route exploit/secret ra test output.
6. Chạy test G0. FAIL ⇒ rollback source, `KQ DỪNG`; **không viết G1**.
7. Nếu G0 test PASS: commit G0 riêng trong repo Agent Data từ VPS SSOT. Deploy bằng **cơ chế hiện hữu**, không tạo service/port/listener mới; trước restart Agent Data gửi Owner một dòng Telegram. Không gửi được ⇒ DỪNG trước restart.
8. Smoke sau deploy: container healthy; public master routes/Full All 2 contract sống; bypass cũ missing/invalid key bị chặn. Regression đỏ ⇒ rollback G0 commit/runtime rồi DỪNG.

## G1. GENERIC AGENT GATEWAY — một route, nhiều profile

Chỉ bắt đầu sau G0 production PASS.

### G1.1 Profile registry — tái dùng config hiện hữu
- Tái dùng file mà env `WORKSPACE_CONFIG` đang trỏ tới; **không tạo config file mới**.
- Thêm section policy dạng `agent_profiles` (tên field có thể điều chỉnh nếu source yêu cầu, nhưng một registry chung):
  - `agent_id`: identity canonical server-trusted;
  - `credential_env`: **tên** biến env chứa credential; config không chứa secret value;
  - `allowed_tools`;
  - `allowed_roots`;
  - `read_paths/read_prefixes`;
  - `write_paths/write_prefixes`;
  - attribution label nếu cần.
- Secret thật nằm trong secret/env material hiện hữu của Agent Data. So khớp credential constant-time; missing env/config malformed/duplicate match ⇒ fail closed.
- **Không fallback sang master `API_KEY`** trên Agent Gateway.

### G1.2 Một route generic
- Tạo đúng **một route generic**, ưu tiên `POST /mcp-agent` trên Agent Data hiện hữu.
- Không tạo `/mcp-hermes`, `/mcp-claude`…; agent mới về sau chỉ thêm profile + secret/config.
- Reuse protocol + tool schema + `_mcp_filtered_handler`/logic hiện hữu ở mức tối đa; không fork một MCP implementation thứ hai.
- Reuse nginx/API port hiện hữu. Không mở port/listener/service mới. Nếu public `/api/mcp-agent` cần sửa route config, chỉ sửa config hiện hữu.

### G1.3 Trusted identity
- Credential hợp lệ ⇒ server xác định `agent_id` từ profile.
- Với Agent Gateway, identity/attribution/presence/Git author signal phải lấy từ authenticated profile, **không** từ `clientInfo`, `User-Agent` hoặc header tên agent do client tự khai.
- Forged `clientInfo` không được đổi effective identity.
- Có thể bổ sung helper vào `hvu_signals.py` hiện hữu; không tạo module mới.

### G1.4 Tool + root + path scope — server-side
- Enforce tool allowlist trước argument validation/dispatch.
- Enforce root/path ở **một choke point chung** (ưu tiên `workspace_tools.call` hoặc context/policy guard tương đương), không chỉ kiểm ở UI/client.
- Read scope và write scope tách riêng.
- Prefix match phải component-aware: `work/a` không được match `work/abc`.
- Tool có path/from/to/operations nested phải kiểm toàn bộ đường liên quan; không chứng minh được path an toàn ⇒ deny.
- Raw MCP/HTTP không bypass scope.
- Master routes không mang agent profile thì giữ behavior hiện hành sau G0.

### G1.5 Hermes profile đầu tiên — least privilege
Production profile Hermes:
- `allowed_roots = ["workspace"]`.
- Read: chỉ exact `AGENTS.md`, `README.md`, root `COLLAB.md` và `work/hermes-joint-workspace` + descendants.
- Write: chỉ `work/hermes-joint-workspace` + descendants.
- Tool allowlist đầu: `workspace_list, workspace_read, workspace_search, workspace_stat, workspace_log, workspace_diff, workspace_edit`.
- **Không cấp** `workspace_write_new`, transaction, move/copy, import/upload/restore, task_*, exec, delete, UI, `vps_status`.
- `workspace_result_read` chỉ được cấp nếu continuation/result đã bind cùng authenticated profile; nếu chưa có binding ⇒ không cấp trong RUN này, ghi follow-up.
- Master key Agent Data **không** quay lại env Hermes.

### G1.6 Credential Hermes
- Tạo narrow credential ngẫu nhiên đủ mạnh; không in/log.
- Đặt server copy vào secret/env material **hiện hữu** của Agent Data theo `credential_env`.
- Đưa client copy cho Hermes qua root-managed secret materialization hiện hữu; Hermes process chỉ nhận narrow key, không nhận master/GSM quyền.
- **Không tạo persistent secret file mới.** Nếu hạ tầng hiện hữu không chứa được credential nếu không tạo file/resource mới ⇒ DỪNG xin Owner.
- Cấu hình `mcp_servers` hiện hữu của Hermes trỏ route generic qua relay/public path phù hợp; không tạo service/port mới.

## G2. TEST — dùng file hiện hữu, không tạo fixture mới

### G2.1 Unit/regression
Bổ sung vào **test files hiện hữu**:
1. Hai profile giả lập, hai credential khác nhau, khác scope; thêm profile thứ hai chỉ sửa config fixture/env, **không sửa route code**.
2. Key A không dùng được profile/scope B; invalid/no key fail closed.
3. Tool ngoài allowlist không xuất hiện trong `tools/list` và `tools/call` bị reject trước dispatch.
4. Read/write ngoài root/path scope bị reject.
5. Forged `clientInfo` không đổi authenticated `agent_id`/Git attribution.
6. Existing master routes + acceptance hiện hành vẫn PASS.
7. Nếu continuation không identity-bound thì Hermes profile không expose `workspace_result_read`.

### G2.2 Live Hermes — không tạo file mới
Sau local/unit PASS và deploy:
- no/invalid/master key trên `/mcp-agent` ⇒ reject;
- narrow Hermes key ⇒ `tools/list` đúng allowlist;
- đọc `AGENTS.md` PASS;
- đọc ngoài scope, ví dụ một task khác dưới `work/` ⇒ DENY trước trả content;
- gọi tool bị cấm ⇒ DENY;
- **write thật**: dùng `work/hermes-joint-workspace/view.html` hiện hữu. Ghi một thay đổi marker tối thiểu bằng `workspace_edit`, kiểm commit author/identity = authenticated Hermes, rồi revert ngay bằng `workspace_edit` thứ hai; hash byte cuối phải đúng bằng hash trước test. Không sửa `PROMPT.md` trong test.
- thử write ngoài HJW ⇒ DENY, 0 diff.
- forged client name vẫn attribution Hermes.

### G2.3 Public + local path
- Nếu route được dùng qua relay 6533 và public nginx, test cả path thực tế cần cho Hermes và path public dành cho agent tương lai; **không mở port mới**.
- Run acceptance hiện hữu cho Full All 2/public route để chứng minh không regression.

## G3. DEPLOY / ROLLBACK

- Agent Data source trên VPS là SSOT; build/deploy bằng cơ chế hiện hữu. Không force/rebase/pull code từ GitHub xuống.
- G0 và G1 dùng commit riêng để rollback rõ.
- Trước mỗi production restart: kiểm worktree sạch/expected HEAD và gửi Owner một dòng Telegram; không gửi được ⇒ DỪNG.
- G1 fail: rollback G1 về G0-good, giữ auth patch; xóa/disable narrow Hermes profile/key khỏi runtime hiện hữu; **không** trả master key cho Hermes.
- G0 regression: rollback G0 theo commit trước và DỪNG; không tiếp tục gateway.
- Không thay/chạm route/plugin Full All 2 ngoài regression cần thiết.

## Nghiệm thu bắt buộc

PASS chỉ khi:
- AUTH-BYPASS-CLOSED: đường root-only finding đã fail-closed; không public chi tiết exploit.
- EXISTING-CLIENTS-PASS: Agent Data + Full All 2/master clients không regression.
- GENERIC: một route code phục vụ ≥2 profile test config độc lập.
- PER-AGENT-AUTH: credential riêng, no shared master/fallback.
- TOOL-SCOPE: server-side allowlist.
- PATH-SCOPE: server-side read/write scope, outside denied.
- TRUSTED-IDENTITY: attribution từ credential/profile; forged clientInfo vô hiệu.
- HERMES-FIRST: live read + reversible write trong HJW PASS; outside DENY; final bytes view.html khôi phục chính xác.
- REVOCABLE: bỏ profile/credential làm access fail mà không ảnh hưởng client khác.
- NO-NEW-FILE: không project/task/file mới.
- SECRETS: không plaintext secret/exploit detail vào repo/chat/evidence public.

## Báo cáo

- Cập nhật **chỉ** `COLLAB.md` và `view.html` hiện hữu.
- Evidence nhạy cảm append vào **CAP-PATH-AUDIT.md hiện hữu root-only**; không tạo evidence file mới.
- Ghi Agent Data before/after commit, tests, deploy health, regression, Hermes live result, rollback state.
- Nếu PASS: đề xuất NEXT = migrate/add agent thứ hai bằng **profile/config**, không code route mới; không tự migrate trong RUN này.

## CẤM

- Không tạo project/task/file/test file/config file/service/port/listener mới.
- Không tạo route riêng từng agent.
- Không dùng shared key cho nhiều agent.
- Không dùng `clientInfo` làm authorization/identity trusted.
- Không đưa master Agent Data key/GSM broad access cho Hermes.
- Không mở rộng Hermes write ngoài HJW trong RUN này.
- Không migrate Claude Code hoặc agent khác production trong RUN này.
- Không log/copy secret hoặc exact bypass exploit vào repo/chat.
- Không tự tiếp tục automation Phase 1 sau KQ.

## AP-CLOSE

- `KQ@HJW-2C-20260924-01 XONG` chỉ khi toàn bộ nghiệm thu PASS.
- `DỪNG` nếu G0 không đóng được auth bypass, regression existing client, cần file/service/resource mới chưa được Owner duyệt, không tạo được credential bằng secret path hiện hữu, path/tool scope không enforce server-side, hoặc rollback không sạch.
- Agent báo XONG không đồng nghĩa DONE; Host phải nghiệm thu KQ/evidence.
