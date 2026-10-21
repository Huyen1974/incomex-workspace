# CT-000 — Bộ kiểm phản biện vòng 5

**Kết luận trên bản chốt: CHƯA ĐẠT.** Đây là công cụ rà nguồn và thử sức phát hiện của H7. Không phải phần mềm vận hành hàng đợi, không phải chứng nhận PG/Directus đã chạy đúng.

## Chạy lại

Giải nén, mở thư mục này và chạy bằng Python 3 (chỉ dùng thư viện chuẩn):

```bash
python3 audit_ct000.py --out audit-output
```

Kết quả bản chốt phải là `REJECT_CURRENT_SPEC_AND_CHECKER`, **exit code 1**. Xem `audit-output/summary.json`; mỗi phép kiểm có JSON, stdout và stderr riêng. Các kết quả đã chạy sẵn nằm trong `evidence/`.

Để chỉ định nguồn đã lấy về:

```bash
python3 audit_ct000.py \
  --html /path/to/ban-duyet.html \
  --collab /path/to/COLLAB.md \
  --checker /path/to/author_checker.py \
  --out audit-output
```

`author_checker.py` phải là khối Python H7 trích nguyên văn từ COLLAB tương ứng. Bộ mutation kiểm sự khớp này. Chỉ chạy mã H7 đã kiểm tra và tin cậy; công cụ gọi Python cục bộ để thực thi khối đó trong thư mục thử tạm.

## Mã thoát và giới hạn

- **1:** còn phát hiện hoặc chưa có bằng chứng chạy thật PG/Flow; không được cho triển khai dựa vào bộ này.
- **2:** nguồn/định nghĩa thay đổi ngoài phạm vi đã kiểm, đầu vào thiếu, hoặc công cụ không đánh giá được. Đây là cần rà lại, không phải đã sửa đạt.
- Bộ tổng không trả 0 để cấp phép triển khai. Nó chưa có phép thử PG/Flow thật. Mỗi bộ con phân biệt kết quả trong phạm vi của mình.

Các probe ngữ nghĩa được gắn với định nghĩa của bản đang chốt. Khi thay định nghĩa, cập nhật probe theo quy tắc mới và kiểm lại bằng ca đúng lẫn ca sai. **Không cập nhật hash chỉ để làm mất cảnh báo.** Các đoạn lời văn chưa có điều kiện/hành động có thể thực thi vẫn phải được đánh dấu chưa kiểm, không tự đoán nghĩa rồi cho qua.

## Thành phần

- `scripts/author_checker.py`: H7 nguyên văn, chưa sửa. Đây là đối tượng bị kiểm.
- `scripts/mutation_audit.py`: chạy lại H7; tạo 11 bản sao có lỗi cố ý và 3 đối chứng; lưu diff/stdout; đo đường đi của 14 ca gốc.
- `scripts/independent_audit.py`: parser độc lập, kiểm bảng/đồ thị, chỗ nối bộ phân loại với dòng T và vòng chờ phục hồi.
- `scripts/semantic_audit.py`: đường đi và dữ kiện cụ thể cho hạn phục hồi, bù, giao lại, ngoại lệ và dùng lại mã thao tác.
- `snapshots/`: phần nguồn đã đọc có đủ các bảng và toàn bộ H7 cần kiểm, kèm metadata. Đây là **trích đoạn**, không phải hai tệp remote đầy đủ.
- `REPORT.md`: kết luận và yêu cầu sửa cụ thể.
- `manifest.json`: phiên nguồn và SHA-256.
- `evidence/`: kết quả thực chạy của bộ tổng và từng bộ con.

## Phạm vi thực hiện

Nguồn `ban-duyet.html` và `COLLAB.md` được đọc qua workspace connector tại head `4c93ecce01d8889dcc4e7558fc604a526fe2b010`. Không sửa remote, không triển khai, không gửi email, không chạy lệnh SQL hoặc Directus Flow. Các số liệu về đột biến không phải lỗi đã tồn tại trong bản gốc; chúng đo chỗ H7 không phát hiện được khi nguồn bị cố ý làm hỏng.

Xem `REPORT.md` trước khi dùng các số đếm. Đặc biệt, 303 đầu vào bị từ chối không phải 303 lỗi; 46 khác biệt tiềm năng không phải 46 lỗi đã chứng minh; độ phủ 22,5% không phải tỷ lệ phần mềm đúng.
