# BIÊN BẢN GỬI CODEX PHẢN BIỆN — vòng MOW-master + sắp xếp lại SO_HOP_DONG
Người soạn: CW (người giữ sổ Excel). Ngày 2026-07-17.
Mục đích: CW không tự tranh luận được, nên liệt kê các điểm đã quyết + điểm chưa chắc để Codex soi và phản biện. Chỗ nào Codex thấy sai, ghi rõ lý do; CW sẽ sửa (mọi thay đổi Excel đều có backup, hoàn tác được).

---

## A. Việc CW đã VERIFY độc lập và ĐỒNG Ý (nhờ Codex xác nhận, không phải bất đồng)
1. **MOW-master 8 mã `mowmaster.*`**: CW tự parse `mow-master-v1.html` → đúng 8 mã, đúng phần tử, 0 mã `mow.*` lọt, source = DOM = manifest. `master-list.js` sha `68b64784…` nguyên vẹn, vẫn 135 mã. ĐẠT.
2. **Bản vá cache `?v=3 → ?v=4`**: CW kiểm lại VPS — 4 trang tĩnh (mow-master, mot-master, mout-home, master-hub) đều đã `v4`, không trang nào còn `v3`; trang thứ 5 `master-list-quy-trinh` nạp bằng `fetch(?ts=)` + no-cache nên luôn tươi, không dính bẫy. CW **đồng ý đây là cách sửa đúng và trọn vẹn**.
   → **Nhờ Codex xác nhận 1 điểm**: có hệ thống nào khác đang *ghim cứng* chuỗi `?v=3` của `master-list.js` (build/CDN/cache tầng trên) mà việc bump lên `v4` có thể làm lệch không? Nếu không, CW khép điểm này.

## B. ĐỀ XUẤT sửa LUẬT (nhờ Codex duyệt câu chữ)
Luật cũ ghi trơn "KHÔNG bump `?v=`". Chính luật này đã *chặn đúng* cách vá cache ở mục A (vòng MOT đổi nội dung `master-list.js` nhưng không bump nên trình duyệt cache bản cũ = data-region vô hình).
**Đề xuất luật mới:** "Không bump `?v=` vô cớ. NHƯNG mỗi khi *nội dung* một file dùng chung (JS/CSS) thay đổi thì BẮT BUỘC bump `?v=` trên **mọi** trang tiêu thụ (đồng loạt) để phá cache; nội dung file giữ nguyên tuyệt đối khi chỉ bump."
→ Codex thấy câu chữ này ổn chưa? Có cần thêm case ngoại lệ (vd trang dùng `fetch(?ts=)` thì miễn)?

## C. SẮP XẾP LẠI SO_HOP_DONG theo Mẹ — ĐIỂM CHÍNH CẦN PHẢN BIỆN
Owner yêu cầu "mỗi Mẹ một khu vực cho dễ rà soát", `mowmaster` để cuối MOW trước MOT. CW đã làm (backup trước, hoàn tác được):
- **Thêm 1 cột `me`** (khu vực Mẹ: DÙNG CHUNG / MOW / MOT / MOIT…) + sắp vật lý theo cột đó. Lý do thêm cột: để lần sau thêm dòng chỉ cần điền `me` rồi sort, **không phải nhớ canh vị trí bằng tay** (đúng nguyên tắc "bỏ hardcode" Owner nêu).
- **Thứ tự vùng**: DÙNG CHUNG (shell 3 + master 135) → MOW (mow 127 → modw 31 → data.mow 5 → behavior.mow 1 → mowmaster 8) → MOT (mot 111 → modt 173 → motstudio 71 → motmaster 8) → MOIT (moit 5). Trang "master list" của mỗi Mẹ để CUỐI Mẹ đó.
- **Shared `master.*` (135)** giữ nguyên ở vùng DÙNG CHUNG, KHÔNG nhân bản vào từng Mẹ. `mowmaster`/`motmaster` (phần vỏ riêng) nằm ở Mẹ tương ứng.
- Giữ nguyên: 678 mã, 3 nhóm (192 D/72 H/414 G), màu theo nhóm, dropdown, lọc (A2:I2000), freeze, 0 lỗi.

**Câu hỏi CW CHƯA chắc, cần Codex phản biện:**
1. **Cột `me` có đáng thêm không**, hay là thừa/over-engineer? Nếu Codex thấy thừa, CW bỏ cột, chỉ sắp vật lý.
2. **Vùng DÙNG CHUNG nên để ĐẦU hay CUỐI sổ?** CW để đầu (nền tảng mọi Mẹ mượn). Có ý kiến khác không?
3. **`data.mow.*` (5) + `behavior.mow.*` (1)** là hợp đồng QUAN HỆ *vô hình* (không có khu UI). CW đang để trong Mẹ MOW. Nên để vậy, hay tách một vùng "QUAN HỆ/DỮ LIỆU ẩn" riêng cho dễ phân biệt với hợp đồng-có-khu-UI?
4. **`mot.run.condition/queue/signal_out` (3)** — 3 mã MOT cũ (DỮ LIỆU, không nguồn UI). Còn hợp lệ không, hay là rác cần soi/loại như mấy mã TO_REMOVE?
5. **`moit.proposal.*` (5)** — CW xếp Mẹ MOIT. Đúng Mẹ chưa? 5 mã này là thật (BUILT) hay placeholder cần đánh dấu lại trạng thái?

## D. ĐỀ XUẤT dọn file (Owner bảo tự đề xuất, để AI phản biện)
Sau khi CW reorg, **file chính (SSOT) = bản mới có cột `me`**. Bản trong `outputs/mowmaster_20260717/hop-dong-thong-tin-sua-re.xlsx` giờ **đã CŨ** (khác main, chưa reorg) + kèm `…​.inspect.ndjson` 4,2 MB.
**Đề xuất:** giữ file chính làm SSOT duy nhất; **xoá (hoặc chuyển sang thư mục `_archive/`)** bản Excel cũ + ndjson trong `outputs/mowmaster_20260717/` để tránh nhầm "file nào thật". Codex đồng ý xoá hay giữ làm dấu vết?

## E. LƯU Ý ĐỒNG BỘ (quan trọng cho vòng sau)
File chính SSOT bây giờ **đã có cột `me` (I) và đã sắp lại thứ tự dòng**. Vòng UI kế tiếp, khi Codex/CW ghi Excel phải lấy **bản main mới nhất** (`/quy trình/hop-dong-thong-tin-sua-re.xlsx`), **không** build trên snapshot cũ trong `outputs/…`. Khi thêm dòng mới nhớ **điền cột `me`** rồi sort lại theo (me, sub-UI).

---
Kết: A–B CW đã ngã ngũ (chỉ nhờ xác nhận). C–D là chỗ CW muốn Codex phản biện thẳng. Codex ghi ý kiến từng mục 1–5 (mục C) + D, CW chỉnh theo.
