# BRIEF GỬI CODEX (GPT-work) — RÀ SOÁT PHẢN BIỆN THIẾT KẾ MOW TRƯỚC KHI SANG MOT

> Đây **không phải** yêu cầu code. Đây là yêu cầu **đọc — đối chiếu — phản biện — viết báo cáo**.
> Việc cần làm: chỉ ra chỗ chưa hợp lý / thiếu / hổng / không khả thi / **phức tạp quá mức cần thiết**, rồi đề xuất cách đơn giản hơn.

---

## 1. BỐI CẢNH — chúng tôi đang làm gì

Incomex đang dựng một hệ vận hành gồm **4 "Mẹ"** (4 loại đối tượng có thể tạo ra và sửa được):

| Mẹ | Là gì | Neo trong cây 7 tầng |
|---|---|---|
| **MOW** | Quy trình | node T2 |
| **MOT** | Công việc (task) | node T1 |
| **MOIT** | Form nhập liệu | ngoài cây (linh kiện dùng chung) |
| **MOUT** | Báo cáo / thông tin tham khảo | ngoài cây (linh kiện dùng chung) |

Triết lý gốc: **"hợp đồng thông tin sửa rẻ"**. Thứ duy nhất chắc chắn là mọi thứ sẽ đổi vào ngày mai — nên không cố làm đúng ngay, mà **thiết kế để sửa rẻ**. Kèm theo đó: **"phức tạp là chết"** — bài toán thật vẫn phải giải và phải bịt lỗ hổng, nhưng giải pháp kỹ thuật phải đơn giản nhất có thể, vì chỉ đơn giản mới đáng tin.

### Đang ở đâu trong lộ trình

1. ✅ **Vừa rà xong rất chi tiết tầng MOW (quy trình, neo T2)** — đây là tầng đầu tiên được soi kỹ.
2. ⏭ **Sắp rà tầng MOT (công việc, neo T1)**.
3. ⏭ Sau đó rà hai form: **MOIT** và **MOUT**.

> **Lưu ý thuật ngữ** (dễ nhầm, xin đọc kỹ): **MOW = quy trình = neo node T2**. **MOT = công việc = neo node T1**. Nếu trong trao đổi thấy viết "MOT (T2 - quy trình)" thì đó là nhầm chữ; bản đúng là như bảng trên.

### Mục tiêu thật sự của giai đoạn này

Đưa **logic vận hành** (quá trình hoạt động · khởi tạo · sửa chữa · nâng cấp) vào hệ thống để:

- **Liệt kê cho đúng và đủ các "hợp đồng thông tin"** (hiện đếm được 8, xem mục 4).
- **Hình dung được sẽ cần những table nào**.
- **Tạo khung để thiết kế schema cho chuẩn** — thay vì dựng schema trước rồi phát hiện thiếu.

Càng làm chi tiết thì càng vướng yếu tố kỹ thuật của hệ đang chạy. Vì vậy chúng tôi **tách ra một trang NHÁP riêng biệt** để thiết kế cho thoải mái, xong xuôi mới nhập vào hệ chung.

---

## 2. NƠI ĐỂ THÔNG TIN — đường dẫn cụ thể

### Trang nháp (mở là chạy được ngay, không cần dựng gì)

```
https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-process-draft-v1.html
```

Cách xem: bấm vào **một dòng bất kỳ** trong danh sách → mở drawer chi tiết.
Trong drawer: **cột trái = MOW làm chủ, sửa được** · **cột phải = chỉ đọc / khối hỗ trợ**.
Các khối cột phải đều **gấp gọn**, bấm tiêu đề mới xổ ra.
Nút **Help** (cuối cột phải và ở ngoài danh sách) mở **SỔ GỐC** — văn bản gốc của toàn bộ thiết kế.

### Các trang liên quan (để so sánh, cùng thư mục)

| Trang | Vai trò |
|---|---|
| `mow-master-v1.html` | **Bản THẬT đang chạy** của danh sách MOW (drawer còn là thiết kế cũ) |
| `mot-master-v1.html` | Danh sách MOT — sắp tới sẽ rà |
| `moit-master-v1.html` | Danh sách MOIT |
| `mow-unified-canvas-v2.html` | Màn hình tạo/sửa quy trình |

*(chưa có `mout-master-v1.html`)*

### File nguồn — đường dẫn trên máy chủ

Thư mục: `/opt/incomex/docs/mcp-writes/ui-preview/`
URL tương ứng: `https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/<tên file>`

**Nhóm DỮ LIỆU — đây là chỗ chứa nội dung thiết kế, đọc kỹ nhất:**

| File | Chứa gì | Biến toàn cục |
|---|---|---|
| `mow-help-doc.js` | **SỔ GỐC** — 16 mục, nguồn văn bản gốc cho cả người và agent | `window.MOW_HELP_DOC` |
| `mow-drawer-scope.js` | Phạm vi quản lý của MOW + **bảng quan hệ phụ thuộc đầy đủ** (4 nhóm nguồn) | `window.MOW_DRAWER_SCOPE` |
| `mow-lifecycle-data.js` | Vòng đời thay đổi — 5 chặng, 3 dấu phê duyệt | `window.MOW_LIFECYCLE` |
| `mow-testplan-data.js` | **Danh mục test cố định 19 phép** | `window.MOW_TESTPLAN` |

**Nhóm GIAO DIỆN — chỉ vẽ, không chứa nội dung:**

`mow-process-drawer-draft.js` (cột trái: bảng công việc, khối bắt đầu, tổng) · `mow-drawer-help-render.js` · `mow-drawer-chain.js` (hai dải liền trước / liền sau) · `mow-drawer-version.js` · `mow-drawer-relations.js` · `mow-drawer-lifecycle.js` · `mow-list-exec.js` (cột "Thực hiện" ở danh sách ngoài)

**Nhóm KHUNG CHUNG (dùng chung cho cả 4 Mẹ — cẩn thận khi động vào):**

`master-list.js` · `master-drawer-view-v1.js` · `mvx-v3.js` · `mot-render-v1.js` · `mot-theme-v1.css` · `eco-nav.js`

### 💡 Cách đọc NHANH NHẤT toàn bộ nội dung thiết kế

Mở trang nháp, vào console trình duyệt, dump 4 biến ra:

```js
copy(JSON.stringify({
  help:      window.MOW_HELP_DOC,      // sổ gốc, 16 mục
  scope:     window.MOW_DRAWER_SCOPE,  // phạm vi + quan hệ phụ thuộc
  lifecycle: window.MOW_LIFECYCLE,     // 5 chặng thay đổi
  testplan:  window.MOW_TESTPLAN       // 19 phép test cố định
}, null, 2));
```

Nhanh hơn nhiều so với đọc file thô, vì mấy file này viết theo lối **append-only**.

> ⚠️ **QUY ƯỚC APPEND-ONLY — rất quan trọng khi đọc file thô:**
> Các file dữ liệu được sửa bằng cách **nối thêm khối mới vào cuối**, khối chạy sau ghi đè khối chạy trước. Đọc file thô mà đọc khối đầu là **đọc phải bản đã bị bỏ**. Ví dụ: `mow-drawer-scope.js` có **ba** khối `rel` chồng nhau, chỉ khối **cuối cùng** còn hiệu lực; `mow-lifecycle-data.js` có một khối `MOW_TESTPLAN` **đã bị bỏ** (bị `mow-testplan-data.js` thay). Vì vậy: **hãy đọc giá trị biến sau khi trang đã chạy**, đừng đọc file thô.

---

## 3. NHỮNG LUẬT ĐÃ CHỐT — hãy dùng làm thước đo khi phản biện

Xin **soi ngược lại chính các luật này**: chỗ nào trong thiết kế đang vi phạm luật của chính nó?

| Luật | Nội dung |
|---|---|
| **Đọc tự do — sửa độc quyền** | Tầng nào cũng ĐỌC được của tầng khác. Nhưng mỗi thứ chỉ MỘT tầng được SỬA. Không có thứ gì hai tầng cùng sửa. |
| **Khoá lúc gọi** | Mỗi tầng khoá phiên bản tại thời điểm được GỌI. Lượt đã khởi tạo chạy hết theo bản của nó. Lời gọi sau mới dùng bản mới. Một câu, không ngoại lệ. |
| **Nhân bản toàn diện** | Sửa = copy TOÀN BỘ thành bản mới, độc lập hoàn toàn. Giữ nguyên mã gốc, chỉ tăng số ver. Đã bác bỏ copy-on-write (tiết kiệm nhưng đánh đổi bằng chính lưới an toàn). |
| **Nghỉ hưu ≠ lưu trữ** | Bản cũ nghỉ hưu = tắt nhưng nguyên vẹn, bật lại được bất cứ lúc nào. Khác hẳn lưu trữ (khai tử). |
| **1 SSOT — hạn chế TEXT** | Thông tin CÓ THỂ THAY ĐỔI thì phải đọc trực tiếp từ bảng, không viết bằng text. Text sẽ lạc hậu mà không ai biết. |
| **Quan hệ ghi một chiều** | Chỉ tầng CHA ghi "tôi dùng ai". Chiều "ai dùng tôi" là truy vấn ngược, không ai ghi. Ghi hai chiều là sớm muộn lệch. |
| **Nút phải chạy** | Nút nào hiện ra thì bấm PHẢI chạy. Chưa đủ điều kiện thì vẽ ổ khoá + lý do, không vẽ nút chết. |
| **Danh mục kiểm phải CỐ ĐỊNH** | Mọi danh mục dùng để kiểm phải là một dãy CỐ ĐỊNH áp lên số dòng dữ liệu thay đổi — không phải danh sách co giãn theo từng ca. Cố định thì mới lặp được, lặp được thì mới không sót. |
| **Lộ chỗ thiếu** | Thiếu thì ghi rõ "chưa nối bảng X" và tô vàng — không bịa, không để trống im lặng. |
| **Chữ đúng nghĩa** | Đặt tên theo đúng hệ quả vận hành. |
| **Phức tạp là chết** | Giải pháp phải đơn giản nhất có thể. |

---

## 4. TÌNH TRẠNG HIỆN TẠI — tóm tắt để đối chiếu

### 8 hợp đồng thông tin (đang đếm được)

| # | Hợp đồng | Trạng thái |
|---|---|---|
| 1 | đối tượng (mã gốc · tầng · tên) | **một bảng chung có cột tầng**, 4 "Danh sách đã đúc" là 4 khung nhìn lọc |
| 2 | phiên bản | chốt |
| 3 | quan hệ dùng | chốt |
| 4 | lượt chạy | chốt |
| 5 | đề xuất | chốt |
| 6 | phê duyệt (3 dấu) | chốt |
| 7 | nhật ký quản trị | **vừa chuyển từ "đề nghị" sang BẮT BUỘC** |
| 8 | đo kết quả | **đang bàn, chưa chốt** |

### Bảng quan hệ phụ thuộc — nhóm theo **NGUỒN ĐỌC**, không theo chiều

1. Đọc thẳng từ PG (18 dòng) · 2. Đọc từ MOT (13 dòng) · 3. Đọc từ MOIT/MOUT — **luôn qua MOT** (8 dòng) · 4. **Tự tính, không đọc từ đâu** (8 dòng)

Nhóm 4 tồn tại để **không ai đi dựng bảng cho thứ vốn là kết quả tính**.

### Vòng đời thay đổi — 5 chặng

Chặng 0 định tầng → 1 đề xuất → 2 duyệt **nghiệp vụ** ("đáng làm không?") → 3 thực hiện (nhân bản) → 4 test **kỹ thuật** ("chạy được chưa?") → 5 duyệt **pháp lý** ("cho cả hệ thống làm theo chưa?") + ban hành.

Ba dấu duyệt nằm ở ba chặng khác nhau, **cấm gộp thành một nút**.

### Danh mục test — 19 phép **cố định**

6 nhóm: A có thật không (5) · B dùng được không (3) · C hình dạng đúng không (4) · D khớp hàng xóm (2) · E so với bản cũ (3) · F trước khi bật công tắc (2).
Hiện **2/19 chạy được**, 17 phép chờ 8 bảng. Danh mục tự xếp hạng **thứ tự nên dựng bảng**.

### Những chỗ ĐANG BIẾT LÀ CÒN THIẾU (đừng chỉ báo lại, hãy đề xuất cách xử)

1. **Hai bộ từ vựng trạng thái chưa hoà giải**: "đang chạy / tạm dừng / lưu trữ" (mã gốc) vs "đang bật / nghỉ hưu / đang dựng" (phiên bản).
2. **Điều kiện hoàn thành của task** (tín hiệu ra) — chưa giao cho tầng nào.
3. **Neo cây 7 tầng** — đã khai vào phạm vi MOW nhưng chưa có bảng nguồn.
4. **Tên và mô tả** — trường bắt buộc nhưng chưa từng khai trong bảng phạm vi.
5. **Phân quyền** (ai được sửa · ai được bật/tắt) — chưa có bảng, nên công tắc chưa chặn được gì.
6. **Danh sách trường của MOUT** chưa rà kỹ.
7. **Badge "còn N điểm cần bổ sung để chạy"** vẫn là số MẪU (7), chưa cùng nguồn với bảng kiểm ban hành.
8. **Hợp đồng #8** (đo kết quả) chưa chốt cấu trúc.

---

## 5. VIỆC CẦN LÀM — hai câu hỏi

### Câu 1 — Có chỗ nào chưa hợp lý?

Đối chiếu **Sổ gốc (Help)** ↔ **các bảng liệt kê** ↔ **giao diện thật đang chạy**, chỉ ra:

- **Mô tả thiếu rõ ràng** — chỗ nào hai người đọc ra hai nghĩa? Chỗ nào không đủ để viết ra một câu truy vấn?
- **Liệt kê thiếu** — hợp đồng thông tin nào còn sót? Trường nào cần mà chưa ai khai? Trạng thái nào có trong đời thật mà chưa có trong thiết kế?
- **Lỗ hổng** — đường nào đi được mà không ai kiểm? Ràng buộc nào chỉ chặn ở giao diện mà **quên chặn ở tầng dữ liệu**? Chỗ nào có thể hỏng **âm thầm, không báo lỗi** (đây là loại chúng tôi sợ nhất)?
- **Không khả thi** — chỗ nào nghe hay nhưng viết ra code sẽ tắc? Chỗ nào đòi dữ liệu mà thực tế sẽ không ai nhập?
- **PHỨC TẠP QUÁ MỨC** — *(mục này quan trọng ngang các mục trên)* chỗ nào đang giải bằng cách phức tạp trong khi có cách đơn giản hơn cho cùng kết quả? Bảng nào có thể gộp? Khái niệm nào có thể bỏ mà không mất gì?

### Câu 2 — Viết báo cáo danh mục cải tiến

Mỗi mục xin đủ **6 phần**:

| Phần | Nội dung |
|---|---|
| Vấn đề | một câu, nói thẳng |
| Nằm ở đâu | file / mục trong sổ / khối trên màn hình |
| Vì sao hỏng | hỏng lúc nào, hậu quả gì, có **âm thầm** không |
| Đề xuất | cách xử **đơn giản nhất** đạt cùng mục tiêu |
| Tầng nào chịu | MOW / MOT / MOIT / MOUT / khung chung |
| Mức | **CHẶN** (không sửa thì không chạy được) · **NÊN** · **ĐỂ SAU** |

Sắp xếp theo mức, **CHẶN lên đầu**.

---

## 6. XIN LƯU Ý

- **Chưa cần viết code.** Vòng này chỉ cần báo cáo. Nếu thấy chỗ nào nên sửa ngay trên trang nháp thì **nói trước, bàn rồi mới sửa**.
- **Đừng thiết kế lại giao diện.** Bố cục (cột trái sửa được / cột phải chỉ đọc, khối gấp gọn, tooltip tại chỗ) đã qua nhiều vòng với Owner. Chỉ góp ý khi bố cục **gây hiểu sai về mặt logic**.
- **Được phép bác bỏ.** Nếu thấy một luật ở mục 3 là sai hoặc quá đắt, xin nói thẳng kèm lý do — điều đó có ích hơn là làm theo.
- **Ưu tiên cái đơn giản.** Giữa hai đề xuất cùng kết quả, luôn chọn cái ít khái niệm hơn, ít bảng hơn, ít bước hơn.
- **Trọng tâm vòng này là MOW.** Nhưng nếu phát hiện điều gì sẽ **vỡ khi sang MOT/MOIT/MOUT**, xin nói ngay — sắp rà tới đó, biết sớm thì rẻ hơn nhiều.

---

## 7. KIỂM CHỨNG TRƯỚC KHI GIAO

Xin tự kiểm 4 điều:

1. Đã **mở trang nháp và bấm vào drawer thật** chưa (không chỉ đọc file)?
2. Đã đọc **giá trị biến sau khi trang chạy** chưa (nhớ quy ước append-only — đọc file thô rất dễ đọc phải bản đã bỏ)?
3. Mỗi mục trong báo cáo có đủ **6 phần** chưa?
4. Có ít nhất một mục thuộc loại **"phức tạp quá — có cách đơn giản hơn"** chưa? Nếu không tìm ra mục nào, xin nói rõ là đã tìm mà không thấy.
