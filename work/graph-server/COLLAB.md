# COLLAB — graph-server
Tên việc: Graph Server — Business × JEV × Code

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — chỉ đạo trực tiếp ngày 24/09/2026: tạo `work/graph-server`, đưa nội dung lên để hội đồng góp ý, theo bốn mục tiêu dưới đây. Chưa duyệt công nghệ hoặc triển khai VPS.

### 1. Mục tiêu
Nguyên văn User, giữ thứ tự ưu tiên:
1. Tạo ra các mối quan hệ về Graph đối với business (khi các mối quan hệ là hữu hạn, chứ không phải quan hệ vô hạn kiểu mạng xã hội.
2. Kết hợp tốt nhất với Jev để đảm bảo Graph truyền thống và Jev bổ sung tốt nhất cho nhau theo các hướng dẫn mới nhất của typesaveai và nhà sáng lập của nó **Diogo Almeida**.
3. Định hướng ứng dụng các skill, frame chính thức của Jev để có thể tận dụng xu thế phát triển thêm Jev trong tương lai (ý là, Jev là 1 xu hướng hiệu quả, giờ mới chỉ bắt đầu, Incomex cần chuẩn bị để không tụt hậu trong xu hướng này)
4. Tự Dựng lại mối quan hệ về về code để các Agent/ AI có thể hiểu nhanh hơn khi hệ thống phức tạp lên.

Bối cảnh nguyên văn User: “Gốc rễ nhất là chúng ta đã dọn VPS còn hơn 50GB để cho việc này.”

### 2. Thế nào là hoàn thành
Phạm vi lượt giao hiện tại, nguyên văn User:
- “tạo 1 task tên work/graph-server”
- “Đưa các nội dung lên đây theo đúng quy đjnh để hội đồng bắt đầu có ý kiến.”

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Chỉ tạo hai file trong task: COLLAB.md điều phối và view.html là tài liệu chính duy nhất. Không tạo PROMPT, file review, bản nháp hoặc pipeline phụ.
- Giữ đủ các nhóm lựa chọn đã thảo luận; phân biệt nguồn kiểm chứng, đề xuất và điều chưa kiểm. Đề xuất cũ không phải quyết định Owner.
- Giữ hướng PostgreSQL/pgvector. Yêu cầu một PostgreSQL vật lý duy nhất chưa được xác nhận; không đồng nhất điều đó với một nguồn chuẩn cho mỗi dữ liệu.
- Giữ đúng thứ tự mục tiêu. Schema/tiêu chí nghiệm thu/kiến trúc trong HTML là đề xuất chờ review, không thêm mục tiêu User.
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
GS | HỒ SƠ REPO VÒNG 1 XONG · OWNER VIEW CHECK DỪNG (AUTH) | Chưa chốt công nghệ; chưa có PROMPT/READY/RUN | NEXT: Claude + Hermes có thể review trực tiếp repo; Host chưa được phép báo Owner View PASS cho tới khi kiểm được nội dung sau đăng nhập.
- Based_on mở việc: `37ae3fe22bc37894242506e4477b055d32fdc540`; GS02 hòa giải trên HEAD hiện hành, commit chen ngang không chạm task này.
- Đã đọc AGENTS.md → COLLAB.md gốc → README.md → work/README.md; áp khuôn MT3 hiện hành.
- Nghiên cứu cập nhật 24/09/2026: TypeSafe official skill/blog; pgvector; AGE; Cognee; Graphiti; Hindsight; Neo4j vector; GraphRAG. Link nguồn ở `view.html` §12.
- Owner View check sau commit `3b909e0c22d554433fdee8c49498c5cbb3cf1701`: gọi đúng URL chuẩn `/knowledge/modules?task=graph-server`, HTTP shell 200 nhưng Directus trả 401 và UI dừng ở Login; không thấy nội dung/revision ⇒ **DỪNG nghiệm thu Owner View, không báo PASS giả**. Repo/diff vẫn PASS.
- Áp: SAME_COMMIT.

## Quyết định Owner
- D01 · 2026-09-24 · Owner cho phép mở đúng task graph-server, tập hợp nội dung để hội đồng góp ý, giữ bốn ưu tiên và bối cảnh VPS. Không có quyết định chọn stack/cài đặt trong lệnh này.

## Ý kiến hội đồng
### P01 · GPT Host · OPEN — giả thuyết vòng 1, chờ Claude/Hermes phản biện
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
- Phản hồi Host: —

## Con trỏ
- Luật: ../../AGENTS.md; kỹ thuật và Owner View: ../../README.md §11–12.
- Nền JEV: ../done-tasks/jev-integration/COLLAB.md và SKILL.md.
- Bối cảnh VPS: ../done-tasks/vps-clean-20-9-26/COLLAB.md.
- Gateway Agent: ../hermes-joint-workspace/COLLAB.md — việc độc lập.

## Owner cần quyết
- P02/D02 (đề xuất Claude · chờ Host GPT hoà giải): vòng 1 KHÔNG chọn DB mới (không Neo4j/Cognee/Graphiti/Hindsight/AGE) — đi bằng graph PG đang có theo Điều 39; vector dùng Qdrant có sẵn; việc đầu tiên = từ điển quan hệ hữu hạn 3 quy trình + đổ node nghiệp vụ đầu tiên từ Lark Base. **Đề xuất: gật.**
