# MOW T1 — Chuẩn mẫu công việc v1

## 1. Quyết định nền

Không tạo một bản HTML/JS cho mỗi task.

Toàn hệ thống chỉ có **một bộ dựng T1 dùng chung**. Mỗi task là một bản ghi dữ
liệu được đưa vào bộ dựng. Vì vậy 10 hay 10.000 task vẫn dùng cùng một cấu trúc,
cùng tooltip, cùng chiều cao hàng và cùng quy tắc kiểm tra.

Nguồn chuẩn:

- `mow-t1-work-standard-v1.js`: cấu hình, luật và kiểm tra tự động.
- `mow-unified-canvas-v2.html`: nơi sử dụng bộ dựng trong MOW.
- Mỏ neo giao diện tham khảo: `mow-tang1-v1.html`. File này chỉ là bản tham khảo
  thẩm mỹ của móc treo, không phải nguồn để nhân bản nghiệp vụ.

## 2. Phần được phép thay cho từng task

Chỉ thay dữ liệu đầu vào:

```js
{
  task: {
    code: "T1-001",
    title: "Nhận đơn"
  },
  inputItems: [
    { code: "FORM", label: "Form tiếp nhận" },
    { code: "WEBHOOK", label: "Webhook trigger" }
  ],
  referenceItems: [
    { code: "recipient", label: "Người nhận" },
    { code: "phone_number", label: "SĐT" }
  ]
}
```

Khi đã nối dữ liệu, mỗi dòng có thể bổ sung `collection`, `field`,
`data_address`, `data_type`, `json_contract`, `test`, `status`, `note`.

## 3. Phần cấm thay riêng

Không được viết lại hoặc copy riêng cho từng task:

- Tên, thứ tự và hướng dẫn cột.
- Kích thước header, hàng và khoảng nối.
- CSS của tooltip, placeholder, Test và Tình trạng.
- Ký hiệu `—` và `✓`.
- Quy tắc căn hàng trái/phải.
- Mã schema và cách sinh `mapping_id`.

Nếu nghiệp vụ buộc phải đổi một mục trong danh sách này, phải sửa file chuẩn,
tăng phiên bản và nghiệm thu lại toàn bộ; không vá riêng một task.

## 4. Quy trình thêm một task

1. Tạo hoặc đọc bản ghi task có `code` và `title`.
2. Chuẩn bị `inputItems` và `referenceItems`.
3. Gọi `MOW_T1_WORK_STANDARD_V1.createMachineData(config)`.
4. Bộ dựng dùng machine data để tạo hai thẻ và hai bảng.
5. Sau khi render, chạy `scheduleAudit(workspace)`.
6. Chỉ coi là đạt khi `.t1-workspace[data-t1-audit="ok"]`.

Không có bước copy file giao diện.

### Chế độ Thường và Đề xuất

T1 Thường dùng workspace hai cột. T1 Đề xuất là UI cũ đã chốt, chỉ có một cột
đề xuất và không hiển thị bảng mapping.

Bản hai cột dành cho admin được tách thành New MODT; không được đưa trở lại MOW
Đề xuất nếu Owner chưa yêu cầu cụ thể.

## 5. Điều kiện audit bắt buộc

- Cấu hình có task code, task title và mapping id không trùng.
- Danh sách cột đúng thứ tự chuẩn.
- Hàng trái và hàng phải cùng số lượng, cùng tọa độ, cùng chiều cao.
- Mọi tooltip chứa trọn nội dung, không có scroll overflow.
- Header màu nhạt nhưng độ đậm tối thiểu 600.
- Trình duyệt không có lỗi.

Kết quả gần nhất có thể đọc tại:

```js
window.__MOW_T1_LAST_AUDIT__
```

## 6. Luật phát hành

Khi sửa `mow-t1-work-standard-v1.js`:

1. Git snapshot trước sửa.
2. Sửa một nguồn chuẩn.
3. Tăng `VERSION` trong file và `?v=` tại trang nạp.
4. Kiểm chế độ Thường, Đề xuất, Vận hành và Quản trị.
5. Kiểm task có 0, 1, nhiều và nội dung rất dài.
6. Xác nhận audit `ok`, không lỗi trình duyệt.
7. Git snapshot sau sửa.

## 7. Nguyên tắc năng suất

Nhân bản **dữ liệu**, không nhân bản **mã**. Đây là điều kiện để sửa một lần áp
dụng cho toàn bộ task và không tạo nợ bảo trì theo số lượng task.
