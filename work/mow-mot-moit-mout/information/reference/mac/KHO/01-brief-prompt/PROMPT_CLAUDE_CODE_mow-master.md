# YÊU CẦU CHO CLAUDE CODE — Gắn data-region cho MOW-master

**File cần sửa (VPS):** `/opt/incomex/docs/mcp-writes/ui-preview/mow-master-v1.html`
**UI:** MOW — Danh sách quy trình đã đúc (https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-master-v1.html)
**Vai:** Bạn là NGƯỜI-SỬA (gắn mã trên VPS). CW là NGƯỜI-KIỂM (verify độc lập 3-tập + điền Excel). Hai vai tách nhau.

---

## 1. NGUYÊN TẮC (bắt buộc)
- `data-region` = ĐỊA CHỈ/mỏ neo của một khu trên UI, thuộc tầng GIAO DIỆN. **Không gánh khái niệm nghiệp vụ.**
- **KHÔNG bump `?v=`** của bất kỳ file nào (master-list.js?v=3, eco-nav.js?v=3, mot-theme?v=17… giữ nguyên).
- **KHÔNG sửa Excel** (CW làm). **KHÔNG đổi hành vi/CSS/logic** — chỉ thêm thuộc tính `data-region`.
- Không chạy lệnh hạ tầng/deploy. Chỉ sửa đúng 1 file HTML nêu trên.

## 2. RANH GIỚI — QUAN TRỌNG NHẤT
Trang này nạp `./master-list.js?v=3` (khuôn danh sách **DÙNG CHUNG**) + `./eco-nav.js?v=3` (thanh dock).

- **`master-list.js` ĐÃ được gắn 135 mã `master.*` ở vòng MOT-master. TUYỆT ĐỐI KHÔNG mở, KHÔNG sửa, KHÔNG gắn lại file này.** Khi MOW-master render, nó sẽ tự sinh ra 135 khu `master.*` y nguyên (mượn) — đó là điều đúng, không phải việc của lệnh này.
- **`eco-nav.js` = dock hệ sinh thái, LOẠI TRỪ** (thuộc `shell.*`/dock). Không gắn.
- **Việc của lệnh này = CHỈ gắn phần vỏ RIÊNG của `mow-master-v1.html`** → prefix **`mowmaster.`** (8 mã), song song 1:1 với `motmaster.*` của trang MOT-master.

## 3. CHỐNG NHIỄM CHÉO PREFIX
Dùng khớp **ranh giới token** `mowmaster\.` — **không** dùng `startswith("mow")` (sẽ nuốt nhầm `mow.*` của canvas). Bài học cũ: `mot.` vs `motstudio.` từng lẫn. Sau khi gắn, kiểm: mọi mã mới đều bắt đầu đúng `mowmaster.`, và **không** có mã `mow.*` (không-master) nào bị thêm vào trang này.

## 4. 8 MÃ CẦN GẮN (song song `motmaster.*` — đặt tên & phân nhóm y hệt để 2 trang giống nhau)

| Mã | Gắn vào phần tử | Mô tả | nhom |
|---|---|---|---|
| `mowmaster.app` | `<body class="mot">` | Toàn bộ màn hình danh sách quy trình MOW đã đúc | GIAO DIỆN |
| `mowmaster.topbar` | `<div class="topbar">` | Thanh đầu trang riêng của MOW Master | GIAO DIỆN |
| `mowmaster.topbar.brand` | `<div class="logo">` (MOW · Danh sách) | Tên trang MOW Danh sách | GIAO DIỆN |
| `mowmaster.topbar.badge` | `<span class="vbadge">` (quy trình đã đúc) | Nhãn quy trình đã đúc | GIAO DIỆN |
| `mowmaster.topbar.open` | `<a>` "Mở MOW" (→ mow-unified-canvas) | Điều hướng tới bàn làm việc MOW | GIAO DIỆN |
| `mowmaster.topbar.hub` | `<a>` "Master tổng →" (→ master-hub) | Điều hướng tới Master tổng | GIAO DIỆN |
| `mowmaster.content` | `<div class="wrap">` | Nội dung chính của trang MOW Master | GIAO DIỆN |
| `mowmaster.list.host` | `<div id="master-root">` | Điểm gắn khuôn danh sách dùng chung vào trang MOW | GIAO DIỆN |

> Ghi chú: cả 8 đều GIAO DIỆN (đúng như `motmaster.*` — link điều hướng tĩnh tính là điều hướng/giao diện, không phải command). Nếu bạn thấy lý do đổi nhóm khác motmaster, DỪNG và ghi rõ trong handoff để CW xét, đừng tự đổi lệch với motmaster.

## 5. SẢN PHẨM GIAO CW (đặt cùng thư mục `/opt/incomex/docs/mcp-writes/ui-preview/`, đặt tên song song motmaster)
1. **`mowmaster-data-region-manifest.csv`** — cột y hệt motmaster: `ma,pham_vi,nhom,mo_ta,vi_tri_source,occurrence,trang_thai`.
   - **Chỉ liệt kê 8 mã `mowmaster.*` MỚI** (pham_vi = `RIENG_MOW_MASTER`, trang_thai = `BUILT`, vi_tri_source = `mow-master-v1.html:<dòng>`).
   - **KHÔNG liệt kê lại 135 `master.*`** vào manifest này (chúng đã đăng ký; sẽ được MOW-master mượn). Nếu muốn, ghi 1 dòng chú thích cuối file rằng "135 master.* mượn từ master-list.js, đã đăng ký ở vòng MOT-master, không thêm lại."
2. **`mowmaster-runtime-audit.json`** — audit DOM runtime qua mọi state của khuôn danh sách (list/search/lọc-trạng-thái/cây-7-tầng/rỗng/drawer/human-DOT). Báo cáo:
   - `runtime.master.count` = **135** (mượn, y nguyên) + `runtime.mowmaster.count` = **8**; tổng union = 143; prefix lạ = 0 (không `shell.*`).
   - `source.mowmaster.count` = 8 == `runtime.mowmaster.count` = 8 (thiếu 0 / thừa 0).
   - `boundary`: `sharedPrefix="master."`, `pagePrefix="mowmaster."`, `excluded=["eco-nav.js","shell.*"]`, `edited=["mow-master-v1.html"]` (CHỈ 1 file — master-list.js KHÔNG nằm trong `edited`).
3. **`mowmaster-data-region-handoff.md`** — tóm tắt: 8 mã đã gắn, ranh giới, xác nhận master-list.js KHÔNG đổi (kèm sha256 trước/sau để chứng minh y nguyên), snapshot/commit id, và xác nhận không bump `?v=`.

## 6. NGHIỆM THU (bạn tự kiểm trước khi giao — CW sẽ kiểm lại độc lập)
- [ ] 8 khu `mowmaster.*` xuất hiện đúng, 0 thừa 0 thiếu so với danh sách trên.
- [ ] `master-list.js` **sha256 KHÔNG đổi** so với trước (chứng minh không đụng file dùng chung).
- [ ] DOM render ra 135 `master.*` + 8 `mowmaster.*`; không có `mow.*` (không-master) lọt vào trang.
- [ ] **Không bump `?v=`** ở bất kỳ script/style nào.
- [ ] Kiểm chéo: master-hub.html, mot-master-v1.html, mout-home-v1.html, master-list-quy-trinh-v1.html vẫn render bình thường (vì cùng mượn master-list.js — mà bạn không đụng tới, nên phải y nguyên).

---

**Sau khi bạn giao 3 file trên, CW sẽ:** verify độc lập 3-tập (parse `mow-master-v1.html` → 8 `mowmaster.*`; đối chiếu DOM union; xác nhận master-list.js y nguyên) → rồi **chèn 8 mã `mowmaster.*` vào `SO_HOP_DONG` ở khối MOW (không chép lại 135 master.*)**.
