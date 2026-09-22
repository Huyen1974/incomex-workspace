# Quy định làm việc của agent — Incomex UI production

File này là chỉ dẫn bền vững cho mọi phiên agent làm việc trong thư mục này.
Phải đọc trước khi sửa UI hoặc dữ liệu hợp đồng.

## Xưởng vẽ canonical

- `/opt/incomex/docs/mcp-writes` là **XƯỞNG VẼ GỐC DUY NHẤT** cho UI, luồng
  nghiệp vụ và hợp đồng thông tin đang thiết kế.
- Owner, Claude Cowork, Codex và Claude Code cùng đọc/ghi đúng cây thư mục này.
- Không tạo một bản “mới hơn” ở thư mục khác rồi để xưởng gốc thành bản cũ.
- `/opt/incomex/docs/mcp-writes/ui-preview` chỉ là symlink tương thích trỏ về
  chính xưởng gốc. Không biến nó lại thành thư mục hoặc SSOT thứ hai.
- Khi mang thiết kế sang repo ứng dụng/PG, phải ghi commit nguồn của xưởng và
  giữ xưởng là bản thiết kế tham chiếu. Không biến file xưởng thành output build.

## 0. Luật cao nhất — không tự sửa phần đã chốt

- Không tự thay đổi bất kỳ UI, nội dung, hành vi hoặc cấu trúc nào đã được Owner
  chốt nếu yêu cầu hiện tại không nói rõ phải sửa phần đó.
- Yêu cầu “lắp thêm”, “nhân sang” hoặc “thêm cột phải” không cho phép viết lại,
  đồng bộ hoặc cải tiến phần cũ.
- Phải giữ nguyên byte/DOM/hình dáng của phần ngoài phạm vi khi có thể.
- Nếu cho rằng cần sửa phần đã chốt để làm tốt hơn, dừng lại và hỏi Owner trước.
- Không dùng suy luận kiến trúc để mở rộng phạm vi thay cho chỉ dẫn của Owner.

## 1. Nguyên tắc nguồn chuẩn

- Không tạo nhiều bản mã cho cùng một loại UI.
- Nhân bản **dữ liệu/config**, không nhân bản HTML, CSS hoặc renderer.
- Mỗi cấu trúc dùng nhiều nơi phải có một nguồn chuẩn duy nhất.
- Khi nguồn chuẩn đổi, mọi consumer phải dùng phiên bản mới; cấm vá riêng một
  consumer nếu thay đổi thuộc quy tắc chung.
- File mẫu thẩm mỹ chỉ dùng để đối chiếu hình dáng, không mặc nhiên là source
  production.

## 2. Chuẩn T1 hiện hành

Nguồn production trên VPS:

- `/opt/incomex/docs/mcp-writes/mow-t1-work-standard-v1.js`
  — schema, tên cột, tooltip, placeholder, quy tắc layout và audit.
- `/opt/incomex/docs/mcp-writes/MOW_T1_WORK_STANDARD_v1.md`
  — hướng dẫn sử dụng và phát hành.
- `/opt/incomex/docs/mcp-writes/mow-unified-canvas-v2.html`
  — consumer production.
- `/opt/incomex/docs/mcp-writes/mow-tang1-v1.html`
  — mẫu thẩm mỹ móc treo, không dùng để nhân bản task.
- `/opt/incomex/docs/mcp-writes/new-modt-v1.html`
  — New MODT đang thiết kế; URL ổn định là `/admin-new-modt`.

Task mới chỉ được thay:

- `task.code`, `task.title`.
- `inputItems[]`, `referenceItems[]`.
- Giá trị mapping của từng dòng.

Không được thay riêng theo task:

- Tên/thứ tự/hướng dẫn cột.
- Kích thước header, hàng, khoảng nối.
- Tooltip, placeholder, Test, Tình trạng.
- Quy tắc căn hàng trái/phải và schema mapping.

T1 Đề xuất trong MOW là UI một cột đã chốt, không có bảng mapping. Bản hai cột
dành cho admin thuộc New MODT; không được đưa cột phải trở lại MOW Đề xuất nếu
Owner chưa yêu cầu.

## 2A. Truy cập trong giai đoạn thiết kế

- `/ui-preview/`, `/ui-preview/mcp-writes/` và `/admin-new-modt` phải mở trực
  tiếp từ VPS, MacBook và các agent.
- Không thêm Basic Auth, đăng nhập hoặc rào cản truy cập vào các đường dẫn này
  khi Owner chưa yêu cầu rõ.
- Quyết định này thay thế chỉ dẫn PHASE-0.5A cũ về việc khóa UI preview.

## 3. Điều kiện nghiệm thu T1

Sau khi render, `.t1-workspace` phải có:

```text
data-t1-audit="ok"
```

Đồng thời phải kiểm:

- Hàng trái/phải chênh lệch 0 px.
- Mọi tooltip chứa trọn nội dung.
- Header màu nhạt nhưng font-weight tối thiểu 600.
- Không trùng mapping id, không sai thứ tự cột.
- Không có lỗi trình duyệt.
- Kiểm các chế độ Thường, Đề xuất, Vận hành, Quản trị có liên quan.

## 4. Quy trình sửa production

1. Đọc file sống trên VPS và Git status.
2. Xác định thay đổi thuộc nguồn chuẩn hay dữ liệu riêng.
3. Git snapshot trước khi sửa nếu chưa có mỏ neo phù hợp.
4. Sửa nguồn chuẩn; không sửa bằng copy-paste hàng loạt.
5. Nếu file JS/CSS dùng chung đổi, tăng version cache tại consumer.
6. Kiểm bằng số và kiểm trực quan trên UI thật.
7. Chỉ đóng việc khi audit đạt và trình duyệt không lỗi.
8. Ghi Git snapshot sau sửa, báo commit cho Owner.

## 5. Git VPS

Cuốn sổ Git của toàn xưởng là local-only:

```text
/usr/local/bin/mcp-writes-git
```

Lệnh ghi mỏ neo:

```text
mcp-writes-git snapshot "ly do"
```

Timer tự chụp mỗi 5 phút chỉ là lưới an toàn. Agent vẫn phải chụp thủ công trước
và sau thay đổi lớn. Không push; repo không có remote.

## 6. Khi yêu cầu chưa rõ

- Không tự cắt yêu cầu nghiệp vụ để làm code gọn.
- Không tự thêm biến thể UI.
- Hỏi hoặc phản biện trước nếu quyết định sẽ làm thay đổi nguồn chuẩn, nghiệp
  vụ hoặc cách người dùng thao tác.
