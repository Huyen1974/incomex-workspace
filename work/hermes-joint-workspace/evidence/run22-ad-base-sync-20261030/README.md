# RUN22 — normal main merge into PR358 development branch

**KQ PARTIAL_BASE_SYNC_CI_PENDING. Base sync and Mac tests PASS; fresh CI job queued, zero steps started. NOT G8_AD_WEXEC_SOURCE_CI_PASS.**

Executor Codex Desktop/MacBook; GPT Chat Host. RUN HJW-G8-AD-BASE-SYNC-CI-20261030-22; READY bd2f115216828a626ac9bad06995f46afb69b772; PROMPT SHA256 3faa4a00fe893a771e1c3811e0d49c0b417830f67f3f1a83ec34c86255048866. STARTED cab946ba0cf5e584ed0e0223a56323e4940ecae8.

PR https://github.com/Huyen1974/agent-data-test/pull/358 remains OPEN/DRAFT.
Before head 53c34ec745c6980a23996273e94b12fdd129b06a; old base b4c9ea19cf2e57594a231c2819e098fe0002c99a.
New head 833bbc183494166496ffbaad0ba3933ea23d3fb4, exactly two parents: original PR head + main 6160f9ad6e5d16012dfe20bb59949abf5ffadad2. PR remote baseRefOid now 6160f9ad6e5d16012dfe20bb59949abf5ffadad2.
Used git merge --no-ff --no-edit origin/main, then ordinary non-force push of the development branch. No rebase, PR merge, main push or functional edit.

## Source preservation
before.json records 25 newly added main files (disjoint from the 10 PR paths), original PR blob IDs and refs. after.json proves new merge parents, ancestor check, unchanged 10-path PR diff, and all ten blobs byte-identical to before sync. This includes workflow/test/carrier files: no CI policy modification. PR357 remained OPEN/DRAFT 36c682914c9f412078113b6d85319f11356d1130 (pr357.json), not merged into this candidate or modified.
The reused clone was shallow. Initial merge refused to infer unrelated histories; no tree changes occurred. Fetched 20 more history levels without tags; Git then found exact common ancestor b4c9ea19 and merged normally, without allow-unrelated-histories or conflicts.

## Tests and CI
Mac existing Unit test list after merge: 202 passed (unit.txt). No need to repeat unchanged RUN21 overlay integration (262 passed already recorded in P482); no new claim of integration execution.
Fresh pull_request synchronize CI: https://github.com/Huyen1974/agent-data-test/actions/runs/41065092635, head 833bbc183494166496ffbaad0ba3933ea23d3fb4. See ci-run.json / ci-evidence.txt for final status, exact preflight base and actual test output; old failed RUN21 event was not rerun.

## Boundaries, cleanup, next step
0 VPS mutation/lease, 0 PR357/Hermes change, 0 merge/push main/deploy, 0 function/workflow edits. Local caches removed, clean clone retained as evidence; no test processes or waiting terminal. Gate/source PASS does not mean KST_ACCEPT/G8_SYSTEM or production. Remaining roadmap unchanged: KB MCP/stdio/REST writes and trusted auto-fill, PR357 fresh DB race/two-file integration, Linux build/rollback, advertise, real-client C1/C2 and guarded enforce. Host accepts P484 before issuing RUN23; no automatic RUN.

Files: README.md; before.json (25 added main paths and original 10 blobs); after.json (merge/10-path preservation); merge.txt and merge-proof.txt; unit.txt; pr358.json/pr357.json/main-final.txt; ci-run.json/ci-evidence.txt.
