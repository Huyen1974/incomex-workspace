# BRIEF GỬI CODEX — RÀ SOÁT TOÀN DIỆN MOW (vòng 3, trước khi sang MOT)

> Hai vòng trước: **vòng 1** rà kỹ thuật / cấu trúc dữ liệu (17 điểm) · **vòng 2** rà theo góc vận hành, đi 10 chặng của một lượt (7 CHẶN + 4 NÊN mới).
> Vòng này là **rà toàn diện**: kiểm sự thống nhất, đi lại từng bước, và **nhìn lại xem cách đặt vấn đề có tối ưu chưa**.

---

## 0. TRẠNG THÁI THẬT — đọc kỹ trước khi rà

**Chúng tôi KHÔNG khẳng định đã sửa hết.** Dưới đây là kiểm kê thật, đã verify trên trang chứ không nói theo trí nhớ.

Chúng tôi dùng luật: **một phát hiện phải đi qua 5 cửa mới gọi là xong.**

| Cửa | Ý nghĩa |
|---|---|
| 1. SỔ | Đã ghi vào Help (`window.BOOK`) |
| 2. QUY TRÌNH | Có bước nào trong 13 quy trình mô tả nó |
| 3. ĐẦU CHỜ | Có dòng trong miếng "Quan hệ phụ thuộc" (schema gap hiện ra) |
| 4. PHÉP TEST | Có phép trong danh mục test canh |
| 5. BẢNG KIỂM | Có mục chặn ban hành (badge đếm) |

Ba cửa đầu để **hiểu**. Hai cửa sau mới là **cưỡng chế**.

### ĐÃ đủ 5 cửa

Toàn bộ nhóm **CHẶN** của cả hai vòng: nhánh lỗi · chống trùng lượt · điều kiện đầu vào + ánh xạ · kết quả cuối của lượt · phong bì bàn giao · đường quay lui + đếm vòng · chốt phiên bản cho cả lượt · chủ vận hành · thử lại · chạy lại an toàn · việc cần can thiệp.

### CHƯA đủ 5 cửa — xin ưu tiên soi những mục này

| Mục | Sổ | Quy trình | Đầu chờ | Test | Bảng kiểm |
|---|:-:|:-:|:-:|:-:|:-:|
| M9 · giữ bằng chứng lúc đánh giá điều kiện | ✓ | ✓ | ✗ | ✗ | ✗ |
| M11 · chặn người thực hiện tự duyệt việc mình làm | ✓ | ✗ | ✗ | ✗ | ✗ |
| K6 · hạn phải xong (khác phút ước lượng) | ✓ | ✓ | ✗ | ✗ | ✗ |
| K7 · người được giao vắng mặt / leo thang | ✓ | ✓ | ✓ | ✗ | ✗ |
| K8 · hai lượt cùng ghi một bản ghi | ✓ | ✓ | ✗ | ✗ | ✗ |
| Quy trình "xử lý sự cố" | ✓ | ✗ | ✓ | ✗ | ✗ |

Xin **đừng tốn thời gian báo lại rằng chúng còn thiếu** — chúng tôi biết. Câu hỏi là: **thiếu chúng có chặn việc sang MOT không**, và **cách xử đơn giản nhất là gì**.

---

## 1. NƠI ĐỂ THÔNG TIN

### Trang nháp

```
https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-process-draft-v1.html
```

Bấm một dòng → mở drawer. Cột phải có 9 miếng, **gấp gọn, bấm tiêu đề mới xổ**:
Quản lý phiên bản · Quan hệ phụ thuộc · Vòng đời thay đổi · **Danh mục test kỹ thuật** · Đường dẫn 7 tầng · Bảng PG kết nối · Danh sách khoá ngoại · **Help** · **Quy trình của MOW**.
Badge **"còn 14 điểm cần bổ sung để chạy"** ở đầu drawer **bấm được** → bung ra bảng kiểm 16 mục.

### Đọc nhanh nhất — dump 6 biến từ console

```js
copy(JSON.stringify({
  book:      window.BOOK,                 // sổ gốc, 4 phần: chung/mow/mot/form
  scope:     window.MOW_DRAWER_SCOPE,     // phạm vi + quan hệ phụ thuộc (4 nhóm nguồn)
  lifecycle: window.MOW_LIFECYCLE,        // 5 chặng thay đổi
  testplan:  window.MOW_TESTPLAN,         // danh mục test cố định, catalog v4
  readiness: window.MOW_READINESS,        // bảng kiểm ban hành (badge đếm từ đây)
  quytrinh:  window.MOW_SELFPROCESS       // 13 quy trình master.qt.01…13
}, null, 2));
```

> ⚠️ Các file sửa theo lối **nối thêm, khối sau ghi đè khối trước**. Đọc file thô rất dễ đọc phải bản đã bỏ. **Hãy đọc giá trị biến sau khi trang đã chạy.**

Thư mục: `/opt/incomex/docs/mcp-writes/ui-preview/` · URL: `https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/<tên file>`

---

## 2. ĐÃ ĐỔI GÌ TỪ VÒNG 2 — để đối chiếu

| Hạng mục | Trước | Nay |
|---|---|---|
| Quy trình của hệ | 6 | **13** — chia 2 nhóm: A quản trị định nghĩa · B vận hành một lượt |
| Mã quy trình | `QT-01`… | **`master.qt.01…13`** — phạm vi `master` vì không cái nào riêng MOW |
| Hợp đồng thông tin | 9 | **10** — thêm `#10 bước-lượt` |
| Danh mục test | 19 (v3) | **26 (v4)** — thêm nhóm **G · khai đủ để vận hành chưa** |
| Câu hỏi của danh mục test | 3 | **4** |
| Bảng kiểm ban hành | 11 | **16** (K01…K16) |
| Badge | 9 mục chặn | **14 mục chặn** |
| Luật khoá lúc gọi | (mơ hồ đơn vị) | làm rõ: **đơn vị khoá là LƯỢT**, không phải bước |

### Ba chỗ chúng tôi ĐÃ BÁC ý kiến của bạn — xin phản biện lại nếu thấy chúng tôi sai

1. **Không chuyển tên/mô tả/neo cây xuống bảng phiên bản.** Lý do: đổi tên là sửa *tương thích*, để ở #2 thì sửa một lỗi chính tả cũng phải nhân bản + ba dấu duyệt; đối tượng mới đăng ký chưa ban hành sẽ không có tên để hiện; và nếu cần "tên lúc đó" thì #4 đã ghi cứng phiên bản.
2. **Không cấm hội tụ (fan-in).** "Hai việc kiểm rồi mới phê duyệt" là hình dạng nghiệp vụ rất thường gặp; cấm thì người ta lách bằng bước giả — tức nói dối trong dữ liệu. Đề xuất thay: cho trường **bước cha nhận DANH SÁCH**, vẫn một trường, không cần bảng N:N.
3. **Không dọn hết lối ghi nối-thêm ngay.** Phân biệt *mã chết vẫn chạy* (nguy hiểm, xoá ngay) với *khối cũ chỉ là dấu vết* (vô hại). Dọn từng file, kiểm sau mỗi lần.

---

## 3. VIỆC CẦN LÀM — ba câu hỏi

### Câu 1 · SỰ THỐNG NHẤT — Help ↔ Quy trình ↔ UI ↔ Hợp đồng còn vênh chỗ nào?

Đây là bệnh tái đi tái lại của dự án này. Trong một ngày chúng tôi đã tự bắt được **6 chỗ vênh** ở vòng trước và **2 chỗ nữa** ở vòng sau — đều do *thêm mục mới mà quên sửa mục cũ nói cùng chuyện*.

Xin kiểm chéo **bốn mặt**, không chỉ hai:

- **Sổ ↔ Quy trình**: luật viết trong sổ có được phản ánh đúng ở bước nào của 13 quy trình không? Có luật nào không quy trình nào thực hiện?
- **Quy trình ↔ Hợp đồng**: mỗi bước có chỉ ra được **đọc gì / ghi gì / ở hợp đồng nào** không? Bước nào không chỉ ra được nơi lưu?
- **Hợp đồng ↔ UI**: mỗi hợp đồng có đầu chờ tương ứng trên miếng "Quan hệ phụ thuộc" không? Có đầu chờ nào không thuộc hợp đồng nào?
- **Sổ ↔ UI**: có tooltip / nhãn nào trên màn hình đang nói ngược lại điều đã chốt trong sổ không?

**Cách kiểm thực tế:** lấy một luật bất kỳ trong sổ, đi tìm nó ở cả ba nơi còn lại. Chỗ nào không tìm thấy hoặc tìm thấy bản khác — đó là vênh.

### Câu 2 · ĐI LẠI TỪNG BƯỚC — còn lỗ hổng nào?

Vòng 2 bạn đi 10 chặng và tìm ra rất nhiều. Nay **13 quy trình đã được viết ra thành bước cụ thể** — nên lần này xin đi theo **chính các bước đó**, không đi theo chặng trừu tượng nữa.

Với **mỗi bước** của `master.qt.01…13`, hỏi:

1. **Đầu vào**: bước này cần gì mới bắt đầu được? Lấy từ đâu?
2. **Nơi lưu**: bước này ghi gì? Vào hợp đồng nào? Nếu không chỉ ra được → lỗ hổng.
3. **Ai làm**: người hay máy? Nếu người thì vắng mặt thì sao? Nếu máy thì chết giữa chừng thì sao?
4. **Hỏng thì sao**: bước này hỏng thì đi đâu? Có ai biết không?
5. **Xung đột**: hai lượt cùng chạy tới bước này thì sao?
6. **Ai phát hiện nếu bước này im lặng không chạy?**

Ưu tiên loại **hỏng âm thầm**: hệ vẫn chạy, không báo lỗi, chỉ là kết quả sai hoặc việc nằm im.

**Đặc biệt xin soi kỹ nhóm B** (`master.qt.07…13`) vì nó vừa được viết, chưa qua vòng phản biện nào.

### Câu 3 · NHÌN TỔNG QUÁT — cách đặt vấn đề đã tối ưu chưa?

Đây là câu **quan trọng nhất** và cũng khó nhất. Chúng tôi đã thêm rất nhiều thứ trong một ngày. Xin lùi lại một bước và hỏi:

- **Có khái niệm nào thừa không?** 10 hợp đồng · 13 quy trình · 26 phép test · 16 mục bảng kiểm · 4 câu hỏi · 2 nhóm quy trình · 3 kiểu nhánh lỗi · 4 kết quả lượt. Cái nào có thể **bỏ hẳn** mà không mất khả năng gì?
- **Có cái nào gộp được không?** Ví dụ: 26 phép test có nhóm nào thực chất là một? 16 mục bảng kiểm có mục nào trùng ý phép test đến mức thừa?
- **Cấu trúc có đối xứng chưa?** Chúng tôi cho rằng có một **cặp gương**: `#2 phiên bản ↔ #4 lượt` và `#3 bước trong định nghĩa ↔ #10 bước-lượt`. Cặp gương này có đúng không, và nếu đúng thì còn khai thác được gì thêm từ nó?
- **Có phải chúng tôi đang giải một bài toán khó hơn cần thiết không?** Owner sợ phức tạp, và đúng. Nếu bạn thấy có một cách đặt vấn đề khác **đơn giản hơn hẳn** mà vẫn giải quyết được, xin nói thẳng — kể cả nếu điều đó nghĩa là bỏ đi phần lớn những gì đã làm hôm nay.
- **Ranh giới MOW/MOT có đúng chỗ không?** Chúng tôi đã đẩy nhiều thứ sang MOT (tín hiệu kết thúc, kiểu lỗi, thử lại, chạy lại an toàn, đầu vào bắt buộc). Có đang đẩy quá tay không? Có thứ nào lẽ ra thuộc MOW?

Một câu hỏi kiểm chứng cho câu 3: **nếu phải giải thích toàn bộ hệ này cho một người mới trong 5 phút, cấu trúc hiện nay có làm được không?** Nếu không thì chỗ nào là chỗ rối nhất?

---

## 4. NGUYÊN TẮC ĐỂ ĐỐI CHIẾU

| Luật | Nội dung |
|---|---|
| Phức tạp là chết | Giải pháp phải đơn giản nhất có thể. Giữa hai đề xuất cùng kết quả, chọn cái ít khái niệm hơn. |
| Đọc tự do — sửa độc quyền | Mỗi thứ chỉ MỘT tầng được sửa |
| Khoá lúc gọi | Đơn vị khoá là **lượt** |
| Quan hệ ghi một chiều | Chiều ngược là truy vấn |
| Một nguồn, nhiều cửa | Không bao giờ có hai nơi ban hành cùng một thông tin |
| Nút phải chạy | Chưa đủ điều kiện thì hiện ổ khoá + lý do |
| Danh mục kiểm phải cố định | Dãy cố định áp lên số dòng thay đổi |
| Chỉ nhét vào mã thứ bất biến trọn đời | Loại đối tượng: được. Phòng ban, tên: cấm |
| Khai báo, không code cứng | Khai thác tính năng sẵn có của PG; chỉ tự viết cái PG không làm được |
| Một cỗ máy, nhiều đối tượng | MOW/MOT/MOIT/MOUT dùng chung 10 bảng, không đẻ bảng riêng |

---

## 5. BÁO CÁO MONG MUỐN

Ba phần, đúng theo ba câu hỏi. Mỗi mục đủ 7 phần:

| Phần | Nội dung |
|---|---|
| Vấn đề | một câu, nói thẳng |
| Loại | VÊNH (câu 1) · LỖ HỔNG (câu 2) · THỪA / RÚT GỌN ĐƯỢC (câu 3) |
| Nằm ở đâu | file / mục sổ / mã quy trình / mã phép test |
| Vì sao hỏng | hậu quả, và **có âm thầm không** |
| Ai phát hiện, bằng cách nào | người dùng tự thấy? báo cáo lệch? hay không ai thấy? |
| Đề xuất | cách xử **đơn giản nhất** |
| Mức | CHẶN · NÊN · ĐỂ SAU |

Kết thúc bằng **một đoạn trả lời thẳng**: theo bạn, MOW đã đủ để sang MOT chưa? Nếu chưa thì **tối thiểu** phải chốt thêm những gì?

---

## 6. XIN LƯU Ý

- **Chưa cần viết code, chưa cần sửa file.**
- **Đừng báo lại 6 mục ở phần 0** — chúng tôi biết chúng chưa đủ 5 cửa. Chỉ cần nói: có chặn việc sang MOT không.
- **Được phép bác chúng tôi**, kể cả ba chỗ ở mục 2 đã bác bạn. Nếu bạn vẫn cho rằng mình đúng, xin lập luận lại — chúng tôi sẽ đổi nếu lý do vững hơn.
- **Câu 3 quan trọng hơn câu 1 và 2.** Tìm thêm mười lỗ hổng nhỏ không giá trị bằng chỉ ra được một chỗ mà cả cách đặt vấn đề đang sai hoặc rườm.

---

## 7. TỰ KIỂM TRƯỚC KHI GIAO

1. Đã mở trang nháp, mở drawer, **bấm badge**, và **xổ cả 9 miếng cột phải** chưa?
2. Đã đọc giá trị **6 biến sau khi trang chạy** chưa?
3. Đã đi qua **từng bước của cả 13 quy trình** chưa, hay chỉ đọc tên?
4. Ở câu 3, có nêu được ít nhất **một đề xuất RÚT GỌN** không? Nếu không tìm ra, xin nói rõ là đã tìm mà không thấy — đó cũng là một kết luận có giá trị.
