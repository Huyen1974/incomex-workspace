# BRIEF GỬI GPT-WORK (Codex) — Drawer QUY TRÌNH: "Admin nhìn một phát thấy đủ"

> Đây KHÔNG phải lệnh thi hành từng bước. Mong Codex **đọc mục tiêu trước, tư duy cùng, góp ý/phản biện, và tự kiểm lại kết quả so với mục tiêu**. Nếu có cách đạt mục tiêu tốt hơn đề xuất dưới đây → cứ nói, ta bàn.

## 1. MỤC TIÊU (thứ phải đạt — đọc kỹ)
Khi Admin bấm vào **một quy trình** trong danh sách MOW, phần chi tiết (drawer) phải để một người **hiểu logic công việc nhưng không giỏi kỹ thuật** (chính là Owner) **nhìn một phát là thấy**:
- Quy trình này **bắt đầu bằng gì?** (trigger khởi động)
- **Tiếp theo là gì → gì → gì?** (thứ tự vận hành các việc; việc nào nối tiếp, việc nào song song)
- **Còn thiếu gì để nó CHẠY được?** (đã đủ điều kiện chưa · đã gán người chưa · trigger đã có chưa · thời gian đã định chưa)

Tiêu chí đậu: đứng ở góc Admin, liếc drawer là trả lời được 3 câu trên mà không cần hỏi ai. Đơn giản, không lạ mắt.

## 2. BỐI CẢNH (để cùng hệ quy chiếu)
- Ta đang xây "hợp đồng thông tin **sửa rẻ**": mỗi khu UI có `data-region` (địa chỉ bền) + sổ Excel `SO_HOP_DONG` làm SSOT. Mục tiêu là **quy trình sửa rẻ, không cầu toàn** — cứ bản chạy được trước, tinh chỉnh sau đều rẻ.
- Hai luật gốc đang chi phối:
  - **"1 form · 1 kiểu · dùng mọi nơi"**: một thiết kế làm 1 lần, xuất hiện y hệt mọi nơi. **Không đẻ concept UI mới.** Con người mất nhiều công học 1 hình lạ.
  - **"1 SSOT · sửa 1 nơi → đồng bộ · PG-first"**: mỗi sự thật (người/vai, trigger, điều kiện, thời gian) sống ở đúng 1 bảng; nơi khác đọc qua khóa ngoại, không chép. Tận dụng tối đa PG (FK/view/function/trigger DB).

## 3. VẤN ĐỀ HIỆN TẠI (vì sao sửa)
Vòng trước Codex đã dựng drawer **2 khu** (Khu A = bản-xem-thật · Khu B = hỗ trợ) — hướng đúng, cảm ơn. Nhưng riêng **Khu A của MOW (quy trình)** đang là **một ma trận MỚI TOANH** → phạm luật "dùng lại UI đã có" và **thiếu rất nhiều thông tin** một quy trình cần.

## 4. NGUYÊN LIỆU ĐÃ CÓ SẴN (CW rà lại — dùng lại, đừng vẽ mới)
- **Thiết kế "MOW · Đề xuất nâng cao"** đã có bảng thời gian, đã gắn data-region: `mow.propose.advanced.timetable.*` = `exectime` · `task_alloc` (thời gian **chỉ định** nhiệm vụ) · `accumulate` · `buffer` · `addbuffer` · `total_exec` · `total_buffer` · `total_all`. **Đây là UI cần dùng lại cho Khu A**, không dựng ma trận khác.
- Khái niệm thời gian **đã chốt** trong sổ: `tg_thuc_thi` (phút 1 task) · `tg_cong_don` (→ T2) · `tg_phat_sinh` · `tg_chi_dinh` (chỉ định cả quy trình) · `han_hoan_thanh` · `tien_do` · `so_phut_qua_han`.
- Trigger/hàng đợi/điều kiện đã có khái niệm: `trigger` · `hang_doi` · `dieu_kien_chay`; object `execution_wiring` (trigger/hàng đợi/điều kiện/tín hiệu ra — chờ Kestra).
- Panel chi tiết T1 của canvas (`.tpanel` / `mow.normal.detail.*`) — có thể tái dùng cho phần chi tiết từng việc.

## 5. HƯỚNG ĐỀ XUẤT (để Codex phản biện, không phải chốt cứng)
Khu A drawer quy trình = trình bày theo **thứ tự vận hành**, dùng lại bảng thời gian nâng cao:
- Đầu: **trigger khởi động** quy trình + điều kiện để bắt đầu.
- Thân: danh sách việc theo thứ tự, mỗi việc kèm: trigger/điều kiện của nó · quan hệ nối tiếp/song song · số phút (thực thi) + chỉ định + buffer · người (thực hiện/báo cáo/làm thay) · hàng đợi.
- Cuối: **tổng** (total_exec · total_buffer · total_all) + phần "**còn thiếu để chạy**" (điều kiện chưa đủ / chưa gán người / chưa có trigger…).
Khu B giữ như đang có (đường dẫn 7 tầng · PG · …).

## 6. GAP ĐÃ LỘ (nhờ Codex xác nhận & bổ sung)
Rà xong thấy 3 thứ **chưa có trong hợp đồng**, CW đã ghi tạm vào `khung_object`/`dinh_nghia_khai_niem` (CHƯA CHỐT):
- `phu_thuoc_viec` — song song vs nối tiếp (`depends_on`) — hiện chỉ ngầm định theo thứ tự.
- `vai_lam_thay` — vai làm thay/chuyển tiếp (mới có thực hiện + báo cáo).
- `trigger_khoi_dong_qt` + `run_condition` — trigger + điều kiện **cấp quy trình**, thiết kế **1 SSOT** (sửa 1 nơi → cả hệ thống theo).
→ **Nhờ Codex**: engine `mvx-v3.js` (CW không đọc được — connector chặn binary) có sẵn logic nào cho song song/nối tiếp/hàng đợi/phút không? Nếu có, ta dùng lại; nếu chưa, xác nhận đây đúng là gap để thiết kế PG sau.

## 7. CÁCH LÀM CW mong (quan trọng hơn code)
1. **Đọc mục tiêu (mục 1) trước.** Thấy cách đạt tốt hơn → đề xuất, ta bàn. Đây là bàn cùng nhau.
2. **Tự kiểm lại cuối cùng**: đứng ở góc Admin, tự trả lời 3 câu ở mục 1. Chưa đạt → sửa tiếp, đừng giao vội.
3. Giữ luật: **dùng lại UI đã có** (bảng nâng cao), không đẻ concept mới; **SSOT** (đọc 1 nguồn, không chép); PG-first cho phần dữ liệu (vòng này vẫn có thể dùng schema/dữ liệu mẫu).
4. **data-region**: nếu Khu A chuyển sang dùng bảng nâng cao — region mượn từ `mow.propose.advanced.*` (mượn, như `mot.*` đang mượn) hay thêm `master.drawer.view.*` mới? Đề xuất phương án + giao **delta** (mã thêm/bỏ) cho CW cập nhật sổ. Bump `?v=` đồng loạt nếu đổi nội dung khuôn chung.
5. Sản phẩm giao: bản chạy trên VPS + delta manifest + audit + handoff — **kèm một đoạn TỰ ĐÁNH GIÁ** so với mục tiêu (đạt/chưa, còn thiếu gì).

Cảm ơn Codex. Ta không tìm "đúng ngay", ta tìm quy trình để **sửa rẻ** và một màn hình **nhìn là hiểu**.
