# PROMPT — pg-nhan-balo
RUN_ID: PGNB-LABEL-20261002-03
Bản lệnh: v4 · 03/10/2026 · sửa theo KQ DỪNG của RUN -01 và -02 (COLLAB P08). Luật, 5 nhãn, phạm vi cột/bảng PG không đổi. Đổi: cách kiểm trước khi làm, cách dựng hai trang, bỏ ba phần phụ thuộc không chắc.
Executor_Surface: Codex
Write_Path: repo = cổng `workspace_*` (hoặc `fs_*` nếu bề mặt bind được) · VPS1 = chỉ qua các DOT ở §1.5
Trạng thái: chỉ chạy khi `COLLAB.md` có `READY@<sha>` trùng commit cuối chạm file này, và Owner đã RUN.

## 0. Một câu
Đặt luật nhãn lên hiện trường và dán 4 nhãn đầu cho mọi vật còn tồn tại trong `balo_thuc_the` (VPS1, database `directus`). **Chỉ dán nhãn.** Không tắt, không xoá, không dời, không đổi cấu hình PG. Đích: Owner mở trang “Balo theo khối”, 30 giây là biết khối nào cần rà.

**Cách chạy lượt này: thử hết rồi mới quyết, không dừng ở lỗi đầu tiên** (§1.5–§1.6). Mục tiêu là chạy tới KQ trong một RUN.

## 1. Read-gate (trước mọi thay đổi production)
1. Đọc `AGENTS.md` → `work/pg-nhan-balo/COLLAB.md` (§0, Bảng, D01–D11, P01–P09, KQ của RUN -01 và -02) → file này → `view.html`: `#C` (từ điển + câu thử), `#bien` (vị trí, mẫu B1/T0/B3), `#cot` (cột + khoá nhãn), `#so-dot`. **Luật nằm ở `view.html`; file này không chép lại luật.** Trước khi bảng luật tồn tại trong PG, `view.html` là bản luật để làm.
2. `READY@` trong COLLAB = commit cuối chạm `PROMPT.md`. Lệch → DỪNG.
3. Ghi `STARTED@PGNB-LABEL-20261002-03 <UTC> · executor=Codex` vào COLLAB + sửa dòng ■/➡/`cập nhật` của Bảng (MT4, DROOT31).
4. **Cờ nâng PG:** đọc Bảng của `work/vps1-up-grade/COLLAB.md`. G7 đang STARTED mà chưa KQ, hoặc có HOLD/STOP cho VPS1 → DỪNG, không đụng VPS1. **Kiểm lại cờ này và READY/HOLD của chính việc này ngay trước lệnh đổi production đầu tiên và trước mỗi nhóm lệnh đổi sau một khoảng chờ (DROOT30).**
5. **Bảng năng lực — thử thật MỌI dòng, gom kết quả, rồi mới quyết.** “Đổi production” = làm đổi PG, Directus, `table_registry` hoặc runtime. Tạo file SQL/spec và thêm dòng manifest trong phạm vi §2 để thử **không** tính là đổi production. File cũ của RUN -02 (`balo-nhan-doc-registry.sql`) để nguyên làm bằng chứng, không dùng.

| # | Cần | Dùng (Host đã đối chiếu mã DOT 03/10) | Phép thử trước khi đổi production | Bắt buộc? |
|---|---|---|---|---|
| N1 | Đọc PG | `dot-pg-atomic-apply <file.sql>` với file chỉ có SELECT (một tham số; file dưới `/opt/incomex/dot/sql/`; có dòng sha256 trong `approved-sql-manifest.tsv`; chạy bằng role `workflow_admin`) | chạy thật một file đọc, ví dụ đếm balo theo `loai_census`; phải in kết quả | CÓ |
| N2 | Ghi cấu trúc + dữ liệu | cùng cổng | soạn trước các file của B1 và B6 (kể cả file thử âm), thêm manifest, chạy với `PG_CONTAINER=__pgnb_validation_never__` → phải qua đường dẫn/hash/guardrail rồi dừng ở preflight rc=3 | CÓ |
| N3 | Ghi chú bảng balo | `dot-pg-label-apply [--check] <file.sql>`; file dưới `/opt/incomex/dot/sql/labels/`; dòng trong `approved-label-manifest.tsv` (công cụ không tự thêm) | `--check` trên file T0 (soạn sau khi đọc ghi chú hiện có bằng N1) | CÓ |
| N4 | Hai trang báo cáo sống | `dot-report-publish --spec-file <json> [--dry-run]` (v2: ghi `table_registry`, không cần đăng nhập Directus; tự gọi `dot-table-ui-verify`); spec ở `/opt/incomex/dot/specs/` | `dot-table-ui-verify --table-id tbl_report_pg` (trang đang có) phải PASS | CÓ |
| N5 | Làm mới balo | `dot-balo-reconcile --verify` / `--sync` | `--verify` PASS | CÓ |
| N6 | Lớp bảo vệ + đèn | cơ chế DROOT29 / DROOT34 đang có | xác định được lệnh sẽ dùng | theo luật gốc |
| N7 | Đổi tên cột 4 trang balo | `dot-list-publish --spec-file <json>` (gọi `dot-collection-track-readonly`, **cần đăng nhập admin Directus**; `--dry-run` thoát trước bước đăng nhập nên không chứng minh được gì) | không thử trước; làm cuối cùng ở B8c | KHÔNG |

6. **Quy tắc quyết định**
   - Thử đủ N1–N6 dù có dòng hỏng. Mọi dòng “CÓ” đạt → **chạy tiếp ngay, không hỏi lại**. Có dòng “CÓ” hỏng → DỪNG **một lần** với danh sách đầy đủ mọi dòng hỏng + lệnh + output thật.
   - Guard từ chối file vì chuỗi cấm (§5.1): viết lại câu SQL để không nêu tên vật (lọc theo `stt`, hoặc để PG tự lấy tên từ catalog lúc chạy). RUN này **không cần đọc hay ghi trực tiếp** bảng nào thuộc danh sách cấm; nếu thấy cần → bước đó sai thiết kế: bỏ nếu không bắt buộc, DỪNG nếu bắt buộc. Không nới guard, không dùng mẹo ghép chuỗi để nhắm vào các bảng đó.
   - Sau khi đã đổi production: mỗi file SQL là một giao dịch. Lỗi ở bước bắt buộc → dừng tại đó, **không tự lùi**, KQ ghi rõ bước nào đã xong, bước nào chưa. Lỗi ở bước không bắt buộc (B8c, B9) → bỏ qua, ghi vào KQ, làm tiếp.
   - Thiếu năng lực thật → không làm tay, không viết DOT mới, không sửa mã DOT trong RUN này.

## 2. Được đổi — danh sách đóng
**PostgreSQL `directus.public`**
- `balo_thuc_the`: +3 cột nhãn `dinh integer`, `ket_luan varchar`, `ngay_do date` · +4 cột khoá tự sinh (STORED) `k_khoi`, `k_vai`, `k_song`, `k_ketluan` · +4 khoá ngoại tổ hợp sang từ điển (theo `view.html#cot`) · cập nhật dữ liệu `nhom`, `loai`, `active`, `dinh`, `ngay_do` · ghi chú bảng (T0, đặt đầu, giữ chữ cũ).
- **Bảng mới duy nhất:** `balo_tu_dien_nhan` (`id` khoá chính một cột, `nhan`, `gia_tri`, `ten_hien_thi`, `ap_cho`, `thu_tu`, `cau_thu`, `vi_du`; UNIQUE (`nhan`, `gia_tri`)) + quyền đọc cho `directus` và `context_pack_readonly` (đúng hai role đang đọc được `balo_thuc_the`).
- **Không tạo view. Không tạo bảng nào khác.**

**`table_registry`** (chỉ qua DOT ở §1.5, không đọc/ghi trực tiếp)
- dòng mới `tbl_balo_luat` → `/reports/report-balo-luat` và dòng mới `tbl_balo_khoi` → `/reports/report-balo-khoi`, **cả hai là báo cáo `view_sql` sống** qua `dot-report-publish`;
- 4 dòng `tbl_balo_table|view|function|trigger`: chỉ đổi nếu B8c làm được.
- **Không** theo dõi `balo_tu_dien_nhan` trong Directus ở RUN này.

**File trên VPS1**
- `/opt/incomex/dot/sql/balo-nhan-*.sql` + dòng tương ứng trong `/opt/incomex/dot/sql/approved-sql-manifest.tsv`;
- `/opt/incomex/dot/sql/labels/balo-nhan-*.sql` + dòng tương ứng trong `/opt/incomex/dot/sql/labels/approved-label-manifest.tsv`;
- `/opt/incomex/dot/specs/`: thêm `balo_luat.spec.json`, `balo_khoi.spec.json`; sửa 4 file `balo_{table,view,function,trigger}.spec.json` chỉ trong B8c;
- hồ sơ `/opt/incomex/work/pg-nhan-balo/` (có `INDEX.md`); baseline lớp bảo vệ cho đúng các vật trên (DROOT29).
- Thư mục mà một DOT ở §1.5 ép buộc (allowlist cứng trong mã DOT) thuộc phạm vi, với điều kiện chỉ thêm file tên `balo-nhan-*` hoặc `balo_*`, không sửa file của việc khác, ghi rõ trong KQ. Không mở rộng phạm vi PG.
- `/opt/incomex/dot` đang có thay đổi chưa commit của việc khác: chỉ commit đúng file của việc này.
- **Không sửa `AGENTS.md` nào trên VPS trong RUN này** (dòng trỏ T1 làm sau G7).

**Repo:** STARTED/KQ + Bảng + trả lời Q10 trong `work/pg-nhan-balo/COLLAB.md`.

## 3. Cấm
- Tắt/bật trigger hoặc cron · DROP/DELETE/TRUNCATE · dời schema · đổi cấu hình PG · restart dịch vụ.
- SQL tay, `psql` trực tiếp, REST admin, kể cả để đọc (DROOT26).
- Ghi bất kỳ giá trị nào vào `ket_luan`, kể cả ghi về trống. Cột này chỉ Owner.
- Suy SỐNG cho view/hàm từ bảng nguồn · điền 0 giả cho DÍNH · dùng bộ đếm cộng dồn khác kỳ thay cho kỳ đo · đoán KHỐI/VAI theo tên.
- Viết thêm nhãn vào `COMMENT ON` của vật khác; sửa/xoá nhãn văn cũ. Chép các dòng luật ra nơi nào ngoài `balo_tu_dien_nhan`.
- Thêm trigger lên `balo_thuc_the`. Lập sổ DOT thứ hai. Chạy `dot-dot-register` chế độ thật. Viết mã Nuxt mới. Sửa `balo-reconcile.sql` hoặc mã của bất kỳ DOT nào. Tìm, dò hay tự nối danh tính/mật khẩu admin Directus.

## 4. Việc, theo thứ tự
- **B0 · Sao lưu và mốc** (bằng N1, lưu vào hồ sơ): toàn bộ dòng balo (đủ cột) · cấu trúc + ràng buộc + quyền + ghi chú hiện có của balo · danh sách trigger bật/tắt · số bảng/view/hàm/trigger · **bộ đếm ghi hiện tại của mọi bảng** (`pg_stat_user_tables`: thêm, sửa, xoá) · bản hiện tại của 4 file spec balo. Không sao lưu dòng `table_registry` (RUN này chỉ thêm 2 dòng mới qua DOT; 4 dòng cũ lùi bằng cách publish lại spec cũ).
- **B1 · Nền và luật.** Thêm 3 cột nhãn. Tạo `balo_tu_dien_nhan`, cấp quyền đọc như §2; nạp đủ giá trị theo `view.html#C1–C6` với mã nhãn ở `#cot`, và **đủ các dòng luật L00–L10 theo `view.html#B1`, không bỏ chữ** (`nhan = 'LUAT'`, chữ luật ở `cau_thu`, `thu_tu` 0–10; các giá trị khác đánh `thu_tu` lớn hơn để luật luôn đứng trước). Chưa bật ràng buộc.
- **B1b · Đọc lại luật qua cửa thật, rồi mới dán.** Đọc L00–L10 và từ điển bằng một file SELECT qua N1, lưu kết quả, so khớp từng chữ với `view.html#B1`. Ghi lại **đúng câu lệnh đã chạy được**: đó là `[lệnh đọc luật]` dùng ở T0 và B3. Không đọc được → DỪNG.
- **B2 · KHỐI** (máy, C1). Bảng/view/hàm: lấy từ nhãn văn cũ của chính vật (`obj_description`, phân tích ngay trong SQL): dòng `HE (so huu):` nếu có, không thì mã đầu của dòng `HE:`; không có hoặc ngoài 23 mã → `CHUA-RO`. Trigger: KHỐI của hàm nó gọi. `chuyen_mon` giữ nguyên.
- **B3 · VAI.** Hàm: giữ 5 giá trị `loai` đang có; hàm trống → theo C3. Bảng: phân loại theo 7 câu thử C2 theo thứ tự; căn cứ là sự thật đo được (cột, khoá ngoại, `pg_depend`, bộ đếm ghi, nguồn nạp), không theo tên; không chắc → `CHUA-RO` + lý do ngắn trong hồ sơ. View và trigger: `x`. Câu UPDATE khoá theo `stt`.
- **B4 · SỐNG** (máy, C4, ghi `ngay_do`). Mốc đầu kỳ = ảnh chụp 01/08 (§5.6); mốc cuối kỳ = bộ đếm lưu ở B0. **Tính hiệu ở ngoài PG** (ghép hai tệp theo tên bảng trong shell), rồi sinh câu UPDATE khoá theo `stt`: không đưa tên bảng vào file SQL (§5.1). Chỉ trừ hai mốc khi đủ cả ba: (1) nghĩa cột đúng như §5.6 (tự kiểm lại bằng phép cộng trên vài dòng); (2) bộ đếm liên tục: `stats_reset` không nằm trong kỳ và không bộ đếm ghi nào của bảng bị lùi; (3) bảng có trong ảnh chụp. Thiếu một điều → `CHUA-RO` + lý do trong hồ sơ; (1) hoặc (2) hỏng cho cả ảnh chụp → mọi bảng `CHUA-RO` và ghi vào KQ (không dừng). Số dòng = `count(*)` thật. Ghi **kỳ đo thật** vào hồ sơ và KQ. View, hàm → `Không đo được`. Trigger → `Bật`/`Tắt` theo catalog.
- **B5 · DÍNH** (máy, C5, chỉ trong PG; tên vật lấy từ catalog lúc chạy). Vật có KHỐI `CHUA-RO` → để trống `dinh`. Phần nào không đo được → báo thiếu trong KQ, không lấp bằng 0.
- **B6 · Ràng buộc** (theo `view.html#cot`). Thêm 4 cột khoá tự sinh và 4 khoá ngoại tổ hợp sau khi dữ liệu đã hợp lệ. Chứng minh PG từ chối: (a) giá trị lạ; (b) giá trị của nhãn khác; (c) giá trị sai loại vật; và chấp nhận ô trống. Cách thử: file `balo-nhan-thu-am-*.sql` cố ý vi phạm → cổng báo lỗi, giao dịch tự rollback; **rc khác 0 ở các file này là kết quả ĐẠT**.
- **B7 · Dòng trỏ T0.** Mẫu `view.html#T0` vào ghi chú bảng balo qua N3, đặt ở ĐẦU, giữ nguyên chữ cũ bên dưới. B3: mẫu `view.html#B3` ở đầu mỗi file SQL của việc này.
- **B8 · Màn hình.**
  - **B8a · `report-balo-luat`** (bắt buộc): báo cáo `view_sql` sống đọc `balo_tu_dien_nhan`, sắp theo `thu_tu`.
  - **B8b · `report-balo-khoi`** (bắt buộc): báo cáo `view_sql` sống, mỗi khối một dòng (vật chưa dán gom vào dòng “(chưa dán)”): số vật theo loại · số bảng Rỗng / Đứng yên / Tự quay / Có ghi · số `CHUA-RO` · số `Không đo được` · tổng DÍNH · `ket_luan` của khối (một giá trị, “lẫn”, hoặc trống).
  - Với cả hai: `--dry-run` trước, rồi publish; `dot-table-ui-verify` phải PASS; mở được trên browser thật. **Thiếu một trong hai trang thì chưa XONG.**
  - **B8c · Đổi tên cột 4 trang balo** (không bắt buộc, làm sau cùng): sửa 4 spec để cột hiện theo thứ tự ID · Tên · Nơi lưu · Khối (`nhom`) · Vai (`loai`) · Sống (`active`) · Dính (`dinh`) · Kết luận (`ket_luan`) · Ngày đo (`ngay_do`) · Chuyên môn · Kiểm soát · Mô tả (`ghi_chu`) · Đã mất; bỏ cột Lớp khỏi màn; mỗi cột nhãn thêm `description` trỏ về “Reports › Luật nhãn”; rồi `dot-list-publish`. **Nếu lệnh hỏng ở bước đăng nhập admin Directus (đã biết đang hỏng trên production, xem việc `vps1-up-grade`) hoặc vì lý do khác: trả 4 file spec về bản cũ, ghi gap vào KQ, không dừng RUN.**
- **B9 · Sổ DOT (Q10)** (không bắt buộc): tìm đúng một sổ thật do việc `vps1-up-grade` lập; đọc được → ghi đường dẫn/cột/từ vựng/quan hệ với `dot_tools` vào COLLAB và thêm dòng cho các file mới theo đúng khuôn sổ; không thấy hoặc chỉ có trên máy lab → giữ OPEN, không lập sổ khác. T1 (dòng trỏ trong `AGENTS.md`) và T2 (KB): không làm ở RUN này.
- **B10 · Làm mới, hồi quy, bảo vệ.** Chụp nhãn theo `khoa_nhan_dien` → chạy `dot-balo-reconcile --sync` (đúng lệnh mà nút Làm mới gọi; bấm thêm nút trên web nếu làm được, không bắt buộc) → chụp lại: không nhãn nào mất hay đổi, không nhân dòng; bảng `balo_tu_dien_nhan` xuất hiện thành dòng mới → dán nhãn cho nó theo luật (sinh sau mốc đo thì SỐNG = `CHUA-RO`). Các file SQL dán nhãn chạy lại được mà không đụng `ket_luan`. 4 trang balo cũ + 2 trang mới mở được trên browser thật; `dot-balo-reconcile --verify` PASS; lớp bảo vệ (DROOT29); đọc bảng đèn (DROOT34).

## 5. Bẫy đã biết (Host đã đối chiếu mã và số liệu thật)
1. `dot-pg-atomic-apply` từ chối mọi file chứa chuỗi `meta_catalog`, `birth_registry`, `table_registry`, `v_registry_`, `qt001_` — **kể cả file chỉ có SELECT, kể cả trong chú thích hay dữ liệu** (RUN -02 dừng vì điều này). ⇒ không file nào của việc này được chứa các chuỗi đó: SQL khoá theo `stt`; tên bảng (nếu cần) do PG lấy từ catalog lúc chạy; cột `vi_du` của từ điển tránh các tên đó; ảnh chụp 01/08 không nạp vào PG (B4 tính ở ngoài). Cổng cũng chặn `DELETE FROM`, `TRUNCATE`, mọi `DROP`, `BEGIN/COMMIT/ROLLBACK/SAVEPOINT` ở đầu câu lệnh (khối `DO $$ … $$` thì được), và dòng bắt đầu bằng `\`.
2. Cổng atomic chặn mọi DROP ⇒ cột, khoá ngoại, bảng mới **không lùi được qua cổng**: thử kỹ rồi mới áp (§8).
3. Cột tự sinh không được tham chiếu cột tự sinh khác: biểu thức khoá tính từ `khoa_nhan_dien`, không từ `loai_census`.
4. `COMMENT ON` ghi đè cả khối ⇒ đọc ghi chú hiện có rồi nối. `dot-pg-label-apply` chỉ nhận câu `COMMENT ON`, từ chối `COMMENT ON TRIGGER`, không nhận khối `DO` hay lệnh `\`.
5. `pg_stat` cộng dồn từ 17/04/2026, còn liên tục tới 03/10 (`stats_reset` trống); `n_live_tup` là ước lượng; TRUNCATE không tính vào `n_tup_del`.
6. **Ảnh chụp 01/08** `/opt/incomex/evidence/del1g-20260801/out/snap_directus_0.psv` (352 dòng schema `public`, chụp 2026-08-01T10:56:06Z). 9 trường ngăn bởi `|`: thời điểm · tên bảng · `seq_scan` · `idx_scan` · tổng đọc · **tổng ghi** · `n_tup_ins` · `n_tup_upd` · `n_tup_del` (Host đã kiểm bằng phép cộng trên 5 bảng). Bảng ngoài `public`: `ngoai_0.psv`, 4 trường: thời điểm · `schema.bảng` · tổng đọc · tổng ghi.
7. Với quyền chỉ đọc, `information_schema` không hiện khoá chính/khoá ngoại. Kiểm ràng buộc bằng `pg_constraint`.
8. `balo_thuc_the` do `workflow_admin` (superuser) sở hữu; quyền: `directus` đọc-ghi, `context_pack_readonly` đọc. Cổng đọc của trang Reports chạy bằng role `directus`. Bảng mới không cấp quyền đọc thì trang “Luật nhãn” và đầu nối chỉ-đọc không đọc được.
9. `dot-report-publish`: `view_sql` là đúng một câu SELECT/WITH, không có `;` ở giữa, bị từ chối nếu chứa nguyên từ `insert`, `update`, `delete`, `drop`, `alter`, `create`, `truncate`, `grant`, `revoke`, `copy`, `call`, `do`. `dot-table-ui-verify` so từng giá trị API với PG: **đừng đặt cột tên `total` hay `refreshed_at`** (hai tên này kéo theo phép kiểm riêng của trang PG Census).
10. Event trigger `evt_trigger_guard_ddl` bật cho `ALTER TABLE` nhưng chỉ ghi cảnh báo khi vật là trigger. Vẫn so `trigger_guard_alerts` trước/sau.
11. `dot-collection-track-readonly` (bên trong `dot-list-publish`) lấy token admin Directus từ biến môi trường hoặc tự đăng nhập bằng thông tin của container Directus; trên production đường này đang hỏng (mật khẩu rỗng). Chỉ B8c dùng tới.

## 6. Xong khi (thiếu một điều là chưa XONG)
- Mọi dòng `da_mat = false` tại lúc chạy: `nhom`, `loai`, `active` không trống; `dinh` chỉ trống khi KHỐI là `CHUA-RO`.
- `ket_luan`: không dòng nào bị RUN này ghi (so với B0).
- PG từ chối giá trị lạ, sai nhãn, sai loại vật (có bằng chứng).
- Đọc được L00–L10 qua cửa DOT (B1b) và trên trang `report-balo-luat`; ghi chú bảng balo có dòng trỏ ở đầu, chữ cũ còn nguyên.
- Có đủ hai trang `report-balo-khoi` và `report-balo-luat`, mở được, đúng dữ liệu.
- `--sync` không làm mất nhãn, không nhân dòng (B10). 4 trang balo cũ không hỏng.
- Danh sách trigger bật/tắt và số view/hàm/trigger không đổi so với B0; số bảng tăng đúng 1.
- B8c, sổ DOT (Q10), T1, T2 có thể còn OPEN mà không chặn XONG; KQ phải ghi rõ từng mục còn mở.

## 7. KQ
Ghi vào `work/pg-nhan-balo/COLLAB.md` một khối ngắn `KQ@PGNB-LABEL-20261002-03 XONG|DỪNG` (kèm sửa ■/➡/`cập nhật` của Bảng):
- bảng N1–N7: từng dòng ĐẠT/HỎNG + lệnh + output thật;
- số vật đã dán đủ · **báo riêng** số `CHUA-RO` theo từng nhãn và số `Không đo được`; kỳ đo thật của SỐNG;
- các khối cần rà (toàn rỗng / đứng yên / tự quay) — là dấu hiệu, không phải kết luận;
- B8c làm được hay bỏ; sổ DOT đọc được hay chưa;
- **bàn giao cho việc `vps1-up-grade` (trước G7):** delta cấu trúc (+1 bảng, +7 cột, +4 khoá ngoại), dữ liệu nhãn, 2 dòng `table_registry` mới, danh sách đủ file đã tạo/sửa trên VPS1 (đường dẫn + sha256); lưu ý sau khi nâng PG bộ đếm về 0 nên lần đo SỐNG sau phải lấy mốc mới;
- blocker cần Owner · `ĐÈN: n xanh · m đỏ` · đường dẫn hồ sơ.
Trả Owner đúng một dòng `XONG` hoặc `DỪNG`.

## 8. Lùi lại
| Phần | Lùi bằng |
|---|---|
| Giá trị nhãn (`nhom`, `loai`, `active`, `dinh`, `ngay_do`) | file SQL sinh từ bản B0, chạy qua cổng |
| Ghi chú bảng balo | `dot-pg-label-apply` với chữ cũ ở B0 |
| 2 trang mới | publish lại với trạng thái không hiện nếu khuôn cho phép; không xoá |
| 4 trang balo (nếu B8c đã làm) | publish lại 4 spec cũ ở B0 |
| Cột, khoá ngoại, bảng mới | **không lùi được qua cổng** (cổng chặn DROP): để nguyên, vô hại vì chỉ thêm và ô trống hợp lệ; nếu khoá ngoại gây lỗi ghi → DỪNG, báo Host, không tự gỡ |
