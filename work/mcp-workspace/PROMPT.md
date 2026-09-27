# PROMPT — MCPW-AD1-FIX · fix periodic GitHub reads + VPS-owned gen2 watch

RUN_ID: MCPW-AD1-FIX-20260928-01
Host: GPT Chat · GPT-MCPW-250925-A
Executor_Surface: Claude Code CLI trên Mac Owner, chỉ cài/smoke ngắn.
Report_Write_Path: chỉ `work/mcp-workspace/COLLAB.md`.
Evidence VPS: `/opt/incomex/work/mcp-workspace/MCPW-AD1-FIX-20260928/`.

## 0. Mục tiêu
Sửa đúng failure của AD1 gen1: periodic workspace reads 24/h > 20/h.
Không nới ngưỡng. Không làm Pha B/C trong RUN này.
Sau cài/smoke, **Mac không còn là dependency**: watcher gen2 24h phải chạy deterministic trên VPS bằng Guard/Kuma/timer/state hiện hữu, không cần Claude Code/Codex/Hermes model.
P02 core = KEEP/FREEZE. GitHub vẫn durable SSOT + write authority.
Căn cứ: DROOT22, DROOT25, DROOT28; N9; P34–P39; Claude P37.

## 1. Gate đầu RUN — đọc state máy trước mọi kết luận
Đọc AGENTS → root COLLAB DROOT22/25/28 → MCPW COLLAB P34–P39 → file này.
Trên VPS chạy read-only `/opt/incomex/work/mcp-workspace/MCPW-AD1-20260927/bin/verify-AD1.sh` và lưu output.
Dòng đầu phải chứng minh gen1 terminal FAIL `periodic_reads` (generation/state/timestamp rõ). Nếu state khác, thiếu, mơ hồ hoặc verify lỗi ⇒ DỪNG, không mutation.
Chụp baseline: P02 image/hash/StartedAt; Guard/ruleset; hvu timer; root/gate hashes; switches; Kuma #21/#22; current hourly ghcall by source.
Mac mất kết nối trước mutation ⇒ dừng an toàn. Mac mất sau partial mutation ⇒ lần sau reconcile exact checkpoint/bytes; không chạy lại mù.

## 2. Scope / hard stops
Được sửa tối thiểu các thành phần AD1 hiện hữu: `hjw-control-root.py`, Protection Guard/counter logic, AD1 switch/state/watch logic và đúng dòng tài liệu vận hành HVU.
Chỉ khi bằng chứng bắt buộc mới sửa code khác trong exact AD1 path; không sửa P02 source/image/config/freshness.
Cấm: restart/recreate `agent-data` hoặc `claude-mcp`; model Hermes/AUTO; service/DB/port/key/token mới; ruleset mutation; ssh/root identity/lease/lifecycle B/C; nới threshold 20/h; production rate-limit test.

## 3. FIX-A · hjw-root local phải = 0 GitHub
Đọc journal `SYSLOG_IDENTIFIER=incomex-ghcall` với `GH_SOURCE=hjw-root` quanh gen1 để xác định **nguyên nhân thật** 4/h: purpose/what/result/freshness/switch.
Không mặc định kết luận `FRESH_MAX=300` là root cause. Chỉ sửa sau khi log/repro chứng minh.
Fix nhỏ nhất để khi VPS-derived state trusted/fresh, root monitor dùng local và **0 GitHub**.
Stale/missing/untrusted/out-of-order vẫn phải bounded fallback/UNKNOWN/fail-closed đúng AD1; không false-green.
Fix không được làm assignment-detection >5′ hoặc hạ điều kiện trust local.

## 4. FIX-B · P02 attribution đúng nguồn
Gen1 đếm `p02-workspace=2`, `p02-fs=2`; phải tách lượt Guard tự gây khỏi client read đồng thời.
Sửa **counter/Guard attribution**, không sửa P02 source nếu chưa có Host approval.
Acceptance bắt buộc có negative control: chạy Guard check đồng thời với client read P02; chỉ lượt do Guard tự kích mới vào budget Guard. Client read không được bị gán cho Guard.
Nếu không thể attribution đáng tin mà không sửa P02 contract/source ⇒ DỪNG và báo blocker; không dùng heuristic dễ false-count.

## 5. Budget và counter
Budget gen2 theo nguồn:
- `hvu-sync periodic <= 15/h`;
- `gate periodic = 0 GitHub/h` khi local trusted;
- `hjw-root periodic = 0 GitHub/h` khi local trusted;
- `Guard-owned <= 4/h` (ruleset + e2e/P02 do chính Guard gây);
- tổng periodic workspace reads <= 20/h.
`hermes-gateway` GitHub Pages/non-workspace network ghi riêng informational; không giấu trong workspace counter và không tự nhập vào budget API nếu không cùng loại quota.
Counter phải giữ source/channel/purpose/result/latency/fallback, dedupe/replay như AD1.

## 6. Alert-only lâu dài + tài liệu
Sau terminal gen2 PASS/FAIL, watcher 24h không được biến mất hoàn toàn.
Giữ hourly **alert-only** deterministic cho sync/gate/root/ruleset/P02 liveness: regression ⇒ Kuma/Telegram, nhưng không đổi terminal gen2 và không auto-rollback sau cửa sổ.
Cập nhật đúng SSOT vận hành hiện hữu `scripts/hvu-b2/00-NHAN-THU-MUC.md` (hoặc path thực tương ứng) thêm AD1: backstop 4′, counter/backoff, rollback source=github. Không tạo bản sao.

## 7. Gen2 24h — VPS giữ, Mac được tắt
Preserve gen1 FAIL evidence nguyên vẹn trong hồ sơ; không overwrite lịch sử.
Re-arm generation 2 với state bền, from/to rõ. `verify-AD1.sh` dòng đầu phải in `GEN=2 RUNNING|PASS|FAIL ...`.
Guard/Kuma/timer hiện hữu tự chấm mỗi giờ. Không cần terminal/Mac/agent chạy nền.
FAIL bất kỳ giờ nào ⇒ state gen2 FAIL + Telegram + rollback **consumer liên quan** về known-good; alert-only vẫn tiếp tục.
24 nhịp xanh liên tiếp ⇒ state gen2 PASS + Telegram; sau đó chuyển sang alert-only.
Watcher tự được watchdog: thiếu nhịp >2h ⇒ FAIL/alert, không im lặng PASS.

## 8. Smoke ngắn trước bàn giao
Agent chỉ cần smoke ngắn đủ để chứng minh delta, **không ngồi chờ 24h**:
1. PRE/POST Guard PASS, ngoài-scope=0.
2. ruleset live PASS; P02 StartedAt/hash unchanged.
3. root source=local và cửa sổ live khoảng 15′: 0 GitHub root.
4. gate local: 0 GitHub, 0 model.
5. attribution negative control concurrent client-read PASS.
6. budget theo source từ smoke/projection <=20/h.
7. rollback exact từng delta + source local↔github↔local nếu cần.
8. gen2 watcher fixture xanh/đỏ đi được tới Kuma nhưng fixture **không** terminalize gen2.
9. sau arm, chứng minh process/timer/watch trên VPS tồn tại độc lập với SSH session; không để background process trên Mac.

## 9. KQ
Khi §8 PASS và gen2 đã arm, ghi:
`KQ@MCPW-AD1-FIX-20260928-01 XONG · GEN2_WATCH_RUNNING_ON_VPS`
rồi **DỪNG phiên Claude Code**. Không chờ 24h, không sang B/C.
Blocker: `KQ@MCPW-AD1-FIX-20260928-01 DỪNG · <lý do>`.
Report phải ghi exact root cause, delta/hash, before/after by-source, watcher generation/state, rollback, verify command, và khẳng định Mac có thể tắt sau KQ.

## 10. N9
Host acceptance sau KQ vẫn theo E1–E6. Full AD1 chỉ ACCEPT khi gen2 machine-state = PASS; Host phải đọc state máy hiện tại trước khi tuyên bố.
Không dùng lời Agent/commit prose thay cho machine state.