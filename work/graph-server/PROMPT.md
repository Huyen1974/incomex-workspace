# PROMPT — GS-R6B-FREETEXT-OCCUPATION-20261006-05

## 0. LỆNH / PHẠM VI

RUN_ID: `GS-R6B-FREETEXT-OCCUPATION-20261006-05`
Executor_Surface: Claude Code CLI
Repo: `Huyen1974/incomex-workspace` · branch `main`
Task: `work/graph-server`
Repo Write_Path: Incomex workspace gateway `workspace_*` · root `workspace`
Runtime Write_Path: terminal/SSH hiện hữu tới VPS1 + đường đọc Lark hiện hữu.

Owner D14: GPT + Claude tự quyết trial nhỏ; chỉ production/quy mô thật mới xin Owner.

MỤC TIÊU DUY NHẤT:
- đo khả năng đọc **văn bản thật do nhân viên tự gõ** và suy ra nghề trong một catalog hữu hạn;
- oracle nằm ở **một cột nhãn riêng**, đóng băng trước model call;
- kiểm cả in-catalog, holdout/NEW, negative sibling, canonical graph và provenance.

Đây KHÔNG phải bài chăm sóc khách hàng.
Không bulk KB.
Không mở Base/table khác.
Không production mutation.

§0.3: đọc/đối chiếu trước mutation.

## 1. READ-GATE / STARTED

Đọc:
1. `AGENTS.md`
2. BẢNG + §0 + D14/D15 + P33–P36 của `work/graph-server/COLLAB.md`
3. `work/graph-server/PROMPT.md`
4. `work/graph-server/view.html` roadmap hiện hành
5. root `COLLAB.md` dòng Graph.

Xác minh READY full SHA = commit cuối chạm PROMPT; không HOLD/STOP/READY mới; không STARTED cùng RUN chưa có KQ.

PASS → ghi:
`STARTED@GS-R6B-FREETEXT-OCCUPATION-20261006-05 <UTC> · executor=Claude Code CLI`

FAIL → 0 runtime mutation, KQ DỪNG.

Trước first runtime mutation: DROOT30 freshness gate.

## 2. NGUỒN DUY NHẤT / SCHEMA FREEZE

Base: `88 - Phái cử`
Table: `Đơn hàng - Chính thức` · `tblh7nrQpK8TqIs2`

Input text DUY NHẤT:
- `Tên và nội dung công việc cụ thể:` · `fldJ3K1OdR`

Oracle label DUY NHẤT:
- `Nghành nghề xin visa:` · `fldHUYGtLA`

Selection-only fields:
- `Mã đơn hàng` — đọc runtime schema để lấy exact field id;
- `Loại Visa` — đọc runtime schema để lấy exact field id.

CẤM model/corpus nhận:
- `TÊN ĐƠN HÀNG`;
- oracle label;
- Loại Visa;
- mọi field khác.

Ghi schema field ids/types vào evidence trước khi đọc corpus.

## 3. ORACLE NORMALIZATION — KHÓA TRƯỚC KHI ĐỌC KẾT QUẢ MODEL

Normalization:
- Unicode NFC;
- trim/collapse whitespace;
- case-insensitive cho matching alias;
- ngoài các alias dưới đây, nhãn nghề giữ nguyên nội dung.

Alias map bị khóa theo P35:
1. `Lắp cốp pha panen` ←
   - `Lắp cốp pha panen`
   - `Lắp đặt cốt pha panen`
   - `Lắp cốt pha panen xây dựng`
2. `Chế biến thuỷ sản không gia nhiệt` ←
   - `Chế biến thuỷ sản không gia nhiệt`
   - `CHẾ BIẾN THỰC PHẨM THỦY SẢN KHÔNG GIA NHIỆT`
3. `Sơn kim loại` ←
   - `Sơn kim loại`
   - `Sơn (Sơn kim loại)`
4. `Gia công kim loại tấm` ←
   - `Gia công tấm kim loại`
   - `Gia công kim loại tấm`
5. `Dựng giàn giáo` ←
   - `Dựng giàn giáo`
   - `Giàn giáo xây dựng`
6. `Vệ sinh toà nhà` ← chính nó
7. `Cấp liệu bê tông bằng áp lực` ← chính nó
8. `Gia công cơ khí` ←
   - `Gia công cơ khí`
   - `Gia công cơ khí (Tiện thông thường)`

Không gộp ngoài map này.
Đặc biệt KHÔNG gộp `Làm sắt` với `GIA CÔNG CỐT THÉP`.

Loại khỏi catalog/sample:
- mọi record `Loại Visa = Tokutei`;
- oracle label `CK-Cơ khí,điện tử và kim loại`.

## 4. SAMPLE — ĐÚNG 16 ĐOẠN, DETERMINISTIC

### 4.1 Approved vA: 12 đoạn
6 nghề × 2 đơn:
- Lắp cốp pha panen
- Chế biến thuỷ sản không gia nhiệt
- Sơn kim loại
- Gia công kim loại tấm
- Dựng giàn giáo
- Vệ sinh toà nhà

### 4.2 Holdout: 4 đoạn
2 nghề × 2 đơn:
- Cấp liệu bê tông bằng áp lực
- Gia công cơ khí

### 4.3 Cách chọn
Trong mỗi nghề:
- sort `Mã đơn hàng` tăng dần;
- chọn record đầu tiên có input text >= 40 ký tự;
- record thứ hai tiếp theo có text >=40 và text không giống hệt record thứ nhất;
- nếu record bị leak-scan loại, lấy record kế tiếp cùng nghề.

Không chọn theo nội dung/ngữ nghĩa.
Không cherry-pick theo model output.

Không đủ **đúng 16** đoạn ⇒ DỪNG `INSUFFICIENT_FREETEXT_SAMPLE`.
Không tự đổi nghề/nguồn.

## 5. PRIVACY / LEAK GATE

Tài liệu đưa ra provider:
`order_xxx + nguyên văn fldJ3K1OdR`.

Không sửa/paraphrase/cắt nội dung đoạn.

Mapping record_id→order_xxx local mode 600; không Git/provider/evidence public.

**RAW-TEXT EXECUTOR BOUNDARY:**
- Lark fetch, sample selection, leak scan, freeze và provider payload phải chạy trong script cục bộ trên VPS.
- CẤM in/cat/grep raw description, oracle label, raw record id hoặc private mapping ra stdout/stderr của Claude Code.
- Terminal/Claude chỉ được thấy count, pseudonym, hash, length, pass/fail, metric và receipt id; evidence công khai cũng không chứa raw text.
- Private raw corpus/oracle/mapping để dưới runtime R6B mode 700/600.

Trước provider:
- phone/email/document-number scan;
- dùng existing local privacy/DLP scanner cho PERSON nếu có;
- nếu scanner PERSON không có, dùng deterministic local name-dictionary/regex path hiện hữu; không nhờ Claude đọc raw text bằng mắt. Nếu không thể kiểm tên người một cách cục bộ đáng tin ⇒ DỪNG `PII_SCAN_UNAVAILABLE`.
- tên nghiệp đoàn/xí nghiệp: tạo dictionary local từ Base và scan exact/normalized; dictionary không in giá trị ra terminal.
- nếu đoạn có tên người hoặc nghi PII/proper-name nhạy cảm ⇒ loại đoạn, lấy record kế tiếp; không sửa chữ.

Leak gate phải 0.
Chỉ sau leak gate, raw description mới được gửi tới đúng OpenAI model của trial và JEV qua gateway hiện hữu. Không gửi raw text tới provider/surface khác.
Không đủ 16 sau leak gate ⇒ DỪNG.

## 6. FREEZE — TRƯỚC MODEL CALL ĐẦU TIÊN

Freeze + SHA256:
- runtime schema;
- alias normalization map;
- full normalized occupation catalog;
- sample record ids + order pseudonyms;
- oracle labels;
- catalog vA;
- holdout list;
- 8 negative sibling tests;
- raw input text hashes.

Freeze timestamp phải trước external/model call đầu tiên.
Sau freeze cấm đổi sample/oracle/catalog để cứu metric.

## 7. CATALOG vA / vB

Relation type cố định:
`ORDER_HAS_OCCUPATION`.

Đây là test **catalog VALUE**, không phải relation-type discovery (R5 đã test relation type).

Catalog vA:
- toàn bộ normalized occupation labels hợp lệ còn lại trong 84 labels sau exclusions;
- TRỪ hai holdout occupations:
  - Cấp liệu bê tông bằng áp lực
  - Gia công cơ khí
- thêm đúng một choice:
  `NOT_IN_CATALOG`.

Expected khoảng 27 nghề + NOT_IN_CATALOG; ghi số thực sau freeze.

JEV:
- bounded `choice`;
- SHADOW;
- receipt: result id/model/probabilities/confidence/choice/order_id;
- không threshold 75/85;
- không business action.

Catalog vB:
- thêm đúng hai holdout occupations;
- reclassify **same frozen evidence**, không re-ingest/re-extract text.

## 8. STACK — REUSE R5, KHÔNG THÊM THÀNH PHẦN

Fresh R6B trial state, không trộn R5/R4 corpus.

Exact baseline:
- Neo4j Community 5.26.31 + APOC 5.26.31
- Cognee 1.6.1 pinned
- PGVector trial `pgvector/pgvector:0.8.6-pg18-trixie`
- embedding `openai/text-embedding-3-small` 1536
- LLM `openai/gpt-5.6-luna`
- JEV existing gateway; record actual returned model
- `HASH_API_KEY=true`
- `BIND_ADDRESS=127.0.0.1`; no Cognee host port
- telemetry off
- Qdrant production untouched
- PostgreSQL production untouched.

Egress/inference/isolation/wipe = cùng pattern R5.
R6B external cost cap <= **1 USD**; overall trial cap 5 USD.

## 9. INGEST / CLASSIFY / CANONICAL GRAPH

Ingest each frozen document into Cognee for document/provenance/vector layer.
Raw Cognee relations are evidence/candidates only, never business truth.

Occupation judgment:
- JEV reads only `order_xxx + raw description` + catalog vA choices;
- oracle label is NEVER in JEV/model input.

Policy:
- vA approved choice ⇒ create one `:GS_CANONICAL` `ORDER_HAS_OCCUPATION` edge to occupation node;
- `NOT_IN_CATALOG` ⇒ store candidate/evidence, do not force canonical occupation;
- each order may have **max one** canonical occupation edge.

vB:
- add holdouts;
- reclassify same evidence;
- create holdout canonical edges only after vB result.

Every canonical edge must trace:
edge → JEV receipt → source document/order_xxx → source text hash.

## 10. 8 NEGATIVE SIBLING TESTS

For each pair below, use **the first selected order by ascending `Mã đơn hàng` within occupation A** and ask bounded yes/no:
“Đoạn này có thuộc nghề B không?”
Cấm chọn giữa hai đoạn dựa trên nội dung/model output.

Expected = NO for all:
1. Sơn kim loại × Sơn xây dựng
2. Dựng giàn giáo × Lắp cốp pha panen
3. Lắp cốp pha panen × Xây dựng thành gia cố
4. Gia công kim loại tấm × Hàn
5. Gia công kim loại tấm × ÉP KIM LOẠI
6. Chế biến thuỷ sản không gia nhiệt × Chế biến thịt bò, thịt lợn
7. Vệ sinh toà nhà × Trát vữa
8. Dựng giàn giáo × Trát vữa

Không tạo canonical edge từ negative test.

## 11. GRAPH QUESTIONS

Sau vB, 8 occupation groups × 2 orders.

Từ canonical graph trả lời exact:
A. Với mỗi group, “đơn nào cùng nghề với `order_x`?” → đúng order còn lại trong cặp.
B. Với mỗi nghề N, “các đơn thử thuộc nghề N?” → đúng exact 2-order set.

=> **16/16 query assertions** exact.
Mỗi answer phải có provenance về source description.

## 12. BASELINE DIFFICULTY — BẮT BUỘC BÁO

Trước model output scoring, tính:
1. string-match baseline: bao nhiêu/16 raw descriptions tự chứa oracle occupation label hoặc alias tương ứng (Unicode/case normalized substring);
2. text length chars: min + median.

KQ phải ghi hai số này.
Nếu string baseline >= **14/16**, KQ bắt buộc ghi:
`EASY_BASELINE: bài này chủ yếu chứng minh pipeline trên văn bản thật có nhãn lộ trong text; không chứng minh semantic extraction khó.`

Không đổi sample để làm bài khó hơn.

## 13. ACCEPTANCE

Core target:
- vA approved: **12/12** đúng occupation;
- vA holdout: **4/4 NOT_IN_CATALOG**, 0 force-map;
- vB holdout: **4/4** đúng occupation, không re-extract;
- canonical extra edge: **0**;
- negative sibling: **8/8 NO**;
- graph questions: **16/16 exact**;
- provenance: **16/16** canonical edges trace source+receipt;
- production PRE=POST;
- leak gate PASS;
- cost <=1 USD hoặc UNKNOWN chỉ khi ledger provider không có, nhưng token/call counts phải ghi.

### Oracle suspect
Human label có thể sai.
Nếu mismatch:
- giữ nguyên frozen oracle;
- ghi mỗi mismatch đúng một dòng:
  - `MACHINE_ERROR`, hoặc
  - `ORACLE_SUSPECT` + lý do từ evidence.
- không tự sửa oracle/alias/sample.

Báo **raw metric** và **machine metric excluding ORACLE_SUSPECT**.
Có ORACLE_SUSPECT ⇒ Host đọc là PASS-WITH-LIMITS tối đa, không được báo “perfect”.

## 14. KHÔNG SUY RỘNG

R6B PASS chỉ chứng minh:
- văn bản thật của **mô tả công việc đơn hàng** có thể map vào catalog nghề trong sample;
- catalog holdout không bị force-map;
- canonical graph/JEV/provenance hoạt động.

Không chứng minh:
- chăm sóc khách hàng;
- chat/email;
- ghi chú phát sinh;
- KB;
- production scale.

Base 88 gần như không có free-text care/exchange.
R6E phải xác định **văn bản chăm sóc khách/trao đổi thật nằm ở đâu** trước production scope.

## 15. CLEANUP / KQ

Evidence:
`/opt/incomex/work/graph-server/evidence/GS-R6B-FREETEXT-OCCUPATION-20261006-05/`

Kết thúc:
- stop/remove R6B containers/network;
- giữ volume/evidence cho Host review;
- dry-run wipe đúng R6B scope;
- production == PRE.

Repo chỉ cập nhật `work/graph-server/COLLAB.md` Bảng/KQ.
Không tạo progress file Git.

KQ:
`KQ@GS-R6B-FREETEXT-OCCUPATION-20261006-05 XONG|DỪNG`

Commit:
`[Claude Code] GS-R6B-FREETEXT-OCCUPATION-20261006-05 · graph-server · <XONG|DỪNG>`

Final:
`XONG · GS-R6B-FREETEXT-OCCUPATION-20261006-05 · <commit>`
hoặc
`DỪNG · GS-R6B-FREETEXT-OCCUPATION-20261006-05 · <blocker> · <commit>`

## 16. AUTONOMY

Claude tự xử chi tiết kỹ thuật trong đúng 9 điều kiện P35 đã khóa.
Không hỏi Owner.
Không đổi nguồn/nghề/sample count/model/provider/stack.
Không mở KB.
Không production mutation.

Nếu không thể thỏa đủ 9 điều kiện P35 ⇒ DỪNG, không tự sửa thiết kế.
