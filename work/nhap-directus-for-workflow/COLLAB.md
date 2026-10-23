# COLLAB — nhap-directus-for-workflow
Tên việc: Bảng đã duyệt → collection Directus; cái chưa có → sáng tạo trên nháp; có sổ theo dõi, sửa 1 dòng tính bằng phút

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner 23/10/2026: lập việc + ô 1 (14:37, 15:02, 16:49); giao Codex làm Host (P06); 17:03 chốt hướng: «bây giờ bạn hiểu vấn đề rồi thì bạn sửa lại cái yêu cầu trên task để làm đúng vấn đề đi» (3.00); 17:26 chốt Đích (ô 1). Ô 2 và mọi việc ghi production vẫn chờ Owner gật từng việc.
Host: Codex · Owner chỉ định trực tiếp 23/10/2026: «bạn làm host việc này nhé». Claude Chat là Host vòng trước.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-23 17:35 +07 · Claude (Owner giao 17:03, 17:26; Host vẫn là Codex) · P11
- 🎯 Mục tiêu: ô 1 Đích (Owner 17:26) — bảng đã duyệt (đang là HTML) ⇒ chuyển sang collection; cái chưa duyệt, chưa có ⇒ sáng tạo trên nháp; Sổ của các sổ theo dõi cái gì đã vào collection, cái gì chưa. Vì sao: HTML làm 1 việc mất cả tiếng; Directus nhẹ, dùng lại được, không làm 2 lần.
- 🏁 Xong khi: ô 2 (9 dòng, đề xuất P11 — chờ Owner gật).
- 📍 Tiến độ: [✅ B0 Chốt đích] → [■ B1 Bảng DOT] → [□ B2 DOT áp chung] → [□ B3 Sổ của các sổ] → [□ B4 Chuyển bảng đã duyệt] → [□ B5 Sáng tạo cái chưa có] → [□ B6 Giao diện đọc collection] → [□ B7 Chạy thử 1 vòng] → [□ B8 Lên thật từng sổ]
- ✅ Đã xong: B0 — Owner 16:49 · 17:03 · 17:26 chốt Đích (ô 1, 3.00) · Owner gật 3.01: Bảng DOT = `dot_tools` đang có (dùng lại) · B1-a kiểm kê phía tệp (3.01): sổ đĩa 251 DOT, `dot_tools` lệch đĩa · Trước đó (P01–P09): khung việc, quy chuẩn vùng nháp 3.4, Một nhà 3.5, bản vẽ HTML (đã dừng).
- ■ Đang làm: Bước B1 Bảng DOT · — · 0 RUN active · song song: Codex chỉnh khuôn trang chủ theo UI cha (thuộc B6, mục «Hiện hành» dưới).
- ⬜ Còn lại: B1-b khảo sát chỉ đọc → B1-c Owner duyệt lệnh ghi → B1-d DOT đồng bộ + «?» + Điều 30/31 → B2 → B3 → B4 · B5 · B6 song song → B7 → B8.
- ➡ Kế tiếp: Host Codex đọc ô 1 Đích + 3.02 + 3.03 (P11), đồng thuận hoặc ghi P12 → Codex soạn 1 lệnh khảo sát chỉ đọc B1-b → GPT ACCEPT → 😊 Owner dán → 🤖 Claude Code. NEXT_TRIGGER=CODEX_DONG_THUAN_P11
- ⛔ Không làm: AI chạm thẳng Directus/PG (kể cả đọc) · vẽ/chép/move dữ liệu vào HTML · gõ tay vào Directus (kể cả Owner) · xoá dòng `dot_tools` · ghi production khi Owner chưa duyệt · trang viết riêng cho từng bảng · sửa MBM khi chưa xin phép · tạo tệp ngoài COLLAB khi Owner chưa gật.
- ⚠ Mỗi lượt sửa task: sửa luôn các dòng tổng — giờ cập nhật · ✅ · ■ · ⬜ · ➡.

### Hiện hành · Owner yêu cầu chỉ chỉnh giao diện trang chủ theo UI cha
Owner: «Kiểm tra lại danh sách UI cha. Thiết kế đúng theo cái đó, đừng tự sáng tạo ra concept mới… tạm thời cho giao diện trang chủ đã!»
- Đã kiểm ML-DEF-017 trong definition-master-data-v1.js: UI.CANVAS dùng mow-unified-canvas-v2.html; UI.MASTER dùng mot-master-v1.html / master-list.js. Mẫu Owner chỉ định: mow-unified-canvas-v2.html?tang=T2&che-do=thuong, nguồn 64c21429.
- Home đã dùng lại font Be Vietnam Pro, nền #f5f5f7, chữ #1d1d1f / #515154, brand #639922 / #3b6d11, nét phân cách rgba(0,0,0,.07), thẻ radius 12px/bóng nhẹ, chấm CSS 7–8px theo mẫu; bỏ emoji và hệ hình khối trang trí cũ. Giữ cột trái 30%, dòng 28px và khe 8px theo Owner.
- Chỉ sửa home.html (fc56f594); không sửa nội dung Công thức, collection, PG hay chuyển SSOT. Đã mở kiểm trang chủ ở 1280px. Đây là áp phong cách mẫu đã có, chưa tuyên bố đã tích hợp renderer cha dùng chung.
- Phạm vi tiếp theo theo chỉ đạo Owner; không tự mở rộng từ giao diện trang chủ sang thiết kế khác.

### P07 · Owner: tập hợp nguyên bản, tiếp cận nhanh
⚠ Owner 16:49 + 17:03 (3.00): copy/move tệp HTML Công thức không tính là tiến độ; Công thức vào collection ở B4. Tệp đã copy giữ nguyên, không xoá.
Chỉ đạo mới: cột trái rộng hơn, dòng dày hơn, khe giữa hai cột hẹp hơn; ít tầng/click; phần đã làm phải giữ nguyên, không thiết kế lại. Bắt đầu từ Công thức, copy 100% cả ghi chú, xổ/thu và tương tác. Collection phục vụ thiết kế những phần mới nhanh hơn.
- Đã sửa home hiện hữu: trái 30% (tối thiểu 320px trên màn rộng), khe 8px, dòng tối thiểu 28px thay 40px; giảm thụt tầng; bỏ tự mở tab MBM.
- Đã copy nguyên tệp ban-duyet.html sang `ui/nhap-directus/cong-thuc.html`, SHA-256 cả nguồn và đích = `9c0e161e2a6fc8bf71deabe86e8ca711ef9b24aa6b58e3baffaf9bb29361e28f`. Giữ nguyên toàn bộ tệp để không mất CSS/script/ghi chú/hành vi; home mở thẳng phần Công thức trong tệp này, không lồng trang Task. Các tài nguyên dùng chung vẫn đọc đường gốc như nguyên bản.
- Bản copy là ứng viên đối chiếu, không cho phép sửa nội dung độc lập. Nguồn chuẩn vẫn ở task mow-mot-moit-mout cho đến khi kiểm đủ hành vi/phụ thuộc và hoàn thành chuyển quyền ghi/gỡ nguồn cũ theo P06. Chưa tuyên bố move hoàn tất.
- Bản trung gian trong task này đã bỏ nội dung trùng, chỉ giữ đường dẫn tới ứng viên trong xưởng. Danh mục tệp: COLLAB quản lý yêu cầu/trạng thái; ban-duyet.html chỉ dẫn bản đối chiếu; xưởng nhap-directus/home.html là cửa vào, cong-thuc.html là bản copy nguyên vẹn. Còn mở: kiểm đủ tương tác, nguồn chuẩn và DOT/collection.

### Chỉ đạo hiện hành P06 · Owner 23/10/2026 · ưu tiên hơn các đề xuất P01–P05
⚠ Owner 16:49 + 17:03 (3.00) đổi cách làm: không vẽ/chép/move HTML; dữ liệu vào Directus bằng DOT; bước đầu = Bảng DOT (3.01). Các ý P06 còn giữ: thiết kế như thật, diễn tập như thật · Masterlist và DOT quản lý bằng collection · mỗi bước ánh xạ DOT · quy trình chuyển SSOT.
Owner giao Codex rà và bổ sung task, bắt đầu thiết kế lại trang chủ và khu vực nháp. Phạm vi này đã được giao trực tiếp; không coi các dòng chờ gật cũ là yêu cầu hỏi lại để bắt đầu thiết kế. Chưa đồng nghĩa duyệt triển khai PG production.
- Mục tiêu Owner: «Mục tiêu của khu vực nhá không phải là liệt kê. Mục tiêu là thiết kế như thật và diễn tập như thật, chỉ là chưa kết nối vào với PG thôi.»
- Nguồn chuẩn Owner: «phải dùng từ move (tức là xóa bản gốc sau khi bản mới tại chỗ này đã ok)».
- Công thức: dùng bộ đã chốt trên trang Công thức; «tách nhỏ thành các "thừa số chung" để lắp từ các thành phần càng nhỏ, càng ít càng tốt».
- Kết quả phải tái sử dụng UI, trường, cấu hình, quan hệ, hợp đồng thông tin và collection đã duyệt khi chuyển sang bảng production; collection production đọc từ bảng tương ứng.
- Masterlist và DOT phải được quản lý bằng collection. Mỗi bản thiết kế có mã ổn định, nguồn hiện tại, đích, phiên duyệt, quyền ghi, quan hệ và bằng chứng chuyển; số lượng phải kiểm kê, không dùng số trong bản vẽ làm kết quả đo.
- Mỗi bước thiết kế/diễn tập phải ánh xạ DOT hiện hữu, đầu vào, đầu ra và bằng chứng. Thiếu DOT ghi rõ khoảng trống trước khi bổ sung; không thao tác Directus/PG trực tiếp.

**Điều chỉnh yêu cầu hoàn thành:** trang đẹp và danh mục chỉ là bước đầu. Phải diễn tập được chuỗi Công cụ/công thức → tạo MMOW → áp dụng MMOW cho quy trình → hợp đồng thông tin → cấu hình trường → kiểm tra → duyệt. Kiểm cả đường lỗi, thiếu trường, quan hệ gãy, phiên cũ và ghi sai nhà; không dùng nút giả hoặc trạng thái tự gán làm bằng chứng thành công.

**Chuyển SSOT:** kiểm kê đúng nguồn/đích và phụ thuộc → khóa ghi nguồn cũ trong lúc chuyển → chuyển đủ nội dung, mã, quan hệ, cấu hình, quyền và lịch sử cần thiết → đọc lại/đối chiếu tại đích → mở duy nhất quyền ghi đích → gỡ nội dung chuẩn ở nguồn cũ. URL cũ có thể chuyển hướng; bản sao phục hồi phải bất biến, không là nơi chỉnh sửa. Khi chưa kiểm xong, đích là ứng viên và nguồn cũ vẫn là nguồn chuẩn. Không tuyên bố đã move khi chỉ nhúng iframe/link. Điều này thay phương án giữ bản chuẩn cũ của 3.0 mục 9 và L4; chưa xóa bản nào trong P06.

**Ranh giới PG:** đề xuất 3.0 mục 2 về nháp chung PG vẫn chưa được chốt. Trước khi dựng collection phải xác minh backend/cách ly bằng DOT và phân biệt cơ sở dữ liệu nền của Directus với bảng nghiệp vụ PG production. Không tự hiểu “nháp Directus” là được sửa bảng production.

**Trạng thái P06:** đang rà nguồn và sửa bản vẽ hiện hữu; chưa dựng collection, chưa chuyển nguồn, chưa chạy diễn tập. Kế tiếp: kiểm kê DOT/nguồn chuẩn, hoàn thiện bản vẽ rồi triển khai một chuỗi mẫu qua DOT. JEV tham khảo chuyển nguồn: gen-dec-1792747951-vNbtJ4mEH3OdcuIx7j71; không thay kiểm chứng.

### 1. Mục tiêu
**Đích (Owner 23/10 17:26 — chốt):** dùng lại hết bản cũ. Trước đây làm bằng HTML ⇒ bảng nào đã duyệt thì chuyển hết sang collection Directus để quản lý. Thứ chưa duyệt, chưa có ⇒ sáng tạo mới và lập giao diện. Lập bảng master để biết cái gì đã vào collection, cái gì chưa.
A · Chuyển: bảng đã duyệt (đang ở HTML / JS tĩnh) ⇒ đưa nguyên nội dung vào collection bằng DOT, không thiết kế lại ⇒ bản HTML cũ chỉ còn đọc.
B · Sáng tạo: thứ chưa duyệt, chưa có ⇒ thiết kế mới trên vùng nháp `nhap_` (3.4) + giao diện ⇒ Owner duyệt ⇒ lên thật y như nháp.
Sổ theo dõi: Sổ của các sổ (3.02), mỗi bảng 1 dòng — đang ở đâu · đã duyệt · dòng A/B · collection đích · tình trạng chuyển ⇒ nhìn là biết đã vào bao nhiêu, còn bao nhiêu.
Thước đo: sửa/thêm 1 dòng tính bằng phút (mục 8). Luật giữ nguyên: DOT 100% (mục 4) · mọi thứ có sổ (mục 5) · SSOT (mục 6). Codex và Claude cùng làm theo phân vai 3.03.

Tình trạng: Đích = Owner 17:26. Mục 1–8 = nguyên tắc Owner viết 14:37 (1–4, Lưu ý), 15:02 (5–7), 16:49 (8). Chỉ sửa chính tả, giữ ý.
1. Tạo task mới work/nhap-directus-for-workflow, dùng để thiết lập các quy trình: 1. Chế tạo cỗ máy sản xuất quy trình 2. Vận hành cỗ máy sản xuất quy trình 3. Các quy trình do cỗ máy sản xuất quy trình tạo ra.
2. Mục tiêu hoàn thiện quy trình, thiết kế và thiết lập chuẩn các khuôn UI, collection chuẩn để sau này thiết lập chuẩn trên PG => Collections.
3. Những gì làm bây giờ là nháp => cần xoá đi dễ dàng, nhưng thiết lập để dùng lại những thứ nháp này tối đa và nhanh nhất (nháp sau khi ok => đưa ra làm thật đúng như vậy).
4. Dùng DOT 100% với Directus (DOT đã tương đối đầy đủ), thiếu DOT viết thêm. AI tuyệt đối không thao tác trên Directus và PG. Thiết kế để đảm bảo các DOT cũ dùng lại được (hoặc sửa thêm) cho cả nháp và production mà không cần sửa lại DOT.
5. Trọng tâm: mọi thứ có sổ => sẽ đảm bảo được thành công.
6. Nguyên tắc đối tượng là SSOT: mỗi việc kiểm soát 1 nơi ghi gốc, chỉ cho phép ghi ở đó; những nơi khác chỉ được thiết kế đọc lại SSOT (nếu được thì khoá quyền ghi, chỉ cho phép đọc) để 1 thông tin không có 2 nguồn sự thật.
7. Người và máy có cùng tư duy: collection thiết kế thế nào => hiển thị ra đúng như vậy. Kiểm soát độ phức tạp để không trở thành đống rác tiếp theo.
8. Giới hạn hiện nay là thời gian: bảng lớn dần, làm 1 việc mất cả tiếng là không chấp nhận được. Chuyển sang Directus vì hệ thống nhẹ, nhanh, và quan trọng nhất là sau này dùng lại được — đỡ phải làm 2 lần. Không đi làm lại đống cũ.
Lưu ý: trong tiến trình có thể vừa tiếp tục nháp để điều chỉnh cho nhanh, vừa triển khai những phần đã chốt lên PG để làm thật (2 quá trình song song).

### 2. Thế nào là hoàn thành
Đề xuất P11 (Claude, theo Đích 17:26) — chờ Owner gật. Bản P10: commit `a68288a3` · bản P02: `181af945`.
1. Sổ của các sổ là 1 collection: mỗi bảng của cỗ máy 1 dòng — đang ở đâu · đã duyệt · dòng A/B · collection đích · tình trạng chuyển; bảng và từng cột có «?».
2. Dòng A: 100% bảng đã duyệt đã vào collection, đếm khớp nguồn; bản HTML cũ chỉ còn đọc, không sửa ở đó nữa.
3. Dòng B: thứ mới thiết kế trên vùng nháp `nhap_` (3.4), có giao diện; Owner duyệt từng sổ rồi lên thật bằng cùng tệp khai báo + cùng DOT + Điều 30/31.
4. Bảng DOT khớp đĩa 100%: 0 lệnh sống vắng · 0 sha lệch · dòng mất file có cờ, không xoá; mỗi bước quy trình ghi «DOT nào áp» bằng mã trong bảng này.
5. Thêm/sửa 1 dòng của bất kỳ sổ nào ≤ 5 phút, từ lúc Owner nói tới lúc thấy trong Directus; bảng to hay nhỏ như nhau.
6. Mỗi thông tin chỉ ghi được ở 1 nhà; ghi chỗ khác bị chặn; chỗ khác chỉ hiện lại.
7. Giao diện cây trái – bảng phải đọc thẳng collection; thêm 1 sổ = 0 dòng mã giao diện.
8. Chạy thử trọn 1 vòng: MBM sinh MMOW 007 → chạy trên 1 MOW → 1 hồ sơ đủ ký.
9. AI thao tác trực tiếp Directus/PG: 0 lần · dữ liệu chép mới vào HTML: 0.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

#### 3.00 Chỉ đạo Owner 16:49 · 17:03 · 17:26 — dùng lại bản cũ, chuyển sang collection, Bảng DOT trước
- 17:26: «Đúng rồi, chúng ta dùng lại hết tất cả các bản cũ. Chỉ có điều trước đây nó là HTML ⇒ tất cả những bảng đã được duyệt rồi thì chuyển sang collection hết. Cho nên lập ra các bảng master để quản lý cái gì đã đưa vào collection, cái gì chưa. Tóm lại bạn hình dung là những cái gì có bây giờ chúng ta chuyển sang collection để quản lý. Và chúng ta sáng tạo và lập giao diện những thứ mà chưa được duyệt, chưa có. Mục tiêu phải rõ ràng như vậy. Sửa lại để bản thân Codex cũng hiểu vấn đề và cùng phối hợp để thực hiện.»
- 17:03: «Bây giờ bạn hiểu vấn đề rồi thì bạn sửa lại cái yêu cầu trên task để làm đúng vấn đề đi. Trước tiên là chúng ta cần liệt kê bảng đầu tiên: Bảng DOT. Xem có gì để Directus quản lý luôn. Thiếu gì thì còn viết.»
- 16:49: «Thế thì các bạn đang chuyển đống rác từ chỗ này sang chỗ khác. Tại sao lại đặt vấn đề ở đó là Nháp? Giới hạn hiện nay là thời gian: khi các bảng bắt đầu lớn, thực hiện được 1 việc các bạn mất cả tiếng đồng hồ. Chuyện này là không chấp nhận được. Đó là tại sao tôi quyết định chuyển sang Directus: ít nhất thì hệ thống nó nhẹ, chưa nói đến thời gian, và quan trọng nhất là sau này dùng lại được. Đỡ phải làm 2 lần. Các bạn đi làm làm lại cái đống cũ thì giải quyết cái gì?»
- Cần đạt: (1) thước đo chính = thời gian cho 1 việc; 1 tiếng/việc là không chấp nhận · (2) làm trong Directus để nhẹ và dùng lại về sau, không làm 2 lần · (3) không làm lại đống cũ: chép/move tệp HTML không tính là tiến độ · (4) bảng đầu tiên = Bảng DOT: cái gì Directus đã có thì dùng luôn, thiếu DOT thì viết.
- Hết hiệu lực từ 3.00: vẽ/chép/move dữ liệu HTML (P04–P07; tệp đã có giữ nguyên, không xoá) · lộ trình L0–L6 (3.1) · P09 mục 3 (dựng 4 collection 1 lượt) lùi sau Bảng DOT.

Lộ trình (thay 3.1; P11 theo Đích 17:26):
| Bước | Làm gì | Ai | Xong khi |
|---|---|---|---|
| B0 ✅ Chốt đích | Owner 16:49 · 17:03 · 17:26 | 😊 | ô 1 Đích |
| B1 ■ Bảng DOT | a kiểm kê tệp ✅ (3.01) · b khảo sát Directus/PG chỉ đọc · c Owner duyệt lệnh ghi · d DOT đồng bộ đĩa → `dot_tools` + «?» + Điều 30/31 | 🤖 Claude Code 2 lệnh (b, d) · 😊 c | ô 2 dòng 4 |
| B2 DOT áp chung | `dot-master-apply` (3.4 V7): tệp khai báo trên GitHub → collection + dòng | 🤖 | 1 lệnh tạo/sửa được collection và dòng |
| B3 Sổ của các sổ | dựng bảng theo dõi chuyển (3.02) bằng B2: nạp Master of Master 86 + ánh xạ Danh sách Master 49 + `meta_catalog` | 🤖 | ô 2 dòng 1 |
| B4 Dòng A · Chuyển | từng bảng đã duyệt: rút 1 lần từ HTML → tệp khai báo → B2; đếm khớp; tích ở Sổ của các sổ; HTML cũ chỉ còn đọc. Thứ tự đề xuất: Công thức → 43 câu → Master MMOW → Master MOW → các Master còn lại | 🤖 | ô 2 dòng 2 |
| B5 Dòng B · Sáng tạo | thứ chưa duyệt / chưa có: thiết kế trên `nhap_` → Owner duyệt | Host + 🤖 · 😊 duyệt | ô 2 dòng 3 |
| B6 Giao diện | khuôn UI cha (Codex) đọc collection, không dữ liệu chép | Codex + 🤖 | ô 2 dòng 7 |
| B7 Chạy thử | MBM → MMOW 007 → 1 MOW → hồ sơ | 🤖 AI mới + GPT | ô 2 dòng 8 |
| B8 Lên thật | Owner duyệt từng sổ nháp → DOT → Điều 30/31 | 😊 + 🤖 | ô 2 dòng 3 |
B4 · B5 · B6 chạy song song khi B2 + B3 xong (ô 1, Lưu ý).

#### 3.01 Bảng DOT — kiểm kê lần 1 (Claude 17:15 · chỉ đọc tệp DOT, sổ DOT, bản đồ hệ thống; chưa đọc Directus/PG — phần đó qua DOT ở B1-b)
Có gì:
| Mã | Đã có | Ở đâu | Tình trạng |
|---|---|---|---|
| D1 | Lệnh DOT sống — nguồn gốc thật | đĩa `/opt/incomex/dot/bin` (git cục bộ) | 251 lệnh (sổ 08/10); thư mục lẫn ~80 bản sao lưu ⇒ đếm thẳng là sai (`00-NHAN-THU-MUC.md`) |
| D2 | Sổ DOT sinh từ đĩa | `dot-dot-catalog` → `/opt/incomex/dot/00-SO-DOT.tsv` (máy) + `.md` (người) | 13 cột: tên · nhóm (25, theo tiền tố) · phiên bản · Tier · ghi/đọc · --help · biển R3 · nhãn · NoDup · sha · ngày sửa · byte · mục đích. Bản 08/10, thư mục đổi 14/10 ⇒ phải `--check` lại. 64/251 lệnh chưa tự ghi mục đích. Chưa vào Directus |
| D3 | Bảng DOT trong Directus | `dot_tools` · sổ CAT-006 «Danh mục DOT» · trang Registries | Lệch đĩa (đo 30/07–01/08): 314 dòng · 81 dòng không ghi đường dẫn file · ~20 lệnh sống vắng · 6 con trỏ chết; `last_executed`, `usage_count` là rác. Bảng chịu lực: `fn_validate_dot_origin` đọc nó cho 19 đường ghi; có cổng khai sinh `fn_birth_gate` và đếm `trg_count_dot_tools` |
| D4 | DOT đang chạm `dot_tools` | `dot-dot-register` (thêm file chưa có) · `dot-dot-health` (đếm dòng mất file / file chưa vào bảng) · `dot-fill-tool-descriptions` (điền mô tả rỗng) — cả 3 có `--dry-run` | dùng lại |
| D5 | Master Tool | ML-DEF-023 trong `definition-master-data-v1.js` (xưởng, tĩnh) | là công cụ (TOOL-…), không phải DOT; nguyên liệu, xét ở B3 |

Thiếu gì:
| Mã | Thiếu | Cách bù |
|---|---|---|
| T1 | Đường đưa sổ đĩa (D2) vào `dot_tools` | 1 DOT đồng bộ: khớp theo tên; thêm dòng qua `dot-dot-register`; cập nhật cột quét; dòng không còn file ⇒ gắn cờ, không xoá. Viết mới hay mở rộng: Claude Code kiểm trùng (NoDup) ở B1-b |
| T2 | Cột quét (Tier, ghi/đọc, sha, phiên bản, nhóm…) trong `dot_tools` | chưa biết cột hiện có ⇒ B1-b đọc rồi quyết |
| T3 | «?» cho bảng và từng cột `dot_tools` | DOT ghi ghi chú trường — B1-b chọn DOT có sẵn |
| T4 | DOT chỉ đọc mô tả 1 collection (cột, kiểu, ghi chú, số dòng) | chưa thấy; B1-b xác nhận; thiếu ⇒ viết 1 DOT Tier A dùng cho mọi bảng sau |
| T5 | Sổ ghi lượt chạy DOT — chưa từng có | ghi nợ, ngoài B1 |
| T6 | 64 lệnh chưa tự ghi mục đích | sửa ở đầu file DOT (nguồn), không sửa trong Directus; làm dần |

✅ Owner gật 17:26 («dùng lại hết tất cả các bản cũ»): Bảng DOT = `dot_tools` đang có, không dựng `nhap_dot`. Lý do: đã nằm trong Directus, đã có trong Sổ của các sổ (CAT-006), 19 đường ghi đang dựa vào; dựng bảng mới = 2 nguồn + làm 2 lần. Nhà của thông tin = file DOT trên đĩa; `dot_tools` chỉ DOT ghi, đọc từ đĩa; muốn sửa mô tả ⇒ sửa đầu file DOT. JEV `gen-dec-1792749996-4t68gOAjnCTcngeSWuti` (0,78).
B1-b — 1 lệnh khảo sát chỉ đọc (🤖 Claude Code): `dot-dot-catalog --check` · `dot-dot-health --dry-run` · `dot-dot-register --dry-run` · `dot-fill-tool-descriptions --dry-run` · đọc cột + ghi chú + số dòng của `dot_tools` qua DOT ⇒ ra bảng chênh đĩa ↔ `dot_tools` · gộp luôn (cùng lượt, chỉ đọc, cho B3): danh sách collection đang có + `meta_catalog` (mã, tên, số dòng), tiền tố `nhap_` chưa ai dùng. DOT nào không chứng minh được là không ghi thì không chạy, báo lại. Lệnh khảo sát không chứa lệnh ghi. Host Codex soạn.

#### 3.02 Sổ của các sổ = bảng master theo dõi chuyển (Owner 17:26) — đề xuất, Owner gật
- Dùng lại Master of Master (86 dòng, đang là HTML `master-of-master-v1.html`) làm khung: đã có mã CAT, tên, nhóm, mục đích, bảng dữ liệu (vd `dot_tools 314`; «—» = chưa có bảng), UI, tình trạng thiết kế/config/UI. Không dựng bảng theo dõi mới song song. JEV `gen-dec-1792751250-JTRWOVLw6OfjLxBsxvLs` (0,99).
- Thêm 6 cột: Đang ở đâu (HTML · JS tĩnh · PG · collection) · Đã duyệt (có/chưa) · Dòng (A chuyển / B sáng tạo) · Collection đích · Tình trạng chuyển (⬜ chưa · 🟡 đang · 🟢 đã vào, đếm khớp · 🔒 nguồn cũ đã khoá ghi) · DOT áp (mã trong Bảng DOT).
- Ánh xạ theo mã, chưa gộp/xoá: Danh sách Master 49 (ML-DEF, JS tĩnh) · `meta_catalog` (~169, PG thật) · các sổ trên trang Công thức. Trùng thì 1 dòng, ghi bí danh.
- Bảng và từng cột có «?». Chỉ DOT ghi.

#### 3.03 Phân vai — Codex và Claude cùng làm (đề xuất, Owner gật)
| Ai | Làm gì |
|---|---|
| Codex · Host | điều hành, giữ Bảng điều khiển, soạn lệnh cho Claude Code; làm B6 giao diện (khuôn UI cha đọc collection) |
| Claude Chat | dòng dữ liệu: Bảng DOT, Sổ của các sổ, danh sách bảng dòng A (B1–B4); rà lệnh; ý kiến ghi mục P |
| GPT Chat | rà, ACCEPT từng lệnh |
| 🤖 Claude Code | chạy DOT, viết DOT thiếu, kiểm lại + Điều 30/31 ngay trong lượt |
| 😊 Owner | gật Đích + ô 2; duyệt mỗi lệnh ghi production |
Quy ước: ai sửa việc thì sửa luôn Bảng điều khiển; khác ý ghi mục P, chốt trong 1 vòng.

#### 3.0 Owner cần quyết — đề xuất sẵn, gật hoặc lắc (P02, thay 3.6 của P01)
⚠ P10: câu 1 thay bằng ô 2 mới · câu 8 thay bằng P06 (Host Codex) · câu 9 theo P06 (move) · câu còn lại xét khi tới bước: 2, 6, 10 ở B2 · 4 ở B3 · 7 ở B4 · 5 ở B5.
1. Ô 2 Hoàn thành 7 dòng. Đề xuất: gật.
2. Vùng nháp nằm ngay trong Directus/PG thật, khoanh bằng quy chuẩn 3.4 — **thay đề xuất P01 «Directus + PG riêng»**. GPT P03 đồng thuận; tiền tố chỉ để nhận diện, cách ly bằng quyền (3.4 V8). Lý do: nháp riêng phải chép bảng thật sang ⇒ 2 nguồn, trái ô 1 mục 6; trong cùng hệ thì nháp trỏ thẳng sang bảng thật bằng mã, không chép. Cách này đã chạy thật ở web công ty (`web_incomex`) và khớp thiết kế Owner gật ở việc TQT 15/10. JEV `gen-dec-1792742987-VzYh7NFAOzmzv3GMs04u`: 1,00. Đề xuất: gật.
3. ✅ ĐÃ CHỐT (Owner 15:37): trang chủ ở `/knowledge/nhap-directus/home` (`/knowledge/home` đang là nháp của KB); cột lấy như trang Task hiện tại, không lấy khung KB; vẽ trước rồi tính.
4. Sổ của các sổ phía thật = `meta_catalog` đang có (trang Registries); vùng nháp có sổ riêng `nhap_so`; lên thật thì dòng chuyển sang `meta_catalog`. L1 chỉ ánh xạ ba danh mục (`meta_catalog` · Master of Master 86 · Danh sách Master 49 / registry 28), chưa gộp, chưa xoá (GPT P03). JEV 0,87: phải kiểm trigger, đếm, cột của `meta_catalog` trước ⇒ kiểm ở L1. Đề xuất: gật, có điều kiện L1.
5. Trang chủ công khai trên VPS, chỉ đọc, đọc bằng 1 thẻ máy chỉ-đọc; không mở quyền public của Directus. Đề xuất: gật.
6. Xoá trong vùng nháp: chỉ thứ có trong sổ sở hữu, theo kế hoạch Owner đã duyệt; mặc định không xoá (GPT P03). Xoá ở production: luôn hỏi Owner từng lần. Đề xuất: gật.
7. Nguồn nạp MOW = Master MOW 35 dòng (ML-DEF-004), không lấy bảng PG `workflows` 3 dòng. Đề xuất: gật.
8. Hội đồng: Claude Chat Host · GPT Chat rà · Claude Code chạy DOT. Đề xuất: gật.
9. Các «trang chủ» cũ — «⌂ Master» (`master-home-v1.html`), «⌂ Trang chủ thiết kế» (các trang `definition-master-*`) — và «Master of Master 86 mục» tĩnh: khi trang mới chạy thì trỏ sang trang mới, giữ làm lịch sử, không xoá. Đề xuất: gật.
10. Trung tâm UI / trang chủ cây (việc TQT, bước 3, Owner 16/10) và DOT `dot-master-apply` (thiết kế TQT R41–R46, chưa viết) chuyển về việc này; việc TQT ghi 1 dòng trỏ sang đây. Đề xuất: gật.

#### 3.1 Lộ trình — trọng tâm «mọi thứ có sổ» (Owner 15:02: «Roadmap thì bạn lập ra để GPT có ý kiến»)
⚠ Đã thay bằng lộ trình B0–B7 ở 3.00 (P10); giữ để truy vết.
| Bước | Làm gì | Ai | Xong khi |
|---|---|---|---|
| L0 Chốt khung + bản vẽ | ô 1–2 · 3.0–3.6 · bản vẽ trang chủ (Owner 15:37: «vẽ ra trước rồi tính») | Host vẽ · GPT đã rà (P03) → 😊 xem + gật 3.0 | Owner gật 3.0, ưng bản vẽ |
| L1 Kiểm kê (chỉ đọc, qua DOT) | Ánh xạ mọi sổ đang có (`meta_catalog` · Master of Master 86 · Danh sách Master 49 / registry 28 · sổ trên trang Công thức) → mã ↔ bí danh ↔ nơi đang ở ↔ nhà đích; **chỉ ánh xạ, chưa gộp/xoá**. Kê DOT Directus có sẵn; kiểm `meta_catalog` (trigger, đếm, cột); tiền tố `nhap_` chưa ai dùng; quyền thật của các thẻ hiện có; đường đọc Directus của Nuxt; đường dựng + triển khai trang Nuxt hiện có. | 🤖 Claude Code (1 lệnh) | bảng sổ + bảng DOT + bản đồ quyền; Host + GPT rà |
| L2 Vòng mẫu | DOT tối thiểu áp **1 sổ mẫu `nhap_so`** (dòng = các sổ trong bản vẽ) + thẻ ghi chỉ vùng nháp + thẻ đọc phía server · trang thật `/knowledge/nhap-directus/home` (bộ hiển thị chung, khung bản vẽ) đọc `nhap_so` + `meta_catalog` · bảo vệ Điều 30/31 | 🤖 Claude Code (lệnh riêng sau L1) | khai báo → trang hiện đúng cột/«?»/link → ghi đúng nhà → thẻ nháp ghi production bị từ chối |
| L3 Mở rộng sổ | 7 sổ còn lại (3.3) + dữ liệu từ GitHub, cùng DOT | Host soạn tệp → 🤖 DOT | 8 sổ có dữ liệu; 0 bảng / cột thiếu «?» |
| L4 Đưa phần đã chốt lên sổ | Công thức (CT-000.x, CT-001…008), MBM, 43 câu, Master MMOW, Master MOW: mỗi thứ 1 nhà, mã thành link; HTML cũ chỉ hiện lại hoặc trỏ | Host + 🤖 DOT | 0 thuộc tính (đối tượng + thuộc tính) có 2 nơi ghi |
| L5 Chạy thử 3 nhóm | 1 AI mới: MBM → MMOW 007 → MOW 001 → hồ sơ đủ ký; thử ghi sai nhà | 🤖 AI mới + GPT kiểm | ô 2 dòng 4–5 đạt |
| L6 Lên thật từng sổ | Mỗi sổ là 1 thao tác riêng: Owner duyệt phần chênh → DOT áp vùng thật (cùng tệp khai báo) → POST-PROTECT Điều 30/31; dòng sổ chuyển `nhap_so` → `meta_catalog` | 🤖 DOT + 😊 duyệt từng sổ | ô 2 dòng 6 đạt |

Vòng nhỏ (GPT P03): kiểm kê → trang chủ + 1 sổ mẫu → dùng thử → mở rộng sổ → duyệt lên thật. L3–L6 lặp theo từng sổ: sổ nào chốt thì lên thật, sổ khác vẫn chỉnh trên nháp (ô 1, Lưu ý).

#### 3.2 Trang chủ (Owner 15:02, điểm 1–3) — đề xuất thiết kế, làm cho production luôn
⚠ 3.00: bản vẽ HTML (T0) dừng, không chép thêm dữ liệu; trang chủ thật = khuôn UI cha (Codex) đọc collection ở B5. Các điểm Owner 15:02 và 16:02 vẫn giữ.
Owner 15:02: (1) chọn 1 nơi làm trang chủ, thiết kế cho Nháp, sau dùng lại hoặc nhân bản thành trang chủ Production · (2) thiết kế lại phần đã chốt (công thức, MBM, các danh sách) để hyperlink tối đa, luôn có nút home ở mọi chỗ; truy cập chéo phải tiện cho con người để còn chỉ đạo · (3) treeview: xem xét lấy luôn màn `knowledge/modules?task=mow-mot-moit-mout&view=content&section=detail-formula-chi-tiet-3`, cùng độ rộng cột; cột trái treeview, cột phải bảng; bảng kiểu master of master là bảng toàn link.

Đã xem 4 nơi đang có (P02):
| Nơi | Đang làm gì | Kết luận |
|---|---|---|
| `ui-preview/mcp-writes/master-home-v1.html` «⌂ Master» | HTML viết tay; đọc 86 mục chép sẵn trong `master-of-master-v1.html` | Không dùng: dữ liệu nằm trong HTML = bản chép thứ 2 |
| `/knowledge/registries` «Danh mục hệ thống» | Đọc `meta_catalog` thật; có trang chung từng loại, mã tự thành link (`AutoLinkedValue`), quan hệ tự đọc (`/api/discovery/relations`) | Dùng lại đường đọc + linh kiện; không sửa trang này |
| `/knowledge/modules` «Task html view» | Khung cột trái danh sách việc, cột phải nội dung; nội dung là tài liệu repo | Lấy khung và độ rộng cột |
| Directus Studio | Đúng khai báo, nhưng phải đăng nhập, đầu cột không có «?» | Để máy dùng |

Thiết kế:
- Owner 16:02 (bản vẽ v1): (1) cột trái có biên giới rõ với cột phải, giữ cấu trúc 2 cột · (2) treeview áp dụng ngay trong cột trái: mẹ ở ngoài, con ở trong · (3) hạn chế tối đa lớp trung gian: bấm vào 1 bảng là hiển thị ngay bảng đó, tiết kiệm thời gian thao tác và chuyển đổi giữa các bảng · (4) trang home phải là 1 treeview tổng — giá trị của treeview là nhìn ra cấu trúc bằng hình; liệt kê kiểu ma trận không có nghĩa.
- T0 Bản vẽ v2 (P05): https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/nhap-directus/home.html — theo đủ 4 điểm Owner 16:02; địa chỉ giữ chỗ đang xem (`?n=<mã>`). Dữ liệu trong bản vẽ chép từ 3.3 để vẽ, **không phải nguồn**; bản thật (L2) đọc thẳng Directus, bản vẽ chuyển lưu trữ khi bản thật chạy.
- T1 Địa chỉ `/knowledge/nhap-directus/home` (Owner 15:37). Nút ⌂ đặt ở 2 chỗ chung: thanh menu Nuxt (mọi trang Nuxt) và `eco-nav.js` (thanh 4 Mẹ của các trang tĩnh) ⇒ trang nào cũng về được trang chủ.
- T2 Khung = trang Task hiện tại, không lấy khung KB (Owner 15:37). Đo thật P04: lưới 2 cột, khoảng cách 24px, lề 24px, rộng tối đa 1552px; cột trái 217px ở màn 1024 · 317px ở 1440 · 355px ở 1920 (≈ 23%); cột phải phần còn lại. Bản thật chép đúng CSS của trang Task. Nền trắng, chữ tối, chữ 16px.
- T3 Cột trái — cây (Owner 16:02 điểm 1–2): khung có viền, nền xám nhạt, tách hẳn cột phải; mẹ ở ngoài, con thụt vào trong, có đường nối; hình theo cấp định nghĩa 1 lần: ■ Nhóm (to) · □ Sổ · ◇ Cụm · • Dòng (nhỏ). Gốc ⌂ → nhóm (3.4 V3 + nhóm của `meta_catalog`) → sổ (số con, 🟢/🟡/🔴) → cụm → dòng; ▸ để mở/đóng.
- T4 Cột phải (Owner 16:02 điểm 3): bấm 1 sổ hay 1 dòng là hiện ngay bảng đó, không qua thẻ trung gian; trên bảng chỉ 1 dòng mảnh: đường dẫn ⌂ › nhóm › sổ · mã collection · tình trạng · mở tab mới. Cột lấy đúng khai báo collection (thứ tự · tên hiện · «?» = ghi chú cột); ô mã, ô quan hệ là link; bấm 1 dòng ⇒ mở dòng đó ngay trong bảng.
- T9 Trang chủ = cây tổng vẽ bằng hình (Owner 16:02 điểm 4): gốc ⌂ ở trên → mỗi nhóm 1 cột (ô to) → sổ (ô vừa) → cụm, dòng (viên nhỏ); bấm ô nào mở ngay bảng đó; bấm nhóm ⇒ cây riêng của nhóm. Không dùng bảng ma trận ở trang chủ; bảng Sổ của các sổ chỉ hiện khi bấm sổ đó.
- T5 Địa chỉ giữ chỗ đang xem: `?so=<mã>&dong=<mã>&vung=nhap|that` ⇒ gửi link là mở đúng chỗ. Nháp và thật là cùng 1 trang, khác tham số vùng: không cần nhân bản.
- T6 Chỉ đọc. Sửa = sửa tệp GitHub ⇒ DOT áp. Đọc bằng 1 thẻ máy chỉ-đọc giữ phía server, không đưa vào trình duyệt, không mở quyền public Directus; trang chỉ xuất dữ liệu đã cho công khai (GPT P03; một thẻ · hai cổng).
- T7 Luật «khai báo = hiển thị» (ô 1 mục 7): 1 bộ hiển thị chung cho mọi sổ, không trang riêng · chữ trên màn chỉ lấy từ khai báo · thiếu gì ⇒ bổ sung khai báo, không viết cứng · trình bày đặc biệt (ma trận màu, thẻ công thức) ⇒ khai thành 1 sổ dạng «khung nhìn», cũng có «?». Màn nào không làm được theo T7 ⇒ ghi nợ, không viết trang riêng.
- T8 Dùng lại cái đã có: đường đọc `$directus` + `/api/discovery/relations` + `AutoLinkedValue` · `SectionFields` · `SectionRelation` (Nuxt Registries). Không thêm gói, không đổi phiên bản.

Ý kiến Host về ô 1 mục 7 (Owner hỏi có khả thi không): khả thi, và đó là chuẩn ngành — giao diện sinh từ khai báo (Directus Studio, Django admin làm như vậy). Lợi lớn nhất: thêm 1 sổ = 0 dòng mã giao diện ⇒ chặn đống rác. Giới hạn nói trước: phần trình bày đặc biệt (ma trận màu, thẻ công thức kiểu CT-000.4) không tự sinh từ bảng thường ⇒ khai thành sổ khung nhìn (T7).

#### 3.3 Các sổ của 3 nhóm quy trình (ô 1 mục 1, mục 5)
| Nhóm | Nghĩa | Sổ nháp (tên máy) | Nhà / nơi đang ở |
|---|---|---|---|
| 0 Sổ | Sổ của các sổ (vùng nháp) | `nhap_so` | thật: `meta_catalog` (CAT-xxx) · tĩnh: Master of Master 86 mục, Danh sách Master 49 mục (`definition-master-index-v1.html`; tệp registry JS ghi 28 — lệch, ánh xạ ở L1) |
| 1 Chế tạo cỗ máy | Dựng MBM: công thức + thừa số chung | `nhap_cong_thuc` · `nhap_cau_hoi` | ML-DEF-021 Master Công thức · CT-000.1 trên `ban-duyet.html` (chưa có sổ) |
| 2 Vận hành cỗ máy | Dùng MBM sinh ra MMOW: Mục tiêu → Miền CV → Bộ câu của MMOW → câu đặc thù → hồ sơ mẫu | `nhap_mmow` · `nhap_khuon` (MMOW × câu) · `nhap_mien_cv` | ML-MOW-TH-001 Master MMOW · CAT-206* · CAT-250* |
| 3 Quy trình do cỗ máy tạo ra | MMOW chạy trên từng dòng Miền CV (MOW / Task / MOIT / MOUT / Field) ⇒ mỗi dòng 1 hồ sơ | `nhap_ho_so` · `nhap_tra_loi` (hồ sơ × câu, Check 1 · Check 2) | việc con CAT-227 · CAT-228* · ký CAT-015 |

\* = chưa có sổ. Cột và quan hệ chi tiết làm ở L1. Lỗ SSOT thấy khi vẽ (P05): CT-008 MBM không có trong Master Công thức ML-DEF-021 (18 dòng) — chỉ nằm trên trang Công thức ⇒ ghi vào bảng ánh xạ L1. Bảng đã có ở production (CAT-227, CAT-015, CAT-025, CAT-140): nháp trỏ sang bằng mã, chỉ đọc, không chép (3.4 V6).

#### 3.4 Quy chuẩn vùng nháp (Owner 15:02: «tất cả collection trong vùng này bắt buộc theo 1 quy chuẩn ⇒ lọc 1 cái là ra hết, không lẫn lộn»)
Dùng lại thiết kế Owner đã gật ở việc TQT (R41–R46, 15/10 16:21 + 21:39: «vùng nháp chỉ là cấu hình»), đổi tiền tố thành tiền tố chung.
- V1 Tiền tố: mọi collection vùng nháp có tên bắt đầu `nhap_`. Lọc `nhap_*` = ra hết. L1 kiểm: chưa collection nào đang dùng tiền tố này.
- V2 Phần sau tiền tố = tên thật khi lên production: `nhap_cong_thuc` ⇒ `cong_thuc`. Chữ thường, không dấu, nối `_` (khớp cách TQT đặt `ma`, `ten`).
- V3 Nhóm Directus: thư mục «NHÁP» → «0 Sổ» · «1 Chế tạo cỗ máy» · «2 Vận hành cỗ máy» · «3 Quy trình tạo ra». Cây trang chủ đọc đúng các nhóm này.
- V4 Ghi chú bảng bắt đầu `[NHAP]`, tiếp theo là «?» của bảng. Mỗi cột có ghi chú = «?» của cột.
- V5 Mỗi bảng có cột `ma` (mã nghiệp vụ, duy nhất, ổn định — không buộc là khoá chính vật lý, GPT P03) và `ten`. Quan hệ nối bằng `ma`.
- V6 Nối sang bảng thật: chỉ bằng mã, chỉ đọc, không khoá ngoại; bảng thật không bao giờ trỏ vào nháp ⇒ xoá vùng không làm gãy bảng thật.
- V7 Người ghi duy nhất: 1 DOT `dot-master-apply` đọc tệp khai báo trên GitHub đúng 1 commit. Vùng khai trong `vung.json` (tiền tố · nhóm · nhãn · xoá được). Nháp ⇒ thật: cùng DOT, cùng tệp, đổi `--vung`; nhưng mỗi lần lên thật là 1 thao tác riêng Owner duyệt + Điều 30/31 (GPT P03). Mẫu đã có: DOT nhận `--mode prod --conf …` (`dot-stack-cutover`).
- V8 Tiền tố chỉ để nhận diện; cách ly thật bằng quyền: thẻ ghi của vùng nháp chỉ ghi được collection `nhap_*` trong sổ sở hữu, với production chỉ đọc, không sửa schema/Flow/trigger production; L2 kiểm bằng quyền thật, không chỉ so tiền tố (GPT P03). DOT chỉ xoá được thứ có trong sổ sở hữu của vùng và mang tiền tố nằm trong danh sách viết cứng trong mã (`nhap_`); sửa tệp khai báo không mở được quyền xoá bảng thật.
- V9 `kiem` báo đỏ khi: sai tiền tố / nhóm / nhãn · khoá ngoại ra ngoài vùng · Flow hoặc trigger trên bảng nháp · quyền public · thẻ ghi khác DOT.
- V10 Tệp khai báo đặt ở `work/nhap-directus-for-workflow/khai-bao/` — chỉ tạo ở L2 sau khi Owner gật.

#### 3.5 Cơ chế Một nhà (ô 1 mục 6)
- N1 Nhà: mỗi thông tin (cột) có đúng 1 collection nhà, ghi ở Sổ của các sổ / Master Field, cột «Quản lý tại» (luật CT-000.2 dòng 11, CAT-000.5).
- N2 Cổng ghi: quyền Directus — chỉ thẻ chủ nhà được ghi collection đó; mọi thẻ khác chỉ đọc. Vùng nháp: chỉ thẻ DOT ghi. Mô hình «một thẻ · hai cổng»: mỗi tác nhân 1 thẻ, cổng đặt đúng ở chỗ ghi; không dựng thêm lớp chặn khác.
- N3 Nơi khác chỉ hiện lại qua quan hệ (link, hiển thị liên kết), không có cột chép.
- N4 Bắt lỗi: DOT `kiem` đếm thuộc tính của cùng 1 đối tượng được ghi ở 2 nơi (theo Master Field: đối tượng + thuộc tính), không xét trùng tên cột — nhiều sổ cùng có `ma`, `ten` là hợp lệ (GPT P03); L4 xong khi số này = 0. Nháp là đề xuất chưa ban hành, không phải nguồn thật thứ hai.

#### 3.6 Luật đã có — chỉ trỏ, không chép
- Root `COLLAB.md`: DROOT26 (Directus/PG chỉ qua DOT, cả lab lẫn production, kể cả đọc) · DROOT35 (DOT 100%) · DROOT27 (DOT tự mô tả: `--help`, dry-run, rollback, exit code) · DROOT29 (mã/DOT lên production phải vào bảo vệ Điều 30/31 + POST-PROTECT) · DROOT39 (chỉ danh tính máy giữ quyền quản trị).
- Lệnh giao Claude Code đụng máy chủ/production phải nhắc: làm xong kiểm lại, đưa ngay vào bảo vệ Điều 30/31.
- Hành động phá huỷ (xoá/dừng/sửa production): chỉ Owner quyết (AGENTS A2).
- Sửa MBM (CT-008): xin phép Owner trước.
- Đầu vào từ việc MMOW 07 (`work/mbm-qtth-07-ve-ui-mow/COLLAB.md`): P101 (3.3 mục 19) 7 bảng + 4 điều kiện — điều kiện (a) nay theo 3.4 · P100 (3.3 mục 18) phép thử AI mới, vướng lớn nhất = không biết ghi ở đâu · MBM r7.1 ở `work/mow-mot-moit-mout/ban-duyet.html`; M2–M6 vẫn chờ gật ở việc đó · lệch đã biết: Master MOW ML-DEF-004 = 35 dòng, bảng PG `workflows` = 3 dòng.

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| Codex | OpenAI | Codex desktop, chat hiện tại | Host | Owner giao trực tiếp P06 |
| Claude | Anthropic | Claude Chat (`[auth:claude-chat]`) | Dòng dữ liệu (3.03): Bảng DOT, Sổ của các sổ, dòng A · Owner giao trực tiếp P10–P11 | Owner gọi trực tiếp |
| GPT Chat | OpenAI | GPT Chat (`openai-mcp`) | Reviewer | Owner chuyển tay |
| Claude Code | Anthropic | Claude Code CLI | Worker · chạy DOT | Owner dán 1 lệnh |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: —

### Vòng trước
- P10 (23/10 17:15): ô 2 bản 7 dòng P02 và lộ trình L0–L6 thay bằng ô 2 8 dòng + B0–B7 (theo Owner 16:49 + 17:03); bản cũ ở commit `181af945`. Tên việc cũ: «Sổ + trang chủ cho cỗ máy sản xuất quy trình — làm trên vùng nháp Directus, phần đã chốt lên PG thật y như nháp».
- P01 (23/10 14:50): ô 2 bản 5 dòng (chưa gật) — thay bằng 7 dòng ở P02. Đề xuất P01 «nháp = Directus + PG riêng, lên thật bằng schema snapshot → diff → apply» — thay bằng 3.0 câu 2 + 3.4 (lý do ở 3.0 câu 2).

### P03 · 23/10/2026 · GPT Chat Reviewer · L0 · vòng 1/1 · Based_on P02 / commit `1b1920bd`
**Kết luận:** ĐỒNG THUẬN hướng dùng Directus/PG hiện hữu, tiền tố `nhap_`, trang chủ dùng chung `/knowledge/home`, tái sử dụng `meta_catalog` và trang Registries. **Đề nghị Owner gật có điều kiện, chưa READY/RUN** vì mục tiêu/ô 2 và mục 3.0 vẫn CHƯA XÁC NHẬN. Chỉ sửa 5 điểm ngắn trong thiết kế, không lập nhánh việc mới:
1. **L0/SSOT:** nháp là đề xuất chưa ban hành; không phải nguồn thật thứ hai. Một sự thật được xác định theo **đối tượng + thuộc tính**, không căn cứ trùng tên cột (nhiều sổ có `ma`, `ten` hợp lệ). Master Field ghi nhà nguồn; bảng khác trỏ mã/quan hệ và chỉ đọc. L1 chỉ ánh xạ ba danh mục 86 tĩnh/28 ML-DEF/`meta_catalog`, chưa gộp/xóa vì có thể khác chức năng.
2. **Nháp chung DB:** `nhap_` + thư mục NHÁP chỉ để nhận diện, không phải cách ly quyền. DOT của vùng nháp cần thẻ/role chỉ ghi các collection được phép; quyền production chỉ đọc, không sửa schema/bảng/Flow/trigger production. Kiểm cả quyền thực tế, không chỉ so tiền tố. Lên thật từng sổ là thao tác riêng cần Owner duyệt và theo Điều 30/31; không chỉ đổi `--vung` là đủ.
3. **Giảm việc trước mắt:** đưa L4 **bản trang chủ tối thiểu + 1 sổ mẫu** ngay sau L1 và bộ khai báo tối thiểu L2; không chờ nạp đủ 8 sổ mới xem được. Dùng lại `/knowledge/registries`, `AutoLinkedValue`, `/knowledge/modules` và DOT đã có; chỉ bổ sung DOT cần thiết nếu kiểm kê L1 xác nhận thiếu. Không ưu tiên làm `xoa-vung`/rollback tổng quát trước khi có sổ mẫu xem được; xóa vùng chỉ theo danh sách sở hữu và kế hoạch Owner duyệt, mặc định không xóa.
4. **Trang chủ:** một renderer chung đọc metadata Directus và quan hệ; `?` dùng ghi chú cột/bảng; cây trái, bảng phải, các link và nút ⌂. Không hứa màn đặc biệt tự có đủ chức năng chỉ từ bảng; phần đặc biệt xử lý sau khi sổ mẫu chứng minh cần. Trang public chỉ xuất dữ liệu đã cho phép công khai; thẻ đọc phải giữ phía server, không chuyển vào trình duyệt hay mở quyền public Directus.
5. **Quy chuẩn:** `nhap_` giữ làm bộ lọc, nhưng `ma` nên là mã nghiệp vụ ổn định/unique, **không buộc là khóa chính vật lý** nếu collection hiện hữu có `id`/UUID. Trước khi nhân hàng loạt, thử một thao tác thiết kế collection → trang chủ hiển thị đúng cột/ghi chú/link → ghi dữ liệu nháp đúng nhà → kiểm từ chối ghi production bằng quyền nháp.
**Chốt 5.1–5.4:** gật có điều kiện như trên; ưu tiên `/knowledge/home`, giữ URL cũ và sử dụng `meta_catalog` sau L1. Bám L0–L7 nhưng thực hiện theo vòng nhỏ: **kiểm kê → trang chủ + một sổ mẫu → dùng thử → mở rộng sổ → duyệt lên thật**. Không thay mục tiêu Owner, không trực tiếp chạm Directus/PG, không tạo file/schema/DOT ở lượt phản biện này.

### P04 · 23/10/2026 16:00 · Claude Chat Host · L0 · trả lời P03 + Owner 15:37
- Nhận cả 5 điểm GPT (ACCEPTED): điểm 1 → N4, 3.0 câu 4 · điểm 2 → V7, V8, 3.0 câu 2 · điểm 3 → lộ trình 3.1 thành vòng nhỏ, L2 = 1 sổ mẫu + trang thật, xoá mặc định không làm (3.0 câu 6) · điểm 4 → T6 · điểm 5 → V5.
- Địa chỉ: GPT đề nghị `/knowledge/home`; Owner 15:37 đã chốt `/knowledge/nhap-directus/home` (`/knowledge/home` đang là nháp của KB) ⇒ theo Owner.
- Owner 15:37 cho vẽ trước: bản vẽ ở T0 (xưởng UI, không đụng production, không cần Claude Code). Sổ mẫu L2 chọn `nhap_so` — chính các dòng của bản vẽ, để trang thật thay bản vẽ 1-1.
- Chưa READY/RUN: chờ Owner gật 3.0 + ưng bản vẽ; sau đó Host soạn 1 lệnh L1 (chỉ đọc) → GPT ACCEPT → Owner dán.

### P08 · 23/10/2026 16:46 · Claude Chat · ý kiến (không phải Host vòng P06) · trả lời câu hỏi Owner 16:42 về DOT 100%
- Sự thật (đo khi viết P08): **0 DOT đã chạy** trong việc này; **0 thao tác Directus/PG** (0 collection, 0 quyền, 0 dữ liệu). Mọi việc tới giờ là tài liệu GitHub + tệp HTML trong xưởng UI (`ui` nhap-directus/home.html, cong-thuc.html).
- Ranh giới luật: DROOT35 — mã nguồn/tài liệu sửa qua repo; **áp vào hệ thống** (Directus, PG, quyền, cấu hình, triển khai Nuxt/nginx) bắt buộc DOT. DROOT26 — Directus/PG kể cả đọc chỉ qua DOT.
- Điểm cần Host nắm: (1) home.html và cong-thuc.html là trang công khai trên VPS, ghi bằng thao tác tệp, không DOT — được chấp nhận nếu chỉ là bản vẽ/ứng viên, không lớn dần thành trang thật · (2) cả hai tệp sửa/tạo lúc 09:43Z chưa có commit riêng trong sổ git của xưởng (git_head vẫn 8d5f897 = ảnh chụp tự động 09:36Z) ⇒ ghi rõ đã ghi bằng đường nào · (3) move Công thức (Codex P07, theo chỉ đạo Owner) là chuyển **HTML tĩnh sang chỗ tĩnh khác** — đúng quy trình move, nhưng chưa phải đưa lên sổ/collection, chưa có DOT; công thức vẫn chưa có nhà trong Directus.
- DOT: có sẵn nhóm DOT chạm Directus trong `/opt/incomex/dot/bin` (`dot-collection-create`, `dot-collection-field-sync`, `dot-schema-apply`, `dot-schema-snapshot`, `dot-schema-diff`, `dot-permission-ensure`, `dot-content-*`…) nhưng chưa kiểm cái nào hợp vùng nháp (PROMPT TQT từng cấm `dot-collection-create`/`dot-collection-register` cho vùng nháp vì tự ghi sổ hệ thống). DOT xương sống `dot-master-apply` (TQT R41–R46) **chưa có** trong `/opt/incomex/dot/bin` ⇒ khoảng trống lớn nhất, phải có trước collection đầu tiên.
- Đề xuất 3 luật (chờ Owner gật; Host ghi vào Chi tiết cần đạt): **(1)** xưởng UI chỉ để vẽ và để ứng viên move — gắn nhãn, không là nguồn dữ liệu lâu dài · **(2)** mỗi bước thiết kế/diễn tập ghi 1 dòng «DOT nào áp» (có sẵn / thiếu ⇒ viết); bước chạm hệ thống đầu tiên là kiểm kê chỉ đọc qua DOT, rồi viết `dot-master-apply` trước khi dựng collection · **(3)** mọi lần ghi lên xưởng/máy chủ đều để lại commit có tên người ghi + lý do.
- Không sửa Bảng điều khiển (việc của Host). Không chạm Directus/PG.

### P09 · 23/10/2026 16:58 · Claude Chat · ý kiến (Host vẫn là Codex) · trả lời Owner 16:49 (3.00)
- Nhận lỗi: bản vẽ trang chủ của Claude (P04–P05) và bản chép Công thức (P07) đều là HTML chép dữ liệu bằng tay ⇒ đúng là chuyển đống cũ, không giải quyết gì. Chữ «Nháp» đã bị dùng sai cho tệp HTML ở xưởng UI; «Nháp» chỉ nên là collection Directus `nhap_` — thiết kế như thật, chỉ chưa nối bảng nghiệp vụ PG production.
- Vì sao 1 việc mất 1 tiếng: dữ liệu nằm lẫn trong tệp HTML lớn (Công thức 881 KB); sửa 1 dòng = đọc khối lớn → sửa → đồng bộ → chụp kiểm; bảng càng lớn càng chậm. Chuyển tệp sang chỗ khác không đổi điều này.
- Directus sửa đúng chỗ đó: mỗi dòng 1 bản ghi; sửa 1 dòng = 1 lần DOT theo `ma`, bảng lớn hay nhỏ như nhau · cùng tệp khai báo + cùng DOT cho nháp và thật ⇒ không làm 2 lần · Directus Studio có sẵn cây thư mục bên trái, bấm là ra bảng ⇒ xem được ngay, 0 dòng mã giao diện.
- Khớp với việc Owner đang giao Codex (khuôn trang chủ theo UI cha ML-DEF-017): khuôn = cách hiển thị, collection = dữ liệu. Hai việc chạy song song, gặp nhau khi khuôn đọc collection thay dữ liệu chép. P09 không dừng việc của Codex.
- Đề xuất (Owner gật/lắc):
  1. Không chép thêm dữ liệu vào HTML (bản vẽ, bản copy). Giữ nguyên tệp đã có, không xoá.
  2. HTML cũ chỉ là nguyên liệu: rút dữ liệu 1 lần bằng script, đếm khớp nguồn, rồi không sửa HTML nữa. Thay cách chép tệp của P07: nội dung Công thức (kể cả ghi chú) vào collection; xổ/thu và tương tác do khuôn hiển thị lo.
  3. 1 lệnh Claude Code: (0) kiểm chỉ đọc qua DOT — Directus dùng CSDL nào, `nhap_` chưa ai dùng; lạ thì dừng · (a) tệp khai báo nhỏ ở `khai-bao/` (V10): `nhap_so` + `nhap_cong_thuc` (18 + CT-008) + `nhap_cau_hoi` (43) + `nhap_mmow` (9) · (b) viết `dot-master-apply` (--help, thử khô, hoàn tác, mã thoát — DROOT27) · (c) áp vào Directus: thư mục NHÁP, ghi chú «?» cho bảng và từng cột, quan hệ bằng `ma` · (d) đọc lại đối chiếu + bảo vệ Điều 30/31.
  4. Thước đo: sau lệnh đó, thêm/sửa 1 công thức ≤ 5 phút từ lúc Owner nói tới lúc thấy trong Directus.
  5. Để đạt mục 4: chạy lại `dot-master-apply` trên commit mới của `khai-bao/`, chỉ vùng `nhap_`, là việc thường đã duyệt 1 lần — không cần vòng READY/ACCEPT mới mỗi lần (ngoại lệ DROOT38 cho vùng nháp — Owner quyết). Lên production vẫn hỏi Owner từng lần + Điều 30/31.
  6. Vùng nháp ở ngay trong Directus đang chạy, tiền tố `nhap_`, không khoá ngoại sang bảng production (= 3.0 mục 2).
- Owner gật ⇒ Host Codex soạn lệnh mục 3 → GPT ACCEPT → Owner dán. Không sửa dòng của Host. Không chạm Directus/PG. JEV `gen-dec-1792749005-1z0Dy4DH0t5BRNyavAnC` (hướng này 1,00) · `gen-dec-1792749234-LQiAC1RTgq4suKU9RkvV`.

### P10 · 23/10/2026 17:15 · Claude Chat · Owner giao trực tiếp 17:03 sửa yêu cầu task (Host vẫn là Codex)
- Đã sửa: Tên việc (nói đích) · Xác nhận User (đúng dấu A0, trang Task hết báo thiếu) · Bảng điều khiển 8 dòng + lộ trình B0–B7 · ô 1 thêm mục 8 (lời Owner 16:49) · ô 2 8 dòng (đề xuất) · 3.00 thêm lời 17:03 + lộ trình · 3.01 Bảng DOT kiểm kê lần 1 · biển ⚠ ở P06, P07, 3.0, 3.1, 3.2.
- Owner giao trực tiếp nên Claude viết lại Bảng; Host Codex rà P10 ở lượt kế tiếp, khác ý ghi P11. Việc khuôn trang chủ Codex đang làm không đổi.
- Kiểm kê 3.01 chỉ đọc tệp (`code`, `docs`: thư mục DOT, `00-SO-DOT.*`, `00-NHAN-THU-MUC.md`, `BAN-DO-HE-THONG-20260729.md` mục 13.6, đầu file `dot-dot-catalog`, `dot-dot-health`, `dot-dot-register`, `dot-fill-tool-descriptions`). Chưa đọc Directus/PG. Số liệu `dot_tools` là số đo cũ (30/07–01/08) — B1-b đo lại.

### P11 · 23/10/2026 17:35 · Claude Chat · Owner 17:26 chốt Đích, giao viết lại để Codex cùng hiểu (Host vẫn là Codex)
- Đã sửa: ô 1 thêm khối Đích (A Chuyển · B Sáng tạo · Sổ theo dõi) · Tên việc · ô 2 9 dòng · lộ trình B0–B8 · 3.02 Sổ của các sổ = Master of Master + 6 cột theo dõi · 3.03 phân vai · Bảng điều khiển.
- Owner gật 3.01 (dùng lại `dot_tools`). Bước đang làm vẫn là B1. Lệnh khảo sát B1-b gộp luôn phần đọc danh sách collection cho B3 để Claude Code chạy 1 lần.
- Gửi Codex: đọc ô 1 Đích → 3.00 → 3.01 → 3.02 → 3.03; đồng ý thì soạn lệnh khảo sát chỉ đọc B1-b; khác ý ghi P12.

## Nhật ký (lời Owner — chỉ sửa chính tả)
- P11 · 23/10 17:26 · «Đúng rồi, chúng ta dùng lại hết tất cả các bản cũ. … Sửa lại để bản thân Codex cũng hiểu vấn đề và cùng phối hợp để thực hiện.» (nguyên văn ở 3.00) → Claude: P11 (ô 1 Đích, ô 2, lộ trình B0–B8, 3.02, 3.03).
- P10 · 23/10 17:03 · «Bây giờ bạn hiểu vấn đề rồi thì bạn sửa lại cái yêu cầu trên task để làm đúng vấn đề đi. Trước tiên là chúng ta cần liệt kê bảng đầu tiên: Bảng DOT. Xem có gì để Directus quản lý luôn. Thiếu gì thì còn viết.» → Claude: P10 (sửa yêu cầu + 3.01 kiểm kê Bảng DOT).
- P09 · 23/10 16:49 · «Thế thì các bạn đang chuyển đống rác từ chỗ này sang chỗ khác. Tại sao lại đặt vấn đề ở đó là Nháp? … Các bạn đi làm làm lại cái đống cũ thì giải quyết cái gì?» (nguyên văn ở 3.00) → Claude: ghi 3.00 + đề xuất P09 (chờ gật); thêm 1 dòng đầu bảng điều khiển; sửa giờ P08 (ghi nhầm 17:00 → 16:46).
- P08 · 23/10 16:42 · (hỏi Claude Chat) «Tôi đang giao Codex thiết kế lại (bạn thiết kế xấu quá). Một câu hỏi là phần DOT 100% đang được áp dụng thế nào nhỉ? Tôi có cảm giác cả bạn và Codex đang thiết kế trực tiếp, chưa có dùng DOT đâu nhỉ? Giải thích kỹ cho tôi chỗ này.» → Claude: P08.
- P05 · 23/10 16:02 · «1. Cột trái nên có biên giới rõ ràng với cột phải. Chúng ta để cấu trúc 2 cột. 2. Bản thân treeview nên áp dụng ngay trong cột trái: cái nào mẹ ở ngoài, cái nào con ở trong. 3. Hạn chế tối đa các lớp trung gian. Tôi hiểu là chúng ta có 1 nơi là SSOT, nhưng bấm vào 1 bảng thì nó cần hiển thị ngay ra bảng đó. Cần tiết kiệm thời gian thao tác và chuyển đổi giữa các bảng cho con người. 4. Trang home phải là 1 danh sách treeview tổng. Cái giá trị nhất của treeview là nó giúp nhìn ra cấu trúc bằng hình hoạ. Chứ còn liệt kê theo kiểu ma trận như thế này thì không có nghĩa. Hiệu chỉnh lại vấn đề giúp tôi.» → Claude Host: bản vẽ v2 (`ui` nhap-directus/home.html, commit cục bộ 18fe7cf); sửa T0, T3, T4, thêm T9; cây có thêm cấp Cụm/Dòng lấy từ Master Công thức (18), Master MMOW (9), 43 câu (G1–G5). Mở kiểm 1440px: trang chủ = cây tổng 4 cột; bấm «Công thức» ⇒ hiện ngay bảng Master Công thức; bấm «2 Vận hành» ⇒ cây riêng của nhóm; 0 lỗi console của trang (lỗi font CSP là của trang Master cũ nhúng vào). Thấy lỗ SSOT: CT-008 MBM không có trong Master Công thức. Không chạm Directus/PG.
- P04 · 23/10 15:37 · «/knowledge/home hiện là nháp của KB. Chúng ta có thể dùng: /knowledge/nhap-directus/home. Lấy cột như phần task hiện tại chứ không lấy của KB đã thiết kế nhé. Giờ cần giao Claude triển khai đúng không? Cứ cho vẽ ra trước rồi tính.» → Claude Host: chốt 3.0 câu 3, sửa T1–T2; đo cột trang Task ở 3 cỡ màn; vẽ bản vẽ ở xưởng UI (`ui` nhap-directus/home.html, commit cục bộ a032a3c + 4192526) — không cần Claude Code để vẽ; mở kiểm 1440px: cây 4 nhóm · 11 sổ, bảng Sổ của các sổ toàn link, bấm sổ ra chi tiết + đường dẫn, «?» hiện khi rê chuột, 0 lỗi console; kiểm link nhà: ML-DEF-021 (18 công thức), ML-DEF-004 (35 MOW), Danh sách Master (49 mục), neo formula-ct-000-1 + formula-ct-008 có thật. Nhận 5 điểm GPT P03. Không chạm Directus/PG.
- P02 · 23/10 15:02 · «Rồi, cần 1 roadmap cho kế hoạch này. Lưu ý là trọng tâm là mọi thứ có "sổ" => sẽ đảm bảo được thành công. Đưa ra ngoài mục tiêu: Nguyên tắc đối tượng là SSOT. Mỗi việc cần kiểm soát 1 nơi ghi gốc, chỉ cho phép ghi ở đó, những nơi khác chỉ được thiết kế đọc thông tin lại SSOT (nếu được thì khoá quyền ghi lại, chỉ cho phép đọc SSOT) để đảm bảo 1 thông tin không có 2 nguồn sự thật. Để con người và máy móc có cùng tư duy, các collection thiết kế thế nào => hiển thị ra đúng như vậy (bạn có ý kiến thêm xem có khả thi không, nhưng đó là cách nhanh nhất để đồng bộ hoá suy nghĩ giữa người và máy); tôi cần kiểm soát sự phức tạp của các bạn để tránh lại trở thành đống rác tiếp theo. Roadmap thì bạn lập ra để GPT có ý kiến. Tôi đề nghị mấy điểm: 1. Cần chọn 1 nơi làm trang chủ. Thiết kế trang chủ cho Nháp (sau này có thể dùng lại hoặc chỉ cần nhân bản là thành trang chủ Production). 2. Thiết kế lại các phần chúng ta đã chốt: các công thức, MBM, các danh sách để làm sao hyperlink tối đa với nhau và luôn có nút home ở bất kỳ chỗ nào. Việc truy cập chéo đầu tiên cần trở nên tiện lợi với con người để còn chỉ đạo. 3. Thiết kế hệ thống treeview => có thể xem xét lấy luôn màn hình https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=detail-formula-chi-tiet-3 với cùng độ rộng của cột. Cột trái làm treeview và cột phải là bảng. Các bảng kiểu master of master nên là một bảng toàn link. Giờ chọn trang chủ và chúng ta bắt đầu thiết kế nhé. Thiết kế để cho production luôn. Một điều quan trọng: bạn chưa quy chuẩn vùng Nháp trong task để cho nhất quán. Tất cả mọi collection trong vùng này bắt buộc phải theo 1 quy chuẩn => để lọc 1 cái là ra hết và không bị lẫn lộn.» → Claude Host: ô 1 thêm mục 5–7; 3.0–3.6 mới (lộ trình L0–L7, trang chủ T1–T8, sổ, quy chuẩn V1–V10, Một nhà N1–N4); đổi đề xuất nháp riêng ⇒ nháp trong hệ thật (JEV `gen-dec-1792742987-VzYh7NFAOzmzv3GMs04u`: nháp trong hệ 1,00 · trang Nuxt chung 0,93 · rủi ro `meta_catalog` 0,87). Đã xem thật: `/knowledge/registries`, `/knowledge/modules`, `master-home-v1.html`, mã Nuxt Registries. Không chạm Directus/PG.
- P01 · 23/10 14:37 · «Bạn ghi những thứ cần thiết và bạn tiếp tục làm host: 1. Tạo task mới: work/nhap-directus-for-workflow. Dùng để thiết lập các quy trình: 1. Chế tạo cỗ máy sản xuất quy trình 2. Vận hành cỗ máy sản xuất quy trình 3. Các quy trình do cỗ máy sản xuất quy trình tạo ra. 2. Mục tiêu hoàn thiện quy trình, thiết kế và thiết lập chuẩn các khuôn UI, collection chuẩn để sau này thiết lập chuẩn trên PG=> Collections. 3. Những gì làm bây giờ là nháp => Cần xoá đi dễ dàng, nhưng thiết lập để dùng lại những thứ nháp này tối đa và nhanh nhất (nháp sau khi ok => đưa ra làm thật đúng như vậy) 4. Dùng DOT 100% với Directus (DOT đã tương đối đầy đủ), thiếu DOT viết thêm. AI tuyệt đối không thao tác trên Directus và PG. Thiết kế để đảm bảo các DOT cũ dùng lại được (hoặc sửa thêm) dùng được cho cả nháp và production mà không cần sửa lại DOT. Lưu ý: 1. Trong tiến trình chúng ta có thể vừa tiếp tục nháp để điều chỉnh cho nhanh và triển khai những phần đã chốt lên PG để làm thật (2 quá trình song song). Làm trước task và mục tiêu => bạn viết các phần liên quan rồi tôi chỉ đạo tiếp.» → Claude Host: tạo task; ô 1; ô 2 + đề xuất. JEV `gen-dec-1792741473-45t55tJ0vzYRd4AsGRg0`. Không chạm Directus/PG.
