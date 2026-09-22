# Formal Pilot A — chuẩn bị, chưa chạy

D08 DECIDED PM: **Ghi nhận thời lượng xử lý**. Gate5 NOT STARTED. Điều kiện vào: PM chấp nhận Gate3/4 theo Pilot;6 fact Task/Context/consumer có nguồn và đường đọc/ghi đã kiểm; D04 chốt nếu chạy HMITL assignment. Không dùng quyết định D04 để tự bỏ khoảng trống kỹ thuật. Phiếu B Platform giữ follow-up adoption riêng; không production mutation trong hồ sơ này.

Một lượt mới bắt đầu bằng câu intent đã ghi PG; dùng catalog được chấp nhận trước, không mớm ID. Chạy idea → reuse → thiếu thật → đúng owner bổ sung → resume → readiness → machine test → review/approve → publish → activate → một event. Tiếp theo feedback → DraftV2 → impact → test/run → so sánh; deactivation/retire chặn use mới, giữ pin cũ, thử rollback theo phạm vi được duyệt. Không đổi fixture khi thấy kết quả xấu mà không ghi version/lý do.

Đo trên từng lượt, giữ nguồn từ PG/receipts và đồng hồ: intent→Draft và Draft→Published elapsed; human active time đo riêng với thời gian chờ; human semantic decisions; số giá trị người nhập tay; refs yêu cầu/reuse, Definition/Version/variant mới; Agent/tool calls; test được máy sinh/chạy/chấm; số lần fail/resume và lý do. Ghi denominator trước chạy. Không suy98% hay thời gian người từ thời gian Agent.

| Kết quả cần kiểm | Tiêu chí quan sát được |
|---|---|
| O1 | Một người mới chỉ nhập thông tin hệ thống chưa có; không chọn tool/bấm từng test; cùng ID/version/revision đi qua UI/Agent và PG. Ghi toàn bộ can thiệp, không ẩn công chuẩn bị catalog/config. |
| Khả năng lặp | Ít nhất2 sessions mới trên cùng input/catalog snapshot; semantic closure/missing tương đương. Báo mọi sai khác, không dùng một lượt đẹp để kết luận toàn bộ. |
| CR1–CR8 | Trước thay đổi nhỏ, chốt phạm vi/expected impact; đo nơi sửa, bước người, typed diff, compatibility, regression, rollback, provenance và mức tái dùng theo định nghĩa CR trong SSOT; không tự tạo bộ CR mới. |
| Không hỏng V1 | V1 Version/Release giữ hash; Instance cũ giữ pin; V2 không thừa hưởng TEST/approval cũ; deactivation không xóa lịch sử. |
| Thao tác người | UI thư viện/rà soát/form/report dùng thành phần có sẵn; báo refresh thủ công và mọi bước phải nhớ. Không gọi thao tác mô phỏng là tự động. |
| O2/O3 | Chỉ đo khi có Task Context thật và baseline phù hợp. Nếu chưa có before/after kinh doanh: NOT MEASURABLE YET, không VERIFIED. |

PM chốt ngưỡng thời gian chấp nhận trước khi chạy; hồ sơ này không bịa target số. Evidence gồm prompt/tools, PG before/after, source/hash, measurements và lỗi; Owner nhận một báo cáo ngắn + một ZIP. Đóng Gate3/4 theo Pilot vẫn mở lại lazy cho mỗi family mới, không khóa toàn hệ.
