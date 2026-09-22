# YÊU CẦU CHO CODEX — DEPLOY + KIỂM moit-master (quy trình MỚI: gắn-trước, đảo vai)

**Bối cảnh — đổi vai lần này:** CW đã THIẾT KẾ trang mới `moit-master-v1.html` với **data-region đặt sẵn** (gắn-trước, đây là UI dựng mới = LOẠI B). Nên vai đảo: **CW = người-sửa** (đã dựng + đặt mã + viết manifest), **Codex = người-KIỂM** (deploy lên VPS + chạy runtime-audit độc lập xác nhận). Giữ nguyên nguyên tắc người-sửa ≠ người-kiểm.

**File CW giao (ở thư mục làm việc của Owner):**
- `moit-master-v1.html` — trang mới, đã có data-region.
- `moit-master-data-region-manifest.csv` — 8 mã `moitmaster.*` CW đã đặt.

## VIỆC CỦA CODEX
1. **Deploy** `moit-master-v1.html` vào `/opt/incomex/docs/mcp-writes/ui-preview/moit-master-v1.html` (đúng chỗ các master khác). KHÔNG sửa nội dung file khi deploy (đặt nguyên xi). Nếu buộc phải chỉnh gì, ghi rõ.

2. **Kiểm ranh giới / bản chất trang (giống mot-master / mow-master):**
   - Trang **mượn khuôn dùng chung `master-list.js?v=4`** (KHÔNG bump, KHÔNG sửa master-list.js) → sẽ render các mã `master.*` (đã đăng ký ở DÙNG CHUNG, **không đăng ký lại**).
   - Phần **RIÊNG trang = 8 mã `moitmaster.*`** (song song `motmaster.*`/`mowmaster.*`).
   - `eco-nav.js` nạp bằng `?ts=` (luôn tươi, không dính cache) — loại trừ.

3. **Runtime-audit độc lập** (xác nhận thiết kế của CW đúng):
   - DOM render ra: **8 mã `moitmaster.*`** (khớp đúng manifest CW giao, thiếu 0 / thừa 0) + họ `master.*` mượn (số lượng theo dữ liệu trang — dự kiến ~97 khu cơ bản như MOW-master vì items không có `steps`, không `showMother`; xác nhận con số thật).
   - **0 mã lọt sang** `moit.form.*`, `moit.proposal.*`, `modit.*`, `mot.*`, `motmaster.*`, `mowmaster.*`.
   - `master-list.js` **sha256 KHÔNG đổi** (chứng minh không đụng khuôn chung).
   - Kiểm chéo các trang master khác (mot-master, mow-master, mout-home, master-hub, master-list-quy-trinh) **vẫn render bình thường** (vì cùng mượn master-list.js — mà bạn không đụng).

4. **Giao lại CW:**
   - `moit-master-runtime-audit.json` — `moitmaster` source=DOM=8, thiếu 0/thừa 0; số `master.*` thật render; boundary (`pagePrefix="moitmaster."`, `sharedPrefix="master."`, `excluded=["eco-nav.js","shell.*"]`, `edited=["moit-master-v1.html"]`, `notEdited=["master-list.js"]`). **Manifest/audit UTF-8, mô tả KHÔNG dùng "›". Audit < 50KB nếu được.**
   - `moit-master-data-region-handoff.md` — xác nhận 8 `moitmaster.*` đúng manifest, số `master.*` mượn, master-list.js sha trước=sau, snapshot/commit id.

## SAU KHI CODEX XÁC NHẬN
CW sẽ điền **8 mã `moitmaster.*`** vào `SO_HOP_DONG` (vùng Mẹ MOIT, `me=MOIT`, sau `modit.*`). **135 `master.*` KHÔNG chép lại** (đã ở DÙNG CHUNG). Nếu Codex thấy lệch (mã thiếu/thừa, hoặc trang không render), báo lại — CW sửa thiết kế.

## LƯU Ý
- Đây là **thử nghiệm quy trình mới** cho UI dựng mới. Nếu chạy trơn, các UI mới sau CW sẽ dựng-kèm-data-region, Codex chỉ deploy + kiểm — bỏ hẳn vòng "gắn-sau".
- Owner ghi chú: trang này "còn phải sửa nhiều" — nội dung items/nhãn sẽ chỉnh sau; nhưng khung + data-region đã chuẩn để đăng ký.
