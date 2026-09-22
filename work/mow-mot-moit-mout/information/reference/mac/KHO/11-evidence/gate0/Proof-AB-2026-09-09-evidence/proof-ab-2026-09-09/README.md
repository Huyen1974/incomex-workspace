# Proof A tiếp nối / Proof B giao nhau / C triage · 09/09/2026

**SUBMITTED / PM REVIEW · PARTIAL.** Retrieval bốn ô của lượt trước đã được PM ACCEPT/DONE theo lệnh mới. Lượt này tạo được một lát cắt khai báo và ghi nháp có quyền thật trong lab, đồng thời phát hiện cổng ghi chưa cưỡng chế đủ contract/revision. Chưa chứng minh UI tích hợp, published MOW hoặc runtime. Factory DONE; FEAS PARTIAL; Gate0 DOING; O1–O3 NOT VERIFIED; R1 chưa mở.

## Chặng nào đã có bằng chứng

| Chặng | Kết quả | Evidence / giới hạn |
|---|---|---|
| Intent → Search Brief | Đã làm bởi Codex từ câu yêu cầu; 6 yêu cầu nguyên liệu gồm 3 vật liệu chính, một paraphrase, hai phản ví dụ | `intent.json`, `search-brief-agent.json`. Không có final JSON đáp án do Owner đưa. Khung schema/fixture do Agent chuẩn bị, không coi sản phẩm tự dựng được cả chuẩn |
| Tìm vật liệu | A1 PG nguyên cấu hình đã nhận; 6 lookup trên 14 provisional concepts | `retrieval-results.json`, SQL/config nguyên hash. Không lặp benchmark/tuning hoặc dọn kho mở rộng |
| Contract / quyết định reuse | 4/6 reuse decisions đúng, 2/6 needs_decision; 3 Field IDs riêng; 0 new Field | `catalog-readback.json`, `admission-decisions-agent.json`; nghĩa TEST ONLY do PM cho phép, không promote source. Giờ không nhận phút; sửa đổi không nhận ngày tạo |
| Validator | Joi17.13.3 có sẵn trong image Directus: 2 khai báo hợp lệ được nhận, 11 biến thể sai bị từ chối | `validator-inputs.json`, `validator-output.json`; profile được đọc qua service API từ PG. Đây là validator ngoài cổng trong test harness, không hệ T1 production |
| Draft write | Service có policy riêng ghi 1 form/MOIT, 1 MOT, 1 MOW; PG readback có đúng refs | `integration-results.json`, `final-capture.json`; model TEST ONLY. MOW/MOT mới chỉ kiểm cột/FK tối thiểu, không full canonical lifecycle contract |
| Dùng lại ghi chú / version | Đường native cuối: POST `/versions/:id/save`, GET item với `version=notes-v2`; main 1 input, version 2 inputs, Field count vẫn3, MOT binding main không đổi | `version-r4-result.json`. Giữ lỗi thử r1–r3; r3 dùng sai PATCH làm main đổi và đã khôi phục fixture. Content version là draft delta trên main mutable, không immutable published MOW version proof |
| Human/service authority | Tester và service đúng quyền ghi được; outsider/scope/spoof/system date/invalid value/FK sai bị chặn trong các ca đã chạy | HTTP raw + PG before/after + audit. Không dùng Owner/admin cho business writes. Không full Proof B hoặc delegated authority |
| Retry | Cùng payload/ID/Idempotency-Key → HTTP400 RECORD_NOT_UNIQUE; không thêm bản ghi | Chỉ chứng minh PK không nhân đôi khi caller giữ ID. Chưa có replay response/idempotency protocol hoặc race/concurrent retry proof |
| Stale revision | **FAIL:** If-Match stale trên item PATCH vẫn HTTP200, thay title | Actual before/after và audit. Chưa kiểm mọi primitive concurrency của Directus; native promote/mainHash chỉ đọc source |
| Nested fake contract | **FAIL:** contract_ref giả trong forms.schema vẫn HTTP200, được lưu | Joi chặn nhưng API chưa dùng Joi profile này. FK profile_ref ngoài JSON chặn đúng không thay bảo vệ refs bên trong |
| Checkpoint/resume | Có checkpoint trong PG; kiểm fresh-Agent độc lập trong artifact riêng | `fresh-agent-report.md`, `resume-comparison.json`; không suy full T0 recovery/runtime |
| UI | **NOT RUN integrated UI**; source gap cụ thể đã xác định | `ui-gap.md`, current compiled source. UForm submit vào inbox, chưa có contract/version/write-target/readback path cần thiết; không tạo renderer/page/adapter để vượt gap |
| Release/runtime | **NOT COMPLETED / NOT RUN** | Không promote, không giả cờ published; C chỉ triage source, không gọi queue primitive |

**Một dòng end-to-end:** intent → tìm/read contract → khai báo → Joi → authenticated Draft → PG readback/checkpoint có evidence; nối validator vào cổng, concurrency, UI, governed publish và runtime chưa khép kín. Không nghiệm thu toàn hệ từ lát cắt này.

## Tử số/mẫu số, công người và code

- 6 yêu cầu nguyên liệu; 4 quyết định reuse (phút, ngày tạo, ghi chú, paraphrase phút), 2 needs_decision (mốc sửa đổi, đơn vị giờ). 3 Field IDs có sẵn trong fixture trước yêu cầu thêm note. Một form family, một content version mới cuối cùng. Không tự dời binding cũ.
- False-reuse **0/4** trong các quyết định có nhãn TEST ONLY và contract đầy đủ do Agent đọc; **không** là tỷ lệ safety của server. Hai request hostile/stale vượt cổng được báo FAIL riêng. False-new **N/A**, vì không có quyết định tạo Field mới. Không suy negative nào là NOT FOUND toàn kho; legacy relevant sets vẫn chưa gán nhãn đủ.
- Hỏi Owner/chủ quản mới: **0**, vì PM đã chốt nghĩa fixture. Không suy công người bằng0: dữ kiện, nhãn và chỉ đạo trước đó là đầu vào do người cung cấp. Human active effort/wait time/total token **NOT MEASURED**.
- PG lookup dùng **0 LLM calls/tokens**. Main Codex chuẩn bị source/config/harness/khai báo và adjudication; một Agent độc lập đọc lại checkpoint. Số lượt gọi/token parse/review của toàn phiên không có telemetry riêng; không gọi đây là hệ đạt98% AI.
- Timing `measured_harness_create_draft_ms` chỉ đo chạy ba POST từ JSON đã chuẩn bị đến Draft, **không** đo đầy đủ ý tưởng→Draft. Setup schema/seed API đo riêng trong `seed-ready.json`; bootstrap/pull/cấu hình/source/debug là công chuẩn bị bổ sung. Ý tưởng→published **NOT COMPLETED**.
- Product code/component mới **0**; .vue/page/rebuild riêng cho form **0**; adapter/runner mới **0**. Có 14 file harness/chuẩn bị/đo/dọn lab, tổng 504 dòng (không gồm bản script lỗi lưu lịch sử hoặc script biên tập báo cáo), cùng config/profiles/8 collections TEST ONLY; xem `code-inventory.json` để biết file và số dòng. Không gọi preparation zero-code. Dùng lại PG A1/unaccent/pg_trgm, Directus CRUD/policy/field validation/FK/Activity/Revisions/Content Versions và Joi. Nuxt chỉ đọc source trong lượt này, không tính là UI đã chạy dùng lại thành công.

## Đọc các thất bại đúng phạm vi

Native field validation và FK bảo vệ một phần dữ liệu; JSON profile không tự được chạy tại `/items/forms` hoặc native `/versions/:id/save`. Cần cổng giữ cùng contract và enforcement, bao gồm đường ghi service/version; một validator do Agent tự gọi trước request có thể bị bỏ qua. `contract_ref` tồn tại và resolve được chưa đủ.

`If-Match` không được thực thi trên đường item PATCH đã dùng. Source VersionsService có hash-check khi promote, nhưng đó không tự là optimistic locking cho mọi Draft write. Không kết luận Directus hoàn toàn không có giải pháp; cũng không viết wrapper để che thiếu này trong lượt thử.

Directus phiên bản thực11.5.1 không nhận caller-supplied ID khi create version. Native service tự tạo hash, đòi policy cho metadata đó. Đã sửa đúng config/envelope và cuối cùng dùng POST version/save theo exact source, giữ toàn bộ lần thử trước. Không bỏ lỗi của Agent khỏi lịch sử hoặc đổi nhãn expected để đạt.

Activity/revisions phân biệt user IDs của human/service. X-Request-ID của harness chưa được chứng minh persist trong Activity: nối evidence bằng item ID, actor, thời điểm và activity/revision ID, không claim full correlation/delegation audit. Trace trong raw requests có body đã khử password/token.

## Proof C và đúng một quyết định tiếp theo

[C triage](./runtime-triage.md): PG có enqueue/atomic claim/ACK, nhưng chưa tìm được Directus approved bridge + executor cho chuỗi MOW. C1 NOT FIT CURRENT trong đường đã truy; dynamic/external bridge ngoài phạm vi UNKNOWN. Tối đa hai library được xét: pg-boss12.30.0 và Graphile Worker0.17.3. Chỉ đề nghị pg-boss làm ứng viên C2 thử sau nếu PM giao; không cài, không viết runner, không chạy hai queue độc lập. Không nghiệm thu runtime.

**Đúng một việc đề nghị PM quyết:** giao một phép thử tiếp theo trên chính lát cắt này để cổng ghi cưỡng chế contract và expected revision, bao gồm native content-version save; ưu tiên khả năng khai báo/quan hệ/validation/authority đã có trước khi xét adapter. Giữ UI/release/runtime ở trạng thái chưa chứng minh và giao theo dependency thực tế; không đổi mục tiêu thành người tự nhớ/chạy việc.

## Bằng chứng và tái chạy

[Execution map](./execution-map.md) được lập trước phép thử. [Source/scope/corrections](./source-and-scope-notes.md) ghi rõ file PM review riêng thiếu, KB chỉ đọc bản tóm tắt do tool trả truncated, các lỗi môi trường/envelope và giới hạn observer. Profile/source/expected có freeze manifests, HTTP/PG raw giữ nguyên.

1. Dùng host lab được giao, Docker sẵn có, tài nguyên và demo được kiểm lại. `provision-lab.py` chỉ tạo tài nguyên tên/nhãn work; r3 replay sửa email, internal-IP readiness và uid tmpfs. Images exact current PG16.13/Directus11.5.1 được pin digest. Không clone production DB/Flow/data/credentials.
2. Chuyển `lab-client.py`, `seed-lab.py`, `contracts-fixture.json`, `search-brief-agent.json` vào private work directory. Đợi copy xong rồi mới seed. Admin chỉ cấu hình fixture; tạo lại ba test identities có password ngẫu nhiên; không đưa password vào archive. `seed-lab.py` từ chối seed nếu seed-ready đã có; bootstrap r1 failure được giữ lịch sử.
3. Chuyển retrieval corpus/schema/SQL và `run-retrieval.py`; chạy sáu lookup. A1 nguyên cấu hình trước, không đọc bảng đáp án.
4. Agent đọc intent/catalog; tạo khai báo như hai file `declaration-agent-*` đã lưu. Trong replay kỹ thuật có thể dùng JSON đã lưu nhưng **không gọi đó là fresh intent authoring**. Copy validator tool/input đã freeze, dùng Joi trong Directus image để kiểm; không lấy safety-guard.sql cũ làm production validator.
5. Chạy `run-integration.py` với test identities sau khi xác minh hash/copy đầy đủ. Nó cố ý nộp các request sai, giữ kết quả FAIL và khôi phục fixture sau chụp để tiếp tục nhánh khác. Các script version-r2/r3/r4 lưu đúng lịch sử và lý do; đường đúng cuối cùng là native `/versions/:id/save`, không phải item PATCH?version. Không gọi promote hoặc runtime.
6. Sau khi process ghi kết thúc, chụp before-resume; dùng một Agent không nhận chat history, chỉ checkpoint ID và `resume-readonly.py`. Chụp after-resume so business hash. Tool readback đơn thuần không tự là fresh-Agent proof; có báo cáo của Agent riêng ở lượt này.
7. Chụp final/audit, copy artifacts về, kiểm hash trước cleanup. `cleanup-lab.py` chỉ xóa đúng labeled work resources/private directory; giữ image cache chung, không prune/restart e-learning. Demo safe HTTP smoke + process snapshot không thay full application regression.

Archive kèm `ssot-v1.6.11-read-only.html` là **snapshot evidence byte-identical sau sửa**, không SSOT current thứ hai. SSOT current vẫn là file trên Desktop Owner. `ssot-update.json` có backup/hash/readback; `manifest.json` có hash toàn bộ artifact cuối, trừ chính manifest.
