# COLLAB — mbm-qtth-07-ve-ui-mow
Tên việc: QTTH 07 — vẽ UI theo Master MOW, đủ Master list và hợp đồng thông tin, làm bằng công thức MBM

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner viết ô 1–2 ngày 16/10/2026 17:05.
Host: Claude Chat · Owner giao trực tiếp 16/10 16:29–17:05.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-17 05:25 +07 · Claude · P14
- 🎯 Mục tiêu: ô 1. Vì sao: bài thử MBM — lần 2 không có Owner, AI vẫn tự chạy.
- 🏁 Xong khi: ô 2.
- 📍 Tiến độ: [✓ 1 Nhận yêu cầu] → [✓ 2 Tạo task] → [✓ 3 Chốt mục tiêu] → [◐ 4 Liệt kê bước — bản thử] → [■ 5 Check Master list] → [□ 6 Bộ câu hỏi] → [□ 7 Ký] → [□ 8 Chạy]
- ✅ Đã xong: ô 1–2 (17:05) · bước 4 làm lại theo MBM r5.8: 3.1 Mốc (7) · 3.2 Mục con (3) · 3.3 Bước (26), có Câu hỏi + Hoàn thành · kiểm kê 17 sổ — xem tab «Nội dung công việc» (`view.html`).
- ■ Đang làm: — · 0 RUN active
- ⬜ Còn lại: chốt bước 4 → đạt bước 5 → 6 → 7 → 8.
- ➡ Kế tiếp: 😊 Owner xem «Vấn đề lộ ra» ở tab Nội dung công việc — nhất là 13 sổ cần duyệt lần đầu và 3 mã CAT lệch nghĩa.
- ⛔ Không làm: G2/PG production · dựng collection trước khi ma trận được ký · gõ tay vào Directus.

### 1. Mục tiêu
Tình trạng: User tạm chốt (Owner 17/10 11:59).
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

Kết quả bước 3, bước 4 và vấn đề lộ ra: tab «Nội dung công việc» trên trang Task (tệp `view.html` của việc này) — 1 nơi, không chép lại ở đây.

#### ☑ Việc cần làm — đọc lại mỗi lượt, xong tích kèm commit
| # | Việc | Ai | Xong khi | |
|---|---|---|---|---|
| 1 | Nhận yêu cầu (MBM ①) | 🤖 | lời Owner ở Nhật ký | ☑ |
| 2 | Tạo task + tên + view.html | 🤖 | đúng khuôn, tên `mbm-`, có `view.html` | ☑ `579bec00` |
| 3 | Chốt mục tiêu (MBM ②) | 😊 | Owner viết ô 1–2 | ☑ 17:05 |
| 4 | Liệt kê Mốc · Mục con · Bước (MBM ③) | 🤖 | 3 bảng 3.1–3.3 đủ dòng, mỗi dòng có Câu hỏi + Hoàn thành, 0 ô ❓ | ◐ bản thử 17/10 05:25 ở view.html · 0 ô ❓ · bước UI theo CT-004/CT-006 |
| 5 | Check Master list (MBM ④) | 🤖 → 😊 | bảng kiểm kê đủ mọi sổ; Tình trạng = «đã có» hết | ■ bảng ở view.html · mới 4/17 «đã có» |
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
| V1 | thiếu bước tạo task | r4.3 |
| V2 | chưa có khuôn tên task | r4.3 |
| V3 | sai thứ tự; task chưa có danh sách việc | r4.4 |
| V4 | tên task chưa cho biết nguồn gốc | r4.5 (`mbm-`) |
| V5 | ma trận đủ A1–C4 từng dòng quá dài | chưa sửa — đổi bộ câu hỏi cần hội đồng |
| V6 | Host bỏ qua bản 25 bước đã gật, tự viết mới (17:25) | r4.6: có bản cũ thì bắt đầu từ bản cũ |
| V7 | bước trỏ tới sổ và lệnh chưa có — AI thường không làm được (18:01) | r5: thêm bước Check Master list |
| V8 | mục «Chia mục và đặt mã» dài, làm không được (20:41) | r5: bảng mẫu |
| V9 | Check Master list đặt trước khi có bước là ngược (21:12) | r5.1: Bước → Check Master list → Bộ câu hỏi |
| V10 | tên bước ngắn, mỗi AI hiểu một kiểu (21:12) | r5.8: thêm cột Câu hỏi cần trả lời + Thế nào là hoàn thành (Owner 22:57) — thay đề xuất «Ra cái gì» |
| V11 | mục 4 không nói tra số lượng ở đâu; Sổ của các sổ rỗng (22:15) | chưa sửa — đề xuất ghi nguồn kiểm kê chuẩn vào mục 4 |
| V12 | bộ tình trạng mục 4 thiếu «rỗng», «dùng lại» (22:15) | chưa sửa — chờ Owner |
| V13 | mã sổ trong bước và tên sổ thật lệch nghĩa (CAT-227/228/239) (22:15) | chưa sửa — đề xuất thêm ô «nghĩa khớp?» vào bảng kiểm kê |
| V14 | kết quả bước 3–4 đặt ngoài ô 3 nên trang Task không hiện; «repo» và «workspace» mỗi bên hiểu một kiểu (Owner 22:07) | r5.6 mục 6: «làm ở workspace» |
| V19 | D1/D2 ghi «trả lời ở dòng MOW» + mục 6 bước 7 bắt trả lời trước khi ký → AI hiểu là việc phải giải xong trong quy trình và biến thành chỗ chặn (Owner 17/10 05:46) | r5.11: D1, D2 là câu hỏi mở, không chặn; ghi chú ẩn giải thích bản chất |
| V18 | Thử như AI mới mục 2: luật «mỗi gạch có số» mâu thuẫn lời User; hoàn thành 1–3 gạch quá ít; chưa rõ hội đồng có phải ký mục tiêu User tự viết (17/10 05:28) | r5.10 (Owner 05:36): AI viết số theo chuẩn, bám nội dung User · hoàn thành 3–5 gạch · User quyết ký/bỏ qua, User duyệt bắt buộc |
| V17 | Host tự đặt bước UI («hành động», «màn») thay vì dùng CT-004/CT-006 có sẵn; rà xuống dữ liệu MOW-001 (con) khi QTTH 07 (mẹ) chưa xong (Owner 17/10 05:15) | r5.9 (Owner 05:22): tiêu đề «3.3 Bước (nền tảng = nhóm con, có thể điều chỉnh cho sát thực tế)»; gỡ ghi chú Host tự thêm |
| V16 | mục 3 chỉ có 1 bảng bước, thiếu tầng Mốc và Mục con có câu hỏi + hoàn thành (Owner 22:57) | r5.8: mục 3 = 3.1 Mốc · 3.2 Mục con · 3.3 Bước |
| V15 | chuyển vào ô 3 vẫn không đọc được: tab Kiểm soát in thô bảng và ô 3 mặc định gập; tab Nội dung báo «Chưa có view» (Owner 22:19) | r5.7: bảng kết quả ghi vào `view.html` của task → tab Nội dung công việc; tạo task kèm `view.html` |

### Vòng trước
- 16/10 15:19 (Owner, nay gộp vào ô 1 bản 17:05): vẽ UI theo Master MOW · hoàn thiện Master list, điền đủ SSOT · đủ trường để Config · dùng DOT tạo collection.
- 15/10 (Owner, G1): vẽ UI, liệt kê trường còn thiếu để chốt hợp đồng thông tin, đủ trường để Config · 17:40: cái gì phát sinh cũng ghi vào Master list và kiểm đã ghi đủ.

## Nhật ký (nguyên văn Owner, giữ lỗi gõ)
- P23 · 17/10 14:17 · chốt 5 mốc + mục con: «Vẫn mơ hồ (ý tôi là chưa thật cụ thể) và mỗi Ai có thể làm 1 kiểu. … Mốc gồm: 1. Khai việc 2. Rà soát chuẩn bị (master list, DOT, tool) 3. Triển khai (nếu Dài AI tự chia bước) 4. Kiểm tra: 5. Báo cáo. Mục con: Trong mục 2 (rà soát), mục 3 triển khai có thể chia nhỏ hơn thành mục con) Tuỳ AI cân đối 1. Lập danh sách DOT đã có, DOT cần thêm và DOT sửa lại (nếu có) 2. Lập danh sách Master list đã có/cần user phê duyệt UI/ Cần làm mới (nếu cần) 3. Tạo mới/nâng cấp các danh sách DOT cần làm nếu có 4. Tạo mới/nâng cấp các danh sách master list cần làm nếu có 5. (Option) AI chia nhỏ triển khai thành nhiều phần nếu cần. => Viết 1 định nghĩa rất ngắn và chốt bảng mốc và mục con luôn. => Bước thực sự phải triển khai theo cả mốc và mục con + Nhóm con đấy (việc này phải nghĩ thêm chút). … Bạn sửa thêm rồi tôi nhìn vào đó bàn tiếp (Sửa MBM trước), chúng xem đưa thẳng vào MBM khoá cứng ổn không?»
- P22 · 17/10 13:54 · định nghĩa Mốc/Mục con: «… Tư duy đơn giản là: cứ có chỗ để điền, AI sẽ biết cách điền thông tin. => Vấn đề là quy định về form mẫu chuẩn. Đọc có thể hiểu. Giờ nhìn vào bạn làm thử: tôi thấy khái niệm: Mốc là gì chưa rõ (AI - Bạn) đang tự làm theo ý. Mục con cũng tương tự. Cái này phải định nghĩa rõ từ MBM. Mốc phải > mục con, mốc chứa nhiều mục con mới đúng (và mục con là nếu có) tức là quá dài thì mới cần mục con để chia nhỏ mốc => Bạn rà soát cái này.»
- P21 · 17/10 12:25 · nhật ký = CAT-227 + CAT-069: «Đây lại là vấn đề thiết kế chưa rõ rõ ràng. MBM có lẽ lần đầu phải mang trọng trách để hướng dẫn hệ thống. Thực sự thì chưa ai, kể cả bạn đang hình dung được Hệ thống gồm những master list nào. Đó là vấn đề cần giải quyết. Tôi thì hình dung ra 1 số nhưng không thể đủ? Phần nhật ký này thực ra về bản chất chúng ta có 2 bảng: 1. Thứ nhất là tiến trình (CAT-227). Chúng ta bắt đầu làm từ việc gì => điền vào đây. Từ việc bé đến việc to (từ sửa 1 cách đến thực hiện 1 quy trình tổng hợp rất lớn, tất cả đều được gọi chung bằng 1 "việc" => có 1 dòng => có 1 mã việc riêng 2. Bảng ghi chép lại công nợ (CAT-069) khi đang làm. Nhưng bảng này chưa điền của mã việc CAT-227. Tức là những khúc mắc của việc 227. Vấn đề là những việc này là hệ thống chung => nên viết từ MBM để các quy trình do MBM sinh ra nhứ QTTH 007 chép lại. Bạn điều chỉnh lại từ MBM và xem 2 việc này còn vướng nữa không? … AI phải tự đọc để xem có hiểu cách làm không? Chứ các bạn cứ góp Ý ào ào, đến lúc làm lại tắc => Vô nghĩa mất thời gian»
- P20 · 17/10 11:59 + 12:04 · tình trạng mục tiêu: «bạn có đang phức tạp hoá lên không. Mục tiêu user tam chốt rồi => đi quay lại 1 vấn đề đã chốt rồi làm gì? Cái chính là hiện nay AI không biết được là User chốt chưa? Thiếu tình trạng. … Cần phải làm kỹ lưỡng từng chút 1. Làm ào là gãy. … Bàn ít một đã» — «Đồng ý thêm tình trạng.»
- P19 · 17/10 11:52 · D1/D2 trỏ CAT-249: «Như vậy cần ghi rõ trên MBM => đọc từ MBM sang QTTH 007 để Ai hiểu là rà soát lại (không chặn) để cập nhật thêm các Tool/giải pháp mới, dùng lại nếu có..... ghi nhắn gọn nhưng mọi người hiểu là có vấn đề D1, D2 và dẫn chiếu đến Cat 249 là ok. Nhìn lại lần nữa xem QTTH 007 làm theo MBM từ 1-4 có còn mắc gì không? Nhìn như AI phải làm việc này lần đầu tiên, để đọc xem còn chỗ nào khó hiểu? Chỗ nào không hiểu?»
- P18 · 17/10 07:13 · Master công cụ giám sát: «Thay vì lý thuyết. Bạn tạo luôn giup tôi 1 master list về: Master công cụ giám sát. Đăt mã, đặt tên, vẽ Ui cho nó và đưa vào thành 48 list. Chỉ cần có list master có chỗ là AI biết điền, giải thích dài dòng làm gì?» → đã tạo CAT-249* · UI.MASTER.TQT.249 · `process-work-master-v1.html?master=CAT-249%2A` · danh sách Master = 48 (commit `65785b73`, `3bd15fae`).
- P17 · 17/10 05:46 · bản chất D1, D2: «D1. D2 bạn cho vào đó là sai => lòi ra. bản chất tôi đã giải thích. 1. Cơ chế này không thể giải quyết hiệu quả trong 1 việc/ trong 1 quy trình cụ thể. Mà phải giải quyết ở tầm MBM hoặc cao hơn. Các giải pháp đưa ra sẽ phức tạp và cần được tích luỹ theo thời gian. Ví dụ cơ chế chốgn lệch của PG giống như các dịch vụ của google về bất đối xứng... các công nghệ chung của Direcutus. Những việc này có thể là tổng hợp của nhiều công nghệ/DOT và giải pháp khác nhau. 2. Tôi muốn viết vào từng việc như QTTH 07 và xét vào từng việc là để 1 lần nhìn lại vấn đề này xem cí làm được gì không? Có cái gì đã bàn , đã làm mà chưa áp dụng không? Có áp dụng được cái mới gì không?.... 3. D1, D2 nó giống như câu hỏi mở, có quy trình để xem, có nơi (sổ /master list) để ghi các phương án đã áp dụng... để trả lời những câu hỏi ở mục 2. Cái này làm rõ và nên ghi chú ẩn được về D1, D2. Không làm thì kết quả tệ,. không ghi thì mai quên lãng không ai nhớ, chẳng ai bàn và viẹc này quên lãng + kết quả tệ. Nhưng ghi ra không được biến thành block»
- P16 · 17/10 05:36 · mục 2 MBM: «2.1 thì thống nhất các bạn viết số vào. Bám vào nội dung của tôi, còn số là phần trình bày, làm thế nào (viết ngắn để AI hiểu là có format chủ động theo chuẩn) 2.2 chuyển luôn thành 3-5 gjach đi 2.3. (User quyết hội đồng ký/bỏ qua bước này), tức là User duyệt vẫn là bắt buộc. 2.4 Tôi chưa hiểu bạn đang vướng gì? Chúng ta làm từng mục cho dễ.»
- P15 · 17/10 05:22 · tiêu đề 3.3 MBM: «3.3 Bước … => đổi thành: 3.3 Bước (nền tảng = nhóm con, có thể điều chỉnh cho sát thực tế). Không tự viết lung tung vào MBM khi tôi chưa yêu cầu!»
- P14 · 17/10 05:08 + 05:15 · bước theo công thức: «Bạn chưa hiểu sâu hết đâu. Mục: 3.3 Bước của QTTH 07 => bạn ghi chú ngay sau "3.3 Bước" là: (Bước tính theo nhóm con, mỗi quy trình có số UI tính theo công thức của UI con) Chúng ta đã có những công thức cho việc này rồi. => bạn thử rà soát lại xem số bước đúng chưa?» — «bạn đang nhầm lẫn: 1. công thức ngay trong này (trên phần MBM một tí ...) 2. Chúng ta đang chế tạo QTTH 07 từ MBM: MBM => QTTH 07 (và các quy trình khác sau này) => QT 01 của master mow. Đừng rà cái con khi cái mẹ còn chưa xong. Các bạn đang phức tạp lên. Nhóm con CT-004 Chuỗi+Bước con+Tầng⇒Nhóm con. UI Con CT-006 Chuỗi+Bước+Tầng+Nhóm+UI cha⇒UI Con. Công thức có vài chữ thôi, nhưng con người nhìn vào đây là hiểu hết. Các bạn chữ nhiều nhưng rối tinh lên»
- P13 · 22:57 · mục 3 thành 3 bảng: «Mục 3 triển khai tôi nhìn thấy phải sửa từ MBM. 1. Thêm mục 3.1. Mốc 3.2 Mục con 3.3 Bước (hiện tại chuyển thành bước) 3.1 Để các cột. STT; Tên Mốc; Câu hỏi cần trả lời; Thế nào là hoàn thành 2. Bảng 3.1 Để các cột. STT; Tên Mốc; Câu hỏi cần trả lời; Thế nào là hoàn thành 3.2 Cột: STT; Tên Mốc; Tên mục con; Câu hỏi cần trả lời; Thế nào là hoàn thành 3.3 Cần thêm 2 cột Câu hỏi cần trả lời; Thế nào là hoàn thành. Sau đó thử làm lại trên Repo xem? Cần hoàn thiện từng bước cho hợp lý.»
- P12 · 22:19 · lỗi hiển thị: «Bạn kiểm tra xem có lỗi gì không? tôi kiểm tra mbm-qtth-07-ve-ui-mow không thấy chuyển về?»
- P11 · 22:07 · làm ở workspace: «Không, bạn đưa lên repo chứ. Đó bạn thấy không? mỗi người vẫn hiểu 1 kiểu, mỗi AI vẫn hiểu 1 kiểu. Và cái đó rõ ràng chưa thể trở thành quy trình được. Ghi thêm vài chữ là làm ở workspace để không hiểu nhầm nữa»
- P10 · 21:57 · làm thử bước 3–4: «Giờ quay lại QTTH 007. bạn làm bước 3,4 trên repo để thử xem còn vấn đề gì nữa chúng ta bàn tiếp.»
- P09 · 21:12 · công thức + 2 vấn đề: «Yêu cầu User+Mục tiêu+Master list+Bước (Mốc · Mục con · Bước)+Bộ câu hỏi⇒MOW đổi thành => Yêu cầu User+ Mục tiêu + Mốc /Mục con/Bước+ Check Master list + Bộ câu hỏi⇒MOW. Tôi thấy bạn làm thực đang có 2 vấn đề: 1. Mục bước ví dụ QTTH 07 đã liệt kê ra, nhưng nhìn vào cột bước (chưa bàn thiếu đủ) thì chắc làm thế nào để hiểu cho nhất quán được. Bạn đang suy diễn theo cách hiểu của bạn để làm. Ai khác có thể sẽ làm theo cách không giống bạn. 2. Việc tiếp theo việc chốt được bước => như bạn vừa làm là kiểm kê lại các danh sách master list rõ ràng là việc cần, nhưng nên đưa vào đâu? Phải làm thực mới rút ra được kinh nghiệm => để ở vị trí đó có hợp lý không?»
- P08 · 20:41 · sửa MBM r5: «rõ ràng là làm thử thấy mắc ngày => cả MBM lẫn quy trình đều không khả thi. Giờ cần sửa lại cả. Chúng ta sẽ vừa sửa MBM vừa làm thử lại. Quy trình mà không thực hiện được hoặc thực hiện không nhất quán, hoặc không thể đạt mục tiêu => chả có nghĩa gì. 1. "② Chia mục và đặt mã" muc hướng dẫn này viết dài rồi cũng không làm được. Quy đinh là liệt kê đầy đủ theo mẫu: # Mốc Mục con Bước / 1 007-1 Khai việc — 1.1 Tra hoặc tạo việc duy nhất / 2 007-1 Khai việc — 1.2 Mở hồ sơ. Như bước bạn vừa làm 2. Trên công thức: Mốc, mục con, bước gồm thành 1 bước. 3. Bước tiếp theo nên là: Rà soát các master list. bạn sửa đi rồi tôi hướng dẫn tiếp. Sửa MBM trước đi»
- P07 · 18:01 · thử hiểu bước 1: «Vấn đề là các bước chúng ta đã bàn. AI bình thường có thực sự biết làm gì không> ví dụ bạn thử mô tả cho tôi mục 1 gồm: 1.1, 1.2 và 1.3 xem bản thân bạn hiểu là bạn cần phải làm gì nếu bạn được giao làm việc này?»
- P06 · 17:25 · dùng lại bản cũ: «Tôi chả hiểu bạn đang viết cái này là cái gì nữa? Bạn kiểm tra xem trước nếu chưa có MBM chúng ta đã bàn thế nào? mấy chục cái bước gồm những bước gì? Việc này mà chúng ta không MBM thì chúng ta cũng làm xong rồi đấy. Kiểm tra lại xem nào? Liệt kê cho tôi các cái bước chi tiết, theo tôi nhớ chúng ta còn làm cả hồ sơ rồi cơ mà? Các bạn cứ viết Tràng giang đại học xong lúc quay lại viết như là người không hiểu gì? Tôi cũng chả hiểu bạn đang viết gì luôn?»
- P05 · 17:05 · chốt ô 1–2: «1. Mục tiêu này 1. vẽ UI theo Master MOW 2. hoàn thiện Master list (đủ các master list có cần dùng và từn master phải được user duyệt lần đầu) 3. Điền đủ (SSOT) ( không có đối tượng liên quan đến quy trình này bị mồi côi (không có "sổ" để ghi, có sổ nhưng chưa được ghi, ghi ở 2 SSOT...) 4. Đủ trường để Config => list được hợp đồng thông tin liên quan 5. Dùng 100% DOT tạo collection, không làm hệ nặng. Bổ sung các DOT cần thiết, để dùng lại lâu dài. Ưu tiên chạy DOT nếu nếu có thể (tức là tự động 2. Thế nào là hoàn thành 1. Vẽ xong UI theo masterlist mow bao gồm hợp nhất các Mow hoặc tách cách mow 2. Xác đinh tin cậy số lượng đối tượng "mồ côi" (dùng dot) => đảm bảo không có đối tượng liên quan mô côi. 3. Các master list điền đầy đủ thông tin, đảm bảo SSOT 4. Xác đinh đủ hợp đồng thông tin để config không lỗi. Theo công thức: Yêu cầu User+Mục tiêu+Mốc+Mục con+Bước+Bộ câu hỏi⇒MOW chúng bạn đưa lên task và hoàn thành mục tiêu. Viết sao cho ngắn gọn nhưng làm được. Kinh nghiệm đau thương của tôi là các bạn viết dài nhưng cuối cùng vẫn sai, con người thì không nhìn được vì nó quá nhiều chữ»
- P04 · 16:50 · viết gọn: «Giờ bạn tạo task trước đi, viết ngắn thôi nhưng đủ. 2 tạo tên 3. chôt mục tiêu + thê nào là hoàn thành => Kiểm tra lại các thông tin tôi đã chỉ đạo trước đây để viết vào. 4. Liệt kê ngắn gọn các đầu việc task (cái này để xem làm thế nào cho gọn). Nhắc lại tổng thể là viết ngắn gọn. Đừng viết dài quá các bạn cũng không đọc được đâu lại làm sai hết.»
- P03 · 16:52 · tên task: «Bạn ghi luôn là tên task mà làm theo MBM thì chữ đầu tiên phải là mbm-.... sau này chúng ta có nhiều công thức, quy định luôn cách đặt tên để còn biết tìm. Nhìn cái là phải hiểu nguồn gốc nó từ đâu.»
- P02 · 16:39 · thứ tự ④ + danh sách việc: «Không tôi nghĩ là nên làm ngược lại: ④ Làm một MOW bằng MBM. Nhận yêu cầu => tạo task Tạo task trên workspace => Chốt mục tiêu (quy trình sẵn cũ). Đưa 1 danh sách list những viẹc cần làm lên Task, cái nào làm xong thì tích. Lý do là các bạn ít đọc công thức, chỉ đọc 1 lần thôi. Còn lại task là cái mà lần nào cũng phải đọc lại, xem lại. Dễ bàn hơn. Sửa lại và làm thử theo xem có hợp lý không. Chưa hợp lý lại tiếp tục sửa. Chỉ có phần quét chi tiết mà hội đồng đã góp Ý nhiều lần => chúng ta nên hạn chế sửa bừa bừa bãi. Bởi vì sửa lại phải kéo cả hội đồng và góp Ý. Còn lại thứ tự quy trình, tôi và bạn làm là đủ rồi. Cho nhanh. Cái gì đúng là nó chạy được thực tế. Còn vào thực tế mà mắc => phải sửa lại hết.»
- P01 · 16:29 · tạo việc: «Thấy bạn lúng túng lắm. Tức là các bạn viết ra đó nhưng các bạn chưa chắc đã làm được 1 quy trình từ MBM đâu. Đây sẽ là bài test thử. Đầu tiên bạn sửa lại việc này. Bổ sung phải taọ task trên workspace nữa. => bạn thấy đấy. Viết không đủ cụ thể, khôgn tính đến khi làm => vào làm là mắc. Chúng ta vừa làm vừa hiệu chỉnh toàn bộ MBM để làm sao các bước thật chi tiết. Lần 2 không có tôi AI thưc sự chạy được. Các bạn viết thì hay, nhưng khi các bạn làm là hỏng ngay. Giờ bổ sung phần đó và việc đầu tiên bạn tạo task trên WP đi. qtth.07-ve-UI-mow»
