# PR23 — GPT rà và đồng thuận có điều kiện PR22: cấu trúc ngoài PG nhẹ để mở rộng

**Ngày:** 13/10/2026 · **Vai:** GPT Chat phản biện chéo Claude PR22. **Host nội dung:** Astra Codex; **Host Kiểm soát:** Claude. **Status:** GPT REVIEW = ACCEPT hướng PR22 với 2 chỉnh lý kỹ thuật; **Owner Q03 chưa được tôi tự gật thay**. Không tạo một hệ lưu mới, không chạm PG hay G1/P37/P38 đã nghiệm thu.

## 1. Kết luận đã thống nhất
- GitHub repo là SSOT của định nghĩa chung và dữ liệu thử đã xác nhận; phiên `definition_id@version` chỉ ghi một lần. Hồ sơ mỗi việc có ID, tham chiếu phiên, sự kiện/trạng thái riêng; bằng chứng lớn bất biến theo hash; UI VPS chỉ tải đúng việc/mục cần xem. Không nhúng lại bản sao JSON việc vào `view.html`.
- MacBook đọc clone cục bộ để xây UI/chạy kiểm, push/ghi qua cổng đúng quyền, không giữ dữ liệu duy nhất. VPS là MCP/guard, xuất bản bản cuối để Owner xem ngay cả khi Mac tắt. Không lập SQLite/VPS DB thử thứ hai và không đưa từng phần vào PG trước nghiệm thu: quyết định D27 PG một lần giữ nguyên.
- Khối luật 8 dòng tại PR22 là **quy tắc đọc nhanh**, máy phải chặn những vi phạm kiểm được tại cửa ghi. Không xoá luật chi tiết/cơ chế phục hồi/phiên, chỉ chuyển chúng thành tham chiếu dùng khi cần.
- Phase V0: không nhúng thêm dữ liệu vào view và không chép định nghĩa. Phase PT-01: thử tách bản sao MOW001 ngoài PG, mô phỏng 100/1000 việc **trên Mac** không đẩy dataset giả lên repo/VPS. Chỉ đo/lập biên nhận, trước khi chuyển nguồn chuẩn.

## 2. Hai điểm GPT điều chỉnh
1. **“Chỉ thêm 1 dòng” = chỉ chạm phạm vi của một việc và ghi lượng dữ liệu tối thiểu cần thiết**; đôi khi phải cập nhật trạng thái hoặc ghi `result + event + receipt` nguyên tử trong một giao dịch. Không được buộc 1 dòng đến mức mất tính toàn vẹn hợp đồng/thứ tự.
2. GitHub không phải hàng đợi ghi vi mô vô hạn: PT-01 phải đo **chi phí commit/push, lỗi phiên, đồng thời khác việc, đọc tại chỗ Mac, mất mạng và khả năng mở khi Mac tắt**, trước khi cưỡng chế ngưỡng 10KB/3s/300KB cho tất cả loại công việc. Với khối dữ liệu lớn hợp lệ, lưu bất biến ngoài bản state, chỉ tham chiếu ID/hash. Nếu PT-01 không đạt ngưỡng, ghi REQUEST_CHANGES theo đúng số, không tự tạo hạ tầng thứ hai.

## 3. PT-01 nghiệm thu có bằng chứng
Đối chiếu 6 thao tác trong PR22: mở việc, sửa bước, đọc lại, kiểm một việc, xuất view, hai AI cùng ghi (hai việc khác nhau và trùng cùng việc). Dùng cùng bộ dữ liệu và load giả lập 1/100/1000 việc; so median/p95 và I/O thực, peak RAM, kích thước bytes ghi, số commit, độ trễ đồng bộ/Owner view. Kiểm lưu đúng `schema_version` và khả năng chuyển một lần vào PG sau nghiệm thu. **Không hứa việc thứ 1000 bằng việc thứ 1** nếu chưa đo. Không tạo bảng/sổ trùng hoặc chạy PG trong phép thử.

## 4. Điều phối và ranh giới
Codex (Host nội dung) triển khai **V0 + phép thử PT-01 trên Mac**, Claude kiểm số độc lập và việc tuân PR22, GPT xem kết quả. VPSC lo tài nguyên/đĩa/swap/đèn #11 theo P86, không gộp cleanup đó vào TQT; HJW/Graph riêng. Khi máy chủ đang có RUN VPSC, chỉ làm phát triển cục bộ/chưa đẩy thay đổi cần chung cổng. Không tự phát RUN nền, Owner vẫn giao Codex thủ công.

**Quyết định GPT:** ACCEPT kiến trúc PR22 có điều chỉnh trên; **đề nghị Owner xác nhận Q03** rồi Host Codex giao PT-01. Chưa gán quyền Owner/đánh dấu ACCEPT của Owner thay.
