# PROMPT — pg-nhan-balo
RUN_ID: PGNB-LABEL-20261002-01
Executor_Surface: Codex
Write_Path: repo = cổng `workspace_*` (hoặc `fs_*` nếu bề mặt bind được) · VPS1 PostgreSQL = chỉ qua DOT sẵn có: `dot-pg-atomic-apply`, `dot-pg-label-apply`, `dot-balo-reconcile`, khuôn report sẵn có
Trạng thái: chỉ chạy khi `COLLAB.md` có `READY@<sha>` trùng commit cuối chạm file này, và Owner đã RUN.

## 0. Một câu
Đặt luật nhãn v1.0 lên hiện trường và dán nhãn cho mọi vật trong `balo_thuc_the` (VPS1, database `directus`). **Chỉ dán nhãn.** Không tắt, không xoá, không dời, không đổi cấu hình PG. Đích: Owner mở một màn theo khối, 30 giây là thấy khối nào đáng nghi.

Giao theo đầu ra trọn gói: trong phạm vi mục 2, tự làm liên tục, tự sửa và kiểm lại. Chỉ dừng khi vượt phạm vi, thiếu capability, hoặc gặp điều kiện DỪNG ghi bên dưới.

## 1. Read-gate (trước mọi thay đổi)
1. Đọc `AGENTS.md` → `work/pg-nhan-balo/COLLAB.md` (§0, Bảng, D01–D07, P01–P02) → file này → `view.html` mục `#C` (từ điển + câu thử), `#bien` (vị trí biển, mẫu B1/T0/B3), `#cot`, `#so-dot`. **Luật nằm ở `view.html`; file này không chép lại luật.**
2. `READY@` trong COLLAB = commit cuối chạm `PROMPT.md`. Lệch → DỪNG.
3. Ghi `STARTED@PGNB-LABEL-20261002-01 <UTC> · executor=Codex` vào COLLAB + sửa dòng ■/➡/`cập nhật` của Bảng (MT4, DROOT31).
4. Đọc Bảng điều khiển của `work/vps1-up-grade/COLLAB.md`: nếu bước chuyển production (G7) đã STARTED mà chưa KQ → DỪNG, không đụng VPS1.
5. Trên VPS1, chỉ đọc: schema hiện tại của `balo_thuc_the`; `dot-balo-reconcile --verify`; nội dung `/opt/incomex/dot/sql/balo-reconcile.sql`; cách khuôn report-pg đang được đúc; **sổ DOT** của việc `vps1-up-grade` (xem mục 4-B9). Ghi lại những gì lệch với file này trước khi làm.

## 2. Được ghi (ngoài danh sách này = DỪNG)
- `public.balo_thuc_the`: thêm 3 cột `dinh integer`, `ket_luan varchar`, `ngay_do date`; cập nhật `nhom`, `loai`, `active`, `dinh`, `ngay_do`; ràng buộc giá trị.
- Bảng mới `public.balo_tu_dien_nhan` (B1 = các dòng luật + B2 = giá trị và câu thử). View mới `public.v_balo_theo_khoi`.
- `COMMENT ON TABLE public.balo_thuc_the` (hai dòng trỏ T0, đặt ở đầu) và comment một dòng cho hai vật mới.
- File dưới `/opt/incomex/dot/sql/` + manifest tương ứng; commit git `/opt/incomex/dot` đúng các file đã tạo/sửa (không `git add -A`).
- Mục Reports: trang `report-balo-khoi`, `report-balo-luat`, và hiện cột mới ở 4 trang balo đang có — bằng khuôn/DOT report sẵn có.
- T1: đúng **một dòng trỏ** vào mỗi file `AGENTS.md` trong `docker/agent-data-repo`, `docker/nuxt-repo`, `docs/mcp-writes` (VPS1).
- Hồ sơ: `/opt/incomex/work/pg-nhan-balo/` (có `INDEX.md`).
- Repo: STARTED/KQ + Bảng trong `work/pg-nhan-balo/COLLAB.md`.

## 3. Cấm
- Tắt/bật trigger hoặc cron · DROP/DELETE/TRUNCATE · dời schema · đổi cấu hình PG (kể cả bật đếm lượt gọi hàm) · restart dịch vụ.
- SQL tay, `psql` trực tiếp, REST admin (DROOT26). Thiếu capability → DỪNG báo Host; **không viết DOT mới trong RUN này**.
- Điền `ket_luan` (chỉ Owner). Để NULL toàn bộ.
- Suy SỐNG cho view/hàm từ bảng nguồn. Đoán KHỐI/VAI theo tên.
- Viết thêm nhãn vào `COMMENT ON` của vật khác; sửa/xoá nhãn văn cũ.
- Thêm trigger lên `balo_thuc_the` (đang 0 trigger, giữ nguyên).
- Đặt tên bảng bắt đầu bằng `v_`. Lập sổ DOT thứ hai. Chạy `dot-dot-register` chế độ thật. Viết mã Nuxt mới.

## 4. Việc, theo thứ tự
- **B0 · Sao lưu.** Xuất toàn bộ 2.148 dòng balo ra file hồ sơ bằng đường đọc/DOT sẵn có (giữ giá trị `nhom` tiếng Việt cũ của 654 hàm). Ghi danh sách trigger bật/tắt và số bảng/view/hàm để so sau.
- **B1 · Nền.** Thêm 3 cột. Tạo `balo_tu_dien_nhan` với các cột: `nhan`, `gia_tri`, `ten_hien_thi`, `ap_cho`, `thu_tu`, `cau_thu`, `vi_du`; nạp đủ giá trị theo `view.html#C1–C6` **và các dòng luật `nhan = 'LUAT'`, `thu_tu` 0–8 theo mẫu `view.html#B1`** (chữ luật để ở cột `cau_thu`; đây là bản gốc duy nhất của luật). Chưa bật ràng buộc.
- **B2 · KHỐI** (máy, theo C1). Bảng/view/hàm: đọc nhãn văn cũ của chính vật (`obj_description`), lấy dòng `HE (so huu):` nếu có, không thì mã đầu của dòng `HE:`; không có hoặc không thuộc 23 mã → `CHUA-RO`. Trigger: KHỐI của hàm nó gọi. `chuyen_mon` giữ nguyên.
- **B3 · VAI.** Hàm: giữ 5 giá trị `loai` đang có; hàm trống → theo C3. Bảng (385): phân loại theo 7 câu thử C2, từ trên xuống; căn cứ là sự thật đo được (cột, khoá ngoại, `pg_depend`, bộ đếm ghi, nguồn nạp), không theo tên; không chắc → `CHUA-RO` + lý do ngắn trong hồ sơ. View và trigger: `x`.
- **B4 · SỐNG** (máy, theo C4, ghi `ngay_do`). Bảng: kỳ = bộ đếm hiện tại trừ ảnh chụp 01/08; số dòng = `count(*)` thật. Bảng không có mốc → `CHUA-RO`. View, hàm → `Không đo được`. Trigger → `Bật`/`Tắt`.
- **B5 · DÍNH** (máy, theo C5, chỉ trong PG).
- **B6 · Ràng buộc.** PG phải từ chối: (a) giá trị không có trong từ điển; (b) giá trị có trong từ điển nhưng của nhãn khác. Thêm giá trị sau này chỉ cần INSERT một dòng từ điển, không cần DROP. Không dùng trigger. Gợi ý: khoá ngoại tổ hợp `(nhan, gia_tri)` với cột hằng sinh sẵn; cách thuần PG tương đương đạt đủ ba điều trên được phép, ghi lý do. Chứng minh bằng hai phép thử không để lại dữ liệu.
- **B7 · Dòng trỏ.** T0: mẫu `view.html#T0` vào ghi chú bảng balo qua `dot-pg-label-apply`, đặt ở ĐẦU, giữ nguyên chữ cũ bên dưới. B3: mẫu `view.html#B3` ở đầu mỗi file SQL của việc này. **Không chép các dòng luật ra nơi nào ngoài bảng `balo_tu_dien_nhan`.**
- **B8 · Màn hình.** View `v_balo_theo_khoi`: mỗi khối một dòng — số vật theo loại (bảng/view/hàm/trigger) · số bảng theo SỐNG (rỗng/đứng yên/tự quay/có ghi) · số `CHUA-RO` · tổng DÍNH · `ket_luan` của khối. Trang `report-balo-khoi` và `report-balo-luat` đúc đúng khuôn `report-pg` đang chạy; 4 trang balo hiện thêm cột mới. Khuôn cần bảng thay vì view → bảng `balo_theo_khoi` nạp lại từ view. Phải viết mã Nuxt mới → không làm phần trang, ghi gap.
- **B9 · Trỏ và sổ.** T1: thêm vào đầu mục “Quy ước bắt buộc từ nay” của 3 `AGENTS.md` đúng dòng: `Nhãn PG hiện hành nằm ở bảng balo_thuc_the; luật dán nhãn đọc ở bảng balo_tu_dien_nhan (các dòng nhan = 'LUAT'). Quy ước DIA CHI / SU KIEN trong COMMENT ON bên dưới là hồ sơ 08/2026, không viết thêm.` T2 (KB): không làm, KB đang khoá ghi → ghi gap. Sổ DOT: tìm sổ do việc `vps1-up-grade` lập; có trên VPS1 → thêm dòng cho các file SQL mới theo đúng khuôn của sổ, và trả lời Q10 trong COLLAB (đường dẫn, cột, chữ ghi/đọc); không có hoặc chỉ có trên máy lab → không lập sổ mới, ghi gap.
- **B10 · Hồi quy và bảo vệ.** 4 trang balo cũ + nút Làm mới vẫn chạy (browser thật); `dot-balo-reconcile --verify` PASS sau thay đổi và không xoá nhãn vừa dán; file bền mới vào lớp bảo vệ sẵn có (DROOT29); đọc bảng đèn (DROOT34).

## 5. Bẫy đã biết
1. `dot-pg-atomic-apply` từ chối mọi file chứa chuỗi `meta_catalog`, `birth_registry`, `table_registry`, `v_registry_`, `qt001_` — kể cả trong chú thích hay dữ liệu. ⇒ SQL dán nhãn khoá theo `stt`, không viết tên vật; cột `vi_du` của từ điển tránh các tên đó. **Không nới guardrail.**
2. Cổng atomic chặn mọi DROP, kể cả `ALTER … DROP CONSTRAINT/COLUMN` ⇒ làm đúng ngay lần đầu; ràng buộc phải mở rộng được bằng INSERT.
3. `COMMENT ON` ghi đè cả khối ⇒ đọc comment hiện có của balo rồi nối. `dot-pg-label-apply` từ chối `COMMENT ON TRIGGER`.
4. `pg_stat` cộng dồn từ 17/04/2026; `n_live_tup` là ước lượng; TRUNCATE không tính vào `n_tup_del`.
5. Ảnh chụp 01/08: `/opt/incomex/evidence/del1g-20260801/out/snap_directus_0.psv` (352 dòng, 9 trường ngăn bởi `|`: thời điểm, tên, 7 số). **Nghĩa 7 cột số phải xác định từ script sinh ra nó trong cùng thư mục evidence**; bảng ngoài `public` ở `ngoai_0.psv`. Không xác định chắc → SỐNG của bảng = `CHUA-RO` và báo Host.
6. Directus theo dõi `balo_thuc_the` như collection; cột mới muốn hiện trên trang phải đi qua DOT/khuôn report, không sửa tay Directus.

## 6. Xong khi
- Dòng `da_mat = false`: không còn ô trống ở `nhom`, `loai`, `active`, `dinh`; `ket_luan` NULL toàn bộ.
- PG từ chối giá trị lạ và giá trị sai nhãn (có bằng chứng).
- Các dòng luật đọc được bằng SELECT từ `balo_tu_dien_nhan`; ghi chú bảng balo có hai dòng trỏ ở đầu, chữ cũ còn nguyên; trang `report-balo-luat` hiện đúng bảng đó (hoặc gap ghi rõ).
- `v_balo_theo_khoi` trả mỗi khối một dòng; trang `report-balo-khoi` mở được (hoặc gap ghi rõ).
- 4 trang balo cũ và nút Làm mới không hỏng.
- Danh sách trigger bật/tắt và số bảng/view/hàm ngoài mục 2 không đổi so với B0.

## 7. KQ
Ghi vào `work/pg-nhan-balo/COLLAB.md` một khối ngắn `KQ@PGNB-LABEL-20261002-01 XONG|DỪNG` (kèm sửa ■/➡/`cập nhật` của Bảng):
- số vật đã dán đủ · số `CHUA-RO` theo từng nhãn;
- các khối có dấu hiệu ít hoặc không sử dụng (toàn rỗng / đứng yên / tự quay);
- công cụ DOT có dấu hiệu không còn dùng theo sổ DOT (nếu đọc được sổ);
- thay đổi schema VPS1 (+1 bảng, +3 cột, +1 view, ràng buộc) để việc `vps1-up-grade` biết;
- gap · blocker cần Owner quyết · `ĐÈN: n xanh · m đỏ` · đường dẫn hồ sơ.
Trả Owner đúng một dòng `XONG` hoặc `DỪNG`.
