# ĐỌC TRƯỚC — thư mục "quy trình"

_Cập nhật 02/09/2026._

## 1. KHÔNG CÓ FILE NÀO BỊ XOÁ

Trước dọn: **406 file / 42 MB**. Sau dọn: **408 file / 42 MB**
(2 file thêm vào là file này + nhật ký dọn dẹp).

Toàn bộ thao tác chỉ là **di chuyển (mv)**, có nhật ký đầy đủ 91 dòng ghi rõ
file nào đi đâu tại `KHO/00-NHAT-KY-DON-DEP.txt`.

## 2. Tài liệu thiết kế DUY NHẤT nằm ở đâu?

> https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/thiet-ke-he-thong.html

File gốc trên VPS: `/opt/incomex/docs/mcp-writes/thiet-ke-he-thong.html`

Đặt trên VPS để chỉ có **một bản** — cùng chỗ với 30 UI đang thiết kế, cả người
và agent đều đọc/sửa được. Hai bản là hai bản lệch nhau sau hai tuần.

**LUẬT:** mọi thay đổi thiết kế **sửa trực tiếp vào file đó**. Không tạo file mới,
không tạo bản v2 rời, không tạo bản tóm tắt. Mỗi lần sửa thêm một dòng vào mục
"Nhật ký tài liệu" ở cuối trang.

Tài liệu gồm 11 mục: mục tiêu (đề bài gốc) → từ điển → mô hình lõi → bản đồ màn
hình → **cấu trúc bảng + chức năng từng bảng** → luật → hợp đồng UI↔dữ liệu →
hiện trạng → việc tiếp theo → kiểm kê kho → nhật ký.

## 3. Kho tài liệu — cái gì ở đâu

| Thư mục | File | Có gì |
|---|---:|---|
| `KHO/01-brief-prompt/`     | 24  | Brief/prompt gửi agent, bàn giao, handoff, AGENTS.md. **Nhiều quyết định nghiệp vụ nằm ở đây.** |
| `KHO/02-tai-lieu/`         | 6   | 6 tài liệu nền: bức tranh 4 lớp MOW, báo cáo kiểm toán, luật nhân bản danh sách, kế hoạch phân loại UI, đề xuất củng cố nền |
| `KHO/03-excel/`            | 22  | **SỔ SSOT** `hop-dong-thong-tin-sua-re.xlsx` (18/07) + 20 backup |
| `KHO/04-ui-mau/`           | 2   | HTML mẫu để ở gốc |
| `KHO/05-anh/`              | 3   | Ảnh review MOW |
| `KHO/06-du-lieu/`          | 5   | JSON/CSV: sổ khái niệm UI quét từ canvas, manifest mã khu |
| `KHO/07-script/`           | 2   | Trọng tài 3 tập (công cụ kiểm quan trọng nhất) |
| `KHO/08-thu-muc-lam-viec/` | 345 | 16 thư mục làm việc: `.codex-*`, `_work_*`, kho backup Excel, 12 ảnh màn hình, **3 file Word gốc trong `z Tài liệu/`** |

## 4. BỐN TÀI LIỆU QUAN TRỌNG NHẤT — đọc lại khi cần quyết định

1. `KHO/08-thu-muc-lam-viec/z Tài liệu /đề bài quản lý quy trình.docx` (22/06)
   → **ĐỀ BÀI GỐC.** "PG có nguyên liệu, nhưng chưa có trí nhớ quy trình."
     4 cái mù · 5 câu hỏi · 16 loại nguyên liệu · 9 loại quy trình.
2. `KHO/08-thu-muc-lam-viec/z Tài liệu /Mẫu viết quy trình .docx` (07/07)
   → **7 trường bắt buộc** của một bước + "quy trình xây dựng quy trình" 5 bước.
3. `KHO/03-excel/hop-dong-thong-tin-sua-re.xlsx` (18/07)
   → 3 sheet quý nhất: `khung_object` (18 object CSDL) · `SO_HOP_DONG` (1.183 mã)
     · `dinh_nghia_khai_niem` (55 khái niệm).
4. `KHO/08-thu-muc-lam-viec/.codex-nhap2-work/nhap2-core.js` (21/07)
   → Mô hình dữ liệu **có tên cột duy nhất trong kho**: 7 bảng lõi · 16 cột sự kiện
     · 29 loại · 14 checkpoint R01–R14 · quy trình P0/P1/P2.

## 5. CẢNH BÁO — cần Owner xác nhận

Hai file trong `z Tài liệu/` có **nội dung giống hệt nhau** (cùng mã băm) nhưng
mang hai tên khác hẳn:
  - `đề bài quản lý quy trình.docx`
  - `Quy trình thiết kế UI - Gemini.docx`
Ít nhất một tên đang **nói dối về nội dung**; tài liệu "quy trình thiết kế UI"
(nếu có thật) đã bị ghi đè mất. Nếu còn bản đúng, xin bổ sung lại.

## 6. Quy tắc dùng thư mục này từ nay

- Thư mục gốc chỉ có đúng 2 thứ: file này và `KHO/`.
- Không tạo file mới ở gốc.
- Nội dung thiết kế thì sửa vào tài liệu trên VPS, không viết ra file rời ở đây.
- **Không xoá gì trong `KHO/`** — các cặp `original`/`edited` là chuỗi bằng chứng,
  và 76 bản backup Excel là bản sao lịch sử duy nhất của sổ SSOT (sổ này chưa
  nằm trong Git).
