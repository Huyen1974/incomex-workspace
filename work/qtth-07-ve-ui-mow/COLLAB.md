# COLLAB — qtth-07-ve-ui-mow
Tên việc: QTTH 07 — vẽ được UI cho một MOW theo Master MOW, làm bằng công thức MBM (thử trên MOW-001)

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: CHƯA XÁC NHẬN — Owner giao tạo việc 16/10/2026 16:29; chờ Owner gật ô 2 (đề xuất), Mốc và Host ở ô 3 (MBM ④.3).
Host: Claude Chat (đề xuất — chờ Owner gật) · lý do: đang giữ công thức MBM (CT-008) và nhận lệnh Owner trực tiếp cho việc này.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-16 16:45 +07 · Claude · P01
- 🎯 Mục tiêu: ô 1 — QTTH 07 vẽ UI cho MOW theo Master MOW, làm bằng MBM. Vì sao: đây là bài thử MBM — lần 2 không có Owner, AI vẫn tự chạy được.
- 🏁 Xong khi: ô 2.
- 📍 Tiến độ: [✓ ④.1 mã MOW-TH-007] → [✓ ④.2 tạo task] → [■ ④.3 😊 Owner chốt ô 2 · Mốc · Host] → [□ ④.4 điền ma trận] → [□ ④.5 ký + D1/D2] → [□ ④.6 chạy thử MOW-001]
- ✅ Đã xong: mã MOW-TH-007 (bản 2, viết bằng MBM) · tạo task đúng khuôn AGENTS (P01).
- ■ Đang làm: — · 0 RUN active
- ⬜ Còn lại: ④.3 → ④.4 → ④.5 → ④.6, đúng thứ tự.
- ➡ Kế tiếp: 😊 Owner gật ô 2 + Mốc + Host (đề xuất ở ô 3) · rồi Host giao hội đồng điền ma trận (④.4), dùng lại bài thử P49 V15 của tools-quy-trinh.
- ⛔ Không làm/để sau: dựng collection trước khi ma trận được ký · làm việc B1/B2 của tools-quy-trinh ở đây · sửa CT-008 ngoài chỗ vấp đã ghi ở Sổ vấp.

### 1. Mục tiêu
Owner 16/10/2026 15:19:
1. Vẽ UI theo Master MOW (mà MOW 001 đang thử nghiệm).
2. Hoàn thiện được các Master list liên quan và điền đầy đủ thông tin vào các Master list (SSOT).
3. Rà soát đủ trường để Config thành công.
Cách làm: dùng DOT tạo collection; các Master list tổ chức thành collection để không xây một hệ thống nặng nề như trước.
Owner 16/10/2026 16:29:
4. Làm QTTH 07 từ MBM — đây là bài test. Vừa làm vừa hiệu chỉnh MBM cho các bước thật chi tiết, để lần 2 không có Owner, AI thực sự chạy được.

### 2. Thế nào là hoàn thành
(đề xuất — chờ Owner gật) Thử trên MOW-001: mọi hành động cần màn hình đều có UI vẽ theo Master MOW; mọi Master list cần dùng đã có collection và đủ dữ liệu nạp từ gốc, không dòng nào thiếu ô bắt buộc; không thiếu Field nào và lượt thử Config trên nháp đạt; Owner xem màn hình thật và gật. Kèm theo: mọi chỗ vấp đã sửa vào MBM (CT-008) để lần sau AI tự chạy.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| Claude | Anthropic | Claude Chat (`[auth:claude-chat]`) | Host (đề xuất — chờ Owner gật) | Owner làm việc trực tiếp |
| GPT Chat | OpenAI | GPT Chat (`openai-mcp`) | Council · ghế ký | Owner chuyển tay |
| Hermes | Hermes VPS (DeepSeek) | `agent-gw/hermes` | Council · ghế ký · nhận việc thường trước (R57 tools-quy-trinh) | Owner chuyển tay |
| Gemini | Google | `gemini-agy` | Council · ghế ký | Owner chuyển tay |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: luật quyết = luật ký MBM (CT-008); danh tính và nhãn chữ ký theo tools-quy-trinh COLLAB mục 3.3

#### Đề xuất cho ④.3 (chờ Owner gật)
- **① Mục tiêu đo được:** (1) UI — hành động có UI / hành động cần UI = 100% · (2) Master list — sổ có collection / sổ cần = 100%, dòng thiếu ô bắt buộc = 0 · (3) Config — Field thiếu = 0, lượt thử Config trên nháp đạt.
- **Mốc (2.1), xem UI cần gì trước rồi mới làm sổ (JEV 0,98):** 007-1 Khai việc · 007-2 UI cần gì (từ Master MOW: hành động → màn → dữ liệu cần) · 007-3 Master list (sổ cần → thiết kế cột, Owner gật → DOT tạo collection → nạp dữ liệu) · 007-4 Field & Config (đủ trường, nối bảng, thử Config) · 007-5 Dựng UI & thử (màn thật trên nháp, ảnh) · 007-6 Kiểm & duyệt (đối soát ⑤, Owner xem màn thật, đóng).
- **Mục con (2.2):** chỉ tách khi mốc có hơn 5 bước — biết khi điền ma trận.
- **D1/D2:** D1 làm sai bị chặn bởi GS-01 · GS-02 · GS-03 · GS-04 · D2 quên ghi sổ bị bắt bởi GS-07 · GS-08 · GS-09 (CT-008 ⑥).
- **Host:** Claude Chat (lý do ở dòng Host đầu §0).

#### Nguồn
- Công thức: CT-008 MBM — `work/mow-mot-moit-mout/ban-duyet.html#formula-ct-008` (đang r4.3). Ô «4 TẦNG» đầu tab Công thức.
- Dùng lại: bài thử MBM — `work/tools-quy-trinh/proposals/TQT-PR-20261013-claude-cowork-87steps-P49.md` mục V15.1 + V15.2 tại `f76fa2e1` (mã 008-x.y đọc là 007-x.y). Chỉ lấy dòng khớp Mốc mới.
- Việc mẹ: tools-quy-trinh (Định vị · R57–R60).

#### Sổ vấp MBM — vấp đâu ghi ngay, rồi sửa CT-008 tại chỗ
| # | Lúc | Vấp ở bước | Vấp gì | Đã sửa ở CT-008 |
|---|---|---|---|---|
| V1 | 16/10 16:29 | ④ (trước ④.2) | MBM thiếu bước tạo task trên workspace; viết không tính đến lúc làm thật (Owner phát hiện) | ④.2 «Tạo task trên workspace», User chốt cả Host ở ④.3, nơi ghi tạm ở COLLAB task (r4.3 `f091ae11`) |
| V2 | 16/10 16:35 | ④.2 | Tên Owner đặt `qtth.07-ve-UI-mow` có dấu chấm, chữ hoa; MBM chưa nói khuôn tên | ④.2 ghi rõ «chữ thường nối gạch ngang»; đã chuẩn hoá thành `qtth-07-ve-ui-mow` (JEV 1,00) |

#### Nơi ghi
- Ô 1–3 của tệp này = dòng MOW-TH-007 cho tới khi Sổ quy trình ML-MOW-TH-001 thành collection.
- Ma trận = mục «Ma trận QTTH 07» bên dưới, cho tới khi ML-DEF-022 thành collection.

### Vòng trước
— (việc mới, chưa có vòng trước)

## Ma trận QTTH 07 (MBM ③ — điền ở ④.4)
_(trống — điền sau khi Owner gật ④.3)_

## P01 · Claude · tạo việc theo MBM ④.2 · 16/10/2026 16:45 +07
- Owner giao (nguyên văn, giữ lỗi gõ): «Thấy bạn lúng túng lắm. Tức là các bạn viết ra đó nhưng các bạn chưa chắc đã làm được 1 quy trình từ MBM đâu. Đây sẽ là bài test thử. Đầu tiên bạn sửa lại việc này. Bổ sung phải taọ task trên workspace nữa. => bạn thấy đấy. Viết không đủ cụ thể, khôgn tính đến khi làm => vào làm là mắc. Chúng ta vừa làm vừa hiệu chỉnh toàn bộ MBM để làm sao các bước thật chi tiết. Lần 2 không có tôi AI thưc sự chạy được. Các bạn viết thì hay, nhưng khi các bạn làm là hỏng ngay. Giờ bổ sung phần đó và việc đầu tiên bạn tạo task trên WP đi. qtth.07-ve-UI-mow»
- Đã làm: (1) sửa CT-008 ④ thêm bước tạo task (r4.3, `f091ae11`); (2) tạo tệp này đúng khuôn AGENTS A0 · MT3 · MT3-C · MT4, kèm Sổ vấp và mục Ma trận; (3) tools-quy-trinh trỏ QTTH 07 sang đây, bỏ lệnh gom `MOW-TH-007.md` cũ.
- Chưa làm (đúng cổng A0): chưa lập kế hoạch chính thức, chưa PROMPT/READY/RUN — chờ Owner gật ô 2, Mốc và Host.
