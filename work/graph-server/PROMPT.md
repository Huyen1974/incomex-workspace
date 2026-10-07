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

Download đúng version; verify SHA trước install.
Install local venv; không package global.
neo4j-mcp -v phải = 1.6.0.
Không dùng neo4j-contrib/mcp-neo4j hay canary.

## 4. E2 · STDIO-ONLY WRAPPER / SECRET BOUNDARY
Không service thường trực, không HTTP, không nginx, không host port mới.

graph-v1 có đúng:
- graph-v1 --help
- graph-v1 mcp
- graph-v1 doctor

graph-v1 mcp:
- lấy secret graph-server-neo4j-password từ GSM vào bộ nhớ;
- không file secret, không argv secret, không stdout/stderr/log secret;
- export nội bộ:
  NEO4J_URI=bolt://127.0.0.1:17687
  NEO4J_USERNAME=neo4j
  NEO4J_DATABASE=neo4j
  NEO4J_READ_ONLY=true
  NEO4J_TELEMETRY=false
- exec official neo4j-mcp 1.6.0.

Tool catalogue production phải có:
- get-schema
- read-cypher
và KHÔNG có write-cypher.
Nếu list-gds-procedures xuất hiện dù production không có GDS => ghi PARTIAL cho Reviewer, không tự allow.

Wrapper root-owned, non-writable by agent users.
Không in secret ở --help/doctor.

## 5. E3 · PROVE READ-ONLY ON TEMP COPY FIRST
Trước khi MCP chạm production:
- dùng dump R7 restore một Neo4j TEMP riêng trong build network;
- 0 host port;
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

Tất cả phải bị từ chối.
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
- README khuyên query có LIMIT và tránh Cartesian/unbounded traversal.

E5 UNKNOWN không chặn R8 nếu E3/E4 PASS; phải ghi residual.

## 8. E6 · AGENT SIGNPOST / TRUST CONTRACT
Nếu work/graph-server/README.md chưa có, tạo đúng file này.

graph-v1 --help và README phải nói:
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

Nếu Hermes current version không hỗ trợ stdio MCP theo schema thật => E7 PARTIAL, không invent config; ghi exact blocker cho HJW. Claude/Codex PASS vẫn giữ.

## 10. E8 · POST-PROTECT / ROLLBACK
Trước KQ XONG/PARTIAL:

Footprint:
- mcp-readonly-v1 install tree;
- graph-v1 wrapper;
- work/graph-server/README.md;
- Claude MCP entry graph-v1;
- Codex MCP entry graph-v1;
- Hermes graph-v1 entry nếu active;
- exact narrow privilege entry nếu cần.

AUTO-PROTECT:
- Config Guard/hash cho wrapper + MANIFEST + README + config snippets;
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
S0 shared-VPS gate
-> E1 pin/install
-> E2 wrapper
-> E3 temp-copy negative-write suite
-> E4 production 13/13 reads
-> E5 limit capability record
-> E6 help/README
-> E7 client integration Claude/Codex/Hermes
-> E8 POST-PROTECT
-> KQ.

No polling/waiting. Gate đỏ => DỪNG sạch.

## 12. ACCEPTANCE
R8 XONG chỉ khi:
- E1-E4 PASS;
- E6 PASS;
- Claude Code + Codex PASS;
- Hermes PASS để E7 full;
- E8 PASS;
- production graph unchanged.

Nếu Hermes capability thật block => KQ PARTIAL; không nói R8 hoàn tất.
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
- README được tạo/sửa theo E6;
- không sửa PROMPT/view khi RUN active.

Final:
KQ@GS-R8-AGENT-READONLY-MCP-20261007-11 XONG|PARTIAL|DỪNG
