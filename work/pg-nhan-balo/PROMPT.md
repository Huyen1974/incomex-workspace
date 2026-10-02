# PROMPT — pg-nhan-balo
RUN_ID: PGNB-LABEL-20261002-02
Bản lệnh: v3 · 02/10/2026 · = v2 (đã áp P03-F1–F6, P05 duyệt) + sửa đường dẫn file theo KQ DỪNG của RUN -01 (COLLAB P06). Luật, nhãn, phạm vi PG/Directus không đổi.
Executor_Surface: Codex
Write_Path: repo = cổng `workspace_*` (hoặc `fs_*` nếu bề mặt bind được) · VPS1 = chỉ qua DOT/khuôn sẵn có theo bảng năng lực §1.5
Trạng thái: chỉ chạy khi `COLLAB.md` có `READY@<sha>` trùng commit cuối chạm file này, và Owner đã RUN.

## 0. Một câu
Đặt luật nhãn lên hiện trường và dán 4 nhãn đầu cho mọi vật còn tồn tại trong `balo_thuc_the` (VPS1, database `directus`). **Chỉ dán nhãn.** Không tắt, không xoá, không dời, không đổi cấu hình PG. Đích: Owner mở trang “Balo theo khối”, 30 giây là biết khối nào cần rà.

Một RUN trọn gói: trong phạm vi §2, tự làm liên tục, tự sửa và kiểm lại. Chỉ dừng khi vượt phạm vi, thiếu năng lực, hoặc gặp điều kiện DỪNG.

## 1. Read-gate (trước mọi thay đổi production)
1. Đọc `AGENTS.md` → `work/pg-nhan-balo/COLLAB.md` (§0, Bảng, D01–D10, P01–P07, KQ của RUN -01) → file này → `view.html`: `#C` (từ điển + câu thử), `#bien` (vị trí, mẫu B1/T0/B3), `#cot` (cột + khoá nhãn), `#so-dot`. **Luật nằm ở `view.html`; file này không chép lại luật.** Trước khi bảng luật tồn tại trong PG, `view.html` là bản luật để làm.
2. `READY@` trong COLLAB = commit cuối chạm `PROMPT.md`. Lệch → DỪNG.
3. Ghi `STARTED@PGNB-LABEL-20261002-02 <UTC> · executor=Codex` vào COLLAB + sửa dòng ■/➡/`cập nhật` của Bảng (MT4, DROOT31).
4. **Cờ nâng PG:** đọc Bảng của `work/vps1-up-grade/COLLAB.md`. G7 đã STARTED mà chưa KQ, hoặc có HOLD/STOP cho VPS1 → DỪNG, không đụng VPS1. **Kiểm lại cờ này và READY/HOLD của chính việc này ngay trước lệnh đổi production đầu tiên và trước mỗi nhóm lệnh đổi sau một khoảng chờ (DROOT30).**
5. **Bảng năng lực — thử thật từng dòng trước lệnh đổi production đầu tiên.** “Đổi production” = làm đổi PG, Directus, `table_registry`, runtime hoặc 3 `AGENTS.md`. Tạo file SQL/spec và thêm dòng manifest trong phạm vi §2 để thử guard **không** tính là đổi production. Thiếu năng lực thật → DỪNG trước khi đổi, báo đúng một dòng `THIẾU NĂNG LỰC: <gì>`; Host quyết theo R3. Không làm tay, không nới guardrail, không viết DOT mới trong RUN này.

| Cần | Dùng (đã đối chiếu mã DOT 02/10) | Cách thử không đổi production |
|---|---|---|
| Ghi cấu trúc + dữ liệu, và **đọc PG** | `dot-pg-atomic-apply <file.sql>` — đúng một tham số, không có `--check`/`--help`. File phải nằm dưới `/opt/incomex/dot/sql/` và có dòng sha256 trong `/opt/incomex/dot/sql/approved-sql-manifest.tsv`. File chỉ có SELECT cũng chạy qua cổng này. | Cách RUN -01 đã dùng: `PG_CONTAINER=__pgnb_validation_never__` → qua đường dẫn/hash/guardrail rồi dừng ở preflight (rc=3). Áp cho chính các file `balo-nhan-*.sql` để chứng minh guard nhận `ADD COLUMN … GENERATED ALWAYS AS (…) STORED`, `ADD CONSTRAINT … FOREIGN KEY`, `CREATE TABLE`, `GRANT`, `INSERT`, `UPDATE`. |
| Ghi chú bảng | `dot-pg-label-apply [--check] <file.sql>` — file phải nằm dưới `/opt/incomex/dot/sql/labels/`, có dòng trong `/opt/incomex/dot/sql/labels/approved-label-manifest.tsv`; công cụ không tự thêm dòng manifest. | `--check` |
| Theo dõi bảng mới + trang danh sách sống | `dot-list-publish --spec-file <json> [--dry-run]` (tự gọi `dot-collection-track-readonly` và `dot-table-ui-verify`); spec ở `/opt/incomex/dot/specs/` | `--dry-run` |
| Trang báo cáo tính sống | `dot-report-publish --spec-file <json> [--dry-run] [--verify-only]` (v2, `view_sql` sống); spec ở `/opt/incomex/dot/specs/` | `--dry-run` |
| Kiểm trang | `dot-table-ui-verify` + browser thật | chạy với một trang balo đang có |
| Làm mới balo | `dot-balo-reconcile --verify` / `--sync` + nút trên web | `--verify` (RUN -01 đã PASS) |
| Sửa 3 `AGENTS.md` | tài liệu, không phải runtime: sửa bằng công cụ repo chuẩn tại chỗ, đúng một dòng | xem được diff 1 dòng |

6. Đọc thực tế rồi ghi lại chỗ lệch với file này: cột + ràng buộc + quyền hiện có của balo; `balo-reconcile.sql`; 6 dòng `table_registry` liên quan; sổ DOT (B9). Lệch làm đổi **phạm vi PG/Directus** ở §2 → DỪNG.

## 2. Được đổi — danh sách đóng (ngoài danh sách = DỪNG)
**PostgreSQL `directus.public`**
- `balo_thuc_the`: +3 cột nhãn `dinh integer`, `ket_luan varchar`, `ngay_do date` · +4 cột khoá tự sinh (STORED) `k_khoi`, `k_vai`, `k_song`, `k_ketluan` · +4 khoá ngoại tổ hợp sang từ điển (theo `view.html#cot`) · cập nhật dữ liệu `nhom`, `loai`, `active`, `dinh`, `ngay_do` · ghi chú bảng (T0, đặt đầu, giữ chữ cũ).
- **Bảng mới duy nhất:** `balo_tu_dien_nhan` (`id` khoá chính một cột, `nhan`, `gia_tri`, `ten_hien_thi`, `ap_cho`, `thu_tu`, `cau_thu`, `vi_du`; UNIQUE (`nhan`, `gia_tri`)) + quyền đọc cho đúng các role đang được đọc `balo_thuc_the`.
- **Không tạo view. Không tạo bảng nào khác.**

**Directus + `table_registry`** (chỉ qua DOT ở §1.5)
- theo dõi chỉ-đọc `balo_tu_dien_nhan`;
- dòng mới `tbl_balo_luat` → `/reports/report-balo-luat` (danh sách sống, sắp theo `thu_tu`);
- dòng mới `tbl_balo_khoi` → `/reports/report-balo-khoi` (báo cáo `view_sql` sống, gom từ balo);
- sửa `fields` của 4 dòng `tbl_balo_table`, `tbl_balo_view`, `tbl_balo_function`, `tbl_balo_trigger` (B8).

**File trên VPS1 — đúng các đường dẫn mà DOT bắt buộc**
- `/opt/incomex/dot/sql/balo-nhan-*.sql` (ghi, đọc, và file thử âm) + dòng tương ứng trong `/opt/incomex/dot/sql/approved-sql-manifest.tsv`;
- `/opt/incomex/dot/sql/labels/balo-nhan-*.sql` + dòng tương ứng trong `/opt/incomex/dot/sql/labels/approved-label-manifest.tsv`;
- `/opt/incomex/dot/specs/`: sửa `balo_table.spec.json`, `balo_view.spec.json`, `balo_function.spec.json`, `balo_trigger.spec.json`; thêm `balo_luat.spec.json`, `balo_khoi.spec.json`;
- một dòng trỏ trong `/opt/incomex/docker/agent-data-repo/AGENTS.md`, `/opt/incomex/docker/nuxt-repo/AGENTS.md`, `/opt/incomex/docs/mcp-writes/AGENTS.md`;
- hồ sơ `/opt/incomex/work/pg-nhan-balo/` (có `INDEX.md`);
- baseline lớp bảo vệ cho đúng các vật trên (DROOT29: có old/new + lý do).
- **Quy tắc chống dừng vì đường dẫn:** nếu một DOT ở §1.5 ép file của nó phải nằm ở thư mục khác (allowlist cứng trong mã DOT) thì thư mục đó thuộc phạm vi, với điều kiện: chỉ thêm file tên bắt đầu `balo-nhan-` hoặc `balo_`, không sửa file có sẵn của việc khác, và ghi rõ trong KQ. Quy tắc này **không** mở rộng phạm vi PG/Directus.
- Thư mục `/opt/incomex/dot` đang có thay đổi chưa commit của việc khác: chỉ commit đúng file của việc này (không `git add -A`, không reset, không gom).

**Repo:** STARTED/KQ + Bảng + trả lời Q10 trong `work/pg-nhan-balo/COLLAB.md`.

## 3. Cấm
- Tắt/bật trigger hoặc cron · DROP/DELETE/TRUNCATE · dời schema · đổi cấu hình PG (kể cả bật đếm lượt gọi hàm) · restart dịch vụ.
- SQL tay, `psql` trực tiếp, REST admin, kể cả để đọc (DROOT26).
- Ghi bất kỳ giá trị nào vào `ket_luan`, kể cả ghi về trống. Cột này chỉ Owner.
- Suy SỐNG cho view/hàm từ bảng nguồn · điền 0 giả cho DÍNH · dùng bộ đếm cộng dồn khác kỳ thay cho kỳ đo · đoán KHỐI/VAI theo tên.
- Viết thêm nhãn vào `COMMENT ON` của vật khác; sửa/xoá nhãn văn cũ. Chép các dòng luật ra nơi nào ngoài `balo_tu_dien_nhan`.
- Thêm trigger lên `balo_thuc_the` (đang 0 trigger). Lập sổ DOT thứ hai. Chạy `dot-dot-register` chế độ thật. Viết mã Nuxt mới. Sửa `balo-reconcile.sql` hoặc mã của bất kỳ DOT nào.

## 4. Việc, theo thứ tự
- **B0 · Sao lưu và mốc.** Lưu vào hồ sơ, qua đường đọc ở §1.5: toàn bộ dòng balo (đủ cột) · cấu trúc + ràng buộc + quyền + ghi chú hiện có của balo · 6 dòng `table_registry` liên quan (4 trang balo, Reports Home, PG Census) · bản cũ của 4 file spec · mã commit hiện tại của 3 `AGENTS.md` · danh sách trigger bật/tắt · số bảng/view/hàm/trigger · **bộ đếm ghi hiện tại của mọi bảng** (để đo SỐNG, lưu ngay ở bước này). Đây là căn cứ lùi ở §8 và so sánh ở §6.
- **B1 · Nền và luật.** Thêm 3 cột nhãn. Tạo `balo_tu_dien_nhan`, cấp quyền đọc như §2; nạp đủ giá trị theo `view.html#C1–C6` với mã nhãn ở `#cot`, và **đủ các dòng luật L00–L10 theo `view.html#B1`, không bỏ chữ** (`nhan = 'LUAT'`, chữ luật ở `cau_thu`, `thu_tu` 0–10; các giá trị khác đánh `thu_tu` lớn hơn để luật luôn đứng trước). Mọi truy vấn và trang phải sắp rõ theo `thu_tu`. Chưa bật ràng buộc.
- **B1b · Đọc lại luật qua cửa thật, rồi mới dán.** Đọc L00–L10 và từ điển từ PG bằng một file SQL chỉ-đọc qua `dot-pg-atomic-apply`, lưu kết quả vào hồ sơ, so khớp từng chữ với `view.html#B1`. Ghi lại **đúng câu lệnh đã chạy được**: đó là “lệnh đọc luật” sẽ ghi vào các dòng trỏ T0/B3/T1. Không đọc được → DỪNG.
- **B2 · KHỐI** (máy, C1). Bảng/view/hàm: lấy từ nhãn văn cũ của chính vật: dòng `HE (so huu):` nếu có, không thì mã đầu của dòng `HE:`; không có hoặc ngoài 23 mã → `CHUA-RO`. Trigger: KHỐI của hàm nó gọi. `chuyen_mon` giữ nguyên.
- **B3 · VAI.** Hàm: giữ 5 giá trị `loai` đang có; hàm trống → theo C3. Bảng: phân loại theo 7 câu thử C2 theo thứ tự; căn cứ là sự thật đo được (cột, khoá ngoại, `pg_depend`, bộ đếm ghi, nguồn nạp), không theo tên; không chắc → `CHUA-RO` + lý do ngắn trong hồ sơ. View và trigger: `x`.
- **B4 · SỐNG** (máy, C4, ghi `ngay_do`). Mốc đầu kỳ = ảnh chụp 01/08 (§5.6); mốc cuối kỳ = bộ đếm lưu ở B0. Chỉ trừ hai mốc khi đủ cả ba: (1) nghĩa cột đúng như §5.6 (tự kiểm lại bằng phép cộng trên vài dòng); (2) bộ đếm liên tục: `stats_reset` không nằm trong kỳ và không bộ đếm ghi nào của bảng bị lùi (delta âm); (3) bảng có trong ảnh chụp. Thiếu một điều → `CHUA-RO` + lý do trong hồ sơ; điều (1) hoặc (2) hỏng cho cả ảnh chụp → mọi bảng `CHUA-RO` và báo Host. Số dòng = `count(*)` thật. Ghi **kỳ đo thật** (từ lúc nào đến lúc nào) vào hồ sơ và KQ. View, hàm → `Không đo được`. Trigger → `Bật`/`Tắt` theo catalog.
- **B5 · DÍNH** (máy, C5, chỉ trong PG). Là số tìm thấy được. Vật có KHỐI `CHUA-RO` → để trống `dinh`. Phần nào không đo được (ví dụ quét thân hàm) → báo thiếu trong KQ, không lấp bằng 0.
- **B6 · Ràng buộc** (theo `view.html#cot`). Thêm 4 cột khoá tự sinh và 4 khoá ngoại tổ hợp sau khi dữ liệu đã hợp lệ. Chứng minh PG từ chối: (a) giá trị lạ; (b) giá trị của nhãn khác; (c) giá trị sai loại vật (ví dụ VAI của bảng đặt cho hàm); và chấp nhận ô trống. Cách thử: file `balo-nhan-thu-am-*.sql` cố ý vi phạm → cổng báo lỗi, giao dịch tự rollback, không để lại dữ liệu.
- **B7 · Dòng trỏ.** T0: mẫu `view.html#T0` vào ghi chú bảng balo qua `dot-pg-label-apply` (file dưới `sql/labels/`), đặt ở ĐẦU, giữ nguyên chữ cũ bên dưới. B3: mẫu `view.html#B3` ở đầu mỗi file SQL của việc này. Chỗ `[lệnh đọc luật]` trong mẫu = câu lệnh đã chạy được ở B1b.
- **B8 · Màn hình.** (1) `report-balo-luat`: danh sách sống của `balo_tu_dien_nhan`, sắp `thu_tu`. (2) `report-balo-khoi`: báo cáo `view_sql` sống, mỗi khối một dòng (vật chưa dán gom vào dòng “(chưa dán)”): số vật theo loại · số bảng Rỗng / Đứng yên / Tự quay / Có ghi · số `CHUA-RO` · số `Không đo được` · tổng DÍNH · `ket_luan` của khối (một giá trị, “lẫn”, hoặc trống). (3) Bốn trang balo: cột hiện theo thứ tự ID · Tên · Nơi lưu · Khối (`nhom`) · Vai (`loai`) · Sống (`active`) · Dính (`dinh`) · Kết luận (`ket_luan`) · Ngày đo (`ngay_do`) · Chuyên môn · Kiểm soát · Mô tả (`ghi_chu`) · Đã mất; bỏ cột Lớp khỏi màn; mỗi cột nhãn có `description` một dòng trỏ về “Reports › Luật nhãn” (nếu DOT không nhận khoá `description` trong `fields` thì bỏ phần mô tả cột và ghi vào KQ; không phải điều kiện dừng). **Thiếu `report-balo-luat` hoặc `report-balo-khoi` thì chưa XONG.**
- **B9 · Trỏ và sổ.** T1: thêm vào đầu mục “Quy ước bắt buộc từ nay” của 3 `AGENTS.md` đúng một dòng: `Nhãn PG hiện hành nằm ở bảng balo_thuc_the; luật dán nhãn đọc ở bảng balo_tu_dien_nhan (các dòng nhan = 'LUAT', theo thu_tu) bằng [lệnh đọc luật]. Quy ước DIA CHI / SU KIEN trong COMMENT ON bên dưới là hồ sơ 08/2026, không viết thêm.` T2 (KB): không làm, KB đang khoá ghi → giữ OPEN. **Sổ DOT (Q10):** tìm đúng một sổ thật do việc `vps1-up-grade` lập; đọc được → ghi đường dẫn/cột/từ vựng/quan hệ với `dot_tools` vào COLLAB và thêm dòng cho các file SQL mới theo đúng khuôn của sổ; không thấy hoặc chỉ có trên máy lab → giữ OPEN trên Bảng, không lập sổ khác. Không có trong sổ không có nghĩa là công cụ không dùng.
- **B10 · Làm mới, hồi quy, bảo vệ.** Chụp nhãn theo `khoa_nhan_dien` → bấm Làm mới thật → chụp lại: không nhãn nào mất hay đổi, không nhân dòng, không đụng vật ngoài phạm vi; bảng `balo_tu_dien_nhan` xuất hiện thành dòng mới → dán nhãn cho nó theo luật (sinh sau mốc đo thì SỐNG = `CHUA-RO`). Các file SQL dán nhãn chạy lại được mà không đụng `ket_luan`. 4 trang balo cũ + 2 trang mới mở được trên browser thật; `dot-balo-reconcile --verify` PASS; vật bền mới vào lớp bảo vệ (DROOT29); đọc bảng đèn (DROOT34).

## 5. Bẫy đã biết (Host đã đối chiếu mã và số liệu thật 02/10)
1. `dot-pg-atomic-apply` từ chối mọi file chứa chuỗi `meta_catalog`, `birth_registry`, `table_registry`, `v_registry_`, `qt001_` — kể cả trong chú thích hay dữ liệu. ⇒ SQL dán nhãn khoá theo `stt`, không viết tên vật; cột `vi_du` tránh các tên đó. Nó cũng chặn `DELETE FROM`, `TRUNCATE`, `BEGIN/COMMIT/ROLLBACK/SAVEPOINT` ở đầu câu lệnh (khối `DO $$ … $$` thì được), lệnh `\` của psql. Không nới guardrail, không đổi tên/định danh để lách.
2. Cổng atomic chặn mọi DROP, kể cả `ALTER … DROP CONSTRAINT/COLUMN` ⇒ cột, khoá ngoại, bảng mới **không lùi được qua cổng**: thử kỹ rồi mới áp (§8).
3. Cột tự sinh không được tham chiếu cột tự sinh khác: biểu thức khoá tính từ `khoa_nhan_dien`, không từ `loai_census` (cột này là `split_part(khoa_nhan_dien, ':', 1)` STORED).
4. `COMMENT ON` ghi đè cả khối ⇒ đọc ghi chú hiện có rồi nối. `dot-pg-label-apply` chỉ nhận câu `COMMENT ON`, từ chối `COMMENT ON TRIGGER`, không nhận khối `DO` hay lệnh `\`.
5. `pg_stat` cộng dồn từ 17/04/2026 và còn liên tục tới 02/10 (PG khởi động lại 02/10 03:59Z nhưng bộ đếm giữ nguyên; `stats_reset` trống); `n_live_tup` là ước lượng; TRUNCATE không tính vào `n_tup_del`.
6. **Ảnh chụp 01/08** `/opt/incomex/evidence/del1g-20260801/out/snap_directus_0.psv` (352 dòng schema `public`, chụp 2026-08-01T10:56:06Z). 9 trường ngăn bởi `|`: thời điểm · tên bảng · `seq_scan` · `idx_scan` · tổng đọc · **tổng ghi** · `n_tup_ins` · `n_tup_upd` · `n_tup_del`. Host đã kiểm bằng phép cộng trên 5 bảng (ví dụ dòng có `…|1671|927|744|0`: 927 + 744 + 0 = 1671). Bảng ngoài `public`: `ngoai_0.psv`, 4 trường: thời điểm · `schema.bảng` · tổng đọc · tổng ghi (chụp 2026-08-01T22:31:53Z). Không có file script riêng sinh ra ảnh chụp; executor tự kiểm lại nghĩa cột bằng phép cộng trước khi dùng.
7. Với quyền chỉ đọc, `information_schema` không hiện khoá chính/khoá ngoại (đo 02/10: 0/161). Kiểm ràng buộc bằng `pg_constraint`.
8. `balo_thuc_the` do role `workflow_admin` sở hữu, đã có khoá chính `stt`, cột sinh `loai_census`, một CHECK trên `lop` (để nguyên), quyền: `directus` đọc-ghi, `context_pack_readonly` đọc. Bảng mới tạo qua cổng sẽ thuộc `workflow_admin`: không cấp quyền đọc thì Directus, Reports và đầu nối chỉ-đọc không đọc được luật.
9. `dot-report-publish`: `view_sql` là đúng một câu SELECT/WITH, không có `;` ở giữa, và bị từ chối nếu chứa nguyên từ `insert`, `update`, `delete`, `drop`, `alter`, `create`, `truncate`, `grant`, `revoke`, `copy`, `call`, `do` (tên cột như `ngay_do` không sao; đừng đặt bí danh đúng bằng các từ này).
10. Event trigger `evt_trigger_guard_ddl` bật cho `ALTER TABLE` nhưng chỉ ghi cảnh báo khi vật là trigger; thêm cột/khoá ngoại không sinh cảnh báo. Vẫn so `trigger_guard_alerts` trước/sau.

## 6. Xong khi (thiếu một điều là chưa XONG)
- Mọi dòng `da_mat = false` tại lúc chạy: `nhom`, `loai`, `active` không trống; `dinh` chỉ trống khi KHỐI là `CHUA-RO`.
- `ket_luan`: không dòng nào bị RUN này ghi (so với B0).
- PG từ chối giá trị lạ, sai nhãn, sai loại vật (có bằng chứng).
- Đọc được L00–L10 qua cửa DOT (B1b) và trên trang `report-balo-luat`; ghi chú bảng balo có dòng trỏ ở đầu, chữ cũ còn nguyên.
- Có đủ hai trang `report-balo-khoi` và `report-balo-luat`, mở được, đúng dữ liệu.
- Làm mới không mất nhãn, không nhân dòng (B10). 4 trang balo cũ không hỏng.
- Danh sách trigger bật/tắt và số view/hàm/trigger không đổi so với B0; số bảng tăng đúng 1.
- Sổ DOT (Q10) và T2 có thể còn OPEN mà không chặn XONG phần PG; nhưng khi đó KQ phải ghi rõ “chưa khoanh được công cụ DOT”.

## 7. KQ
Ghi vào `work/pg-nhan-balo/COLLAB.md` một khối ngắn `KQ@PGNB-LABEL-20261002-02 XONG|DỪNG` (kèm sửa ■/➡/`cập nhật` của Bảng):
- số vật đã dán đủ · **báo riêng** số `CHUA-RO` theo từng nhãn và số `Không đo được`, kèm căn cứ; kỳ đo thật của SỐNG;
- các khối cần rà (toàn rỗng / đứng yên / tự quay) — là dấu hiệu, không phải kết luận;
- công cụ DOT có bằng chứng ít dùng theo sổ DOT, hoặc ghi rõ chưa đọc được sổ;
- **bàn giao cho việc `vps1-up-grade` (trước G7):** delta cấu trúc (+1 bảng, +7 cột, +4 khoá ngoại), dữ liệu nhãn, 2 trang mới + 4 trang sửa, dòng trỏ, danh sách đủ file đã tạo/sửa trên VPS1 (đường dẫn + sha256), mốc bằng chứng; lưu ý sau khi nâng PG bộ đếm về 0 nên lần đo SỐNG sau phải lấy mốc mới;
- đầu việc còn OPEN (Q10, T2) · blocker cần Owner · `ĐÈN: n xanh · m đỏ` · đường dẫn hồ sơ.
Trả Owner đúng một dòng `XONG` hoặc `DỪNG`.

## 8. Lùi lại
| Phần | Lùi bằng |
|---|---|
| Giá trị nhãn (`nhom`, `loai`, `active`, `dinh`, `ngay_do`) | file SQL sinh từ bản B0, chạy qua cổng |
| Ghi chú bảng balo | `dot-pg-label-apply` với chữ cũ ở B0 |
| 4 trang balo | publish lại 4 spec cũ ở B0 |
| 2 trang mới | publish lại với trạng thái không hiện (nếu khuôn cho phép), không xoá |
| 3 `AGENTS.md` | hoàn tác đúng một dòng đã thêm |
| Cột, khoá ngoại, bảng mới | **không lùi được qua cổng** (cổng chặn DROP): để nguyên, vô hại vì chỉ thêm và ô trống hợp lệ; nếu khoá ngoại gây lỗi ghi → DỪNG, báo Host, không tự gỡ |
