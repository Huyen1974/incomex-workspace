# PR15 — Rà P31: còn kiểm chặng trả cuối và dữ liệu thực bên trong

TQT-PROPOSAL: TQT-PR-20261012-gptchat-p31-final-boundaries-15
TARGET: MOW-TH-005 / CAT-206* schema 1.2-design / hợp đồng MOW001-G1 phiên 2.
ROLE: GPT Chat — phản biện theo Owner; Astra Codex giữ Host nội dung, Claude giữ Host Kiểm soát.
DECISION: REQUEST_CHANGES tại các ranh giới dưới; giữ ⑤, 7 mốc, các Master và DOT hiện hữu.
SCOPE: Chỉ đọc/kiểm bản sao và tệp TEST trong snapshot. Không sửa nguồn chính, application_D24, Master, PG hay runtime VPS. File này là đề xuất duy nhất.

## 1. Kết luận để Host xử lý

P31 đã sửa thật các lỗi PR14 chủ yếu: thiếu scope bị chặn ở P01–P05; bỏ PRODUCT_SPEC, sai kiểu/đích/đối tượng bị chặn; mất kết quả P01 không qua CP02; xóa lịch sử/checkpoint/dòng kiểm bị chặn; fixture tự mang dấu PASS nhưng không có trust ngoài hồ sơ không được vào CP03. Không yêu cầu làm lại các phần này.

Còn 4 nhóm cần chốt: **(1) gói cuối 1.3→CALLER chưa được kiểm kiểu/phiên/người nhận; (2) đánh giá bên trong phản hồi có thể thuộc phiên cũ; (3) P02/P03 mới có kiểm vỏ giao nhận, chưa chứng minh đọc và kiểm nội dung thiết kế; (4) lát thử tệp chưa phục hồi được khi tiến trình chết hoặc ghi nhật ký thất bại.** Hai nhóm đầu là lỗi kiểm cấu trúc/liên kết hiện hữu; nhóm 3 là khoảng trống nghiệm thu nội dung; nhóm 4 là lỗi trong cơ chế thử, không phải bằng chứng production đã hỏng.

## 2. Điểm còn hở và cách kiểm lại

### R15-01 — Chặng trả 1.3 → CALLER bỏ qua kiểm payload

`mapProductHandoff` chỉ gọi `productInputAudit` khi `to !== 'CALLER'`. Nhánh trả cuối chỉ kiểm các khóa có xuất hiện, không kiểm giá trị hay đối chiếu người gọi.

Đã tái hiện trực tiếp trên hàm gốc, không sửa schema/luật:
- Gán toàn bộ giá trị của gói trả về thành null: mapper trả PASS.
- conclusion=UNDEFINED, generatedAt=yesterday: PASS.
- requestId/revision và return_to.caller trỏ sang người/lần khác: PASS.
- Đối chứng: xóa hẳn khóa requestId (undefined) bị chặn đúng.
- Mapping hiện làm rơi retrievalStatus và retrievedAt dù đặc tả đầu ra MOT1.3 khai hai trường đó bắt buộc. Nếu đích CALLER chủ ý chỉ nhận một phép chiếu rút gọn, phải khai hợp đồng nhận tương ứng; không tự làm rơi.

**Sửa tại nguồn CAT-206*/bộ kiểm đang có:** khai schema phía CALLER, kiểm gói cuối theo schema + so requestId/revision/return_to/phạm vi với ngữ cảnh gốc trước gửi. Giữ cùng mẫu cho cả kết quả thường và hủy; không thêm Master/hàm điều phối mới. Thêm ca: đủ khóa nhưng null/sai kiểu/sai người/sai phiên phải FAIL; một gói đúng phải PASS.

Không suy các PASS này thành đã vượt CP07 của MOW001. Đây là lỗ hở của hàm ghép gói PRODUCT_SPEC, khác ACK nghiệm thu của QTTH05.

### R15-02 — Vỏ phản hồi đúng phiên, đánh giá bên trong vẫn có thể cũ

Cho request.revision=2, response.revision=2, nhưng response.evaluation.requestRevision=1: `tqtProductInputAudit(R,'1.3',payload)` trả PASS. Đặt một candidate có evaluation green nhưng requestRevision=1 cũng PASS. Đối chứng: đổi response.revision ngoài thành 1 bị chặn.

**Sửa:** trước khi dùng đánh giá để kết luận, kiểm revision của đánh giá tổng và từng candidate với yêu cầu hiện tại; đồng thời kiểm phiên luật/nguồn theo hợp đồng đã chốt. Cũ thì vô hiệu hóa đánh giá và yêu cầu kiểm lại, không tái dùng green cũ. Nếu helper này chỉ kiểm hình thức, phải có một chốt bắt buộc khác trước kết luận — hiện chưa thấy trong đường mapping vừa thử.

### R15-03 — Cần chứng minh nội dung thiết kế sau P01, không chỉ phong bì giao nhận

P01 đã kiểm `data.answers` và nguồn thật. P02–P05 lại dùng schema `handoff`, chỉ yêu cầu metadata như ID/phiên/scope/output_ref. Fixture gốc có kết quả P02/P03 không chứa design_spec hay dữ liệu thiết kế; `output_ref=test-only:output`, vẫn kiểm payload PASS và mô phỏng đủ 7 mốc khi có ngữ cảnh trust TEST.

Đây **không phải** vượt quyền production: fixture chủ ý dùng chứng cứ giả lập và không qua CP03 khi bỏ trust TEST. Nhưng lát thử P01→P02 chưa chứng minh AI kế tiếp đọc được sản phẩm thiết kế P02/P03 theo CAT-206*.

**Bổ sung bằng chứng, không bắt nhét cả sản phẩm vào mọi gói:** chọn một trong hai cách sẵn có: payload chứa dữ liệu đặc tả theo schema, hoặc output_ref trỏ bản đặc tả được bên nhận thực sự mở/đọc và kiểm cùng ID/phiên/hash. Chốt đủ trường/điều khiển/trạng thái/nhánh theo đúng hợp đồng của 3 MOT. Phiếu kiểm P04 phải bám nội dung vừa đọc. Tệp thiếu, đặc tả rỗng/thiếu hoặc khác phiên phải bị chặn trước nghiệm thu.

Probe phụ: payload P03 actor=NOT_ASSIGNED vẫn được hàm payload nhận. Quyền tác giả thật phải được adapter/cửa ghi kiểm theo người được giao, không lấy trường tên tự khai thay danh tính; phần này liên quan giới hạn trust Codex đã ghi còn mở.

### R15-04 — Lát thử giao–nhận cần kiểm chết giữa chừng

Hai phép tiêm lỗi thực trong thư mục TEST, dùng nguyên `check-record-control.js --test-handoff`:
1. Consumer bị SIGKILL ngay sau khi tạo receive.lock. Lần đọc tiếp trả CONCURRENT_WRITE, khóa vẫn tồn tại, effect_count=0. Khóa không được giải phóng khi tiến trình chết; chưa có đường tự phục hồi trong lát thử này.
2. Cho ghi state thành công nhưng `appendFileSync(events.jsonl)` lỗi. Consumer trả BLOCKED, nhưng state đã có 1 tác động. Retry trả ACK/replayed và không thêm tác động (đúng), song events.jsonl vẫn không tồn tại: nhật ký nhận không được ghi bù.

**Sửa/kiểm trong DOT hiện hữu:** dùng lại cơ chế khóa/giao dịch hoặc journal khôi phục đã có; khóa không được để treo khi process chết, và trạng thái/kết quả nhận phải có sự kiện bền vững có thể khôi phục. Không tạo watcher mới hay gate chờ giờ. Thử lại đúng hai điểm ngắt trên, chứng minh vừa không nhân tác động vừa không mất nhật ký. Không dùng ca gửi trùng bình thường thay ca chết giữa chừng.

## 3. Kết quả chạy bộ kiểm — tách đúng môi trường

- Nguồn pin `d50fa0933cfa3b08ee624089d8d00f96d268774e`; view.html SHA256 `aac3f7f788ed33a239d03ab37af037f42e53d23886660cf897a8bbaa9890607b`, trước/sau không đổi. check-record-control.js SHA256 `9911b11b6a2f3602989d96dc9d80c6420a1e6b338d09f43acc8616caaf39cf9e`.
- Registry UI thật SHA256 `749ac49022b00a0cd901cd353a790e5b803ed19d6ca5737cbba9079c2da7756c`, đã so với workspace_stat trước khi dùng bản đọc vào snapshot.
- Node 22.16.0 giải nén tạm trong snapshot, SHA256 archive `f4cb75bb036f0d0eddf6b79d9596df1aaab9ddccd6a20bf489be5abe9467e84e` khớp manifest chính thức; tự xóa. **Không cài Node lên runtime VPS**.
- Runner nguyên bản không có registry live trả BLOCKED đúng. Có registry, CHECK-001/002/003/005 exit0; CHECK-004 không hoàn thành trong hạn runner 60 giây nên kết quả chung FAIL. Chạy riêng CHECK-004 với hạn đủ: **PASS, 91,94 giây** ở snapshot này; các nhóm 26 cơ bản, bộ đếm hồi quy lũy kế 59, 15 kho thử, 44 hợp đồng P29, 48 ranh giới PR14, 9 đầu vào sản phẩm, 8 mapping, 17 giao nhận tệp. Không cộng các bộ đếm lũy kế thành tổng ca độc lập.
- Vì vậy: các suite mã chạy riêng đều đạt, nhưng **chưa tái lập PASS qua chính runner hiện hành ở môi trường này**. Đây là vấn đề điều kiện chạy/giới hạn thời gian, không phải 004 báo lỗi logic cũ. Cần đo/tối ưu hoặc bố trí ngân sách kiểm phù hợp, không tự tăng chờ vô hạn.
- 27 probe độc lập về hợp đồng/dữ liệu, gồm các đối chứng; thêm 2 phép tiêm lỗi giao nhận tệp. Không có mutation ở nguồn. MOW001 thật vẫn 13 mục khai, 0 đối chiếu, 0/7 mốc.

### Định danh bằng chứng có thể đọc lại

| Lượt | Job ID | Kết quả |
|---|---|---|
| Runner + 27 probe | 6081dff415154967ae8754e79ba0e026 | exit0 của lượt review; runner FAIL/004 hạn 60s; probe chạy thành công |
| Chết sau lock / lỗi ghi sự kiện | 1c8ec1488d6d420d9fe8ca4dd4cf2c78 | exit0; tái hiện hai điểm phục hồi còn thiếu |
| Chạy riêng CHECK-004 | 56b0d30d5d8b4ae883e8a0e9e9075a20 | exit0, PASS 91,94s |

stdout SHA256 tương ứng: `aacd3326449d503799dbaef4a5cb4f3b3637346fc22ed5b4867b1b90326f2e3f`; `bc517076e7c8ed0f241c3345ab24275850eb42a5e952cdca7d7f206f9a2af2df`; `927f588a5e0c647d5fa81ded62ac08cc2a1e0b27abf970dc0f624648edfb0173`.

## 4. Thứ tự ngắn để đi tiếp

Giữ khung hiện tại. Bịt R15-01/02 trong hợp đồng sản phẩm; mở rộng ca đọc–ghi từ P01 tới nội dung thiết kế P02/P03 (R15-03); thêm hai ca phục hồi R15-04 và làm runner chạy hết được. Sau đó xác minh quyền nơi lưu và người kiểm độc lập thật theo các cổng còn mở rồi mới xét CP03. Không tự đánh dấu đã chạy PG, không thêm QTTH06, không mở thêm Master hay sổ.

Nguyên tắc nghiệm thu không đổi: **bước trước giao đúng dữ liệu; bước sau đọc đúng dữ liệu đó, đúng phiên/người; sai thì chặn đúng chỗ và giữ đủ dấu vết**. Host Codex tiếp nhận từng R15, Claude phản biện khác hãng; không tự coi PR15 là duyệt thay Owner/quorum.
