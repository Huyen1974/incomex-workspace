# RUN16 test evidence

## Source-aligned regression

96 passed, 0 failed, 0 skipped; one pre-existing Pydantic settings annotation warning. Executed with Python 3.11 pytest on Mac. Existing FS/helper/contract/four-facts tests reused; contract imports target Claude copy, Agent Data-only forgery case excluded, single-contract equality narrowed to two FS/helper copies. Added two meaningful helper cases: legacy/nonwriter/off-menu and payload upload/carry/cleanup. No candidate application code changes from RUN14.

All 16 tested Python files were hash-compared with the final release manifest. The follow-up commit changes build script/README only, not source. Cases cover four required facts, aliases/unknown valid products, task mismatch, verified vs self-declared fields, missing-field guidance, zero mutation, optional schema, receipts, retry/idempotency, read preservation, transactions and helper carrier. ACL action functions remain byte-equivalent at AST level.

Linux: rebuilt Git-ref image, no network, no real credentials, no production data mounts, 512 MiB and 1 CPU ceiling. Real HTTP initialize → tools/list → tools/call passed: missing facts isError and no file; supplied facts writes file with raw/canonical/provenance receipt; replay succeeds; changed facts with reused operation ID rejected. This is a fixture HTTP client, NOT real-AI C1/C2.

Linux helper: 15 queue requests; all six writers reject missing carrier without invoking action, all six accept trusted carried facts with receipt; upload bytes preserved and temporary payload cleaned; legacy advertise writer and read-only git-head work; off-menu command denied. Privileged action bodies mocked, no external command execution.

## Three negative impacts

1. Hermes: Guard PRE/POST real read-only INV7 and INV19 check seven tools, authenticated E2E, wrong credential 401, unchanged ACL/no sudo/GSM/docker exposure. Agent Data live image remains pinned; no source/PR changes. No Hermes mutation canary attempted.
2. Claude/Gemini: offline catalog of original Claude, rebuilt Claude and original Gemini each has exactly 23 names with SHA256 `b6a1d817824c6c734d70c1c29287b1787c9d6612b9458ef0c98b19a458eee35c`. Claude original/candidate label `Anthropic/ClaudeAI [auth:claude-chat]`; Gemini uses its existing `gemini-agy [auth:google-main]`. Live Gemini image remains original. This does not authorize rebuilding Gemini from Claude candidate.
3. Shared helper: AST comparison of every original function/class shows only `handle` changed. Existing action/ACL implementations and function set preserved. Local and Linux cases verify unchanged legacy/nonwriter/off-menu behavior, plus bounded declaration carrier behavior.

## Observed failures and repairs

- New test initially forgot the existing response `id`; fixture expectation corrected, source untouched.
- HTTP/catalog fixture initially used an inaccessible parent mount / missing Python path and dummy PG environment; corrected lab-only invocation, source untouched.
- Initial parity assertion included 12 RUN14 AppleDouble files; recorded their removal separately from executable hashes.
- Git archive initially yielded 0664 app files; final committed build recipe explicitly restores 0644 files/0755 directories. Final image HTTP and metadata checks rerun PASS. Initial image was never deployed.
- One automatic command-approval review timed out; one retry succeeded. No approval bypass.

Rollback: reverse patch restores 14 baseline hashes and removes added modules. Retained ref plus pinned base rebuilds final image. No production changes or rollback needed.
