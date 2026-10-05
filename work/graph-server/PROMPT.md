# PROMPT — GS-RUN1-INFRA-20261006-01

## 0. LỆNH / PHẠM VI

RUN_ID: `GS-RUN1-INFRA-20261006-01`
Executor_Surface: Claude Code CLI
Repo: `Huyen1974/incomex-workspace` · branch `main`
Task: `work/graph-server`
Repo Write_Path: Incomex workspace gateway `workspace_*` · root `workspace`
Runtime Write_Path: terminal/SSH path hiện hữu tới VPS1; không tạo credential/gateway mới.

Đây là **RUN-1 HẠ TẦNG** của roadmap GS-RM1. Owner 06/10 yêu cầu Claude **tự hành động tối đa trong scope** vì Owner đi ngủ. Không hỏi Owner chi tiết kỹ thuật; tự kiểm, tự làm, tự verify, tự rollback phần trial khi cần. Chỉ dừng khi:
1. cổng an toàn thất bại;
2. cần đổi scope/version/component/port/quyền đã khóa;
3. cần chạm production ngoài scope;
4. cần quyết định thật sự chỉ Owner được quyết.

**KHÔNG chạy RUN-2. KHÔNG gửi dữ liệu công ty ra provider. KHÔNG gọi LLM/embedding/JEV bên ngoài trong RUN-1.**

§0.3: phải đọc lại và đối chiếu từng dòng trước mutation.

## 1. READ-GATE + READY

1. Bind đúng repo/workspace; kiểm một read của Write_Path `workspace_*`.
2. Đọc theo thứ tự:
   - `AGENTS.md`
   - BẢNG + §0 của `work/graph-server/COLLAB.md`
   - `work/graph-server/PROMPT.md`
   - `work/graph-server/view.html` §16 PLAN01/VER01/TEST01/GATE01
   - root `COLLAB.md` dòng HJW + Graph
   - phần trạng thái mới nhất P154/P155 (hoặc mới hơn) của `work/hermes-joint-workspace/COLLAB.md`
3. Xác minh:
   - `READY@<full SHA>` trong graph-server COLLAB khớp commit cuối chạm PROMPT.md;
   - không có HOLD/STOP/READY mới cho RUN này;
   - không có `STARTED@GS-RUN1-INFRA-20261006-01` chưa có KQ.
4. Gate FAIL ⇒ **0 runtime mutation**, ghi KQ DỪNG.

Ngay sau read-gate PASS, trước PRE:
- ghi `STARTED@GS-RUN1-INFRA-20261006-01 <UTC> · executor=Claude Code CLI` vào COLLAB;
- cập nhật BẢNG: RUN-1 đang chạy; không sửa mục tiêu/PLAN01.

## 2. N1 RELEASE GATE — KHÔNG CHỜ NỀN

Mục đích là tránh đè mutation chung, không chờ chữ “N1 XONG” máy móc.

Được giải phóng EXECUTION_HOLD_N1 và đi tiếp nếu fresh evidence cho thấy **phần server mutation của HJW N1 đã kết thúc**, kể cả N1 còn D2/final human test. Tối thiểu phải cùng đúng:
- trạng thái HJW mới nhất chỉ còn D2/final acceptance hoặc terminal;
- không còn executor N1 đang mutation agent-data/nginx/Lark/shared connector runtime;
- không còn busy/lease/STOP đang giữ vùng Docker/VPS dùng chung;
- root/HJW không ghi một server mutation kế tiếp đang active;
- protection/guard dùng chung không đỏ.

Nếu N1 vẫn còn server mutation thật hoặc evidence mâu thuẫn:
- không poll/chờ;
- ghi KQ DỪNG sạch với `N1_MUTATION_STILL_ACTIVE`;
- không pull image, không tạo container/network/volume/secret.

Repo đổi do task khác: re-read rồi tiếp tục nếu graph PROMPT/READY/HOLD không đổi.

## 3. PRE — CHỈ ĐỌC TRƯỚC FIRST MUTATION

Ghi toàn bộ bằng chứng vào:
`/opt/incomex/work/graph-server/evidence/GS-RUN1-INFRA-20261006-01/`

Runtime root:
`/opt/incomex/work/graph-server/runtime/run1/`

Không ghi runtime/evidence vào Git.

PRE bắt buộc:
- `docker ps`, networks, volumes, image inventory;
- RAM/swap/load; disk free/inodes;
- listener/port inventory;
- trạng thái production containers;
- guard/protection hiện hành;
- xác minh không có runtime Graph trial cũ trùng tên.

Hard gates:
- RAM available **>= 5 GB** trước cài;
- disk free **>= 30 GB** trước pull/build;
- floor toàn VPS sau mutation **>= 20 GB**;
- tổng trial disk (images + runtime + volumes + build cache + logs) **<= 10 GB**;
- không có port conflict ở `127.0.0.1:17474`, `127.0.0.1:17687`, `127.0.0.1:18080`.

Không tự tăng swap, restart Docker daemon, restart PG/Directus/Qdrant/nginx hay sửa firewall production.

Nếu hard gate fail ⇒ KQ DỪNG, 0 cài.

Trước first mutation: chạy lại DROOT30 freshness gate.

## 4. BASELINE KHÓA — KHÔNG TỰ ĐỔI

### Thành phần
- Neo4j Community: **5.26.31-community**
- APOC core: **5.26.31**
- Cognee: **1.6.1**
- Neo4j MCP: **1.6.0** chỉ khi cần cho read-only verification; không bắt buộc dựng service riêng nếu cypher-shell đủ.
- Python: **3.12** nếu artifact Cognee 1.6.1 yêu cầu runtime Python.
- Không Cognee MCP.
- Không Cognee UI.
- Không Graphiti.
- Không GDS.
- Không Hindsight.
- Không codebase-memory-mcp.
- Không PostgreSQL/pgvector profile.
- Không Qdrant integration.

RUN-1 không dùng model/provider nào.

### Artifact
Ưu tiên artifact/package/image **official, exact 1.6.1**, pin digest/lock.
Không `latest`; không `main`; không nâng lẻ dependency.
Không deploy mã Incomex từ GitHub xuống VPS.
Nếu Cognee 1.6.1 không có artifact official/immutable đủ để xác định đúng release, **DỪNG trước cài Cognee**, báo blocker; không tự clone/fork source để “cho chạy bằng được”.

Neo4j/APOC: ghi platform + image digest + checksum artifact vào KQ trước cài.

## 5. RUNTIME ISOLATION — TÊN/ĐÍCH ĐÃ KHÓA

Docker Compose project: `graph-server-trial`
Network: `graph-server-trial-net`

Container logical names:
- `graph-neo4j-trial`
- `graph-cognee-trial`

Host bindings:
- Neo4j HTTP: `127.0.0.1:17474`
- Neo4j Bolt: `127.0.0.1:17687`
- Cognee API: `127.0.0.1:18080` → map tới listen port chính thức của Cognee 1.6.1 đã xác minh từ artifact.

Memory hard limits:
- Neo4j: **1.5 GB**
  - heap: **768 MB**
  - pagecache: **256 MB**
- Cognee API: **1.5 GB**
- tổng trial <= **3 GB**

Dùng persistent paths/volumes dưới runtime root; mount đúng những path Cognee 1.6.1 thật sự cần sau khi đối chiếu artifact. Không mount Docker socket; không privileged; không mount source/secret toàn VPS.

Không expose 0.0.0.0 / public Internet.
Không reload nginx cho RUN-1.
Không thêm DNS/cert/public route.

## 6. SECRET / AUTH

Không dùng password mặc định.
Không in secret vào terminal transcript, repo, COLLAB, evidence hoặc chat.

Neo4j:
- auth ON;
- generate secret trial ngẫu nhiên;
- lưu bằng secret mechanism hiện hữu nếu có; nếu không, trial-only env file dưới runtime root, mode 600, không commit.

Cognee target config:
- `GRAPH_DATABASE_PROVIDER=neo4j`
- `ENABLE_BACKEND_ACCESS_CONTROL=false`
- `REQUIRE_AUTHENTICATION=true`
- metadata/vector backend chỉ theo baseline Cognee 1.6.1; không mở PG/Qdrant.

Runtime Cognee phải không nhận OpenAI/provider key trong RUN-1.
Nếu có thể, đặt runtime network/egress sao cho API không thể gọi inference provider; pull/install phase tách khỏi runtime phase.

## 7. CÀI / KHỞI ĐỘNG

Chỉ sau toàn bộ gate PASS:
1. tạo runtime dirs + manifest cấu hình;
2. pull/install exact artifacts;
3. xác minh digest/version trước start;
4. start Neo4j trial;
5. kiểm health/auth/loopback;
6. start Cognee API trial với Neo4j provider + auth bắt buộc;
7. không bật component khác.

Không sửa production Docker compose/project/network.

Nếu một lỗi kỹ thuật thông thường nằm trong scope:
- tự đọc log/source exact release;
- sửa cấu hình nhỏ nhất;
- retry hữu hạn;
- ghi before/after.
Không hỏi Owner.

Nếu sửa đòi đổi version/component/public exposure/production service ⇒ DỪNG.

## 8. TEST RUN-1

### T19 · Security
Chứng minh:
- no token → reject;
- wrong token → reject;
- valid token → chỉ operation được phép;
- không có public listener;
- không default credential;
- hidden/alternate write path không bypass auth;
- direct Neo4j write credential không được giao cho agent surface;
- before/after graph không đổi sau negative probes.

### K1 · Backend thật
Chứng minh:
- runtime provider = Neo4j;
- Neo4j có fixture node/edge;
- không có runtime graph ở Ladybug/Kuzu;
- cấu hình chỉ tới trial Neo4j.

Không gọi LLM để tạo fixture.
Dùng structured/synthetic path hoặc graph adapter chính thức không cần inference. Nếu Cognee path bắt buộc embedding/provider cho thao tác đó, ghi CHƯA KIỂM phần write-via-Cognee; vẫn phải chứng minh provider/config Neo4j.

### Persistence
- tạo fixture tổng hợp, không PII;
- restart trial containers → fixture còn;
- recreate trial containers với cùng persistent data → fixture còn.

### K4 · Cognee-off
- stop Cognee trial;
- Neo4j vẫn đọc/query/export được fixture qua đường độc lập.

### Dump/restore
- tạo dump/backup Neo4j trial;
- stop original trial services nếu cần;
- restore vào **fresh isolated restore-check volume/container** cùng version, không ghi đè production;
- verify fixture bằng query;
- giữ backup/evidence.
Không cần chạy original + restore-check Neo4j đồng thời nếu vượt RAM cap.

### T18 construction — synthetic only
Dùng code/package Cognee 1.6.1, **không LLM call**, để kiểm hành vi identity tối thiểu:
- hai chunk/tài liệu có cùng tên nhưng là hai thực thể khác;
- cùng source-id qua ingest lặp;
- thiếu ID.
Nếu default construction có nguy cơ gộp cùng tên như PLAN01 dự đoán:
- ghi `T18=PARTIAL/BLOCKER_FOR_IDENTITY_DATA`;
- không cố fork Cognee;
- RUN-1 hạ tầng vẫn có thể XONG nếu các gate an toàn khác PASS;
- RUN-2 bắt buộc có mitigation dữ liệu/ID được Host review trước nạp.

### Resource
Trong chạy:
- RAM available < **2 GB** ⇒ dừng chỉ trial containers, KQ DỪNG;
- disk free < **20 GB** hoặc trial footprint > **10 GB** ⇒ dừng/rollback trial;
- production health suy giảm so PRE ⇒ dừng trial + verify production phục hồi.

## 9. ROLLBACK

Mọi artifact tạo mới phải có nhãn RUN_ID.

Nếu FAIL sau mutation:
- stop/remove chỉ trial containers/network được tạo bởi RUN;
- không xóa evidence/backup;
- không xóa dữ liệu production;
- cleanup trial image/cache chỉ khi chính RUN này kéo/tạo và cần để phục hồi disk floor;
- verify production containers/guard trở lại PRE state;
- ghi KQ DỪNG + blocker.

Không “sửa production để trial chạy”.

## 10. KQ / REPO

Evidence chi tiết ở VPS path đã nêu.
Repo chỉ ghi summary vào `work/graph-server/COLLAB.md`; không tạo progress/evidence file Git mới.

Kết thúc bắt buộc:
- cập nhật BẢNG cùng commit KQ;
- ghi `KQ@GS-RUN1-INFRA-20261006-01 XONG|DỪNG`;
- tóm tắt version/digest, PRE resources, ports, tests, footprint, rollback status, blocker cho RUN-2;
- commit qua workspace gateway với tiền tố:
  `[Claude Code] GS-RUN1-INFRA-20261006-01 · graph-server · <XONG|DỪNG>`

`XONG` chỉ khi:
- N1 release gate an toàn;
- security/auth/network PASS;
- resource gates PASS;
- Neo4j backend + persistence + dump/restore + Cognee-off PASS;
- production không suy giảm;
- mọi PARTIAL (ví dụ T18 identity) được ghi rõ thành gate RUN-2, không bị giấu.

**Không soạn/chạy RUN-2 trong cùng lượt.**

## 11. TỰ HÀNH ĐỘNG / KHÔNG ĐÁNH THỨC OWNER

Owner đi ngủ. Áp DROOT42 + DROOT43:
- tự xử hết kỹ thuật nằm trong scope;
- không nhắn hỏi Owner về command, Docker, port, secret, retry, log, cấu hình;
- không giữ terminal chỉ để chờ N1/Owner;
- nếu đến bước thật sự ngoài scope hoặc cần Owner → checkpoint + KQ DỪNG sạch;
- không tạo waiter/poll nền.

Cuối cùng trả đúng một dòng cho Owner:
`XONG · GS-RUN1-INFRA-20261006-01 · <commit>`
hoặc
`DỪNG · GS-RUN1-INFRA-20261006-01 · <blocker ngắn> · <commit>`
