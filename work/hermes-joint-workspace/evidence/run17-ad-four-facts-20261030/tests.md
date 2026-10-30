# RUN17 validation

## Main-based candidate

```text
........................................................................ [ 80%]
.................                                                        [100%]
89 passed in 0.18s
```

## Runtime four-worker candidate

```text
.........................................................................................QUEUE10: accepted=10 active=4 queued=6 completed=10 replay=10 duplicate_jobs=0
.
90 passed in 0.35s
```

Both variants verify declaration errors/zero mutation, names/normalization, verified versus self-declared context, receipt provenance, idempotency, upload/import and queued write carry, legacy calls and ACL rejection. Added runtime case proves 10 accepted, 4 claimed + 6 queued, 10 completed, 10 replays, zero duplicates; changed declaration with reused operation ID rejects.

Three negative impacts: (1) full pre-existing main workspace_tools bytes remain as exact prefix, including Hermes AGENT_INFRA_TOOLS and ACL logic; ACL tests reject self-declared Owner/root attempting forbidden tools/paths; (2) Claude/fs/Gemini/helper files absent from PR and runtime overlay; shared contract bytes reused unchanged; (3) runtime workspace_runtime.py and workspace_execution.py unchanged, workspace_tasks functions other than install/run byte-equivalent AST, all three baseline queue files match PR357; enqueue_once and durable replay retained.

Workspace catalog stays 26 tools in all four source trees; no KB/server/tool-count changes.

Docker daemon is unavailable on Mac. IMAGE_REBUILD_NOT_TESTED; no VPS build. G8_SYSTEM, deployment, real AI C1/C2 and enforcement NOT_TESTED.

A first gh pr create invocation outside the clone failed before creation (not a Git repository); retry inside correct clone created one PR #358. No failed application test, no hidden skips, no PR357 modifications.
