# PROMPT — GS-R4-CODE-FIRST-20261006-02

## 0. LỆNH / PHẠM VI

RUN_ID: `GS-R4-CODE-FIRST-20261006-02`
Executor_Surface: Claude Code CLI
Repo: `Huyen1974/incomex-workspace` · branch `main`
Task: `work/graph-server`
Repo Write_Path: Incomex workspace gateway `workspace_*` · root `workspace`
Runtime Write_Path: terminal/SSH hiện hữu tới VPS1; không tạo credential/gateway mới.

Owner 06/10 đổi thứ tự trial:
1. **quy mô nhỏ**;
2. **code graph trước** vì quan hệ code có ground truth rõ, dễ chấm;
3. embedding phải dùng **đúng model OpenAI mà Agent Data hiện dùng**;
4. vector Graph trial lưu **PostgreSQL/pgvector riêng**, độc lập Qdrant;
5. dữ liệu trial là disposable; trước production phải xóa sạch và rebuild;
6. KB hiện có nhiều nội dung cũ/nhiễu ⇒ **không ingest KB rộng trong RUN này**; KB curation là mốc roadmap bắt buộc trước production.

Đây là RUN triển khai micro-trial code-first. Owner cho phép thử model trong phạm vi dưới đây.
Không dùng dữ liệu cá nhân/Lark/customer trong RUN này.

§0.3: đọc lại và đối chiếu trước mutation.

## 1. READ-GATE / READY / STARTED

1. Bind đúng repo/workspace; đọc:
   - `AGENTS.md`
   - BẢNG + §0 + D mới nhất + P21/P22 của `work/graph-server/COLLAB.md`
   - `work/graph-server/PROMPT.md`
   - `work/graph-server/view.html` §16/roadmap hiện hành
   - root `COLLAB.md` dòng Graph/HJW
2. Xác minh READY full SHA khớp commit cuối chạm PROMPT; không HOLD/STOP/READY mới; không STARTED chưa KQ cho RUN_ID này.
3. Gate PASS → ghi:
   `STARTED@GS-R4-CODE-FIRST-20261006-02 <UTC> · executor=Claude Code CLI`
   rồi mới PRE.
4. Gate fail → 0 runtime mutation, KQ DỪNG.

## 2. PRE — FRESH RUNTIME GATES

Evidence:
`/opt/incomex/work/graph-server/evidence/GS-R4-CODE-FIRST-20261006-02/`

Runtime:
`/opt/incomex/work/graph-server/runtime/run1/`
(reuse retained RUN-1 trial data/config only after hash/version check; do not touch production).

PRE read-only:
- production containers/health;
- Docker networks/volumes/images;
- RAM/swap/load/disk/inode;
- listeners;
- current trial files/data/backup hashes;
- Qdrant collection point count/read-only snapshot;
- production PostgreSQL status **read-only only**; do not enable extension/create schema/db there.

Hard resource gates:
- RAM available >= **5.5 GB** before starting 3 trial services;
- disk free >= **25 GB**;
- floor disk >= **20 GB**;
- trial footprint <= **10 GB**;
- during run RAM available < **2 GB** ⇒ stop only trial services;
- do not change swap; record PRE/POST swap because RUN-1 left swap nearly full.

Production health regression ⇒ stop trial + rollback.

Before first runtime mutation: DROOT30 freshness gate.

## 3. CURRENT EMBEDDING MODEL — MUST MATCH AGENT DATA

Do not assume from memory.

Read current Agent Data runtime **without exposing secrets**:
- inspect `QDRANT_EMBED_MODEL` effective env/config in the running Agent Data service;
- if unset, verify current main source `Huyen1974/agent-data-test/agent_data/vector_store.py` default.

Known source evidence at prompt time:
`self.embedding_model = os.getenv("QDRANT_EMBED_MODEL", "text-embedding-3-small")`.

Effective model rule:
- if runtime `QDRANT_EMBED_MODEL` is set ⇒ use exactly that model;
- if unset ⇒ use `text-embedding-3-small`.

Record exact model + vector dimension in KQ.
For Cognee configure the equivalent explicit OpenAI model, e.g. `openai/text-embedding-3-small` when effective model is `text-embedding-3-small`.
No silent fallback/local HuggingFace model.

Embedding API key: reuse existing OpenAI secret path already used by Incomex; never print/store secret in repo/evidence.

## 4. VECTOR STORAGE — DEDICATED DISPOSABLE PGVECTOR

Qdrant is OUT OF SCOPE for Graph writes.

Cognee 1.6.1 pinned source has official `PGVectorAdapter` and `VECTOR_DB_PROVIDER=pgvector`.

Create a **dedicated trial PostgreSQL+pgvector container**, NOT production PG.

Logical container:
`graph-pgvector-trial`

Rules:
- prefer official `pgvector/pgvector` image compatible with PostgreSQL 18;
- resolve an exact immutable image digest before create; no `latest`;
- if suitable official pg18 artifact cannot be pinned, DỪNG rather than touch production PG;
- no host port publish;
- internal trial network only;
- memory limit **768 MB**;
- persistent trial volume under graph trial scope;
- unique random trial DB password, secret file mode 600.

Cognee config:
- `VECTOR_DB_PROVIDER=pgvector`
- `VECTOR_DATASET_DATABASE_HANDLER=pgvector` if required by pinned code;
- point vector connection only to `graph-pgvector-trial`;
- verify `CREATE EXTENSION vector` succeeded and vector tables are in trial PG.

Qdrant proof:
- PRE and POST point counts/config unchanged;
- no Qdrant env/key/URL supplied to Cognee trial.

Production PG proof:
- no CREATE EXTENSION/db/schema/table;
- no config mutation;
- no restart.

## 5. REBUILD TRIAL SERVICES WITH T19 FIX-B

Keep:
- Neo4j Community 5.26.31 + APOC 5.26.31
- Cognee 1.6.1 exact pinned image/source
- `HASH_API_KEY=true`
- resource limits from prior RUN, plus pgvector 768 MB.

Cognee:
- `BIND_ADDRESS=127.0.0.1`
- **NO `ports:` publish**
- API listens only `127.0.0.1:8000` in its own network namespace
- harness executes inside Cognee container/namespace.
- no Cognee MCP/UI.

T19 closeout:
1. host `127.0.0.1:18080` = no listener;
2. host → Cognee container IP:8000 = fail;
3. unrelated container same trial network → Cognee:8000 = fail;
4. unrelated container other network → fail;
5. inside Cognee namespace listener only `127.0.0.1:8000`.
Root/docker-admin is privileged boundary outside T19.

Smoke only:
- K1 provider still Neo4j;
- retained synthetic fixture readable;
- persistence hash unchanged;
- resource footprint.

Do not repeat full K4/dump-restore unless version/core volume changed.

## 6. CODE-FIRST DATASET — SMALL / NO KB BULK

Source only:
`/opt/incomex/dot/`

PRE inventory read-only; choose the **smallest coherent code subset** satisfying:
- prefer Python package/module supported by Cognee code graph;
- 10–30 source files;
- <= **250 KB** total source text;
- at least 3 modules/files with deterministic import/call/declaration relations;
- include 1–3 relevant tests if available;
- exclude `.env`, credential/config secret files, logs, data dumps, vendor, build, generated, node_modules, caches.

Before external call:
- secret scan;
- 0 credential/API key/private key/password/token;
- create manifest path + sha256 + byte count;
- if scan fails, reduce sample; do not redact a secret and keep surrounding sensitive config—exclude file.

No Lark, no customer data, no broad KB ingestion in this RUN.

## 7. BUILD CODE GRAPH — PRODUCT FIRST

Use **Cognee 1.6.1 built-in code graph path first** (Enola/integrated code pipeline from pinned release).
Do not build an Incomex parser/framework if built-in path is available.

Ground truth / oracle is deterministic:
- for Python use AST/import graph and direct symbol definitions/calls;
- for another supported language use existing parser/tool already present;
- AI/JEV never determines whether an import/call literally exists.

Graph targets:
- Neo4j stores code nodes/edges;
- exact deterministic relations where supported: DECLARES / IMPORTS / CALLS / DEPENDS_ON (or Cognee's equivalent canonical labels);
- provenance includes source file + revision/hash.

Minimum useful graph:
- >= 15 deterministic edges total;
- >= 5 source files represented;
- no secret/config files.

Accuracy acceptance:
- sample >= 15 oracle facts;
- **sampled precision = 100%** for edges Cognee claims as exact deterministic relations;
- **sampled recall >= 80%** on the chosen oracle facts;
- every miss/unsupported construct listed; do not hide dynamic-language limitations.

If Cognee built-in code graph cannot ingest the selected supported subset without custom framework changes:
- DỪNG with exact blocker;
- do not replace it by a new custom graph engine in this RUN.

## 8. EMBEDDING + PGVECTOR SMOKE

Use the exact effective Agent Data embedding model from §3.

Embed only the selected code micro-dataset.
Store embeddings in trial PGVector.

Verify:
- embedding vector dimension matches model;
- vector row/table count > 0;
- simple semantic query over code returns a relevant symbol/file in top results;
- record query and expected rationale, not secret/source dump;
- Qdrant point count unchanged.

Do not mix vectors made by another model into the same trial collection/schema.
If effective embedding model cannot be called through existing OpenAI account, DỪNG; do not silently use another model.

## 9. OPTIONAL SMALL MODEL/JEV SEMANTIC SMOKE

Owner allows trying model, but deterministic code graph remains primary.

LLM baseline if needed:
- `gpt-5.6-luna`
- only secret-scanned code subset;
- no fallback model without recording.

Use LLM only for a **small semantic layer**, e.g. classify 5–10 modules/symbol groups into bounded roles such as:
`gateway | persistence | guard | workflow | ui | other`.
Do not use LLM to invent literal imports/calls.

If JEV Reference/gateway is already bound to Claude Code:
- run 3–10 bounded SHADOW judgments on already selected candidate roles/impacts;
- record model/result id/confidence;
- JEV does not authorize writes or create exact code edges.
If JEV tool is not bound, record `JEV_SMOKE=CHUA_KIEM`; do not add a new connector in this RUN.

External-call cost cap for this RUN: **<= 1 USD**.
If no reliable provider cost ledger is available, bound by dataset size/call count and report cost UNKNOWN; never exceed the existing overall trial cap 5 USD.

## 10. TRIAL DATA IS DISPOSABLE

Mark all graph/vector/code dataset state:
`TRIAL_ONLY · GS-R4-CODE-FIRST-20261006-02`

Do not mix trial data with production sources.

At KQ:
- stop trial containers unless evidence requires them running;
- keep trial volumes only for Host/Claude review;
- document one-command/one-scope wipe of Neo4j trial data + PGVector trial DB/volume + Cognee trial metadata.

**Do not wipe before review.**
Roadmap requires mandatory wipe/reset before production build.

## 11. ROADMAP / KB RULE

This RUN must not ingest the existing KB broadly.

Record in KQ that production cannot begin before:
1. KB inventory;
2. classify each candidate source: CURRENT/KEEP · ARCHIVE · DELETE-CANDIDATE · RECHECK;
3. deduplicate/retire stale material with Owner approval for destructive deletion;
4. freeze the official source scope;
5. wipe all trial graph/vector state;
6. rebuild production graph/vector clean from approved sources.

No destructive KB deletion in this RUN.

## 12. KQ / PASS

Repo: only update `work/graph-server/COLLAB.md` + BẢNG/KQ; do not create progress files in Git.
Evidence stays VPS runtime path.

KQ commit:
`[Claude Code] GS-R4-CODE-FIRST-20261006-02 · graph-server · <XONG|DỪNG>`

XONG requires:
- T19 FIX-B PASS;
- Neo4j/Cognee still correct versions;
- dedicated PGVector trial works;
- effective embedding model confirmed and reused;
- Qdrant unchanged;
- production PG untouched;
- code graph minimum + accuracy criteria pass;
- secret scan pass;
- resource gates pass;
- production health unchanged;
- trial wipe path proven/documented.

T18 business-identity is **not a blocker in this code-only RUN**; it returns as a gate before business-person data.

If security/vector/code graph core passes but optional JEV semantic smoke is unavailable, KQ may be XONG with `JEV_SMOKE=CHUA_KIEM`; Goal #2/#3 remains open for later.

No business RUN and no production install in this RUN.

## 13. AUTONOMY

Owner asked to continue.
Within scope, Claude Code should self-resolve technical details, inspect pinned source, retry boundedly, and choose the smallest valid configuration.
Do not ask Owner about Docker commands, exact pgvector digest, test fixture mechanics, or minor config.
Out-of-scope/production mutation/secret exposure/need to change stack ⇒ KQ DỪNG cleanly.

Final line:
`XONG · GS-R4-CODE-FIRST-20261006-02 · <commit>`
or
`DỪNG · GS-R4-CODE-FIRST-20261006-02 · <blocker> · <commit>`
