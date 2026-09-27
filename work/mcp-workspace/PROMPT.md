# PROMPT — MCPW Lifecycle Audit · reliable START/FINISH + GitHub hot-path audit

RUN_ID: MCPW-LIFECYCLE-AUDIT-20260927-01
STATUS: Chỉ thực thi sau READY/RUN hiện hành của Host.
Host: GPT Chat · Host_ID GPT-MCPW-250925-A
Executor_Surface: Claude Code CLI phiên mới trên Mac Owner.
Report_Write_Path: gateway fs_*/workspace_* vào chính work/mcp-workspace/COLLAB.md và view.html hiện hữu.
Runtime: **AUDIT CHỈ ĐỌC**; không deploy/restart/sửa config/source/runtime trong RUN này.

Căn cứ: MCPW §0.2(1)(2)(3)(4), N1–N7/P17/P18/P19; HJW P61–P64; DROOT22; DROOT24.
JEV Host: gen-dec-1790471705-Zn5vjV7eAItb2Sf6Z4Mh — AUDIT_FIRST 1,00; giữ P02 không đổi trừ khi có regression cụ thể 0,89.

## 0. Hai câu hỏi Owner bắt buộc trả lời bằng bằng chứng

### Q1 — START/FINISH có thực sự đáng tin?
Owner cần hệ thống biết **một cách đáng tin cậy**:
- AI/Agent nào đã nhận/bắt đầu làm;
- AI/Agent nào đang có execution hợp lệ;
- đã kết thúc chưa;
- kết quả/báo cáo ở đâu;
- ai tiếp theo.

Không được dựa vào Agent nhớ tự báo, commit cuối, polling may rủi hoặc câu “XONG” trong chat.

Định nghĩa chuẩn để máy có thể cưỡng chế:
- **DISPATCHED**: có assignment/RUN hợp lệ, chưa phải đang làm.
- **CLAIMED/STARTED**: runner/gateway đã nhận execution, identity + work/RUN/role/scope/generation được xác thực, START bền đã ghi.
- **ACTIVE_ACTIVITY**: có tool/process/checkpoint thật của execution.
- **WAITING**: execution/process/session còn hợp lệ nhưng không có activity mới; không gọi đây là “AI đang suy nghĩ”.
- **LOST/INTERRUPTED**: process/session/TTL mất.
- **AWAITING_REPORT**: runner đã kết thúc nhưng thiếu KQ/P/report/artifact bắt buộc.
- **REPORTED**: báo cáo/KQ/P + artifact/commit phù hợp đã có.
- **VERIFIED/ACCEPTED**: Reviewer/Host đã nghiệm thu.

Yêu cầu “mọi trường hợp” áp cho **mọi hành động có thể tác động workspace/runtime do hệ thống quản**. Suy nghĩ/offline không phát event không thể quan sát và không được giả là đang làm. Nếu một đường mutation hiện có thể đi vòng monitored choke point thì tiêu chí §0.2(1) = CHƯA ĐẠT.

### Q2 — GitHub còn nằm ở hot path quá mức không?
GitHub vẫn phải là durable SSOT + write authority.
Nhưng:
- tương tác/read/lifecycle/Owner View nên dùng VPS/local state;
- read không được bị GitHub chậm kéo BUSY như sự cố cũ;
- write vẫn revalidate GitHub trước commit/push;
- không tạo SSOT Git thứ hai.

Kiểm P02 hiện hành bằng source + runtime + metrics; **không tune/rewrite P02** nếu không có regression thật.

## 1. G0 — read gate

Đọc: AGENTS.md → root COLLAB.md → work/mcp-workspace/COLLAB.md §0/N1–N7/P17–P19 → PROMPT này.

Xác nhận:
- READY exact;
- MCPW-LOCK/ruleset vẫn active;
- P02 source/runtime hiện hành và Protection Guard/Kuma healthy;
- HJW CLOSED nhưng control runtime live, AUTO rỗng;
- không có mutation MCPW khác đang STARTING;
- `/opt/incomex/docker/docker-compose.yml` dirty cũ được nhận diện, không tự sửa.

Không đạt → KQ DỪNG, không mutation.

## 2. Phạm vi audit lifecycle — phải phủ tất cả bề mặt

Lập **LIFECYCLE_GAP_MATRIX** với từng dòng:
`surface/path → actor identity source → session/execution id → work/RUN/scope binding → durable START? → activity source → terminal/finish signal → required report binding → mutation choke point → can bypass? → durable store/hook hiện hữu → verdict`.

Tối thiểu:
1. GPT/ChatGPT qua Agent Data master `workspace_*`.
2. Agent Gateway profile (Hermes hiện hành).
3. Claude Chat/Claude Code qua `fs_*`/claude-mcp.
4. Claude Code CLI local process + terminal work trên Mac giữa hai MCP call.
5. Codex/runner nếu đang có đường production thực dùng.
6. `workspace_exec` + `workspace_task_*` queue/worker.
7. SSH/operator/root runtime path hiện hành.
8. Hermes interactive chat có terminal/file/cron/runtime capability.
9. Owner emergency/bypass path.
10. Owner View/HVU publisher/presence path.

Không suy từ docs; đọc source/runtime/config/log thật. Không in secret.

## 3. Điều tra lỗ “agent lẳng lặng code”

Đối chiếu source hiện hành, đặc biệt:
- `agent_data/hvu_signals.py`: transport/trust/touch/begin/finish/heartbeat;
- store của `workspace_runtime.py`;
- claude-mcp/fs gateway tương ứng;
- runner/exec/task state;
- SSH/auth/journal/audit hiện có;
- Owner View publisher/HVU.

Phải trả lời cụ thể:
- khi Claude Code session bắt đầu nhưng chưa gọi gateway: VPS biết gì?
- khi Claude Code đang edit/build/test local 1–5 phút giữa hai gateway calls: hệ thống có event sống nào không?
- lần MCP read đầu tiên có tạo durable execution hay chỉ presence heuristic?
- commit nhanh giữa hai poll có thể bị mất khỏi “đang/vừa làm” không?
- process exit 0 nhưng quên KQ/report: hiện hệ thống gọi DONE hay không biết?
- crash/terminal bị đóng: có terminal state nào bền không?
- một runtime SSH change không có Git commit: ai/việc nào được ghi?
- sự cố HJW `~/.hermes/config.yaml approvals.timeout:500` ngày 26/09 có thể quy actor/work/execution từ evidence hiện có không? Nếu không, ghi rõ nguyên nhân.

Cho phép **probe chỉ đọc**:
- một session SSH/read-only command `true/id/date/ss/read log` nếu cần để xem audit trail;
- một local-only interval/no-op để đối chiếu VPS event gap;
- queue/exec read-only/no-op nếu cần.
Cấm sửa file/config/service chỉ để tạo evidence.

## 4. Phân biệt identity

Phải tách:
- authenticated actor/profile;
- surface label;
- session_id;
- execution_id;
- RUN_ID/assignment_id.

Không cho:
- clientInfo/User-Agent/commit prefix tự trở thành trusted identity;
- RUN_ID thay session/execution;
- “Claude Code” chung cho nhiều terminal thành một execution.

Nếu master routes hiện chỉ có display-label trust yếu, ghi PARTIAL; Agent Gateway profile server-auth là evidence mạnh hơn.

## 5. START/FINISH enforcement candidate — reuse first

Audit các thành phần hiện hữu trước khi đề xuất code:
- gateway audit/idempotency;
- `workspace_runtime.py` Queue/jobs/tasks SQLite/state;
- existing operation/task/job ids + heartbeat;
- `hvu-signals.json`;
- fs gateway audit/state;
- SSH/system journal/audit hook hiện hữu;
- HJW lifecycle/notepad/dispatch;
- Guard/Kuma.

Chọn **một durable execution ledger/lifecycle source chung hoặc ghép từ store hiện hữu**; không dựng DB/service/server mới trừ khi chứng minh tất cả store hiện hữu không đáp ứng atomicity/recovery/cursor.

Implementation plan sau audit phải nêu:
- choke point nào phát START;
- execution_id ai sinh, uniqueness/restart semantics;
- heartbeat/activity lấy từ đâu;
- process/session death → LOST;
- exit → AWAITING_REPORT hoặc REPORTED;
- report/KQ mapping;
- lease/generation fencing;
- Owner emergency path logging;
- publisher cursor/dedupe/recovery;
- cách chặn mutation khi thiếu active execution/lease.

## 6. Scoped lease audit

Không implement lease trong RUN audit, nhưng phải xác định chính xác vị trí enforce tối thiểu cho:
- work-id + RUN_ID + role + scope + generation;
- two independent scopes allowed;
- overlapping mutation denied;
- read-only Reviewer coexist;
- stale generation denied;
- crash TTL release/fencing;
- handoff/preempt Owner/Host.

Tìm xem gateway/runner hiện có lock/idempotency/version nào reuse được và cái nào **không thể thay lease**.

## 7. GitHub hot-path audit — P02 không được “đập đi làm lại”

Lập **GITHUB_HOTPATH_MATRIX**:
`path/component → GitHub call? → read/write → cadence/trigger → holds request/lock? → cached/local fallback? → failure behavior → last 24h error evidence → needed? → action`.

Tối thiểu:
1. workspace_* read/search/list/stat/log/diff.
2. fs_* read/search/list/stat/log/diff.
3. both write paths.
4. Owner View sync/publisher.
5. lifecycle/presence/NEXT publisher.
6. Hermes dispatch/backstop.
7. any git ls-remote/fetch/pull polling jobs.
8. Protection Guard/periodic jobs.

Phải:
- verify P02 `workspace_snapshot.py` / fs equivalent hashes/runtime;
- đọc metrics 24h và timestamp lỗi, tách pre-P02 vs post-P02;
- xác nhận hiện tại read answers `freshness/recheck_required`;
- đo/đếm GitHub refresh/fetch cadence nếu sổ có;
- chứng minh GitHub chậm/down thì **lifecycle event store trên VPS vẫn ghi/đọc được**, Owner View có thể hiện last-known state + freshness; không cần GitHub cho từng heartbeat;
- write vẫn revalidate GitHub, không hạ chuẩn.

Nếu không tìm thấy regression P02: `P02_VERDICT=KEEP`. Không restart/deploy/tune.

## 8. Acceptance audit A1–A12

A1. Có matrix đủ 10 bề mặt lifecycle.
A2. Có ít nhất một bằng chứng source/runtime cho từng verdict, không chỉ prose.
A3. Chỉ rõ mọi blind spot hiện tại: local-only, SSH/runtime, master identity, exit-without-report, poll-gap.
A4. Chỉ rõ đường nào đã machine-enforced và đường nào heuristic.
A5. Sự cố Hermes config không rõ actor được đối chiếu, không đoán.
A6. Có lifecycle state machine và minimal choke-point plan.
A7. Có scoped-lease enforcement map.
A8. Có GITHUB_HOTPATH_MATRIX đầy đủ.
A9. P02 verdict dựa source/runtime/metrics; không dùng số error lịch sử không có timestamp.
A10. Chứng minh hoặc bác bỏ: sau P02, read-side BUSY/OVERLOADED/GIT_FETCH_FAILED không còn regression hiện hành.
A11. Không runtime/config/service mutation; 0 model Hermes call; không thêm service/DB/key/port.
A12. Phân loại §0.2 (1)–(4): ENFORCED/PARTIAL/NOT_ENFORCED kèm bằng chứng và NEXT.

## 9. Báo cáo

Ghi vào **chính** work/mcp-workspace/COLLAB.md + view.html hiện hữu; không tạo repo file/task mới.

Báo cáo phải có:
- `LIFECYCLE_GAP_MATRIX`;
- `GITHUB_HOTPATH_MATRIX`;
- state machine;
- minimal implementation pack chia phase nếu cần;
- `P02_VERDICT`;
- §0.2 verdict;
- regression/out-of-scope observations;
- rollback không áp dụng vì audit không mutation.

Nếu audit đủ:
`KQ@MCPW-LIFECYCLE-AUDIT-20260927-01 XONG`

Nếu không đủ quyền đọc/bằng chứng:
`KQ@MCPW-LIFECYCLE-AUDIT-20260927-01 DỪNG · <blocker>`

**KQ XONG của audit không có nghĩa MCPW hoàn thành.** Sau audit Host mới phát implementation RUN; không tự implement trong cùng phiên.