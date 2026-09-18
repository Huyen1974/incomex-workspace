# AGENTS.md — Incomex Workspace

> ⏳ **ĐANG CHỈNH (vòng 2, 18/09/2026)** — file này đang được vòng 2 rút gọn thành cửa vào; hợp đồng chuẩn chuyển hết sang `README.md` (lên v1.1). **Các agent khác không sửa `AGENTS.md` và `README.md` cho tới khi hợp đồng lên v1.1.** Dòng này sẽ được gỡ khi xong.

Quy tắc chung cho AI/Agent làm việc trong repo này. Đọc khi cần thao tác file/repo; không cần nghiên cứu lại từ đầu mỗi phiên.

## 1. Nguồn hiện hành
- GitHub trên đúng branch/ref đang làm là nguồn hiện hành.
- Trước khi sửa, lấy **SHA hiện tại** của file. Không tin bản chat/local cũ nếu chưa đối chiếu.
- Nếu SHA đã đổi: **không ghi đè**; đọc lại và reconcile.

## 2. Đọc file hiệu quả
- Nếu chỉ cần một phần, **không đưa cả file lớn vào context/model**.
- File >1 MB: dùng `fetch_file` lấy metadata/SHA → `fetch_blob` → search/cắt đoạn trong tool → chỉ đưa đoạn liên quan cho AI.
- `fetch_file(start_line/end_line)` có thể trả content rỗng với file >1 MB; dùng blob thay thế.
- Chỉ đọc toàn file khi nhiệm vụ thật sự cần suy luận/kiểm toàn cục.

## 3. Sửa file
- Xác nhận target đúng và duy nhất trước khi replace.
- Giữ phần ngoài phạm vi yêu cầu nguyên vẹn; không dựng lại phần chưa đọc.
- Update bằng **SHA hiện tại**.
- Sau sửa: đọc lại/diff. Có thay đổi ngoài dự kiến → dừng hoặc hoàn nguyên.
- Thử nghiệm dùng branch/path riêng; không chạm production nếu chưa được giao rõ.

## 4. Đường dẫn, Unicode, assets
- Giữ nguyên path/tên file Unicode; không tự normalize/rename.
- Giữ relative paths, assets và manifest liên quan nếu nhiệm vụ không yêu cầu thay đổi.
- Không tự nhúng binary/base64 vào file text lớn.
- Hạn chế tạo thêm tài liệu hướng dẫn; ưu tiên cập nhật chính file `AGENTS.md` này.

## 5. Cách Agent báo kết quả
- Chỉ báo PASS khi đã gọi tool/kiểm thật; không suy từ báo cáo cũ.
- Nêu ngắn: file/path, branch/ref, SHA trước/sau, phần đã đổi, kiểm tra đã chạy.
- Nếu có giới hạn công cụ: nói đúng giới hạn và dùng workaround đã kiểm chứng.
