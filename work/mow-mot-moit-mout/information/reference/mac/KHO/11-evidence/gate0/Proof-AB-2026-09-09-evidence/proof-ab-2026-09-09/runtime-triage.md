# Proof C — source/config triage, chưa chạy runtime

Chỉ đọc metadata/source ngày 09/09/2026. Không gọi enqueue/claim/ACK trên queue hiện hữu. Không cài thư viện, không viết runner.

## C1 current: chưa có đường nối executable được chứng minh

| Đoạn | Bằng chứng actual | Kết luận giới hạn |
|---|---|---|
| Enqueue | `fn_job_enqueue(text,text,text,jsonb,text,text,integer,timestamptz,text,integer,uuid)` → JSONB; flag trong dot_config; dedupe tra active states bằng idempotency_key | Actor là text tham số, không phải authenticated user. Dedupe sau terminal state không được chứng minh là bất biến. Không kiểm hành vi đồng thời bằng gọi thật |
| Claim | `fn_job_claim(text,text[],integer)` → count + claimed JSONB; SELECT FOR UPDATE SKIP LOCKED rồi UPDATE cùng statement/transaction; ghi lease_owner/lease_until | Có primitive atomic claim. lease_owner là text do SQL caller đưa; không chứng minh delegated identity. Không kéo external action vào transaction này |
| ACK | `fn_job_ack(uuid,text,text)` → JSONB; row lock, chỉ leased/in_progress, đối chiếu lease_owner; cập nhật succeeded/clear lease | Không thấy kiểm lease_until trong body; summary chỉ trả về JSON, không thấy persist vào hàng queue trong hàm ACK. Phải thử expired lease/summary durability sau nếu chọn đường này |
| SQL authority | Các hàm SECURITY DEFINER owner workflow_admin, search_path public/pg_temp; ACL NULL; role directus được `has_function_privilege(...,'EXECUTE')=true` | Quyền SQL có thật, không đồng nghĩa mỗi Directus human/service có quyền API gọi. Không gọi hàm để thử |
| Directus bridge | Installed 11.5.1; extension đã mount chỉ có L2 checkpoint guard; 320 operations gồm CRUD/condition/request/exec/log/trigger/transform; 0 options có literal fn_job_*/job_queue | Không thấy operation/approved endpoint nối primitive này trong phạm vi đọc. Không suy tất cả HTTP targets bên ngoài đã được truy hết |
| Nuxt bridge | Quét 314 compiled modules của current build: 0 literal fn_job_enqueue/claim/ack | Không có cầu nối được tìm bằng dấu vết này; dynamic indirection vẫn UNKNOWN, không chứng minh tuyệt đối không tồn tại |
| Internal runner | E07 đã truy cowork agent/coworkd: shell/job adapter dùng state directory; agent-api-executor plan-only/dry-run | Không có proof executor load exact MOW/version → safe effect → persist/ACK. Không lấy runner shell đang Up làm T5 PASS |

**C1 = NOT FIT CURRENT đối với đường Directus composition đã tìm; bridge ngoài phạm vi = UNKNOWN.** Không kết luận mọi phiên bản Directus đều không làm được. Source chi tiết: [source-database.json](./source-database.json), [c1-endpoint-trace.json](./c1-endpoint-trace.json). Đây là đọc mã, chưa là behavioral/authority/runtime acceptance.

## Hai ứng viên reuse, chỉ khuyến nghị một

| Ứng viên | Compatibility/license theo nguồn chính thức đã đọc | Gánh tích hợp và quyết định |
|---|---|---|
| **pg-boss 12.30.0 — đề nghị thử giới hạn nếu PM giao C2** | Package/README current: MIT, Node ≥22.12, PG ≥13. PG16.13 và Node22.14 đã hiện diện ở Directus image đáp ứng số phiên bản; Nuxt Node20.20 không đáp ứng. Không đề nghị chạy worker bên trong process CMS | Có queue/worker/retry/SQL + transaction adapters. Dùng schema queue riêng do thư viện quản lý; không trực tiếp claim bảng job_queue hiện tại. Cần một worker process và handler nối capability/version/audit: phần nối này vẫn là code candidate chưa được cấp phép xây |
| Graphile Worker 0.17.3 — chưa chọn cho lát cắt này | MIT; current requirements PG≥12, Node≥22.18. Native SQL add_job và task executors có sẵn | Cũng cần executor code và schema graphile_worker; Node22.14/20.20 hiện đo đều chưa đạt current requirement. Không nâng runtime hoặc pin bản cũ chưa kiểm chỉ để chọn được nó. Không kết luận thư viện kém hoặc vĩnh viễn không phù hợp |

**Khuyến nghị duy nhất cho nhánh C2:** pg-boss là ứng viên thử tiếp, chưa là implementation path được nghiệm thu. Lý do là phù hợp PG và Node version đã quan sát, cộng API transaction/retry đã có; vẫn phải đo effort/authority/version pin/duplicate effect/crash behavior trong lab riêng sau. Tác dụng bên ngoài vẫn cần idempotency; lời giới thiệu “exactly once” của queue không chứng minh external effect exactly-once.

**Một nguồn work execution:** nếu thử pg-boss, chỉ chọn một queue làm chủ execution của fixture; không enqueue cùng việc độc lập vào job_queue cũ và pg-boss. PG canonical MOW/version/business result vẫn là nguồn nghiệp vụ; schema queue không tự là business truth cạnh tranh. Đường exit phải dừng intake, drain/đối chiếu job đang chạy, giữ mapping occurrence/job/result và lịch sử, rồi chuyển từng cohort. Không xóa hoặc migrate queue hiện hữu trong lượt này. Migration/compatibility của mapping còn chưa thử; maintenance gồm process, library/schema upgrades, capability handler, observability và rollback.

Nguồn chính thức: [pg-boss package](https://github.com/timgit/pg-boss/blob/master/package.json), [requirements và transaction support](https://github.com/timgit/pg-boss/blob/master/README.md), [pg-boss jobs/workers](https://pgboss.io/introduction), [Graphile requirements](https://worker.graphile.org/docs/requirements), [Graphile package](https://github.com/graphile/worker/blob/main/package.json), [SQL add_job](https://worker.graphile.org/docs/sql-add-job), [task executors](https://worker.graphile.org/docs/tasks), [MIT](https://github.com/graphile/worker/blob/main/LICENSE.md). Các nhánh master/main là ảnh chụp nguồn tại ngày đọc, chưa là package lock đã cài/chạy. Không dựa nguồn bên thứ ba để kết luận.
