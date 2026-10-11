# PROMPT — VPSC-N2A-DISK11-CONTROLS-20261011-01 · THREE CONTROL_DEBT #11 HOTFIX (SCOPE N2a)

RUN_ID: VPSC-N2A-DISK11-CONTROLS-20261011-01
Task: `work/vps-clean-20-9-26` (VPSC) · D22/roadmap N2a, **not a new task**.
Executor: Claude Code CLI (new session), Owner manually pastes after **Claude Reviewer exact ACCEPT + GPT Host READY same SHA**.
Repo_Write_Path: existing Incomex MCP `workspace_*`, root=`workspace`; VPS config/runtime via already accepted native paths and `incomex-config-apply-v0` only.
Status: **DRAFT · REVIEW REQUESTED · NO READY · NO RUN**.
Evidence: reuse `/opt/incomex/work/vps-clean-20-9-26/` under a run-scoped subdir; report one section under existing `BAO-CAO.md` and KQ in task `COLLAB.md`. Never create duplicate repo files as progress notes.

## 0. GOAL — CLEAR THE *ACTUAL* BLOCKER, NO SCOPE CREEP
Owner has directed priority to complete Graph R10 promptly; the sole known hard execution gate is **Kuma #11 Disk Usage RED** caused by three VPSC `CONTROL_DEBT` deadlines 2026-10-11T01:00:00Z (not disk fullness: 11/10 physical free ≈42 GB):
1. `/opt/incomex/data/workspace-tools/transactions`: operation backups, baseline historical +62 MB/day.
2. `/var/lib/incomex-mcp-helper`: queue/out, done and P02 backlog, historical +105 MB/day.
3. `/opt/incomex/mcp-roots/gh` (under `/opt/incomex/mcp-roots`): loose Git objects/ref growth.

**Mục tiêu RUN N2a:** xác nhận nguyên nhân #11 từ live `scripts/storage-registry.tsv`, `storage-watch.py`, `disk-watch/state.json`, Kuma; áp dụng **các van tăng dung lượng an toàn có hiệu lực thật** cho đúng ba nguồn qua công cụ có sẵn, có bằng chứng và rollback, sao cho #11 chuyển GREEN thật, Guard/Kuma POST same-or-better, không phá dữ liệu. Không dùng "gia hạn cho hết đỏ", không nới ngưỡng/tắt đèn, không ghi FALSE PASS nếu còn nợ chưa đóng bằng control đã kiểm. Nếu một nguồn không thể khóa an toàn không cần quyền xoá, **KQ DỪNG**, giữ nguyên thứ đã PASS và đề xuất duy nhất một đường gỡ đúng nguồn.

**Ngoài RUN / bảo toàn:** C2 = 312 provenance UNKNOWN + 2 EXCLUDED vẫn mở ở VPSC (KHÔNG chạm/lấy danh nghĩa đã sửa), 3 EVIDENCE_DEBT PG/Qdrant/uploads vẫn mở, D22 health inventory & SMALLFIX việc khác để lượt sau. R7 A/B/C1/C3/D/POST đã PASS không rerun. Không chạm Graph R10, Hermes, Directus, PG nghiệp vụ, Nuxt, agent-data services, O-R7-KEY, #19, swap, Docker/image, network, cron mới, các task đã đóng. Không hard-delete/prune, git reflog expiration, queue truncation, broad wipe hoặc đổi production schema nếu chưa có Owner approval riêng.

## 1. S0 HARD AUTH + LIVE RESOURCE / GUARD
1. Đọc `AGENTS.md` → root `COLLAB.md` → VPSC Bảng, §0, P68–P72/BAO-CAO R7, last-touch PROMPT và reviewer/Host exact SHA. Kiểm **không có STARTED active/STOP/COUNCIL_ALERT, no HJW/Graph concurrent mutation**. #11 RED là **đối tượng đang chữa**, không giả vờ PRE 22/22: freeze `PRE_RED_SET` và raw reason, yêu cầu các đèn khác cùng Guard Config CLEAN hoặc có reason và owner minh bạch. Active resource floor: MemAvailable ≥3GiB + disk free ≥20GiB, no active PSI/OOM hazard. Nếu khác mà không giải thích được ⇒ KQ DỪNG sạch. **Do not wait/poll/hold terminal.**
2. Preflight full SHA and root gate before writing. If passed, record `STARTED@VPSC-N2A-DISK11-CONTROLS-20261011-01` + root shared busy atomically in one repo commit before first mutation. Preserve all actual scripts/registry/queue state/baseline hashes, support existing coverage Guard C3 and revocable rollback to PRE. No secret or raw customer data in Git/evidence.
3. Read-only inspect each `CONTROL_DEBT` row in `scripts/storage-registry.tsv`: canonical owner, due, path, cap, source classifier, current bytes/rate and what evidence the detector requires before clearing. Inspect existing `storage-watch.py`, retention scripts/timers, `incomex-config-apply-v0 --help`, and Config Guard protected paths. Freeze **allowed exact footprint matrix**, candidate patches and inverse before mutation. If status RED is a real fault (not just deadline) fix it under the same three source boundaries, not by changing the monitor definition.

## 2. N2a — THREE SOURCE CONTROLS, REUSE EXISTING FIRST
**A. transactions:** classify `workspace-tools/transactions` by canonical operation/queue/recovery status, not file age alone. Preserve all prepared/push_unknown/rollback_conflict/unknown, running/queued, operation_id/idempotency and rollback references. Use existing native retention path to enforce bounds/candidate selection with **dry-run + reversible archive only** if it has testable reference safety. Hard deletion or unverified consumer ownership: forbidden. If only dry-run can be proved, leave debt OPEN.

**B. helper:** inspect queue/in, out/done/p02, pending/running/error, latest stable/trace references and downstream consumer. Keep alert context/history required for rollback. Reuse existing 7d classification/TTL and native maintenance hooks; dry-run and reversible archive only if all active references preserved. Do not change HJW courier/gate/plugin; HJW may be watching same queues, so fresh-check shared busy before each mutation. A timer/TTL declared without proof of working bounding is NOT PASS.

**C. gh:** check refs/reflogs/bundles/protected remote heads/recovery/loose objects, `git fsck`; use existing safe maintenance candidates only after provenance/ref preservation is proved, with dry-run/oracle proof. **No `git gc --prune`, no aggressive GC, no reflog expiry** without separately explicit Owner release. Can set up safe ongoing monitor/compact only if within approved native Git capabilities and under Guard/protected footprint; do not alter current GH history to chase disk #11. If cannot prove a live protective control without deletion, leave debt OPEN, not fake green.

For each: measured PRE/POST bytes; observed growth or forecast with source; control `INSTALLED_AND_PROVEN | DRY_RUN_ONLY | BLOCKED`, consumer protection/rollback test receipts, native script/config diff+hash and follow-up monitor reason. Moving within same disk is NOT disk reclaimed. Keep current source alive.

## 3. #11 REAL GREEN / POST GATE
- Any protected mutation must apply by `incomex-config-apply-v0` with exact target and validated rollback. Do not change registry debt due/status directly to hide `DEBT_OVERDUE`. Registry can be updated **only after** each installed/verified control has evidence and native lifecycle contract permits it; then match Guard baseline using sanctioned apply. If missing control, keep explicit RED/DEBT and explain.
- After each bounded candidate apply, validate source consumers/queue recovery/refs, Config Guard, existing retention paths. POST should be **same-or-better relative to legitimate PRE**: #11 GREEN, other 21 lamps no newly RED, Guard protected footprint exactly approved modifications with coverage, no secret leak. If #11 remains RED from these debts, KQ DỪNG, do NOT override it.
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

**DO NOT do C2, do not rewrite Graph, do not open HJW mutation.** Reviewer should read this narrowly and sign exact SHA or state ONE material safety blocker; no second loop if accepted (DROOT53).
