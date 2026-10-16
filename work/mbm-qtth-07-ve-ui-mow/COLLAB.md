# COLLAB — mbm-qtth-07-ve-ui-mow
Tên việc: QTTH 07 — vẽ UI theo Master MOW, đủ Master list và hợp đồng thông tin, làm bằng công thức MBM

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner viết ô 1–2 ngày 16/10/2026 17:05.
Host: Claude Chat · Owner giao trực tiếp 16/10 16:29–17:05.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-16 22:35 +07 · Claude · P12
- 🎯 Mục tiêu: ô 1. Vì sao: bài thử MBM — lần 2 không có Owner, AI vẫn tự chạy.
- 🏁 Xong khi: ô 2.
- 📍 Tiến độ: [✓ 1 Nhận yêu cầu] → [✓ 2 Tạo task] → [✓ 3 Chốt mục tiêu] → [◐ 4 Liệt kê bước — bản thử] → [■ 5 Check Master list] → [□ 6 Bộ câu hỏi] → [□ 7 Ký] → [□ 8 Chạy]
- ✅ Đã xong: ô 1–2 (17:05) · bản thử bước 3 (26 bước) + bước 4 (kiểm kê 17 sổ) — xem tab «Nội dung công việc» (`view.html`).
- ■ Đang làm: — · 0 RUN active
- ⬜ Còn lại: chốt bước 4 → đạt bước 5 → 6 → 7 → 8.
- ➡ Kế tiếp: 😊 Owner xem «Vấn đề lộ ra» ở tab Nội dung công việc — nhất là 13 sổ cần duyệt lần đầu và 3 mã CAT lệch nghĩa.
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
| 4 | Liệt kê bước (MBM ③) | 🤖 | bảng đủ bước, mọi AI hiểu giống nhau | ◐ bản thử bên dưới · còn 1 ô ❓ (2.1) · chờ Owner gật khuôn + thử chéo |
| 5 | Check Master list (MBM ④) | 🤖 → 😊 | bảng kiểm kê đủ mọi sổ; Tình trạng = «đã có» hết | ■ bảng có · mới 4/17 «đã có» |
| 6 | Bộ câu hỏi (MBM ⑤) | 🤖 | mọi bước đủ ô | ☐ |
| 7 | Ký | 🤖 Hermes kiểm · ✍️ GPT, Gemini · 😊 Owner | 0 ô trống, 0 ô ❓, 0 phản đối | ☐ |
| 8 | Chạy | 🤖 | đạt ô 2 | ☐ |

Kết quả bước 3, bước 4 và vấn đề lộ ra: tab «Nội dung công việc» trên trang Task (tệp `view.html` của việc này) — 1 nơi, không chép lại ở đây.

<!-- BEGIN-REMOVE-P12
1. 🔴 **13/17 sổ chưa «đã có»** → mục 4 chặn, không sang được bộ câu hỏi. Cần Owner duyệt lần đầu — đề xuất duyệt theo nhóm.
2. 🔴 **Mã lệch nghĩa:** CAT-227 (trang: tiến trình công việc ↔ QTTH 07: Sổ việc) · CAT-228 (trang: việc thật MOT ↔ QTTH 07: hồ sơ 25 dòng) · CAT-239 (trang: Sổ tệp ↔ QTTH 07: ảnh). Không sửa thì ghi nhầm sổ.
3. 🟡 **Sổ của các sổ rỗng:** ML-DEF-012 = 0, việc của nó đang ở trang 47 Master List → 2 nơi cho 1 việc. Mục 4 cần ghi nguồn kiểm kê chuẩn.
4. 🟡 **Bộ tình trạng thiếu** «rỗng» và «dùng lại».
5. 🟡 **Bước 2.1 mơ hồ:** «nạp bước từ Công thức» — không viết được «Ra cái gì» chắc chắn → ❓.
6. 🟡 **Bước 2.2 trùng mục 4 MBM:** lúc chạy chỉ còn «So sổ cần với bảng kiểm kê».
7. 🟡 **Số lượng «—»** (CAT-239): nguồn chưa đọc, chưa đếm được.
8. ⚠ **Claude ghi sai số ở R59** (Master Tool 9 → thật 35; Master DOT «trống» → thật 311 qua CAT-006) vì đếm từ 1 tệp thay vì trang tổng — đã sửa R59.

#### Bước 3 · Mốc / Mục con / Bước — bản thử 16/10 22:15
Gốc: 25 bước Owner đã gật 15:19 (tools-quy-trinh P49 V15.1 tại `f76fa2e1`) + 4.0 đề xuất. Thử khuôn chưa gật: động từ chuẩn (Tạo · Ghi · Đếm · So · Duyệt · Chụp · Báo) + cột «Ra cái gì» + «Ghi vào sổ».

| # | Mốc | Mục con | Bước | Ra cái gì | Ghi vào sổ |
|---|---|---|---|---|---|
| 1 | 007-1 Khai việc | — | 1.1 Tạo việc cho MOW đích | 1 dòng việc có mã, đúng MOW đích, không trùng | CAT-227 |
| 2 | 007-1 Khai việc | — | 1.2 Tạo bảng hồ sơ cho việc | 1 bảng, số dòng = số bước | CAT-228 |
| 3 | 007-1 Khai việc | — | 1.3 Ghi 5 ô của việc | 5 ô có nội dung + nguồn | CAT-227 |
| 4 | 007-2 Chuẩn bị | — | 2.1 Ghi danh sách bước của MOW đích | ❓ «nạp bước từ Công thức» — Công thức nào, ra danh sách gì? | ML-MOW-TH-001 |
| 5 | 007-2 Chuẩn bị | — | 2.2 So sổ cần với bảng kiểm kê | danh sách sổ lệch; lệch = 0 | ML-DEF-012 |
| 6 | 007-2 Chuẩn bị | — | 2.3 Đếm lượt thử DOT đạt | 1 lượt PASS đúng phiên | CAT-229 |
| 7 | 007-3 Cổng | — | 3.1 Đếm bước 1.1–2.3 đạt | 6/6 đạt | CAT-228 |
| 8 | 007-4 Làm | A UI | 4.0 Duyệt giữ · hợp nhất · tách MOW (đề xuất) | mỗi MOW 1 quyết định | ML-DEF-004 · CAT-025 |
| 9 | 007-4 Làm | A UI | 4.1 Ghi UI cho từng hành động | hành động có UI / cần = 100% | ML-DEF-018 |
| 10 | 007-4 Làm | A UI | 4.2 So UI mới với UI có sẵn | mỗi cặp trùng có quyết định dùng lại | ML-DEF-018 |
| 11 | 007-4 Làm | A UI | 4.3 Ghi bảng cho từng màn | màn có bảng / màn = 100% | ML-DEF-018 · ML-DEF-012 |
| 12 | 007-4 Làm | B Hợp đồng | 4.4 Tạo nghĩa vụ thông tin cho từng màn | nghĩa vụ có dòng hợp đồng = 100% | CAT-206 |
| 13 | 007-4 Làm | B Hợp đồng | 4.5 So dữ liệu cần với Sổ Field, tạo Field thiếu | Field thiếu = 0 | ML-DEF-008 |
| 14 | 007-4 Làm | B Hợp đồng | 4.6 Ghi bảng đọc/ghi, ô bắt buộc | dòng hợp đồng đủ ô = 100% | CAT-206 |
| 15 | 007-4 Làm | C Đối soát | 4.7a Đếm đối tượng phát sinh: có sẵn · mới ghi · còn thiếu | còn thiếu = 0 | ML-DEF-012 |
| 16 | 007-4 Làm | C Đối soát | 4.7b So đối tượng đổi với nơi dùng | mỗi đổi có dòng ảnh hưởng | CAT-016 |
| 17 | 007-4 Làm | C Đối soát | 4.8 Tạo bản nháp bằng DOT, thử, đọc lại | biên nhận ĐẠT đúng SHA | CAT-229 |
| 18 | 007-5 Kiểm | — | 5.1 Đếm nghĩa vụ đã đủ | 100%; ghi khống = 0 | CAT-015 |
| 19 | 007-5 Kiểm | — | 5.2 Chụp mọi màn | màn có ảnh = 100% | CAT-239 |
| 20 | 007-5 Kiểm | — | 5.3 Duyệt chéo (ghế khác hãng) | 1 phiếu APPROVE hoặc REJECT | CAT-025 |
| 21 | 007-6 Duyệt | — | 6.1 Tạo gói duyệt | 1 gói đủ 5 thứ: link · ảnh · số · nợ · thay đổi | CAT-227 |
| 22 | 007-6 Duyệt | — | 6.2 Duyệt (Owner gật/lắc) | 1 quyết định | CAT-025 |
| 23 | 007-6 Duyệt | — | 6.3 Tạo nợ quay về khi lắc | mỗi lần lắc 1 nợ có bước quay về | CAT-069 |
| 24 | 007-7 Đóng | — | 7.1 Đếm 24 bước trước đạt | 100% | CAT-228 |
| 25 | 007-7 Đóng | — | 7.2 Đếm nợ mở đủ 4 ô | 100% | CAT-069 |
| 26 | 007-7 Đóng | — | 7.3 Ghi đóng việc, Báo Owner | việc «G1 đã duyệt» · 1 tin báo | CAT-227 |

#### Bước 4 · Check Master list — bảng kiểm kê 16/10 22:15
Nguồn số: trang «47 Master List · đang rà» (`ui-preview/mcp-writes/definition-master-index-v1.html`, cột Total theo nguồn) + sổ đăng ký `definition-master-registry-v1.js`. Gom từ cột «Ghi vào sổ» của bước 3.

| STT | Mã bảng | Tên bảng | Số lượng | Tình trạng | Ghi chú |
|---|---|---|---|---|---|
| 1 | ML-DEF-004 | Master MOW | 35 | đã có | xanh |
| 2 | ML-DEF-018 | Master UI con | 29 | đã có | xanh |
| 3 | ML-DEF-024 | Master DOT | 311 | đã có | dùng lại CAT-006 |
| 4 | ML-DEF-023 | Master Tool | 35 | đã có | xanh; cho DOT/công cụ mới (R59) |
| 5 | ML-DEF-008 | Master Field | 250 | User chưa duyệt UI | đã kiểm kê, PG chưa xác minh |
| 6 | ML-MOW-TH-001 | Master Quy trình tổng hợp | 6 | User chưa duyệt UI | đang thiết kế; QTTH 07 phải thành 1 dòng ở đây |
| 7 | CAT-227 | Master tiến trình công việc | 2 | User chưa duyệt UI | QTTH 07 dùng làm «Sổ việc» — cần đối chiếu nghĩa |
| 8 | CAT-228 | Sổ việc thật MOT · bản ghi · người | 8 | User chưa duyệt UI | QTTH 07 dùng làm «hồ sơ 25 dòng» — nghĩa lệch |
| 9 | CAT-229 | Sổ lần thử | 11 | User chưa duyệt UI | |
| 10 | CAT-206 | Danh mục hợp đồng vào/ra loại bản ghi | 66 | User chưa duyệt UI | |
| 11 | CAT-016 | Sổ nhật ký định nghĩa | 69 | User chưa duyệt UI | |
| 12 | CAT-015 | Sổ kết quả kiểm | 36 | User chưa duyệt UI | |
| 13 | CAT-239 | Sổ tệp | — | User chưa duyệt UI | chưa đọc nguồn nên chưa đếm; QTTH 07 dùng cho «ảnh màn» |
| 14 | CAT-025 | Sổ phiếu duyệt ý · bản | 41 | User chưa duyệt UI | |
| 15 | CAT-069 | Sổ nhu cầu · góp ý | 83 | User chưa duyệt UI | |
| 16 | ML-DEF-012 | Master of Master | 0 | chưa có | rỗng; việc của nó đang do trang 47 Master List làm |
| 17 | ML-DEF-022 | Master Step | 0 | chưa có | rỗng; MBM ghi ma trận vào đây |

END-REMOVE-P12 -->

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
| V1 | thiếu bước tạo task | r4.3 |
| V2 | chưa có khuôn tên task | r4.3 |
| V3 | sai thứ tự; task chưa có danh sách việc | r4.4 |
| V4 | tên task chưa cho biết nguồn gốc | r4.5 (`mbm-`) |
| V5 | ma trận đủ A1–C4 từng dòng quá dài | chưa sửa — đổi bộ câu hỏi cần hội đồng |
| V6 | Host bỏ qua bản 25 bước đã gật, tự viết mới (17:25) | r4.6: có bản cũ thì bắt đầu từ bản cũ |
| V7 | bước trỏ tới sổ và lệnh chưa có — AI thường không làm được (18:01) | r5: thêm bước Check Master list |
| V8 | mục «Chia mục và đặt mã» dài, làm không được (20:41) | r5: bảng mẫu |
| V9 | Check Master list đặt trước khi có bước là ngược (21:12) | r5.1: Bước → Check Master list → Bộ câu hỏi |
| V10 | tên bước ngắn, mỗi AI hiểu một kiểu (21:12) | chưa sửa — đang thử khuôn «Ra cái gì + Ghi vào sổ + động từ chuẩn», chờ Owner gật |
| V11 | mục 4 không nói tra số lượng ở đâu; Sổ của các sổ rỗng (22:15) | chưa sửa — đề xuất ghi nguồn kiểm kê chuẩn vào mục 4 |
| V12 | bộ tình trạng mục 4 thiếu «rỗng», «dùng lại» (22:15) | chưa sửa — chờ Owner |
| V13 | mã sổ trong bước và tên sổ thật lệch nghĩa (CAT-227/228/239) (22:15) | chưa sửa — đề xuất thêm ô «nghĩa khớp?» vào bảng kiểm kê |
| V14 | kết quả bước 3–4 đặt ngoài ô 3 nên trang Task (workspace) không hiện; «repo» và «workspace» mỗi bên hiểu một kiểu (Owner 22:07) | r5.6 mục 6: «làm ở workspace» |
| V15 | chuyển vào ô 3 vẫn không đọc được: tab Kiểm soát in thô bảng markdown và ô 3 mặc định gập; tab Nội dung báo «Chưa có view» (Owner 22:19) | r5.7: kết quả bước ghi vào `view.html` của task (HTML chính theo README) → tab Nội dung công việc; tạo task kèm `view.html` |

### Vòng trước
- 16/10 15:19 (Owner, nay gộp vào ô 1 bản 17:05): vẽ UI theo Master MOW · hoàn thiện Master list, điền đủ SSOT · đủ trường để Config · dùng DOT tạo collection.
- 15/10 (Owner, G1): vẽ UI, liệt kê trường còn thiếu để chốt hợp đồng thông tin, đủ trường để Config · 17:40: cái gì phát sinh cũng ghi vào Master list và kiểm đã ghi đủ.

## Nhật ký (nguyên văn Owner, giữ lỗi gõ)
- P12 · 22:19 · lỗi hiển thị: «Bạn kiểm tra xem có lỗi gì không? tôi kiểm tra mbm-qtth-07-ve-ui-mow không thấy chuyển về?»
- P11 · 22:07 · làm ở workspace: «Không, bạn đưa lên repo chứ. Đó bạn thấy không? mỗi người vẫn hiểu 1 kiểu, mỗi AI vẫn hiểu 1 kiểu. Và cái đó rõ ràng chưa thể trở thành quy trình được. Ghi thêm vài chữ là làm ở workspace để không hiểu nhầm nữa»
- P10 · 21:57 · làm thử bước 3–4: «Giờ quay lại QTTH 007. bạn làm bước 3,4 trên repo để thử xem còn vấn đề gì nữa chúng ta bàn tiếp.»
- P01 · 16:29 · tạo việc: «Thấy bạn lúng túng lắm. Tức là các bạn viết ra đó nhưng các bạn chưa chắc đã làm được 1 quy trình từ MBM đâu. Đây sẽ là bài test thử. Đầu tiên bạn sửa lại việc này. Bổ sung phải taọ task trên workspace nữa. => bạn thấy đấy. Viết không đủ cụ thể, khôgn tính đến khi làm => vào làm là mắc. Chúng ta vừa làm vừa hiệu chỉnh toàn bộ MBM để làm sao các bước thật chi tiết. Lần 2 không có tôi AI thưc sự chạy được. Các bạn viết thì hay, nhưng khi các bạn làm là hỏng ngay. Giờ bổ sung phần đó và việc đầu tiên bạn tạo task trên WP đi. qtth.07-ve-UI-mow»
- P02 · 16:39 · thứ tự ④ + danh sách việc: «Không tôi nghĩ là nên làm ngược lại: ④ Làm một MOW bằng MBM. Nhận yêu cầu => tạo task Tạo task trên workspace => Chốt mục tiêu (quy trình sẵn cũ). Đưa 1 danh sách list những viẹc cần làm lên Task, cái nào làm xong thì tích. Lý do là các bạn ít đọc công thức, chỉ đọc 1 lần thôi. Còn lại task là cái mà lần nào cũng phải đọc lại, xem lại. Dễ bàn hơn. Sửa lại và làm thử theo xem có hợp lý không. Chưa hợp lý lại tiếp tục sửa. Chỉ có phần quét chi tiết mà hội đồng đã góp Ý nhiều lần => chúng ta nên hạn chế sửa bừa bừa bãi. Bởi vì sửa lại phải kéo cả hội đồng và góp Ý. Còn lại thứ tự quy trình, tôi và bạn làm là đủ rồi. Cho nhanh. Cái gì đúng là nó chạy được thực tế. Còn vào thực tế mà mắc => phải sửa lại hết.»
- P03 · 16:52 · tên task: «Bạn ghi luôn là tên task mà làm theo MBM thì chữ đầu tiên phải là mbm-.... sau này chúng ta có nhiều công thức, quy định luôn cách đặt tên để còn biết tìm. Nhìn cái là phải hiểu nguồn gốc nó từ đâu.»
- P04 · 16:50 · viết gọn: «Giờ bạn tạo task trước đi, viết ngắn thôi nhưng đủ. 2 tạo tên 3. chôt mục tiêu + thê nào là hoàn thành => Kiểm tra lại các thông tin tôi đã chỉ đạo trước đây để viết vào. 4. Liệt kê ngắn gọn các đầu việc task (cái này để xem làm thế nào cho gọn). Nhắc lại tổng thể là viết ngắn gọn. Đừng viết dài quá các bạn cũng không đọc được đâu lại làm sai hết.»
- P09 · 21:12 · công thức + 2 vấn đề: «Yêu cầu User+Mục tiêu+Master list+Bước (Mốc · Mục con · Bước)+Bộ câu hỏi⇒MOW đổi thành => Yêu cầu User+ Mục tiêu + Mốc /Mục con/Bước+ Check Master list + Bộ câu hỏi⇒MOW. Tôi thấy bạn làm thực đang có 2 vấn đề: 1. Mục bước ví dụ QTTH 07 đã liệt kê ra, nhưng nhìn vào cột bước (chưa bàn thiếu đủ) thì chắc làm thế nào để hiểu cho nhất quán được. Bạn đang suy diễn theo cách hiểu của bạn để làm. Ai khác có thể sẽ làm theo cách không giống bạn. 2. Việc tiếp theo việc chốt được bước => như bạn vừa làm là kiểm kê lại các danh sách master list rõ ràng là việc cần, nhưng nên đưa vào đâu? Phải làm thực mới rút ra được kinh nghiệm => để ở vị trí đó có hợp lý không?»
- P08 · 20:41 · sửa MBM r5: «rõ ràng là làm thử thấy mắc ngày => cả MBM lẫn quy trình đều không khả thi. Giờ cần sửa lại cả. Chúng ta sẽ vừa sửa MBM vừa làm thử lại. Quy trình mà không thực hiện được hoặc thực hiện không nhất quán, hoặc không thể đạt mục tiêu => chả có nghĩa gì. 1. "② Chia mục và đặt mã" muc hướng dẫn này viết dài rồi cũng không làm được. Quy đinh là liệt kê đầy đủ theo mẫu: # Mốc Mục con Bước / 1 007-1 Khai việc — 1.1 Tra hoặc tạo việc duy nhất / 2 007-1 Khai việc — 1.2 Mở hồ sơ. Như bước bạn vừa làm 2. Trên công thức: Mốc, mục con, bước gồm thành 1 bước. 3. Bước tiếp theo nên là: Rà soát các master list. bạn sửa đi rồi tôi hướng dẫn tiếp. Sửa MBM trước đi»
- P07 · 18:01 · thử hiểu bước 1: «Vấn đề là các bước chúng ta đã bàn. AI bình thường có thực sự biết làm gì không> ví dụ bạn thử mô tả cho tôi mục 1 gồm: 1.1, 1.2 và 1.3 xem bản thân bạn hiểu là bạn cần phải làm gì nếu bạn được giao làm việc này?»
- P06 · 17:25 · dùng lại bản cũ: «Tôi chả hiểu bạn đang viết cái này là cái gì nữa? Bạn kiểm tra xem trước nếu chưa có MBM chúng ta đã bàn thế nào? mấy chục cái bước gồm những bước gì? Việc này mà chúng ta không MBM thì chúng ta cũng làm xong rồi đấy. Kiểm tra lại xem nào? Liệt kê cho tôi các cái bước chi tiết, theo tôi nhớ chúng ta còn làm cả hồ sơ rồi cơ mà? Các bạn cứ viết Tràng giang đại học xong lúc quay lại viết như là người không hiểu gì? Tôi cũng chả hiểu bạn đang viết gì luôn?»
- P05 · 17:05 · chốt ô 1–2: «1. Mục tiêu này 1. vẽ UI theo Master MOW 2. hoàn thiện Master list (đủ các master list có cần dùng và từn master phải được user duyệt lần đầu) 3. Điền đủ (SSOT) ( không có đối tượng liên quan đến quy trình này bị mồi côi (không có "sổ" để ghi, có sổ nhưng chưa được ghi, ghi ở 2 SSOT...) 4. Đủ trường để Config => list được hợp đồng thông tin liên quan 5. Dùng 100% DOT tạo collection, không làm hệ nặng. Bổ sung các DOT cần thiết, để dùng lại lâu dài. Ưu tiên chạy DOT nếu nếu có thể (tức là tự động 2. Thế nào là hoàn thành 1. Vẽ xong UI theo masterlist mow bao gồm hợp nhất các Mow hoặc tách cách mow 2. Xác đinh tin cậy số lượng đối tượng "mồ côi" (dùng dot) => đảm bảo không có đối tượng liên quan mô côi. 3. Các master list điền đầy đủ thông tin, đảm bảo SSOT 4. Xác đinh đủ hợp đồng thông tin để config không lỗi. Theo công thức: Yêu cầu User+Mục tiêu+Mốc+Mục con+Bước+Bộ câu hỏi⇒MOW chúng bạn đưa lên task và hoàn thành mục tiêu. Viết sao cho ngắn gọn nhưng làm được. Kinh nghiệm đau thương của tôi là các bạn viết dài nhưng cuối cùng vẫn sai, con người thì không nhìn được vì nó quá nhiều chữ»
