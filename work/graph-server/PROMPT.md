# REVIEW DRAFT — GS-WORKERS6TO4-RAM-DECISION-20261029-23
TASK: work/graph-server · REVIEW ONLY of shared AgentData resource proposal. Any later production execution belongs existing work/vps-clean-20-10-26 under same GPT Host. No new task.
STATUS: DRAFT_FOR_CLAUDE_CHAT_P303 / NOT_READY / DO_NOT_DISPATCH / OWNER_CONSENT_NOT_GIVEN. This is NOT an executable Claude Code CLI prompt.
HOST GPT Chat · REVIEWER Claude Chat · future WORKER Claude Code CLI only after explicit Owner YES and a separate signed VPSC2 READY. Do not disturb existing VPSC2 RAG-A READY/ongoing sessions.
EVIDENCE: Graph P301 f9a47f14; archived MCPW-STAB 24/09 benchmarks: six workers intentionally selected, 2-worker prior failures, 8/12/15-way post PASS, four workers untested; VPSC2 Owner goal optimize VPS without breaking AI gateway.

P303 ONE ROUND (no production action):
1) Judge whether bounded 6→4 trial is reasonable given memory PSS and historical throughput; cannot guarantee RAM gain nor no 503. Compare only evidenced alternative claude-mcp restart (benefit unmeasured, temporary).
2) Explicit Owner permission must cover 30–60s AgentData gateway interruption and reduced parallel capacity. One CLI at a time, no active conflicting VPSC2 RAG-A RUN/VPS-GHI, avoid busy sessions.
3) Future DoR: verify live AGENT_DATA_WORKERS=6 and approved compose baseline, one-field diff, apply-v0 vpsup-docker-compose, Guard PRE/POST, source hash, rollback 6, bounded wait for health <=5m. Do not change other fields, PG/Directus, secrets, Graph, swap, registry, policy.
4) Future POST: measure actual MemAvailable 2 times, service health, existing initialize/tools/list + protected read/stat/search and permitted Git-CAS readback; compare gateway 503, timeout, OVERLOADED, p50/p95 to known baseline using existing metrics, no heavy synthetic burst. Regress => stop/revert via approved path. K4 not READY until >3GiB PLUS safe reader budget and 2 reader error fixes; 6GiB code import still NOT_READY.
5) Claude Chat writes P303 advisory to Graph COLLAB only, no mutation/PROMPT edits. GPT Host B3 decides; if approved technically, ask Owner one scoped YES/NO before issuing production VPSC2 READY. Do not open a second review unless a real new technical blocker.
