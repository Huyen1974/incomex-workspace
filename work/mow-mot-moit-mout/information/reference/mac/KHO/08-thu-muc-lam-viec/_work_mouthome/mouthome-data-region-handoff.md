# Bàn giao data-region — MOUT Home

## Kết quả

- UI: `mout-home-v1.html`
- Prefix riêng: `mouthome.*`
- Mã mới cần bổ sung vào sổ: **8**, đều thuộc nhóm **GIAO DIỆN**.
- Snapshot chứa source + manifest + runtime audit: **`45a99d4`** (`mouthome: gắn data-region`).

## Ranh giới dùng chung

- `master-list.js` là khuôn danh sách dùng chung, giữ nguyên SHA-256: `68b6478407428815784ed5c5a3959b2db6b5a925b6f8aec6a3945e65304f105d` — 42,496 byte.
- 135 mã `master.*` đã đăng ký một lần trong `SO_HOP_DONG`; **không thêm lại** ở vòng MOUT Home.
- Chỉ sửa `mout-home-v1.html`; không sửa `master-list.js`, `eco-nav.js`, theme và không bump `?v=`.
- `shell.dock`, `shell.dock.chip` do dock dùng chung sinh ra, đã loại trừ.

## Trọng tài source và DOM

- Source riêng `mouthome.*`: **8**.
- DOM riêng `mouthome.*`: **8**.
- Thiếu: **0**; thừa: **0**.
- Source dùng chung `master.*`: **135**.
- DOM dùng chung xuất hiện trên riêng trang này: **97**.
- 38 mã không render trên trang này là đúng thiết kế: 33 mã `master.process.*` cần payload `steps`; 5 mã họ `mother` cần `showMother=true`.
- Tổng union riêng trang: **105** = 97 dùng chung + 8 riêng.
- Đã quét 14 state: danh sách, tìm trúng/rỗng, 4 trạng thái lọc, drawer human/DOT, cây đầy/mở/rỗng và quay về danh sách.
- Runtime error: **0**.

## Chứng minh chỉ-thêm-thuộc-tính

- SHA-256 gốc: `5570705426e6d170d4ff770f306fde169739cfd9c2b9a3722cc27cc366524c3d` — 3,669 byte.
- SHA-256 sau gắn: `15db17c6116facd0b0c667846d8a758874593719b0ada582b7d037491933639d` — 3,931 byte.
- Gỡ 8 thuộc tính `data-region="mouthome.*"` tái tạo đúng byte và SHA-256 bản gốc.

## Lưu ý vận hành

- Các địa chỉ UI đã BUILT và hoạt động.
- Danh sách 10 báo cáo hiện lấy từ `window.MASTER_CONFIG.items` khai tĩnh trong HTML; chưa chứng minh đọc registry/PG thật. Ghi lưu ý này tại hợp đồng `mouthome.list.host` để tránh hiểu nhầm “đã đúc” là dữ liệu sống.

## Sản phẩm

- `mouthome-data-region-manifest.csv`
- `mouthome-runtime-audit.json`
- `mouthome-data-region-handoff.md`

Khi nối Excel: chỉ chèn 8 dòng `mouthome.*` vào vùng Mẹ MOUT; không chép lại 135 dòng `master.*`.
