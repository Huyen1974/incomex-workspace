# PROMPT — MMIM.FIELD02 · FIELD UI-first

RUN_ID: MMIM-FIELD02-20260923-01

## 0. Gate
Lượt này chỉ làm **FIELD**, chỉ làm **UI**, chưa làm config.

- Executor_Surface: **Claude Code CLI**.
- Write_Path: **fs_*** đã audit. Bắt đầu bằng `fs_read`/`fs_stat`; ghi bằng tool cùng family `fs_*`. Không Git CLI/native/API để ghi.
- Đọc: `AGENTS.md` → `README.md` §0/D12 → `work/mow-mot-moit-mout/COLLAB.md` → prompt này.
- READY phải là commit cuối chạm `PROMPT.md`, kiểm bằng `fs_log`.
- HTML baseline: `work/mow-mot-moit-mout/mow-mot-moit-mout.html` SHA-256 `d66e2f5475f9bf6c7bea32ee832dc73a3f97c2e8114bc47e47a5b93c3573fe73`. Lệch target block → DỪNG, không ghi đè.

## 1. Mục tiêu
Bỏ cách FIELD01 dài/mơ hồ. Làm một bản FIELD nhìn là kiểm được:

- Tab **Step quy trình**: giữ nguyên bảng 7 cột Owner đã thiết kế, chỉ còn **3 bước ngắn**.
- Tab **Quy trình**: có đúng **3 mảnh UI thật** tương ứng 1–1 với 3 bước, xếp dọc từ trên xuống.
- Trong từng mảnh UI, bôi **vàng** đúng trường/nút phải thao tác ở bước đó; phần khác để xám.
- Từ phần bôi vàng lập **một bảng danh sách 7 mục** và đếm ra cột “Tổng số trường cần khai”.
- **Cột config để trống.**
- Không đụng MOUT/MOIT/MOT/MOW, deep-link, HVU, VPS runtime hoặc connector.

## 2. Ba bước FIELD — chốt theo UI thật
### FIELD.S01 · Tìm / quyết định dùng lại hay tạo mới
Nguồn: UI-022 · Master Field.
- Mảnh UI: cắt đúng vùng tìm/tạo của UI-022.
- Bôi vàng:
  1. `Tìm mã / tên…`
  2. `＋ Khai báo trường`
- Logic ngắn: tìm trước; có Field phù hợp thì dùng lại; chưa có thì bấm `＋ Khai báo trường` sang S02.
- “Tổng số trường cần khai” = **2**.

### FIELD.S02 · Khai Field mới
Nguồn: UI-018 · hộp “Đề xuất thêm trường”.
- Mảnh UI: cắt phần form khai Field.
- Bôi vàng đúng 4 field:
  1. `Tên trường *`
  2. `Định dạng *`
  3. `Mô tả`
  4. `Nhóm quản lý *`
- Không tách các option của Định dạng/Nhóm quản lý thành field riêng.
- “Tổng số trường cần khai” = **4**.

### FIELD.S03 · Lưu đề xuất
Nguồn: UI-018 · footer hộp khai Field.
- Mảnh UI: cắt vùng nút cuối form.
- Bôi vàng:
  1. `Lưu đề xuất`
- `Đóng` để xám, không tính.
- “Tổng số trường cần khai” = **1**.

Tổng FIELD02 cần đối chiếu: **7 mục = 2 + 4 + 1**.

## 3. Giữ đúng thiết kế Owner
Trong `#list-quy-trinh-field`:
- **giữ nguyên 7 cột**, thứ tự cột, table ID, tên tab và vị trí bảng;
- body FIELD đổi từ 8 dòng FIELD01 xuống đúng 3 dòng `FIELD.S01..S03`;
- nội dung mỗi dòng rất ngắn, không nhét lý thuyết;
- cột “Tổng số trường cần khai” lần lượt **2 · 4 · 1**;
- cột “Tổng số trường cần config” để **trống cả 3 dòng**;
- cột trạng thái UI giữ theo thiết kế hiện có; không tự gán UI_OK.

MOUT/MOIT/MOT/MOW giữ nguyên hoàn toàn.

## 4. Bên Quy trình = 3 mảnh UI thật
Trong **tab Quy trình**, tạo một khu FIELD ngắn, xếp dọc:
- `step-detail-field-s01`
- `step-detail-field-s02`
- `step-detail-field-s03`

Mỗi mảnh chỉ có 4 phần:
1. **Ô UI** — bản HTML tĩnh nhìn giống đúng vùng UI nguồn.
2. **Trường bôi vàng** — tên + số đếm.
3. **Kết quả** — một câu ngắn.
4. **Nguồn** — UI-022 hoặc UI-018 + URL.

### Cách lấy UI
- Phải đọc **source/runtime thật** đang phục vụ UI-022/UI-018 trên VPS hoặc DOM render thật; **cấm tự vẽ lại từ mô tả**.
- Chép đoạn HTML nhỏ nhất đủ nhìn; bỏ JS, handler, submit thật, dữ liệu động không cần thiết.
- Không dùng ảnh/base64.
- Nếu cần CSS, chỉ thêm CSS tối thiểu và namespace riêng cho FIELD02.
- Giữ thứ tự/nhãn/control như UI thật.
- Vùng phải thao tác = nền vàng nhạt + viền vàng; phần còn lại = xám/nhạt.
- Không biến mảnh UI thành form hoạt động; đây là **minh họa tĩnh để kiểm**.

Nếu không xác định được source/DOM thật của UI-022 hoặc UI-018 → DỪNG, không dựng giả.

## 5. Bảng danh sách trường FIELD
Ngay dưới 3 mảnh UI, tạo một bảng duy nhất:
`STT · Mã trường · Tên hiển thị · Loại · Bắt buộc · Thuộc bước · UI nguồn`

Đúng 7 dòng dự kiến:
1. `FIELD02.01` · `Tìm mã / tên…` · điền · không · S01 · UI-022
2. `FIELD02.02` · `＋ Khai báo trường` · bấm · không · S01 · UI-022
3. `FIELD02.03` · `Tên trường *` · điền · có · S02 · UI-018
4. `FIELD02.04` · `Định dạng *` · chọn · có · S02 · UI-018
5. `FIELD02.05` · `Mô tả` · điền · không · S02 · UI-018
6. `FIELD02.06` · `Nhóm quản lý *` · chọn · có · S02 · UI-018
7. `FIELD02.07` · `Lưu đề xuất` · bấm · không · S03 · UI-018

Phải đối chiếu lại nhãn với UI thật trước khi ghi. Nếu nhãn thật khác → dùng nhãn thật và ghi mismatch vào COLLAB; không tự sửa UI nguồn.

## 6. Bỏ rác FIELD01
- Bỏ 8 bảng chi tiết 14 mục của FIELD01.
- Bỏ FIELD.S04–S08 khỏi bảng Step FIELD.
- Không xóa lịch sử trong Git/COLLAB; chỉ sản phẩm hiện hành phải gọn.
- Không thêm lớp lý thuyết mới.

## 7. Kỹ thuật sửa
- File ~1,87 MB: không rewrite toàn file, không prettify/reformat.
- Neo theo ID duy nhất; không replace chuỗi generic.
- Mutation HTML + COLLAB trong **một fs_transaction**.
- Không đổi ID/tab/table ngoài FIELD được nêu.

## 8. Acceptance
1. FIELD Step = **3 dòng**, mã `FIELD.S01..S03`.
2. Bảng Step vẫn đúng **7 cột** và cùng ID.
3. Tổng trường khai = **2 / 4 / 1**; config trống.
4. Tab Quy trình có đúng **3 mảnh UI**, ID `step-detail-field-s01..s03`.
5. Mỗi mảnh lấy từ UI thật; không ảnh, không JS chạy.
6. Số control bôi vàng = **2 / 4 / 1**.
7. Bảng danh sách FIELD = **7 dòng** và tổng theo bước khớp 2/4/1.
8. Không còn 8 bảng chi tiết FIELD01 hiện hành.
9. MOUT/MOIT/MOT/MOW không đổi.
10. Không sửa VPS runtime/HVU/deep-link/config.
11. Mở bản mirror nếu đã đồng bộ và kiểm nhìn được; nếu chưa thì `VIEW_PENDING_REVISION`.
12. Diff chỉ trong phạm vi FIELD02.
13. Ghi trong COLLAB cùng transaction:
   `KQ@MMIM-FIELD02-20260923-01 XONG` hoặc `DỪNG`.

## 9. Báo cáo
Báo ngắn:
`XONG · MMIM.FIELD02 · steps=3 · ui_tiles=3 · field_list=7 · counts=2/4/1 · config=blank · main_html_sha=<new> · Owner review`

Hoặc:
`DỪNG · MMIM.FIELD02 · <lý do>`
