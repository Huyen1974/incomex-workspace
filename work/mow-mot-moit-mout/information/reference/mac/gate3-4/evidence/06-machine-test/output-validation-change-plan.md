# Sửa sau ca thiếu đầu ra chạy thật

Raw before: native Flow được TEST fixture buộc trả record không có review_required, dù release mang required output profile. Worker nhận HTTP200 và native queue completed. Đây là lỗi bị phát hiện, không được xóa hoặc tính PASS.

I0/I1: PG kiểu boolean bảo vệ type nhưng cột nullable vì bước HMITL chưa có kết quả AUTO; một NOT NULL toàn bảng sẽ sai stage và phá accepted legacy slice. I2: blocking Flow chạy trước khi PG tạo system date/readback; kiểm riêng Flow không bảo vệ toàn output contract sau ItemsService. I3: UI check không đủ cho Agent/worker. I4: Joi17.13.3 đã có, không validator mới. I5: compose output profile đã pin trong release + readback trong transaction, trước receipt/commit; fail→rollback. Adapter thêm đúng một conditional generic, không chứa tên trường/threshold/workflow. Legacy release không có output profile giữ bounded behavior cũ, không được suy thành full output-contract proof.

Rerun ca thiếu output và happy59/60/61; frozen P1–P4 sau source thay đổi. Chưa production.
