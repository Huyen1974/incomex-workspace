# PROMPT — pg-nhan-balo
RUN_ID: PGNB-LABEL-MISSING-20261003-01
Executor_Surface: Codex

## 0. Mục tiêu duy nhất — Owner xác nhận 03/10/2026

**Chỉ dán nhãn cho những thứ CHƯA CÓ NHÃN để Balo nhận/phân loại được chúng.**

Không dán lại vật đã có nhãn. Không sửa nhãn đã có. Không tạo hệ nhãn mới. Không mở rộng thành bài đo SỐNG/DÍNH, đánh giá thừa-rác, dọn dẹp hay thiết kế lại Balo.

Nguồn chuẩn:
- trạng thái PG/Balo hiện tại;
- canonical `knowledge/dev/laws-new/pg-read-pg/balo-thuc-the-quy-dinh.md`;
- các quy tắc hiện hành trong `knowledge/dev/laws-new/pg-read-pg/label-rules/`.
Nếu tài liệu của việc này mâu thuẫn với canonical hoặc mục tiêu Owner ở trên thì **mục tiêu Owner + canonical thắng**.

## 1. Nguyên tắc

1. **Chỉ xử lý phần thiếu nhãn.** Giá trị nhãn hiện có là bất biến trong RUN này.
2. Dùng đúng cơ chế nhãn hiện hữu của Balo/canonical. Không thêm cột, bảng, FK, view, report, trigger, cron, registry hay format nhãn mới.
3. Không bịa nhãn. Không chắc thì để nguyên và đưa vào danh sách `CHUA-RO`/cần Owner hoặc Host xem sau.
4. Chỉ qua DOT/script-wrapper hiện hữu theo AGENTS; không SQL/REST tay.
5. Gate an toàn chung của hệ thống thuộc hạ tầng chung. Nếu gate chung chặn thì trả đúng một blocker; **không sửa/đẻ thêm yêu cầu vào PROMPT này**.
6. Không tắt, xoá, dời bất cứ vật nào.

## 2. Việc Codex làm — một lượt

### A. Kiểm hiện trạng
- Chạy `dot-balo-reconcile --verify` và đọc live PG/Balo bằng đường hiện hữu.
- Lập danh sách **chỉ những thực thể/vật còn thiếu nhãn cần thiết theo canonical**.
- Nếu có vật PG chưa vào Balo vì thiếu nhãn nguồn theo cơ chế hiện hành, ghi nó vào cùng danh sách.
- Tách rõ:
  - đã có nhãn → **không đụng**;
  - thiếu nhãn nhưng quy tắc xác định được → sẽ dán;
  - thiếu nhãn nhưng chưa đủ căn cứ → để nguyên, báo `CHUA-RO`.

### B. Dry-run
Trước khi ghi, xuất bảng ngắn:
`vật | nhãn đang thiếu | giá trị sẽ dán | quy tắc/căn cứ`.

Không có dòng ngoài nhóm thiếu nhãn.

### C. Dán nhãn
- Dùng DOT/cơ chế nhãn hiện hữu để chỉ điền ô/nhãn đang thiếu.
- Nếu vật chưa vào Balo vì thiếu nhãn nguồn, chỉ bổ sung **nhãn nguồn hiện hành** cần thiết rồi chạy reconcile hiện hữu; không sửa cơ chế reconcile.
- Không UPDATE/COMMENT lại vật đã có đủ nhãn.
- Không tạo schema hay hạ tầng mới.

### D. Kiểm lại
- Chạy `dot-balo-reconcile --sync` nếu cần, rồi `--verify`.
- Chứng minh:
  1. các vật vừa dán đã vào/được phân loại trong Balo theo cơ chế hiện hành;
  2. nhãn cũ của các vật khác không đổi;
  3. không tạo bảng/cột/view/FK/report/trigger/cron mới;
  4. không tắt/xoá/dời vật nào.

## 3. Xong khi

- Tất cả vật **có thể xác định nhãn bằng quy tắc hiện hành** đã được dán nhãn.
- Vật đã có nhãn trước RUN giữ nguyên từng byte ở phần nhãn.
- Vật chưa đủ căn cứ được liệt kê riêng, không đoán.
- Balo reconcile/verify PASS.
- Không có thay đổi cấu trúc/hạ tầng ngoài việc dán nhãn.

## 4. KQ

Ghi một khối ngắn vào `work/pg-nhan-balo/COLLAB.md`:

`KQ@PGNB-LABEL-MISSING-20261003-01 XONG|DỪNG`

Kèm:
- số vật thiếu nhãn trước RUN;
- số vật đã dán được;
- số vật còn `CHUA-RO`;
- danh sách nhãn/giá trị đã ghi;
- bằng chứng vật đã có nhãn không bị đổi;
- `dot-balo-reconcile --verify` PASS/FAIL.

Trả Owner đúng một dòng `XONG` hoặc `DỪNG: <blocker>`.
