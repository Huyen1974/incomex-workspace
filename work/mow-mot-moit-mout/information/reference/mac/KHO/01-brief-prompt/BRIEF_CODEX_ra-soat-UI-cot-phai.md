# BRIEF GỬI CODEX — ĐỌC KỸ CỘT PHẢI, RÀ VÊNH/THIẾU, VÀ **PHẢN BIỆN QUYẾT LIỆT CHỖ PHỨC TẠP**

> Việc chính của vòng này **không phải tìm thêm thứ để thêm vào**.
> Việc chính là **cắt bớt**. Chúng tôi đã thêm rất nhiều trong một ngày và cần một cái đầu lạnh kéo mọi thứ về đơn giản nhất có thể mà vẫn đạt mục tiêu.

---

## 0. VÌ SAO VÒNG NÀY LÀ VÒNG CẮT

Con số tăng trưởng trong **một ngày**:

| Hạng mục | Đầu ngày | Hiện tại |
|---|---:|---:|
| Mục trong sổ (Help) | 16 | **53** |
| Miếng ở cột phải | 7 | **10** |
| Quy trình của hệ | 0 | **15** |
| Phép test | 19 | **28** |
| Mục bảng kiểm ban hành | 11 | **19** |
| Dòng đầu chờ (Quan hệ phụ thuộc) | ~40 | **74** |

Không có gì đảm bảo tất cả những thứ thêm vào đều **đáng tồn tại**. Nguyên tắc của Owner là **"phức tạp là chết"** — và tốc độ tăng ở trên là đúng thứ ông ấy sợ.

**Xin bạn vào với tâm thế của người phải bảo vệ ngân sách phức tạp.** Mỗi khái niệm phải tự biện minh. Cái nào không biện minh được thì đề nghị **bỏ hẳn**, không phải "để sau".

---

## 1. NƠI XEM

```
https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-process-draft-v1.html
```

Bấm một dòng bất kỳ → mở drawer. **Cột phải là trọng tâm của vòng này.** Có đúng **10 miếng**, tất cả gấp gọn, **bấm tiêu đề mới xổ ra** — xin xổ hết cả 10:

1. Quản lý phiên bản quy trình
2. Quan hệ phụ thuộc *(74 dòng, 4 nhóm nguồn)*
3. Vòng đời thay đổi *(5 chặng, nút ở trạng thái khoá)*
4. Danh mục test kỹ thuật *(28 phép, catalog v5)*
5. Đường dẫn 7 tầng + tên cụ thể
6. Bảng PG kết nối
7. Danh sách khoá ngoại
8. Help · quy trình (MOW) *(cửa vào sổ gốc)*
9. Quy trình của MOW *(15 quy trình, 2 nhóm)*
10. Dữ liệu ghi lại *(mới nhất — 9 bảng · sự kiện 11 cột · 25 loại)*

Badge đầu drawer **"còn 17 điểm cần bổ sung để chạy"** — **bấm được**, bung ra bảng kiểm 19 mục.

### Đọc dữ liệu — dump từ console

```js
copy(JSON.stringify({
  book:      window.BOOK,               // sổ gốc, 53 mục, 4 phần chung/mow/mot/form
  scope:     window.MOW_DRAWER_SCOPE,   // phạm vi + quan hệ phụ thuộc
  lifecycle: window.MOW_LIFECYCLE,      // 5 chặng thay đổi
  testplan:  window.MOW_TESTPLAN,       // 28 phép, catalog v5
  readiness: window.MOW_READINESS,      // bảng kiểm 19 mục
  quytrinh:  window.MOW_SELFPROCESS,    // 15 quy trình master.qt.01…15
  mohinh:    window.INCOMEX_MOHINH      // 9 bảng · 11 cột sự kiện · 25 loại
}, null, 2));
```

> ⚠️ Các file sửa theo lối **nối thêm, khối sau ghi đè khối trước**. **Đọc giá trị biến sau khi trang chạy**, đừng đọc file thô — sẽ đọc phải bản đã bỏ.

---

## 2. NGUYÊN TẮC ĐÃ CHỐT — dùng làm thước đo

| Luật | Nội dung |
|---|---|
| **Phức tạp là chết** | Giữa hai giải pháp cùng kết quả, chọn cái ít khái niệm hơn, ít bảng hơn, ít bước hơn |
| **PG FIRST** | Phạm vi: xử lý dữ liệu. Không làm lại cái gì PG xử lý được. Giao diện · gọi ra ngoài · kết nối thì đương nhiên viết mã — **không thuộc phạm vi, không phải "ngoại lệ"** |
| **Ghi DỌC** | Cột cố định, tăng dòng. Không thêm cột theo số việc |
| **Người không nhập** | Ứng dụng gửi 3 thứ (mã bước · loại sự kiện · kết quả), PG tự suy phần còn lại |
| **Khoá ngoại THẬT** | Không dùng cặp (tên bảng, mã bản ghi) — PG không canh được gì |
| **Muốn nhìn ở đâu thì làm KHUNG NHÌN ở đó** | Đừng chép dữ liệu tới đó |
| **Tính được thì cấm lưu** | Trạng thái hiện tại là khung nhìn, không phải cột |
| **Ưu tiên PHÁT HIỆN hơn NGĂN CHẶN** | Ghi rồi quét tốn một cột; chặn tốn cả cơ chế và vẫn bị lách |
| **Việc tìm đến người** | Không ai đi tìm bản ghi. Việc đẩy về dashboard đúng người, đúng lúc |
| **Một cỗ máy, nhiều đối tượng** | MOW/MOT/MOIT/MOUT dùng chung, không đẻ bảng riêng |
| **Chữ phải đúng nghĩa** | Đặt tên theo đúng hệ quả vận hành |
| **Danh mục kiểm phải cố định** | Dãy cố định áp lên số dòng thay đổi |

---

## 3. BA VIỆC — theo thứ tự ưu tiên

### ⭐ VIỆC 1 (QUAN TRỌNG NHẤT) · PHẢN BIỆN QUYẾT LIỆT CHỖ PHỨC TẠP

Với **từng miếng** trong 10 miếng, và với **từng khái niệm** trong đó, hỏi thẳng:

- **Bỏ hẳn cái này thì mất gì?** Nếu không mất gì rõ ràng → đề nghị bỏ.
- **Có gộp được với cái khác không?** Hai thứ na ná nhau thì sớm muộn sẽ lệch nhau.
- **Có đang giải một bài toán không tồn tại không?** *(Chúng tôi đã mắc lỗi này hôm nay: dựng cả một tình huống "hai người cùng sửa một đơn hàng" — trong khi mô hình đẩy việc làm nó không thể xảy ra.)*
- **Có đang giải bài toán khó hơn cần thiết không?** Vòng 1 chấp nhận giới hạn, miễn là **ghi rõ giới hạn**.
- **Người mới nhìn vào có hiểu trong 5 phút không?** Nếu không, chỗ nào là chỗ rối nhất?

**Những chỗ chúng tôi tự nghi ngờ nhất, xin soi trước:**

| Nghi ngờ | Câu hỏi |
|---|---|
| **28 phép test, 7 nhóm (A–G), 4 câu hỏi** | Có thừa không? Nhóm nào thực chất là một? Có phép nào trùng ý với mục bảng kiểm đến mức thừa? |
| **19 mục bảng kiểm** vs **28 phép test** | Hai danh sách này có đang chồng nhau không? Có nên là MỘT không? |
| **15 quy trình** chia 2 nhóm | Có quy trình nào thực chất là bước của quy trình khác? *(Chúng tôi đã gộp "duyệt" và "kiểm tra" vào rồi — còn cái nào nữa không?)* |
| **74 dòng đầu chờ** | Có dòng nào là ghi chú chứ không phải mối nối thật? |
| **25 loại sự kiện** | Có loại nào gộp được? |
| **9 bảng** | Có bảng nào là cột của bảng khác? Đặc biệt: **uỷ quyền** (5 cột) có đáng một bảng riêng không? |
| **Ba cột neo** (lượt · phiên bản · đề xuất) trên bảng sự kiện | Có cách đơn giản hơn không? |
| **Cột chủ thể riêng cho từng loại** trên bảng lượt | Chúng tôi chọn cách này thay vì bảng trung gian. Đúng không? |

**Xin đừng ngại đề nghị bỏ thứ vừa làm hôm nay.** Nếu bạn thấy nên bỏ phần lớn, hãy nói — điều đó có giá trị hơn nhiều so với thêm mười điểm nhỏ.

### VIỆC 2 · VÊNH TRÊN UI

Kiểm chéo **bốn mặt**: SỔ ↔ MIẾNG TRÊN MÀN HÌNH ↔ QUY TRÌNH ↔ HỢP ĐỒNG/BẢNG.

Bệnh tái đi tái lại của dự án này. Riêng hôm nay chúng tôi tự bắt được **6 chỗ vênh** ở một vòng và **4 chỗ nữa** ở vòng sau — tất cả đều do *thêm mục mới mà quên sửa mục cũ nói cùng chuyện*.

Cách kiểm thực tế: lấy một con số hoặc một luật bất kỳ trên màn hình, đi tìm nó ở ba nơi còn lại. Không tìm thấy, hoặc tìm thấy bản khác → vênh.

**Đặc biệt để ý:** một số mục cũ trong sổ đã bị **dán nhãn** *"bản cũ — xem mục CHỐT SỐ"* thay vì xoá. Xin kiểm xem cách dán nhãn đó có đủ rõ không, hay vẫn gây nhầm.

### VIỆC 3 · THIẾU TRÊN UI

- Miếng nào **nói mà không có đầu chờ**, hoặc **có đầu chờ mà sổ không nói**?
- Có thông tin nào người vận hành cần mà **không miếng nào hiện**?
- Thứ tự 10 miếng có hợp lý không? Cái nào nên lên trên / xuống dưới / **gộp vào nhau**?
- Có miếng nào **không ai sẽ mở lần thứ hai** không? Nếu có thì bỏ.

---

## 4. TRẠNG THÁI THẬT — đừng báo lại

**Đã đủ 5 cửa** (sổ · quy trình · đầu chờ · phép test · bảng kiểm): toàn bộ nhóm CHẶN của cả hai vòng trước.

**Chưa đủ 5 cửa — 6 mục, chúng tôi biết rồi:** bằng chứng lúc đánh giá điều kiện · chặn người thực hiện tự duyệt · hạn phải xong · người vắng mặt · hai lượt cùng ghi một bản ghi · quy trình xử lý sự cố.
→ Chỉ cần trả lời: **có chặn việc sang MOT không**, và **có nên bỏ bớt cái nào không**.

**Ba chỗ chúng tôi đã bác bạn** — xin phản biện lại nếu vẫn cho là mình đúng:
1. Không chuyển tên/mô tả/neo cây xuống bảng phiên bản.
2. **Không cấm hội tụ (fan-in)** — thay bằng cho "bước cha" nhận danh sách.
3. Không dọn hết lối ghi nối-thêm ngay.

---

## 5. BÁO CÁO MONG MUỐN

Ba phần theo ba việc. Phần 1 để **đầu tiên và dài nhất**.

Mỗi mục:

| Phần | Nội dung |
|---|---|
| Vấn đề | một câu |
| Loại | **BỎ ĐƯỢC** · **GỘP ĐƯỢC** · VÊNH · THIẾU |
| Nằm ở đâu | miếng nào / mục sổ nào / mã nào |
| Bỏ/gộp thì mất gì | nói thẳng cái giá |
| Đề xuất | phương án đơn giản nhất |
| Mức | CHẶN · NÊN · ĐỂ SAU |

Kết thúc bằng **một đoạn thẳng thắn**:
- Nếu phải cắt **30%** số khái niệm hiện có, bạn cắt cái gì?
- MOW đã đủ đơn giản để sang MOT chưa? Nếu chưa, chỗ nào rối nhất?

---

## 6. XIN LƯU Ý

- **Chưa cần viết code, chưa cần sửa file.**
- **Thiên vị về phía CẮT.** Khi phân vân giữ hay bỏ — đề nghị bỏ, kèm cái giá phải trả. Chúng tôi thà bỏ nhầm rồi thêm lại, còn hơn giữ một thứ không ai dùng mà phải nuôi mãi.
- **Được phép nói "cả cách đặt vấn đề đang sai"** — đó là loại phát hiện giá trị nhất.
- **Đừng khen.** Chỉ cần chỗ hỏng và chỗ thừa.

---

## 7. TỰ KIỂM TRƯỚC KHI GIAO

1. Đã **xổ hết cả 10 miếng** cột phải và **bấm badge** chưa?
2. Đã đọc **7 biến sau khi trang chạy** chưa?
3. Ở việc 1, có nêu được ít nhất **ba đề nghị BỎ HẲN** hoặc **GỘP** không? Nếu không tìm ra cái nào, xin nói rõ là đã tìm mà không thấy — nhưng hãy tìm thật kỹ trước khi kết luận như vậy.
