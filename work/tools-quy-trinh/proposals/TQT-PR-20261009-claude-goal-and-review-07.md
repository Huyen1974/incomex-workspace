# TQT-PR-20261009-claude-goal-and-review-07
## Mục tiêu ngắn cho ô 1–2 + rà hiện trạng "một bên sửa"

TQT-PROPOSAL: TQT-PR-20261009-claude-goal-and-review-07
TARGET: COLLAB §0 (dòng Xác nhận User · Bảng điều khiển · ô 1 · ô 2 · ô 3 TQT-DIR/TQT-REQ · Owner cần quyết); README (chỉ mục ý kiến); view.html tab "List quy trình tổng hợp".
TESTED: Claude-review đọc COLLAB/README/view.html tại commit 86f0e24; render 5 tab view.html bằng Chromium cục bộ; xem trang Owner thật (Kiểm soát + Nội dung) và trang Công thức MMIM; đối chiếu git log 08–09/10 của work/tools-quy-trinh. Dùng JEV kiểm độ phủ 24 ý chỉ đạo trên bản mục tiêu mới. Không sửa view.html/COLLAB.md/README.md.
BLOCKER_TYPE: THIEU_QUYET_DINH (ô 1–2 mới cần Owner gật) · LOI_QUY_TRINH (Bảng điều khiển sai khuôn MT4)
OBSERVED: Ô 1 từ 15 dòng (bản Owner duyệt 08/10) phình thành khoảng 105 dòng vì chép nguyên văn 7 khối chỉ đạo 08–09/10 và 7 ý Host diễn giải. Owner đọc không ra đích. Bảng điều khiển thiếu dòng theo MT4 nên trang Owner báo "⚠ Bảng điều khiển thiếu dòng ⛔".
PROPOSED_CHANGE: Thay ô 1–2 bằng bản ngắn ở mục 2 (sau khi Owner gật). Chuyển nguyên văn mọi khối cũ xuống ô 3 hoặc Vòng trước theo bảng ở mục 3, không xoá chữ nào. Sửa Bảng theo mục 5. Thêm chỉ mục ý kiến theo mục 4.2.

---

## 1. Chỉ đạo Owner · 09/10/2026 15:08 +07 · phiên Claude (nguyên văn)

> Bản của bạn làm hiên nó nằm trong: Quy trình hiện có. đang để tạm. Vì nó chưa toàn diện và nó khó hiểu (rối với tôi). Tôi chỉ muốn nhìn thấy cái gì đơn giản: Nhìn cái phải hiểu như kiêủ công thức hoặc phần: "câu hỏi cơ bản"
> Bạn có 2 nhiêm vụ.
> 1. xem lại phần hiện nay (để codex làm host) chúng ta chi có ý kiến ra 1 nơi, không ghi thẳng vào main. Host sẽ xem xét và tiếp nhận lại các thông tin. (1 bên edit để đảm bảo nhất quán)
> 2. Viết lại cho tôi phần mục tiêu. Mục tiêu trước là ban viết. Nhưng mục tiêu hiện tại là codex đang chép nguyên chỉ đạo. Có thể chuyển bớt xuống phần thế nào là hoàn thành hoặc chi tiết cần đạt. Để mục tiêu ngắn gọn, đầy đủ nhưng ngắn gọn.
> […] Những việc bổ sung là do con người nhìn ra. Để con người nhìn ra vấn đề thì tôi phải hiểu. Và đó là tại sao tôi cần cái gì đó ít chữ, nhìn cái là hiểu để có thể tư duy cùng các bạn.
> Rà soát vòng này đã nhé

Host ghi thành D17 + HUMAN_DIRECTIVE@TQT-GOAL-SHORT-20261009 khi áp.

---

## 2. Bản ô 1–2 mới · ĐỀ XUẤT, Owner chưa gật

Cách làm giống D03/D04: Claude soạn trong chat, Owner gật hoặc sửa, khi đó bản này là lời Owner. Host chép nguyên văn, giữ đúng tiêu đề khoá máy. Theo MT4, ô 1–2 dùng câu thường, không bảng.

```text
### 1. Mục tiêu
Đích: việc gì lặp lại cũng có quy trình chuẩn → người mới, phiên AI mới làm theo là ra đúng sản phẩm, hướng tới muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể.

1. Quy trình = các bước có thứ tự + đủ câu hỏi + thế nào là xong.
2. Câu hỏi = chuyên môn (Bước · Tầng · Chuỗi) + nghiệp vụ (UI · Config · Test · giao việc…) + ghi chú riêng. Một ma trận gốc, các màn khác chỉ là cách xem.
3. Ra sản phẩm = quy trình tổng hợp gọi các quy trình con: Thiết kế → Triển khai → Vận hành, chặng nào cũng có nghiệm thu.
4. Sai/thiếu → ghi sổ → sửa đúng nguồn → kiểm lại → đóng. Đạt có nhiều mức; lần sau chỉ kiểm phần chưa đạt.
5. Mọi thứ có mã. Giờ ghi tay ngoài PG cho nhanh, chuẩn rồi bê nguyên khối vào PG. Máy (PG · DOT · JEV) kiểm trước, agent sau cùng.
6. Nền = chuẩn tốt nhất ngành IT + phần riêng Incomex.
7. Trình bày kiểu Công thức: ít chữ, nửa phút thấy có gì · thiếu gì · tắc ở đâu.
8. Một Host sửa nguồn; AI khác góp ý một nơi; hội đồng hiệu chỉnh liên tục.

Phạm vi: 3 Chuỗi (CTCM · VHCM · CMSXQT) × nghiệp vụ × 3 lớp (design → execute → DOT; chạm Directus/PG bắt buộc DOT, phần khác dừng ở design/execute là đủ).
Chưa làm lúc này: quy trình Chuỗi 3 (phái cử, tuyển dụng…).

(Owner chốt <ngày giờ>. AI không sửa chữ ô này. Chi tiết và nguyên văn chỉ đạo: ô 3 TQT-DIR.)

### 2. Thế nào là hoàn thành
Một quy trình đạt = người mới hoặc phiên AI mới làm theo, không hỏi thêm, ra đúng sản phẩm thật.
Chưa đạt → sửa quy trình, thêm câu hỏi còn thiếu → chạy lại.
Ba mốc, qua mốc trước mới sang mốc sau:
– Thiết kế đạt: câu hỏi áp dụng đều có đáp án và căn cứ; mô phỏng kiểu PG không còn lỗi chặn.
– Triển khai đạt: config/PG thật; AI thao tác UI như người; kiểm kỹ thuật qua.
– Vận hành đạt: chạy thật, có log và phản hồi người dùng; bàn giao VHCM theo dõi; sai/thiếu có nơi nhận tới khi đóng.
Kín: không quãng gãy, không chồng lấn; mỗi bước rõ ai làm, nhận gì, giao gì; mọi trạng thái có mã, chỗ ghi và điều kiện đóng.
Owner nhìn nửa phút trả lời được: có gì · thiếu gì · tắc ở đâu.

(Owner chốt <ngày giờ>.)
```

Ghi chú cho Host (không đưa vào ô 1):
- Câu Đích giữ nguyên chữ Owner (D05).
- Hai dòng đầu ô 2 giữ nguyên chữ Owner (D04).
- Đã gỡ một chữ hai nghĩa. Ô 1 cũ dùng "nhóm chuyên môn" cho UI/Config, còn chỉ đạo 08/10 lại gọi Bước/Tầng/Chuỗi là "chuyên môn" và UI/Config/Test là "nghiệp vụ". Ngoài ra, "quy trình nghiệp vụ (phái cử, tuyển dụng)" lại là Chuỗi 3. Bản mới chốt: **chuyên môn = Bước · Tầng · Chuỗi; nghiệp vụ = UI · Config · Test · giao việc…; Chuỗi 3 gọi bằng tên chuỗi**. Khi áp, Host rà chữ "nhóm chuyên môn" trong TQT-REQ-01/04 và TQT-LAYERS cho cùng nghĩa.

---

## 3. Khối nào chuyển đi đâu · không xoá chữ nào

| Khối đang nằm trong ô 1–2 | Chuyển tới | Ô 1–2 mới trỏ về |
|---|---|---|
| 15 dòng bản 08/10 (D04/D05), gồm "(Owner chốt 08/10/2026…)" | `### Vòng trước` · tiêu đề "Bản mục tiêu 08/10/2026 — Owner duyệt (D04/D05); thay bằng bản ngắn 09/10 (D17). Giữ nguyên văn." | — |
| #### Bổ sung trực tiếp Owner · 09/10 · rà khả thi hướng PG | Ô 3 · TQT-DIR, nguyên văn kèm ngày | ô 1 dòng 5 · ô 2 "Thiết kế đạt" |
| #### Làm rõ mục tiêu theo yêu cầu Owner · 09/10 (7 ý Host) | Ô 3 · mục mới `TQT-GOAL-NOTES · Host diễn giải cho AI` | ô 1 dòng 1–8 |
| #### Bổ sung của Owner · 08/10 · giao Astra Codex làm Host | Ô 3 · TQT-DIR, nguyên văn | ô 1 dòng 2, 7, 8 |
| #### Bổ sung Owner · 09/10 (ghi chú riêng bước con/tầng) | Ô 3 · TQT-DIR, nguyên văn | ô 1 dòng 2 |
| #### Bổ sung Owner · 09/10 · Quy trình tổng hợp | Ô 3 · TQT-DIR, nguyên văn | ô 1 dòng 3 · ô 2 ba mốc |
| #### Bổ sung Owner · 09/10 · Khép kín quy trình | Ô 3 · TQT-DIR, nguyên văn | ô 1 dòng 4–5 · ô 2 "Kín" |
| #### Bổ sung Owner · 09/10 · Chuẩn dữ liệu ngoài PG | Ô 3 · TQT-DIR, nguyên văn | ô 1 dòng 5 |
| Ô 2 · #### Tiêu chí kiểm soát bổ sung · Host | Ô 3 · mục mới `TQT-ACCEPT · bảng kiểm chi tiết theo ô 2` | ô 2 |
| TQT-REQ "REQ-01 → dòng 2, 5…" (số dòng của bản cũ) | Host đánh lại số dòng theo bản mới | — |

Quy tắc đề xuất từ nay cho task này: **chỉ đạo mới của Owner → ô 3 TQT-DIR nguyên văn ngay lượt đó. Nếu chỉ đạo đổi đích, Host soạn tối đa một dòng cho ô 1, ghi "(đề xuất — chờ Owner gật)".** Không dán khối chỉ đạo dài vào ô 1. MT3 cho phép đúng cách này. Muốn áp cho mọi task thì phải sửa AGENTS (DROOT51) riêng; đề xuất này không đụng tới.

---

## 4. Rà hiện trạng · vòng 1

### 4.1 Một bên sửa: ✅ đang giữ đúng
- Từ khi Astra Codex làm Host (commit 131cfdf, 08/10), **chỉ `codex` sửa** view.html/COLLAB/README/PROMPT/checker. GPT Chat chỉ nộp 6 file `proposals/` (PR-01…06). Claude không ghi main.
- Host có tiếp nhận thật: ô 3 có các mục "tiếp nhận proposal04", "tiếp nhận proposal05", "vòng 2", "phiếu GPT vòng 3".

### 4.2 🟡 Thiếu "một chỗ nhìn" các ý kiến
- Ý kiến đã nằm đúng một nơi (`proposals/`). Nhưng kết luận của Host lại rải trong ô 3 và không có danh sách. PR-06 (09/10 15:07) chưa có kết luận. Muốn biết ý kiến nào đang chờ xét thì phải đọc hết.
- **Đề xuất:** Host giữ một bảng ở README, mục cửa vào. Host là người duy nhất ghi cột kết luận.

| Mã | Ai | Việc | Host kết luận | Áp ở commit |
|---|---|---|---|---|
| PR-01 | GPT Chat | 135 câu | … | … |
| … | | | | |
| PR-07 | Claude | Mục tiêu ngắn + rà | chưa xét | — |

### 4.3 🔴 Bảng điều khiển sai khuôn MT4 → trang Owner đang báo lỗi
- Thiếu giờ, P, 🏁, 📍, ✅, ■ (`— · 0 RUN active`), ⬜, ➡ và ⛔. Thay vào đó là các nhãn tự đặt (Đã có, Còn hở, Ba mốc, Quyền, Cách báo cáo). Trang Kiểm soát hiện "⚠ Bảng điều khiển thiếu dòng ⛔".
- Bản nháp đúng khuôn: mục 5.

### 4.4 🟡 Chữ cũ về Host
- Dòng `Xác nhận User:` vẫn viết "chỉ định trực tiếp GPT Chat làm Host" ngay trên dòng `Host: Astra Codex`.
- `## Owner cần quyết` vẫn là Q01 "GPT Chat làm Host (D06)".
- Danh sách Quyết định Owner chưa có dòng D cho việc Owner giao Astra Codex làm Host ngày 08/10. Việc này chỉ thấy ở dòng Xác nhận bổ sung, ở ô 1 và ở HỘI ĐỒNG.
- **Đề xuất:** thêm một D kèm HUMAN_DIRECTIVE cho lần đổi Host. Sửa dòng `Xác nhận User:` thành: `ĐÃ XÁC NHẬN — Owner chốt ô 1–2 bản ngắn ngày 09/10/2026 <giờ> (D17); Host Astra Codex do Owner chỉ định trực tiếp 08/10/2026. Bản 08/10 ở Vòng trước.`

### 4.5 🟡 Khoá kỹ thuật vẫn chưa có (TQT-ISS-006)
- "Một bên sửa" hiện chỉ dựa vào việc các AI tự giữ đúng README. Gateway chưa chặn AI khác ghi vào main. Giữ ISS-006 mở và không ghi là đã khoá.

### 4.6 🟡 Trình bày: tab Câu hỏi cơ bản đạt, tab đầu chưa
- ✅ **Câu hỏi cơ bản** đúng kiểu Công thức: mỗi khối có một dòng công thức, các miếng bấm được, ít chữ.
- 🔴 **List quy trình tổng hợp** (tab mở đầu tiên) đưa ngay khối máy lên đầu. Người đọc gặp `DRAFT-MOW-GAP-001`, `SIM-CALL-001`, "Người giữ: OpenAI-main · mô phỏng", "HỢP ĐỒNG ĐANG KIỂM · CHƯA ĐÓNG BĂNG GÓI PG", rồi 7 mục xổ tên kỹ thuật như "Mã nào thuộc định nghĩa, mã nào thuộc lần làm?" hay "Hai cột dễ nhìn, ba trường riêng". Trong khi đó **TQT-TH-001**, đúng cái Owner đặt, lại nằm cuối và đang đóng.
- 🟡 **Quy trình hiện có** (bản P10 của Claude): Owner thấy rối. Đề xuất đổi tên thành "Lưu trữ · bản 08/10", không làm thêm vào đó, không xoá. Phần còn dùng (9 Tool, sổ) khi cần thì kéo dần sang khuôn thẻ.
- Gợi ý khuôn cho tab đầu: mục 6.

---

## 5. Bảng điều khiển đúng khuôn MT4 · nháp cho Host (số liệu lấy từ Bảng hiện tại)

```text
### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-09 <HH:MM> +07 · Astra Codex · P<n>
- 🎯 Mục tiêu: <câu Đích ô 1>. Vì sao: người nhìn ra vấn đề thì mới cùng sửa được.
- 🏁 Xong khi: ô 2 — ba mốc Thiết kế → Triển khai → Vận hành đều đạt bằng một lượt làm theo thật.
- 📍 Tiến độ: [■ Thiết kế] → [□ Triển khai] → [□ Vận hành]
- ✅ Đã xong: ma trận 159 câu/53 nhóm · TQT-TH-001 bản đầu · mô hình có mã TQT-MODEL-001 v2, 83 ca mô phỏng đạt (chưa chạy PG).
- ■ Đang làm: — · 0 RUN active
- ⬜ Còn lại: chốt khai báo MOW/MOT + chỗ nối → một ca thiếu Field/MOW001 đi hết → thử quy trình UI, Config, Test → sửa đúng nguồn → kiểm lại.
- ➡ Kế tiếp: Host xét PR-06, PR-07 · 😊 Owner gật ô 1–2 bản ngắn · NEXT_TRIGGER=OWNER_GOAL_APPROVAL
- ⛔ Không làm/để sau: MOW002 · quy trình Chuỗi 3 · chạy PG thật và cấp mã Master trước khi duyệt.
```

---

## 6. Tab đầu kiểu Công thức · gợi ý cho Host

```text
TQT-TH-001 = Thiết kế ▸ Triển khai ▸ Vận hành        mốc: ⬜ chưa · 🟡 đang · 🟢 đạt · 🔴 tắc
Sai/thiếu  = Phát hiện → Xác minh → Xử lý → Đấu lại → Kiểm nơi phát hiện → Đóng
```
- Trên cùng là **một dòng công thức**, như "Tìm → { Dùng | Tạo mới | Sửa | Vô hiệu }".
- Dưới đó là **3 thẻ giai đoạn**. Mỗi thẻ gồm tên, một câu, chấm màu mốc và số quy trình con đạt/tổng.
- Tiếp theo là **danh sách quy trình dạng thẻ**: TQT-TH-001 (tổng hợp) đứng trước, "Xử lý sai/thiếu" (con) đứng sau. Bấm thẻ mới xổ ra.
- Chữ máy (mã nháp, SIM, OpenAI-main, NOT_FROZEN, gói PG) gom vào **một mục "Cho AI · chi tiết"** cuối tab. "Người giữ" thay bằng 😊/🤖 và màu.

---

## 7. Rà vòng 2 · tự kiểm đề xuất này
- **Độ phủ:** JEV kiểm 24 ý (15 dòng bản 08/10 + 9 nhóm chỉ đạo 08–09/10) trên bản mục tiêu mới. Mỗi ý đạt ≥ 0,82 sau khi bổ sung "ghi tay ngoài PG", "ai làm, nhận gì, giao gì" và "kiểu Công thức".
- **Độ ngắn:** ô 1 từ khoảng 105 dòng xuống 1 Đích + 8 dòng + Phạm vi + Chưa làm.
- **Không mất chữ:** mọi khối cũ đều có nơi đến ở mục 3. Bản 08/10 xuống Vòng trước nguyên văn.
- **Đúng luật:** giữ tiêu đề khoá máy MT3; ô 1–2 dùng câu thường; Owner gật mới thành lời Owner (như D03/D04); Claude không ghi main, chỉ ghi file này.
- **Rủi ro còn lại:** số dòng TQT-REQ phải đánh lại. Nếu Host chỉ dán ô 1 mà không chuyển các khối kia xuống ô 3 thì nguyên văn sẽ mất. Vì vậy cả hai việc phải làm trong cùng một transaction.

---

## 8. Owner duyệt
Chưa có. Khi Owner gật hoặc sửa trong phiên Claude, Claude ghi nguyên văn lời Owner vào mục này. Host áp mục 2 + 3 + 4.4 trong một transaction, rồi ghi kết luận cho PR-07.
