# PROMPT — MCPW-AD1 · trace hardening + GitHub hot-path reduction

RUN_ID: MCPW-AD1-20260927-01
STATUS: Chỉ chạy sau READY/RUN hiện hành.
Host: GPT Chat · GPT-MCPW-250925-A
Executor_Surface: Claude Code CLI phiên mới trên Mac Owner.
Report_Write_Path: chỉ `work/mcp-workspace/COLLAB.md`; không tạo repo report/view/task mới.
Hồ sơ VPS: `/opt/incomex/work/mcp-workspace/MCPW-AD1-20260927/`.

## 0. Mục tiêu
AD1 chỉ làm hai việc low-risk: (A) tăng độ tin cậy control-plane/Guard; (D) giảm polling GitHub chỉ-đọc bằng VPS-derived state.
**AD1 không giải quyết “Agent âm thầm code”.** Pha B mới làm execution lifecycle. Không gọi §0.2(1)/(3)/(4) PASS sau AD1.
P02 core = KEEP/FREEZE. GitHub vẫn durable SSOT + write authority.
Căn cứ: DROOT22/DROOT24; N1–N9; audit `44dcb97`; P23/P24; Claude P25.

## 1. PRE
Đọc AGENTS → root COLLAB → MCPW COLLAB §0/N1–N9/P20–P25 → PROMPT.
Chụp baseline: ruleset 23976991; Agent Data/Claude MCP health + image/StartedAt; hashes `hvu_signals.py`, `workspace_snapshot.py`, `workspace_runtime.py`; HJW STOP/AUTO/gate/plugin/root-monitor; Guard/config-guard/Kuma; pending recovery/write; compose dirty cũ; owner/mode của sync-status/revisions.
PRE fail hoặc mutation chen ngang không hòa giải được ⇒ DỪNG.

## 2. Scope
Được sửa script/config/test hiện hữu của Protection Guard, HVU backstop, HJW deterministic gate/watchers/root monitor; thêm structured counter/log vào state/log hiện hữu.
Có thể reload/restart đúng component bắt buộc bởi delta, theo PRE/POST/rollback; **không restart P02 gateways nếu không cần**.
Cấm: sshd VERBOSE; auditd; đổi root key/SSH/sudoers/authorized_keys; execution ledger/hooks/lease; service/DB/port/key/token mới; sửa P02 source/image/freshness; model Hermes/AUTO; đổi ruleset; gây 429 thật; xóa GitHub fallback.

## 3. Ruleset Guard — 3 trạng thái
Kiểm khoảng 1 lần/giờ bằng cơ chế hiện hữu.
PASS xanh chỉ khi khớp đủ: id=23976991, enforcement=active, target ~ALL, đúng 4 rule creation/update/deletion/non_fast_forward, bypass chỉ DeployKey.
FAIL đỏ ngay: 200 lệch spec; 404; bằng chứng chắc chắn disabled/deleted/changed.
UNKNOWN vàng: 403/429/5xx/timeout/DNS/parse/verification unavailable. Không false-green/false-red cấu hình. Tôn trọng Retry-After/reset; không retry trong cùng giờ khi backoff còn hiệu lực.
Lưu `last_attempt`, `last_result`, `last_pass`; last_pass >2h ⇒ vàng một lần; >6h ⇒ đỏ liveness. Kuma/tin Owner mang last_attempt + last_pass.
Fixture: lệch spec→FAIL, 404→FAIL, 429/timeout→UNKNOWN; không tamper ruleset production.

## 4. Hermes control-plane drift
Bao phủ whole-file hash + semantic keys của `config.yaml` gồm `approvals.*`, `jobs.json`, thư mục/plugins + enable/hash, platform toolsets/backend/gate/control, STOP/controller state.
Alert chỉ path/key + hash/changed-key đã sanitize, không value/secret. Chưa có lifecycle evidence ⇒ `actor=CHƯA_XÁC_ĐỊNH`.
Fixture copy đổi approvals.timeout/jobs/plugin phải bị bắt; không sửa config production để test.

## 5. Điều kiện tin VPS-derived state
Chỉ tin local khi đủ TẤT CẢ:
1. sync-status phản ánh lần **sync thành công** còn fresh;
2. SHA published có `revisions/<sha>` đầy đủ, publish nguyên tử/immutable;
3. revision không lùi/out-of-order;
4. uid `hermes` không write/rename/replace được sync-status/revisions — negative permission test phải FAIL;
5. Hermes chat/session không thể tự dựng assignment/revision cho chính mình;
6. freshness giữ hợp đồng nhận việc ≤5′.
Thiếu một điều ⇒ stale/untrusted; gate không wake; fallback GitHub tối đa một đường bounded có backoff.
Webhook vẫn là đường nhanh. Backstop HVU hiện hữu đổi 15′ → **4′**, một poller/single-flight chung; không tạo poller/service mới.

## 6. Hermes gate/watchers dùng VPS trước
Áp `ws-dispatch`, `ws-handoff-watch`, `ws-run-watch`.
Local trusted/fresh ⇒ đọc exact revision/task từ VPS; **0** ls-remote/raw/REST GitHub cho quyết định đó.
Giữ deterministic filter, claim, chống lặp, Owner approval, START/RESULT, STOP.
Local stale/missing/out-of-order ⇒ tối đa một fallback GitHub bounded; không chứng minh assignment hiện hành ⇒ fail-closed `wakeAgent=false`; không model call.
Mỗi consumer giữ switch `source=local|github`; không xóa đường cũ.

## 7. HJW root monitor
`hjw-control-root.py tick`: fresh SHA == accepted SHA ⇒ no fetch; SHA khác ⇒ đúng một bounded refresh/proof; stale/untrusted ⇒ bounded GitHub fallback.
403/429/timeout phân loại riêng, không biến thành drift. UNKNOWN không false-green.
Rollback: source=github + cadence cũ.

## 8. 403/429/backoff
Tách auth/config · rate-limit · transient network/5xx/timeout · valid 404.
REST đọc Retry-After / X-RateLimit-Reset khi có; không retry sớm. git/raw dùng bounded backoff, không tight-loop.
Rate-limit + local fresh ⇒ dùng local; local stale ⇒ gate fail-closed/monitor UNKNOWN. P02/K8 write giữ nguyên.
Test bằng local stub/fixture; cấm tạo 429 production.

## 9. GitHub-call counter bền — không DB mới
Mỗi remote-call path AD1 chạm ghi structured event vào log/state hiện hữu: timestamp, source/process/consumer, channel git-https|git-ssh|raw|REST, auth_class, purpose, result class, latency, fallback_used, safe revision/task.
Không secret/IP/token. Counter tính calls/hour theo source, có cursor/dedupe/event identity để restart không double-count.
Số ~160/h/~89/h cũ = `MEASURED_BY_EXECUTOR`, không invariant.

## 10. Rollback từng mục
D1/D2 giữ switch local↔github; checker/config monitor có enable/disable config hiện hữu; counter thụ động.
Lưu exact bytes/hash trước deploy. Diễn tập fixture rollback từng delta + một vòng thật local→github→local trong cửa sổ yên. Rollback không bật AUTO/fail-open/disable ruleset.

## 11. Acceptance của Agent
1. PRE/POST Guard PASS; ngoài-scope diff=0.
2. P02 image/hash/StartedAt không đổi; không regression BUSY/OVERLOADED/GIT_FETCH_FAILED do AD1.
3. Ruleset live PASS + mutants: lệch spec FAIL, 404 FAIL, 429/timeout UNKNOWN; last_attempt/last_pass đúng.
4. Config fixture bắt approvals.timeout/jobs/plugin, không lộ value; actor unknown trung thực.
5. uid hermes không write/rename/replace sync-status/revisions.
6. Local fresh + GitHub read blocked/stubbed ⇒ gate đúng, 0 GitHub call, 0 model call.
7. Local stale/missing/out-of-order ⇒ bounded fallback/fail-closed; không wake sai.
8. Root monitor fresh/no change ⇒ no fetch; change/stale ⇒ bounded refresh.
9. 429 stub tôn trọng backoff/Retry-After; không tight-loop/false PASS.
10. HJW manual contract PASS; AUTO rỗng; STOP/approval/Telegram không hồi quy; 0 model call.
11. Counter reconciliation 0 orphan/double; mutant bỏ đếm một source ⇒ reconciliation FAIL.
12. Rollback từng delta exact; source switch lật thật một vòng an toàn.
13. Live smoke 15′ ổn định; counter giảm periodic GitHub đúng hướng. Trong smoke chạy 1 lần đối chiếu counter với mẫu SYN/network 10′ (±15%). Cài xong bước canh tự động §12 và chứng minh nó đẩy được 1 nhịp xanh + 1 nhịp đỏ fixture vào monitor Kuma hiện hữu.
Sau PASS ghi `KQ@MCPW-AD1-20260927-01 XONG · HOST_ACCEPT_PENDING_24H` rồi DỪNG; không sang Pha B.

## 12. Canh 24h do máy làm — không ai phải quay lại
Guard hằng giờ hiện hữu đánh giá trên cửa sổ 60′ gần nhất:
1. GitHub đọc định kỳ toàn hệ ≤20/h, REST ẩn danh ≤2/h;
2. Hermes gate khi local fresh = 0 lần gọi GitHub;
3. phát hiện assignment p95 ≤5′, 0 assignment/commit bị sót;
4. ruleset checker có `last_pass` ≤2h;
5. P02 hash/StartedAt/health không đổi.

Kết quả đẩy vào monitor Kuma hiện hữu của Guard, không tạo token/service/DB mới. Kuma không nhận nhịp quá 2h ⇒ đỏ để canh cả chính watcher.

**Vi phạm bất kỳ mục nào** ⇒ Telegram + tự lật consumer liên quan về `source=github` bằng switch an toàn đã có + ghi `AD1_24H=FAIL <mục>` vào state hồ sơ VPS. Chỉ rollback consumer liên quan; không bật AUTO/fail-open, không đụng P02/ruleset.

**Đủ 24 nhịp xanh liên tiếp** ⇒ ghi `AD1_24H=PASS <from>→<to>` vào state hồ sơ VPS rồi dừng đánh giá cửa sổ AD1-24h; giám sát thường trực của Guard/Kuma vẫn chạy.

VERIFY (§13) phải in đúng dòng `AD1_24H=...` đầu tiên. Host ACCEPT = đọc và đối soát dòng PASS bất cứ lúc nào sau đó; không có lịch, không ai/AI phải nhớ quay lại.

## 13. N9 — kiểm lại được độc lập
Hồ sơ VPS phải có exact read-only verification commands + expected invariant (`VERIFY.txt` hoặc script read-only trong hồ sơ task, không repo file): ruleset state/liveness; config hashes/fixture; hermes permissions; source switches; calls/hour; p95 detect; counter reconciliation; P02 hashes/StartedAt/health; rollback state.
Không chứa secret. Host nghiệm thu theo E1 scope diff · E2 runtime identity · E3 independent live/source check · E4 mutant FAIL · E5 reconciliation · E6 post-window+rollback.

## 14. Báo cáo
Chỉ cập nhật `work/mcp-workspace/COLLAB.md`. Ghi exact runtime delta/hashes/switches, acceptance 1–13, before/after smoke counters, verify commands, rollback, residuals, `P02_VERDICT=KEEP`, và nhắc rõ **Pha B chưa làm**.
PASS smoke: `KQ@MCPW-AD1-20260927-01 XONG · HOST_ACCEPT_PENDING_24H`.
Blocker: `KQ@MCPW-AD1-20260927-01 DỪNG · <lý do>`.