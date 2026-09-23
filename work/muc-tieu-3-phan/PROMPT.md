# PROMPT — MT3 · Chuẩn hoá §0 thành ba phần (GitHub + view)

RUN_ID: MT3-20260923-01
Host: Claude Chat · Host_ID: CLAUDE-MT3-260923-A
Executor_Surface: Codex/GPT Work
VPS_Evidence: theo AGENTS A8 — `/opt/incomex/work/muc-tieu-3-phan/`

## 0. Cổng trước khi sửa bất cứ thứ gì
- Đọc `AGENTS.md` → root `COLLAB.md` → `work/muc-tieu-3-phan/COLLAB.md` → file này.
- Commit cuối chạm `work/muc-tieu-3-phan/PROMPT.md` phải khớp `READY@<40 hex>` trong COLLAB việc này. Lệch → DỪNG.
- Tài liệu/workspace: GitHub là SSOT. Mã chạy (parser `sync.py`, app view): VPS là SSOT theo §11 — sửa trên VPS, đẩy bản sao tham khảo lên GitHub, không kéo mã từ GitHub xuống.

## 1. Bối cảnh ngắn
Mỗi việc trong repo có một `COLLAB.md`; mục `## 0. MỤC TIÊU/NHIỆM VỤ USER` là thứ Owner đọc đầu tiên và cũng là thứ Task html view hiển thị trên đầu trang chi tiết. Hiện §0 vừa dài vừa lẫn nhiều vòng, Owner không dùng được làm kim chỉ nam. Lượt này chuẩn hoá §0 thành ba phần cố định, **trên GitHub trước**, rồi view hiển thị theo.

## 2. Khuôn §0 chuẩn — ghi vào AGENTS (A0)
```
## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN (…) | CHƯA XÁC NHẬN

### 1. Mục tiêu
<lời Owner, ngắn>

### 2. Thế nào là hoàn thành
- <lời Owner, mỗi ý một dòng>

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
<tùy AI>

### Vòng trước
<các khối A0 cũ, giữ nguyên>
```
Luật kèm theo (ghi cùng chỗ trong AGENTS):
- Tên bốn mục con **đúng từng chữ** để máy đọc được; dòng `Xác nhận User:` giữ nguyên vị trí đầu §0 (A9 không đổi).
- Phần 1 và 2 là **lời Owner**: AI không tự sửa chữ. AI được đề xuất nhưng phải đánh dấu `(đề xuất — chờ Owner gật)`.
- Phần 3 do Host quản; hạng mục đã XONG được cắt còn một dòng tóm tắt + mã commit, để §0 luôn ngắn.
- `### Vòng trước` chứa nguyên văn các khối A0 cũ; **không xoá lịch sử**.
- Mở việc mới hoặc `Mở lại <id>`: viết ngay theo khuôn này.

## 3. Parser (`sync.py` trên VPS)
- Tách `goal` hiện tại thành `objective`, `doneWhen`, `details`, `history`.
- Đọc được **cả §0 cũ lẫn mới**: thiếu mục nào → chuỗi rỗng + cảnh báo `§0 chưa chuẩn`; không được vỡ hay bỏ việc.
- Tìm kiếm vẫn quét toàn bộ §0 như hiện nay (id + title + mọi vòng mục tiêu).
- Không đổi A9/4 thanh trạng thái, presence, actor, retention, webhook.

## 4. View
- Trang chi tiết: **Mục tiêu** và **Thế nào là hoàn thành** mở sẵn, ở trên cùng; **Chi tiết cần đạt** và **Vòng trước** gập lại.
- Việc chưa chuẩn: hiện nguyên §0 như cũ + nhãn nhỏ `§0 chưa chuẩn`.
- Sidebar, master list, deep-link, “Vừa làm/Đang làm” giữ nguyên.

## 5. Di trú các việc hiện có (cả `work/` và `work/done-tasks/`)
- Phần 1: lấy **nguyên văn** câu Owner của vòng hiện hành; không viết lại, không tóm tắt.
- Phần 2: tiêu chí nào do Owner từng nói thì đưa lên; không có thì soạn tối đa 3 gạch đầu dòng từ chính nội dung đã có và đánh dấu `(đề xuất — chờ Owner gật)`.
- Phần 3: phần diễn giải kỹ thuật còn lại; hạng mục đã có KQ XONG rút còn một dòng + mã commit.
- Các khối A0 cũ → `### Vòng trước`, nguyên văn.
- **Chỉ đụng §0**; không sửa phần khác của COLLAB, không đổi trạng thái/PROMPT/READY/KQ của bất kỳ việc nào.
- Việc đang có RUN dở dang: vẫn di trú §0 (chỉ sắp xếp lại chữ), không chạm PROMPT của việc đó.

## 6. Thứ tự
1. Sửa parser + view trên VPS, chạy fixture cả §0 cũ lẫn mới → deploy, health PASS (lỗi → rollback, DỪNG).
2. Ghi khuôn + luật vào AGENTS.
3. Di trú §0 của từng việc, mỗi việc một commit hoặc một commit chung rõ ràng.
4. Kiểm lại trên web sau khi webhook đổ xuống.

## 7. Nghiệm thu
- 100% việc trong `work/` và `work/done-tasks/` có đủ bốn mục con đúng tên.
- Mở một việc trên web: thấy ngay Mục tiêu + Thế nào là hoàn thành; Chi tiết và Vòng trước gập.
- Fixture §0 cũ (chưa chuẩn): hiện được + có nhãn cảnh báo, không vỡ.
- Tìm kiếm cũ vẫn ra đúng việc; 4 thanh trạng thái, Vừa làm/Đang làm, deep-link không đổi.
- B2 regression + webhook PASS; không đụng gateway/MCP/presence; retention giữ nguyên.
- Không xóa lịch sử, không sửa chữ của Owner.

## 8. Cấm
- Không đổi MCP schema/version/auth, không đụng hai gateway B3.
- Không tạo file/trang/database mới ngoài bằng chứng trong `/opt/incomex/work/muc-tieu-3-phan/`.
- Không đổi nội dung ngoài §0 của các việc khác.
- Không tự mở rộng sang deep-link/MMIM hay việc khác.

## 9. Báo cáo
- Cập nhật chính `work/muc-tieu-3-phan/COLLAB.md`: refs runtime, danh sách việc đã di trú, test, rollback.
- Ghi `KQ@MT3-20260923-01 XONG|DỪNG` trong COLLAB.
- Trả đúng một dòng: `XONG · MT3 · <refs>` hoặc `DỪNG · MT3 · <lý do>`.
