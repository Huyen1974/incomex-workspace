# BRIEF GỬI CODEX — RÀ SOÁT MOW TỪ **GÓC ĐỘ VẬN HÀNH** (không phải kỹ thuật)

> Vòng trước bạn rà từ góc **kỹ thuật / cấu trúc dữ liệu** và tìm ra 17 điểm — rất tốt, chúng tôi đã nhận 14.
> Vòng này xin đổi hẳn góc nhìn. **Không rà cấu trúc nữa.**

---

## 1. VÌ SAO ĐỔI GÓC NHÌN

Sau vòng của bạn, Owner yêu cầu rà lại theo cách khác: **đi theo một lượt chạy thật**, mỗi lần công việc **đổi tay** thì dừng lại và hỏi ba câu.

Chúng tôi làm thử một vòng và tìm ra **10 lỗ hổng, trong đó 5 mục CHẶN** — và **không có mục CHẶN nào trong số đó từng bị phát hiện ở vòng rà kỹ thuật**, kể cả bởi bạn.

Lý do rất rõ: xét về **cấu trúc dữ liệu thì không có gì sai**. Các lỗ hổng chỉ lộ ra khi hỏi *"lúc chạy thật thì chuyện gì xảy ra?"*.

Kết luận chúng tôi rút ra và muốn bạn kiểm chứng ngược lại:
**rà vận hành trước, rà kỹ thuật sau.** Kỹ thuật chỉ trả lời *"cái đã khai có đúng không"*; vận hành mới trả lời *"đã khai đủ chưa"*.

---

## 2. BA CÂU HỎI PHẢI HỎI Ở MỖI LẦN CÔNG VIỆC ĐỔI TAY

Đây là phương pháp, xin bám sát:

1. **Điều kiện đầu vào để chuyển là gì?** Cái gì phải có sẵn, phải đúng, phải xong thì bước sau mới được bắt đầu?
2. **Quy định ở đâu?** Điều kiện đó được KHAI Ở TẦNG NÀO, trong BẢNG NÀO? Nếu không chỉ ra được nơi khai thì đó là lỗ hổng.
3. **Có xung đột với việc liên quan khác không?** Hai lượt cùng chạy, hai người cùng làm, hai quy trình cùng chạm một bản ghi thì sao?

Và một câu thứ tư nên hỏi kèm:
4. **Nếu chuyện này KHÔNG xảy ra như mong đợi thì hệ thống có BIẾT không?** (Chúng tôi sợ nhất loại hỏng âm thầm — không báo lỗi, chỉ ra số sai.)

---

## 3. ĐI THEO ĐÚNG ĐƯỜNG NÀY

Xin đi tuần tự, đừng bỏ chặng nào:

| # | Chặng | Gợi ý câu hỏi |
|---|---|---|
| 1 | **Trigger đến → lượt được khởi tạo** | Ai phát? Đến hai lần thì sao? Điều kiện không đạt thì lượt đi đâu? |
| 2 | **Lượt khởi tạo → bước 1 sẵn sàng** | Việc nằm ở hàng đợi nào? Ai được nhặt? Không ai nhặt thì sao? |
| 3 | **Bước đang làm → bước xong** | Ai xác nhận là xong? Xong nhưng thiếu dữ liệu ra thì có tính là xong không? |
| 4 | **Bước xong → bước sau bắt đầu** | Bước sau cần gì từ bước trước? Ai kiểm? |
| 5 | **Nhiều bước song song → bước hội tụ** | Bước sau cần CẢ HAI nhánh xong thì biểu diễn thế nào? |
| 6 | **Bước phê duyệt → bị TỪ CHỐI** | Từ chối đi đâu? Có phải là "lỗi" không? |
| 7 | **Bước hỏng → nhánh lỗi** | Ba kiểu đã chốt (xem mục 5). Có kín chưa? |
| 8 | **Quy trình xong → trigger ra → quy trình sau** | Trigger có mang theo bản ghi không? Quy trình sau biết làm việc trên cái gì? |
| 9 | **Xuyên suốt: đổi phiên bản, tạm dừng, huỷ** | Đang chạy dở mà quy trình bị PAUSED / bị huỷ / có bản mới thì sao? |
| 10 | **Xuyên suốt: con người** | Người được giao nghỉ phép, nghỉ việc, quá hạn thì sao? |

---

## 4. NƠI ĐỂ THÔNG TIN

### Trang nháp (mở là chạy, không cần dựng gì)

```
https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-process-draft-v1.html
```

Bấm một dòng bất kỳ → mở drawer. **Cột trái = MOW làm chủ · cột phải = chỉ đọc.** Các khối cột phải gấp gọn, bấm tiêu đề mới xổ.
Badge **"còn N điểm cần bổ sung để chạy"** ở đầu drawer nay **bấm được** → bung ra bảng kiểm ban hành.

### Sổ gốc — nay chỉ còn MỘT nguồn

`incomex-book-v1.js` → `window.BOOK`, tách 4 phần: **chung · mow · mot · form**.
Cả Help ngoài danh sách lẫn Help trong drawer đều là **khung nhìn** của nó.

### Đọc nhanh nhất — dump 5 biến từ console

```js
copy(JSON.stringify({
  book:      window.BOOK,            // sổ gốc, 4 phần
  scope:     window.MOW_DRAWER_SCOPE,// phạm vi + quan hệ phụ thuộc (4 nhóm nguồn)
  lifecycle: window.MOW_LIFECYCLE,   // 5 chặng thay đổi
  testplan:  window.MOW_TESTPLAN,    // danh mục test cố định, catalog v3
  readiness: window.MOW_READINESS    // bảng kiểm ban hành (badge đếm từ đây)
}, null, 2));
```

> ⚠️ **Các file sửa theo lối NỐI THÊM, khối sau ghi đè khối trước.** Đọc file thô rất dễ đọc phải bản đã bỏ. **Hãy đọc giá trị biến sau khi trang đã chạy.**

Thư mục file: `/opt/incomex/docs/mcp-writes/ui-preview/` · URL: `https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/<tên file>`

---

## 5. ĐÃ CHỐT SAU VÒNG CỦA BẠN — để không rà lại cái đã xong

| Đã chốt | Nội dung |
|---|---|
| Danh tính | Cột `tầng` → **`loại_đối_tượng`**. *(Đã BÁC phần chuyển tên/neo xuống bảng phiên bản — lý do ghi trong sổ, mục Tám quyết định.)* |
| Trạng thái | Đối tượng `ACTIVE/PAUSED/ARCHIVED` · Phiên bản `DRAFT/PUBLISHED/RETIRED` |
| Ban hành | Chỉ qua **một hàm dữ liệu nguyên tử** + ràng buộc tối đa một `PUBLISHED`/mã gốc |
| Chuỗi chuyên môn | Lưu **một chiều** bằng thứ tự; bỏ phép test D2 |
| Tuần tự / song song | **Bước cha** (`after_step`); cùng cha = song song. Vòng 1 chưa hỗ trợ hội tụ |
| Tín hiệu kết thúc | **MOT sở hữu** (thành công / thất bại / huỷ + dữ liệu ra); MOW chỉ điều phối |
| Nhánh lỗi | Ba kiểu `LOI_DUNG` · `LOI_CHUYEN` · `LOI_BO_QUA`. MOT khai kiểu (#10), MOW khai đích nhận, được ghi đè ở cấp bước. Bước phụ thuộc bước hỏng thì **suy từ bước cha** |
| Danh mục test | **Cố định, có số phiên bản** (`MOW-CAT-v3`, 19 phép). Kết quả lưu ở hợp đồng **#9** |
| Bật lại bản nghỉ hưu | Phải **kiểm tương thích** (chạy lại danh mục test), không phải "bật lại bất cứ lúc nào" |
| Hợp đồng | **9 cái**. #7 nhật ký sinh trong cùng giao dịch, chỉ tham chiếu #6 |
| Badge | Tự đếm từ **bảng kiểm ban hành** (11 mục), bấm bung ra, mỗi mục ghi **tầng phải sửa** |

---

## 6. 10 LỖ HỔNG CHÚNG TÔI ĐÃ TỰ TÌM RA — xin ĐỪNG báo lại, hãy ĐÀO SÂU HƠN

Đây là kết quả vòng rà vận hành của chúng tôi. Xin bạn: với mỗi mục, **đề xuất cách xử đơn giản nhất**, và quan trọng hơn — **tìm những mục CHÚNG TÔI CHƯA THẤY**.

**CHẶN**

1. **Không có đường QUAY LUI.** Người duyệt TỪ CHỐI thì đi đâu? Từ chối không phải lỗi; ép vào "thất bại" thì nhánh lỗi báo sự cố cho một việc bình thường. Hệ hiện chỉ có đường tiến.
2. **Không có điều kiện đầu vào ở CẤP BƯỚC.** Chỉ có điều kiện ở cấp quy trình. Bước 3 cần số lô mà bước 2 không ghi thì bước 3 vẫn chạy với dữ liệu rỗng.
3. **Không chống TRÙNG LƯỢT.** Trigger đến hai lần → hai lượt cho cùng một đơn hàng. Không có gì trong 9 hợp đồng hay 19 phép test nói về "một trigger + một bản ghi = một lượt".
4. **Hội tụ — hệ quả nặng hơn đã ghi.** Bước 5 cần cả bước 3 và 4 xong, nhưng mô hình một-cha chỉ chờ được một → bước 5 **chạy sớm, ra kết quả sai**. Không phải bất tiện mà là sai số liệu.
5. **Bàn giao dữ liệu giữa hai quy trình.** Trigger chỉ là tín hiệu. Quy trình sau cần biết **bản ghi nào**. Phép kiểm chéo D1 chỉ so mã trigger nên hai quy trình có thể "khớp" mà chuỗi vẫn không chạy.

**NÊN**

6. **Hạn phải xong ≠ phút ước lượng.** Đang gộp hai khái niệm. Quá hạn thì nhắc ai, leo thang cho ai?
7. **Người được giao vắng mặt** (nghỉ phép, nghỉ việc, công tác) → chưa có thay thế, chưa có leo thang.
8. **Hai lượt cùng chạm một bản ghi** → chưa có khoá tài nguyên, chưa có quy tắc ai thắng.
9. **Huỷ cả lượt đang chạy** → ai được huỷ, bước đang chạy dở xử sao, dữ liệu đã ghi có rút lại không.
10. **Điều kiện quy trình KHÔNG đạt** → từ chối lượt, hay xếp hàng chờ, hay báo ai? Khai điều kiện mà không khai nhánh trượt là nửa vời.

---

## 7. VIỆC CẦN LÀM

### Câu 1 — Đi hết 10 chặng ở mục 3, tìm lỗ hổng MỚI

Ưu tiên loại **hỏng âm thầm**: hệ vẫn chạy, không báo lỗi, chỉ là kết quả sai hoặc công việc nằm im mà không ai biết. Đó là loại đắt nhất và khó phát hiện nhất.

### Câu 2 — Với 10 mục ở mục 6, đề xuất cách xử ĐƠN GIẢN NHẤT

Nhắc lại nguyên tắc của chúng tôi: **"phức tạp là chết"**. Giữa hai đề xuất cùng kết quả, luôn chọn cái **ít khái niệm hơn, ít bảng hơn, ít bước hơn**. Nếu một mục có thể **không cần giải** ở vòng 1 (chỉ cần ghi rõ giới hạn), xin nói thẳng.

### Câu 3 — Báo cáo, mỗi mục đủ 7 phần

| Phần | Nội dung |
|---|---|
| Vấn đề | một câu, nói thẳng |
| **Xảy ra ở chặng nào** | theo bảng 10 chặng ở mục 3 |
| Vì sao hỏng | hậu quả gì, và **có âm thầm không** |
| **Ai phát hiện ra, bằng cách nào** | người dùng tự thấy? báo cáo lệch? hay không ai thấy? |
| Đề xuất | cách xử **đơn giản nhất** |
| Tầng nào chịu | MOW / MOT / MOIT / MOUT / khung chung |
| Mức | **CHẶN** · **NÊN** · **ĐỂ SAU** |

---

## 8. XIN LƯU Ý

- **Chưa cần viết code, chưa cần sửa file.** Vòng này chỉ cần báo cáo.
- **Đừng rà lại cấu trúc dữ liệu.** Vòng trước đã làm rồi. Nếu buộc phải nhắc thì để ở cuối, mục phụ.
- **Được phép nói "cái này vòng 1 không cần giải".** Ghi rõ giới hạn còn tốt hơn giải bằng một cơ chế phức tạp mà không ai dùng.
- **Trọng tâm vẫn là MOW**, nhưng nếu thấy điều gì sẽ **vỡ khi sang MOT**, xin nói ngay — chúng tôi sắp rà MOT.

---

## 9. TỰ KIỂM TRƯỚC KHI GIAO

1. Đã **mở trang nháp và bấm vào drawer thật** chưa (kể cả bấm vào badge để xem bảng kiểm)?
2. Đã đọc **giá trị biến sau khi trang chạy** chưa (nhớ quy ước nối-thêm)?
3. Đã đi **đủ 10 chặng** ở mục 3 chưa, hay bỏ qua chặng nào?
4. Có tìm được ít nhất **một lỗ hổng loại "hỏng âm thầm"** mà mục 6 chưa có không? Nếu không, xin nói rõ là đã tìm mà không thấy.
