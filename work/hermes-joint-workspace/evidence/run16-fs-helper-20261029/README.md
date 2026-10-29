# RUN16 — G8 Claude/fs + helper candidate

Executor: Codex Desktop / MacBook; source Git: VPS local `/opt/incomex`. No GitHub remote, Agent Data PR, production deployment, advertise, enforce or restart.

Authority: Host P467 `READY@806230863ae5a26f0cd8ecade4317d32c083a593`; PROMPT SHA256 `adde2e7003a09606c88ab466392d69077c8abb20549a8b691a5b92164d1981ef`; Owner dispatch RUN16. STARTED/lease commit `03ef7cff2053ee02a6b9ccfb4a15d13a65f3dd3f`.

## Retained release

- Git ref: `refs/heads/hjw/g8-fs-helper-20261029-16`.
- Final commit: `7e3c04967d054e7a40877d00c264aaee623546d1`.
- First source commit: `c8c90f67a245c6f455dee5d48d5547eeb7dc7352`; follow-up changes only build recipe to preserve original file modes.
- Live Git HEAD unchanged: `00452246b1ac499d2e62cba8ea12be2aee919f2b`.
- Final candidate image: `sha256:5fb82e3a1296c06b19d04610c06081ff750a2da803eab65183548a664250b351`, tag `hjw-run16-fs:candidate`.
- Pinned base image: `sha256:bacd21605a06825d0a725bcaefecdf55abbe85e075ab7be8fe93da3e04b5f961`.

Candidate has four modified existing Python files plus two identical contract modules. Four release artifacts plus one build script record provenance, scoped patch and reconstruction. No extra shared runtime module. All 16 candidate Python file hashes match the tested sources; six reconstructed files, ten unchanged runtime-pinned files, zero unknown source files. Canonical/live source is not replaced: the separate ref intentionally reconstructs Claude runtime's hardcoded label, excluding canonical Gemini environment override. No Agent Data/Hermes source changes.

## Rebuild and rollback

Use the retained candidate ref in an isolated Git worktree; run `sh claude-mcp/release/run16/build.sh` there. The script exports exact HEAD, uses pinned local image, no network/pull, normalizes app directories to 0755 and files to 0644, and removes its temporary context. Recipe is committed; live checkout must not be used for mutation.

The final image retains every base filesystem layer, adds one app layer, and retains entrypoint, command, user, workdir and exposed-port metadata. All 12 executable Python source files equal RUN14 candidate bytes. Image IDs are intentionally different: RUN16 removes 12 non-executable AppleDouble `._*` files, changes source mtimes and RUN label; final file modes match RUN14. Exact hashes/metadata differences are in `verification.json.md`.

Rollback was exercised in isolated scratch by reversing the scoped cumulative patch once: all 14 original app/helper files restored byte-for-byte, new contract files removed. Pinned original image remains available and its catalog was exercised offline. Production never changed; no production rollback performed.

## Evidence map

- `manifest.json.md`: every source file's canonical, runtime and candidate hashes, provenance and consumer mapping.
- `verification.json.md`: source/rollback receipt, image/layer metadata, catalog identities, exact non-executable differences and HTTP receipt.
- `tests.md`: 96 local tests, Linux helper and HTTP checks, three negative impacts, limits and observed fixture issues.
- `scoped-patch.md`: exact seven-path RUN14 scoped patch; only six runtime destination files changed.
- `build-recipe.md`: final reproducible build script.
- `guard.md`: both POST attempts retained, cleanup and lease closure.

Acceptance is limited to G8_FS_HELPER_CANDIDATE_ONLY. G8_SYSTEM, Agent Data PR, real-AI C1/C2 and production rollout are NOT_TESTED in this RUN. Next: GPT Host review P468; no automatic next RUN.
