# PROMPT — GS-R8R2-PINS-GUARDED-MCP-20261009-13

## 0. STATUS / AUTHORITY
RUN_ID: GS-R8R2-PINS-GUARDED-MCP-20261009-13
Task: work/graph-server · **same R8 roadmap node**, lượt phục hồi sau P80; không mở task mới
Executor_Surface: Claude Code CLI terminal MỚI do Owner dán RUN thủ công
Repo_Write_Path: Incomex MCP full all 2 workspace_* · root workspace
Runtime: Owner Mac + VPS1 production
Status: DRAFT · Claude P82 PARTIAL (M1–M4) ĐÃ TIẾP NHẬN · CHỜ REVIEWER ACCEPT SHA MỚI · HOST CHƯA READY · NO RUN

Authority: Owner A0/D10/D14/D16; AGENTS A4/A6/A9/DROOT30/31/50; Graph P72–P83. R8 lần 1 `GS-R8-AGENT-READONLY-MCP-20261007-11` KQ DỪNG E3, R8R lần 2 `GS-R8R-AGENT-READONLY-MCP-20261008-12` KQ DỪNG P80 do STOP_REQUESTED sai phiên, 0 mutation. Không tái sử dụng RUN_ID, READY P79 hết hiệu lực sau KQ P80. Claude Reviewer P82 PARTIAL SHA `566b876`; P76 chỉ ACCEPT SHA cũ `9315ede`; **lần này phải REVIEWER ACCEPT exact last-touch SHA mới**, Host READY lại sau HJW priority/slot clean, Owner mới dán RUN. Khi task/Guard/busy không sạch ⇒ DỪNG trước mutation, không giữ terminal/schedule chờ.

Bốn mục tiêu Owner và GS-RM1 không đổi: (1) business relations finite-by-version/discovery; (2) Graph×JEV; (3) official JEV skills; (4) Code Graph. R0–R7 Graph thật 3.596 node/6.823 edges; chỉ R8 agent-read-path chưa đạt, sau đó mới R9 Business refresh/catalog → R10 Graph→JEV SHADOW → R11 code agent-data/Nuxt. Không thực hiện việc HJW/VPSC trong RUN này.

## 1. MỤC TIÊU / DANH SÁCH 5 TỆP ĐÓNG — P82 M1
R8 còn cùng một mục tiêu: đóng đường URL/APOC write-bypass bằng Neo4j 5.26.31, rồi đưa official Neo4j MCP 1.6.0 stdio read-only cho Claude Code/Codex đọc Graph thật. R9–R11 và HJW/VPSC không thuộc RUN. Không đổi Graph data/schema/roles/image/digest/ports/network; không mở service mới.

**NĂM MỤC TỆP PRODUCTION DUY NHẤT được thay/tạo, phải chứng minh C3 v2 và Đ31 coverage từng mục:**

| Tệp | Target Config Guard | Delta và rollback |
|---|---|---|
| `prod-v1/compose.yaml` | `graph-v1-compose` | +1 env `NEO4J_internal_dbms_cypher__ip__blocklist: "0.0.0.0/0,::/0"` (+<=1 comment); apply-v0 đảo về PRE |
| `prod-v1/manifest/pins.json` | `graph-v1-pins` | thay đúng 1 SHA compose trong `files`, `restarts_baseline:0` nguyên; apply-v0 đảo PRE |
| `mcp-readonly-v1/bin/graph-v1` (MỚI) | `graph-v1-mcp-wrapper` (MỚI) | wrapper root-owned, tự kiểm SHA binary trước exec; rollback `new:<remove>` |
| `/var/lib/incomex-config-guard-v0/registry.tsv` | `guard-registry` | +1 row target wrapper (+<=1 comment); apply-v0 đảo PRE |
| `/opt/incomex/scripts/code-ledger.tsv` | `r7-code-ledger-tsv` | +1 `LOCKED` executable wrapper theo schema thực; apply-v0 đảo PRE |

Đây là **1 delta chức năng Neo4j + 1 metadata pin + 1 executable wrapper mới + 2 tệp đăng ký bảo vệ**, không phải thay thiết kế Graph. Mọi tệp production khác/Guard target khác có delta ⇒ FAIL. Neo4j container recreate **cùng image ID** KHÔNG là mục C3 (C3 v2 gồm `file:/kuma:/image:`); log container ID/StartedAt vào evidence, thay image ID = FAIL. Mac Claude/Codex user-scope config thuộc E7, backup/reverse riêng, không tính vào 5 tệp VPS. `venv/` được loại khỏi bề mặt mã, `MANIFEST.json` chỉ chứng từ (không là executable, wrapper không đọc) nên KHÔNG register Guard, ghi SHA evidence.

Config Guard baseline của tệp đã đăng ký cập nhật ngay bằng `incomex-config-apply-v0`; target wrapper mới được đăng ký bằng khuôn R7 `c-register.py` đã kiểm S0 (baseline mới trước registry). Không sửa tay registry/ledger, không lách Config Guard. Binary official MCP `neo4j-mcp-server` phải được wrapper tự SHA256 check trước **mỗi lần exec**. **CẤM `rollback-r7.sh`** vì xóa volume Graph. Không được tạo đường code chạy thêm để vượt danh sách 5 mục.

## 2. S0 · AUTHORITY / SHARED VPS / 5-FILE FOOTPRINT + STORAGE — P82 M4
1. Read-gate workspace_* root workspace: AGENTS → root COLLAB → Graph COLLAB P72–P84 → active PROMPT. Reviewer ACCEPT exact **SHA mới** sau P82 + Host READY same SHA mới cho `GS-R8R2-PINS-GUARDED-MCP-20261009-13`; P79 READY/P80 RUN đã terminal không hợp lệ cho lượt này. Không có STOP/active shared mutation. Ghi STARTED+root busy theo A6 khi đã đủ cổng.
2. **E1–E8 độc quyền VPS**: fresh HJW (P241 hoặc mới hơn)/VPSC/Graph/root busy, `workspace_exec`/container `workspace-job-*`/process/Guard. HJW retry đang ưu tiên, có STARTED ⇒ DỪNG trước mutation. RAM available>=3GiB, disk free>=20GiB, Guard PRE + đèn thuộc Graph xanh; swap thấp chuyển residual VPSC, không sửa. Không tự chen hàng/cấp RUN.
3. S0(a) Neo4j 5.26.31 effective `neo4j.conf`, `apoc.conf`, `compose.yaml` hiện hữu, Guard baselines. S0(b) grep bounded `http/https/ftp` sources thật trong Graph v1/B8/R7 ingest/Cognee: **14 dòng LOAD CSV = 13 câu thực đọc `file:///` + 1 comment**, không phải đường mạng (K8), ghi file/line; có network URL đang sử dụng ⇒ DỪNG. S0(c) dump R7 SHA + graph PRE 3.596 nodes/6.823 edges + INV22 verify.
4. S0(d) pins coupling: trong `pins.json`, `files` key đường dẫn **tuyệt đối**, phải chứa exact PRE SHA của `compose.yaml` đúng **một** lần, giữ `restarts_baseline:0`; candidate thay **đúng một chuỗi 64 ký tự bằng bytes**, không parse/re-serialize JSON. Config Guard `graph-v1-compose` và `graph-v1-pins` baseline = sha live. CLI chính R7 là `prod-v1/bin/graph-v1` target `graph-v1-cli` **không sửa**; `check_fast()` chỉ là hàm bên trong, nghiệm thu bằng `prod-v1/bin/graph-v1 status` exit 0 + `bad_fast` rỗng và `watch --guard` PASS, không gọi `check_fast()` như CLI.
5. **S0(e) anti-blind-spot bắt buộc:** đọc `registry.tsv`, `code-ledger.tsv`, `pins.json`, C3 `check_coverage`, INV23/Đ31 và `graph-v1-cli` template. Lập bảng `path / existed PRE? / candidate delta / registry target / ledger / baseline / rollback / C3 category` cho từng tệp sẽ tạo/sửa; **tập hợp phải đúng 5 mục §1**, wrapper mới cần `new:<remove>`, registry+ledger schema chuẩn theo R7 `c-register.py`. Thiếu target/quyền/cú pháp, footprint bất ngờ ⇒ DỪNG trước mutation, không tự cho phép file thứ 6.
6. Chạy `storage-watch.py event-preflight` nhóm GRAPH theo help thật (P82 footprint ~8.55/10GiB là snapshot, phải fresh đo và tính thêm wheel/venv/TEMP/evidence); đảm bảo <=10 GiB Graph và disk floor. Check `incomex-config-apply-v0 --help` cho `graph-v1-compose`, `graph-v1-pins`, `guard-registry`, `r7-code-ledger-tsv` + Guard registration path for new target. Bất kỳ thiếu đường ghi đã duyệt hay resource FAIL ⇒ DỪNG, không tự viết bypass.
7. Kiểm Guard thực tế INV22/INV23 `TWO_PASS` periodic */5 (một lỗi `2-pass 1/2` chỉ warning, hai liên tiếp đỏ), Config Guard mismatch một nhịp đỏ, C3 v2 file/kuma/image. Xác nhận một-script §6 có rollback PRE bytes và bounded slot wait; trước first mutation re-read root/STOP/PROMPT SHA/root busy + Guard/resource/5-file PRE. Không WAIT ở cấp task.

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

Chữ `graph-v1` sau đây chỉ **wrapper MỚI** trong `mcp-readonly-v1/bin/`, KHÔNG phải `prod-v1/bin/graph-v1` R7. Wrapper kiểm sha256 installed executable against exact `00d4882f412427db064df39492b882781ba1040db82f94ea8cdeedd16db0dfff` trước **mọi** exec, mismatch ⇒ từ chối chạy, không đưa secret; wrapper phải được Guard+ledger đăng ký §6.6/§10. `MANIFEST.json` chỉ evidence, không được coi là runtime binary integrity control.

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

Wrapper root-owned, non-writable by agent users; chỉ expose client MCP sau khi đã registered/baseline/C3 check.
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

## 6. E4 · GUARDED ONE-SHOT + 5-FILE WRAPPER REGISTRATION — P82 M1/M2/M4
Sau S0+E3 TEMP N1–N4/P PASS, no write/egress, backup dump/invariants. Không apply allowlist production, không xóa Graph.
1. **PREP trước mutation:** snapshot PRE bytes+SHA `prod-v1/compose.yaml`, `prod-v1/manifest/pins.json`, target baselines, image/Neo4j Graph counts. Candidate A = compose PRE + đúng 1 env blocklist(+<=1 comment). Candidate B = pins PRE **thay đúng 1 chuỗi SHA-256 compose ở absolute key**, giữ mọi byte khác/`restarts_baseline:0`. Validate SHA A/B, `docker compose config`, json, delta, two apply-v0 targets, rollback byte PRE; S0 5-file footprint đã PASS. Dựng run-scoped apply script ở evidence/staging **ngoài surface mã Guard đã kiểm S0**; nếu script rơi vào surface monitored ⇒ DỪNG, không tạo tệp Guard thứ 6.
2. **E4.2–E4.5 chạy trong MỘT SCRIPT ÁP-MỘT-LỆNH (mẫu HJW `n3-2a-apply.sh`)**, có rollback tự động khi bất kỳ bước nào fail sau mutation đầu. Freeze script SHA/candidates/rollback+Guard PRE trước khi xin đúng 1 permission Owner. Script recheck lease/process/foreign containers/hash rồi dùng `slot_wait` trần **<=6 phút**, bắt đầu APPLY **trong 20 giây sau dòng `GUARD PERIODIC` MỚI HOÀN TẤT** ở `/var/log/incomex/mcpw-guard.log`; nếu không có khe hợp lệ thì DỪNG TRƯỚC mutation. Đây là căn giờ hữu hạn **trong một RUN đã READY**, không phải task HOLD hay background schedule.
3. **K7 CHỈ CĂN MỘT LẦN CHO CẢ CHUỖI**; không đòi >=3 phút lần 2 trước recreate. Khe khoảng 235 giây gồm hai apply (vài giây), single-service Neo4j recreate (thường ~90s, health <=180s), 3 URL harmless probes. Script áp liên tiếp qua `incomex-config-apply-v0`: **compose A trước → pins B sau**, mỗi apply cập nhật baseline NGAY; verify SHA live compose/pins/entry==SHA A/other pins unchanged. Không chỉnh tay, không đợi E8 rebaseline. Fail #1 thì 0 mutation; fail #2 hoặc bất kỳ sau đó ⇒ **reverse pins nếu đã applied, rồi reverse compose** từ original PRE bytes qua apply-v0 (expected-baseline NEW), rollback health/Guard/INV22.
4. Script recreate **chỉ** `neo4j` (không compose down/pull/volume prune), giữ image ID/dữ liệu, health/Bolt/HTTP <=180s. Conf `internal.dbms.cypher_ip_blocklist` đo từ file trong container + startup, KHÔNG `SHOW SETTINGS`. Ba harmless URL probes READ không POST/mật khẩu prod phải lỗi đúng tên setting, 0 network hits; fail thì rollback ngay trong một-script. **INV22/INV23 periodic `2-pass 1/2`** trong chuyển tiếp chỉ ghi receipt, không FAIL; 2 failed ticks liên tiếp/Config Guard NOT CLEAN/health timeout/POST fail => rollback + KQ DỪNG. Không bypass Guard, không tự nới whitelist.
5. Khi một-script PASS: xác minh Graph production counts 3.596/6.823/invariants, users/schema/ports/hash/INV22, `prod-v1/bin/graph-v1 status` exit 0 (`bad_fast` empty) + `watch --guard` PASS. Chạy **13/13 B8 bằng official Neo4j MCP production thật** qua *run-scoped temp stdio harness đã pin* (chưa expose final unguarded wrapper), 0 unauthorized outbound, UNKNOWN giữ UNKNOWN. Fail => rollback compose+pins scoped, KQ DỪNG; không dùng direct cypher-shell thay MCP.
6. **M1 SAU B8 PASS, TRƯỚC E7 — Guard wrapper mới/INV23:** Tạo final root-owned wrapper `mcp-readonly-v1/bin/graph-v1` từ candidate đã thử, binary SHA pre-exec check §4. Dùng đúng template R7 `c-register.py`/Guard tool đã đo: (i) apply-v0 `r7-code-ledger-tsv` +1 `LOCKED` wrapper; (ii) đăng ký baseline target MỚI `graph-v1-mcp-wrapper` (sha wrapper, rollback `new:<remove>`); (iii) apply-v0 `guard-registry` +1 row(+<=1 comment). Thực hiện gói đăng ký liên tục bounded, POST `check_coverage` phải đủ 5 `file:` và Đ31 `config-guard:<id>`, INV23+Config Guard PASS; không cài client nếu wrapper chưa được bảo vệ. Nếu không có sanctioned path/schema/Guard baseline => rollback toàn bộ, không sửa Guard code hoặc tự ghi ngoài apply-v0.
7. **Rollback nếu E4/E7/E8 fail:** revert `guard-registry` rồi `r7-code-ledger-tsv` bằng apply-v0 về PRE nếu đã thay; remove target `graph-v1-mcp-wrapper` baseline bằng approved Guard registration reversal, xóa wrapper/new install tree đúng marker `new:<remove>`, xóa scoped Mac client entries RUN này; reverse **pins → compose** by apply-v0, recreate chỉ Neo4j nếu đã recreate, prove PRE hashes/baselines/invariants/Guard/INV22/23. **CẤM `rollback-r7.sh`** vì xóa Graph volume; rollback không sạch => ĐỎ/Telegram/KQ DỪNG, không sửa broad.
8. **Ranh giới:** đúng 5 production files §1 + user-scope Mac client changes scoped, `venv/` excluded, `MANIFEST.json` evidence. Container identity change same image ID chỉ log, **không là C3 item**. No extra Guard targets/roles/Graph data/network changes, HJW/VPSC giữ lane riêng. E8 audit final baselines đã update ngay trong apply/registration, không làm rebaseline chậm.

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

## 9. E7 · CHỈ 2 AGENT SURFACES — P82 M3
Một wrapper `mcp-readonly-v1/bin/graph-v1` dùng chung, **chỉ** Claude Code và Codex trên Mac; phải bảo vệ đủ §6.6 trước khi đăng ký client, không tạo gateway mới hay repo `.mcp.json`.

### Claude Code trên Mac
Dùng `claude mcp --help` runtime, user scope server id `graph-v1`, stdio tương đương `ssh contabo /opt/incomex/graph-server/mcp-readonly-v1/bin/graph-v1 mcp`; backup+diff user config. Fresh Claude Code tools catalogue đúng get-schema/read-cypher (no write-cypher), schema+read+non-PII question PASS.
### Codex trên Mac
Dùng current Codex MCP help/config, stdio `ssh contabo /opt/incomex/graph-server/mcp-readonly-v1/bin/graph-v1 mcp`, user scope, backup+diff `~/.codex/config.toml`. Fresh Codex connected+schema+read PASS, 0 write tools. Không lộ secret argv/config/log.
### Hermes: DEFERRED TO HJW, KHÔNG CHẠM TRONG RUN NÀY
Ghi `HERMES_ENTRY=NOT_INSTALLED`, reason `HJW_OWNS_HERMES_CONFIG`. **Không** đọc/sửa `/var/lib/hermes/.hermes/config.yaml`, không đổi Guard target `hermes-config-yaml`, không cài/test Hermes MCP, không ASSIGN/vé Hermes. Đây là residual task HJW và **không chặn R8 XONG**.

## 10. E8 · FIVE-FILE CONFIG GUARD / INV22+23 / TELEGRAM — P82 M1
**Chốt footprint C3 v2 là ĐÚNG 5 item `file:` §1**, không phải 3 deltas và không tính container recreate same image. Kết quả mong đợi:
- `graph-v1-compose`: compose 1 env (+<=1 comment), Guard baseline mới via apply-v0.
- `graph-v1-pins`: đúng 1 SHA compose entry ở absolute key, Guard baseline via apply-v0.
- `graph-v1-mcp-wrapper`: new wrapper, SHA binary verified before exec, baseline mới+rollback `new:<remove>`.
- `guard-registry`: +1 dòng target wrapper(+<=1 comment), baseline via apply-v0.
- `r7-code-ledger-tsv`: +1 dòng `LOCKED`, baseline via apply-v0.
Mọi tệp code/prod config khác delta => FAIL. Record `path/old-new SHA/target/coverage Đ31/rollback` đủ 5; C3 `check_coverage` mỗi tệp = `config-guard:<registered-id>` và new target có `new:<remove>`. **Container Neo4j recreated cùng image ID không tính item C3**, chỉ ID/StartedAt receipt; image ID thay = FAIL. Mac client config backups/scoped delta ngoài VPS C3.

INV22/INV23 periodic TWO_PASS: một `2-pass 1/2` trong chuyển tiếp ghi evidence, **không** là đèn đỏ thật; hai nhịp fail liên tiếp = RED. Config Guard lệch thì đỏ ở nhịp kế, nên các tệp đã đăng ký luôn đổi bằng apply-v0 kèm baseline ngay; đừng tắt/nới Guard. POST PRE/POST không có two_pass => mọi file/INV22/INV23/Đ31 phải PASS. Kiểm `prod-v1/bin/graph-v1 status` exit 0 + `bad_fast` empty, `watch --guard` PASS; không dùng `check_fast()` làm lệnh CLI; tệp CLI R7 `graph-v1-cli` không sửa. R7 graph data/source/roles/ports, health/Bolt/HTTP, no leaked secrets/public port; storage cap GRAPH 10GB.
Critical E6/E7/E8 FAIL sau production mutation ⇒ rollback đúng cả 5 target/file trong phạm vi đã thay (§6.7), recreate chỉ Neo4j, KQ DỪNG/Telegram RED nếu không clean; **CẤM `rollback-r7.sh`**. Không đăng ký COLLAB.md/MANIFEST vào Guard; Git bảo quản signpost. Receipt Telegram <=3 dòng + delivery proof; `HERMES_ENTRY=NOT_INSTALLED` residual HJW.

## 11. STEP_WALK_V1 · CHECKPOINTS / NO-WAIT
PRE MemAvailable>=3GiB, disk>=20GiB; TEMP mem/swap cap<=1GiB, image local. Các checkpoint đo rồi chuyển ngay; không terminal/schedule chờ gate chuyển xanh. Riêng `slot_wait` bounded 6 phút trong script một-lệnh E4 là căn giờ hợp lệ trong RUN, không phải task HOLD.

| Bước | Ai | Trigger/SLA | Evidence | Failure detection & next |
|---|---|---|---|---|
| S0 | Claude Code | RUN Host, read-gate trước STARTED/first mutation | new SHA ACCEPT+READY, HJW slot, Guard, RAM/disk, **5-file footprint registry+ledger + storage GRAPH preflight**, compose/pins/dump | fail ghi KQ DỪNG ngay; nếu PASS→E1 |
| E1 | Claude Code | S0 PASS, verify trước install | full wheel/binary SHA/version/pin | mismatched→DỪNG; PASS→E2 |
| E2 | Claude Code | E1 PASS, trước E3 | TEMP MCP catalogue/read-only + GSM boundary | mismatch→DỪNG; PASS→E3 |
| E3 | Claude Code | E2 PASS, mỗi test bounded | N1 20, N2/N3/N4/P, correct blocklist errors, packet/DB PRE=POST | fail/Y→DỪNG trước prod; PASS→E4 |
| E4A | Claude Code | E3 PASS, Guard */5 window and S0 SHA recheck | **one-script** slot_wait <=6m, 20s post Guard tick, paired apply-v0 compose+pins, one Neo4j recreate <=180s + 3 probes, auto rollback | mismatch/external job/fail → reverse both as applicable then DỪNG; PASS→E4B |
| E4B | Claude Code | E4A PASS, probes trước MCP | 3 prod harmless URL denials, 13/13 B8 via real MCP, **5-file wrapper+ledger/registry registration**, INV23/counts/invariants | fail rollback→DỪNG; PASS→E5 |
| E5/E6 | Claude Code | E4B PASS | cost-bound residual + trust signpost COLLAB | fail Graph hard gate→rollback; else→E7 |
| E7 | Claude Code | E6 PASS | Claude+Codex real schema/read; `HERMES_ENTRY=NOT_INSTALLED` (no Hermes actions) | critical FAIL→rollback; PASS→E8 |
| E8 | Claude Code | E7 PASS | Guard **5 file deltas C3/Đ31**, compose/pins SHA, INV22/23, `graph-v1 status`, rollback, Telegram | KQ XONG|DỪNG+gỡ busy, đóng CLI |

Host+Reviewer nghiệm thu bằng evidence thực, không thay runtime proof bằng JEV. Nếu KQ DỪNG: một NEXT_TRIGGER, không WAIT/HOLD, không sleep/poll, không giữ terminal.

## 12. ACCEPTANCE / CLAIM BOUNDARY — P82 M1–M4
R8 XONG khi: (i) S0 exact Reviewer ACCEPT new SHA+Host READY, exclusive VPS, Guard/resource+storage GRAPH preflight PASS, **5-file footprint và registration/rollback path được đo**, (ii) official MCP 1.6.0 wheel/binary SHA đúng, 0 write tools và secret-safe, (iii) TEMP N1 19/19 áp dụng blocked + T7b N/A; N2 URL named-blocklist; N3 file; N4 **PROCEDURES ∪ FUNCTIONS**; P temp B8 13/13 + HTTP/Bolt, PRE=POST và 0 egress, (iv) production one-shot guarded apply compose+pins, single Neo4j restart <=180s, 3 harmless blocklist probes, **13/13 B8 qua MCP production**, Graph data 3.596/6.823+invariants unchanged, (v) **năm C3 file delta §1** all registered Guard/Đ31, target `graph-v1-mcp-wrapper` new, `guard-registry` và `r7-code-ledger-tsv` updated, binary re-hash at runtime, INV22/INV23/status/watch Guard PASS, footprint clean+Telegram, 22/22 lights, scoped rollback evidence, (vi) Claude Code + Codex fresh schema/read pass; `HERMES_ENTRY=NOT_INSTALLED` chuyển HJW, không chặn XONG. Native query/token limit missing = residual `NATIVE_QUERY_LIMIT=UNKNOWN` allowed if documented.

Security/Guard/footprint/rollback/client critical FAIL or UNKNOWN ⇒ DỪNG không nới phạm vi. `2-pass 1/2` periodic được ghi warning, không coi là POST PASS; POST phải sạch. Không dùng code/JEV/docs thay proof. Sau XONG chỉ nói: “Đã chặn các đường write/URL đã thử và Claude Code/Codex đọc Graph qua MCP trong phạm vi B8”, KHÔNG nói read-only tuyệt đối/JEV runtime/KB đầy đủ/agent-data+Nuxt bao phủ/Hermes đã cài.

## 13. KQ / EVIDENCE / RELEASE ROOT BUSY
Evidence run-scoped `/opt/incomex/work/graph-server/evidence/GS-R8R2-PINS-GUARDED-MCP-20261009-13/`; giữ toàn bộ lịch sử P72/P80 STOP/KQ. Ghi S0 5-file footprint path-target-rollback/Guard registry+ledger+pins, storage-watch GRAPH preflight/quota, E1 wheel/binary SHA, TEMP N1–N4/P, one-script Guard slot timing+candidate SHA/apply-v0 and auto rollback, two-file pin SHA coupling, 3 production probes, B8 temp+production MCP 13/13, wrapper binary pre-exec hash, code-ledger LOCKED/new wrapper baseline/registry, 5/5 C3 Đ31 coverage, INV22/23/status/watch Guard, Claude/Codex user scopes, no Hermes touch, 22/22/Telegram, data unchanged.
Chỉ edit Graph COLLAB/Bảng/KQ + root STARTED/Busy/KQ theo A6; E6 signpost trong COLLAB (Git, không Config Guard), không tạo file repo hoặc sửa PROMPT/view khi RUN active; không log secret/PII. Hard FAIL => revert changed targets + KQ DỪNG có exact one NEXT_TRIGGER, root busy release cùng commit, CLI đóng, không giữ terminal.
Final: `KQ@GS-R8R2-PINS-GUARDED-MCP-20261009-13 XONG|DỪNG`

