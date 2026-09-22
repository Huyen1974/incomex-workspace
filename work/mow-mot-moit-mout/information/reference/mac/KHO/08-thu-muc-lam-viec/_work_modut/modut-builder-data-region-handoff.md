# Bàn giao data-region — MODUT

## Kết quả

- UI: `modut-builder-v1.html`
- Prefix riêng: `modut.*`
- Tổng số mã: **104**
  - DỮ LIỆU: **26**
  - HÀNH VI: **22**
  - GIAO DIỆN: **56**
- Snapshot chứa source + manifest + runtime audit: **`f4534ac`** (`modut: gắn data-region`)

## Trọng tài nguồn và DOM

- Source unique: **104**
- DOM runtime union: **104**
- State đã quét: **14**
- Thiếu trong DOM: **0**
- Thừa trong DOM: **0**
- Runtime error: **0**
- Prefix khác của trang: chỉ `shell.dock`, `shell.dock.chip` do dock dùng chung; đã loại trừ đúng.
- Không có mã thuộc `mout.*`, `mouthome.*`, `mot.*`, `modt.*`, `moit.*`, `modit.*`, `motstudio.*` trong source MODUT.

Các state gồm: base; đổi báo cáo; mở/tìm kho neo; mở/tìm/chọn người; thêm/xóa trigger; đổi kỳ/lịch; tắt/bật định dạng xuất; bấm đúc; trạng thái danh sách lặp rỗng.

## Ranh giới sửa

- Chỉ sửa `modut-builder-v1.html` và chỉ bổ sung thuộc tính `data-region` hoặc lệnh `setAttribute('data-region', ...)` cho phần tử render động.
- Không sửa `eco-nav.js`, `guide-dock.js`, `mot-theme-v1.css`.
- Không có `entry-engine.js` hay nhánh `modut.entry.*`.
- Không bump tham số `?v=`.

## Chứng minh chỉ-thêm-thuộc-tính

- SHA-256 gốc: `63a03dd941e3f12a9575ec32442310de693205ff20d074da94dd913e8a11110d` — 28,561 byte.
- SHA-256 sau gắn: `0e1f85169660f80d1f7ad44d5b8fd56740838019254caec372081fd07f83c458` — 32,367 byte.
- Gỡ mọi `data-region="modut.*"` và mọi lệnh `setAttribute('data-region','modut.*')` tái tạo đúng byte bản gốc và đúng SHA-256 gốc.
- Bản phục vụ công khai byte-identical với bản đã kiểm.

## Sản phẩm

- `modut-builder-data-region-manifest.csv`: UTF-8, 104 dòng dữ liệu, không dùng ký tự `›` trong mô tả.
- `modut-builder-runtime-audit.json`: 14,907 byte; có boundary, state, occurrence min/max, union và kiểm tra chức năng.
- `modut-builder-data-region-handoff.md`: file này.

## Hành vi demo cần ghi vào sổ

- `modut.run.cast` — nút **Đúc & lên lịch** hiện chỉ mở `alert` mô tả quy trình; chưa đăng ký thật vào `output_table_registry`, chưa tạo lịch/trigger chạy thật và chưa phân phối báo cáo thật.
- Các thao tác cấu hình còn lại cập nhật preview và JSON ở phía trình duyệt; chưa lưu PG/Directus.

## Đề nghị CW nghiệm thu độc lập

Parse lại `modut-builder-v1.html`, chạy DOM qua các state, đối chiếu manifest và chỉ tính prefix `modut.`; loại `shell.*`. Sau khi đạt mới điền 104 hợp đồng vào vùng Mẹ MOUT trong `SO_HOP_DONG`.
