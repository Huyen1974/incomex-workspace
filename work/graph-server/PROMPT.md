# PROMPT — GS-R6C-NUXT-ORACLE-20261007-07

## 0. LỆNH / PHẠM VI

RUN_ID: `GS-R6C-NUXT-ORACLE-20261007-07`
Executor_Surface: Claude Code CLI
Repo: `Huyen1974/incomex-workspace` · branch `main`
Task: `work/graph-server`
Repo Write_Path: Incomex workspace gateway `workspace_*` · root `workspace`
Runtime Write_Path: terminal/SSH hiện hữu tới VPS1.

Owner D14: GPT + Claude tự quyết trial nhỏ; production/quy mô thật mới xin Owner.

MỤC TIÊU DUY NHẤT:
- kiểm độ tin cậy của Graph trên **explicit static imports** của một lát Nuxt/TypeScript/Vue thật;
- chấm chính ở cấp **thư mục importer → đích import**, đúng representation Enola/Cognee hiện tại;
- cấp file chỉ đo/giải thích, KHÔNG dùng recall >=95% làm gate.

KHÔNG:
- audit toàn frontend;
- Nuxt auto-import;
- dynamic import/require làm acceptance;
- generated routes/plugin injection;
- LLM/JEV/vector;
- cài package/parser mới;
- custom regex parser;
- production mutation.

§0.3: đọc/đối chiếu toàn bộ trước runtime mutation.

## 1. READ-GATE / STARTED

Đọc:
1. `AGENTS.md`
2. BẢNG + §0 + D14/D15 + P41–P44 của `work/graph-server/COLLAB.md`
3. `work/graph-server/PROMPT.md`
4. `work/graph-server/view.html` roadmap
5. root `COLLAB.md` dòng Graph.

Xác minh:
- READY full SHA = commit cuối chạm PROMPT;
- không HOLD/STOP/READY mới;
- không STARTED cùng RUN chưa có KQ.

PASS → ghi:
`STARTED@GS-R6C-NUXT-ORACLE-20261007-07 <UTC> · executor=Claude Code CLI`

FAIL → 0 runtime mutation, KQ DỪNG.

Trước mutation đầu: DROOT30 freshness gate.

## 2. SOURCE SSOT / PRE

Production source SSOT, **READ-ONLY**:
`/opt/incomex/docker/nuxt-repo/web`

Không sửa source, node_modules, .nuxt, mtime, ownership hoặc Git state.

PRE ghi:
- source Git HEAD/status;
- SHA256 + mtime của 16 sample files + 3 config files;
- SHA256 + mtime của:
  - `node_modules/typescript/package.json`
  - `node_modules/@vue/compiler-sfc/package.json`
- package versions phải đúng:
  - `typescript==5.9.3`
  - `@vue/compiler-sfc==3.5.25`
- production containers/health read-only baseline.

Nếu source/config/package thiếu hoặc version lệch ⇒ DỪNG `R6C_SOURCE_OR_ORACLE_DRIFT`.

## 3. SAMPLE — KHÓA ĐÚNG 16 FILE THEO P43

Chép byte-exact, giữ relative path, sang:
`/opt/incomex/work/graph-server/runtime/r6c/sample/`

16 files:

### components/modules/comment-module/
1. `components/modules/comment-module/CommentInput.vue`
2. `components/modules/comment-module/CommentModule.vue`
3. `components/modules/comment-module/CommentThread.vue`
4. `components/modules/comment-module/types.ts`
5. `components/modules/comment-module/composables/useComments.ts`
6. `components/modules/comment-module/partials/CheckpointPanel.vue`

### components/modules/workflow-module/partials/
7. `components/modules/workflow-module/partials/InlineWcrPopup.vue`
8. `components/modules/workflow-module/partials/ProcessRegistryView.vue`
9. `components/modules/workflow-module/partials/StepsTimeline.vue`
10. `components/modules/workflow-module/partials/WcrIntakePanel.vue`

### direct targets
11. `types/tasks.ts`
12. `types/checkpoints.ts`
13. `types/workflow-dsl.ts`
14. `types/workflows.ts`
15. `composables/useCheckpoints.ts`

### importer
16. `pages/knowledge/workflows/[id].vue`

Ba file cấu hình chép kèm, byte-exact:
17. `package.json`
18. `tsconfig.json`
19. `.nuxt/tsconfig.json`

Không chép `nuxt.config.ts`.
Không mở rộng sample.
Không thay file vì metric xấu.

Sau copy:
- verify hash source == sample cho cả 19 file;
- freeze manifest + SHA256 **trước oracle/extraction**.

## 4. ORACLE ĐỘC LẬP — DÙNG GÓI CÓ SẴN, KHÔNG CÀI

Oracle packages:
- TypeScript compiler API 5.9.3;
- @vue/compiler-sfc 3.5.25.

Runtime:
1. ưu tiên `node` hiện hữu trên VPS;
2. nếu không có, chỉ được dùng local image `node:20-alpine` nếu image đã tồn tại:
   - `--pull never`
   - `--network none`
   - source/node_modules mount read-only.
3. không có cả hai ⇒ DỪNG `ORACLE_RUNTIME_UNAVAILABLE`.

CẤM npm/pnpm install, download, network.
`NODE_DISABLE_COMPILE_CACHE=1`.
cwd/output/temp đều dưới `runtime/r6c`.

Oracle script được viết mỏng chỉ để gọi API hai gói, **không tự parse syntax bằng regex**.

Oracle:
- Vue: compiler-sfc tách `<script>` / `<script setup>` và map line về file .vue gốc.
- TypeScript compiler API lấy:
  - top-level static `import ... from`
  - top-level static `export ... from`
- `import type` tính như explicit static dependency.
- dynamic `import()` / `require()` nếu thấy: **đếm riêng, OUT_OF_SCOPE acceptance**.
- Nuxt auto-import/generated behavior: không oracle, UNKNOWN.

Alias/module resolution:
- đọc `tsconfig.json` + `.nuxt/tsconfig.json` bằng TypeScript config parser;
- relative import: resolve từ importer directory;
- alias `~/...`: resolve theo config/root;
- package external: giữ package specifier theo rule frozen.

Oracle output freeze trước Enola:
- statement list: importer file, line, raw specifier, resolved target, internal/external, type-only yes/no;
- unique `(file,target)`;
- unique `(directory,target)`;
- SHA256.

Không in source body.

## 5. EXTRACTION — ENOLA/COGNEE, 0 LLM

Fresh R6C runtime:
`/opt/incomex/work/graph-server/runtime/r6c/`

Reuse exact local Enola/Cognee code-graph path/version đã dùng R4:
- Enola 0.4.21
- Cognee 1.6.1
- fresh Neo4j R6C volume/network
- không import R4 graph
- không PGVector
- không Cognee API/UI
- không OpenAI
- không JEV
- 0 outbound.

Prefer reuse reviewed R4 scripts/config where applicable; only adapt source/sample/output path.
Không sửa extractor/loader.

Neo4j:
- Community 5.26.31
- local image only; `--pull never`
- loopback/docker-internal only.

Enola output `.enola/facts.jsonl` phải được giữ raw trước Cognee loader.

## 6. POPULATION CHẤM

Chỉ score dependency facts/nodes mà `file_path` thuộc 16 sample files.

Expected node name key theo semantics P43:
`<directory_of_importer> -> <normalized_target>`

Normalization phải freeze trước extraction:
- importer directory = relative POSIX directory của file;
- relative target = resolved path/module theo oracle;
- alias target = resolved theo tsconfig;
- external package = normalized package specifier;
- extension/index normalization phải dùng một rule duy nhất và ghi evidence trước chấm.

Hai cấp phải báo riêng:

### A. File-level — CHỈ ĐO
- oracle statement count;
- unique (file,target) pair count;
- Enola dependency fact count;
- Enola unique fact-id count;
- Cognee node count;
- file-level precision/recall nếu reconstruct được từ provenance.

KHÔNG gate PASS bằng recall file-level.

### B. Directory-level — GATE CHÍNH
- expected set = unique `(directory,target)` from oracle.
- actual set = dependency-node names after Cognee.
- đây là thước đo exact chính.

## 7. 6 ĐIỀU KIỆN PASS — TẤT CẢ PHẢI ĐẠT

### C1 · DIRECTORY SET EXACT
Actual dependency-node name set =
oracle `<directory> -> <target>` set.
**0 extra, 0 missing.**

### C2 · PROVENANCE TRUE
Mỗi node actual phải có `(file_path,line)` trỏ tới **một câu explicit static import/export thật** trong oracle có cùng expected node name.

PASS = 100% nodes provenance-valid.

### C3 · SOURCE CLASS EXACT
`source=internal|external` của Enola/Cognee phải khớp oracle rule cho 100% scored nodes/facts.
Nếu Cognee không giữ property nhưng raw Enola giữ, score ở raw Enola và ghi rõ representation loss; canonical conclusion chỉ dựa trên layer thật sự có field.

### C4 · COUNTS EXPLAINED
Báo đủ:
- oracle static statement count;
- oracle unique (file,target);
- oracle unique (directory,target);
- Enola dependency fact count;
- Enola unique fact IDs;
- Cognee dependency node count.

Node count PASS nếu:
- bằng oracle unique (directory,target), **hoặc**
- bằng oracle unique (file,target).

Ra số khác cả hai ⇒ DỪNG + exact diff.
Không sửa rule sau khi thấy số.

### C5 · 3 GRAPH QUESTIONS
Q1. “Thư mục nào import `types/tasks`?” → exact directory set theo oracle.

Q2. “`pages/knowledge/workflows/[id].vue` import những đích explicit-static nào?”  
File này đứng một mình trong directory scope của sample, nên graph phải trả exact target set theo oracle.

Q3. “Những file nào trong `components/modules/comment-module` import `types/tasks`?”
- nếu graph representation vẫn giữ đủ file provenance để trả exact set ⇒ exact match;
- nếu Cognee gộp node directory-level ⇒ đáp án đúng bắt buộc:
  `UNKNOWN_FROM_GRAPH`
  + đúng **một** provenance witness file;
- cấm suy/điền đủ file set từ source/oracle khi trả lời “bằng graph”.

### C6 · ZERO PRODUCTION DRIFT
- production PRE = POST;
- 16 source files + 3 config files SHA/mtime unchanged;
- TypeScript/compiler-sfc package SHA/mtime unchanged;
- no source/node_modules/.nuxt write;
- R6C containers/network removed;
- 0 outbound/provider cost.

## 8. CHỈ ĐẾM, KHÔNG CHẤM

Ghi evidence, không dùng PASS/FAIL:
- Enola fact counts theo `kind`;
- relation counts;
- Vue component symbol count;
- Vue/template `calls` count;
- Neo4j `imports` edge count nếu có;
- route fact cho `pages/knowledge/workflows/[id].vue`;
- dynamic import/require count nếu có;
- số source files toàn Nuxt không có explicit import nếu đo sẵn được bằng bounded local grep/parser; **không scan/audit thêm chỉ để lấy số này**.

Semantics cảnh báo:
- Vue `calls` có thể nghĩa template-use, không mặc định là function call;
- `import type` không được Enola đánh dấu riêng ⇒ import presence không đồng nghĩa runtime load.

## 9. KẾT LUẬN ĐƯỢC PHÉP

Nếu PASS, Host có thể nâng sau review:
`CODE-EDGE-TRUST v0.4`

Chỉ được nói:
- TS/Vue **explicit static imports** chính xác ở cấp directory→target trong sample đã đo;
- file-level fidelity được đo nhưng **không bảo đảm** nếu Cognee gộp node;
- provenance có thể dùng để quay về một file/line làm chứng.

CẤM nói:
- “Graph đã phủ dependency Nuxt”;
- “auto-import đã được phủ”;
- “route/runtime dependency đã chính xác”;
- “mọi file Nuxt có dependency đầy đủ”.

Nuxt auto-import, generated types/routes, dynamic/runtime behavior = UNKNOWN trừ evidence riêng.

## 10. RESIDUALS — GHI, KHÔNG MỞ VIỆC TRONG RUN

Không làm trong R6C:
1. auto-import oracle từ `.nuxt/components.d.ts` / `.nuxt/imports.d.ts` — Host quyết sau R6C;
2. CODE-EDGE-TRUST v0.4 — Host nghiệm thu sau KQ;
3. Presidio+Stanza — chỉ nếu Owner mở lại free-text source scope;
4. R5 OpenAI extraction cost vẫn `UNKNOWN (ước ≤0.47 USD)` — chốt ở R7 report;
5. Directus License #23 — root/HJW, ngoài Graph;
6. xóa `runtime/r6b/private` và `runtime/r6b0/private` — **chờ Owner gật**, R6C không xoá.

## 11. EVIDENCE / CLEANUP / KQ

Evidence:
`/opt/incomex/work/graph-server/evidence/GS-R6C-NUXT-ORACLE-20261007-07/`

Evidence gồm tối thiểu:
- PRE/POST;
- sample manifest + hashes;
- oracle script hash + oracle.json/hash;
- raw Enola facts hash/counts;
- node/provenance diff;
- metrics.json;
- 3 graph-question results;
- 00-KQ.md.

Cleanup:
- stop/remove R6C containers/network;
- giữ R6C volume/evidence cho Host review;
- wipe dry-run R6C scope;
- không xóa R4/R5/R6B evidence/private.

Repo:
- chỉ cập nhật `work/graph-server/COLLAB.md` Bảng/KQ;
- không tạo progress/review file Git.

KQ:
`KQ@GS-R6C-NUXT-ORACLE-20261007-07 XONG|DỪNG`

Commit:
`[Claude Code] GS-R6C-NUXT-ORACLE-20261007-07 · graph-server · <XONG|DỪNG>`

Final:
`XONG · GS-R6C-NUXT-ORACLE-20261007-07 · <commit>`
hoặc
`DỪNG · GS-R6C-NUXT-ORACLE-20261007-07 · <blocker> · <commit>`

## 12. AUTONOMY

Claude tự xử Docker/Node/oracle/extraction/scoring mechanics trong scope.
Không hỏi Owner.
Không cài package.
Không sửa production source.
Không đổi sample.
Không gọi model/JEV.
Không mở auto-import follow-up trong cùng RUN.

Nếu oracle packages/runtime không dùng được, sample drift, hoặc cần custom parser/patch extractor ⇒ DỪNG sạch.
