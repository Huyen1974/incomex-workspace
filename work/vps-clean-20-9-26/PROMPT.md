# PROMPT — VPSC-N2A-DISK11-CONTROLS-20261011-01 · THREE CONTROL_DEBT #11 HOTFIX (SCOPE N2a)

RUN_ID: VPSC-N2A-DISK11-CONTROLS-20261011-01
Task: `work/vps-clean-20-9-26` (VPSC) · D22/roadmap N2a, **not a new task**.
Executor: Claude Code CLI (new session), Owner manually pastes after **Claude Reviewer exact ACCEPT + GPT Host READY same SHA**.
Repo_Write_Path: existing Incomex MCP `workspace_*`, root=`workspace`; VPS config/runtime via already accepted native paths and `incomex-config-apply-v0` only.
Status: **DRAFT · P75 GPT Host áp 4 điểm P73 · P76 Claude Reviewer chỉnh trong phạm vi 4 điểm theo mã + ACCEPT đúng SHA bản này · OWNER AUTH MISSING · NO READY/RUN**.
Evidence: reuse `/opt/incomex/work/vps-clean-20-9-26/` under a run-scoped subdir; report one section under existing `BAO-CAO.md` and KQ in task `COLLAB.md`. Never create duplicate repo files as progress notes.

## 0. GOAL — CLEAR THE *ACTUAL* BLOCKER, NO SCOPE CREEP
Owner has directed priority to complete Graph R10 promptly; the sole known hard execution gate is **Kuma #11 Disk Usage RED** caused by three VPSC `CONTROL_DEBT` deadlines 2026-10-11T01:00:00Z (not disk fullness: 11/10 physical free ≈42 GB):
1. `/opt/incomex/data/workspace-tools/transactions`: operation backups, baseline historical +62 MB/day.
2. `/var/lib/incomex-mcp-helper`: queue/out, done and P02 backlog, historical +105 MB/day.
3. `/opt/incomex/mcp-roots/gh` (under `/opt/incomex/mcp-roots`): loose Git objects/ref growth.

**Mục tiêu RUN N2a:** sửa đúng ba nguồn CONTROL_DEBT bằng van giới hạn thật, kiểm chứng Kuma #11 GREEN và Guard POST same-or-better. Không lách bằng nới ngưỡng, đổi hạn debt/kind, đặt cap-only hoặc di chuyển dữ liệu sang thư mục khác cùng ổ.

**Ngoài RUN:** C2 312 UNKNOWN+2 excluded, 3 EVIDENCE_DEBT, D22/N2b để VPSC sau; R7 A/B/C1/C3/D/POST giữ nguyên. Không sửa Graph R10, HJW, ứng dụng agent-data/helper hoặc task đã đóng. Cấm Git prune/reflog expiry, queue truncate, xoá wildcard không có danh sách kiểm chứng, broad wipe hay đổi services/PG/Directus.

## 0A. OWNER-ONLY PERMISSION · CHƯA ĐƯỢC CẤP
Câu sau là CHÍNH SÁCH ĐỀ XUẤT, không phải giấy phép vì nó xuất hiện trong PROMPT. Chỉ được thêm luật giữ hạn/cài timer và xoá nếu Owner thực sự tự dán RUN chứa nguyên văn câu (một dòng):
Owner cho VPSC N2a trên VPS1 thêm luật dọn hằng ngày vào vps-retention.sh hiện có (chỉ khi không làm được thì tạo tối đa một script và một systemd timer) để xoá đúng dữ liệu không còn tham chiếu là backups workspace-tools/transactions đã hoàn tất quá 14 ngày cùng helper queue/out/*.json, queue/done và snapshot p02 đã hết vai trò quá 7 ngày, sau khi dry-run có danh sách và hash chính xác và kiểm lại trạng thái, idempotency, tham chiếu khôi phục ngay trước khi xoá, giữ mọi dữ liệu chưa rõ, còn hoạt động hoặc là bản khôi phục duy nhất, không xoá gì khác và không prune hay sửa lịch sử Git.

Thiếu câu này, thiếu READY exact SHA, thiếu Guard/no concurrent thì DỪNG trước STARTED/mutation. Owner cấp quyền một lần cho đúng policy định kỳ trong phạm vi trên; từng lần tự kiểm refs/hash/fresh receipt, lỗi/UNKNOWN thì KEEP và cảnh báo. Không phải xin Owner mỗi ngày. Không đụng dữ liệu độc nhất cần khôi phục khi chưa có proof offsite/restore.

## 1. S0 HARD AUTH + LIVE RESOURCE / GUARD
1. Đọc `AGENTS.md` → root `COLLAB.md` → VPSC Bảng, §0, P68–P76/BAO-CAO R7, Claude P73/P76 ACCEPT and Owner policy §0A, last-touch PROMPT và reviewer/Host exact SHA. Kiểm **không có STARTED active/STOP/COUNCIL_ALERT, no HJW/Graph concurrent mutation**. #11 RED là **đối tượng đang chữa**, không giả vờ PRE 22/22: freeze `PRE_RED_SET` và raw reason, yêu cầu các đèn khác cùng Guard Config CLEAN hoặc có reason và owner minh bạch. Active resource floor: MemAvailable ≥3GiB + disk free ≥20GiB, no active PSI/OOM hazard. Nếu khác mà không giải thích được ⇒ KQ DỪNG sạch. **Do not wait/poll/hold terminal.**
2. Preflight full SHA and root gate before writing. If passed, record `STARTED@VPSC-N2A-DISK11-CONTROLS-20261011-01` + root shared busy atomically in one repo commit before first mutation. Preserve all actual scripts/registry/queue state/baseline hashes, support existing coverage Guard C3 and revocable rollback to PRE. No secret or raw customer data in Git/evidence.
3. Read-only inspect each `CONTROL_DEBT` row in `scripts/storage-registry.tsv`: canonical owner, due, path, cap, source classifier, current bytes/rate and what evidence the detector requires before clearing. Inspect existing `storage-watch.py`, retention scripts/timers, `incomex-config-apply-v0 --help`, and Config Guard protected paths. Freeze **allowed exact footprint matrix**, candidate patches and inverse before mutation. If status RED is a real fault (not just deadline) fix it under the same three source boundaries, not by changing the monitor definition.

## 2. N2a — THREE SOURCE CONTROLS (FOUR FIXES P73)
A · Transactions: chỉ backup completed, quá 14 ngày, chứng minh không còn prepared/push_unknown/rollback_conflict/unknown, queued/running, operation_id/idempotency, audit/rollback/recovery refs. Tuổi không đủ để xóa; UNKNOWN/sole recovery => KEEP. Sau OWNER permission §0A, dry-run exact sorted candidate paths + SHA256/state/ref proof, kiểm tra lại ngay trước xóa. Không có chứng cứ đủ => nợ vẫn OPEN, KQ DỪNG.

B · Helper: chỉ queue/out/*.json, completed queue/done và p02 snapshot superseded/noncurrent, quá 7 ngày, chứng minh không có pending/running/error, consumer/alert/current pin/P02/audit/recovery refs; queue/in và current state phải giữ. Dry-run exact candidates/hashes + recheck references, UNKNOWN => KEEP. Không sửa helper/HJW code; no concurrent HJW trước mọi mutation.

C · mcp-roots/gh: git fsck trước/sau; kiểm HEAD, refs/recovery/reflogs/bundles và P02 writer lock, chỉ native git repack -d (không dùng git gc, kể cả --prune=never, vì gc tự chạy reflog expire theo gc.reflogExpire 90d/unreachable 30d) nếu chứng minh tất cả refs/objects phục hồi còn nguyên. Cấm prune/reflog expire/ref rewrite; không đủ bằng chứng => nợ OPEN.

ONE VALVE: dùng lại công cụ hiện có trước. agent-data/helper không có retention cho A/B (P73), nhưng VPSC đã có người gác kho /opt/incomex/scripts/vps-retention.sh (R2–R5b: cron mỗi giờ /etc/cron.d/vps-retention, flock, log /var/log/incomex/vps-retention.log, luật (a)–(l), chế độ chỉ in danh sách + sha256 như --chi-l-thu, LOCKED trong code-ledger, đã là van cron=vps-retention\.sh của 4 dòng sổ). Mặc định: thêm luật A/B/C vào script đó, mỗi ngày một lượt theo giờ UTC như (k), qua incomex-config-apply-v0 + rollback, chạy lại chế độ thử của luật cũ để chứng minh không hồi quy; không sửa /etc/cron.d/vps-retention. Chỉ khi không làm được (ghi lý do đo được) mới tạo đúng một script retention dưới /opt/incomex/scripts/ + một systemd timer (service unit tối thiểu của nó) chạy hằng ngày, gọi A/B/C theo điều kiện an toàn, cài qua incomex-config-apply-v0 và đăng ký Code Ledger/Config Guard/coverage/rollback. Lượt đầu dry-run, test fail-closed với active/unknown/symlink/ref mismatch; rồi mới thực thi cleanup trong quyền §0A. Mỗi lượt timer chạy trong shared lock, có receipt và quan sát actual bytes; có job khác thì SKIP, không sleep/WAIT.

Mọi source phải có PRE/POST bytes/slope, proof reference safety/restore, status INSTALLED_AND_PROVEN|DRY_RUN_ONLY|BLOCKED, receipts; move trên cùng ổ và cap-only không chứng minh giảm tăng dung lượng.

## 3. #11 REAL GREEN / POST GATE
- Any protected mutation must apply by `incomex-config-apply-v0` with exact target and validated rollback. Do not change registry debt due/status directly to hide `DEBT_OVERDUE`. Registry chỉ được đổi ba CONTROL_DEBT sang ROTATING khi van đã chạy thật có receipt, có proof cleanup/Guard/rollback; valve bắt buộc gồm cap= + phần sống: cron=vps-retention\.sh (kèm file=vps-retention.sh~<mã luật>) nếu dùng cron hiện có, hoặc fresh=<tệp dấu chỉ ghi khi lượt dọn chạy xong>@26 nếu là systemd timer — valve_ok cron= chỉ đọc crontab root + /etc/cron.d (storage-watch.py:412–417), không thấy systemd timer. cap=/file= đứng một mình là xanh giả, cấm. Không sửa storage-watch.py trong N2a; khe valve_ok cho qua cap-only (P73) ghi nợ VPSC lượt sau. Không đổi hạn debt/kind/threshold để né đỏ. If missing control, keep explicit RED/DEBT and explain.
- After each bounded candidate apply, validate source consumers/queue recovery/refs, Config Guard, existing retention paths. POST should be **same-or-better relative to legitimate PRE**: #11 GREEN, other 21 lamps no newly RED, Guard protected footprint exactly approved modifications with coverage, no secret leak. **Cổng XONG đủ cả ba, đo thật:** (i) mỗi nguồn A/B/C có receipt lượt chạy thật của van + bytes PRE/POST đo được (cap=, file= hay sửa hạn nợ không tính); (ii) Kuma #11 GREEN với lý do mới do storage-watch tính lại; (iii) Protection Guard POST --coverage PASS, không đèn nào mới đỏ so với PRE_RED_SET. If #11 remains RED from these debts, KQ DỪNG, do NOT override it.
- If RED arises from another independent VPSC defect, give one bounded root cause/owner, no scope widening without separate authorization. No nightly/24h terminal wait, no background experiment; existing watcher/Guard monitors steady state after run.

## 4. KQ / SHARE SLOT WITH GRAPH
Report `KQ@VPSC-N2A-DISK11-CONTROLS-20261011-01 XONG|DỪNG` with evidence for each of the 3 debt sources, Config Guard PRE/POST, Kuma #11 final reason, no regressions, actual vs forecast disk and slope, tests, rollback, any unresolved debt and NEXT_TRIGGER. Write VPSC COLLAB (same commit release root busy) and existing BAO-CAO; leave Graph PROMPT/SHA untouched.
- If **XONG and #11 GREEN with Guard proof**, note `NEXT_TRIGGER=GRAPH_R10_HOST_FRESH_PRE_READY_EBF52956...`; host Graph independently does fresh Guard PRE and issues READY at its already signed SHA, then Owner manually pastes R10.
- If **DỪNG**, return exact smallest fix/Owner-only decision, do not ask Owner to run Graph against RED and do not relabel as green.

## 5. STEP WALK
| Phase | Who | Trigger | Proof | Fault |
|---|---|---|---|---|
| S0 | Claude Code | exact REVIEW+HOST READY+Owner pasted RUN | no concurrent + PRE snapshot/resource/protected footprint | KQ DỪNG before mutation |
| A transactions | Claude Code | S0 pass | operation/recovery reference proofs, native control candidate/dry-run | preserve evidence, continue independent sources |
| B helper | Claude Code | A measured | queue/P02 reference/TTL control tests | preserve evidence, continue |
| C gh | Claude Code | B measured | fsck/refs/GC non-destructive validation | preserve refs, no prune |
| POST | Claude Code | A-C accounted | actual control receipts, true #11 GREEN, all other lamps same-or-better | KQ DỪNG or rollback scoped delta |
| KQ | Claude Code | terminal | exact KQ, release root busy, no unapproved writes | next trigger VPSC or Graph R10 |

**DO NOT do C2, Graph, HJW mutation.** Claude P73 đã ký 4 sửa có điều kiện, Host P75 áp 4 sửa, Claude P76 chỉnh trong phạm vi 4 điểm theo mã và ACCEPT bản này; không thêm vòng review nếu không có blocker vật chất. NO READY trước Owner §0A permission và shared VPS free.
