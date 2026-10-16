# COLLAB — mbm-qtth-07-ve-ui-mow
Tên việc: QTTH 07 — vẽ UI theo Master MOW, đủ Master list và hợp đồng thông tin, làm bằng công thức MBM

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner viết ô 1–2 ngày 16/10/2026 17:05.
Host: Claude Chat · Owner giao trực tiếp 16/10 16:29–17:05.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-16 17:20 +07 · Claude · P05
- 🎯 Mục tiêu: ô 1. Vì sao: bài thử MBM — lần 2 không có Owner, AI vẫn tự chạy.
- 🏁 Xong khi: ô 2.
- 📍 Tiến độ: [✓ 1 Nhận yêu cầu] → [✓ 2 Tạo task] → [✓ 3 Chốt mục tiêu] → [■ 4 Ma trận] → [□ 5 Ký] → [□ 6 Chạy]
- ✅ Đã xong: task `mbm-qtth-07-ve-ui-mow` · Owner chốt ô 1–2 (17:05) · ma trận bản gọn (Claude).
- ■ Đang làm: — · 0 RUN active
- ⬜ Còn lại: 5 Ký (Hermes kiểm mã + đếm ô · GPT, Gemini ký) → 6 Chạy từ bước 007-2.1.
- ➡ Kế tiếp: Host gửi hội đồng ký ma trận · 😊 Owner gật → chạy 007-2.1.
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
| 1 | Nhận yêu cầu | 🤖 | lời Owner ở Nhật ký | ☑ |
| 2 | Tạo task + tên | 🤖 | đúng khuôn, tên `mbm-` | ☑ `c8bfe619` |
| 3 | Chốt mục tiêu | 😊 | Owner viết ô 1–2 | ☑ 17:05 |
| 4 | Ma trận | 🤖 Claude viết | đủ Mốc · Bước · ô | ■ bản gọn đã có |
| 5 | Ký | 🤖 Hermes kiểm · ✍️ GPT, Gemini · 😊 Owner | 0 ô trống, 0 ô ❓, 0 phản đối | ☐ |
| 6 | Chạy | 🤖 | đạt ô 2 | ☐ |

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
| V5 | ma trận đủ A1–C4 từng dòng quá dài, người không đọc được | chưa sửa — đề xuất bản gọn (5 cột + luật chung); đổi bộ câu hỏi nên cần hội đồng ký ở bước 5 |

### Vòng trước
- 16/10 15:19 (Owner, nay gộp vào ô 1 bản 17:05): vẽ UI theo Master MOW · hoàn thiện Master list, điền đủ SSOT · đủ trường để Config · dùng DOT tạo collection.
- 15/10 (Owner, G1): vẽ UI, liệt kê trường còn thiếu để chốt hợp đồng thông tin, đủ trường để Config · 17:40: cái gì phát sinh cũng ghi vào Master list và kiểm đã ghi đủ.

## Ma trận QTTH 07 — Yêu cầu + Mục tiêu + Mốc + Bước + Bộ câu hỏi ⇒ MOW
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

## Nhật ký (nguyên văn Owner, giữ lỗi gõ)
- P01 · 16:29 · tạo việc: «Thấy bạn lúng túng lắm. Tức là các bạn viết ra đó nhưng các bạn chưa chắc đã làm được 1 quy trình từ MBM đâu. Đây sẽ là bài test thử. Đầu tiên bạn sửa lại việc này. Bổ sung phải taọ task trên workspace nữa. => bạn thấy đấy. Viết không đủ cụ thể, khôgn tính đến khi làm => vào làm là mắc. Chúng ta vừa làm vừa hiệu chỉnh toàn bộ MBM để làm sao các bước thật chi tiết. Lần 2 không có tôi AI thưc sự chạy được. Các bạn viết thì hay, nhưng khi các bạn làm là hỏng ngay. Giờ bổ sung phần đó và việc đầu tiên bạn tạo task trên WP đi. qtth.07-ve-UI-mow»
- P02 · 16:39 · thứ tự ④ + danh sách việc: «Không tôi nghĩ là nên làm ngược lại: ④ Làm một MOW bằng MBM. Nhận yêu cầu => tạo task Tạo task trên workspace => Chốt mục tiêu (quy trình sẵn cũ). Đưa 1 danh sách list những viẹc cần làm lên Task, cái nào làm xong thì tích. Lý do là các bạn ít đọc công thức, chỉ đọc 1 lần thôi. Còn lại task là cái mà lần nào cũng phải đọc lại, xem lại. Dễ bàn hơn. Sửa lại và làm thử theo xem có hợp lý không. Chưa hợp lý lại tiếp tục sửa. Chỉ có phần quét chi tiết mà hội đồng đã góp Ý nhiều lần => chúng ta nên hạn chế sửa bừa bừa bãi. Bởi vì sửa lại phải kéo cả hội đồng và góp Ý. Còn lại thứ tự quy trình, tôi và bạn làm là đủ rồi. Cho nhanh. Cái gì đúng là nó chạy được thực tế. Còn vào thực tế mà mắc => phải sửa lại hết.»
- P03 · 16:52 · tên task: «Bạn ghi luôn là tên task mà làm theo MBM thì chữ đầu tiên phải là mbm-.... sau này chúng ta có nhiều công thức, quy định luôn cách đặt tên để còn biết tìm. Nhìn cái là phải hiểu nguồn gốc nó từ đâu.»
- P04 · 16:50 · viết gọn: «Giờ bạn tạo task trước đi, viết ngắn thôi nhưng đủ. 2 tạo tên 3. chôt mục tiêu + thê nào là hoàn thành => Kiểm tra lại các thông tin tôi đã chỉ đạo trước đây để viết vào. 4. Liệt kê ngắn gọn các đầu việc task (cái này để xem làm thế nào cho gọn). Nhắc lại tổng thể là viết ngắn gọn. Đừng viết dài quá các bạn cũng không đọc được đâu lại làm sai hết.»
- P05 · 17:05 · chốt ô 1–2: «1. Mục tiêu này 1. vẽ UI theo Master MOW 2. hoàn thiện Master list (đủ các master list có cần dùng và từn master phải được user duyệt lần đầu) 3. Điền đủ (SSOT) ( không có đối tượng liên quan đến quy trình này bị mồi côi (không có "sổ" để ghi, có sổ nhưng chưa được ghi, ghi ở 2 SSOT...) 4. Đủ trường để Config => list được hợp đồng thông tin liên quan 5. Dùng 100% DOT tạo collection, không làm hệ nặng. Bổ sung các DOT cần thiết, để dùng lại lâu dài. Ưu tiên chạy DOT nếu nếu có thể (tức là tự động 2. Thế nào là hoàn thành 1. Vẽ xong UI theo masterlist mow bao gồm hợp nhất các Mow hoặc tách cách mow 2. Xác đinh tin cậy số lượng đối tượng "mồ côi" (dùng dot) => đảm bảo không có đối tượng liên quan mô côi. 3. Các master list điền đầy đủ thông tin, đảm bảo SSOT 4. Xác đinh đủ hợp đồng thông tin để config không lỗi. Theo công thức: Yêu cầu User+Mục tiêu+Mốc+Mục con+Bước+Bộ câu hỏi⇒MOW chúng bạn đưa lên task và hoàn thành mục tiêu. Viết sao cho ngắn gọn nhưng làm được. Kinh nghiệm đau thương của tôi là các bạn viết dài nhưng cuối cùng vẫn sai, con người thì không nhìn được vì nó quá nhiều chữ»
