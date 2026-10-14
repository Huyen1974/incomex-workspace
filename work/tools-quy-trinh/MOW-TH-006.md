# QTTH 006 — Quy trình thực hiện QTTH 05

**Mã quy trình:** `MOW-TH-006` · **Tên:** Quy trình thực hiện QTTH 05. Đây là **một quy trình**, không phải loại đối tượng “hướng dẫn” riêng.
**Phiên:** `0.9-manual-applicability` · **Ngày rà:** 14/10/2026 · **Trạng thái:** ĐÃ RÀ THEO QTTH 05 / HỒ SƠ MOW001 G1, **HOST ĐÃ RÀ THỨ TỰ / CHƯA NGHIỆM THU AI MỚI THỰC HIỆN**. Đăng ký thiết kế MOW-TH-006 trong Master quy trình tổng hợp; chưa tuyên bố đã chạy trọn việc thật theo 006.
**Nguồn:** tệp này là quy định chuẩn do Host quản lý, hiển thị tại Overview. Bản v0.1 có **100 bước** được lưu trong lịch sử Git; PR20 giữ bảng đối chiếu đầy đủ 100 mã cũ. Không đổi tiến độ MOW001/P37/P38.

## 1. Nguyên tắc chính

**QTTH 05** quy định bảy checkpoint; **QTTH 06** triển khai thao tác chi tiết để hoàn thành checkpoint đó. Không ép một số lượng bước. Bản này có **71 bước**, kết quả của rà gộp/tránh trùng, chuyển thứ tự và bổ sung chỗ thiếu; sửa đúng nội dung thì số bước được thay theo phiên.

Một **bước nguyên tử** phải có: một hành động có thể giao một bên thực hiện, một đầu ra/biên nhận có thể kiểm, một nơi ghi và điều kiện đạt/rẽ nhánh. Bước lặp trên nhiều MOT/field/plan/case vẫn là **một định nghĩa**, khi thực hiện sinh bản áp dụng theo `item_key`. Bước có quyền hoặc bên nhận khác phải tách riêng. Không hiểu “độc lập” là bỏ quan hệ trước–sau: `step_id`, `depends_on` và `return_to` vẫn bắt buộc khi có phụ thuộc.

### Hai tầng, một hồ sơ

- **Tầng định nghĩa**: danh sách bước QTTH 006 theo phiên; **không chứa kết quả của MOW001 hoặc việc khác**. `MOW-TH-005` tiếp tục là 7 mốc và 6 MOT nguồn, 006 không tự gọi 006 thành vòng lặp hay chen vào `selected_process` của 005.
- **Tầng áp dụng**: hồ sơ việc trên `DEF 00.1 / CAT-227*` ghim đúng `MOW-TH-006@process_version`; hiển thị toàn bộ bước áp dụng (cùng nhóm theo CP của 005), chỉ lưu **trạng thái, bằng chứng, ngoại lệ và thay đổi** theo `application_id + process_version + target_version + step_id + item_key + revision` ở **sổ hiện có**. Không sao chép một danh sách có thể sửa độc lập, không tạo Master “tiến độ QTTH 006” thứ hai.
- **Tình trạng ghi nhận**: để trống khi chưa ghi; DONE/NOT_DONE/BLOCKED theo §6. Ghi nhận đã làm không là nghiệm thu mốc; nghiệm thu cần bằng chứng đúng nguồn, quyền, phiên và đối chiếu.

### Bước bổ sung và trường hợp không thực hiện

Hồ sơ không có cột “Điều chỉnh +/−”. Giữ nguyên mã CP của bước chuẩn. Bước riêng dùng mã **BS-001, BS-002…** duy nhất trong hồ sơ; ghi `added_steps[] = {id, after_step, action, reason, completion}` trong binding hiện hữu, neo sau một CP chuẩn. Không tự cấp mã CP mới. Khi bước bổ sung cần đổi quyền, phạm vi hoặc nghĩa vụ lõi, phải có quyết định hợp lệ trước khi thực hiện.

Ô tình trạng thực tế để trống khi chưa có ghi nhận. `DONE` = Đã làm (việc thực hiện + kết quả/bằng chứng); `BLOCKED` = Bị chặn (lý do, issue, người xử lý, bước quay lại); `NOT_DONE` = Không làm (điều kiện hoặc quyết định và lý do). Không làm không tự được tính hoàn thành, không dùng để bỏ đầu vào, quyền, kiểm, duyệt hay ACK bắt buộc. Hướng dẫn sử dụng đặt trong dấu **?** ngay tại cột/bước; không điền lời hướng dẫn vào ô thực tế.

### Sổ/Tool và khi bị lỗi

Cột “Nơi ghi kết quả” chỉ **Master ghi bằng chứng hoặc kết quả của thao tác**, không phải chỉ nguồn tra cứu. Ví dụ: *tra MOW* là đọc `ML-DEF-004/005`, nhưng **ghi lựa chọn MOW/MOT vào hồ sơ DEF 00.1**; không tự sửa Master MOW khi chỉ tra.

Cần luôn chỉ **mã và tên Master** thực, kể cả sổ thiếu/sai (`CAT-069?` hiện là mã thiết kế có dấu ?, Host phải xác minh alias/đường ghi trước khi đưa vào dùng rộng). Tool có mã trong Master DOT/Tool nhưng **chưa đủ quyền hoặc chỉ là thiết kế** không coi đã chạy. Tham chiếu quy trình xử lý sai `MOW-TH-002` hoặc hiệu chỉnh `MOW-TH-003` thuộc quy trình, **không phải Tool**. Khi lỗi: ghi `issue_ref, owner, next_action, return_to`, không xóa checkpoint cũ không bị ảnh hưởng.

### Khớp với MOW001 đã thực hiện

MOW001 G1 đã 7/7 theo QTTH05 ở P37; P38 đã giảm trùng lịch sử mà giữ bằng chứng. **P01 chuẩn bị phải tạo trước khi CP03 nhận/kiểm**, không được sinh đầu tiên ở CP04. P02/P03 là sản phẩm lúc Làm, P04 là kiểm, P05 kết thúc duyệt và bàn giao. Hồ sơ MOW001 **chưa chạy QTTH 006 phiên 0.3**, không đánh 87/87 theo suy đoán. Tình trạng G2/G3/PG vẫn giữ riêng. QTTH 06 dùng được cho loại việc khác MOW; trường G1/G2/G3 và các ca UI chỉ áp dụng khi đúng loại việc.


### Lịch sử rà thứ tự P40 — mã hiện hành xem §2/§10

- Bổ sung CP02.23 (quyền trước lần ghi) và CP07.08 (KQ/nhả busy). Chuyển CP07.05@0.2 sang CP05.10@0.3 (fullsuite trước duyệt); không tái dùng mã cũ với nghĩa mới. Các mã còn lại giữ nghĩa và được làm rõ. 85 → 87 không là chỉ tiêu cố định.
- CP01.05 chọn phiên; CP01.11 khởi tạo binding trong cùng hồ sơ. CP03.06/07 kiểm độ mới của đích/quyền đã đo trước chuẩn bị, không bắt thử lại máy móc. CP03.10 ghi quyết định tại CAT025; CP05.01/CP07.02 ghi kết quả kiểm tại CAT015, không sửa sổ định nghĩa khi chỉ kiểm.
- MOW001: P01 chuẩn bị trước CP03; P02/P03 thực hiện ở CP04; P04 kiểm ở CP05; P05 bàn giao ở CP07. Mỗi vòng tạo → kiểm trước ghi → ghi → đọc lại → bên nhận kiểm được áp cho việc con tới hạn; không đòi P04/P05 xong ngay CP04. CP07.01 tạo gói, chỉ đóng P05 sau CP07.04 nhận thật.
- Các nhánh lỗi CP04.10–16 và CP05.08 có thể phát sinh ngay tại bước liên quan, không đợi đi đến dòng trong bảng. Giữ output cũ, ghi issue/owner/return_to, sửa rồi kiểm lại đúng phụ thuộc. Khóa chống trùng lập trước tác động; không cấp sau khi tác động đã xảy ra.
- Bằng chứng quyền trước lần ghi đầu áp cả khai việc; chưa có quyền thì chỉ chuẩn bị nháp ngoài kho, ghi blocker tại kênh đã được phép. Không làm vòng “phải ghi vào sổ mất quyền để chứng minh mất quyền”.
- Mốc tổng quát 005 và lượt chi tiết 006 có tiến độ riêng. G1 7/7 đã nhận không mở lại; 006 ghim mới chỉ dùng để đối chiếu, không hồi tố. Con số 85% ổn định là định hướng dùng lại, chưa phải tỷ lệ đã đo.

## 2. Bảng bước 71 thao tác, mở/thu theo 7 mốc QTTH 05

Mỗi dòng gộp giữ đủ các nghĩa vụ; bằng chứng chi tiết theo item. Bản đồ mã cũ ở §10. Không sửa hồ sơ cũ thành đã làm theo bản mới.

<details>
<summary><strong>CP01 · Khai việc · 8 bước</strong></summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả | Tool gợi ý | Điều kiện / ghi chú |
|---|---|---|---|---|---|
| **1 · CP01.01** | Đọc nguyên yêu cầu Owner và điều không được làm | Có mục tiêu/người giao/nguồn rõ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | LUÔN · Không tự thay ý Owner |
| **2 · CP01.02** | Xác nhận A0, quyền Owner và phạm vi trước khi mở hồ sơ | Đủ từng nghĩa vụ: CP01.02: Có phạm vi được xác nhận; CP01.07: Có một phạm vi được xác nhận gồm sản phẩm, các nhánh ngoài phạm vi và điều kiện mở lại | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | LUÔN · Kiểm từng nghĩa vụ áp dụng, không lấy thành công một phần làm hoàn thành cả nhóm. |
| **3 · CP01.04** | Tra trùng rồi mở hồ sơ, ghim phiên và khởi tạo chỗ ghi | Đủ từng nghĩa vụ: CP01.03: Không tạo hồ sơ trùng; CP01.04: Hồ sơ mở được đúng ID; CP01.05: Hồ sơ trỏ 005@version và 006@version; không có vòng gọi 006; CP01.11: Có liên kết hồ sơ + phiên định nghĩa bất biến và sổ sự kiện bước; trạng thái ban đầu Trống | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-005 · Kiểm Master; —; TQT-CHECK-002 · Kiểm mã; TQT-CHECK-001 · Kiểm mô hình | LUÔN · Kiểm từng nghĩa vụ áp dụng, không lấy thành công một phần làm hoàn thành cả nhóm. |
| **4 · CP01.06** | Đối chiếu đối tượng công việc và các đối tượng con theo nguồn chuẩn | Đúng mã/phiên/quan hệ con; với MOW tra đúng MOW/MOT, loại khác tra Master đối tượng tương ứng | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-005 · Kiểm Master | LUÔN · Nguồn tra cứu: ML-DEF-004 Master MOW / ML-DEF-005 Master MOT chỉ khi việc thuộc MOW; hồ sơ phải ghi đúng mã+tên Master loại khác. |
| **5 · CP01.08** | Ghi nguồn đầu vào một lần để CP02 dùng lại | Có dữ liệu nguồn truy được | DEF 00.1 · Master tiến trình công việc (CAT-227*) | MCP workspace_read/stat (có quyền) | LUÔN · Giữ nguồn ở CP01; CP02.03 kiểm phiên/hash của cùng tham chiếu. |
| **6 · CP01.09** | Khai người nhận cuối, nơi gọi và nơi trả | Đúng đích bàn giao | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | LUÔN · Caller có thể khác recipient |
| **7 · CP01.10** | Khai người làm, người kiểm, người duyệt | Vai trò/quyền có căn cứ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | LUÔN · Không giả quorum |
| **8 · CP01.12** | Đối chiếu kết quả khai việc với CP01 của QTTH 05 | Mốc CP01 được kiểm từ hồ sơ nguồn hoặc có Vướng/owner/return_to | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm bản ghi/mốc | LUÔN · Bước này kiểm gate, không tự đánh dấu bằng nút giao diện |

</details>

<details>
<summary><strong>CP02 · Chuẩn bị đủ · 18 bước</strong></summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả | Tool gợi ý | Điều kiện / ghi chú |
|---|---|---|---|---|---|
| **9 · CP02.01** | Nạp câu hỏi bắt buộc theo MOW/MOT/phạm vi | Đủ bộ câu liên quan | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | KHI(quy trình có bộ câu hỏi) · Bộ câu hỏi của MOW001 không phải yêu cầu mặc định cho mọi việc. |
| **10 · CP02.02** | Ghi đáp án, mã câu, người và nguồn | Có đáp án hoặc ghi thiếu | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | KHI(có câu hỏi áp dụng) · Lặp theo item_key=câu hỏi, không tạo một bước định nghĩa mới cho từng câu. |
| **11 · CP02.03** | Đọc lại và kiểm phiên/hash của nguồn đã ghi CP01.08 | Đọc lại đúng phiên | CAT-239* · Master tệp/bằng chứng | MCP workspace_read/stat (có quyền) | KHI(có nguồn cần kiểm) · Dùng lại tham chiếu CP01.08; không nhập lại nguồn. |
| **12 · CP02.04** | Kiểm quyền đọc dữ liệu từ nguồn thật | Có bằng chứng quyền | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Kiểm nguồn và quyền đọc trước dùng; biên nhận ghi vào CAT-015, không chỉnh hợp đồng khi đang kiểm. |
| **13 · CP02.06** | Lập hợp đồng CAT-206* và ghim MOW/MOT/quy trình/luật theo phiên | Có ID, contract_version, phụ thuộc và nguồn luật xác minh được | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Lập hợp đồng một lần theo scope; đổi nguồn tăng phiên và kiểm lại. |
| **14 · CP02.07** | Định nghĩa từng field và ánh xạ nguồn–đích | Đủ từng nghĩa vụ: CP02.07: Mỗi field có schema đủ nghĩa/type/unit/nullable/cardinality/miền giá trị; ca sai bị chặn; CP02.08: Có nguồn–đích thực, đúng loại/phiên và phép biến đổi rõ | CAT-206* · Master hợp đồng đầu vào/đầu ra | —; TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Kiểm từng nghĩa vụ áp dụng, không lấy thành công một phần làm hoàn thành cả nhóm. |
| **15 · CP02.10** | Lập hợp đồng giao–nhận, đầu ra và nhánh lỗi | Đủ từng nghĩa vụ: CP02.09: Bên giao kiểm được payload; CP02.10: Bên nhận đủ đầu vào; CP02.11: Có điều kiện và đường xử lý | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc; TQT-CHECK-004 · Kiểm giao–nhận; TOOL-CTCM-003 · Phủ nhánh (nếu dùng được) | LUÔN · Kiểm từng nghĩa vụ áp dụng, không lấy thành công một phần làm hoàn thành cả nhóm. |
| **16 · CP02.12** | Lập một bộ ca nghiệm thu gồm ca đúng, sai, rỗng, sai phiên, sai người nhận | CAT-012 có ca bắt buộc và expected theo contract/phiên đã chốt | CAT-012 · Danh mục bộ kiểm/ca thử | TOOL-CTCM-005 · Rà dữ liệu/lỗi (nếu dùng được) | LUÔN · Chỉ lập bộ ca một lần; CP05 phải thực thi các ca này, không khai lại. |
| **17 · CP02.13** | Đối chiếu các giao điểm giữa MOT | Không còn cạnh phải đoán | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-002 · Kiểm mã | KHI(có nhiều bước giao nhận) · Đây là kết quả kiểm các cạnh từ CAT-206*, không sửa contract bằng dấu PASS. |
| **18 · CP02.14** | Lập bảng nghĩa vụ thông tin và Master đích | Đủ từng nghĩa vụ: CP02.05: Mỗi loại thông tin có mã+tên sổ, item_key hoặc issue nếu chưa xác minh; CP02.14: Không mất nghĩa vụ bắt buộc | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-005 · Kiểm Master; TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Kiểm từng nghĩa vụ áp dụng, không lấy thành công một phần làm hoàn thành cả nhóm. |
| **19 · CP02.15** | Phân biệt sổ thiếu, chưa ghi, chưa có quyền | Có issue với từng thiếu sót | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-005 · Kiểm Master | LUÔN · Thiếu sổ/thiếu bản ghi/thiếu quyền là ba trường hợp khác nhau; nếu lỗi mở CAT-069?. |
| **20 · CP02.16** | Xác định các bước QTTH 006 áp dụng cho hồ sơ và từng item_key | Ghim 006@version, phân loại lõi/điều kiện theo từng plan_id/MOT/field và biết bước đến hạn | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm hồ sơ | LUÔN · Bản định nghĩa chỉ lưu một lần; từng hồ sơ lưu phiếu áp dụng/ngoại lệ |
| **21 · CP02.17** | Rà bước thêm, không áp dụng hoặc thay thế trước khi xác nhận kế hoạch | Mọi +/−/↔ có lý do, người kiểm, điều kiện xong, Master đích; không bỏ bước lõi không có phép | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm nghĩa vụ | KHI(có nhánh điều kiện/điều chỉnh) · Bước không áp dụng không tự là Hoàn thành; bước thêm được tính là nghĩa vụ bắt buộc khi đã duyệt |
| **22 · CP02.18** | Lập kế hoạch việc con, đầu ra và nơi ghi | Đủ từng nghĩa vụ: CP02.18: Có P01…Pn hoặc tương đương, không vòng phụ thuộc; CP02.20: Mỗi plan_id có expected_output, Master mã+tên, product_key và tiêu chí đọc lại | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-001 · Kiểm mô hình; TOOL-CTCM-001 · Lập hành trình (nếu dùng được) | LUÔN · Kiểm từng nghĩa vụ áp dụng, không lấy thành công một phần làm hoàn thành cả nhóm. |
| **23 · CP02.19** | Giao actor/reviewer/recipient cho từng việc con | Mọi việc tới hạn có người | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | LUÔN · Chưa phân công là Vướng |
| **24 · CP02.23** | Kiểm cửa ghi và quyền ghi–đọc trước lần ghi chuẩn bị đầu tiên | Có đích/schema/khóa thật và biên nhận quyền đúng scope; thiếu quyền thì dừng ghi | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm quyền kho tệp; MCP theo quyền hiện có | LUÔN · Với lần ghi khai việc sớm hơn cũng áp cổng này trước ghi. Chỉ TEST quyền tại đích thử được phép; không tự tạo quyền hay lấy TEST thay P01. |
| **25 · CP02.21** | Tạo và ghi gói chuẩn bị P01 hoặc đầu ra chuẩn bị tương đương | Có sản phẩm chuẩn bị thật, đúng contract và nguồn; đọc lại trước CP03 | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 --read-preparation | KHI(quy trình có bước chuẩn bị P01/tương đương) · BƯỚC ĐƯỢC CHUYỂN TỪ CP04 VỀ CP02; tạo trước khi kiểm CP03. Chỉ ghi sau CP02.23; gói nháp có thể soạn trước, chưa coi đã ghi. |
| **26 · CP02.22** | Chạy kiểm chuẩn bị của checkpoint 2 | Đạt CP02 hoặc ghi Vướng rõ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | LUÔN · Không PASS vì ô có chữ |

</details>

<details>
<summary><strong>CP03 · Xác nhận bắt đầu · 11 bước</strong></summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả | Tool gợi ý | Điều kiện / ghi chú |
|---|---|---|---|---|---|
| **27 · CP03.12** | Tiếp tục sau DỪNG tại đúng mốc đang dừng | Đọc KQ cũ, kiểm phiên/quyền/biên nhận và phạm vi thay đổi; chỉ tiếp phần còn thiếu, không lặp tác động đã ghi | DEF 00.1 + CAT-229* + CAT-015 | CHECK004/005 + gateway hiện hữu | KHI(tiếp tục sau DỪNG) · Áp tại mọi mốc; không chờ tới CP03 mới kiểm; không hồi sinh RUN cũ. |
| **28 · CP03.01** | Tra và kiểm tính sẵn sàng của Tool/DOT sẽ dùng | Mỗi tool có ID/phiên/hash, nguồn, quyền và ca gần nhất, hoặc phương án làm tay | CAT-229* · Sổ lượt thực hiện/thử | TQT-CHECK-006 · Chạy tổng | KHI(kế hoạch có Tool/DOT) · Tra nguồn ML-DEF-024 Master DOT, ML-DEF-023 Master Tool; không chạy chỉ vì có tên. |
| **29 · CP03.02** | Xác thực người làm qua quyền ngoài hồ sơ | Có quyền thực, không tự khai | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Phân vai đúng người |
| **30 · CP03.03** | Kiểm lại reviewer đã được phân công và quyền kiểm | Đúng người/phiên và mức độc lập theo quy định | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | KHI(cần người kiểm) · Không phân công reviewer mới trùng với bước phân vai ở CP01. |
| **31 · CP03.04** | Rà xác nhận kế hoạch đúng bản/phiên | Kế hoạch đủ quyền/đầu ra | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | LUÔN · Không dùng plan cũ |
| **32 · CP03.05** | Rà độc lập trường/nguồn/đích hợp đồng | Có kết luận đúng contract phiên | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | KHI(cần review độc lập theo quy tắc) · Đây là kết quả review hợp đồng, không phải sửa CAT-206*. |
| **33 · CP03.07** | Kiểm lại schema/đường ghi và hiệu lực biên nhận quyền | Đủ từng nghĩa vụ: CP03.06: Kết quả kiểm lại đúng phiên, không dùng địa chỉ/biên nhận cũ đã đổi; CP03.07: Biên nhận CP02.23 còn đúng actor/scope/nguồn; chỉ thử lại nếu điều kiện đã đổi | CAT-015 · Sổ kết quả kiểm; CAT-229* · Master lượt làm/thử | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Kiểm từng nghĩa vụ áp dụng, không lấy thành công một phần làm hoàn thành cả nhóm. |
| **34 · CP03.08** | Bên nhận độc lập đọc và đối chiếu kết quả chuẩn bị P01 hoặc tương đương | P01/tương đương đã được tạo trước CP03; đọc đúng schema/phiên/hash | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 --read-preparation | KHI(có gói chuẩn bị) · Gộp kiểm nhận lặp từ bước cũ 058; cấm tới CP03 nếu chưa tạo kết quả chuẩn bị. |
| **35 · CP03.09** | Giải quyết issue đang chặn bắt đầu | Không còn blocker CP03 | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | TQT-CHECK-003 · Kiểm khai | KHI(có issue chặn CP03) · Không có blocker thì đánh − Không áp dụng, không tạo issue giả. |
| **36 · CP03.10** | Ghi xác nhận bắt đầu đúng người và phiên | Có quyết định và căn cứ | CAT-025 · Sổ phiếu duyệt/quyết định | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Không tự chuyển CONFIRMED |
| **37 · CP03.11** | Tính lại CP01–03 trước khi vào làm | CP03 đạt bằng chứng | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Chưa đạt thì dừng |

</details>

<details>
<summary><strong>CP04 · Làm theo quy trình · 15 bước</strong></summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả | Tool gợi ý | Điều kiện / ghi chú |
|---|---|---|---|---|---|
| **38 · CP04.01** | Chọn việc con có đủ các phụ thuộc trước | Biết đúng việc đến lượt | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-001 · Kiểm mô hình | LUÔN · Chỉ việc con tới hạn CP04. MOW001: P01 ở CP02, P02/P03 ở CP04, P04 ở CP05, P05 ở CP07; không đòi P04/P05 xong mới qua CP04. |
| **39 · CP04.02** | Bên thực hiện đọc và kiểm gói đầu vào thật của việc con | Gói hợp lệ theo trường/type/đơn vị/nguồn/phiên trước khi làm | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Một lần đọc+kiểm của bên nhận, ghi theo item_key=plan_id. |
| **40 · CP04.04** | Chọn cách làm/tool đúng phiên rồi tạo sản phẩm việc con | Đủ từng nghĩa vụ: CP04.03: Có cách thực hiện hợp lệ; CP04.04: Có sản phẩm thật với đầy đủ identity và output_version | CAT-229* · Master lượt làm/thử; CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-006 · Chạy tổng; TOOL-CTCM-001 · Lập hành trình (nếu dùng được) | LUÔN · Kiểm từng nghĩa vụ áp dụng, không lấy thành công một phần làm hoàn thành cả nhóm. |
| **41 · CP04.06** | Ghi an toàn: kiểm trước → khóa chống trùng → ghi → biên nhận → đọc lại | Đủ từng nghĩa vụ: CP04.05: Đủ trường và đúng kiểu/scope/nguồn/phiên trước commit; CP04.06: Có biên nhận ghi hợp lệ; CP04.07: Nội dung bằng bản gửi; CP04.08: Retry không nhân tác động | CAT-015 · Sổ kết quả kiểm; CAT-228* · Sổ việc thật MOT/kết quả; CAT-238* · Sổ lệnh gửi–nhận–trả | TQT-CHECK-004 · Kiểm ghi/mốc; MCP workspace_transaction (có quyền) | LUÔN · Kiểm/ghi/đọc lại có kết quả riêng; thất bại ở đâu ghi ở đó; không bao gồm ACK của bên nhận. |
| **42 · CP04.09** | Bên nhận mở, kiểm gói nhận và xác nhận ACK bước con | Bên nhận kiểm payload đúng schema/phiên rồi mới ACK | CAT-238* · Sổ lệnh gửi–nhận–trả | TQT-CHECK-004 · Kiểm giao–nhận | KHI(có giao nhận giữa bước/đơn vị) · ACK giao bước không thay Owner ACK nghiệm thu cuối. |
| **43 · CP04.10** | Nếu gửi trùng, chặn nhân tác động | Giữ một kết quả hợp lệ | CAT-238* · Sổ lệnh gửi–nhận–trả | TQT-CHECK-004 · Kiểm ghi/mốc | KHI(gửi trùng hoặc retry) · Nhánh không phát sinh phải ghi − Không áp dụng, không tô Hoàn thành. |
| **44 · CP04.11** | Nếu phản hồi cũ, so phiên và từ chối | Không dùng green cũ | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | TQT-CHECK-004 · Kiểm ghi/mốc | KHI(phản hồi stale) · Không dùng giá trị green/đánh giá cũ; mở issue. |
| **45 · CP04.12** | Nếu mất quyền, dừng và ghi sự cố | Có người xử lý vấn đề quyền | CAT-017 · Sổ sự cố vận hành | — | KHI(permission_denied) · Ghi CAT-017, không tự nâng quyền. |
| **46 · CP04.13** | Nếu thiếu Master đích, tra lại và ghi issue | Biết sổ/người/bước sửa | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | TQT-CHECK-005 · Kiểm Master | KHI(chưa có sổ/đích ghi đúng) · Ghi CAT-069?, chỉ rõ thiếu sổ khác chưa xác định sổ. |
| **47 · CP04.14** | Nếu dữ liệu sai, gọi QTTH002 giải quyết | Có kết quả sửa được kiểm lại | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | — | KHI(sai dữ liệu/sản phẩm) · Gọi QUY TRÌNH MOW-TH-002 (không là Tool); giữ mốc trước không bị ảnh hưởng. |
| **48 · CP04.15** | Nếu sửa quy trình/hợp đồng, theo QTTH003 | Tăng phiên và giữ lịch sử | CAT-016 · Sổ nhật ký thay đổi định nghĩa | — | KHI(cần sửa quy trình/hợp đồng) · Áp dụng QUY TRÌNH MOW-TH-003; tăng phiên, đánh giá ảnh hưởng. |
| **49 · CP04.16** | Nếu hủy, ghi lý do/phiên/nơi nhận/việc bù | Có bản ghi hủy khi phát sinh | CAT-244* · Sổ hủy và việc bù | TQT-CHECK-004 · Kiểm ghi/mốc | KHI(hủy/việc bù) · Ghi CAT-244* chỉ khi phát sinh, giữ receipt idempotency. |
| **50 · CP04.17** | Kiểm dấu lịch sử bất biến của lần thực hiện, ghi bù nếu thiếu | Sự kiện/receipt/version được lưu chính xác, không xóa bản cũ | CAT-233* · Sổ sự kiện bản ghi/chống trùng | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Không ghi lại kết quả đã lưu nếu chỉ khôi phục nhật ký. |
| **51 · CP04.18** | Chỉ đóng việc con khi có output_ref thật | Có sản phẩm/bằng chứng đúng | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Lặp theo plan_id đến hạn; kết quả được nhận đúng hợp đồng mới đóng. P04/P05 đóng tại mốc tương ứng, không tạo vòng chờ CP04. |
| **52 · CP04.19** | Chốt CP04 sau khi kiểm đầu ra tới hạn | Mọi việc con đến hạn CP04 có đầu ra + đọc lại hợp lệ; việc ở CP05/07 chưa bị ép đóng | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Không tích tay |

</details>

<details>
<summary><strong>CP05 · Kiểm đầu ra · 8 bước</strong></summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả | Tool gợi ý | Điều kiện / ghi chú |
|---|---|---|---|---|---|
| **53 · CP05.03** | Reviewer nạp ca, tự mở đúng bản và chạy kiểm | Đủ từng nghĩa vụ: CP05.01: Tập ca áp dụng đủ, không tạo lại ca kiểm; CP05.02: Có log mở đúng ID/phiên/hash và nội dung; CP05.03: Mỗi ca có kết luận và CAT-015 đọc lại được | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc; TQT-CHECK-004 --read-designs (nếu là bản thiết kế); reader phù hợp loại khác | LUÔN · Kiểm từng nghĩa vụ áp dụng, không lấy thành công một phần làm hoàn thành cả nhóm. |
| **54 · CP05.04** | Nếu là UI, thử nút/trạng thái/nhánh thật | Có bằng chứng UI đúng phiên | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 --check-g1-ui (nếu phù hợp) | KHI(sản phẩm là UI) · Có UI thật mới kiểm giao diện, không lấy test mẫu. |
| **55 · CP05.05** | Kiểm nội dung bản thiết kế từng MOT | Đủ trường/nút/nhánh/luật/hash | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 --read-designs | KHI(sản phẩm là thiết kế) · Kiểm đủ field/state/control/branch/rule_ref theo mã/phiên. |
| **56 · CP05.06** | Kiểm kết quả trả cuối đúng caller/phiên/kiểu | Không trả sai nơi nhận | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | KHI(có trả kết quả cho caller) · Chặng trả cuối phải kiểm giá trị, người nhận, kiểu, thời điểm. |
| **57 · CP05.07** | Nếu G2/G3, kiểm nguồn/evaluator/permission live | Không nhầm demo thành live | CAT-015 · Sổ kết quả kiểm | TOOL-CTCM-005 · Rà dữ liệu/lỗi (nếu dùng được) | KHI(có nguồn hoặc evaluator live trong phạm vi) · Không ép G2/G3 vào nghiệm thu G1 chỉ thiết kế. |
| **58 · CP05.08** | Nếu ca FAIL, ghi issue/người sửa/bước quay | Lỗi có cách khắc phục | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | — | KHI(ca kiểm FAIL) · Áp dụng MOW-TH-002, ghi CAT-069?, quay về đúng nguồn lỗi. |
| **59 · CP05.10** | Chạy bộ kiểm tổng đúng phiên khi quy trình hoặc mức rủi ro yêu cầu | Kết quả bộ tổng PASS có hash/biên nhận hoặc quyết định không yêu cầu đã ghi | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-006 · Chạy bộ kiểm tổng | KHI(cần fullsuite theo phạm vi) · Chạy trước CP05/Owner duyệt/ACK; thất bại quay bước sửa. Đổi sản phẩm sau kiểm thì kết quả cũ không còn hiệu lực. |
| **60 · CP05.09** | Chốt CP05 khi đủ ca và đúng phiên | CP05 đạt hoặc Vướng rõ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | LUÔN · Kỹ thuật không thay Owner |

</details>

<details>
<summary><strong>CP06 · Duyệt kết quả · 4 bước</strong></summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả | Tool gợi ý | Điều kiện / ghi chú |
|---|---|---|---|---|---|
| **61 · CP06.02** | Xác thực người duyệt/thẩm quyền theo phạm vi | Không dùng worker tự ký | CAT-025 · Sổ phiếu duyệt/quyết định | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Reviewer khác approver |
| **62 · CP06.03** | Gom đúng sản phẩm/bằng chứng rồi trình người có quyền quyết định | Đủ từng nghĩa vụ: CP06.01: Người duyệt mở đúng bản; CP06.03: Có quyết định rõ ràng | CAT-025 · Sổ phiếu duyệt/quyết định | TQT-CHECK-005 · Kiểm Master; — | LUÔN · Kiểm từng nghĩa vụ áp dụng, không lấy thành công một phần làm hoàn thành cả nhóm. |
| **63 · CP06.04** | Ghi quyết định kèm product_binding và phiên | Có phiếu duyệt đọc lại được | CAT-025 · Sổ phiếu duyệt/quyết định | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Không giả APPROVED |
| **64 · CP06.05** | Chốt CP06 sau khi so quyết định với sản phẩm | CP06 đạt hoặc quay xử lý | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Kỹ thuật không là Owner |

</details>

<details>
<summary><strong>CP07 · Bàn giao · kết thúc · 7 bước</strong></summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả | Tool gợi ý | Điều kiện / ghi chú |
|---|---|---|---|---|---|
| **65 · CP07.01** | Tạo gói bàn giao P05 hoặc việc con cuối theo kế hoạch | Có đầu ra để giao đúng bản; chỉ đóng P05 sau ACK thật CP07.04 | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | KHI(kế hoạch có việc bàn giao cuối P05/tương đương) · Không tạo kết quả bàn giao giả nếu quy trình không có việc con ấy. |
| **66 · CP07.02** | Kiểm hợp đồng nhận cuối và nơi trả | Đúng người/sản phẩm/phiên | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm giao–nhận | LUÔN · Duyệt chưa là ACK |
| **67 · CP07.03** | Ghi giao đúng bản, người và nguồn sản phẩm | Có sổ bàn giao thật | CAT-232* · Sổ bàn giao/xác nhận nhận | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Không chỉ gửi link |
| **68 · CP07.04** | Lấy ACK thật từ bên nhận có thẩm quyền | Có biên nhận đúng bản | CAT-232* · Sổ bàn giao/xác nhận nhận | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Iframe không là Owner ACK |
| **69 · CP07.06** | Kiểm liên tục CP01–07 và nghĩa vụ áp dụng | 7/7 bằng chứng thật, P05 đóng sau ACK; không suy 006 đã đạt chỉ từ 005 | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | LUÔN · Không ép nhánh chưa có |
| **70 · CP07.07** | Ghi bài học, công cụ đã dùng và vấn đề còn mở để dùng lần sau | Có liên kết tool/phiên/kết quả/issue và giới hạn nghiệm thu ở sổ nguồn | CAT-233* · Sổ sự kiện bản ghi/chống trùng | TQT-CHECK-006 · Chạy tổng | LUÔN · Lưu liên kết, không chép sổ: lượt tool ở CAT-229*, vấn đề ở CAT-069?, sửa định nghĩa ở CAT-016. Không có bài học ghi không phát sinh; lịch sử đóng vẫn bắt buộc. |
| **71 · CP07.08** | Khép RUN và nhả cờ bận sau khi xác minh tiến trình/lease | Có KQ cùng RUN_ID XONG hoặc DỪNG, giữ STARTED; Bảng/root đồng bộ; không còn lease của RUN | CAT-233* · Sổ sự kiện bản ghi/chống trùng | MCP workspace_task_status/exec_status và gateway theo quyền | LUÔN · XONG chỉ trong phạm vi thật đã đạt. Bị chặn hoặc hết scope thì DỪNG sạch tại bất kỳ mốc nào, không giữ RUN để chờ. G1 đạt không thay KQ RUN. |

</details>

## 3. Ví dụ cách ghi — không chép sẵn vào hồ sơ

- Bước phát sinh: thêm `BS-001`, `after_step=CP02.07`, hành động, lý do và điều kiện xong vào `added_steps`. Kết quả thực hiện chỉ ghi khi đã làm; mã BS không thay mã chuẩn.
- Nhánh không có UI: CP05.04 là bước có điều kiện. Ghi đánh giá `NOT_APPLICABLE` kèm căn cứ loại sản phẩm và biên nhận máy hoặc phiếu rà khác hãng đúng hồ sơ/phiên theo §11 trong `cycle.applicability`; máy giữ căn cứ, giao diện thu gọn nhánh. Chưa kiểm được thì `UNKNOWN` và hiện ra; không tự ghi DONE/Không làm để bỏ bước.
- Dùng dấu ? ở cột/bước để tra hướng dẫn. Ô thực tế chưa có bằng chứng để trống.

## 4. Điều kiện trước khi đưa vào chạy và gắn cùng trang QTTH 05

1. **Giao diện:** trên Over view, QTTH 05 là bản đồ bảy mốc; ngay **bên dưới phần chi tiết 005**, QTTH 006 là các nhóm CP01–07 thu/mở. Không để 006 thành một trang rời thay thế. Tổng quan không cho sửa tình trạng.
2. **Hồ sơ DEF 00.1:** với mỗi application ghim 006@version, sinh danh sách bước chuẩn + dòng thêm/N/A/điều chỉnh riêng, đúng thứ tự và item_key. Cùng một hồ sơ là nguồn trạng thái và bằng chứng. Mặc định các bước chưa có biên nhận `Trống`; không hồi tố P37 thành đã làm 006.
3. **Check chuyển mốc:** chỉ tính các bước **đến hạn và áp dụng** cùng nghĩa vụ gốc của 005; không bỏ qua bước lõi nhờ đánh N/A; bước bổ sung có phê duyệt được tính vào CP tương ứng. Khi có vấn đề biết thiếu gì, ai làm, quay bước nào.
4. **Trước khi chuyển Master/PG:** Host Codex phải kiểm tên/mã sổ và quyền ghi thực, chống trùng Master; chọn một SSOT cho step definitions và một nguồn result theo hồ sơ, có kiểm phiên/hash và đồng bộ giao diện; dùng lại CHECK001–006.
5. **Thử với AI mới:** chọn một công việc mới nhỏ và một công việc có biến thể (+/−). AI chỉ đọc 005/006 + hồ sơ và Tool/Master hiện hữu; phải biết làm gì, ghi ở đâu và xử lý lỗi. Chưa có ca này thì phiên 006 chưa được nghiệm thu vận hành độc lập.

**Tác động:** đây là hiệu chỉnh bản thiết kế 006, KHÔNG sửa MOW-TH-005, checkpoint/ứng dụng P37, PG hay Master vật lý. P40 đăng ký thiết kế và ghép cùng hồ sơ; không thay G1 hoặc quyền production.

## 5. Ghi bước thực hiện và dùng lại — một nguồn

Nguồn định nghĩa duy nhất là tệp này. `catalog.detailed_workflow` và UI là bản sinh theo SHA256, CHECK005 đối chiếu từng dòng; không chỉnh tay bảng chiếu. Ghim `process_version + definition_sha256`; phiên đã dùng phải giữ lại qua lịch sử Git, không tự cập nhật hồ sơ sang phiên mới.

Nguồn theo việc: `view.html → catalog.work_schedule.records[record_id].detail_tracking`, thuộc DEF00.1 hiện hữu, không mở Master. Binding gồm `application_id, target_version, process_version, definition_sha256, mode, events`. MOW001 giữ hồ sơ chẩn đoán P46 theo phiên gốc; bản xem gộp không sửa kết quả cũ. Việc chưa mở chỉ xem mẫu, không gắn hồ sơ hộ.

Sự kiện thêm nối tiếp gồm `event_id, revision, at, actor, application_id, target_version, process_version, definition_sha256, step_id, item_key, status, adjustment, reason, evidence_ref, result_ref, issue_ref, owner, return_to`. Bằng chứng giữ ở Master gốc, không nhét bản sao vào từng dòng. `DONE` cần kết quả/bằng chứng đã kiểm đúng phiên; `NA` phải là nhánh có điều kiện đã xác minh; +Bổ sung/↔Thay thế giữ định nghĩa cha, phụ thuộc, người/phạm vi phê duyệt và không xóa dòng cũ. Điều chỉnh chưa đủ căn cứ hiện Vướng; kiểm bằng CHECK005 trước ghi. Không dùng localStorage làm hồ sơ.

**Giới hạn P40:** ghép hiển thị và kiểm khuôn tại CHECK005; chưa mở phiên làm thật theo 006, chưa cưỡng chế chuyển 7 mốc bằng 006 ở gateway. Không dùng bảng này làm căn cứ nâng tiến độ hoặc cấp quyền. Bước tiếp theo do Owner giao: thử một việc mới và một biến thể trên cửa ghi, có bằng chứng từng item_key; thiếu quyền/schema thì dừng tại đúng bước và sửa trong sổ hiện hữu. Không tự nâng runtime để hoàn tất thủ tục giao diện.

## 6. Quy định chuẩn và hồ sơ thực tế — P42

Overview là cửa đọc quy định chuẩn: 7 mốc → 11 mục phải ghi → 71 bước, cùng nguồn theo phiên. Bảng chuẩn chỉ có hành động, điều kiện xong, Master đích và công cụ gợi ý; không có cột kết quả hay tình trạng việc thật. Không giữ bản hồ sơ MOW001 thứ hai trên Overview.

Hồ sơ DEF00.1 giữ sẵn mã/tên bước chuẩn và liên kết quy định. Các cột thực tế ban đầu rỗng: xác nhận đã làm/không làm, việc đã làm hoặc lý do không làm, công cụ thực dùng, kết quả/bản ghi, người và thời điểm. Rỗng là chưa ghi, KHÔNG có nghĩa không làm. Không lấy tên tool/Master/ghi chú gợi ý trong quy định làm dữ liệu thực tế. Không làm phải ghi lý do; không tự tính như đã hoàn thành.

Sự kiện trong detail_tracking.events bổ sung các trường `performed` (DONE|NOT_DONE|BLOCKED), `actual_action`, `tool_uses` (mảng tên/mã công cụ thực dùng), `record_ref`. Dùng lại `reason,result_ref,evidence_ref,actor,at,status` có sẵn. DONE cần mô tả việc làm + kết quả/bằng chứng; NOT_DONE/BLOCKED cần lý do, không dùng để bỏ nghĩa vụ bắt buộc. Các khai báo phải đúng binding/phiên; thiếu hoặc lệch không hiển thị như kết quả hợp lệ. Khi chưa có adapter xác thực, xác nhận chỉ được ghi rõ là khai báo chưa đối chiếu, tuyệt đối không tích xanh. Lịch sử nối tiếp, không xóa; thay đổi hiển thị không sửa hồ sơ G1 đã nghiệm thu.

11 mục hồ sơ giữ kết quả/bằng chứng đã có; dấu ? tại cột/mục giải thích ngay nơi dùng, lấy nội dung từ nguồn chuẩn. Overview vẫn là nơi chứa luật. Lượt nào xong thì KQ/nhả lease và dọn tài nguyên của chính lượt đó ngay; không xóa khóa dịch vụ hay tài nguyên AI khác.

## 7. Lịch sử phát hiện P45 — luật lượt mới xem §8
Giữ mã việc; mỗi vòng làm lại có application_id mới, giữ hồ sơ G1 và quyết định/ACK cũ nguyên vẹn. Trước CP01.04 phải xác minh đường ghi bảo vệ đúng application_id mới, phiên nguồn và sự kiện006; quyền ghi tệp chung không thay bằng chứng kiểm hợp đồng. Nếu chưa có, ghi lượt thật và điểm tắc tại CAT229/CAT069 hiện hữu, liên kết từ DEF00.1, không mở hồ sơ giả hoặc ghi vòng mới vào G1 cũ. KQ DỪNG tại đúng bước, không giữ khóa; sau sửa kiểm lại cửa ghi rồi tiếp tục, không hồi tố bước chưa làm.
P45 đo cấu hình thật: policy MOW001-G1-P36-2 chỉ ghim application G1 cũ. Chưa có nghiệm thu quyền/adapter vòng mới; không suy rằng cả hệ thống bị từ chối ghi. Trạng thái hiện hành theo Master lỗi/lượt làm, không lấy mục này làm kết quả kiểm cho lần sau.

## 8. Luật dùng cho lượt mới — P51, phiên 0.6

### Cửa ghi ngoài PG: kiểm bởi Host, không giả là máy chủ cưỡng chế

Trong giai đoạn thử hồ sơ ngoài PG, có hai mức khác nhau. `HOST_CHECK` là quy trình kiểm trước khi ghi bằng công cụ hiện có; `SERVER_ENFORCED` chỉ được ghi khi máy chủ thật đã bảo vệ đúng application/phạm vi. P51 chỉ chuẩn bị mức HOST_CHECK, không thay cấu hình bảo vệ G1, không cấp quyền mới. Lượt thật tiếp theo chỉ mở sau hai hãng duyệt đúng bộ sửa và Owner đồng ý ca thử.

Với một application mới, Host phải ghi rõ path/phạm vi/nguồn quyền hiện hữu, kiểm ứng viên bằng CHECK005, ghi CAS `expected_version` qua gateway được phép, lấy receipt và đọc lại so hash. `cycle.write_authorization` gồm `mode=HOST_CHECK, application_id, path, authority_ref, precheck_ref, cas_receipt, readback_ref, server_enforced=false`. Trước khi có receipt, chưa xác nhận đã ghi. Ứng viên có thể soạn local; hồ sơ chuẩn chỉ ở DEF00.1. Không dùng quyền ghi tài liệu để gọi endpoint nghiệp vụ chưa được phép. Cổng từ chối hoặc nguồn đổi thì DỪNG, không dùng SSH ghi vòng qua cổng. ENTRY-b (mở rộng bảo vệ máy chủ) là việc riêng cần quyền/duyệt tương ứng.

Kiểm dùng lại: `node check-work-masters.js view.html --validate-dossier candidate.json`. Tệp đầu vào có `dossier` là binding của application mới ; bộ kiểm tự đối chiếu biên nhận trực tiếp với Git trên VPS, không tin `server_receipts` do người gọi tự khai. Lệnh này kiểm hợp đồng, không ghi nguồn; PASS không tự cấp quyền và không nghiệm thu sản phẩm. Khi xin hoàn tất toàn việc, đầu vào kiểm phải có `require_complete=true`: đủ bảy mốc đã khép và dẫn chiếu quyết định/ACK; chưa đủ thì không PASS hoàn tất. Sau CAS phải kiểm đúng bản đọc lại; thiếu/sai thì ghi issue và chặn bước phụ thuộc.

### Thời gian: 7 mốc, không bắt 174 lượt ghi

Mỗi mốc ghi `cycle.milestone_events[]` một sự kiện STARTED trước làm và một KQ sau làm: `event_id, application_id, checkpoint, kind=STARTED|KQ, outcome` (KQ là XONG hoặc DỪNG), `evidence_ref`. Không tự khai giờ máy chủ. Ghi bằng CAS; lấy commit SHA trả về. Chạy **trên repo chuẩn VPS**, chỉ đọc:

`node work/tools-quy-trinh/check-work-masters.js --commit-receipt /opt/incomex/data/workspace-tools/github-workspace <commit-SHA> work/tools-quy-trinh/view.html <event_id>`

DOT đọc chính sự kiện trong commit, lấy giờ commit `%cI` và hash bản đã ghi. Ghi biên nhận vào `cycle.milestones[]` (`checkpoint,start_receipt,end_receipt`) cùng lần ghi kế tiếp, không phát sinh một lượt ghi chỉ để thêm giờ. Mất phản hồi: tra operation_id/commit cũ; không tạo STARTED mới. Biên nhận JSON tự khai không đủ: Host/Reviewer phải đối chiếu bằng lệnh đọc repo chuẩn trên.

Thời lượng mốc = giờ KQ − giờ STARTED, bao gồm ghi/đọc và thời gian chờ trong khoảng đó. Bước tay dùng `SHARED_INTERVAL` và `interval_ref` của mốc; không cộng lại từng dòng. Tool có thời gian riêng thì giữ receipt riêng. Tổng tới khép RUN và tổng tới ACK Owner là hai con số riêng; chưa ACK thì tổng hoàn tất để trống. Mốc DỪNG rồi tiếp tục có cặp sự kiện mới; không đè cặp cũ. Không ghi thời gian mốc bằng `RECORDING_ONLY`; P46 không đo được hồi tố.

### Bước lặp, Không làm, người kiểm

Bước lặp ghi từng item hoặc một manifest: `expected_ids,checked_ids,count,source_version,evidence_ref`; count khớp ID duy nhất, DONE phải đủ tập cần kiểm. Không dùng item_key=G1 chung cho mọi câu/trường/MOT trong lượt mới.

Mọi BLOCKED mới nhất có reason/issue_ref/owner/return_to/next_trigger. NOT_DONE có condition_evidence và lý do; bước LUÔN hoặc nghĩa vụ đến hạn còn cần exception_approval gồm approver,authority_ref,evidence_ref,scope đúng mã bước. Ngoại lệ không được vượt quyền Owner hay bỏ nghĩa vụ cốt lõi. Rà/duyệt độc lập có subject_actor,reviewer,evidence_ref,target_version và hai người phải khác nhau; hãng khác khi phạm vi yêu cầu đồng thuận hai hãng. Lời khai hoặc TEST không thay review hợp đồng.

### Hai bên xác nhận đúng một bộ sửa

Sổ duyệt CAT-025 hiện hữu giữ một phiếu theo bộ sửa gồm manifest (hash luật006, luật002, CHECK005, UI), binding, scope và reviews nối tiếp. Hai cột cuối **GPT duyệt** / **Claude duyệt** lấy từ phiếu này, không nhập tay lần nữa. Mỗi review có vendor,reviewer,reviewed_at,decision,evidence_ref,binding,scope. Đổi hash/phạm vi thì dấu cũ hết hiệu lực. Chưa có review để trống. Đồng thuận chỉ khi cả OpenAI và Anthropic APPROVE cùng binding/phạm vi; Owner quyết sau đó, không suy từ hai chữ ký thành Owner duyệt hoặc sản phẩm nghiệm thu. Claude P49 duyệt bản P50 không thay chữ ký cho P51.

## 9. Hoàn thành một việc QT001 · hợp đồng nghiệm thu P52

Đọc phạm vi đã được Owner giao ở §0 của việc trước khi làm. **XONG một RUN chỉ xác nhận đã khép lượt và nhả tài nguyên; không xác nhận sản phẩm đạt.** G1 đã duyệt chỉ là thiết kế. G2 là triển khai/kiểm kỹ thuật; G3 là vận hành/bàn giao. Không gọi “QT001 hoàn thành toàn bộ” khi chỉ có G1. P46 vẫn là chẩn đoán, không là bằng chứng AI mới tạo sản phẩm mới.

### 9.1 Khi nào GPT và Claude được ký OK?

Cả hai đọc cùng một phiên sản phẩm, cùng phạm vi và cùng bộ bằng chứng. Chỉ ký **nghiệm thu việc thật** khi đủ các điều sau:

1. Mục tiêu, đầu vào, sản phẩm phải giao, giới hạn G1/G2/G3, người nhận và điều kiện bắt đầu được xác nhận cho đúng lượt. Không kế thừa chữ ký G1 sang lượt mới.
2. Người/AI mới thực hiện theo quy trình ra sản phẩm thực. Có manifest từng câu hỏi và câu trả lời, từng MOT/field/nhánh áp dụng; bên nhận mở và dùng được nội dung đúng phiên, kiểm cả đầu nối. TEST chỉ chứng minh bộ kiểm.
3. Có bản ghi cho đủ 7 mốc và mọi bước/item áp dụng của bản006 đã ghim. DONE có bằng chứng; Không làm có điều kiện/ngoại lệ hợp lệ. Bước bắt buộc bị chặn hoặc còn thiếu không được chuyển thành nợ để ký đạt.
4. Mười một nhóm ghi được đối chiếu với bản ghi thật tại Master tương ứng. DOT/Tool thực dùng có mã/phiên/kết quả/biên nhận; lỗi công cụ được ghi và kiểm lại. Đọc lại đúng hồ sơ DEF00.1, không bàn giao trang local thay thế.
5. Đo 7 mốc bằng thời điểm commit máy chủ của sự kiện STARTED/KQ. Thời gian công cụ đo riêng; không cộng hai khoảng chồng nhau. Giờ nhập hồ sơ không là giờ hoàn thành; thiếu số đo lịch sử ghi chưa đo, không hồi tố. Có tổng tới khép RUN và tổng tới ACK riêng.
6. Kiểm độc lập hợp đồng/sản phẩm ghi người làm, hãng người làm, người rà, hãng người rà, phiên và bằng chứng. Hai hãng phải là OpenAI và Anthropic, không chỉ khác tên.
7. Danh sách nợ và kiểm kê field theo 9.2–9.3 được cả hai hãng duyệt đúng phiên. Không có nợ chặn phạm vi đang nghiệm thu.
8. GPT và Claude tự ký hai ô CAT-025 của **nghiệm thu sản phẩm**, rồi Owner quyết định khi đến hạn; bên nhận ACK đúng phiên; ghi KQ, nhả cờ/lease, không còn công việc nền thuộc lượt này.

Chữ ký **duyệt luật/bộ sửa**, **duyệt danh sách nợ**, **duyệt kiểm kê field** và **nghiệm thu sản phẩm thực** có phạm vi khác nhau. Lưu ở cùng CAT-025, hiển thị cùng hồ sơ; không suy một chữ ký thay cho chữ ký khác. Mỗi phiếu có `record_id, scope, binding, manifest, reviews`; review có hãng/người/kết luận/thời điểm/bằng chứng. Binding là SHA256 của manifest đã chuẩn hoá; đổi nguồn/phạm vi/nợ/field thì phải rà delta và ký lại phần bị ảnh hưởng. Giữ nguyên chữ ký cũ trong lịch sử. Không ký thay hãng kia.

### 9.2 Danh sách nợ để làm tiếp

Một nguồn: `cycle.issues` của hồ sơ → CAT-069; phiếu CAT-025 trỏ hash danh sách đó. Mỗi dòng phải có: mã, việc còn thiếu, phạm vi bị chặn (`blocks_scope`), người nhận (`owner`), việc cần làm (`next_action`), quy trình xử lý (`route_process`), bước quay lại (`return_to`), điều kiện chạy tiếp (`next_trigger`). Có thể gộp các phát hiện cùng nghĩa vụ bằng tham chiếu, không xoá lịch sử.

OPEN là chưa giải quyết. Đề nghị để sau vẫn OPEN tới khi hai hãng cùng duyệt danh sách và người có quyền chấp nhận; khi đó DEFERRED cần quyết định/bằng chứng. CLOSED cần sản phẩm sửa, đọc lại tại nơi lỗi, người kiểm độc lập. SUPERSEDED cần ánh xạ nghĩa vụ sang sản phẩm thay thế; sản phẩm mới tồn tại không tự khép nợ cũ. Ghi rõ nợ thuộc G2/PG không chặn G1; nợ kiểm hợp đồng/đầu ra thật chặn nghiệm thu lượt làm thật. Mỗi bên phải ký cả tính đầy đủ của danh sách lẫn việc nợ nào được phép để sau.

### 9.3 Field: kiểm kê trước, tạo sau

Dùng **ML-DEF-008 · Master Field** (`definition-master-v1.html?stt=8`), không lập Master khác. Từ 18 thiết kế Master, gom theo định nghĩa đầy đủ; cùng tên khác kiểu/ý nghĩa không tự gộp. Mỗi field có mã, tên/khóa, kiểu, phiên định nghĩa, nguồn, các nơi dùng, tình trạng ngoài PG, tình trạng PG, đích PG và bằng chứng đọc lại khi có. Quy tắc bắt buộc theo nơi dùng ở quan hệ Field–nơi dùng, không ép thành thuộc tính chung.

Tình trạng ngoài PG: Đã đăng ký → Cần bổ sung → Đã có trong kho tệp → Đã kiểm; Ngừng dùng giữ lịch sử. PG: **Chưa xác minh**, **Cần tạo thêm** (đã đối chiếu schema và không có), **Đã tạo trong PG** (có migration/đích/phiên và đọc lại), **Đã kiểm PG**. Không có bằng chứng thì không tích xanh PG. Lượt P52 không đọc/ghi PG: số cần tạo mới trong PG **chưa xác định**, không ghi 0.

Báo cáo cuối mỗi việc phải ghi: số lượt dùng field, số định nghĩa dùng lại, số định nghĩa mới của lượt, danh sách mã/nguồn và số còn chưa đối chiếu PG. Dùng lại trường đã có trước khi thêm. Dấu ? ở tên cột giải thích cách điền; ô thực tế chưa có bằng chứng để trống. Hai cột cuối GPT duyệt / Claude duyệt trỏ phiếu kiểm kê field đúng phiên trong CAT-025, không phải chữ ký tạo PG.

### 9.4 Kiểm giờ và hãng (sửa phản biện Claude V3)

CHECK005 mặc định và `--validate-dossier` dùng chung logic đọc sự kiện trong commit Git của chính kho chứa view.html đã được theo dõi. Commit phải thuộc lịch sử HEAD, đúng event/application/checkpoint/STARTED-KQ/thời điểm; sai thì FAIL. Không dùng `server_receipts` người gọi tự cung cấp làm chứng cứ. Snapshot không có Git chuẩn báo UNVERIFIED_RECEIPT, vẫn kiểm các phần khác; `require_complete=true` phải dừng, không được nghiệm thu. `--commit-receipt` chỉ là cách đọc cùng dữ kiện, không là đường cấp chữ ký.

P52 thêm `review.subject_vendor`, `review.reviewer_vendor`; phải có trong tập hãng quy định và khác nhau tại bước rà độc lập. Không thay chữ ký review hợp đồng bằng review hồ sơ. Luật này áp cho mọi hồ sơ dùng bản006 có execution_policy, không hardcode P46.


## 10. Rút gọn thao tác, giữ nghĩa vụ · P53

71 bước gồm 70 bước sau gộp 17 dòng cũ và một bước tiếp tục sau DỪNG. Không bỏ nghĩa vụ: 87 mã cũ ánh xạ duy nhất tới mã mới; mỗi bước gộp có `members` và kết quả kiểm từng nghĩa vụ. Ghi một thao tác không có nghĩa chỉ kiểm một điều. Giữ phiên 0.5–0.7 và events cũ; hồ sơ cũ chỉ có bản xem gộp, không tự đổi phiên hoặc nghiệm thu 71 bước mới.

A0/phạm vi/quyền Owner (CP01.02) trước mở hồ sơ. Tra trùng là khâu đầu của CP01.04. CP01.08 ghi nguồn một lần; CP02.03 chỉ đọc lại và kiểm phiên/hash. CP04.06 giữ riêng kết quả precheck, operation_id trước tác động, ghi, receipt và đọc lại; không bao gồm ACK bên nhận. CP06.04 là quyết định người có quyền, không phải chữ ký reviewer khác hãng; hai chữ ký chuyên môn kiểm ở CP03.05/CP05.03 và phiếu CAT-025.

### Ai làm, mức tự động và điều kiện là ba thông tin khác nhau

`step_policies`: actor (AI/REVIEWER/HUMAN/MACHINE là vai dự kiến); automation_current (MANUAL/NO_COMMAND/HAS_COMMAND); applicability (ALWAYS/CONDITIONAL). HAS_COMMAND chỉ được khai khi có command và last_real_run_ref chứng minh lệnh tự thực hiện và ghi cả bước. Có bộ kiểm không có nghĩa đã có lệnh tự thực hiện. Hiện các bước dự kiến máy vẫn NO_COMMAND: AI thực hiện bằng DOT hỗ trợ, ghi `execution_mode=MANUAL_ASSISTED`; nợ lệnh cần làm TQT-P53-AUTOMATION. Không lập DOT mới trong lượt này. Mục tiêu 29 dòng ghi tay chưa được chứng minh.

Hồ sơ mới ghi applicability theo step_id/item_key: APPLIES, NOT_APPLICABLE, UNKNOWN. Chưa có dữ kiện là UNKNOWN, hiện để xử lý; không đồng nghĩa Không làm. NOT_APPLICABLE cần bằng chứng đúng việc/phiên/nhánh theo §11: có lệnh đánh giá thì biên nhận máy; chưa có lệnh thì AI làm tay và reviewer khác hãng xác nhận. Chưa đủ xác nhận để UNKNOWN; không giả chữ ký máy. ALWAYS không được chuyển NOT_APPLICABLE để lách nghĩa vụ. Khi đã phát sinh nhánh phải có sự kiện tương ứng. Không lấy việc thiếu issue làm bằng chứng không phát sinh lỗi.

Bước DONE gộp có `obligation_checks`: mỗi mã trong members được kiểm PASS kèm evidence_ref; nghĩa vụ có điều kiện có thể NOT_APPLICABLE với biên nhận đánh giá đúng nghĩa vụ. Không đồng nhất NOT_APPLICABLE với DONE. Bước HAS_COMMAND ghi tool_run_id nối bản ghi CAT-229 cùng application/step/phiên, trạng thái thành công, bằng chứng, người ghi và giờ thật; lệnh hỗ trợ không đủ thay bằng chứng trọn bước.

Giờ milestone: STARTED khi thực sự vào mốc; KQ khi khép. Event mới dùng started_at/completed_at nếu đã đo, nếu chỉ có at thì chỉ kiểm giờ ghi (không đổi thành thời lượng). Thời điểm kiểm phải trong khoảng milestone; thiếu biên nhận mốc báo chưa xác minh, không nghiệm thu. Khi tiếp tục ghi vòng mốc mới, không sửa thời điểm mốc cũ. CP03.12 áp tại nơi dừng ở mọi mốc: previous_run_id/return_to/source_version/rights_receipt, đối chiếu thay đổi rồi mới tiếp tục; không lặp tác động đã có receipt.

KPI ca thật: thời gian từng mốc và toàn lượt; số lần nhập tay; revision; item lặp; số điều kiện UNKNOWN. Không có số đo thì để trống. Chưa chạyQT002 và chưa nghiệm thu QT001.

### Field và nợ

Nợ chỉ dùng OPEN/VERIFIED/FIXING/VERIFYING/CLOSED/DEFERRED/REJECTED/SUPERSEDED. Giữ lịch sử đổi trạng thái và bằng chứng kiểm độc lập. D1/D2 được đóng theo Claude V5.1; sửa luật nhưng chưa kiểm trong việc thật để VERIFYING, không OPEN cũng không tự CLOSED.

Field gộp khi cùng nghĩa + khóa + kiểu + miền/ràng buộc. Các nhãn tại nơi dùng chuyển về usage_labels; old_to_new/aliases giữ ID cũ. Cùng tên nhưng khác nghĩa (phiên đối tượng so với SHA256 nguồn) giữ riêng. Không suy cùng kiểu text là cùng một field. Tình trạng khác miền có tên phân biệt theo Master dùng. 327 lượt dùng thiết kế + 9 lượt quản lý giữ nguyên; PG vẫn chưa xác minh. Field-COVERAGE chưa khép.

<details><summary>Bảng đối chiếu 87 nghĩa vụ cũ → mã hiện hành</summary>

| Mã cũ | Mã hiện hành |
|---|---|
| CP01.01 | CP01.01 |
| CP01.02 | CP01.02 |
| CP01.03 | CP01.04 |
| CP01.04 | CP01.04 |
| CP01.05 | CP01.04 |
| CP01.06 | CP01.06 |
| CP01.07 | CP01.02 |
| CP01.08 | CP01.08 |
| CP01.09 | CP01.09 |
| CP01.10 | CP01.10 |
| CP01.11 | CP01.04 |
| CP01.12 | CP01.12 |
| CP02.01 | CP02.01 |
| CP02.02 | CP02.02 |
| CP02.03 | CP02.03 |
| CP02.04 | CP02.04 |
| CP02.05 | CP02.14 |
| CP02.06 | CP02.06 |
| CP02.07 | CP02.07 |
| CP02.08 | CP02.07 |
| CP02.09 | CP02.10 |
| CP02.10 | CP02.10 |
| CP02.11 | CP02.10 |
| CP02.12 | CP02.12 |
| CP02.13 | CP02.13 |
| CP02.14 | CP02.14 |
| CP02.15 | CP02.15 |
| CP02.16 | CP02.16 |
| CP02.17 | CP02.17 |
| CP02.18 | CP02.18 |
| CP02.19 | CP02.19 |
| CP02.20 | CP02.18 |
| CP02.23 | CP02.23 |
| CP02.21 | CP02.21 |
| CP02.22 | CP02.22 |
| CP03.01 | CP03.01 |
| CP03.02 | CP03.02 |
| CP03.03 | CP03.03 |
| CP03.04 | CP03.04 |
| CP03.05 | CP03.05 |
| CP03.06 | CP03.07 |
| CP03.07 | CP03.07 |
| CP03.08 | CP03.08 |
| CP03.09 | CP03.09 |
| CP03.10 | CP03.10 |
| CP03.11 | CP03.11 |
| CP04.01 | CP04.01 |
| CP04.02 | CP04.02 |
| CP04.03 | CP04.04 |
| CP04.04 | CP04.04 |
| CP04.05 | CP04.06 |
| CP04.06 | CP04.06 |
| CP04.07 | CP04.06 |
| CP04.08 | CP04.06 |
| CP04.09 | CP04.09 |
| CP04.10 | CP04.10 |
| CP04.11 | CP04.11 |
| CP04.12 | CP04.12 |
| CP04.13 | CP04.13 |
| CP04.14 | CP04.14 |
| CP04.15 | CP04.15 |
| CP04.16 | CP04.16 |
| CP04.17 | CP04.17 |
| CP04.18 | CP04.18 |
| CP04.19 | CP04.19 |
| CP05.01 | CP05.03 |
| CP05.02 | CP05.03 |
| CP05.03 | CP05.03 |
| CP05.04 | CP05.04 |
| CP05.05 | CP05.05 |
| CP05.06 | CP05.06 |
| CP05.07 | CP05.07 |
| CP05.08 | CP05.08 |
| CP05.10 | CP05.10 |
| CP05.09 | CP05.09 |
| CP06.01 | CP06.03 |
| CP06.02 | CP06.02 |
| CP06.03 | CP06.03 |
| CP06.04 | CP06.04 |
| CP06.05 | CP06.05 |
| CP07.01 | CP07.01 |
| CP07.02 | CP07.02 |
| CP07.03 | CP07.03 |
| CP07.04 | CP07.04 |
| CP07.06 | CP07.06 |
| CP07.07 | CP07.07 |
| CP07.08 | CP07.08 |

</details>

<details><summary>Ai làm và mức tự động hiện tại · từng bước</summary>

| Bước | Ai làm dự kiến | Tự động hiện tại | Điều kiện | Công cụ hỗ trợ |
|---|---|---|---|---|
| CP01.01 | AI | MANUAL | ALWAYS | — |
| CP01.02 | AI | MANUAL | ALWAYS | — |
| CP01.04 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-005 · Kiểm Master; —; TQT-CHECK-002 · Kiểm mã; TQT-CHECK-001 · Kiểm mô hình |
| CP01.06 | AI | MANUAL | ALWAYS | TQT-CHECK-005 · Kiểm Master |
| CP01.08 | AI | MANUAL | ALWAYS | MCP workspace_read/stat (có quyền) |
| CP01.09 | AI | MANUAL | ALWAYS | — |
| CP01.10 | AI | MANUAL | ALWAYS | — |
| CP01.12 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm bản ghi/mốc |
| CP02.01 | MACHINE | NO_COMMAND | CONDITIONAL | TQT-CHECK-003 · Kiểm khai |
| CP02.02 | AI | MANUAL | CONDITIONAL | — |
| CP02.03 | AI | MANUAL | CONDITIONAL | MCP workspace_read/stat (có quyền) |
| CP02.04 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP02.06 | AI | MANUAL | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP02.07 | AI | MANUAL | ALWAYS | —; TQT-CHECK-004 · Kiểm ghi/mốc |
| CP02.10 | AI | MANUAL | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc; TQT-CHECK-004 · Kiểm giao–nhận; TOOL-CTCM-003 · Phủ nhánh (nếu dùng được) |
| CP02.12 | AI | MANUAL | ALWAYS | TOOL-CTCM-005 · Rà dữ liệu/lỗi (nếu dùng được) |
| CP02.13 | AI | MANUAL | CONDITIONAL | TQT-CHECK-002 · Kiểm mã |
| CP02.14 | AI | MANUAL | ALWAYS | TQT-CHECK-005 · Kiểm Master; TQT-CHECK-004 · Kiểm ghi/mốc |
| CP02.15 | AI | MANUAL | ALWAYS | TQT-CHECK-005 · Kiểm Master |
| CP02.16 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-003 · Kiểm hồ sơ |
| CP02.17 | AI | MANUAL | CONDITIONAL | TQT-CHECK-004 · Kiểm nghĩa vụ |
| CP02.18 | AI | MANUAL | ALWAYS | TQT-CHECK-001 · Kiểm mô hình; TOOL-CTCM-001 · Lập hành trình (nếu dùng được) |
| CP02.19 | AI | MANUAL | ALWAYS | — |
| CP02.23 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm quyền kho tệp; MCP theo quyền hiện có |
| CP02.21 | AI | MANUAL | CONDITIONAL | TQT-CHECK-004 --read-preparation |
| CP02.22 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-003 · Kiểm khai |
| CP03.12 | MACHINE | NO_COMMAND | CONDITIONAL | CHECK004/005 + gateway hiện hữu |
| CP03.01 | MACHINE | NO_COMMAND | CONDITIONAL | TQT-CHECK-006 · Chạy tổng |
| CP03.02 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP03.03 | MACHINE | NO_COMMAND | CONDITIONAL | — |
| CP03.04 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-003 · Kiểm khai |
| CP03.05 | REVIEWER | MANUAL | CONDITIONAL | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP03.07 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP03.08 | REVIEWER | MANUAL | CONDITIONAL | TQT-CHECK-004 --read-preparation |
| CP03.09 | AI | MANUAL | CONDITIONAL | TQT-CHECK-003 · Kiểm khai |
| CP03.10 | AI | MANUAL | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP03.11 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP04.01 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-001 · Kiểm mô hình |
| CP04.02 | AI | MANUAL | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP04.04 | AI | MANUAL | ALWAYS | TQT-CHECK-006 · Chạy tổng; TOOL-CTCM-001 · Lập hành trình (nếu dùng được) |
| CP04.06 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc; MCP workspace_transaction (có quyền) |
| CP04.09 | REVIEWER | MANUAL | CONDITIONAL | TQT-CHECK-004 · Kiểm giao–nhận |
| CP04.10 | AI | MANUAL | CONDITIONAL | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP04.11 | AI | MANUAL | CONDITIONAL | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP04.12 | AI | MANUAL | CONDITIONAL | — |
| CP04.13 | AI | MANUAL | CONDITIONAL | TQT-CHECK-005 · Kiểm Master |
| CP04.14 | AI | MANUAL | CONDITIONAL | — |
| CP04.15 | AI | MANUAL | CONDITIONAL | — |
| CP04.16 | AI | MANUAL | CONDITIONAL | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP04.17 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP04.18 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP04.19 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP05.03 | REVIEWER | MANUAL | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc; TQT-CHECK-004 --read-designs (nếu là bản thiết kế); reader phù hợp loại khác |
| CP05.04 | AI | MANUAL | CONDITIONAL | TQT-CHECK-004 --check-g1-ui (nếu phù hợp) |
| CP05.05 | AI | MANUAL | CONDITIONAL | TQT-CHECK-004 --read-designs |
| CP05.06 | AI | MANUAL | CONDITIONAL | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP05.07 | AI | MANUAL | CONDITIONAL | TOOL-CTCM-005 · Rà dữ liệu/lỗi (nếu dùng được) |
| CP05.08 | AI | MANUAL | CONDITIONAL | — |
| CP05.10 | MACHINE | NO_COMMAND | CONDITIONAL | TQT-CHECK-006 · Chạy bộ kiểm tổng |
| CP05.09 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-003 · Kiểm khai |
| CP06.02 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP06.03 | AI | MANUAL | ALWAYS | TQT-CHECK-005 · Kiểm Master; — |
| CP06.04 | HUMAN | MANUAL | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP06.05 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP07.01 | AI | MANUAL | CONDITIONAL | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP07.02 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm giao–nhận |
| CP07.03 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP07.04 | HUMAN | MANUAL | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP07.06 | MACHINE | NO_COMMAND | ALWAYS | TQT-CHECK-004 · Kiểm ghi/mốc |
| CP07.07 | AI | MANUAL | ALWAYS | TQT-CHECK-006 · Chạy tổng |
| CP07.08 | MACHINE | NO_COMMAND | ALWAYS | MCP workspace_task_status/exec_status và gateway theo quyền |

</details>

## 11. P54 — đánh giá nhánh khi chưa có lệnh và quyết định Field

Cấu trúc71bước/87nghĩa vụ không đổi. `execution_policy.applicability_evaluator` quy định khả năng **đánh giá điều kiện**, riêng với công cụ thực hiện bước. `NO_COMMAND`: AI ghi đánh giá tay, người rà khác hãng xác nhận tại CP05.03. `HAS_COMMAND`: chỉ nhận biên nhận máy; không dùng đường tay. Nợ dùng lại TQT-P53-AUTOMATION, bao gồm bộ đánh giá điều kiện.

Khi chưa được rà, giữ `UNKNOWN` và ghi bằng chứng dự kiến; kiểm thường cho phép lưu, nhưng kiểm hoàn tất vẫn chặn. Khi đủ rà, ghi `NOT_APPLICABLE`, `evaluated_by=AI`, `execution_mode=MANUAL_ASSISTED`, `actor,subject_vendor,evidence_ref,at,revision,review_ref`. Phiếu CAT-015 tại CP05.03 phải APPROVE, khác người/khác hãng, đúngapplication/phiên/quy trình/hash. `assessment_binding` là JSON tuple do `assessmentBinding` trong CHECK005 tạo từ chính đánh giá; đổi bằng chứng/phiên/revision thì chữ ký không còn khớp. Không tin tên người rà tự điền làm quyền máy chủ: đây vẫn là HOST_CHECK; Reviewer tự ghi phiếu qua đường có quyền. Máy chỉ kiểm hợp đồng, không tự kết luận căn cứ nghiệp vụ đúng.

Luật này áp cho cả nhánh riêng và nghĩa vụ có điều kiện nằm trong bước gộp. Nghĩa vụ LUÔN không được dùng NA. UI chỉ thu nhánh có đánh giá hợp lệ; thiếu rà hoặc không khớp thì hiện Chưa xác định. KPI số đánh giá tay lấy từ các đánh giá thực có execution_mode=MANUAL_ASSISTED (kể cả trong obligation_checks), không khai trước. Cấm lấy không có issue làm bằng chứng không phát sinh.

Tạo binding bằng DOT hiện có: `node check-work-masters.js view.html --assessment-binding input.json`, trong đó input có `dossier` và `assessment`. Bộ kiểm trả `manual_assessments` để đo KPI từ dữ kiện thực, không nhập tay con số.

Field: trước khi thêm, đối chiếu key/type/validation. Nếu nhóm có nhiều định nghĩa, `collision_decisions` phải có quyết địnhKEEP với đủ chính xác cácID hiện hành, lý do theo nghĩa và người quyết. MERGE giữ bảngIDcũ→mới, nhãn theo nơi dùng. ThêmID vào nhóm mà chưa cập nhật quyết định thì bộ kiểm chặn. Quyết định hiện hành nằm trong MasterField, không mở Master mới.
