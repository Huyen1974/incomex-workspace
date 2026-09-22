# BRIEF GỬI GPT-WORK (Codex) — Click-through kiểu Wikipedia: mọi thứ nối vòng tròn, click là có thông tin

> Vẫn tinh thần cũ: đọc MỤC TIÊU trước, tư duy cùng, góp ý/phản biện, tự kiểm lại kết quả so với mục tiêu — không phải lệnh thi hành từng bước. Cảm ơn vòng drawer quy trình vừa rồi, rất tốt (đã tự lộ đúng phần còn thiếu).

## 1. MỤC TIÊU
Một quy trình (MOW) có nhiều **task**. Admin đang xem drawer quy trình, muốn hiểu sâu một task → **bấm vào task đó → hiện ngay CHI TIẾT của task (MOT)**. Từ chi tiết MOT, bấm tiếp vào form/người/báo cáo → lại ra thông tin của nó. **Kiểu Wikipedia: mọi thứ nối với nhau thành vòng, user chỉ cần click chuột là có thông tin, không phải đi tìm ở đâu khác.**

Tiêu chí đậu: đứng ở góc Admin — bấm 1 task trong quy trình → thấy đúng chi tiết task đó (chính là drawer MOT đã có) → bấm quay lại được → cảm giác "đi lại trong hệ thống bằng chuột" mượt, không lạc.

## 2. BỐI CẢNH
- Ta đang xây "hợp đồng thông tin sửa rẻ": data-region + sổ Excel SSOT; mục tiêu quy trình sửa-rẻ, không cầu toàn.
- Luật gốc đang chi phối:
  - **"1 form · 1 kiểu · dùng mọi nơi"** — không đẻ concept UI mới; dùng lại cái đã có.
  - **"1 SSOT · sửa 1 nơi → đồng bộ · PG-first"** — mỗi thực thể sống 1 bảng; nơi khác THAM CHIẾU qua khóa ngoại, không chép. Chính cơ chế "click-through" này là **hiện thân của khóa ngoại trên UI**: task trong quy trình = con trỏ (FK) tới MOT task; MOT task = FK tới form MOIT + báo cáo MOUT + người (bảng nhân sự). Click = đi theo FK.
- Đã có sẵn để dùng lại:
  - Drawer **MOT** 2-khu (Khu A = form MOIT của task · Khu B = trigger/3 vai/PG/đường dẫn) — chính là "chi tiết task" cần hiện khi bấm.
  - Drawer **quy trình** vừa làm liệt kê các task theo thứ tự (`master.drawer.process.task.*`).

## 3. HƯỚNG ĐỀ XUẤT (để Codex phản biện, không chốt cứng)
- Trong drawer quy trình, mỗi **task** (`master.drawer.process.task`) trở thành **bấm được** → mở **chi tiết MOT của đúng task đó** (dùng lại nguyên drawer MOT 2-khu, KHÔNG dựng màn mới).
- Cách mở: đề xuất phương án hợp lý nhất cho "cảm giác Wikipedia" — có thể là drawer chồng (stack, có nút ‹ quay lại), hoặc điều hướng sang MOT-master mở đúng task rồi quay lại. Codex chọn cách ít concept mới nhất, mượt nhất, và nói rõ lý do.
- Trong chi tiết MOT, tiếp tục cho bấm sâu hơn khi hợp lý (form → MOIT, báo cáo → MOUT, người → hồ sơ nhân sự) — nối vòng. Vòng này KHÔNG cần làm hết ngay; làm task→MOT trước, chừa móc cho các link sau.
- Điều kiện SSOT: task trong quy trình phải mang **tham chiếu tới MOT task (id/khóa)** để biết mở cái nào. Nếu source sống CHƯA có khóa này (giống các gap vòng trước) → **nói rõ "chưa có liên kết chuẩn"** thay vì đoán, và đây lại là một gap hợp đồng để CW ghi vào `khung_object`.

## 4. NHỜ CODEX SOI THÊM
- Source sống hiện có sẵn **khóa nối task↔MOT** chưa? (canvas/mvx-v3.js hay MASTER_CONFIG). Nếu chưa → xác nhận đây là gap `task_ref` cần thêm (SSOT/FK).
- Có rủi ro nào khi mở drawer-trong-drawer (state, cuộn, đóng) mà Codex thấy trước không? Đề xuất cách xử l.

## 5. CÁCH LÀM CW mong (quan trọng hơn code)
1. **Đọc mục tiêu (mục 1) trước.** Thấy cách "Wikipedia mượt hơn" đề xuất của CW → nói ra, ta bàn.
2. **Tự kiểm cuối**: bấm 1 task → có ra đúng chi tiết MOT của task đó không? Quay lại quy trình được không? Có bị lạc/kẹt state không? Chưa đạt thì sửa, đừng giao vội.
3. Giữ luật: **dùng lại drawer MOT đã có** (không màn mới); **SSOT** (mở theo khóa, không chép dữ liệu task sang chỗ khác); PG-first cho phần dữ liệu (vòng này schema/dữ liệu mẫu vẫn được).
4. **data-region**: phần "task bấm được" + cơ chế mở — mã mượn từ đâu / thêm mã gì (vd `master.drawer.process.task.open`?). Giao **delta** (thêm/bỏ) cho CW cập nhật sổ. Bump `?v=` đồng loạt nếu đổi khuôn chung.
5. Giao: bản chạy trên VPS + delta manifest + audit + handoff + **1 đoạn tự đánh giá** so với mục tiêu (bấm-được chưa? mượt chưa? còn link nào chừa lại?).

Ta không tìm "đúng ngay", ta tìm một hệ thống mà **click chuột là hiểu**, và mọi mảnh **nối với nhau qua khóa (SSOT)** đúng như dữ liệu thật sẽ chạy.
