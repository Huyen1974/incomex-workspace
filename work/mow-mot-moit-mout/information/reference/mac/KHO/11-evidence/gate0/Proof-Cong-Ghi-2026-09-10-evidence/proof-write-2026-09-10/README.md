# Proof cổng ghi — thực thi 10/09/2026

**Kết luận: PASS trong lát cắt đã đóng băng; nộp PM review, chưa tự nghiệm thu A/B.** Lệnh PM đề ngày 09/09 được Owner giao thực hiện; bản gốc lưu trong [pm-command.md](pm-command.md). Factory DONE, retrieval ACCEPT/DONE; FEAS PARTIAL, Gate0 DOING, O1–O3 NOT VERIFIED, R1 chưa mở. Không đo/tune retrieval lại.

## Đường được chọn và lý do cần code

Hai lỗi cũ đã tái hiện trước sửa: contract giả trong JSON và PATCH với If-Match giả đều HTTP200, có mutation; xem [baseline-results.json](baseline-results.json). Điều này xác định thiếu enforcement trong đường tích hợp đang thử, không kết luận mọi Directus đều không hỗ trợ.

Chọn **một bundle extension chuẩn**, gồm endpoint và core filter hook bắt buộc cùng nạp, `partial:false`, `EXTENSIONS_MUST_LOAD=true`. Dùng lại native ItemsService với accountability thật, Joi17.13.3 trong image, native audit/revisions và transaction PG. Không fork, không cài dependency, không viết CRUD/auth/validator engine hay code theo MOW/Field. [Code inventory](code-inventory.md) tính cả code chuẩn bị và SQL.

`POST /proof-write/form/:id` và `/proof-write/record/:id` cùng nhận `{request_id, expected_revision, data}`. PG route quyết target, whitelist và exact governed profile; caller không chọn profile hoặc tên bảng. Native service giữ kiểm quyền. Core hook chỉ cho ghi protected collection trong transaction nội bộ của endpoint; caller không thể tự gửi cờ để bỏ qua. Xem [đường ghi sau sửa](write-paths-after.md).

Quan hệ PG dùng composite FK cho Field → exact contract/version → profile cho phép → form. JSON và material links được đồng bộ trong cùng transaction, không hai nguồn đều cho business caller tự ghi. Server đối chiếu thuộc tính với catalog, kiểm cả trạng thái hợp nhất, duration bắt buộc, ngày tạo thuộc hệ thống. Ba bảng phụ composite PK bị Directus inspector bỏ qua: chúng là PG support tables, **chưa chứng minh authoring chúng trong Data Studio**. Catalog/route bị khóa đối với identities của pilot; fixture do harness cấu hình, chưa chứng minh quản trị catalog production.

Server khóa row rồi so revision và ghi trong cùng PG transaction. Receipt khóa theo actor + logical request; exact retry trả kết quả cũ, cùng key khác payload trả409. Server correlation được lưu trong item/native revision/receipt và nối với native Activity actor. Error log tách khỏi successful business audit.

## Kết quả và bằng chứng

| Nhóm | Actual | Nguồn |
|---|---|---|
| Bộ chính | **66/66 PASS**; có cả valid human/service và negative/bypass | [Tóm tắt từng ca](case-summary.json), [HTTP + PG trước/sau](gate-results.json) |
| Đọc lại/quan hệ/audit | 20/20 assertion độc lập từ raw PASS | [Kiểm read-back](readback-audit-verification.json) |
| Hai writer tuần tự | A200, B dùng revision cũ409 | `sequential-writer-*` trong raw |
| Hai writer đồng thời | Cùng đọc revision5, PG trace chứng minh cả hai đang đợi khóa; **200 +409**, chỉ revision6 commit | `concurrent-writers` trong raw, cùng script đã freeze |
| Retry | Exact original data/meta được replay, không thêm object/receipt/audit; đổi payload409 | `same-logical-request-replay`, `same-key-different-payload` |
| Rollback sau native write | Test-only CHECK tại receipt INSERT gây PG23514/HTTP500; form/ref/audit/receipt đều không đổi; CHECK đã gỡ | [rollback-result.json](rollback-result.json) |
| Phiên Agent mới | Đọc checkpoint → MOW/MOT/form/record + catalog/profile thật; tự thực hiện đúng một update record **2→3** | [Báo cáo Agent](fresh-agent-report.md), [raw](fresh-agent-evidence.json), [root đối chiếu PG](fresh-resume-root-verification.json) |
| Extension load lỗi | Chèn lỗi nạp trong riêng bundle lab: app dừng exit1; phục hồi đúng hash, ping200 | [load-failure-result.json](load-failure-result.json), log đi kèm |
| Sau restart | Native PATCH vẫn403; original request replay200 cùng kết quả, không mutation | [postrestore-result.json](postrestore-result.json) |

Ca âm tính bao gồm fake/null/missing material; ID thật sai Field/contract/version/unit/operation/target/subject/datatype; note-only thiếu duration; profile dễ hơn/scope sai; fragment hợp nhất sai; outsider/spoof actor/approver/ngày tạo/revision/correlation; bypass REST/bulk/version/GraphQL. GraphQL HTTP200 chứa lỗi WRITE_GATE_REQUIRED/FORBIDDEN và **không commit**, không nhầm HTTP200 với ghi thành công. Bypass bị từ chối vẫn giữ toàn bộ canonical object/ref/version/receipt và successful audit trước–sau trong scope observer.

Cuối phép thử còn đúng 1 MOW, 1 MOT, 1 form family, 3 Field, 3 contract, 1 record. Form revision6; record revision3 sau Agent mới; 8 receipts. [final-capture.json](final-capture.json) có constraints đã validated, actual environment và trạng thái PG.

## Version, UI và runtime

**Chỉ guarded editable `main` Draft.** Draft revision tăng khác ID native history và khác business release version. MOT vẫn bind `main`: sửa main sẽ đổi Draft mà binding này đọc; chưa pin bản cũ bất biến. Một native content version là fixture ID thật để thử deny, không kho release. Native version read/create/save/promote/metadata đóng cho pilot; exact save cần read authority, nên chỉ bỏ update permission là chưa đủ.

**UI NOT RUN.** Giữ [ui-gap nguồn từ proof trước](../proof-ab-2026-09-09/ui-gap.md), bản sao trong gói là [prior-ui-gap.md](prior-ui-gap.md); các source context kèm theo giữ ngày 09/09 trong [provenance](prior-context-provenance.json). UForm đang submit inbox; chưa có action/revision/conflict/read-back phù hợp. [ui-handoff.md](ui-handoff.md) và [request/response thực](ui-request-response.json) chỉ rõ phần nối tối thiểu. Không sửa `.vue`, dựng trang/renderer hoặc dùng API PASS thay UI PASS. Cần nối renderer hiện hữu với write action được policy chọn và xử lý409/read-back; chưa có ước lượng triển khai.

Runtime **NOT RUN**, pg-boss chưa cài; C vẫn triage theo [nguồn lượt trước](prior-runtime-triage.md). Replay qua restart Directus không chứng minh queue/runner, crash recovery hoặc full T0 autonomy. Publish/activation/immutable release, toàn bộ authoring/admission và permission/security/load audit toàn hệ chưa hoàn tất.

## Môi trường, công thực hiện và giới hạn bảo trì

VPS2 lab riêng, cùng pinned images với A/B: PG16.13 Debian16.13-1.pgdg13+1; Directus **11.5.1**, internal API package25.0.1, Node22.14.0, Joi17.13.3. Hai image digest trong provision/final capture; không suy từ tag. PG512MiB, Directus1024MiB, mỗi container0.5CPU; PG tmpfs512MiB, network internal, không cổng public/egress hoặc Flow nguồn. Nuxt không chạy hoặc nâng cấp.

`/ping`200; authenticated `/health`503 **chỉ lỗi email** do SMTP loopback port9 đóng chủ ý; PG và storage checks ok. Không gọi full health PASS. [Cleanup](cleanup.json) xác nhận xóa đúng hai container, network, volume mang nhãn và thư mục credential riêng; 5 demo containers giữ ID/image/start/restart/status/OOM, hai safe GET giữ status/body/location. Đây không full application regression. Không sửa production hay prune shared images.

Seed 20,797ms; cấu hình r2 tiếp tục phần chưa xong 4,897ms, **không phải tổng chuẩn bị profile**. 64 ca HTTP có elapsed, median522ms; concurrency/GraphQL có trace riêng. [metrics.json](metrics.json) ghi tổng dựng môi trường, chuẩn bị profile, debug, số phán đoán/calls/tokens và công người **NOT MEASURED**. Hỏi Owner mới0, một fresh Agent độc lập; không suy 0 công người hay tỷ lệ98% khai báo. [corrections.md](corrections.md) và execution-logs giữ lỗi readiness, permission row, package resolution, hook registration/parser và thu evidence; không đổi expected để làm PASS.

Bundle phụ thuộc semantics exact native service/events/transaction và cấu trúc schema. Nâng stack hoặc đổi permissions/routes cần chạy regression. Code không mang logic riêng của ba Field nhưng vẫn là custom phải bảo trì. Chưa chốt người bảo trì/triển khai production; không dùng proof này làm quyền deploy. Chọn một component sau khi native route không đáp ứng, không xây hai phương án hoặc runtime engine.

## Kiểm lại và tái chạy

Kiểm `manifest.json` cho bytes/hash từng tệp; `remote-transfer-hashes.json` đối chiếu28 artifact remote đã tải đủ trước cleanup; `freeze-verification.json` ánh xạ hashes r1/r2 sang nguồn lịch sử và r3 sang nguồn thực đo. `ssot-update.json` ghi backup và hash sau **một lần** sửa SSOT. HTML read-only trong gói là snapshot, không SSOT thứ hai.

Tái chạy cần môi trường lab mới, capacity/ownership check và credentials mới do provision sinh. Dùng `provision-lab.py` → chuyển fixture cùng `lab-client.py`/scripts → `seed-lab.py` → freeze + `baseline.py` → `configure-guard.py` (fresh lab, không chạy continuation r2) (script này đã áp dụng `relations.sql`, không chạy DDL lần hai) → chuyển thư mục extension → `install-guard.py` → freeze + `run-ready.py` (gọi suite) → rollback/fresh-resume/load-failure/postrestore → capture/transfer/hash → cleanup. Giữ root/name nhất quán giữa scripts; không chạy vào DB hiện hữu. `configure-resume-r2.py` chỉ lưu lịch sử lần lỗi, không bước bắt buộc của fresh replay. Agent mới phải là phiên độc lập có nhiệm vụ giới hạn như report, không thay bằng root đọc checkpoint.

Offline replay assertion: chạy `verify-results.py` với working directory thư mục evidence; các HTTP/PG tests cần dựng lab. [final-verifications.py](final-verifications.py) là root hậu kiểm từ workspace gốc và evidence, có bước chép execution logs; không phải runtime code. Sources exact Directus `directus-*-exact.js.txt`/versions được giữ để PM đối chiếu điểm kiểm quyền, native transaction và loader.

**Đề nghị PM:** xem xét nhận riêng proof cổng ghi này; nếu nhận, giao lát cắt nối UI hiện hữu bằng action/revision/read-back đã cung cấp. Giữ release/runtime và các tiêu chí authoring còn thiếu ở trạng thái chưa nghiệm thu; chưa mở R1 toàn UI hoặc deploy.
