# QTTH 006 — Quy trình thực hiện QTTH 05

**Mã:** `MOW-TH-006` · **Tên:** Quy trình thực hiện QTTH 05. Là một **quy trình** mới theo chỉ đạo Owner, không tạo đối tượng “hướng dẫn” độc lập.  
**Phiên:** `0.1-owner-directed-design` (12/10/2026).  
**Trạng thái:** Có **100 bước thiết kế** trong tệp repo; **chưa tích hợp vào Master quy trình tổng hợp/UI và chưa nghiệm thu QTTH 006**. Việc tích hợp do Codex Host nội dung thực hiện sau khi Owner giao lượt tiếp theo.

## 1. Đường đi và nguyên tắc

**QTTH 05 là bản đồ 7 mốc. QTTH 06 là các bước thực hiện chi tiết nằm dưới từng mốc.** 006 tham chiếu CP01–CP07 của 005, **không tạo 7 checkpoint thứ hai, không tự gọi lại 006 thành vòng lặp**.

**CP01 Khai việc → CP02 Chuẩn bị đủ → CP03 Xác nhận bắt đầu → CP04 Làm theo quy trình → CP05 Kiểm đầu ra → CP06 Duyệt kết quả → CP07 Bàn giao · kết thúc.** Bảng có các nhóm **14 + 26 + 12 + 24 + 13 + 5 + 6 = 100 bước**. Bước “nếu/khi phát sinh” không bắt thực hiện khi không có nhánh.

**Mỗi dữ liệu có sổ:** cột Nơi ghi kết quả phải chỉ mã/tên Master đích; chưa rõ sổ/khóa/quyền/sản phẩm thì ghi **Vướng** tại CAT-069? với người xử lý và bước quay lại. Từ hai thành phần cùng loại trở lên tra Master chung hiện có trước khi đề xuất bổ sung; không tạo Master trùng.

**Dùng lại công cụ:** tra `ML-DEF-024 · Master DOT`, `ML-DEF-023 · Master Tool`; kiểm phiên/hash/quyền/tình trạng trước dùng. CAT-012 giữ ca, CAT-015 kết quả; JEV nếu được dùng chỉ hỗ trợ lựa chọn hữu hạn, không ký duyệt.

**Một nguồn thực thi:** định nghĩa bước này ở `work/tools-quy-trinh/MOW-TH-006.md` là nguồn tạm trước khi Host đưa vào catalog. Sau tích hợp chỉ có **một** SSOT cho bước; nếu catalog làm nguồn chính, Markdown này là bản chiếu/trỏ có phiên/hash. Trạng thái/bằng chứng từng bước thuộc đúng hồ sơ việc DEF 00.1 (CAT-227*) cùng các Master kết quả, gắn `application_id + process_version + target_version + step_id`; không mở sổ kết quả 006 riêng.

**Tình trạng chỉ:** **Trống / Hoàn thành / Vướng**. Hoàn thành có bằng chứng và đọc lại đúng phiên; Vướng ghi thiếu gì, ai xử lý, quay lại đâu. **Việc bổ sung** có checkbox riêng: các dòng gốc ☐, dòng mới tại riêng hồ sơ `006-023-B01` đánh ☑, gắn bước cha, nguồn yêu cầu, người làm, nơi ghi và đủ 8 cột. Checkbox này **không** phải nút duyệt/xong.

**Không hồi tố giả:** MOW001 P37 đã **7/7 mốc theo QTTH 05**, nhưng chưa có lịch sử 100 bước của 006. Không tự biến 7/7 thành 100/100. G1 không là G2/G3/PG.

## 2. Bảng 100 bước, thu/mở theo 7 mốc

Trạng thái “Trống” và ☐ trong bảng **là mẫu định nghĩa**, không phải tiến độ đã thực hiện của bất kỳ hồ sơ nào.

<details>
<summary><b>CP01 — Khai việc, 14 bước</b> · bấm mở/thu</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (mã + tên Master List) | Tool use (nếu có) | Tình trạng | Việc bổ sung | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **006-001** | Đọc nguyên yêu cầu Owner và điều không được làm | Có mục tiêu/người giao/nguồn rõ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | ☐ | Không tự thay ý Owner |
| **006-002** | Đối chiếu A0, xác nhận phạm vi và quyền Owner | Có phạm vi được xác nhận | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | ☐ | Lời tiếp tục không là duyệt |
| **006-003** | Tra mã và mục tiêu của việc đã có trước khi mở | Không tạo hồ sơ trùng | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-005 · Kiểm Master | Trống | ☐ | Tìm bằng mã |
| **006-004** | Ghi mã việc, người giữ và nguồn yêu cầu | Hồ sơ mở được đúng ID | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | ☐ | Một hồ sơ việc |
| **006-005** | Chọn MOW-TH-005 và phiên 7 checkpoint | Mã/phiên 005 khớp | ML-MOW-TH-001 · Master quy trình tổng hợp | TQT-CHECK-002 · Kiểm mã | Trống | ☐ | 006 không tự gọi 006 |
| **006-006** | Tra đúng đối tượng MOW đang làm | Có bản MOW đúng phiên | ML-DEF-004 · Master MOW | TQT-CHECK-005 · Kiểm Master | Trống | ☐ | Không mượn MOW khác |
| **006-007** | Tra MOT thuộc MOW và phiên của từng MOT | Quan hệ cha–con đúng | ML-DEF-005 · Master MOT | TQT-CHECK-002 · Kiểm mã | Trống | ☐ | Số MOT tùy việc |
| **006-008** | Ghi giai đoạn G1/G2/G3 của lượt này | Phạm vi giai đoạn rõ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | ☐ | G1 không là G2/PG |
| **006-009** | Ghi điều không làm và điều mở lại về sau | Giới hạn phạm vi được lưu | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | ☐ | Không giả DONE |
| **006-010** | Gắn link và phiên nguồn đầu vào được phép đọc | Có dữ liệu nguồn truy được | CAT-206* · Master hợp đồng đầu vào/đầu ra | MCP workspace_read/stat (có quyền) | Trống | ☐ | Không chép hai nơi |
| **006-011** | Khai người nhận cuối, nơi gọi và nơi trả | Đúng đích bàn giao | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | ☐ | Caller có thể khác recipient |
| **006-012** | Khai người làm, người kiểm, người duyệt | Vai trò/quyền có căn cứ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | ☐ | Không giả quorum |
| **006-013** | Tra sổ sai thiếu và người nhận issue | Có địa chỉ vấn đề | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | — | Trống | ☐ | Dùng sổ hiện có |
| **006-014** | Khởi tạo tiến độ 7 mốc của 005 đúng hồ sơ | CP01 hiển thị, chưa tự PASS | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-001 · Kiểm mô hình | Trống | ☐ | Không chép trạng thái vào quy trình |

</details>

<details>
<summary><b>CP02 — Chuẩn bị đủ, 26 bước</b> · bấm mở/thu</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (mã + tên Master List) | Tool use (nếu có) | Tình trạng | Việc bổ sung | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **006-015** | Nạp câu hỏi bắt buộc theo MOW/MOT/phạm vi | Đủ bộ câu liên quan | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | Trống | ☐ | 50 câu chỉ là MOW001 |
| **006-016** | Ghi đáp án, mã câu, người và nguồn | Có đáp án hoặc ghi thiếu | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | ☐ | Không bịa dữ liệu |
| **006-017** | Ghim nguồn và hash bằng chứng đầu vào | Đọc lại đúng phiên | CAT-239* · Master tệp/bằng chứng | MCP workspace_read/stat (có quyền) | Trống | ☐ | Giữ một nguồn gốc |
| **006-018** | Lập issue cho câu hoặc dữ kiện chưa có | Có thiếu gì/ai sửa/quay đâu | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | — | Trống | ☐ | Đánh Vướng |
| **006-019** | Kiểm quyền đọc dữ liệu từ nguồn thật | Có bằng chứng quyền | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không tin PASS tự khai |
| **006-020** | Tra Master đích cho mỗi loại thông tin | Có mã + tên sổ hoặc issue | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-005 · Kiểm Master | Trống | ☐ | Hai cùng loại tra Master chung |
| **006-021** | Khai hợp đồng CAT-206* đúng việc/phiên | Có ID và phiên hợp đồng | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không tạo hợp đồng thứ hai |
| **006-022** | Ghi ý nghĩa nghiệp vụ từng trường | Đủ nghĩa, không đoán tên | CAT-206* · Master hợp đồng đầu vào/đầu ra | — | Trống | ☐ | Tên nhóm không là khóa |
| **006-023** | Định kiểu và đơn vị dữ liệu từng trường | Kiểu được schema kiểm | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không dùng kiểu tùy ý |
| **006-024** | Định required_when và nullable | Thiếu bắt buộc bị phát hiện | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không đếm cứng số dòng |
| **006-025** | Định cardinality và xử lý rỗng | Có quy tắc kiểm số lượng | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Rỗng khác lỗi nguồn |
| **006-026** | Chỉ Master/cột/đường dẫn nguồn và phiên | Đường nguồn có thật | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Chữ URL chưa đủ |
| **006-027** | Chỉ Master/cột đích và phép ánh xạ | Đường đích phân giải được | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không tự tách/gộp |
| **006-028** | Ghim phiên MOW/MOT/quy trình/luật | Đổi phiên buộc rà lại | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Giữ bản cũ |
| **006-029** | Liệt kê trường bắt buộc của gói đầu ra | Bên giao kiểm được payload | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không chỉ kiểm dấu MATCHED |
| **006-030** | Liệt kê trường phải nhận và người nhận | Bên nhận đủ đầu vào | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm giao–nhận | Trống | ☐ | Không rơi trường |
| **006-031** | Khai nhánh lỗi/thiếu/hủy/không quyền | Có điều kiện và đường xử lý | CAT-206* · Master hợp đồng đầu vào/đầu ra | TOOL-CTCM-003 · Phủ nhánh (nếu dùng được) | Trống | ☐ | Chỉ kích hoạt khi phát sinh |
| **006-032** | Định nghĩa tiêu chí nghiệm thu từng đầu ra | Có ca, expected và luật | CAT-012 · Danh mục bộ kiểm/ca thử | TOOL-CTCM-005 · Rà dữ liệu/lỗi (nếu dùng được) | Trống | ☐ | Theo phạm vi |
| **006-033** | Khai ca âm: thiếu trường/sai kiểu/sai phiên | Ca âm phải chặn đúng | CAT-012 · Danh mục bộ kiểm/ca thử | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | FAIL đúng là đạt test |
| **006-034** | Đối chiếu các giao điểm giữa MOT | Không còn cạnh phải đoán | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-002 · Kiểm mã | Trống | ☐ | Theo tập MOT áp dụng |
| **006-035** | Liệt kê tất cả thông tin/bằng chứng phải ghi | Không mất nghĩa vụ bắt buộc | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Nhánh không tới hạn thì không ép |
| **006-036** | Phân biệt sổ thiếu, chưa ghi, chưa có quyền | Có issue với từng thiếu sót | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | TQT-CHECK-005 · Kiểm Master | Trống | ☐ | Không tạo Master trùng |
| **006-037** | Lập các việc con P01…Pn có quan hệ thứ tự | Không vòng phụ thuộc | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-001 · Kiểm mô hình | Trống | ☐ | Không cố định P01–P05 |
| **006-038** | Giao actor/reviewer/recipient cho từng việc con | Mọi việc tới hạn có người | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | ☐ | Chưa phân công là Vướng |
| **006-039** | Khai sản phẩm thật, đích và cách kiểm từng việc | Biết rõ bên sau phải nhận gì | CAT-228* · Sổ việc thật MOT/kết quả | TOOL-CTCM-001 · Lập hành trình (nếu dùng được) | Trống | ☐ | Plan.output chưa là kết quả |
| **006-040** | Chạy kiểm chuẩn bị của checkpoint 2 | Đạt CP02 hoặc ghi Vướng rõ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | Trống | ☐ | Không PASS vì ô có chữ |

</details>

<details>
<summary><b>CP03 — Xác nhận bắt đầu, 12 bước</b> · bấm mở/thu</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (mã + tên Master List) | Tool use (nếu có) | Tình trạng | Việc bổ sung | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **006-041** | Tra công cụ theo việc cần làm trong Master DOT/Tool | Có mã và trạng thái công cụ | ML-DEF-024 · Master DOT | TQT-CHECK-006 · Chạy tổng | Trống | ☐ | Tra cả ML-DEF-023 |
| **006-042** | Kiểm hash/phiên/ca/giới hạn và quyền tool | Không dùng tool sai phiên | CAT-229* · Master lượt làm/thử | TQT-CHECK-006 · Chạy tổng | Trống | ☐ | Mẫu chưa là runtime |
| **006-043** | Xác thực người làm qua quyền ngoài hồ sơ | Có quyền thực, không tự khai | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Phân vai đúng người |
| **006-044** | Giao người kiểm độc lập khi cần | Có reviewer được giao | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | ☐ | Không tự tạo quorum hãng khác |
| **006-045** | Rà xác nhận kế hoạch đúng bản/phiên | Kế hoạch đủ quyền/đầu ra | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | Trống | ☐ | Không dùng plan cũ |
| **006-046** | Rà độc lập trường/nguồn/đích hợp đồng | Có kết luận đúng contract phiên | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Sửa hợp đồng rà lại |
| **006-047** | Kiểm schema/khóa/đường nơi lưu vật lý | Địa chỉ ghi có thật | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | UI mock không là kho |
| **006-048** | Thử ghi rồi đọc lại bằng quyền cho phép | Có biên nhận readback | CAT-229* · Master lượt làm/thử | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | TEST không tăng mốc thật |
| **006-049** | Bên nhận mở gói chuẩn bị P01/tương đương | Đọc được đúng dữ liệu/phiên | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 --read-preparation | Trống | ☐ | Không dựng lại qua chat |
| **006-050** | Giải quyết issue đang chặn bắt đầu | Không còn blocker CP03 | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | TQT-CHECK-003 · Kiểm khai | Trống | ☐ | Không xóa issue cũ |
| **006-051** | Ghi xác nhận bắt đầu đúng người và phiên | Có quyết định và căn cứ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không tự chuyển CONFIRMED |
| **006-052** | Tính lại CP01–03 trước khi vào làm | CP03 đạt bằng chứng | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Chưa đạt thì dừng |

</details>

<details>
<summary><b>CP04 — Làm theo quy trình, 24 bước</b> · bấm mở/thu</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (mã + tên Master List) | Tool use (nếu có) | Tình trạng | Việc bổ sung | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **006-053** | Chọn việc con có đủ các phụ thuộc trước | Biết đúng việc đến lượt | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-001 · Kiểm mô hình | Trống | ☐ | Song song cần có căn cứ |
| **006-054** | Mở gói đầu vào từ sổ theo ID/phiên/hash | Có dữ liệu thật | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không dùng tóm tắt chat |
| **006-055** | Kiểm hợp đồng nhận về kiểu/nghĩa/số lượng | Thiếu/sai bị chặn | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm giao–nhận | Trống | ☐ | Không điền null bừa |
| **006-056** | Chọn DOT/Tool đúng phiên hoặc làm tay đúng quy trình | Có cách thực hiện hợp lệ | CAT-229* · Master lượt làm/thử | TQT-CHECK-006 · Chạy tổng | Trống | ☐ | Không tự gọi tool mock |
| **006-057** | Thực hiện gói chuẩn bị P01 nếu còn cần | Có đầu ra chuẩn bị thật | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 --read-preparation | Trống | ☐ | Dùng lại khi có sẵn |
| **006-058** | Để bước sau tự đọc gói chuẩn bị đã ghi | Bên nhận dùng được nội dung | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm giao–nhận | Trống | ☐ | Không diễn lại trong chat |
| **006-059** | Tạo sản phẩm của việc con đúng hợp đồng | Có sản phẩm thật được lưu | CAT-228* · Sổ việc thật MOT/kết quả | TOOL-CTCM-001 · Lập hành trình (nếu dùng được) | Trống | ☐ | G1 không phải G2 |
| **006-060** | Gắn application/plan/target/contract vào sản phẩm | Danh tính/phiên khớp | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không trộn việc |
| **006-061** | Ghi kết quả qua cửa máy chủ được phép | Có biên nhận ghi hợp lệ | CAT-228* · Sổ việc thật MOT/kết quả | MCP workspace_transaction (có quyền) | Trống | ☐ | Không bỏ cửa ghi |
| **006-062** | Đọc lại đúng bản vừa ghi và so hash | Nội dung bằng bản gửi | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | HTTP200 không là readback |
| **006-063** | Kiểm schema đầu ra bên giao bằng payload thật | Không mất trường bắt buộc | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không tin MATCHED suông |
| **006-064** | Kiểm schema đầu vào bên nhận theo hợp đồng | Bên nhận đủ dữ liệu dùng | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm giao–nhận | Trống | ☐ | Gồm cả chặng cuối |
| **006-065** | Gửi lệnh với idempotency key đúng phiên | Retry không nhân tác động | CAT-238* · Sổ lệnh gửi–nhận–trả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | TEST khác runtime thật |
| **006-066** | Lấy ACK người nhận đúng gói bước con | Có biên nhận đúng hash | CAT-238* · Sổ lệnh gửi–nhận–trả | — | Trống | ☐ | Khác ACK Owner cuối |
| **006-067** | Nếu gửi trùng, chặn nhân tác động | Giữ một kết quả hợp lệ | CAT-238* · Sổ lệnh gửi–nhận–trả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Chỉ khi phát sinh |
| **006-068** | Nếu phản hồi cũ, so phiên và từ chối | Không dùng green cũ | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Chỉ khi phát sinh |
| **006-069** | Nếu mất quyền, dừng và ghi sự cố | Có người xử lý vấn đề quyền | CAT-017 · Sổ sự cố vận hành | — | Trống | ☐ | Không đi đường tắt |
| **006-070** | Nếu thiếu Master đích, tra lại và ghi issue | Biết sổ/người/bước sửa | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | TQT-CHECK-005 · Kiểm Master | Trống | ☐ | Không lập sổ trùng |
| **006-071** | Nếu dữ liệu sai, gọi QTTH002 giải quyết | Có kết quả sửa được kiểm lại | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | MOW-TH-002 · Xử lý thiếu/sai | Trống | ☐ | Giữ mốc không bị ảnh hưởng |
| **006-072** | Nếu sửa quy trình/hợp đồng, theo QTTH003 | Tăng phiên và giữ lịch sử | CAT-016 · Sổ nhật ký thay đổi định nghĩa | MOW-TH-003 · Hiệu chỉnh | Trống | ☐ | Không sửa âm thầm |
| **006-073** | Nếu hủy, ghi lý do/phiên/nơi nhận/việc bù | Có bản ghi hủy khi phát sinh | CAT-244* · Sổ hủy và việc bù | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không giả hủy |
| **006-074** | Ghi receipt, revision và sự kiện đầy đủ | Lịch sử còn và đọc lại được | CAT-233* · Sổ sự kiện bản ghi/chống trùng | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Lỗi sự kiện phải ghi bù |
| **006-075** | Chỉ đóng việc con khi có output_ref thật | Có sản phẩm/bằng chứng đúng | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Plan không phải kết quả |
| **006-076** | Chốt CP04 sau khi kiểm đầu ra tới hạn | Mốc làm đạt hoặc báo Vướng | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không tích tay |

</details>

<details>
<summary><b>CP05 — Kiểm đầu ra, 13 bước</b> · bấm mở/thu</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (mã + tên Master List) | Tool use (nếu có) | Tình trạng | Việc bổ sung | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **006-077** | Đọc bộ tiêu chí G1/G2 đúng phạm vi và phiên | Đủ ca kiểm áp dụng | CAT-012 · Danh mục bộ kiểm/ca thử | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | 11 ca chỉ riêng MOW001 G1 |
| **006-078** | Tạo ca input hợp lệ với expected rõ | Có ca đúng đo được | CAT-012 · Danh mục bộ kiểm/ca thử | TOOL-CTCM-007 · Kiểm UI (nếu dùng được) | Trống | ☐ | TEST không tăng tiến độ |
| **006-079** | Tạo ca thiếu/sai kiểu/rỗng/không quyền | Có ca âm chặn đúng | CAT-012 · Danh mục bộ kiểm/ca thử | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | FAIL đúng vẫn là kết quả kiểm |
| **006-080** | Tạo ca stale, sai người nhận và sai phiên | Sai phiên/đích không lọt | CAT-012 · Danh mục bộ kiểm/ca thử | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Khi giao điểm áp dụng |
| **006-081** | Reviewer đọc sản phẩm thật đúng hash/phiên | Có biên nhận đọc độc lập | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 --read-designs | Trống | ☐ | Không lấy ảnh cũ |
| **006-082** | Chạy bộ kiểm hợp đồng và lưu biên nhận | Có kết quả PASS/FAIL có nguồn | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không tự báo xanh |
| **006-083** | Nếu là UI, thử nút/trạng thái/nhánh thật | Có bằng chứng UI đúng phiên | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 --check-g1-ui (nếu phù hợp) | Trống | ☐ | G1 không là backend G2 |
| **006-084** | Kiểm nội dung bản thiết kế từng MOT | Đủ trường/nút/nhánh/luật/hash | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 --read-designs | Trống | ☐ | Link rỗng bị chặn |
| **006-085** | Kiểm kết quả trả cuối đúng caller/phiên/kiểu | Không trả sai nơi nhận | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Chặng cuối vẫn cần kiểm |
| **006-086** | Nếu G2/G3, kiểm nguồn/evaluator/permission live | Không nhầm demo thành live | CAT-015 · Sổ kết quả kiểm | TOOL-CTCM-005 · Rà dữ liệu/lỗi (nếu dùng được) | Trống | ☐ | Chỉ khi trong phạm vi |
| **006-087** | Ghi actual/expected/reviewer/evidence cho từng ca | Có kết quả thật trong sổ | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | CAT012 ca, CAT015 kết quả |
| **006-088** | Nếu ca FAIL, ghi issue/người sửa/bước quay | Lỗi có cách khắc phục | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | MOW-TH-002 · Xử lý thiếu/sai | Trống | ☐ | Chỉ khi phát sinh |
| **006-089** | Chốt CP05 khi đủ ca và đúng phiên | CP05 đạt hoặc Vướng rõ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | Trống | ☐ | Kỹ thuật không thay Owner |

</details>

<details>
<summary><b>CP06 — Duyệt kết quả, 5 bước</b> · bấm mở/thu</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (mã + tên Master List) | Tool use (nếu có) | Tình trạng | Việc bổ sung | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **006-090** | Gom sản phẩm, phạm vi và kết quả kiểm trình duyệt | Người duyệt mở đúng bản | CAT-025 · Sổ phiếu duyệt/quyết định | TQT-CHECK-005 · Kiểm Master | Trống | ☐ | Không trộn G1/G2/PG |
| **006-091** | Xác thực người duyệt/thẩm quyền theo phạm vi | Không dùng worker tự ký | CAT-025 · Sổ phiếu duyệt/quyết định | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Reviewer khác approver |
| **006-092** | Xin quyết định đồng ý/từ chối/sửa đúng sản phẩm | Có quyết định rõ ràng | CAT-025 · Sổ phiếu duyệt/quyết định | — | Trống | ☐ | Tiếp tục không là duyệt |
| **006-093** | Ghi quyết định kèm product_binding và phiên | Có phiếu duyệt đọc lại được | CAT-025 · Sổ phiếu duyệt/quyết định | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không giả APPROVED |
| **006-094** | Chốt CP06 sau khi so quyết định với sản phẩm | CP06 đạt hoặc quay xử lý | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Kỹ thuật không là Owner |

</details>

<details>
<summary><b>CP07 — Bàn giao · kết thúc, 6 bước</b> · bấm mở/thu</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (mã + tên Master List) | Tool use (nếu có) | Tình trạng | Việc bổ sung | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **006-095** | Hoàn tất đầu ra P05 hoặc việc con cuối | Có kết quả cuối đúng kế hoạch | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không ghi giả nhánh |
| **006-096** | Kiểm hợp đồng nhận cuối và nơi trả | Đúng người/sản phẩm/phiên | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm giao–nhận | Trống | ☐ | Duyệt chưa là ACK |
| **006-097** | Ghi giao đúng bản, người và nguồn sản phẩm | Có sổ bàn giao thật | CAT-232* · Sổ bàn giao/xác nhận nhận | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không chỉ gửi link |
| **006-098** | Lấy ACK thật từ bên nhận có thẩm quyền | Có biên nhận đúng bản | CAT-232* · Sổ bàn giao/xác nhận nhận | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Iframe không là Owner ACK |
| **006-099** | Kiểm liên tục CP01–07 và nghĩa vụ áp dụng | 7/7 với bằng chứng thật | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | ☐ | Không ép nhánh chưa có |
| **006-100** | Chạy CHECK005/006 và lưu bài học/tool đã dùng | Có biên nhận để tái sử dụng | CAT-233* · Sổ sự kiện bản ghi/chống trùng | TQT-CHECK-006 · Chạy tổng | Trống | ☐ | G2/PG chưa làm vẫn OPEN |

</details>

## 3. Mẫu việc bổ sung (không tính trong số bước cố định)

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (mã + tên Master List) | Tool use (nếu có) | Tình trạng | Việc bổ sung | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **006-023-B01** | Khi thiếu một nguồn đặc thù, tạo yêu cầu xử lý, rồi kiểm nguồn đúng phiên. | Có nguồn hợp lệ hoặc issue có người/điểm quay lại. | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | TQT-CHECK-005 · Kiểm Master | Trống | ☑ | Chèn ngay sau 006-023 trong hồ sơ phát sinh; không thêm vào định nghĩa chung. |

## 4. Yêu cầu triển khai tiếp trên DEF 00.1

1. Giữ bảy checkpoint và 11 nhóm sổ của QTTH 05 làm **bảng tổng hợp**. Trong **Chi tiết của hồ sơ từng việc**, đặt ngay **bên dưới** một khối `<details>` **đóng mặc định**: “QTTH 006 · Quy trình thực hiện QTTH 05 — 100 bước”. Mở ra có 7 nhóm con **đóng mặc định**, bảng ngang có thể cuộn trên mobile.
2. 8 cột theo đúng thứ tự của Owner; mã bước 006-001…006-100. Bước bổ sung có `parent_step_id`, `is_supplemental`, thuộc application riêng và giữ dấu ☑. Không cài trạng thái giả ở bảng định nghĩa.
3. MOW001 7/7 đã nghiệm thu G1 theo 005 nhưng bước 006 chưa có dấu vết riêng: hiển thị **Trống**, ghi rõ “chưa theo dõi hồi tố”; không phá hồ sơ P37. Dòng Vướng trỏ đúng CAT-069? và người xử lý; nhánh chưa phát sinh không báo lỗi.
4. Dùng chính Master và DOT hiện hữu, không thêm sổ hoặc PG mới. Kiểm hoạt động ca thiếu sổ, sai phiên, khác hồ sơ, việc bổ sung, nhánh điều kiện và AI mới đọc tiếp không hỏi người cũ.
5. Chưa nghiệm thu QTTH 006 cho đến khi Host so lại code/name từng Master/Tool, đăng ký một mã `MOW-TH-006` trong Master quy trình tổng hợp, gắn UI và có ca AI mới đi theo quy trình tạo sản phẩm thực đúng.

**Vai:** GPT ghi quy trình theo chỉ đạo Owner; Codex Host nội dung tiếp nhận; Claude Host Kiểm soát giữ §0. Không tự phát RUN và không duyệt thay Owner.
