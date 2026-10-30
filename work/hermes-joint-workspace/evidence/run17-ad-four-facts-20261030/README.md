# RUN17 — Agent Data four-facts source/PR candidate

Result: **G8_AD_SOURCE_PR_CANDIDATE_PASS**, not merge/deployment/G8_SYSTEM acceptance.

- PR: https://github.com/Huyen1974/agent-data-test/pull/358 — OPEN/DRAFT.
- Branch: `dev/codex-ad/hjw-g8-four-facts-20261030`.
- Head: `4851f6cde86bade6ce70433958cddc76a307f9f1`.
- Main/base: `b4c9ea19cf2e57594a231c2819e098fe0002c99a`.
- PR357 remains OPEN/DRAFT at `36c682914c9f412078113b6d85319f11356d1130`, unchanged.
- Current runtime source D2: `1cc706dc0f1ba7ef05f4631c04f604d2cacd9982`; image `sha256:4635e417e5400a9f85d1ed569f1c2f977845405bf7b8d834ab7002006f7d1045`; explicit `AGENT_DATA_WORKERS=4` read live.
- CI gate SUCCESS at the exact PR head, completed 2026-10-30 02:16:07 UTC: https://github.com/Huyen1974/agent-data-test/actions/runs/40990592102/job/123851762290.

## What changed

Exactly six AD files: two contract modules plus workspace_idempotency, workspace_tasks, workspace_tools and workspace_transfer. Four-facts errors, normalized names and provenance receipts; uploads/tasks carry declarations; replay hashes bind original attribution. No server/Hermes/Gemini/config/worker/queue algorithm changes. All original workspace_tools bytes remain before the added declaration installer, preserving Hermes infrastructure declarations and ACLs. The adapter explicitly classifies existing infra read/plan tools as non-source; it never grants access.

The PR is deliberately based on main, not on PR357. A separate Mac lab overlay applies the same semantic declaration changes to the freshly read running four-worker source. All three queue baseline files match PR357 bytes. `workspace_tasks.py` overlaps: KST must preserve PR357's enqueue_once and durable replay when rebasing; this draft is not a deployable replacement of the current source tree.

## Validation and limits

89 tests passed on main-based candidate; 90 on runtime overlay; no failures/skips. The runtime test accepts ten writes, claims four slots with six queued, completes all ten and replays all ten without duplicate jobs. This is controlled in-process SQLite scheduling plus real temporary file writes, not a four-OS-worker load benchmark. Public workspace catalog remains 26 entries, KB/server unchanged. Auth/ACL, missing facts/zero mutation, aliases, receipts, idempotency, uploads and legacy behavior verified.

Docker daemon unavailable on Mac: IMAGE_REBUILD_NOT_TESTED. No VPS writes/build/lease/Guard, no merge/deploy, no production mode changes, no modification of PR357. G8_SYSTEM, advertise rollout, cold-AI C1/C2 and enforce NOT_TESTED.

Temporary clone removed after PR remote-head readback; local run17 source snapshots/evidence retained. Tests spawned no supervisor/background worker. No CI rerun or waiting loop.

## Evidence index

- `manifest.json.md`: pinned source/image, both candidate hashes, diff and test-file checksums.
- `gh-main-to-pr.patch.md`: exact six-file PR diff against main.
- `runtime-overlay.patch.md`: same declaration behavior adapted to current queue source, with queue logic preserved.
- `tests.md` and `tests-source.md`: results and reproducible Mac fixtures.
- `github-receipts.json.md`: actual draft PR, exact HEAD/base, successful gate, unchanged PR357 and cleanup.

Authority: HJW P473 READY@656bf8719eed13d16a793792f03f72ff0d81c6c1; PROMPT SHA256 7ea0326cd389e97b5f3544d21bf43ef7036323478ec54621d65c47c826fdab84. STARTED commit 7750d9ddcce721cea28bf4135494284a307433f7. Owner direct RUN17 dispatch. Next: Host accepts P474 and dispatches KST Claude Code CLI review through the existing workflow; no automatic RUN18/merge/deploy.
