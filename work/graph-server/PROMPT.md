# PROMPT — GS-R8R-AGENT-READONLY-MCP-20261008-12

## 0. STATUS / AUTHORITY
RUN_ID: GS-R8R-AGENT-READONLY-MCP-20261008-12
Task: work/graph-server · recovery của R8, KHÔNG mở roadmap/task mới
Executor_Surface: Claude Code CLI · Owner dán thủ công vào terminal MỚI
Repo_Write_Path: Incomex MCP full all 2 workspace_* root workspace
Runtime: Owner Mac + VPS1 production
Status: DRAFT · CHƯA CÓ REVIEWER ACCEPT SHA MỚI · NO READY · NO RUN

Căn cứ: Owner D10/D14/D16/DROOT49; A0/A4/A6/A9; Graph P72 (R8 DỪNG ở E3 vì APOC URL), GPT P73, Claude Reviewer P74 đồng thuận Δ1–Δ7. P74 là ACCEPT HƯỚNG, chưa phải ACCEPT PROMPT hiện tại. Phải có REVIEWER ACCEPT full last-touch commit SHA PROMPT mới rồi Host READY same SHA trước khi Owner dán RUN. PROMPT cũ `GS-R8-AGENT-READONLY-MCP-20261007-11` đã KQ DỪNG, không hồi tố đổi thành PASS.
Bốn mục tiêu Owner giữ nguyên: Business Graph; Graph×JEV; official JEV skills; Code Graph. R7 production v1 = 3.596 node/6.823 edge, R8 agent read path chưa đạt; sau R8 mới R9 business refresh → R10 JEV SHADOW → R11 code. Không sửa nhiệm vụ HJW/VPSC, không Hermes ASSIGN/schedule.

## 1. MỤC TIÊU / THAY ĐỔI ĐƯỢC PHÉP — Δ1
Khắc phục APOC/Cypher gọi URL và write-bypass, sau đó kết nối official Neo4j MCP 1.6.0 cho Claude Code/Codex ĐỌC Graph v1 thật. Vẫn chỉ dùng stdio, không mở HTTP/port mới, không phát secret.

**Một thay đổi cấu hình Neo4j production duy nhất sau khi test TEMP PASS:** Thêm tại environment của đúng service Neo4j trong `/opt/incomex/graph-server/prod-v1/compose.yaml` đúng một dòng:
`NEO4J_internal_dbms_cypher__ip__blocklist: "0.0.0.0/0,::/0"`
(tương ứng `internal.dbms.cypher_ip_blocklist=0.0.0.0/0,::/0`), cộng TỐI ĐA một comment “R8R block Cypher/APOC URL; Neo4j upgrade phải kiểm lại URL”. Recreate chỉ service Neo4j một lần có rollback, không đổi image/digest, graph data/schema/roles, network, ports, volume, các service khác. Config Guard cập nhật baseline đúng mục tiêu `graph-v1-compose` theo E8. Không apply allowlist lên production.

Không thuộc R8R: JEV runtime, R9 data refresh, agent-data/Nuxt, KB/care-chat, broad cleanup, nâng version Neo4j/APOC, đổi quyền database, tự viết Cypher parser/bridge/extra gateway, thay hạ tầng/việc HJW-VPSC. Nếu E3 không chứng minh an toàn thì DỪNG trước production.

## 2. S0 · READ-GATE / SHARED-VPS / CONFIG BASELINE — Δ2
1. Đọc AGENTS.md → root COLLAB.md → Graph COLLAB (Bảng, P72–P76) → PROMPT hiện hành; đối chiếu Reviewer ACCEPT + Host READY cùng commit last-touch PROMPT và đúng RUN_ID. Ghi STARTED theo A6 trước PRE nếu read-gate PASS, không giả READY, không chờ permission kỹ thuật tự động.
2. Kiểm tra *tươi* các task HJW/VPSC/Graph + root busy, CLI, lệnh SSH/compose/Guard: **không chạy song song hai mutation shared-VPS**. Nếu phiên HJW P230 chỉ đọc log, không đụng Neo4j/Guard và VPS còn đủ tài nguyên thì có thể làm song song theo phép đo; nếu không chứng minh được hoặc xuất hiện mutation/đèn đỏ liên quan ⇒ DỪNG, không poll/chờ. Cờ P230 là snapshot, không phải giấy miễn kiểm. RAM MemAvailable >=3GiB, disk free >=20GiB, Guard PRE PASS, đo bảng đèn thực tế.
3. S0(a): đọc đúng Neo4j prod 5.26.31 `neo4j.conf`, `apoc.conf`, compose và effective config; baseline: `unrestricted=apoc.*`, allowlist chưa bị thu hẹp, blocklist chưa có/rỗng. Không khớp ⇒ DỪNG, không tự merge.
4. S0(b): bounded grep `LOAD CSV|apoc\.load|apoc\.import` trên code chạy của Graph `graph-v1`, INV22, 13 câu B8 và script ingest R7/Cognee; nếu thành phần hiện hành cần URL ⇒ DỪNG trước production (ghi exact file/line). Không tự giả định từ repo không cùng runtime.
5. S0(c): xác minh dump R7 SHA so manifest, khả năng restore và prod counts/hash/schema/INV22. Giữ nguyên R7 dump (không tạo dump mới nếu đúng), snapshot compose production nguyên byte/SHA và đường rollback.
6. Đối chiếu cấu hình chính xác Neo4j 5.26.31 trên bản TEMP: setting internal + Docker env mapping đôi underscore, strict validation, không dùng docs/current-image thay bằng chứng runtime. Trước first production mutation re-read A6/READY/STOP/root busy/resource/Guard/config SHA. Bất kỳ chênh lệch hard gate ⇒ KQ DỪNG/đóng CLI, 0 WAIT/HOLD.

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

P72 đã verify wheel/binary SHA, được reuse evidence, nhưng phải verify lại artifact/install thực tế vì P72 đã dọn footprint.
Download đúng version; verify SHA wheel trước install.
Install local venv; không package global.
Lệnh thật phải là `<venv>/bin/neo4j-mcp-server` (fallback identity check: `python -m neo4j_mcp_server`), không dùng tên đời cũ `neo4j-mcp`.
Trước wrapper, chạy exact binary với cờ help/version mà chính binary hỗ trợ; ghi nguyên văn output và output phải chứa `1.6.0`. Danh tính package quyết định bởi BOTH: wheel SHA256 `f6aeac50e04ed93b7e22c634426aca27f5e91f371ea67caad028afe424704cb0` + installed binary SHA256 `00d4882f412427db064df39492b882781ba1040db82f94ea8cdeedd16db0dfff`.
Không dùng neo4j-contrib/mcp-neo4j, canary hay `latest`.
Ghi provenance đúng mức: PyPI không có build attestation; “official” ở đây dựa trên package/docs Neo4j + release date + source path `github.com/neo4j/mcp`, không nói quá thành supply-chain attested.

## 4. E2 · STDIO-ONLY WRAPPER / SECRET BOUNDARY
Không service thường trực, không HTTP, không nginx, không host port mới.

E3 dùng MCP stdio process/harness TEMP trước; không tạo wrapper production cho tới khi E3 PASS.

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

## 5. E3 · TEMP WRITE/SSRF BLOCKLIST — N1–N4+P, Y TEMP-ONLY (Δ3/Δ4)
Dùng dump R7 đã verify khôi phục Neo4j TEMP local image/digest/APOC đúng production. Compose TEMP riêng trong build network `internal:true`, DNS/plugin/env tương đương, 0 host port, password TEMP riêng không dùng production, mem_limit <=1GiB, memswap_limit=mem_limit, không pull mới. TEMP compose có chính dòng `NEO4J_internal_dbms_cypher__ip__blocklist: "0.0.0.0/0,::/0"`; effective neo4j.conf đúng `internal.dbms.cypher_ip_blocklist`. Sai setting/server không start ⇒ DỪNG; không dùng allowlist ở nhánh chính.

Test **qua official Neo4j MCP read-cypher** đúng pin; write-cypher phải vắng. Independent state oracle dùng Cypher-shell chỉ PRE/POST. Đối với T10a/T10c/T10f và toàn bộ N2, chỉ PASS khi lỗi nêu đúng `internal.dbms.cypher_ip_blocklist` và không phát GET/POST/egress; lỗi “Network unreachable”, DNS, timeout, HTTP 401/404 **không tính PASS** cho các phép này. Riêng T10b lịch sử (hostname không phân giải do DNS chặn) được giữ BLOCKED_BY_DNS theo P74/N1; T7b = N/A, N3 file phải bị chặn đúng cơ chế file-import, không bắt error chứa IP blocklist. Fixture chỉ trong TEMP/local hoặc dải tài liệu, tuyệt đối không gọi IP Internet thật.

N1: chạy lại đúng **20 phép P72** (không đổi tiêu chí): 16 phép đã chặn theo cơ chế cũ giữ nguyên, T7b = N/A (Neo4j 5 không còn đổi password kiểu đó, T7a+T11 xác minh); ba phép **T10a GET loopback, T10c URL dạng IP, T10f POST loopback có mật khẩu TEMP** phải chuyển từ mở sang blocklist rejection; 19/19 applicable BLOCKED, 1 N/A, 0 node/user/schema mutation, T11 temp password cũ còn đăng nhập.

N2: Với từng loại URL, thử **cả ba đường** `apoc.load.json` GET, `apoc.load.jsonParams` POST, native `LOAD CSV FROM ... RETURN`:
- `http://127.0.0.1:7474/`, `http://localhost:7474/`, `http://[::1]:7474/`, `http://[::ffff:127.0.0.1]:7474/`, `http://2130706433:7474/`;
- `https://127.0.0.1:7473/`, IP riêng thật TEMP, `http://192.0.2.1/`, `http://[2001:db8::1]/`.
- Kiểm redirect/DNS-variation bằng fixture cô lập khi test được đúng mã hiện hành; route unknown ⇒ DỪNG thay vì bỏ lặng. Network TEMP internal nhưng không coi “unreachable” là bằng chứng blocklist.

N3: `apoc.load.json('file:///etc/passwd')` bị file-import guard từ chối; native `LOAD CSV` file traversal không trả nội dung ngoài import directory. Không bật apoc.import.file.enabled/apoc.export.file.enabled.

N4: Lấy danh mục thật `SHOW PROCEDURES YIELD name, mode WHERE name STARTS WITH 'apoc.'`; nhóm READ/DEFAULT có khả năng tạo giao dịch/tiến trình/url (`cypher.*`, `periodic.*`, `trigger.*`, `systemdb.*`, `bolt.*`, `load.*`, `import.*`, `log.*`) phải được thử bằng negative fixture một procedure một case trong TEMP (ít nhất `apoc.cypher.runTimeboxed` ghi R8Probe nếu hiện diện). Không cài: N/A có receipt; không thử an toàn được: UNKNOWN/DỪNG; không được suy cả nhóm an toàn từ một ca.

P — positive trên TEMP: `get-schema`, B8 13/13 qua **MCP**, 1 read query, HTTP 7474 inbound 200, Bolt login, APOC meta dùng cho schema. Counts/edge hash/gs_key/schema/user list trước=sau, R8Probe=0, egress 0. Lưu toàn bộ matrix N1–N4+P + lỗi đúng tên setting; không được ghi PASS từ docs/JEV.

**Nhánh Y chỉ trên TEMP:** nếu phát hiện đường ghi không qua URL sau N1–N4, được thử allowlist `dbms.security.procedures.allowlist` thu hẹp từ catalogue + APOC/Cognee actual usage, replay N/P; dù PASS vẫn **KQ DỪNG cùng exact Y** để Host/Claude duyệt prompt khác. Không bao giờ apply Y production trong RUN này. Nếu A còn URL mở, không dùng allowlist để che native LOAD CSV. Sau FAIL/UNKNOWN/Y: teardown TEMP, production không đổi.

## 6. E4 · NARROW PRODUCTION CONFIG / READ ACCEPTANCE — Δ5
Chỉ sau E3 A-only N1–N4+P PASS, fresh A6/no-concurrent/Guard/resources xanh.
1. Backup nguyên byte+SHA compose production vào evidence; diff thật **chỉ** một env line `NEO4J_internal_dbms_cypher__ip__blocklist: "0.0.0.0/0,::/0"` (+ tối đa một comment) dưới đúng Neo4j service. Một thay đổi bất ngờ về image/ports/volume/env khác/network ⇒ DỪNG trước mutation.
2. Recreate **riêng** Neo4j service đúng compose hiện hành, không down stack, không pull, đo outage và health timeout **180s**; vượt/failed ⇒ tự rollback.
3. Kiểm effective config đúng `internal.dbms.cypher_ip_blocklist=0.0.0.0/0,::/0`; HTTP 17474 inbound/Bolt/INV22/Guard/Graph 3.596/6.823, SHA/invariants/users/dump restore path giữ nguyên. Ba harmless probes production KHÔNG POST, KHÔNG gửi secret/traffic: `apoc.load.json` URL loopback, native LOAD CSV URL `192.0.2.1`, `apoc.load.json` URL private gateway thật; tất cả báo **tên blocklist** trước kết nối. Bất kỳ fail ⇒ rollback.
4. Sau probes mới materialize wrapper production §4; chạy B8 **13/13 qua MCP thật production**, UNKNOWN vẫn UNKNOWN. Không chấm bằng direct shell thay MCP. Packet capture quanh query phase 0 outbound ngoài Neo4j local; GSM fetch đo riêng trước phase, không log secret. Prod counts/edges/schema/user/source SHA/INV22 trước=sau.
5. Rollback nếu bất kỳ critical stage production fail: phục hồi **nguyên byte compose/SHA cũ**, recreate chỉ Neo4j, chứng minh effective config cũ+counts/hash/INV22/Guard/HTTP/Bolt, gỡ chính entries/client MCP run này tạo, KQ DỪNG. Không vá để “cứu”, không giữ Graph ở trạng thái nửa thay đổi. Rollback cũng fail ⇒ đèn đỏ/Telegram và KQ DỪNG, không nói XONG.

## 7. E5 · QUERY COST BOUNDARY
Pinned official 1.6.0:
- chỉ dùng timeout/row/token controls nếu exact runtime --help/config/docs xác nhận.
- Host precheck chưa thấy timeout/token-limit native trong official 1.6.0 => nếu runtime cũng không thấy, ghi NATIVE_QUERY_LIMIT=UNKNOWN/NOT_EXPOSED.
- Không đổi Neo4j query timeout/token/row; **ngoại lệ duy nhất** server config ở E4 là one-line Cypher URL blocklist đã qua TEMP.
- không tự dựng Cypher parser/filter.
- `graph-v1 --help` + mục `## Cổng đọc Graph cho agent` trong COLLAB khuyên query có LIMIT và tránh Cartesian/unbounded traversal.

E5 UNKNOWN không chặn R8 nếu E3/E4 PASS; phải ghi residual.

## 8. E6 · AGENT SIGNPOST / TRUST CONTRACT
KHÔNG tạo README/file repo mới. Signpost mô tả mức chứng minh URL blocklist chỉ trong phạm vi N1–N4/P, không quảng cáo an toàn tuyệt đối.

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
Chỉ best-effort nếu HJW không mutation xung đột và Hermes hỗ trợ mcp_servers stdio thật; không phát Hermes ASSIGN, không đổi công tắc MANUAL.
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

## 10. E8 · POST-PROTECT / ROLLBACK / TELEGRAM — Δ6
Ghi expected deltas TRƯỚC production: (1) `graph-v1-compose` SHA thay vì đúng env line + optional comment, Config Guard rebaseline **chỉ** target này theo DROOT29; (2) container identity `ctr.incomex-graph-neo4j` thay do recreate nhưng image digest, volume, graph data, ports không đổi. Không tắt/bypass Guard để đạt.
Bảo vệ wrapper/MANIFEST/binary/secret boundary và exact client entries Claude/Codex (Hermes optional), Mac config backup/diff/SHA trong evidence; **KHÔNG đưa COLLAB.md hoặc bản sao vào Config Guard** (Git đã giữ provenance).
Sau E4–E7: Config Guard + INV22 + production graph counts/hash + bảng đèn live/Telegram xanh. Nếu cảnh báo đỏ, ghi nguồn/chủ và hard gate Graph không PASS. Không public port, không in/ghi secret. Rollback proof trên TEMP và script rollback production nếu cần; bất kỳ E7/E8 critical FAIL sau prod change ⇒ E4 rollback compose/Neo4j ngay + gỡ scoped graph-v1 client entries/privilege/install tree có marker, KQ DỪNG. Không cleanup rộng trial.
Telegram receipt <=3 dòng, delivery proof, downtime thực tế, expected Guard delta, rebaseline đúng `graph-v1-compose` và container identity; comment nhắc test URL lại mỗi lần nâng Neo4j/APOC.

## 11. STEP_WALK_V1 · CHECKPOINTS / NO-WAIT
PRE MemAvailable>=3GiB, disk>=20GiB; TEMP mem/swap cap<=1GiB, image local. Các checkpoint đo rồi chuyển ngay; không terminal/schedule chờ gate chuyển xanh.

| Bước | Ai | Trigger/SLA | Evidence | Failure detection & next |
|---|---|---|---|---|
| S0 | Claude Code | RUN Host, read-gate trước STARTED/first mutation | SHA ACCEPT+READY, root active, Guard, RAM/disk, config, dump SHA, code URL usage | fail ghi KQ DỪNG ngay; nếu PASS→E1 |
| E1 | Claude Code | S0 PASS, verify trước install | full wheel/binary SHA/version/pin | mismatched→DỪNG; PASS→E2 |
| E2 | Claude Code | E1 PASS, trước E3 | TEMP MCP catalogue/read-only + GSM boundary | mismatch→DỪNG; PASS→E3 |
| E3 | Claude Code | E2 PASS, mỗi test bounded | N1 20, N2/N3/N4/P, correct blocklist errors, packet/DB PRE=POST | fail/Y→DỪNG trước prod; PASS→E4 |
| E4A | Claude Code | E3 PASS, Guard fresh; Neo4j health <=180s | exact compose diff+SHA, status, effective setting, rollback | mismatch/fail tự rollback→DỪNG; PASS→E4B |
| E4B | Claude Code | E4A PASS, probes trước MCP | 3 prod harmless URL denials, 13/13 B8 via MCP, counts/invariants | fail rollback→DỪNG; PASS→E5 |
| E5/E6 | Claude Code | E4B PASS | cost-bound residual + trust signpost COLLAB | fail Graph hard gate→rollback; else→E7 |
| E7 | Claude Code | E6 PASS | Claude+Codex real schema/read; Hermes optional | critical FAIL→rollback; PASS→E8 |
| E8 | Claude Code | E7 PASS | Guard expected deltas, rollback, Telegram, alarms | KQ XONG|DỪNG+gỡ busy, đóng CLI |

Host+Reviewer nghiệm thu bằng evidence thực, không thay runtime proof bằng JEV. Nếu KQ DỪNG: một NEXT_TRIGGER, không WAIT/HOLD, không sleep/poll, không giữ terminal.

## 12. ACCEPTANCE / CLAIM BOUNDARY — Δ7
R8R XONG chỉ khi E1–E8 hoàn tất: official 1.6.0 pin/hash PASS; TEMP **19/19 applicable original P72 tests** blocked + T7b N/A; N2 URL tất cả bị chặn bởi named blocklist, N3 file guard, N4 catalogue negative, P temp B8 13/13 + HTTP/Bolt + invariants; production đúng one-line config, healthy restart <=180s, 3 harmless URL probes denied, B8 13/13 **MCP production** and UNKNOWN preserved, prod data/users/hash/INV22 unchanged; Claude Code+Codex real read, Guard expected deltas/rebaseline, rollback evidence, 22/22 live alerts if green, Telegram proof. E5 native query limit UNKNOWN documented residual allowed; Hermes version blocked best-effort `HERMES_ENTRY=NOT_INSTALLED` allowed with evidence, not an R8 FAIL.

Hard security N1–N4/P unknown/fail, unexpected config diff, production/Guard/client critical fail ⇒ rollback/DỪNG. Do not claim PASS from code/doc/JEV alone. Sau XONG chỉ nói “đã chặn các đường ghi và gọi URL đã biết trong phạm vi thử bản TEMP + production; Agent Claude/Codex đã đọc đúng 13/13 B8 qua MCP”. KHÔNG nói “an toàn tuyệt đối”, “agent đã có toàn bộ KB/customer chat”, “JEV active runtime”, “đã phủ agent-data/Nuxt” hay “Hermes PASS” nếu chưa đo.

## 13. KQ
Evidence runtime:
/opt/incomex/work/graph-server/evidence/GS-R8R-AGENT-READONLY-MCP-20261008-12/
Giữ nguyên evidence và KQ lịch sử của RUN cũ P72.
Repo: Agent cập nhật Bảng/KQ/COLLAB đúng việc theo A4; E6 chỉ cập nhật mục `## Cổng đọc Graph cho agent` trước `## Con trỏ`, không tạo file repo khác. Ghi STARTED và KQ cùng cờ root theo A6; không sửa PROMPT/view khi RUN active. Không ghi secret/PII.
KQ phải gồm: S0 source snapshot, pin hashes, N1–N4/P matrix + URL errors, TEMP/prod B8 13/13, config diff/restore proof, production counts/hash/INV22, agent tool/read receipts, Guard/đèn/Telegram, residual/next trigger. DỪNG thì gỡ busy/đóng CLI, không schedule.
Final A9:
KQ@GS-R8R-AGENT-READONLY-MCP-20261008-12 XONG|DỪNG

