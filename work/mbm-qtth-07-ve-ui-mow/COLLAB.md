# COLLAB — mbm-qtth-07-ve-ui-mow
Tên việc: QTTH 07 — vẽ UI theo Master MOW, đủ Master list và hợp đồng thông tin, làm bằng công thức MBM

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner viết ô 1–2 ngày 16/10/2026 17:05.
Host: Claude Chat · Owner giao trực tiếp 16/10 16:29–17:05.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-16 21:20 +07 · Claude · P09
- 🎯 Mục tiêu: ô 1. Vì sao: bài thử MBM — lần 2 không có Owner, AI vẫn tự chạy.
- 🏁 Xong khi: ô 2.
- 📍 Tiến độ: [✓ 1 Nhận yêu cầu] → [✓ 2 Tạo task] → [✓ 3 Chốt mục tiêu] → [■ 4 Liệt kê bước] → [□ 5 Check Master list] → [□ 6 Bộ câu hỏi] → [□ 7 Ký] → [□ 8 Chạy]
- ✅ Đã xong: task `mbm-qtth-07-ve-ui-mow` · Owner chốt ô 1–2 (17:05) · ma trận = bản 25 bước Owner đã gật 15:19 + 1 bước đề xuất.
- ■ Đang làm: — · 0 RUN active
- ⬜ Còn lại: 4 → 5 → 6 → 7 → 8, đúng thứ tự (MBM mục ⑥).
- ➡ Kế tiếp: bước 4 Liệt kê bước — chốt cách viết bước để mọi AI hiểu giống nhau (Sổ vấp V10), rồi hoàn thiện bảng từ bản 25 bước.
- ⛔ Không làm: G2/PG production · dựng collection trước khi ma trận được ký · gõ tay vào Directus.

### 1. Mục tiêu
Owner 16/10/2026 17:05:
1. Vẽ UI theo Master MOW.
2. Hoàn thiện Master list: đủ các Master list cần dùng, và từng Master phải được User duyệt lần đầu.
3. Điền đủ (SSOT): không có đối tượng liên quan đến quy trình này bị mồ côi (không có sổ để ghi, có sổ nhưng chưa được ghi, ghi ở 2 SSOT…).
4. Đủ trường để Config: liệt kê được hợp đồng thông tin liên quan.
5. Dùng 100% DOT tạo collection, không làm hệ nặng. Bổ sung các DOT cần thiết để dùng lại lâu dài. Ưu tiên chạy DOT nếu có thể (tự động).
Owner 16/10 16:29: đây là bài test MBM — vừa làm vừa sửa MBM để lần 2 không có Owner, AI vẫn chạy được.

### 2. Thế nào là hoàn thành
Owner 16/10/2026 17:05:
1. Vẽ xong UI theo Master list MOW, bao gồm hợp nhất các MOW hoặc tách MOW.
2. Xác định tin cậy số lượng đối tượng mồ côi (dùng DOT), đảm bảo không có đối tượng liên quan mồ côi.
3. Các Master list điền đầy đủ thông tin, đảm bảo SSOT.
4. Xác định đủ hợp đồng thông tin để Config không lỗi.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

#### ☑ Việc cần làm — đọc lại mỗi lượt, xong tích kèm commit
| # | Việc | Ai | Xong khi | |
|---|---|---|---|---|
| 1 | Nhận yêu cầu (MBM ①) | 🤖 | lời Owner ở Nhật ký | ☑ |
| 2 | Tạo task + tên | 🤖 | đúng khuôn, tên `mbm-` | ☑ `c8bfe619` |
| 3 | Chốt mục tiêu (MBM ②) | 😊 | Owner viết ô 1–2 | ☑ 17:05 |
| 4 | Liệt kê bước (MBM ③) | 🤖 | bảng # · Mốc · Mục con · Bước, mọi AI hiểu giống nhau (bản 25 bước đã gật làm gốc) | ■ |
| 5 | Check Master list (MBM ④) | 🤖 → 😊 | mọi sổ các bước đọc/ghi: có đường dẫn thật, hoặc đã lập + Owner duyệt lần đầu | ☐ |
| 6 | Bộ câu hỏi (MBM ⑤) | 🤖 | mọi bước đủ ô | ☐ |
| 7 | Ký | 🤖 Hermes kiểm · ✍️ GPT, Gemini · 😊 Owner | 0 ô trống, 0 ô ❓, 0 phản đối | ☐ |
| 8 | Chạy | 🤖 | đạt ô 2 | ☐ |

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| Claude | Anthropic | Claude Chat (`[auth:claude-chat]`) | Host | Owner làm việc trực tiếp |
| GPT Chat | OpenAI | GPT Chat (`openai-mcp`) | Council · ghế ký | Owner chuyển tay |
| Hermes | Hermes VPS (DeepSeek) | `agent-gw/hermes` | Council · ghế ký · việc thường | Owner chuyển tay |
| Gemini | Google | `gemini-agy` | Council · ghế ký | Owner chuyển tay |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: luật quyết = luật ký MBM (CT-008)

#### Sổ vấp MBM — vấp đâu ghi ngay, sửa CT-008 tại chỗ
| # | Vấp | Đã sửa ở CT-008 |
|---|---|---|
| V1 | thiếu bước tạo task | ④ r4.3 |
| V2 | chưa có khuôn tên task | ④ r4.3 |
| V3 | sai thứ tự; task chưa có danh sách việc | ④ r4.4 |
| V4 | tên task chưa cho biết nguồn gốc | ④ r4.5 (`mbm-`) |
| V5 | ma trận đủ A1–C4 từng dòng quá dài, người không đọc được | chưa sửa — task chỉ đặt mục lục, bản đủ để ở nơi đã ký; đổi bộ câu hỏi cần hội đồng |
| V6 | Host bỏ qua bản 25 bước đã gật, tự viết ma trận mới (Owner phát hiện 17:25) | ④.4 r4.6: có bản cũ thì bắt đầu từ bản cũ, chỉ thêm/sửa phần mục tiêu mới đòi |
| V7 | Thử làm 1.1–1.3: bước trỏ tới sổ và lệnh chưa có (CAT-227/228, mo-viec, mo-ho-so) → AI thường không làm được; Mốc 1 còn trùng bước tạo task (18:01) | ④ r5: thêm bước Rà soát Master list trước khi liệt kê bước; mỗi bước phải có nơi làm thật hoặc cách làm tay tạm |
| V8 | Mục ② «Chia mục và đặt mã» viết dài, làm không được (Owner 20:41) | ② r5: thay bằng bảng mẫu # · Mốc · Mục con · Bước; công thức gộp Mốc · Mục con · Bước thành 1 thành phần |
| V9 | Rà Master list đặt trước khi có bước là ngược: chưa biết bước thì chưa biết cần sổ nào (Owner 21:12) | r5.1: công thức và ④ đổi thành Bước → Check Master list → Bộ câu hỏi |
| V10 | Tên bước ngắn (vd «1.2 Mở hồ sơ») mỗi AI hiểu một kiểu; Host đang suy diễn theo cách hiểu riêng (Owner 21:12) | chưa sửa — đề xuất chờ Owner gật |

### Vòng trước
- 16/10 15:19 (Owner, nay gộp vào ô 1 bản 17:05): vẽ UI theo Master MOW · hoàn thiện Master list, điền đủ SSOT · đủ trường để Config · dùng DOT tạo collection.
- 15/10 (Owner, G1): vẽ UI, liệt kê trường còn thiếu để chốt hợp đồng thông tin, đủ trường để Config · 17:40: cái gì phát sinh cũng ghi vào Master list và kiểm đã ghi đủ.

## Ma trận QTTH 07 — bản Owner đã gật 16/10 15:19 (viết bằng MBM)
Bản đủ (mỗi bước đủ câu A1–C4, 53 mã ghi danh): tools-quy-trinh P49 V15.1 + V15.2 tại `f76fa2e1` — mã 008-x.y đọc là 007-x.y. Bảng dưới là mục lục 7 mốc · 25 bước. **Hồ sơ:** mỗi lần chạy = 1 việc (CAT-227) + 25 dòng hồ sơ (CAT-228).

| Mốc | Bước | Hồ sơ ghi ở |
|---|---|---|
| 007-1 Khai việc | 1.1 tra/tạo 1 việc · 1.2 mở hồ sơ 25 dòng · 1.3 điền 5 ô riêng của việc | CAT-227 · CAT-228 |
| 007-2 Chuẩn bị | 2.1 nạp bước từ Công thức · 2.2 điểm danh sổ cần, Owner duyệt cột · 2.3 thử DOT | ML-MOW-TH-001 · ML-DEF-012 · CAT-229 |
| 007-3 Cổng | 3.1 6 bước trên đạt mới mở làm | CAT-228 |
| 007-4 Làm | **A UI:** 4.1 hành động → UI · 4.2 xét UI dùng lại · 4.3 chọn bảng, khai sổ mới · **B Hợp đồng:** 4.4 nghĩa vụ thông tin · 4.5 ghép Field cũ/mới · 4.6 bảng đọc/ghi, bắt buộc · **C Đối soát:** 4.7a đếm phát sinh, thiếu = 0 · 4.7b rà ảnh hưởng · 4.8 DOT áp nháp, thử, đọc lại | ML-DEF-018 · CAT-206 · ML-DEF-008 · CAT-016 · CAT-229 |
| 007-5 Kiểm | 5.1 kiểm đủ · 5.2 xem màn, ảnh · 5.3 ghế khác hãng rà | CAT-015 · CAT-239 · CAT-025 |
| 007-6 Duyệt | 6.1 gom gói · 6.2 Owner gật/lắc · 6.3 lắc thì quay lại | CAT-227 · CAT-025 · CAT-069 |
| 007-7 Đóng | 7.1 kiểm toàn bộ · 7.2 rà nợ · 7.3 đóng, báo | CAT-228 · CAT-069 · CAT-227 |

**Đối chiếu 5 mục tiêu 17:05:** MT1 UI ← 4.1–4.3 · 4.8 · 5.2 · MT2 Master list + duyệt lần đầu ← 2.2 · 4.3 · 6.2 · MT3 không mồ côi ← 4.7a (DOT đếm) · MT4 hợp đồng thông tin ← 4.4–4.6 · MT5 DOT ← 2.3 · 4.8 + DOT ghi danh ở V15.2.
**Thiếu 1 bước** cho ô 2 mục 1 (hợp nhất hoặc tách MOW): đề xuất thêm **4.0 Rà Master MOW: giữ · hợp nhất · tách → Owner gật** (chờ Owner gật).

<details><summary>Bản 14 bước Claude tự viết 17:20 — SAI, bỏ (giữ để tra V6)</summary>

**Luật chung (mọi bước, không chép lại):** chưa đạt → làm lại chính bước đó, ghi nợ CAT-069 · đối tượng mới phát sinh ghi danh vào sổ trước khi làm · việc thường giao Hermes, việc khó giao frontier · D1 làm sai bị chặn: GS-01 · 02 · 03 · 04 · D2 quên ghi bị bắt: GS-07 (DOT đếm mồ côi) · 08 · 09.

| Mã | Bước | Làm bằng | Xong khi | Ghi ở |
|---|---|---|---|---|
| **007-1** | **Khai việc** | | | |
| 1.1 | Tạo task, chốt mục tiêu | 🤖 + 😊 | Xác nhận User = ĐÃ | task này · ☑ |
| **007-2** | **UI cần gì** (MT1) | | | |
| 2.1 | Rà Master MOW: giữ · hợp nhất · tách | 🤖 đề xuất → 😊 gật | mỗi MOW có 1 quyết định | Master MOW · CAT-025 |
| 2.2 | Mỗi MOW: hành động → màn cần | 🤖 | hành động có màn / cần = 100% | ML-DEF-018 |
| 2.3 | Mỗi màn: dữ liệu cần | 🤖 | màn có danh sách dữ liệu / màn = 100% | ML-DEF-018 |
| **007-3** | **Master list** (MT2 · MT3 · MT5) | | | |
| 3.1 | Điểm danh sổ cần: có · thiếu | 🤖 Hermes | sổ cần đều có mã | ML-DEF-012 |
| 3.2 | Thiết kế cột sổ mới → User duyệt lần đầu | 🤖 → 😊 | sổ duyệt / sổ cần = 100% | CAT-025 |
| 3.3 | Tạo collection + nạp dữ liệu từ gốc | 🤖 DOT | collection / sổ cần = 100% · ô bắt buộc trống = 0 | biên nhận CAT-229 |
| 3.4 | Đếm mồ côi: không sổ · có sổ chưa ghi · ghi 2 nơi | 🤖 DOT | mồ côi = 0 | biên nhận CAT-229 |
| **007-4** | **Hợp đồng thông tin** (MT4) | | | |
| 4.1 | Mỗi dữ liệu màn cần → 1 dòng hợp đồng | 🤖 | dòng / dữ liệu cần = 100% | CAT-206 |
| 4.2 | Ghép Field cũ / mới | 🤖 | Field thiếu = 0 | ML-DEF-008 |
| 4.3 | Thử Config trên nháp | 🤖 DOT | lỗi = 0 | biên nhận CAT-229 |
| **007-5** | **Dựng UI** (MT1) | | | |
| 5.1 | Dựng màn trên nháp theo 2.2–2.3, chụp ảnh | 🤖 DOT | màn dựng / màn cần = 100% | ML-DEF-018 · ảnh CAT-239 |
| **007-6** | **Kiểm & duyệt** | | | |
| 6.1 | Đếm lại: mồ côi, ô trống | 🤖 DOT | cả hai = 0 | biên nhận CAT-229 |
| 6.2 | Owner xem màn thật, gật → đóng | 😊 | 1 quyết định gật | CAT-025 |

**DOT cần (MT5):** tạo collection + nạp + thử Config (`dot-master-apply`) · đếm mồ côi · chụp màn. Chưa có thì ghi danh «cần làm» ở ML-DEF-024 rồi dựng để dùng lâu dài.
**Nguồn:** CT-008 MBM (`work/mow-mot-moit-mout/ban-duyet.html#formula-ct-008`) · dùng lại bài thử V15 (tools-quy-trinh P49 tại `f76fa2e1`).

</details>

## Nhật ký (nguyên văn Owner, giữ lỗi gõ)
- P01 · 16:29 · tạo việc: «Thấy bạn lúng túng lắm. Tức là các bạn viết ra đó nhưng các bạn chưa chắc đã làm được 1 quy trình từ MBM đâu. Đây sẽ là bài test thử. Đầu tiên bạn sửa lại việc này. Bổ sung phải taọ task trên workspace nữa. => bạn thấy đấy. Viết không đủ cụ thể, khôgn tính đến khi làm => vào làm là mắc. Chúng ta vừa làm vừa hiệu chỉnh toàn bộ MBM để làm sao các bước thật chi tiết. Lần 2 không có tôi AI thưc sự chạy được. Các bạn viết thì hay, nhưng khi các bạn làm là hỏng ngay. Giờ bổ sung phần đó và việc đầu tiên bạn tạo task trên WP đi. qtth.07-ve-UI-mow»
- P02 · 16:39 · thứ tự ④ + danh sách việc: «Không tôi nghĩ là nên làm ngược lại: ④ Làm một MOW bằng MBM. Nhận yêu cầu => tạo task Tạo task trên workspace => Chốt mục tiêu (quy trình sẵn cũ). Đưa 1 danh sách list những viẹc cần làm lên Task, cái nào làm xong thì tích. Lý do là các bạn ít đọc công thức, chỉ đọc 1 lần thôi. Còn lại task là cái mà lần nào cũng phải đọc lại, xem lại. Dễ bàn hơn. Sửa lại và làm thử theo xem có hợp lý không. Chưa hợp lý lại tiếp tục sửa. Chỉ có phần quét chi tiết mà hội đồng đã góp Ý nhiều lần => chúng ta nên hạn chế sửa bừa bừa bãi. Bởi vì sửa lại phải kéo cả hội đồng và góp Ý. Còn lại thứ tự quy trình, tôi và bạn làm là đủ rồi. Cho nhanh. Cái gì đúng là nó chạy được thực tế. Còn vào thực tế mà mắc => phải sửa lại hết.»
- P03 · 16:52 · tên task: «Bạn ghi luôn là tên task mà làm theo MBM thì chữ đầu tiên phải là mbm-.... sau này chúng ta có nhiều công thức, quy định luôn cách đặt tên để còn biết tìm. Nhìn cái là phải hiểu nguồn gốc nó từ đâu.»
- P04 · 16:50 · viết gọn: «Giờ bạn tạo task trước đi, viết ngắn thôi nhưng đủ. 2 tạo tên 3. chôt mục tiêu + thê nào là hoàn thành => Kiểm tra lại các thông tin tôi đã chỉ đạo trước đây để viết vào. 4. Liệt kê ngắn gọn các đầu việc task (cái này để xem làm thế nào cho gọn). Nhắc lại tổng thể là viết ngắn gọn. Đừng viết dài quá các bạn cũng không đọc được đâu lại làm sai hết.»
- P09 · 21:12 · công thức + 2 vấn đề: «Yêu cầu User+Mục tiêu+Master list+Bước (Mốc · Mục con · Bước)+Bộ câu hỏi⇒MOW đổi thành => Yêu cầu User+ Mục tiêu + Mốc /Mục con/Bước+ Check Master list + Bộ câu hỏi⇒MOW. Tôi thấy bạn làm thực đang có 2 vấn đề: 1. Mục bước ví dụ QTTH 07 đã liệt kê ra, nhưng nhìn vào cột bước (chưa bàn thiếu đủ) thì chắc làm thế nào để hiểu cho nhất quán được. Bạn đang suy diễn theo cách hiểu của bạn để làm. Ai khác có thể sẽ làm theo cách không giống bạn. 2. Việc tiếp theo việc chốt được bước => như bạn vừa làm là kiểm kê lại các danh sách master list rõ ràng là việc cần, nhưng nên đưa vào đâu? Phải làm thực mới rút ra được kinh nghiệm => để ở vị trí đó có hợp lý không?»
- P08 · 20:41 · sửa MBM r5: «rõ ràng là làm thử thấy mắc ngày => cả MBM lẫn quy trình đều không khả thi. Giờ cần sửa lại cả. Chúng ta sẽ vừa sửa MBM vừa làm thử lại. Quy trình mà không thực hiện được hoặc thực hiện không nhất quán, hoặc không thể đạt mục tiêu => chả có nghĩa gì. 1. "② Chia mục và đặt mã" muc hướng dẫn này viết dài rồi cũng không làm được. Quy đinh là liệt kê đầy đủ theo mẫu: # Mốc Mục con Bước / 1 007-1 Khai việc — 1.1 Tra hoặc tạo việc duy nhất / 2 007-1 Khai việc — 1.2 Mở hồ sơ. Như bước bạn vừa làm 2. Trên công thức: Mốc, mục con, bước gồm thành 1 bước. 3. Bước tiếp theo nên là: Rà soát các master list. bạn sửa đi rồi tôi hướng dẫn tiếp. Sửa MBM trước đi»
- P07 · 18:01 · thử hiểu bước 1: «Vấn đề là các bước chúng ta đã bàn. AI bình thường có thực sự biết làm gì không> ví dụ bạn thử mô tả cho tôi mục 1 gồm: 1.1, 1.2 và 1.3 xem bản thân bạn hiểu là bạn cần phải làm gì nếu bạn được giao làm việc này?»
- P06 · 17:25 · dùng lại bản cũ: «Tôi chả hiểu bạn đang viết cái này là cái gì nữa? Bạn kiểm tra xem trước nếu chưa có MBM chúng ta đã bàn thế nào? mấy chục cái bước gồm những bước gì? Việc này mà chúng ta không MBM thì chúng ta cũng làm xong rồi đấy. Kiểm tra lại xem nào? Liệt kê cho tôi các cái bước chi tiết, theo tôi nhớ chúng ta còn làm cả hồ sơ rồi cơ mà? Các bạn cứ viết Tràng giang đại học xong lúc quay lại viết như là người không hiểu gì? Tôi cũng chả hiểu bạn đang viết gì luôn?»
- P05 · 17:05 · chốt ô 1–2: «1. Mục tiêu này 1. vẽ UI theo Master MOW 2. hoàn thiện Master list (đủ các master list có cần dùng và từn master phải được user duyệt lần đầu) 3. Điền đủ (SSOT) ( không có đối tượng liên quan đến quy trình này bị mồi côi (không có "sổ" để ghi, có sổ nhưng chưa được ghi, ghi ở 2 SSOT...) 4. Đủ trường để Config => list được hợp đồng thông tin liên quan 5. Dùng 100% DOT tạo collection, không làm hệ nặng. Bổ sung các DOT cần thiết, để dùng lại lâu dài. Ưu tiên chạy DOT nếu nếu có thể (tức là tự động 2. Thế nào là hoàn thành 1. Vẽ xong UI theo masterlist mow bao gồm hợp nhất các Mow hoặc tách cách mow 2. Xác đinh tin cậy số lượng đối tượng "mồ côi" (dùng dot) => đảm bảo không có đối tượng liên quan mô côi. 3. Các master list điền đầy đủ thông tin, đảm bảo SSOT 4. Xác đinh đủ hợp đồng thông tin để config không lỗi. Theo công thức: Yêu cầu User+Mục tiêu+Mốc+Mục con+Bước+Bộ câu hỏi⇒MOW chúng bạn đưa lên task và hoàn thành mục tiêu. Viết sao cho ngắn gọn nhưng làm được. Kinh nghiệm đau thương của tôi là các bạn viết dài nhưng cuối cùng vẫn sai, con người thì không nhìn được vì nó quá nhiều chữ»
