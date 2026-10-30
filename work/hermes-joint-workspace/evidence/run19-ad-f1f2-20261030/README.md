# RUN19 — F1/F2 source and CI evidence

KQ: G8_AD_F1F2_SOURCE_CI_PASS. PR358 remains OPEN/DRAFT; NOT KST_ACCEPT, NOT G8_SYSTEM, NO MERGE/DEPLOY.
Executor: Codex Desktop/MacBook. RUN HJW-G8-AD-F1F2-FIX-GATE-20261030-19. Host READY 16b112eab51dd48cf33cd86ffc99c82da2bd7458; PROMPT sha256 16179733fa30883fa40e6948e86a531e8b7e49b534b6bf603f6b522d313d9631.

- PR: https://github.com/Huyen1974/agent-data-test/pull/358
- Before: 4851f6cde86bade6ce70433958cddc76a307f9f1. After: 58a44c0559bfd42e7e62f5faf8df49ebd2259e78.
- main: b4c9ea19cf2e57594a231c2819e098fe0002c99a unchanged.
- PR357: 36c682914c9f412078113b6d85319f11356d1130 OPEN/DRAFT unchanged; no queue/Hermes edits in RUN19.
- Exactly 3 RUN19 files: declaration_contract.py, tests/unit/test_hjw_four_facts.py, .github/workflows/ghm-pr-gate.yml. Eight files in total PR358. source-diff.patch is the exact commit diff.

## F1
Same final test file against old contract: 20 failed / 98 passed (red.txt). Fixed: 118 passed (green.txt). Covers active/archived IDs, directories and files, close/reopen, multi-operation, absent/unsafe path, declared mismatch, cross-task refusal. Actual fixture filesystem transactions close/reopen and reject wrong-task with zero mutation. A preliminary harness alias/schema error was corrected before these retained product results; no production failure inferred from harness setup.

## F2
Existing CI Unit tests list gained one unconditional filename only. No trigger/permission/policy/scan/runner changes. Mac exact list: 151 passed (unit.txt); old list collects 33, new suite 118. Local missing-file probe exits 4; deliberate appended failing test exits 1 with 151 otherwise passed (gate-missing.txt, gate-failing.txt). Original file restored before commit. Thus neither missing nor failing new suite can silently pass the existing set-e gate.
GitHub run https://github.com/Huyen1974/agent-data-test/actions/runs/41025111338 SUCCESS, head 58a44c0559bfd42e7e62f5faf8df49ebd2259e78, merge-test/executing-workflow c22c9192d5f68588db89d6c2d00949b4b95da35a. ci-run.json records all steps; ci-evidence.txt includes exact mandatory TESTS filename, pytest command and actual 151 passed in 8.94s. This is 33 existing + 118 new, not reuse of the old green run. gate_matches_main=false and ci_change_kst_review=true explicitly require independent KST review.

## Regression and boundaries
RUN17 main 89 passed; Mac runtime/PR357 overlay 90 passed, contract temporarily overlaid then restored. No production/VPS operations; no PR357 edits; no push main, merge or deploy. Queue fixture is not real-client/OS worker evidence. Local caches/build scratch removed; clone and evidence retained for review. GitHub gh pr edit hit legacy Projects GraphQL incompatibility; official REST update succeeded without changing scope.

NEXT_TRIGGER: Host accept P478 and dispatch independent KST review of F1/F2 + workflow diff. Remaining G8_SYSTEM work is unchanged: workspace_exec/KB logical writes, trusted auto-fill, PR357 empty-DB bootstrap debt, Linux image rebuild/rollback and real-AI C1/C2. Not implemented in RUN19.

## Files
README.md: result, pins, boundaries and next trigger.
source-diff.patch: exact three-file commit.
red.txt / green.txt / unit.txt: RED, GREEN and local CI list.
gate-missing.txt / gate-failing.txt: negative gate probes.
run17-main.txt / run17-overlay.txt: preserved regression results.
ci-run.json / ci-evidence.txt: GitHub status and actual execution.
