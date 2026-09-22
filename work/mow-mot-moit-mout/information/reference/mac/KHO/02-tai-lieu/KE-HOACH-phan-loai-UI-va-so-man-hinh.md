# KẾ HOẠCH CHỐT — PHÂN LOẠI UI & HỢP ĐỒNG THÔNG TIN (v3)

> Tổng hợp Desktop + Fable/CW + Sol, sau vòng phản biện của Sol (nhận 7/8, phản biện 1).
> File: `hop-dong-thong-tin-sua-re.xlsx` · sheet `ui_cay_ma_khu_vuc`, `man_hinh`, `CONG_CU`.

---

## 0. VÌ SAO TRƯỚC GIỜ "CHƯA CLEAR"
Đang bắt **một cột làm nhiều việc**: `nhom` lẫn danh từ (người) + động từ (thêm); `loai` lẫn vai trò + hành động + đổi trạng thái. **Lối ra:** tách mỗi khu thành các câu hỏi ĐỘC LẬP, không loại trừ nhau.

---

## 1. MỖI KHU TRẢ LỜI 7 CÂU (mỗi câu = 1 cột, dùng TỪ ĐIỂN CHUẨN)

| Câu | Cột | Giá trị (dropdown) | Ghi chú |
|---|---|---|---|
| Ở đâu? | `man_hinh_so` | 01–10… | đã có — địa chỉ hiển thị |
| Tìm lại trong mã? | `ui_cay_ma_khu_vuc` (cột C) | `mow.shell.mode.normal`… | **= `data-region` nhúng trong DOM → grep ra khu. LÀ anchor.** |
| Là loại khu gì? | `ban_chat_khu` | THUC_THE · THONG_TIN · HANH_DONG · DIEU_HUONG · KHUNG_NHOM · KY_THUAT_TRANG_TRI | **chức năng CHÍNH** của khu |
| Nói về đối tượng nào? | `doi_tuong` | người · quy trình · công việc · thời gian · đề xuất · báo cáo · cảnh báo · dữ liệu · kho · trạng thái | danh từ |
| Đối tượng đóng vai gì? | `vai_tro` | phụ trách · thực hiện · nhận báo cáo · phê duyệt · làm thay… | trống nếu không có vai con |
| Có hành động gì? | `hanh_dong` | thêm · chọn · sửa · xoá · gửi · duyệt · từ chối · chuyển · sắp xếp | **trống** nếu chỉ hiển thị |
| Có vào hợp đồng không? | `pham_vi_hop_dong` | **IN · OUT · REVIEW** | (đã bỏ NOT_BUILT — xem §2) |

Các chiều **độc lập** → khu "vừa chứa vừa thao tác" xử gọn: combobox *Người phụ trách* = `THONG_TIN` + `doi_tuong=người` + `vai_tro=phụ trách` + `hanh_dong=chọn`.
`ban_chat_khu` là **chức năng chính**; các chiều khác ghi riêng, không nhồi vào nó.

Giữ thêm: `khai_niem_chung` · `mo_ta_thuc_te` (câu ngắn để lọc) · `ban_chat` (nghĩa đầy đủ, đấu PG) · `note`.

---

## 2. HAI TRỤC KHÁC NHAU — KHÔNG TRỘN (sửa theo Sol, điểm 1)

**Trục A — có thuộc hợp đồng không?** `pham_vi_hop_dong`:
- `IN` — phải vào hợp đồng · `OUT` — giữ trong bản đồ, không vào hợp đồng · `REVIEW` — Owner quyết.

**Trục B — đã dựng trên UI chưa?** `trang_thai` (chuẩn hoá):
- `BUILT` · `NOT_BUILT` (đáng lẽ cần, UI chưa dựng) · `TO_REMOVE` (thiết kế lỗi, cần xoá) · `DEPRECATED` (bỏ) · `REVIEW` (chờ Owner) · **`NUT_CAY`** (gốc cây / không gắn mã — LUẬT 5).

> `NUT_CAY` là chỗ Sol thiếu: 9 nút cây + 1 không-gắn không xếp được vào 5 giá trị kia.

Ví dụ: chấm trạng thái đáng lẽ có → `pham_vi=IN` + `trang_thai=NOT_BUILT`. Icon trang trí thừa → `pham_vi=OUT` + `trang_thai=TO_REMOVE`.

**Đủ hợp đồng khi:** không còn `pham_vi=REVIEW`; mọi `IN` có `khai_niem_chung`; mọi `IN + NOT_BUILT` đã có quyết định xây/hoãn/bỏ; mọi `TO_REMOVE` đã xử lý.

---

## 3. VÍ DỤ

| Khu | `ban_chat_khu` | `doi_tuong` | `vai_tro` | `hanh_dong` | `pham_vi` | `trang_thai` |
|---|---|---|---|---|---|---|
| Ô "Assignee: Ng.A" | THONG_TIN | người | phụ trách | — | IN | BUILT |
| Nút "+ Thêm người thực hiện" | HANH_DONG | người | thực hiện | thêm | IN | BUILT |
| Dropdown chọn người phụ trách | THONG_TIN | người | phụ trách | chọn | IN | BUILT |
| Nút Gửi đề xuất | HANH_DONG | đề xuất | — | gửi | IN | BUILT |
| Nút "Huỷ sửa" (local) | HANH_DONG | — | — | huỷ | **OUT** | BUILT |
| Chấm trạng thái (chưa dựng) | THONG_TIN | trạng thái | — | — | IN | **NOT_BUILT** |
| Nhóm "Thông tin" (drawer) | KHUNG_NHOM | — | — | — | OUT | BUILT |
| Tab T2 | DIEU_HUONG | quy trình | tầng T2 | — | OUT | BUILT |
| Gốc cây MOW | — | — | — | — | OUT | **NUT_CAY** |

---

## 4. BA TẦNG WORKBOOK
```
man_hinh          → Hệ có những màn/state nào?
ui_cay_ma_khu_vuc → Mỗi màn có khu nào? (CHỨA TẤT CẢ: nav, khung, kỹ thuật, khu OUT)
sổ hợp đồng        → CHỈ dòng pham_vi=IN → usage → concept gốc
```

## 5. MA TRẬN động-từ × danh-từ = CÔNG CỤ
Chạy trên khu `IN` để soi khoảng trống → ô trống chỉ là **`GAP_CANDIDATE`**, KHÔNG tự kết luận thiếu (nghiệp vụ có thể cố ý cấm). Owner quyết → thiếu thật thì tạo dòng `NOT_BUILT`.

## 6. QUY TẮC ĐIỀN (mặc định = GỢI Ý, không phải kết luận — sửa theo Sol, điểm 4 & 8)
1. `ban_chat_khu`: suy từ tiền tố `tac_dong_du_lieu` (điều_hướng→DIEU_HUONG, trường→THONG_TIN, hành_động_ghi→HANH_DONG, thực_thể→THUC_THE; tách KHUNG_NHOM khi đuôi "nhóm…", KY_THUAT_TRANG_TRI cho badge/chấm/footer trang trí).
2. `pham_vi` **gợi ý** theo `ban_chat_khu`, CW soi lại từng dòng, KHÔNG chốt máy:
   - THONG_TIN / THUC_THE → thường IN
   - HANH_DONG **đổi dữ liệu nghiệp vụ** → IN; HANH_DONG **local** (huỷ/đóng/kéo/mở-đóng nhóm) → OUT
   - DIEU_HUONG / KY_THUAT_TRANG_TRI → thường OUT (có ngoại lệ) · KHUNG_NHOM → OUT
3. `doi_tuong` suy từ đuôi `tac_dong_du_lieu` + `khai_niem_chung`.
4. `vai_tro` / `hanh_dong`: điền khi có; trống là hợp lệ.
5. **Phân loại thật cả 155 dòng.** IN ra bao nhiêu báo bấy nhiêu — KHÔNG lấy "~92" làm đích/điều kiện dừng.
6. Gom mọi ca ranh-giới-mờ + mọi `REVIEW_NEW_VALUE` thành **một phiếu trình** → Owner duyệt một lượt.

## 7. TỪ ĐIỂN CHUẨN — không gõ tự do (Sol, điểm 7)
Các cột `ban_chat_khu` · `doi_tuong` · `vai_tro` · `hanh_dong` · `pham_vi_hop_dong` · `trang_thai` dùng **dropdown (data-validation) nguồn từ sheet `CONG_CU`**. Giá trị mới: CW ghi `REVIEW_NEW_VALUE` → gom phiếu → Owner duyệt → mới thêm vào từ điển. (Không khoá cứng từ điển, nhưng không cho nhập tự do.)

## 8. DI TRÚ AN TOÀN — không đổi tên thẳng, giữ legacy (Sol, điểm 3)
```
1. Đổi tên cột cũ thành dữ liệu thô, GIỮ LẠI:
   nhom → nhom_legacy · loai → loai_legacy · tac_dong_du_lieu → tac_dong_du_lieu_raw
   (tac_dong_du_lieu_raw là NGUỒN để suy ban_chat_khu + doi_tuong, và để kiểm chéo — KHÔNG xoá)
2. Thêm cột mới: ban_chat_khu · doi_tuong · vai_tro · hanh_dong · pham_vi_hop_dong
3. Giữ: ui_cay_theo_ten_hien_thi · ui_cay_ma_khu_vuc(=anchor) · man_hinh_so ·
        mo_ta_thuc_te · ban_chat · khai_niem_chung · trang_thai · note
4. CW migrate từng giá trị cũ → cột mới (không đổi tên máy móc).
5. pham_vi_hop_dong = IN / OUT / REVIEW.  trang_thai = BUILT / NOT_BUILT / TO_REMOVE / DEPRECATED / REVIEW / NUT_CAY.
6. CHƯA nghỉ hưu cột legacy trong lượt đầu. Chỉ retire sau khi: 155 dòng migrate xong · tiền kiểm PASS · không mất nội dung · Owner đã xem ca mờ.
```

## 9. SỬA RẺ — anchor CHÍNH LÀ cột C (phản biện Sol, điểm 2)
Không thêm cột `location_anchor`. Trong hệ này **`ui_cay_ma_khu_vuc` = `data-region` nhúng trong DOM = anchor**: `grep data-region` ↔ cột C là cơ chế trọng tài đã chạy. `data-region` ổn định hơn file:line (không bao giờ đổi). Thêm cột anchor riêng = trùng cột C.
- Khu `NOT_BUILT`: cột C là *dự kiến*, vị trí dự kiến ghi ở `note`.
Khi UI đổi, so tập cột C cũ/mới: giữ → giữ phân loại+concept · mới → phân loại 1 dòng · mất → usage thành không-hiện-hành · nghĩa đổi → Owner duyệt · khu OUT → chỉ ghi cây. Mọi khu (kể cả OUT) đều trong cây → máy biết anchor lạ là hợp-đồng/điều-hướng/trang-trí.

---

## 10. CÒN QUYẾT ĐỊNH CHO OWNER
1. Duyệt bộ `trang_thai` 6 giá trị (có `NUT_CAY` mới thêm) — ok chưa?
2. Có đồng ý **KHÔNG thêm `location_anchor`** (dùng cột C làm anchor) như em phản biện không?
3. Khu OUT có ý nghĩa tra cứu (vd Tab T-tầng) → có điền `doi_tuong` không? (Sol: nên; em: đồng ý, tuỳ khu.)

Gật 3 câu là CW: (a) tạo cột + dropdown từ `CONG_CU`, (b) migrate 155 dòng theo §6, (c) gom ca mờ thành 1 phiếu, (d) dừng chờ duyệt.
