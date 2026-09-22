# KIỂM TOÁN KIẾN TRÚC ĐỘC LẬP — HỆ “SỬA RẺ”

Ngày kiểm: 2026-07-16 (Asia/Ho_Chi_Minh)

Phạm vi bằng chứng:

- Workbook `hop-dong-thong-tin-sua-re.xlsx`, đủ 13 sheet; đã đọc giá trị/công thức và render toàn bộ sheet.
- Mã live trên VPS: `mow-unified-canvas-v2.html`, `modw-builder-v1.html`, `mvx-v3.js`, `eco-nav.js`, `_README-DATA-REGION.md`.
- DOM runtime của hai URL, đi qua 20 state MOW và 5 state MODW.
- PostgreSQL `directus`: schema, dữ liệu, ràng buộc và index của hai bảng `sua_re_*_nhap`.
- Git notebook, timer snapshot và các kênh backup trên VPS.

Hash workbook đã kiểm: `8eafa97870e6aee1dfde54af0d4428c926aeb119a10d42666a7a73398017d4f5`.

## Kết luận thẳng

Hướng `data-region` là đúng và đáng giữ. Bản đồ hiện có 169 mã, không trùng, không sai cú pháp; DOM runtime thực sự chạm đủ 100 mã MOW `BUILT`, 25 mã MODW `BUILT` và 3 mã shell. Đây là phần tốt hơn mức tự mô tả.

Nhưng hệ chưa đạt “sửa rẻ” ở tầng hợp đồng và vận hành. MOW/MODW hiện là prototype phía trình duyệt, chưa ghi PG; trọng tài MOW đang sai ngay trên dữ liệu hiện tại; sổ khái niệm Excel và PG là hai hệ tên rời nhau hoàn toàn; và `id/parent/order/version` đang bị hoãn dù đó chính là phần đắt nhất nếu thêm muộn. Nếu tiếp tục nhân sang 6 UI còn lại trước khi khóa các điểm này, chi phí sửa sẽ tăng chứ không giảm.

## Phát hiện theo rủi ro

### F1 — MOW/MODW chưa “chạy thật”; nút Đúc và Gửi chỉ mô phỏng phía trình duyệt

1. Vấn đề: Khẳng định “MODW hiện thực hóa MOW và có thể chạy thật” không đúng với mã live được chỉ định.
2. Bằng chứng:
   - `modw-builder-v1.html:239-250` chỉ dựng JSON vào `<pre>`; `App.cast()` chỉ `alert('Đúc node (demo)...')`.
   - `mow-unified-canvas-v2.html:429-435` giữ đề xuất trong `editSt.proposedNodes` và tự xóa sau 10 phút.
   - `mow-unified-canvas-v2.html:507-517` chèn node vào mảng `D[...]` trong bộ nhớ.
   - Runtime ghi nhận không có request nghiệp vụ/API; chỉ có tải HTML/JS/CSS/ảnh/font và fetch lại `eco-nav.js`.
   - MOW tự gắn nhãn `DRAFT · mock data` tại dòng 250.
3. Rủi ro: **Cao** — checklist có thể chứng nhận một hợp đồng “BUILT” chỉ vì UI hiển thị được, trong khi không có persistence, transaction, quyền, idempotency hay khôi phục.
4. Fix rẻ nhất: Tạo đúng một “vertical slice” thật trước khi làm UI thứ ba: `MODW cast → API → transaction PG → đọc lại bằng MOW`. Chỉ cần một node T2, nhưng phải có test ghi/đọc/xóa trong DB test. Tách trạng thái thành `UI_BUILT`, `CONTRACT_BOUND`, `PERSISTED`, `E2E_VERIFIED`; không dùng một chữ `BUILT` cho cả bốn.

### F2 — Trọng tài ghi trong Excel đang sai trên chính MOW hiện tại

1. Vấn đề: Câu lệnh được gọi là “robust” không đọc được mã truyền qua map/tham số, nên báo thiếu 11 mã có thật; đồng thời thấy 4 mã `TO_REMOVE` vẫn đang sống.
2. Bằng chứng:
   - Chạy đúng logic câu lệnh tại `quy_trinh` cho prefix `mow` và hai file MOW cho kết quả: Excel kỳ vọng 100, lệnh chỉ tìm 93; thiếu 11 và thừa 4.
   - 7 mã `mow.shell.layer.t1..t7` nằm trong `LAYER_REGION` ở `mow-unified-canvas-v2.html:270` rồi được nội suy ở dòng 300; grep chỉ tìm attr literal hoặc `setAttribute` nên không thấy.
   - 4 mã section `mow.normal.detail.info`, `trigger_output`, `assignee_sla`, `history` được truyền vào `mkSec(...)` tại dòng 426 và emit ở dòng 428; grep hiện tại cũng không thấy.
   - Runtime DOM lại thấy đủ cả 11 mã này.
   - Bốn mã còn sống nhưng Excel đánh `TO_REMOVE`: `mow.shell.view.template`, `mow.shell.view.ops`, `mow.normal.detail.info.iu_ref`, `mow.propose.advanced.timetable.accumulate`.
3. Rủi ro: **Cao** — NT1 có thể báo đỏ giả hoặc được con người “giải thích bỏ qua”, làm mất tính tất định; trạng thái MOW “khép/sạch” hiện không tái lập được.
4. Fix rẻ nhất: Hạ grep xuống vai trò chẩn đoán nhanh. Gate chính dùng một manifest literal được sinh/kiểm bằng parser + DOM state runner. Ngay lập tức sửa trọng tài để xuất ba tập riêng: `source literals`, `runtime DOM union`, `Excel expected`; không gọi PASS nếu bất kỳ `comm` nào còn dòng.

Lệnh đã chạy để tái hiện:

```text
{ grep -o 'data-region="mow\.[^"]*"' mow-unified-canvas-v2.html mvx-v3.js;
  grep "setAttribute('data-region'" mow-unified-canvas-v2.html mvx-v3.js |
  grep -o "'mow\.[^']*'"; } | sort -u
```

### F3 — So tập `sort -u` che mất lỗi số lần xuất hiện và dead code

1. Vấn đề: Một mã còn ở bất kỳ đâu là đủ PASS, dù một trong nhiều cửa bắt buộc đã bị xóa, nằm trong comment, nhánh không chạy hoặc template không bao giờ render.
2. Bằng chứng:
   - `_README-DATA-REGION.md:19` yêu cầu so tập phân biệt và cố ý bỏ số lần xuất hiện.
   - Source có `mow.propose.advanced.items.del` ba literal; runtime có tối đa năm phần tử. Xóa hai literal vẫn cho cùng tập sau `sort -u`.
   - `modw.picker.item` có hai đường sinh code và runtime có tối đa 10 phần tử; tập chỉ còn một mã.
   - Câu lệnh nhánh `setAttribute` lấy mọi literal prefix trên cùng dòng, không chứng minh literal đó là đối số thực của attribute.
3. Rủi ro: **Cao** — đây là ca giả-PASS đúng loại “10 lần rà vẫn có thể giống nhau nhưng đều sai”. Tính tất định của công cụ không đồng nghĩa tính đúng.
4. Fix rẻ nhất: Thêm hai cột `occurrence_policy` (`ONE`, `AT_LEAST_ONE`, `EXACT_N`, `PER_ITEM`) và `state_id`. So count ở DOM của state tương ứng; với template dữ liệu dùng `AT_LEAST_ONE`, với copy-paste tĩnh dùng `EXACT_N`. Comment/dead code không được tính vào runtime.

### F4 — NT2/NT3 pass hình thức nhưng hợp đồng khái niệm chưa kín

1. Vấn đề: NT2 chỉ kiểm ô `khai_niem_chung` không trống, không kiểm key tồn tại, đúng nghĩa hay đã được hiện thực hóa.
2. Bằng chứng:
   - 100 dòng `IN` dùng 58 key khác nhau, trong khi sổ định nghĩa có 47 key.
   - Có 20 dòng `IN` map tới key không tồn tại trong sổ, gồm `sla`, `thoi_gian_thuc_thi`, `trang_thai_muc`, `bang_thoi_gian`, `ghi_chu`, `dieu_huong`…
   - Có 8 concept đã định nghĩa nhưng không được dòng `IN` nào dùng, gồm `tg_cong_don`, `tg_phat_sinh`, `han_hoan_thanh`, `vi_tri_de_xuat`…
   - `modw.build.time` được mô tả là “thời gian thực thi (phút)” nhưng control thực tế nhận chuỗi “Khi có lệnh nhập · hạn +1 ngày” và xuất trường JSON `when`; đây là trigger/deadline, không phải số phút.
   - `modw.preview.bread` đang map `dieu_huong` nhưng lại đánh `IN` và đối tượng `quan hệ cha-con`; key đúng phải là quan hệ cha-con hoặc phải OUT.
3. Rủi ro: **Cao** — máy có thể xác nhận “mọi khu có concept” trong khi concept không tồn tại hoặc sai ranh giới, làm PG sai schema ngay từ gốc.
4. Fix rẻ nhất: Biến NT2 thành FK máy: mọi dòng `IN` bắt buộc `concept_key` tồn tại trong sổ canonical và `concept.status` đạt mức phù hợp. Thêm kiểm kiểu đơn giản: `tg_thuc_thi` phải là numeric phút; `trigger/han` là key khác. Sửa 20 mapping trước khi map UI tiếp.

### F5 — Excel và hai bảng PG đang là hai hệ hoàn toàn rời nhau

1. Vấn đề: Chưa có “đổ hợp đồng vào 2 bảng PG” theo nghĩa SSOT; workbook và PG không dùng chung key, schema hay dữ liệu.
2. Bằng chứng:
   - Excel canonical có 47 concept; PG có 14 concept; giao chính xác theo `concept_key` là **0**.
   - PG dùng key `workflow`, `workflow.step`, `field.trigger`, `role.nguoi_thuc_hien`…; Excel dùng `quy_trinh`, `cong_viec`, `trigger`, `nguoi_thuc_hien`…
   - PG `sua_re_ui_khai_niem_nhap` có 32 dòng và chỉ cho `master-list-quy-trinh-v1`; không có MOW/MODW. Ba usage current còn `concept_id IS NULL`; toàn bộ `owner_concept_id` trống.
   - Excel tab `sua_re_khai_niem_nhap` có 0 dòng; tab usage có 78 dòng MOW nhưng cả 78 `owner_decision` và `owner_concept_key` đều trống.
   - PG ép `concept_kind ∈ {workflow,step,task,field,role,org,relation}` và `status ∈ {draft,active,retired}`; Excel canonical dùng `người/thời gian/quy trình/đề xuất/tổ chức` và `BUILT/NOT_BUILT/...`.
   - Hai cột `id bigint NOT NULL` của PG không có default, nên đường import trực tiếp còn phải tự cấp id.
3. Rủi ro: **Cao** — sửa Excel không làm PG đổi; sửa PG không phản hồi về Excel. Hai bên có thể cùng “đúng” nội bộ nhưng lệch âm thầm.
4. Fix rẻ nhất: Chọn một canonical keyset ngay. Khuyến nghị PG là SSOT sau khi Owner duyệt; Excel là view/xưởng nhập. Viết một import dry-run một chiều với bảng mapping legacy→canonical, transaction và report `insert/update/reject`; cấm copy-paste tay. Chưa import UI mới cho tới khi 47 concept có quyết định map rõ.

Các lệnh PG đã chạy:

```text
docker exec postgres psql -U directus -d directus -Atqc "select table_name,column_name,data_type,is_nullable,column_default from information_schema.columns where table_name in ('sua_re_khai_niem_nhap','sua_re_ui_khai_niem_nhap') order by 1,2"
docker exec postgres psql -U directus -d directus -Atqc "select 'concept',count(*) from public.sua_re_khai_niem_nhap union all select 'usage',count(*) from public.sua_re_ui_khai_niem_nhap"
docker exec postgres psql -U directus -d directus -Atqc "select concept_key from public.sua_re_khai_niem_nhap order by 1"
```

### F6 — Hai bảng hiện tại chưa đủ biểu diễn một “hợp đồng thông tin” có thể thực thi và sửa rẻ

1. Vấn đề: Schema chỉ lưu concept và usage quan sát; thiếu binding tới table/column, kiểu, cardinality, required/default, operation, quyền, version và input/output của hành động.
2. Bằng chứng:
   - `sua_re_ui_khai_niem_nhap` chỉ có `location_anchor`, một `concept_id`, near-match và quyết định Owner; không có `data_region`, PG object/column, kiểu/cardinality hay version nguồn.
   - Mỗi dòng Excel chỉ có một `khai_niem_chung`, nhưng `modw.preview.cast` là một hành động cần ghi đồng thời node, parent, executors, recipients, stores và time.
   - `ux_sruk_slot_current` chỉ cho một row current trên mỗi `slot_key`, nên không biểu diễn tự nhiên quan hệ N:M giữa một khu UI và nhiều field/concept.
3. Rủi ro: **Cao** — hai bảng có thể làm từ điển/ledger, nhưng không đủ sinh migration, kiểm impact hoặc chứng minh UI ghi đúng PG.
4. Fix rẻ nhất: Giữ hai bảng hiện tại làm `concept` và `ui_region`; tái dùng registry/edge sẵn có hoặc thêm một bảng binding nhỏ `contract_binding(region_id, concept_id, storage_object, storage_field, operation, cardinality, required, valid_from, valid_to, source_hash)`. Nếu tuyệt đối không thêm bảng, phải chấp nhận JSONB và mất FK/unique/check ở tầng field — trái mục tiêu kiểm bằng máy.

### F7 — Stable ID, parent, order và version bị hoãn dù đây là nợ đắt nhất

1. Vấn đề: Cây hiện dựa nhiều vào tên/mảng; khi trùng tên, đổi tên, chuyển cha hoặc chèn giữa, liên kết không còn bền.
2. Bằng chứng:
   - `_README-DATA-REGION.md:104-109` tự ghi nhận thiếu `parent_id`, id bền cho mục con, `order` bền và tham chiếu bằng id, nhưng hoãn.
   - `modw-builder-v1.html:144-153` dùng tên hiển thị làm key của `TREE` và `p` cũng là tên.
   - JSON MODW tại dòng 240-246 xuất `parent` là tên và `derived_path` là mảng tên.
   - MOW tạo node mới bằng `id:'pnew-'+Date.now()` tại dòng 511; child chủ yếu chỉ có `code/title`, không có FK/version.
3. Rủi ro: **Cao** — ở quy mô 10.000×10, collision, rename và reorder sẽ tạo sửa lan truyền; thêm sau khi nhiều UI đã sinh dữ liệu là migration khó nhất.
4. Fix rẻ nhất: Làm ngay trước UI tiếp theo: `node_id UUID/ULID`, `parent_id FK`, `sort_key` phân số/lexicographic, `version`, `created_at/by`. Tên chỉ là label. T1 dùng bảng nối khi nhiều cha; T7–T2 một cha theo quyết định hiện có.

### F8 — Backup UI là local-only trên cùng VPS; “full backup” không chứa UI/docs

1. Vấn đề: Git notebook sạch và timer chạy, nhưng repo không có remote và các backup offsite hiện không lấy thư mục UI hoặc bare repo notebook.
2. Bằng chứng:
   - `ui-preview-git remote -v` trả rỗng; service tự mô tả “local-only git, no push”.
   - Timer `ui-preview-notebook-daily` chạy thành công ngày 16/7, nhưng repo nằm ở `/var/lib/incomex/ui-preview-notebook.git` trên cùng VPS.
   - `/opt/incomex/scripts/backup-to-gdrive.sh:76-95` chỉ lấy Docker config, nginx/SSL và scripts; không lấy `/opt/incomex/docs` hay `/var/lib/incomex/ui-preview-notebook.git`.
   - Code backup/GitHub hiện xử lý `web-test` và `agent-data-test`, không phải notebook UI.
   - Điểm tốt: PG backup hằng ngày thành công và có offsite GDrive; container restore-test vẫn tồn tại.
3. Rủi ro: **Cao** — mất VPS có thể mất cả mã UI live lẫn lịch sử notebook, đúng hai nguồn đang được gọi là SSOT.
4. Fix rẻ nhất: Thêm đúng hai path UI vào backup offsite hiện có hoặc push bare notebook vào private remote. Kiểm bằng một restore drill tự động mỗi tuần: clone/restore sang temp, so HEAD + hash 5 file lõi. Không cần CI/CD deploy.

### F9 — Tài liệu “đọc trước khi sửa” đang mâu thuẫn với luật mới

1. Vấn đề: Người/AI làm đúng README vẫn có thể làm sai Excel hiện hành.
2. Bằng chứng:
   - `_README-DATA-REGION.md:50-64` nói 7 tab chỉ khác dữ liệu nên gộp một mã `layer.tab`.
   - Excel/quy trình mới lại ghi rõ 7 tier khác bản chất và phải giữ 7 mã `mow.shell.layer.t1..t7`.
   - README dòng 14-22 yêu cầu chia từng nhánh; dòng 87-94 lại yêu cầu một spec/UI; `quy_trinh` cũng nói không chia mẻ vụn.
   - README dòng 19 vẫn ghi grep nháy kép, trong khi dòng 69 mới yêu cầu hai dạng.
3. Rủi ro: **Vừa** — nhiều AI không độc lập về failure mode nếu đều đọc cùng tài liệu mâu thuẫn; số người kiểm tăng nhưng lỗi chung vẫn lọt.
4. Fix rẻ nhất: Một SSOT thực sự cho HOW. Rút README còn 10–15 dòng dẫn tới phiên bản/commit của quy trình canonical; xóa ví dụ đã bị lật. Mỗi rule có `rule_id` và `supersedes`, không để hai câu đúng cũ/mới cùng sống.

### F10 — NT4 chỉ chứng minh “có tên file ảnh”, chưa chứng minh ảnh đúng phiên bản code

1. Vấn đề: 12 ảnh hiện đều tồn tại, nhưng workbook không nhúng ảnh, không có hash/commit/state script, nên ảnh cũ vẫn PASS.
2. Bằng chứng:
   - Sheet `man_hinh` chỉ lưu tên file; workbook không có `xl/media/*`.
   - Ảnh nằm ngoài workbook trong thư mục `anh-man-hinh-ui/`.
   - Không có cột `code_commit`, `captured_at`, `sha256`, `scenario_id`.
3. Rủi ro: **Vừa** — NT4 có thể giả-pass sau khi UI đổi; chuyển workbook sang máy khác sẽ mất bằng chứng ảnh.
4. Fix rẻ nhất: Thêm 4 cột trên và một lệnh verify file tồn tại + hash + commit. Không cần nhúng ảnh nếu đường dẫn tương đối và bundle backup chứa cả workbook lẫn thư mục ảnh.

### F11 — Source đang “append-only” và nạp lặp, làm tăng diện tích lỗi mỗi lần sửa

1. Vấn đề: MOW/MODW nạp cùng script nhiều lần, eval code động và có nội dung sau `</html>`.
2. Bằng chứng:
   - MOW nạp `mvx-v3.js` ba lần (`?v=1`, `?v=2`, `?v=3`) tại dòng 1320-1327; nạp `eco-nav.js` hai script tag rồi fetch+eval lần nữa tại 1329-1333.
   - MODW đóng `</html>` ở dòng 258 nhưng còn script ở 260-264.
   - `eco-nav.js:133-146` tự fetch và eval lại theo focus/pageshow/45 giây.
   - Runtime thấy CSP chặn Google Font trên cả hai trang.
3. Rủi ro: **Vừa** — state có thể bị reset/handler bị bọc nhiều lần; source khó review và một sửa nhỏ có hiệu ứng xa, trái “sửa rẻ”.
4. Fix rẻ nhất: Một script tag/version cho mỗi module, bỏ fetch+eval tự đồng bộ, đưa nội dung về trước `</body>`, dùng cache bust theo commit hash. Dọn một lần rồi khóa lint đơn giản: không duplicate `src`, không nội dung sau `</html>`.

### F12 — Nếu nối PG như hiện trạng, MODW mở cửa stored XSS

1. Vấn đề: Dữ liệu người dùng được ghép vào HTML rồi gán `innerHTML` mà không escape.
2. Bằng chứng:
   - `modw-builder-v1.html:220-227`: giá trị `nNode` đi qua `bread()` rồi gán vào `cBread.innerHTML`.
   - Dòng 231-236 ghép trực tiếp `nWhen` vào `cBody.innerHTML`.
3. Rủi ro: **Vừa hiện tại / Cao khi persistence** — hiện chỉ tự-XSS trong demo; khi lưu/đọc PG sẽ thành stored XSS và ảnh hưởng người khác.
4. Fix rẻ nhất: Dựng DOM bằng `textContent`; chỉ dùng `innerHTML` cho template tĩnh. Thêm một test payload `<img src=x onerror=...>` vào smoke test trước khi mở ghi thật.

### F13 — Workbook có lỗi dữ liệu nhỏ và cơ chế backup thủ công gây nhiễu

1. Vấn đề: Một ô định nghĩa đang là công thức lỗi và thư mục chứa hàng chục bản `.bak` không có retention/version manifest.
2. Bằng chứng:
   - `dinh_nghia_khai_niem!E10` là công thức `= SLA hiện tại.` và hiển thị `#NAME?`.
   - Có nhiều chục bản `hop-dong-thong-tin-sua-re*.xlsx` cạnh file chính, không có Git/manifest để biết bản nào canonical ngoài tên.
3. Rủi ro: **Thấp riêng lẻ, Vừa cộng dồn** — lỗi nhỏ làm hỏng tìm kiếm/đổ dữ liệu; backup rác tăng khả năng mở nhầm file.
4. Fix rẻ nhất: Sửa E10 thành text, giữ một thư mục `backups/` với retention 7–14 bản và `SHA256SUMS`; mỗi export canonical ghi `workbook_version` + thời gian + hash code live.

## Thứ tự sửa để rẻ nhất

### Trong 48 giờ — chặn nhân lỗi

1. Đóng băng mở rộng sang UI thứ ba.
2. Sửa trọng tài thành ba tập source/runtime/Excel; xử 11 missing giả và 4 `TO_REMOVE` thật.
3. Thêm trạng thái thực thi bốn mức, bỏ cách hiểu `BUILT = chạy thật`.
4. Chốt canonical concept key và xuất bảng reconcile 47 Excel ↔ 14 PG.
5. Đưa notebook UI ra offsite.

### Trong 7 ngày — chứng minh vertical slice

1. Chốt `node_id`, `parent_id`, `sort_key`, `version`.
2. Làm một `MODW cast → PG test → MOW readback` có transaction/idempotency.
3. Khóa FK NT2 và sửa 20 mapping undefined/sai nghĩa.
4. Dọn script nạp lặp và XSS trước khi persistence.

### Sau khi gate trên xanh

1. Mới map UI thứ ba theo cùng manifest/state runner.
2. Đo “concept mới/UI” bằng số canonical key được Owner duyệt, không đo bằng nhãn tự điền.
3. Chỉ giữ các AI handoff có failure mode khác nhau: source parser, runtime DOM, PG constraints. Không cần năm người cùng grep.

## Definition of Done đề xuất

Một UI chỉ được gọi là “chuẩn xong” khi đồng thời:

- `source ↔ runtime DOM ↔ Excel` không có missing/extra ngoài policy đã khai.
- Mỗi dòng `IN` có FK tới canonical concept; không còn key mồ côi.
- Mỗi concept cần lưu có binding tới storage field/operation và test kiểu/cardinality.
- Ít nhất một E2E test ghi PG và đọc lại đúng dữ liệu, actor, thời gian, vị trí, id/version.
- Ảnh có scenario + code commit + hash.
- Snapshot code và workbook có bản offsite, restore drill qua.

## Phán quyết cuối

Không nên bỏ `data-region`; nó là phần đúng nhất của kiến trúc. Cần bỏ ảo tưởng rằng “grep sạch + ô Excel đầy = hợp đồng chạy được”. Trọng tâm sửa rẻ tiếp theo không phải gắn thêm mã, mà là khóa canonical key, stable identity, storage binding và một đường E2E thật. Làm bốn việc đó trước sẽ rẻ; làm sau 6 UI nữa sẽ đắt.
