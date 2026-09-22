# Phát hiện trong lúc thực hiện

1. Lần đầu enqueue gặp 42501: SELECT FOR SHARE cần quyền UPDATE trên binding, trong khi producer chỉ có SELECT. Không cấp thêm quyền ghi. Đổi sang SELECT MVCC: admission linearize tại lần đọc active binding trong transaction enqueue; pin ID đó vào instance. Deactivate có hiệu lực với admission đọc sau nó. Enqueue lần lỗi rollback toàn transaction, 0 instance/effect; release TEST chưa được dùng vẫn giữ nguyên, lần tiếp theo tạo ID/version mới, không sửa lịch sử.
2. Bootstrap runtime-control kế thừa pin Node22.14 từ Gate0; sửa về exact worker22.23.2 đã nhận Gate2 trước thực chạy P1. Không nhận bootstrap Node22.14 là target proof.
3. Contract90cases chỉ shape, không thay P1–P6.

4. Joi array item required() nghĩa là mảng phải chứa item, khác với việc từng phần tử đúng kiểu. 13 positive fixture fail vì mảng N/A rỗng. Đổi requiredness của phần tử sang tùy chọn, giữ array.required/min và các trường con bắt buộc; không nới kiểm type/owner/unit. Rerun90.

5. P5/P6 lần đầu seed context sau khi đã cài route đầu tiên, native filter chặn403 kể cả bootstrap. Giữ nguyên filter; seed hết fixture trước route. LượtB dùng bảng lab_context_b / lab_semantic_defs_b / lab_missing_requests_b; tất cả xóa cùng owned lab. Không gọi seed failure là business proof failure.
6. Native DELETE permission trả204 không có body; helper data() giả định body.data nên lỗi sau khi thu hồi đã thành công. Dùng call() cho DELETE. Resume test xác nhận quyền thực sự bị thu hồi,17/17 runtime đạt.
7. Rà cuối snapshotv1 phát hiện mot.form_version=main và form.submit_config.fixed_input.form_version=main là metadata đã copy nhưng không được runtime đọc. Các semantics MOUT/Condition còn prototype dangling refs. Không nhận đó là fullclosure. Fresh lab proof-g34b dùng cùng guard/workerhash, compile graph chỉ reachable refs, pin hai profiles, bỏ UI config và mutable refs. Giữ artifact g34 cũ là initial bounded evidence; thay P1/P4 verdict cuối bằng fresh closure proof.
8. Siết C01 thành8identity variants; C08 bằng native alternatives cấm AUTH retry tự động/unknown masquerade transient;110shape cases. Không biến việc thêm case thành bằng chứng runtime mới.

## 8. Kiểm cấu trúc cuối sau khi dọn lab

Tự rà phát hiện C01.Version còn mang edit_revision/activation từ prototype. Đã sửa khai báo: Version immutable chỉ giữ source_revision để truy nguồn; edit_revision thuộc Draft/Binding, activation thuộc Binding. Thêm hai ca âm; kiểm lại toàn bộ 112/112 ca bằng Joi17.13.3 trên Node24.21.0 local. Đây là kiểm cấu trúc với cùng phiên bản Joi, không phải lần chạy runtime lab thứ ba. Kết quả cuối: contract-shape-final.json và receipt; 110/110 trong final-closure vẫn giữ nguyên bằng chứng thời điểm lab. Guard/worker không đổi. Khai báo C06 generic và representation graph lab vẫn cần mapping được nhận; không suy shape PASS thành full semantic/data lock.
