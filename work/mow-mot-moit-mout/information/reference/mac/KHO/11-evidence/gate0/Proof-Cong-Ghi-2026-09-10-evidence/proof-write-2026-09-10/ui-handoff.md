# UI handoff — chưa chạy renderer

UI gap được giữ từ proof trước: UForm hiện submit inbox, chưa chọn đúng version/revision/write target/read-back của lát cắt. Không tạo .vue/page/renderer hoặc runtime trong lượt này. API evidence không thay UI PASS.

Hợp đồng nối tối thiểu của candidate:

1. Đọc GET `/items/forms/{form_id}` để lấy schema, system_fields, `profile_ref`, `profile_version` và `revision` thực. `main` là Draft đang sửa, không immutable business release.
2. Form biên tập: POST `/proof-write/form/{form_id}` với `request_id` UUID giữ nguyên khi retry, `expected_revision` vừa đọc và `data` chỉ gồm field được route cấu hình cho phép. Không gửi actor/approver/date_created/revision server hoặc tên bảng đích.
3. Form nhập liệu: POST `/proof-write/record/{record_id}`. Tạo mới dùng expected_revision=0; input duration_minutes/note cùng form_ref/form_version=main/form_revision thực. Profile và target do route record trong PG quyết, không cho UI chọn collection tùy ý.
4. Response trả record/form ID, `meta.revision`, server_request_id, logical_request_id, transaction_id và dữ liệu đọc lại bằng native service trong cùng transaction. Đọc lại bằng GET `/items/lab_task_records/{record_id}` hoặc GET form. HTTP409 đòi đọc revision hiện hành và giải quyết xung đột; không tự đổi expected_revision rồi gửi lại payload cũ.
5. Gửi lại nguyên logical request trả lại response đã lưu, `replayed=true`; dùng cùng key cho payload khác phải409. Header server của lần retry khác correlation của commit gốc trong response.meta; giữ cả hai để truy vết.

`ui-request-response.json` sẽ lấy request/response thực từ các ca đã đo; không phải mock. Phần nối còn thiếu ở renderer là gọi đúng submit action và xử lý revision/conflict/read-back; chưa có smoke UI hoặc ước lượng hoàn thiện renderer. Native content versions bị đóng cho pilot identities; không dùng /versions/save làm đường vòng.
