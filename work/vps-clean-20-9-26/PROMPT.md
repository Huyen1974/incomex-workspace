# PROMPT — VPSC N2a + C2 PROVENANCE · 08/10/2026

RUN_ID: VPSC-N2A-C2-CONTROLS-20261008-01
Task: work/vps-clean-20-9-26
Executor_Surface: Claude Code CLI, Mac Owner → VPS1 SSH, only via existing reviewed gateways
Repo_Write_Path: workspace_* root=workspace
Evidence_Dir: /opt/incomex/work/vps-clean-20-9-26/N2A-20261008/
Report: same task BAO-CAO.md, one new section ## N2a-C2; COLLAB.md only for lifecycle/KQ.
STATUS: DRAFT · NO READY · NO RUN. Reviewer ACCEPT exact last-touch SHA, Host READY same SHA, read-gate then RUN. Do not reuse R7 READY/RUN.

## 0. OWNER GOAL AND LIMIT
Owner: stable VPS, truthful alerts, every disk growth source identified and bounded, provenance protection for running code, no endless waiting. P68 R7 already terminal DỪNG at C2; A/B/C1/C3/D and POST 22/22 PASS are retained. Do not rerun or undo proven PASS work.

One RUN with two lanes that do not block each other: **C2 evidence reconciliation** and **N2a three existing-source controls**. No unrelated #19, production core restarts, swap changes, Directus pressure knob, agent-data image changes, Graph trial cleanup, key rotation, new task/architecture/file, package upgrades, network/auth changes. R8 is scoped to proven additive maintenance and provenance, NOT broad cleanup.

Security/owner gate: Owner-only deletion/irreversible history pruning remains prohibited without a separate explicit Owner decision. Existing copies, references, and rollback must remain recoverable; no mass Git add/commit of unknown DOT code, no trust upgrade solely from live hashes.

## 1. S0 READ AND PRE GATE
Read AGENTS.md (DROOT30/31/48/50/52/A2/A9), root COLLAB, task COLLAB P67–P69 and §0.3, BAO-CAO ## R7 §§0/6/7/8, this PROMPT. Assert Reviewer ACCEPT + READY same full SHA, no other shared-VPS STARTED/mutation. If not green, report KQ DỪNG before mutation; no terminal HOLD.

Capture independent PRE: 22 Kuma monitor states/reasons, Config Guard and INV23, original registry hashes, code-ledger (N=558, M=244, K=314 as historical baseline), disk-watch inventory/rates/debt flags, df, source service health, MemAvailable, memory PSI, vmstat swap in/out and recent OOM/cgroup counters. Swap was 2/2 GiB used in R7; **swap usage alone does not prove active pressure**. If current memory/PSI/OOM shows danger for a proposed operation, skip mutation and report resource gate; no swapoff, sysctl, reboot/restart, memory-limit guess, or forcing green.

After PRE, STARTED@VPSC-N2A-C2-CONTROLS-20261008-01 <UTC> · executor=Claude Code CLI only while actually running.

## 2. LANE C2 — 312 UNKNOWN PROVENANCE; READ + PROVE, NOT BLESS
Read the frozen R7 `c/ledger-final.json`, `c/reg3/code-ledger.tsv`, and current `scripts/code-ledger.tsv`. Precisely distinguish 314 uncovered = 312 lacking proof + 2 with provenance but explicitly excluded; preserve exclusion. Reconcile per file ID/path/hash with:
(A) authoritative repository commit at a known path + same bytes;
(B) accepted build/deployment manifest + verifiable hash and prior acceptance receipt;
(C) labels/comments/mtime/current runtime hashes only = NOT proof.

Batch by actual evidence families, not 312 Owner/Reviewer manual approvals:
- 227 `dot/bin` DEL-1I whose current contents differ from HEAD; find label provenance, historical review/deploy manifests and matching authoritative source. A DEL-1I label alone NEVER certifies current bytes.
- 12 untracked and other DOT outliers;
- 38 systemd units, 10 /usr/local/sbin, 5 cron.d, 4 logrotate, remaining paths grouped by owning system/source.
- inaccessible mount-ro trees remain UNKNOWN; no bypass.

Deliver a machine-filterable per-row classification in existing runtime evidence: PROVEN_REPO / PROVEN_ACCEPTED_ARTIFACT / DECLARED_ONLY / UNKNOWN / EXPLICITLY_EXCLUDED, with source ref, hash, evidence ID, change risk, owner. Sum MUST reconcile to 558/244/314 and 312+2; gaps report mismatch, never silently drop. For PROVEN rows only: register in Config Guard if owner policy and exact verified manifest allow, through reviewed config gate with rollback + post-tests; otherwise report as eligible without mutation.

For unproven DOT/unit/scripts: DO NOT copy from runtime into Git as if it were historical original; do not bulk `git add` 227 files; do not overwrite live code. If adoption of a new baseline rather than restoration is required, record one bounded Owner-only decision with counts and exact scope, not one request per file. Do not mark C2 complete while any in-scope provenance UNKNOWN remains.

## 3. LANE N2a — THREE NAMED CONTROL_DEBT SOURCES
Deadline from P68/B7: 2026-10-11T01:00Z. Freeze sources and queue states before applying anything. Reuse existing retention/cron/gateway tools only; use `incomex-config-apply-v0` + Config Guard for approved edits. No new service/parallel pipeline. Install only SAFE, reversible controls with tests; require explicit Owner gate for actual irreversible deletion/pruning.

A. `/opt/incomex/data/workspace-tools/transactions`
- Baseline 916 backup_id directories/358 MB/+62 MB per 24h, candidate complete >14d (~198 dirs, 76 MB).
- Keep every backup referenced by prepared/push_unknown/rollback_conflict/unknown, queued/running work, operation_id/idempotency/recovery state.
- Prove state via canonical queue DB and recovery records; do not infer completion from directory age. Implement existing-route retention candidate selection + dry-run list/reason + reversible move-to-archive only where native consumer guarantees no references and original restoration is tested. Do not delete any contents until Owner permission.

B. `/var/lib/incomex-mcp-helper`
- Baseline queue/out+done+p02 (~+105 MB/24h), candidate >7d (~96 MB).
- Preserve queue/in, running/pending/error, current P02 statuses/alerts and latest known-good.
- Implement existing-route 7d classification+dry-run, with reversible/archive-only operations if consumer references and rollback are independently verified. No hard delete.

C. `/opt/incomex/mcp-roots/gh`
- Baseline 179 MB, 4256 loose objects 126 MiB, refs/recovery and P02 refs must survive.
- Run `git fsck`, refs/reflog/recovery inventory and `git gc --dry-run`/equivalent provenance checks without mutating history. Do not run destructive `git gc --prune` absent explicit Owner approval. Existing GC schedule candidate = 2-week prune, not yet authority to apply.

For each lane report before/after bytes, actual daily growth, live control state vs DRY_RUN_ONLY, expected steady-state *as estimate*, rollback proof. Moving data within same filesystem does NOT count as reclaiming disk; refuse false "sealed leak" PASS. A source remains CONTROL_DEBT until a live bounded control is both authorized and observed; do not hide overdue flags.

## 4. ALERT TRUTH / RESIDUALS
- SLOPE7D possible false-looking red 12–13 Oct from Graph one-off event and missing comparable 7-day taxonomy baseline: **NO blanket waiver or threshold lowering**. Preserve RED/UNKNOWN according to current B3; annotate baseline gap and identify historical one-off if source proof exists. No repetitive duplicate pager changes in this RUN.
- NOISE_GUARD measured idle 12 KiB vs busy-time -66 MB: remeasure independent live samples without overlapping own fixtures, do not silently relax threshold; report anomaly.
- #19 is push monitor, not HTTP; do not apply unsafe R7 recipe. Keep exact D6.
- Swap full 2GiB, Chrome-headless OOM and Directus 503: record current pressure + provenance, no speculative core changes or restart.
- O-R7-KEY remains Owner-only separate security decision, not a blocker for this read-only/safe maintenance scope.

## 5. STEP_WALK (DROOT48)
| Phase | Who | Trigger | Evidence | Fail response | Next |
|---|---|---|---|---|---|
| S0 read/PRE/concurrency/resources | Claude Code | exact READY+RUN | gate, PRE snapshots | KQ DỪNG clean | C2 |
| C2 source reconciliation | Claude Code | S0 PASS | per-row 558 ledger, group proof | keep UNKNOWN, continue independent N2a | N2a |
| N2a transaction retention | Claude Code | C2 evidence frozen | referential proof, dry-run/rollback | isolate this source, continue | helper |
| N2a helper retention | Claude Code | transaction checked | in/out/done/p02 proof | isolate this source, continue | gh |
| N2a gh object retention | Claude Code | helper checked | fsck/refs/prune dry-run | isolate source, continue | POST |
| POST-PROTECT | Claude Code | lanes finished | PRE/POST, exact changes, Guard, Kuma, Telegram | rollback only changed footprint, KQ DỪNG | KQ |

No WAIT/HOLD, no sleeping for future samples or deadlines, no terminal reuse. After scoped work record KQ XONG only when promised evidence/authorized controls within this bounded RUN are satisfied; otherwise KQ DỪNG with individually preserved PASS work and one actionable next action. Final VPSC task cannot close until control debt and C2 evidence gaps resolved + independent 24h clean machine proof.

## 6. POST / REPORT
Use same-or-better independent PRE→POST: no new RED, no secret disclosure, no source mutation unless approved and tracked, Guard coverage rows per changed config, rollback actual, keep #11/#22 semantics. Telegram via existing sender <=3 lines + message_id if runtime mutation occurred. No new watcher/timer. BAO-CAO ## N2a-C2 and task COLLAB must name C2 PROVEN/UNKNOWN/EXCLUDED counts, live controls vs dry-run, remaining debt, swap/PSI/SLOPE status, exact Owner gate (only if genuinely required), and owners.
KQ@VPSC-N2A-C2-CONTROLS-20261008-01 XONG|DỪNG
