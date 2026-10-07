# PROMPT — GS-R7-PROD-CLEAN-BUILD-20261007-10

## 0. STATUS
RUN_ID: GS-R7-PROD-CLEAN-BUILD-20261007-10
Status: DRAFT · NO READY · NO RUN UNTIL OWNER RELEASE

Host design decision P57:
- mặc định phương án R7 = GẬT cả 6 lựa chọn đã hội tụ ở P55/P56;
- đây là quyết định điều hành/design của Host, chưa phải quyền mutation production;
- trước STARTED bắt buộc có OWNER_RELEASE và READY theo full SHA commit cuối chạm PROMPT.

## 1. GOAL
Dựng Graph production v1 sạch, không reuse trial graph/data snapshot làm production seed.

Lane S · SYSTEM/CODE:
- PostgreSQL native trigger relations;
- live DOT command existence;
- DOT registry declarations;
- code trees vượt qua runtime identity + source-set + oracle gates.

Lane B · BUSINESS STRUCTURED, chỉ nếu Owner release giữ R7-2=GẬT:
- CANDIDATE_FOR_ORDER
- SELECTED_FOR_ORDER
- ORDER_MANAGED_BY_UNION
- ORDER_FOR_COMPANY

Không thuộc v1:
- KB cũ;
- care/chat free text;
- function/script body inferred relations;
- Nuxt auto-import/runtime/generated ngoài trust scope;
- JEV/LLM runtime.

## 2. OWNER RELEASE GATE
Trước STARTED:
1. đọc AGENTS.md, BẢNG/§0/P55–P57 và PROMPT này;
2. phải có OWNER_RELEASE@GS-R7-PROD-CLEAN-BUILD-20261007-10 do Host ghi sau Owner approval;
3. READY full SHA phải đúng commit cuối chạm PROMPT;
4. không HOLD/STOP/STARTED chưa KQ.

Thiếu OWNER_RELEASE hoặc READY => DỪNG trước mọi mutation.

## 3. SAFETY
- preserve-by-default;
- không sửa PG/Directus/Lark/code source để cứu gate;
- không delete/archive source systems;
- không LLM/JEV/provider calls;
- không nới gate sau khi thấy số;
- lane fail thì fail-closed, không phá lane khác.

## 4. B1 · MANIFEST v1.1
Dùng frozen R6E inventory + policy final P55/P56: 5 KEEP / 31 ARCHIVE / 7 DELETE-CANDIDATE / 15 RECHECK.
Materialize production-source-manifest-v1.1 + SHA256 trước ingest.
Không rewrite evidence P53.
RECHECK chỉ được nâng nếu B2/B5/B6 sinh bằng chứng mới.
Mỗi dòng phải trỏ exact capture method, trust contract, file-set hash và provenance.

## 5. B2 · RUNTIME IDENTITY CHO MỌI CODE TREE
Áp cho agent-data-repo, claude-mcp, claude-kb, Nuxt web và mọi tree muốn vào v1.

Python image-built service:
- chứng minh deploy/service gắn đúng source root;
- so hash source trong container/image với approved source snapshot khi material tồn tại;
- không đủ material => RECHECK/OUT, không suy từ image name/date/branch.

Nuxt:
- chứng minh deploy/build path thuộc đúng nuxt-repo/web;
- nếu có build stamp/source commit thì bind;
- nếu không, running build == HEAD giữ UNKNOWN.

## 6. B3 · EXACT SOURCE FILE SET
Không ingest whole repo.

Python:
- chỉ tracked first-party *.py trong approved root.

TS/Vue:
- chỉ tracked first-party *.ts và *.vue trong approved Nuxt root.

Loại generated/vendor/cache:
.git, .venv, venv, site-packages, node_modules, .nuxt, .output, node-compile-cache, build/dist/tmp/cache và tương đương.
Không xoá file.
Freeze exact relative file list + per-file SHA256 + aggregate hash.

## 7. B4 · ORACLE TRÊN ĐÚNG B3 SET
Python:
- chạy R6A-style independent AST oracle trên từng admitted Python tree;
- không copy 88/88 hay 99/99 từ trial.

TS/Vue:
- TypeScript 5.9.3 + @vue/compiler-sfc 3.5.25;
- explicit static import/export-from;
- canonical exact gate ở directory→target;
- file-level/auto-import/dynamic/generated giữ limits v0.4.

Nếu oracle unavailable => affected tree OUT, không cài package để cứu.

## 8. B5 · PG / DOT FRESH CAPTURE
Re-run R6D-style read-only capture.
PG native trigger catalog = source truth trong measured scope.
DOT disk = command existence truth.
dot_tools = DECLARED only.
Freeze/hash trước load.
Re-run exact identity/set/provenance gates.
FK/view không thêm mặc định; chỉ thêm nếu Host explicit và có R6D-style exact gate.

## 9. B6 · BASE88 STRUCTURED BUSINESS, CONDITIONAL
Chỉ nếu OWNER_RELEASE có R7-2=GẬT.

Read-only bằng đường Lark hiện hữu.
Chỉ đọc:
- exact link fields cho 4 relations;
- record IDs;
- business code của order/union/company nếu có.

Không ingest:
- tên người;
- contact;
- free text;
- notes;
- phone/email/address;
- field ngoài scope.

Identity:
- person/TTS = table + record_id only;
- order/union/company = table + record_id canonical key + business code property.

Pre-load:
- export exact node/edge sets;
- freeze/hash;
- reverse-link symmetry nếu nguồn có hai chiều.

Post-load:
- graph edge set = export edge set;
- 0 extra / 0 missing;
- each edge có provenance + snapshot UTC.

B6 fail => Lane B OUT; Lane S vẫn tiếp tục.
Không LLM/JEV.

## 10. B7 · IDENTITY / COLLISION
- mỗi node ID class-prefixed + deterministic;
- 0 key collision across PG/DOT/code/Base88;
- cùng file hash không được nằm trong hai admitted code trees nếu không có explicit justification;
- mọi imported relation family có provenance.

## 11. BUILD
Chỉ sau B1–B7 PASS cho lane tương ứng mới dựng production graph.

Baseline:
- Neo4j Community 5.26.31
- APOC core 5.26.31 khi cần
- Cognee 1.6.1 chỉ ở pipeline code đã duyệt
- Enola 0.4.21 cho code supported
- 0 model/provider call.

Production phải rebuild được từ manifest/captures.
Trial volumes không làm production seed.

## 12. B8 · FINAL ACCEPTANCE
A. Precompute oracle answers rồi mới hỏi graph.
Phủ:
- Python imports/dependency từ mỗi admitted tree;
- TS/Vue explicit imports;
- PG triggers;
- DOT existence/DECLARED;
- Base88 4 relations nếu Lane B active;
- UNKNOWN questions cho body/runtime/free-text gaps.

B. Trust honesty:
- giữ đúng v0.3/v0.4/v0.5 limits;
- Base88 chỉ exact structured snapshot;
- KB NOT_IN_V1;
- care/chat NO_SOURCE;
- JEV/LLM not active runtime.

C. Cognee-off survivability:
- canonical Neo4j vẫn query/export được khi Cognee stopped;
- backup/export;
- restore vào fresh isolated Neo4j;
- key/count checks match.

D. Production health:
- health/resources;
- no unintended public exposure;
- no source mutation;
- no model/provider traffic.

## 13. CLEANUP ORDER
Nếu OWNER_RELEASE có R7-6=GẬT:

Có thể xoá sớm đúng 3 private paths sau exact dry-run/path guard:
- runtime/r5/private
- runtime/r6b/private
- runtime/r6b0/private

Không xoá broad trial trước B8 PASS.

Sau B8 PASS:
- wipe approved trial runtime/Neo4j/pgvector volumes bằng existing wipe scripts;
- evidence giữ ARCHIVE;
- không xoá source/code/KB/Lark data.

B8 fail => giữ trial rollback/evidence, không broad-clean.

## 14. OWNER DECISIONS ENCODED
OWNER_RELEASE phải encode:
R7-1 install code/system v1;
R7-2 Base88 structured lane;
R7-3 exclude old KB;
R7-4 KB cleanup separate/archive-index-first;
R7-5 care/chat post-R7 source task;
R7-6 cleanup order/private paths.

## 15. KQ
Evidence path:
/opt/incomex/work/graph-server/evidence/GS-R7-PROD-CLEAN-BUILD-20261007-10/

KQ repo phải ghi:
- Owner release;
- B1–B8;
- manifest v1.1 hash;
- admitted code roots + B3 hashes;
- PG/DOT snapshot hashes;
- Base88 hash nếu active;
- graph counts;
- acceptance Q/A;
- Cognee-off export/restore;
- cleanup receipts;
- residual UNKNOWNs.

Final:
KQ@GS-R7-PROD-CLEAN-BUILD-20261007-10 XONG|DỪNG

## 16. AUTONOMY
Sau OWNER_RELEASE + READY:
- Claude tự chạy B1–B8;
- không hỏi Owner kỹ thuật;
- fail-closed;
- không nới gate;
- một KQ cuối.

Trước OWNER_RELEASE:
- NO STARTED;
- NO production mutation;
- NO cleanup.
