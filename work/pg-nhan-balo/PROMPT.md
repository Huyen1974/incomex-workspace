# PROMPT — pg-nhan-balo
RUN_ID: PGNB-LABEL-20261002-03
Bản lệnh: v4 · 03/10/2026 · **P11 rút gọn điều hành** sau khi P10 đã chạy thử phần PG trên 16.15/18.4. Vẫn một PROMPT, không tạo v5. Chi tiết thử nghiệm/bug công cụ nằm ở COLLAB P10; prompt này chỉ giữ việc Codex phải làm + chốt an toàn bắt buộc.
Executor_Surface: Codex
Write_Path: repo = cổng `workspace_*` (hoặc `fs_*` nếu bề mặt bind được) · VPS1 = chỉ qua các DOT ở §1.5
Trạng thái: chỉ chạy khi `COLLAB.md` có `READY@<sha>` trùng commit cuối chạm file này, và Owner đã RUN.

## 0. Một câu
Đặt luật nhãn lên hiện trường và dán 4 nhãn đầu cho mọi vật còn tồn tại trong `balo_thuc_the` (VPS1, database `directus`). **Chỉ dán nhãn.** Không tắt, không xoá, không dời, không đổi cấu hình PG. Đích: Owner mở trang “Balo theo khối”, 30 giây là biết khối nào cần rà.

**Codex tự làm trọn gói.** Trước mutation chỉ smoke các cổng thật một lần; lỗi thì gom đủ và DỪNG một lần. Đạt thì chạy thẳng tới KQ, không quay lại hội đồng giữa chừng.

## 1. Read-gate (trước mọi thay đổi production)
1. Đọc `AGENTS.md` → `work/pg-nhan-balo/COLLAB.md` (§0, Bảng, D01–D11, P01–P10, KQ của RUN -01 và -02) → file này → `view.html`: `#C` (từ điển + câu thử), `#bien` (vị trí, mẫu B1/T0/B3), `#cot` (cột + khoá nhãn), `#so-dot`. **Luật nằm ở `view.html`; file này không chép lại luật.** Trước khi bảng luật tồn tại trong PG, `view.html` là bản luật để làm.
2. `READY@` trong COLLAB = commit cuối chạm `PROMPT.md`. Lệch → DỪNG.
3. Ghi `STARTED@PGNB-LABEL-20261002-03 <UTC> · executor=Codex` vào COLLAB + sửa dòng ■/➡/`cập nhật` của Bảng (MT4, DROOT31).
4. **Một cổng an toàn chung:** ngay trước mutation, kiểm READY/HOLD/STOP của chính việc + shared production lock/Guard theo AGENTS. Nếu máy đang bận bởi mutation khác hoặc Guard chung chưa healthy ⇒ DỪNG một lần với `BLOCKER HẠ TẦNG CHUNG`; không đọc/điều hành task khác để tự xử lý.
5. **Preflight tối thiểu — Codex tự làm, không quay lại hội đồng:**
   - `dot-pg-atomic-apply`: chạy một SELECT thật; kiểm các file SQL cuối qua path/hash/guard. P10 đã integration-test DDL/ràng buộc trên PG 16.15 và 18.4 với đủ 2.148 dòng; **không dựng lại lab**. Chỉ TEMP-probe lại nếu live PG/schema khác bằng chứng P10.
   - `dot-pg-label-apply --check`: dùng đúng `sql/labels/` + label manifest.
   - `dot-report-publish`: dry-run hai spec bằng truy vấn probe trên vật đang có; sau khi có dữ liệu mới dry-run truy vấn cuối. Dùng đúng mẫu đã thử ở `view.html#ddl-mau`.
   - `dot-balo-reconcile --verify`: phải PASS.
   - Shared production Guard: dùng **CLI chuẩn hiện hành của hệ thống**, không chép/reimplement tham số Guard trong prompt này. Guard/preflight phải healthy trước mutation; POST-PROTECT theo AGENTS DROOT29/DROOT34 sau mutation.
   - Thử hết các mục trên rồi mới quyết. Có lỗi ⇒ báo **một KQ DỪNG duy nhất** liệt kê đủ blocker. Tất cả đạt ⇒ chạy thẳng B0→B10, không hỏi lại.

## 2. Được đổi — danh sách đóng
**PostgreSQL `directus.public`**
- `balo_thuc_the`: +3 cột nhãn `dinh integer`, `ket_luan varchar`, `ngay_do date` · +4 cột khoá tự sinh (STORED) `k_khoi`, `k_vai`, `k_song`, `k_ketluan` · +4 khoá ngoại tổ hợp sang từ điển (theo `view.html#cot`) · cập nhật dữ liệu `nhom`, `loai`, `active`, `dinh`, `ngay_do` · ghi chú bảng (T0, đặt đầu, giữ chữ cũ).
- **Bảng mới duy nhất:** `balo_tu_dien_nhan` (`id` khoá chính một cột, `nhan`, `gia_tri`, `ten_hien_thi`, `ap_cho`, `thu_tu`, `cau_thu`, `vi_du`; UNIQUE (`nhan`, `gia_tri`)) + quyền đọc cho `directus` và `context_pack_readonly` (đúng hai role đang đọc được `balo_thuc_the`).
- **Không tạo view. Không tạo bảng nào khác.**

**`table_registry`** (chỉ qua DOT ở §1.5, không đọc/ghi trực tiếp)
- dòng mới `tbl_balo_luat` → `/reports/report-balo-luat` và dòng mới `tbl_balo_khoi` → `/reports/report-balo-khoi`, **cả hai là báo cáo `view_sql` sống** qua `dot-report-publish`;
- 4 dòng `tbl_balo_table|view|function|trigger`: **không đổi trong RUN -03**.
- **Không** theo dõi `balo_tu_dien_nhan` trong Directus ở RUN này.

**File trên VPS1**
- `/opt/incomex/dot/sql/balo-nhan-*.sql` + dòng tương ứng trong `/opt/incomex/dot/sql/approved-sql-manifest.tsv`;
- `/opt/incomex/dot/sql/labels/balo-nhan-*.sql` + dòng tương ứng trong `/opt/incomex/dot/sql/labels/approved-label-manifest.tsv`;
- `/opt/incomex/dot/specs/`: chỉ thêm/sửa trong RUN này `balo_luat.spec.json`, `balo_khoi.spec.json` (probe trước, truy vấn cuối sau B1/B6); **không sửa 4 spec balo cũ**;
- hồ sơ `/opt/incomex/work/pg-nhan-balo/` (có `INDEX.md`); baseline lớp bảo vệ cho đúng các vật trên (DROOT29).
- Thư mục mà một DOT ở §1.5 ép buộc (allowlist cứng trong mã DOT) thuộc phạm vi, với điều kiện chỉ thêm file tên `balo-nhan-*` hoặc `balo_*`, không sửa file của việc khác, ghi rõ trong KQ. Không mở rộng phạm vi PG.
- `/opt/incomex/dot` đang có thay đổi chưa commit của việc khác: chỉ commit đúng file của việc này.
- **Không sửa `AGENTS.md` nào trên VPS trong RUN này** (dòng trỏ T1 làm sau G7).

**Repo:** STARTED/KQ + Bảng trong `work/pg-nhan-balo/COLLAB.md`. Q10/T1/T2 giữ OPEN, không xử lý task khác trong RUN này (DROOT37).

## 3. Cấm
- Tắt/bật trigger hoặc cron · DROP/DELETE/TRUNCATE · dời schema · đổi cấu hình PG · restart dịch vụ.
- SQL tay, `psql` trực tiếp, REST admin, kể cả để đọc (DROOT26).
- Ghi bất kỳ giá trị nào vào `ket_luan`, kể cả ghi về trống. Cột này chỉ Owner.
- Suy SỐNG cho view/hàm từ bảng nguồn · điền 0 giả cho DÍNH · dùng bộ đếm cộng dồn khác kỳ thay cho kỳ đo · đoán KHỐI/VAI theo tên.
- Viết thêm nhãn vào `COMMENT ON` của vật khác; sửa/xoá nhãn văn cũ. Chép các dòng luật ra nơi nào ngoài `balo_tu_dien_nhan`.
- Thêm trigger lên `balo_thuc_the`. Lập sổ DOT thứ hai. Chạy `dot-dot-register` chế độ thật. Viết mã Nuxt mới. Sửa `balo-reconcile.sql` hoặc mã của bất kỳ DOT nào. Tìm, dò hay tự nối danh tính/mật khẩu admin Directus.

## 4. Việc, theo thứ tự
- **B0 · Sao lưu và mốc** (bằng N1, lưu vào hồ sơ): toàn bộ dòng balo (đủ cột) · cấu trúc + ràng buộc + quyền + ghi chú hiện có của balo · danh sách trigger bật/tắt · số bảng/view/hàm/trigger · **bộ đếm ghi hiện tại của mọi bảng** (`pg_stat_user_tables`: thêm, sửa, xoá). Không đọc trực tiếp registry bị guard cấm; không sửa 4 spec balo cũ trong RUN này.
- **B1 · Nền và luật.** Thêm 3 cột nhãn. Tạo `balo_tu_dien_nhan`, cấp quyền đọc như §2; nạp đủ giá trị theo `view.html#C1–C6` với mã nhãn ở `#cot`, và **đủ các dòng luật L00–L10 theo `view.html#B1`, không bỏ chữ** (`nhan = 'LUAT'`, chữ luật ở `cau_thu`, `thu_tu` 0–10; các giá trị khác đánh `thu_tu` lớn hơn để luật luôn đứng trước). Chưa bật ràng buộc.
- **B1b · Đọc lại luật qua cửa thật, rồi mới dán.** Đọc L00–L10 và từ điển bằng một file SELECT qua N1, lưu kết quả, so khớp từng chữ với `view.html#B1`. Ghi lại **đúng câu lệnh đã chạy được**: đó là `[lệnh đọc luật]` dùng ở T0 và B3. Không đọc được → DỪNG.
- **B2 · KHỐI** (máy, C1). Bảng/view/hàm: lấy từ nhãn văn cũ của chính vật (`obj_description`, phân tích ngay trong SQL): dòng `HE (so huu):` nếu có, không thì mã đầu của dòng `HE:`; không có hoặc ngoài 23 mã → `CHUA-RO`. Trigger: KHỐI của hàm nó gọi. `chuyen_mon` giữ nguyên.
- **B3 · VAI.** Hàm: giữ 5 giá trị `loai` đang có; hàm trống → theo C3. Bảng: phân loại theo 7 câu thử C2 theo thứ tự; căn cứ là sự thật đo được (cột, khoá ngoại, `pg_depend`, bộ đếm ghi, nguồn nạp), không theo tên; không chắc → `CHUA-RO` + lý do ngắn trong hồ sơ. View và trigger: `x`. Câu UPDATE khoá theo `stt`.
- **B4 · SỐNG** (máy, C4, ghi `ngay_do`). Mốc đầu kỳ = ảnh chụp 01/08 (§5.6). **«P10» Mốc cuối kỳ, chọn một lần cho mọi bảng:** nếu bộ đếm B0 của mọi bảng ≥ ảnh chụp 02/10 13:56Z ở `view.html#bo-dem-0210` (bảng không liệt kê ở đó = 0|0|0) thì cụm PG chưa bị nạp lại ⇒ mốc cuối = B0. Nếu có bảng lùi so với ảnh 02/10 (PG đã nâng bằng dump/restore: bộ đếm về 0 rồi bị chính lượt nạp lại làm bẩn) ⇒ mốc cuối = ảnh chụp 02/10 cho MỌI bảng, kỳ đo = 01/08 10:56Z → 02/10 13:56Z, không dùng bộ đếm hiện tại; bảng sinh sau 02/10 ⇒ `CHUA-RO`. **Tính hiệu ở ngoài PG** (ghép hai tệp theo tên bảng trong shell), rồi sinh câu UPDATE khoá theo `stt`: không đưa tên bảng vào file SQL (§5.1). Chỉ trừ hai mốc khi đủ cả ba: (1) nghĩa cột đúng như §5.6 (tự kiểm lại bằng phép cộng trên vài dòng); (2) bộ đếm liên tục: `stats_reset` không nằm trong kỳ và không bộ đếm ghi nào của bảng bị lùi; (3) bảng có trong ảnh chụp. Thiếu một điều → `CHUA-RO` + lý do trong hồ sơ; (1) hoặc (2) hỏng cho cả ảnh chụp → mọi bảng `CHUA-RO` và ghi vào KQ (không dừng). Số dòng = `count(*)` thật. Ghi **kỳ đo thật** vào hồ sơ và KQ. View, hàm → `Không đo được`. Trigger → `Bật`/`Tắt` theo catalog.
- **B5 · DÍNH** (máy, C5, chỉ trong PG; tên vật lấy từ catalog lúc chạy). Vật có KHỐI `CHUA-RO` → để trống `dinh`. Phần nào không đo được → báo thiếu trong KQ, không lấp bằng 0.
- **B6 · Ràng buộc** (theo `view.html#cot`; «P10» mẫu DDL Host đã chạy thật trên PG 16.15 và 18.4 ở `view.html#ddl-mau`). Thêm 4 cột khoá tự sinh và 4 khoá ngoại tổ hợp sau khi dữ liệu đã hợp lệ. Chứng minh PG từ chối: (a) giá trị lạ; (b) giá trị của nhãn khác; (c) giá trị sai loại vật; và chấp nhận ô trống. Cách thử: file `balo-nhan-thu-am-*.sql` cố ý vi phạm → cổng báo lỗi, giao dịch tự rollback; **rc khác 0 ở các file này là kết quả ĐẠT**.
- **B7 · Dòng trỏ T0.** Mẫu `view.html#T0` vào ghi chú bảng balo qua N3, đặt ở ĐẦU, giữ nguyên chữ cũ bên dưới. B3: mẫu `view.html#B3` ở đầu mỗi file SQL của việc này.
- **B8 · Màn hình.**
  - **B8a · `report-balo-luat`** (bắt buộc): báo cáo `view_sql` sống đọc `balo_tu_dien_nhan`, sắp theo `thu_tu`.
  - **B8b · `report-balo-khoi`** (bắt buộc): báo cáo `view_sql` sống, mỗi khối một dòng (vật chưa dán gom vào dòng “(chưa dán)”): số vật theo loại · số bảng Rỗng / Đứng yên / Tự quay / Có ghi · số `CHUA-RO` · số `Không đo được` · tổng DÍNH · `ket_luan` của khối (một giá trị, “lẫn”, hoặc trống).
  - Với cả hai: `--dry-run` trước, rồi publish; `dot-table-ui-verify` phải PASS; mở được trên browser thật. **Thiếu một trong hai trang thì chưa XONG.**
  - **B8c · KHÔNG LÀM trong RUN -03.** Đổi tên cột/ẩn `Lớp` trên 4 trang balo cần đường admin Directus đã biết chưa sẵn sàng. Giữ nguyên 4 trang/spec cũ, chỉ nghiệm thu không hỏng ở B10; ghi đầu việc OPEN, không thử một đường đã biết dễ thất bại.
- **B9 · ĐỂ OPEN.** Q10 sổ DOT, T1 (`AGENTS.md`) và T2 (KB) không thuộc đường bắt buộc của RUN -03; không đọc/sửa task khác để “bàn giao” hay cập nhật sổ (DROOT37). KQ chỉ ghi chúng còn OPEN.
- **B10 · Làm mới, hồi quy, POST-PROTECT.** Chụp nhãn theo `khoa_nhan_dien` → `dot-balo-reconcile --sync` → chụp lại: không mất/đổi nhãn, không nhân dòng; bảng `balo_tu_dien_nhan` xuất hiện thành dòng mới → dán theo luật (SỐNG=`CHUA-RO` vì sinh sau mốc). SQL dán nhãn chạy lại không đụng `ket_luan`. 4 trang balo cũ + 2 trang mới mở bằng browser thật; `dot-balo-reconcile --verify` PASS. Sau đó chạy POST-PROTECT đúng kế hoạch N6 trên **footprint PRE→POST thật**: D30 regression · D31 integrity/drift · watchdog/self-check · rollback/known-good. POST phải gửi receipt Telegram và lưu `message_id`/delivery proof. Cuối cùng đọc bảng đèn thật bằng đường N6 và ghi `ĐÈN: n xanh · m đỏ`; đèn đỏ thuộc PGNB hoặc thiếu receipt ⇒ chưa XONG.

## 5. Bằng chứng kỹ thuật đã kiểm — tham khảo, không tạo thêm gate
1. `dot-pg-atomic-apply` từ chối mọi file chứa chuỗi `meta_catalog`, `birth_registry`, `table_registry`, `v_registry_`, `qt001_` — **kể cả file chỉ có SELECT, kể cả trong chú thích hay dữ liệu** (RUN -02 dừng vì điều này). ⇒ không file nào của việc này được chứa các chuỗi đó: SQL khoá theo `stt`; tên bảng (nếu cần) do PG lấy từ catalog lúc chạy; cột `vi_du` của từ điển tránh các tên đó; ảnh chụp 01/08 không nạp vào PG (B4 tính ở ngoài). Cổng cũng chặn `DELETE FROM`, `TRUNCATE`, mọi `DROP`, `BEGIN/COMMIT/ROLLBACK/SAVEPOINT` ở đầu câu lệnh (khối `DO $$ … $$` thì được), và dòng bắt đầu bằng `\`.
2. Cổng atomic chặn mọi DROP ⇒ DDL additive không có đường DROP qua cổng. Vì vậy **không được dùng câu “để nguyên là vô hại” làm rollback**. Trước mutation phải PASS N2 TEMP-probe + N6 rollback/known-good; sau mutation phải PASS regression write path cũ và POST-PROTECT. N6 không chấp nhận known-good ⇒ DỪNG trước DDL thật.
3. Cột tự sinh không được tham chiếu cột tự sinh khác: biểu thức khoá tính từ `khoa_nhan_dien`, không từ `loai_census`.
4. `COMMENT ON` ghi đè cả khối ⇒ đọc ghi chú hiện có rồi nối. `dot-pg-label-apply` chỉ nhận câu `COMMENT ON`, từ chối `COMMENT ON TRIGGER`, không nhận khối `DO` hay lệnh `\`.
5. `pg_stat` cộng dồn từ 17/04/2026, Host đo còn liên tục tới 02/10 13:56Z (`stats_reset` trống); «P10» việc nâng PG (G7) có thể chạy trước RUN này: khi đó bộ đếm hiện tại không dùng được cho kỳ này (B4); `n_live_tup` là ước lượng; TRUNCATE không tính vào `n_tup_del`.
6. **Ảnh chụp 01/08** `/opt/incomex/evidence/del1g-20260801/out/snap_directus_0.psv` (352 dòng schema `public`, chụp 2026-08-01T10:56:06Z). 9 trường ngăn bởi `|`: thời điểm · tên bảng · `seq_scan` · `idx_scan` · tổng đọc · **tổng ghi** · `n_tup_ins` · `n_tup_upd` · `n_tup_del` (Host đã kiểm bằng phép cộng trên 5 bảng). Bảng ngoài `public`: `ngoai_0.psv`, 4 trường: thời điểm · `schema.bảng` · tổng đọc · tổng ghi.
7. Với quyền chỉ đọc, `information_schema` không hiện khoá chính/khoá ngoại. Kiểm ràng buộc bằng `pg_constraint`.
8. `balo_thuc_the` do `workflow_admin` (superuser) sở hữu; quyền: `directus` đọc-ghi, `context_pack_readonly` đọc. Cổng đọc của trang Reports chạy bằng role `directus`. Bảng mới không cấp quyền đọc thì trang “Luật nhãn” và đầu nối chỉ-đọc không đọc được.
9. `dot-report-publish`: `view_sql` là đúng một câu SELECT/WITH, không có `;` ở giữa, bị từ chối nếu chứa nguyên từ `insert`, `update`, `delete`, `drop`, `alter`, `create`, `truncate`, `grant`, `revoke`, `copy`, `call`, `do`. `dot-table-ui-verify` so từng giá trị API với PG: **đừng đặt cột tên `total` hay `refreshed_at`** (hai tên này kéo theo phép kiểm riêng của trang PG Census). «P10» Cột đầu phải là `stt` duy nhất, các cột khác tên từ 4 ký tự, không trả cột kiểu `date` (lý do ở N4).
10. Event trigger `evt_trigger_guard_ddl` bật cho `ALTER TABLE` nhưng chỉ ghi cảnh báo khi vật là trigger. Vẫn so `trigger_guard_alerts` trước/sau.
11. `dot-collection-track-readonly` (bên trong `dot-list-publish`) lấy token admin Directus từ biến môi trường hoặc tự đăng nhập bằng thông tin của container Directus; trên production đường này đang hỏng (mật khẩu rỗng). Chỉ B8c dùng tới.

## 6. Xong khi (thiếu một điều là chưa XONG)
- Mọi dòng `da_mat = false` tại lúc chạy: `nhom`, `loai`, `active` không trống; `dinh` chỉ trống khi KHỐI là `CHUA-RO`.
- `ket_luan`: không dòng nào bị RUN này ghi (so với B0).
- PG từ chối giá trị lạ, sai nhãn, sai loại vật (có bằng chứng).
- Đọc được L00–L10 qua cửa DOT (B1b) và trên trang `report-balo-luat`; ghi chú bảng balo có dòng trỏ ở đầu, chữ cũ còn nguyên.
- Có đủ hai trang `report-balo-khoi` và `report-balo-luat`, mở được, đúng dữ liệu.
- `--sync` không làm mất nhãn, không nhân dòng (B10). 4 trang balo cũ không hỏng.
- Danh sách trigger bật/tắt và số view/hàm/trigger không đổi so với B0; số bảng tăng đúng 1. «P10» “Trigger” ở đây và ở B0 = trigger người dùng (`NOT tgisinternal`, đúng cách đếm của `balo-reconcile.sql`); 4 khoá ngoại sinh 16 trigger nội bộ của PG trên hai bảng, không tính.
- Đổi tên cột/ẩn `Lớp`, Q10 sổ DOT, T1, T2 còn OPEN theo chủ ý và không chặn XONG phần dán nhãn; KQ ghi rõ, nhưng RUN -03 không thử/sửa các phần này.
- POST-PROTECT DROOT29 PASS trên footprint thật, có Telegram receipt `message_id`/delivery proof; bảng đèn DROOT34 đã đọc thật và không có đèn đỏ thuộc PGNB.

## 7. KQ
Ghi vào `work/pg-nhan-balo/COLLAB.md` một khối ngắn `KQ@PGNB-LABEL-20261002-03 XONG|DỪNG` (kèm sửa ■/➡/`cập nhật` của Bảng):
- preflight tối thiểu: từng cổng PASS/FAIL + lệnh/output thật; nếu FAIL phải là danh sách đầy đủ trong một lần;
- số vật đã dán đủ · **báo riêng** số `CHUA-RO` theo từng nhãn và số `Không đo được`; kỳ đo thật của SỐNG;
- các khối cần rà (toàn rỗng / đứng yên / tự quay) — là dấu hiệu, không phải kết luận;
- các đầu việc deferred: đổi tên cột/ẩn `Lớp`, Q10, T1, T2;
- footprint thật của PGNB: delta cấu trúc (+1 bảng, +7 cột, +4 FK), dữ liệu nhãn, 2 report mới, file đã tạo/sửa (path + sha256). Nếu việc khác cần biết thì chỉ ghi một con trỏ `→ việc vps1-up-grade: đọc KQ PGNB`, không điều hành/bàn giao thay task khác (DROOT37);
- POST-PROTECT: PRE/POST evidence · rollback/known-good · Telegram receipt `message_id` · `ĐÈN: n xanh · m đỏ`; blocker cần Owner · đường dẫn hồ sơ.
Trả Owner đúng một dòng `XONG` hoặc `DỪNG`.

## 8. Lùi lại
| Phần | Lùi bằng |
|---|---|
| Giá trị nhãn (`nhom`, `loai`, `active`, `dinh`, `ngay_do`) | file SQL sinh từ bản B0, chạy qua cổng |
| Ghi chú bảng balo | `dot-pg-label-apply` với chữ cũ ở B0 |
| 2 trang mới | publish lại với trạng thái không hiện nếu khuôn cho phép; không xoá |
| 4 trang balo | RUN -03 không sửa, nên không có bước lùi |
| Cột, FK, bảng mới | Không có DROP qua cổng. **Known-good bắt buộc:** chỉ được áp sau N2 TEMP-probe + N6 PASS; B10 phải chứng minh các write path cũ/reconcile vẫn đạt và POST-PROTECT chấp nhận coverage. Nếu N6 yêu cầu rollback vật lý mà không có DOT hợp lệ thì cấm mutation, không dùng “để nguyên” thay rollback. |
