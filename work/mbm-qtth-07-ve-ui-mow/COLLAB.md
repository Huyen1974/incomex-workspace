# COLLAB — mbm-qtth-07-ve-ui-mow
Tên việc: QTTH 07 — vẽ UI cho MOW theo Master MOW, làm bằng công thức MBM (thử trên MOW-001)

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: CHƯA XÁC NHẬN — chờ Owner gật ô 1–2, Mốc và Host.
Host: Claude Chat (đề xuất — chờ Owner gật) · đang giữ MBM, làm trực tiếp với Owner.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-16 17:05 +07 · Claude · P04
- 🎯 Mục tiêu: ô 1. Vì sao: bài thử MBM — lần 2 không có Owner, AI vẫn tự chạy.
- 🏁 Xong khi: ô 2.
- 📍 Tiến độ: [✓ 1 Nhận yêu cầu] → [✓ 2 Tạo task] → [■ 3 😊 Chốt mục tiêu] → [□ 4 Điền ma trận] → [□ 5 Ký] → [□ 6 Chạy thử MOW-001]
- ✅ Đã xong: tạo task, tên `mbm-qtth-07-ve-ui-mow`.
- ■ Đang làm: — · 0 RUN active
- ⬜ Còn lại: 3 → 4 → 5 → 6, đúng thứ tự.
- ➡ Kế tiếp: 😊 Owner gật ô 1–2 + Mốc + Host → Host giao hội đồng điền ma trận.
- ⛔ Không làm: G2/PG production · dựng collection trước khi ma trận được ký · gõ tay vào Directus.

### 1. Mục tiêu
Owner 15/10: vẽ UI, liệt kê được các trường còn thiếu để chốt được hợp đồng thông tin, và đảm bảo có đủ trường để Config.
Owner 15/10 17:40: bất cứ cái gì phát sinh phải ghi vào Master list tương ứng, rồi kiểm xem đã ghi đủ chưa.
Owner 16/10 15:19:
1. Vẽ UI theo Master MOW (MOW-001 đang thử nghiệm).
2. Hoàn thiện các Master list liên quan và điền đầy đủ thông tin (SSOT).
3. Rà soát đủ trường để Config thành công.
Cách làm: dùng DOT tạo collection; Master list tổ chức thành collection, không xây hệ thống nặng nề như trước.
Owner 16/10 16:29: làm QTTH 07 bằng MBM — bài test; vừa làm vừa sửa MBM để lần 2 không có Owner, AI vẫn chạy được.

### 2. Thế nào là hoàn thành
Trên MOW-001: UI thật đủ cho mọi hành động; Master list ghi đủ, đếm được phát sinh = đã có + mới ghi + còn thiếu, và còn thiếu = 0 (phát sinh 5 ghi 3 là chưa đạt); hợp đồng thông tin và Field đủ; Config chạy được trên nháp; Owner xem màn thật và duyệt. Chưa phải G2/PG production.
Và: một phiên AI mới làm theo QTTH 07, không hỏi thêm, vẫn ra đúng kết quả; mọi chỗ vấp đã sửa vào MBM.
(Nguồn: tiêu chí G1 Owner đã duyệt ở tools-quy-trinh ô 2, áp vào MOW-001.)

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

#### ☑ Việc cần làm — đọc lại mỗi lượt, xong tích kèm commit
| # | Việc | Ai | Xong khi | |
|---|---|---|---|---|
| 1 | Nhận yêu cầu | 🤖 | lời Owner ghi ở P01 | ☑ |
| 2 | Tạo task + tên | 🤖 | đúng khuôn AGENTS, tên `mbm-` | ☑ `c8bfe619` |
| 3 | Chốt mục tiêu | 😊 | Owner gật ô 1–2, Mốc, Host | ■ |
| 4 | Điền ma trận | 🤖 GPT điền · Hermes kiểm | mọi dòng đủ ô Thiết kế | ☐ |
| 5 | Ký + D1/D2 | 👥😊 | 0 ô trống, 0 ô ❓, hội đồng ký, Owner gật | ☐ |
| 6 | Chạy thử MOW-001 | 🤖 | đạt ô 2 | ☐ |

#### Mốc đề xuất (chờ Owner gật)
007-1 Khai việc → 007-2 UI cần gì → 007-3 Master list → 007-4 Field & Config → 007-5 Dựng UI & thử → 007-6 Kiểm & duyệt.

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| Claude | Anthropic | Claude Chat (`[auth:claude-chat]`) | Host (đề xuất) | Owner làm việc trực tiếp |
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

#### Nguồn
Công thức: CT-008 MBM (`work/mow-mot-moit-mout/ban-duyet.html#formula-ct-008`) · dùng lại: bài thử V15 (tools-quy-trinh P49 tại `f76fa2e1`) · việc mẹ: tools-quy-trinh.

### Vòng trước
—

## Ma trận QTTH 07
_(trống — điền ở bước 4)_

## Nhật ký (nguyên văn Owner, giữ lỗi gõ)
- P01 · 16:29 · tạo việc: «Thấy bạn lúng túng lắm. Tức là các bạn viết ra đó nhưng các bạn chưa chắc đã làm được 1 quy trình từ MBM đâu. Đây sẽ là bài test thử. Đầu tiên bạn sửa lại việc này. Bổ sung phải taọ task trên workspace nữa. => bạn thấy đấy. Viết không đủ cụ thể, khôgn tính đến khi làm => vào làm là mắc. Chúng ta vừa làm vừa hiệu chỉnh toàn bộ MBM để làm sao các bước thật chi tiết. Lần 2 không có tôi AI thưc sự chạy được. Các bạn viết thì hay, nhưng khi các bạn làm là hỏng ngay. Giờ bổ sung phần đó và việc đầu tiên bạn tạo task trên WP đi. qtth.07-ve-UI-mow»
- P02 · 16:39 · thứ tự ④ + danh sách việc: «Không tôi nghĩ là nên làm ngược lại: ④ Làm một MOW bằng MBM. Nhận yêu cầu => tạo task Tạo task trên workspace => Chốt mục tiêu (quy trình sẵn cũ). Đưa 1 danh sách list những viẹc cần làm lên Task, cái nào làm xong thì tích. Lý do là các bạn ít đọc công thức, chỉ đọc 1 lần thôi. Còn lại task là cái mà lần nào cũng phải đọc lại, xem lại. Dễ bàn hơn. Sửa lại và làm thử theo xem có hợp lý không. Chưa hợp lý lại tiếp tục sửa. Chỉ có phần quét chi tiết mà hội đồng đã góp Ý nhiều lần => chúng ta nên hạn chế sửa bừa bừa bãi. Bởi vì sửa lại phải kéo cả hội đồng và góp Ý. Còn lại thứ tự quy trình, tôi và bạn làm là đủ rồi. Cho nhanh. Cái gì đúng là nó chạy được thực tế. Còn vào thực tế mà mắc => phải sửa lại hết.»
- P03 · 16:52 · tên task: «Bạn ghi luôn là tên task mà làm theo MBM thì chữ đầu tiên phải là mbm-.... sau này chúng ta có nhiều công thức, quy định luôn cách đặt tên để còn biết tìm. Nhìn cái là phải hiểu nguồn gốc nó từ đâu.»
- P04 · 16:50 · viết gọn: «Giờ bạn tạo task trước đi, viết ngắn thôi nhưng đủ. 2 tạo tên 3. chôt mục tiêu + thê nào là hoàn thành => Kiểm tra lại các thông tin tôi đã chỉ đạo trước đây để viết vào. 4. Liệt kê ngắn gọn các đầu việc task (cái này để xem làm thế nào cho gọn). Nhắc lại tổng thể là viết ngắn gọn. Đừng viết dài quá các bạn cũng không đọc được đâu lại làm sai hết.» → viết lại toàn tệp ngắn gọn; ô 1 lấy đủ lời Owner 15/10 · 15/10 17:40 · 16/10 15:19 · 16:29; ô 2 lấy tiêu chí G1 Owner đã duyệt (tools-quy-trinh ô 2).
