# PROMPT — GS-R6A-CODE-TRUST-20261006-04

## 0. LỆNH / PHẠM VI

RUN_ID: `GS-R6A-CODE-TRUST-20261006-04`
Executor_Surface: Claude Code CLI
Repo: `Huyen1974/incomex-workspace` · branch `main`
Task: `work/graph-server`
Repo Write_Path: Incomex workspace gateway `workspace_*` · root `workspace`
Runtime Write_Path: terminal/SSH hiện hữu tới VPS1.

Owner đã ủy quyền trial nhỏ cho GPT + Claude; chỉ production/quy mô thật mới xin phép.

ĐÂY LÀ R6A RẤT HẸP:
- chỉ kiểm độ tin của file-level import/dependency trên đúng corpus R4;
- chỉ bật Neo4j bằng volume R4 đang giữ;
- 0 Cognee, 0 PGVector, 0 OpenAI, 0 JEV, 0 Lark, 0 KB;
- không trích xuất lại code;
- không sản phẩm dự phòng;
- không custom parser;
- không tạo graph engine hay pipeline mới.

§0.3: đọc/đối chiếu toàn bộ trước mutation.

## 1. READ-GATE

Đọc:
1. `AGENTS.md`
2. BẢNG + §0 + D15 + P29–P32 trong `work/graph-server/COLLAB.md`
3. `work/graph-server/PROMPT.md`
4. `work/graph-server/view.html` roadmap hiện hành
5. root `COLLAB.md` dòng Graph.

Xác minh READY full SHA khớp commit cuối chạm PROMPT; không HOLD/STOP/READY mới; không STARTED cùng RUN chưa có KQ.

PASS → ghi:
`STARTED@GS-R6A-CODE-TRUST-20261006-04 <UTC> · executor=Claude Code CLI`

FAIL → 0 runtime mutation, KQ DỪNG.

Trước first runtime mutation: DROOT30 freshness gate.

## 2. NGUỒN / ORACLE KHÓA

R4 evidence:
`/opt/incomex/work/graph-server/evidence/GS-R4-CODE-FIRST-20261006-02/`

R4 runtime:
`/opt/incomex/work/graph-server/runtime/run1/`

Dùng đúng `MANIFEST-R4.md`, `compose.r4.yaml`, retained Neo4j R4 data volume và đúng R4 source snapshot:
`/opt/incomex/dot/iu-cutter-v0.6/cutter_agent/orchestrator/` (+ `phases/` đã có trong R4 sample).

Oracle = Python stdlib `ast` deterministic trên đúng source snapshot/hash R4. Không AI/reviewer làm oracle.

PRE:
- hash/source path khớp R4 evidence;
- production containers/health/ports + Qdrant/PG status read-only;
- nếu R4 volume/source drift ⇒ DỪNG `R4_STATE_MISSING_OR_DRIFTED`.

## 3. CHỈ BẬT NEO4J R4

Dùng đúng Neo4j Community 5.26.31 + retained R4 data volume/config/auth.
Chỉ start Neo4j từ R4 compose/manifest.
Không Cognee/pgvector.
Không pull image.
Không public port mới.
Dùng docker exec/cypher-shell hoặc loopback port R4 hiện hữu.
0 outbound network calls.

## 4. MỘT GRAPH DATA QUERY DUY NHẤT

Trước query, đọc evidence/export R4 đã có để xác nhận label/property shape của dependency node; không chạy chuỗi query dò schema.

Sau đó chạy **một Cypher data query duy nhất** lấy toàn bộ dependency nodes cần cho bài test, tối thiểu:
- source file path;
- dependency target text/name;
- source line;
- provenance/node id nếu có.

Không query lần hai để sửa đáp án.
Hai câu hỏi mẫu ở §6 phải trả lời từ cùng result set này.

## 5. NORMALIZE / ORACLE COMPARE

Từ result set:
- lấy relative imports trong package;
- normalize relative module → target file path theo Python package semantics;
- không LLM;
- không source parser mới.

Oracle:
- Python stdlib `ast` như R4;
- pair key = `(source_file,target_file/module)`;
- duplicate statements cùng pair không thành extra pair;
- line metadata graph phải là line hợp lệ của pair.

Expected P31:
- 89 relative import statements;
- **88 unique pairs**.

Nếu AST snapshot hiện tại không ra 88 unique pairs ⇒ DỪNG `ORACLE_DRIFT`; không đổi expected.

PASS pair-set:
- graph = **88/88** oracle pairs;
- 0 extra.

## 6. HAI CÂU HỎI TỪ CÙNG RESULT SET

Q1 direct: “Những file nào import `enums.py`?”
- exact source-file set từ 88-pair result;
- so exact AST oracle set.

Q2 transitive: “`runner.py` phụ thuộc gián tiếp những file nào?”
- dựng transitive closure deterministic **trong bộ nhớ** từ cùng 88 direct pairs;
- cycle-safe, unique;
- exact equality với closure từ AST oracle.

Không query graph lần hai.
Không ghi edge mới vào Neo4j.

## 7. ACCEPTANCE

XONG chỉ khi:
1. Neo4j R4 đọc nguyên vẹn.
2. 88/88 unique file-import pairs, 0 extra.
3. file+line provenance hợp lệ.
4. Q1 exact.
5. Q2 exact.
6. production PRE=POST.
7. 0 external call.
8. chỉ start/stop Neo4j trial; R4 volume content không bị mutate bởi test.

Nếu PASS, KQ đề nghị Host nâng:
`CODE-EDGE-TRUST v0.3: file-level imports represented by dependency nodes = EXACT_POSITIVE`.

Ghi rõ: relation tồn tại ở dependency-node representation; không bắt buộc có file→file edge để được coi là có dữ liệu.
Materialize `GS_CODE_IMPORTS` nếu production cần hiệu năng là quyết định R7, không làm ở R6A.

Nếu fail:
- KQ DỪNG + exact mismatch;
- không fallback product;
- không parser/filter;
- không đổi version.

## 8. KHÔNG LÀM TRONG R6A

Không free-text business.
Không Nuxt.
Không shell DOT.
Không SQL/PG relationship build.
Không KB curation.

Roadmap sau R6A:
- R6B FREE-TEXT ORACLE;
- R6C NUXT ORACLE;
- R6D DOT/SQL EXPLICIT-LINK COVERAGE;
- R6E KB CURATION/SOURCE FREEZE.

## 9. CLEANUP

Stop/remove temporary R6A Neo4j container/network nếu tạo riêng.
Giữ nguyên R4 volume/evidence.
Không xóa R4/R5 data.
Verify production == PRE.

## 10. KQ / REPO

Evidence:
`/opt/incomex/work/graph-server/evidence/GS-R6A-CODE-TRUST-20261006-04/`

Repo chỉ cập nhật `work/graph-server/COLLAB.md` Bảng/KQ; không tạo progress/review file.

KQ:
`KQ@GS-R6A-CODE-TRUST-20261006-04 XONG|DỪNG`

Commit:
`[Claude Code] GS-R6A-CODE-TRUST-20261006-04 · graph-server · <XONG|DỪNG>`

Final:
`XONG · GS-R6A-CODE-TRUST-20261006-04 · <commit>`
hoặc
`DỪNG · GS-R6A-CODE-TRUST-20261006-04 · <blocker> · <commit>`

## 11. AUTONOMY

Trong scope R6A Claude tự quyết chi tiết Docker/Cypher/AST comparison.
Không hỏi Owner.
Không mở rộng scope.
Không production mutation.

Nếu cần sản phẩm thứ hai, parser mới, version mới hoặc corpus mới ⇒ DỪNG; không tự mở.
