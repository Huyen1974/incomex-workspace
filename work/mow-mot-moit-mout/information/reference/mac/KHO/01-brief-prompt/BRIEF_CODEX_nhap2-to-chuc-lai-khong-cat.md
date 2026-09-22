# BRIEF GỬI CODEX — TỔ CHỨC LẠI CHO NGẮN GỌN, **KHÔNG PHẢI CẮT BỚT**

> Vòng trước bạn làm gọn rất tốt về mặt kỹ thuật. Nhưng có 12 phần **nghiệp vụ thực tiễn** đã biến mất khỏi phần đang dùng.
> Vòng này: **giữ lại đủ, nhưng tổ chức ngắn gọn hơn.** Không quay lại 47 checkpoint, cũng không bỏ nghiệp vụ.

---

## 0. HAI VIỆC DUY NHẤT MÀ CẢ HỆ NÀY PHẢI LÀM ĐƯỢC

Owner tóm gọn — và đây là thước đo cuối cùng cho mọi quyết định thiết kế:

1. **Tạo được bất cứ quy trình nào một cách nhanh, đơn giản.**
2. **Sửa rẻ** — điều chỉnh một quy trình một cách đơn giản, **từ lúc có đề xuất cho tới khi ra được quy trình mới**.

Mọi thứ trong hệ tồn tại là để phục vụ hai việc này. Cái gì không phục vụ hai việc này thì đúng là nên cắt.

---

## 1. RANH GIỚI CẮT — luật quan trọng nhất của brief này

> **Cái gì thuộc CHUYÊN MÔN THỰC TIỄN thì không cắt được.**
> **Cái gì thuộc TỔ CHỨC KỸ THUẬT thì tái cấu trúc thoải mái — Owner ủng hộ.**

Hai vế đều bắt buộc:

- **Quá phức tạp → thất bại ở khâu triển khai.**
- **Cắt bớt nghiệp vụ → không chạy được trong thực tế.**

Phải cân cả hai, **không bỏ cái nào**.

### Được cắt / gộp / đổi thoải mái (tổ chức kỹ thuật)

Số miếng UI · số checkpoint · số bảng · số cột · số loại sự kiện · cách chia nhóm · số mục trong sổ · cách đánh mã nội bộ · cách hiển thị · thứ tự · tên gọi kỹ thuật.

**Bạn đã làm rất tốt phần này. Giữ nguyên tinh thần đó.**

### KHÔNG được mất (chuyên môn thực tiễn)

Danh sách ở mục 3. Chúng có thể **đổi hình dạng** — gộp vào một bước, thành một trường, thành một dòng trong bảng — nhưng **không được biến mất**.

---

## 2. NHÁP 1 LÀ TỪ ĐIỂN — không phải bản để copy

`.../mow-process-draft-v1.html`

Nội dung ở đó **đã được duyệt về mặt chuyên môn**. Khi nghi ngờ một mục có phải nghiệp vụ thật hay không, tra ở đó.

Nhưng **đừng copy cấu trúc của nó** — cấu trúc đó chính là thứ chúng ta đang sửa. Lấy **nội dung**, bỏ **cách tổ chức**.

---

## 3. MƯỜI HAI PHẦN NGHIỆP VỤ ĐANG MẤT KHỎI NHÁP 2

Đã quét toàn bộ phần đang dùng của Nháp 2 (checks · help · model · registry · contract). Kết quả:

### Nhóm A — Đường đi của một thay đổi *(chính là việc số 2 của Owner)*

| # | Nghiệp vụ | Vì sao không cắt được |
|---|---|---|
| **1** | **Quy trình đề xuất cải tiến** | Đây là **đầu vào của toàn bộ việc "sửa rẻ"**. Không có nó thì không ai biết ý tưởng vào hệ bằng đường nào. Phải ghi: ai nêu · quy trình nào · vì sao · mong muốn đạt gì. |
| **2** | **Định tầng** | Người đề xuất **không phải biết** việc này thuộc MOW hay MOT hay form — người hiểu kỹ thuật xác định. Bỏ bước này là bắt người làm nghề phải hiểu kiến trúc. |
| **3** | **Duyệt nghiệp vụ** *(dấu thì còn, quá trình thì mất)* | **Cửa lọc rẻ nhất của cả hệ.** Chặn một ý tưởng ở đây tốn một phút; để lọt tới lúc kiểm thì đã tốn cả công dựng. Từ chối cũng **phải ghi lý do và giữ lại** — ý tưởng sai hôm nay có thể đúng sau sáu tháng. |
| **4** | **Bản mô tả cho người duyệt = máy sinh diff + người viết lý do** | Nếu chỉ có lời người viết thì **người duyệt ký vào một thứ, hệ thống chạy một thứ khác**. Đây là chỗ dễ hỏng nhất của mọi quy trình phê duyệt. |
| **5** | **Nhiều phiếu chờ, một phiếu đang dựng** | Không được chặn người ta **nêu** ý tưởng. Nhưng hai người cùng dựng hai bản trên một mã gốc rồi cùng đòi phát hành thì hỏng ngay ở khâu bật/tắt. |

### Nhóm B — An toàn khi đổi

| # | Nghiệp vụ | Vì sao không cắt được |
|---|---|---|
| **6** | **Nhân bản phải copy CẢ danh sách công việc** | Quên bước này thì bản mới **trông y hệt bản cũ nhưng rỗng** — không gọi ra công việc nào. Nhìn bằng mắt không thấy gì khác. |
| **7** | **Chưa sửa gì thì phải chạy y hệt bản cũ** | Đây là phép kiểm chứng duy nhất bắt được lỗi số 6. |
| **8** | **Bật mới + tắt cũ trong MỘT giao dịch** | Lỗi giữa chừng bằng hai lệnh rời = **hai bản cùng bật, hoặc không bản nào bật**. |
| **9** | **Nghỉ hưu ≠ khai tử** | Bản cũ tắt nhưng **nguyên vẹn**, gọi lại được. Đây là lưới an toàn: bản mới hỏng thì còn đường lùi. |
| **10** | **Khoá lúc gọi — đơn vị là LƯỢT** | Một lượt kéo dài vài ngày không được chạy bước đầu bằng công việc phiên bản 2 và bước cuối bằng phiên bản 3 — **một bộ linh kiện chưa từng được kiểm cùng nhau**. |

### Nhóm C — Vận hành thật

| # | Nghiệp vụ | Vì sao không cắt được |
|---|---|---|
| **11** | **Uỷ quyền khi vắng mặt** | Chị Lan nghỉ thì **chính chị** thêm chị Mai làm thay; không tự làm được thì **trưởng phòng** làm hộ. Thiếu cái này thì việc nằm im và **không ai biết** — vì mô hình của Incomex là không ai phải nhớ quy trình. |
| **12** | **Trả lại sửa: về đúng chỗ + đếm vòng** | Từ chối là **kết quả hợp lệ**, không phải lỗi. Nhưng trả lại — gửi lại vô hạn thì lượt "đang chạy" mãi không xong. |
| **13** | **Huỷ lượt không được xoá dữ liệu đã ghi** | Người bấm huỷ thường tưởng mọi thứ đã thu hồi. Tiền đã chi, kho đã xuất **vẫn nằm đó** — phải sinh việc xử lý hậu quả. |
| **14** | **Trưởng phòng xem được việc của cấp dưới** | Nguyên tắc phân quyền đầu tiên của hệ: **người được báo cáo có quyền xem việc của người thực hiện**. Đây là cách duy nhất phát hiện người vắng mặt mà chưa uỷ quyền. |

*(Đánh số tới 14 vì hai mục nhỏ nằm chung nhóm.)*

---

## 4. NHỮNG THỨ BẠN ĐÃ GIỮ ĐƯỢC — xin giữ nguyên

Đã kiểm và **còn đủ**: nhánh lỗi ba kiểu · thử lại · bàn giao có xác nhận · việc cần can thiệp · việc chỉ tính giờ · tải so với năng lực · tải quá thấp · chậm bất thường · tỷ lệ máy làm · đo nhiều mốc · phạm vi bốn tầng · quy ước đặt mã · bật lại phải kiểm tương thích · ba vai người.

Cấu trúc hai lớp **validator 10 luật + catalog 14 bằng chứng** là một thiết kế tốt. **Giữ.**

---

## 5. YÊU CẦU — NGẮN GỌN, KHÔNG PHẢI BỎ ĐI

Mười bốn mục trên **phải có mặt**, nhưng **được phép đổi hình dạng hoàn toàn**.

Một vài hướng để bạn cân nhắc *(gợi ý, không bắt buộc — bạn tự chọn cách)*:

- Phần lớn nhóm A là **các bước của quy trình "Thiết kế + phát hành"** — có thể nằm gọn trong chính quy trình đó thay vì thành mục riêng.
- Nhóm B phần lớn là **điều kiện của một bước** ("bật phiên bản") — có thể là danh sách điều kiện của bước đó.
- Nhóm C phần lớn là **nhánh của quy trình "Chạy + quan sát"**.
- Nếu một mục vừa là luật vừa là bước, **đừng viết hai lần** — viết ở bước, luật trỏ tới bước.

**Điều kiện duy nhất:** đọc Nháp 2 xong phải trả lời được hai câu:

1. *Một ý tưởng cải tiến đi từ đâu tới đâu, qua những ai?*
2. *Nếu bản mới hỏng thì quay về bằng đường nào?*

Hiện tại **cả hai câu đều không trả lời được** từ phần đang dùng của Nháp 2.

---

## 6. VÌ SAO PHẢI GIỮ QUY TRÌNH DẠNG BƯỚC

Nháp 2 đang mạnh hai thứ và thiếu một thứ:

| Lớp | Trả lời câu gì | Nháp 2 |
|---|---|---|
| **Ý ĐỊNH** — quy trình viết ra từng bước | *Công việc diễn ra thế nào? Ta muốn nó chạy ra sao?* | **thiếu** |
| **CẤU HÌNH** — validator + catalog | *Đã khai đủ chưa?* | mạnh |
| **THỰC TẾ** — sự kiện | *Đã xảy ra những gì?* | mạnh |

Muốn biết **"hệ có đang vận hành đúng ý định chuyên môn không"** thì phải so **ba lớp** với nhau. Bỏ lớp đầu thì chỉ còn *cấu hình khớp với chính nó* và *thực tế khớp với cấu hình* — **không ai trả lời được "nhưng đây có phải điều ta muốn không?"**

Hai quy trình lõi hiện chỉ có 5 và 7 dòng một câu. Xin viết đủ dạng bước: **điểm bắt đầu · các bước · điểm kết thúc · còn thiếu gì**. Vẫn ngắn — nhưng đủ để một người mới đọc và làm theo.

---

## 7. GIAO GÌ

1. Nháp 2 chạy được, **14 mục nghiệp vụ đã có mặt** — bằng hình dạng nào là tuỳ bạn.
2. **Bảng đối chiếu**: mỗi mục 1–14 → nằm ở đâu trong cấu trúc mới.
3. Chỗ nào bạn thấy **thực ra là tổ chức kỹ thuật chứ không phải nghiệp vụ** → nói rõ lý do, chúng tôi sẽ xem lại. Chúng tôi có thể phân loại sai.
4. Chỗ nào bạn **gộp được nhiều mục vào một** → nói rõ, đó chính là thứ chúng tôi muốn.
5. Xác nhận Nháp 1 vẫn chạy nguyên.

---

## 8. MỘT LƯU Ý VỀ CÁCH LÀM VIỆC

Chúng tôi có nhiều ngày để bàn từng ý; bạn chỉ có vài phút cho mỗi vòng. **Việc bạn chưa nắm hết ngữ cảnh là bình thường** — không phải lỗi.

Vì vậy khi bạn thấy một yêu cầu **vô lý hoặc quá đắt**, xin **hỏi lại hoặc phản biện**, đừng lặng lẽ bỏ. Ba lần trong ngày hôm qua bạn phản biện đúng và chúng tôi đã đổi theo bạn.
