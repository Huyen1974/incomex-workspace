# HANDOFF — Drawer khuôn chung “1 form · 1 kiểu · dùng mọi nơi” (vòng 1)

## Kết quả

Drawer `master-list.js` đã đổi từ kiểu “kitchen-sink” thành **một khung cố định gồm 2 khu** cho MOW, MOT, MOIT và MOUT:

- **Khu A — bản xem thật:** ưu tiên phần lớn diện tích, chỉ đọc (`inert`), không dựng lại form trong drawer.
- **Khu B — hỗ trợ vận hành:** đường dẫn 7 tầng, trigger/hàng đợi/điều kiện khi có, 3 vai người khi có, và bảng PG kết nối.

Khung, vị trí và cách đọc giữ nguyên giữa các Mẹ; chỉ nội dung theo Mẹ thay đổi.

## Cách tái dùng renderer

- **MOW:** dùng lại nguyên ma trận `master.process.*`.
- **MOT:** dùng đúng form MOIT qua `MOT.renderCluster`.
- **MOIT:** dùng form nhập qua cùng `MOT.renderCluster`.
- **MOUT:** dùng renderer KV/bảng hiện có của MOT qua hàm công khai mới `MOT.renderReferences`.

`master-drawer-view-v1.js` chỉ là adapter schema: chọn `form_schema` / `report_schema`, chuẩn hóa đầu vào, rồi gọi renderer chung. File này **không vẽ lại ô nhập, form hay bảng báo cáo**.

Các region `mot.*` xuất hiện trong Khu A là region **mượn từ renderer chung**, không đăng ký lại thành `master.*`.

## Delta data-region để CW cập nhật sổ

- Trước: **143** mã `master.*` đang hoạt động.
- Thêm: **18** mã BUILT cho Khu A/Khu B.
- Bỏ: **10** mã kitchen-sink; ghi lịch sử `TO_REMOVE`.
- Sau: **151** mã `master.*` đang hoạt động.

File delta: `master-list-drawer-manifest.csv`.

Nhóm bỏ:

- `master.drawer.info*`
- `master.drawer.links*`

Nhóm giữ:

- `master.drawer.hierarchy.*`
- `master.process.*`
- header/identity/actions của drawer.

## Audit trên URL công khai

- Source **151** = DOM union **151**.
- Thiếu **0**, thừa **0**.
- 10 mã bỏ còn trong source **0**, còn trong DOM **0**.
- **25 state**: list/tree/drawer/empty trên các consumer; đủ MOW/MOT/MOIT/MOUT, Master hub và list quy trình.
- MOT/MOIT: form dùng cùng renderer.
- MOUT: đã kiểm cả báo cáo KV và báo cáo dạng bảng.
- Runtime error: **0**.
- Có 6 cảnh báo CSP Google Fonts vốn đã tồn tại; fallback font hoạt động, không liên quan thay đổi này.

File chi tiết: `master-list-drawer-audit.json`.

## Cache đã nâng đồng loạt

- `master-list.js?v=5` → `master-list.js?v=6` trên các consumer URL cố định.
- `master-list-quy-trinh-v1.html` tiếp tục dùng `?ts=` nên không cần số phiên bản.
- `mot-render-v1.js?v=17` → `v=18` vì công khai renderer báo cáo dùng chung.
- Adapter mới: `master-drawer-view-v1.js?v=1`.

## File thay đổi

- `master-list.js`
- `mot-render-v1.js`
- `master-drawer-view-v1.js` (mới)
- `master-hub.html`
- `mot-master-v1.html`
- `mow-master-v1.html`
- `moit-master-v1.html`
- `mout-home-v1.html`
- `master-list-quy-trinh-v1.html`
- `mot-dashboard-v1.html`
- `mot-studio-v1.html`

## Giới hạn chủ đích của vòng 1

- Khi item chưa có `form_schema`, `report_schema`, `steps` hoặc dữ liệu hỗ trợ, adapter dùng **dữ liệu mẫu có nhãn rõ “mẫu vòng 1”**.
- Tên bảng PG, trigger và vai người mẫu **chưa phải sự thật PG**.
- Khi PG/schema thật sẵn sàng, chỉ thay dữ liệu trong `MASTER_CONFIG.items`; khung drawer và renderer không phải viết lại.

## Hash chính sau sửa

- `master-list.js`: `eea6d2a84fca3f3ec669b9a9d0fb1bfd5eb69bbd60440ec3654ebeac745b6791`
- `mot-render-v1.js`: `a56beced841e526d8ba31f192d2e6ea3c2c7c54a974ad4eea86c0c57186f88e8`
- `master-drawer-view-v1.js`: `434bc380a5695987f7689f45361f2991a64e8dfc7b4ede079fa5f813660fa927`

Snapshot source: `d3e7f84`.
