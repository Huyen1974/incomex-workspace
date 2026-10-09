# PROMPT — GS-R8R2-PINS-GUARDED-MCP-20261009-13

## 0. STATUS / AUTHORITY
RUN_ID: GS-R8R2-PINS-GUARDED-MCP-20261009-13
Task: work/graph-server · **same R8 roadmap node**, lượt phục hồi sau P80; không mở task mới
Executor_Surface: Claude Code CLI terminal MỚI do Owner dán RUN thủ công
Repo_Write_Path: Incomex MCP full all 2 workspace_* · root workspace
Runtime: Owner Mac + VPS1 production
Status: DRAFT · REVIEWER SHA CHƯA ACCEPT · HOST CHƯA READY · NO RUN

Authority: Owner A0/D10/D14/D16; AGENTS A4/A6/A9/DROOT30/31/50; Graph P72–P81. R8 lần 1 `GS-R8-AGENT-READONLY-MCP-20261007-11` KQ DỪNG E3, R8R lần 2 `GS-R8R-AGENT-READONLY-MCP-20261008-12` KQ DỪNG P80 do STOP_REQUESTED sai phiên, 0 mutation. Không tái sử dụng RUN_ID, READY P79 hết hiệu lực sau KQ P80. Claude Reviewer P76 chỉ ACCEPT SHA cũ `9315ede`; **lần này phải REVIEWER ACCEPT exact last-touch SHA mới**, Host READY lại sau HJW priority/slot clean, Owner mới dán RUN. Khi task/Guard/busy không sạch ⇒ DỪNG trước mutation, không giữ terminal/schedule chờ.

Bốn mục tiêu Owner và GS-RM1 không đổi: (1) business relations finite-by-version/discovery; (2) Graph×JEV; (3) official JEV skills; (4) Code Graph. R0–R7 Graph thật 3.596 node/6.823 edges; chỉ R8 agent-read-path chưa đạt, sau đó mới R9 Business refresh/catalog → R10 Graph→JEV SHADOW → R11 code agent-data/Nuxt. Không thực hiện việc HJW/VPSC trong RUN này.

## 1. MỤC TIÊU & EXACT PRODUCTION DELTA — NATIVE NEO4J + PIN/INV22
Chặn gọi URL / write-bypass qua APOC bằng native Neo4j 5.26.31, rồi nối official Neo4j MCP v1.6.0 **stdio read-only** để Claude Code/Codex hỏi Graph production thật. Không đổi dữ liệu Graph, image/digest, DB roles, volume, port, network hoặc các services khác; Hermes best-effort không ASSIGN.

**Đúng một thay đổi chức năng Neo4j** tại service `neo4j` trong `/opt/incomex/graph-server/prod-v1/compose.yaml`:
`NEO4J_internal_dbms_cypher__ip__blocklist: "0.0.0.0/0,::/0"`
và tối đa một comment nhắc test URL sau upgrade. **Một thay đổi metadata đồng bộ BẮT BUỘC** tại `prod-v1/manifest/pins.json`: cập nhật **chỉ một** hash đang pin `prod-v1/compose.yaml` trong `files` từ PRE SHA sang SHA byte thực của compose candidate; giữ nguyên mọi entry khác, thứ tự/format khi có thể, đặc biệt `restarts_baseline: 0`. Không thêm allowlist production.

**Ba expected protected deltas**: (1) Guard `graph-v1-compose` new SHA, (2) Guard `graph-v1-pins` new SHA, (3) Neo4j container identity `ctr.incomex-graph-neo4j` đổi sau single-service recreate; data/count/manifest/other guard targets giữ nguyên. Cả hai file config phải ghi và lùi **chỉ qua `incomex-config-apply-v0`**, baseline cập nhật tức thì trong từng apply, KHÔNG sửa trực tiếp/KHÔNG đợi E8 mới rebaseline. Cấm tuyệt đối `rollback-r7.sh` vì nó xóa volume Graph.

Không thuộc R8: HJW/VPSC, R9–R11, JEV runtime, KB/care-chat, broad delete/cleanup, nâng Neo4j, tự viết parser/gateway, mở host port, sửa DB user/secret, thay Graph provenance/data. Nếu thiếu phép đo/pin coupling => DỪNG thay vì tự nới ngoài hai targets.

## 2. S0 · AUTHORITY / EXCLUSIVE-VPS / CONFIG+PINS READ-ONLY GATES
1. Dùng Write_Path `workspace_*` root `workspace` read-gate, đọc AGENTS.md → root COLLAB → Graph COLLAB P72–P82 → PROMPT hiện hành. Cần **Claude Reviewer ACCEPT exact PROMPT last-touch SHA MỚI + Host READY same SHA** cho `GS-R8R2-PINS-GUARDED-MCP-20261009-13`; KQ lịch sử P80 DỪNG, không dùng READY P79. Gate PASS ghi STARTED vào task và root trước PRE theo A6; thiếu gate → DỪNG sạch, không giả READY.
2. Fresh-check root/HJW P239 tiếp theo + VPSC/Graph status, CLI/SSH/Guard/lease, `workspace_exec`/orphan `workspace-job-*`, temporary containers/processes. HJW có quyền ưu tiên retry trước theo P239; **cả E1–E8 của R8 phải độc quyền VPS**, không chồng mutation HJW/VPSC hoặc AI khác. Gate đỏ, chưa đo được, HJW STARTED → KQ DỪNG (không WAIT/HOLD/poll). PRE MemAvailable>=3 GiB, disk free>=20 GiB, Guard PRE và đèn Graph xanh, không ép chạy vì ngưỡng RAM chỉ mới đo hôm qua; SwapFree thấp ghi residual VPSC, không tự sửa.
3. S0(a): đọc `neo4j.conf`, `apoc.conf`, Neo4j 5.26.31 image/runtime, effective `prod-v1/compose.yaml` và Config Guard registry. Baseline mong đợi compose = exact baseline hash và SHA thực; Neo4j chưa có blocklist; allowlist chưa thu hẹp; `unrestricted=apoc.*`. Sai/missing => DỪNG.
4. S0(b): check bounded network URL dependence trong `graph-v1`, INV22/B8, scripts R7/Cognee; `LOAD CSV FROM 'file:///…'` là file import hợp lệ (P76 K8: 14 lệnh), không coi là network. Gặp call http/https/ftp đang dùng thật ⇒ DỪNG. S0(c): R7 dump SHA khớp manifest, graph PRE 3.596/6.823, INV22/current source fingerprints/backup/rollback dry proof.
5. **S0(d): PIN COUPLING — STOP GATE.** Đọc live `/opt/incomex/graph-server/prod-v1/manifest/pins.json`, `bin/graph-v1 check_fast()` actual pin contract và registry exact target `graph-v1-pins`; xác nhận `files` có đúng một key trỏ `prod-v1/compose.yaml`, giá trị SHA == sha256(compose PRE byte), `restarts_baseline: 0`, pins target baseline == sha256(pins PRE), compose target baseline == sha256(compose PRE), các target khác CLEAN. P80 đo hai targets riêng, **chưa độc lập xác minh live hôm nay**. Nếu key/path/hash/shape khác dự kiến ⇒ DỪNG trước runtime mutation, không tự thêm key/giả cấu trúc. SHA P80 là snapshot, phải fresh.
6. Kiểm `incomex-config-apply-v0 --help`/validator và quyền scoped, post_action=NONE; chứng minh target `graph-v1-compose` và `graph-v1-pins` đều thuộc allowlisted write path, mỗi target có candidate/expected-baseline riêng + rollback byte PRE. Phải đủ thời gian cho *cả cặp apply* trong khe Guard */5, ngay sau nhịp Guard, không disable Guard, không sleep/wait. Nếu không đủ cửa sổ/không chứng minh cách apply hai targets an toàn: DỪNG trước mutation, báo Reviewer. Trước first production apply đọc lại A6/root/task/PROMPT/READY/Guard/no-concurrent và hai hash PRE theo DROOT30.

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
- Redirect/DNS-rebinding nhiều hop: ghi `N/A_BY_CONSTRUCTION` với mã nguồn Neo4j 5.26.31 vì blocklist toàn dải chặn hop đầu trước kết nối; KHÔNG tính các URL/đường N2 khác chưa kiểm thành N/A (P76 K4). Network TEMP internal nhưng không coi “unreachable” là bằng chứng blocklist.

N3: `apoc.load.json('file:///etc/passwd')` bị file-import guard từ chối; native `LOAD CSV` file traversal không trả nội dung ngoài import directory. Không bật apoc.import.file.enabled/apoc.export.file.enabled.

N4 (P76 K5): Lấy danh mục thật CẢ `SHOW PROCEDURES` VÀ `SHOW FUNCTIONS` lọc `name STARTS WITH 'apoc.'`; nhóm READ/DEFAULT hay hàm APOC có khả năng tạo giao dịch/tiến trình/url (`cypher.*`, `periodic.*`, `trigger.*`, `systemdb.*`, `bolt.*`, `load.*`, `import.*`, `log.*`) phải được thử bằng negative fixture một procedure một case trong TEMP (ít nhất `apoc.cypher.runTimeboxed` ghi R8Probe nếu hiện diện). Không cài: N/A có receipt; không thử an toàn được: UNKNOWN/DỪNG; không được suy cả nhóm an toàn từ một ca. Thử cả `apoc.cypher.runFirstColumnSingle` / `runFirstColumnMany` nếu có, negative `CREATE (:R8Probe ...)` qua MCP TEMP và assert R8Probe=0.

P — positive trên TEMP: Nếu mount đúng import dir, thử read-only 1 CSV R7 `file:///pgdot/...` và assert không bị blocklist. `get-schema`, B8 13/13 qua **MCP**, 1 read query, HTTP 7474 inbound 200, Bolt login, APOC meta dùng cho schema. Counts/edge hash/gs_key/schema/user list trước=sau, R8Probe=0, egress 0. Lưu toàn bộ matrix N1–N4+P + lỗi đúng tên setting; không được ghi PASS từ docs/JEV.

**Nhánh Y chỉ trên TEMP:** nếu phát hiện đường ghi không qua URL sau N1–N4, được thử allowlist `dbms.security.procedures.allowlist` thu hẹp từ catalogue + APOC/Cognee actual usage, replay N/P; dù PASS vẫn **KQ DỪNG cùng exact Y** để Host/Claude duyệt prompt khác. Không bao giờ apply Y production trong RUN này. Nếu A còn URL mở, không dùng allowlist để che native LOAD CSV. Sau FAIL/UNKNOWN/Y: teardown TEMP, production không đổi.

## 6. E4 · TWO GUARDED CONFIG TARGETS + ONE NEO4J RECREATE / REAL MCP
**Chỉ sau S0 và E3 N1–N4+P A-only PASS**, mọi negative đúng named blocklist, 0 egress, TEMP before=after. P80 từng DỪNG trước E1 nên không có runtime phần này được nghiệm thu; bắt buộc đo lại.
1. **Staging trước mutation (không đụng production):** snapshot backup PRE byte+SHA `prod-v1/compose.yaml`, `prod-v1/manifest/pins.json`, registry baseline mỗi target, Neo4j digest/container identity/R7 dump. Candidate A = compose PRE + đúng 1 env blocklist dòng và <=1 comment, không diff khác; sha A = sha256(candidate bytes). Candidate B = pins PRE nhưng thay **duy nhất một** giá trị `files[actual-compose-key]` bằng sha A, giữ các keys/values khác và `restarts_baseline:0`, không thêm record mới. Validate json/hash matching, `docker compose config`, tool scope, schema and expected-baseline exact. Candidate SHA/pin phải được tạo từ bytes sẽ được apply, không tính trước định dạng lại rồi sai SHA. Không có candidate chính xác => KQ DỪNG trước production mutation.
2. **Apply cặp cực hẹp qua `incomex-config-apply-v0` (K1) trong Guard window:** lấy PRE Guard PERIODIC vừa hoàn tất, còn >=3 phút tới nhịp kế, no shared-process/container. (a) Apply target `graph-v1-compose` candidate A với expected-baseline=compose PRE; apply-v0 backup/atomic write + baseline update ngay. (b) **Ngay lập tức** apply target `graph-v1-pins` candidate B với expected-baseline=pins PRE; baseline update ngay. Không chờ Guard ticker giữa hai bước, không tự sửa tay/skip Config Guard. Nếu target thứ hai fail, rollback target đầu **ngay** bằng apply-v0 reverse từ original PRE; nếu rollback fail => DỪNG+RED/Telegram. Interval giữa (a) và (b) có thể tạm làm INV22 thấy mismatch; đo/dặn báo ngắn nếu monitor chớp, không giả “100% không thể báo đỏ”. Cửa sổ không đủ/Guard tick chen hoặc unauthorized changes => revert bounded và DỪNG.
3. **Verify pair trước recreate:** sha live(compose)=sha A, actual pin entry=sha A, sha live(pins)=candidate B SHA, cả 2 Guard baselines khớp, những entry khác/restarts_baseline không đổi. Chỉ khi pair consistent mới recreate **riêng** Neo4j service (không `compose down`, không pull/volume prune); health/Bolt/HTTP stable <=180s, log downtime; container digest/data/port giữ nguyên. Neo4j 5.26.31 internal config `internal.dbms.cypher_ip_blocklist` kiểm bằng `/var/lib/neo4j/conf/neo4j.conf`, KHÔNG chỉ dùng `SHOW SETTINGS` (K3).
4. **Prod acceptance:** INV22, `bin/graph-v1 check_fast()`, Guard+both target baselines, graph 3.596/6.823/count/hash/schema/users/invariant, HTTP 17474/Bolt/restore oracle PASS. Ba URL harmless probes READ không POST/không prod secret/0 traffic phải nêu `internal.dbms.cypher_ip_blocklist`. Chỉ SAU đó materialize MCP wrapper/connect; chạy B8 **13/13 qua MCP production** (UNKNOWN vẫn UNKNOWN), packet capture query 0 unauthorized outbound, Claude/Codex agent smoke theo E7. Không dùng cypher-shell thay MCP; không ghi Graph.
5. **Rollback an toàn ở bất kỳ failure sau first apply (K2):** **TUYỆT ĐỐI CẤM `rollback-r7.sh`** (xóa data volume). Đường duy nhất apply-v0 REVERSE theo target với candidate byte PRE và expected-baseline NEW cho từng target đang thay. Nếu cả hai đã applied, reverse **pins target trước, compose target sau** trong cùng guarded window, verify hashes/pins equality; nếu mới compose applied, chỉ reverse compose. Recreate chỉ Neo4j nếu đã recreate, prove PRE config/INV22/Graph state/Config Guard/health/ports restored. Gỡ scoped MCP/client footprint của RUN này, không xóa bất kỳ data volume, không rollback Graph R7. Nếu revert, Guard/restore/health fail => KQ DỪNG + RED/Telegram, báo rõ không sạch; không tự vá broad.
6. **Hard invariants:** ngoài 1 dòng env(+comment) + 1 pins hash value, 0 file config/procedure/permission/role/network/Neo4j image khác. Có external job/Guard mutation/Pin/hash drift từ lúc PRE => DỪNG. E8 là **hậu kiểm 2 baselines đã cập nhật kịp lúc ở E4**, không phải nơi trì hoãn rebaseline. Bảo vệ đúng phạm vi R8, không làm HJW/VPSC.

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

## 10. E8 · POST-PROTECT / GUARD COUPLING / TELEGRAM
Trước first production mutation, ghi **BA expected changes**: (1) `graph-v1-compose` hash thay do 1 env/comment; (2) **`graph-v1-pins`** hash thay do duy nhất sha256 `compose.yaml` trong `files`, `restarts_baseline:0` giữ nguyên; (3) container `ctr.incomex-graph-neo4j` identity đổi sau single-service recreate. Hai Config Guard baselines update ngay trong hai lần `incomex-config-apply-v0` E4; E8 chỉ audit/diff PRE/POST, KHÔNG bổ sung thủ công hay delay tới phút */5. Không chạm bất kỳ Guard targets khác. External footprint do `workspace_exec` hoặc container của phiên khác gây PRE→POST FAIL thì dừng/rollback; không whitelist/bypass Guard.

MCP wrapper/MANIFEST/binary pinned, user-scope Claude+Codex entries, Hermes optional, Mac config backups và secret hygiene; **không ghi COLLAB.md/bản sao vào Config Guard**, Git giữ provenance. Sau E4–E7: Graph `bin/graph-v1 check_fast()` PASS, `INV22.graph_v1`/Guard/đèn xanh, hashes of compose/pins and matching pin entry, volume/source/count/schema unchanged, HTTP/Bolt/backup PASS, no public port/secret printed. Chứng minh rollback thực hiện được ở TEMP và E4 production scoped reversal path sẵn, **CẤM `rollback-r7.sh`**.

Nếu E7/E8 critical FAIL sau production changes: **rollback cả hai targets qua apply-v0** như E4.5, recreate duy nhất Neo4j, cleanup chỉ scoped entries, KQ DỪNG và evidence; không hard-delete. Guard RED hoặc rollback không hoàn tất => báo ngay cho Owner/Telegram, không nói XONG. Telegram receipt <=3 dòng + delivery proof, xác nhận theo evidence thực tế; test URL lại khi nâng Neo4j/APOC.

## 11. STEP_WALK_V1 · CHECKPOINTS / NO-WAIT
PRE MemAvailable>=3GiB, disk>=20GiB; TEMP mem/swap cap<=1GiB, image local. Các checkpoint đo rồi chuyển ngay; không terminal/schedule chờ gate chuyển xanh.

| Bước | Ai | Trigger/SLA | Evidence | Failure detection & next |
|---|---|---|---|---|
| S0 | Claude Code | RUN Host, read-gate trước STARTED/first mutation | NEW SHA ACCEPT+READY, HJW slot, Guard, RAM/disk, compose PRE+pins PRE/hash coupling, dump | fail ghi KQ DỪNG ngay; nếu PASS→E1 |
| E1 | Claude Code | S0 PASS, verify trước install | full wheel/binary SHA/version/pin | mismatched→DỪNG; PASS→E2 |
| E2 | Claude Code | E1 PASS, trước E3 | TEMP MCP catalogue/read-only + GSM boundary | mismatch→DỪNG; PASS→E3 |
| E3 | Claude Code | E2 PASS, mỗi test bounded | N1 20, N2/N3/N4/P, correct blocklist errors, packet/DB PRE=POST | fail/Y→DỪNG trước prod; PASS→E4 |
| E4A | Claude Code | E3 PASS, Guard */5 window and S0 SHA recheck | paired apply-v0 compose+pins baseline updates/verified pin, one Neo4j recreate <=180s, scoped rollback | mismatch/external job/fail → reverse both as applicable then DỪNG; PASS→E4B |
| E4B | Claude Code | E4A PASS, probes trước MCP | 3 prod harmless URL denials, 13/13 B8 via MCP, counts/invariants | fail rollback→DỪNG; PASS→E5 |
| E5/E6 | Claude Code | E4B PASS | cost-bound residual + trust signpost COLLAB | fail Graph hard gate→rollback; else→E7 |
| E7 | Claude Code | E6 PASS | Claude+Codex real schema/read; Hermes optional | critical FAIL→rollback; PASS→E8 |
| E8 | Claude Code | E7 PASS | Guard 3 deltas, pins/compose same SHA, INV22/check_fast, rollback, Telegram | KQ XONG|DỪNG+gỡ busy, đóng CLI |

Host+Reviewer nghiệm thu bằng evidence thực, không thay runtime proof bằng JEV. Nếu KQ DỪNG: một NEXT_TRIGGER, không WAIT/HOLD, không sleep/poll, không giữ terminal.

## 12. ACCEPTANCE / CLAIM BOUNDARY — Δ7
R8R XONG chỉ khi E1–E8 hoàn tất: official 1.6.0 pin/hash PASS; TEMP **19/19 applicable original P72 tests** blocked + T7b N/A; N2 URL tất cả bị chặn bởi named blocklist, N3 file guard, N4 catalogue negative, P temp B8 13/13 + HTTP/Bolt + invariants; production đúng one-line Neo4j config **và đúng one-hash metadata update pins.json** via paired apply-v0 with both Guard baselines; health <=180s, 3 harmless URL probes denied, B8 13/13 **MCP production** and UNKNOWN preserved, prod data/users/hash/INV22 unchanged; Claude Code+Codex real read, Guard expected **3** deltas (compose/pins/container), `graph-v1 check_fast()`+INV22 PASS, pin SHA==live compose, restore/reverse-both proof, 22/22 live alerts if green, Telegram proof. E5 native query limit UNKNOWN documented residual allowed; Hermes version blocked best-effort `HERMES_ENTRY=NOT_INSTALLED` allowed with evidence, not an R8 FAIL.

Hard security N1–N4/P unknown/fail, unexpected config diff, production/Guard/client critical fail ⇒ rollback/DỪNG. Do not claim PASS from code/doc/JEV alone. Sau XONG chỉ nói “đã chặn các đường ghi và gọi URL đã biết trong phạm vi thử bản TEMP + production; Agent Claude/Codex đã đọc đúng 13/13 B8 qua MCP”. KHÔNG nói “an toàn tuyệt đối”, “agent đã có toàn bộ KB/customer chat”, “JEV active runtime”, “đã phủ agent-data/Nuxt” hay “Hermes PASS” nếu chưa đo.

## 13. KQ / EVIDENCE & ROOT BUSY
Evidence RUN mới:
/opt/incomex/work/graph-server/evidence/GS-R8R2-PINS-GUARDED-MCP-20261009-13/
Preserve full history P72 and P80 evidence, including STOP_REQUESTED, never rewrite. Repo: only Graph COLLAB/Bảng/KQ and root busy per A6, no new repo artifact files; E6 only adds/updates existing `## Cổng đọc Graph cho agent` section, not PROMPT/view during STARTED. No secrets in repo/Telegram.
KQ includes S0 baseline both files/target IDs, exact new/old SHA, pins one-field delta and restarts_baseline proof, apply-v0 two receipts + forward/reverse rollback, E3 N1–N4/P full matrix incl APOC functions, B8 temp+production through MCP, effective setting/probes, Guard/INV22/check_fast/alerts, transaction count/edge/source hashes unchanged, 2 client read tests, Telegram, outstanding residual. Hard FAIL ⇒ bounded scoped reversal + KQ DỪNG with exact blocker/one NEXT_TRIGGER; gỡ root busy/close CLI, no wait/parallel mutation.
Final:
KQ@GS-R8R2-PINS-GUARDED-MCP-20261009-13 XONG|DỪNG

