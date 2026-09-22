# Quy định làm việc của agent — Incomex UI production

File này là chỉ dẫn bền vững cho mọi phiên agent làm việc trong thư mục này.
Phải đọc trước khi sửa UI hoặc dữ liệu hợp đồng.

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

- `/opt/incomex/docs/mcp-writes/ui-preview/mow-t1-work-standard-v1.js`
  — schema, tên cột, tooltip, placeholder, quy tắc layout và audit.
- `/opt/incomex/docs/mcp-writes/ui-preview/MOW_T1_WORK_STANDARD_v1.md`
  — hướng dẫn sử dụng và phát hành.
- `/opt/incomex/docs/mcp-writes/ui-preview/mow-unified-canvas-v2.html`
  — consumer production.
- `/opt/incomex/docs/mcp-writes/ui-preview/mow-tang1-v1.html`
  — mẫu thẩm mỹ móc treo, không dùng để nhân bản task.

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

Trong giai đoạn thiết kế hiện tại, New MODT phải mở trực tiếp, không đặt đăng
nhập, Basic Auth hoặc rào cản truy cập. Chỉ bổ sung phân quyền khi Owner yêu cầu.

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

Cuốn sổ Git của UI preview là local-only:

```text
/usr/local/bin/ui-preview-git
```

Lệnh ghi mỏ neo:

```text
ui-preview-git snapshot "ly do"
```

Không dùng `git -C /opt/incomex/docs/mcp-writes/ui-preview` vì có thể đi vào
repo cha sai phạm vi.

## 6. Khi yêu cầu chưa rõ

- Không tự cắt yêu cầu nghiệp vụ để làm code gọn.
- Không tự thêm biến thể UI.
- Hỏi hoặc phản biện trước nếu quyết định sẽ làm thay đổi nguồn chuẩn, nghiệp
  vụ hoặc cách người dùng thao tác.
