# Code và configuration inventory — 10/09/2026

Đếm **dòng vật lý, gồm blank/comment**, không tối ưu LOC bằng nén code. Không lấy LOC làm thời gian hay phần trăm khai báo. Nguồn cuối/nguồn lịch sử có SHA256 trong manifest.

| Nhóm đang chạy trong lab | File | Dòng | Phải bảo trì |
|---|---|---:|---|
| Một generic write-guard component | [extension/index.js](extension/index.js) | 163 | Endpoint + core hook trong cùng bundle; quyền native, Joi, merged state/catalog, PG locks/CAS, atomic links/receipt. |
| Empty app export, không UI/renderer | [extension/app.js](extension/app.js) | 2 | Metadata bundle yêu cầu app artifact; không tạo UI. |
| Extension manifest | [extension/package.json](extension/package.json) | 26 | Inseparable entries, partial=false, pinned host. Không dependency mới. |
| PG relational DDL mới | [relations.sql](relations.sql) | 50 | Constraints/composite FK, ba bảng phụ; không function/trigger/custom SQL engine. |

**Một component mới chỉ trong lab; 0 deployed production.** Native/config insufficiency có baseline HTTP+mutation và exact items/version source. Endpoint dùng lại ItemsService với accountability/knex transaction; hook bắt buộc là phần bảo vệ bypass của cùng component, không được tách/disable riêng. Không có code branch theo ID Field/MOW. Không phải zero-code.

Bốn bảng hỗ trợ mới: lab_write_routes qua native collection configuration; lab_profile_materials, lab_material_links, lab_write_receipts qua PG DDL. Sáu cột thêm: forms.revision/last_request/profile_version; records.revision/last_request/form_revision. Native permission/config/profile JSON trong configured.json; Joi description được chuẩn bị bằng dependency đã có. Ba composite-PK tables PG bị Directus inspector bỏ qua: chưa Data Studio authoring. Mọi schema này TEST ONLY, không số bảng production đã duyệt.

## Harness / công cấu hình / evidence (không miễn phí)

| File | Dòng | Chức năng / xuất xứ |
|---|---:|---|
| [baseline.py](baseline.py) | 14 | Mới: tái hiện hai FAIL cũ và khôi phục fixture. |
| [capture-final.py](capture-final.py) | 16 | Mới: đọc final PG/config/environment và sanitized resources. |
| [cleanup-lab.py](cleanup-lab.py) | 39 | Dùng lại ownership cleanup; bảo toàn demo. |
| [configure-guard.py](configure-guard.py) | 58 | Mới: tạo profile/route, sửa native permissions và sáu cột; gọi SQL constraints. |
| [configure-resume-r2.py](configure-resume-r2.py) | 36 | Lịch sử continuation sau permission-row lỗi; không chạy thêm trên fresh config. |
| [final-verifications.py](final-verifications.py) | 58 | Mới: hậu kiểm hashes/fresh PG/cleanup và lập metrics/summary. |
| [install-guard.py](install-guard.py) | 29 | Mới: mount bundle vào riêng lab, giữ image/limits và exact runtime read. |
| [lab-client.py](lab-client.py) | 32 | Dùng lại có chỉnh; authenticated HTTP và log đã khử secret. |
| [postrestore-check.py](postrestore-check.py) | 12 | Mới: đo lại native deny và durable receipt replay sau restart. |
| [prepare-resume.py](prepare-resume.py) | 12 | Mới: lưu checkpoint/hành động được phép trước giao Agent mới. |
| [provision-lab.py](provision-lab.py) | 64 | Dùng lại có chỉnh mail/readiness; dựng tài nguyên riêng, limits và ownership. |
| [resume-action.py](resume-action.py) | 16 | Mới: tool read/write có quyền service cho Agent độc lập. |
| [run-ready.py](run-ready.py) | 18 | Mới: readiness và chạy suite đã freeze. |
| [seed-lab.py](seed-lab.py) | 78 | Dùng lại fixture/schema/identities; không product runtime. |
| [test-gate.py](test-gate.py) | 105 | Mới: finite HTTP/PG suite, observer khóa đồng thời và snapshot. |
| [test-load-failure.py](test-load-failure.py) | 30 | Mới: lỗi nạp bundle tạm trên riêng lab và restore đúng bytes. |
| [test-rollback.py](test-rollback.py) | 24 | Mới: fault injection constraint tạm sau write, kiểm rollback; gỡ finally. |
| [transfer-evidence.py](transfer-evidence.py) | 8 | Mới: allowlist artifact/hash nén; không tải secrets. |
| [update-ssot.py](update-ssot.py) | 88 | Mới: biên tập tài liệu có guard hash/backup/một lần ghi và QA, không product code. |
| [verify-results.py](verify-results.py) | 27 | Mới: root assertion từ raw readback/audit, không HTTP-only. |

Tổng **20 file Python cuối/continuation, 764 dòng vật lý**. Có dùng lại source; tổng này là kích thước phải đọc/bảo trì của harness, không phải toàn bộ dòng mới viết hoặc product runtime LOC.

## Lịch sử sửa lỗi giữ riêng

| File lịch sử | Dòng |
|---|---:|
| [configure-guard-r1.py.txt](configure-guard-r1.py.txt) | 57 |
| [extension-index-r1.js.txt](extension-index-r1.js.txt) | 149 |
| [extension-index-r2.js.txt](extension-index-r2.js.txt) | 152 |
| [extension-package-r2.json](extension-package-r2.json) | 11 |
| [install-guard-r1.py.txt](install-guard-r1.py.txt) | 29 |
| [provision-lab-r1.py.txt](provision-lab-r1.py.txt) | 64 |
| [test-gate-r2.py.txt](test-gate-r2.py.txt) | 105 |

Native `directus-*.js.txt` là source đọc từ exact image/cùng digest cũ, không code mới của agent. JSON fixture, request payload, profile và kết quả là artifact khai báo/test, không cộng thành JS runtime; vẫn tốn công chuẩn bị. Lỗi/historical output ở corrections.md và execution-logs.

## Dependency, trách nhiệm và lối ra

Không npm/pip install, không fork hay image build. Runtime guard dùng Node crypto/module/fs, Joi17.13.3 và @directus/errors đã có trong exact image; ItemsService, transaction và event context lấy từ native Directus. SQL chỉ dùng PG16 primitives. Resolve package qua realpath exact pnpm layout là coupling cần regression khi đổi stack.

Guard và PG route/profile/link representation phải được nâng/chuyển cùng nhau; admin hoặc deployment config nằm ngoài business caller trust boundary. Proof chỉ kiểm malformed required bundle dừng app, không mọi misconfiguration. Nếu native target sau này cung cấp atomic governed write tương đương, chạy lại cùng negative/concurrency/replay cases trước thay guard; không giữ hai write authorities.

Chưa chốt maintenance owner sản phẩm, license/platform deployment hoặc production acceptance. Lệnh PM cho phép thử đúng một candidate trong lab; không tự suy thành quyền deploy. Chi phí thực hiện ngoài các mốc có telemetry là NOT MEASURED (metrics.json).
