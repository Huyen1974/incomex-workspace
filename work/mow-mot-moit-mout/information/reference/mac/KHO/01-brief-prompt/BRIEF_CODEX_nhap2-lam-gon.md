# BRIEF GỬI CODEX — TỰ SỬA **NHÁP 2** THEO ĐỀ XUẤT CỦA CHÍNH BẠN

> Báo cáo cắt độ phức tạp của bạn đã được chấp nhận phần lớn. Nay **bạn tự thực hiện nó** trên một bản nhân bản riêng.
> Kèm theo là **7 lưu ý về ngữ cảnh bạn chưa nắm** — có vài chỗ bạn đề nghị cắt lại đúng là **yêu cầu trực tiếp của Owner**, không phải thứ chúng tôi tự nghĩ ra.

---

## 1. HAI ĐƯỜNG DẪN — ĐỪNG NHẦM

| | Đường dẫn | Vai trò |
|---|---|---|
| **NHÁP 1** | `.../mow-process-draft-v1.html` | **MỐC SO SÁNH. TUYỆT ĐỐI KHÔNG ĐỤNG.** |
| **NHÁP 2** | `.../mow-master-nhap2-v1.html` | **Bạn làm việc ở đây.** |

Cả hai đã có trong khung 4 Mẹ → chip **MOW** → *Nháp 1* / *Nháp 2*.

Nháp 2 hiện là **bản sao y hệt** Nháp 1: 53 mục sổ · 10 miếng cột phải · 15 quy trình · 28 phép test · 19 mục bảng kiểm · badge 17.

---

## 2. LUẬT TUYỆT ĐỐI CỦA NHÁP 2

1. **KHÔNG sửa bất kỳ file nào đang phục vụ Nháp 1.** Sửa một dòng là Nháp 1 hỏng theo, và chúng tôi mất mốc so sánh.
2. **Chỉ tạo file mới tiền tố `nhap2-`.** Ví dụ `nhap2-core.js`, `nhap2-catalog.js`, `nhap2-render.js`.
3. **Chỉ sửa danh sách `<script>` trong `mow-master-nhap2-v1.html`**, ở khu đã đánh dấu.
4. File nạp sau **ghi đè biến toàn cục** — muốn thay hẳn một phần thì gán lại biến đó trong `nhap2-*.js`.
5. Muốn **bỏ hẳn một miếng** thì **gỡ thẻ `<script>`** khỏi Nháp 2 — **không xoá file**.

Đã có sẵn `nhap2-override.js` (đang trống) làm chỗ bắt đầu.

---

## 3. VIỆC CẦN LÀM — theo đúng đề xuất của bạn

Bốn việc bạn xếp là điều kiện trước khi sang MOT, làm theo thứ tự đó:

1. **Gộp 28 phép test + 19 readiness thành MỘT catalog kiểm ban hành.** Mỗi kiểm tra: mã · câu hỏi · mức chặn · tầng sửa · cách chạy · dòng vi phạm. Badge đếm mục chặn chưa đạt. Màn test là khung nhìn chi tiết của **cùng** catalog.
2. **Phân loại lại 15 "quy trình"** → 2 quy trình lõi + lệnh / job / nhánh / khung nhìn. **Đặt tên đúng loại** — đừng gọi tất cả là "quy trình" (luật *chữ phải đúng nghĩa*).
3. **Fan-in bằng bảng cạnh FK thật.** Chúng tôi rút lại đề xuất "danh sách bước cha trong một cột" — bạn đúng, không có phương án thứ ba.
4. **Đưa mục superseded ra khỏi sổ canonical** — `active:false` hoặc `BOOK_ARCHIVE`. Chỉ một mục canonical được hiện trong Help.

Cộng thêm, nếu còn sức:

5. Rút cột phải (10 miếng → ít hơn hẳn).
6. Rút 25 loại sự kiện → ~15-16, một hành động = một loại, kết quả ở `result_code`.
7. Trạng thái hiện tại **lưu trên `run` / `step_run`**, event chỉ là nhật ký. *(Chúng tôi nhận sai ở điểm này — luật "tính được thì cấm lưu" đã bị áp quá rộng.)*

---

## 4. ⚠️ BẢY LƯU Ý — NGỮ CẢNH BẠN CHƯA NẮM

Đây là phần quan trọng nhất của brief này. Có vài chỗ bạn đề nghị cắt **lại là yêu cầu trực tiếp của Owner**.

### 4.1 · KHÔNG được cắt — đây là yêu cầu nghiệp vụ của Owner

Bạn đề nghị bỏ khỏi vòng 1: *index chậm bất thường · tải quá thấp · đo kết quả nhiều mốc*.

**Không.** Owner nêu trực tiếp ba thứ này, có ví dụ cụ thể:

> *"Chị Lan chỉ có 6 tiếng làm việc mỗi ngày, nhưng tổng thời gian đang giao là 10 tiếng → không có cách nào hoàn thành đúng hạn. Đây là LỖI CỦA HỆ THỐNG, người điều hành phải can thiệp."*
> *"Chị Lan nghỉ ốm, vì lý do nào đó không thông báo được. Hệ thống có index chậm bất thường → admin lập tức được cảnh báo."*
> *"Chị Mai cùng chuyên môn nhưng quá ít việc — cả hai chiều đều phải ghi lại."*

Đây là **mục tiêu điều hành theo thời gian thực**, không phải trang trí. Bạn được phép **đơn giản hoá cách làm**, nhưng không được bỏ mục tiêu.

Ghi chú: phần lớn chúng **tính được** từ `step_run` — chỉ cần đúng một trường mới là *năng lực phút mỗi ngày của người*.

### 4.2 · Bảng "người" — PHẢI HỎI TRƯỚC, đừng dựng mới

Bạn nói đúng: *nếu hệ đã có bảng người/HR thì không dựng bảng người mới cho MOW*. Chúng tôi **chưa kiểm** việc này — đó là thiếu sót của chúng tôi.

**Đề nghị:** trong Nháp 2 để nó là **đầu chờ có ghi chú "nguồn ngoài, chưa xác nhận"**, đừng thiết kế chi tiết cho tới khi Owner trả lời.

### 4.3 · Hai miếng bạn đề nghị bỏ — chuyển, đừng xoá

*"Quy trình của MOW"* và *"Dữ liệu ghi lại"*: bạn đúng về nguyên tắc — chúng là tài liệu thiết kế, không phải dữ liệu của `WF-0001`.

Nhưng **đây là trang NHÁP**, và hai miếng đó chính là mặt bàn làm việc của chúng tôi lúc này. **Chuyển sang khu vực riêng** (một trang quản trị, hoặc một khu tách hẳn trong cùng trang), **không xoá**.

### 4.4 · Sổ 53 → 12-15 mục: giữ ARCHIVE có liên kết

Đồng ý canonical phải mỏng. Nhưng nhiều mục là **lý do đã bác một phương án** — Owner nói rõ muốn giữ để **không mở lại tranh luận cũ**.

**Đề nghị:** canonical mỏng + `BOOK_ARCHIVE` đầy đủ, mỗi mục canonical **có liên kết xuống mục archive tương ứng**. Không xoá lý do.

### 4.5 · Mô hình vận hành gốc — có thể bạn chưa nắm

**Không ai phải nhớ quy trình. Việc TỰ ĐẨY về dashboard của từng người, đúng thời điểm.**

- Anh A chỉ thấy việc của anh A. Việc không giao thì A **không có cách nào** biết nó ở đâu.
- Việc **phê duyệt** là việc khác, đẩy về **trưởng phòng** — nên A không có cách nào tự duyệt. Cơ chế mạnh hơn luật.
- **Không có hàng đợi chung để nhiều người tranh nhau nhặt.** Chữ "nhặt" là sai nghĩa; đúng là "nhận".
- Người **không đi tìm bản ghi — việc tìm đến người**.

Điều này làm **nhiều lo ngại về đồng thời nhỏ đi đáng kể**. Xin kiểm lại các đề xuất chống đồng thời của bạn dưới ánh sáng mô hình này.

### 4.6 · Phương pháp làm việc Owner yêu cầu — giữ nguyên

> **Có vấn đề → viết thành QUY TRÌNH (bước 1, 2, 3) → rà TỪNG BƯỚC xem cần THÔNG TIN gì → gom thành HỢP ĐỒNG THÔNG TIN + kiểm tính khả thi.**

Bạn được rút gọn kết quả, nhưng **đừng bỏ phương pháp**. Mỗi bước phải chỉ ra được **đọc gì / ghi gì / ở bảng nào** — bước nào không chỉ ra được nơi lưu thì đó là lỗ hổng.

### 4.7 · PG FIRST — bản chính xác

**Phạm vi: xử lý dữ liệu. Nguyên tắc: không được làm lại cái gì mà PG có thể xử lý.**

Giao diện · gọi ra ngoài · kết nối · việc chạy lâu thì **đương nhiên viết mã — không thuộc phạm vi, KHÔNG phải "ngoại lệ"**. (Chúng tôi từng dùng chữ "ngoại lệ" và Owner bác đúng: nói vậy làm nguyên tắc trông như có lỗ hổng.)

---

## 5. OWNER MUỐN GÌ Ở NHÁP 2

Nguyên văn: **"chủ yếu là đưa ra các nguyên tắc cho rõ ràng, các check point cần cụ thể."**

Nghĩa là ưu tiên theo thứ tự:

1. **Nguyên tắc rõ ràng** — ít, ngắn, không chồng nhau, mỗi cái một câu đọc là hiểu.
2. **Check point cụ thể** — mỗi kiểm tra phải nói được: kiểm cái gì · đạt là thế nào · hỏng thì trả về dòng nào · ai sửa.
3. Còn lại cắt.

Thước đo: **người mới nhìn Nháp 2 trong 5 phút có hiểu được hệ không?**

---

## 6. GIAO GÌ

1. **Nháp 2 chạy được** với thay đổi của bạn.
2. **Một trang / một mục ghi rõ ĐÃ CẮT GÌ** — bảng đối chiếu Nháp 1 ↔ Nháp 2 theo từng con số (mục sổ · miếng · quy trình · kiểm tra · loại sự kiện · bảng).
3. **Danh sách những gì bạn CỐ Ý GIỮ** dù có vẻ thừa, kèm lý do.
4. **Danh sách những gì bạn KHÔNG cắt được** vì vướng lưu ý ở mục 4, kèm đề nghị hỏi Owner.
5. Xác nhận **Nháp 1 vẫn chạy y nguyên** — mở lại và kiểm, đừng chỉ nói.

---

## 7. TỰ KIỂM TRƯỚC KHI GIAO

1. Mở **Nháp 1**, xổ đủ 10 miếng, bấm badge — còn nguyên vẹn chứ?
2. Mở **Nháp 2**, xổ hết các miếng còn lại — có chỗ nào vỡ không?
3. Có file nào **không mang tiền tố `nhap2-`** bị sửa không? Nếu có, hoàn lại.
4. Bảng đối chiếu số liệu Nháp 1 ↔ Nháp 2 đã có chưa?
5. Bảy lưu ý ở mục 4 — đã đọc và tôn trọng đủ chưa? Chỗ nào không đồng ý thì **nói rõ lý do**, đừng lặng lẽ cắt.
