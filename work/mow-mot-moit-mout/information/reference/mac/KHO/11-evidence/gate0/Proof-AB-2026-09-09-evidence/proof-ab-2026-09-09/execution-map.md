# Bảng lắp thực thi trước phép đo · 09/09/2026

| Chặng | Đường cụ thể đã tìm | Dùng lại / thiếu |
|---|---|---|
| Khai báo/profile | SSOT v1.6.10; E05 concepts 5/8/12; PM fixture nghĩa phút/ngày tạo/ghi chú; `forms.schema` | Chuẩn hóa chỉ 3 TEST ONLY contracts; nguồn không có contract_ref; không promote |
| Validator | Directus 11.5.1 dependency Joi 17.13.3; built-in field/permission validation | Joi ở harness kiểm cấu trúc + contract đọc từ catalog. Chưa có resolver/validator authoring được nối server; thử trực tiếp cổng để lộ gap |
| Cổng ghi | Directus 11.5.1 REST `/items/{collection}` với authenticated tester/service policies | Chạy lab DB mới; schema tối thiểu/config test. Không dùng WCR/service admin cho business request |
| Bản ghi/checkpoint | PG16.13 current digest; Directus item ID/Activity/Revisions; lab checkpoint collection | Kiểm retry/stale thực, không giả CAS/idempotency; checkpoint TEST ONLY, chưa T0 production |
| Renderer | Current Nuxt3.20.2/Nitro2.12.8 build 04/09; `server/chunks/build/UForm-0Pia6Vp9.mjs` + `FormCustom` | Đọc `form.schema`; submit `{data,form}` tới inbox. Chưa có contract_ref/version-binding/write_target mapping hoặc open saved runtime record. Không sửa renderer |
| Version/release | Directus content-versioning API có sẵn, cần thử exact lab | Content version khác governed MOW release. Chưa tìm được release path MOW có authority; giữ Draft |

Một nhánh thiếu không chặn các nhánh API/quyền/validator độc lập. Nuxt current Node20.20.0 khác Directus Node22.14.0; không thay nền để chữa mapping. `PM_review_Proof_A_2026-09-09.md` được nhắc nhưng không có attachment riêng tìm được; trạng thái ACCEPT lấy trực tiếp lệnh PM, không nhận là đã đọc file thiếu.
