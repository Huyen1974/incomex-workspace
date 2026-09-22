# YÊU CẦU CHO CODEX — Thiết kế lại DRAWER khuôn chung master-list.js theo "1 FORM · 1 KIỂU · DÙNG MỌI NƠI" (vòng 1)

**File sửa (VPS):** `/opt/incomex/docs/mcp-writes/ui-preview/master-list.js` (khuôn DÙNG CHUNG — áp cho mọi master: mow/mot/moit/mout).
**Tinh thần:** đây là vòng 1, mục tiêu **quy trình sửa-rẻ** (không cầu toàn) — cứ làm bản dùng được, refine sau đều rẻ nhờ data-region.
**Vai:** Codex sửa engine chung + audit; CW cập nhật sổ.

## NGUYÊN TẮC GỐC (Owner chốt)
- **1 form/báo cáo thiết kế MỘT LẦN (Studio) → xuất hiện Y HỆT mọi nơi**: độc lập (list MOIT/MOUT) · cắm vào MOT · trong drawer master-list. KHÔNG dựng lại, KHÔNG đổi vị trí/hình.
- **Mỗi loại chỉ 1 KIỂU duy nhất.** Cần dạng khác → thêm ở Studio, không đẻ biến thể tại chỗ.
- Lý do: đổi vị trí/hình thì máy vô cảm, NGƯỜI phải học lại từ đầu → ít concept = đào tạo rẻ, nhận ra sai/thiếu nhanh.

## DRAWER MỚI = 2 KHU CỐ ĐỊNH (1 khung cho cả 4 list, chỉ đổi nội dung)
**Khu A — bản xem THẬT (ưu tiên, chiếm phần lớn):** render đúng cái người dùng cuối nhìn thấy, **tái dùng renderer đã có** — KHÔNG vẽ layout drawer riêng. Nguồn = `form_schema`/mold mà chính builder đã xuất (MOIT-form, MOUT-builder, Studio đều đã có JSON mold). Hiển thị dạng **chỉ-xem** (read-only), nhìn y hệt UI thật.

**Khu B — hỗ trợ (lấp chỗ trống, DÙNG LẠI khối có sẵn):** đường dẫn 7 tầng (đã có `master.tree.item.path`/`master.drawer.hierarchy.*`) · trigger/hàng đợi/điều kiện · **3 vai người** (thực hiện · báo cáo · làm thay — dùng lại chip-người kiểu MODUT/MODW) · **bảng PG kết nối**.

### Nội dung theo Mẹ
| List | Tầng | Khu A (bản xem thật) | Khu B (hỗ trợ) |
|---|---|---|---|
| MOW | T2 quy trình | Tổng quan quy trình: các task T1 + luồng (tái dùng ma trận `master.process.*` sẵn có) | trigger-out · hàng đợi · trigger từng task · 3 vai người · đường dẫn |
| MOT | T1 task | **Form MOIT của task** (MOT KHÔNG có form riêng — dùng lại đúng form MOIT) | trigger bắt đầu (queue/bảng trigger) · điều kiện+hàng đợi giữa việc · thống kê 3 vai người · đường dẫn T7…/T2/tên task |
| MOIT | form nhập | Form nhập thật (render từ schema) | bảng PG kết nối · đường dẫn T7…/T1/tên form |
| MOUT | báo cáo | Báo cáo thật (vài info hoặc 1 bảng ma trận — theo thiết kế Studio) | bảng PG nguồn · đường dẫn T7…/T1/tên form |

## DATA-REGION — TÁI CẤU TRÚC master.drawer.*
- **BỎ/GỘP** phần "kitchen-sink" không theo nguyên tắc (vd lưới liên kết 4 Mẹ `master.drawer.links.*`, info chung rời rạc) — đánh dấu các mã đó **TO_REMOVE** trong manifest để CW ghi lịch sử.
- **GIỮ + TÁI DÙNG**: `master.drawer.hierarchy.*` (đường dẫn), `master.process.*` (ma trận quy trình → Khu A của MOW).
- **THÊM**: mã cho **Khu A** (điểm nhúng bản xem thật, vd `master.drawer.view` + con của nó nếu cần) và **Khu B** (các khối `master.drawer.support.*`: trigger · roles · pg_tables).
- Codex tự đề xuất danh mục **bỏ / giữ / thêm** (delta), miễn theo 2-khu. Owner + CW rà lại.

## RÀNG BUỘC
- Nội dung `master-list.js` đổi → **bump `?v=5 → ?v=6` ĐỒNG LOẠT** trên mọi consumer URL cố định; trang `?ts=` miễn.
- Renderer Khu A phải **tái dùng** (nhúng từ schema), KHÔNG viết lại UI form trong master-list.js. Nếu cần một module render-form-từ-schema dùng chung, đề xuất — đó chính là "1 renderer, mọi nơi".

## GIAO CW
- `master-list-drawer-manifest.csv`: **delta** — mã THÊM (BUILT) + mã TO_REMOVE, UTF-8, mô tả không "›". Kèm số `master.*` trước→sau.
- `master-list-drawer-audit.json`: render đúng Khu A + Khu B trên ≥1 consumer mỗi Mẹ (mow/mot/moit/mout); source=DOM; `?v=` bump đồng loạt.
- Handoff: tóm tắt bỏ/giữ/thêm + snapshot.

## LƯU Ý
- Vòng 1 chấp nhận Khu A dùng dữ liệu mẫu/schema hiện có (`MASTER_CONFIG.items`), chưa cần PG thật.
- Đây là thay đổi lớn của khuôn chung nhưng RẺ vì có sổ: đổi tới đâu, trọng tài lộ tới đó, CW cập nhật. Cứ làm bản chạy được trước.
