# Code và gánh bảo trì — phạm vi R2–R8

**Product code mới = 0.** Không sửa product source, Flow, SQL function/trigger, schema, API, worker, runtime dependency hoặc luật nguồn. SSOT HTML chỉ đổi nội dung; scripts/styles giữ nguyên.

| Chỉ số | Lượt này | Giới hạn |
|---|---|---|
| New custom product code | 0 file / 0 dòng | Không build/deploy/upgrade; không cài runtime |
| Legacy custom — KEEP | Vai trò/component đề nghị trong role map | Chưa có inventory định lượng toàn hệ và maintenance owner đầy đủ; reuse không có nghĩa miễn phí bảo trì |
| Legacy custom — RETIRE | Ứng viên và điều kiện trong duplicate-disposition.md | Chưa xóa/vô hiệu hóa gì; consumer ngoài scope UNKNOWN |
| Legacy custom — REVIEW | Toàn bộ nguồn được rà trong freeze | Chưa xác minh runtime đầy đủ; không gọi source tồn tại thành PASS |
| Business truth ngoài PG | Chưa đo toàn hệ | Nhiều mock vẫn dùng memory/DOM/sessionStorage/localStorage; không được nhận làm canonical truth |

Gate0 candidate vẫn kê riêng: guard 163 dòng core + 2 entry và 50 SQL; UI adapter 87 dòng, UForm +9/−1; worker 92 dòng, 33 dòng DDL/5 bảng TEST. pg-boss 12.30.0 + pg 8.23.0 có 21 locked packages, schema queue 40 bảng và process worker riêng. Đây là chi phí đã có từ proof trước, không code mới lượt R2–R8, không production-final. Xem accepted/Gate0/code-inventory.md và platform-freeze.md.

**Harness rà soát cục bộ:** 10 file Python, 488 dòng vật lý (kể cả comment/blank). Chỉ thu thập bằng chứng, tạo báo cáo, QA và chuẩn bị một lần ghi SSOT; không thành phần sản phẩm. Danh sách/hash ở review-harness-inventory.json. CUA dùng snippet tương tác đọc UI và chụp bằng chứng; không có browser runner được cài vào sản phẩm. Số dòng harness không bao gồm snippet công cụ tương tác.

Patch RULE-SYNC là bản đề nghị chưa áp dụng. Source/evidence Gate0/R1 được sao chép chỉ để kiểm toán; không chạy lại các script có khả năng ghi. Không xem LOC thấp là bằng chứng chi phí thấp; trước adoption phải có exact compatibility, maintenance owner và đường thay thế.
