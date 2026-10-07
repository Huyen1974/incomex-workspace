# PROMPT — GS-R8-AGENT-READONLY-MCP-20261007-11

## 0. STATUS / AUTHORITY
RUN_ID: GS-R8-AGENT-READONLY-MCP-20261007-11
Executor_Surface: Claude Code CLI
Repo_Write_Path: Incomex workspace gateway workspace_* · root workspace
Runtime surfaces: Owner Mac + VPS1 production
Status: DRAFT · NO READY · NO RUN

Owner D14 + D16/DROOT49:
- R8 là trial nhỏ/additive sau production R7; Host + Reviewer tự quyết, không hỏi Owner kỹ thuật.
- Không đổi mục tiêu, không gửi field mới, không ghi graph.
- Trước RUN vẫn cần Reviewer ACCEPT đúng SHA + Host READY theo A9.
- Nếu shared-VPS worker khác đang STARTED thì DỪNG sạch, không poll/chờ.

## 1. MỤC TIÊU DUY NHẤT
Làm cho agent thật sự ĐỌC được Graph v1 qua Neo4j MCP chính hãng, read-only, không mở HTTP/port mới và không trao secret cho agent.

XONG khi:
- official Neo4j MCP được pin + hash;
- write path bị chặn thật trên bản sao tạm;
- 13/13 câu B8 đọc đúng qua MCP trên production;
- Claude Code + Codex + Hermes có entry path read-only đã thử;
- có help/README trust rules;
- POST-PROTECT + Telegram PASS.

Không thuộc R8:
- refresh dữ liệu;
- thêm agent-data/Nuxt;
- JEV runtime;
- KB/care-chat;
- broad trial cleanup;
- sửa Neo4j data/config để cứu test.

## 2. S0 · SHARED-VPS EXECUTION GATE
Trước mutation:
- fresh-read root COLLAB + work/hermes-joint-workspace/COLLAB.md + task Graph.
- Graph R7 phải KQ XONG/P63 accepted.
- HJW/VPSC/shared-VPS task khác phải không có STARTED mutation hiện hành.

Hiện tại lúc Host soạn PROMPT: HJW N3-2a đang STARTED.
=> Reviewer được review PROMPT bình thường; executor chỉ RUN khi Host fresh-check gate xanh và đặt READY.
=> Không giữ terminal chờ; gate đỏ thì KQ DỪNG/HOLD trước mutation.

## 3. E1 · OFFICIAL SERVER PIN
Dùng đúng:
- package: neo4j-mcp-server
- version: 1.6.0
- artifact Linux x86_64:
  neo4j_mcp_server-1.6.0-py3-none-manylinux_2_17_x86_64.whl
- SHA256:
  f6aeac50e04ed93b7e22c634426aca27f5e91f371ea67caad028afe424704cb0

Nguồn: official project neo4j-mcp-server, release 2026-09-10.

Preflight:
- uname -m phải x86_64/amd64;
- python >= 3.10;
- nếu lệch => DỪNG, không tự chọn artifact khác/latest.

Install root:
- /opt/incomex/graph-server/mcp-readonly-v1/
- wheel cache: /opt/incomex/graph-server/mcp-readonly-v1/dist/
- venv: /opt/incomex/graph-server/mcp-readonly-v1/venv/
- wrapper: /opt/incomex/graph-server/mcp-readonly-v1/bin/graph-v1
- manifest: /opt/incomex/graph-server/mcp-readonly-v1/MANIFEST.json

Download đúng version; verify SHA wheel trước install.
Install local venv; không package global.
Lệnh thật phải là `<venv>/bin/neo4j-mcp-server` (fallback identity check: `python -m neo4j_mcp_server`), không dùng tên đời cũ `neo4j-mcp`.
Trước wrapper, chạy exact binary với cờ help/version mà chính binary hỗ trợ; ghi nguyên văn output và output phải chứa `1.6.0`. Danh tính package quyết định bởi BOTH: wheel SHA256 `f6aeac50e04ed93b7e22c634426aca27f5e91f371ea67caad028afe424704cb0` + installed binary SHA256 `00d4882f412427db064df39492b882781ba1040db82f94ea8cdeedd16db0`.
Không dùng neo4j-contrib/mcp-neo4j, canary hay `latest`.
Ghi provenance đúng mức: PyPI không có build attestation; “official” ở đây dựa trên package/docs Neo4j + release date + source path `github.com/neo4j/mcp`, không nói quá thành supply-chain attested.

## 4. E2 · STDIO-ONLY WRAPPER / SECRET BOUNDARY
Không service thường trực, không HTTP, không nginx, không host port mới.

graph-v1 có đúng:
- graph-v1 --help
- graph-v1 mcp
- graph-v1 doctor

graph-v1 mcp:
- lấy secret graph-server-neo4j-password từ GSM vào bộ nhớ; mỗi phiên agent có thể fetch GSM một lần, ghi residual/cost không đáng kể;
- không file secret, không argv secret, không stdout/stderr/log secret;
- TRƯỚC khi viết wrapper: chạy `<venv>/bin/neo4j-mcp-server --help`/config help và đối chiếu đúng tên biến của 1.6.0; lệch bất kỳ tên dưới đây => DỪNG, không dùng alias deprecated;
- export nội bộ chỉ cho child process:
  NEO4J_MCP_URI=bolt://127.0.0.1:17687
  NEO4J_MCP_USERNAME=neo4j
  NEO4J_MCP_PASSWORD=<GSM value in process memory>
  NEO4J_MCP_DATABASE=neo4j
  NEO4J_MCP_READ_ONLY=true
  NEO4J_MCP_TELEMETRY=false
  NEO4J_MCP_TRANSPORT_MODE=stdio
- exec `<venv>/bin/neo4j-mcp-server`.

“Read-only” ở R8 là rào chống ghi nhầm qua MCP tool, KHÔNG phải security boundary chống lại Claude Code/Codex vốn đã có SSH vào VPS.

Tool catalogue production phải có:
- get-schema
- read-cypher
và KHÔNG có write-cypher.
Nếu list-gds-procedures xuất hiện dù production không có GDS => ghi PARTIAL cho Reviewer, không tự allow.

Wrapper root-owned, non-writable by agent users.
Không in secret ở --help/doctor.

## 5. E3 · PROVE READ-ONLY ON TEMP COPY FIRST
Trước khi MCP chạm production:
- dùng dump R7 restore một Neo4j TEMP riêng trong build network bằng **compose file riêng của R8**; tuyệt đối không sửa `/opt/incomex/graph-server/prod-v1/compose.yaml` đang được Guard băm;
- dùng local Neo4j image đã có, **không pull image mới**;
- 0 host port;
- temp Neo4j mem_limit <= 1 GiB và memswap_limit = mem_limit;
- temp password riêng, không production secret;
- temporary MCP process/harness cùng isolated build network;
- remove toàn bộ temp containers/network/volume sau test.

Qua MCP tool catalogue:
- write-cypher phải absent.
Qua read-cypher, thử tối thiểu:
1. CREATE node
2. SET property
3. DELETE node
4. MERGE
5. CREATE INDEX/CONSTRAINT
6. LOAD CSV kèm mutation
7. admin/password-changing query
8. APOC write procedure có sẵn
9. APOC chạy Cypher gián tiếp có ghi: `apoc.cypher.doIt` hoặc `apoc.periodic.iterate` — dùng cái thực sự có trong APOC production
10. `apoc.load.*` gọi mạng và `apoc.export.*` ghi file — phải bị từ chối hoặc bị cấu hình hiện hữu chặn
11. Sau password-change attempt: đăng nhập lại bằng **mật khẩu temp cũ** phải vẫn PASS; kiểm trạng thái thật, không chỉ dựa message lỗi

Tất cả phải bị từ chối/chặn đúng nghĩa và temp DB state không đổi.
Trước/sau: node count, edge count, schema fingerprint, sample invariant = exact same.
Một mutation lọt => E3 FAIL; không trỏ production.

Không đổi APOC/Neo4j để làm test PASS.

## 6. E4 · PRODUCTION READ ACCEPTANCE
Chỉ sau E3 PASS.

- freeze production counts + INV22 + source hashes trước MCP query.
- chạy 13 câu B8 đã đóng băng của R7 qua MCP path mới.
- 13/13 phải đúng.
- mỗi câu UNKNOWN vẫn phải UNKNOWN.
- production counts/hash/invariants trước=sau.
- INV22 xanh trước/sau.
- packet capture quanh query phase: 0 outbound ngoài local Neo4j; GSM secret fetch đo tách trước query và ghi expected secret-control traffic.

Không dùng direct cypher-shell để chấm thay MCP; direct query chỉ independent before/after invariant.

## 7. E5 · QUERY COST BOUNDARY
Pinned official 1.6.0:
- chỉ dùng timeout/row/token controls nếu exact runtime --help/config/docs xác nhận.
- Host precheck chưa thấy timeout/token-limit native trong official 1.6.0 => nếu runtime cũng không thấy, ghi NATIVE_QUERY_LIMIT=UNKNOWN/NOT_EXPOSED.
- không sửa Neo4j server config trong R8.
- không tự dựng Cypher parser/filter.
- `graph-v1 --help` + mục `## Cổng đọc Graph cho agent` trong COLLAB khuyên query có LIMIT và tránh Cartesian/unbounded traversal.

E5 UNKNOWN không chặn R8 nếu E3/E4 PASS; phải ghi residual.

## 8. E6 · AGENT SIGNPOST / TRUST CONTRACT
KHÔNG tạo README/file repo mới.

graph-v1 --help và một mục ngắn `## Cổng đọc Graph cho agent` trong `work/graph-server/COLLAB.md` (đặt trước `## Con trỏ`) phải nói:
- cách gọi;
- tools get-schema + read-cypher only;
- ví dụ Cypher có LIMIT;
- trust Python v0.3 / TS-Vue v0.4 / PG-DOT v0.5 / production v0.6;
- vắng quan hệ nói UNKNOWN trừ exact-at-snapshot scope;
- file test_*.py, tests/**, conftest.py bị Enola bỏ => OUTSIDE_EXTRACTION_SCOPE/UNKNOWN;
- production code graph hiện 3 Python trees / 51 extracted files; agent-data + Nuxt OUT;
- Base88 person chỉ record_id, không dùng để suy/tra danh tính;
- KB/care-chat OUT;
- JEV không active runtime.

Không ghi secret/private fields.

## 9. E7 · INSTALL FOR 3 AGENT SURFACES
Một server wrapper dùng chung; không gateway riêng từng agent.

### Claude Code trên Mac
Dùng current claude mcp CLI syntax từ --help, không đoán.
Cấu hình ở **user scope**; KHÔNG tạo `.mcp.json` hay file MCP mới trong repo.
Server name: graph-v1.
Stdio command tương đương:
ssh contabo /opt/incomex/graph-server/mcp-readonly-v1/bin/graph-v1 mcp

Backup/diff current MCP config.
Không đụng connector khác.
Fresh Claude Code process:
- tools list đúng read-only;
- schema call PASS;
- một read query PASS;
- một natural question dùng non-PII graph result PASS.

### Codex trên Mac
Dùng current Codex MCP config/CLI đã cài, không đoán syntax.
Desired stdio identity:
command = ssh
args = [contabo, /opt/incomex/graph-server/mcp-readonly-v1/bin/graph-v1, mcp]
server id = graph-v1
enabled tools nếu config native hỗ trợ: get-schema, read-cypher only.

Backup/diff ~/.codex/config.toml.
Fresh Codex process:
- server connected;
- tool catalogue read-only;
- schema/read smoke PASS.
Không đổi plugin/JEV config khác.

### Hermes trên VPS
Chỉ thực hiện khi HJW không còn STARTED và config hiện hành xác nhận hỗ trợ mcp_servers stdio.
Đọc local Hermes version/help/config schema trước edit.
Server id graph-v1, command local:
  /opt/incomex/graph-server/mcp-readonly-v1/bin/graph-v1 mcp

Secret không đưa vào Hermes config/env; wrapper tự fetch GSM.
Nếu cần privilege để chạy root-owned wrapper:
- chỉ đúng exact wrapper command bằng least-privilege hiện hữu;
- wrapper/root config immutable với hermes;
- không sudo/shell rộng;
- chứng minh hermes không đọc secret value.

Fresh Hermes invocation:
- list tools;
- get-schema;
- một read query không PII.

Nếu Hermes current version không hỗ trợ stdio MCP theo schema thật => ghi `HERMES_ENTRY=NOT_INSTALLED` + exact blocker và chuyển residual sang HJW; không invent config. **Hermes không chặn R8 XONG** nếu Claude Code + Codex + E1–E6/E8 PASS và production graph không đổi.

## 10. E8 · POST-PROTECT / ROLLBACK
Trước KQ XONG/PARTIAL:

Footprint:
- mcp-readonly-v1 install tree;
- graph-v1 wrapper;
- mục `## Cổng đọc Graph cho agent` trong COLLAB.md;
- Claude MCP user-scope entry graph-v1;
- Codex MCP entry graph-v1;
- Hermes graph-v1 entry nếu active;
- exact narrow privilege entry nếu cần.

AUTO-PROTECT:
- Config Guard/hash cho wrapper + MANIFEST + COLLAB signpost + config snippets;
- production INV22 vẫn xanh;
- graph counts unchanged;
- no public listener;
- rollback proof.

Rollback:
- remove MCP client entries graph-v1 only;
- remove narrow Hermes privilege/config entry only;
- remove /opt/incomex/graph-server/mcp-readonly-v1 only if RUN marker matches;
- production Neo4j untouched.

Telegram receipt <=3 dòng + delivery proof.
Không broad-clean trial data.

## 11. STEP_WALK
PRE resource gate trước mutation: MemAvailable >= 3 GiB; disk free >= 20 GiB. Không đạt => DỪNG sạch. Temp Neo4j E3 <=1 GiB, memswap=mem; không pull image mới.

| Bước | Ai | Trigger | Bằng chứng | Hỏng thì ai biết | Kế |
|---|---|---|---|---|---|
| S0 shared-VPS + resource gate | Agent | STARTED/read-gate | HJW/VPSC terminal + RAM/disk | Host qua KQ DỪNG | E1 |
| E1 pin/install | Agent | S0 PASS | wheel/binary hash + version output | Host | E2 |
| E2 wrapper | Agent | E1 PASS | help/env/tool catalogue + secret scan | Host | E3 |
| E3 temp write-negative | Agent | E2 PASS | 11-case matrix + state PRE=POST | Host | E4 |
| E4 production reads | Agent | E3 PASS | 13/13 + INV22/count/hash PRE=POST | Host | E5 |
| E5 cost boundary | Agent | E4 PASS | native capability status | Host | E6 |
| E6 signpost | Agent | E5 | graph-v1 --help + COLLAB section | Host | E7 |
| E7 clients | Agent | E6 | Claude/Codex/Hermes receipts | Host/HJW | E8 |
| E8 POST-PROTECT | Agent | E7 | Guard/rollback/Telegram | Owner+Host | KQ |

No polling/waiting. Gate đỏ => DỪNG sạch.

## 12. ACCEPTANCE
R8 XONG chỉ khi:
- E1-E4 PASS;
- E6 PASS;
- Claude Code + Codex PASS;
- E8 PASS;
- production graph unchanged.

Hermes PASS là mục tiêu phụ của E7. Nếu capability/version thật của Hermes block, ghi `HERMES_ENTRY=NOT_INSTALLED` + residual sang HJW; R8 vẫn XONG nếu các gate bắt buộc trên PASS.
E5 UNKNOWN/NOT_EXPOSED được phép là residual.

KQ ghi:
- official version/artifact/SHA;
- tools list;
- write-negative matrix;
- 13/13 answers;
- before/after invariants;
- client config hashes/diffs;
- secret non-disclosure scan;
- POST-PROTECT + Telegram;
- NATIVE_QUERY_LIMIT status;
- remaining limitations.

## 13. KQ
Evidence:
/opt/incomex/work/graph-server/evidence/GS-R8-AGENT-READONLY-MCP-20261007-11/

Repo:
- Agent cập nhật Bảng/KQ/COLLAB theo A4;
- E6 chỉ thêm/cập nhật mục `## Cổng đọc Graph cho agent` trong COLLAB.md; không tạo file mới;
- không sửa PROMPT/view khi RUN active.

Final chỉ dùng trạng thái A9:
KQ@GS-R8-AGENT-READONLY-MCP-20261007-11 XONG|DỪNG
