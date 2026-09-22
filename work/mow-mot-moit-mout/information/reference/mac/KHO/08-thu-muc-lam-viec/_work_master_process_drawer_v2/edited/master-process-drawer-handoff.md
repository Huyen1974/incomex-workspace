# HANDOFF — Drawer QUY TRÌNH “Admin nhìn một phát thấy đủ” — vòng 1

## Kết quả

Đã làm lại **riêng Khu A của drawer MOW/quy trình**. Ma trận lạ của vòng trước đã bỏ hoàn toàn. Bản mới là chế độ chỉ-xem của chính **MOW · Đề xuất nâng cao**, mở rộng đủ thông tin vận hành:

1. **Bắt đầu bằng gì:** trigger khởi động · điều kiện chạy · hàng đợi đầu vào.
2. **Tiếp theo là gì:** thứ tự từng việc · nối tiếp/song song · phụ thuộc · trigger/điều kiện/queue/tín hiệu ra · ba vai người · phút thực thi và dự phòng.
3. **Còn thiếu gì để chạy:** số điểm thiếu hiện ngay trên đầu drawer; checklist chi tiết ở cuối.

Khu B giữ đường dẫn 7 tầng và bảng PG. Trigger/vai người cấp việc đã chuyển vào Khu A nên không chép lại ở Khu B.

## Dùng lại UI đã có

Renderer read-only được đặt trong `mvx-v3.js`, cùng file đang vận hành giao diện MOW nâng cao. Drawer mượn nguyên các region:

- `mow.propose.advanced.timetable`
- `mow.propose.advanced.timetable.accumulate`
- `mow.propose.advanced.timetable.buffer`
- `mow.propose.advanced.timetable.inputmode`
- `mow.propose.advanced.timetable.total_exec`
- `mow.propose.advanced.timetable.total_buffer`
- `mow.propose.advanced.timetable.total_all`

Không đăng ký lại bảy mã này trong Excel. Các thông tin vận hành chưa từng có UI dùng nhóm mới `master.drawer.process.*`.

## Ý kiến/phản biện sau khi đọc engine thật

`mvx-v3.js` hiện chỉ có:

- kéo-thả để đổi thứ tự;
- phút thực thi từng việc;
- buffer phát sinh;
- cộng tổng tự động/nhập tay.

Engine **chưa có logic thật** cho:

- `depends_on` hoặc song song/nối tiếp;
- hàng đợi từng việc;
- trigger và điều kiện cấp quy trình;
- tín hiệu ra thành hợp đồng;
- vai làm thay từ SSOT nhân sự.

Mã/region `task_alloc` nêu trong brief **không tồn tại trong source sống**. Vì khái niệm đã chốt `tg_chi_dinh` là phút chỉ định **cả quy trình T2**, bản này hiển thị nó ở phần tổng, không tự đẻ “phút chỉ định từng việc”. Nếu Owner muốn phút chỉ định cấp T1, đó phải là quyết định nghiệp vụ mới trước khi thêm UI/PG.

Khi chưa có contract thật, drawer nói rõ “chưa có trong nguồn chuẩn” hoặc “đang suy từ thứ tự”; không giả vờ dữ liệu đã hoàn chỉnh.

## Delta cho CW cập nhật sổ

- Trước: 151 mã `master.*` hoạt động.
- Bỏ ma trận cũ: 33 mã `master.process*` → `TO_REMOVE`.
- Thêm bản vận hành: 30 mã `master.drawer.process*` → `BUILT`.
- Sau: 148 mã `master.*` hoạt động.

File: `master-process-drawer-manifest.csv`.

## Audit công khai

- Source **148** = DOM union **148**.
- Thiếu 0 · thừa 0.
- 33 mã cũ còn trong source 0 · còn trong DOM 0.
- 24 state trên MOW Master, list quy trình, Master Hub, MOT, MOIT, MOUT.
- MOW Canvas: “Đề xuất nâng cao” vẫn mở; timetable/tổng vẫn nguyên.
- MOT/MOIT/MOUT: renderer cũ không đổi.
- Runtime error: 0.

File: `master-process-drawer-audit.json`.

## Tự đánh giá theo mục tiêu Owner

### 1. Quy trình bắt đầu bằng gì?

**Đạt về UI.** Ba thông tin nằm ngay đầu. Dữ liệu hiện nói thật “chưa có trong nguồn chuẩn” khi chưa có SSOT.

### 2. Tiếp theo là gì, việc nào song song/nối tiếp?

**Đạt về cách nhìn, chưa đạt về dữ liệu thật.** Trình tự và trường quan hệ nhìn rõ; nhưng quan hệ hiện phải suy từ thứ tự vì engine/PG chưa có `depends_on`.

### 3. Còn thiếu gì để chạy?

**Đạt.** Số điểm thiếu thấy ngay ở đầu drawer; checklist nêu đúng từng nhóm thiếu.

Kết luận trung thực: **drawer đã đạt mục tiêu “nhìn là hiểu”; hệ thống dữ liệu chưa đủ để quy trình chạy thật**. Chính UI mới đã làm lộ đúng phần phải thiết kế PG tiếp theo.

## Cache và file thay đổi

- `master-list.js?v=7`
- `master-drawer-view-v1.js?v=2`
- `mvx-v3.js?v=4`
- Các consumer cố định đã bump đồng loạt; list quy trình tiếp tục `?ts=`.

File code:

- `master-list.js`
- `master-drawer-view-v1.js`
- `mvx-v3.js`
- `mow-unified-canvas-v2.html`
- `mow-master-v1.html`
- `master-hub.html`
- `master-list-quy-trinh-v1.html`
- `mot-master-v1.html`
- `moit-master-v1.html`
- `mout-home-v1.html`

Snapshot source: `59ab442`.
