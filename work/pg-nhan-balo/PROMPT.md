# PROMPT — pg-nhan-balo
RUN_ID: PGNB-AUDIT-COVERAGE-20261003-01
Executor_Surface: Codex

## 0A. OVERRIDE HIỆN HÀNH — AUDIT ONLY, ZERO MUTATION

Owner chưa chốt phạm vi dán nhãn. **Không dán nhãn, không sync, không WRITE PG/VPS.** Chỉ kiểm tra và báo cáo coverage Balo trên máy thật.

Canonical đã xác nhận:
- Census định nghĩa 12 loại: `schema | table | view | matview | sequence | function | procedure | trigger | constraint | index | foreign_table | column`;
- `dot-balo-reconcile` hiện chỉ có scope `table | view | function | trigger`.

Vì vậy số `2148/2148` chỉ chứng minh reconcile đủ trong 4 loại này; **không được kết luận mọi object PG đều có Balo**.

### Audit bắt buộc
Dùng đường đọc/DOT hiện hữu, read-only, để lập bảng 12 dòng:
`loại | live_pg | balo_active | thiếu_dòng_balo | balo_dư/stale | ghi_chú`.

Bắt buộc phân biệt 3 trường hợp:
1. **Coverage gap:** object live thuộc một loại nhưng không có dòng tương ứng trong `balo_thuc_the`.
2. **Scope gap:** loại Census chưa thuộc scope reconcile hiện hành; không gọi đây là "thiếu nhãn".
3. **Annotation gap:** đã có dòng Balo nhưng các ô nhãn/thông tin đang trống.

Riêng 4 loại đang reconcile (`table/view/function/trigger`): đối chiếu theo identity thật và liệt kê số object live thiếu dòng Balo, nếu có.
Riêng 8 loại còn lại: báo live count, Balo có/không, và căn cứ canonical rằng reconcile chưa mở scope.
Sau đó, với các dòng Balo đang tồn tại, đếm ô trống theo từng cột nhãn hiện hữu và theo `loai_census`.

### KQ audit
Ghi `KQ@PGNB-AUDIT-COVERAGE-20261003-01 XONG|DỪNG` vào COLLAB với:
- bảng 12 loại;
- tổng live PG theo 12 loại;
- tổng dòng Balo active;
- coverage gap / scope gap / annotation gap tách riêng;
- kết luận **chỉ là số liệu**, không đề xuất dán gì nếu chưa được Owner chốt.

Nếu không có đường đọc hợp lệ cho một phép đo thì ghi `UNKNOWN` + blocker; không đoán, không thay bằng số cũ trong repo.

## 0. Mục tiêu dán nhãn — TẠM HOLD, chỉ dùng sau khi Owner chốt audit

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

## 1b. Phần thiếu là gì, dán theo quy tắc nào (Host đo 03/10 — P13)

**Đo thật:** cả 2.148 vật đã có dòng Balo, không vật nào nằm ngoài. Hàm 654/654 đã đủ `nhom` · `loai` · `chuyen_mon` · `ghi_chu` theo Rule 02 (`label-rules/02-function-balo-agent-discovery.md`) ⇒ không đụng. **Bảng 385 · view 699 · trigger 410: mọi ô nhãn đang trống ⇒ đây là phần thiếu.** Rule 02 chỉ phủ hàm; `label-rules/` chưa có quy tắc cho ba loại này. RUN này điền ba loại đó **theo đúng hợp đồng cột và danh sách giá trị của Rule 02**, chỉ thêm các dòng sau (không thêm cột, bảng, khoá hay trang nào):

- **Trigger:** `chuyen_mon`, `nhom` = của hàm nó gọi (đã đo: 410/410 hàm đó có nhãn) · `loai` = `Trigger nội bộ`.
- **View:** `chuyen_mon`, `nhom` = của bảng nó đọc, lần theo `pg_depend` tới bảng gốc; các bảng gốc khác miền ⇒ theo họ tên view khi họ đó trùng một họ hàm đã dán (`v_qt001_*`, `v_rp_*`, `v_birth_*`, `v_process_*`, `v_iu_*`…) · `loai` = `View đọc`.
- **Bảng — `chuyen_mon`** theo thứ tự bằng chứng: (1) cùng họ tên hoặc cùng schema với một họ hàm đã dán ⇒ slug của họ đó; (2) không có ⇒ theo mã hệ ở dòng `HE:` trong nhãn cũ của chính bảng: IU→`iu.core` · TAC→`tac` · PIVOT→`pivot` · WORKFLOW→`workflow` · PROCESS→`process` · TAXONOMY, BALO→`classification` · KHAI-SINH→`birth_registry` · REGISTRY→`registry` · GOVERNANCE→`governance` · KB, CONTEXT-PACK→`content_metadata` · HA-TANG, DOT→`utility` · DIRECTUS→`directus` · UI, OS→`web` · AI→`ai`.
- **Bảng — `loai`** = một trong 7, xét theo thứ tự, khớp câu nào dừng ở câu đó: `Nền tảng` (do Directus, extension hoặc mẫu website cài sẵn) · `Tạm / sao lưu` (bản chụp của bảng khác, không vật nào đọc) · `Bảng nối` (chỉ gồm khoá trỏ sang hai bảng khác) · `Nhật ký` (chỉ thêm dòng theo thời gian) · `Kết quả tính` (xoá đi chạy lại hàm là có lại) · `Danh mục` (danh sách giá trị hoặc cấu hình để nơi khác tra) · `Dữ liệu` (phần còn lại). Căn cứ là cột, khoá ngoại, `pg_depend`; không theo tên.
- **`nhom` của cả ba loại** = suy từ `chuyen_mon` bằng đúng cặp slug→nhóm đang có trên 654 hàm (đọc từ Balo; đã đo: mỗi slug đúng một nhóm). Ba slug chưa có ở hàm: `directus`→`Nền tảng Directus` · `web`→`Web & giao diện` · `ai`→`AI & agent`. Không đặt thêm tên nào khác.
- **`ghi_chu`** = một dòng theo khuôn Rule 02 §3.7, chỉ gồm sự thật lấy từ catalog. Trigger: thời điểm · sự kiện · bảng · hàm gọi · đang bật hay tắt, kèm `[GỌI] INTERNAL_TRIGGER; không gọi trực tiếp`. View: đọc từ những bảng/view nào. Bảng: vai + trỏ khoá ngoại tới bảng nào, được bảng nào trỏ tới. Thẻ `[BẰNG CHỨNG]` ghi nguồn. Không viết mô tả suy đoán.
- **Không ghi:** `lop`, `active` (Rule 02 §3.4–3.5: chưa có danh sách chuẩn) · `kiem_soat` (giữ `false`).
- **Chỉ lấp ô đang trống.** Ô nào không đủ căn cứ ⇒ để trống ô đó, đưa vật vào danh sách `CHUA-RO` kèm lý do.
- **Cách ghi:** trước khi ghi, xuất toàn bộ dòng Balo ra hồ sơ `/opt/incomex/work/pg-nhan-balo/` (đường lùi). Ghi bằng `dot-pg-atomic-apply`: file `/opt/incomex/dot/sql/balo-nhan-*.sql` + dòng sha256 trong `approved-sql-manifest.tsv`; UPDATE khoá theo `stt`, luôn có `WHERE <ô> IS NULL`. Cổng này từ chối mọi file chứa chuỗi `meta_catalog`, `birth_registry`, `table_registry`, `qt001_`, `v_registry_` (kể cả trong chú thích hay giá trị) ⇒ file không nêu tên vật; chữ trong `ghi_chu` do PG ghép từ catalog lúc chạy; **giá trị `chuyen_mon`/`nhom` chép từ một dòng hàm mẫu theo `stt`, không gõ chữ** (slug `birth_registry` cũng là chuỗi bị chặn).

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
