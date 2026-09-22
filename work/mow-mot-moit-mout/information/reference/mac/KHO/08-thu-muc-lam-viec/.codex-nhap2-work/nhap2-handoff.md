# NHÁP 2 — BÁO CÁO KHÔI PHỤC ĐỦ NGHIỆP VỤ, TỔ CHỨC LẠI CHO GỌN

Ngày kiểm: 2026-07-21  
Trang: `mow-master-nhap2-v1.html`  
Nguồn góp ý: `mow-unified-canvas-v2.html` — chế độ **Đề xuất/Cải tiến**.

## 1. Kết luận

Nháp 2 không cắt bài toán của Nháp 1. Bản này tổ chức lại theo thứ tự:

> **YÊU CẦU → QUY TRÌNH → HỢP ĐỒNG/BẢNG/UI/MÃ**

Thay đổi quan trọng nhất:

- Đề xuất không còn là phiếu thay đổi. Nó là một dòng text do người đang làm gửi; hệ tự gắn bối cảnh.
- Admin đọc, gộp, họp và quyết định bằng con người. Hệ không bắt phân tầng, không tạo vòng đời phiếu năm chặng.
- Quy trình Thiết kế & phát hành chỉ bắt đầu khi admin đã quyết định sửa.
- Một task MOT có đúng một MOIT; có thể có nhiều MOUT. Hai MOIT là hai task.
- `WAIT_ONLY` chỉ là timer, không phải task.
- Một `event_log` append-only lưu toàn bộ sự kiện thật. Không đặt chỉ tiêu số lượng event.

## 2. Các luồng theo chuẩn ba phần

### P0 · Góp ý cải tiến trong MOW

**ĐIỂM BẮT ĐẦU:** Người đang làm một task và nhận ra điều bất hợp lý hoặc có thể làm tốt hơn.

1. Mở Góp ý ngay từ công việc hiện tại.
2. Gõ một dòng text và gửi.
3. Hệ tự gắn người, thời điểm, task, run, bước và bản ghi nghiệp vụ.
4. Hệ thêm một dòng vào sổ góp ý nháp của admin.

**ĐIỂM KẾT THÚC:** `IMPROVEMENT_SUGGESTION_QUEUED`.

### Cầu nối con người · không tự động hóa

**ĐIỂM BẮT ĐẦU:** `IMPROVEMENT_SUGGESTION_QUEUED`.

1. Admin đọc, gộp, trao đổi hoặc họp.
2. Admin quyết định không sửa, chờ thêm hoặc bắt đầu thiết kế.
3. Nếu sửa, admin ghi mục tiêu ngắn và bối cảnh bị ảnh hưởng.

**ĐIỂM KẾT THÚC NẾU SỬA:** `DESIGN_DECISION_RECORDED`.

### P1 · Thiết kế & phát hành

**ĐIỂM BẮT ĐẦU:** `DESIGN_DECISION_RECORDED`.

1. Mở lượt thiết kế, ghi mục tiêu ngắn và các góp ý liên quan.
2. Giữ một lượt đang dựng trên mỗi mã gốc; các góp ý khác tiếp tục nằm trong sổ nháp.
3. Tạo v1 hoặc sao nguyên nhóm phiên bản hiện hành.
4. Chứng minh bản sao chưa sửa chạy y hệt bản cũ.
5. Lắp MOW với các MOT; mỗi MOT có đúng 1 MOIT và 0..n MOUT.
6. Máy sinh diff; admin ghi lý do, tác động và đường quay lại.
7. Chạy catalog kiểm theo phiên bản; dấu kỹ thuật trỏ đúng lần kiểm.
8. Ghi dấu pháp lý.
9. Bật nguyên tử cả nhóm; bản cũ thành `RETIRED`, không bị xóa.
10. Lập các mốc đo kết quả và đóng lượt thiết kế.

**ĐIỂM KẾT THÚC:** `RELEASE_GROUP_PUBLISHED`.

### P2 · Chạy & quan sát

**ĐIỂM BẮT ĐẦU:** `BUSINESS_TRIGGER_ACCEPTED` hoặc `NEXT_WORKFLOW_TRIGGER_ACCEPTED`.

1. Chống trigger trùng và gắn khóa ngoại bản ghi nghiệp vụ.
2. Khóa trọn nhóm phiên bản MOW + MOT + MOIT + MOUT cho suốt run.
3. Tạo run, step_run và timer `WAIT_ONLY` riêng.
4. Tìm đúng người/agent, áp ủy quyền còn hiệu lực và đẩy việc về MOT.
5. Kiểm đầu vào; thiếu thì `BLOCK_AND_NOTIFY`.
6. Nhận việc nguyên tử; hiện đúng 1 MOIT và các MOUT tham khảo.
7. Ghi kết quả, thay đổi dữ liệu và event; chỉ hoàn tất một lần.
8. Xử lý retry, lỗi, trả sửa, hủy-bù và bàn giao có xác nhận.
9. Kết thúc run, phát tín hiệu tiếp theo và ghi quan sát tải/chậm/kết quả.

**ĐIỂM KẾT THÚC:** `RUN_FINISHED` hoặc `NEXT_WORKFLOW_TRIGGER_ACCEPTED`.

## 3. Kiểm khoảng trống

| Mối nối | Kết thúc trước | Bắt đầu sau | Kết quả |
|---|---|---|---|
| Góp ý → admin xem | `IMPROVEMENT_SUGGESTION_QUEUED` | `IMPROVEMENT_SUGGESTION_QUEUED` | Khớp |
| Admin quyết định → thiết kế | `DESIGN_DECISION_RECORDED` | `DESIGN_DECISION_RECORDED` | Khớp |
| Run này → workflow sau | `NEXT_WORKFLOW_TRIGGER_ACCEPTED` | `NEXT_WORKFLOW_TRIGGER_ACCEPTED` | Khớp |
| Phát hành → chạy | `RELEASE_GROUP_PUBLISHED` | `BUSINESS_TRIGGER_ACCEPTED` | Cố ý không nối trực tiếp: phát hành chỉ làm bản sẵn sàng; trigger nghiệp vụ đến sau mới tạo run. |

## 4. Công thức MOT

> **1 MOIT + 0..n MOUT + vai/người + thời gian + input/output + trigger/kết quả + loại việc + FK bản ghi + xử lý lỗi + retry-safe = 1 MOT**

- MOIT: đúng một form nhập. Cần nhiều dữ liệu thì thêm field. Hai form là hai task.
- MOUT: không hoặc nhiều báo cáo chỉ-đọc để người/máy ra quyết định.
- Người/máy dùng cùng một cấu trúc task.
- Loại task: thực hiện, kiểm tra hoặc phê duyệt.
- Failure: dừng/báo, mở sự cố hoặc bỏ qua nhánh độc lập.
- `retry_safe` quyết định được chạy lại tự động hay phải giao người đối chiếu.
- `WAIT_ONLY` không có MOIT, người hay cạnh công việc.

## 5. Mười bốn việc nghiệp vụ

| # | Việc | Nằm ở đâu |
|---:|---|---|
| 1 | Góp ý cải tiến | P0 bước 1–4 |
| 2 | Định tầng/gộp ý | Cầu nối con người; không ép thành bước hệ thống |
| 3 | Duyệt nghiệp vụ | `DESIGN_DECISION_RECORDED`; P1 bước 1 giữ bằng chứng |
| 4 | Diff máy + lý do người | P1 bước 6 |
| 5 | Nhiều góp ý, một lượt đang dựng | Sổ nháp P0 + P1 bước 2 |
| 6 | Nhân bản cả danh sách việc | P1 bước 3 |
| 7 | Chưa sửa phải chạy y hệt | P1 bước 4 |
| 8 | Bật/tắt nguyên tử | P1 bước 9 |
| 9 | Nghỉ hưu khác khai tử | P1 bước 9 + nhánh dọn `RETIRED` |
| 10 | Khóa phiên bản theo run | P2 bước 2 |
| 11 | Ủy quyền khi vắng | P2 bước 4; chờ xác nhận nguồn người |
| 12 | Trả lại sửa có đếm vòng | P2 bước 8 |
| 13 | Hủy không xóa dữ liệu, có bù | P2 bước 8 |
| 14 | Quản lý xem việc cấp dưới | P2 bước 4 + view vận hành; chờ `reports_to` |

## 6. Dữ liệu gốc và sự kiện

- Một `event_log` append-only bắt tất cả sự kiện đã xảy ra.
- Có bao nhiêu sự kiện thật thì bổ sung bấy nhiêu; không có con số mục tiêu.
- Định nghĩa, phiên bản, quan hệ, run và step_run vẫn là bảng vận hành riêng.
- Trạng thái hiện tại không suy lại từ event.
- Event giữ actor, thời điểm xảy ra/ghi nhận, loại, kết quả, lý do, chuỗi nguyên nhân, idempotency và payload nhỏ.
- Run/step_run gắn task MOT và khóa ngoại bản ghi nghiệp vụ; sự kiện quản trị gắn quyết định/phiên bản.

## 7. Câu hỏi bắt buộc gửi Owner

1. Incomex đã có một bảng nhân sự/người chính thức hay chưa? Tên bảng và khóa chính là gì?
2. Bảng người hiện có quan hệ ai báo cáo cho ai (`reports_to`/`manager_id`) hay chưa?
3. Năng lực phút/ngày nằm trong bảng người, lịch làm hay chưa có nguồn?
4. Một người có thể có nhiều lần ủy quyền, các khoảng thời gian chồng nhau hoặc phạm vi khác nhau không?
5. Mỗi loại run được phép trỏ tới những bảng nghiệp vụ nào?
6. Từng loại kết quả cần đo ở mốc nào và ai sở hữu metric?
7. Ai có quyền duyệt, phát hành và chuyển phiên bản trong vận hành thật?

Chưa có câu trả lời thì ghi **CHỜ XÁC NHẬN**, không tự dựng bảng.

## 8. Lệch còn mở trên MOW hiện tại

Nguồn góp ý đã xác nhận là `mow-unified-canvas-v2.html`. Tuy nhiên UI sống hiện còn:

- form “Đề xuất thêm ô” có tiêu đề + nội dung;
- form sửa cấu trúc mục con;
- chế độ “Đề xuất nâng cao” có nhiều trường;
- câu “Mọi thay đổi tạo đề xuất”.

Các phần này mâu thuẫn với quyết định mới “một dòng text + bối cảnh tự gắn”. Vòng này không sửa MOW gốc; cần một vòng riêng, có Git trước/sau.

## 9. Kiểm thử

- Cú pháp `nhap2-core.js` và `nhap2-render.js`: đạt.
- Bảy contract mẫu: mỗi contract đạt 10/10 validator nghiệp vụ.
- Mỗi ACTION có đúng một `moit_form_id`, mảng `mout_report_ids`, vai, FK bản ghi và `retry_safe`.
- `WAIT_ONLY` không có MOIT/người.
- Bảng đối chiếu có đủ 14/14 việc.
- Bốn mối nối đã được giải thích; ba mối nối event khớp byte-for-byte.
- DOM thật: 7 dòng danh sách; 6 tab Mặt bàn; luồng, công thức MOT, gap audit và 14 mapping đều render.
- Cổng phát hành vẫn bị chặn do bằng chứng chưa đủ; không tự nhận đã sẵn sàng.

## 10. Bảo toàn và Git

- Tag trước sửa: `nhap2-before-restore-business-intent`.
- Tag sau sửa: `nhap2-after-restore-business-intent`.
- Chỉ ba file Nháp 2 và báo cáo này thuộc phạm vi commit.
- Không sửa `mow-process-draft-v1.html` hoặc `master-list.js` trong vòng này.

SHA-256 sau sửa:

- `mow-master-nhap2-v1.html`: `f180462950397b0c26aa9e4d75b66855b59ba0ae57e26c2e4cd690b8b45d6483`
- `nhap2-core.js`: `8bd277b8d88686f115a6c91c6c4d7990d527fb2e6868414f0dcba7f7c93d170c`
- `nhap2-render.js`: `dddeb121a0398ba38fd3c9bad067ce7f6191e1228149652998af24530df85929`

