# PROMPT — GS-R5-BUSINESS-ORACLE-20261006-03

## 0. LỆNH / PHẠM VI

RUN_ID: `GS-R5-BUSINESS-ORACLE-20261006-03`
Executor_Surface: Claude Code CLI
Repo: `Huyen1974/incomex-workspace` · branch `main`
Task: `work/graph-server`
Repo Write_Path: Incomex workspace gateway `workspace_*` · root `workspace`
Runtime Write_Path: terminal/SSH hiện hữu tới VPS1 + đường đọc Lark hiện hữu; không tạo connector/credential mới.

Owner 06/10 ủy quyền GPT + Claude **tự quyết toàn bộ trial kỹ thuật trong phạm vi nhỏ**. Chỉ khi chuyển sang **production/quy mô triển khai thật** mới phải xin Owner.

Mục tiêu duy nhất của RUN này:
- kiểm **business graph + finite catalog/open discovery + JEV SHADOW** bằng một bộ dữ liệu có ground truth máy chấm được;
- không mở rộng nguồn;
- không chứng minh bằng cảm giác/reviewer prose nếu có oracle deterministic.

Không bulk-ingest KB.
Không lấy customer notes tự do ở lượt này.
Không hành động business.
Không production mutation.

§0.3: đọc/đối chiếu toàn bộ trước mutation.

## 1. READ-GATE / STARTED

Đọc theo thứ tự:
1. `AGENTS.md`
2. BẢNG + §0 + D13/D14 + P26–P28 của `work/graph-server/COLLAB.md`
3. `work/graph-server/PROMPT.md`
4. `work/graph-server/view.html` roadmap/PLAN01 hiện hành
5. root `COLLAB.md` dòng Graph.

Xác minh:
- READY full SHA = commit cuối chạm PROMPT;
- không HOLD/STOP/READY mới;
- không STARTED cùng RUN chưa có KQ.

PASS → ghi:
`STARTED@GS-R5-BUSINESS-ORACLE-20261006-03 <UTC> · executor=Claude Code CLI`

FAIL → 0 runtime mutation, KQ DỪNG.

Trước first runtime mutation: DROOT30 freshness gate.

## 2. NGUYÊN TẮC BÀI THỬ — ORACLE TRƯỚC, AI SAU

Không dùng AI để tạo đáp án.

Ground truth lấy từ **link field Lark thật** trong Base `88 - Phái cử`.
Sau khi oracle được freeze + hash, mới tạo text đã che và mới gọi OpenAI/JEV.

Nguồn DUY NHẤT:
- `Đơn hàng - Chính thức` — `tblh7nrQpK8TqIs2`
- `TTS - Thông tin` — `tblKnzaih6154r2e`
- `Nghiệp đoàn` — `tblG18kR9aFhWrJW`
- `Xí nghiệp` — `tblqFRpClTG0OCjE`

Không đọc PTTT notes, KB, COLLAB, code hoặc nguồn business khác để làm corpus R5.

### 2.1 Schema freeze
Đọc schema Lark read-only và ghi vào evidence:
- field id + field name + type của primary key/source-id/link fields liên quan;
- xác nhận thực tế các field tương đương:
  - TTS ↔ Đơn hàng tiến cử;
  - TTS ↔ Đơn hàng trúng tuyển;
  - Đơn hàng ↔ Nghiệp đoàn;
  - Đơn hàng ↔ Xí nghiệp.
Tên field có thể khác lịch sử; **field ID/runtime schema mới là ground truth**.

Nếu một trong bốn relation không tồn tại/không đọc được:
- không mở rộng sang Base khác;
- dùng tối đa các exact-link relation còn đủ để có 3 relation types;
- nếu còn <3 relation types ⇒ DỪNG `INSUFFICIENT_ORACLE_RELATIONS`.

### 2.2 Sample
Chọn deterministic, không cherry-pick theo kết quả AI:
- sắp record theo source record ID;
- chọn tập nhỏ đầu tiên thỏa relation coverage;
- tối đa **20 text snippets**;
- mục tiêu:
  - 8–12 positive snippets từ exact links;
  - 2–4 positive snippets cho relation holdout/new-type;
  - 4 negative controls từ cặp cùng entity types nhưng **không có link** trong oracle.
- ít nhất 3 orders và 4 TTS pseudonyms nếu dữ liệu cho phép.

Freeze manifest + oracle **trước model call**, sha256 cả hai.

## 3. PRIVACY / PSEUDONYM

Không gửi ra ngoài:
- tên người;
- tên xí nghiệp/nghiệp đoàn thật;
- điện thoại/email;
- CCCD/hộ chiếu/giấy tờ;
- raw record ID;
- credential/secret;
- text field ngoài template đã định.

Pseudonym ổn định từ `source-table-id + source-record-id`, mapping local mode 600:
- `tts_001`
- `order_001`
- `union_001`
- `company_001`

Cùng source ID ⇒ cùng pseudonym.
Khác source ID ⇒ không được trùng.
Mapping không Git, không provider, không evidence public.

Leak scan corpus trước provider:
- 0 tên thật;
- 0 raw Lark record id;
- 0 phone/email/document number;
- 0 secret.

Fail ⇒ DỪNG trước external call.

## 4. TEXT PROJECTION — DETERMINISTIC

Text không lấy từ AI. Tạo bằng fixed Vietnamese templates từ oracle:

- candidate:
  `<tts> được tiến cử cho <order>.`
- selected:
  `<tts> đã trúng tuyển <order>.`
- union:
  `<order> thuộc nghiệp đoàn <union>.`
- company:
  `<order> tuyển lao động cho xí nghiệp <company>.`

Nếu runtime schema dùng relation tương đương nhưng khác nghĩa, sửa template **trước model call** để phản ánh đúng link thực; lưu template version trong manifest.

Negative controls:
`<entityA> và <entityB> là hai mã độc lập trong bộ kiểm thử; không có liên kết nguồn giữa hai mã.`

Không paraphrase AI.
Không thêm facts ngoài oracle.

## 5. CATALOG v0.1 — CLOSED-WORLD DECISION × OPEN-WORLD DISCOVERY

Từ các relation thật tìm được, chọn:
- 3 relation types vào catalog APPROVED v0.1;
- **1 relation type thật làm HOLDOUT**, cố tình không có trong catalog để test discovery.

Ưu tiên nếu đủ dữ liệu:
- `CANDIDATE_FOR_ORDER`
- `SELECTED_FOR_ORDER`
- `ORDER_MANAGED_BY_UNION`
- HOLDOUT: `ORDER_FOR_COMPANY`

Catalog v0.1 được freeze/hash trước model call.

JEV classification choices cho mỗi extracted candidate:
- các APPROVED types hợp source/target;
- `NEW_RELATION`;
- `NO_RELATION`.

Không dùng threshold 75/85.
Không cho JEV invent exact source/target.
Không cấp action permission.

## 6. TRIAL RUNTIME

Dựng **fresh R5 trial state**, không trộn R4 corpus:
- Neo4j Community 5.26.31 + APOC 5.26.31
- Cognee 1.6.1 pinned
- PGVector trial `pgvector/pgvector:0.8.6-pg18-trixie`, reuse exact R4 artifact/digest đã có local; không pull latest
- embedding `openai/text-embedding-3-small`, 1536
- LLM `openai/gpt-5.6-luna`
- JEV existing gateway, model thực phải ghi từ response
- `HASH_API_KEY=true`
- `BIND_ADDRESS=127.0.0.1`, no Cognee host port
- telemetry off
- no Cognee MCP/UI
- Qdrant production untouched
- PostgreSQL production read-only untouched.

Fresh R5 volumes/dataset names:
`TRIAL_ONLY · GS-R5-BUSINESS-ORACLE-20261006-03`

Không import R4 code graph vào R5.

Resource gates:
- RAM available >= 5.5 GB trước start;
- RAM available <2 GB khi chạy ⇒ stop trial;
- disk floor >=20 GB;
- total active R5 trial footprint <=10 GB.
- không đổi swap; record PRE/POST.

## 7. EXTRACTION — MỘT TUYẾN MẶC ĐỊNH

Nạp **chỉ text projection** vào Cognee default text/KnowledgeGraph path.
Không custom GraphSchemaSpec.
Không custom extraction prompt nếu default path chạy được.
Không dùng structured oracle làm input cho extraction.

Mỗi snippet phải giữ:
- snippet_id;
- source pseudonyms;
- oracle relation id ở file local riêng;
- provenance hash.

Raw relation output phải lưu trước JEV mapping để có thể tái phân loại mà không re-extract.

## 8. JEV SHADOW — TỰ GỌI SAU EXTRACTION

R5 harness phải tự gọi JEV cho từng candidate relation sau extraction; không phụ thuộc executor nhớ gọi thủ công từng item.

Dùng bounded `choice`:
approved shortlist + NEW_RELATION + NO_RELATION.

Input JEV chỉ gồm:
- raw relation text;
- pseudonym source/target types;
- candidate approved choices;
- evidence snippet.

Không đưa oracle label vào JEV state.

Ghi receipt:
- result id;
- model;
- probabilities/confidence;
- choice;
- snippet id.

Nếu JEV connector unavailable/model call fail:
- retry hữu hạn;
- vẫn fail ⇒ KQ DỪNG vì Goal #2 là core R5.

## 9. DISCOVERY TEST — KHÔNG RE-EXTRACT

Với holdout relation:
1. catalog v0.1 không có type đó;
2. JEV phải chọn `NEW_RELATION` thay vì force-map type cũ;
3. lưu candidate + evidence;
4. trong sandbox trial, giả lập human approve bằng deterministic test step:
   - tạo catalog v0.2 thêm đúng holdout type từ oracle;
5. **không gọi Cognee extraction lại**;
6. chỉ classify lại raw candidate đã lưu với catalog v0.2;
7. PASS nếu map sang type vừa được thêm.

Không auto-approve mọi edge cùng type.
Đây chỉ là test catalog evolution.

## 10. NEGATIVE CONTROL

4 negative snippets phải:
- không tạo canonical positive edge;
- JEV = `NO_RELATION`.

Nếu extraction sinh candidate từ negative:
- vẫn đưa JEV;
- PASS nếu policy không canonicalize và receipt phản ánh NO_RELATION.

## 11. METRICS / ACCEPTANCE

### A. Oracle pairing
Đối chiếu bằng source/target pseudonym + relation type.

### B. Positive relation extraction
- pair recall = **100%** trên sample nhỏ;
- false source/target pair = **0**.

### C. Approved relation mapping
- approved-type precision = **100%**;
- approved-type recall = **100%**.

### D. Holdout discovery
- v0.1: **100% holdout items → NEW_RELATION**
- không holdout nào bị force-map approved type.
- v0.2 reclassification: **100% → holdout approved type**, không re-extract.

### E. Negative controls
- canonical false positive = **0/4**
- JEV NO_RELATION = **4/4**.

### F. Graph answers
Freeze ít nhất 5 deterministic questions từ oracle, ví dụ:
- TTS nào được tiến cử cho order_X?
- TTS nào trúng tuyển order_X?
- order_X thuộc union nào?
- order_X tuyển cho company nào?

Query graph và so exact set:
- **5/5 exact answer**.

### G. Provenance
Mỗi canonical edge phải trace được:
edge → raw candidate/snippet → manifest/oracle source pseudonym.
Không lưu raw identity thật trong graph.

### H. Vector smoke
3 semantic queries over R5 snippets:
- >=3/3 expected snippet/entity trong top-3.
Qdrant point/config PRE = POST.

### I. Cost
External R5 cost cap **<= 1 USD**.
Nếu provider không có ledger, report UNKNOWN + call/token counts; không vượt overall trial cap 5 USD.

## 12. CÁCH ĐỌC KẾT QUẢ

PASS chỉ chứng minh:
- pipeline business relation trên **oracle-controlled micro-sample** đáng tin;
- finite catalog + discovery + JEV integration hoạt động kỹ thuật.

PASS **không chứng minh**:
- mọi ghi chú chăm sóc khách tự do đều tốt;
- KB hiện tại sạch;
- production scale;
- action automation.

Nếu PASS:
- không mở rộng sample tự động;
- chuyển roadmap sang R6 KB curation/source freeze;
- chỉ sau khi technical evidence + curation đủ mới trình Owner production scope.

Nếu metric core lệch:
- không đổi threshold để “cho qua”;
- ghi chính xác false positive/negative;
- KQ DỪNG hoặc PASS-WITH-LIMITS theo evidence;
- không mở rộng nguồn.

## 13. CLEANUP / DISPOSABLE

Kết thúc:
- stop/remove R5 containers/network;
- giữ R5 volumes/evidence cho Host review;
- dry-run wipe command chứng minh xóa đúng R5 scope;
- không xóa R4 evidence;
- production services/health phải == PRE.

Không production install.
Không destructive KB cleanup.

## 14. KQ / REPO

Evidence:
`/opt/incomex/work/graph-server/evidence/GS-R5-BUSINESS-ORACLE-20261006-03/`

Repo chỉ cập nhật:
- `work/graph-server/COLLAB.md`
- BẢNG/KQ.
Không tạo progress/review file Git.

KQ:
`KQ@GS-R5-BUSINESS-ORACLE-20261006-03 XONG|DỪNG`

Commit:
`[Claude Code] GS-R5-BUSINESS-ORACLE-20261006-03 · graph-server · <XONG|DỪNG>`

Cuối cùng trả đúng một dòng:
`XONG · GS-R5-BUSINESS-ORACLE-20261006-03 · <commit>`
hoặc
`DỪNG · GS-R5-BUSINESS-ORACLE-20261006-03 · <blocker> · <commit>`

## 15. AUTONOMY

Owner đã ủy quyền trial cho GPT + Claude:
- tự quyết kỹ thuật nhỏ trong scope;
- không hỏi Owner về record nào, field nào, Docker command, retry, số sample trong giới hạn;
- không mở rộng Base/table/source;
- không tăng sample >20;
- không đổi model/provider;
- không production mutation.

Nếu muốn vượt bất kỳ giới hạn trên ⇒ DỪNG; production/quy mô thật phải xin Owner.
