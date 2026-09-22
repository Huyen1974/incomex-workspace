# Code và gánh bảo trì — scope Gate0, 10/09/2026

Đếm dòng vật lý, có cả comment/blank; không coi LOC là thước đo duy nhất. Tất cả chỉ ở bản thử cô lập, **0 production deploy**, không sửa repo nguồn hoặc 5 demo.

| Nhóm | Thực tế | Vì sao cần / trách nhiệm bảo trì |
|---|---|---|
| Product candidate mới: UI | `useGuardedSubmission.ts`: **87 dòng** | Generic guarded submit, logical request/revision, read-back, reopen, explicit conflict resolution, exact retry. Renderer hiện hữu chưa có luồng này; dùng lại Nuxt `$fetch`, Vue state và renderer. Không branch theo Field/MOW/collection. |
| Existing product code sửa | `UForm.vue`: **76→84 dòng, +9/−1** | Chọn generic adapter từ governed metadata; hiển thị lỗi/success và hai thao tác đọc lại/retry. `FormCustom.ts` và Form block giữ nguyên. Không gọi thay đổi `.vue` là config. |
| Product candidate mới: runtime | `runtime/kernel.mjs`: **92 dòng** | Bao gồm event producer + transaction adapter + event/instance/attempt mapping + một registered capability gọi guard + worker lifecycle. PG driver và pg-boss giữ transaction/delivery/claim/retry/ACK. Không queue algorithm hoặc per-MOW logic. |
| Tổng thêm lượt này | **179 dòng ở 2 file mới; +9/−1 trong UForm** | 188 dòng thêm, 1 dòng bỏ, net +187; không bao gồm DDL/harness/dependency/legacy bên dưới. |
| Candidate đã có, vẫn phải bảo trì | Guard **163 JS +2 app export +metadata**, **50 dòng SQL** | Bytes không đổi; PM đã nhận scope authority/write/audit. Một Directus bundle, không fork CMS. Trước target production phải kiểm lại built-in có thay được không. |
| SQL/DDL mới | **33 dòng**, 5 bảng TEST ONLY | Release, binding, event, instance, attempt. PK/UNIQUE/FK/CHECK của PG. Không SQL function/trigger mới. Thêm 1 trường JSON `forms.submit_config` bằng native Directus schema API; role/GRANT/config bootstrap nằm trong harness được kê riêng. |
| Dependencies mới | **2 direct: pg-boss12.30.0, pg8.23.0; 21 packages trong lock** | PG driver vốn được pg-boss kéo vào; kê direct vì kernel import. `npm ls --all` hợp lệ. Không cài UI package mới; dùng @nuxt/image đã có khi build harness. |
| Native schema của thư viện | `proof_boss`, schema version **40** | Có bảng/phân vùng/index riêng do pg-boss tạo và giám sát. `remote/final-capture.json` kê đầy đủ. Không giấu schema/retention/upgrade burden vào chữ “thin”. |
| Process/container | **1 worker mới** | Tách CMS. Dùng lại pinned Directus image làm Node22.14 runtime, không chạy thêm CMS. Lab tổng cộng PG +Directus +worker, container setup/emit tạm, UI rehearsal +SSH tunnel local. Tất cả đã dọn; không public port. |
| Test harness | Python bootstrap/control/observer/export/verifier; Nuxt mount/proxy/identity plugin; setup.mjs; frozen fixture JSON | Kê từng file/LOC ở `code-files.json`. Harness tạo identity synthetic, đưa metadata vào Form block và vận hành lab; không phải production login/page/release service. Plugin `$formRequest` 4 dòng đi qua proxy lab; production auth/session wiring còn phải tích hợp và thử. |

Nguồn trước/sau và diff ở `ui-source-before/`, `ui-source-after/`, `ui-product.diff`. 36 hash source/build UI giữ nguyên trong cả V1→V2 và nhóm test. Source guard và runtime đã đối chiếu với bytes container. Các bản sửa lỗi bootstrap được giữ ở `corrections.md` và `harness-logs/`.

**Bố trí dữ liệu:** PG giữ declaration/profile/catalog, TEST release snapshots, binding và business instance/result/receipt. Release snapshot là bản phiên bản cố định, không business-writable copy cạnh Draft. pg-boss chỉ làm chủ delivery; không enqueue song song vào queue cũ. Worker không tự giữ luật duration/note; input lấy từ release configuration. API guard vẫn kiểm current main revision/profile — đây là giới hạn có chủ đích của proof, không đã xây release-aware production write API.

**Trước production:** phải chỉ định chủ sở hữu kỹ thuật cho (1) guard/Directus policy và regression; (2) UI adapter/session storage/conflict và auth integration; (3) worker/service credential, pg-boss/PG schema migrations, retention, telemetry, retry/reconcile. Hiện chưa chỉ định cá nhân chịu vận hành sản phẩm dài hạn; Codex chỉ bàn giao candidate/evidence. PM chọn target stack trước bù UI hàng loạt. Kiểm built-in target bằng cùng contract; nếu đủ thì thay phần nối custom. Khi thay queue, dừng intake, drain hoặc reconcile job→instance→receipt rồi chuyển binding; không dual execution.

Các rủi ro chưa được scope này kiểm: mất mạng đúng lúc ghi/read-back; localStorage lỗi hoặc dùng chung nhiều tài khoản; kill worker giữa effect và ACK; retry/terminal FAIL; schema/release production governance; backpressure/load/DR. Không suy lời hứa vận hành production từ ba lần chạy thành công.
