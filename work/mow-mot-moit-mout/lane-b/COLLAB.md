# COLLAB — MMIM Lane B · Process / Model / JEV

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — Owner 28/09/2026 yêu cầu tổ chức Lane A/B/C trên repo; Lane B phụ trách Quy trình · Model · JEV, làm nối tiếp qua nhiều phiên.

### 1. Mục tiêu
Rà và làm rõ hệ thống Quy trình/Model để tích lũy lâu dài; tìm trùng · chồng · xung đột · khoảng trống; dùng JEV cho các quyết định mơ hồ có tập lựa chọn hữu hạn.

### 2. Thế nào là hoàn thành
B01 tạo được bản đồ 39 quy trình hiện có theo chữ ký chuẩn; chỉ ra các cụm trùng/chồng/gap ưu tiên bằng evidence; chưa sửa CAT-003. Kết quả đủ rõ để Host chốt batch process tiếp theo.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- SSOT canonical: `../ban-duyet.html#ml5-cho-ai` và `../COLLAB.md`.
- 39 = process đã có definition; ≈98 = dự tính/khung, không coi là đã viết.
- Lane B **không sửa Step/UI**.
- Kết quả B01 là working evidence; chỉ Host/Owner mới hợp nhất vào canonical CAT-003.
- KQ mới nhất: **B01 XONG · Host đã nghiệm thu để mở B02** — 39 chữ ký/10 cụm; 8 overlap candidate/10 nhóm gap; xem KQ dưới đây.
- B02 HOST GATE · PASS · PROCESS=`CHUNG.APQUYTRINH` · catalog=`ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7` · prompt=`2daa910521ffda335916e182d582374fd31865d1ef9a565374b32b5610c22e36`.
- READY@f39ca2ded193af84048937452c937923348ec6b1 · RUN_ID `MMIM-LANE-B02-20260928-01`.
- RUN ISSUED · B02 chỉ sửa ban-duyet + lane-b/COLLAB; không sửa gate/Step/UI; XONG/DỪNG rồi dừng.
- HOST GATE · PASS · PROCESS=`CHUNG.TIM` · catalog=`ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7` · prompt=`86ecde4f60461e33cd19b5ab6ce4407885fb71c9e1c16c228a0ccbcc0fe8680d`.
- READY@8794c1fa9c868db731a6e1b9d4b99dad56e56c53 · RUN_ID `MMIM-LANE-B01-20260928-01`.
- RUN ISSUED · chỉ lane-b/COLLAB được ghi; canonical parent READ-ONLY; XONG/DỪNG rồi dừng.

### Vòng trước
A01 đã PASS P0/process gate. Lane B được mở sau D59.

## KQ · MMIM-LANE-B01-20260928-01 · Codex · 28/09/2026

KQ@MMIM-LANE-B01-20260928-01 XONG
KQ@LANE-B B01 · PROCESS=CHUNG.TIM · PROCESS_GATE=PASS · HEAD=4b668f996a9c2274b2dd8f70b1dd4253c6ff6caa · process=39 · overlap=8 · gaps=10 · NEXT=Host chốt một batch thí điểm CHUNG.TIM + MOW.TAO/LAP/KHAI/SUA/CHAY, ràng buộc đích tìm và gọi/nhận kết quả con

**B01 đã xong phần rà/evidence; chờ Host nghiệm thu và chốt batch.** Đây là working evidence, chưa hợp nhất CAT-003; không phải quyết định gộp/tạo quy trình hoặc nghiệm thu toàn Máy.

- **Có gì:** 39 definitions trong 10 cụm; 22 ⚙️ · 8 🔁 · 9 🏗. Exact code/name trùng=0. Tám quan hệ chồng/dùng chung đã hỏi JEV; chưa có trường hợp đủ căn cứ gộp toàn bộ.
- **Cần chú ý:** 10 nhóm gap dưới đây.33 mã PASS cú pháp;6 mã BLOCK khi thử chính PROCESS của chúng. **0 bản Step/UI trọn luồng đã được chứng minh;39 mã chưa được chứng minh hoàn chỉnh.** Có thể dùng khung/bước ứng viên, không coi39 mã là không dùng được.
- **Tiếp theo:** đúng một batch thí điểm đề xuất **CHUNG.TIM + MOW.TAO/LAP/KHAI/SUA/CHAY**; kiểm một ca MOW có quy trình con trước nhân rộng. Host chốt/review/READY trước RUN tiếp; B01 dừng.

### 1. Bản đồ 10 cụm

| Cụm | Mã hiện có | Definition | 👤 / 🤖 trực tiếp | Điều cần làm rõ |
|---|---|---:|---:|---|
| Chung | `CHUNG.APQUYTRINH` · `CHUNG.TIM` · `CHUNG.NEU` · `CHUNG.DUYET` · `CHUNG.CAPMA` · `CHUNG.KIEM` · `CHUNG.BAT` · `CHUNG.NGUNG` | 8 | 6 / 12 | Gate · tìm · nêu · duyệt · cấp mã · kiểm · bật · ngừng; hợp đồng gọi/đích chưa đủ. |
| Field | `FIELD.TAO` · `FIELD.LAP` · `FIELD.KHAI` · `FIELD.SUA` · `FIELD.XOA` | 5 | 5 / 5 | Đã có 5 luồng; FIELD.TAO/KHAI có lời gọi chưa định danh, SUA chưa nêu FIELD_SYNC. |
| Form · MOIT/MOUT | `FORM.TAO` · `FORM.LAP` · `FORM.KHAI` · `FORM.SUA` · `FORM.XOA` | 5 | 7 / 4 | MOIT/MOUT chung họ FORM; KHAI/TAO cần rõ ranh giới hợp đồng, SUA thiếu phần liên kết. |
| MOT | `MOT.TAO` · `MOT.LAP` · `MOT.KHAI` · `MOT.SUA` · `MOT.XOA` · `MOT.CHAY` | 6 | 10 / 11 | 5 luồng + CHAY; TAO gắn form, SUA chưa nêu clone 10/13; runtime đã ghi/đọc 18→. |
| MOW | `MOW.TAO` · `MOW.LAP` · `MOW.KHAI` · `MOW.SUA` · `MOW.XOA` · `MOW.CHAY` | 6 | 8 / 11 | 5 luồng + CHAY; thiếu đường tạo con/chờ/quay về và dispatch MOW lồng. |
| Vẽ UI | `VEUI.FIELD` · `VEUI.FORM` · `VEUI.MOT` · `VEUI.MOW` | 4 | 20 / 8 | Cùng khuôn, khác đối tượng; chưa suy được số UI unique từ “mỗi bước người → một màn”. |
| Công cụ | `CONGCU.TAO` · `CONGCU.RA` | 2 | 2 / 8 | Đăng ký + rà; chưa đọc sổ 35 trong bước tìm/rà; chưa có sửa/ngừng/phục hồi. |
| Chỉ đạo Owner | `YEUCAU.GHI` | 1 | 1 / 2 | Khác loại/chủ thể với nhu cầu; K13 còn trống. |
| Tài liệu | `TAILIEU.NHAP` | 1 | 1 / 3 | Nhập/sửa một nguồn chuẩn; K14 còn trống, chưa rõ kiểm revision sau đồng bộ. |
| Luật | `LUAT.BANHANH` | 1 | 2 / 2 | Ban hành + cưỡng chế; sửa/ngừng/phục hồi và kiểm xung đột nội dung còn thiếu. |
| **Tổng** | **Giữ nguyên 39 mã/tên** | **39** | **62 / 66** | **Không phải số Step/UI unique** |

### 2. Mười gap ưu tiên · evidence → ảnh hưởng → đề xuất

Nguồn chung: [39 definitions](../ban-duyet.html#ml5-cho-ai), [khung dự tính](../ban-duyet.html#ml5-qt), [Tool/K01–K18](../ban-duyet.html#mom-tool-catalog), parent COLLAB D36/D56–D60 và P17/P19. “Cao” chỉ nói độ chắc của trích dẫn/omission trong văn bản, không chứng nhận runtime lỗi hoặc xác suất của giải pháp. Đề xuất chưa là quyết định.

| # · Mã / loại | Evidence đã thấy | Ảnh hưởng | Đề xuất ngắn · confidence |
|---|---|---|---|
| 1 · CHUNG.TIM · gap đích tìm | Chỉ đọc 01/61/20/64/48; chưa nhận/đọc catalog đích04,06/07,08,09 như P17 yêu cầu. | Không chứng minh tìm đủ để quyết dùng lại/tạo mới; ảnh hưởng mọi *.TAO/LAP. | Ràng buộc catalog + loại + phạm vi/trạng thái + version. Cao về thiếu tham chiếu; JEV urgency3,82/4, confidence0,85. |
| 2 · VEUI.* +39 definitions · gap suy Step/UI | Lấy bước từ11 rồi “Mỗi bước người → một màn”; chưa có contract expand call/nhánh hoặc quy tắc UI dùng lại. | 62 icon người không phải62 Step/UI unique; chưa đóng đủ trường hợp cho C. | C lấy bước ứng viên có nguồn, chốt ngữ cảnh/nhánh/đường về trước số cuối. Cao về giới hạn nguồn; readiness JEV confidence0,79. |
| 3 · FIELD.TAO · 4 *.KHAI · MOW.CHAY · gap lời gọi | Cùng gate, đổi PROCESS trong bộ nhớ cho từng mã: 6/39 BLOCK PROCESS_STEPS_UNPARSEABLE; ↪ Thiếu…, ↪ Nếu…, ↪ Chạy từng bước chưa là mã call. | Có definition nhưng chưa qua khuôn để RUN bằng chính E1; B01 PASS không chứng minh cả catalog PASS. | Version definition và branch rõ, giữ mã; không để ghi chú giả làm named call. Cao · ca chạy thật. |
| 4 · FORM.TAO · MOT.TAO · MOW.TAO · gap tạo/lắp/khai con | “Gắn Field” ghi14, “Gắn form” ghi13, “Xếp bước” ghi11; chưa named-call *.LAP/KHAI hay nhánh con thiếu. | Chưa rõ ghi trực tiếp bao hàm kiểm bản/quyền/cấu hình; thiếu chờ con và nhận kết quả về cha. | Ràng buộc definition con/chỗ gắn/nhu cầu con/bước quay về, reuse khuôn có sẵn. Cao về omission; runtime chưa kiểm. |
| 5 · FIELD/FORM/MOT/MOW.SUA · gap version cấu trúc | Clone chỉ ghi/đọc46. FORM.SUA chưa nêu14/69; MOT.SUA chưa nêu10/13; MOW.SUA chưa nêu11/12/khoá gói; FIELD.SUA chưa nêu FIELD_SYNC76 như TAO. | Chưa chứng minh bản mới giữ liên kết/thành phần/cột vật lý; có thể bỏ bước sửa cấu trúc. | Nêu clone/giữ/sửa liên kết, phạm vi áp dụng, kiểm trước bật và phục hồi. Cao về khác biệt chữ; không khẳng định runtime lỗi. |
| 6 · MOW.TAO/LAP/CHAY · MOT.CHAY · gap chạy lồng/đường về | TAO cho MOT/quy trình con, LAP gắn MOW vào cha; CHAY chỉ named-call MOT.CHAY và còn prose “Chạy từng bước”. | Named-call không có cycle nhưng dispatch MOW con/context/join/quay về/retry chưa rõ. | Giữ definition/bước/lượt riêng; nêu truyền vào, chờ/nhận output, lỗi/trả sửa, tiếp tục đúng cha. Cao về chưa nêu. |
| 7 · CHUNG.* · gap hợp đồng vào/ra/duyệt | DUYET ghi42/63, người đọc41; NEU/CAPMA cùng ghi02 chưa truyền loại/đích; BAT đọc46 chưa nêu điều kiện đã kiểm/duyệt. | Duyệt ý/bản và mã nhu cầu/sản phẩm có thể lẫn; output/return chưa đóng. | Nêu id/version/hash, loại/đích, result/status và bước trả trong nội dung hiện có. Cao về thiếu binding; cách ghép là đề xuất. |
| 8 · 9 quy trình Nhà máy · gap lifecycle | VEUI và5 quy trình CONGCU/YEUCAU/TAILIEU/LUAT chưa có đường đầy đủ sửa→kiểm→duyệt→áp, ngừng→nơi dùng, phục hồi. CONGCU.TAO/RA chưa đọc 35 ở bước tìm/rà. | Không gọi9 quy trình là đã vận hành trọn; cập nhật và rollback còn mở. | Version đường hiện có, dùng CHUNG con, đọc đúng sổ35; xử lý sau batch thí điểm MOW. Cao về coverage chữ; không suy cần mã mới. |
| 9 · YEUCAU.GHI · TAILIEU.NHAP · LUAT.BANHANH/CHUNG.KIEM · gap tool | K13/K14 TRỐNG; K16 chưa so mâu thuẫn nội dung; K11 chỉ exact; K18 không chứng minh toàn tool readiness/quyền. Chỉ P0 có Tool bắt buộc tường minh. | Có definition không đồng nghĩa có tool bắt buộc đủ; chưa chứng nhận RUN các luồng đó. | Host/A xử lý readiness/tool bắt buộc; B giữ gap theo nguồn. Cao · đã mở metadata, không sửa Tool. |
| 10 · ml5-qt · gap definition/đếm dự tính | D=18×3=54 ô lifecycle chưa có từng definition; E ghi10 nhưng kể5+6=11, factory intro đã ghi bất nhất;6 tên E chưa có definition trong39. | ≈98 chưa là tổng cuối;54 ô+6 tên chưa chứng minh60 process unique cần thêm. | Giữ39 là số definition, tra/reuse từng candidate trước viết/chốt số; không sinh mã từ phép nhân. Cao · đọc/đếm trực tiếp. |

### 3. Model và điều C có thể suy từ B01

**Cây định nghĩa quan sát được:** MOW chứa bước MOT hoặc MOW con → MOT gắn **1 MOIT +0..n MOUT** → Form gắn Field. FORM đã chứa cả MOIT/MOUT; không kết luận thiếu hai process riêng chỉ vì dùng chung họ FORM.

Giữ ba thứ khác nhau theo P19: **định nghĩa/bản** (04 ·06/07 ·08 ·09 ·46), **chỗ gắn/nối** (10–14 ·15), **nhu cầu chế tạo và nơi đang chờ kết quả** (39/72, con trỏ cha/con — hợp đồng còn OPEN). Lượt nghiệp vụ thật ở50/51/52 không tự đồng nghĩa việc chế tạo. Một definition dùng nhiều nơi; một chỗ gắn có ngữ cảnh/trạng thái riêng. Đây là mô hình phân tích từ nguồn, chưa thêm bảng/record/field.

**Số đủ/thiếu cho C, tách mức kiểm:**

| Mức kiểm | Đủ/đạt | Thiếu/chưa chứng minh | Ý nghĩa |
|---|---:|---:|---|
| Chữ ký process đã rút theo B01 |39|0|Mã/tên/Thuộc, object/intent, input suy ra hoặc OPEN, actor/call và đọc/ghi đã có bản đồ.|
| Khuôn bước E1 chấp nhận khi kiểm từng PROCESS |33|6|PASS cú pháp là ứng viên lấy khung bước; không chứng minh mở rộng trọn nhánh/call.|
| Bản suy diễn Human Step/UI trọn luồng đã chứng minh |0|39|Nguồn này chưa chứng minh đủ hợp đồng/nhánh/đường về để đóng trọn từng definition; không có nghĩa 39 mã không dùng được.|

Tiêu chí mức cuối: đúng object–cha–chỗ gắn–version; expand mọi call/nhánh có giới hạn; rõ việc người làm/điều đã có, kết quả lưu và điều kiện đi tiếp/trả sửa/lỗi; bước có định danh truy nguồn; cùng C xác định UI dùng lại. Khối 39 chưa đưa bộ hợp đồng này cho từng process. JEV readiness **candidate_only**, p=0,85/confidence=0,79 (gen-dec-1790542522-NaVwXRX48XWO5K8Eg8x9); không phải JEV xác nhận từng dòng sai.

**Giới hạn đếm:** 62 👤/66 🤖 là dấu actor trực tiếp, chưa expand 80 call có mã, chưa gộp chỗ dùng/nhánh. CHUNG.APQUYTRINH chứa 2 👤 ghi “Người / AI”, nên62 không khẳng định 62 thao tác người vật lý. Bỏ P0 thì 60/62 khớp C12 cũ 38; không phải mất process. **18→** là Master nghiệp vụ do18 trỏ tới, không phải số19/Master mới. Không dùng 470 requirements hoặc ≈98 để suy Step/UI count.

<details>
<summary><b>Chi tiết · chữ ký đủ39 process · mở khi cần truy từng dòng</b></summary>

Actor/Master dưới đây là **trực tiếp**; phần của child ở cột calls phải expand riêng. XOA không có actor trực tiếp vẫn có thao tác người qua NEU/DUYET. Mọi bước có ghi còn đọc 35/37 theo luật chung canonical; không lặp vào mỗi ô. Input/trigger là diễn giải ngắn từ hành động hoặc metadata P0, không phải contract đăng ký. OPEN là điều nguồn chưa nêu đủ, không tự điền mặc định. Giữ mã/tên/nhãn từ canonical; không cấp mã mới.


#### Chung

| Mã · tên | Thuộc | Đối tượng | Intent | Input/trigger (đọc từ chữ; thiếu ghi OPEN) | Người · trực tiếp | Máy · trực tiếp | Process calls theo thứ tự | Master đọc · trực tiếp | Master ghi · trực tiếp |
|---|---|---|---|---|---|---|---|---|---|
| `CHUNG.APQUYTRINH` · Áp dụng quy trình trước khi làm | 🔁 | RUN/quy trình + tool | kiểm quy trình trước việc | Tường minh: yêu cầu/RUN · PROMPT · CAT-003 · CAT-006. | 2: Người / AI: thiếu process thì DỪNG; rà trùng/chồng; đề xuất + tạm chốt rồi quay lại;<br>Người / AI: process sai/lạc hậu/chồng thì DỪNG; sửa/version, giữ mã+tên+lịch sử rồi quay lại | 4: Đọc yêu cầu/RUN; tra process + tool;<br>Có process phù hợp; kiểm tool bắt buộc;<br>Gate PASS mới READY/RUN;<br>Ghi KQ/evidence/gap; lệch thực tế thì quay lại sửa process | — | 09 35 38 | 09 45 46 49 68 |
| `CHUNG.TIM` · Tìm | 🔁 | đối tượng cần tìm | tìm để dùng lại | Ý tìm theo tên/nghĩa/nhãn; danh mục đích + phạm vi/trạng thái OPEN. | 1: Tìm theo tên · nghĩa · nhãn | 0: — (xem lời gọi) | — | 01 20 48 61 64 | — |
| `CHUNG.NEU` · Nêu nhu cầu | 🔁 | nhu cầu | nêu và cấp mã nhu cầu | Nhu cầu của người/AI; quan hệ nhu cầu gốc/con và output id OPEN. | 1: Ghi 1 dòng nhu cầu (thảo luận với AI nếu có) | 1: Cấp mã nhu cầu | — | 30 61 | 02 39 72 |
| `CHUNG.DUYET` · Duyệt ý · bản | 🔁 | ý/bản + phiếu duyệt | duyệt/trả | Ý/bản cần duyệt + NT03; id/version/hash của bản và bước trả OPEN. | 1: Duyệt / trả kèm lý do | 1: Tạo phiếu, chọn người duyệt (NT03) | — | 24 30 34 40 41 75 | 42 63 73 |
| `CHUNG.CAPMA` · Cấp mã | 🔁 | đối tượng cần mã | khai sinh mã | Loại/đối tượng + NT17; phân biệt mã nhu cầu/mã sản phẩm OPEN. | 0: — (xem lời gọi) | 1: Khai sinh mã (NT17) | — | 30 | 02 |
| `CHUNG.KIEM` · Máy kiểm | 🔁 | bản cần kiểm + ca thử | máy kiểm | Bộ kiểm + ca thử theo NT21; đối tượng/version/result nối cha OPEN. | 0: — (xem lời gọi) | 2: Chạy bộ kiểm + ca thử (NT21);<br>Lỗi máy → sự cố | — | 30 43 44 | 45 63 68 |
| `CHUNG.BAT` · Bật · tắt | 🔁 | bản/nơi áp dụng | bật/phát hành | Bản ở 46; nơi/lúc/tham số người khai; điều kiện đã kiểm/duyệt OPEN. | 1: Bật: nơi · lúc · tham số | 1: Tự sinh dùng ở đâu | — | 46 | 47 48 49 71 |
| `CHUNG.NGUNG` · Ngừng | 🔁 | nơi dùng + lượt chạy | ngừng/lưu trữ | Đối tượng/nơi dùng + NT20/22; trả BLOCK/cho ngừng và đường phục hồi OPEN. | 0: — (xem lời gọi) | 2: Kiểm nơi dùng · lượt đang chạy (NT20);<br>Ngừng · lưu trữ (NT22) | — | 30 48 50 | 47 49 71 |

#### Field

| Mã · tên | Thuộc | Đối tượng | Intent | Input/trigger (đọc từ chữ; thiếu ghi OPEN) | Người · trực tiếp | Máy · trực tiếp | Process calls theo thứ tự | Master đọc · trực tiếp | Master ghi · trực tiếp |
|---|---|---|---|---|---|---|---|---|---|
| `FIELD.TAO` · Field · tạo mới | ⚙️ | định nghĩa FIELD | tạo bản mới | Nhu cầu sau tìm/duyệt; chọn bản con và nhánh con thiếu OPEN. | 1: Khai Field: tên · kiểu · đơn vị · cột lưu · khoá ngoại | 1: Đồng bộ cột vật lý (FIELD_SYNC) | `CHUNG.TIM` → `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.CAPMA` → `CHUNG.KIEM` → `CHUNG.DUYET` → `CHUNG.BAT`;<br>OPEN: Thiếu bộ giá trị / khái niệm | 03 05 17 18 19 20 28 30 61 | 04 46 49 64 76 |
| `FIELD.LAP` · Field · lắp ráp (có rồi, gọi lại) | ⚙️ | chỗ gắn FIELD vào cha | lắp bản đã có | Bản có sẵn + cha; id/version của cả hai và mapping/output OPEN. | 1: Gắn vào cha | 2: Kiểm bản · quyền;<br>Tự sinh dùng ở đâu | `CHUNG.TIM` | 44 46 75 | 14 45 48 49 |
| `FIELD.KHAI` · Field · khai báo (cấu hình chỗ dùng) | ⚙️ | cấu hình tại chỗ dùng FIELD | cấu hình chỗ dùng | Chỗ gắn đã chọn; điều kiện cần duyệt + kết quả quay về OPEN. | 1: Cấu hình Field trong form: hiện-ẩn · tự điền · tính · kiểm hợp lệ (NT13–16) | 0: — (xem lời gọi) | `CHUNG.DUYET` → `CHUNG.BAT`;<br>OPEN: Nếu nguyên tắc cần duyệt | 29 31 | 14 30 |
| `FIELD.SUA` · Field · sửa · nâng cấp | ⚙️ | bản mới + các chỗ dùng FIELD | sửa/nâng cấp | Bản hiện hành + nhu cầu sửa; clone liên kết/giữ con + nơi áp dụng OPEN. | 2: Khai Field: tên · kiểu · đơn vị · cột lưu · khoá ngoại;<br>Áp khi sửa: tất cả / chỉ nơi này (NT19) | 2: Xem ảnh hưởng: dùng ở đâu · lượt đang chạy;<br>Nhân bản thành bản mới (không sửa đè) | `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.KIEM` → `CHUNG.DUYET` → `CHUNG.BAT` | 03 05 17 18 19 20 28 30 46 48 50 61 | 04 30 46 49 64 |
| `FIELD.XOA` · Field · xoá (= ngừng, không xoá thật) | ⚙️ | đối tượng/nơi áp dụng FIELD | đề nghị ngừng | Đối tượng muốn ngừng; ngữ cảnh truyền vào CHUNG.* chưa nêu. | 0: — (xem lời gọi) | 0: — (xem lời gọi) | `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.NGUNG` | — | — |

#### Form · MOIT/MOUT

| Mã · tên | Thuộc | Đối tượng | Intent | Input/trigger (đọc từ chữ; thiếu ghi OPEN) | Người · trực tiếp | Máy · trực tiếp | Process calls theo thứ tự | Master đọc · trực tiếp | Master ghi · trực tiếp |
|---|---|---|---|---|---|---|---|---|---|
| `FORM.TAO` · Form (MOIT · MOUT) · tạo mới | ⚙️ | định nghĩa FORM | tạo bản mới | Nhu cầu sau tìm/duyệt; chọn bản con và nhánh con thiếu OPEN. | 3: Chọn loại MOIT / MOUT, khai form;<br>Gắn Field vào form (bắt buộc · mặc định · thứ tự);<br>MOUT: định nghĩa đếm · chỉ số | 0: — (xem lời gọi) | `CHUNG.TIM` → `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.CAPMA` → `CHUNG.KIEM` → `CHUNG.DUYET` → `CHUNG.BAT` | 04 05 17 18 30 57 | 06 07 14 46 49 64 69 |
| `FORM.LAP` · Form (MOIT · MOUT) · lắp ráp (có rồi, gọi lại) | ⚙️ | chỗ gắn FORM vào cha | lắp bản đã có | Bản có sẵn + cha; id/version của cả hai và mapping/output OPEN. | 1: Gắn vào cha | 2: Kiểm bản · quyền;<br>Tự sinh dùng ở đâu | `CHUNG.TIM` | 44 46 75 | 13 45 48 49 |
| `FORM.KHAI` · Form (MOIT · MOUT) · khai báo (cấu hình chỗ dùng) | ⚙️ | cấu hình tại chỗ dùng FORM | cấu hình chỗ dùng | Chỗ gắn đã chọn; điều kiện cần duyệt + kết quả quay về OPEN. | 1: Cấu hình form trong MOT: nhập / đọc · bản ghi nguồn–đích · phân phối (NT18) | 0: — (xem lời gọi) | `CHUNG.DUYET` → `CHUNG.BAT`;<br>OPEN: Nếu nguyên tắc cần duyệt | 18 34 | 10 13 30 |
| `FORM.SUA` · Form (MOIT · MOUT) · sửa · nâng cấp | ⚙️ | bản mới + các chỗ dùng FORM | sửa/nâng cấp | Bản hiện hành + nhu cầu sửa; clone liên kết/giữ con + nơi áp dụng OPEN. | 2: Chọn loại MOIT / MOUT, khai form;<br>Áp khi sửa: tất cả / chỉ nơi này (NT19) | 2: Xem ảnh hưởng: dùng ở đâu · lượt đang chạy;<br>Nhân bản thành bản mới (không sửa đè) | `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.KIEM` → `CHUNG.DUYET` → `CHUNG.BAT` | 05 17 18 46 48 50 | 06 07 30 46 49 64 |
| `FORM.XOA` · Form (MOIT · MOUT) · xoá (= ngừng, không xoá thật) | ⚙️ | đối tượng/nơi áp dụng FORM | đề nghị ngừng | Đối tượng muốn ngừng; ngữ cảnh truyền vào CHUNG.* chưa nêu. | 0: — (xem lời gọi) | 0: — (xem lời gọi) | `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.NGUNG` | — | — |

#### MOT

| Mã · tên | Thuộc | Đối tượng | Intent | Input/trigger (đọc từ chữ; thiếu ghi OPEN) | Người · trực tiếp | Máy · trực tiếp | Process calls theo thứ tự | Master đọc · trực tiếp | Master ghi · trực tiếp |
|---|---|---|---|---|---|---|---|---|---|
| `MOT.TAO` · MOT · tạo mới | ⚙️ | định nghĩa MOT | tạo bản mới | Nhu cầu sau tìm/duyệt; chọn bản con và nhánh con thiếu OPEN. | 3: Khai MOT: tên · loại việc · người / máy làm;<br>Gắn form (1 MOIT + 0..n MOUT);<br>Hợp đồng vào/ra: loại bản ghi · lấy từ đâu · tạo / cập nhật · 0/1/n | 0: — (xem lời gọi) | `CHUNG.TIM` → `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.CAPMA` → `CHUNG.KIEM` → `CHUNG.DUYET` → `CHUNG.BAT` | 02 06 07 18 26 27 | 08 10 13 46 49 64 |
| `MOT.LAP` · MOT · lắp ráp (có rồi, gọi lại) | ⚙️ | chỗ gắn MOT vào cha | lắp bản đã có | Bản có sẵn + cha; id/version của cả hai và mapping/output OPEN. | 1: Gắn vào cha | 2: Kiểm bản · quyền;<br>Tự sinh dùng ở đâu | `CHUNG.TIM` | 44 46 75 | 11 12 45 48 49 |
| `MOT.KHAI` · MOT · khai báo (cấu hình chỗ dùng) | ⚙️ | cấu hình tại chỗ dùng MOT | cấu hình chỗ dùng | Chỗ gắn đã chọn; điều kiện cần duyệt + kết quả quay về OPEN. | 1: Cấu hình MOT trong MOW: giao việc · làm thay · hạn · nhắc · leo thang · trả sửa (NT01–07, 12) | 0: — (xem lời gọi) | `CHUNG.DUYET` → `CHUNG.BAT`;<br>OPEN: Nếu nguyên tắc cần duyệt | 22 23 24 29 31 34 | 11 25 30 |
| `MOT.SUA` · MOT · sửa · nâng cấp | ⚙️ | bản mới + các chỗ dùng MOT | sửa/nâng cấp | Bản hiện hành + nhu cầu sửa; clone liên kết/giữ con + nơi áp dụng OPEN. | 2: Khai MOT: tên · loại việc · người / máy làm;<br>Áp khi sửa: tất cả / chỉ nơi này (NT19) | 2: Xem ảnh hưởng: dùng ở đâu · lượt đang chạy;<br>Nhân bản thành bản mới (không sửa đè) | `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.KIEM` → `CHUNG.DUYET` → `CHUNG.BAT` | 26 27 46 48 50 | 08 30 46 49 64 |
| `MOT.XOA` · MOT · xoá (= ngừng, không xoá thật) | ⚙️ | đối tượng/nơi áp dụng MOT | đề nghị ngừng | Đối tượng muốn ngừng; ngữ cảnh truyền vào CHUNG.* chưa nêu. | 0: — (xem lời gọi) | 0: — (xem lời gọi) | `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.NGUNG` | — | — |
| `MOT.CHAY` · MOT · chạy (việc thật) | ⚙️ | việc thật + bản ghi | chạy nghiệp vụ | Việc/bản ghi/người/hạn; form MOUT và kết quả lỗi/đường quay về OPEN. | 3: Nhận · mở form với đúng bản ghi;<br>Lưu / gửi (khoá chống trùng · kết quả);<br>Tệp · bình luận | 7: Giao việc (NT01): bản ghi · người · hạn;<br>Báo người nhận;<br>Ghi bản ghi vào danh sách nghiệp vụ đích (18 trỏ tới) + mã bản ghi;<br>Đọc lại: lưu đúng mới cho chuyển bước;<br>Ghi sự kiện “đã lưu” (sự kiện không thay dữ liệu nghiệp vụ);<br>Bàn giao sản phẩm;<br>Lỗi: thử lại (NT11) → sự cố · trả sửa (NT12) | — | 02 06 10 14 18 18→ 23 30 34 54 | 02 18→ 51 52 53 54 55 56 63 68 73 74 |

#### MOW

| Mã · tên | Thuộc | Đối tượng | Intent | Input/trigger (đọc từ chữ; thiếu ghi OPEN) | Người · trực tiếp | Máy · trực tiếp | Process calls theo thứ tự | Master đọc · trực tiếp | Master ghi · trực tiếp |
|---|---|---|---|---|---|---|---|---|---|
| `MOW.TAO` · MOW · tạo mới | ⚙️ | định nghĩa MOW | tạo bản mới | Nhu cầu sau tìm/duyệt; chọn bản con và nhánh con thiếu OPEN. | 3: Khai MOW: tên · loại · neo T2;<br>Xếp bước: MOT / quy trình con;<br>Nối bước trước → sau (song song · hội tụ · điều kiện) | 2: AI phác thảo từ thảo luận (tay trước, máy sau);<br>Khoá gói phiên bản | `CHUNG.TIM` → `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.CAPMA` → `CHUNG.KIEM` → `CHUNG.DUYET` → `CHUNG.BAT` | 06 07 08 09 21 22 26 27 31 72 | 09 11 12 46 49 64 |
| `MOW.LAP` · MOW · lắp ráp (có rồi, gọi lại) | ⚙️ | chỗ gắn MOW vào cha | lắp bản đã có | Bản có sẵn + cha; id/version của cả hai và mapping/output OPEN. | 1: Gắn vào cha | 2: Kiểm bản · quyền;<br>Tự sinh dùng ở đâu | `CHUNG.TIM` | 44 46 75 | 11 15 45 48 49 |
| `MOW.KHAI` · MOW · khai báo (cấu hình chỗ dùng) | ⚙️ | cấu hình tại chỗ dùng MOW | cấu hình chỗ dùng | Chỗ gắn đã chọn; điều kiện cần duyệt + kết quả quay về OPEN. | 1: Cấu hình nơi chạy: trigger · khuôn ↔ đơn vị · kho lưu · kích hoạt · rẽ nhánh · quyền (NT03, 05, 08, 09) | 0: — (xem lời gọi) | `CHUNG.DUYET` → `CHUNG.BAT`;<br>OPEN: Nếu nguyên tắc cần duyệt | 17 18 22 31 32 33 | 15 16 30 47 75 |
| `MOW.SUA` · MOW · sửa · nâng cấp | ⚙️ | bản mới + các chỗ dùng MOW | sửa/nâng cấp | Bản hiện hành + nhu cầu sửa; clone liên kết/giữ con + nơi áp dụng OPEN. | 2: Khai MOW: tên · loại · neo T2;<br>Áp khi sửa: tất cả / chỉ nơi này (NT19) | 2: Xem ảnh hưởng: dùng ở đâu · lượt đang chạy;<br>Nhân bản thành bản mới (không sửa đè) | `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.KIEM` → `CHUNG.DUYET` → `CHUNG.BAT` | 21 22 46 48 50 | 09 30 46 49 64 |
| `MOW.XOA` · MOW · xoá (= ngừng, không xoá thật) | ⚙️ | đối tượng/nơi áp dụng MOW | đề nghị ngừng | Đối tượng muốn ngừng; ngữ cảnh truyền vào CHUNG.* chưa nêu. | 0: — (xem lời gọi) | 0: — (xem lời gọi) | `CHUNG.NEU` → `CHUNG.DUYET` → `CHUNG.NGUNG` | — | — |
| `MOW.CHAY` · MOW · chạy (lượt) | ⚙️ | lượt MOW + gói phiên bản | chạy nghiệp vụ | Trigger đã gắn + hồ sơ/gói bản; bước con/nhánh/join/quay về OPEN. | 1: Theo dõi lượt | 5: Tín hiệu đến (trigger đã gắn);<br>Mở lượt: gói phiên bản · hồ sơ chính;<br>Rẽ nhánh · bước sau (NT09);<br>Nhắc · leo thang (NT07 · NT04);<br>Kết thúc / hỏng (NT10) | `MOT.CHAY`;<br>OPEN: Chạy từng bước | 02 12 18 30 32 46 47 57 69 70 | 50 55 56 63 |

#### Vẽ UI

| Mã · tên | Thuộc | Đối tượng | Intent | Input/trigger (đọc từ chữ; thiếu ghi OPEN) | Người · trực tiếp | Máy · trực tiếp | Process calls theo thứ tự | Master đọc · trực tiếp | Master ghi · trực tiếp |
|---|---|---|---|---|---|---|---|---|---|
| `VEUI.FIELD` · Vẽ UI của Field | 🏗 | UI của FIELD | vẽ/kiểm/đấu nối/ban hành | Các luồng đối tượng + bước ở 11; thiếu cách expand call/nhánh và nhận đúng phiên bản bước. | 5: Mỗi bước người → một màn (mã = bước + UI cha);<br>Đầu bài: hợp đồng thông tin · khái niệm · câu hỏi UIQ;<br>Vẽ nháp;<br>Kiểm người mới làm được;<br>Hướng dẫn · ban hành | 2: Lấy đủ bước của các luồng FIELD.*;<br>Đấu nối: bảng hiển thị · đường mở · module | `CHUNG.DUYET` | 11 44 58 61 67 | 45 46 47 49 59 60 62 65 66 |
| `VEUI.FORM` · Vẽ UI của Form (MOIT · MOUT) | 🏗 | UI của FORM | vẽ/kiểm/đấu nối/ban hành | Các luồng đối tượng + bước ở 11; thiếu cách expand call/nhánh và nhận đúng phiên bản bước. | 5: Mỗi bước người → một màn (mã = bước + UI cha);<br>Đầu bài: hợp đồng thông tin · khái niệm · câu hỏi UIQ;<br>Vẽ nháp;<br>Kiểm người mới làm được;<br>Hướng dẫn · ban hành | 2: Lấy đủ bước của các luồng FORM.*;<br>Đấu nối: bảng hiển thị · đường mở · module | `CHUNG.DUYET` | 11 44 58 61 67 | 45 46 47 49 59 60 62 65 66 |
| `VEUI.MOT` · Vẽ UI của MOT | 🏗 | UI của MOT | vẽ/kiểm/đấu nối/ban hành | Các luồng đối tượng + bước ở 11; thiếu cách expand call/nhánh và nhận đúng phiên bản bước. | 5: Mỗi bước người → một màn (mã = bước + UI cha);<br>Đầu bài: hợp đồng thông tin · khái niệm · câu hỏi UIQ;<br>Vẽ nháp;<br>Kiểm người mới làm được;<br>Hướng dẫn · ban hành | 2: Lấy đủ bước của các luồng MOT.*;<br>Đấu nối: bảng hiển thị · đường mở · module | `CHUNG.DUYET` | 11 44 58 61 67 | 45 46 47 49 59 60 62 65 66 |
| `VEUI.MOW` · Vẽ UI của MOW | 🏗 | UI của MOW | vẽ/kiểm/đấu nối/ban hành | Các luồng đối tượng + bước ở 11; thiếu cách expand call/nhánh và nhận đúng phiên bản bước. | 5: Mỗi bước người → một màn (mã = bước + UI cha);<br>Đầu bài: hợp đồng thông tin · khái niệm · câu hỏi UIQ;<br>Vẽ nháp;<br>Kiểm người mới làm được;<br>Hướng dẫn · ban hành | 2: Lấy đủ bước của các luồng MOW.*;<br>Đấu nối: bảng hiển thị · đường mở · module | `CHUNG.DUYET` | 11 44 58 61 67 | 45 46 47 49 59 60 62 65 66 |

#### Công cụ

| Mã · tên | Thuộc | Đối tượng | Intent | Input/trigger (đọc từ chữ; thiếu ghi OPEN) | Người · trực tiếp | Máy · trực tiếp | Process calls theo thứ tự | Master đọc · trực tiếp | Master ghi · trực tiếp |
|---|---|---|---|---|---|---|---|---|---|
| `CONGCU.TAO` · Nhà máy · đăng ký công cụ | 🏗 | định nghĩa/tool nguồn | đăng ký công cụ | Nhu cầu công cụ + TEMPLATE-DOT-SCRIPT; sổ 35 chưa được đọc ở bước tìm. | 1: Viết theo khuôn TEMPLATE-DOT-SCRIPT: mã · việc · loại A/B · phạm vi · cặp A↔B | 4: Tìm trùng: sổ công cụ + phạm vi (JEV so mô tả);<br>Chạy thử trên ca thử;<br>Đăng ký sổ (DOT-REGISTER) + cập nhật độ phủ;<br>Nhập kho: xưởng thử → /opt/incomex/dot | `CHUNG.NEU` → `CHUNG.DUYET` | 36 38 44 | 35 38 45 46 49 63 71 |
| `CONGCU.RA` · Nhà máy · rà trùng · phủ công cụ | 🏗 | ma trận công cụ/phạm vi | rà trùng/phủ | Phạm vi × công cụ + đĩa; dòng đọc sổ 35 chưa nêu. | 1: Ô trống → nêu nhu cầu · ô chồng → ghi luật chồng hoặc gộp | 4: Dựng ma trận phạm vi × công cụ;<br>So sổ công cụ với đĩa · lệch → sự cố;<br>JEV so trùng từng cặp cùng ô;<br>Báo cáo độ phủ | — | 36 38 69 | 38 39 63 68 70 |

#### Chỉ đạo Owner

| Mã · tên | Thuộc | Đối tượng | Intent | Input/trigger (đọc từ chữ; thiếu ghi OPEN) | Người · trực tiếp | Máy · trực tiếp | Process calls theo thứ tự | Master đọc · trực tiếp | Master ghi · trực tiếp |
|---|---|---|---|---|---|---|---|---|---|
| `YEUCAU.GHI` · Nhà máy · ghi chỉ đạo Owner (bồi đắp) | 🏗 | chỉ đạo Owner | ghi/rá thực hiện chỉ đạo | Chỉ đạo Owner + các D cũ; loại bản ghi ở 39 và revision evidence OPEN. | 1: Ghi dòng D: mã · ngày · ý · trạng thái · nơi làm | 2: Tìm trùng · mâu thuẫn với chỉ đạo cũ (JEV);<br>Rà mỗi lượt: đã làm · chưa làm · thay thế | — | 09 39 46 | 39 49 63 |

#### Tài liệu

| Mã · tên | Thuộc | Đối tượng | Intent | Input/trigger (đọc từ chữ; thiếu ghi OPEN) | Người · trực tiếp | Máy · trực tiếp | Process calls theo thứ tự | Master đọc · trực tiếp | Master ghi · trực tiếp |
|---|---|---|---|---|---|---|---|---|---|
| `TAILIEU.NHAP` · Nhà máy · nhập tài liệu thiết kế | 🏗 | tài liệu nguồn + KB | nhập/sửa/đồng bộ | Chủ đề + tài liệu nguồn repo; revision, cách so kết quả/đường lỗi OPEN. | 1: Sửa đúng tài liệu nguồn ở repo, không tạo file mới | 3: Tìm tài liệu cùng chủ đề (1 chủ đề = 1 nguồn);<br>Đồng bộ sang KB để tra cứu;<br>Kiểm trùng nội dung | — | 44 61 84 | 45 46 64 84 |

#### Luật

| Mã · tên | Thuộc | Đối tượng | Intent | Input/trigger (đọc từ chữ; thiếu ghi OPEN) | Người · trực tiếp | Máy · trực tiếp | Process calls theo thứ tự | Master đọc · trực tiếp | Master ghi · trực tiếp |
|---|---|---|---|---|---|---|---|---|---|
| `LUAT.BANHANH` · Nhà máy · ban hành luật · quy định | 🏗 | luật/quy định + nơi áp dụng | dự thảo/ban hành/kiểm | Luật cũ + câu hỏi kiểm khung; revision/phạm vi/rollback OPEN. | 2: Dự thảo;<br>Ban hành + chốt cưỡng chế (R2) | 2: 4 câu khung: có luật chưa · đủ chưa · thực tế theo chưa · xung đột không;<br>Kiểm tuân thủ định kỳ | `CHUNG.DUYET` | 30 44 83 | 45 46 47 49 68 83 |

</details>

<details>
<summary><b>Chi tiết · 8 case JEV về chồng/dùng chung · kết quả và cách dùng</b></summary>

Result **gen-dec-1790542448-sNWqEQdK7zcXOJ1F1Cjs** · model do gateway trả **typesafe/jev-1.13-20260917** · raw/faithful definitions từ catalog SHA bên dưới. Tám câu hỏi có lựa chọn: gộp toàn bộ / dùng chung phần / giữ riêng / chưa đủ dữ kiện. State chứa chữ definition, không chèn kết luận mong muốn. Bảng tách p của lựa chọn và confidence gateway.

| Case | JEV chọn | p | confidence | Đề xuất của B · chưa chốt canonical |
|---|---|---:|---:|---|
| CHUNG.NEU ↔ YEUCAU.GHI | Dùng chung phần | 0,73 | 0,63 | Giữ nhu cầu và chỉ đạo Owner khác loại/chủ thể; reuse khi binding39 rõ. |
| CHUNG.NEU ↔ CHUNG.CAPMA trong TAO | Giữ riêng · chưa chắc | 0,53 | 0,37 | shared_part=0,45; làm rõ mã nhu cầu→mã sản phẩm, chưa gộp. |
| CONGCU.TAO ↔ CONGCU.RA | Dùng chung phần | 0,83 | 0,77 | Reuse rà trước đăng ký/định kỳ; không gộp toàn đăng ký và báo phủ. |
| 4 *.XOA ↔ CHUNG.NGUNG | Dùng chung phần | 0,98 | 0,98 | XOA là wrapper nêu→duyệt→ngừng, giữ đối tượng/mã; dùng child NGUNG. |
| MOW.KHAI ↔ CHUNG.BAT | Dùng chung phần | 0,70 | 0,59 | Rõ cấu hình47/phát hành47/71, chuyển tham số để không nhập hai lần. |
| FORM.KHAI ↔ phần gắn form/hợp đồng trong MOT.TAO | Dùng chung phần | 0,82 | 0,76 | Chốt chủ ghi hợp đồng10/chỗ gắn13 và reuse từ hai cửa vào. |
| CHUNG.BAT ↔ CHUNG.NGUNG | Giữ riêng · chưa chắc | 0,49 | 0,33 | shared_part cũng0,49; BAT có tên “tắt” nhưng body chỉ bật. Chưa gộp. |
| 4 VEUI.* | Dùng chung phần | 0,99 | 0,98 | Dùng một khuôn tham số, giữ4 mã/đích; chưa suy4 là UI count. |

**overlap=8** là 8 quan hệ candidate đã rà/hỏi, không phải 8 bản trùng được xác nhận. Không có lựa chọn merge_full thắng; birth_target/activate_stop thấp confidence vẫn OPEN. Wrapper XOA cùng body và VEUI cùng khuôn không bị coi mất định danh đối tượng. Không kiểm/gộp Tool theo tên trùng.

Result phụ **gen-dec-1790542522-NaVwXRX48XWO5K8Eg8x9**: readiness candidate_only p=0,85/confidence=0,79; NEXT mow_search p=1/confidence=1. Urgency của 10 gap chỉ tham khảo, confidence 0–0,85; không dùng điểm thấp để đóng gap hoặc quyết thứ tự máy móc.

| Gap key | Urgency /4 | confidence |
|---|---:|---:|
| child_attach | 2.75 | 0.00 |
| context_return | 2.90 | 0.08 |
| factory_lifecycle | 2.02 | 0.00 |
| forecast | 1.41 | 0.00 |
| runtime_return | 2.18 | 0.21 |
| search | 3.82 | 0.85 |
| step_ui | 3.37 | 0.48 |
| structural_edit | 2.40 | 0.13 |
| symbolic | 3.17 | 0.58 |
| tool_readiness | 3.15 | 0.30 |

Chi phí provider trả: lượt 1 USD 0.000230244; lượt 2 USD 0.000851886; tổng USD 0.00108213. Chi phí Codex/phiên khác UNKNOWN; không nhân giá tay.

</details>

<details>
<summary><b>Chi tiết · phần mới nêu ở khung, lifecycle và giới hạn nguồn</b></summary>

- Nhóm D mới có 18 loại × tạo/sửa/ngừng = 54 ô dự tính: giá trị · mẫu ô nhập · hợp đồng vào/ra · bảng · đối tượng nghiệp vụ · nhãn · cây tổ chức · người · vai · ủy quyền · agent · nguyên tắc · điều kiện · trigger · loại sự kiện · bộ kiểm · UI cha · hướng dẫn. **Chưa có từng definition này trong khối 39.** Không cấp tên/mã hoặc coi 54 là 54 workflow độc lập sau reuse.
- Nhóm E đã viết 5: CONGCU.TAO/RA · YEUCAU.GHI · TAILIEU.NHAP · LUAT.BANHANH. Còn 6 tên chưa có definition trong 39: thêm danh sách · ngừng danh sách · kiểm thiếu · xử lý sự cố · đấu nối nguồn ngoài · nhập từ hệ cũ. Bảng E ghi 10 trong khi 5+6=11; factory intro đã nhận diện. **39+54+6=99 chỉ là phép cộng ô/tên trước rà trùng**, không phải tổng process unique hoặc đề xuất mở 60 quy trình.
- Nhóm F n là quy trình thương mại (phái cử L001, nhập kho WF-0001...), ngoài batch 39; không kết luận thiếu toàn repo hoặc mở nghiên cứu thêm.
- Exact tên/mã trùng=0; named-call thiếu đích=0; cycle named-call=0. Sáu prose-call và dispatch MOW động không nằm trong đồ thị, nên **không chứng minh toàn mô hình không có vòng**. P0 có vòng quay lại sửa/version trong lời văn; cần điều kiện/bản quay lại, không tự gán là cycle named-call.
- Lifecycle 20 của bốn họ có TAO/LAP/KHAI/SUA/XOA; XOA ghi rõ ngừng, không xoá thật. Gap là hợp đồng/liên kết/version/phục hồi/kiểm, không phải thiếu năm tên khuôn mỗi họ.
- Case gộp còn OPEN; một template dùng lại được không đồng nghĩa gộp mã. BAT có tên “Bật · tắt” nhưng body chỉ “Bật” là khác biệt chữ thực; ngữ nghĩa tắt/ngừng cần Host chốt.
- Tool catalogue là metadata/readiness: K13/K14 trống, K11 semantic OPEN, K16 content conflict chưa chứng minh. Gate/JEV B01 chạy thật; không tuyên bố tool khác đã bind/chạy hoặc đủ quyền. Không mở 79 Master, không sửa Tool/Step/UI.

</details>

<details>
<summary><b>Bằng chứng chạy thật · gate, chữ ký, version và phạm vi ghi</b></summary>

- Executor_Surface: **Codex** · Write_Path: **connector workspace_*** đã audit. Read-gate/nguồn fresh qua workspace gateway; local clone thiếu lane-b chỉ dùng định vị, không ghi/push local.
- READY kiểm bằng workspace_log: **8794c1fa9c868db731a6e1b9d4b99dad56e56c53** đúng commit cuối chạm lane-b/PROMPT.md; RUN_ID/PROCESS khớp lệnh Owner và D60.
- Gate đúng lệnh PROMPT trên isolated snapshot **a64e26fef286b44242677b86e5982151aeb9ce05**: job **8bbc4e968e6643de9cf41c5564f79c79**, exit 0; PROCESS_GATE=PASS · process=CHUNG.TIM · process_count=39 · step_count=1 · reason=OK.
- Audit chỉ đọc, cùng snapshot: job **9ccc3d4d5b544e4294a5249f5c9d08f0**, exit 0. Dùng chính CatalogParser/evaluate của gate; tạo dòng PROCESS trong bộ nhớ để thử 39 mã, **không phát RUN mới/không ghi fixture**. 33 PASS/6 BLOCK; 62/66 actor trực tiếp; 80 named-call occurrences; 6 prose-call occurrences; thiếu/cycle named-call=0. Mỗi con số có phạm vi như phần trên.
- Catalog ban-duyet.html: SHA256 **ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7**.
- Prompt lane-b: SHA256 **86ecde4f60461e33cd19b5ab6ce4407885fb71c9e1c16c228a0ccbcc0fe8680d**.
- Gate source cong-cu/dot-process-gate.py: SHA256 **de2fa6cebc32b6db1b9484aaec89db6566f548370ff77912c6fb39d8aa5b9b7c**.
- Parent COLLAB: SHA256 **4f68f65b5a260d25718e3c3f0b58fc441bcb8e6fca49b22419e7bba6ad04f80f**. Evidence gắn các version này; HEAD ở dòng KQ là source HEAD fresh trước transaction, không phải hash tự tham chiếu của commit đang tạo.
- Chỉ path ghi **lane-b/COLLAB.md**; một transaction expected_head/expected_version; **Áp: SAME_COMMIT**. Canonical ban-duyet/COLLAB cha, lane-b/PROMPT, Tool/Step/UI/VPS/PG read-only. Không tạo file/prototype/pipeline mới. Không sửa HTML nên không có lượt publish Owner View.
- Giới hạn: chỉ rà 39 definitions + khung/tool window PROMPT chỉ; không audit runtime/schema 79 Master/toàn repo. PASS cú pháp và KQ XONG B01 không thay Host nghiệm thu, kiểm P0 chọn đúng quy trình hay READY batch mới.
- Ghi nhận gap CHUNG.TIM là kết quả audit; B01 không chạy quyết định reuse/new hoặc mutation catalog nghiệp vụ dựa vào cuộc tìm thiếu đích ấy. Gate B01 PASS chỉ là E1, chưa biến CHUNG.TIM thành quy trình đã đủ contract.

</details>

### NEXT · đúng một batch đề xuất

**Host chốt một batch thí điểm CHUNG.TIM + MOW.TAO/LAP/KHAI/SUA/CHAY, ràng buộc đích tìm và gọi/nhận kết quả con.** Kiểm chứng trên **một ca MOW có quy trình con**: tìm đúng catalog theo loại/phạm vi/version; phân biệt definition–chỗ gắn–nhu cầu con; gọi khuôn con có sẵn; nêu output/đường quay về; giữ liên kết khi sửa và xử lý MOW lồng. Giữ mã/tên, Host chốt nội dung/version ở CAT-003; C nhận bước ứng viên có nguồn. Batch thí điểm không mặc nhiên giải quyết mọi gap FIELD/FORM/MOT hoặc cả 39. Không tự B02/triển khai đề xuất sau KQ.
