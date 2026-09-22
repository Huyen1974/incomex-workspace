# BRIEF GỬI CODEX — MƯỜI NHIỆM VỤ NGHIỆP VỤ NHÁP 2 CÒN THIẾU

> **Cách đọc brief này:** chúng tôi mô tả **NHIỆM VỤ** và **KHI NÀO COI LÀ XONG**.
> Chúng tôi **KHÔNG chỉ đạo cách làm**. Bạn tự đề xuất, tự xử lý — chúng tôi xem kết quả rồi cho ý kiến.
> Nếu bạn có cách đơn giản hơn cách chúng tôi từng làm ở Nháp 1, cứ làm theo cách của bạn.

---

## 0. VÌ SAO CÓ BRIEF NÀY

Hướng làm gọn của bạn **đúng** và chúng tôi giữ. Nhưng khi đối chiếu Nháp 2 với Nháp 1, chúng tôi thấy:

- **27/28 khái niệm nghiệp vụ vẫn còn dấu vết chữ** → bạn không xoá nội dung.
- Nhưng **checkpoint đi từ 47 xuống 14**, và khi soi từng luật xem *còn ai canh không* thì **có 10 nhiệm vụ nghiệp vụ không còn nơi nào canh**.

Nghĩa là chúng chỉ còn nằm trong văn xuôi. Ở dự án này chúng tôi đã học được một bài rất đắt:

> **Ghi vào tài liệu chỉ là cửa thứ nhất. Ghi mà không có gì cưỡng chế thì vài tuần sau sẽ có người phát hành một quy trình thiếu đúng thứ ta đã biết là thiếu — và họ không có lỗi, vì hệ đã bảo là đủ.**

Vì vậy: **không cần quay lại 47 checkpoint.** Chỉ cần 10 nhiệm vụ dưới đây **có nơi cưỡng chế**, bằng cách nào là tuỳ bạn.

---

# PHẦN A — NĂM NHIỆM VỤ CHẶN

## A1 · Việc hỏng thì quy trình đi đâu

**Nhiệm vụ.** Khi một công việc trong quy trình hỏng, hệ phải biết phải làm gì tiếp — và phải có người được báo.

**Chuyện thật.** Quy trình Nhập kho, bước "Đối chiếu tồn kho" hỏng. Có ba cách xử khác nhau và Incomex dùng **cả ba, tuỳ theo việc**:
- Dừng cả quy trình và báo người phụ trách.
- Chuyển sang một quy trình xử lý sự cố.
- Ghi lỗi rồi chạy tiếp các bước không phụ thuộc.

Cách xử là **thuộc tính của chính công việc đó** (việc nào cũng mang theo cách hỏng của nó), nhưng **đích nhận** thì thuộc quy trình.

**Hỏng thế nào nếu thiếu.** Việc hỏng → hệ không biết làm gì → **im lặng đứng**. Không lỗi kỹ thuật nào, không ai được báo. Vài ngày sau mới có người hỏi "sao hàng chưa vào kho".

**Coi là xong khi.** Không thể phát hành một quy trình mà trong đó có công việc chưa khai cách xử khi hỏng, hoặc đã khai "dừng và báo" mà chưa khai **báo cho ai**, hoặc đã khai "chuyển sự cố" mà **quy trình sự cố đó không tồn tại / không đang chạy**.

---

## A2 · Nối hai quy trình với nhau

**Nhiệm vụ.** Quy trình Nhập kho chạy xong phải bàn giao được sang Quy trình Xuất kho, và phải biết chắc **bên kia đã nhận**.

**Chuyện thật.** Trong một chuyên môn, các quy trình nối nhau thành chuỗi. Nhập kho xong → phát tín hiệu → Xuất kho bắt đầu. Nhưng tín hiệu chỉ là tín hiệu: bên nhận còn phải biết **làm việc trên đơn hàng nào**.

**Hỏng thế nào nếu thiếu.** Ba kiểu hỏng, **cả ba đều âm thầm**:
- Tín hiệu ra không khớp tín hiệu vào của quy trình sau → **chuỗi đứt**, hai quy trình đều "chạy đúng", chỉ là không nối được với nhau.
- Tín hiệu có mà không mang mã bản ghi → quy trình sau **không biết xử đơn hàng nào**.
- Bên A ghi xong, việc gửi tín hiệu hỏng → **B không bao giờ được tạo, mà A tưởng đã bàn giao**. Chỉ lộ khi đối chiếu "A đã xong nhưng B không có lượt nào".

**Coi là xong khi.** Trả lời được ba câu: *tín hiệu ra có khớp bên nhận không* · *bàn giao có mang theo bản ghi cụ thể không* · *bên nhận đã xác nhận chưa*. Và khi chưa xác nhận thì **nhìn thấy được là đang chờ**, không phải coi như xong.

---

## A3 · Bước sau lấy dữ liệu từ đâu

**Nhiệm vụ.** Mỗi công việc cần dữ liệu gì mới làm được, và dữ liệu đó lấy từ bước nào.

**Chuyện thật.** Bước 5 "Phê duyệt nhập kho" cần **số lô** và **số lượng thực nhận**. Hai thứ đó do bước 3 và bước 4 tạo ra. Nếu bước 3 không ghi số lô, bước 5 vẫn được đẩy về dashboard người duyệt — và người đó ngồi nhìn một phiếu trống.

**Hỏng thế nào nếu thiếu.** Bước sau **luôn chạy với dữ liệu rỗng** mà không có gì báo lỗi. Hệ vẫn "chạy đúng", chỉ là ra số vô nghĩa. Nếu bước đó do agent làm thì **không ai thấy** cho tới lúc đối soát.

*(Ghi chú: đây là chỗ chúng tôi đánh giá thiếu nặng nhất khi rà từng bước ở Nháp 1. R06 hiện nay hỏi về khoá ngoại tới bảng nghiệp vụ — đó là chuyện khác.)*

**Coi là xong khi.** Với mỗi công việc, trả lời được: *cần dữ liệu gì* và *lấy từ đâu*; và khi thiếu thì **việc không đi tiếp một cách im lặng** mà phải lộ ra là đang thiếu gì, ai phải cung cấp.

---

## A4 · Sửa một quy trình đang chạy mà không làm hỏng nó

**Nhiệm vụ.** Sửa quy trình là **nhân bản ra bản mới rồi sửa**, bản đang chạy không bị đụng. Nhưng việc nhân bản phải **đầy đủ**.

**Chuyện thật và cái bẫy.** Nhân bản không phải chỉ copy thông tin quy trình — phải copy **cả danh sách công việc mà nó gọi**. Quên bước đó thì bản mới **trông y hệt bản cũ nhưng rỗng**: không gọi ra công việc nào. Nhìn bằng mắt **không thấy gì khác**.

Tương tự khi **bật lại một bản cũ**: bản cũ gọi công việc theo mã gốc, mà công việc nay đã sang phiên bản khác — nên *"quay về nguyên trạng"* là **không đúng**, phải kiểm mới biết còn chạy được không.

**Hỏng thế nào nếu thiếu.** Phát hành một bản rỗng, hoặc bật lại một bản cũ nay đã không tương thích. Cả hai đều **không báo lỗi lúc phát hành**, chỉ hỏng lúc chạy thật.

**Coi là xong khi.** Trả lời được: *bản mới nhân bản đã đủ chưa* · *chưa sửa gì thì có chạy y hệt bản cũ không* · *bản cũ định bật lại có còn tương thích không*.

---

## A5 · Ai đã cho phép phát hành, và dựa trên bằng chứng gì

**Nhiệm vụ.** Một phiên bản chỉ được phát hành khi có đủ **ba loại phê duyệt khác nhau**, và dấu duyệt kỹ thuật phải **dựa trên bằng chứng**, không phải cảm tính.

**Chuyện thật.** Ba câu hỏi hoàn toàn khác nhau, ba người khác nhau, ba thời điểm khác nhau:
- **Nghiệp vụ**: "Ý tưởng này có đáng làm không?"
- **Kỹ thuật**: "Nó chạy được chưa?"
- **Pháp lý**: "Cho cả hệ thống làm theo chưa?"

Gộp ba cái thành một nút thì người ký cuối phải chịu cả ba loại trách nhiệm mà họ **không đủ chuyên môn để chịu** — đó là cách nhanh nhất biến phê duyệt thành hình thức.

**Hỏng thế nào nếu thiếu.** Ai đó bấm "kỹ thuật đạt" mà chưa chạy gì. Sáu tháng sau không ai chứng minh được lúc đó đã kiểm những gì.

*(Ghi chú: R12 hiện hỏi "ai được sửa, duyệt, phát hành" — đó là **phân quyền**, khác với "đã đủ dấu chưa".)*

**Coi là xong khi.** Trả lời được: *đã đủ ba dấu chưa* · *dấu kỹ thuật dựa trên lần kiểm nào* · *lần kiểm đó chạy theo bộ kiểm phiên bản nào*.

---

# PHẦN B — NĂM NHIỆM VỤ NÊN CÓ

## B6 · Người duyệt từ chối thì đi đâu

**Nhiệm vụ.** Từ chối phê duyệt là **kết quả hợp lệ**, không phải lỗi. Phải có đường quay lại sửa, và đường đó phải có điểm dừng.

**Chuyện thật.** Trưởng phòng xem phiếu, thấy sai số lượng, trả lại cho người làm sửa. Sửa xong gửi lại. Nhưng nếu cứ trả lại — gửi lại mãi thì lượt **vẫn "đang chạy"** mà không bao giờ xong.

**Hỏng thế nào nếu thiếu.** Ép từ chối vào nhánh lỗi → hệ **báo sự cố cho một việc hoàn toàn bình thường**. Hoặc không có đường lùi → quy trình đứng im.

**Coi là xong khi.** Từ chối quay về **đúng chỗ đã định trước** (không quay tuỳ ý), và **quá số vòng cho phép thì chuyển người quản lý quyết**, không tự chạy vòng vô hạn.

---

## B7 · Đo tiến độ tự động hoá

**Nhiệm vụ.** Biết được mỗi quy trình hiện **máy làm bao nhiêu phần, người làm bao nhiêu phần**, và so với **mức mong muốn** đã khai lúc đề xuất cải tiến.

**Chuyện thật.** Mục tiêu dài hạn của Incomex là **tăng tỷ lệ việc do agent làm, giảm việc người làm**. Đề xuất cải tiến có khai "mong muốn: chỉ máy làm" — nếu sau khi làm xong thực tế vẫn còn việc người làm thì **chưa đạt mục tiêu**, và điều đó phải nhìn thấy được.

**Hỏng thế nào nếu thiếu.** Không có thước đo thì không biết cả hệ đang tiến hay lùi. Đây là **chỉ số chiến lược**, không phải số trang trí.

**Coi là xong khi.** Nhìn được **tỷ lệ máy làm thực tế** và **lệch so với mong muốn** — không phải điền tay, mà tính ra từ dữ liệu đã có.

---

## B8 · Việc chỉ tính giờ, không ai làm

**Nhiệm vụ.** Trong quy trình có loại việc **chỉ chiếm thời gian chứ không ai thực hiện** — ví dụ "Chờ kiểm đếm 15 phút". Nó phải được cộng vào tổng thời gian nhưng **không tham gia luồng công việc**.

**Hỏng thế nào nếu thiếu.** Việc kiểm quan hệ giữa các bước sẽ coi nó là **bước mồ côi** và **báo lỗi giả mỗi lần chạy**. Báo động giả lặp lại nhiều lần thì người ta ngừng đọc báo động — rồi báo động thật cũng bị bỏ qua.

**Coi là xong khi.** Việc loại này được cộng giờ, không bị đòi người thực hiện, và **không sinh cảnh báo giả**.

---

## B9 · Việc nằm im mà không ai biết

**Nhiệm vụ.** Có một nơi duy nhất nhìn thấy mọi việc **không chết nhưng cũng không đi tiếp**.

**Chuyện thật.** Thiếu dữ liệu đầu vào · chờ bên kia xác nhận bàn giao · mất liên lạc với agent · quá hạn · chưa ai nhận. **Không cái nào là lỗi kỹ thuật**, nên không nơi nào báo. Mà mỗi bộ phận chỉ nhìn danh sách việc của mình → **không ai nhìn thấy chúng cả**.

Đặc biệt: mô hình của Incomex là **việc tự đẩy về đúng một người, không ai phải nhớ quy trình**. Ưu điểm là không cần đào tạo — nhưng **nhược điểm là khi việc kẹt thì cũng không ai nhớ để đi tìm**.

**Hỏng thế nào nếu thiếu.** Việc nằm im vô hạn. Phát hiện bằng cách khách hàng gọi điện.

**Coi là xong khi.** Có nơi gom hết các trường hợp đó, mỗi dòng biết **ai chịu trách nhiệm** và **nằm bao lâu rồi**; và mỗi quy trình có một người nhận những ngoại lệ **không có chủ**.

---

## B10 · Đọc mã là hiểu được một chút

**Nhiệm vụ.** Với hàng chục ngàn quy trình, mã phải giúp con người định vị ngay: **cái này thuộc phạm vi nào, loại gì**.

**Chuyện thật.** Owner yêu cầu trực tiếp hôm nay. Đây là thứ duy nhất trong mười mục mà chúng tôi **không tìm thấy dấu vết** trong Nháp 2.

Có hai họ mã, đừng trộn:
- Mã **đối tượng nghiệp vụ** (quy trình, công việc cụ thể): máy cấp, người không gõ, hàng chục ngàn cái, người không cần đọc hiểu.
- Mã **thành phần của hệ** (checkpoint, quy trình quản trị, loại sự kiện): người đặt, ít, cố định, và **người phải đọc hiểu ngay**.

Một luật đã chốt cần giữ: **chỉ được nhét vào mã những thứ bất biến trọn đời**. Loại đối tượng thì được (một quy trình không bao giờ thành một công việc). Phòng ban, tên, trạng thái thì cấm — vì mai đổi thì mã **nói dối**.

**Coi là xong khi.** Nhìn một mã bất kỳ trong hệ là biết nó thuộc đâu, loại gì; và cách đặt mã áp **nhất quán** cho mọi họ mã do người đặt.

---

# PHẦN C — MỘT LỖI CẦN SỬA

Báo cáo bàn giao ghi *"10 khối bên phải → đúng 3 khối"*.

Thực tế cột phải đang có **7 khối**: 3 khối mới của Nháp 2, **cộng 4 khối cũ của Nháp 1 vẫn còn nguyên** (Đường dẫn 7 tầng · Bảng PG kết nối · Danh sách khoá ngoại · Help).

Thêm cái mới mà chưa gỡ cái cũ — đúng loại lỗi chúng tôi đã mắc nhiều lần trong ngày. Xin gỡ, hoặc nếu cố ý giữ thì nói rõ lý do.

---

# GIAO GÌ

1. **Nháp 2 chạy được** với 10 nhiệm vụ trên đã có nơi cưỡng chế.
2. **Bảng đối chiếu**: mỗi nhiệm vụ A1–B10 → bạn giải bằng cách nào, nằm ở đâu.
3. **Chỗ nào bạn không đồng ý** là nhiệm vụ thật → nói rõ lý do, đừng lặng lẽ bỏ.
4. **Chỗ nào bạn giải được rẻ hơn** cách Nháp 1 từng làm → nói rõ, chúng tôi muốn học.
5. Xác nhận **Nháp 1 vẫn chạy y nguyên** — mở lại và kiểm.

**Nhắc lại:** chúng tôi mô tả nhiệm vụ, **không chỉ đạo cách làm**. Nếu 10 nhiệm vụ này giải được bằng 3 checkpoint thay vì 10, càng tốt. Điều duy nhất không chấp nhận được là **nhiệm vụ có thật mà không nơi nào canh**.
