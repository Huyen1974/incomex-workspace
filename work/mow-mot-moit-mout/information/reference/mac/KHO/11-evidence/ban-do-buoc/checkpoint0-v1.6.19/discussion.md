**Đúng. Việc tiếp theo phải là lập một tài liệu HTML mới, đi từ từng bước cần có rồi mới đối chiếu UI — không tiếp tục vá sáu điểm dữ liệu để tiến tới Pilot.**

Tôi đã đọc snapshot **v1.6.18**, QA và ma trận dữ liệu trong ZIP. Kết quả Rev2 có giá trị, nhưng **chưa trả lời được câu hỏi chính của anh: toàn hệ thống cần những bước nào, mỗi bước cần thông tin/UI/tool gì, và còn thiếu bao nhiêu**. Các phép thử kỹ thuật đạt không thay thế được bản đồ này.

## 1. Tài liệu mới sẽ là gì?

Tên hiển thị:

### **Bản đồ từng bước — cần gì, đã có gì, còn thiếu gì**

File: **`BAN-DO-BUOC-UI-AGENT.html`**

Tài liệu này không được là một bài diễn giải kiến trúc nữa. Nó phải cho anh **chọn MOW, MOT, MOIT, MOUT hoặc Field → chọn Tạo/Sửa/Loại bỏ/Sử dụng → xem lần lượt từng bước**.

Mỗi bước mở ra phải thấy:

| Nội dung                            | Phải thể hiện cụ thể                                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Bước này để làm gì?**             | Bắt đầu khi nào, từ đâu tới, kết thúc ra sao, chuyển đi đâu; thiếu/lỗi thì quay lại đâu.                                 |
| **Người cần thấy và làm gì?**       | Thông tin phải xem, phần cần nhập, phần máy tự điền, nút/hành động, điều kiện và quyền.                                  |
| **Agent/công cụ làm gì song song?** | Agent suy luận gì; tool nào tìm, kiểm, ghi, đọc lại, nhớ trạng thái và tiếp tục. Phần nào chưa có phương án phải chỉ rõ. |
| **UI hiện có đáp ứng đến đâu?**     | Gắn trực tiếp ảnh/thiết kế của đúng màn hoặc vùng; chỉ ra thiếu trường, thiếu trạng thái, sai vai hoặc chưa có thiết kế. |
| **Giữ, sửa hay bổ sung?**           | Chọn phần dùng lại, sửa cụ thể gì, cần thiết kế thêm gì, bản trùng nào đề nghị ngừng dùng.                               |
| **Hợp đồng và dữ liệu liên quan**   | Thông tin thuộc ai, đọc/ghi đâu, hợp đồng đã có hay thiếu, nguồn/table nào mới chỉ là ứng viên.                          |

**Hai đường Người/UI và Agent/tool phải đặt cạnh nhau tại cùng một bước**, dùng chung thông tin và kết quả. Không được chỉ ghi “AI xử lý” hoặc “dùng panel Review”.

## 2. Cách kiểm kê phải đảo lại hoàn toàn

Trình tự được giao sẽ là:

> **Đọc thiết kế → liệt kê các bước cần phục vụ → xác định thông tin từng bước → tìm và gắn UI hiện hữu → so đủ/thiếu → chốt phương án xử lý.**

Không phải:

> Mở những UI đang có → gom thành năm pattern → kết luận đã đủ.

Phạm vi phải phủ **cả tạo mới, dùng lại, sửa/cải tiến, ngừng/loại bỏ và sử dụng**, cho từng đối tượng. Những bước chung được dùng lại, nhưng khác biệt của từng loại phải được thể hiện.

**Không giới hạn bản đồ vào quy trình “Ghi nhận thời lượng xử lý”.** Pilot đó chỉ là một ví dụ để kiểm xuyên chuỗi; nó không đại diện cho toàn bộ sản phẩm.

## 3. Phải đếm đúng ba loại, không trộn vào nhau

Tôi chưa có căn cứ xác nhận hiện mới đủ 25% hay dưới 50%. Lượt này phải đo để trả lời, không lấy ước tính làm kết luận.

HTML phải có ba thống kê riêng:

**Thứ nhất, số bước:** bao nhiêu bước cần UI; bao nhiêu đã có thiết kế đủ; bao nhiêu thiếu thông tin; bao nhiêu chưa có UI; bao nhiêu chưa xác minh. Song song là số bước còn thiếu phương án Agent/tool.

**Thứ hai, số giao diện hoặc vùng giao diện cần thiết kế:** một drawer dùng cho mười bước chỉ tính một thiết kế dùng chung, nhưng phải chứng minh phục vụ đủ yêu cầu của cả mười bước. Ngược lại, tên “Review chung” không được che việc các trạng thái và thông tin bên trong chưa được thiết kế.

**Thứ ba, số khoảng thiếu hợp đồng/dữ liệu:** không cộng số field, thuộc tính khai báo hay bảng dữ liệu vào số UI.

Đối với table, trước hết phải truy được **thông tin cần dùng → chủ quản → hợp đồng → nguồn đọc/ghi**. Chưa đủ căn cứ thì ghi rõ, không quyết số bảng từ số màn hình hoặc từ 119 khai báo logic trong lab.

## 4. Những UI có ba hoặc bốn phiên bản phải được xử lý thật

Trong từng bước, Codex phải đặt các ứng viên cạnh nhau và trả lời: **bản nào đúng logic nhất; phần nào đáng giữ từ bản khác; phần nào thiếu; phần nào trùng hoặc sai**.

Không chọn chỉ vì bản mới nhất, đẹp nhất hoặc có nhiều control nhất. Kết quả phải có danh sách giữ, hợp nhất, sửa và đề nghị ngừng dùng.

**Lượt lập bản đồ chưa xóa UI/code thật.** Trước khi loại bỏ phải biết nội dung cần bảo toàn, nơi thay thế và liên kết/consumer còn sử dụng. Như vậy mới dọn được các bản cũ mà không mất phần tư duy đã làm.

## 5. Trạng thái trong v1.6.18 cần sửa theo chỉ đạo mới

Tôi xác nhận hai điểm đang lệch với cuộc trao đổi gần nhất:

* **D04 vẫn ghi WAITING OWNER**, trong khi anh đã đồng ý D04-A. Lệnh mới ghi rõ quyết định Owner; không hỏi lại.
* **Gate1–2 vẫn thể hiện DONE**, trong khi phần kiểm độ đầy đủ Bước 1 đã được yêu cầu mở lại. Lệnh mới yêu cầu sửa trạng thái hiện hành, nhưng bảo toàn lịch sử và các bằng chứng đã đạt.

Gate3–4 giữ kết quả đã làm, **chưa tiếp tục khóa cuối hoặc mở Pilot**. Sáu gap mới sẽ được gắn vào đúng bước của bản đồ — đặc biệt đoạn giao việc, nhận input người dùng, bàn giao và MOUT — chứ không được gọi là “chỉ còn sáu việc”.

Sau khi lập bản đồ, phải **kiểm ngược Gate0**. Chỗ nào thiếu bước, mâu thuẫn quyền, không có nguồn thông tin hoặc buộc người nhớ quy trình thì phải đưa ra sửa thiết kế tại nguồn. Không ép mọi thứ vào baseline chỉ vì trước đây đã ghi “đã khóa”.

## 6. Hai tài liệu có vai trò rõ, không thành hai bộ nhớ cạnh tranh

**`cấu trúc hệ thống.html`** tiếp tục giữ kiến trúc, quyết định, trạng thái và lịch sử.

**`BAN-DO-BUOC-UI-AGENT.html`** giữ chi tiết từng bước và toàn bộ đối chiếu đủ/thiếu. SSOT dẫn tới tài liệu này, không chép lại toàn bộ ma trận.

Anh chỉ cần mở HTML mới để xem từng bước, thấy ngay thiết kế hiện hữu và phần còn trống. Các số tổng phải sinh từ cùng ma trận, không nhập tay ở nhiều nơi.

## Anh gửi Codex đúng **một file lệnh này**

[**Lệnh Codex — lập bản đồ từng bước/UI/Agent và rà lại đầy đủ Bước 1**](sandbox:/mnt/data/Lenh_Codex_Lap_Ban_Do_Buoc_UI_Agent_Ra_Lai_Buoc1.md)

Đây là **gói công việc kế tiếp thay cho hướng khép sáu gap rồi mở Pilot**. Codex phải làm trọn bản đồ, gắn thiết kế hiện hữu, kiểm đủ/thiếu từng thông tin, thống kê, rà ngược Gate0 và cập nhật SSOT trước khi báo cáo.

**Điều kiện hoàn thành không phải “đã xem hết UI”. Phải là: với từng bước hệ thống cần có, chúng ta chỉ được người thấy gì, máy làm gì, cái gì đã đủ, cái gì thiếu và cần sửa hoặc thiết kế thêm chính xác ở đâu.**
