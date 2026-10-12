# PR19 — Gắn bảng QTTH 006 vào Over view chính

**Owner yêu cầu:** hiển thị **100 bước QTTH 006** tại `knowledge/modules?task=tools-quy-trinh&view=content&section=over-view`, **ngay trước** mục “5 Quy trình tổng hợp”, trong khối **thu gọn mặc định**; bảng này là **quy trình dùng chung**, còn trạng thái thực hiện là **hồ sơ từng việc**.

## Đã hoàn thành và kiểm được

- **Nguồn 100 bước:** `work/tools-quy-trinh/MOW-TH-006.md`, phiên `0.1-owner-directed-design`, SHA256 `7b60a1c212d564b46fde8a3d8e6e4ea8b4741f12fb9eaa3a0425a89060f6805b`. Bảng đủ 100 bước và 8 cột; 7 mốc CP01–CP07: 14/26/12/24/13/5/6.
- **Bản chiếu thuần đọc đã tạo trên UI VPS:** `ui/qtth006-overview-v1.js`, SHA256 `2aff33ef79983e524456f51578b227f1f9e7e1df6b3879e51cab9deed5ca8005`. JavaScript tự chèn một khối `<details>` và bảy nhóm con trước `.ov-section > h2` có dòng “5 Quy trình tổng hợp”, dùng mã + tên Master/DOT đúng nguồn; không tự ghi trạng thái. Bảng tình trạng là “—” vì đây là quy trình dùng chung.
- **Trang QA đọc ngay:** https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/qtth006-overview-preview-v1.html . Bản xem thử chỉ là QA độc lập, **không phải đã tích hợp lên Overview chính**.
- **Kiểm browser:** trên trang QA `#tqt006-overview-guide` HTTP 200; hiển thị tiêu đề, dòng “100 bước · 7 mốc”, mặc định thu gọn; `console_errors.count=0`. Lượt kiểm mobile/nhóm khác bị `BROWSER_UNAVAILABLE/WORKSPACE_BUSY`, chưa xác nhận toàn bộ UI.

## Điểm còn phải xử lý (CHƯA XONG)

`work/tools-quy-trinh/view.html` hiện ~101,7 MB; hai lần gọi `workspace_transaction` cố sửa trực tiếp tệp lớn trả `RECOVERY_REQUIRED` (chưa có commit đổi view). Tác vụ sửa một dòng được đưa vào `workspace_task_start` nhưng worker restart rồi kẹt hàng đợi, đã **hủy an toàn** (task `fe73256f4a4c496bbbf533064981e0a7`). Đối chiếu `workspace_diff` từ HEAD `0292df4...` đến HEAD `1620c650...` cho view.html cho kết quả **diff rỗng**; chưa được phép tuyên bố Overview chính đã đổi.

**Host Codex được Owner giao UI phải dùng đường vá luồng/terminal phù hợp cho tệp lớn, tránh đưa 100 MB vào bộ nhớ/chạy lại giao dịch lỗi.** Chỉ cần chèn một dòng trước `</body>` của `work/tools-quy-trinh/view.html`:

```html
<script defer src="/ui-preview/mcp-writes/qtth006-overview-v1.js"></script>
```

Giữ nguyên toàn bộ `view.html` ngoài dòng đó. Kiểm `grep/rg` để **không chèn hai lần**, kiểm HEAD/source hash trước sửa, backup rollback; tuân thủ cổng ghi VPS và quy định công cụ hiện hành. Không dùng SSH đi vòng cổng bảo vệ. Nếu không thể vá đúng quyền, ghi BLOCKED cho Owner, không phá P37.

## Nghiệm thu bắt buộc sau khi Host gắn

1. Trang **[Over view chính](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=over-view)** hiển thị `QTTH 006 · Quy trình thực hiện QTTH 05` **ngay trên** mục `5 Quy trình tổng hợp`; không được chỉ đưa link trang riêng.
2. Khối ngoài đóng mặc định; khi mở có **7 nhóm** cũng đóng, bấm mở các nhóm thấy **100 dòng trong 8 cột**, đọc được bảng trên desktop/mobile (cuộn ngang có giới hạn).
3. Nguồn/phiên/hash QTTH006 hiển thị là bản thiết kế dùng chung; ô Tình trạng không tự nhận đã thực hiện, checkbox việc bổ sung không làm thay quyết định/ACK; không chép dữ liệu vào hồ sơ MOW001 hoặc MOW002.
4. Sau xuất kiểm **revision/html script có tồn tại**, CSS/JS tải đúng và `ui_inspect`/browser không lỗi (HTTP 200 đơn độc không đủ). Chạy các bộ CHECK005/006 nếu quy định hiện hành yêu cầu, lưu kết quả vào các Master/sổ đang có.
5. Đọc lại và ghi commit/bằng chứng; **không tự coi QTTH006 đã nghiệm thu** chỉ vì trình bày thành công. Đăng ký quy trình 006 vào Master và triển khai bảng tình trạng riêng của mỗi hồ sơ là việc Host tiếp theo theo PR18, không trộn vào bước hiển thị nhỏ này.

**Vai:** GPT đề xuất/QA read-only; Codex Host nội dung tiếp nhận, Claude giữ §0. Không phát RUN tự động; Owner tự giao như hiện hành.
