# BRIEF GỬI GPT-WORK (Codex) — Bước nhỏ #1: thay Khu A drawer quy trình bằng BẢNG GỌN

> Tinh thần cũ: đọc mục tiêu, tư duy cùng, tự kiểm lại. Đây là **1 việc nhỏ** trong chuỗi nhiều bước — cố ý làm hẹp để chắc. Đừng ôm hết một lúc.

## 1. MỤC TIÊU (việc nhỏ này)
Trong drawer quy trình (MOW master), **Khu A "Công việc trong nhiệm vụ"** hiện đang là các CARD dài (mỗi việc 1 khối to: Trigger/Điều kiện/Hàng đợi/Tín hiệu/3 vai/Thực thi/Dự phòng) → **quá rậm, Admin xử chục ngàn quy trình sẽ rối**. Thay bằng **BẢNG GỌN 5 cột** để nhìn-một-phát-hiểu (kiểu Apple: đơn giản tối đa, tận dụng tư duy thường).

Chỉ đổi phần danh sách việc. **GIỮ NGUYÊN**: khung drawer, khối "▶ Bắt đầu quy trình", badge "N điểm cần bổ sung", 2 tổng (cộng dồn/chỉ định), Khu B (đường dẫn 7 tầng + PG).

## 2. BẢN THIẾT KẾ CHUẨN (làm theo)
File `mow-process-view-v1.html` (CW dựng, tự chạy được — mở xem/di chuột). Bảng gọn gồm cột: **# · Tên việc · Phút · Chạy khi**. Quy tắc:
- **Mã việc ẨN**, chỉ hiện khi di chuột vào dòng (như MOW cố ý — mã là id máy đọc).
- **Chạy khi** = chấm màu trigger + chữ:
  - Chấm **cùng màu** = chung trigger; **khác màu** = trigger riêng. Palette thứ tự: xanh #185FA5 → hổ phách #BA7517 → ngọc #1D9E75 → tím #7F77DD → cam #D85A30 → xám #888780. (>6 trigger: lặp màu + thêm ký tự nhỏ trong chấm.)
  - **Di chuột vào chấm → hiện mã + tên trigger** (đọc từ nguồn trigger; vòng này lấy tạm từ dữ liệu mẫu, sau nối bảng trigger SSOT thật).
  - Chữ **"ngay"** = đủ điều kiện chạy liền khi trigger đến; **"sau #n"** = đợi việc #n xong.
- Dòng **dự phòng** = 1 dòng ĐỎ (không làm, chỉ tính giờ).
- Trigger ra = 1 dòng mờ "◀ kết thúc quy trình" dưới bảng.

## 3. CHƯA LÀM VÒNG NÀY (để bước sau)
- **Cột "Bản ghi"** (khóa ngoại từng việc) — CHƯA đưa vào.
- **Click-through** (bấm việc → chi tiết MOT) — bước sau.
- Chi tiết verbose từng việc (điều kiện/hàng đợi/tín hiệu/3 vai) → sẽ nằm ở **LỚP TRONG** (chưa dựng). Vòng này chúng bị bỏ khỏi Khu A.

## 4. data-region — giao DELTA cho CW
- **Dùng lại**: `master.drawer.process`, `.start.*`, `.sequence`, `.task`, `.task.order`, `.task.name`, `.task.time.exec`, `.task.relation` (="chạy khi"), `.totals`, `.totals.assigned`, `.readiness.*`.
- **THÊM (BUILT)** — CW đã đặt sẵn NOT_BUILT, Codex render là thành BUILT: `.title`, `.sub`, `.totals.accumulated`, `.start.trigger.dot`, `.task.code`, `.task.trigger.dot`, `.exit`, `.exit.trigger`, `.exit.trigger.dot`.
- **TO_REMOVE (đẩy sang lớp trong, chưa dựng)**: các mã verbose từng việc không còn hiện ở Khu A gọn — `.task.trigger` (ô giá trị), `.task.condition`, `.task.queue`, `.task.signal`, `.task.dependency`, `.task.wiring`, `.task.roles`, `.task.role`, `.task.role.label`, `.task.role.value`, `.task.time.buffer`. (Sẽ re-add khi dựng lớp trong / click-through.)
- Codex tự rà lại danh mục bỏ/giữ/thêm cho khớp DOM thật rồi giao **delta manifest** (UTF-8, mô tả không "›") + audit + handoff. Bump `?v=` đồng loạt nếu đổi khuôn chung.

## 5. CÁCH LÀM CW mong
1. Đọc mục tiêu; thấy cách gọn/mượt hơn → nói, ta bàn.
2. **Chèn README ngắn trong code** phần Khu A (giải thích bảng gọn + quy tắc chấm màu/ẩn mã) — để CW/Owner đọc lại hiểu ngay (Owner dặn: ghi khi còn nóng).
3. **Tự kiểm cuối**: liếc Khu A mới — có gọn hơn hẳn card cũ không? 3 câu (bắt đầu gì · thứ tự việc · thiếu gì để chạy) còn trả lời được không? MOT/MOIT/MOUT/MOW-canvas không vỡ?
4. Giao: bản chạy VPS + delta manifest + audit + handoff + 1 đoạn tự đánh giá.

Xong bước này, CW đổi 9 mã NOT_BUILT → BUILT + đánh TO_REMOVE các mã verbose. Rồi mình sang bước nhỏ tiếp (bản ghi, hoặc click-through).
