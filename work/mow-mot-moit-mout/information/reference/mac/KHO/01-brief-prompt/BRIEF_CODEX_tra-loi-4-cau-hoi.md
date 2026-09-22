# TRẢ LỜI BỐN CÂU HỎI CỦA CODEX + YÊU CẦU VÒNG TIẾP

> Cảm ơn vì đã **hỏi trước khi sửa**. Đó đúng là cách làm chúng tôi muốn.
> Một trong bốn câu cho thấy **cả bạn và chúng tôi đều đang thiết kế sai bản chất** — câu 3. Xin đọc kỹ phần đó nhất.

---

## LUẬT LÀM VIỆC — đặt lên đầu vì nó giải thích vì sao có brief này

> **KHÔNG CHẮC ĐÚNG = SAI. Đừng quyết định trên dữ liệu chưa chắc chắn. Cái gì không biết thì HỎI LẠI.**

Vì sao cần luật này: bốn Mẹ liên quan chằng chịt. Phần "đề xuất cải tiến" **đã có sẵn trong MOW từ trước**, nhưng nội dung rộng quá nên không ai đọc hết — rồi **cả người lẫn agent** đều đi thiết kế lại một thứ đã có, theo cách sai.

Một câu hỏi tốn một phút. Một quyết định sai trên dữ liệu mơ hồ tốn cả vòng làm lại.

---

## Câu 1 — "Một bảng dữ liệu gốc"

**Trả lời: đúng như bạn đề nghị.**

**Một bảng lưu toàn bộ SỰ KIỆN đã xảy ra**, có khoá ngoại đổ về task (MOT) và bản ghi nghiệp vụ. Còn **định nghĩa · phiên bản · quan hệ · lượt · bước-lượt** vẫn là bảng vận hành riêng.

Lý do đúng như bạn nói: gộp cả trạng thái vận hành và cấu hình vào một bảng sự kiện thì **giao việc, khoá phiên bản và ban hành nguyên tử đều mất tin cậy**.

### ⚠️ Xin bỏ con số "100 dữ kiện" ra khỏi mọi tài liệu

Con số đó là **lỗi ghi chép của chúng tôi**. Owner có nói "khoảng 100 gì đó" **một lần**, rồi **ngay sau đó rút lại** — nhưng chúng tôi đã biến câu nói miệng đó thành **tiêu đề một mục trong sổ**, nên nó thành số chính thức và bạn đọc lại từ archive.

**Câu đúng: có bao nhiêu sự kiện thì bắt hết. Không có con số.**

---

## Câu 2 — Công thức tạo một MOT task

### Định nghĩa gốc, xin dùng làm chuẩn

> **CÔNG VIỆC, BẢN CHẤT, LÀ NHẬP LIỆU.**
> Mọi thứ khác là **hạ tầng và đầu vào** cho việc nhập liệu đó.

Từ đó suy ra:

- **Đúng MỘT form nhập (MOIT) cho một công việc.** Không có khái niệm nhiều form.
- Cần nhập nhiều thứ → **làm form nhiều trường**, không phải nhiều form.
- **Hai form = hai việc.**
- **Bấm xác nhận một cái cũng là một việc.**
- **MOUT lắp vào để người thực hiện RA QUYẾT ĐỊNH** — là thông tin tham khảo, không phải nơi ghi. Được nhiều.

### Hai hệ quả

- Việc do **máy làm** cũng là nhập liệu — máy ghi thay người. **Cùng một cấu trúc**, không cần loại riêng.
- **Việc dự phòng** (chỉ tính giờ) **không phải công việc** theo định nghĩa này. Nó là một khoảng chờ: không form, không người, không tham gia luồng. Bạn đã làm đúng với `WAIT_ONLY`.

### Công thức bạn nêu còn thiếu bốn thứ

Bạn viết: *form + vai người + thời gian + input/output + trigger/kết quả*.

Nháp 1 quy định MOT quản **10 thứ**. So với công thức của bạn thì thiếu:

1. **Loại việc** — thực hiện / kiểm tra / phê duyệt
2. **Bản ghi** (khoá phụ tới dữ liệu nghiệp vụ)
3. **Kiểu xử lý khi hỏng** — dừng / chuyển sự cố / bỏ qua
4. **Có chạy lại an toàn không** — quyết định được retry hay phải giao người đối chiếu

---

## Câu 3 — ⚠️ CÂU NÀY ĐỔI NHIỀU NHẤT

### Cả bạn và chúng tôi đều thiết kế sai bản chất

Chúng ta cùng coi "đề xuất" là **một phiếu thay đổi có cấu trúc** — có tầng, có linh kiện, có trạng thái, có vòng đời, có "một phiếu đang dựng". Nên mới sinh ra câu hỏi *"một đề xuất chạm nhiều Mẹ thì duyệt mấy lần, ban hành thế nào"*.

**Sai. Đề xuất không phải phiếu. Nó là MỘT DÒNG GÓP Ý.**

### Bản chất thật

**Mục đích:** lấy ý kiến **trực tiếp từ người làm, ngay lúc họ đang làm** — vì đó là lúc nhiều sáng tạo nhất. Vấn đề hiện nay là họ **không có công cụ để góp ý**.

**Nguyên tắc thiết kế:** *nhập liệu tối thiểu, thông tin tối đa.*

**Người thực hiện chỉ nhìn thấy đúng việc họ đang làm.** Họ **không biết** quy trình là gì, task là gì, MOIT và MOUT là gì — và **không cần biết**. **Đừng đặt vấn đề đó ra với họ.**

Phần lớn người thực hiện chỉ có khả năng nêu ý kiến về **sự hợp lý hay không hợp lý**. Còn **thiết kế được một quy trình thì phải người có chuyên môn**.

### Vì vậy

- Góp ý **chỉ mang tính TEXT**, **hoàn toàn không có tính chất thay đổi cấu trúc**. Kể cả khi họ viết *"bỏ bước này đi"* hay *"thêm một bước kiểm tra A B C"* — vẫn chỉ là text.
- Mỗi lần góp ý = **một dòng mới** trong danh sách đề xuất cải tiến.
- Gửi xong → **chuyển sang một hệ thống nháp để xem xét**.
- Người góp ý **gõ vài chữ là đủ**. Hệ tự gắn bối cảnh: ai · lúc nào · đang làm việc nào.
- **"Cái này thuộc một quy trình nào, một việc nào"** — **không phải việc của người góp ý**, đừng bắt họ quan tâm.
- **Việc tổng hợp và ghép lại là của ADMIN** — một hai người hiểu cả hệ thống. **Không cần giải thích gì với họ, tự họ ghép được.**

### Điều quan trọng nhất

**Không phải cứ đề xuất là sửa được ngay.** Đôi khi còn phải họp, và làm rất nhiều thao tác khác mới quyết định sửa.

> **Việc đó do CON NGƯỜI vận hành. Hệ thống chỉ khoá cứng đúng phần LẶP ĐI LẶP LẠI.**

### Ba thứ này biến mất khỏi thiết kế

Chúng là do chúng tôi tự nghĩ ra cho một bài toán **không tồn tại**:

- ~~Định tầng như một bước bắt buộc trong hệ~~ → admin tự làm khi ghép
- ~~Trạng thái phiếu năm chặng~~ → không có phiếu
- ~~"Một phiếu đang dựng trên một mã gốc"~~ → không có phiếu

**Câu hỏi "một đề xuất chạm nhiều Mẹ thì sao" cũng tan theo** — vì đề xuất không chạm Mẹ nào cả. Nó chỉ là chữ.

### Ranh giới sạch

**Đề xuất là ĐẦU VÀO của quy trình thiết kế, không phải bước đầu tiên của nó.**
Quy trình thiết kế bắt đầu khi **admin quyết định sửa**.

---

## Câu 4 — Nguồn người và uỷ quyền

### Nguyên tắc: MỘT bảng nhân sự

Tư duy **lắp ráp từ dưới lên**. Người phải nằm trong **bảng nhân sự**, và **chỉ một bảng**. Người kiểu gì thì **phân loại ngay trong bảng đó**.

Phân loại bằng **nhãn**: nhân sự chính thức · cộng tác viên · nhà thầu · đơn vị vận chuyển… để lọc khi cần.

### Khi nào được tách bảng thứ hai

**Chỉ khi có lợi ích rất rõ ràng.** Ví dụ: một vị trí chỉ chọn **người liên lạc của khách hàng** — có thể tạo một mảng nhân sự riêng cho vị trí đặc thù đó, **để chọn cho nhanh**.

**Nguyên tắc chung: hạn chế thêm bảng mới cùng khái niệm.** Một bảng dễ quản lý hơn hai.

### Thứ tự ưu tiên khi cân nhắc

1. **Thao tác của người thực hiện phải nhanh nhất có thể** — ưu tiên số một, **vì đây là việc lặp đi lặp lại**.
2. **Rồi mới tới cấu trúc hệ thống đơn giản** — kết nối đỡ rắc rối, hạn chế sai lỗi, khoá ngoại đơn giản.

### ❓ Một điều chưa xác nhận — xin hỏi trước khi thiết kế

**Incomex đã có bảng nhân sự sẵn chưa?** Và nếu có, nó đã có sẵn quan hệ **ai báo cáo cho ai** chưa?

Chúng tôi **chưa xác nhận được**. Theo đúng luật ở đầu brief — **không chắc đúng = sai** — xin bạn **hỏi lại Owner** thay vì tự quyết. Nếu chưa có thì mới dựng; nếu có rồi thì chỉ nối vào.

Tương tự với **năng lực phút mỗi ngày** và **uỷ quyền khi vắng mặt**: theo nguyên tắc một bảng thì chúng là **cột trong bảng nhân sự**. Nhưng uỷ quyền có khoảng *từ ngày – đến ngày*, nên nếu thực tế một người có thể uỷ quyền nhiều lần chồng nhau thì có thể cần bảng nhỏ riêng. **Xin hỏi trước.**

---

# YÊU CẦU VÒNG TIẾP

## 1 · Thứ tự sinh ra mọi thứ

> **YÊU CẦU → QUY TRÌNH → rồi mới đến những thứ khác** (bảng, hợp đồng, UI, mã).

Không bao giờ đi ngược. Phần yêu cầu và quy trình **rất ngắn và đơn giản** — viết ra một lần, **đọc lại hàng chục, hàng trăm lần** sau đó. Đó là khoản **rẻ nhất** trong cả dự án.

## 2 · CHUẨN VIẾT MỘT QUY TRÌNH — mới bổ sung, bắt buộc áp dụng

Một quy trình phải có **ba phần**, và **cả ba đều viết cực ngắn**:

| Phần | Nội dung |
|---|---|
| **ĐIỂM BẮT ĐẦU** | một câu |
| **CÁC BƯỚC** | mỗi bước một dòng |
| **ĐIỂM KẾT THÚC** | một câu |

### Vì sao hai đầu quan trọng ngang các bước

> **Hai quy trình có thể ĐỀU ĐÚNG mà công việc vẫn không chạy — vì giữa chúng có một KHOẢNG TRỐNG.**

Không định nghĩa rõ hai đầu thì hệ sẽ **đẻ ra rất nhiều khoảng trống**, và không ai nhận phần rơi vào đó.

**Cách kiểm:** xếp các quy trình nối nhau, đọc **điểm kết thúc của cái trước** và **điểm bắt đầu của cái sau** — phải là **CÙNG MỘT sự kiện**. Nếu phải giải thích thêm một câu để nối hai đầu đó, thì **chính câu giải thích đó là khoảng trống**.

## 3 · Ghi lại các quy trình — ngắn gọn nhất có thể

Đây là yêu cầu chính của vòng này.

**Câu chuyện bắt đầu từ đâu:** quy trình **đầu tiên** của mọi thay đổi là **ĐỀ XUẤT CẢI TIẾN / NÂNG CAO trong MOW**. Đừng bắt đầu kể từ chỗ đang sửa — bắt đầu từ chỗ **ý tưởng vào hệ**.

Cấu trúc hai quy trình lõi + các nhánh mà bạn đề xuất — **chúng tôi đồng ý**. Xin viết đủ dạng bước theo chuẩn ở mục 2, và **giữ ngắn**.

**Lưu ý sau khi đọc câu 3:** quy trình "Thiết kế và phát hành" của bạn hiện bắt đầu bằng *đề xuất → định tầng → duyệt nghiệp vụ → chiếm lượt dựng*. Theo bản chất thật thì **ba bước đầu không thuộc quy trình này**:
- **Đề xuất** là một quy trình riêng, rất ngắn, và **do người thực hiện làm** (gõ vài chữ).
- **Định tầng và quyết định sửa** là **thao tác của con người**, có thể phải họp — hệ không mô hình hoá.
- Quy trình "Thiết kế và phát hành" **bắt đầu khi admin đã quyết định sửa**.

Đó chính là chỗ cần định nghĩa **điểm bắt đầu** cho rõ, nếu không sẽ có khoảng trống giữa "góp ý" và "bắt tay vào sửa".

## 4 · Vì sao phải ghi lại, dù thấy hiển nhiên

Chỉ một thời gian ngắn thôi là đã hiểu vấn đề khác đi — chuyện vừa xảy ra với chính "đề xuất cải tiến" hôm nay.

**Lười một chút lúc này, mất rất nhiều thời gian về sau.**

Nhìn vào code và UI thì bạn hiểu được một phần. Nhưng **quy trình nghiệp vụ thì không có tiêu chuẩn nào** — không ghi lại rõ ràng, khái niệm mập mờ, thì **rất dễ hiểu lầm và làm nhầm**.

---

# GIAO GÌ

1. **Các quy trình đã ghi lại**, theo chuẩn ba phần, **ngắn nhất có thể**.
2. **Kiểm khoảng trống**: xếp các quy trình nối nhau, chứng minh điểm kết thúc cái trước khớp điểm bắt đầu cái sau.
3. **Bảng đối chiếu** 14 mục nghiệp vụ → nằm ở bước nào.
4. **Câu hỏi gửi lại Owner** cho những gì bạn không chắc — đặc biệt chuyện bảng nhân sự. Đừng tự quyết.
5. Xác nhận Nháp 1 vẫn chạy nguyên, kèm tag Git trước–sau.
