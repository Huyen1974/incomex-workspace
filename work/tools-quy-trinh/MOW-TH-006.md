# QTTH 006 — Quy trình thực hiện QTTH 05

**Mã quy trình:** `MOW-TH-006` · **Tên:** Quy trình thực hiện QTTH 05. Đây là **một quy trình**, không phải loại đối tượng “hướng dẫn” riêng.
**Phiên:** `0.2-reviewed-draft` · **Ngày rà:** 13/10/2026 · **Trạng thái:** ĐÃ RÀ THEO QTTH 05 / HỒ SƠ MOW001 G1, **CHỜ HOST CODEX XÁC MINH VÀ NGHIỆM THU**. Không tuyên bố đã đăng ký 006 trong Master quy trình tổng hợp hoặc đã chạy thực theo 006.
**Nguồn:** tệp này là bản thiết kế quy trình đang rà. Bản v0.1 có **100 bước** được lưu trong lịch sử Git; PR20 giữ bảng đối chiếu đầy đủ 100 mã cũ. Không đổi tiến độ MOW001/P37/P38.

## 1. Nguyên tắc chính

**QTTH 05** quy định bảy checkpoint; **QTTH 06** triển khai thao tác chi tiết để hoàn thành checkpoint đó. Không ép một số lượng bước. Bản này có **85 bước**, kết quả của rà gộp/tránh trùng, chuyển thứ tự và bổ sung chỗ thiếu; sửa đúng nội dung thì số bước được thay theo phiên.

Một **bước nguyên tử** phải có: một hành động có thể giao một bên thực hiện, một đầu ra/biên nhận có thể kiểm, một nơi ghi và điều kiện đạt/rẽ nhánh. Bước lặp trên nhiều MOT/field/plan/case vẫn là **một định nghĩa**, khi thực hiện sinh bản áp dụng theo `item_key`. Bước có quyền hoặc bên nhận khác phải tách riêng. Không hiểu “độc lập” là bỏ quan hệ trước–sau: `step_id`, `depends_on` và `return_to` vẫn bắt buộc khi có phụ thuộc.

### Hai tầng, một hồ sơ

- **Tầng định nghĩa**: danh sách bước QTTH 006 theo phiên; **không chứa kết quả của MOW001 hoặc việc khác**. `MOW-TH-005` tiếp tục là 7 mốc và 6 MOT nguồn, 006 không tự gọi 006 thành vòng lặp hay chen vào `selected_process` của 005.
- **Tầng áp dụng**: hồ sơ việc trên `DEF 00.1 / CAT-227*` ghim đúng `MOW-TH-006@process_version`; hiển thị toàn bộ bước áp dụng (cùng nhóm theo CP của 005), chỉ lưu **trạng thái, bằng chứng, ngoại lệ và thay đổi** theo `application_id + process_version + target_version + step_id + item_key + revision` ở **sổ hiện có**. Không sao chép một danh sách có thể sửa độc lập, không tạo Master “tiến độ QTTH 006” thứ hai.
- **Tình trạng**: `Trống` / `Hoàn thành` / `Vướng`. Đây là trạng thái thực của bước áp dụng; bảng chung bên dưới chỉ dùng “Trống” làm mẫu. `Hoàn thành` đòi đúng nguồn, quyền, phiên, readback và đối chiếu, không lấy dấu đã qua CP05 tự phủ sang các bước 006 chưa có biên nhận.

### Điều chỉnh (+/−) của một hồ sơ cụ thể

Cột **“Điều chỉnh (+/−)”** thay tên cột checkbox “Việc bổ sung” để theo dõi đầy đủ **thêm và không dùng**:

| Hiển thị ở hồ sơ | Khi nào dùng | Ảnh hưởng tiến độ |
| --- | --- | --- |
| **— Theo chuẩn** | Bước chuẩn bắt buộc hoặc bước chuẩn đủ điều kiện áp dụng | Phải có kết quả/biên nhận mới tính Hoàn thành. |
| **☑ + Bổ sung** | Phát sinh việc riêng cần chèn sau bước chuẩn, mã ví dụ `006.CP02.08+B01`; khai `parent_step_id`, `position_after`, mã/tên Master đích, người làm, `depends_on`, đầu ra, điều kiện xong, bằng chứng phê duyệt. | Sau khi phê duyệt trở thành bước **phải làm** đúng mốc; không tự cộng thành hoàn thành. |
| **☑ − Không áp dụng** | Điều kiện nhánh không xảy ra hoặc phạm vi việc loại trừ có căn cứ; khai `condition_ref`, `reason`, `approved_by` khi cần và bản nguồn. | Loại khỏi mẫu số **các bước đến hạn phải làm**, vẫn hiện dòng và lịch sử để sau cải tiến. Không đánh dấu Hoàn thành giả. |
| **☑ ↔ Thay thế** | Một bước chuẩn được thay bằng bước đặc thù đã có phép; giữ bản gốc và `replaced_by_step_id` để truy vết. | Bước thay thế có nghĩa vụ hoàn thành; bước gốc không bị xóa. Nếu chạm lõi/luật chung phải hiệu chỉnh theo MOW-TH-003. |

**Bước lõi của 005 không được bỏ tùy ý.** Nếu N/A làm mất đầu vào, quyền, kiểm, duyệt hoặc ACK bắt buộc thì CP tương ứng phải **Vướng** cho tới khi thay đổi hợp đồng/phạm vi hợp lệ. Nhánh không phát sinh phải có lý do “điều kiện không xảy ra”; *chưa đánh giá được điều kiện* khác với *không áp dụng*. Điều chỉnh chỉ xảy ra ở hồ sơ cụ thể; nếu +/− lặp lại nhiều lần, tập hợp tín hiệu để đề xuất sửa 006@phiên mới theo QTTH 003, không tự thay nguồn chuẩn.

### Sổ/Tool và khi bị lỗi

Cột “Nơi ghi kết quả” chỉ **Master ghi bằng chứng hoặc kết quả của thao tác**, không phải chỉ nguồn tra cứu. Ví dụ: *tra MOW* là đọc `ML-DEF-004/005`, nhưng **ghi lựa chọn MOW/MOT vào hồ sơ DEF 00.1**; không tự sửa Master MOW khi chỉ tra.

Cần luôn chỉ **mã và tên Master** thực, kể cả sổ thiếu/sai (`CAT-069?` hiện là mã thiết kế có dấu ?, Host phải xác minh alias/đường ghi trước khi đưa vào dùng rộng). Tool có mã trong Master DOT/Tool nhưng **chưa đủ quyền hoặc chỉ là thiết kế** không coi đã chạy. Tham chiếu quy trình xử lý sai `MOW-TH-002` hoặc hiệu chỉnh `MOW-TH-003` thuộc quy trình, **không phải Tool**. Khi lỗi: ghi `issue_ref, owner, next_action, return_to`, không xóa checkpoint cũ không bị ảnh hưởng.

### Khớp với MOW001 đã thực hiện

MOW001 G1 đã 7/7 theo QTTH05 ở P37; P38 đã giảm trùng lịch sử mà giữ bằng chứng. **P01 chuẩn bị phải tạo trước khi CP03 nhận/kiểm**, không được sinh đầu tiên ở CP04. P02/P03 là sản phẩm lúc Làm, P04 là kiểm, P05 kết thúc duyệt và bàn giao. Hồ sơ MOW001 **chưa chạy QTTH 006 phiên 0.2**, không đánh 85/85 theo suy đoán. Tình trạng G2/G3/PG vẫn giữ riêng. QTTH 06 dùng được cho loại việc khác MOW; trường G1/G2/G3 và các ca UI chỉ áp dụng khi đúng loại việc.

## 2. Bảng bước 85 thao tác, mở/thu theo 7 mốc QTTH 05

**Các cột “Trống” và “—” dưới đây là giá trị MẪU** cho phiên quy trình, không phải trạng thái của một hồ sơ. Các nhánh có `KHI(...)` chỉ sinh nghĩa vụ khi điều kiện tương ứng xảy ra. Cách đánh số thứ tự chỉ phục vụ hiển thị; **mã bước có cả phiên + checkpoint** để không tái sử dụng mã 006-023 cũ với nghĩa khác.

<details>
<summary><strong>CP01 · Khai việc · 12 bước</strong> (mở/thu)</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (Master mã + tên) | Tool use (nếu có) | Tình trạng | Điều chỉnh (+/−) | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **01 · CP01.01** | Đọc nguyên yêu cầu Owner và điều không được làm | Có mục tiêu/người giao/nguồn rõ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | — | LUÔN · Không tự thay ý Owner |
| **02 · CP01.02** | Đối chiếu A0, xác nhận phạm vi và quyền Owner | Có phạm vi được xác nhận | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | — | LUÔN · Lời tiếp tục không là duyệt |
| **03 · CP01.03** | Tra mã và mục tiêu của việc đã có trước khi mở | Không tạo hồ sơ trùng | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-005 · Kiểm Master | Trống | — | LUÔN · Tìm bằng mã |
| **04 · CP01.04** | Ghi mã việc, người giữ và nguồn yêu cầu | Hồ sơ mở được đúng ID | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | — | LUÔN · Một hồ sơ việc |
| **05 · CP01.05** | Ghim bộ quy trình QTTH 05/06 đúng phiên vào hồ sơ | Hồ sơ trỏ 005@version và 006@version; không có vòng gọi 006 | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-002 · Kiểm mã | Trống | — | LUÔN · 005 có 6 MOT và 7 checkpoint hiển thị; 006 là tầng thao tác, không thay selected_process. |
| **06 · CP01.06** | Đối chiếu đối tượng công việc và các đối tượng con theo nguồn chuẩn | Đúng mã/phiên/quan hệ con; với MOW tra đúng MOW/MOT, loại khác tra Master đối tượng tương ứng | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-005 · Kiểm Master | Trống | — | LUÔN · Nguồn tra cứu: ML-DEF-004 Master MOW / ML-DEF-005 Master MOT chỉ khi việc thuộc MOW; hồ sơ phải ghi đúng mã+tên Master loại khác. |
| **07 · CP01.07** | Chốt loại sản phẩm, phạm vi/giai đoạn và các phần loại trừ | Có một phạm vi được xác nhận gồm sản phẩm, các nhánh ngoài phạm vi và điều kiện mở lại | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | — | LUÔN · Không buộc G1/G2/G3 nếu việc không phải xây một sản phẩm dạng này. |
| **08 · CP01.08** | Gắn link và phiên nguồn đầu vào được phép đọc | Có dữ liệu nguồn truy được | DEF 00.1 · Master tiến trình công việc (CAT-227*) | MCP workspace_read/stat (có quyền) | Trống | — | LUÔN · Đây là nơi ghi liên kết nguồn; hợp đồng chi tiết sẽ lưu CAT-206* ở CP02. |
| **09 · CP01.09** | Khai người nhận cuối, nơi gọi và nơi trả | Đúng đích bàn giao | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | — | LUÔN · Caller có thể khác recipient |
| **10 · CP01.10** | Khai người làm, người kiểm, người duyệt | Vai trò/quyền có căn cứ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | — | LUÔN · Không giả quorum |
| **11 · CP01.11** | Gắn mốc QTTH 05 và bản định nghĩa QTTH 006 với hồ sơ việc | Có 7 mốc, mã/phiên 006 và mã hồ sơ; chưa tự tô bước thực hiện | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-001 · Kiểm mô hình | Trống | — | LUÔN · Hồ sơ áp dụng bước 006 theo version; không chép 100 dòng vào mỗi nguồn nhập. |
| **12 · CP01.12** | Đối chiếu kết quả khai việc với CP01 của QTTH 05 | Mốc CP01 được kiểm từ hồ sơ nguồn hoặc có Vướng/owner/return_to | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm bản ghi/mốc | Trống | — | LUÔN · Bước này kiểm gate, không tự đánh dấu bằng nút giao diện |

</details>

<details>
<summary><strong>CP02 · Chuẩn bị đủ · 22 bước</strong> (mở/thu)</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (Master mã + tên) | Tool use (nếu có) | Tình trạng | Điều chỉnh (+/−) | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **13 · CP02.01** | Nạp câu hỏi bắt buộc theo MOW/MOT/phạm vi | Đủ bộ câu liên quan | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | Trống | — | KHI(quy trình có bộ câu hỏi) · Bộ câu hỏi của MOW001 không phải yêu cầu mặc định cho mọi việc. |
| **14 · CP02.02** | Ghi đáp án, mã câu, người và nguồn | Có đáp án hoặc ghi thiếu | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | — | KHI(có câu hỏi áp dụng) · Lặp theo item_key=câu hỏi, không tạo một bước định nghĩa mới cho từng câu. |
| **15 · CP02.03** | Ghim nguồn và hash bằng chứng đầu vào | Đọc lại đúng phiên | CAT-239* · Master tệp/bằng chứng | MCP workspace_read/stat (có quyền) | Trống | — | KHI(có nguồn/bằng chứng để dẫn) · Cần nguồn/hash thật; không tạo bản sao dư. |
| **16 · CP02.04** | Kiểm quyền đọc dữ liệu từ nguồn thật | Có bằng chứng quyền | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Kiểm nguồn và quyền đọc trước dùng; biên nhận ghi vào CAT-015, không chỉnh hợp đồng khi đang kiểm. |
| **17 · CP02.05** | Tra và gắn Master đích cho mọi nghĩa vụ ghi của việc | Mỗi loại thông tin có mã+tên sổ, item_key hoặc issue nếu chưa xác minh | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-005 · Kiểm Master | Trống | — | LUÔN · Bước này không ghi kết quả kiểm vào Master được tra; chỉ gắn link tới nó. |
| **18 · CP02.06** | Lập hợp đồng CAT-206* và ghim MOW/MOT/quy trình/luật theo phiên | Có ID, contract_version, phụ thuộc và nguồn luật xác minh được | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Lập hợp đồng một lần theo scope; đổi nguồn tăng phiên và kiểm lại. |
| **19 · CP02.07** | Định nghĩa từng trường thông tin: nghĩa, kiểu, đơn vị, required_when và số lượng | Mỗi field có schema đủ nghĩa/type/unit/nullable/cardinality/miền giá trị; ca sai bị chặn | CAT-206* · Master hợp đồng đầu vào/đầu ra | — | Trống | — | LUÔN · Một bước chuẩn dùng lại cho mỗi field với item_key, không ép năm bước thủ công lặp thông tin. |
| **20 · CP02.08** | Ánh xạ Master/cột nguồn sang Master/cột đích và chuyển đổi | Có nguồn–đích thực, đúng loại/phiên và phép biến đổi rõ | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Không chấp nhận đường dẫn có chữ nhưng không tồn tại. |
| **21 · CP02.09** | Liệt kê trường bắt buộc của gói đầu ra | Bên giao kiểm được payload | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | KHI(có gói dữ liệu đầu ra) · Gói giao phải có schema nguồn thật, đúng phạm vi. |
| **22 · CP02.10** | Liệt kê trường phải nhận và người nhận | Bên nhận đủ đầu vào | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm giao–nhận | Trống | — | KHI(có gói dữ liệu đầu vào cho bước sau) · Bên nhận phải đọc payload thật và hiểu đúng identity/ACK. |
| **23 · CP02.11** | Khai nhánh lỗi/thiếu/hủy/không quyền | Có điều kiện và đường xử lý | CAT-206* · Master hợp đồng đầu vào/đầu ra | TOOL-CTCM-003 · Phủ nhánh (nếu dùng được) | Trống | — | KHI(quy trình có nhánh) · Khai điều kiện ngay từ thiết kế, không tạo bản ghi lỗi giả. |
| **24 · CP02.12** | Lập một bộ ca nghiệm thu gồm ca đúng, sai, rỗng, sai phiên, sai người nhận | CAT-012 có ca bắt buộc và expected theo contract/phiên đã chốt | CAT-012 · Danh mục bộ kiểm/ca thử | TOOL-CTCM-005 · Rà dữ liệu/lỗi (nếu dùng được) | Trống | — | LUÔN · Chỉ lập bộ ca một lần; CP05 phải thực thi các ca này, không khai lại. |
| **25 · CP02.13** | Đối chiếu các giao điểm giữa MOT | Không còn cạnh phải đoán | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-002 · Kiểm mã | Trống | — | KHI(có nhiều bước giao nhận) · Đây là kết quả kiểm các cạnh từ CAT-206*, không sửa contract bằng dấu PASS. |
| **26 · CP02.14** | Liệt kê tất cả thông tin/bằng chứng phải ghi | Không mất nghĩa vụ bắt buộc | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Nhánh không tới hạn thì không ép |
| **27 · CP02.15** | Phân biệt sổ thiếu, chưa ghi, chưa có quyền | Có issue với từng thiếu sót | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-005 · Kiểm Master | Trống | — | LUÔN · Thiếu sổ/thiếu bản ghi/thiếu quyền là ba trường hợp khác nhau; nếu lỗi mở CAT-069?. |
| **28 · CP02.16** | Xác định các bước QTTH 006 áp dụng cho hồ sơ và từng item_key | Ghim 006@version, phân loại lõi/điều kiện theo từng plan_id/MOT/field và biết bước đến hạn | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm hồ sơ | Trống | — | LUÔN · Bản định nghĩa chỉ lưu một lần; từng hồ sơ lưu phiếu áp dụng/ngoại lệ |
| **29 · CP02.17** | Rà bước thêm, không áp dụng hoặc thay thế trước khi xác nhận kế hoạch | Mọi +/−/↔ có lý do, người kiểm, điều kiện xong, Master đích; không bỏ bước lõi không có phép | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm nghĩa vụ | Trống | — | KHI(có nhánh điều kiện/điều chỉnh) · Bước không áp dụng không tự là Hoàn thành; bước thêm được tính là nghĩa vụ bắt buộc khi đã duyệt |
| **30 · CP02.18** | Lập kế hoạch các việc con có phụ thuộc, người nhận và thứ tự rõ | Có P01…Pn hoặc tương đương, không vòng phụ thuộc | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-001 · Kiểm mô hình | Trống | — | LUÔN · Không cố định năm việc con hay ép ca nhỏ chạy mọi bước. |
| **31 · CP02.19** | Giao actor/reviewer/recipient cho từng việc con | Mọi việc tới hạn có người | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | — | LUÔN · Chưa phân công là Vướng |
| **32 · CP02.20** | Chỉ đích danh đầu ra thật và nơi ghi của từng việc con | Mỗi plan_id có expected_output, Master mã+tên, product_key và tiêu chí đọc lại | CAT-228* · Sổ việc thật MOT/kết quả | TOOL-CTCM-001 · Lập hành trình (nếu dùng được) | Trống | — | LUÔN · Dòng kế hoạch chưa phải kết quả sản phẩm. |
| **33 · CP02.21** | Tạo và ghi gói chuẩn bị P01 hoặc đầu ra chuẩn bị tương đương | Có sản phẩm chuẩn bị thật, đúng contract và nguồn; đọc lại trước CP03 | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 --read-preparation | Trống | — | KHI(quy trình có bước chuẩn bị P01/tương đương) · BƯỚC ĐƯỢC CHUYỂN TỪ CP04 VỀ CP02; tạo trước khi kiểm CP03. |
| **34 · CP02.22** | Chạy kiểm chuẩn bị của checkpoint 2 | Đạt CP02 hoặc ghi Vướng rõ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | Trống | — | LUÔN · Không PASS vì ô có chữ |

</details>

<details>
<summary><strong>CP03 · Xác nhận bắt đầu · 11 bước</strong> (mở/thu)</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (Master mã + tên) | Tool use (nếu có) | Tình trạng | Điều chỉnh (+/−) | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **35 · CP03.01** | Tra và kiểm tính sẵn sàng của Tool/DOT sẽ dùng | Mỗi tool có ID/phiên/hash, nguồn, quyền và ca gần nhất, hoặc phương án làm tay | CAT-229* · Sổ lượt thực hiện/thử | TQT-CHECK-006 · Chạy tổng | Trống | — | KHI(kế hoạch có Tool/DOT) · Tra nguồn ML-DEF-024 Master DOT, ML-DEF-023 Master Tool; không chạy chỉ vì có tên. |
| **36 · CP03.02** | Xác thực người làm qua quyền ngoài hồ sơ | Có quyền thực, không tự khai | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Phân vai đúng người |
| **37 · CP03.03** | Kiểm lại reviewer đã được phân công và quyền kiểm | Đúng người/phiên và mức độc lập theo quy định | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | Trống | — | KHI(cần người kiểm) · Không phân công reviewer mới trùng với bước phân vai ở CP01. |
| **38 · CP03.04** | Rà xác nhận kế hoạch đúng bản/phiên | Kế hoạch đủ quyền/đầu ra | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | Trống | — | LUÔN · Không dùng plan cũ |
| **39 · CP03.05** | Rà độc lập trường/nguồn/đích hợp đồng | Có kết luận đúng contract phiên | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | KHI(cần review độc lập theo quy tắc) · Đây là kết quả review hợp đồng, không phải sửa CAT-206*. |
| **40 · CP03.06** | Kiểm schema/khóa/đường nơi lưu vật lý | Địa chỉ ghi có thật | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · UI mock không là kho |
| **41 · CP03.07** | Thử ghi rồi đọc lại bằng quyền cho phép | Có biên nhận readback | CAT-229* · Master lượt làm/thử | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | KHI(có nơi ghi cần thử ghi–đọc) · TEST chỉ kiểm quyền và schema; không thay kết quả nghiệp vụ. |
| **42 · CP03.08** | Bên nhận độc lập đọc và đối chiếu kết quả chuẩn bị P01 hoặc tương đương | P01/tương đương đã được tạo trước CP03; đọc đúng schema/phiên/hash | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 --read-preparation | Trống | — | KHI(có gói chuẩn bị) · Gộp kiểm nhận lặp từ bước cũ 058; cấm tới CP03 nếu chưa tạo kết quả chuẩn bị. |
| **43 · CP03.09** | Giải quyết issue đang chặn bắt đầu | Không còn blocker CP03 | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | TQT-CHECK-003 · Kiểm khai | Trống | — | KHI(có issue chặn CP03) · Không có blocker thì đánh − Không áp dụng, không tạo issue giả. |
| **44 · CP03.10** | Ghi xác nhận bắt đầu đúng người và phiên | Có quyết định và căn cứ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Không tự chuyển CONFIRMED |
| **45 · CP03.11** | Tính lại CP01–03 trước khi vào làm | CP03 đạt bằng chứng | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Chưa đạt thì dừng |

</details>

<details>
<summary><strong>CP04 · Làm theo quy trình · 19 bước</strong> (mở/thu)</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (Master mã + tên) | Tool use (nếu có) | Tình trạng | Điều chỉnh (+/−) | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **46 · CP04.01** | Chọn việc con có đủ các phụ thuộc trước | Biết đúng việc đến lượt | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-001 · Kiểm mô hình | Trống | — | LUÔN · Song song cần có căn cứ |
| **47 · CP04.02** | Bên thực hiện đọc và kiểm gói đầu vào thật của việc con | Gói hợp lệ theo trường/type/đơn vị/nguồn/phiên trước khi làm | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Một lần đọc+kiểm của bên nhận, ghi theo item_key=plan_id. |
| **48 · CP04.03** | Chọn DOT/Tool đúng phiên hoặc làm tay đúng quy trình | Có cách thực hiện hợp lệ | CAT-229* · Master lượt làm/thử | TQT-CHECK-006 · Chạy tổng | Trống | — | KHI(việc con dùng Tool/DOT) · Tra và xác minh tool của việc con; nếu chỉ làm tay, khai phương pháp. |
| **49 · CP04.04** | Tạo một sản phẩm việc con kèm application_id/plan_id/phiên và hợp đồng | Có sản phẩm thật với đầy đủ identity và output_version | CAT-228* · Sổ việc thật MOT/kết quả | TOOL-CTCM-001 · Lập hành trình (nếu dùng được) | Trống | — | LUÔN · Lặp theo plan_id; định danh là phần của việc tạo một gói sản phẩm. |
| **50 · CP04.05** | Kiểm gói đầu ra theo hợp đồng TRƯỚC khi ghi | Đủ trường và đúng kiểu/scope/nguồn/phiên trước commit | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Sửa thứ tự sai: pre-commit contract check, không đợi ghi rồi mới kiểm. |
| **51 · CP04.06** | Ghi kết quả qua cửa máy chủ được phép | Có biên nhận ghi hợp lệ | CAT-228* · Sổ việc thật MOT/kết quả | MCP workspace_transaction (có quyền) | Trống | — | LUÔN · Không bỏ cửa ghi |
| **52 · CP04.07** | Đọc lại đúng bản vừa ghi và so hash | Nội dung bằng bản gửi | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · HTTP200 không là readback |
| **53 · CP04.08** | Gửi lệnh với idempotency key đúng phiên | Retry không nhân tác động | CAT-238* · Sổ lệnh gửi–nhận–trả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | KHI(có giao nhận cần khóa chống trùng) · Bắt buộc có idempotency key và contract_binding khi phát sinh. |
| **54 · CP04.09** | Bên nhận mở, kiểm gói nhận và xác nhận ACK bước con | Bên nhận kiểm payload đúng schema/phiên rồi mới ACK | CAT-238* · Sổ lệnh gửi–nhận–trả | TQT-CHECK-004 · Kiểm giao–nhận | Trống | — | KHI(có giao nhận giữa bước/đơn vị) · ACK giao bước không thay Owner ACK nghiệm thu cuối. |
| **55 · CP04.10** | Nếu gửi trùng, chặn nhân tác động | Giữ một kết quả hợp lệ | CAT-238* · Sổ lệnh gửi–nhận–trả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | KHI(gửi trùng hoặc retry) · Nhánh không phát sinh phải ghi − Không áp dụng, không tô Hoàn thành. |
| **56 · CP04.11** | Nếu phản hồi cũ, so phiên và từ chối | Không dùng green cũ | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | KHI(phản hồi stale) · Không dùng giá trị green/đánh giá cũ; mở issue. |
| **57 · CP04.12** | Nếu mất quyền, dừng và ghi sự cố | Có người xử lý vấn đề quyền | CAT-017 · Sổ sự cố vận hành | — | Trống | — | KHI(permission_denied) · Ghi CAT-017, không tự nâng quyền. |
| **58 · CP04.13** | Nếu thiếu Master đích, tra lại và ghi issue | Biết sổ/người/bước sửa | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | TQT-CHECK-005 · Kiểm Master | Trống | — | KHI(chưa có sổ/đích ghi đúng) · Ghi CAT-069?, chỉ rõ thiếu sổ khác chưa xác định sổ. |
| **59 · CP04.14** | Nếu dữ liệu sai, gọi QTTH002 giải quyết | Có kết quả sửa được kiểm lại | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | — | Trống | — | KHI(sai dữ liệu/sản phẩm) · Gọi QUY TRÌNH MOW-TH-002 (không là Tool); giữ mốc trước không bị ảnh hưởng. |
| **60 · CP04.15** | Nếu sửa quy trình/hợp đồng, theo QTTH003 | Tăng phiên và giữ lịch sử | CAT-016 · Sổ nhật ký thay đổi định nghĩa | — | Trống | — | KHI(cần sửa quy trình/hợp đồng) · Áp dụng QUY TRÌNH MOW-TH-003; tăng phiên, đánh giá ảnh hưởng. |
| **61 · CP04.16** | Nếu hủy, ghi lý do/phiên/nơi nhận/việc bù | Có bản ghi hủy khi phát sinh | CAT-244* · Sổ hủy và việc bù | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | KHI(hủy/việc bù) · Ghi CAT-244* chỉ khi phát sinh, giữ receipt idempotency. |
| **62 · CP04.17** | Kiểm dấu lịch sử bất biến của lần thực hiện, ghi bù nếu thiếu | Sự kiện/receipt/version được lưu chính xác, không xóa bản cũ | CAT-233* · Sổ sự kiện bản ghi/chống trùng | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Không ghi lại kết quả đã lưu nếu chỉ khôi phục nhật ký. |
| **63 · CP04.18** | Chỉ đóng việc con khi có output_ref thật | Có sản phẩm/bằng chứng đúng | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Plan không phải kết quả |
| **64 · CP04.19** | Chốt CP04 sau khi kiểm đầu ra tới hạn | Mốc làm đạt hoặc báo Vướng | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Không tích tay |

</details>

<details>
<summary><strong>CP05 · Kiểm đầu ra · 9 bước</strong> (mở/thu)</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (Master mã + tên) | Tool use (nếu có) | Tình trạng | Điều chỉnh (+/−) | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **65 · CP05.01** | Nạp bộ ca đã lập từ CP02 theo đúng hợp đồng/phiên | Tập ca áp dụng đủ, không tạo lại ca kiểm | CAT-012 · Danh mục bộ kiểm/ca thử | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Không khai lại các ca đúng/âm/sai phiên ở CP05. |
| **66 · CP05.02** | Reviewer tự mở và xác minh bản sản phẩm cần kiểm | Có log mở đúng ID/phiên/hash và nội dung | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 --read-designs (nếu là bản thiết kế); reader phù hợp loại khác | Trống | — | LUÔN · G1 UI chỉ là một loại sản phẩm; không mặc định mọi việc là thiết kế. |
| **67 · CP05.03** | Chạy ca nghiệm thu đã chốt và ghi actual/expected/reviewer/bằng chứng | Mỗi ca có kết luận và CAT-015 đọc lại được | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Không tách lệnh chạy và ghi kết quả nếu cùng một receipt/tool. |
| **68 · CP05.04** | Nếu là UI, thử nút/trạng thái/nhánh thật | Có bằng chứng UI đúng phiên | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 --check-g1-ui (nếu phù hợp) | Trống | — | KHI(sản phẩm là UI) · Có UI thật mới kiểm giao diện, không lấy test mẫu. |
| **69 · CP05.05** | Kiểm nội dung bản thiết kế từng MOT | Đủ trường/nút/nhánh/luật/hash | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 --read-designs | Trống | — | KHI(sản phẩm là thiết kế) · Kiểm đủ field/state/control/branch/rule_ref theo mã/phiên. |
| **70 · CP05.06** | Kiểm kết quả trả cuối đúng caller/phiên/kiểu | Không trả sai nơi nhận | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | KHI(có trả kết quả cho caller) · Chặng trả cuối phải kiểm giá trị, người nhận, kiểu, thời điểm. |
| **71 · CP05.07** | Nếu G2/G3, kiểm nguồn/evaluator/permission live | Không nhầm demo thành live | CAT-015 · Sổ kết quả kiểm | TOOL-CTCM-005 · Rà dữ liệu/lỗi (nếu dùng được) | Trống | — | KHI(có nguồn hoặc evaluator live trong phạm vi) · Không ép G2/G3 vào nghiệm thu G1 chỉ thiết kế. |
| **72 · CP05.08** | Nếu ca FAIL, ghi issue/người sửa/bước quay | Lỗi có cách khắc phục | CAT-069? · Sổ nhu cầu/góp ý/sai thiếu | — | Trống | — | KHI(ca kiểm FAIL) · Áp dụng MOW-TH-002, ghi CAT-069?, quay về đúng nguồn lỗi. |
| **73 · CP05.09** | Chốt CP05 khi đủ ca và đúng phiên | CP05 đạt hoặc Vướng rõ | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-003 · Kiểm khai | Trống | — | LUÔN · Kỹ thuật không thay Owner |

</details>

<details>
<summary><strong>CP06 · Duyệt kết quả · 5 bước</strong> (mở/thu)</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (Master mã + tên) | Tool use (nếu có) | Tình trạng | Điều chỉnh (+/−) | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **74 · CP06.01** | Gom sản phẩm, phạm vi và kết quả kiểm trình duyệt | Người duyệt mở đúng bản | CAT-025 · Sổ phiếu duyệt/quyết định | TQT-CHECK-005 · Kiểm Master | Trống | — | LUÔN · Không trộn G1/G2/PG |
| **75 · CP06.02** | Xác thực người duyệt/thẩm quyền theo phạm vi | Không dùng worker tự ký | CAT-025 · Sổ phiếu duyệt/quyết định | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Reviewer khác approver |
| **76 · CP06.03** | Xin quyết định đồng ý/từ chối/sửa đúng sản phẩm | Có quyết định rõ ràng | CAT-025 · Sổ phiếu duyệt/quyết định | — | Trống | — | LUÔN · Tiếp tục không là duyệt |
| **77 · CP06.04** | Ghi quyết định kèm product_binding và phiên | Có phiếu duyệt đọc lại được | CAT-025 · Sổ phiếu duyệt/quyết định | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Không giả APPROVED |
| **78 · CP06.05** | Chốt CP06 sau khi so quyết định với sản phẩm | CP06 đạt hoặc quay xử lý | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Kỹ thuật không là Owner |

</details>

<details>
<summary><strong>CP07 · Bàn giao · kết thúc · 7 bước</strong> (mở/thu)</summary>

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (Master mã + tên) | Tool use (nếu có) | Tình trạng | Điều chỉnh (+/−) | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **79 · CP07.01** | Hoàn tất đầu ra P05 hoặc việc con cuối | Có kết quả cuối đúng kế hoạch | CAT-228* · Sổ việc thật MOT/kết quả | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | KHI(kế hoạch có việc bàn giao cuối P05/tương đương) · Không tạo kết quả bàn giao giả nếu quy trình không có việc con ấy. |
| **80 · CP07.02** | Kiểm hợp đồng nhận cuối và nơi trả | Đúng người/sản phẩm/phiên | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm giao–nhận | Trống | — | LUÔN · Duyệt chưa là ACK |
| **81 · CP07.03** | Ghi giao đúng bản, người và nguồn sản phẩm | Có sổ bàn giao thật | CAT-232* · Sổ bàn giao/xác nhận nhận | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Không chỉ gửi link |
| **82 · CP07.04** | Lấy ACK thật từ bên nhận có thẩm quyền | Có biên nhận đúng bản | CAT-232* · Sổ bàn giao/xác nhận nhận | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Iframe không là Owner ACK |
| **83 · CP07.05** | Chạy bộ kiểm tổng đúng phiên khi quy trình hoặc mức rủi ro yêu cầu | Kết quả bộ tổng PASS có hash/biên nhận hoặc quyết định không yêu cầu đã ghi | CAT-015 · Sổ kết quả kiểm | TQT-CHECK-006 · Chạy bộ kiểm tổng | Trống | — | KHI(cần fullsuite theo phạm vi) · Không áp dụng bộ tổng nặng cho việc nhỏ nếu hợp đồng không yêu cầu |
| **84 · CP07.06** | Kiểm liên tục CP01–07 và nghĩa vụ áp dụng | 7/7 với bằng chứng thật | DEF 00.1 · Master tiến trình công việc (CAT-227*) | TQT-CHECK-004 · Kiểm ghi/mốc | Trống | — | LUÔN · Không ép nhánh chưa có |
| **85 · CP07.07** | Ghi bài học, công cụ đã dùng và vấn đề còn mở để dùng lần sau | Có liên kết tool/phiên/kết quả/issue và giới hạn nghiệm thu ở sổ nguồn | CAT-233* · Sổ sự kiện bản ghi/chống trùng | TQT-CHECK-006 · Chạy tổng | Trống | — | KHI(có tool/sự kiện hoặc bài học cần lưu) · Đây là việc sau nghiệm thu, không tự thu hồi CP07 nếu chỉ có ghi chú mới. |

</details>

## 3. Mẫu bước bổ sung và không áp dụng của một hồ sơ

| Bước | AI phải làm gì? | Thế nào là xong? | Nơi ghi kết quả? (Master mã + tên) | Tool use (nếu có) | Tình trạng | Điều chỉnh (+/−) | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `006.CP02.08+B01` · Bổ sung nguồn pháp lý | Đọc và gắn một nguồn còn thiếu đúng phiên vào hợp đồng áp dụng | Có nguồn hợp lệ, kiểm lại được | CAT-206* · Master hợp đồng đầu vào/đầu ra | TQT-CHECK-004 · Kiểm hợp đồng/mốc | Trống | ☑ + Bổ sung | Lý do/actor/nguồn duyệt và đích ghi thuộc **riêng application**; step cha `006.CP02.08`. |
| `006.CP05.04` · Không có UI | Không chạy ca kiểm giao diện vì đầu ra việc này không chứa UI | Có căn cứ loại sản phẩm không có UI | DEF 00.1 · Master tiến trình công việc (CAT-227*) | — | — | ☑ − Không áp dụng | Có `reason=not_ui_product`; bước chuẩn vẫn được giữ để người sau học từ sự khác nhau. |

## 4. Điều kiện trước khi đưa vào chạy và gắn cùng trang QTTH 05

1. **Giao diện:** trên Over view, QTTH 05 là bản đồ bảy mốc; ngay **bên dưới phần chi tiết 005**, QTTH 006 là các nhóm CP01–07 thu/mở. Không để 006 thành một trang rời thay thế. Tổng quan không cho sửa tình trạng.
2. **Hồ sơ DEF 00.1:** với mỗi application ghim 006@version, sinh danh sách bước chuẩn + dòng thêm/N/A/điều chỉnh riêng, đúng thứ tự và item_key. Cùng một hồ sơ là nguồn trạng thái và bằng chứng. Mặc định các bước chưa có biên nhận `Trống`; không hồi tố P37 thành đã làm 006.
3. **Check chuyển mốc:** chỉ tính các bước **đến hạn và áp dụng** cùng nghĩa vụ gốc của 005; không bỏ qua bước lõi nhờ đánh N/A; bước bổ sung có phê duyệt được tính vào CP tương ứng. Khi có vấn đề biết thiếu gì, ai làm, quay bước nào.
4. **Trước khi chuyển Master/PG:** Host Codex phải kiểm tên/mã sổ và quyền ghi thực, chống trùng Master; chọn một SSOT cho step definitions và một nguồn result theo hồ sơ, có kiểm phiên/hash và đồng bộ giao diện; dùng lại CHECK001–006.
5. **Thử với AI mới:** chọn một công việc mới nhỏ và một công việc có biến thể (+/−). AI chỉ đọc 005/006 + hồ sơ và Tool/Master hiện hữu; phải biết làm gì, ghi ở đâu và xử lý lỗi. Chưa có ca này thì phiên 006 chỉ là thiết kế.

**Tác động:** đây là hiệu chỉnh bản thiết kế 006, KHÔNG sửa MOW-TH-005, checkpoint/ứng dụng P37, PG hay Master vật lý. Việc Host nhận vào Master Quy trình tổng hợp và triển khai giao diện là bước tiếp theo có kiểm độc lập.
