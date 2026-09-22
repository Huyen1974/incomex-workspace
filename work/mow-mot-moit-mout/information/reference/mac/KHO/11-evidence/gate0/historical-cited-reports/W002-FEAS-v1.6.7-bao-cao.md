# W002-FEAS v1.6.7 — Báo cáo nộp PM

Ngày 08/09/2026 · Codex · D1 + D2 SUBMITTED / PM REVIEW · PARTIAL

Đã cập nhật trực tiếp file HTML gốc và kiểm đọc lại; backup nguyên v1.6.6 đã xác minh khớp byte.

Đã sửa thiết kế theo chỉ đạo GPT Chat: việc tìm và so khớp do T1 bằng query/tool/index có bằng chứng; Agent chỉ hỗ trợ ý nghĩa và những trường hợp mơ hồ. Chưa đủ evidence để chốt danh mục chuẩn, semantic path, quyền và admission runtime. Gate 0 vẫn DOING.

Phạm vi: đọc PG catalog/source/config, đọc metadata Qdrant, đối chiếu source và một bundle đang deploy; chạy một batch SELECT trên metadata nháp. Không DDL/DML, gọi hàm nghiệp vụ, chạy Flow, nâng cấp hoặc thay ứng dụng production. Việc sửa HTML và tạo báo cáo là thay đổi tài liệu được yêu cầu.

[Thiết kế v1.6.7](cau-truc-he-thong-v1.6.7.html) · [Evidence có cấu trúc](W002-FEAS-v1.6.7-evidence.json) · [16 ca benchmark](W002-FEAS-v1.6.7-benchmark.csv)

**1. D1 consumer trace.** job_queue: 13 dòng pilot, lần cập nhật/heartbeat cuối tháng 5; chưa truy được executor hiện hành. event_outbox có producer system_issues đang enabled và sự kiện mới 08/09; event_read do producer ghi implicit_self nên không chứng minh delivery/ACK. event_pending rỗng, consumer UNKNOWN. binding_registry là lookup normative còn validator tham chiếu, chưa là workflow binding engine. Không tuyên bố toàn bộ đã chết từ bounded scan.

**2. 15 Flow exec.** Đọc và phân loại 15/15: 13 tự tính mã bằng MAX(last code)+1, 2 chuyển tiếp payload. Cả 15 thuộc Flow inactive; đề xuất RETIRE CANDIDATE, chưa xóa hoặc kích hoạt. Creator không được dùng thay maintenance owner. Chi tiết từng ID ở phụ lục.

**3. 8 business-rule locations.** KEEP 1 / MOVE 4 / RETIRE candidate 1 / UNKNOWN 2; 6/8 có đề xuất. MOVE chỉ phần quyết định nghiệp vụ, không chuyển cả file về PG. Validation có 327 non-null nhưng 321 là {} và chỉ 6 nonempty.

**4. Auth authority.** User proxy chuyển cookie/Authorization sang Directus. WCR source dùng static service token và nhận approved_by từ body; bundle apply đang deploy cũng có handler này. Nginx proxy /api/workflows/ tới Nuxt. Chưa thấy actor check trong handler apply/status đã đọc; global/upstream enforcement và request thực tế chưa đủ bằng chứng. Đây là blocker cần proof deny/actor/audit, chưa kết luận lỗ hổng khai thác. Không gọi POST.

**5. Eligible canonical Field N.** N = UNKNOWN, không phải 0 hay 1.497. Có 3.968 cột bảng vật lý public, 1.497 metadata fields Directus; 1.438 khớp column/view metadata và 59 cần phân loại alias/virtual/stale. Con số 9.424 information_schema có cả view. Chưa có mapping approved để biến bất kỳ mẫu số nào thành canonical Field Definitions.

**6. Business subject/object catalog.** meta_catalog và 11 collection_field_standards phục vụ danh mục/chuẩn kỹ thuật. taxonomy/facets và species/collection mappings có phần cấu trúc dùng lại được; chưa chứng minh stable business subject identity/authority. Kho nháp sua_re_khai_niem_nhap có 14 concept, 6 kinds, 7 Field; UI mappings 30 current không tự là MOIT/MOUT where-used.

**7. PG search extensions.** Trong DB directus: pg_trgm, vector/pgvector, unaccent NOT INSTALLED; version/use N/A. Có plpgsql 1.0, pgcrypto 1.3, btree_gist 1.7, postgres_fdw 1.1. Không tìm thấy index trgm/vector/tsvector trong inventory; index tên vector_sync là btree trạng thái. Không suy cho mọi DB.

**8. Qdrant actual.** 1.16.3, hai collection green: production_documents 20.112 points và iu_core_iu_chunks 149 points; 1.536 chiều, Cosine; payload_schema {} nghĩa không payload index khai báo. Agent Data KB search dùng production_documents, chưa là catalog resolver. Kho IU chưa truy được consumer hiện hành, last use UNKNOWN. Không dump vector/payload.

**9. Semantic-index recommendation.** NEED_MORE_EVIDENCE. Ưu tiên proof tái sử dụng Qdrant đang có trước thêm pgvector. So ACL/filter, stable IDs, freshness/rebuild/restore, exact target support và chi phí vận hành; PM chọn một đường chính. PG giữ canonical truth; vector chỉ projection.

**10. T1 Resolver.** Đã thêm tại #t1-resolver: Search Brief → RZ0 quyền/phạm vi → RZ1 loại/anchor → RZ2 key exact → RZ3 approved alias → RZ4 lexical → RZ5 hard contract → RZ6 semantic candidates → RZ7 full diff/recheck → RZ8 shortlist ≤5 → admission. TARGET, chưa là endpoint đang chạy. Không thêm T6, framework hoặc product code.

**11. Primary Search Anchor.** Field: concept + subject/GLOBAL_SHARED; MOIT: write target + operation; MOUT: report subject + sources; MOT: work case + reads/writes/effects; MOW: outcome + participants; Trigger/Condition/NTGV theo event/evaluation/assignment domain. Unknown anchor không cho lọc cứng mất ứng viên.

**12. Resolver Benchmark V0.** Native exact SQL batch trên 14 khái niệm nháp, 16 cases. Trong 12 positive retrieval cases: 8/12 Recall@5 = 66,7%; 4 misses bỏ dấu/typo/cách nói/mô tả. Shortlist 0–1, trung bình 0,625. Toàn batch docker+psql 174,91 ms, 0 LLM calls trong query. Full T1 false-reuse/false-new/NEEDS_DECISION/latency = NOT MEASURED. B12/B13 là phản ví dụ exact≠reuse, không tính thành lỗi admission thực đo. Đây chưa là full Resolver Benchmark hoàn thành.

**13. Cold-start sample.** Đã rà toàn bộ 14 provisional concepts: key/description/alias 14/14, contract_ref 0/14, promoted_at 0/14. Có 7 Field nhưng chưa có cấu trúc datatype/unit/primary-subject/owner/version đủ kiểm. Completeness approved, duplicate rate canonical và unknown rate trên canonical population đều UNKNOWN. Chưa lấy mẫu canonical vì N chưa xác định; không giả mẫu 200 từ metadata Directus.

**14. Gray-zone matrix.** Đã phân biệt display-only, thêm optional/required field, thay write target/operation/contract, cùng cấu trúc khác nghĩa, cùng family khác unit/subject và trường hợp chưa đủ bằng chứng. Rejected candidates còn được giữ cho new version/variant; không làm CREATE bằng cách lọc mất họ hàng.

**15. Negative Search Evidence.** Kết luận chưa có phải lưu brief/normalization/profile/query/filter/scope/catalog/index/model revisions, stages executed/skipped, candidates và lý do loại, coverage/freshness, errors, final conclusion. Permission hạn chế/lỗi/timeout/index cũ không là bằng chứng không tồn tại toàn kho; final admission phải recheck trong transaction.

**16. Reuse Economics.** CREATE phải bác bỏ reuse/version/variant bằng material diff. Duyệt theo rủi ro/ảnh hưởng, không cho CREATE rẻ hơn chỉ vì ít click. Đo thời gian, số quyết định người, nơi phải sửa, số definition mới và chi phí sửa reuse sai; không chỉ đếm dòng code.

**17. VS1-R.** Bổ sung ba tình huống đối kháng về Field tương đương khác tên, MOIT gần giống có material diff và label gần nhưng subject/contract khác; giữ BACKLOG, cùng VS1 sau MIG1 và preconditions. Có tiêu chí không tạo mới khi search thiếu/lỗi và không reuse từ score/label.

**18. Feasibility Question Register.** 20 câu: ANSWERED 8 / DEFERRED WITH REASON 6 / BLOCKER 6. Sáu blocker: CAT-01, CAT-02, SEA-02, COL-01, TST-02, PERM-01. ANSWERED ở mức thiết kế không đồng nghĩa runtime PASS; các defer ghi Gate và lý do.

**19. FZ3/FZ4/FZ5.** FZ3 yêu cầu đường T1/resolver khả thi trên target; FZ4 gồm VS1 và VS1-R; FZ5 phải giải material catalog/resolver/admission questions, không chỉ có platform inventory. Giữ FZ1–FZ7, không thêm FZ8.

**20. Object-card cleanup.** Rà 12 card, đồng bộ baseline và ranh giới đã chốt, tách việc kiểm UI ở R1–R8 khỏi quyết định thiết kế đã có. A02/D04 vẫn OPEN ở R6; không tự quyết thay Owner/PM.

**21. Trạng thái.** D1+D2 SUBMITTED / PM REVIEW, kết quả PARTIAL. Gate 0 DOING; MIG1, VS1+VS1-R, RULE-SYNC-01, W003/R1 BACKLOG. Chưa tự mở migration, build, test tác động thật hoặc nghiệm thu Gate.

**22. File/version/backup/delta.** v1.6.7, ngày 08/09/2026. 459.121 → 477.857 byte (+4.08%); 1.453 → 1.505 dòng. Backup nguyên v1.6.6 được lưu trước sửa trong thư mục backup cạnh file gốc, tên cau-truc-he-thong-v1.6.6-truoc-resolver-2026-09-08.html. SHA-256 bản gốc: 8be404e89ae1ef771cb5ac1d6b6cf18c0fc7c3b5412190d067746d8ddc4e72b4. Giữ nguyên JavaScript tương tác của tài liệu; chỉ sửa nội dung thiết kế. Phần lịch sử được dẫn tới backup để hạn chế phình file.

## Phụ lục E04 — 15 exec operations

Tất cả inactive; maintenance owner và lần thực thi cuối UNKNOWN. Creator có mặt không chứng minh ownership. Tất cả là inline custom script (I7 legacy), không là config native. Phân loại đề xuất RETIRE CANDIDATE cần kiểm where-used/output contract trước hành động.

| Flow | Flow ID | Operation ID | Purpose | Replacement candidate |
|---|---|---|---|---|
| [AUTO-ID] DOT Tools | 0551e29b-8559-4495-ba1f-821f4a7fd81d | 90cab902-cc5f-4010-a2f6-8fdea2f02084 | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] Checkpoint Types | 14da71a1-d39a-4d6d-9d7c-9b1eab360773 | fce761c3-a001-4321-80ba-2c3b0ccea94f | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] Collections | 90d02156-b62a-4b1b-a1f0-b4e1b70c8f33 | 086e74a1-ce57-4368-8df5-8580de7756a0 | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] Modules | e8df593c-0578-4fe4-abdb-69cf12507032 | 08df5552-856a-4e2a-a24a-8c0c49810c25 | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] Checkpoint Sets | 5ff2dd48-40af-4fa4-8cc7-a3a4ddb87ba7 | 507d4b52-4e8d-49af-9fd1-59455f0119cc | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] Agents | e7483fee-658d-44aa-acaf-774713e93e2a | 5e87b932-35f4-4fd6-95a3-3cbf3ec5a4f3 | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] WCR | dd4dd0d5-4ee8-468a-af88-c5339cdf57c5 | 67ff5196-f4ba-465a-8b6e-010b1861a102 | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] Workflow Steps | cf9ddcbd-a03a-4825-91d9-a8bd24e1e77a | 77720f58-e08d-482f-8820-730e64d1d34c | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] Pages | f01051a2-24c2-44b1-b677-ca4a057066fc | dd1cd9de-af0e-4204-b4fd-b488ddc21d6e | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] Meta Catalog | 92333788-ae30-4a14-af82-c54d5b14dcf9 | 085b06dc-9e14-46ca-b2fe-834229f29d67 | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] Table Registry | e8925ae3-96a4-479f-98eb-347b48acf7b4 | cb82dec7-9d08-4861-a069-fcaa05bc959b | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] Tasks | 7b4988ed-6615-48ad-a413-98d2e37e7c07 | d6794e59-9b77-43fc-878f-ec874330a253 | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [AUTO-ID] Workflows | a89de048-7638-4622-a3b2-133ccc3958fc | d9870413-841a-44fc-bbf6-090e49cd8ae2 | MAX(last code)+1 and format | PG identity/sequence + format after collision/compatibility review |
| [DOT] Knowledge Delete from Agent Data | 3ffb797d-06d2-432f-ab9c-0fb5f76909ca | 8a70629f-bec3-4c27-ba78-6bc4031965d9 | Pass through trigger payload | Native Flow transform/direct mapping after output contract check |
| [DOT] Knowledge Sync to Agent Data | dca43a81-d642-4734-892d-e22fb352a947 | bfc984f7-cf14-477b-a09d-f37f1644ec90 | Pass through trigger payload | Native Flow transform/direct mapping after output contract check |

## Phụ lục E06 — kết quả retrieval

Expected chỉ dựa trên kho nháp đã đọc, chưa là nhãn admission được PM duyệt. B12/B13 giữ để chỉ ra rủi ro khác runtime/unit; loại khỏi mẫu số positive recall.

| Ca | Câu tìm | Expected retrieval | Actual candidates | Vào recall? |
|---|---|---|---|---|
| B01 | field.so_phut | field.so_phut | field.so_phut | Có |
| B02 | phút | field.so_phut | field.so_phut | Có |
| B03 | PHÚT | field.so_phut | field.so_phut | Có |
| B04 |   phút   | field.so_phut | field.so_phut | Có |
| B05 | so phut thuc hien | field.so_phut | [] | Có |
| B06 | WF | workflow | workflow | Có |
| B07 | Số phút thưc hiện | field.so_phut | [] | Có |
| B08 | thời lượng một task | field.so_phut | [] | Có |
| B09 | Tổng phút | field.tong_phut_congdon | field.tong_phut_congdon | Có |
| B10 | ngày tạo | field.ngay_lap | field.ngay_lap | Có |
| B11 | ngày sửa đổi | Chưa có positive target | [] | Không |
| B12 | trạng thái | field.trang_thai_quy_trinh | field.trang_thai_quy_trinh | Không |
| B13 | phút | Chưa có positive target | field.so_phut | Không |
| B14 | người nhận hàng | role.nguoi_thuc_hien | [] | Có |
| B15 | khoi | org.khoi | org.khoi | Có |
| B16 | CCCD | Chưa có positive target | [] | Không |

## Dấu vết nguồn và giới hạn

E04: public tables/functions/triggers + directus_flows/operations/permissions; source `/opt/incomex/docker/nuxt-repo/web`, extension `/directus/extensions/l2-checkpoint-guard`, bundle apply `/opt/incomex/deploys/nuxt-output/server/chunks/routes/api/workflows/change-requests/_id/apply.post.mjs`, Nginx config. Bounded scan chưa thấy caller không chứng minh không có caller ở mọi nơi. DB counts là snapshot, các lần đọc khác nhau không là một snapshot transaction toàn hệ.

E05: pg_extension/index definitions; meta_catalog/taxonomy/species/collection registries; 14 provisional concepts và UI usages; Qdrant authenticated GET metadata; Agent Data running config/source. Per-point embedding provenance và IU last consumer use chưa có proof.

E06: equality/lower/btrim và JSON alias expansion trong PG, một batch 16 query terms, BEGIN READ ONLY, timeout 8s, ROLLBACK. Không semantic search hay admission implementation.

Hướng kỹ thuật được đối chiếu với tài liệu chính thức: [PG trgm](https://www.postgresql.org/docs/current/pgtrgm.html) và [unaccent](https://www.postgresql.org/docs/current/unaccent.html) cho lexical lookup; [Qdrant filtering](https://qdrant.tech/documentation/search/filtering/) và [hybrid search](https://qdrant.tech/documentation/search/hybrid-queries/) cho phương án candidate retrieval; [pgvector](https://github.com/pgvector/pgvector) cho phương án so sánh; [Directus operations](https://docs.directus.io/app/flows/operations) để phân biệt built-in và script; [Nuxt upgrade](https://nuxt.com/docs/4.x/getting-started/upgrade) cho rehearsal. Tài liệu latest không chứng minh phiên bản đang cài hỗ trợ mọi khả năng đó.

Kiểm tài liệu: không ID trùng, không fragment link nội bộ thiếu đích, thẻ HTML lồng hợp lệ, JavaScript giữ nguyên; đã xem bố cục trên trình duyệt. Các link lịch sử ngoài file được giữ nguồn, chưa kiểm khả dụng từng URL cũ.
