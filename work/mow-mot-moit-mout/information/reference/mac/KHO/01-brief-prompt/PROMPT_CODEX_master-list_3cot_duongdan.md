# YÊU CẦU CHO CODEX — Nâng khuôn CHUNG master-list.js: 3 cột T3/T2/T1 + đường dẫn đầy đủ (đuôi = tên form)

**File sửa (VPS):** `/opt/incomex/docs/mcp-writes/ui-preview/master-list.js` (khuôn DÙNG CHUNG — mọi master mượn).
**Ảnh hưởng:** áp ĐỒNG LOẠT cho mọi consumer: `mot-master`, `mow-master`, `mout-home`, `moit-master`, `master-hub`, `master-list-quy-trinh`. Sửa 1 lần, đẹp cả loạt.
**Vai:** đây là engine chung (không phải UI dựng mới), Codex là người-sửa + kiểm; CW cập nhật sổ sau.

## BỐI CẢNH MÔ HÌNH (Owner chốt)
- Cây 7 tầng: T7 Lĩnh vực > T6 Công ty > T5 Khối > T4 Phòng ban > T3 Chuyên môn > T2 Nhiệm vụ (quy trình) > T1 Công việc (task).
- MOIT (form nhập) / MOUT (báo cáo) là **thành phần** neo vào cây; đuôi địa chỉ = **TÊN CỤ THỂ của form/báo cáo** (KHÔNG phải chữ "moit"/"mout" chung chung — vô nghĩa).
- **Cả T1 và T2 đều có thể trống**; tầng nào khuyết thì hiển thị **`·`**.

## VIỆC CẦN LÀM
1. **Thêm 3 cột vào bảng danh sách** (thay/mở rộng cột "Chuyên môn" hiện tại):
   - `Chuyên môn (T3)` · `Nhiệm vụ (T2)` · `Công việc (T1)`.
   - Giá trị suy từ `anchor` của item resolve qua cây 7 tầng. Tầng khuyết → `·`.
2. **Đường dẫn đầy đủ** (ở dạng cây + trong drawer chi tiết) = 8 đoạn:
   `T7 / T6 / T5 / T4 / T3 / T2 / T1 / <tên form>`.
   - Tầng khuyết (T1 và/hoặc T2…) → `·`.
   - **Đoạn cuối = `item.name`** (tên form cụ thể), KHÔNG phải type.
3. **Áp cho mọi consumer** tự động (vì là khuôn chung). Mỗi trang chỉ cung cấp `name` + `anchor` (node neo — có thể là node T1/T2/T3…); master-list.js tự suy các tầng + chèn `·`.
4. **Không phá consumer cũ**: mot/mow master (task/quy trình) vẫn hiển thị đúng (task = có T1; quy trình = T1 khuyết `·`).

## RÀNG BUỘC
- Nội dung `master-list.js` ĐỔI → theo luật cache (PHẦN 7 quy_trinh): **bump `?v=4 → ?v=5` ĐỒNG LOẠT** trên MỌI trang nạp bằng URL cố định (mot-master, mot? … kiểm hết); trang dùng `?ts=`/no-cache thì miễn. `moit-master-v1.html` CW mới dựng đang để `?v=4` — nhớ bump theo.
- Việc này **thêm mã `master.*`** (3 cột mới + đoạn đường dẫn) → khuôn chung nở ra.

## GIAO LẠI CW
- `master-list-data-region-manifest.csv` (hoặc phần bổ sung): **danh sách mã `master.*` MỚI** thêm vào (3 cột T3/T2/T1 + đoạn path nếu có mã riêng), UTF-8, mô tả KHÔNG dùng "›". Kèm **số master.* trước → sau** (hiện 135 → ?).
- `master-list-runtime-audit.json`: xác nhận render đúng trên ≥2 consumer (1 có T1 = mot-master/task, 1 khuyết T1 = mout-home/moit-master); master.* source=DOM; `?v=` đã bump đồng loạt; sha các file khác không đổi.
- Handoff: tóm tắt thay đổi + snapshot.

CW sẽ: cập nhật sổ (thêm mã `master.*` mới ở vùng DÙNG CHUNG) + kiểm chéo mout-home/moit-master hiển thị đúng.

## LƯU Ý
- Đây là bước "sửa lại mọi master cho nhất quán" Owner yêu cầu (gồm cả mout-home đã làm nhưng cần sửa).
- Dữ liệu items (tên/anchor) từng trang có thể cần rà cho đúng tầng neo — nhưng phần LOGIC hiển thị nằm ở master-list.js này.
