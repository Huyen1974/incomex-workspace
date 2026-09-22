# Lệnh Codex — sửa mẫu “Tạo một quy trình”: nhìn tổng thể, ảnh dễ đọc, một bản hiện hành

**GPT Chat / PM · 12/09/2026**

## 1. Mục tiêu và phạm vi

Chỉ hoàn thiện mẫu **“Tạo một quy trình — tôi làm gì, AI làm thay gì?”**, rồi dừng để Owner xem. Mục tiêu: người mới nhìn menu biết đường đi; mở một bước biết phải làm gì, nhìn ở đâu, còn thiếu gì và AI giúp phần nào.

Đây là lệnh thay thế lệnh sửa mẫu trước trong phạm vi này. Không mở luồng khác, không thiết kế bù hàng loạt, không đóng Gate hoặc tự khóa format.

Đọc mẫu hiện hành tại:
`/Users/nmhuyen/Desktop/quy trình/KHO/11-evidence/ban-do-buoc/mau-de-duyet/TAO-MOT-QUY-TRINH.html`

Đọc đối chiếu bản đồ, nguồn UI/Help và evidence liên quan đã có trong dự án. Không tìm lại toàn hệ thống. Giữ dữ liệu/bằng chứng của bản đồ 87 bước; không đổi nghĩa kiến trúc để vừa cách trình bày mới.

## 2. Một nơi cố định để Owner mở — không thêm các bản “mới nhất”

Bản hiện hành sau lượt này phải nằm tại:
**`/Users/nmhuyen/Desktop/quy trình/TAO-MOT-QUY-TRINH.html`**

Từ đây sửa tại đúng tên đó; ngày sửa/phiên bản nằm trong trang, không sinh tên `v2`, `final`, `new` ngoài thư mục gốc. Kiểm đường dẫn thật và dạng Unicode trên máy để không tạo hai thư mục/tệp nhìn giống nhau.

Ba tệp có vai trò cố định:
- `cấu trúc hệ thống.html`: kiến trúc, chỉ đạo, quyết định, tiến trình.
- `BAN-DO-BUOC-UI-AGENT.html`: dataset và đối chiếu chi tiết toàn hệ.
- `TAO-MOT-QUY-TRINH.html`: mẫu người đọc hiện hành, **chờ Owner duyệt**, không phải kiến trúc thứ hai.

Trước thay: backup bản gốc; nếu root đã có tệp thì đối chiếu phiên bản/hash và hợp nhất đúng nguồn, không ghi đè mù. Bản làm việc cũ trong `mau-de-duyet` không tiếp tục là một bản hiện hành: sau khi lưu nguyên bản vào kho lịch sử, chuyển đường cũ thành thông báo ngắn dẫn về root. Nếu là snapshot đã niêm phong trong manifest, giữ nguyên và ghi vai trò lịch sử trong INDEX, không sửa bằng chứng niêm phong.

Sửa tất cả đường dẫn tương đối của mẫu sau khi đưa ra root: bản đồ, source, nhật ký, ảnh, lệnh cũ phải trỏ đúng; không còn `../../..` sai cấp. Giữ ảnh nhúng để mở một HTML là thấy ảnh; tài liệu kỹ thuật phụ được dẫn tới kho evidence ổn định, không thư mục phiên Codex.

**Ngoại lệ cập nhật tài liệu được PM cho phép trong lượt này:** chỉ cập nhật tối thiểu mục tài liệu/đường dẫn của SSOT và link “Mẫu tạo quy trình” trong bản đồ, ghi vị trí mới và trạng thái chờ Owner duyệt. Giữ nguyên dataset, kết luận kỹ thuật, kiến trúc và Gate. Ghi ngắn chỉ đạo “menu tổng thể, ảnh đọc được, tên tệp cố định”; không để chỉ đạo chỉ tồn tại trong chat. Nếu SSOT có quy tắc version riêng, tuân thủ quy tắc đó, không đoán trước version kế.

Owner không phải đọc một INDEX mới hoặc chọn giữa các bản. Báo cáo cuối chỉ dẫn tới HTML root.

## 3. Màn đầu = menu nhìn hết đường đi

Rút phần mở đầu thành tên mẫu, một câu ví dụ, một câu giới hạn và menu. Giữ bốn chặng đang có, trình bày các bước thành ô/link có số và tên ngắn bằng tiếng Việt. Không xếp tất cả thành 16 ô nhỏ trên một hàng hoặc buộc cuộn ngang.

- Mỗi ô bấm tới đúng thẻ bên dưới; thể hiện rõ thứ tự và chặng.
- Nhánh “chỉ khi thiếu” tách khỏi đường chính, có đường quay về.
- Từ mỗi thẻ có “Về tổng thể”, “Bước trước”, “Bước tiếp”; trường hợp có nhánh ghi rõ điều kiện, không đi tiếp giả khi còn thiếu.
- Khi cuộn chỉ cần thanh điều hướng gọn, không ghim cả menu lớn che nội dung.
- Menu và dòng tổng phải nhìn được ở 1280×720, zoom 100%, không thu chữ xuống li ti. Phần giới thiệu dài chuyển xuống dưới.
- Số liệu lấy từ cùng dữ liệu của các thẻ: có, cần sửa, thiếu, không cần màn. Tách số hành động chính và nhánh điều kiện; không đếm cả nhóm 06 và các mục con như các bước độc lập cùng cấp.

Bản cũ có 16 dòng, nhãn 0 CÓ / 6 CÓ–CẦN SỬA / 9 THIẾU / 1 KHÔNG CẦN MÀN RIÊNG. Đây là kết quả cũ, **không phải số phải giữ sau khi tách bước**. Không suy ra % hoàn thành toàn hệ, số màn duy nhất hoặc phủ nhận các proof lab từ các số này. Không gọi dải thiếu 8–13 là toàn bộ việc còn phải làm.

## 4. Thẻ rộng thay bảng năm cột

Mỗi thẻ:

**Đầu thẻ:** số + tên hành động dễ hiểu + đúng một nhãn tình trạng. Vai thực hiện ghi ngắn để không hiểu một người phải làm cả việc dựng, duyệt, bật và thực hiện.

**Thân thẻ:** ảnh lớn và nội dung bên cạnh, gồm:
1. **Cần sửa/bổ sung:** đúng vấn đề của bước, tối đa hai câu; khi đủ thì nói phần đã có.
2. **AI làm thay:** một câu; ai còn phải quyết điều gì. Nếu thực chất hệ thống tự kiểm thì gọi “hệ thống”, không gán mọi thao tác cho LLM.
3. **Xong thì thấy:** một kết quả quan sát được và nơi đi tiếp.

Giữ câu hướng dẫn chính bằng động từ, ví dụ “Chọn người chịu trách nhiệm việc này”. Không đưa tên bảng, mã contract, endpoint, revision key vào phần mặc định. Chi tiết bằng chứng và giới hạn kỹ thuật gập xuống dưới nhưng không che cảnh báo quan trọng: ảnh mẫu hoặc đường chưa nối phải có chú thích thấy ngay.

Không nhân bản cùng một đoạn cảnh báo dài ở mọi thẻ. Không thêm checklist người phải tick hoặc biến menu tài liệu thành giao diện giả lưu/duyệt/chạy nghiệp vụ.

## 5. Ảnh phải giúp đọc ngay, không chỉ làm hình minh họa nhỏ

Ảnh chính phải chụp/cắt đúng vùng của hành động đang nói, giữ đủ tên màn/nhãn để biết mình đang ở đâu. Khung ảnh desktop ưu tiên từ khoảng 640px trở lên; nếu còn chật thì ảnh nằm cả hàng, nội dung bên dưới. Ở màn nhỏ xếp một cột, không cố giữ 640px gây tràn.

- Không ép mọi ảnh vào hộp cao 145px. Giữ tỷ lệ, không kéo méo.
- Không phóng ảnh bé bị mờ rồi gọi là đọc được. Ưu tiên source/screenshot độ phân giải phù hợp, chụp element/crop từ nguồn tốt. Vùng hẹp không cần kéo giãn cho đủ số pixel.
- Khoanh khung đỏ hoặc đánh dấu đúng control đang nói; không che chữ. Chú thích cụ thể, ví dụ “Chọn người ở ô này”. Lưu nguồn ảnh và vùng crop phía sau; không sửa bản evidence gốc.
- Bấm ảnh mở bản gốc đủ ngữ cảnh, đóng lại vẫn ở bước đang xem; không phải mở ảnh lớn mới đọc được nhãn quan trọng.
- Ảnh của Nhập kho/Giao hàng chỉ chứng minh thiết kế đang có: ghi đúng tên ví dụ trong ảnh, không sửa nội dung ảnh thành quy trình thời lượng để tạo bằng chứng giả.
- Ảnh 404 chỉ chứng minh đường mở đã thử bị lỗi, không chứng minh toàn hệ không có màn đó.

Chỗ thực sự chưa có thiết kế phù hợp: đặt một **phác thảo nội dung tĩnh, nhỏ và dễ hiểu** với nhãn rõ “ĐỀ XUẤT MINH HỌA — CHƯA CÓ CHỨC NĂNG”. Có thể dùng HTML/CSS đơn giản ngay trong tài liệu, không cần thêm công cụ hay xây prototype nghiệp vụ. Thể hiện thông tin/nút tối thiểu để Owner góp ý; không tính phác thảo vào UI đã có, không tự thêm feature.

## 6. Chỉnh ba chỗ logic, không làm lại toàn luồng

### Bước 06: tách việc để nhìn được phần đã có và phần thiếu

Giữ liên kết nguồn cũ, nhưng nhóm 06 mở thành:
- **6a:** Chọn biểu mẫu nhập và thông tin cần xem. Giữ phần MOUT/hướng dẫn cần thiết; báo cáo tham khảo không phải kết quả hoàn thành công việc. Chọn dùng lại trước, chỉ mở editor đúng owner khi cần.
- **6b:** Chọn người hoặc máy thực hiện. Phân biệt người làm, làm thay, người làm bước tiếp, người nhận báo cáo, đầu mối bàn giao theo D04 đã Owner chốt; không hỏi lại D04.
- **6c:** Chọn kết quả cần bàn giao và bước nhận. Nêu rõ dữ liệu vừa nhập được chuyển thế nào, lưu ở đâu; không thay bằng tên người nhận báo cáo.
- **6d — chỉ khi thiếu:** Gửi yêu cầu bổ sung phần còn thiếu. Phân biệt “thiếu trường thông tin” và “thiếu nơi lưu phù hợp”; người nêu nhu cầu, người phụ trách dữ liệu quyết cách lưu, không bắt người dùng thiết kế bảng SQL. Cho thấy đã gửi cho ai, đang chờ gì và quay lại đúng 6a/6b/6c ra sao; Condition thiếu cũng theo đường phù hợp.

Rà đúng candidate form builder/giao việc/handoff đã lưu, lấy ảnh có nguồn. Không mặc định đổi 6a/6b thành CÓ vì giám sát nói đã có màn; phải so nội dung cần thiết. Không ép số card cuối vẫn bằng 16. Mapping dòng cũ→mới nằm ở chi tiết PM, không tăng tổng dataset 87 bước trong lượt này.

### Bước 14: tách việc máy nhận tín hiệu khỏi nhu cầu người theo dõi

Hành động của người là **“Xem lượt mới đã bắt đầu chưa”**. Máy tự nhận tín hiệu và mở lượt; không tạo biểu mẫu/nút giả bắt người làm thay.

Vì người cần xem lượt, không dùng nhãn KHÔNG CẦN MÀN để che thiếu màn theo dõi. Kiểm nguồn C40/monitor đã có: có surface nhưng chưa nối thì CÓ–CẦN SỬA; chưa có phần cần thiết trong phạm vi đã tìm thì THIẾU, ghi rõ cần gì. Không đổi nhãn chỉ dựa ảnh 404.

Bước14 và16 có thể dùng **cùng màn theo dõi lượt ở hai trạng thái** (vừa bắt đầu / đã có kết quả); đừng thiết kế hai trang nếu không cần. Giữ bước15 là người được giao nhập thông tin, không phải người dựng tự làm.

### Các nhánh giữ nguyên nhưng phải nhìn thấy

Bản có sẵn phù hợp → có thể bỏ tạo/ban hành lại; thiếu vật liệu → chờ rồi về đúng nháp; trả sửa → sửa và kiểm lại; từ chối → dừng; ban hành khác bật chạy. Gắn link rõ trong menu/thẻ, không giấu hết trong đoạn kỹ thuật.

## 7. Nhãn dễ hiểu nhưng không đánh tráo mức đạt

Bốn nhãn tình trạng UI của bước: **CÓ · CÓ–CẦN SỬA · THIẾU · KHÔNG CẦN MÀN**.

Cùng một nhãn/màu ở menu và đầu thẻ; có chữ, không chỉ màu. Không lặp thêm “CHƯA CÓ MÀN PHÙ HỢP” như một trạng thái thứ hai trong ảnh.

Nhãn đánh giá UI phục vụ bước trong phạm vi này. **CÓ không tự nghĩa là toàn quy trình lưu/chạy được.** Chú thích ảnh và một câu “đường này chưa nối/đã thử ở đâu” giữ ranh giới thiết kế, kết nối, lab. Cột AI là phần có thể làm thay và phạm vi đã biết, không tuyên bố tool triển khai toàn hệ. Không tự chuyển mọi dòng sang THIẾU chỉ vì chưa production; thiếu evidence thì ghi giới hạn thay vì khẳng định đã kiểm.

Giữ đúng kiến thức đã có: bước người làm là đường giải thích; máy vẫn tự tìm, điền, kiểm, lưu theo quyền; Owner không phải nhớ tool, chạy từng test hay gõ raw ID.

## 8. Kiểm trước khi báo — không dùng kiểm file thay cho kiểm cách đọc

| Kiểm | Đạt khi |
|---|---|
| Tổng thể | 1280×720 ở 100% thấy menu các chặng/bước và tóm tắt; không cuộn ngang, không chữ cỡ nhỏ để ép vừa. |
| Điều hướng | Mọi ô tới đúng tiêu đề; nhánh 6d có đường về; trước/tiếp/tổng thể đúng; thanh ghim không che tiêu đề. |
| Ảnh | Render thực và nhìn từng ảnh ở kích thước hiển thị; đọc được nhãn/ô đang chỉ, khung đánh dấu đúng, không méo/mờ; có phóng to và đóng trở lại. |
| Thẻ | Đọc được ai làm, hành động, thiếu gì, AI giúp gì, kết quả ở đâu mà không mở phần kỹ thuật. |
| Logic | 06 không che form/người làm/bàn giao; 14 không giấu monitor; không mất MOUT, D04 hoặc nhánh bù thiếu; không sinh thao tác máy giả cho người. |
| Số liệu | Menu, thẻ và tổng cùng nguồn; nhóm không cộng thêm vào con; nhánh không bị tính là ai cũng phải đi; ảnh đề xuất không tăng tồn kho UI. |
| Bản hiện hành | Root mở đúng bản mới; link PM/source/ảnh đúng sau chuyển vị trí; SSOT/bản đồ dẫn về cùng root; kho không có bản current cạnh tranh. |
| Phạm vi | Không sửa product UI, dataset kỹ thuật, quyền, DB, Gate; không chạy lưu/duyệt/ban hành/activate để thử; chỉ sửa tài liệu và điều hướng được cho phép. |

Kiểm thêm một màn desktop hẹp và điện thoại để thẻ/ảnh không tràn; kiểm bàn phím, nút đóng ảnh và không lỗi JS. Không dùng ảnh vẽ của trang để giả đã render HTML thật. Nếu công cụ render bị chặn, nêu rõ, không ghi visual PASS; giám sát có thể mở bản bàn giao để kiểm.

Codex/giám sát tự QA trước. **Owner là người chốt mẫu có dễ hiểu hay chưa**, không chịu trách nhiệm rà hash/quyền/ảnh thay Agent. Format chưa được tự khóa chỉ vì checklist máy đạt.

## 9. Bàn giao và dừng

Làm staging, backup, kiểm current hash tránh đè thay đổi của phiên khác, rồi cập nhật bản hiện hành một lượt. Lưu evidence nhỏ vào kho đã có; không tạo một gói 46 MB chỉ để báo sửa format. Không đổi/bỏ manifest lịch sử.

Báo Owner tối đa năm ý:
1. Một link mở `TAO-MOT-QUY-TRINH.html` tại root — đây là bản cần xem.
2. Menu/ảnh/thẻ đã thay gì.
3. Bước06/nhánh thiếu/bước14 đã làm rõ ra sao; số liệu mới đúng phạm vi.
4. Bản cũ chuyển vai trò gì, SSOT/bản đồ đã trỏ đúng bản hiện hành chưa.
5. Kết quả tự kiểm và giới hạn; **CHỜ OWNER DUYỆT MẪU**.

Không mở luồng khác, không bắt đầu xây dải UI thiếu8–13, không tự nghiệm thu Gate1. Khi Owner duyệt được cách đọc và logic mẫu này, PM mới giao áp format cho các luồng khác.
