# Lệnh giao Codex — làm một mẫu “Tạo một quy trình” cho người mới, rồi dừng để Owner duyệt

**GPT Chat / PM · 12/09/2026**  
**Nguồn:** `BAN-DO-BUOC-UI-AGENT.html` hiện v1.6.20, SSOT và các ảnh/nguồn đã có trong thư mục `/Users/nmhuyen/Desktop/quy trình`.

## 1. Chỉ làm việc này

Tạo **một trang HTML mẫu dễ đọc**, mô tả từ lúc một người muốn tạo quy trình tới lúc bật cho chạy và biết đã có kết quả. Đặt đường thao tác bằng UI cạnh phần AI/công cụ làm thay.

Đây là mẫu để Owner xét **cách trình bày và logic**, không phải xây thêm tính năng hoặc hoàn tất toàn bộ bản đồ. Thay phạm vi mở rộng trước đây bằng lệnh này. Chưa áp cách trình bày mới cho các luồng còn lại.

Giữ nguyên dataset, nguồn, bằng chứng lab và các kết luận có giới hạn. Không gọi 87 bước là đã đầy đủ về nghiệp vụ chỉ vì kiểm đếm thành công. Không yêu cầu Owner đọc kho kỹ thuật để hiểu trang mẫu.

**Đường người làm bằng UI là bản mô tả gốc của mẫu; AI tự động hóa cùng hành động và cùng dữ liệu, không dựng một hệ thống thứ hai.** Làm bằng tay vẫn dùng tìm kiếm, kiểm tra tự động, lưu và phân quyền của hệ thống; không bắt người gõ ID, SQL, JSON hoặc chạy từng tool kỹ thuật.

## 2. Đọc đúng nguồn, không ép đủ 16 dòng

Bắt đầu từ luồng `MOW / Tạo` trong dataset: 16 bước hiện kết thúc ở `publish → readback`. Đối chiếu thêm các bước đã có ở luồng sử dụng: gắn nơi áp dụng, kích hoạt, tín hiệu khởi chạy, nhìn việc/kết quả.

**Ban hành chưa có nghĩa đã bật chạy.** Trang mang mục tiêu “tạo quy trình để chạy” không được dừng ở ban hành rồi coi như hoàn tất. Chỗ chưa có phương án hoặc UI phải hiện rõ.

- 16 bước là mốc nguồn để truy vết, không là chỉ tiêu phải giữ bằng mọi giá.
- Có thể gộp các thao tác kỹ thuật thành một việc người hiểu được; không làm mất nội dung hoặc quyền quyết định.
- Bước tự động như kiểm ngữ cảnh, sinh mã hay chạy bộ test không thành một việc bắt người thao tác riêng.
- Các nội dung chuyển ra khỏi đường chính phải còn trong chỗ mở chi tiết hoặc nhánh có điều kiện. Ghi mapping về ID nguồn ở tầng kỹ thuật.
- Không sửa global dataset hoặc Factory/INV để phù hợp với mẫu. Thiếu hoặc mâu thuẫn mới: ghi đề xuất có nguồn, chưa tự chốt kiến trúc.

Dùng một ví dụ xuyên suốt đã có, ưu tiên “Ghi nhận thời lượng xử lý”. Nêu ví dụ một câu, không thêm nghiệp vụ mới. Đây chỉ là ví dụ làm rõ format, không thay phạm vi toàn hệ.

## 3. Trang người đọc: một luồng, không phải một dashboard

Tên: **“Tạo một quy trình — tôi làm gì, AI làm thay gì?”**

Trang mở thẳng vào hành trình, không bắt chọn trong 12 family, không đặt bảng tool hay số liệu 87/987 lên trước. Có thể dùng 3–4 tiêu đề chặng bằng tiếng Việt để dễ định vị.

Bảng chính chỉ có:

| Bước | Tôi làm gì, xong thấy gì? | Màn hình | Có gì / còn thiếu gì? | AI làm thay gì? |
|---|---|---|---|---|

Quy tắc:
- Mỗi dòng là một việc có ý nghĩa với người: động từ rõ, một câu ngắn; kết quả mong thấy ngay sau đó một câu ngắn nếu cần.
- Nói rõ ai làm nếu chuyển vai: người dựng, người duyệt, người được giao. Không giả định một người có mọi quyền.
- Một ảnh nhỏ đúng vùng thao tác, bấm phóng to được. Không ép toàn trang dài vào một ảnh bé không đọc nổi.
- Mỗi dòng nêu đúng phần thiếu riêng, ví dụ “chưa chọn được ngày bắt đầu”; không lặp “thiếu thông tin” cho mọi bước.
- Không tên bảng, endpoint, mã hợp đồng, G/J/C/R hay thuật ngữ chưa giải thích ở bảng chính.
- Một trang HTML được phép cuộn; không ép 16 dòng và ảnh vào một màn rồi giảm chữ. Kiểm ở 1280×720, cỡ chữ dễ đọc, không cuộn ngang.
- Không thêm bộ lọc, dashboard, chỉ số hoặc tương tác không cần cho việc hiểu mẫu.

Ví dụ về cách viết, **không phải xác nhận UI đã có**:
- Thay “resolve scope/revision” bằng “Mở đúng quy trình đang sửa; tên và bản đang xem hiện ở đầu màn”.
- Thay “validate closure” bằng “Bấm Kiểm tra; xem chỗ nào còn thiếu và cần sửa gì”. Nếu nguồn quy định máy tự kiểm thì viết “Xem kết quả hệ thống tự kiểm”, không bịa thêm nút.
- Thay “binding/activation” bằng “Chọn nơi áp dụng và lúc bắt đầu; xác nhận bật quy trình”.

Chi tiết cho PM/Agent gập ở cuối trang, không gập hàng chục khối chen giữa đường đọc chính.

## 4. Ảnh, nhãn và chỗ thiếu phải giúp phán đoán

Dùng ảnh/source UI hiện hữu trong kho dự án trước; chỉ kiểm thêm đúng những màn liên quan mẫu. Cắt đúng vùng, giữ nguồn/ngày/bối cảnh trong chi tiết. Không lấy cùng một ảnh Nháp2 đại diện cho mọi bước nếu ảnh không có thông tin/nút đó.

Bốn nhãn **độ có của thiết kế UI**: `CÓ`, `CÓ — CẦN SỬA`, `THIẾU`, `KHÔNG CẦN MÀN RIÊNG`.

- `CÓ`: thấy thiết kế đáp ứng đúng việc tại dòng, không mặc nhiên hệ thống chạy được.
- `CÓ — CẦN SỬA`: chỉ ra đã có gì và thiếu/sai chính xác gì.
- `THIẾU`: chưa tìm được thiết kế phù hợp trong nguồn đã kiểm; hiện khung trống nêu màn cần phục vụ việc gì.
- `KHÔNG CẦN MÀN RIÊNG`: máy làm bên dưới; chỉ rõ người thấy tiến độ/kết quả/lỗi ở đâu.

Nếu chưa kiểm được nguồn, ghi “Chưa kiểm được” và lý do; không ép thành CÓ hoặc THIẾU để đủ nhãn.

Dưới nhãn, chỉ khi cần, dùng một câu hiện trạng cụ thể: “Mới có bản vẽ, chưa nối lưu”, “Đã thử riêng trong lab”, “Chưa thử thao tác này”. Không dùng nhãn xử lý tài sản CHỐT/NHÁP/CÔNG CỤ/BỎ thay cho độ đầy đủ.

Nếu cần minh họa màn còn thiếu, chỉ dùng khung nội dung tối thiểu và ghi rõ **ĐỀ XUẤT — CHƯA XÂY**. Không tính minh họa vừa tạo là UI tồn kho hoặc bằng chứng chạy thật.

## 5. Cột AI: hành động cụ thể, không khẩu hiệu

Viết bằng tiếng Việt: AI tìm gì, điền gì, nối gì, kiểm gì; người còn phải quyết điều gì. Một thao tác AI có thể làm thay nhiều dòng tay: chỉ rõ nhóm dòng, không giả mỗi dòng là một Agent call.

Tách ý định tự động hóa khỏi hiện trạng. Ví dụ: “AI tự tìm các mẫu gần giống và nêu khác biệt. Hiện đã thử việc tìm trong lab; chưa có nút gọi trong màn này.” Không lặp nguyên cảnh báo “chưa có đường tự động đầy đủ” 16 lần.

Các tên tool, request/response, nguồn quyền và bằng chứng để ở phần gập, dẫn về tool có thật. Chưa có tool thì ghi đúng; không đặt tên mới rồi tính là đã có. AI không ký duyệt thay người chưa được ủy quyền.

## 6. Đi thử để biết kẹt ở đâu — không xây sản phẩm trong lượt này

Kiểm các màn/nút đang có theo đường người dùng. Được xem UI hiện hữu an toàn hoặc dùng môi trường thử riêng đã được cho phép. Không lấy script đổi dấu tick làm bằng chứng hoàn tất thao tác.

- Ghi bước nào vào được, thông tin/nút có gì, bước nào không thể đi tiếp và ảnh đúng chỗ kẹt.
- Nếu thực sự kiểm lưu trên môi trường thử được phép, phải mở lại và đối chiếu kết quả. Ghi rõ là lab, không phải production.
- Không dùng API/SQL/terminal để vượt một bước UI bị thiếu rồi báo người đã đi hết bằng tay.
- Không tạo lab mới, nâng nền, sửa guard/worker, tạo UI nghiệp vụ hoặc cấp quyền để cố chạy hết mẫu.
- Không bấm publish/activate/delete có tác động thật trên hệ hiện hữu. Khi chưa có môi trường an toàn, ghi thao tác chưa chạy; xem tiếp các màn sau như kiểm thiết kế riêng, không giả chuỗi đã nối liền.

**Thiếu UI là kết quả hợp lệ của mẫu.** Không buộc sửa hết hệ thống trước khi Owner được xem format.

## 7. Tự kiểm trước khi nộp

| Kiểm | Đạt khi |
|---|---|
| Đúng đầu-cuối | Phân biệt tạo nháp, duyệt, ban hành, bật chạy, thấy kết quả; thiếu đoạn nào hiện ngay. |
| Đọc không cần kiến thức IT | Mỗi dòng chỉ được việc cần làm, nơi làm và kết quả; không phải mở phần kỹ thuật mới hiểu. |
| Manual thật, không manual giả | Không bắt người gõ ID/JSON hoặc chọn tool; không coi hệ thống tự tính là nhiệm vụ người. |
| Ảnh đúng | Ảnh đọc được, đúng control/bối cảnh, đường ảnh hoạt động; phần chưa có không mượn ảnh để giả có. |
| Phân biệt rõ trạng thái | CÓ thiết kế không đồng nghĩa đã chạy; mỗi chỗ thiếu có mô tả riêng và ảnh/nguồn tương ứng. |
| AI không hứa quá | Hành động đề xuất và khả năng đã thử tách rõ; không bỏ qua quyền hoặc bịa tool. |
| Không giấu nhánh quan trọng | Thiếu nguyên liệu, trả sửa, lưu dở/tiếp tục có ghi nơi quay lại, không trải mọi nhánh thành đường dài bắt buộc. |
| Giữ nguồn | Các dòng có mapping về dataset; phần bổ sung/điều chỉnh là đề xuất, không sửa lịch sử. |
| Tài liệu dùng được | Mở local không cài dependency; bảng, ảnh phóng to, liên kết hoạt động; không có nút ghi dữ liệu thật. |
| Đúng giới hạn | Chỉ một mẫu; không rollout 87 bước, không sửa SSOT/dataset nguồn hay đóng Gate. |

Nhờ một Agent khác đọc mẫu mà không đọc phần kỹ thuật có thể tìm câu khó hiểu, nhưng phải ghi đó là **self/simulated review**, không thay phản hồi người thật.

Sau tự kiểm, dừng ở **“Mẫu chờ Owner xem cách trình bày và logic”**. Không tự ghi “người mới đã hiểu”.

Owner chỉ cần cho biết: có hiểu đường đi không; bước nào thiếu/sai; đoạn nào khó đọc. PM và giám sát chịu kiểm đủ nguồn, kỹ thuật và xử lý phản hồi, không giao Owner làm QA từng field. Nếu phải giải thích miệng mới hiểu một dòng, ghi dòng đó cần sửa, không quy lỗi cho người đọc hoặc ép thời gian duyệt.

## 8. Lưu và bàn giao

Tạo đúng một trang mẫu mở trực tiếp tại:
`/Users/nmhuyen/Desktop/quy trình/KHO/11-evidence/ban-do-buoc/mau-de-duyet/TAO-MOT-QUY-TRINH.html`

Ảnh đi kèm gọn hoặc dẫn tương đối tới kho đã có. Chỉ trích phần dataset cần cho mẫu; không nhúng lại toàn bộ 2,1 MB vào trang người đọc. Mapping/ghi chú bổ sung là lớp trình bày, không một nguồn kiến trúc mới.

Không ghi lại SSOT hoặc thay bản đồ chính trước khi Owner duyệt mẫu. Lưu lệnh này và tình trạng đang chờ vào hồ sơ công việc/README hiện có để không quên. Chuẩn bị ba nội dung nhập SSOT ở lần cập nhật sau:
1. Luồng/UI chỉ được nghiệm thu khi có cả kiểm kỹ thuật và xác nhận người hiểu đường đi; không lấy hash/số lượng dòng thay xác nhận này.
2. Bản đồ có lớp hướng dẫn người dùng theo format được Owner chọn; dataset/trace kỹ thuật ở phía sau.
3. D04 đã Owner chấp thuận; Gate1 completeness chưa đóng; mẫu được duyệt không tự đóng Gate hoặc chứng minh vận hành.

Báo cáo tối đa 5 dòng: link mở trang mẫu; số dòng và phạm vi đầu-cuối; những chỗ thực sự kẹt; thao tác nào chưa chạy; chờ Owner duyệt format. **Không yêu cầu Owner tải ZIP 46 MB hoặc chuyển thêm file kỹ thuật.** Dừng sau mẫu, chưa nhân rộng.
