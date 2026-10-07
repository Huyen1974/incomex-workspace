# PROMPT — GS-R7-PROD-CLEAN-BUILD-20261007-10

## 0. STATUS / AUTHORITY
RUN_ID: GS-R7-PROD-CLEAN-BUILD-20261007-10
Executor_Surface: Claude Code CLI
Repo Write_Path: Incomex workspace gateway workspace_* · root workspace
Runtime target: VPS1 production
Status: DRAFT · NO READY · NO RUN

Production rule:
Host sửa PROMPT -> Reviewer ACCEPT đúng full SHA của PROMPT -> Owner nói CHO CHẠY R7 -> Host ghi OWNER_RELEASE + READY cùng SHA -> Agent mới được STARTED.
D14 chỉ cho tự quyết trial nhỏ; không dùng D14 để bỏ Reviewer hoặc Owner gate của production.
Thiếu một gate => DỪNG trước mutation.

Scope Host đã chốt mặc định: R7-1..R7-6 = GẬT theo P55/P56/P57, trừ khi Owner phản đối rõ.

## 1. MỤC TIÊU
Dựng Graph production v1 sạch, không dùng trial volume/data snapshot làm production seed.

Lane S · SYSTEM/CODE:
- PostgreSQL native trigger relations;
- live DOT command existence;
- DOT registry declarations;
- code trees vượt B2-B4.

Lane B · BUSINESS STRUCTURED:
- CANDIDATE_FOR_ORDER
- SELECTED_FOR_ORDER
- ORDER_MANAGED_BY_UNION
- ORDER_FOR_COMPANY
Chỉ active khi Owner release gồm R7-2=GẬT và B6 PASS.

Không thuộc v1:
- KB cũ;
- care/chat free text;
- body-inferred PG/DOT relations;
- Nuxt auto-import/generated/runtime ngoài v0.4;
- JEV/LLM runtime.

## 2. PRODUCTION FOOTPRINT CỐ ĐỊNH
Không để executor tự chọn.

Install root:
- /opt/incomex/graph-server/prod-v1
- compose: /opt/incomex/graph-server/prod-v1/compose.yaml
- backups/exports: /opt/incomex/graph-server/prod-v1/backups
- rollback script: /opt/incomex/graph-server/prod-v1/rollback-r7.sh

Compose project:
- incomex-graph-v1

Resident service duy nhất:
- container: incomex-graph-neo4j
- image: neo4j:5.26.31-community
- image digest phải khớp digest đã đo RUN-1: sha256:d9cfe82983d27f5a75b3aaae8f316d04f9a698a3b7f6103a508f7caf8362f255
- APOC core 5.26.31 chỉ dùng bản đã checksum-match RUN-1
- volume: incomex_graph_v1_data
- networks: incomex_graph_v1_local + incomex_graph_v1_build
- restart: unless-stopped
- database duy nhất: neo4j

Host ports:
- 127.0.0.1:17474 -> 7474
- 127.0.0.1:17687 -> 7687
- không nginx
- không bind 0.0.0.0
- không port Cognee/Enola

Builder:
- Cognee 1.6.1 image digest sha256:db0973f4b913d73daa4061bc19362cde6edc59d1be8243b6667fade364b06428 khi code pipeline cần;
- Enola 0.4.21;
- builder chỉ tạm thời trong build network, không host port, tắt/gỡ sau code load;
- 0 provider key, 0 LLM/JEV call.

Neo4j memory:
- mem_limit 1536 MiB
- memswap_limit = mem_limit
- heap 768 MiB
- pagecache 256 MiB

Builder memory:
- tổng builder thêm tối đa 1536 MiB;
- memswap = mem.

PRE resource gate:
- MemAvailable >= 5 GiB;
- disk free >= 30 GiB;
- swap free >= 256 MiB;
- ports 17474/17687 phải trống;
- install root chưa tồn tại hoặc phải có marker đúng RUN cũ đã được Host cho tiếp tục; nếu lạ => DỪNG.
Trong build:
- disk free không dưới 20 GiB;
- nếu MemAvailable < 2 GiB hoặc swap free < 128 MiB: stop builder ngay, không mutation tiếp;
- bất kỳ production container cũ restart/health xấu hơn PRE do R7 => DỪNG + rollback R7 footprint.

## 3. NEO4J SECRET
Secret ID cố định: graph-server-neo4j-password trong Google Secret Manager.

- Nếu secret có latest enabled version: dùng version đó.
- Nếu secret chưa tồn tại: sau Owner release được tạo đúng secret ID này và đúng một version random 32-byte/hex qua đường GSM hiện hữu.
- không in value;
- không ghi value vào repo/evidence/log/argv;
- chỉ ghi secret ID + version metadata;
- dùng protected transient file dưới /run, mode 600, rồi xoá ngay sau compose start.
Nếu không truy cập GSM hoặc secret state ambiguous => DỪNG trước Neo4j start.
Không dùng neo4j/pleaseletmein.

## 4. READ GATE / STARTED
Đọc:
1. AGENTS.md, đặc biệt A9 và R4 AUTO-PROTECT;
2. Bảng/§0/P55-P59;
3. PROMPT này;
4. root COLLAB;
5. view roadmap.

Bắt buộc:
- Reviewer ACCEPT đúng full SHA commit cuối chạm PROMPT;
- OWNER_RELEASE@GS-R7-PROD-CLEAN-BUILD-20261007-10 có đủ 1G-6G + 3 private paths;
- READY@same-full-SHA;
- không HOLD/STOP/STARTED chưa KQ.

PASS -> ghi STARTED rồi PRE.
Trước first runtime mutation lặp DROOT30 freshness gate.

## 5. STEP_WALK_V1
| Bước | Ai | Trigger | SLA | Evidence | Hỏng thì ai biết | Kế |
|---|---|---|---|---|---|---|
| S0 PRE | Agent | STARTED | cùng RUN, không chờ | resources/ports/prod fingerprint/GSM metadata | Host qua KQ DỪNG | B1 |
| B1 Manifest v1.1 | Agent | PRE PASS | trước ingest | manifest+hash | Host | B2 |
| B2 Runtime identity | Agent | B1 | trước file set | service/image/root/hash proof | Host | B3 |
| B3 File whitelist | Agent | B2 | trước oracle | exact list+hash | Host | B4 |
| B4 Code oracle | Agent | B3 | trước graph load | fresh oracle metrics | Host | B5 |
| B5 PG/DOT capture | Agent | B4 | trước load | frozen snapshots+set oracle | Host | B6 |
| B6 Base88 | Agent | B5 | trước business load | metadata gate+export hash+edge oracle | Host | B7 |
| B7 Identity | Agent | active inputs frozen | trước load/finalize | constraints/collision report | Host | BUILD |
| BUILD | Agent | B1-B7 lane gates | một mạch | compose/load receipts | Host | B8 |
| B8 Acceptance | Agent | build complete | trước cleanup | Q/A/export/restore/health | Host+Reviewer | POST-PROTECT |
| POST-PROTECT | Agent | B8 PASS | trước KQ XONG | R4 coverage+Telegram proof | Owner+Host | private cleanup/KQ |

Không có polling/chờ người trong RUN.

## 6. B1 · MANIFEST v1.1
Dùng frozen R6E inventory + final policy:
5 KEEP / 31 ARCHIVE / 7 DELETE-CANDIDATE / 15 RECHECK.

Materialize production-source-manifest-v1.1 + SHA256 trước ingest.
Không rewrite P53 evidence.
RECHECK chỉ nâng khi B2/B5/B6 sinh evidence mới.
Mỗi admitted source phải có capture method, trust contract, exact file/snapshot hash, provenance.

## 7. B2 · ĐÚNG 5 CODE TREES
Chỉ xét:
1. /opt/incomex/docker/agent-data-repo
2. /opt/incomex/claude-mcp
3. /opt/incomex/claude-kb
4. /opt/incomex/lark-client  — loại .venv
5. /opt/incomex/docker/nuxt-repo/web

/opt/incomex/scripts đứng ngoài v1 vì dirty ở R6E.

B2 áp cho cả 5, không miễn tree đang KEEP.

Python image-built service:
- prove deploy/service/image gắn đúng root;
- nếu source files tồn tại trong container/image, so hash với approved git snapshot;
- image name/date/branch không đủ bằng chứng;
- không đủ material => tree OUT/RECHECK.

Nuxt:
- prove deployment/build config trỏ đúng nuxt-repo/web;
- nếu có build stamp/source commit thì bind;
- nếu không có, running build == HEAD = UNKNOWN; chỉ source tree được xét cho build khi B3/B4 PASS, không tuyên bố runtime == HEAD.

## 8. B3 · SOURCE FILE WHITELIST
Không ingest whole repo.

Python:
- chỉ tracked first-party files có đuôi .py.

Nuxt:
- chỉ tracked first-party .ts và .vue.

Exclude directories:
.git, .venv, venv, site-packages, node_modules, .nuxt, .output, node-compile-cache, build, dist, tmp, cache, vendor/generated tương đương.

Không dùng regex tên backup làm cách chính để cho vào.
Không xoá file.
Freeze exact relative file list + per-file SHA256 + aggregate hash.
Ghi counts bị loại theo reason.

## 9. B4 · FRESH ORACLE
Python:
- R6A-style independent AST oracle trên đúng B3 set của từng admitted tree;
- không copy score trial;
- trust v0.3 limits giữ nguyên.

TS/Vue:
- TypeScript 5.9.3 + @vue/compiler-sfc 3.5.25;
- oracle trên đúng B3 set;
- explicit static import/export-from;
- directory->target exact gate;
- raw file-level facts giữ riêng;
- auto-import/dynamic/generated/runtime = UNKNOWN.

Oracle unavailable => tree OUT; không install package để cứu.

## 10. B5 · PG/DOT FRESH CAPTURE
Re-run đúng R6D read-only contract.
PG native trigger catalog = truth trong measured scope.
DOT disk + 00-SO-DOT.tsv = command existence truth.
dot_tools = DECLARED only.
Freeze/hash trước load.
0 extra/0 missing theo exact identity/set gates.
FK/view không vào v1 mặc định.

## 11. B6 · BASE88 — CHỈ 11 FIELD IDs
Chỉ nếu Owner release có R7-2=GẬT.

Tables:
- Đơn hàng: tblh7nrQpK8TqIs2
- Thực tập sinh: tblKnzaih6154r2e
- Nghiệp đoàn: tblG18kR9aFhWrJW
- Xí nghiệp: tblqFRpClTG0OCjE

Allowed fields, đúng 11:
Đơn hàng:
- fldQ7ZT2Ui  Mã đơn hàng
- fldsNJFiHT  tiến cử
- fldxYn8vJL  trúng tuyển
- fldurWDSGm  nghiệp đoàn
- fldhKyCARN  xí nghiệp

Thực tập sinh:
- fldPTsPOxl  reverse tiến cử
- fldm9OBbrp  reverse trúng tuyển

Nghiệp đoàn:
- fldt9VGyvm  Mã Nghiệp đoàn
- fldhRnmjCa  reverse đơn hàng

Xí nghiệp:
- fldNME4A3o  Mã Xí Nghiệp
- fldu9SLrpg  reverse đơn hàng

Cấm đọc bất kỳ field khác.

Trước record read:
- metadata-check đủ đúng 11 field IDs, đúng table, đúng expected kind: code field phải scalar/auto-number compatible; relation field phải link-compatible;
- lệch một field => BUSINESS_LANE_BLOCKED, không dò field thay thế.

Payload:
- TTS/person node: record_id only;
- order/union/company: record_id + allowed business code;
- không tên người, mã TTS, contact, phone/email/address, note/free-text.

Trước load:
- export chỉ whitelist columns;
- leak scan: schema columns ngoài whitelist = 0; phone/email/document/free-text field = 0;
- reverse-link symmetry phải khớp;
- freeze node/edge sets + hash + UTC.

Approved catalog v1.0:
CANDIDATE_FOR_ORDER
SELECTED_FOR_ORDER
ORDER_MANAGED_BY_UNION
ORDER_FOR_COMPANY

Post-load graph set = export set, 0 extra/0 missing.
Fail => Lane B OUT; Lane S tiếp tục.
0 LLM/JEV.

## 12. B7 · ONE DATABASE / IDENTITY
Neo4j Community chỉ dùng database neo4j.

Load order:
1. tạo constraints/namespace;
2. code load bằng Enola/Cognee trên B3/B4 admitted sets;
3. giữ raw Enola facts.jsonl theo từng tree + hash;
4. sau code phase tắt/gỡ Cognee/Enola builder;
5. từ thời điểm code load đầu tiên trở đi: cấm Cognee prune/reset/delete/forget/recreate database;
6. LOAD CSV/Cypher PG/DOT;
7. LOAD CSV/Cypher Base88 nếu B6 PASS.

Node IDs class-prefixed + deterministic.
0 collision across code/PG/DOT/Base88.
0 same admitted file hash ở hai code trees nếu không có explicit justification.
Mỗi imported relation có provenance.

## 13. BUILD / ROLLBACK
Chỉ build lane đã PASS B1-B7.

Neo4j resident dùng footprint §2.
Không expose Cognee.
0 provider traffic.

Rollback trigger:
- B8 fail;
- POST-PROTECT fail;
- old production services regress because of R7;
- resource floor breached after mutation và không hồi khi stop builder.

Rollback exact R7 footprint:
- stop/remove builder;
- docker compose project incomex-graph-v1 down;
- remove only container/network/volume created by this RUN: incomex-graph-neo4j, incomex_graph_v1_data, incomex_graph_v1_local, incomex_graph_v1_build;
- remove install root /opt/incomex/graph-server/prod-v1 only when marker RUN_ID matches this RUN;
- ports 17474/17687 phải đóng;
- secret version created by this RUN: disable version; không in value;
- verify all PRE-existing container IDs/restarts/health/ports unchanged;
- keep evidence under work/graph-server/evidence.

Không chạm trial data trong rollback.

## 14. B8 · ACCEPTANCE TỐI THIỂU
Precompute oracle answers trước graph query.

Mỗi active layer tối thiểu 3 câu, trong đó ít nhất 1 câu bắt buộc trả UNKNOWN_FROM_GRAPH:

Python:
- exact import/dependency;
- exact declaration/navigation;
- UNKNOWN cho runtime/dynamic call ngoài trust.

TS/Vue nếu admitted:
- explicit import target;
- directory dependency;
- UNKNOWN auto-import/runtime/generated.

PG:
- trigger -> table;
- trigger -> function/enabled;
- UNKNOWN function body reads/writes.

DOT:
- command existence;
- registry DECLARED relation;
- UNKNOWN script body/table/DOT calls.

Base88 nếu active:
- exact relation query;
- reverse relation/cardinality query;
- UNKNOWN free-text/contact/reason not ingested.

Ngoài ra:
- trust wording đúng v0.3/v0.4/v0.5;
- KB NOT_IN_V1;
- care/chat NO_SOURCE;
- JEV/LLM not runtime.

Cognee-off survivability:
- stop builder/Cognee;
- Neo4j query works;
- export/backup;
- restore into fresh isolated Neo4j;
- deterministic key/count checks match.

Production health:
- Neo4j healthy;
- loopback ports only;
- external scan ports closed;
- source systems unchanged;
- resources above floors;
- 0 provider/model traffic.

## 15. POST-PROTECT — AGENTS R4
Bắt buộc trước KQ XONG.

Coverage PRE->POST trên footprint thật, mỗi row phải có:
1. Điều 30 regression hành vi;
2. Điều 31 integrity/drift/runtime;
3. watchdog/self-check;
4. rollback/known-good.

Required protection rows:
- Neo4j container/service health;
- loopback 17687 TCP + authenticated RETURN 1 local probe;
- port exposure invariant: 17474/17687 loopback only, 0 public;
- compose/image/manifest v1.1 hash drift;
- graph key/count/source snapshot invariants;
- rollback-r7.sh exact-path guard + dry-run proof.

Đăng ký service mới vào registry theo dõi/Guard hiện hữu; không tạo bot/timer mới.
Nếu existing Guard không thể monitor các invariant trên => rollback R7, KQ PARTIAL/BLOCKED.

Telegram receipt bắt buộc:
- dùng sender hiện hữu;
- tối đa 3 dòng tiếng Việt;
- nêu vừa cài/kiểm gì · trạng thái protection/rollback · RUN/commit ngắn;
- lưu message_id/delivery proof.
Không gửi được => rollback hoặc KQ PARTIAL/BLOCKED; không XONG.

## 16. PRIVATE CLEANUP TRONG R7
Broad trial wipe KHÔNG thuộc RUN này.

Chỉ được xoá đúng 3 paths nếu OWNER_RELEASE ghi đủ:
- /opt/incomex/work/graph-server/runtime/r5/private
- /opt/incomex/work/graph-server/runtime/r6b/private
- /opt/incomex/work/graph-server/runtime/r6b0/private

Chỉ sau B8 + POST-PROTECT PASS.

Trước xoá:
- path phải nằm đúng runtime graph-server;
- không symlink;
- dry-run phải in đúng 3 path;
- fingerprint phải khớp frozen R6E post/private-fingerprint.tsv;
- mỗi directory đúng 2 files như frozen evidence.
Lệch => KHÔNG XOÁ, ghi residual; không tự sửa.

Không wipe runtime/volumes trial khác.
Broad cleanup chỉ sau Host+Reviewer nghiệm thu R7 và Owner nói riêng.

## 17. R8 NOT IN R7
Cài xong R7, agent CHƯA có đường đọc graph.

Mốc kế tiếp sau R7 acceptance:
R8 · AGENT READ-ONLY GATE
- thử nhỏ Neo4j MCP chính hãng;
- NEO4J_READ_ONLY=true;
- chỉ read-cypher/get-schema;
- chứng minh không write;
- rồi mới cài cho agent.

R7 KQ phải ghi rõ: AGENT_READ_PATH=NOT_INSTALLED.

## 18. KQ
Evidence:
/opt/incomex/work/graph-server/evidence/GS-R7-PROD-CLEAN-BUILD-20261007-10/

KQ ghi:
- Owner release;
- Reviewer ACCEPT SHA + READY SHA;
- PRE/POST;
- B1-B8;
- admitted code trees + B3 hashes;
- manifest v1.1 hash;
- PG/DOT snapshots;
- Base88 snapshot nếu active;
- graph counts;
- B8 questions;
- export/restore;
- POST-PROTECT coverage;
- Telegram message_id;
- exact private cleanup receipts/residual;
- AGENT_READ_PATH=NOT_INSTALLED;
- residual UNKNOWNs.

KQ XONG chỉ khi B8 + POST-PROTECT PASS.
Nếu lane B fail nhưng Lane S PASS: KQ phải ghi PARTIAL/BUSINESS_LANE_BLOCKED; Host/Reviewer quyết có ACCEPT phần system hay rollback toàn R7. Agent không tự gọi XONG đầy đủ.

## 19. AUTONOMY
Sau Reviewer ACCEPT + OWNER_RELEASE + READY:
- Claude tự chạy một mạch;
- không hỏi Owner kỹ thuật;
- không chờ/poll;
- không đổi port/path/secret ID/tree/field list;
- không nới gate;
- fail closed;
- một KQ cuối.

Trước đủ 3 gate:
- NO STARTED;
- NO production mutation;
- NO cleanup.
