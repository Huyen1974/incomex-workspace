# data-region — README CHO AGENT (đọc TRƯỚC khi sửa UI ở thư mục này)

## Đây là gì
Mỗi khu vực UI có nghĩa hợp đồng được gắn một MÃ BỀN ngay trong thẻ HTML:
    data-region="mow.propose.advanced"
Mã = ĐÚNG cột `ui_cay_ma_khu_vuc` (cột C) trong file Excel cây khu vực (hop-dong-thong-tin-sua-re.xlsx).
Mục đích: mỗi lần UI đổi, chỉ cần `grep data-region` trong code rồi so cột C → thấy ngay
thiếu/thừa, KHỎI quét lại toàn bộ. Đây là nền "SỬA RẺ".

## Quy tắc mã
chữ thường · không dấu · các cấp nối bằng dấu CHẤM. Cùng chức năng = cùng từ khoá ở MỌI UI:
đề xuất=propose · vận hành=ops · nâng cao=advanced · thường=normal · quản trị=admin.

## QUY TRÌNH GẮN (lặp cho MỖI nhánh — KHÔNG làm một cục 100 mã)
1. CW map 1 nhánh → xuất spec FIND→REPL lên VPS (/opt/incomex/docs/mcp-writes/ui-preview-regions-*.txt).
   Đọc HTML QUA TRÌNH DUYỆT (fetch) để trích chuỗi FIND CHÍNH XÁC (connector chặn file >50KB).
2. Claude Code đọc spec → thay LITERAL (str.replace, không đoán) → ui-preview-git snapshot "...".
3. CW nghiệm thu ĐỘC LẬP (đường tool khác người sửa):
   - grep -o 'data-region="[^"]*"' 2 file → tập mã PHÂN BIỆT phải khớp cột C (so TẬP, không so số dòng: name/comment lặp theo tầng là hợp lệ).
   - byte-check: gỡ hết data-region → phải hiện lại đủ mọi chuỗi FIND gốc (chứng minh chỉ thêm attr, không mất byte).
   - mở UI, bấm ⚙ → modal chạy, không vỡ.
4. Owner duyệt → nhánh tiếp.
5. FIND không khớp → CW SỬA SPEC, KHÔNG để Claude Code đoán.

## 4 CẢNH BÁO (đã trả giá để biết)
1. Chia theo NHÁNH (~10–25 mã), nghiệm thu từng nhánh. Spec 100 entry một cục = sai một chỗ hỏng cả mẻ, khó lần.
2. File HTML 112KB nhiều class TRÙNG (nhiều <div class="card">, <button>…). Với MỖI FIND trong HTML,
   phải ĐẾM số lần khớp TRƯỚC khi đưa vào spec. Khớp >1 mà ghi OCC:first = gắn nhầm chỗ mà không ai biết. BẪY LỚN NHẤT.
3. Cột C có thể SAI/THIẾU (CW quét ra, chưa soát từng dòng). Mã trong Excel không ứng thẻ thật → BÁO, đừng bịa thẻ.
   Thẻ thật mà cột C thiếu mã → thêm vào Excel trước (id mới, tăng dần không tái dùng), KHÔNG tự chế mã trong code.
4. "Gắn xong 121 mã" KHÔNG phải đích. Mã chỉ là GIÁ ĐỠ. Đích = HỢP ĐỒNG THÔNG TIN
   (lọc concept nghiệp vụ → 2 bảng PG: sua_re_khai_niem_nhap + sua_re_ui_khai_niem_nhap).

## SỬA LẠI SAU NÀY (maintenance — việc này làm đi làm lại)
UI đổi → TRONG CÙNG lần sửa: gắn data-region cho khu mới + ui-preview-git snapshot.
Định kỳ: ui-preview-git log --since="7 days ago" -p → xem tuần qua đổi gì → grep data-region mới ↔ cột C → cập nhật delta.
Cơ chế Git (cuốn sổ): xem ../ui-preview-notebook/README.txt.

## AN TOÀN
CHỈ thêm thuộc tính, không xoá/đổi logic. Người sửa (Claude Code) ≠ người kiểm (CW).
KHÔNG bump ?v= trong HTML. KHÔNG sửa tay ngoài quy trình. KHÔNG cài hook chặn (để sau, khi gắn xong).

---
Cập nhật: 2026-07-12. Pilot ĐẠT: nhánh mow.propose.advanced (21 mã, commit 545eef2, CW nghiệm thu độc lập).


## HIẾN PHÁP WIDGET — 4 luật gắn data-region (chốt 2026-07-13)
Mọi mã data-region rơi vào ĐÚNG 1 trong 4 ô — khỏi dừng bàn lại từng kiểu template:

LUẬT 1 — Thẻ do template sinh NHIỀU BẢN, mỗi bản chỉ khác DỮ LIỆU → GỘP 1 mã widget.
  (= luật cũ "hàng lặp tính theo TEMPLATE, không nhân theo số dòng dữ liệu" — KHÔNG phải luật mới.)
  Cách: 1 data-region / 1 setAttribute TRONG vòng lặp/template. VD: 7 tab → layer.tab; dock chip → dock.chip; thẻ lưới → grid.card.

LUẬT 2 — KHÁI NIỆM RIÊNG tình cờ dùng chung 1 widget → TRUYỀN MÃ QUA THAM SỐ widget → emit data-region="${reg}".
  VD: mkSec render 4 nhóm drawer = 4 khái niệm KHÁC HẲN (Thông tin / Trigger & Output / Assignee & SLA / Lịch sử) → truyền 4 mã. (Chúng sẽ thành CỘT PG — gộp là mất khái niệm.)

LUẬT 3 — Thẻ TĨNH riêng biệt (có sẵn trong markup) → FIND→REPL literal. VD: banner, drawer container, field label.

LUẬT 4 — Thẻ DOM riêng biệt (mk()/createElement) → setAttribute('data-region','CODE') NGAY dòng tạo thẻ (không gom cuối hàm; spec ghi rõ tên biến).

RANH GIỚI LUẬT 1 vs LUẬT 2 (chỗ tinh tế nhất — dễ gộp bừa):
  Câu hỏi phân biệt: "các bản khác nhau ở DỮ LIỆU hay ở Ý NGHĨA?"
  - Khác DỮ LIỆU (7 tab = 1 control, 7 tầng chỉ là data đổ vào) → LUẬT 1, GỘP.
  - Khác Ý NGHĨA (4 section = 4 nhóm nghiệp vụ, sẽ thành cột PG) → LUẬT 2, TRUYỀN THAM SỐ, giữ riêng.
  Gộp nhầm khái niệm = mất concept = TRÁI ĐÍCH (hợp đồng thông tin).

RÀNG BUỘC CHUNG:
  - Anchor (FIND / dòng mk-createElement) phải ĐẾM = 1. Trùng → ghi rõ ngữ cảnh, đừng gắn nhầm.
  - Nghiệm thu quét CẢ 2 dạng: data-region="…" VÀ setAttribute('data-region',…). Byte-check gỡ cả 2 dạng.
  - LUẬT 2 (đổi logic widget: thêm tham số) → byte-check KHÔNG đủ, PHẢI mở UI thật bấm thử; làm RIÊNG lượt, đừng trộn batch chèn-attr thuần.


## LUẬT 5 (mở rộng hiến pháp → 5 LUẬT) — NÚT CÂY
Mã chỉ là NÚT GOM NHÁNH trong cây (như thư mục cha), KHÔNG phải khu hiển thị riêng → KHÔNG gắn data-region vào code.
Đánh dấu trong Excel: cột trang_thai = "nút cây". Cơ chế kiểm grep ↔ cột C PHẢI BỎ QUA các mã này
(nếu không → báo "thiếu mã" giả VĨNH VIỄN — đúng bệnh 119/120 rác cần tránh nhất).

Bằng chứng đã đọc code (2026-07-13, không đoán): đổi chế độ qua go()/render() CHỈ toggle class '.show'/'.on'
+ vẽ lại CÙNG #nodes-wrap; KHÔNG có <div id="mode-..."> / data-mode / class="mode-" nào (modeWrap=0).
Cả 4 chế độ DÙNG CHUNG một bộ thẻ → không có phần tử bọc chế độ để gắn.
→ 5 mã mode-level đã đánh dấu nút cây: mow, mow.normal, mow.propose, mow.ops, mow.admin.

Khi soạn spec sau: gặp mã là nút gom nhánh KHÔNG có element thật (vd có thể là mow.propose.insert nếu 3 nút ＋
gắn riêng lẻ) → áp LUẬT 5, đánh dấu trang_thai='nút cây', đừng ép gắn.


## QUY TRÌNH RÚT GỌN cho UI TIẾP THEO (MOT / MOIT / MOUT) — 5 luật đã xong, KHÔNG khám phá lại
1. CW quét cây khu vực UI mới → điền cột C (Excel).
2. CW map spec theo 5 LUẬT CÓ SẴN → 1 spec/UI (KHÔNG chia mẻ; chỉ TÁCH RIÊNG phần ĐỔI LOGIC nếu có).
3. Desktop soi spec.
4. Claude Code chạy 1 lượt.
5. CW grep + byte-check (quét cả 2 dạng: data-region="…" và setAttribute('data-region',…)).

Ước 1–2 lượt/UI. Chỉ DỪNG BÀN nếu gặp KIỂU DỰNG THỨ SÁU (khả năng thấp — 5 luật phủ 100% MOW, UI phức tạp nhất: 4 chế độ × 7 tầng × modal lồng).
Ghi nhớ: MOW tốn ~8 lượt vì VỪA LÀM VỪA ĐẺ 5 LUẬT. Luật xong → 3 UI kia là ĐƯỜNG BẰNG.


## TRIẾT LÝ DỮ LIỆU + ĐẦU CHỜ (chốt 2026-07-13 — đọc để KHÔNG bàn lại)

**Nhập tối thiểu, thông tin tối đa:** người dùng bấm/kéo như chơi game; hệ thống tự bắt vị trí/nội dung/cha-con/thứ tự. → MỖI HÀNH ĐỘNG UI = MỘT LỆNH GHI DỮ LIỆU.

**Cột `tac_dong_du_lieu` (Excel, thêm sau ban_chat):** mỗi khu ghi 2 chiều — LOẠI (thực_thể/trường/hành_động_ghi/điều_hướng) + đụng dữ liệu gì. Điền bằng đọc code. Đầu chờ rẻ nhất.

**4 lỗ hổng cấu trúc (biết thiếu — HOÃN CÓ CHỦ Ý, làm ở phiên thiết kế dữ liệu):**
1. `parent_id` — parent=0 cả file → cây cross-tier không lưu.
2. id bền cho mục con — chỉ `rid++` tạm.
3. `order` bền — chỉ origIndex/vị trí mảng.
4. chèn/tham chiếu bằng tên/code, không id.
GHI NỢ: modal nâng cao (mvx-v3.js) thiếu `_userMoved`/`_roleChanged` mà editor thường (html) có → 2 luồng ghi lệch.

**Kiến trúc (chốt để đặt tên đúng, CHƯA làm):**
- KHUÔN + BẢN ĐÚC (nút "Khuôn mẫu/Vận hành" = `st.vm` chính là cơ chế này). KHÔNG nhiều-cha ở tầng trên.
- Nhiều-cha CHỈ ở T1 (work dùng lại nhiều quy trình → bảng nối). T7→T2 mỗi ô một cha.
- Chuyển cha trên UI → hoãn; nhưng parent_id trong data phải có.

**Hệ mã 8+ UI (áp khi làm tới, không đoán):** shell.* = dùng chung (dock) · mow./mot./moit./mout.* = 4 Mẹ · modw./modt./modit./modut.* = 4 công cụ thiết kế. "Nằm trong ai mang tên người đó." ĐANG LÀM MOW — không khảo sát UI khác.

**Nghĩ rộng, làm hẹp:** thêm-sau-đắt→làm ngay; thêm-sau-rẻ→hoãn. Data-region không lạc hậu → gắn nốt.


## ✅ MOW — GẮN MÃ KHÉP 100% (2026-07-13)
TRỌNG TÀI (grep 3 file ↔ cột C active): **0 THIẾU · 2 THỪA** (view.template/ops = nút chết `cần xoá`). A_active=105, B_code=107.
- 3 file: mow-unified-canvas-v2.html (72) · mvx-v3.js (26) · eco-nav.js (3 `shell.dock.*` SHELL_SHARED).
- 4 commit cuối: `6fb69d1` tier · `605d357` dock · `df93f61` mvx · `5c9aeb0` badge (vá sót mẻ #4).
- Bằng chứng cơ chế: grep bắt `mow.shell.layer.badge` bị sót ở mẻ #4 (gắn lên nút tab, quên badge bên trong) — Claude Code + CW + Desktop đều không thấy, nghiệm thu DOM vẫn PASS. → **CHẠY TRỌNG TÀI SAU MỖI UI**.
- Ghi nợ: [dọn UI] xoá 2 nút Khuôn/Vận hành · dựng shell.dot · gom mvx-del helper. [thiết kế dữ liệu] 4 lỗ hổng (id/parent_id/order/chèn-tên) · cây-không-phải-cây · modal thiếu _userMoved/_roleChanged.
