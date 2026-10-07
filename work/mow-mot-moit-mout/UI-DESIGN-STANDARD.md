# Quy chuẩn UI cha — đọc trước khi thiết kế
> **Thông tin chính rõ; thông tin phụ lùi lại. Cùng loại việc dùng cùng một khuôn. AI kiểm trước, Owner quyết thiết kế.**
Owner 07/10/2026 11:08 +07. CE-20261007-UI-PARENT-STANDARD. Đây là văn bản hóa mẫu/chỉ đạo đã có, không phải đợt thiết kế mới.

## 1. Sáu quy tắc chung
1. Chọn đúng UI cha và phiên bản nguồn trước khi làm. Không nhớ bằng chat, không vẽ lại từ ảnh.
2. Tên đối tượng, nội dung đang xử lý, hành động và trạng thái cần quyết định phải rõ. ID, đường dẫn, mô tả kỹ thuật, thông tin phụ nhạt nhưng đọc/bấm được.
3. Chia thông tin thành nhóm; tổng quan trước, chi tiết mở khi cần. Giữ quan hệ cha/con bằng bố cục và thụt lề.
4. Giữ font, khoảng cách, vị trí nút, icon, thứ tự vùng và hành vi của đúng mẫu cha. UI con chỉ thay phần mẫu cho phép.
5. Màu có nghĩa thống nhất; không trang trí thêm, không làm tất cả đậm. Không áp máy móc bảng màu/cột của Master List lên form, Canvas hoặc Workspace.
6. Một nguồn quy chuẩn; sửa cha rồi kiểm các con bị ảnh hưởng. Owner không phải người nhớ checklist hoặc phát hiện lỗi lặp lại.

## 2. Danh mục đối chiếu
| Họ UI cha | Phần chính cần thấy ngay | Phần phụ | Nguồn thực thi |
|---|---|---|---|
| UI.MASTER | Tên, trạng thái; ngữ cảnh theo schema | ID, tham chiếu, metadata | mot-master-v1.html + master-list.js |
| UI.CANVAS | Tên thẻ, trạng thái, bước đang xem | Mã, mô tả bổ trợ, chi tiết mở thêm | mow-unified-canvas-v2.html |
| UI.CONFIG | Nhóm đang cấu hình, trường nhập, Test/tình trạng | Mapping kỹ thuật, placeholder, hướng dẫn | New MODT / moit-config / modal Field |
| UI.STUDIO | Thành phần đang chọn, ô nhập, preview | Mã và giải thích kỹ thuật | mot/moit/mout-studio; mot-theme + mot-render |
| UI.REVIEW | Tóm tắt quyết định, thiếu gì, bằng chứng | Thông tin kỹ thuật mở thêm | nhap2-render.js / chi tiết MOW |
| UI.WORKSPACE | Việc đang chọn, thao tác, hạn/trạng thái | Đường quy trình, metadata, tham khảo | mot-dashboard + mot-render + mot-app |

Nguồn đăng ký: ui/child-ui-registry.json (29 UI con), ML-DEF-017 (6 họ). Nhãn “đang dùng/có UI” không tự chứng minh mọi chi tiết đã được Owner duyệt. UI-008/011/012 chưa gán cha: giữ bản đã có, không tự gán hoặc thiết kế lại.
**29 UI con và 29 Master danh mục là hai tập khác nhau; không lấy kết quả của tập này để báo đã kiểm tập kia.**

## 3. Quy tắc riêng Master hiện hành
Chi tiết token/đậm-nhạt: xem mục “Quy chuẩn thị giác UI.MASTER” trong [FORMULA-AI-README.md](FORMULA-AI-README.md). Đây là một nguồn chi tiết; không nhân bản token.
Các số đo Master trong bản ghi lịch sử phía dưới chỉ để truy nguồn; quyết định cập nhật 07/10 thắng số đo cũ.
Navigation phải kiểm từ đúng nơi Owner mở (cả trang trực tiếp và khung Knowledge nếu dùng). Link tồn tại không chứng minh bấm được; hiện còn lỗi sandbox Knowledge mở Master, không được ghi PASS cho đường đó.

## 4. Cổng bàn giao bắt buộc
Mỗi lần sửa UI phải có phiếu trong báo cáo kiểm với:
- ID UI, cha, URL Owner, phiên bản nguồn/commit; danh sách tất cả UI bị ảnh hưởng.
- Kết quả riêng cho: cấu trúc; chính/phụ; nhãn; thao tác; hẹp/chữ dài/rỗng; lỗi console; dữ liệu/config.
- Mỗi mục ghi PASS / FAIL / BLOCKED / N-A (N-A có lý do), kèm bằng chứng đo/ảnh/thao tác. Chưa đo = NOT_TESTED, tuyệt đối không PASS.
- Sửa nguồn cha: kiểm hiển thị tất cả con liên quan; thao tác đại diện từng loại renderer, mọi biến thể bị thay đổi. Không chỉ mở một trang rồi suy ra tất cả đúng.
- Thử thao tác thật và kết quả cuối: tìm/lọc, mở/đóng, quay lại/Home, tooltip bằng chuột/bàn phím; form/preview theo phạm vi. Không bấm lưu dữ liệu production để thử.
- Nếu chưa đủ bằng chứng hoặc còn lỗi liên quan: bàn giao PARTIAL/BLOCKED kèm điểm còn lại, không yêu cầu Owner tự dò lỗi.
- Người thực hiện tự sửa lỗi kỹ thuật; chỉ hỏi Owner khi có quyết định thiết kế/khái niệm mới hoặc mâu thuẫn không giải được từ nguồn.

**Cưỡng chế trong quy trình:** README bắt buộc đọc tài liệu này; AI không được chuyển XONG/PASS khi phiếu chưa đạt. Đây là cổng quy trình, chưa phải CI tự chặn mọi lần deploy. Không được nói đã có CI nếu chưa triển khai.
**Cổng máy:** `python3 work/mow-mot-moit-mout/check-ui-review.py <receipt.json>` kiểm độ đủ phiếu và chặn PASS thiếu bằng chứng; không thay kiểm bằng mắt/bấm thật. Khuôn phiếu và danh sách ID nằm trong `UI-REVIEW-CONTRACT.json`.

## 5. Quy tắc kế thừa từ thiết kế đã có
Nguồn: ban-duyet.html, mục “Quy chuẩn UI cha → UI con”, phiên bản ac343a054efd80793954535c6f53766cbb21e6d2bc8dcb697e63dfd78012a6e3. Phần dưới ghi lại hợp đồng mẫu và số đo tham khảo đã có; không coi số đo lịch sử là quyết định mới.

Quy chuẩn UI cha → UI con
Dùng lại khuôn đã chọn; thay nhãn và dữ liệu đúng chỗ. Các gạch đầu dòng dưới đây tổng hợp từ chỉ đạo Owner và mẫu đang chạy ngày 16/09/2026; thông số đo hiện trạng không phải quyết định đổi thiết kế.

- Chọn đúng mẫu cha trước. UI con dùng lại bộ dựng và kiểu trình bày của cha; thay dữ liệu/nhãn được khai báo, không tự vẽ một khuôn mới.
- Chỉ hai view: Kanban và Master list. Studio, Config, Review, bàn làm việc là khu làm việc; không đặt thêm loại view.
- Giữ nguyên thứ tự vùng, vị trí nút, biểu tượng, font, khoảng cách, cách mở chi tiết và quy tắc thu gọn của mẫu cha.
- Để rõ tên đối tượng, nội dung đang làm và thông tin cần quyết định. Mã, đường dẫn, thông tin phụ và phần kỹ thuật dùng cấp chữ nhạt của mẫu; nhạt vẫn phải đọc và thao tác được.
- Tài liệu UI: nền giữa các miếng chỉ tối vừa; bên trong theo UI cha. Vàng thao tác nhạt.
- Đầu miếng: tên UI đậm; mã bước, tên bước, mã UI con/cha và liên kết nhạt nhưng đọc được. Mã bước chừa khoảng để chèn.
- Mã UI con (bản thử): mã bước trước, mã UI cha sau — S010.UI.MASTER. Phần mã cha bấm mở UI Master. UI dùng lại giữ mã gốc; UI thứ hai cùng bước và cha thêm A/B. Quan hệ lưu bằng khóa; mã đã cấp thật không đổi.
- Hàng mẹ rõ; hàng con thụt lề. Tổng quan gọn trước, chi tiết mở khi cần. Không đổ tất cả thông tin ra lần đầu.
- Màu trạng thái giữ nghĩa: xám trung tính/chưa làm, xanh đạt, vàng cần chú ý, đỏ có vấn đề; giữ chữ/ký hiệu đi kèm. Không dùng màu thương hiệu để thay nghĩa trạng thái.
- Mỗi UI con có mã ổn định, khu vực, mẫu cha và URL. Một UI dùng nhiều bước chỉ đếm một lần. Khác nhãn/thông số riêng thì khai báo riêng, không sao chép mã giao diện.
- Nếu phải đổi cột, cấu trúc hoặc thao tác ngoài cấu hình cha: ghi vào phần cần chốt tại đây, sửa chuẩn cha rồi áp dụng chung; không âm thầm tạo biến thể riêng.


### Master list · phần phải giữ / phần được thay
[Mở mẫu cha để đối chiếu ↗](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-master-nhap2-v1.html)

- Bố cục: tìm/lọc và thao tác ở trên, danh sách ở dưới; từ một dòng mở thông tin/kiểm tra/Config của đúng đối tượng.
- Mẫu MOW hiện có 11 cột nhìn thấy: Sửa · # · Mã · Tên · Chuyên môn (T3) · Nhiệm vụ (T2) · Công việc (T1) · Máy / mục tiêu · Vai trò · Trạng thái · Mở chi tiết.
- Giữ thứ tự và hành vi cột. Số cột phụ thuộc cấu hình mẫu (ví dụ Vai trò/Mẹ); không ép mọi UI con có 11 cột và không tự thêm cột ngoài khai báo chung.
- Tên đối tượng là điểm nhìn chính; mã và thông tin phụ nhạt. Cột T3/T2/T1 giữ ngữ cảnh; không kéo đường dẫn dài ra thay bố cục.
- Giữ bút sửa đầu dòng, đường mở chi tiết cuối dòng, tooltip và bộ lọc. Ngừng là trạng thái/lọc trong List, không dựng thêm màn riêng.
- UI con được thay tên loại, nhãn nghiệp vụ, nguồn dữ liệu và cấu hình cột được mẫu hỗ trợ. Không tự đổi font, độ đậm, màu hoặc vị trí nút.


### Thông số và nguồn cho AI triển khai

- Font Be Vietnam Pro; thân trang 14px/1.5; bảng 12.5px; header thực tế 10px, weight 600.
- Đo trên UI-001: Tên #2c2c2e; T3 #6e6e73; T2/T1 đang #b0b0b5. Mã/header phụ dùng khoảng #bcbcc1; STT #c8c8cd.
- Nguồn master-list.js có quy tắc nhấn Tên/T3/T2/T1 nhưng lớp đang chạy cho độ nhạt khác nhau. Giữ hiện trạng; mức nhấn bốn cột còn cần Owner xem, không tự coi tất cả đã đồng nhất.
[mot-theme-v1.css](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-theme-v1.css) · [master-list.js](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-list.js) · [mow-master-nhap2-v1.html](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-master-nhap2-v1.html)




### Kanban · phần phải giữ / phần được thay
[Mở mẫu cha để đối chiếu ↗](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html?tang=T2&che-do=thuong)

- Giữ hàng trên: 🔍 Tìm kiếm · Thường · Đề xuất · Vận hành; giữ Quản trị ở vị trí hiện có. Breadcrumb và các tầng nằm bên dưới.
- T2–T7 dùng chung khuôn thẻ. Số thẻ trên hàng tự theo bề rộng màn hình, không quy định mọi nơi phải có một số cột cố định.
- Mỗi thẻ: tên và tín hiệu trạng thái rõ; các mục con gọn, có “+N nữa” để mở thêm. Không kéo dài tất cả thẻ theo toàn bộ quy trình.
- Biểu tượng người/robot phản ánh Task bên trong; có cả hai khi có Task người và tự động. Không suy cả quy trình chỉ có người từ một biểu tượng mặt cười.
- MOIT và MOUT là hai loại riêng cùng T0,5; Field là T0. T1 có bố cục riêng, không ép thành thẻ T2.
- UI con thay đối tượng, nhãn, liên kết và dữ liệu; giữ kiểu thẻ, icon, tương tác mở sâu và (+) trong Đề xuất.


### Thông số và nguồn cho AI triển khai

- Font Be Vietnam Pro; nền #f5f5f7; chữ chính #1d1d1f; thang 11/12/14/16px; thân 14px, line-height 1.5.
- CSS nền: thẻ 232px, gap 24px, lề trái 48px; thanh trên cao 56px. Lấy giá trị từ nguồn chung và các breakpoint đang có, không chép số cột theo ảnh chụp.
[mow-unified-canvas-v2.html](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html)




### Config theo nhóm · phần phải giữ / phần được thay
[Mở mẫu cha để đối chiếu ↗](https://vps.incomexsaigoncorp.vn/admin-new-modt?tang=T1&che-do=de-xuat)

- Giữ bố cục và các nhóm của New MODT; mở nhóm cần cấu hình, thu phần chưa cần. Không tự biến toàn bộ config thành một form dài.
- Tên nhóm/việc và thông tin người phải nhập rõ; placeholder, mapping kỹ thuật, hướng dẫn và thông tin chưa nối dùng cấp nhạt hiện có.
- Bảng thuộc từng nhóm có số cột riêng. Giữ schema và thứ tự của đúng nhóm, không áp cùng một số cột cho toàn trang Config.
- Giữ tooltip, Test, Tình trạng và cách mở hàng dài; không thay chữ “chưa test/chưa kết nối” bằng trạng thái đạt.
- UI con khai báo trường/nguồn/điều kiện riêng theo mẫu. Tên/thứ tự cột dùng chung không được sửa riêng cho từng task.
- Owner 17/09/2026: T1 Đề xuất trong Kanban dùng toàn bộ Config New MODT: MOIT/MOUT, bảng kết nối, Nguyên tắc giao việc, Ai làm & ai nhận, Chạy & kết thúc. Đây là phần tiêu chuẩn; hai nơi dùng chung nguồn. T1 Đề xuất hiển thị các task theo chiều dọc: thu gọn còn một dòng, mở task hiện toàn bộ Config hai cột. Dấu + trước/giữa/sau dùng lại form thêm mới; tạo task đồng thời có MOIT/MOUT, bảng bên phải và ba nhóm Config. Một task mở tại một thời điểm.


### Thông số và nguồn cho AI triển khai

- Nguồn new-modt-v1.html có nhiều nhóm: ví dụ lưới luật giao việc 6 cột; bảng mapping cần đọc schema của đúng biến thể. Không lấy một bảng làm chuẩn số cột cho mọi nhóm.
- Kế thừa Be Vietnam Pro, nền và thang chữ của mẫu; giữ phần cấu hình thu/mở và placeholder của chính module.
[new-modt-v1.html](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/new-modt-v1.html)




### Studio · phần phải giữ / phần được thay
[Mở mẫu cha để đối chiếu ↗](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-studio-v1.html)

- Dùng bộ có sẵn: F = ô nhập; L = khung sắp xếp; E = form nhúng; C = cụm chuẩn. Thiếu loại thì bổ sung vào bộ chung một lần.
- Khung L1–L4 chọn 1–4 ô mỗi hàng; hệ thống sắp và co theo màn hình. Không tự tạo thêm cách chia cột ngoài bộ đã có.
- Giữ chọn thành phần → xem thử; giữ thứ tự danh mục và mã mẫu. Nhãn trường, ô nhập và kết quả xem thử rõ; giải thích/cấu hình phụ nhạt.
- Giữ ô nhập, kiểm tra định dạng, hướng dẫn và phản hồi của F tương ứng; không vẽ một ô khác cho cùng loại dữ liệu.
- MOT, MOIT, MOUT là ba Studio riêng cùng định dạng. Thay nhãn, danh mục và nguồn đúng loại; không coi Studio MOT là đã làm xong hai Studio còn lại.


### Thông số và nguồn cho AI triển khai

- Nguồn chung mot-theme-v1.css + mot-render-v1.js; Studio cấu hình tại mot-studio-v1.js.
- Gallery 2 cột; bộ lắp 330px + phần còn lại, gap 16px; dưới 880px về 1 cột. L3/L4 giảm về 2 cột dưới 900px theo CSS hiện có.
[mot-theme-v1.css](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-theme-v1.css) · [mot-render-v1.js](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-render-v1.js) · [mot-studio-v1.js](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-studio-v1.js)




### Review quy trình · phần phải giữ / phần được thay
[Mở mẫu cha để đối chiếu ↗](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-master-nhap2-v1.html?chi-tiet=WF-0001)

- Giữ vùng chi tiết ba câu hỏi đã chọn; không tạo thêm một màn review song song cho cùng quy trình.
- Tóm tắt để quyết định rõ trước; thông tin giải thích và kỹ thuật ở phần mở thêm.
- 14 checkpoint và Dữ liệu & sự kiện có trang riêng; giữ đường đi tới đúng quy trình và đường quay lại.
- Giữ tiêu đề, thứ tự khối, đóng/mở, tooltip và nguồn bằng chứng. UI con chỉ đổi dữ liệu/nhãn phù hợp, không biến thiếu bằng chứng thành đạt.


### Thông số và nguồn cho AI triển khai

- Chi tiết MOW cùng trang Master và nhap2-render.js; các khu mở rộng hiện có layout riêng. Không suy ra một số cột chung cho mọi trang kiểm tra.
[nhap2-render.js](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/nhap2-render.js)




### Bàn làm việc MOT · phần phải giữ / phần được thay
[Mở mẫu cha để đối chiếu ↗](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-dashboard-v1.html?cong-viec=MOT-2599)

- Giữ hai vùng lớn: trái là danh sách việc và bộ lọc; phải là việc đang chọn.
- Khung việc giữ bốn vùng: thông tin việc → thao tác → tham khảo → hướng dẫn. Đổi task thì nội dung đổi, khuôn không đổi.
- Tên việc, hành động cần làm và tín hiệu hạn/trạng thái rõ; mã, người giao, đường quy trình và giải thích phụ nhạt theo mẫu.
- Giữ tìm/lọc, chuyển việc, biểu tượng trạng thái và phản hồi thao tác. Không gộp việc đang giao cho người với task mẫu trong Master.
- UI con thay dữ liệu task, form nhập, tham khảo và hướng dẫn qua bộ dựng có sẵn; không viết một dashboard khác cho từng việc.


### Thông số và nguồn cho AI triển khai

- mot-theme-v1.css: sidebar cơ sở 304px, font Be Vietnam Pro, 14px/1.5; mot-render-v1.js dựng bốn vùng. Kế thừa breakpoint và phần tăng cường đang nạp.
[mot-theme-v1.css](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-theme-v1.css) · [mot-render-v1.js](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-render-v1.js) · [mot-app-v1.js](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-app-v1.js)




### T1 · biến thể đã chuẩn hóa

- Thường: giữ chuẩn hai cột và audit. Đề xuất: toàn bộ Config, cùng mẫu New MODT; các hàng trái/phải khớp nhau.
- Bảng mapping chuẩn T1 có 9 cột: Nội dung chuyên môn · Collection · Field · Địa chỉ dữ liệu · Kiểu dữ liệu · Hợp đồng JSON · Test · Tình trạng · Ghi chú.
- Chỉ thay mã/tên task, inputItems, referenceItems và giá trị mapping. Giữ tên/thứ tự cột, tooltip, khoảng cách, chiều cao hàng và ký hiệu — / ✓.
- Header nhạt nhưng weight ít nhất 600; chữ nháp giữ kiểu placeholder. Kiểm lệch hàng 0px, tooltip đủ nội dung và data-t1-audit="ok".



### MOUT Builder v3 · giữ UI đã có

- Đây là UI tạo MOUT đã duyệt, không tính là Studio MOUT và không cần dựng lại vì chưa gán vào một tên mẫu cha chung.
- Giữ trái khai báo khuôn, phải xem báo cáo; bản nguồn dùng 370px + phần còn lại, gap 18px, dưới 1040px về một cột.
- Số cột báo cáo do cấu hình; giữ chọn/ẩn/hiện/sắp xếp cột, lọc, thời gian, tổng và xem thử. Không áp số cột báo cáo này cho mọi MOUT.



### Kiểm trước khi bàn giao UI con

- Đúng mã UI con, khu vực và mẫu cha; tên/URL truy đúng loại.
- Đúng bố cục, thứ tự cột, font, màu rõ/nhạt, icon và vị trí nút của cha.
- Thử dữ liệu rỗng, ít/nhiều, chữ dài và màn hình hẹp; không che nút hay ép chữ quá nhỏ.
- Thử tìm/lọc, mở chi tiết, quay lại, nhập và phản hồi liên quan; kiểm lỗi trình duyệt.
- Ghi riêng: đúng khuôn UI; nhãn đã rà; config đã rà; đã nối dữ liệu thật. Không đánh dấu xong tất cả chỉ vì UI hiện được.

Còn cần xem cùng Owner: Master hiện nhấn Tên rõ hơn T3/T2/T1; chưa có một cấu hình cột riêng đã chốt cho mọi UI con. Giữ khuôn hiện có, liệt kê chênh lệch khi làm từng UI; không tự tăng số màn hay đổi độ nhấn.

