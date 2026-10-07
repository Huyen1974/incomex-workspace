# PROMPT — GS-R6E-SOURCE-MANIFEST-20261007-09

## 0. LỆNH / PHẠM VI

RUN_ID: `GS-R6E-SOURCE-MANIFEST-20261007-09`
Executor_Surface: Claude Code CLI
Repo: `Huyen1974/incomex-workspace` · branch `main`
Task: `work/graph-server`
Repo Write_Path: Incomex workspace gateway `workspace_*` · root `workspace`
Runtime Write_Path: terminal/SSH hiện hữu tới VPS1.

Owner D14: trial nhỏ được tự quyết trong scope; production/quy mô thật chỉ R7 Owner duyệt.

MỤC TIÊU DUY NHẤT:
- tạo **manifest whitelist nguồn được phép vào Graph production v1**;
- kiểm kê **có biên**, không kiểm kê toàn hệ thống;
- xếp từng nguồn trong biên vào đúng một loại:
  `CURRENT/KEEP · ARCHIVE · DELETE-CANDIDATE · RECHECK`;
- freeze danh sách + cách chụp + trust contract để R7 clean build dùng.

R6E KHÔNG:
- dọn KB;
- xoá/di chuyển/sửa file;
- sửa COMMENT/registry;
- ingest Neo4j/Cognee;
- build production;
- đọc nội dung/title tài liệu KB;
- đụng Lark;
- mở lại care/chat discovery;
- gọi LLM/JEV;
- tạo parser/graph feature mới.

Manifest = **danh sách cho vào**. Thứ không có dòng `CURRENT/KEEP` trong manifest v1 thì không vào Graph v1.

## 1. READ-GATE

Đọc:
1. `AGENTS.md`
2. BẢNG + §0 + D13–D15 + P49–P52 của `work/graph-server/COLLAB.md`
3. `work/graph-server/PROMPT.md`
4. `work/graph-server/view.html`
5. root `COLLAB.md` dòng Graph.

Xác minh READY full SHA = commit cuối chạm PROMPT; không HOLD/STOP/READY mới; không STARTED cùng RUN chưa có KQ.

PASS → ghi:
`STARTED@GS-R6E-SOURCE-MANIFEST-20261007-09 <UTC> · executor=Claude Code CLI`

FAIL → 0 runtime mutation, KQ DỪNG.

## 2. BIÊN KIỂM KÊ U1–U3 — CẤM MỞ RỘNG

### U1 · Nguồn đã dùng trong R4–R6D
Chỉ metadata/provenance của các source đã xuất hiện trong evidence:
- R4/R6A Python sample source (frozen `dot/iu-cutter-v0.6`) — để xếp loại, không ingest;
- R5 Base 88 explicit-link source — chỉ dùng evidence cũ, **không đọc Lark**;
- R6B/R6B0 trial runtime/evidence;
- R6C Nuxt source;
- R6D PG/DOT sources.

### U2 · Ứng viên production đã khóa ở P51
Đúng các lớp/candidate này:

1. PostgreSQL trigger native catalog (capture contract = R6D `Q_TRG`).
2. DOT live command existence: `/opt/incomex/dot/bin` + `/opt/incomex/dot/00-SO-DOT.tsv`.
3. DOT registry declarations: `public.dot_tools` theo R6D `Q_DOT`.
4. Python first-party candidate roots, xác nhận tồn tại tại runtime:
   - `/opt/incomex/docker/agent-data-repo`
   - `/opt/incomex/lark-client` — tuyệt đối loại `.venv`
   - `/opt/incomex/claude-mcp`
   - `/opt/incomex/claude-kb`
   - `/opt/incomex/scripts`
5. TS/Vue source:
   - `/opt/incomex/docker/nuxt-repo/web`
6. Các nguồn P51 đã xếp ARCHIVE/RECHECK:
   - PG: `trigger_registry`, `dot_domains`, `dot_operations`, `_recon_dot_fs_inventory`, `entity_dependencies`, họ `v_qt001_*`, `dot_iu_command_catalog`, `iu_relation`, `universal_edges`;
   - FK/view native dependency counts;
   - `knowledge_documents`;
   - `normative_registry` (metadata/count/link coverage only; không mở KB);
   - conceptual source `Lark Base 88 explicit links` = RECHECK/Owner decision, **không đọc Lark**;
   - care/chat = no source.

Nếu một exact path candidate không tồn tại:
- chỉ được resolve **cùng basename trong /opt/incomex, depth tối đa 2**;
- thấy 0 hoặc >1 candidate ⇒ ghi RECHECK `PATH_UNRESOLVED`;
- không search toàn filesystem.

### U3 · Trial artifacts
Chỉ:
- `/opt/incomex/work/graph-server/runtime/`
- `/opt/incomex/work/graph-server/evidence/`

Phân theo từng RUN/task folder.
Không xoá.

### Ngoài biên
Thấy source khác ⇒ tăng `OUT_OF_SCOPE_COUNT`/ghi category ngắn nếu dễ xác định; **không xếp loại, không đào tiếp**.

## 3. READ-ONLY GATE

### PostgreSQL
Dùng đúng role read-only đã chứng minh ở R6D:
- non-superuser;
- transaction read-only;
- 0 INSERT/UPDATE/DELETE/DDL.

Cho phép ở R6E:
- SELECT metadata/catalog trong U1/U2;
- đọc COMMENT của object trong biên;
- aggregate counts trên `knowledge_documents`;
- aggregate metadata của `normative_registry`.

Cấm output row-level business/KB content.

### Filesystem/Git
Chỉ:
- stat/list/hash;
- `git rev-parse HEAD`, `git status --porcelain`, `git ls-files`;
- đọc metadata labels `00-NHAN-THU-MUC.md`, `GHI-CHU-CAY-GIT.md`, phần bản đồ hệ thống P51 đã dùng;
- không sửa mtime/content/permissions.

Production PRE = POST bắt buộc.

## 4. KB — CHỈ 3 PHÉP ĐẾM TỔNG HỢP

Nếu cần mapping tên cột do schema drift:
- được đọc `information_schema.columns` của `knowledge_documents`;
- không đọc row content/title.

Sau đó chỉ ba aggregate families:

### KB-A · TOTAL
Xuất duy nhất aggregate:
- row count;
- tổng `length(content)`;
- min/max create/update timestamps nếu cột tồn tại.

### KB-B · FOLDER × MONTH
Group bằng **bucket thư mục**, không xuất full document path/title:
- top-level/known class bucket;
- month(create/update theo query đã freeze);
- count.

Evidence public chỉ bucket + count.

### KB-C · BYTE-DUPLICATE COUNTS
Dùng `md5(content)` trong SQL chỉ để aggregate:
- số duplicate hash groups;
- tổng redundant rows.
Không xuất hash, content, title, path từng tài liệu.

`knowledge_documents` luôn xếp:
`RECHECK · NOT_IN_V1`
trong R6E, bất kể số đếm.
Không chọn một subset KB trong RUN này.

`normative_registry` chỉ ghi aggregate:
- active/current rule count theo status hiện hữu;
- số row có document path/link non-null;
- nếu có thể đối chiếu existence mà không xuất nội dung/title thì ghi count-only.
Không đưa KB vào KEEP từ phép đối chiếu này.

## 5. CODE ROOT INVENTORY

Với từng exact candidate code root U2:

1. xác nhận path;
2. tìm git root bằng `git -C <root> rev-parse --show-toplevel`;
3. record:
   - git HEAD;
   - dirty tracked/untracked count;
   - branch nếu có;
   - tracked file count theo extension;
   - label `00-NHAN-THU-MUC.md` có/không + metadata life-state/date nếu label có;
4. file hash inventory:
   - chỉ `git ls-files` dưới candidate root;
   - không hash `.git`, `.venv`, `node_modules`, `.nuxt`, `.output`, cache/build artifacts;
   - hash list để private evidence; repo/KQ chỉ count + aggregate hash.
5. cross-tree duplicate:
   - so hash của tracked files giữa các **candidate KEEP roots**;
   - nếu cùng bytes xuất hiện ở hai cây candidate KEEP ⇒ cả hai liên quan xuống `RECHECK · CROSS_TREE_DUPLICATE` cho đến R7;
   - không xoá.

Nếu root không có git, dirty, label missing/expired/frozen/dead:
- không sửa;
- xếp theo §6, thường RECHECK/ARCHIVE.

### Trust contract cho code
- Python: v0.3 chỉ chứng minh tool behavior trên sample frozen; candidate source root có thể KEEP, nhưng manifest phải ghi:
  `R7_REVERIFY=AST_ORACLE_REQUIRED_BEFORE_INGEST`.
- TS/Vue: v0.4 trust = explicit-static directory→target trên measured slice; candidate Nuxt root KEEP chỉ với scope trust đó; file-level/auto-import vẫn theo UNKNOWN/residual.

## 6. LUẬT XẾP LOẠI — 4 CÂU, DỪNG Ở CÂU ĐẦU TRÚNG

Áp cùng một thứ tự cho mỗi source row trong U1–U3:

### RULE-1 → DELETE-CANDIDATE
Là:
- dữ liệu/runtime trial; hoặc
- rỗng có bằng chứng; hoặc
- byte-identical duplicate của một source đã giữ.

Chỉ lập danh sách.
**Không xoá.**
Tên/path một mình không đủ làm căn cứ duplicate/delete.

### RULE-2 → ARCHIVE
Nhãn/provenance sẵn có chứng minh một trong:
- frozen/dead/disabled target;
- bản copy/mirror của source gốc;
- version cũ đã superseded;
- vendored/external library không phải first-party source.

Để nguyên tại chỗ; không vào Graph v1.

### RULE-3 → RECHECK
Thiếu **bất kỳ** điều kiện nào:
1. label/currentness evidence còn hạn ≤6 tháng;
2. read-only capture method + hash;
3. measured trust contract đúng relation/source type;
4. Owner privacy/scope decision nếu source có personal/business data.

Ngoài ra code root:
- no git / dirty / unresolved path / cross-tree duplicate ⇒ RECHECK.

### RULE-4 → CURRENT/KEEP
Chỉ khi:
- source gốc;
- đang sống theo label/currentness;
- chụp read-only + hash được;
- relation type có trust contract đã đo;
- privacy decision không thiếu.

Mỗi source row phải ghi `rule_hit=1|2|3|4`.
Không được override thủ công sau khi thấy kết quả.

## 7. NHÓM XẾP LOẠI ĐÃ KHÓA / EXPECTED POLICY

Đây là policy expectation, nhưng RUN vẫn phải áp §6 và ghi evidence:

### KEEP candidates
- PG native trigger catalog;
- DOT disk live command source;
- DOT registry declaration source `dot_tools` với trust=DECLARED;
- first-party Python code roots nào PASS §5/§6;
- Nuxt web root nếu PASS §5/§6.

### ARCHIVE expected
- stale/frozen PG registries/views P51 nêu;
- `dot/iu-cutter*`;
- `lark-client/.venv`;
- deploy/copy/context-pack/evidence copies;
- 78 backup entries trong `dot/bin`;
- historical evidence folders = ARCHIVE, không delete.

### RECHECK expected
- FK/view native dependencies;
- `universal_edges`;
- `knowledge_documents` whole class = NOT_IN_V1;
- Lark Base88 business links = OWNER_SCOPE_REQUIRED;
- any code root failing KEEP gate;
- care/chat = NO_SOURCE.

### DELETE-CANDIDATE expected
- trial runtime folders;
- proven empty/byte-identical duplicate if any.
Không delete.

## 8. MANIFEST OUTPUT

Evidence:
`/opt/incomex/work/graph-server/evidence/GS-R6E-SOURCE-MANIFEST-20261007-09/`

Tạo:
- `production-source-manifest.csv`
- `production-source-manifest.json`
- `manifest.sha256`
- `inventory.json`
- `classification-replay.json`
- `owner-decisions-r7.md`
- `00-KQ.md`
- `EVIDENCE.sha256`.

Mỗi manifest row tối thiểu:
- source_id / class_id;
- exact location hoặc conceptual source id;
- origin_or_copy;
- label region/life_state/measure_date;
- capture_method **nguyên văn command/query**;
- count summary;
- aggregate/source hash;
- trust_contract (`v0.3/v0.4/v0.5/UNKNOWN`);
- exclusions;
- classification;
- rule_hit;
- missing_gate / residual;
- R7_reverify requirement.

Freeze manifest SHA256.
“Freeze” = chốt **whitelist + capture contract + reference snapshot**.
R7 clean build phải chụp dữ liệu thật lại; không reuse trial snapshot như production data.

## 9. E1–E6 PASS

### E1 · ZERO MUTATION
- PG read-only pre/post proof;
- production PRE=POST;
- 0 delete/move/edit/ingest;
- 0 Neo4j/Cognee container started;
- 0 provider call/cost.

### E2 · BOUNDED COMPLETENESS
- mọi source trong U1–U3 xuất hiện đúng một lần trong inventory/manifest classification;
- đúng một classification + một `rule_hit`;
- ngoài biên không bị kéo vào.

### E3 · KEEP GATES COMPLETE
Mỗi KEEP row có:
- capture method;
- count;
- hash;
- valid current label;
- measured trust contract.
Code KEEP:
- git HEAD;
- dirty count = 0;
- no cross-tree duplicate hashes.
Python KEEP luôn có `AST_ORACLE_REQUIRED_BEFORE_INGEST`.

### E4 · DETERMINISTIC REPLAY
Chạy classifier lần hai **trên frozen inventory**, không reread production.
Output classification phải byte-identical / same hash.

### E5 · TRUST/UNKNOWN HONEST
- không KEEP row thiếu measured trust;
- UNKNOWN list v0.5 giữ nguyên;
- TS/Vue file-level/auto-import limits giữ nguyên;
- care/chat = NO_SOURCE;
- KB = RECHECK whole class, NOT_IN_V1, aggregate-only;
- business Lark links = RECHECK/OWNER_SCOPE_REQUIRED.

### E6 · R7 DECISION BUNDLE
`owner-decisions-r7.md` có đúng các nhóm:
1. Graph v1 KB: đề xuất **không đưa KB cũ vào v1**.
2. KB cleanup: việc riêng sau R7; Owner chọn archive-index-first vs selective delete. Không làm trong Graph task.
3. Business Graph: có cho phép explicit Lark Base88 links vào production scope không + privacy rule.
4. Care/chat: có bắt đầu capture/connect nguồn không.
5. Trial cleanup: xoá private R6B/R6B0 + wipe trial runtime/evidence theo scope nào sau quyết định production.
6. R5 OpenAI cost: `UNKNOWN, estimate ≤0.47 USD` cần ghi trong R7 report.
7. R7 build gates:
   - rerun Python AST oracle trên actual KEEP Python trees trước ingest;
   - nếu thêm FK/view relations thì phải có R6D-style identity/set gate;
   - fresh capture hashes for all KEEP sources.

Mỗi decision có:
- `WHY`
- `HOST_RECOMMENDATION`
- `OWNER_CHOICE`.
Không yêu cầu Owner trả lời trong R6E.

## 10. STOP RULES

DỪNG nếu:
- cần mutation để đo;
- read-only PG path không chứng minh được;
- cần đọc KB content/title;
- cần đụng Lark;
- cần search ngoài U1–U3 để phân loại;
- classifier cần subjective/manual exception;
- cần cài package/LLM/JEV.

Không rerun để đổi classification.
Source dirty/missing label/unknown ⇒ RECHECK, **không phải blocker toàn RUN** nếu vẫn đo được read-only và manifest ghi đủ lý do.

## 11. KQ / CLEANUP

Không có trial DB/graph container.
Runtime nếu cần:
`/opt/incomex/work/graph-server/runtime/r6e/`
chỉ scripts/temp inventory, không business content.

Cuối RUN:
- rerun PRE/POST metadata;
- freeze evidence;
- wipe dry-run runtime/r6e only;
- không xoá R6B/R6B0/R6C/R6D artifacts.

Repo:
- chỉ update Bảng/KQ trong `work/graph-server/COLLAB.md`;
- không sửa PROMPT/view ở executor.

KQ:
`KQ@GS-R6E-SOURCE-MANIFEST-20261007-09 XONG|DỪNG`

Final:
`XONG · GS-R6E-SOURCE-MANIFEST-20261007-09 · <commit>`
hoặc
`DỪNG · GS-R6E-SOURCE-MANIFEST-20261007-09 · <blocker> · <commit>`

## 12. AUTONOMY

Claude tự xử read-only inventory/scripts/classifier trong đúng U1–U3.
Không hỏi Owner.
Không delete/archive/move.
Không ingest/build.
Không đổi policy sau khi thấy số.
Ngoài biên ⇒ ghi OUT_OF_SCOPE, không đào.
