# PROMPT — GS-K4-READTIME-SOURCE-FENCE-20261028-21
RUN_ID: GS-K4-READTIME-SOURCE-FENCE-20261028-21
TASK: work/graph-server · K4 source fingerprint at graph-v1 read-time, not code/data ingestion.
STATUS: DRAFT_BLOCKED_RESOURCE / NOT_READY / DO_NOT_DISPATCH. P297 Host accepts Claude P296 B2 but RAM <3GiB and runtime graph-v1 reload/Guard rollback unverified. Host later signs exact PROMPT last-touch SHA40 and SHA256; no READY now.
EXECUTOR_SURFACE: Claude Code CLI Mac, Git-CAS + authorized Graph/VPS read; one CLI.
WRITE_PATH: approved graph-v1 reader code only via apply-v0, VPS-GHI CAS, Config Guard PRE/POST, byte-exact rollback; task P/Board/GS-RM1/view/root KQ one Git-CAS commit. No Neo4j nodes/edges, Nuxt code or label, PG/Directus/Qdrant/Lark/GSM, Guard policy, timer, new monitor/CDC.
READ: AGENTS A0/A5/A6/A8/A9/DROOT29/30/31/44/56/57/58/59, root/task COLLAB P194/P207/P221/P223/P236/P261/P272/P294–P297, GS-RM1, exact deployed graph-v1 wrapper, current cert-baselines and apply-v0/Guard rollback manifests. Historical repo tools require live hash check.
REVIEW_REUSED: Claude P296 §7 and P236. No new B2 if scope identical.
OWNER_CONSENT_EXACT (requires later READY): "Tôi giao Claude Code CLI chạy GS-K4-READTIME-SOURCE-FENCE-20261028-21 CHỈ SAU KHI GPT Host ký READY đủ RAM và đường lùi. Chỉ cập nhật lớp đọc graph-v1 để dấu nguồn thay đổi/mất quyền/thiếu baseline trả MỘT PHẦN/NOT_ACTION_SAFE. Không sửa Graph data, Nuxt, PG/Directus hay làm xanh #24; thiếu an toàn thì dừng trước ghi."

## FIVE HARD DoR before Host READY
1. Source cheap fingerprints already available: Docker IDs, ports, unit hash, Git HEAD/worktree, DEPLOYED Nuxt server/index.mjs SHA+nitro build date (NOT current GitHub HEAD/generic Node image), cert/catalog; match baseline actually saved at certificate time T. Missing original baseline => SOURCE_VERSION_UNVERIFIED+NOT_ACTION_SAFE, not retroactive green. No new reader/CDC.
2. subprocess rc, stderr, permission, bounded timeout checked; incomplete/error => UNKNOWN/NOT_ACTION_SAFE, not empty-success. If reusing native_live.py, fix silent failure first.
3. Deployed graph-v1 code and narrow approved apply-v0 target, Guard PRE/POST, byte-exact backup and rollback verified. No new sudo/key, no graph/source write.
4. Root VPS-GHI free plus fresh MemAvailable above 3GiB floor AND measured safe graph-v1 reader reload headroom; swap/service pressure safe. Current measured 2.67GiB => FAIL now. Code DELTA separate >=6GiB.
5. Negative fixtures on isolated COPY: changed fingerprint => SOURCE_CHANGED_SINCE_CERT/NOT_ACTION_SAFE; read denied/failed/missing baseline => UNVERIFIED/NOT_ACTION_SAFE; unchanged may only preserve existing valid N4 label, never promote PARTIAL. No production source mutation to test.

## Only after signed READY
S0 Read current STOP/READY/lease/RAM/Guard. Any hard failure => DỪNG before mutation, no WAIT.
S1 Inspect live reader and cert fingerprint baseline; choose only supported cheap signals. Sources without baseline remain UNKNOWN.
S2 Run isolated negative fixtures and rc/stderr/timeout checks, capped CPU/latency, no production impact.
S3 One protected graph-v1 reader update via approved apply-v0/CAS lease/Guard/rollback and code ledger; no heavy Enola/Cognee/temporary Neo4j, no Nuxt relabel.
S4 Cold graph-v1 N4 verified stable/stale/missing source; no false green, preserve #24 natural state; Guard failure => rollback and DỪNG.
KQ@GS-K4-READTIME-SOURCE-FENCE-20261028-21 XONG|DỪNG: evidence hashes, negative matrix, Guard PRE/POST, source limits, all remaining G1/G2/G3 PARTIAL if not independently proven; DOCS_MATCH Board/GS-RM1/P/view/root one Git-CAS commit, no private raw data in public repo. Do not self-run next.
STEP_WALK_V1: Owner manual dispatch AFTER READY -> S0 -> S1/S2 -> S3 guarded -> S4 cold N4 -> KQ.
