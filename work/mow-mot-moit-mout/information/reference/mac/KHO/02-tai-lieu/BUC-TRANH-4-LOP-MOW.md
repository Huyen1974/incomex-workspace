# BỨC TRANH TỔNG THỂ — 4 LỚP + QUY TRÌNH VẬN HÀNH

> Xây HỆ THỐNG 4 lớp khép kín TRƯỚC, rồi mới xây cái "trích xuất" (đề xuất sửa chữa) vào nó.
> Cách làm đúng chiều: **hình dung quy trình → thiết kế UI theo quy trình → mới văng ra hợp đồng thông tin.**
> Quy trình chưa khép kín + khả thi ⇒ chưa có cách nào chạy được. Chốt với Owner 22/7/2026.

---

## 0. GỌI TÊN CHO KHỎI NHẦM
- **TẦNG** (T7 → T1) = cây tổ chức: Lĩnh vực · Công ty · Khối · Phòng ban · Chuyên môn · Nhiệm vụ · Công việc.
- **LỚP** (1 → 4) = độ sâu của MỘT đối tượng: khái niệm → danh sách → chi tiết → bảng D.

## 1. BỐN MẸ = BỐN DANH SÁCH SẢN PHẨM (đều ở LỚP 2)
1. **MOW** — danh sách **QUY TRÌNH** (WF, neo T2).
2. **MOT** — danh sách **CÔNG VIỆC** (task, T1, con của WF).
3. **MOIT** — danh sách **FORM nhập**.
4. **MOUT** — danh sách **BÁO CÁO**.
Dùng chung một khuôn list (luật nhân bản master list).

## 2. BỐN LỚP CỦA MỖI ĐỐI TƯỢNG (WF / task / form / báo cáo)
| Lớp | Tên | Là gì | MOW hiện có |
|---|---|---|---|
| **1** | Khái niệm | Sơ đồ khung, nhìn tổng thể trên MOW. Cực ngắn. | canvas MOW |
| **2** | Danh sách (master list) | Sản phẩm người dùng NHÌN & LÀM VIỆC. **DANH SÁCH CHỈ Ở LỚP NÀY.** | mow-master-nhap2 — *tạm xong* |
| **3** | Chi tiết | Quy trình chi tiết (bấm "mở chi tiết"). | đã làm |
| **4** | Bảng D (MODW / MODT) | Biến thành hiện thực: **config · khai báo · test · trạng thái · đã phê duyệt**. | modw-builder |

- Hết **Lớp 4 → quay lại Lớp 1** (vòng tròn). **Lớp 3, 4 "ăn theo" Lớp 2.**
- Mỗi WF/task/form đi cùng **đủ 4 lớp như MỘT KHỐI**.

## 3. ĐI LẠI — HAI CHIỀU
- **Dọc (lớp):** 1 ↔ 2 ↔ 3 ↔ 4 → 1.
- **Ngang (xuyên TẦNG + xuyên MẸ):** WF (MOW) ↔ task (MOT) ↔ form/báo cáo (MOIT/MOUT), lên xuống với **LỚP TƯƠNG ỨNG**. Ở Lớp 4, vì MODT đã gộp (mục 4), đi lại là **MODW ↔ MODT** — trong MODT có sẵn phần form + báo cáo.

## 4. MODT = MỘT BUILDER GỘP 3 D  (MODT ≡ MODIT ≡ MODUT)
Một **MOT** bản chất gồm **4 phần**:
1. **Header** — vai trò · tên · mã · nhận trigger. Cố định, chỉ khai báo → tách riêng.
2. **Phần công việc** = bản chất là **MOIT** (form nhập).
3. **Thông tin tham khảo** = bản chất là **MOUT** (báo cáo).
4. **Hướng dẫn** — quy định phần 2 phải làm gì. (Cố gắng thiết kế trực quan để **nhìn là hiểu, khỏi cần hướng dẫn**.)

- **Đúc 1 MOT ⇒ đồng thời đúc 1 mã MOIT + 1 mã MOUT, mặc định gắn mã MOT** → bắt được **khoá ngoại TỰ NHIÊN** giữa MOT · MOIT · MOUT.
- Cần **báo cáo độc lập** → một **nút "tách mã MOUT độc lập"** (không gắn MOT).
- Khi sửa (Lớp 4 = D): **3 D là 1** — MODT/MODIT/MODUT chung một builder, chỉ khác **một nút "thuộc quy trình / không thuộc"**.

### Dùng lại (M2M) + cơ chế sửa
- Nhiều MOT **dùng chung** 1 MOIT/MOUT (quan hệ **M2M**).
- 1 MOT sửa MOIT/MOUT ⇒ hệ hỏi **2 lựa chọn**:
  - **Áp dụng TẤT CẢ** → đổi cả loạt.
  - **Chỉ riêng MOT này** → lưu **BẢN SAO**, tên form mới; các MOT khác **KHÔNG đổi**.
- Điều kiện để quyết đúng: **đưa quan hệ RA NGOÀI để NHÌN** — admin thấy ngay **danh sách các MOT đang dùng chung** MOIT/MOUT này (khung nhìn PG, đếm được, không lưu).
- Vận hành thật: người ta ngại rắc rối, hay chọn bản riêng cho an toàn — nhưng riêng thì tốn config/đấu nối. **Quy trình tối ưu ban đầu phức tạp nhưng tiết kiệm lặp lại.**

## 5. QUY TRÌNH TẠO MOW (T2) — 7 BƯỚC
1. Vẽ **sơ đồ khái quát** (vài dòng) trên MOW (= đề xuất cải tiến): tên quy trình + các bước (task) **dự kiến**. Rà: đã lên **đủ bước dự kiến** chưa.
2. Rà từng task: cái nào **dùng task đang có**, cái nào **làm mới**. *(M2M — chọn là hệ **tự cập nhật quan hệ**: ai dùng tôi · tôi dùng ai · ai thuộc tôi · tôi thuộc ai. UI chính là nơi ĐỊNH NGHĨA quan hệ và ghi lại vào PG.)*
3. Đi **hoàn thiện các task mới**.
4. Rà soát + **config** data do quy trình quản lý (trigger · hàng đợi · …).
5. **Test thử** — chế độ test: thao tác trên **table THẬT** như bình thường, nhưng dữ liệu **gán nhãn test**, PG **tự xử lý** (trong ngày / sau 15 phút).
6. Bấm **"đã test OK"** (nút thêm trong MODW) → vào **danh sách chờ phê duyệt**.
7. **Người phê duyệt pháp lý** duyệt → quy trình **chạy ra hệ thống**, bắt đầu nhận tín hiệu, giao việc.
- **Bổ sung:** đề xuất cải tiến của T2/T1 thêm phần **"config"** để liệt kê/khai báo cái cố định — đơn giản nhất, khỏi quên.

## 6. QUY TRÌNH TẠO MOT (T1) — 6 BƯỚC
1. Xem **MOIT/MOUT đã có** trong danh sách chưa? Có → **import / dán mã** là tự lắp. *(MODT thêm phần **nhập form cũ**, không chỉ lắp form mới.)*
2. (Chỗ này chỉnh thêm MOT riêng tầng 1) — cải tiến phần **đề xuất nâng cao**.
3. Chưa có MOIT/MOUT → dùng **MOT studio** tạo **MOIT** (phần làm việc chính) + **MOUT** (thông tin tham khảo); cả hai **lấy từ config đọc thông nhau**.
4. Thiết kế bằng **MODT** để tạo Task.
5. **Test Task** (nút Test trên MODT).
6. Chuyển **phê duyệt pháp lý** → đưa ra sử dụng.

## 7. SSOT — MỘT NGUỒN SỰ THẬT (điều kiện KHẢ THI)
- **Không hardcode.** Mỗi giá trị sửa đúng **MỘT nơi**; mọi nơi khác **TỰ cập nhật** (trường tự chèn lên form · danh sách · chi tiết). Mọi trường là **khung nhìn** về cùng một nguồn.

## 8. BA LỖ HỔNG VẬN HÀNH CẦN CHỐT
1. **B1 tạo MOT (kiểm form cũ) chạy TRƯỚC auto-đúc** MOIT/MOUT — nếu dùng lại thì đừng đúc thừa mã.
2. **Chế độ test** cần PG hỗ trợ thật: nhãn test + tự dọn/xử lý sau 15 phút — một yêu cầu ở Lớp 4, không chỉ là nút.
3. **"Sửa riêng → bản sao"** phải sinh mã mới + giữ FK riêng; **"danh sách MOT dùng chung"** phải là **khung nhìn PG** (đếm được, không lưu).

## 9. CHƯA SANG MOT
MOW chưa khép kín (đủ 4 lớp + đi lại 2 chiều + SSOT + config + test + phê duyệt) thì **CHƯA sang MOT**.

---
*Đưa vào help cấu trúc của MOW (Codex đã giản lược, nay bổ sung lại).*
