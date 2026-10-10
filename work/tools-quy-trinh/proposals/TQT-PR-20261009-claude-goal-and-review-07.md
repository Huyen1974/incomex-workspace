# TQT-PR-20261009-claude-goal-and-review-07
## Mục tiêu ngắn cho ô 1–2 + rà hiện trạng "một bên sửa"

> **Host đọc trước · theo chỉ đạo Owner 09/10 15:24**
> - **Host xét ngay:** mục 4 (rà hiện trạng, trong đó 4.7 là góp ý chuyên môn), mục 5 (Bảng điều khiển), mục 6 (tab đầu).
> - **Chưa áp:** mục 2–3 (ô 1–2 Mục tiêu). Owner và Claude đang rà phần này. Host chỉ áp khi mục 8 có lời Owner chốt.

TQT-PROPOSAL: TQT-PR-20261009-claude-goal-and-review-07
TARGET: COLLAB §0 (dòng Xác nhận User · Bảng điều khiển · ô 1 · ô 2 · ô 3 TQT-DIR/TQT-REQ · Owner cần quyết); README (chỉ mục ý kiến); view.html tab "List quy trình tổng hợp"; JSON `tqt-composite-processes` (lời gọi quy trình con) và `tqt-process-model` / `closure_review.tracking` (thang mức kiểm).
TESTED: Claude-review đọc COLLAB/README/view.html tại commit 86f0e24; render 5 tab view.html bằng Chromium cục bộ; xem trang Owner thật (Kiểm soát + Nội dung) và trang Công thức MMIM; đối chiếu git log 08–09/10 của work/tools-quy-trinh. Dùng JEV kiểm độ phủ 24 ý chỉ đạo trên bản mục tiêu mới. Không sửa view.html/COLLAB.md/README.md.
BLOCKER_TYPE: THIEU_QUYET_DINH (ô 1–2 mới cần Owner gật) · LOI_QUY_TRINH (Bảng điều khiển sai khuôn MT4)
OBSERVED: Ô 1 từ 15 dòng (bản Owner duyệt 08/10) phình thành khoảng 105 dòng vì chép nguyên văn 7 khối chỉ đạo 08–09/10 và 7 ý Host diễn giải. Owner đọc không ra đích. Bảng điều khiển thiếu dòng theo MT4 nên trang Owner báo "⚠ Bảng điều khiển thiếu dòng ⛔".
PROPOSED_CHANGE: Host xét ngay mục 4–6: chỉ mục ý kiến (4.2), sửa chữ cũ về Host (4.4), góp ý chuyên môn C1–C4 (4.7), Bảng đúng MT4 (5), tab đầu kiểu Công thức (6). Mục 2–3 (ô 1–2 bản ngắn và chuyển khối) chỉ áp sau khi Owner chốt ở mục 8. Khi áp thì chuyển nguyên văn mọi khối cũ xuống ô 3 hoặc Vòng trước, không xoá chữ nào.

---

## 1. Chỉ đạo Owner · 09/10/2026 15:08 +07 · phiên Claude (nguyên văn)

> Bản của bạn làm hiên nó nằm trong: Quy trình hiện có. đang để tạm. Vì nó chưa toàn diện và nó khó hiểu (rối với tôi). Tôi chỉ muốn nhìn thấy cái gì đơn giản: Nhìn cái phải hiểu như kiêủ công thức hoặc phần: "câu hỏi cơ bản"
> Bạn có 2 nhiêm vụ.
> 1. xem lại phần hiện nay (để codex làm host) chúng ta chi có ý kiến ra 1 nơi, không ghi thẳng vào main. Host sẽ xem xét và tiếp nhận lại các thông tin. (1 bên edit để đảm bảo nhất quán)
> 2. Viết lại cho tôi phần mục tiêu. Mục tiêu trước là ban viết. Nhưng mục tiêu hiện tại là codex đang chép nguyên chỉ đạo. Có thể chuyển bớt xuống phần thế nào là hoàn thành hoặc chi tiết cần đạt. Để mục tiêu ngắn gọn, đầy đủ nhưng ngắn gọn.
> […] Những việc bổ sung là do con người nhìn ra. Để con người nhìn ra vấn đề thì tôi phải hiểu. Và đó là tại sao tôi cần cái gì đó ít chữ, nhìn cái là hiểu để có thể tư duy cùng các bạn.
> Rà soát vòng này đã nhé

**Owner · 09/10/2026 15:24 +07 (nguyên văn):** “Trước tiên bạn cứ ghi các ý kiến góp ý của claude vào đẻ host codex rà soát phần chuyên môn. Sau đó tôi và bạn sẽ rà soát phần mục tiêu.”

**Owner · 09/10/2026 15:58 +07 (nguyên văn):** “Giờ quay lại phần mục tiêu. Được hiểu là từ đầu đến nôi dung: "Chưa làm lúc này: quy trình nghiệp vụ (phái cử, tuyển dụng…). Chúng thuộc Chuỗi 3 CMSXQT; để sau cho đỡ lan man." là chúng ta chốt rồi. Thực tế thì tôi có bổ sung 1 số yêu cầu, nhưng phần dưới viết dài quá. Bạn tách từ dưới nội dung vừa rồi (đã chốt) xem lại những nội dung nào có nội dung quan trọng để viết nó ngắn lại. 1. Trước tiên lọc những nội dung bổ sung ở phần dưới đó từ ngày 8 tháng 10 => viết ngắn gọn lại những yêu cầu. (cái này cần việc riêng) 2. Sau đó lấy nội dung đã chốt ở bên trên cộng với nội dung mục 1 đã được duyệt để hoàn thiện thanh toán toàn bộ mục tiêu. 3. Tôi duyệt xong rồi mới đưa đến repo”

Áp dụng: 15 dòng ô 1 bản 08/10 (từ Đích đến “Chưa làm lúc này”) **giữ nguyên, đã chốt**. Chỉ rút gọn phần bổ sung từ 08/10 trở đi, làm theo 3 bước. Bản nháp ở mục 2 bên dưới **không dùng nữa**. Bản rút gọn chỉ ghi lên repo sau khi Owner duyệt.

**Owner · 09/10/2026 22:58 +07 (nguyên văn):** “Có thêm 1 vấn đề. Nguyên tắc là tạo ra các quy trình tổng hợp là liên kết lại: Chỉ đạo là mọi tiến trình cần được "Quy trình hoá". các việc phức tạp thì tạo thêm các quy trình tổng hợp. Không có tiến trình thực hiện nào đứng lẻ (không nằm trong quy trình, không có quy trình nào không có ID, không nằm trong master list. Bô sung phần này rồi bạn sửa lại luôn mục tiêu giúp tôi nhé.”

Áp dụng: nguyên tắc này vào bản mục tiêu rút gọn đang trình Owner (chưa lên repo). Với Host, nguyên tắc này biến C1/C2 ở mục 4.7 thành bắt buộc. Hiện có ba chỗ đang trái nguyên tắc: TQT-TH-001 chưa có ID Master (`master_record_id = null`, vướng cách đăng ký MOW tổng hợp · TQT-ISS-007); 21 lời gọi quy trình con không có mã; quy trình `DRAFT-MOW-GAP-001` đứng lẻ (mã nháp, không quy trình tổng hợp nào gọi).

Host ghi thành D17 + HUMAN_DIRECTIVE@TQT-GOAL-SHORT-20261009 khi áp.

---

## 2. Bản ô 1–2 mới · NHÁP CŨ, KHÔNG DÙNG (Owner 15:58 giữ 15 dòng đã chốt) · Host không áp

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
- **Đề xuất làm ngay:** thêm một D kèm HUMAN_DIRECTIVE cho lần đổi Host. Trong dòng `Xác nhận User:`, thay "GPT Chat làm Host" bằng "Astra Codex làm Host, Owner chỉ định trực tiếp 08/10/2026". Sửa Q01 ở `## Owner cần quyết` cho khớp.
- **Chỉ thêm khi mục 8 có lời Owner:** thêm vào dòng `Xác nhận User:` cụm "Owner chốt ô 1–2 bản ngắn ngày 09/10/2026 <giờ> (D17); bản 08/10 ở Vòng trước".

### 4.5 🟡 Khoá kỹ thuật vẫn chưa có (TQT-ISS-006)
- "Một bên sửa" hiện chỉ dựa vào việc các AI tự giữ đúng README. Gateway chưa chặn AI khác ghi vào main. Giữ ISS-006 mở và không ghi là đã khoá.

### 4.6 🟡 Trình bày: tab Câu hỏi cơ bản đạt, tab đầu chưa
- ✅ **Câu hỏi cơ bản** đúng kiểu Công thức: mỗi khối có một dòng công thức, các miếng bấm được, ít chữ.
- 🔴 **List quy trình tổng hợp** (tab mở đầu tiên) đưa ngay khối máy lên đầu. Người đọc gặp `DRAFT-MOW-GAP-001`, `SIM-CALL-001`, "Người giữ: OpenAI-main · mô phỏng", "HỢP ĐỒNG ĐANG KIỂM · CHƯA ĐÓNG BĂNG GÓI PG", rồi 7 mục xổ tên kỹ thuật như "Mã nào thuộc định nghĩa, mã nào thuộc lần làm?" hay "Hai cột dễ nhìn, ba trường riêng". Trong khi đó **TQT-TH-001**, đúng cái Owner đặt, lại nằm cuối và đang đóng.
- 🟡 **Quy trình hiện có** (bản P10 của Claude): Owner thấy rối. Đề xuất đổi tên thành "Lưu trữ · bản 08/10", không làm thêm vào đó, không xoá. Phần còn dùng (9 Tool, sổ) khi cần thì kéo dần sang khuôn thẻ.
- Gợi ý khuôn cho tab đầu: mục 6.

### 4.7 Góp ý chuyên môn · quy trình tổng hợp TQT-TH-001 và mô hình (kiểm trên view.html @86f0e24)

| # | Thấy gì | Đề xuất |
|---|---|---|
| C1 🔴 | **Hai đường xử lý sai/thiếu chạy song song.** TQT-TH-001 gọi "Sổ vấn đề · Tool 008" ở bước 1.4 và 2.3. Trong khi đó mô hình TQT-MODEL-001 dựng riêng quy trình 6 ô `DRAFT-MOW-GAP-001` (Phát hiện → Xác minh → Xử lý → Đấu lại → Kiểm nơi phát hiện → Kết thúc). TQT-TH-001 không gọi GAP-001 ở bước nào, và Tool 008 cũng không nhắc tới GAP-001. Đây đúng là loại "chồng lấn" Owner yêu cầu rà. | Chốt một đường: GAP-001 là quy trình con chuẩn cho sai/thiếu. Tool 008 hoặc nhập vào GAP-001, hoặc ghi rõ là bản cũ và trỏ sang. Các bước 1.4, 2.3, 3.2 gọi GAP-001 bằng mã. |
| C2 🟡 | **Gọi quy trình con bằng link, không bằng mã.** TQT-TH-001 có 21 lời gọi, lời nào cũng chỉ có `{label, href}` và không có mã. 13 trong 21 lời gọi trỏ vào tab "Quy trình hiện có", tab Owner nói chỉ để tạm. Đổi hoặc thu tab đó là gãy cả quy trình tổng hợp. Máy cũng không rà được chỗ "gọi tới quy trình không tồn tại". Như vậy là trái nguyên tắc "không gì là không có mã". | Mỗi lời gọi thêm `code` + `version` của quy trình con (TOOL-CTCM-00x, DRAFT-MOW-GAP-001…), href sinh từ mã. Checker thêm phép kiểm: mã nào được gọi thì phải có định nghĩa còn hiệu lực. Quy trình con còn dùng thì đưa thành thẻ có mã ở tab đầu, không neo vào tab tạm. |
| C3 🟡 | **Ba thang trạng thái chưa nối với nhau.** (a) Mức kiểm 0–4: Chưa khai báo → Có đáp án → Đã đối chiếu nguồn → Đã kiểm thiết kế → Đã kiểm chạy thật, kèm hiệu lực Còn hiệu lực / Cần kiểm lại (`closure_review.tracking`, CHECK `level BETWEEN 0 AND 4`). (b) Kết quả NOT_TESTED / PASS / FAIL / BLOCKED / NA. (c) Checkpoint giai đoạn: đạt / có điều kiện / chưa. Chưa có luật "mốc nào cần mức nào". Mức 4 "chạy thật" lại dùng chung cho cả mốc Triển khai lẫn Vận hành nên không phân biệt được hai mốc. | Luật cộng dồn từ dưới lên. Mốc 1 đạt ⇔ mọi câu áp dụng ≥ mức 3, còn hiệu lực, không BLOCKED. Mốc 2 đạt ⇔ ca kỹ thuật bắt buộc đạt mức 4 trên môi trường thật. Mốc 3 đạt ⇔ thêm mức 5 "Đã vận hành ổn" (đủ log và phản hồi trong khoảng quan sát đã chốt). Khi đó máy tự tính màu mốc từ dữ liệu, người không phải tự chấm. |
| C4 🟢 | **Đã có sẵn công thức khép kín 5 ý** trong `closure_review.formula`: Có tên/mã & nguồn → Có việc con & thứ tự → Nối đầu ra → đầu vào → Ghi kết quả & sai/thiếu → Có người nhận đến khi xong. Công thức này đang nằm khuất trong mục xổ "Rà vòng trước". | Đưa lên làm dòng công thức thứ hai của tab đầu, cạnh dòng TQT-TH-001 ở mục 6. Mỗi ý thành một cột màu cho từng quy trình, nhìn là biết quy trình nào hở ở ý nào. |

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
- **Góp ý chuyên môn 4.7:** số liệu đếm bằng script trên JSON `tqt-composite-processes`: 21 lời gọi, 0 có mã. Trong đó 13 trỏ vào tab tạm; 5 trỏ vào phần bổ sung của TQT-TH-001 (đã render trong Chromium, tồn tại); 2 ra ngoài; 1 vào tab nghiệp vụ. Tìm "GAP" trong TQT-TH-001: 0 lần. Thang 0–4 lấy từ `closure_review.tracking` và CHECK của bảng `assessment`.
- **Rủi ro còn lại:** số dòng TQT-REQ phải đánh lại. Nếu Host chỉ dán ô 1 mà không chuyển các khối kia xuống ô 3 thì nguyên văn sẽ mất. Vì vậy cả hai việc phải làm trong cùng một transaction.

---

## 8. Owner duyệt mục tiêu
**ĐÓNG theo D25 (10/10/2026 07:38):** Owner tự viết ô 1 còn 3 ý và giao Claude làm Host Kiểm soát. Bản nháp mục 2–3 của file này không dùng; Claude đã áp trực tiếp §0 ở commit 9704bed (P24). Phần rà 4–6 đã được Host nội dung tiếp nhận ở P16.

Lịch sử trước D25: Chưa chốt. Owner 09/10 15:24 giao thứ tự: Host rà phần chuyên môn (mục 4–6) trước; phần mục tiêu Owner và Claude rà tiếp. Khi Owner chốt, Claude ghi nguyên văn lời Owner vào mục này. Sau đó Host áp mục 2 + 3 trong một transaction và ghi kết luận cho PR-07.
