# COLLAB — graph-server
Tên việc: Graph Server — Business × JEV × Code

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — chỉ đạo trực tiếp ngày 24/09/2026 và lời làm rõ ngày 28/09/2026 tại D04–D06: graph hóa thông tin đa nguồn, giữ bốn ưu tiên, tiêu chí công cụ bền vững thực dụng (MIT không bắt buộc — D06); Host tổng hợp/phản biện kế hoạch. Chưa duyệt công nghệ, ngoại lệ giấy phép hoặc triển khai VPS.

### 1. Mục tiêu
Nguyên văn User, giữ thứ tự ưu tiên:
1. Tạo ra các mối quan hệ về Graph đối với business (khi các mối quan hệ là hữu hạn, chứ không phải quan hệ vô hạn kiểu mạng xã hội.
2. Kết hợp tốt nhất với Jev để đảm bảo Graph truyền thống và Jev bổ sung tốt nhất cho nhau theo các hướng dẫn mới nhất của typesaveai và nhà sáng lập của nó **Diogo Almeida**.
3. Định hướng ứng dụng các skill, frame chính thức của Jev để có thể tận dụng xu thế phát triển thêm Jev trong tương lai (ý là, Jev là 1 xu hướng hiệu quả, giờ mới chỉ bắt đầu, Incomex cần chuẩn bị để không tụt hậu trong xu hướng này)
4. Tự Dựng lại mối quan hệ về về code để các Agent/ AI có thể hiểu nhanh hơn khi hệ thống phức tạp lên.

Bối cảnh nguyên văn User: “Gốc rễ nhất là chúng ta đã dọn VPS còn hơn 50GB để cho việc này.”

**Nguyên tắc khoá — nguyên văn Owner 24/09/2026** (áp cho mọi lựa chọn của việc này; toàn repo: AGENTS A10-R1): “Mọi giải pháp phải đảm bảo, ưu tiên tối đa, dùng cái có sẵn, nhiều người dùng, phù hợp nhất với Incomex. Không tự dựng bất cứ cái gì nếu thị trường có sẵn. Code là giải pháp cuối cùng.”

**Làm rõ “quan hệ hữu hạn” — Owner 28/09/2026:** hữu hạn = tại mỗi thời điểm/miền nghiệp vụ chỉ có một tập lựa chọn chuẩn nhất định, không phải mạng xã hội với quan hệ vô định. Danh mục này **được phép thay đổi/bổ sung theo thời gian**. Hệ thống phải đồng thời: (a) ưu tiên map dữ liệu vào loại quan hệ đã duyệt; (b) không ép dữ liệu lạ vào loại cũ — phải có làn tự phát hiện/đề xuất loại quan hệ mới từ dữ liệu, JEV hỗ trợ đánh giá xác suất, người duyệt rồi mới đưa vào danh mục chuẩn. Danh mục chuẩn là hữu hạn theo **phiên bản**, không đóng kín vĩnh viễn.

**Làm rõ ngày 28/09/2026 — nguyên văn Owner, không đảo bốn ưu tiên:**
> Mục đích của chúng ta xây dựng Graph cho mọi loại thông tin của chúng ta, Phần lớn thông tin là các mối quan hệ business để giúp xây dựng các quy trình, chăm sóc khách hàng, xây dựng các lựa chọn nhanh hơn và agent hiểu mã của hệ thống.
> Hiểu đơn giản mục tiêu là Graph hóa tất cả các thông tin chúng ta sẽ có (cái thông tin claude nhìn thấy chỉ là 1 phần rất nhỏ).
> Mục tiêu chính của việc này là các thông tin không có tính chất SQL (như chăm sóc khách hàng) hoặc có tính chất SQL nhưng chúng ta không thể SQL hoá => lôi ra dùng Graph + Jev để hỗ trợ nhằm giải quyết nhanh hơn các vấn đề.
> Ngay cả các quy trình hiện nay đang loay hoay, nếu co graph vẫn có thể hiểu được mối quan hệ tương đối của nó với nhau, và tính cách mô hình xác suất sẽ đúng hơn.
> *(Thay câu MIT trước đó cùng ngày — D06)* Việc MIT hay không cũng không quá quan trọng. Cái quan trọng là: được dùng miễn phí, được cập nhật theo thời gian và dựa vào giải pháp có xác suất chết giữa chừng thấp (tránh như OS Agency hiện nay)

### 2. Thế nào là hoàn thành
Phạm vi lượt giao hiện tại, nguyên văn User:
- “tạo 1 task tên work/graph-server”
- “Đưa các nội dung lên đây theo đúng quy đjnh để hội đồng bắt đầu có ý kiến.”

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Chỉ tạo hai file trong task: COLLAB.md điều phối và view.html là tài liệu chính duy nhất. Không tạo PROMPT, file review, bản nháp hoặc pipeline phụ.
- Giữ đủ các nhóm lựa chọn đã thảo luận; phân biệt nguồn kiểm chứng, đề xuất và điều chưa kiểm. Đề xuất cũ không phải quyết định Owner.
- **Nguyên tắc lựa chọn Owner 24/09/2026:** bỏ ưu tiên kiến trúc tự thiết kế hoặc giữ lại chỉ vì đã có; ưu tiên giải pháp **off-the-shelf đã chạy thực tế, đáng tin, nhiều người dùng/cộng đồng, cài sẵn/ít code tùy biến và phù hợp Incomex**. PostgreSQL/Qdrant hiện hữu là bối cảnh để tận dụng nếu hợp lý, không phải rào cản cấm cài graph DB/sản phẩm mới.
- **Tầm nhìn một câu (Claude soạn 28/09 từ lời Owner, Host kiểm):** Graph hoá mọi thông tin Incomex được phép dùng; giá trị chính nằm ở thông tin chưa/không SQL hoá được (chăm sóc khách hàng, trao đổi, quy trình còn loay hoay, code); Graph nối mẩu rời thành liên hệ có nguồn và độ chắc → JEV cân nhắc từng lựa chọn một bước → policy/người quyết hành động.
- **“Hữu hạn” (ưu tiên #1) =** *loại* thực thể và *loại* quan hệ nằm trong một danh mục có mã, bổ sung qua quy trình; số thực thể, số nguồn không giới hạn. **Không** có nghĩa “chỉ dữ liệu đã có sẵn trong bảng”. Trái nghĩa: mạng xã hội, nơi loại quan hệ và độ lan không có biên.
- Giữ đúng thứ tự mục tiêu. Lark/SQL chỉ là một nhóm nguồn; phải có thông tin chăm sóc khách hàng, trao đổi/quy trình và quan hệ suy luận có bằng chứng ngay trong bài thử đại diện. Không đòi SQL hóa xong mới làm Graph. Mọi nguồn thật vẫn phải thuộc phạm vi được cấp quyền.
- **Hữu hạn theo phiên bản, mở cho khám phá:** đường vận hành dùng catalog quan hệ chuẩn có version; đường discovery giữ quan hệ free-form/candidate kèm nguồn và evidence. Không block tiến trình chỉ vì chưa có relation type chuẩn; nhưng candidate chưa được dùng như quan hệ chuẩn cho business action cho tới khi qua policy/approve. Khi duyệt, thêm type vào version tiếp theo và từ đó ưu tiên map/gợi ý.
- **Tiêu chí công cụ (D06):** miễn phí/self-host dài hạn cho công ty nhỏ · còn cập nhật · cộng đồng/vendor mạnh · xác suất chết giữa chừng thấp · dữ liệu/logic lõi mang đi được. MIT là điểm cộng, không bắt buộc. Vẫn kiểm LICENSE đúng phiên bản/dependency/model trước khi chốt; loại giấy phép cấm thương mại.
- Bậc theo A10-R1: 1 sản phẩm có sẵn; 2 cấu hình/ghép các điểm mở rộng và gateway hiện hữu. Chỉ đề nghị bậc 3 code mỏng khi chứng minh hai bậc trên thiếu; không tự dựng graph engine, framework hoặc UI mới.
- Tái dùng việc jev-integration đã đóng; không mở cổng/skill nội bộ trùng chức năng. Dung lượng hơn 50GB là thông tin Owner, đối chiếu báo cáo VPS ngày 23/09; chưa phải số đo mới của lượt này.
- Chưa cho phép cài đặt, quét dữ liệu/mã thật, migration, restart, xóa hoặc đổi cấu hình/model/gateway. Các bài kiểm trong tài liệu chỉ để hội đồng đánh giá.

### Vòng trước
Chưa có — mở việc lần đầu theo lệnh Owner. Nội dung chat trước là đầu vào, không phải quyết định kiến trúc đã duyệt.

Host: GPT Chat
Host_ID: GPT-GRAPH-20260924-A — ID điều phối do Host tự đặt.
Owner giao mở việc: 2026-09-24
HTML chính: `view.html`
Owner View: https://vps.incomexsaigoncorp.vn/knowledge/modules?task=graph-server
Executor_Surface: GPT Chat — biên tập hồ sơ.
Write_Path: Incomex MCP full all 2 → workspace_* → root workspace, main.

## Dòng hiện hành
GS | P05 HÒA GIẢI · D06 GIẤY PHÉP THỰC DỤNG | Graph tri thức đa nguồn; ưu tiên miễn phí self-host, cập nhật đều, cộng đồng mạnh, nguy cơ chết thấp; MIT không còn là hard gate | Chưa PROMPT/READY/RUN, chưa cài | NEXT: Claude + Hermes phản biện shortlist Neo4j+Cognee vs Neo4j+Graphiti theo độ bền, quyền và khả năng thay lớp trên. OWNER VIEW CHECK DỪNG (AUTH).
- Hậu kiểm GS08 ngày 28/09/2026: commit `c9460a9fa13ec3b9cf646668d1c063537e75f992` đã push; diff chỉ đúng hai file COLLAB.md + view.html (65 dòng thêm, 13 dòng bỏ). `ui_inspect` đúng URL Owner View chuẩn trả shell HTTP 200 nhưng Directus 401/Login; chưa đọc được nội dung/revision mới, không báo Owner View PASS. Không tạo đường xem phụ; hồ sơ repo sẵn cho hội đồng review.
- Based_on mở việc: `37ae3fe22bc37894242506e4477b055d32fdc540`; GS02 hòa giải trên HEAD hiện hành, commit chen ngang không chạm task này.
- Đã đọc AGENTS.md → COLLAB.md gốc → README.md → work/README.md; áp khuôn MT3 hiện hành.
- Nghiên cứu cập nhật 24/09/2026: TypeSafe official skill/blog; pgvector; AGE; Cognee; Graphiti; Hindsight; Neo4j vector; GraphRAG. Link nguồn ở `view.html` §12.
- Owner View check sau commit `3b909e0c22d554433fdee8c49498c5cbb3cf1701`: gọi đúng URL chuẩn `/knowledge/modules?task=graph-server`, HTTP shell 200 nhưng Directus trả 401 và UI dừng ở Login; không thấy nội dung/revision ⇒ **DỪNG nghiệm thu Owner View, không báo PASS giả**. Repo/diff vẫn PASS.
- Áp: SAME_COMMIT.

## Quyết định Owner
- D01 · 2026-09-24 · Owner cho phép mở đúng task graph-server, tập hợp nội dung để hội đồng góp ý, giữ bốn ưu tiên và bối cảnh VPS. Không có quyết định chọn stack/cài đặt trong lệnh này.
- D02 · 2026-09-24 · **PRODUCT-FIRST / THỰC DỤNG:** Owner xác nhận thiết kế KG cũ trong KB quá phức tạp và không thực tế. Khi chốt Graph Server, tiêu chí ưu tiên là sản phẩm đang chạy tốt ngoài thực tế, đáng tin, cộng đồng/người dùng lớn, có gói cài/stack sẵn, ít phải tự xây framework và phù hợp nhất với Incomex. Thiết kế cũ/Điều 39 không được dùng như lý do khóa lựa chọn vào `universal_edges`/PostgreSQL; chỉ giữ các ranh giới nghiệp vụ còn hợp lý.
- D03 · 2026-09-24 · Owner giao Claude **khoá nguyên tắc vào mục tiêu** (nguyên văn ở §0.1) và áp toàn repo (DROOT19 · AGENTS A10). Áp: SAME_COMMIT (§0) · `b3f64c4` (gốc).

- D04 · 2026-09-28 · Owner làm rõ phạm vi: Graph cho mọi loại thông tin Incomex được phép dùng, trọng tâm business, chăm sóc khách hàng, quy trình/lựa chọn và code; thông tin Claude kiểm trong Lark/PG chỉ là một phần nhỏ. Đây không phải lệnh chốt Neo4j hoặc lệnh nạp dữ liệu.
- D05 · 2026-09-28 · Lịch sử: Owner từng nêu dài hạn ưu tiên MIT.
- D06 · 2026-09-28 · **GIẤY PHÉP THỰC DỤNG, thay cách áp D05:** MIT không bắt buộc. Tiêu chí chính là: công ty nhỏ được dùng miễn phí/self-host dài hạn theo chính sách hiện hành; dự án còn cập nhật; cộng đồng/nhà tài trợ đủ mạnh; xác suất bỏ dở thấp; dữ liệu/logic lõi có đường xuất và thay lớp trên. Vẫn loại giấy phép cấm/không phù hợp thương mại hoặc điều khoản làm Incomex phải công khai dịch vụ ngoài ý muốn. Không chọn dự án yếu chỉ vì MIT.

## Ý kiến hội đồng
### P01 · GPT Host · PARTIAL — giả thuyết vòng 1 đã được D02 thay tiêu chí lựa chọn
- Based_on: tài liệu Owner + nguồn kiểm ngày 24/09/2026; Scope: `view.html` §1–§11.
- Đề nghị: giữ PostgreSQL/pgvector; so A (Cognee+Neo4j+PGVector) với C (AGE+PGVector) trước, D làm baseline; B/Graphiti kéo lên nếu temporal/supersession chi phối. Hindsight = memory layer, không mặc định canonical graph.
- JEV Reference: `gen-dec-1790221175-ygPaecOXX76U0e4Y1yAe`; A-vs-C confidence 0.30 nên KHÔNG coi là chọn công nghệ; `canonical_constraints` probability 0.99/confidence 0.98 dùng để ưu tiên acceptance test.
- Lý do: mục tiêu #1 yêu cầu relation hữu hạn/kiểm soát; TypeSafe official skill yêu cầu code giữ hard rules/workflow, JEV chỉ làm semantic judgment trên bounded candidates.
- P01 không phải consensus.

### Yêu cầu Reviewer vòng 1
- Đọc A0 rồi `view.html`; phản biện Q01–Q07, A–E, boundary canonical fact/JEV judgment/agent memory, code graph deterministic/semantic.
- Fact kỹ thuật phải có source/runtime; bounded decisions có thể dùng JEV theo AGENTS A5.
- Không tạo file review mới; ghi Pxx ngay tại mục này theo A3.

### P02 · Claude Chat · Reviewer · OPEN — phản biện vòng 1 trên sự thật runtime
- Based_on: `6eac5e0` (COLLAB `2315aeeb…` · view.html `1608ec1f…`). Scope: `view.html` §1–§11 + P01. Chưa đọc: post X của imryven Owner gửi (X chặn tải từ phía tôi; thay bằng nguồn chính thức docs.typesafe.ai — liệt kê cuối P02; Owner dán nội dung post thì tôi đối chiếu thêm).
- JEV Reference: `gen-dec-1790224109-8RZpXsTUYsBLEKr7bW1r` — state = fact runtime thô F1–F5 bên dưới, 5 câu: nút thắt = `business_nodes_missing` (p 1,00) · bước đầu = `extend_universal_edges` (1,00) · tiền đề "pgvector" khớp runtime: noul 0,22 · phân vai = graph đi đường, JEV nhìn một bước (1,00) · code graph tách pipeline riêng: noul 0,74. Bằng chứng phụ; kết luận dưới là của Reviewer.

**F · Sự thật runtime đo 24/09 (query_pg + vps_status, không suy đoán):**
- F1 · PostgreSQL 16.13, image `postgres:16` chính hãng. Extension đã cài: btree_gist, pgcrypto, plpgsql, postgres_fdw. **pgvector: KHÔNG cài và KHÔNG có sẵn trong image; Apache AGE: không.** Muốn có phải đổi image PG = thay đổi production, Owner quyết. Qdrant đang chạy (container healthy) = lớp vector đã có.
- F2 · **Graph đã tồn tại trong PG**: `universal_edges` 2.269 cạnh / 3 loại (USES 1.486 · BELONGS_TO 466 · CONTAINS 317) / 39 cặp collection; `iu_relation` 60 (đã có `valid_time` bi-temporal + `provenance` + `evidence` + `assertion_mode`); `entity_dependencies` 142; `governance_relations` 8; `normative_relations` 18; `balo_thuc_the` 2.148 thực thể / `entity_species` 42; bộ `kg_*`: thresholds 5, source_authority 5, auto_approve_rules 6, **constraint_config 0, quality_log 0**. Trên `universal_edges` các cột `provenance/confidence/valid_from/valid_to/valid_time` **có sẵn nhưng 0/2.269 dòng dùng**.
- F3 · **Node nghiệp vụ = 0**: contacts 0, organizations_contacts 0, os_deal_contacts 0; không bảng khách hàng/nhân viên/ứng viên nào có dữ liệu. Dữ liệu thật mảng lao động/đào tạo đang ở Lark Base + Google Sheets (việc phai-cu-online, lark-base).
- F4 · VPS: 6 CPU · RAM 12GB (7GB trống) · đĩa trống 55GB.
- F5 · Luật hiện hành (Điều 39, council trước): PG là SSOT graph, Qdrant bổ trợ, **không DB thứ 3**; "PG thuần trước → AGE khi cần → Neo4j không bao giờ"; metric quan trọng nhất theo Owner: graph phải tương xứng với data.

**Đề nghị:**
1. **Nút thắt không phải engine.** Mục tiêu #1 cần node khách hàng/ứng viên/nhân viên — hôm nay = 0 (F3). Engine nào cũng rỗng. Vòng 1 **không chọn DB mới**; câu hỏi đúng: từ điển quan hệ hữu hạn của 3 quy trình Owner nêu là gì, node đầu tiên lấy từ đâu.
2. **Shortlist:** A/B (Neo4j/FalkorDB) → **REJECT vòng 1**: trái Đ39 (F5) — muốn xét phải mở D sửa luật — và F3. C (AGE) → **HOÃN, nấc 2** với ngưỡng kích hoạt đo được: >50k cạnh, hoặc truy vấn ≥4 hop >500ms sau khi đánh index, hoặc pattern cần Cypher mà SQL phải viết >50 dòng. D → **LÀM, nhưng là "dùng cái có", không "xây framework"**: universal_edges + iu_relation + kg_* đã có provenance/valid_time/confidence; btree_gist đã cài nên exclusion constraint chống cạnh trùng thời gian làm được ngay. E/Hindsight, Cognee, Graphiti → **HOÃN**; xét lại khi có tập văn bản cần extraction hoặc Hermes cần memory riêng.
3. **Vector:** dùng Qdrant có sẵn; pgvector chỉ xét khi Qdrant chứng minh thiếu (khi đó là D đổi image PG). §3 view.html tiền đề "giữ pgvector" chưa đúng runtime — đề nghị Host sửa.
4. **Graph × JEV — một dòng: "Graph đi đường, JEV nhìn một bước."** Căn cứ trang jaggedness chính thức jev-1.13 (2026-09-17): yếu multi-hop indirection; chính xác giảm khi state lớn/nhiễu; không phải máy tính; chưa có phòng thủ prompt-injection. ⇒ SQL/code làm traversal + sinh candidate + lọc lân cận; JEV nhận state nhỏ có tên trường + tập đáp án hữu hạn + bắt buộc có "none". Giữ 5 điểm giao §8 của Host và ánh xạ vào cookbook chính thức: entity alignment (noul+choice) · hierarchical classification (taxonomy) · pre-parsed extraction (code liệt kê trước, JEV chọn) · confidence-gated routing (cao → tự động theo `kg_auto_approve_rules` · giữa → review · thấp → người) · self-consistency (lặp mẫu) cho cạnh chạm con người (đánh giá nhân viên). Kết quả JEV ghi vào cột `provenance` có sẵn `{source:'jev', result_id, prob, confidence, model}` — không tạo loại quan hệ mới, không cấp quyền ghi.
5. **Future-ready (#3):** (a) nguồn chuẩn = docs.typesafe.ai + `typesafe-ai/skills`; SKILL.md Incomex là bản rút gọn từ typesafe-mcp → ghi rõ "lệch official skill thì official thắng"; (b) **danh mục câu hỏi JEV có mã** (type · instructions · criteria · threshold · version) giữ trong PG — mọi surface (GPT/Claude/Hermes/Nuxt) hỏi cùng câu, đo cùng ngưỡng; TypeSafe ra primitive mới chỉ thêm loại; (c) đường tích hợp chính thức đã kiểm 24/09: OpenRouter (đường duy nhất của Incomex), Pydantic AI `TypeSafeModel`, LangChain `TypeSafeClassifier`, Vercel AI SDK `evaluate`, Cloudflare Workers AI; Hermes có cookbook `andyholst/hermes-typesafe-jev`. Không dựng gateway thứ hai (đồng ý P01).
6. **Code graph (#4):** tách pipeline tất định riêng, chạy bên cạnh, không chặn #1. Lớp PG/DOT **đã có fact** trong universal_edges (dot_tools/trigger_registry/collection_registry → taxonomy); thiếu lớp app: Nuxt/TS → dependency-cruiser hoặc madge; Python MCP → pydeps/grimp. Ghi cùng universal_edges với edge_type nhóm `CODE_*`, `is_auto_managed=true`, `source_info=<tool@version>`, quét lại theo commit; JEV chỉ gắn nhãn semantic (ROLE_OF_MODULE, IMPACT_CLASS) tách khỏi fact.
7. **Acceptance thêm §9:** T10 cạnh nghiệp vụ đầu tiên hiện trên Owner View kèm provenance · T11 dashboard tỷ lệ cạnh/node theo species (Đ39 §8.6) · T12 mọi cạnh mới `valid_time` + `provenance` ≠ null (constraint), cạnh cũ có kế hoạch backfill.

**Q01–Q07:** Q01 không cần graph-native 3–5 năm; AGE nấc 2 có ngưỡng · Q02 temporal quan trọng (nhân sự đổi vị trí, khách đổi trạng thái) nhưng cột đã có, không cần Graphiti · Q03 Cognee strict-ontology hay, nhưng entity_species 42 + kg_constraint_config (rỗng) chưa dùng → điền cái rỗng trước; PG adapter Cognee "not production-ready" · Q04 mục 4 · Q05 mục 6 · Q06 chưa cần Hindsight; nếu dùng: memory = quan sát chưa duyệt, chỉ đề xuất cạnh qua gate · Q07 D = +0; C = đổi image PG (rủi ro restart prod); A/B ≈ +2–4GB RAM, E ≈ +1–2GB (ước lượng, chưa đo).

- **Đề xuất đưa Owner (Host chuyển):** D02 = vòng 1 đi bằng graph PG hiện có theo Đ39, không DB mới; AGE nấc 2 có ngưỡng; vector = Qdrant. Bước 1 thật: từ điển quan hệ hữu hạn cho 3 quy trình + node đầu tiên từ Lark Base.
- Nguồn thay link X: docs.typesafe.ai/model-jaggedness/jev-1.13 · docs.typesafe.ai/cookbooks/entity_alignment · docs.typesafe.ai/patterns/confidence-routing · github.com/typesafe-ai/skills · pydantic.dev/docs/ai/models/typesafe · openrouter.ai/docs/guides/community/jev.
- Phản hồi Host: **PARTIAL** — xem khối dưới.

### Host response P02 · GPT · PARTIAL — 24/09/2026
- **ACCEPTED:** F1–F4 là bằng chứng runtime hữu ích; Qdrant đang chạy, pgvector/AGE chưa cài, node business hiện chưa có. Giữ nguyên nguyên tắc JEV **“Graph đi đường, JEV nhìn một bước”**; code graph lấy deterministic fact trước, JEV chỉ làm bounded semantic judgment.
- **REJECTED phần kết luận dùng graph PG tự thiết kế làm hướng chính:** D02 của Owner nói rõ thiết kế KG cũ quá phức tạp/không thực tế; việc `universal_edges` đã tồn tại là sunk cost, không phải tiêu chí chọn kiến trúc.
- **F5 cần sửa:** Host tìm trực tiếp KB `docs` ngày 24/09. Điều 39 tìm được chỉ ghi KG là lớp intelligence/provenance/recommendation/XAI, không phải runtime/checker/executor/promote; không tìm thấy câu `không DB thứ 3`, `PG thuần trước`, `AGE khi cần` hay `Neo4j không bao giờ`. Vì vậy không dùng F5 để loại sản phẩm.
- **Shortlist theo D02 + mức dùng/độ chín hiện tại:** (1) **Cognee + Neo4j** = ứng viên trial số 1: Cognee ~30,9k stars/3,1k forks, có Docker/API/UI/MCP, code graph + custom domain ontology; Neo4j là graph DB trưởng thành, có Community Edition/deployment chính thức. (2) **Graphiti + Neo4j** = ứng viên đối chứng: ~31,1k stars/3,2k forks, temporal/provenance mạnh nhưng OSS là framework và cần tự vận hành surrounding system nhiều hơn. (3) **Hindsight** ~26,5k stars = giữ cho agent memory, không làm business graph chính. (4) **AGE** ~4,8k stars + team nhỏ, lại đụng image PG production = bỏ khỏi shortlist đầu. (5) custom PG graph = bỏ khỏi primary shortlist theo D02.
- **JEV Reference:** `gen-dec-1790226001-T0LHg4y3r0CP99thOmaY` → first trial = `cognee_neo4j` confidence 1.00; bỏ custom PG khỏi primary shortlist = noul 0.91. Bằng chứng phụ, không thay Owner.
- **Qdrant:** giữ nguyên service hiện hữu; không cài pgvector chỉ để phục vụ vòng trial.
- **NEXT:** Hermes phản biện shortlist product-first. Nếu không có blocker thực tế, Host đưa Owner so sánh cuối **Cognee+Neo4j vs Graphiti+Neo4j**; không quay lại framework graph nội bộ.

### P03 · Claude Chat · Reviewer · PARTIAL — giữ kiểm nguồn, quyền riêng tư, tài nguyên; cập nhật phạm vi tại P05
- Based_on `cf270d3`. Scope: Host response P02 + `view.html` §14. Đã đọc đủ.
- **Rút:** kết luận P02 “vòng 1 không DB mới, đi graph PG” — Owner D02 đã thay. **F5 sai nguồn:** Claude trích từ bản nháp Điều 39 (phiên S158), không phải văn bản ban hành — lỗi của Claude, bỏ. §13 view.html đã thay bản cũ cùng commit.
- **ACCEPT:** D02 product-first; trial #1 Cognee+Neo4j, đối chứng Graphiti+Neo4j; graph PG tự dựng ra khỏi primary shortlist; giữ Qdrant; không cài pgvector cho trial. Đúng R1 (A10).
- **Bổ sung 4 bài đo “phù hợp nhất với Incomex”** — đề nghị Host đưa vào §9 acceptance và PROMPT trial (không phải rào cản):
  - T13 dữ liệu thật — PG nghiệp vụ = 0 (contacts/organizations + 25 bảng `os_*` = 0 dòng, đo 24/09); dữ liệu thật ở Lark Base. Qua khi nạp được một lô xuất Lark thật (đã che) và truy được quan hệ ứng viên–đơn hàng–xí nghiệp.
  - T14 dữ liệu cá nhân — Cognee/Graphiti gọi LLM để trích quan hệ ⇒ hồ sơ ứng viên đi qua nhà cung cấp LLM. Trial chỉ dữ liệu che/giả; dữ liệu thật cần Owner gật riêng; ghi rõ LLM provider.
  - T15 tài nguyên — RAM 12GB (trống ~7GB), 12 container đang chạy; đặt trần heap/pagecache Neo4j, đo RAM/CPU lúc nạp; vượt trần → thử FalkorDB (Graphiti hỗ trợ).
  - T16 có sẵn trước graph — Directus đã có bộ bảng CRM tiền tố `os_` (dạng mẫu AgencyOS; 27 bảng kể cả contacts/organizations, 0 dòng). Chốt nơi nhập liệu khách hàng (CRM có sẵn hoặc Lark); graph đọc từ đó, không thay hệ ghi chép.
- **JEV:** giữ “Graph đi đường, JEV nhìn một bước”; điểm cắm trong Cognee = entity alignment · relation classification · confidence routing (thay lượt LLM phân loại đắt). Không gọi JEV thêm: P03 không chọn phương án mới, chỉ thêm bài đo.
- Phản hồi Host 28/09: PARTIAL. Giữ T13–T16 như kiểm nguồn, quyền riêng tư, tài nguyên và không thay hệ ghi chép; T13 chỉ là một ca trong bộ thử hỗn hợp, không định nghĩa toàn mục tiêu. Khả năng gửi dữ liệu ra ngoài phải kiểm cả extraction, embedding và JEV, không đồng nhất dùng Cognee với bắt buộc dùng cloud. Rà giấy phép trước mọi chọn stack theo D05.

### P04 · Claude Chat · Reviewer · PARTIAL — phản biện 28/09; phản hồi Host và mô hình hòa giải tại P05
- Based_on: task `5b64f55` · HEAD `af98926` · đề xuất GPT 28/09 **chỉ có trong chat, Owner chuyển; Host chưa ghi repo** (Host ghi lại để hồ sơ đủ). Scope: toàn bộ đề xuất đó (stack 7 tầng, J1–J5, harness, Shadow→Auto, ranh giới JEV). JEV `gen-dec-1790582600-5ubQHwTXs2EsE0qFKHa1` (lưu ý: tiêu chí do Claude viết, có thể nghiêng — bằng chứng phụ).
- **Fact mới 28/09 (nguồn ở view §15):** F6 Neo4j Community: 1 database người dùng; không RBAC; ràng buộc tồn tại/kiểu/khoá, backup online đều chỉ Enterprise; có unique constraint, full-text + vector index; 5.26 là LTS tới 06/06/2028, bản lịch 2026.x chỉ hỗ trợ bản mới nhất; Data Importer chỉ Aura — self-managed dùng `LOAD CSV`/APOC/`neo4j-admin import`. F7 Neo4j MCP chính hãng `neo4j/mcp`: `get-schema`/`read-cypher`/`write-cypher`, `NEO4J_READ_ONLY=true` tắt ghi. F8 Cognee: `cognify` = LLM trích thực thể/quan hệ; `add_data_points` = model Pydantic, không LLM; MCP hiện là `remember`/`recall`/`forget` (`forget everything=true` xoá toàn bộ memory user sở hữu; `prune`/`delete` cũ đã bỏ ⇒ API còn đổi nhanh). F9 code graph: `codebase-memory-mcp` MIT, 1 binary, nhiều ngôn ngữ, cộng đồng lớn; GitNexus giấy phép PolyForm **Noncommercial** ⇒ Incomex không dùng được.
- **ACCEPT:** Neo4j Community 5.26 LTS — lý do chính: LTS ổn định tới 2028 và cả Cognee lẫn Graphiti đều chạy trên nó ⇒ chốt không hối tiếc. UI nghiệp vụ giữ Directus/Lark; Neo4j Browser cho kỹ thuật. J1–J5; **JEV do pipeline gọi, không để agent nhớ** (đúng A10-R2); Shadow→Assist→Gate→Auto; receipt; ranh giới JEV; jev-harness chỉ học mẫu, không cài gói community; Hermes chỉ kiểm blocker; LanceDB cho lớp Cognee nếu dùng.
- **CHANGE 1 · mục tiêu #1 — ai ghi quan hệ nghiệp vụ.** Đường ghi canonical = **Neo4j thuần**, từ vựng hữu hạn (nhãn + loại quan hệ liệt kê sẵn, có mã), nạp **tất định** từ nguồn nghiệp vụ (Lark → CSV → `LOAD CSV`, một script mapping), **một writer duy nhất**. Cognee/Graphiti = lớp đọc **văn bản** (CV, ghi chú phỏng vấn, email khách) → chỉ sinh **đề xuất**; đề xuất thành cạnh canonical chỉ qua J1/J2 + policy. Lý do: dữ liệu #1 là bản ghi có cột liên kết sẵn, không phải văn bản — cho LLM đọc lại để đoán quan hệ vừa tốn, vừa có thể tự đặt ra thực thể/quan hệ (ngược “hữu hạn”), vừa đưa hồ sơ ra ngoài (T14); schema canonical không nên buộc vào chu kỳ phát hành Cognee (MCP vừa đổi toàn bộ tool). JEV 0,95 (conf 0,93).
- **CHANGE 2 · R2 cưỡng chế.** Agent đọc graph nghiệp vụ qua **Neo4j MCP chính hãng `NEO4J_READ_ONLY=true`**; không trỏ Cognee MCP (`remember`/`forget everything`) vào graph nghiệp vụ. CE không RBAC ⇒ cổng read-only là khoá duy nhất, giống ruleset repo. JEV 0,98.
- **CHANGE 3 · thứ tự.** Hôm nay chỉ chốt **Neo4j**. Cognee vs Graphiti chọn ở B3 bằng bài đo trên văn bản thật, chạy trên **Neo4j instance riêng** (CE 1 database; `forget everything` không được chạm graph nghiệp vụ; JEV noul 0,71). JEV 0,92.
- **CHANGE 4 · mục tiêu #4.** Code graph dùng công cụ chuyên dụng giấy phép MIT (`codebase-memory-mcp` đứng đầu danh sách thử), tách khỏi graph nghiệp vụ; không dùng code pipeline của Cognee; loại GitNexus vì giấy phép. JEV 0,99.
- **Bổ sung T14:** J1 cũng gửi tên/năm sinh/quê ra ngoài (OpenRouter) ⇒ Shadow trên dữ liệu đã che trước; dữ liệu thật cần Owner gật riêng. **Bổ sung backup (Hermes kiểm):** graph nghiệp vụ dựng lại được từ nguồn; phần không dựng lại được = quyết định người + receipt JEV ⇒ dump offline hằng đêm (CE không backup online).
- **Thang bước (một ô làm một lúc):** B1 Neo4j + danh mục quan hệ + nạp 1 lô Lark thật đã che (T13, T15) → B2 J1 Shadow trên trùng lặp ứng viên → B3 lớp văn bản Cognee vs Graphiti → B4 code graph.
- Đề xuất P04 lịch sử: Owner chọn giữa hai đề xuất. Host 28/09: không chuyển đề xuất này thành D chốt Neo4j; Owner đã làm rõ phạm vi và MIT. Phản hồi Host nằm ở P05 dưới đây, nguồn và phương án hợp nhất ở view.html §15.

### P05 · GPT Chat · Host · OPEN — hòa giải P04 theo phạm vi thật và MIT
- Based_on: P04 `356e7da036526dfcaa0a9e6a199c28b70089d602`; HEAD đọc `f0897b576aa06f950a8444eaafe5a4f58e9d4ad0`; chỉ đạo Owner 28/09; nguồn chính thức kiểm trong lượt này tại `view.html` §15.
- Scope: `COLLAB.md` §0/D04–D05/P03–P05/Owner cần quyết; `view.html` §0 và §15, giữ các mục và bố cục hiện hữu. Không sửa luật gốc, không tạo file, không runtime.
- Phần chưa kiểm: runtime của các sản phẩm chưa cài, dữ liệu nội bộ ngoài hồ sơ đã đọc, LICENSE/dependency của release sẽ cài, độ an toàn tích hợp gateway và bài đo Incomex. Chưa nhận review Hermes. Không coi số stars hoặc JEV là chứng minh production.
- **ACCEPT từ P04:** quan hệ đã rõ không cần AI đoán lại; agent không có quyền phá hủy; giữ nguồn gốc/thời gian; che dữ liệu cả với JEV; pipeline gọi JEV theo checkpoint; công cụ code chuyên dụng MIT là ứng viên hợp lý.
- **CHANGE từ P04:** bỏ tiền đề mục tiêu #1 chỉ là bản ghi Lark; không hoãn tri thức phi cấu trúc tới B3; không đồng nhất Cognee với LLM đoán mọi cạnh. Chính tài liệu `add_data_points` có nạp quan hệ cấu trúc không qua `cognify`; phần embedding vẫn phải kiểm đường ra. MCP đọc Neo4j không thay thế retrieval ngữ nghĩa của knowledge layer. JEV đánh giá, không duyệt quyền hoặc bảo đảm sự thật.
- **Cập nhật theo D06:** rút việc dùng MIT làm hard gate. Neo4j CE (GPLv3) trở lại ứng viên graph server mạnh nhất vì miễn phí Community, vendor/ecosystem lớn, LTS và đường nâng cấp rõ. Cognee/Graphiti Apache-2.0 không bị loại chỉ vì không phải MIT; vẫn kiểm điều khoản đúng phiên bản/dependency/model. Không đổi sang engine kém chín chỉ để có nhãn MIT.
- **Phương án hợp nhất:** một lớp tri thức chung có hai đường nhập (quan hệ tường minh / trích xuất-suy luận), tách trạng thái theo nguồn, suy luận, mâu thuẫn/hết hiệu lực. Suy luận có bằng chứng được dùng để gợi ý, không cần biến thành fact chắc chắn; business action/merge/phá hủy vẫn qua policy đã được cấp quyền. Code dùng bộ phân tích phù hợp và nối vào ngữ cảnh bằng định danh nguồn, không thành đảo thông tin.
- **Kết quả tham khảo JEV:** `gen-dec-1790583554-COLXJRUuVnb7y97JLGkL`; trial hỗn hợp nhỏ `mixed_small` p=0.85/confidence=0.80; `labelled_inferences` p=1/confidence=1. Chỉ hỗ trợ thứ tự bài thử/cách giữ suy luận, không xác minh license hay bỏ phiếu chọn công nghệ.
- **Hướng review tiếp:** Claude + Hermes tập trung ba điểm: (a) đủ phạm vi đa nguồn; (b) bề mặt hỏi và quyền ghi tách, kiểm cả tools/call và đường trực tiếp; (c) độ bền dự án — miễn phí self-host, nhịp release, cộng đồng/vendor, backup/export và khả năng thay knowledge layer. Đề xuất khác phải đáp ứng phạm vi + product-first + D06; không yêu cầu Owner chọn giữa tên AI.

### P06 · GPT Chat · Host · OPEN — lựa chọn tối ưu theo D06
- **Graph server:** ưu tiên **Neo4j Community 5.26 LTS** cho trial và làm nền bền: Community miễn phí, GPLv3, native graph, vendor/ecosystem lớn; Neo4j công bố 5.26 LTS nhận critical/security patches tới 06/2028. Không đồng nghĩa Enterprise features miễn phí.
- **Knowledge layer:** ưu tiên **Cognee** trước Graphiti vì phạm vi rộng hơn (structured + unstructured + code), đóng gói API/UI/MCP/Docker và release rất mới; Graphiti giữ đối chứng nếu temporal/provenance quan trọng hơn breadth hoặc trial cho thấy Cognee quá biến động.
- **Vector:** với trial, dùng backend built-in của Cognee thay vì buộc ghép Qdrant; Qdrant hiện hữu giữ nguyên cho workload cũ. Không đổi production PG chỉ để có pgvector.
- **Bề mặt:** business user tiếp tục Lark/Directus; AI/workflow dùng API/MCP qua gateway chỉ-đọc theo mặc định; người kỹ thuật dùng Cognee UI + Neo4j Browser để quan sát. Writer ingestion là service identity riêng, không phải credential của agent.
- **Chống rủi ro dự án chết:** nguồn nghiệp vụ vẫn ở hệ gốc; canonical graph/provenance phải export/dump được độc lập; không giữ logic nghiệp vụ chỉ trong Cognee task/prompt; version pin + backup/export định kỳ. Nếu Cognee chết, thay knowledge layer mà không mất source hoặc graph. Nếu Neo4j CE đổi chính sách về sau, giữ khả năng export sang open graph/CSV và thử backend khác.
- **Graphiti:** không bỏ; là phương án #2 rất khỏe và active, nhất là temporal graph. Nhưng framework-style hơn nên tốn integration hơn cho phạm vi graph hóa mọi thông tin.
- **Hindsight:** để sau cho agent memory, không làm graph chính.
- **FalkorDB:** active và nhỏ hơn Neo4j; SSPL nội bộ có thể dùng nhưng cộng đồng/server ecosystem nhỏ hơn. Giữ fallback nếu Neo4j resource/licensing thực tế trở thành blocker, không ưu tiên số 1.
- **JEV Reference theo D06:** `gen-dec-1790584801-9CITMUfPGm8ENWRwb5nX` chọn `neo4j_cognee` và mô hình `durable_graph_replaceable_layer`, confidence 1. Bằng chứng phụ.
- P06 chưa phải RUN/cài đặt. Chờ Claude/Hermes review; nếu không có blocker, Host đề nghị trial Neo4j CE + Cognee trên dữ liệu hỗn hợp đã che, với export/rollback ngay từ ngày đầu.
- Chưa có đồng thuận cho P05. Chi tiết duy nhất Owner đọc: `view.html` §15. Áp: SAME_COMMIT.

### P07 · Claude Chat · Reviewer · PARTIAL — ACCEPT stack/K1/K3/K4; K2 được Host sửa tại P08
- Based_on `140ceb4` (task) · HEAD `15d3a11`. Scope: §0, D04–D06, P05, P06, view §0 + §15. JEV `gen-dec-1790585399-Fa5OqevSI3TJmWJqujUj`.
- **Nhận lỗi đọc mục tiêu:** P04 đọc “hữu hạn” thành “chỉ bản ghi có sẵn” nên thu hẹp mục tiêu về Lark. Sai. **Rút P04 CHANGE 1 và CHANGE 3.** Cách hiểu đúng đã ghi vào §0 (tầm nhìn đủ nguyên văn; định nghĩa “hữu hạn” ở §0.3). Câu MIT cũ trong §0 mâu thuẫn D06 → đã thay bằng lời Owner mới hơn cùng ngày.
- **ACCEPT P05** (hai đường nhập, 3 trạng thái quan hệ, JEV bổ sung bằng chứng chứ không chứng nhận sự thật, bài thử hỗn hợp ngay từ đầu). **ACCEPT P06 có điều kiện:** Neo4j CE 5.26 LTS là lõi bền + Cognee là lớp thay được; Graphiti phương án B; Hindsight để sau; FalkorDB dự phòng. JEV noul 0,64 — đồng ý nhưng chưa chắc, nên K1–K4 là **bắt buộc trong PROMPT trial**, không phải gợi ý.
- **K1 · Bẫy cấu hình Neo4j CE.** Cognee mặc định dùng **Kuzu — đã bị bỏ rơi (archived 10/2025)**, đúng kiểu “chết giữa chừng” Owner lo. Chế độ multi-user của Cognee chỉ chạy với Kuzu hoặc Neo4j Enterprise/Aura; bật nó với Neo4j CE thì Cognee **âm thầm ghi vào Kuzu** (issue #1873). Chốt: `ENABLE_BACKEND_ACCESS_CONTROL=false` trên một Neo4j CE; phân quyền ở gateway như P06 (agent chỉ đọc, writer dịch vụ riêng, xoá/quản trị tách). Không dùng handler `neo4j_community` (mỗi dataset một container Neo4j, trần 6 ⇒ tốn RAM). Bài đo: sau lần nạp đầu, đếm node trong Neo4j > 0 và không có dữ liệu Kuzu. JEV 0,99.
- **K2 lịch sử · PARTIAL:** Cognee `graph_model` đúng là cơ chế giữ schema chuẩn, nhưng nếu chỉ cho phép quan hệ đã khai sẵn thì trái lời làm rõ mới của Owner. Host sửa thành mô hình hai làn tại P08: canonical hữu hạn theo version + discovery free-form có evidence; ontology `annotate` dùng grounding, không dùng `strict` làm blocker discovery.
- **K3 · Code graph.** Đồng ý Cognee trước (không thêm thành phần; tất định, không LLM). Lưu ý độ bền: nó dựa vào Enola (Apache-2.0, ~183 sao, nhóm nhỏ) — chấp nhận cho trial vì kết quả nằm trong Neo4j; `codebase-memory-mcp` (MIT) là phương án thay sẵn nếu bài đo hỏng hoặc Enola ngừng. JEV 0,97.
- **K4 · Bài đo “Cognee chết”** — biến nguyên tắc chống chết giữa chừng của P06 thành phép thử máy (A10-R2): tắt Cognee → Neo4j MCP chỉ-đọc vẫn trả lời 3 câu hỏi mẫu bằng Cypher thuần; dump/export chạy; nguồn nghiệp vụ không mất gì. Không qua = chưa đạt “lõi bền”.
- Hermes kiểm thêm: RAM khi Neo4j + Cognee API/UI cùng chạy; LLM provider cho `cognify` (qua OpenRouter) + che dữ liệu trước khi gửi.
- **GPT–Claude không còn vênh về stack; còn phải review cơ chế relation discovery P08.** Chờ Claude phản biện một vòng cuối + Hermes kiểm runtime/tài nguyên. Owner cần quyết về tiêu chí hoàn thành vẫn giữ ở cuối file; P08 không tự coi là Owner đã duyệt ngưỡng production.

### P08 · GPT Chat · Host · OPEN — closed-world decision × open-world discovery
- Based_on: chỉ đạo Owner 28/09 trong chat; P07 `b156a631e9e85bfba63d7f3af20ab998a7891c62`; tài liệu Cognee/TypeSafe kiểm 28/09. Scope: §0.1/§0.3, P07–P08 và `view.html` §15; không runtime/PROMPT.
- **Định nghĩa chuẩn:** “hữu hạn” = tập quan hệ **được phép dùng trong một quyết định tại một phiên bản** là hữu hạn; catalog toàn hệ được phép tiến hóa. Câu ngắn: **closed-world decision, open-world discovery**.
- **Cognee phù hợp mô hình hai chiều:** custom graph model có thể đặt edge cố định, `Literal[...]` để LLM chọn trong danh mục, và `str` để LLM nêu quan hệ free-form **trong cùng model**. Không ontology thì relation name được LLM suy trực tiếp; ontology mặc định `annotate` giữ unmatched; `strict` chỉ drop entity không ground và tài liệu nói relationship names không được ontology validate. Vì vậy không dùng ontology strict để chặn discovery; canonical governance nằm ở graph_model/catalog + policy.
- **Lane A · MAP vào quan hệ chuẩn:** nguồn/LLM sinh edge candidate → code lọc theo domain/source-target → đưa shortlist quan hệ đã APPROVED + `none/unknown` cho JEV. Nếu lựa chọn chuẩn đủ mạnh thì **ưu tiên đề xuất/map**; không cần AI phát minh nhãn mới. Danh mục lớn thì shortlist theo domain/embedding trước, không ném toàn catalog cho JEV.
- **Lane B · DISCOVER quan hệ mới:** khi không relation chuẩn nào đạt ngưỡng hoặc raw extraction phát hiện relation free-form có evidence, giữ nó ở trạng thái `PROPOSED`, không ép sang type gần nhất. Gom các đề xuất tương tự + provenance/tần suất/ví dụ. LLM/Cognee được **đề xuất tên + mô tả**; JEV không phát minh type mới vì answer space của JEV phải hữu hạn — JEV chỉ đánh giá các câu bounded như: “có khác type hiện hữu không?”, “evidence có hỗ trợ không?”, “có hữu ích để ra quyết định không?”, “domain/source-target phù hợp không?”. Human approve → type mới vào catalog version N+1; reject/merge/deprecate giữ audit.
- **Ngưỡng 75%/85% của Owner = seed cho trial, chưa phải production:** (a) existing relation khoảng 0,75 có thể là ngưỡng ưu tiên đề xuất; (b) novel-candidate khoảng 0,85 có thể là ngưỡng **đưa vào hàng chờ định nghĩa mới**, không tự approve. Phải định nghĩa rõ đang đọc `choice probability` hay `confidence`; TypeSafe nói answer/probability cho “what”, confidence cho “whether to act”, và threshold tùy hậu quả. Trial phải hiệu chỉnh riêng theo relation/domain trên case đã gán nhãn; không dùng một số toàn hệ.
- **Không để catalog thành blocker:** edge/candidate mới vẫn được lưu/retrieve dưới trạng thái proposal/inference kèm evidence; nó chưa được dùng như canonical relation cho merge, mutation hoặc automation rủi ro cao. Như vậy graph vẫn học được trước khi ontology theo kịp.
- **Versioning tối thiểu:** mỗi relation type chuẩn có `code + version/status`; mỗi edge giữ relation code/version nếu canonical, còn candidate giữ raw label + evidence + discovery metadata. Khi catalog đổi, không rewrite lịch sử mù; remap theo migration/review khi cần.
- **Bài thử mới T17:** chuẩn bị dữ liệu đã che có (1) relation đã khai sẵn; (2) cách diễn đạt khác nhưng map được về relation cũ; (3) relation thật sự chưa có. PASS khi 1–2 ưu tiên đúng relation chuẩn, ca 3 đi lane PROPOSED chứ không bị ép/loại; reviewer duyệt ca 3 thì lần nạp sau hệ thống ưu tiên relation mới. Đo cả false-map và false-new-type.
- **Nguồn kỹ thuật:** Cognee custom graph model cho fixed/Literal/free-form edges; ontology annotate/strict và giới hạn relation validation; TypeSafe confidence routing; entity alignment cookbook. GitHub issue #1873/#2098 chỉ dùng để kiểm rủi ro backend Kuzu/Neo4j, không liên quan định nghĩa hữu hạn.
- **JEV Reference:** `gen-dec-1790587126-gvt9Oee3rVMMcZcafzRX` → `versioned_finite_discovery` và `calibrated_two_lane`, confidence 1. Bằng chứng phụ.
- **NEXT:** Claude review P08 đúng một vòng cuối theo A5; Hermes kiểm K1/K4/RAM và khả năng cấu hình Neo4j thật. Nếu Claude ACCEPT/PARTIAL không còn vênh nguyên tắc và Hermes không có blocker, Host mới soạn PROMPT trial; chưa READY/RUN.

## Con trỏ
- Luật: ../../AGENTS.md; kỹ thuật và Owner View: ../../README.md §11–12.
- Nền JEV: ../done-tasks/jev-integration/COLLAB.md và SKILL.md.
- Bối cảnh VPS: ../done-tasks/vps-clean-20-9-26/COLLAB.md.
- Gateway Agent: ../hermes-joint-workspace/COLLAB.md — việc độc lập.

## Owner cần quyết
- 28/09 · P07 · §0.2 “Thế nào là hoàn thành” vẫn là lời mở việc 24/09 (đã xong). Đề xuất thay bằng: (1) hội đồng đồng thuận stack, Owner gật; (2) chạy thử trên dữ liệu hỗn hợp đã che (liên kết Lark + ghi chú chăm sóc khách + trao đổi quy trình + một đoạn code): hỏi được “khách/ứng viên này liên quan gì, nên làm gì tiếp” kèm nguồn; JEV được máy tự gọi ít nhất một chỗ; tắt Cognee vẫn đọc được graph; (3) cài thật chỉ sau khi Owner gật kết quả chạy thử. **Đề xuất: gật.**
