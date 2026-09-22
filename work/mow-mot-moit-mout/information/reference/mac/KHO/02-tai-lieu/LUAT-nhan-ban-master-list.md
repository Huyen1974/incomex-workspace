# LUẬT NHÂN BẢN MASTER LIST

> Mục tiêu: nhìn vào **bất kỳ** list nào cũng có **cảm giác giống nhau, quen thuộc** → giảm chi phí đào tạo. Làm list mới = **ĐÚC từ khuôn**, chỉ khai **2 thứ mới**; 8 thứ còn lại tự có. >50% list xử lý nhanh.
>
> Trạng thái: đã chốt với Owner 22/7/2026.

---

## GIAO THỨC BẮT BUỘC (đọc trước khi làm)

Trước khi làm hoặc nhân bản **bất kỳ** list nào, đọc:
1. `master-list.js` (khuôn gốc — CSS `.ml-*` + render + drawer).
2. File luật này.

Chỉ sau đó mới khai **2 thứ mới**. Không dựng trang mới, không chép CSS rời, không đẻ khái niệm mới.

---

## A. BÊN NGOÀI (màn danh sách) — 8 THỨ ĐÚC SẴN, GIỮ NGUYÊN

Giữ nguyên **cấu trúc + format + vị trí**, chỉ **đổi TÊN/nhãn** cho hợp list.

1. **Hàng công cụ:** ＋ Tạo mới · ô tìm (⌕) · lọc trạng thái · chuyển **Bảng / Theo cây 7 tầng** · Help. (đổi nhãn, giữ format)
2. **Khung lọc 7 TẦNG** (Lĩnh vực · Công ty · Khối · Phòng ban · Chuyên môn · Nhiệm vụ · Công việc), cascade. **TUYỆT ĐỐI không thay bằng "tầng" kiểu khác** (vd MOW/MOT/MOIT/MOUT) — đó là đẻ khái niệm mới.
3. **Khung bảng** `.ml-scroll` bo góc 12px + **header IN HOA DÍNH (sticky)** + hàng **hover** + con trỏ tay. Bảng dài thì cuộn TRONG khung (trang không tràn → thanh 4 Mẹ cân).
4. **Dấu ? / tooltip trên đầu MỖI cột** — GIỮ, nhưng **đổi nội dung ? đúng nghĩa cột mới**.
5. **3 cột đầu GIỮ NGUYÊN:** Sửa (✎) · # · Mã. **Cột cuối GIỮ NGUYÊN:** mở chi tiết ›. → **bốn cột này theo format MỜ.**
6. **Khoảng cách hàng chuẩn — KHÔNG tự đổi:** ô `padding:9px 12px`, viền hàng `1px rgba(0,0,0,.07)`, cỡ chữ bảng `12.5px`, header `10px` in hoa `letter-spacing:.4px`. Mọi list cùng nhịp.
7. **Nút ✎ = mở chi tiết / sửa khuôn; bấm hàng hoặc "mở chi tiết ›" = mở DRAWER trượt phải** (không link rời 404).
8. **Trạng thái:** cùng format — badge chấm màu (nếu là trạng thái vòng đời) **hoặc** ô chọn (nếu người nhập). Không tự chế kiểu khác.

### Nguyên tắc thị giác quan trọng nhất: MỜ / RÕ
- **Phần lớn cột để MỜ** (xám nhạt, cỡ nhỏ, phụ trợ).
- **Chỉ 2–4 cột quan trọng để RÕ** (đậm, đen `#1d1d1f`) — giữ mắt tập trung vào nội dung chính.
- Sửa · # · Mã · mở chi tiết **luôn MỜ**.

---

## B. BÊN TRONG (drawer chi tiết) — GIỮ NGUYÊN FORMAT 2 CỘT

- **Cột phải:** tài liệu · quy định · hướng dẫn · hỗ trợ vận hành.
- **Cột trái:** nội dung chi tiết — **BẮT BUỘC thiết kế theo CHUYÊN MÔN** của list đó.
- Trên cùng: đường dẫn **7 tầng** + tên bản.

---

## C. MỖI LẦN CHỈ BÀN 2 THỨ MỚI

1. **Cột nghiệp vụ** ở giữa: cột nào, cột nào RÕ / cột nào MỜ.
2. **Nội dung chi tiết trong drawer** (thiết kế theo chuyên môn) + **nghĩa của "Trạng thái"** cho list này.

Mọi thứ khác (mục A + format B) = **đúc sẵn, không bàn lại.**

---

## D. CÁCH ĐÚC (kỹ thuật — để không thể lệch)

Dùng chung **một khuôn** `master-list.js`. List mới = một `MASTER_CONFIG` (khai cột + data) + renderer drawer theo chuyên môn. **Không viết trang mới.**

Hiện `master-list.js` **đóng cứng cột** cho danh sách quy trình → chưa nhúng được list khác. Việc cần làm để luật này chạy thật: **mở rộng `master-list.js` nhận cột tùy khai + đánh dấu cột MỜ/RÕ trong config.** Khi đó mọi list — kể cả góp ý — đúc từ đúng một khuôn, 8 thứ mục A tự có, không cách nào lệch.

---

## E. VÍ DỤ SAI ĐỂ TRÁNH (rút từ thực tế)

- Dựng lại bảng bằng CSS rời thay vì dùng `.ml-*` của khuôn → nhìn khác, phải nhắc lại từng chi tiết.
- Đẻ bộ lọc "MOW/MOT/MOIT/MOUT" thay vì **lọc 7 tầng** — góp ý đến từ **mọi tầng**, phải neo vào cây 7 tầng.
- Bỏ dấu ? trên đầu cột, hoặc đổi khoảng cách hàng → mất cảm giác quen thuộc.
