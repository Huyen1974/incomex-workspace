# COLLAB — mow-mot-moit-mout

## Owner · 25/09/2026 · Thể thức tab UIs
- Theo Owner: nền xanh đậm ở ngoài ba miếng; giữ nền sáng và bố cục Kanban/UI cha bên trong; vàng thao tác giảm sắc. Header mỗi miếng gộp mã bước, tên bước, mã con và link mã cha. Chưa đổi nội dung S001–S003; đây là thể thức để Owner duyệt. JEV tham khảo lựa chọn nền: `gen-dec-1790309121-WMnBWvBG16QkT25xMs7t`.
- Kiểm trên VPS commit `dcad873`: bản mở rộng và trang công việc đều hiện nền tối, vàng nhạt, mã con/cha ở header; bấm `UI.CANVAS ↗` mở đúng chuẩn cha trong tab UI Master. Trang công việc báo `fresh`.

## Owner · 25/09/2026 · Tách tab UIs
- Theo Owner: ba màn thử S001–S003 chuyển sang tab **★ UIs**, xếp dọc; tab **★ Quy trình vẽ UI** giữ danh sách bước gọn, liên kết mã UI mở đúng màn. Tab **★ UI Master** cũng được đánh dấu; ★ chỉ là dấu kiểm soát tab của Owner, không duyệt nội dung ba màn. Các tab còn lại giữ để dọn sau. Không tạo UI cha, file hay mã đăng ký mới. K0 FIELD vẫn chưa PASS.
- Kiểm Owner View publish commit `ad62f0e`: thấy ba ★ trên đúng tab, S001→S003 xếp dọc, tab quy trình trở lại danh sách gọn; bấm `KB.YC ↗` mở tab UIs tại `&section=wf5-s001`. Trang báo `fresh`.

## Owner · 25/09/2026 · Mẫu UI S001–S003 để duyệt (lịch sử)
- Đã vẽ 3 màn gập/mở ngay dưới các bước S001–S003 trong ban-duyet.html → Quy trình vẽ UI. Vàng = chỗ người cần bấm/điền. S002 nút ＋ Yêu cầu mở mẫu S003; không ghi dữ liệu thật. Bản Owner View publish commit 167977a: đã bấm mở cả ba màn, mở menu Master và chuyển S002→S003; URL section đổi đúng.
- Mã con đề xuất: KB.YC (cha KB = UI.CANVAS, S001), ML.YC (cha ML = UI.MASTER, S002), CF.YC (cha CF = UI.CONFIG, S003; tham chiếu hộp UI-018). Alias ngắn chỉ dùng trong bản thử, chưa đổi mã UI cha/đăng ký khóa thật. UI-030/031 cũ vẫn ở các bước sau để đối chiếu sau khi Owner duyệt.
- Kiểm UI T0 thật: nút Master có menu Quy trình/Field/MOT/MOUT, **chưa có Yêu cầu**. S001 đánh dấu mục này còn thiếu; chưa tự thêm vào UI chạy. Đây cũng cho thấy có thể cần tách thêm bước chọn Yêu cầu trước S002. Chờ Owner quyết trên bản vẽ.
- JEV tham khảo: S003 dùng Config (0,73; id gen-dec-1790307175-7SRxBJSCzocxhBXGLIjS); mã phân biệt KB/ML/CF (0,92; id gen-dec-1790307247-LVnVd3suvrl2zMp8eyqM); S001 báo thiếu menu trên Canvas (0,98; id gen-dec-1790307355-jg3zCJkBvIkxTWGhKqR5). JEV là tham khảo, không thay quyết định Owner. K0 FIELD chưa PASS.

## Owner · 25/09/2026 · URL theo tab và chi tiết
- ban-duyet.html: bấm 5 tab ghi hash của panel; mở mục ?/details ghi hash riêng; các mã S001–S033 là link tới từng bước. Tải lại và Quay lại khôi phục đúng tab/mục. Nút **🔗 Mở mục này** mở bản rộng tại đúng điểm đang xem.
- Nút UI cha trỏ tới từng hàng UI con (ví dụ UI-001 → &section=child-UI-001). Khi mở liên kết, hàng đích nằm dưới thanh tab cố định; đã kiểm trực tiếp vị trí 72px trên bản publish 8705354. Không cấp UI mới.
- Đã kiểm Owner View sau publish commit 607f9dd: URL Task view tự đồng bộ &section=matrix-view-ui-workflow, &section=wf4-s001, &section=detail-ui-workflow-diem-chua-thong-can-so-ui-that, &section=matrix-view-qa; tải lại vẫn mở đúng mục, Quay lại trở về mục trước. Chỉ đổi cách định vị bản duyệt; không đổi quy trình/K0.
- JEV tham khảo phạm vi sửa tại nguồn hiện có: gen-dec-1790306163-Lq0c1pxJAAN48hda0uJ8.

## Owner · 25/09/2026 · Kiểm kê dọc luồng khai yêu cầu FIELD
- Theo chỉ đạo mới: tab **Quy trình vẽ UI** đổi từ 3 màn ngang sang 33 bước người làm dọc trên một trang, chia 4 đoạn: khai/lưu, xét duyệt, xử lý/kiểm, đổi/dừng. Mỗi bước có mã 3 chữ số, hành động, UI và nhánh tiếp; chưa vẽ thêm màn.
- Giữ ba mã UI dự thảo UI-030/031/032, tái dùng theo mẫu cha UI.MASTER và UI.WORKSPACE; không cấp mã UI mới. UI-018/022 chỉ là điểm nối sang nhánh tạo Field. Mã YC giữ xuyên luồng, việc máy cấp mã/chuyển trạng thái không thành bước người.
- Chỗ chưa thông được ghi ngay cuối tab: Master yêu cầu thật và điểm vào; tạo/giao MOT duyệt; lịch sử khi trả/sửa; nhánh thiếu Field và đường trở về; người test/xác nhận; quyền đổi/rút. Bản kiểm kê chưa chứng minh quy trình khép kín hay PG/DOT, K0 FIELD chưa PASS. JEV phân loại người/máy: gen-dec-1790305037-18WOhIbkuyS1DA8PeCu8.
- Ba màn tương tác ở bản trước đã rút khỏi tab vì Owner yêu cầu **kiểm kê đủ bước trước khi thiết kế**. Mục "Ba bước người làm đầu tiên" bên dưới là nhật ký bản cũ, không còn là trạng thái hiện hành.

## Owner · 25/09/2026 · Ba bước người làm đầu tiên
- Owner sửa phạm vi: một bước người làm = một miếng UI riêng, có mã bước, mã UI, tên UI. Bản S00/UI-030 gộp khai + Master + duyệt là sai, đã thay trong tab **Quy trình vẽ UI** của `ban-duyet.html`.
- Bản vẽ dự thảo: `MMIM.FIELD.S001` → `UI-030 · Phiếu khai nhu cầu`; `MMIM.FIELD.S002` → `UI-031 · Master yêu cầu` (lọc Chờ duyệt); `MMIM.FIELD.S003` → `UI-032 · Phiếu duyệt yêu cầu (MOT)`. Mã ba chữ số để mở rộng hơn 150 bước FIELD. Mã YC cấp ở S001, đi xuyên S002/S003, sau này liên kết MOT/Field. Mã bước/UI chưa đăng ký chính thức; người duyệt và quyền còn chờ chốt. JEV tham khảo mã bước: `gen-dec-1790289577-EK9JvkcchX0vEBIEpfay` (độ tin cậy thấp).
- Bản vẽ chỉ đổi dữ liệu trong trình duyệt. Chưa có Master yêu cầu thật, chưa ghi PG/DOT, chưa kiểm quyền duyệt; K0 FIELD chưa PASS. S01–S07 cũ giữ ở tab Step quy trình để rà sau. Không tạo file mới.
- Verify VPS revision `71fb667b39b784516bff006a5846fe83145d0dbc`: UI-030 bấm thử tạo `YC-THỬ-001`; UI-031 hiện `YC-THỬ-001 · Trường mã dự án · Chờ duyệt`; bấm `Mở` sang UI-032 thấy cùng mã và đủ nội dung; bấm `Duyệt` hiện `Đã duyệt`, hai nút quyết định bị khóa. Đây là output UI thật của bản vẽ, không phải PG.

## K0 FIELD · 24/09/2026
- Đã đọc catalog PG trên VPS bằng giao dịch chỉ đọc. Bằng chứng gọn và phân mức ở `ban-duyet.html` → Step quy trình → Bài thử FIELD · K0. Điểm nghẽn quyền Directus không còn chặn việc kiểm kê; K0 toàn phần vẫn chờ Owner gật mục tiêu/phạm vi V1. Không mở K1, không đổi UI, không tạo master mới.
- JEV tham khảo: input = PG 24/09 (`collection_registry` 168 dòng/35 cột, `table_registry` 28/21, `directus_fields` 1.497, standards 11, thiếu `field_registry`, UI demo); lựa chọn = collection_registry / table_registry / directus_fields / standards / none / unknown; model `typesafe/jev-1.13-20260917`; result `none` 0,77, confidence 0,74; id `gen-dec-1790243828-KHbJiwWPBkzu1OYPlOpc`; Host kết luận không nguồn nào làm Master Field nghiệp vụ nguyên trạng.

## Sự cố khỏi điểm · Claude tự ý dựng bản xem sai nơi (23/09) — Owner yêu cầu đưa về đúng chỗ
Owner mở UI không thấy gì đổi. Thay vì sửa đúng cơ chế §12, **Claude tự copy HTML chính sang `ui:mow-mot-moit-mout.html`** (`/ui-preview/mcp-writes/…`, commit `b889b29` trên root ui). Sai kỉ luật: §12.2–§12.3 ghi rõ VPS chỉ có **một** đường đồng bộ (webhook push → snapshot → Task view, backstop 15′, nút Cập nhật chỉ đọc lại snapshot), “không có pipeline thứ hai” và mirror không được làm nguồn thứ hai. Claude nhận lỗi, không tự xử lý tiếp.

**Giao việc — Host soạn prompt, Agent làm, đúng ba điểm, không mở thêm:**
1. **Giải tán bản sai chỗ**: xoá `mow-mot-moit-mout.html` ở root `ui` (chỉ file này, do Claude tạo lúc 23/09, không phải bản gốc; bản chuẩn vẫn nằm trong Git). Owner đã yêu cầu đưa về đúng nơi quy định — đây là uỷ quyền cho đúng một thao tác xóa này, không suy rộng.
2. **Làm cho đúng §12 chạy thật cho việc này**: tìm vì sao HTML chính của `work/mow-mot-moit-mout/` không mở được từ Task view (`/knowledge/modules?task=…`) — ba lượt FIELD01–03 đều ghi `VIEW_PENDING_REVISION` mà không ai truy: snapshot có gồm HTML chính không · webhook/backstop có chạy không · vì sao trang đòi đăng nhập. Phần sửa thuộc mã runtime → **việc `work/hpml-view-for-user/`**, không sửa ở đây. Kết quả phải là **một đường link Owner mở được**.
3. **Luật mới, áp cho mọi bên kể cả Claude:** cấm tự tạo bản xem / đường dẫn nằm ngoài §12. Mỗi lượt phải kết thúc bằng link Owner View theo §12; snapshot chưa lên thì **DỪNG và báo ngay**, không được ghi `pending` rồi đi tiếp, càng không được dựng chỗ khác cho tiện.

## Claude phân tích KQ FIELD03 (`1ecb549`) · JEV `gen-dec-1790160609-8yAvAAgF8QcznrIgcKi9`
Đạt: 39 kịch bản, 15/15 chiều, G đặt trước + sơ đồ + đề xuất kèm hệ quả (đúng K1–K4), HTML nguyên SHA, mã đã có tiền tố việc `MMIM.FIELD.*`. Agent còn tự tìm ra lỗi thật: nút ✎ ở UI-022 không mở được hộp sửa vì hai UI dùng tham số khác nhau (`edit=` vs `truong=`) — tức luồng SỬA hiện **không chạy được trên máy thật**, không phải chỉ thiếu thiết kế.

**Hai điều Host phải xử lý trước khi đưa Owner gật:**
- **L01 · G04 hỏi sai thế lưỡng → JEV đổi kết luận.** Agent hỏi “tự chuyển ACTIVE hay thêm nút kích hoạt” → JEV 0,50, không dùng được. Hỏi lại có kèm điều chưa biết (**chính FIELD03 đã loại câu hỏi config/lưu trữ sang lượt sau, nên chưa ai biết Field sau duyệt có cần cấu hình mới dùng được hay không**) thì JEV chọn phương án thứ ba với **0,99 (độ tin 0,97): tách hẳn hai trạng thái** — *duyệt* là quyết định của người, *chạy* là khi Field thực sự dùng được trong form, máy tự chuyển khi đủ điều kiện (điều kiện đó chốt ở lượt config). Cả “tự chuyển ngay” lẫn “thêm nút bấm tay” đều ~0. Đổi đề xuất G04 theo hướng này rồi mới đưa Owner; để nguyên thì sau lượt config phải sửa cả máy trạng thái lẫn các dòng kịch bản dính tới.
- **L02 · Ngưỡng 150 KB của Claude đặt hôm qua là sai, tôi rút.** COLLAB đã 128 KB sau **một** đối tượng; còn bốn đối tượng cùng khuôn → ~300–400 KB, mà **mọi phiên đều phải đọc COLLAB ở read-gate**. JEV: tách ra ngoài **0,99 (độ tin 0,99)**. Ngay sau khi Owner gật G: chuyển thiết kế FIELD thành **một tài liệu sống riêng cho FIELD** (về sau sửa trực tiếp trên đó, không đẻ bản mới), COLLAB giữ bảng quyết định + con trỏ. Bốn đối tượng sau theo cùng khuôn ngay từ đầu.

**Owner cần biết trước khi gật G02:** gật “chỉ tính thành công khi Field ACTIVE sau duyệt” = mở một mảng dựng mới (màn duyệt, hàng chờ, ghi vào dữ liệu thật), vì 22/39 dòng đang `UI_THIEU`. Đây là đặt hàng dựng UI, không còn là việc viết tài liệu.

## Rà FIELD03 · Claude · Based_on READY `2873a38` · JEV `gen-dec-1790154754-Ezr2cwg5NjqJYQUQBXS1`
Khung A–G đúng và đủ; không mở lại điểm nào về nội dung. Bốn điểm về **cách trình bày và quy mô** — nếu không sửa thì sản phẩm lại thành bức tường chữ như FIELD01:

- **K1 · Đảo thứ tự tài liệu (JEV 0,99).** Prompt đang để bảng “Owner cần quyết” ở mục **G cuối cùng**. Luật trình bày của Owner: mở ra là thấy ngay hôm nay cần quyết gì. Đổi thứ tự: **G trước → một sơ đồ trạng thái nhìn được (khối + mũi tên, kèm 3 khối S01/S02/S03) → rồi mới A–F**. Owner đọc hình nhanh hơn chữ nhiều lần; bảng chữ chỉ là tầng dưới.
- **K2 · Mỗi câu hỏi đưa lên Owner phải kèm sẵn đề xuất.** Bảng G hiện chỉ có cột “quyết định cần Owner chốt” → Owner phải tự nghĩ ra phương án, trái luật đã đặt. Thêm cột **Đề xuất của hội đồng (Owner chỉ gật hoặc lắc)** + cột **hệ quả nếu lắc**. Không có đề xuất thì không được đưa lên.
- **K3 · Đặt trần cho lượt này (JEV 0,67).** 15 chiều × không trần = dễ ra 60–80 dòng, Owner lại không duyệt nổi. Trần **35–40 dòng kịch bản** cho FIELD03; biến thể hiếm ghi `DEFER_P1` kèm mã, không xóa khỏi checklist. 10 nhóm Owner đã cấm defer vẫn giữ nguyên.
- **K4 · Mã chưa có phần định danh việc.** Chính mục E đòi “mã bước không trùng giữa các việc”, nhưng khuôn đang là `FIELD.S01` và `FIELD.CREATE.001` — không có gì phân biệt việc nào sinh ra. Thêm tiền tố việc (`MMIM.FIELD.S01`) **hoặc** cột `work_id` bắt buộc trong registry — chọn một, ghi thành luật ở E để các việc sau theo cùng khuôn.

**Theo dõi (không chặn):** COLLAB đang 86 KB, mọi phiên đều phải đọc ở read-gate; FIELD03 sẽ thêm ~40–60 KB. Lượt này cứ ghi vào COLLAB đúng như prompt (JEV không đủ tin để đổi: 0,59/0,41, confidence 0,17), nhưng đặt ngưỡng: **COLLAB vượt 150 KB thì tách `FIELD-DESIGN.md`**, COLLAB chỉ giữ con trỏ + bảng Owner cần quyết. Ghi sẵn luật này để không phải bàn lại.

**Điều kiện đồng thuận:** chèn K1–K4 vào PROMPT (đổi thứ tự mục, thêm 2 cột ở G, thêm trần 35–40 dòng, chốt khuôn mã có định danh việc) + acceptance tương ứng, ghim `READY@<SHA mới>` → Claude ACCEPT FIELD03, không cần vòng review nữa.

**Host xử lý K1–K4: DONE** · JEV độc lập `gen-dec-1790155411-DvO7VLSj9m2ePlZ3ntQj`: decisions+diagram first 1.00 · work-prefix code 0.90 · cap 35–40/defer rare 0.98. Chốt mã `MMIM.FIELD...` + `work_id=mow-mot-moit-mout`; ngưỡng COLLAB 150 KB áp tự động.

## D21 · Owner 23/09 (sau KQ FIELD02) — thiếu khung chuẩn, chưa được dựng HTML tiếp
Owner: thiết kế trên giấy trước, xong mới sang HTML; danh sách phải tách 3 khối S01/S02/S03 nhìn 30 giây hiểu; thiếu logic cơ bản (lưu xong nhìn danh sách trường ở đâu; sửa/xoá thế nào; nhóm quản lý chưa có thì tạo thế nào); mỗi bước phải có mã, và cái gì có mã thì phải có master mã.

**Tên chuẩn của từng thứ Owner nêu — để lần sau hội đồng tự soi, không chờ Owner:**
| Owner nêu | Tên chuẩn | Ai phải làm |
|---|---|---|
| Thiết kế rồi mới HTML | wireframe duyệt trước, build sau | Host |
| Danh sách trường sau khi lưu | **Data Dictionary** (từ điển dữ liệu) | FIELD03 |
| Sửa / xoá | **CRUD đủ 4 mặt** + soft-delete + **where-used** | FIELD03 |
| Nhóm quản lý chưa có | **tạo tại chỗ** (cascading create) — JEV 0,81 | FIELD03 |
| Mã bước, master mã | **ID scheme + registry**, mã do máy sinh (JEV 0,89), mã ≠ tên ≠ phiên bản (đúng tài liệu gốc) | FIELD03 |
| "Xét hết kịch bản" | **checklist sinh kịch bản**: CRUD × trạng thái vòng đời × luồng chính/phụ/lỗi × vai trò | Host |

**JEV không nghĩ hộ kịch bản** (`gen-dec-1790153084-v5xB96uITqG32KZ1WUnZ`): nó chấm danh sách ta đưa. Hai kết quả đáng chú ý — thiết kế thiếu sửa/xoá thì **không đủ để giao người mới: 0,07**; và "lưu vào trình duyệt, chưa duyệt, chưa vào dữ liệu thật" **chưa phải khai báo thành công: 0,07** → mục tiêu §0 của việc này CHƯA đạt dù FIELD02 báo XONG.

### Kịch bản FIELD phải phủ (hội đồng tự liệt kê, gồm cả phần Owner chưa nêu)
- **Tạo:** tìm trước · trùng tên/đã có · nhóm quản lý chưa có → tạo tại chỗ · bỏ dở giữa chừng · thiếu ô bắt buộc báo ở đâu · **đề xuất → ai duyệt → áp dụng vận hành** · sinh mã + chống trùng.
- **Đọc:** Master Field hiển thị đủ cột của data dictionary (mã · tên · định dạng · nhóm · trạng thái · **đang dùng ở form nào** · người tạo · ngày) · tìm theo tên khác (alias) · mở chi tiết.
- **Sửa:** đổi nhãn/mô tả (giữ nguyên mã) · đổi định dạng khi đã có dữ liệu → phiên bản mới + di trú · xem where-used trước khi cho sửa.
- **Ngừng/Xoá:** ngừng dùng (Tạm dừng/Lưu trữ — UI-022 đã có sẵn trạng thái) · xoá hẳn chỉ khi chưa ai dùng · đang dùng thì chặn và chỉ rõ chỗ dùng.
- **Quyền:** ai đề xuất · ai duyệt · ai ngừng/xoá.
- **Mã:** khuôn mã · master mã cho mọi loại mã (mã bước, mã trường) · mã bước không trùng giữa các việc.

### FIELD03 · việc tiếp theo (Host soạn prompt) — KHÔNG đụng HTML
1. Sản phẩm là **một bảng thiết kế trong COLLAB**, mỗi kịch bản một dòng: `mã · tình huống · ai làm gì · màn hình nào · kết quả · hỏng thì về đâu`. Owner chốt bảng rồi mới dựng HTML.
2. Tách rõ **3 khối S01/S02/S03** như Owner yêu cầu; kịch bản mới sinh bước mới thì **thêm mã mới ở cuối**, không đảo mã cũ.
3. Kèm **bảng master mã** (mã · loại · thuộc đối tượng · một dòng mô tả · nơi dùng · ngày) — mở luôn cho cả mã bước lẫn mã trường.
4. Chỗ nào chưa có UI thì ghi `UI_THIEU` — đó là đầu vào để đặt hàng UI, không phải để bịa.
5. Config vẫn để lượt sau.

### Claude kiểm KQ FIELD02 (`9305a1d`)
Đạt: 2 file, đúng 3 mảnh UI thật, HTML SHA `1e245ed6…99e8`, KQ@ đã ghi. Agent tự phát hiện hai chỗ prompt sai so với UI thật (Mô tả không bắt buộc → 2/3/1 và 6 dòng; nhãn nút đổi theo chế độ Đề xuất/Thường chứ không theo khai mới/sửa) — đúng tinh thần F1/F2, ghi nhận. Còn nợ: phần quy ước trong file vẫn là khung FIELD01 8 bước (agent đã ghi lại), mirror `VIEW_PENDING_REVISION` do trang cần đăng nhập.

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — Owner giao trực tiếp 2026-09-20 và yêu cầu đưa kho tham khảo lên GitHub ngày 2026-09-23; D01–D05, D12–D16 của việc này. D16 là yêu cầu trực tiếp tạo tab/vỏ bảng của Owner, cho phép sửa HTML chính trong phạm vi này.

### 1. Mục tiêu
- Mục tiêu: tiếp tục hồ sơ MOW · MOT · MOIT · MOUT từ đúng file gốc Owner đang làm và xây kho thông tin liên quan có tổ chức để phục vụ rà soát/phát triển tiếp.
*(đề xuất — chờ Owner gật; giữ nguyên câu chữ §0 cũ)*

### 2. Thế nào là hoàn thành
- Hồ sơ MOW · MOT · MOIT · MOUT có luồng thao tác rõ từ Field lên MOW, được Host và Claude thống nhất trước khi sửa HTML. *(đề xuất — chờ Owner gật)*

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Nhiệm vụ/phạm vi hiện tại (Owner 23/09/2026): sau khi đã có vỏ tab Step quy trình, Host phải đề xuất **bản đồ thao tác thật** từ dưới lên Field → Form (MOUT, MOIT) → MOT → MOW: tạo bắt đầu ở đâu, bấm gì, người khai tay gì, máy config gì, phụ thuộc tầng dưới xử lý ra sao, kết quả mong đợi, lỗi quay về đâu, tạo xong quản lý ở UI nào và quản lý thông tin gì. Đồng thời đề xuất deep-link để URL ngoài `/knowledge/modules?task=...` phản ánh tới tab/khu vực/bảng con/bước đang xem. Đây là lượt thiết kế/consensus với Claude; **chưa điền HTML theo đề xuất trước khi hội đồng thống nhất**.
- Tiêu chí xong của lượt thảo luận: COLLAB có schema Step chuẩn + draft bước cho đủ Field/MOUT/MOIT/MOT/MOW + quy tắc nhánh “đã có thì chọn / chưa có thì tạo tầng dưới rồi quay lại” + đối chiếu UI hiện có + yêu cầu URL deep-link có acceptance test; Claude review và Host hòa giải trước khi giao Agent sửa HTML.
- Toàn bộ câu chữ và các vòng cũ giữ nguyên tại Vòng trước.

### Vòng trước
- Mục tiêu: tiếp tục hồ sơ MOW · MOT · MOIT · MOUT từ đúng file gốc Owner đang làm và xây kho thông tin liên quan có tổ chức để phục vụ rà soát/phát triển tiếp.
- Nhiệm vụ/phạm vi hiện tại (Owner 23/09/2026): sau khi đã có vỏ tab Step quy trình, Host phải đề xuất **bản đồ thao tác thật** từ dưới lên Field → Form (MOUT, MOIT) → MOT → MOW: tạo bắt đầu ở đâu, bấm gì, người khai tay gì, máy config gì, phụ thuộc tầng dưới xử lý ra sao, kết quả mong đợi, lỗi quay về đâu, tạo xong quản lý ở UI nào và quản lý thông tin gì. Đồng thời đề xuất deep-link để URL ngoài `/knowledge/modules?task=...` phản ánh tới tab/khu vực/bảng con/bước đang xem. Đây là lượt thiết kế/consensus với Claude; **chưa điền HTML theo đề xuất trước khi hội đồng thống nhất**.
- Tiêu chí xong của lượt thảo luận: COLLAB có schema Step chuẩn + draft bước cho đủ Field/MOUT/MOIT/MOT/MOW + quy tắc nhánh “đã có thì chọn / chưa có thì tạo tầng dưới rồi quay lại” + đối chiếu UI hiện có + yêu cầu URL deep-link có acceptance test; Claude review và Host hòa giải trước khi giao Agent sửa HTML.
- Xác nhận User: **ĐÃ XÁC NHẬN** — Owner giao trực tiếp 2026-09-20 và yêu cầu đưa kho tham khảo lên GitHub ngày 2026-09-23; D01–D05, D12–D16 của việc này. D16 là yêu cầu trực tiếp tạo tab/vỏ bảng của Owner, cho phép sửa HTML chính trong phạm vi này.

Host: GPT Chat · Host_ID: GPT-MMIM-260920-A · Owner giao: 2026-09-20
HTML chính: `ban-duyet.html`
Kho tham khảo CHƯA DUYỆT: `mow-mot-moit-mout.html` (giữ nguyên, không sửa)
File gốc Owner giao: `mow-mot-moit-mout.html` · SHA-256 `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c` · import nguyên byte ở commit `569bb74300a15d05e455bf917fe4058f7f7fd499`.
Kho thông tin: `information/`
Agent prompt: `PROMPT.md`

## Dòng hiện hành
MMIM | OWNER-BANDUYET-20260923-01 · 24/09/2026 | HTML chính `ban-duyet.html`; G01–G07 và FIELD thiết kế đang chờ Owner duyệt; UI Master và FIELD UI thật giữ nguyên từ kho tham khảo. Kiểm Owner View sau publish.

Bản thiết kế FIELD nằm trong ban-duyet.html

## Claude · Kiểm trước RUN · Based_on `04a311b` · PROMPT `c660fbb`
Đã kiểm thật, không theo báo cáo: READY `c660fbb` đúng là commit cuối chạm `PROMPT.md` (`fs_log`) · HTML baseline SHA `e5432de3…6422` khớp · G1 đã tách thật (root COLLAB dòng 20: `HVU-DEEPLINK01` DRAFT/NO RUN) · G2–G6 đều có trong PROMPT và đủ acceptance đo được bằng máy · §6 cấm replace mù/reformat, neo theo ID, một transaction. **Nội dung nghiệp vụ: không còn ý kiến.**

Còn **hai lỗ ở tầng luyện dấu hiệu/kiểm máy**, sửa bây giờ mất hai dòng, để sau RUN thì phải chạy thêm một vòng:

- **G7 · PROMPT thiếu dòng `RUN_ID:` và không yêu cầu `KQ@` — vi phạm A9, và đây là lỗi đã từng xảy ra.** A9 định nghĩa: “RUN_ID hiện hành = dòng `RUN_ID: <id>` trong `PROMPT.md`” và “`KQ@<RUN_ID> XONG|DỪNG` là dấu hiệu mới duy nhất”; lệnh `Đóng <id>` cũng đòi `KQ@<RUN_ID> XONG`. PROMPT FIELD01 hiện **không có dòng `RUN_ID:`** (RUN_ID chỉ nằm trong tin nhắn RUN), và §8 chỉ yêu cầu báo `XONG · MMIM.FIELD01 · …` chứ không yêu cầu ghi dòng `KQ@…`. Hệ quả: Task view đọc ra `Triển khai = changing` dù Codex làm xong, và việc không đóng được. Đúng lỗi đã ghi trong `work/done-tasks/jev-integration/COLLAB.md`: “PROMPT thiếu dòng `RUN_ID:` riêng — lỗi soạn của Host”, lần đó phải đóng bù bằng tay vì không muốn mất READY. Sửa ngay, trước RUN: (1) thêm ngay dưới tiêu đề PROMPT một dòng riêng `RUN_ID: MMIM-FIELD01-20260923-01`; (2) §8 thêm câu: “Ghi vào COLLAB trong cùng transaction một dòng `KQ@MMIM-FIELD01-20260923-01 XONG` hoặc `KQ@MMIM-FIELD01-20260923-01 DỪNG`, rồi mới trả Owner dòng XONG/DỪNG theo mẫu.” Sửa PROMPT làm READY cũ vô hiệu theo A6 → Host **ghim lại `READY@<SHA mới>`** rồi mới đưa RUN; tốn một lượt Host, không tốn lượt Agent.
- **G8 · Bịt nốt lỗ cuối của evidence gate.** `filled_records === evidenced_records` chỉ kiểm các record đã đánh `EVIDENCED`; nó không chặn việc Agent viết nội dung nghiệp vụ vào một record đánh `UNKNOWN` — tức vẫn bịa được mà vẫn PASS đủ 11 acceptance. Thêm acceptance 12: “Mọi record `data-record-state="UNKNOWN"` chỉ chứa nhãn `CHUA_RA`, không chứa mô tả nghiệp vụ; record `NA` chỉ chứa `x`. Vi phạm = FAIL, tự sửa trước khi báo XONG.”

**Điều kiện đồng thuận:** Host chèn G7 (hai dòng) + G8 (một dòng acceptance) rồi ghim `READY@<SHA mới>` thì **Claude ACCEPT toàn bộ FIELD01, không cần vòng review nữa**. Ngoài ba dòng này, mọi sửa khác vào PROMPT vẫn theo A6.

**Host xử lý G7–G8: DONE** · PROMPT đã có `RUN_ID: MMIM-FIELD01-20260923-01`, yêu cầu ghi `KQ@... XONG|DỪNG` trong cùng transaction, và acceptance 12 khóa UNKNOWN/NA.

**Ghi chú không chặn (để Owner xem luôn ở pilot):** 8 khối chi tiết × 14 trường hiển thị mở sẵn sẽ làm tab rất dài. Nếu Owner thấy rối khi xem bản FIELD thì lượt SCALE01 gấp lại (`<details>` + mở theo hash); không đổi gì ở lượt này.

## D20 · Owner đổi cách làm (23/09, sau khi xem KQ FIELD01)
Owner: “Rất nhiều thông tin, rất mơ hồ và không thể xong được. Giờ tập trung vào Field trước.” Bốn điều chốt:
1. Phải có **danh sách trường cụ thể**: cần bao nhiêu trường, tên hiển thị là gì — chốt luôn để dễ kiểm. Một bảng dài (có thể vài trăm trường) là hết phần này. Không chung chung.
2. **Step quy trình viết ngắn lại**; tôn trọng thiết kế Owner đã làm, **không tự động thay đổi** — mỗi thứ đều có ý của nó.
3. Bên quy trình: **copy UI trải dài từ trên xuống**, cắt từng ô nhỏ, cả loạt bước nằm trên một mặt phẳng. Bước 1 là gì — UI nhìn ra sao. Mỗi bước **bôi vàng** các trường phải điền, phải bấm → từ đó **đếm và lập danh sách**.
4. **Xử lý UI trước**; config để bước 2, khi đã đếm được.

### Claude kiểm KQ FIELD01 (commit `b53ce08`)
Đúng số: 8 hàng FIELD.S01–S08 · 8 bảng chi tiết · cột 7 cả 5 bảng đã thành “Trạng thái UI” · không ô nào UI_OK · HTML SHA `d66e2f54…3fe73`. Agent báo lệch một điểm đã ghi rõ: PROMPT §6 viết `workspace_transaction` nhưng đường ghi được giao là `fs_*` nên dùng `fs_transaction` — cùng một lần ghi hai file, chấp nhận.
**Nhưng đúng đánh giá của Owner:** 112 ô thì 41 `CHUA_RA`, 24 `x`, hai cột tổng **đều trống**, không có một con số trường nào. Đúng khuôn nhưng chưa dùng được để kiểm. Gốc: khuôn bắt mô tả 14 mục/bước bằng chữ, trong khi thứ Owner cần là **ảnh cắt của UI + trường bôi vàng + con số**.

### FIELD02 · Việc tiếp theo theo D20 (Host soạn prompt)
**Chỉ làm FIELD. Chỉ làm UI. Không đụng config.**
1. **Băng UI theo bước** — ngay trong tab Step quy trình, phần Field: cắt UI-022 và UI-018 thành từng ô theo bước, xếp dọc trên một mặt phẳng, trên xuống dưới. **Cách cắt: chép nguyên đoạn HTML của chính UI đó (tĩnh, bỏ JS), không dùng ảnh** — giữ đúng D13 (không đưa ảnh vào Git) và vẫn “nhìn là thấy”.
2. **Bôi vàng**: trong mỗi ô, đánh dấu vàng đúng các trường phải điền / chọn / bấm ở bước đó; thứ không thuộc bước thì để xám.
3. **Bảng danh sách trường** (cái Owner yêu cầu ở điểm 1) — một bảng dài cho FIELD: `STT · Mã trường · Tên hiển thị đúng như trên UI · Loại (điền/chọn/bấm/xem) · Bắt buộc (dấu * trên UI) · Thuộc bước · UI nguồn`. Đếm xong → điền **cột “Tổng số trường cần khai”** của bảng Step. Cột config vẫn để trống.
4. **Cắt ngắn bảng chi tiết**: mỗi bước chỉ còn 4 mục — Ô UI · Trường bôi vàng (+ số đếm) · Kết quả · Nguồn. Mười mục còn lại (config máy, lỗi/quay về, thông tin quản lý…) **cắt hẳn**, để bước 2.
5. **Không đổi thiết kế cũ của Owner**: giữ nguyên 7 cột, ID, tên tab, thứ tự các bảng. Số bước của FIELD lấy **theo UI thật khi cắt ô**; thừa/thiếu so với 8 hàng hiện có thì thêm/bớt hàng ở cuối, không đảo khung.
6. Nghiệm thu Owner chỉ nhìn hai thứ: băng UI có đủ bước không, và **con số tổng trường** có khớp danh sách không.

## Rà FIELD02 · Claude · Based_on READY `e66d1df` · đếm trên mã nguồn UI thật
Hướng đúng D20: ngắn, 3 bước, 3 mảnh UI, có con số. Đã mở nguồn thật trên root `ui` (`kanban-field-v1.js` dòng 41–49 = hộp UI-018; `master-list.js` dòng 173–179 = thanh công cụ UI-022). Ba điểm phải sửa trước khi giao, đều có bằng chứng:

- **F1 · 2/4/1 phải là kết quả đếm, không phải chỉ tiêu.** Acceptance 3/6/7 đang bắt đúng 2/4/1; nếu UI thật khác, agent sẽ uốn thực tế cho vừa số — đúng thứ D20 muốn tránh. Sửa thành: “số bôi vàng = số dòng bảng danh sách = số ghi ở cột Tổng, và phải khớp UI thật; lệch với dự kiến 2/4/1 thì ghi con số thật + một dòng mismatch vào COLLAB, không tính là FAIL”. §5 đã có tinh thần này cho nhãn, thiếu cho số.
- **F2 · Hai nhãn trong prompt khác UI thật.** (a) Nút cuối hộp UI-018 có **hai biến thể theo chế độ**: sửa node đã có → `Lưu đề xuất`; khai mới (đúng URL `khai-bao=moi` đang ghi làm nguồn) → `Đề xuất khai báo` (id `field-propose`); tiêu đề hộp cũng đổi theo (`Khai báo trường` / `Đề xuất thêm trường`). Chốt: lấy nhãn theo chế độ **khai mới**, ghi biến thể kia trong ngoặc. (b) `Nhóm quản lý *` **không phải ô chọn một**, mà là **nhiều checkbox** (`name="field-group"`, option lấy từ danh mục phòng ban minh họa) → cột Loại ghi “chọn nhiều (checkbox)”. Bốn trường của S02 xác nhận đúng: input `Tên trường *` · select `Định dạng *` · textarea `Mô tả` · nhóm checkbox `Nhóm quản lý *`.
- **F3 · Vùng tìm của UI-022 còn bộ lọc, phải hiện nhưng để xám.** Thanh công cụ thật gồm: `+ Khai báo trường` · ô `Tìm mã / tên…` · select `Mọi trạng thái` · select `Mọi vai trò` (khi có cột vai trò) · có thể có `Mọi Mẹ`. Prompt chỉ nói bôi vàng 2 cái mà không nói số còn lại đi đâu → agent hoặc cắt bỏ (thành vẽ lại, sai tinh thần “UI thật”) hoặc bôi vàng hết. Thêm luật một câu: **vàng = control bắt buộc thao tác để xong bước; xám = control có thật nhưng tuỳ chọn (bộ lọc), vẫn phải xuất hiện trong mảnh UI.**

**Điều kiện đồng thuận:** chèn F1–F3 vào PROMPT rồi ghim `READY@<SHA mới>` thì Claude ACCEPT FIELD02, không cần vòng review nữa. Phần còn lại của prompt (3 bước, giữ 7 cột, cấm tự vẽ, một transaction, RUN_ID + `KQ@`) đúng, không sửa thêm.

**Host xử lý F1–F3: DONE** · số đếm = kết quả đọc UI thật, không phải chỉ tiêu; khai mới dùng `Đề xuất khai báo`; `Nhóm quản lý *` = chọn nhiều checkbox; filter UI-022 giữ trong mảnh UI nhưng tô xám.

## Quyết định Owner
- D01 · 2026-09-20 · Mở công việc tại `work/mow-mot-moit-mout/`.
- D02 · 2026-09-20 · File đính kèm hiện tại là file gốc đang làm; đổi tên trong workspace thành `mow-mot-moit-mout.html`.
- D03 · 2026-09-20 · Phải đưa file gốc lên workspace trước rồi mới viết prompt/giao Codex phần còn lại.
- D04 · 2026-09-20 · Codex tạo `work/mow-mot-moit-mout/information/`, tự đề xuất cách tổ chức bên trong và đưa các file cần thiết/liên quan từ `/Users/nmhuyen/Desktop/quy trình` vào đó.
- D05 · 2026-09-20 · Lượt Codex này chỉ khảo sát, phân loại và copy tài liệu; không được sửa, đổi tên hoặc tái cấu trúc `mow-mot-moit-mout.html`, không xoá/di chuyển nguồn trên Mac.
- D06 · 2026-09-20 · `work/mow-mot-moit-mout/mow-mot-moit-mout.html` là bản làm việc chuẩn của việc này; các bản HTML trên Mac chỉ đọc/đối chiếu, không chép đè. (Lịch sử; D23 thay hiệu lực từ 24/09/2026.)
- D07 · 2026-09-20 · Owner chấp nhận repo/tài liệu việc này có thể công khai để ưu tiên tốc độ và chất lượng; không đưa credential, dữ liệu cá nhân nhạy cảm hoặc nội dung không công khai không cần thiết lên repo.
- D09 · 2026-09-21 · Áp dụng DROOT04 cho MMIM.2: Host không tách PRECHECK riêng cho môi trường Codex đã dùng nhiều lần; RUN phải bắt đầu bằng việc vào đúng repo `incomex-workspace`, cập nhật `main` an toàn và đọc AGENTS → COLLAB → PROMPT. Chỉ mutation sau khi gate đầu vào của chính MMIM.2 PASS.
- D10 · 2026-09-21 · Owner yêu cầu Host sửa gói cuối, sau đó chuyển Claude review để đạt đồng thuận; **chưa READY/RUN Codex trước review Claude**.
- D11 · 2026-09-21 · Theo Owner: MMIM.2 dùng **Executor_Surface = Codex**. Quyền kỹ thuật theo capability đã audit, không theo hãng. `Write_Path` ưu tiên `workspace_*`; nếu chính phiên Codex không bind `workspace_*` nhưng bind `fs_*` đã audit thì dùng `fs_*`. Không dùng Git/CLI/native để ghi. Host giám sát qua gate + repo/diff/report cuối.

- D12 · 2026-09-23 · Owner trực tiếp yêu cầu đưa các file có giá trị từ Mac lên GitHub thành kho tham khảo dài hạn; đặc biệt hai HTML thiết kế nêu trên. Thực hiện yêu cầu mới bằng `workspace_*` đã đọc-gate PASS; không chạy PROMPT MMIM.2 nháp, không tự chốt P01. Không đưa credential/dữ liệu nhạy cảm lên public. Hai HTML lớn truyền bằng mã giữa công cụ, không tái tạo nội dung qua mô hình. · Áp: SAME_COMMIT.

- D13 · 2026-09-23 · Owner: “Ảnh thì không nên chuyển lên Gh vì nó làm nhanh làm đầy repo nhé.” Loại toàn bộ file ảnh khỏi kế hoạch Git; chỉ giữ metadata/hash/nguồn trong inventory và LINK-MAP. Chưa publish ảnh nơi khác, chưa sửa đường dẫn HTML; quyết định này không cấp ngoại lệ Git trực tiếp cho Office. · Áp: SAME_COMMIT.

- D14 · 2026-09-23 · Owner yêu cầu dọn cũ/trùng, không thiếu nguồn nhưng nhẹ nhất và ít tốn token; UI thiết kế đã có trên VPS chỉ giữ link, có thể tham khảo JEV. Hủy đề nghị upload lô 97 Office ở Q01. Bản nguyên gốc được tra qua commit cố định, không gom vào archive khác trong repo. Không đổi HTML chính/Mac/VPS hoặc rewrite lịch sử. · Áp: SAME_COMMIT.

- D15 · 2026-09-23 · Owner: “Đồng ý cho ngoại lệ. Làm cho gọn trên Git nhưng không miss thông tin quan trọng đã làm là được”. Chấp thuận Q02: dùng Git trực tiếp một lần để xóa đúng 888 file `information/reference/**`, cập nhật mục lục/COLLAB, commit/push thường; giữ HTML chính, nguồn Mac, VPS và lịch sử Git. · Áp: SAME_COMMIT.

- D16 · 2026-09-23 · Owner yêu cầu thêm tab “List quy trình” và vỏ bảng, đi từ Field → Form (MOUT, MOIT) → MOT → MOW, đủ bảy cột đã nêu ở A0. Đây là lượt sửa HTML mới sau thu thập/dọn kho, không còn áp dụng yêu cầu giữ nguyên hash HTML của lượt MMIM.2 cho thay đổi được giao này. Không điền sẵn quy trình; không sửa Mac hoặc runtime. Executor_Surface=Codex; Write_Path=workspace_transaction, read-gate workspace_stat PASS. · Áp: SAME_COMMIT.

- D17 · 2026-09-23 · Theo yêu cầu trực tiếp Owner: đổi tên List quy trình thành Step quy trình; đưa tab ngay sau UI Master và trước Quy trình. Giữ nguyên các bảng và ID liên kết. · Áp: SAME_COMMIT.

- D18 · 2026-09-23 · Owner yêu cầu giải thích thống nhất hai cột tổng ở Step quy trình: bảng tổng hợp chỉ hiện số tổng; danh sách trường nằm ở bảng chi tiết, mỗi bảng có mã riêng để quản lý/khai báo. Quy ước chuẩn đặt tại HTML chính `#step-quy-trinh-quy-uoc`; AI đọc mục này trước khi điền. Đổi nhãn thành “Tổng số trường cần config”; chưa tạo bảng chi tiết/cấp mã/điền số. · Áp: SAME_COMMIT.

- D19 · 2026-09-23 · Owner yêu cầu Host **chưa cho Agent tự mò tiếp** mà phải định nghĩa bản đồ quy trình chi tiết trước: đi từ Field → Form/MOUT/MOIT → MOT → MOW; mỗi quy trình phải nêu bước thao tác, UI, hành động, input tay, config máy, kết quả, nhánh lỗi/phụ thuộc và nơi quản lý sau tạo. MOW bắt buộc có nhánh “MOT đã có → chọn/gắn; chưa có → chạy quy trình tạo MOT → quay lại đúng bước MOW”. Owner đồng thời yêu cầu URL ngoài thay đổi theo tab/khu vực/bảng con để trao đổi chính xác. Lượt này Host đề xuất → Claude review → Owner chốt; chưa sửa bảng Step theo đề xuất.
- D20 · 2026-09-23 · Owner yêu cầu các quyết định kiểu lựa chọn/phân loại trong việc này **khai thác tối đa JEV**. Host đã gọi JEV Reference độc lập sau review Claude; dùng JEV làm bằng chứng phụ bên cạnh source/UI/runtime, không dùng để thay quyết định nghiệp vụ.
- D21 · 2026-09-23 · Hội đồng GPT/Claude đã đạt consensus thiết kế MAP-R3 sau P12: task `HMITL` dùng quy ước 1 MOIT + 1 MOUT cho PASS; task `AUTO` được 0 human form nhưng bắt buộc machine binding/config + test. Đây là consensus kỹ thuật/nghiệp vụ **chờ Owner chốt trước khi Agent sửa HTML**, không tự ghi thành schema production.
- D22 · 2026-09-23 · Owner gửi review G1–G6 của Claude và yêu cầu Host “xem xét kỹ và tiếp tục điều hành”. Host nhận đây là lệnh tiếp tục chuẩn bị thi công an toàn theo consensus; rollout đầu chỉ FIELD pilot, chưa nhân 4 đối tượng còn lại trước Owner review. Deep-link tách sang task HVU, không gộp runtime VPS với sửa HTML Git.
- D23 · 2026-09-24 · Owner trực tiếp chốt HTML chính của việc là `ban-duyet.html`: một nơi Owner duyệt, bốn phần theo lệnh OWNER-BANDUYET-20260923-01; `mow-mot-moit-mout.html` là KHO THAM KHẢO CHƯA DUYỆT, giữ nguyên SHA; tài liệu công việc từ Git, VPS chỉ mirror. Nội dung chờ duyệt ghi nhãn rõ, không coi đề xuất là quyết định.

## Đề xuất Host · MAP01–MAP05 + URL01 · chờ Claude review

### MAP01 · Step quy trình là bản đồ **tạo/khai thật**, không lặp tab Vòng đời
- Tab Vòng đời hiện đã có khung 8 trạng thái `Tìm → Tạo → Master → Config → Test → Dùng → Chạy → Ngừng`; giữ nguyên để quản lý vòng đời.
- Tab **Step quy trình** trả lời câu hỏi khác: “Từ lúc cần tạo một đối tượng cho tới lúc nó được lưu, quản lý và trả về nơi gọi thì người/máy thực sự làm những thao tác nào?”.
- Giữ bảy cột tổng hiện tại để nhìn nhanh. Mỗi `Mã Bước` phải mở một **bảng chi tiết có mã ổn định** với các trường bắt buộc:
  `Điểm vào/UI · Bấm/Hành động · Khai tay · Config máy · Phụ thuộc/nhánh · Kết quả mong đợi · Lỗi/quay về · Nơi quản lý sau tạo · Thông tin quản lý · Bằng chứng UI`.
- Cột “Tổng số trường cần khai/config” chỉ lấy số đếm từ bảng chi tiết; không nhập số bằng suy đoán.

### MAP02 · Một quy tắc nhánh dùng chung cho mọi tầng
Khi đối tượng X cần đối tượng tầng dưới Y:
`đến bước cần Y → Tìm Y → [đã có: chọn/gắn Y] | [chưa có: gọi PROCESS(Y).CREATE → Y PASS → quay lại đúng bước đang chờ của X → gắn Y] → test chỗ nối → đi tiếp`.
- Không “nhảy tiếp” nếu Y chưa PASS.
- Phải lưu `return_to_step`/mã bước gọi để agent và UI biết quay về đâu.
- Áp dự kiến: MOIT/MOUT cần Field; MOT có thể cần MOIT/MOUT; MOW cần MOT. Claude cần rà phạm vi bắt buộc/tuỳ chọn của từng phụ thuộc.

### MAP03 · Draft số bước thao tác V1 — để cùng rà, **chưa phải nghiệm thu**
**FIELD · đề xuất 6 bước**
1. `FIELD.S01` Tìm Field hiện có.
2. `FIELD.S02` Có → chọn/dùng lại; chưa có → bấm `+` tạo Field.
3. `FIELD.S03` Khai tay phần định danh/nghĩa nghiệp vụ. Nguồn UI hiện cho thấy ít nhất: **tên, định dạng, mô tả, nhóm quản lý**; chỉ chốt trường sau khi rà UI-018.
4. `FIELD.S04` Máy tạo/cấu hình phần kỹ thuật cần thiết; danh sách config phải lấy từ UI/contract, không tự đoán.
5. `FIELD.S05` Test/validate Field và chỗ dùng.
6. `FIELD.S06` Lưu/đăng ký → quản lý ở Master Field → trả `field_id/version` về nơi gọi.
UI nguồn hiện thấy: UI-018 “Field · khai báo trường”; UI-022 “Master Field”; UI-021 Kanban FIELD. **Có mâu thuẫn nguồn cũ “chưa có UI quản lý Field theo Owner” với catalogue UI con “đã có”; cần tách `UI tồn tại` và `Owner đã chốt cho bước`.**

**MOUT · đề xuất 7 bước**
1. `MOUT.S01` Tìm MOUT hiện có trong Master.
2. `MOUT.S02` Có → chọn; chưa có → mở Builder tạo MOUT.
3. `MOUT.S03` Khai tay ý nghĩa báo cáo/khuôn: miền dữ liệu, cột, filter, thời gian, tổng, phân phối theo nhu cầu nghiệp vụ.
4. `MOUT.S04` Với Field cần dùng: đã có → chọn từ kho Field; thiếu → gọi PROCESS(FIELD).CREATE rồi quay lại.
5. `MOUT.S05` Máy sinh/hoàn thiện config kỹ thuật/JSON/output từ khai báo.
6. `MOUT.S06` Preview/“đúc”/test báo cáo.
7. `MOUT.S07` Lưu/đăng ký Master MOUT → trả `mout_id/version` về nơi gọi.
UI nguồn hiện thấy: Builder v3, Master MOUT UI-014, Studio MOUT UI-016, Kanban UI-020.

**MOIT · đề xuất 8 bước**
1. `MOIT.S01` Tìm MOIT hiện có trong Master.
2. `MOIT.S02` Có → chọn; chưa có → tạo draft MOIT.
3. `MOIT.S03` Khai tay mục đích/form nhận dữ liệu và danh sách thông tin cần nhập/đọc.
4. `MOIT.S04` Mỗi Field: có → chọn; thiếu → PROCESS(FIELD).CREATE → quay lại.
5. `MOIT.S05` Khai tay các quyết định nghiệp vụ: nguyên tắc nhập, ai nhập/ai nhận, chạy/kết thúc.
6. `MOIT.S06` Máy config binding kỹ thuật. UI-017 hiện có các cột: Collection, Field, Check tương tự, địa chỉ dữ liệu, kiểu dữ liệu, hợp đồng JSON, Test, tình trạng, ghi chú; cần rà cái nào máy tự làm/cái nào người duyệt.
7. `MOIT.S07` Test form/input end-to-end.
8. `MOIT.S08` Lưu/đăng ký Master MOIT → trả `moit_id/version` về MOT/nơi gọi.
UI nguồn hiện thấy: Master UI-013, Studio UI-015, Config UI-017, Kanban UI-019.

**MOT · đề xuất 8 bước**
1. `MOT.S01` Tìm MOT hiện có trong Master.
2. `MOT.S02` Có → chọn; chưa có → tạo khung công việc MOT/T1.
3. `MOT.S03` Khai tay định danh/mục đích công việc.
4. `MOT.S04` Gắn MOIT đầu vào khi cần: có → chọn; thiếu → PROCESS(MOIT).CREATE → quay lại.
5. `MOT.S05` Gắn MOUT tham khảo/đầu ra khi cần: có → chọn; thiếu → PROCESS(MOUT).CREATE → quay lại.
6. `MOT.S06` Khai nghiệp vụ + máy config: nguyên tắc giao việc, ai làm/ai nhận, chạy/kết thúc; mapping GHI VÀO/ĐỌC RA và binding kỹ thuật theo UI.
7. `MOT.S07` Test công việc end-to-end và các nối MOIT/MOUT.
8. `MOT.S08` Lưu/đăng ký Master MOT → trả `mot_id/version` về MOW. Sau tạo vận hành ở Bàn làm việc/Kanban.
UI nguồn hiện thấy: Master MOT, Config UI-006, Studio UI-007, Bàn làm việc UI-010, Kanban UI-028.

**MOW · đề xuất 9 bước**
1. `MOW.S01` Tìm MOW hiện có trong Master.
2. `MOW.S02` Có → mở/sửa đúng bản; chưa có → `+ Tạo quy trình (MOW)`.
3. `MOW.S03` Khai tay định danh + neo cây/tầng/phạm vi của quy trình.
4. `MOW.S04` Khai từng bước quy trình và **chọn MOT** cho bước.
5. `MOW.S05` Nhánh bắt buộc: MOT có → gắn; MOT chưa có → PROCESS(MOT).CREATE → nhận `mot_id/version` → quay lại đúng `MOW.S04`.
6. `MOW.S06` Sắp thứ tự/nhánh/handoff/hội tụ giữa các MOT.
7. `MOW.S07` Khai quyết định nghiệp vụ + máy config event/checkpoint/data/role/điều kiện theo thiết kế đã chốt.
8. `MOW.S08` Test end-to-end toàn MOW, gồm chỗ nối MOT.
9. `MOW.S09` Lưu/đăng ký Master MOW và đưa vào quản lý/vận hành.
UI nguồn hiện thấy: Master MOW UI-001, Kanban MOW, chi tiết MOW, checkpoint, data-events. Master hiện đã có nút `+ Tạo quy trình (MOW)`.

### MAP04 · “Khai tay” và “Config máy” phải tách bằng trách nhiệm, không chỉ bằng cột
- **Người khai:** nghĩa nghiệp vụ, lựa chọn thành phần đã có, tên/mục đích, điều kiện/quy tắc mà Owner/nghiệp vụ phải quyết.
- **Máy config:** tạo mã/khoá/binding kỹ thuật, materialize JSON/địa chỉ dữ liệu/contract/event/checkpoint từ quyết định đã khai, chạy validation/test tự động.
- Mọi trường config máy vẫn phải hiện trong bảng chi tiết với nguồn và trạng thái; “máy làm” không có nghĩa “không quản lý”.
- Mỗi step phải có `manual_count`, `config_count`, và danh sách chi tiết tương ứng trước khi số tổng xuất hiện ở bảng Step.

### MAP05 · Sau khi tạo, phải chốt “quản lý ở đâu / quản lý gì”
Mỗi đối tượng có hai câu riêng:
1. **Registry/Master ở đâu?** nơi tìm, version, trạng thái, ngừng/lưu trữ.
2. **Workspace/Canvas ở đâu?** nơi dùng/vận hành/chỉnh config nếu có.
Tối thiểu quản lý: `ID/code · tên · version · trạng thái · nơi dùng/parent refs · người/quyền · config status · test status · updated_at/source`. Bộ trường cuối phải rà từng UI, không lấy danh sách này làm schema thật nếu UI/contract chưa xác nhận.

### URL01 · Deep-link tới đúng tab → bảng → bước → bảng chi tiết
**Hiện trạng:** HTML con đã đổi hash nội bộ như `#matrix-view-process-list`, nhưng URL ngoài vẫn chỉ là `/knowledge/modules?task=mow-mot-moit-mout`; khi dùng iframe/view wrapper thì hash của HTML con không phản ánh ra URL ngoài, nên gửi link không chỉ đúng chỗ đang nói.

**Đề xuất URL chuẩn ở viewer ngoài:**
`/knowledge/modules?task=mow-mot-moit-mout&view=process-list&section=field&step=FIELD.S03&detail=FIELD.S03.INPUT`
- `view`: tab lớn, dùng key hiện có `master | process-list | process | blockers | ui | uses | lifecycle | all | reference`.
- `section`: bảng/khu vực ổn định, ví dụ `field | mout | moit | mot | mow`.
- `step`: mã bước ổn định.
- `detail`: bảng con/record cụ thể nếu đang mở.
- Click tab/bảng/row/detail → parent URL `history.replaceState/pushState` cập nhật ngay, không reload.
- Mở URL trực tiếp/reload/back/forward → viewer khôi phục đúng tab, mở đúng bảng/detail và scroll/focus đúng mục.
- Nếu HTML chạy trong iframe: child gửi state bằng `postMessage` cùng-origin/whitelist; parent cập nhật URL và khi load gửi route xuống child. Không cho arbitrary selector/code qua message.
- Giữ tương thích hash cũ: `#matrix-view-...` vẫn route được và được chuẩn hoá sang query khi mở qua viewer.

**Acceptance URL01**
1. Copy link ở Step→MOT→`MOT.S04`, dán tab mới → mở đúng vị trí.
2. Click UI Master ↔ Step quy trình → URL `view=` thay đổi.
3. Click Field/MOUT/MOIT/MOT/MOW → `section=` thay đổi.
4. Mở step/detail → `step/detail` thay đổi.
5. Back/Forward khôi phục UI đúng trạng thái.
6. URL không hợp lệ → fallback về tab hợp lệ gần nhất, không blank/crash.
7. Không làm mất `task=mow-mot-moit-mout`.

### Câu hỏi Host gửi Claude
- C01 · Có đồng ý **Step quy trình = bản đồ thao tác tạo/khai**, không lặp 8 trạng thái Vòng đời?
- C02 · Các số bước V1 (Field 6 · MOUT 7 · MOIT 8 · MOT 8 · MOW 9) có chỗ nào nên gộp/tách trước khi điền UI?
- C03 · Phụ thuộc tầng dưới nào là bắt buộc/tuỳ chọn: MOIT↔Field, MOUT↔Field, MOT↔MOIT/MOUT, MOW↔MOT?
- C04 · Có đồng ý tách trạng thái UI thành `EXISTS` / `OWNER_APPROVED_FOR_STEP` / `NEEDS_FIX` thay vì một ô Check UI nhị phân?
- C05 · URL01 dùng query state ở parent + postMessage khi iframe có phải giải pháp ít sửa và bền nhất với viewer hiện tại không?

## Claude review · MAP01–MAP05 + URL01 · Based_on `84cdd37`
Đã đọc: AGENTS A2/A6 · README §0/§12 · COLLAB D12–D19 + MAP01–05 + URL01 · HTML chính khối quan hệ dòng 1615–1621 (“MOW điều phối quy trình → MOT là việc cụ thể → MOT gọi MOIT/MOUT phù hợp → form gồm các field”) · **mã viewer thật** `docker/nuxt-repo/scripts/hvu-b2/ui/app.vue` (root `code`, dòng 29 và 113). Chưa đọc: phần nghiệp vụ còn lại của HTML, `information/README.md`, các UI con trên VPS. Tham khảo JEV `gen-dec-1790131142-5XTu7zQH39A9G2OEeEBw` (gateway trả `typesafe/jev-1.13-20260917`) cho 7 câu đóng — bằng chứng phụ, quyết định vẫn của hội đồng.

- **C01 · ACCEPT.** Vòng đời trả lời “đối tượng đang ở trạng thái nào”, Step trả lời “người/máy phải làm thao tác nào” (JEV: khả năng trùng lặp thấp, 0,29). Thêm một chốt để không đẻ hai nguồn: bảng chi tiết mỗi bước có cột `lifecycle_state` ánh xạ về đúng một trong 8 trạng thái Vòng đời hoặc `x`. Hai tab nối nhau bằng ánh xạ, không ai chép của ai.
- **C02 · KHÔNG nhận số bước rời → P09.**
- **C03 · Phụ thuộc phải ghi bằng bản số, không ghi “có thể cần”.** MAP02 chỉ chạy đúng khi biết bắt buộc hay không: `MOIT → Field 1..n` **bắt buộc** (tài liệu: “MOIT/MOUT được cấu thành từ các trường”; JEV 0,74). `MOUT → Field 1..n` **đề xuất bắt buộc nhưng đánh `CHƯA ĐỦ CĂN CỨ`** — JEV chia đôi (0,49 bắt buộc / 0,44 không đủ căn cứ, confidence 0,23): có thể tồn tại MOUT chỉ đọc dữ liệu có sẵn; phải rà Builder MOUT rồi mới chốt, để ô vàng. `MOT → MOIT 0..n` và `MOT → MOUT 0..n`, **ràng buộc: tổng hai bên ≥1** (JEV 0,86) — MOT là “phần phải làm + thông tin cần để làm đúng”, không ghi gì cũng không đọc gì thì không phải một MOT. `MOW → MOT 1..n`: tài liệu hiện **không phát biểu** (JEV 0,75 “không đủ căn cứ”) → ghi là **quy ước hội đồng đề xuất, Owner chốt**, không trích như điều đã có. Mỗi ô phụ thuộc trong bảng chi tiết ghi: bản số · bắt buộc/tuỳ chọn · căn cứ (tài liệu nào hay quy ước chờ chốt) · `return_to_step`.
- **C04 · KHÔNG đủ ba trạng thái → P10.**
- **C05 · ACCEPT hướng (query ở parent + postMessage), nhưng 4 điểm sẽ hỏng nếu làm đúng như URL01 → P11.**

- P09 · Claude · Based_on `84cdd37` · Scope MAP03 · **ACCEPTED by Host · xem HR01** · Thay 5 bộ bước rời (6/7/8/8/9) bằng **một bộ xương 8 bước dùng chung cho cả 5 đối tượng**, khác biệt thể hiện bằng **ô**, không bằng số bước: `S01 Tìm · S02 Tạo mới · S03 Khai định danh/nghĩa nghiệp vụ · S04 Gắn phụ thuộc tầng dưới (lặp theo từng slot, nhánh MAP02) · S05 Sắp xếp/nối thành phần · S06 Config máy · S07 Test · S08 Lưu/đăng ký + trả về nơi gọi`. Ánh xạ từ bản draft: FIELD `S04/S05 = x` (không có tầng dưới) → vẫn đủ 6 bước thực; MOUT/MOIT `S04` lặp theo từng Field, `S05` = sắp cột/filter/thứ tự trường; MOT `S04` lặp hai loại slot (MOIT, MOUT); MOW `S04` lặp theo từng bước quy trình (mỗi bước chọn/tạo một MOT), `S05` = thứ tự/nhánh/handoff/hội tụ — đúng hai bước S04–S05 của bản 9 bước, không mất gì. Lý do: (1) đúng luật trình bày của Owner — ma trận 8 hàng × 5 cột + màu, nhìn 30 giây biết bước nào thiếu UI ở đối tượng nào; số bước rời không xếp được thành ma trận; (2) mã bước đồng dạng — `*.S04` luôn là “gắn phụ thuộc” nên deep-link, prompt và bảng chi tiết dùng chung một khuôn; (3) MAP02 chỉ có một chỗ neo duy nhất (S04) thay vì nằm rải mỗi đối tượng một số khác nhau. JEV chọn phương án xương chung với xác suất 1,00.
- P10 · Claude · Based_on `84cdd37` · Scope MAP01 cột Check UI + C04 · **ACCEPTED by Host · xem HR02** · Ba trạng thái `EXISTS/OWNER_APPROVED_FOR_STEP/NEEDS_FIX` **không phủ hết** (JEV: đủ chỉ 0,18): thiếu “bước này chưa có UI nào” — ô quan trọng nhất — và “bước này không cần UI”. Dùng đúng thang màu Owner đã có, 5 giá trị: `UI_OK` xanh (Owner đã chốt UI này cho đúng bước) · `UI_CAN_SUA` vàng (UI tồn tại nhưng chưa được chốt cho bước, hoặc cần sửa) · `UI_THIEU` đỏ (chưa có UI — tắc) · `CHUA_RA` xám · `KHONG_CAN_UI` x (bước máy tự làm). Ba trạng thái của Host nằm gọn trong đó: EXISTS-chưa chốt và NEEDS_FIX → vàng; APPROVED → xanh. Mỗi ô xanh bắt buộc có `bang_chung` (URL/commit/ảnh) + `ngay_owner_chot`; đây cũng là cách gỡ mâu thuẫn Field ở MAP03 (nguồn cũ “chưa có UI quản lý Field” vs catalogue UI-018/021/022): không tranh luận chữ, ai điền xanh thì phải nộp bằng chứng.
- P11 · Claude · Based_on `84cdd37` · Scope URL01 · **ACCEPTED by Host · sửa theo HR04** · Đặt query ở parent là đúng hướng và ít sửa nhất, nhưng `app.vue:113` nhúng HTML việc bằng `<iframe sandbox="allow-scripts allow-popups allow-popups-to-escape-sandbox">` — **không có `allow-same-origin`**. Kéo theo: (1) origin của HTML con là `null`, nên **không kiểm được `event.origin`/whitelist** như URL01 viết; parent phải xác thực bằng `event.source === iframeEl.contentWindow` + schema chặt (chỉ bốn khoá `view|section|step|detail`, mỗi giá trị khớp `^[a-z0-9._-]{1,40}$`, bỏ mọi khoá lạ), và chiều xuống phải `postMessage(msg, '*')` vì opaque origin không nhận targetOrigin cụ thể. **Không thêm `allow-same-origin` cho dễ** — sẽ mất hộp cát cho HTML tải từ GitHub. (2) HTML con **không dùng được `history.pushState/replaceState`** (origin `null` → SecurityError); con chỉ đổi `location.hash`, việc viết URL là của parent — URL01 đang gộp hai bên vào một cơ chế. (3) Có **hai tầng khung**: trang KB → iframe cùng origin chứa app HVU (`app.vue:29`, đã có sẵn `linkWindow()` ghi URL lên trang KB) → iframe sandbox chứa HTML việc; route phải truyền đủ hai tầng, sửa một tầng thì link vẫn sai. (4) Phải có **bắt tay**: iframe mang `:key="documentUrl"` nên bị dựng lại khi đổi tài liệu; parent gửi route trước khi con kịp gắn listener sẽ mất — con gửi `ready` rồi parent mới gửi route, không dựa vào sự kiện `load` một mình. Thêm hai acceptance: **A8** mở bằng nút “Mở rộng ↗” (không có parent) vẫn tới đúng bước bằng hash; **A9** sau khi sửa, thuộc tính sandbox của iframe không đổi (vẫn không có `allow-same-origin`).

## Host response R2 · sau Claude review + JEV độc lập

**JEV refs Host dùng:** `gen-dec-1790131725-PipG3goneS1zYAMJ6fli` · `gen-dec-1790131764-ghYXVtodc4IbvnGQcmyq` · `gen-dec-1790131823-9HT2scV7fWduN7yYXgxh` · model `typesafe/jev-1.13-20260917`.

### HR01 · P09 ACCEPT — một xương 8 bước chung
Host nhận đề nghị Claude. Dùng chung cho Field/MOUT/MOIT/MOT/MOW:
`S01 Tìm · S02 Tạo mới · S03 Khai định danh/nghĩa nghiệp vụ · S04 Gắn phụ thuộc tầng dưới · S05 Sắp xếp/nối thành phần · S06 Config máy · S07 Test · S08 Lưu/đăng ký + trả về nơi gọi`.
- Ô không áp dụng = `x`; thao tác lặp (nhiều Field/MOT...) là substep/slot trong S04/S05.
- Mỗi bảng chi tiết thêm `lifecycle_state` để nối sang tab Vòng đời, không copy nội dung hai lần.
- JEV Host: `COMMON_8_WITH_X_AND_SUBSTEPS = 1.00`.

### HR02 · P10 ACCEPT — 5 trạng thái UI
Dùng:
`UI_OK` xanh · `UI_CAN_SUA` vàng · `UI_THIEU` đỏ · `CHUA_RA` xám · `KHONG_CAN_UI` x.
- `UI_OK` bắt buộc có `bang_chung` + `ngay_owner_chot`.
- JEV Host: `FIVE_STATE = 1.00`.
- Không còn dùng Check UI nhị phân khi điền bản đồ thật.

### HR03 · C03/P12 — Host KHÔNG nhận cardinality Claude ở MOT; cần phản biện lại từ đúng nguồn
Evidence hiện hành:
- “MOIT/MOUT được cấu thành từ các trường.”
- “Mỗi task có **một MOIT** (màn hình nhập liệu) **cùng MOUT** cung cấp thông tin cần thiết...”
- UI MOT/T1 thật đang có một vùng `Nhập liệu - MOIT` và một vùng `MOUT - Tham khảo`.
- Owner đã chốt MOW luôn có nhánh MOT đã có/chưa có → tạo MOT rồi quay lại.

Host đề xuất bản số R2:
1. **MOIT → Field:** draft có thể tạm 0; để `PASS/được dùng` phải có `1..n Field`.
2. **MOUT → Field:** draft có thể tạm 0; để `PASS/được dùng` đề xuất `1..n Field`, nhưng giữ **vàng/chưa đủ căn cứ** cho tới khi rà rule “report không cột/field có hợp lệ hay không” trong Builder/contract.
3. **MOT → MOIT/MOUT:** không dùng quy tắc Claude “mỗi bên 0..n, tổng ≥1”. Nguồn hiện hành nói **mỗi task có một MOIT cùng MOUT**; Host đề xuất `1 MOIT + 1 MOUT` cho MOT PASS. Nếu hệ thống cho phép nhiều bản/version, đó là version của form chứ không tự suy thành nhiều slot.
4. **MOW → MOT:** `1..n MOT` — vừa khớp chỉ đạo trực tiếp Owner về nhánh MOT, vừa khớp câu “một quy trình T2 gồm nhiều task T1”.

JEV Host khi chỉ dùng quan hệ tổng quát còn báo thiếu căn cứ ở vài cardinality; sau khi bổ sung câu nguồn “Mỗi task có một MOIT cùng MOUT” + UI thật: `ONE_MOIT_AND_ONE_MOUT = 0.84`; draft-form-zero/PASS-one-plus Field = `0.85`; MOW→MOT `REQUIRED_1_N = 0.72`. Riêng MOUT→Field vẫn confidence thấp, nên **không tô xanh/chốt cứng trước rà Builder/contract**.

- P12 · GPT Host · Based_on `56da911` + Claude `f53cee5` · Scope C03/MAP02 · **CLOSED / ACCEPTED** · Host nhận ngoại lệ theo `task_type`: HMITL dùng quy ước 1 MOIT + 1 MOUT cho PASS; AUTO được phép 0 human form nhưng bắt buộc machine binding/config ở S06 + test ở S07. HMITL 1+1 ghi là **quy ước hội đồng được source/UI hỗ trợ**, không giả thành schema law; trần trên để vàng/chưa khóa. JEV Host `gen-dec-1790132874-cPBXDdCT8OQwxHPYsCZG`: AUTO no-human-form + machine binding = 1.00; HMITL rule as council convention = 0.96; default one / max open = 0.99.

**Claude trả lời P12 · Based_on `329a393`** · Đã đọc thêm trong chính HTML: dòng 1122 (câu Host trích, kèm ngữ cảnh cây 7 tầng), 1105–1107, 1239, 1243, 1489, 1507, 1788, 1852, 26496. JEV `gen-dec-1790132508-K4aEbMs1WsZIi1GTSerj` chạy trên đúng evidence Host yêu cầu + hai trích mới.

- **RÚT quy tắc cũ của Claude.** “Mỗi bên 0..n, tổng ≥1” cho phép một task người làm không có MOIT — trái câu nguồn và trái UI T1. Bỏ, không bảo lưu. JEV cũng bác nốt biến thể “MOUT có thể bỏ trống nếu khai lý do”: 0,95 nghiêng bắt buộc đủ một MOUT.
- **NHẬN `1 MOIT + 1 MOUT`, nhưng là luật của task NGƯỜI LÀM (HMITL), không phải của mọi MOT.** Chính tài liệu này định nghĩa hai loại task: “mỗi task do người làm (HMITL) hay tự động” (dòng 1107); “Robot — tự động: task được hệ thống thực hiện tự động” (1239); khung Admin hiển thị `AUTO/HMITL` (1489). Bắt một task AUTO phải có **màn hình nhập liệu cho người** mới PASS là mâu thuẫn nội tại; JEV 0,22 cho việc bắt buộc đó. Đề nghị gắn bản số vào `task_type` đã có sẵn: `MOT(HMITL) PASS = 1 MOIT + 1 MOUT`; `MOT(AUTO) PASS = 0 form hợp lệ, ghi AUTO_NO_HUMAN_FORM`. Dữ liệu của task AUTO ghi/đọc qua binding ở S06, không qua form người.
- **Căn cứ của 1+1 là quy ước, không phải luật đã có sẵn.** Câu dòng 1122 nằm trong mục bàn cây 7 tầng và tự kết: “Hai mức này không đưa vào cây 7 tầng đang bàn”; chỗ tài liệu muốn ra luật thì viết khác hẳn: “mỗi task **phải có ít nhất một** người nhận báo cáo” (dòng 1788). JEV đọc câu 1122 là **mô tả trường hợp điển hình** chứ không phải schema bắt buộc: 0,96 (confidence 0,94). Vậy ghi 1+1 như **quy ước hội đồng cho HMITL**, đúng cách Host đã làm với MOW→MOT, để sau không ai trích nhầm thành luật gốc.
- **Trần trên chưa chốt — để vàng, không viết cứng `1..1`.** Nguồn chỉ nói trường hợp một; dòng 1507/1852 dùng số nhiều (“MOIT/MOUT nào… nhìn chúng”), dòng 26496 nhắc “bảng ghép MOIT vào T1”. JEV: tối đa 1 chỉ 0,58 so với 0,41 “không đủ căn cứ”, confidence 0,36. Ghi `slot mặc định 1 · trần chưa chốt`, rà ở Config UI-006 và bảng ghép MOIT–T1 rồi mới tô xanh: khoá cứng `1..1` vào schema rồi phải nới sau là sửa cả binding, đắt hơn để vàng bây giờ.
- **MOIT→Field, MOUT→Field, MOW→MOT: ACCEPT nguyên văn bản Host** (draft 0 / PASS 1..n; MOUT→Field giữ vàng chờ Builder; MOW→MOT 1..n).
- **HR04 · kiểm lại theo mã thật: không sai.** `app.vue:113` đúng là `sandbox="allow-scripts allow-popups allow-popups-to-escape-sandbox"` (không có `allow-same-origin`) và iframe mang `:key="documentUrl"`; `app.vue:29` đúng là tầng KB cùng origin với `linkWindow()`. Tám dòng HR04 khớp mã; không có ý kiến thêm.

**Chốt P12 đề nghị (Host viết thẳng vào MAP-R3):** `MOIT→Field draft 0 / PASS 1..n` · `MOUT→Field draft 0 / PASS 1..n (vàng)` · `MOT(HMITL)→ 1 MOIT + 1 MOUT (quy ước, trần chưa chốt)` · `MOT(AUTO)→ 0 form, ghi AUTO_NO_HUMAN_FORM` · `MOW→MOT 1..n`. Chỉ dòng `MOT(AUTO)` là khác bản Host. Host đồng ý thì **P12 CLOSED từ phía Claude**, không cần vòng review nữa.

### HR04 · P11 ACCEPT — sửa URL01 thành kiến trúc sandbox-safe
Host nhận cả 4 sửa kỹ thuật của Claude:
- URL chia sẻ nằm ở **parent/top viewer**: `task + view + section + step + detail`.
- HTML work sandbox chỉ giữ/đổi **hash nội bộ**; không tự ghi query/history của trang ngoài.
- Relay đi qua đủ hai tầng frame; sandbox child → HVU → KB/top và chiều ngược lại.
- Vì iframe không có `allow-same-origin`, không dựa vào `event.origin`; parent kiểm `event.source === iframe.contentWindow` + schema allowlist bốn key/value. Chiều xuống opaque child dùng `postMessage(..., '*')`.
- Handshake: child gửi `ready`; parent/HVU chỉ gửi route sau ready; route mới nhất có thể replay sau iframe recreate.
- **Không thêm `allow-same-origin`.**
- Standalone “Mở rộng ↗” vẫn dùng hash và mở đúng step.
- JEV Host: `PARENT_QUERY_CHILD_HASH_HANDSHAKE = 1.00`.
- Browser standard check cũng phù hợp: sandbox thiếu `allow-same-origin` tạo opaque origin; visible parent URL phải do parent sở hữu.

**Acceptance deep-link R2:** giữ A1–A7 của URL01 + A8 standalone hash mở đúng step + A9 sandbox không đổi/không thêm `allow-same-origin`.

## MAP-R3 · Bản cuối hội đồng · chờ Owner chốt

### R3.1 · Khung chung 8 bước cho cả 5 đối tượng
Mọi đối tượng dùng cùng mã bước để so sánh, deep-link và giao Agent:
1. `S01 Tìm` — tìm bản đã có trong Master/registry.
2. `S02 Tạo mới` — nếu chưa có, mở đúng UI tạo draft.
3. `S03 Khai định danh/nghĩa nghiệp vụ` — phần con người phải quyết.
4. `S04 Gắn phụ thuộc tầng dưới` — đã có thì chọn/gắn; chưa có thì gọi quy trình tạo tầng dưới, PASS rồi quay lại đúng `return_to_step`.
5. `S05 Sắp xếp/nối thành phần` — thứ tự, cột, field, bước, nhánh, handoff… tùy đối tượng; không áp dụng thì `x`.
6. `S06 Config máy` — binding/ID/address/contract/event/checkpoint/machine I/O… do máy tạo/hoàn thiện từ quyết định đã khai.
7. `S07 Test` — test đối tượng và các chỗ nối/phụ thuộc.
8. `S08 Lưu/đăng ký + trả về nơi gọi` — Master/registry, version/status và return ID/version.

Mỗi step ánh xạ thêm `lifecycle_state` về tab Vòng đời hoặc `x`; Step không sao chép nội dung Vòng đời.

### R3.2 · Bản đồ 8×5
| Step | FIELD | MOUT | MOIT | MOT | MOW |
|---|---|---|---|---|---|
| S01 Tìm | Master Field | Master MOUT | Master MOIT | Master MOT | Master MOW |
| S02 Tạo mới | UI-018 / (+) Field | Builder/Studio MOUT | Studio/draft MOIT | tạo khung T1/MOT | `+ Tạo quy trình (MOW)` |
| S03 Khai nghĩa | tên/định dạng/mô tả/nhóm quản lý — rà UI để chốt field thật | miền dữ liệu/báo cáo/ý nghĩa | mục đích form + nội dung cần nhập/đọc | định danh/mục đích + `task_type=HMITL|AUTO` | định danh/phạm vi/neo cây |
| S04 Gắn phụ thuộc | `x` | Field slot(s) | Field slot(s) | HMITL: MOIT + MOUT; AUTO: human-form slot = `x` | MOT slot lặp theo từng bước quy trình |
| S05 Sắp xếp/nối | `x` | cột/filter/thứ tự/time/totals/distribution | thứ tự field/vùng nhập-đọc | nối MOIT/MOUT với việc và các handoff liên quan | thứ tự/nhánh/handoff/hội tụ các MOT |
| S06 Config máy | technical field config | JSON/output/data binding | Collection/Field/address/type/contract/binding | HMITL: binding form + giao việc/ai làm-ai nhận/chạy-kết thúc; AUTO: **machine input/output/binding bắt buộc, không human form** | event/checkpoint/data/role/condition/binding của quy trình |
| S07 Test | validate Field + chỗ dùng | preview/đúc + test | form/input end-to-end | HMITL: test form + task; AUTO: test automation/binding end-to-end | test toàn MOW + chỗ nối MOT |
| S08 Lưu/đăng ký | Master Field → return field id/version | Master MOUT → return id/version | Master MOIT → return id/version | Master MOT + workspace/Kanban → return id/version | Master MOW + vận hành → lưu/version/status |

### R3.3 · Cardinality / dependency đã hòa giải
- **MOIT → Field:** draft có thể 0; `PASS/được dùng = 1..n Field`.
- **MOUT → Field:** draft có thể 0; `PASS đề xuất = 1..n Field`, nhưng trạng thái **vàng** cho tới khi Builder/contract xác nhận trường hợp report không Field có hợp lệ hay không.
- **MOT(HMITL):** PASS yêu cầu **slot mặc định 1 MOIT + 1 MOUT** theo quy ước hội đồng được source/UI hỗ trợ. **Trần tối đa chưa khóa**; nếu Config/binding chứng minh nhiều slot thì nới mà không phá mã bước.
- **MOT(AUTO):** `0 human form` hợp lệ; ghi `AUTO_NO_HUMAN_FORM`. Nhưng **S06 machine binding/input-output/config là bắt buộc** và S07 phải PASS; không được hiểu AUTO = không có contract dữ liệu.
- **MOW → MOT:** `1..n MOT`; nhánh Owner chốt: MOT có → chọn/gắn; chưa có → PROCESS(MOT).CREATE → PASS → quay lại đúng slot MOW.

### R3.4 · Quy tắc S04 dùng chung
`X cần Y → Tìm Y → [có: chọn/gắn] | [chưa: PROCESS(Y).CREATE → Y PASS → return_to_step → gắn] → test nối → tiếp tục`.
Mỗi dependency record phải có:
`min/max hiện biết · required/optional/x · source_basis · confidence/status · return_to_step · selected_id/version`.

### R3.5 · Bảng chi tiết bắt buộc cho mỗi mã Step
Mỗi `<OBJECT>.Sxx` mở bảng chi tiết có mã ổn định, tối thiểu:
`lifecycle_state · Điểm vào/UI · Bấm/Hành động · Khai tay · Config máy · Phụ thuộc/nhánh · Kết quả mong đợi · Lỗi/quay về · Nơi quản lý sau tạo · Thông tin quản lý · UI_state · bằng chứng · manual_count · config_count`.

Hai cột tổng ở bảng Step chỉ đếm từ bảng chi tiết; chưa có danh sách đã rà thì để trống, không coi là 0.

### R3.6 · Trạng thái UI 5 giá trị
- `UI_OK` xanh — Owner đã chốt UI cho đúng step; bắt buộc `bang_chung + ngay_owner_chot`.
- `UI_CAN_SUA` vàng — UI có nhưng chưa chốt cho step hoặc cần sửa.
- `UI_THIEU` đỏ — chưa có UI cần thiết, blocker.
- `CHUA_RA` xám — chưa rà/thiếu evidence.
- `KHONG_CAN_UI` x — step máy tự làm, không cần UI người dùng.

Không suy `UI_OK` chỉ từ việc có URL. Mâu thuẫn FIELD cũ/mới giải bằng evidence + ngày Owner chốt.

### R3.7 · Quản lý sau tạo
Mỗi đối tượng phải chỉ rõ:
1. **Master/Registry:** tìm, ID/code, version, trạng thái, nơi dùng/parent refs, ngừng/lưu trữ.
2. **Workspace/Canvas/Config:** nơi vận hành/chỉnh cấu hình nếu có.
Các trường quản lý thực tế phải lấy từ UI/contract đã rà; không biến danh sách gợi ý thành schema nếu chưa có bằng chứng.

### R3.8 · Deep-link contract sandbox-safe
URL ngoài:
`/knowledge/modules?task=mow-mot-moit-mout&view=<...>&section=<field|mout|moit|mot|mow>&step=<OBJECT.Sxx>&detail=<id>`.

- Browser-visible query do **KB/top parent** sở hữu.
- Work HTML sandbox chỉ dùng hash nội bộ; không tự `pushState/replaceState` query ngoài.
- Relay hai tầng: `KB/top ↔ HVU app ↔ sandbox work HTML`.
- Sandbox không thêm `allow-same-origin`.
- Message sandbox child được xác thực bằng `event.source === iframe.contentWindow` + schema allowlist `view|section|step|detail`; value `^[a-z0-9._-]{1,40}$`; bỏ key lạ. Chiều xuống opaque child dùng `postMessage(...,'*')`.
- Handshake: child gửi `ready`; parent gửi/replay route mới nhất sau ready.
- Standalone “Mở rộng ↗” vẫn route bằng hash.

Acceptance: A1–A7 URL01 + A8 standalone hash mở đúng step + A9 sandbox giữ nguyên, không thêm `allow-same-origin`.

### R3.9 · JEV evidence cuối
- `gen-dec-1790131725-PipG3goneS1zYAMJ6fli`: xương 8 bước = 1.00; UI 5-state = 0.99/1.00; deep-link kiến trúc = 1.00.
- `gen-dec-1790131823-9HT2scV7fWduN7yYXgxh`: draft form 0 / PASS ≥1 Field = 0.85; HMITL one MOIT + one MOUT = 0.84.
- `gen-dec-1790132874-cPBXDdCT8OQwxHPYsCZG`: AUTO 0 human form + machine binding = 1.00; HMITL 1+1 là council convention supported by source = 0.96; default one, max open = 0.99.

## Claude · Rà soát tiền triển khai · Based_on `af76f8d`
**MAP-R3 về nội dung: ACCEPT, không mở lại điểm nào.** P12 CLOSED đúng như `f53cee5` đã hẹn; bản siết AUTO của Host (AUTO không human form nhưng **bắt buộc** machine binding ở S06 + PASS S07) đúng hơn bản Claude viết, nhận nguyên văn. HTML chính kiểm lại: SHA `e5432de39716c761fea7d6ab11692791b404b494e13d36edb655ad29c6b26422` — khớp.

Nhưng MAP-R3 là bản thiết kế, chưa phải bản thi công. Đối chiếu với **vỏ bảng thật** (`mow-mot-moit-mout.html` dòng 472–491) và với **chỗ mã deep-link thực sự nằm**, còn 6 khoảng trống. Sau khi điền 40 hàng thì kiểm lại rất đắt, nên chốt trước khi soạn lệnh.

- **G1 · R3.8 KHÔNG thuộc repo này — phải tách thành việc riêng.** Mã khung xem là `docker/nuxt-repo/scripts/hvu-b2/ui/app.vue` (nguồn) + bản build `docker/nginx/static/ui-preview/hpml-view-for-user/view.html`, nằm trên VPS. Theo README §11, VPS là SSOT của MÃ và **nghiêm cấm GitHub → VPS**; write path `workspace_*`/`fs_*` của repo này không chạm tới đó, lại còn cần build/deploy Nuxt. Đề nghị: `MMIM.3` = chỉ điền HTML trong repo; deep-link đưa sang `work/hpml-view-for-user/` như hợp đồng đầu vào (R3.8 nguyên văn + A1–A9), có Executor_Surface/Write_Path riêng. **Không gộp hai việc vào một prompt** — gộp là lặp đúng lỗi I02 ở cấp khác.
- **G2 · Vỏ bảng hiện tại chưa khớp MAP-R3, phải nói đích danh trong prompt.** Đo thật: 5 bảng `list-quy-trinh-{field|mout|moit|mot|mow}`, mỗi bảng **7 cột** `STT · Mã Bước · Tên Bước · Nội dung · Tổng số trường cần khai · Tổng số trường cần config · Check UI` và **đúng 3 hàng trống**. MAP-R3 cần 8 hàng/đối tượng (40 hàng), cột 7 phải đổi từ nhị phân “Check khi UI đã đúng” sang **UI_state 5 giá trị**, và **bảng chi tiết R3.5 hiện chưa tồn tại trong file**. Prompt phải chốt sẵn: bảng chi tiết đặt ở đâu, khuôn ID (đề xuất `step-detail-<OBJECT>-S0x`, chữ thường, ổn định) và `detail=` của deep-link trỏ đúng ID đó. Không để Agent tự chọn layout rồi phải sửa lại.
- **G3 · Cập nhật `#step-quy-trinh-quy-uoc` trong CÙNG commit.** Khối này là luật nằm trong file (D18: AI đọc mục này trước khi điền), hiện mới nói hai cột số tổng. Phải bổ sung: 8 bước chuẩn, 5 trạng thái UI + màu, luật nhánh S04 + `return_to_step`, cardinality R3.3 (kể cả HMITL/AUTO). Không làm thì file và COLLAB nói hai luật khác nhau, phiên sau đọc file sẽ điền sai.
- **G4 · An toàn khi sửa file 1,8 MB.** Năm bảng có **ba hàng trống giống hệt nhau**, mỗi bảng nằm trọn trong một dòng rất dài → `old_str` theo chuỗi hàng trống sẽ trùng nhiều chỗ hoặc vào nhầm bảng. Bắt buộc: neo theo `id="list-quy-trinh-<object>"`, sửa trong **một transaction**, cấm ghi đè cả file, cấm reformat/prettify, cấm đổi ID đang có (D17). Nghiệm thu bằng số đo chứ không bằng lời: SHA trước/sau · delta bytes · đếm `<tr>` mỗi bảng = 8 · đếm đủ 40 mã bước đúng khuôn OBJECT.S01–S08 · mở thử bản xem một lần.
- **G5 · Chống bịa nội dung — rủi ro lớn nhất sau khi điền.** Agent chỉ điền thứ có nguồn; mỗi ô có nội dung phải kèm `bằng chứng` (URL UI · commit · dòng tài liệu). Không có bằng chứng → `CHUA_RA` (xám) và **để trống hai cột số tổng**, đúng quy ước đã có trong file (ô trống ≠ 0). **Cấm Agent tự đánh `UI_OK`** — xanh chỉ do Owner chốt, kèm ngày. Báo cáo cuối phải có ba số đối chiếu được: số ô đã điền · số ô có bằng chứng · số ô xám; “đã điền > có bằng chứng” là FAIL, tự sửa trước khi báo XONG.
- **G6 · Chạy thử một đối tượng trước.** Lượt đầu chỉ làm **FIELD** (8 hàng + bảng chi tiết + sửa quy ước + đổi cột UI_state). Owner liếc một bảng 8 hàng là biết khuôn đúng hay sai; sửa lúc đó rẻ. Đúng khuôn rồi mới chạy 4 đối tượng còn lại trong một lượt. Sửa khuôn sau khi đã điền 40 hàng thì đắt gấp nhiều lần.

**Điều kiện đồng thuận từ phía Claude:** Host đưa G1–G6 vào bản giao việc (G1 thành việc riêng; G2–G6 thành điều khoản prompt + acceptance) thì **không cần thêm vòng review nào**; Host đặt READY sau khi Owner chốt MAP-R3.

**Host xử lý G1–G6 · ACCEPTED**
- G1: đã mở lại `work/hpml-view-for-user/`; R3.8/A1–A9 vào `HVU-DEEPLINK01`, DRAFT/NO RUN. Không Git→VPS, không sửa connector.
- G2: FIELD01 đổi header UI_state cho 5 bảng; FIELD = 8 summary rows + 8 detail blocks; 4 body còn lại giữ trống.
- G3: cập nhật `#step-quy-trinh-quy-uoc` cùng transaction.
- G4: patch neo theo ID; cấm replace generic/rewrite/reformat; acceptance đếm/hash/diff.
- G5: evidence-per-record + coverage gate. JEV `gen-dec-1790134092-aO1ALXq7oHvk0kKWxh8g` = 1.00.
- G6: FIELD pilot trước; JEV cùng result = 1.00.
- lifecycle mapping: JEV `gen-dec-1790134441-cc5M3quXTJLHbOyhLsDI`: S01=Tìm; S02=Tạo; S03=Tạo; S04=Tạo; S05=Tạo; S06=Config; S07=Test; S08=Master; non-applicable=`x`.

## NEXT sau G1–G6
- FIELD01: READY đã pin; Owner/GPT có thể RUN Claude Code CLI. Sau KQ, Host + Owner review đúng một bảng FIELD trước khi scale.
- SCALE01: chỉ sau FIELD được Owner chấp nhận mới điền MOUT/MOIT/MOT/MOW.
- HVU-DEEPLINK01: đã tách/reopen; giữ DRAFT/NO RUN tới khi child ID/bridge contract MMIM ổn định.


## Kế hoạch
- MMIM.1 | Tạo work + import file gốc | ✅
- MMIM.2 | Thu thập/dọn kho tham khảo | ✅ lịch sử D12–D15
- MMIM.FIELD01 | FIELD 8 bước + detail/evidence + quy ước mới | ▶ prompt final · pin READY kế tiếp
- MMIM.SCALE01 | MOUT/MOIT/MOT/MOW theo khuôn FIELD đã duyệt | □ chờ Owner nghiệm thu FIELD
- HVU-DEEPLINK01 | URL tab/section/step/detail | ↗ task riêng · DRAFT/NO RUN

## Ý kiến (P)
Reviewer: Claude Chat · Based_on `39cc96d` / commit review `f5f97fc`. Host GPT đã đối chiếu lại HTML chính và README §12 trước khi xử lý.

- P01 · Scope COLLAB §0 · **REJECTED trong lượt này** · Claude đề nghị mở rộng mục tiêu toàn việc sang “thiết kế chuẩn UI + quy trình tạo/khai báo thành công MOW/MOT/MOIT/MOUT/Field”. Đây là thay đổi A0; trong tin nhắn hiện tại Owner chỉ quyết rõ việc công khai có lọc nhạy cảm, chưa xác nhận lại câu mục tiêu rộng đó. Giữ nguyên §0 đã xác nhận. Khi Owner xác nhận mục tiêu rộng, mở D mới và cập nhật A0 riêng; không dùng lời Reviewer để thay Owner. · Claude vòng 2 (Based_on `17b5470`): câu mục tiêu không phải đề xuất của Reviewer mà là nguyên văn Owner gõ khi giao Claude review (chat 2026-09-20). Đồng ý A0 cần Owner xác nhận rõ → chuyển **OWNER**. Không chặn MMIM.2 (thu thập không mâu thuẫn mục tiêu rộng).
- P02 · Scope PROMPT §2A/§3/§6 · **PARTIAL** · ACCEPT chẩn đoán NFD và yêu cầu `LINK-MAP`; GPT kiểm thật meta `project-assets-root` ghi NFD và README §12.3 hiện chỉ mirror một HTML. Không nhận đề nghị đưa `assets/` ra cạnh HTML ngay trong MMIM.2 vì D04–D05 của Owner yêu cầu lượt này chỉ gom vào `information/` và cấm sửa sản phẩm. PROMPT mới stage phụ thuộc dưới cha ASCII `information/direct-dependency/source-assets/`, kiểm 16 ảnh + manifest + mọi file-ref tương đối. Việc đổi đường dẫn HTML/Owner View là lượt riêng sau MMIM.2, chưa RUN.
- P03 · Scope public safety · **ACCEPTED theo quyết định Owner 2026-09-20** · repo được phép công khai để ưu tiên tốc độ/chất lượng; chỉ loại thông tin thật sự quá nhạy cảm/không cần thiết. PROMPT chặn credential/secret, định danh cá nhân rủi ro, dữ liệu tài chính/cá nhân và tài liệu không công khai cần bảo vệ; không tự loại tên người/tên công ty/thông tin nghiệp vụ công khai. File >50MB hoặc tổng >250MB được ghi nhận để tránh làm chậm/đẩy file lớn.
- P04 · Scope đúng bản · **ACCEPTED** · bản repo `mow-mot-moit-mout.html` là working SSOT của việc; Mac read-only. Codex đọc các sổ chỉ đường nếu có, so SHA bản Mac và SHA nguồn được HTML ghi; lệch thì ghi divergence, không chép đè.
- P05 · Scope UI runtime · **ACCEPTED** · UI đang chạy lấy VPS root `ui` làm thực địa theo A8; bản HTML/JS/CSS tương ứng trên Mac không được xếp CURRENT. Nếu cần đối chiếu thì LEGACY/MAC_RUNTIME_COPY; MMIM.2 không fetch runtime VPS.
- P06 · Claude · Based_on `6f15da7` · Scope PROMPT §0 + §7 / README D12 · **ACCEPTED theo nguyên tắc Owner, sửa căn cứ** · Nhận đúng yêu cầu phải gọi tên Write_Path và test đúng một read-gate trước mutation. Không nhận cách hiểu “GPT key/Claude key”: DROOT06/README đã sửa capability-first. MMIM.2 chốt `Executor_Surface=Codex`; primary `Write_Path=workspace_*`, fallback `fs_*` nếu chính phiên Codex bind path đó; cấm Git/CLI/native write. Prompt phải ghi tên tool family + gate; Agent không tự suy và không đổi vai giữa chừng.
- P07 · Claude · Based_on `6f15da7` · Scope PROMPT §0.4 · §5 · §6 · §7 · **ACCEPTED có siết chống chọn nhầm nguồn** · (a) so commit cuối chạm PROMPT, không so HEAD; phạm vi thay đổi chỉ tính mutation do Codex tạo. (b) text >100 KB không relay qua model: inventory `PENDING_LARGE_TEXT` + bytes/SHA, xử lý như external/shared asset sau. (c) transport đổi newline/BOM thì ghi `NORMALIZED_BY_TRANSPORT` + SHA hai bên, không retry vòng lặp; nội dung phải được xác nhận tương đương text. (d) `OUTCOME_UNKNOWN` → read-back/journal/idempotency, không ghi lại mù. (e) ưu tiên path Owner đã chỉ; nếu lookup lỗi do Unicode/path thì resolve trong Desktop trước, sau đó Documents/Google Drive cục bộ; nếu nhiều candidate phải đối chiếu marker/SHA, không chọn chỉ vì trùng tên.
- P08 · Claude · Based_on `2d673a3` · Scope PROMPT §0.5 · §2 · §6 · §7 · **OPEN — 4 câu chèn nguyên văn, không cần vòng review nữa** · R2 đã gỡ đúng gốc I02 (Write_Path gọi tên + read-gate đầu). Còn 4 đường có thể làm Codex DỪNG oan hoặc chạy quá tốn. Đã kiểm nguồn connector: family `workspace_*` có `workspace_log`/`workspace_stat`/`workspace_write_new`/`workspace_transaction`; family `fs_*` có `fs_log`/`fs_stat` — đủ để làm hết bằng đúng family đã qua gate. Chèn nguyên văn: (1) §0 bước 5, thêm: “Tra commit cuối chạm `PROMPT.md` bằng `workspace_log`/`fs_log` của chính Write_Path; không dùng clone local (clone local cũ là nguyên nhân I01).” (2) §7, thêm: “Nếu guard bí mật của Write_Path từ chối một file: KHÔNG sửa/che nội dung để lọt guard; bỏ file đó khỏi lô, ghi `OMITTED_SECRET_GUARD` + path + SHA nguồn vào README, ghi lại phần còn lại của lô và tiếp tục. Đây không phải lý do DỪNG.” (lý do: tài liệu cũ trong `quy trình/` rất có thể chứa URL connector có token; hiện dòng cuối prompt ghi “secret không xử lý an toàn → DỪNG” → một file bị guard chặn có thể dừng cả lượt, và transaction nhiều file bị hủy cả lô.) (3) §2 cuối, thêm: “Lớp D chỉ inventory, không copy. Tổng nội dung text relay qua model cả lượt ≤300 KB, ưu tiên A → B → C; vượt ngân sách → phần còn lại `PENDING_LARGE_TEXT`. Ghi theo lô nhỏ (≤10 file/commit), không dồn một transaction khổng lồ.” (lý do: ngưỡng 100 KB/file chưa chặn tổng — 20 file × 90 KB vẫn là khối output rất lớn, dễ tràn ngữ cảnh/timeout và tốn tiền.) (4) §6, sửa dòng “mỗi file text đã copy có hash nguồn = hash đích” thành “… = hash đích **hoặc `NORMALIZED_BY_TRANSPORT` theo §5**” (hiện §5 cho phép nhưng §6 cấm → Codex đọc chặt sẽ tự đánh trượt).

Claude REVIEWED@2d673a370a030e2b679d161132cb908f897b9503 · **ACCEPT có điều kiện P08** — Host chèn đúng nguyên văn 4 câu P08 thì coi như Claude đã ACCEPT bản mới, Host đặt READY luôn, không cần gửi Claude review lại. Ngoài 4 câu này, mọi sửa khác vào PROMPT vẫn phải review theo A6. HTML chính kiểm lại: SHA `f4aac30c…a050c` PASS.

## Phương án Host chờ Claude review
- H01 · **ACCEPTED + mở rộng:** Git chỉ giữ HTML, text nhỏ (≤100 KB/file), README, `assets-manifest.json` và LINK-MAP. Binary và text >100 KB không relay qua model/không commit ở MMIM.2; chỉ inventory bytes/SHA/path/state để shared-assets/external step sau.
- H02 · **Shared assets ngoài Git:** sau MMIM.2, publish binary một lần vào kho static HTTPS dùng chung để GPT/Claude/Codex/Hermes và Owner View cùng đọc bằng URL tuyệt đối. Ưu tiên tái dùng hạ tầng static hiện có; không mở dự án sửa MCP/connector. Repo giữ SHA/bytes/URL làm SSOT metadata. Cơ chế/path publish cụ thể phải được Claude phản biện trước khi Host chốt MMIM.3.
- H03 · MMIM.2 không được DỪNG chỉ vì connector không nhập binary; binary pass ở lượt này = định vị + SHA/bytes + manifest/link-map.

**Claude trả lời H01–H03 (Based_on `6f15da7`):**
- H01 · **ACCEPT + bổ sung**: tách đúng hướng, nhưng tiêu chí thật không phải “binary hay text” mà là **file có phải đi qua ngữ cảnh của mô hình hay không**. Text lớn (ví dụ `00-NGUON-THIET-KE.html`, `cấu trúc hệ thống.html`) khi đẩy qua connector vẫn phải chạy qua mô hình → vừa tốn vừa có nguy cơ sai byte. Chi tiết ở P07b.
- H02 · **Đồng ý nguyên tắc, chưa chốt được đường đi**: binary ngoài Git + URL tuyệt đối + repo giữ metadata là đúng và hợp README §11.5/§12. Nhưng hiện **chưa tồn tại đường vận chuyển binary nào đã nghiệm thu**: Codex không nhập được binary (I02), `fs_write` của Claude chỉ nhận text, và dựng endpoint upload mới = sửa dịch vụ VPS (ngoài phạm vi, đúng như Host đã loại). Đề nghị: không chốt cơ chế bây giờ; MMIM.2 cứ chạy với inventory. Đến bước shared-assets mới chọn, và ứng viên rẻ nhất lúc này là Owner upload MỘT lần đúng 16 ảnh vào vùng static hiện có, có hướng dẫn từng bước — không dựng hạ tầng mới, không sửa connector.
- H03 · **ACCEPT**: đúng nguyên nhân gốc của I02 về phần binary.

## Owner cần quyết
- —
P01 lịch sử đã được A0 ngày 23/09 + D19–D22 thay thế cho lượt hiện hành; không còn là gate FIELD01.

## Sự cố / bài học Host
- I01 · 2026-09-21 · Codex trả: `DỪNG · MMIM.2 · Workspace hiện tại không có work/mow-mot-moit-mout/COLLAB.md và PROMPT.md; không thể xác minh ba gate bắt buộc. Chưa thay đổi file nào.` → Host đã sửa bootstrap/input gate.
- I02 · 2026-09-21 · Codex trả: `DỪNG · MMIM.2 · Gate công cụ ghi chưa đạt: README §0/D12 cấm AI push bằng Git/CLI; connector hiện có chưa có đường nhập ảnh nhị phân từ Mac đáp ứng giao dịch bắt buộc. Chưa tạo information/ hoặc sửa nguồn, HTML, COLLAB.`
- Kết luận Host I02: prompt sai kiến trúc khi bắt binary đi vào Git. Sửa nguyên nhân gốc: MMIM.2 không đưa binary vào Git; chỉ inventory/hash. Shared-assets ngoài Git là bước riêng sau consensus, không sửa connector.

## Giao Agent — MMIM.FIELD03
- RUN_ID: `MMIM-FIELD03-20260923-01`
- Executor_Surface: Claude Code CLI · Write_Path: `fs_*`
- Prompt hiện hành: thiết kế kịch bản trên COLLAB, KHÔNG HTML.
- READY@`7b1685bfcfcff6bf14634034cc8790e5ccbb7600` · commit cuối chạm `PROMPT.md` sau K1–K4.

## KQ · MMIM.FIELD03 · Claude Code CLI
KQ@MMIM-FIELD03-20260923-01 XONG
- RUN_ID `MMIM-FIELD03-20260923-01` · Executor_Surface Claude Code CLI · Write_Path `fs_*` (read-gate `fs_log`/`fs_stat` PASS; ghi COLLAB bằng một `fs_transaction`). Commit này: SAME_COMMIT.
- Gate: READY@`7b1685bfcfcff6bf14634034cc8790e5ccbb7600` = commit cuối chạm `PROMPT.md` (`fs_log`) · HTML SHA `1e245ed6997f5dc117bd809807a9e963527068c89cc6985e442b8eeb133099e8` **không đổi** (không ghi HTML).
- Sản phẩm: mục **“FIELD03 · Thiết kế FIELD trên giấy”** ngay dưới Dòng hiện hành, thứ tự G → sơ đồ → A–F → phụ lục UI thiếu.
- Số đếm: scenarios=39 dòng chính (CHOT 12 · CHUA_CHOT 5 · UI_THIEU 22) + 6 `DEFER_P1` · owner_decisions=7 · ui_gaps=15 · transitions=12 · data dictionary 15 cột · coverage 15/15 COVERED về thiết kế (UI nói riêng ở cột UI).
- Quy mô: COLLAB 90.843 B → 128.131 B, ≤150 KB → giữ toàn bộ trong COLLAB, không tạo `FIELD-DESIGN.md`.
- Bằng chứng đọc thật 23/09 (chỉ đọc root `ui`, không sửa): `kanban-field-v1.js`, `master-list.js`, `search-demo-data.json`; DOM UI-022 (bảng + `?chi-tiet=full_name`), UI-018 (`khai-bao=moi`, `truong=full_name`, `edit=full_name`); ma trận FIELD.1–8 và ô UI trong HTML chính.
- Phát hiện mới (đã ghi vào A và UIGAP.10): nút ✎ của UI-022 gửi `&edit=<mã>` (`master-list.js:283`) nhưng UI-018 chỉ đọc `&truong=<mã>` (`kanban-field-v1.js:66`) → bấm ✎ **không mở** được hộp sửa. Ngăn chi tiết UI-022 chỉ hiện một đường dẫn cha, chưa phải where-used đầy đủ.
- JEV: coverage `gen-dec-1790156331-nwE2yw485cC38Ciz9Ukm` (13/15 ≥0,89; RBAC 0,35 do Agent rút gọn AUTH.001 khi hỏi, where-used 0,75 → đã thêm “xem nơi dùng trước” vào UPDATE.003/004) → chấm lại `gen-dec-1790156350-H9n6o9cJksQfXWlrcvXY`: RBAC 0,95 · where-used 0,89 · người mới đọc là làm được 0,65 (lần đầu) · quyết định G `gen-dec-1790156368-mZBmJBd5gqdw7q6YzfQT` (6/7 ≥0,91; G04 không chắc).
- Acceptance: 1 PASS (HTML không đổi) · 2 PASS · 3 PASS (7/7 dòng G có đề xuất + hệ quả nếu lắc) · 4 PASS · 5 PASS (39 ≤ 40; 6 `DEFER_P1` có mã) · 6 PASS (mọi mã bước/kịch bản có `MMIM.`; registry có `work_id`) · 7 PASS (S01–S03 giữ; S04–S07 nối cuối) · 8 PASS (bảng B 27 dòng checklist → mã) · 9 PASS (15 chiều) · 10 PASS · 11 PASS · 12 PASS · 13 PASS (G + phụ lục UI thiếu) · 14 PASS (12 dòng CHOT đều có bằng chứng) · 15 PASS · 16 PASS (dòng KQ này).
- Để Host/Owner xem: HTML vẫn ghi `FIELD.S01–S03` và `FIELD02.0x` không có tiền tố `MMIM.` — registry ghi rõ, đổi ở lượt HTML sau Owner duyệt. Không chạm HTML/VPS runtime/HVU/connector/config.

## Giao Agent — MMIM.FIELD02 · LỊCH SỬ
- RUN_ID: `MMIM-FIELD02-20260923-01`
- Executor_Surface: Claude Code CLI · Write_Path: `fs_*`
- Prompt hiện hành: FIELD02 UI-first · 3 bước/3 mảnh UI/7 mục.
- READY@`487df06a037c10d3528e1dcc6d41db767cb0e9bd` · commit cuối chạm `PROMPT.md` sau F1–F3.
- Chỉ RUN FIELD02; không SCALE/config/deep-link.

## KQ · MMIM.FIELD02 · Claude Code CLI
KQ@MMIM-FIELD02-20260923-01 XONG
- RUN_ID `MMIM-FIELD02-20260923-01` · Executor_Surface Claude Code CLI · Write_Path `fs_*` (read-gate `fs_stat`/`fs_log`/`fs_diff` PASS; ghi bằng MỘT `fs_transaction` gồm HTML + COLLAB). Commit này: SAME_COMMIT.
- Gate: READY@`487df06a037c10d3528e1dcc6d41db767cb0e9bd` = commit cuối chạm `PROMPT.md` (`fs_log` + `fs_diff` full SHA) · HTML SHA trước khớp baseline `d66e2f54…3fe73`.
- HTML SHA-256 trước `d66e2f5475f9bf6c7bea32ee832dc73a3f97c2e8114bc47e47a5b93c3573fe73` (1.870.469 B) → sau `1e245ed6997f5dc117bd809807a9e963527068c89cc6985e442b8eeb133099e8` (1.855.314 B).
- steps=3 · ui_tiles=3 · field_list=6 · counts S01=2 · S02=3 · S03=1 · config=trống cả 3 dòng · Trạng thái UI giữ `UI_CAN_SUA` cả 3 (0 `UI_OK`).
- Nguồn UI thật (chỉ đọc root `ui`, không sửa): UI-022 `field-master-v1.html` → `master-list.js` dòng 173–182 + DOM `ui_inspect` vùng `master.tools` và `#mlTier`; UI-018 = đúng link «＋ Khai báo trường» của UI-022 `mow-unified-canvas-v2.html?tang=T0&form=MOIT&cong-viec=T01&che-do=de-xuat&khai-bao=moi` → `kanban-field-v1.js` dòng 38–56 + DOM `ui_inspect` `#field-declaration`. CSS lấy từ `master-list.js` dòng 49–61 và `mow-unified-canvas-v2.html` dòng 639–658, gói trong namespace `#quy-trinh-field`.
- **Mismatch so với dự kiến PROMPT (dùng số/nhãn thật, không FAIL):**
  - M1 · **S02 = 3, không phải 4.** `Mô tả` không có `*` và `save()` chỉ đòi tên + định dạng + ≥1 nhóm (`kanban-field-v1.js:56`) → xám theo luật vàng/xám §4; vẫn hiện trong mảnh UI. Vì vậy danh sách 6 mục thay vì 7. JEV `gen-dec-1790151441-hLrCyPh1KrHAAGw9PXJ8`: Mô tả = grey 1,00 · Nhóm quản lý = yellow 0,97.
  - M2 · **Nút cuối khi khai mới là `Lưu đề xuất`, không phải `Đề xuất khai báo`.** Source: `edit = st.s==='proposal'` (dòng 38); nhãn nút (dòng 49) đổi theo **chế độ Đề xuất/Thường**, không theo khai mới/sửa. Link tạo của UI-022 mang `che-do=de-xuat&khai-bao=moi` → DOM thật: tiêu đề `Đề xuất thêm trường`, footer `Đóng` + `Lưu đề xuất`. `Đề xuất khai báo` chỉ hiện ở chế độ Thường, khi các ô bị khoá (bấm để chuyển sang Đề xuất). Tên bước S03 và mục FIELD02.06 vì vậy dùng `Lưu đề xuất`; biến thể ghi ở dòng Nguồn của S03.
  - M3 · Mã trường đánh liên tục `FIELD02.01–06` (Nhóm quản lý = .05, Lưu đề xuất = .06) vì bỏ Mô tả.
  - M4 · UI-022 **không có** `Mọi Mẹ` (tắt ở UI-022); vùng tìm có thêm `Bảng / Theo tầng` và hàng 9 bộ lọc tầng → hiện đủ, tô xám.
- S01: JEV `gen-dec-1790151454-GGMXpEU0gTrLJeQLFPkQ`: `Tìm mã / tên…` vàng 0,95 · bộ lọc xám 0,99 · `＋ Khai báo trường` nghiêng xám 0,62 (confidence 0,42, thấp) → Agent **giữ VÀNG** theo PROMPT §2: trong luồng khai mới đó là đường duy nhất sang S02. Nếu Owner chỉ đếm nhánh “đã có thì dùng lại” thì S01 = 1.
- Vị trí: tab Quy trình = section `#quy-trinh-field` lồng cuối `#quy-trinh-tao-mow` (script tab chỉ chuyển `#quy-trinh-tao-mow` vào panel; không sửa JS). Link `FIELD.S0x` ở bảng Step tự nhảy sang tab Quy trình — đã kiểm bằng render cục bộ (Chrome headless, bản dựng trùng SHA sau).
- Diff đúng 5 vùng: bỏ 1 dòng CSS chết `#step-details-field` trong `#process-list-shell-style` · `#step-quy-trinh-quy-uoc`: bullet “Bảng chi tiết từng bước” (14 mục → 4 phần) + ghi chú FIELD · tbody `#list-quy-trinh-field` 8 → 3 dòng + bỏ `#step-details-field` (8 bảng FIELD01 + danh sách nguồn) · thêm `#quy-trinh-field` (style `#field02-ui-style`, 3 `article`, bảng `#field02-list`).
- Acceptance: 1 PASS (3 dòng FIELD.S01..S03) · 2 PASS (7 cột, cùng ID) · 3 PASS (vàng = danh sách = cột Tổng: 2/2/2 · 3/3/3 · 1/1/1; mismatch ghi ở trên) · 4 PASS (`step-detail-field-s01..s03`, mỗi ID duy nhất) · 5 PASS (0 `<img>`/`<script>`/`on*=`/base64 trong khu FIELD02; mảnh UI `inert`) · 6 PASS · 7 PASS (6 = 2+3+1) · 8 PASS (0 `step-details-field`, 0 `data-record-state`) · 9 PASS (bảng MOUT/MOIT/MOT/MOW trùng byte) · 10 PASS · 11 `VIEW_PENDING_REVISION` — ghi cùng commit nên chưa mở được bản mirror mới; Host kiểm sau · 12 PASS (cân thẻ 0 lỗi ở khối Step, `#quy-trinh-tao-mow`, `#quy-trinh-field`) · 13 PASS (dòng KQ này).
- Để Host/Owner xem (không chặn, không tự sửa): bullet “8 bước chuẩn” và “Mỗi mục phải có nguồn/EVIDENCED” trong `#step-quy-trinh-quy-uoc` vẫn là khung MAP-R3/FIELD01; FIELD nay 3 bước theo D20 → rà khi SCALE. Không chạm config/SCALE/deep-link/HVU/VPS runtime.

## Giao Agent — MMIM.FIELD01 · LỊCH SỬ
- RUN_ID dự kiến: `MMIM-FIELD01-20260923-01`.
- Executor_Surface: Claude Code CLI · Write_Path: `fs_*`.
- Prompt hiện hành: FIELD pilot.
- READY@`7aaa8b61d65eeccd5341a415eaf533a2096455fe` · commit cuối chạm `PROMPT.md` sau đổi Executor/Write_Path.
- RUN: **CHƯA PHÁT**. Khi RUN chỉ dùng RUN_ID `MMIM-FIELD01-20260923-01`.
- Không RUN SCALE01 trong cùng lượt.

## KQ · MMIM.FIELD01 · Claude Code CLI
KQ@MMIM-FIELD01-20260923-01 XONG
- RUN_ID `MMIM-FIELD01-20260923-01` · Executor_Surface Claude Code CLI · Write_Path `fs_*` (read-gate `fs_stat`/`fs_read` PASS; ghi bằng `fs_transaction` — PROMPT §6 viết `workspace_transaction`, đây là tool giao dịch cùng family `fs_*` mà §0 chỉ định). Commit này: SAME_COMMIT.
- Gate: READY@`7aaa8b61d65eeccd5341a415eaf533a2096455fe` = commit cuối chạm `PROMPT.md` (`fs_log` + `fs_diff` full SHA) · HTML SHA trước khớp baseline.
- HTML SHA-256 trước `e5432de39716c761fea7d6ab11692791b404b494e13d36edb655ad29c6b26422` (1.836.178 B) → sau `d66e2f5475f9bf6c7bea32ee832dc73a3f97c2e8114bc47e47a5b93c3573fe73` (1.870.469 B) · delta +34.291 B.
- field_rows=8 · detail_blocks=8 · records=112 · filled=47 · evidenced=47 · unknown=41 · na=24 · ui_ok=0.
- UI_state: S01 `UI_CAN_SUA` · S02 `UI_CAN_SUA` · S03 `UI_CAN_SUA` · S04 `KHONG_CAN_UI` · S05 `KHONG_CAN_UI` · S06 `CHUA_RA` · S07 `CHUA_RA` · S08 `UI_CAN_SUA`.
- Nguồn đã dùng (mã trong HTML `#step-evidence-field`): `UI-018`, `UI-021`, `UI-022` (danh mục UI con + đọc trực tiếp UI-018/UI-022 bằng `ui_inspect` ngày 23/09) · `MT-FIELD` (ô ma trận FIELD.*) · `MAP-R3` · `JEV-LC` · `JEV-F01` · `PROMPT-FIELD01`.
- JEV lượt này `gen-dec-1790137102-wBtdlo8F0q8Ck2N53WDm`: S03 manual_count để trống 0,75 · S06 CHUA_RA 0,40 · S08 UI_CAN_SUA 0,65 · S07 chia đôi (UI_CAN_SUA 0,51 / CHUA_RA 0,47) → Agent chọn `CHUA_RA` cho khớp ô ma trận `FIELD.5.UI.TEST = ?`. Cả hai cột tổng của 8 bước để trống (S04/S05 = `x`).
- Acceptance: 1 PASS (SHA/delta ở trên) · 2 PASS (tbody FIELD = 8 tr) · 3 PASS (MOUT/MOIT/MOT/MOW giữ 3 hàng trống) · 4 PASS (FIELD.S01..S08) · 5 PASS (`step-detail-field-s01..s08`, mỗi ID duy nhất) · 6 PASS (cột 7 cả 5 bảng = `Trạng thái UI`) · 7 PASS (0 `UI_OK`) · 8 PASS (47 = 47; unknown 41) · 9 PASS · 10 PASS (diff chỉ 3 vùng: `#process-list-shell-style` +2 dòng CSS, `#step-quy-trinh-quy-uoc`, 4 dòng bảng `list-quy-trinh-*`; kiểm cân thẻ khối Step = 0 lỗi) · 11 `VIEW_PENDING_REVISION` — ghi cùng commit nên chưa thể mở bản mirror mới; Host kiểm sau · 12 PASS (UNKNOWN chỉ `CHUA_RA`, NA chỉ `x`).
- Để Owner/Host xem khi duyệt FIELD (không chặn): UI-018 «Lưu đề xuất» hiện chỉ lưu trên trình duyệt, UI-022 là dữ liệu minh họa chưa nối PG → S08 chưa có nguồn cho khuôn id/version trả về; nhóm quản lý trong UI-018 là nhóm minh họa. Không chạm deep-link/HVU/VPS, không làm SCALE01.

## Giao Agent — lịch sử prompt MMIM.2 trước yêu cầu mới 23/09
- READY@`7d8e1df9e50cfdd5a4b7cfaf8c66cad9343e26f3` → **HẾT HIỆU LỰC** vì Host đã sửa `PROMPT.md` sau I02.
- **NO RUN** theo D10. Chờ Claude review bản prompt mới và H01–H03.

## Lịch sử nhập kho trước D14 (không phải chỉ dẫn đọc hiện hành)
- Executor_Surface: Codex · Write_Path: `workspace_*` · read-gate PASS. Theo lệnh trực tiếp Owner mới, không chạy PROMPT MMIM.2 nháp và không tự đặt READY cho bản nháp.
- Đã commit/push 888 tài liệu nguyên byte, 87.874.934 bytes; gồm cả hai HTML ưu tiên. Commit nhập cuối: `42e2db1ce50dd42563351aa252145fed541ffa76`; các commit nhập từng file nằm trong inventory lịch sử tại `b2666914babf884670d80597d639609681f9d3ea` (link ở README).
- Đọc lại blob Git: 888/888 SHA nguồn = đích. Kiểm lại 2.155/2.155 file Mac: hash không đổi. HTML chính SHA `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c` giữ nguyên.
- Sau D13: 97 Excel/Word/10.507.371 bytes chưa publish; 207 ảnh khác nhau/35.582.774 bytes không đưa lên Git. 16/16 ảnh manifest nguồn đúng hash/bytes; chỉ giữ metadata. Phần bỏ/chờ/trùng ghi trong inventory; không tuyên bố đã chuyển hết, không nghiệm thu nghiệp vụ, không chạm VPS/runtime.
- Mục lục, inventory và LINK-MAP: `information/README.md`. · Áp: SAME_COMMIT.

- Ghi nhận dung lượng: 3 HTML tham khảo đã lưu nguyên bản chứa khoảng 12,22 MB chuỗi ảnh nhúng. Đã loại ba bản chép đó cùng lô 888 khỏi cây hiện tại theo D15; bản lưu lịch sử không sửa.

## Kết quả rà dọn D14
- JEV: `gen-dec-1790115453-3T8Uh0LawUeGYjT756bc`, model do gateway trả `typesafe/jev-1.13-20260917`; năm nhóm đều ưu tiên link lịch sử hoặc VPS, không giữ toàn bộ bản chép trong phần đọc hằng ngày.
- 15 URL kiểm GET TLS, HTTP 200; mục lục giữ 14 link không trùng (URL Kanban trơn gộp vào URL Owner có query). Đây không phải nghiệm thu chức năng/UI/PG. Web reader và browser connector không dùng được; curl kiểm đọc thành công, không ghi VPS.
- Link tài liệu gốc cố định tại `b2666914babf884670d80597d639609681f9d3ea`; hai tài liệu thiết kế quan trọng vẫn truy nguyên byte. Không giả định URL UI là bản thay thế cho tài liệu.
- Đã xóa chính xác: 888 file/87.874.934 bytes dưới `information/reference/`. Xóa cây không thu hồi lịch sử Git; không hứa giảm dung lượng lưu GitHub tương ứng. Ở thời điểm rà, clone local báo object rời 4,49 MiB + pack 10,71 MiB; API GitHub trả size 1.824 KiB có thể cập nhật chậm, không dùng làm số tiết kiệm.
- Bốn file chỉ dẫn/metadata đã thay bằng bản gọn; hoàn tất xóa theo D15. Kiểm trước xóa: 888/888 file khớp manifest SHA-256, blob hiện tại bằng blob lịch sử; 11/11 nguồn Mac được chọn khớp SHA. HTML chính khớp SHA đầy đủ ghi ở đầu hồ sơ. Không chuyển rác sang archive trong repo. · Áp: SAME_COMMIT.

## Kiểm tra tab List quy trình
- Bản xem thử trên trình duyệt: mở đúng tab bằng hash và nút; đủ Field, Form/MOUT, Form/MOIT, MOT, MOW, bảy cột và ba hàng trống mỗi bảng. Chuyển sang Quy trình và UI Master hiển thị đúng nội dung cũ. Bảng cuộn ngang trên màn hình hẹp. Chưa có dữ liệu để đánh Check UI; không thêm lưu dữ liệu hoặc bảng con. · Áp: SAME_COMMIT.

## NEXT
- Cùng Owner đi từng bước để điền Step quy trình; chưa tự khai bước, số trường hoặc đánh Check UI. P01 vẫn chờ Owner, không tự chốt mục tiêu rộng.

## KQ · OWNER-BANDUYET-20260923-01
KQ@OWNER-BANDUYET-20260923-01 XONG

## KQ · OWNER-BANDUYET-20260924-02
KQ@OWNER-BANDUYET-20260924-02 XONG
