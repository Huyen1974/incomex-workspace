# COLLAB — tools-quy-trinh
Tên việc: Tools quy trình — làm theo quy trình ra được sản phẩm

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner viết lại ô 1 ngày 10/10/2026 07:38 (D25), thay 15 ý bản 08/10 (D04/D05). Bản cũ và các khối bổ sung 08–10/10 giữ nguyên văn ở Vòng trước; nội dung đã vào ô 3. Owner giao Claude làm Host phần Kiểm soát (Bảng, ô 1–3); Astra Codex vẫn là Host nội dung (D22).
Host: Astra Codex — Host nội dung: view.html, README, catalog, tiếp nhận đề xuất nội dung (D22) · Claude — Host Kiểm soát: Bảng điều khiển, ô 1–3 của §0 (D25)
Host_ID: Astra-Codex (nội dung) · Claude-review (Kiểm soát)
Host_Surface: Codex · phiên 01a129ed-a979-7d13-af46-d3b3ec3e2abf do Owner chỉ định 11/10/2026 · Claude · phiên Claude Chat Owner giao ngày 10/10/2026
Xác nhận bổ sung: Owner giao trực tiếp dựng ma trận và UI câu hỏi, giữ nội dung cũ, tiếp nhận ý kiến qua Host. Chỉ đạo này thay phần Host/PROMPT READ-ONLY cũ trong phạm vi tools-quy-trinh.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-15 17:40 +07 · GPT Chat · P65 · OWNER ĐỔI PHẠM VI
- 🎯 Mục tiêu: ô 1 — cỗ máy biến ý tưởng thành quy trình. G1: vẽ UI, đủ Field/Hợp đồng/Config **và ghi đủ mọi đối tượng phát sinh vào Master List tương ứng**, theo dõi quan hệ/đổi nguồn.
- 🏁 Xong khi: ô 2 — có danh mục các Master cần dùng, nơi lưu trên Directus; mọi UI/Field/DOT/nợ/thay đổi phát sinh đã ghi đủ, kiểm đếm đối chiếu được; QT001 có UI thật và Config khả thi.
- 📍 Tiến độ: [■ B0 RÀ LẠI: điều chỉnh Master + MOW-TH-007] → [□ B1 điểm danh mọi loại đối tượng → Sổ của các sổ + Owner duyệt cột] → [□ B2 dựng sổ Directus + DOT] → [□ B3 hoàn thành QT001/đối soát] → [□ B4 lô tiếp] → [□ B5 nghiệm thu]. Không tự nhảy G2.
- ✅ Đã xong: Owner từng chốt Q1 tài khoản xem NHÁP, Q2 DOT lâu dài và khung bảy bước 007; đã có định nghĩa Master, Công thức, bản r2 và các ý kiến Claude/GPT/Gemini. **Đồng thuận cũ chỉ đúng phạm vi cũ.**
- ■ Đang làm: — · 0 RUN active; GPT Chat rà lại phạm vi Owner sửa. `PROMPT.md` r2, `READY@914580c4...` **KHÔNG CÒN HIỆU LỰC** do thay đổi yêu cầu, chưa tạo Collection nháp.
- ⬜ Còn lại: kiểm các Master định nghĩa vs Collection/dữ liệu thực → sửa 007 (đăng ký phát sinh + đếm thiếu + rà ảnh hưởng) → Claude phản biện 1 vòng (✅ P49 V12.8 + R53 Luật Sổ) → GPT chốt R49–R53 → Owner rà kỹ, chốt → sửa PROMPT/READY mới.
- ➡ Kế tiếp: đưa Owner bản phương pháp luận và lộ trình đã điều chỉnh, chưa phát RUN; không hỏi lại các nguyên tắc đã có bằng chứng.
- ⛔ Không làm: coi 5 bảng lõi là đủ mọi sổ; bỏ ghi Master DOT/UI/Field/nợ; nhân bản Master đã có; ghi thẳng production; tự tạo hạ tầng/UI riêng; chạy r2 hoặc G2 trước khi Owner giao.

#### Bảng P61 trước đổi hướng (giữ để tra)
- 🎯 Mục tiêu: ô 1 — cỗ máy tạo quy trình chạy được; nhìn là hiểu, làm có bằng chứng.
- 🏁 Xong khi: ô 2 — người/AI mới làm theo, không hỏi thêm, ra đúng sản phẩm thật.
- 📍 Tiến độ: [✅ G1 đã nhận] → [■ Hiệu chỉnh theo VÒNG 9] → [□ AI mới làm thật] → [□ PG sau nghiệm thu]
- ✅ Đã xong: rà VÒNG 9; ứng viên P61 kiểm tổng PASS và đã công bố; P60/P58 là lịch sử. Chưa có Anthropic duyệt P61, chưa chuẩn.
- ■ Đang làm: P61 đã công bố nguồn/UI; đang kiểm trang Owner trước khi ký.
- ⬜ Còn lại: công bố ứng viên/kiểm UI sau cờ trống, rồi ký hai hãng; FIELD-COVERAGE/AI mới; Owner 5 ô/Master; CHECK004/HVU riêng.
- ➡ Kế tiếp: NEXT_TRIGGER=P61_CONG_BO_VA_UI_DAT; ký OpenAI rồi Owner chuyển Claude.
- ⛔ Không làm: PG · QT002/MOW002 · nghiệm thu QT001 bằng TEST · ký thay Anthropic/Owner · ghi đồng thời VPSC.

**Chỉ đạo tiếp tục 11/10/2026 · D26:** Owner chuyển sang phiên mới và giao: “Bạn là Host, hãy thực hiện vai trò rà soát và cập nhật thêm các điểm hở để đảm bảo tính khả thi nhé.” Phạm vi: đi bộ QTTH 05 theo phản biện GPT Pro và rà Master DOT/script/bộ kiểm để tái sử dụng. Nguồn chuẩn tiếp tục tools-quy-trinh trên VPS; không mở task mới.

### 1. Mục tiêu
1. Xây dựng 1 cỗ máy sản xuất quy trình, mà ở đó, con người đưa ra ý tưởng => AI + cỗ máy đó biến thành quy trình chạy được, tự động tối đa.
2. Tất cả mọi thứ phải viết thành quy trình, kể cả quy trình thực hiện quy trình... không có thứ gì là không có quy trình. Cứ 2 danh mục trở lên là phải có Master List.
3. Yêu cầu phải trình bày cực kỳ đơn giản: Con người nhìn cái hiểu ngay.

(Owner viết 10/10/2026 07:38 · D25 · chỉ sửa lỗi gõ. AI không sửa chữ ô này. Mọi chi tiết ở ô 3.)

Owner cập nhật mục tiêu G1 ngày 15/10/2026 (nguyên văn): “bây giờ mục tiêu ngắn gọn lại là vẽ UI, liệt kê được các trường còn thiếu và để chốt được hợp đồng thông tin và đảm bảo là có đủ trường để config.”
**Owner đính chính trực tiếp 15/10/2026 17:40 (cập nhật phạm vi G1; chưa chốt cách triển khai mới):**
> “Tóm lại bất cứ một cái gì khi nó phát sinh ra thì chúng ta phải ghi nó vào master list tương ứng.”
> “... chúng ta phải đi đến việc là chúng ta ghi các thông tin vào các sổ phát sinh. Rồi chúng ta phải đi kiểm tra xem là vừa rồi ví dụ phát sinh năm cái, chúng ta mới ghi có ba, hay là chúng ta đã ghi đủ năm rồi, những cái mới.”
**Nghĩa hiện hành:** vẫn ưu tiên thiết kế UI/Field/Config QT001 nhưng **phải thiết lập đủ các Master List liên quan và ghi/đếm đủ mọi phát sinh**, quan hệ và thay đổi. Không định mức 5, 85 hay 100 Collection: **Master List nào cần ghi/tra/soát thật phải có đích Directus tương ứng hoặc dẫn tới bảng đã có**, xác minh cả số đã ghi và số thiếu. Năm bảng lõi có thể dùng làm nền, **không là toàn bộ hệ sổ**. Chủ trương “năm bảng là đủ” của r2 đã bị Owner bác; không sử dụng để triển khai.

**Lịch sử yêu cầu 13/10/2026 · P53 (nguyên văn; phần rà 71 bước không là điều kiện chạy G1 hiện tại):**
> Claude chưa ký. Ngoài ra thì claude có vẻ đồng thuận với bạn về rút gọn 87 bước hiện tại. Nếu bạn thấy rút gọn đã đồng thuận thì sửa luôn cả phần QTTH 006 và hồ sơ.
> 
> Những điểm nào bạn thấy claude vô lý cứ phản bác thẳng thừng. tôi khuyên kích các bạn bảo vê quan điểm nếu thấy đúng.
> 
> Bạn tiếp tục hiệu chỉnh nhé. Chúng ta cần tối ưu quy trình (còn nhiều việc) trước khi thấy ổn và làm thử 002

### 2. Thế nào là hoàn thành
Một quy trình đạt = người mới hoặc phiên AI mới làm theo, không hỏi thêm, ra đúng sản phẩm thật.
Chưa đạt → sửa quy trình, thêm câu hỏi còn thiếu → chạy lại.
Cỗ máy đạt = User chỉ cần mục tiêu → phần còn lại tự chạy ra kết quả. AI hiểu phải làm gì theo quy trình, làm đúng theo là ra kết quả, không tự sáng tạo; sáng tạo là sửa quy trình.

(Hai dòng đầu Owner duyệt 08/10/2026 · D04. Dòng cuối là lời Owner 10/10/2026 · D24/D25.)

Với G1 đang rà lại: **đủ sổ trước khi chốt hợp đồng** — mọi Master List liên quan được điểm danh, có mã và đích lưu/quan hệ xác minh (Directus NHÁP hoặc bản có sẵn); mọi phát sinh có mã bản ghi thuộc đúng sổ; đếm được tổng cần ghi = đã có/dùng lại + mới đã ghi + còn thiếu (không im lặng bỏ qua). Phát sinh 5, ghi 3 ⇒ **thiếu 2, chưa đạt**. Field cần 10 ⇒ phải rõ bao nhiêu cũ, bao nhiêu mới, bao nhiêu chưa đăng ký/ánh xạ.
B3/QT001 đạt khi **sổ đã ghi đủ + UI thật đủ + hợp đồng thông tin/Field đủ + Config khả thi + quan hệ ảnh hưởng đã kiểm** và Owner duyệt. Chưa là G2/PG production. Điều kiện cụ thể B1+B2/B3 sẽ do Host hiệu chỉnh theo R49–R52, Claude rà và Owner chốt lại trước READY mới.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

**Chỉ mục hiện hành (đọc trước nội dung dài):** `README.md` mục “Đọc nhanh” chỉ đường tới ô 1–2 và **R49–R53 (hiệu chỉnh 17:40; R53 Luật Nhà cho mọi đối tượng 18:20)**. R40/R43/R48 và PROMPT r2 là phương án cũ **chưa đủ ghi sổ**, không phát RUN. G1 dùng MOW-TH-007 (7 bước) để thiết kế; 005 là khuôn chung, 006 (71 bước) dành triển khai/việc rủi ro cao. R04a/R09 và hồ sơ P61 trở về trước là bằng chứng lịch sử trong phạm vi đã bị R40–R48 thay thế, **không tạo cửa RUN mới**. GitHub giữ nguồn thông tin, VPS giữ runtime; không tự coi READY là RUN.

**Owner 14/10/2026 — thanh điều hướng:** luôn duy trì thanh dưới 4 Mẹ (MOW/MOT/MOIT/MOUT), Master và các UI đã thiết kế tại mọi UI đang dùng. Dùng một nguồn eco-nav.js; không tự bỏ thanh khi sửa hồ sơ/Overview. Kiểm thanh nhìn thấy ở đáy và liên kết đúng trước khi bàn giao.


- Owner 13/10/2026 · P51: “Tôi cần cả 2 bên xác nhận ok.” “bạn xác nhận OK, claude xác nhận ok. Lúc đó tôi mới có ý kiến.” Codex hoàn thiện001, Claude rà độc lập; phiếuCAT025 trong hồ sơ001, không chạy002 trước khi đủ điều kiện và Owner quyết.


Cách đọc cho G1/UI (không bắt AI quét cả lịch sử): `AGENTS.md` → COLLAB gốc → Bảng + ô 1–2 tại đây → README “Đọc nhanh” → **R49–R53** (R53 Luật Nhà: hỏi 5 câu cho mọi đối tượng, đủ mới xong). R40–R48 cũ là tiền đề/đối chiếu, R30/R36/R37 tiếp tục dùng; `PROMPT.md` r2 đang **NOT_READY**, chỉ đọc lại khi được viết lại và Owner chốt. Các mục khác chỉ tra đúng chỗ cần; nguyên văn chỉ đạo Owner ở 3.4, bằng chứng ở P. Không có STARTED/RUN hiện hành.

#### 3.1 Yêu cầu theo mục tiêu
- R00 ⬜ Đích nền (Owner 08/10 · D05, vẫn hiệu lực): việc gì lặp lại cũng có quy trình chuẩn → người mới, phiên AI mới làm theo là ra đúng sản phẩm, hướng tới muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể. Mỗi quy trình ghi rõ bước nào đã có chốt chặn làm sai, bước nào mới là lời dặn (AGENTS A10-R2).

M1 · Cỗ máy: ý tưởng → quy trình chạy được, tự động tối đa
- R01 🟡 Khuôn chung cho mọi việc lớn/nhỏ: một quy trình tổng hợp chung nhất, vừa là khuôn làm, khuôn kiểm, khuôn lập kế hoạch, tự động hoá, giám sát và biết sai ở đâu. Trả lời đủ 13 câu: việc gì (mã + Master) · bắt đầu từ đâu (kiểm nối vào) · kết thúc ở đâu (kiểm nối ra) · đầu vào đủ chưa · điều kiện thực hiện · kế hoạch ghi đâu · kết quả ghi đâu · sai/thiếu ghi đâu · ai làm, báo thế nào · ai test, đạt là gì, ghi đâu · duyệt đưa vào dùng · phiếu đủ/thiếu cho AI · vòng đời trạng thái. Chỉ bắt đầu khi đủ đầu vào, đủ nơi ghi và kế hoạch đã được xác nhận. → MOW-TH-005@1.1 (D24). Không thêm TH-06: 005 đã giữ đúng vai này, và Owner D22 hạn chế khái niệm mới.
- R02 🟡 Mỗi việc có một bảng nhìn là hiểu: cần làm gì · đã làm gì · làm tiếp gì · ai làm tiếp · đến đâu · tắc ở đâu · lý do. → application_preview trên Over view (P23); mới có 1 phiếu (MOW001/G1).
- R03 🟡 AI không tự sáng tạo trong việc lặp lại. Thiếu quy trình → 002 nhận → 003 xây/sửa và công bố → mới làm tiếp. Sáng tạo = sửa quy trình.
- R04 ⬜ Đường chuẩn "ý tưởng → quy trình chạy được": Owner đưa ý tưởng → 005 khai việc → 003 dựng quy trình (design/execute) → 001 khi cần config/PG/DOT → chạy được. Chưa có ca thật nào đi hết đường này; đây là phép thử chính của M1. → Lịch: ca thử thứ 3 ở bước ② (PR-12 v2 T6, C2).
- R04a 🔴 Nơi ghi khi chạy thử = **kho thử ngoài PG** (Owner 11/10 18:02, D27): một file trong repo, mỗi Master một khối đúng cột và khoá PG dự kiến (mã bản ghi, mã đích, phiên). Ở bước ②, "Đã ghi" = có dòng trong kho thử, bộ kiểm đọc lại được; mốc 3 kiểm kho thử, không đòi PG. Chưa có kho thử thì ca không qua được mốc 3 — lý do MOW001/G1 đứng ở mốc 2 (34/34 nghĩa vụ chưa có record_ref). Không dùng bảng PG làm nơi ghi thử. → PR-12 v2 C1, việc làm đầu tiên. *(Cách ghi cũ được thay bằng R40–R44: vùng thử là bảng nháp `tqt_draft_*` trong PG, tuyệt đối không đụng bảng nghiệp vụ production; giữ câu cũ để truy lịch sử D27.)*
- R05 🟡 Quy trình tổng hợp nối các quy trình con: trước/sau, khi nào đi tiếp, khi nào quay lại; thiếu thì bổ sung. Không dừng ở thiết kế UI mà phải chạy được tới cùng. → MOW-TH-001…004.
- R06 🟡 Ba giai đoạn, mỗi giai đoạn một mốc nghiệm thu: G1 thiết kế + đánh giá khả thi (gồm dự kiến config, đủ trường/danh sách) → G2 config thật, vào PG, test kỹ thuật, AI test trên UI như người → G3 vận hành thật, log + phản hồi người dùng, hiệu chỉnh, bàn giao VHCM theo dõi. Thiết kế được duyệt ≠ đã triển khai ≠ đã dùng thật. → G1 đang thử; G2, G3 ⬜.
- R07 🟡 Quy trình tổng hợp đầu tiên MOW-TH-001 "chế tạo một chi tiết/chức năng": đặt tên trong Master → thiết kế UI → chạy thử giả định các quy trình sau. Đích: được thông qua, yên tâm chạy; hoặc ghi sai/thiếu vào sổ, giải xong là chạy.
- R08 ⬜ Tự động tối đa: máy làm trước (PG · DOT · JEV), agent sau cùng vì chậm, tốn, vẫn có thể sai. Ba lớp: design (đủ câu hỏi để thiết kế) → execute (thứ tự bước + xong khi, agent làm lặp) → DOT/script (trigger, máy tự chạy). Phần nào viết thành DOT thì DOT là trạng thái cuối; chạm Directus/PG bắt buộc DOT; phần khác dừng ở design/execute là đủ (vd thiết kế UI).
- R09 🟡 Cách đi tới PG (Owner 11/10 18:02, D27): ① thiết kế hệ thống đúng → ② chạy thử một số ca ngoài PG để hiệu chỉnh thiết kế, bổ sung cột (làm tay được; giờ ghi tay trên repo/VPS cho nhanh) → ③ chạy ổn mới rà và đưa vào PG một lần, vì mỗi lần sửa PG tốn hơn rất nhiều. ① ② thuộc G1, ③ mở G2 (R06). Thiết kế tính sẵn phiên bản, lần chạy, vòng chạy; mã cho khoá chính/phụ; mô phỏng lắp thật vào PG để bắt lỗi; chịu quy mô gấp nghìn, triệu lần. Qua bước: ①→② khi đã gộp 3 bản thiết kế dữ liệu thành 1, chốt mã thật, có kho thử (PR-12 v2 T1, T2, C1, T8) · ②→③ khi 3 ca khác loại đi hết 7 mốc, ca cuối không phải thêm cột, AI mới đi hết không hỏi, mọi nhóm ghi có bản ghi (C5) · ③ có ánh xạ cuối, kịch bản nạp DOT thử trên staging, đường lui (P1–P3). → TQT-MODEL-001 v2, 87 ca mô phỏng; đang ở ①, ca thử đầu kẹt ở ②. *(Lịch sử trước R40–R44: nguyên tắc G1 thử rồi mới duyệt G2 giữ nguyên; hình thức thử mới là Collection nháp vật lý, không phải bảng production.)*

M2 · Mọi thứ là quy trình; từ 2 trở lên có Master List
- R10 🟡 Mọi trình tự, luồng, hướng dẫn đều là quy trình, kể cả quy trình thực hiện quy trình (005) và quy trình làm/sửa quy trình (003). Không tiến trình nào đứng lẻ; quy trình nào cũng có ID và nằm trong Master List. Chỉ quản lý MOW/MOT, hạn chế khái niệm mới (D22). Tách rõ mã tài liệu · bản nháp · quy trình được phép gọi. → 5 tổng hợp + 12 thành phần đã có mã; TQT-ISS-007 (đăng ký MOW tổng hợp, quan hệ gọi con) còn mở.
- R11 🟡 Cứ 2 trở lên là có Master List, bổ sung dần (D14). → 30 Master + 18 Master thiết kế mới 11/10 (chưa có phiên bản, chưa nối với TQT-MODEL-001: PR-12 v2 T1, T3); các danh sách bên trong quy trình (13 câu khai, 11 trạng thái, loại kết quả, vai) còn nằm trong JSON, chưa là Master.
- R12 🟡 Quy trình = các bước + đủ câu hỏi + thế nào là xong. Câu hỏi = chuyên môn (Bước lớn · Bước con · Tầng · Chuỗi) + nghiệp vụ (UI · Config · Test · giao việc…). Làm việc gì thì ghép bộ câu hỏi việc đó; đủ góc độ, đúng trình tự. Danh sách nghiệp vụ mở rộng dần. "Nhóm chuyên môn" ở bản 08/10 nay gọi là nghiệp vụ. → 159 câu/53 nhóm.
- R13 🟡 Một ma trận câu hỏi gốc (SSOT, AI quét được) chạy ra từng miếng trên trang; bấm miếng nào ra câu hỏi miếng đó. Câu ngắn, làm đến đâu hiệu chỉnh đến đó, có ý kiến hội đồng.
- R14 🟡 Quy định chung để ghép + ghi chú riêng từng bước con, từng tầng. Cái gì phổ quát được thì đưa lên tầng. Thêm Bước con → thêm bộ câu hỏi riêng, vẫn kế thừa bước lớn (D15).
- R15 🟡 Khép kín sai/thiếu: chưa sửa ngay → ghi một sổ, theo vòng đời tới khi xong (phát hiện → xác minh → xử lý → đấu lại → kiểm tại nơi phát hiện → kết thúc). Gửi ≠ đã nhận; bị từ chối ≠ đạt. Đạt có nhiều mức tăng dần và có chỗ ghi; tách mức kiểm · kết quả · hiệu lực để lần sau chỉ kiểm phần chưa đạt hoặc bị ảnh hưởng. → MOW-TH-002.
- R16 🟡 Có quy trình rà: chỗ gãy · chỗ chồng lấn (2 quy trình cùng 1 việc) · tiến trình đứng lẻ · trạng thái/thông tin chưa có chỗ ghi · chưa có điều kiện đạt/kết thúc · chưa có quy trình xử lý tiếp. → đang là bộ kiểm khai báo (PR-08 → D24); chưa là một quy trình có mã.
- R17 🟡 Danh mục = 3 Chuỗi × nghiệp vụ × 3 lớp. 3 Chuỗi: CTCM Chế tạo cỗ máy · VHCM Vận hành cỗ máy · CMSXQT Cỗ máy sản xuất quy trình.
- R18 ⬜ Nền = chuẩn tốt nhất ngành IT + phần riêng Incomex. Mỗi chuẩn ghi "Nền: … · Riêng Incomex: …"; chưa tìm được nền thì ghi CHƯA TÌM và tính chưa đạt. Trong nhà: mỗi Master ghi kèm đích PG dự kiến (dùng lại bảng đang chạy như checkpoint_instances, approval_requests, lifecycle_log, dot_tools hay tạo mới) để bước ③ nạp một lần (PR-12 v2 T4); bảng PG đang chạy không dùng làm nơi ghi thử (D27).

M3 · Nhìn là hiểu
- R19 🟡 Ít chữ, kiểu Công thức, một khuôn; nửa phút biết có gì · thiếu gì · tắc ở đâu. Dùng màu (xanh ok · vàng cảnh báo · đỏ tắc · xám chưa làm) và biểu tượng (😊 người làm · 🤖 máy làm). Chi tiết máy để ở phần "cho AI". Mỗi quy trình có chú giải 4 ý (để làm gì · khi nào dùng · tránh gì · xong khi) ở một nguồn duy nhất (D21).
- R20 🟡 Trang nội dung: Over view (quan hệ quy trình tổng hợp ↔ thành phần, mã nhỏ mờ cạnh tên) → List quy trình tổng hợp → Câu hỏi cơ bản (giống Công thức) → Câu hỏi nghiệp vụ → Ma trận câu hỏi → bản cũ để đối chiếu.
- R21 🟡 Thông tin đến Owner phải đơn giản để Owner thấy vấn đề và cùng sáng tạo. Câu hỏi lên Owner luôn kèm sẵn đề xuất để gật/lắc.

Cách làm
- R22 Vai: Owner đưa mục tiêu/ý tưởng · Astra Codex là Host nội dung (D22) · Claude là Host Kiểm soát (D25) · AI khác góp ý một nơi, Host xét rồi mới nhận (D08/D17). Mỗi phần chỉ một bên sửa để nhất quán. Luật ghi trong README cho AI dễ đọc.
- R23 Hội đồng AI hiệu chỉnh liên tục. Mục tiêu đã chốt thì AI tự điều hành tới khi xong, không chờ Owner.
- R24 Chỉ đạo mới của Owner → ghi nguyên văn ở 3.4 ngay lượt đó + thêm/sửa dòng R ở 3.1. Ô 1–2 chỉ đổi theo lời Owner.

Quy mô và cách làm chung (Owner 13/10 · D28)
- R25 🟡 Hai điều phải giữ: (1) mọi AI làm chung một nơi trên GitHub để trao đổi nhanh nhất; (2) Owner nhìn UI thật từ Directus hiện có qua quyền xem được duyệt; UI cuối đơn giản, Owner quyết cấu trúc cuối; GitHub vẫn SSOT thông tin. → view cũ chỉ giữ lịch sử (PR-22 S1; R40–R44).
- R26 🔴 Quy mô: một nghìn vấn đề mới bàn một mà đã "đơ" thì không scale được. Việc thứ 1.000 không được làm chậm việc thứ 1; dữ liệu thử ngoài PG không được chậm dần khi các bảng đầy đủ. → 10–13/10: view 0,6 → 101,7 → 16,3 MB; một việc 12,9 MB và bị chép thêm 1 bản vào view (PR-22 S1–S7).
- R27 🔴 Quy định cho AI ngắn gọn, hiệu quả, AI đọc được và tuân thủ được; quy định quan trọng thì máy chặn (R00). → Hiện ~30.000 chữ phải đọc; Bảng 13 dòng thay vì 8; nhật ký lọt vào ô 3 (PR-22 S8–S9).
- R28 ⬜ Tận dụng MacBook để tính nhanh nhất; VPS vẫn là nơi các AI nói chuyện chung và Owner xem bản cuối. G1 dùng `tqt_draft_*` là bảng PG nháp được cô lập bằng DOT, không đụng bảng PG nghiệp vụ production; chốt rồi mới xin Owner đưa vào production ở G2 (R40–R44).

Cách ghi hồ sơ (Owner 12–13/10 · P34–P46)
**Phân tuyến từ 15/10:** R29–R38 là bộ yêu cầu hồ sơ sâu, **không bắt đi 71 bước/đủ phiếu khi thiết kế UI G1**. Riêng R30 (hướng dẫn ngay tại màn), R36 (Master Field) và R37 (câu hỏi chuẩn) vẫn dùng trong MOW-TH-007; đừng bỏ các nội dung có ích này. Cửa G1 hiện hành là R40–R48.
- R29 🟡 Hồ sơ ghi thực tế, ít nhất: chưa làm/chưa có/chưa đối chiếu để trống; không điền sẵn tool/kết quả; có xác nhận đã làm/không làm + lý do; bước bổ sung có mã riêng, không đổi mã chuẩn. Luật 7 mốc/11 mục/87 bước nằm ở Overview; hồ sơ quy trình 05 và 06 là cùng một trang (P42, P43, QTTH06).
- R30 🟡 Hướng dẫn ngay nơi thao tác bằng dấu "?": không cần nhớ, không cần hỏi (P44).
- R31 🟡 Thử bằng việc thật: AI mới đóng vai làm theo QTTH 06 cho việc thật; không lấy TEST thay việc thật; đo thời gian toàn việc và từng bước; làm đến đâu dọn đến đó; vẫn ngoài PG (P35, P36, P45, P46). Hồ sơ nhẹ mà không mất lịch sử; ô xong tích xanh (P38).
- R32 🟡 Mọi DOT/tool ghi đủ vào Master List và có 2 cột chữ ký cuối: OpenAI duyệt · Anthropic duyệt (P34).

Đường độc đạo (Owner 14/10/2026 10:43 · nguyên văn 3.4 · việc chi tiết + phép thử: proposals/TQT-PR-20261013-claude-cowork-87steps-P49.md › VÒNG 8 · chặn ca thử QT002 tới khi xong)
- R33 ⬜ Mục tiêu cuối: một con đường độc đạo — ai vào cũng chỉ một lối, không thể lạc, muốn làm sai cũng không được. Ba nguyên tắc: ① cần làm thế nào thì viết rõ, có thứ tự ② làm đúng thứ tự, phải xong; không xong thì quay lại sửa luật ③ làm phải để lại bằng chứng + ô tích, tìm lại dễ. → trang 1 của 006 (VÒNG 8 A1, G1).
- R34 ⬜ Mỗi việc có thẻ 3 ô Owner nhìn nhanh, máy tự tính, xanh mới là ok: ① hoàn thành cả việc (định nghĩa rõ, Owner gật trước khi làm) ② cần tạo bao nhiêu field mới, đã ghi chưa ③ GPT/Claude/Owner đã ký đủ chưa. Rõ trong cả 006 và hồ sơ. → VÒNG 8 B1–B3.
- R35 ⬜ Có Master List thì phải có mã riêng; Master tiến trình công việc có UI mà chưa có mã chính thức ("DEF 00.1" ↔ CAT-227*). → VÒNG 8 C1–C2.
- R36 ⬜ Master Field chuẩn để đưa thẳng vào PG: mã DB (tên cột) có quy tắc thống nhất · tên hiển thị ngắn, đủ nghĩa, có "?" · mã việc sinh ra field · mô tả để làm gì · vòng đời Cần tạo mới → Đã tạo → Đã nghiệm thu. → VÒNG 8 D1–D5.
- R37 ⬜ Mỗi bước trả lời một bộ câu hỏi chuẩn (làm gì · sau bước nào · đầu vào · ai · công cụ · xong khi · ghi đâu · khi nào báo cáo · lỗi đi đâu) và tích việc đã làm; máy chặn sai thứ tự. → VÒNG 8 E1–E3.
- R38 ⬜ Hồ sơ sửa chữa thiết kế từ đầu: sửa ghi vào đâu, đã sửa bao nhiêu lần, sửa gì, lúc nào, ai chịu trách nhiệm; người làm chỉ điền vào ô có sẵn. → VÒNG 8 F1.
- R39 ⬜ Cấu trúc kỹ thuật phải nhẹ để mỗi lượt nhanh (Owner 14/10 15:38): việc của ta là quy trình, logic, UI — không dựng lại một bộ công nghệ nặng. Giữ GitHub làm nơi làm chung và chưa đưa thiết kế vào PG thật; tận dụng Directus đang có làm vùng nháp hiển thị, lấy nguồn từ GitHub. → P49 VÒNG 10. *(Cách làm cụ thể đã thay bằng R40.)*

Đường NHÁP trước khi Owner đổi phạm vi 15/10 17:40 — chỉ giữ R41/R42/R44–R47 còn phù hợp, R40/R43/R48 xem mục mới R49–R52; mọi mốc READY r2 đã mất hiệu lực.
- R40 🟡 **Ba sản phẩm G1 không đổi:** (1) UI có mã/tên, dùng lại hay tạo mới; (2) thông tin cần có được ánh xạ Field/Hợp đồng; (3) Config đúng bảng đọc/ghi, kiểu, quyền. **Mỗi đối tượng phát sinh phải đăng ký đúng Master và kiểm đủ** theo R49–R52. Năm Collection lõi của bản r2 là một phần nền, **không đủ thay tất cả Master List**. Bản giải thích cũ xem P49 V12.7 và lịch sử Git.
- R41 ⬜ **GitHub là nguồn · một DOT lâu dài là người ghi · vùng nháp chỉ là cấu hình (Owner 16:21 + 21:39).** Không ai ghi tay Directus/PG, kể cả Owner và AI; mọi thay đổi bắt đầu từ tệp trên GitHub (R45); xoá vùng rồi áp lại phải ra y hệt. Người ghi duy nhất: **`dot-master-apply`** — DOT dùng lâu dài, đặt tên theo việc (áp Master từ GitHub vào một vùng), không mang chữ «nháp». **Bốn luật để xoá phần tạm mà DOT vẫn dùng được:** ① **0 dòng sửa DOT cũ** — không thêm chế độ nháp vào DOT nào đang chạy (`dot-web-incomex` đang phục vụ web công ty) · ② **không gọi DOT cũ khi chạy** — chỉ dựa Directus API chính thức + khoá máy GSM (DROOT39, lâu dài); 227 DOT cũ nhãn DEL-1I đang được VPSC xét tắt, tắt chúng không làm hỏng DOT này; mẫu an toàn của `dot-web-incomex` (từ chối ngoài vùng, sổ sở hữu, chạy thử mặc định, gắn Guard) được chép cách làm, không gọi, không sửa · ③ **vùng là dữ liệu** — `master/vung.json` khai mỗi vùng (tiền tố, nhóm, nhãn, `xoa_duoc`); vùng `nhap` = `tqt_draft_`, `xoa_duoc: true`; G2 thêm vùng `that` với `xoa_duoc: false`; ngoài cờ này **mã DOT khoá cứng**: chỉ xoá được đối tượng có trong sổ sở hữu, mang tiền tố nằm trong danh sách viết trong mã (`tqt_draft_`, `tqt_selftest_`) và nhãn vùng — sửa tệp JSON không mở được quyền xoá bảng thật; chức năng G2 để sẵn chỗ, chỉ bật bằng một thay đổi có duyệt khi Owner giao G2 · ④ **bảo vệ Điều 30/31 thuộc về DOT, không thuộc vùng nháp** — ghim Config Guard, vào sổ DOT, bài thử chạy trên vùng thử riêng tự tạo-tự xoá, Guard kiểm theo danh sách vùng; xoá nháp xong mọi thứ này vẫn xanh. B1 đọc mã live xác nhận 4 luật; thư viện chung đã được Guard bảo vệ thì được dùng. Cấm `dot-collection-create`/`dot-collection-register`/`dot-registry-*` (gắn trigger khai sinh + sổ registry đang tắt). Owner xem bằng 1 tài khoản chỉ-đọc (R46, Q1); tuyệt đối không cấp admin. Bằng chứng: P49 V11.7.
- R42 ⬜ **Giữ nguyên giá trị đã làm, bỏ phần tự dựng không cần nữa.** Không mở rộng view.html lớn, UI thử riêng hoặc CHECK005/006; giữ nguyên bằng chứng G1/P61 và phần nghiệp vụ R33–R38 (3 chỉ số Owner nhìn nhanh, 5 ô đầu vào, mã, mô tả Field, 9 câu/bước, lịch sử sửa, 71 bước/7 mốc). Chuyển các phần này sang Collection nháp + chức năng Directus; chỉ viết UI/mã bổ sung nếu chức năng có sẵn không làm được việc đã được chốt.
- R43 🟡 **Lộ trình đề xuất mới (Owner đang rà, chưa READY):** B0 chốt phương pháp Master và sửa 007 → B1 kiểm kê Master/đích Directus, mã/alias/dữ liệu/quan hệ → B2 dùng DOT dựng/ánh xạ **mọi sổ cần ghi** (không chỉ 5), nạp dữ liệu hiện có, test ghi/đọc/đối soát → B3 QT001 thực hiện UI+Field+Config+kiểm ghi đủ Master theo R51 → B4 nhân lô cùng khuôn → B5 Owner nghiệm thu. Không kéo QTTH006 71 bước vào G1; G2/PG production là quyết định riêng.
- R44 ⬜ **G2 dùng chính DOT này, đổi vùng — quyết định riêng sau G1, không tự chạy.** Owner giao G2 → thêm vùng `that` (`xoa_duoc: false`) vào `master/vung.json` → `dot-master-apply ap <SHA> --vung that` dựng bảng thật từ đúng tệp đã duyệt (không đổi tên nháp thành thật; `master/thu/` không nạp vào vùng thật; dữ liệu thật theo kế hoạch riêng), đối chiếu mã/quan hệ/số dòng/UI + rollback. Xác minh xong, Owner chọn MỘT lệnh: `dot-master-apply co-lap nhap` hoặc `dot-master-apply xoa-vung nhap` (R46); không dọn khi chưa có biên nhận; `master/thu/` chuyển kho lưu trữ, không xoá. DOT, tệp cấu trúc, bảo vệ Điều 30/31 ở lại dùng tiếp. Không chạm Flow/quyền/trigger production ngoài phạm vi.
- R45 ⬜ **Quy trình cấp tin cho DOT (Owner 16:21: DOT cứng nhắc, phải có đường cấp tin).** Một thư mục `master/` trong việc này, dùng lâu dài: `master.json` (mỗi dòng 1 Master: mã, tên, loại; bảng nghiệp vụ **không khai cột** — DOT lấy cột từ các dòng Hợp đồng nhập/tính/duyệt vào bảng đó, khai 1 nơi) · `field.json` (mỗi Field: mã, tên cột, kiểu, tên hiển thị, mô tả) · `vung.json` (các vùng, R41) · `<mã>.json` (dữ liệu tham chiếu của Master đó) · `thu/<mã>.json` (dữ liệu thử, chỉ nạp vào vùng nháp). Mỗi tệp sửa tại chỗ, không đẻ tệp theo lượt; dòng nào cũng có `ma`. **`ma` là khoá chính của bảng:** nối bảng chỉ cần ghi mã; Directus tự chặn trùng mã, chặn nối tới mã chưa có (⇒ lộ chỗ thiếu: thêm vào master tương ứng trước), hiện quan hệ hai chiều (mở Field thấy màn hình nào đang dùng ⇒ tránh tạo trùng) và có sẵn bộ lọc «thiếu» (Màn hình chưa có Field · Field chưa ai dùng · nơi ghi chưa có trong Master). Mỗi lượt 4 nhịp: ① AI sửa đúng tệp, commit ghi `ai · việc · lý do` ② `dot-master-apply ap <SHA đầy đủ> --vung nhap` ③ DOT đọc JSON đúng commit đó (không chạy mã nào từ GitHub), kiểm hết → chạy thử → ghi → đọc lại → biên nhận ĐẠT/LỖI kèm SHA và phần đã đổi ④ AI dán 1 dòng biên nhận vào mục P. DOT dừng trước khi ghi nếu: thiếu/trùng `ma` · đổi kiểu Field (thêm Field mã mới) · dòng biến mất khỏi tệp (muốn bỏ ghi `trang_thai: ngung`) · quan hệ hoặc đích ngoài vùng · commit đổi giữa lúc kiểm và lúc ghi · lệch không giải thích được. Đổi cấu trúc giữ cờ `VPS-GHI` vài phút; ghi dữ liệu nháp không cần cờ. Ví dụ xuyên suốt: P49 V11.3.
- R46 ⬜ **Khoanh vùng bằng máy + một lệnh cô lập/xoá (Owner 16:21).** `dot-master-apply kiem` (gắn Guard, kiểm mọi vùng khai trong `vung.json`) báo đỏ khi: sai tiền tố/nhóm/nhãn `[TQT_NHAP]` của vùng · quan hệ ra ngoài vùng hoặc bảng ngoài trỏ vào · có Flow/trigger/hook trên bảng nháp · quyền khác 2 thứ (danh tính máy DOT ghi; 1 quyền xem của Owner) · có quyền public · đăng ký vào sổ hệ thống. `co-lap nhap` = khoá ghi + gỡ quyền xem, giữ dữ liệu. `xoa-vung nhap` = chụp trước → xoá đúng những gì trong sổ sở hữu của vùng (bảng, cột, quan hệ, dữ liệu, nhóm, quyền/policy, tài khoản xem, khai báo Guard của vùng) → đếm còn sót = 0; nhật ký audit hệ thống giữ nguyên, báo riêng, không tính là sót. Vùng `xoa_duoc: false` ⇒ từ chối. Owner xem bằng **1 tài khoản chỉ-đọc**: chỉ đọc, admin=false, không gắn policy nào khác (Directus cộng dồn quyền), 0 public, 0 production, giao diện sáng, tiếng Việt; DOT tạo và thu hồi (Q1).
- R47 ⬜ **DOT 100% phải là «muốn làm cũng không làm được» (Owner 15/10 14:34) — đo 15/10:** 🟢 MCP PG chỉ đọc (vai chỉ-đọc, giao dịch READ ONLY) · 🟡 MCP Directus ghi được 7 bảng cũ trong danh sách viết cứng, cấm bảng hệ thống; vùng nháp không ghi được · 🟢 Directus MCP trên Mac bị từ chối 403 · 🔴 **SSH vào VPS** (Claude Code, Codex, Antigravity tự cấu hình 14/10, MCP Graph dùng root): vào được container PG — có vai `workflow_admin` là superuser đăng nhập được — hoặc lấy khoá admin Directus ⇒ làm được mọi thứ, chỉ bị chặn bằng lời dặn (DROOT39 tự ghi «chưa cưỡng chế hoàn toàn»). **Trong TQT:** `kiem` so Directus với tệp GitHub ở biên nhận gần nhất, lệch ⇒ đỏ trong vài phút. **Owner 15/10 15:00 chốt làm đơn giản trước:** ghi Directus/PG phải có khoá; DOT tự đọc khoá (GSM), agent không được cấp và không phải nhớ khoá; B1 liệt kê đường nào hiện ghi được mà không cần khoá (chỉ đọc, không sửa). Không chuẩn bị phức tạp lúc này; khoá SSH theo lệnh cố định của OpenSSH để sau, khi cần. Bằng chứng: P49 V11.8.
- R48 🟡 **MOW-TH-007 vẫn giữ khuôn 7 bước nhưng nội dung R2 chưa đạt Owner 17:40.** Trước đây chỉ kiểm UI/Field/Config, chưa bắt buộc ghi đủ UI/DOT/Field/nợ/thay đổi vào Master và rà tác động. **Dự thảo sửa ở R51** bổ sung hai nghĩa vụ này trong cùng bảy thao tác, không tạo quy trình 008 hoặc thêm vòng RUN. Bản cũ/ý kiến Claude/GPT/Gemini lưu ở P49 V12.6–V12.7.
- R49 🔴 **NGUYÊN TẮC OWNER: GHI SỔ MỌI PHÁT SINH, KHÔNG MẤT THÀNH QUẢ.** Mỗi đối tượng mới/chỉnh (UI, Field, DOT, Tool, quy trình/MOW/MOT, Master, hợp đồng, nợ/vấn đề, thay đổi, test, quyết định...) phải: (a) tìm đúng Master List có mã; (b) tra tồn tại để DÙNG LẠI hay ghi MỚI (mã/tên/loại/quan hệ/nguồn/phiên/trạng thái); (c) đọc lại bản ghi và liên kết đúng sổ; (d) đối soát **phát hiện N = đã có dùng lại A + mới đăng ký B + chưa đăng ký C**. C>0 ⇒ báo thiếu rõ mã, không được ghi đạt. Ví dụ 5 DOT phát hiện, 3 đã ghi ⇒ thiếu 2. Sổ nợ/vấn đề nhận ngay mục chưa giải quyết, không chỉ để trong chat/báo cáo. Không tạo một DOT hay một Collection mới cho mỗi *bản ghi*.
- R50 🔴 **MASTER LIST LÀ NỀN, KHÔNG PHẢI CHỈ NĂM BẢNG LÕI.** Rà nguồn đã có trước khi tạo: registry `evidence/ui-inputs/definition-master-registry-v1.js` hiện có **28 mã ML-DEF + 1 Master Quy trình tổng hợp** (bao gồm Field/ML-DEF-008, UI cha/con/017–018, Tool/023, DOT/024, Test/025, Bằng chứng/026, Quyết định/027); `evidence/field-origin-snapshot.json` có **18 nhóm thiết kế Master** gồm CAT-069 (vấn đề/nợ), CAT-016 (thay đổi), CAT-206 (hợp đồng), CAT-015 (kiểm), CAT-025 (quyết định). Các số là **bộ nguồn định nghĩa, KHÔNG chứng minh từng bảng vật lý Directus đã có**; cần đối chiếu Master of Master và cả alias/trùng mã. Với MỖI Master lập ánh xạ `mã · tên · nguồn SSOT · Collection thực tế/nháp/cần tạo · số bản ghi · quan hệ · khả năng xem/ghi · trạng thái`; dùng lại Collection có sẵn nơi được phép, tạo `tqt_draft_*` theo DOT cho Master cần lưu/soát mà chưa có, **không giới hạn cứng 5 hay 100**. Không nối FK từ nháp sang production; khi cần đối chiếu bản có sẵn dùng mã tham chiếu/đích đọc được duyệt.
- R51 🟡 **DỰ THẢO SỬA MOW-TH-007 VẪN CHỈ 7 BƯỚC, CHỜ OWNER CHỐT:** ① Từ Công thức/quy trình xác định toàn bộ đối tượng, màn, thông tin và Master cần dùng (danh sách dự kiến có mã tạm). ② Tra đúng Master; xác định CŨ/DÙNG LẠI/MỚI; **ghi tất cả phát sinh ngay vào sổ đúng mã**, thiếu sổ thì đăng ký Master + đích Directus, không lờ đi. ③ Vẽ/ghép UI, UI nào hình thành cũng cập nhật ngay Master UI và liên kết quy trình/bước/phiên. ④ Liệt kê thông tin; tra Field cũ, thêm Field mới vào Master Field, ghi Hợp đồng qua mã, không nhập lặp thuộc tính. ⑤ Rà Config (bảng đọc/ghi, quan hệ, quyền, kiểm hợp lệ); phát hiện nợ/thay đổi thì ghi Master nợ/thay đổi và danh sách nơi chịu ảnh hưởng. ⑥ Một lệnh DOT áp GitHub→Directus, mở UI/test, **đối chiếu 3 thứ**: số phát sinh ↔ số ghi đúng sổ; số Field cần ↔ tái dùng+mới đủ; các nơi bị ảnh hưởng ↔ đã rà/chưa rà. Thiếu được lưu trong NHÁP, nhưng chưa đạt nghiệm thu; lỗi an toàn bị CHẶN. ⑦ Owner xem bản ghi/UI/báo cáo đủ-thiếu, gật theo lô. Đây là **7 thao tác logic**, không là 7 RUN/đợt chữ ký.
- R52 🟡 **DÙNG QUAN HỆ DIRECTUS ĐỂ KHÔNG SỬA CHỖ NÀY BỎ CHỖ KIA.** Các danh sách đã được chuẩn hóa nối theo mã (UI↔Quy trình/Bước, UI↔Field qua Hợp đồng, DOT↔Tool/việc, nợ↔đối tượng/nguồn, thay đổi↔đối tượng/phiên). Dùng relation M2O/O2M/M2M, bộ lọc và danh sách nơi đang dùng khi thích hợp, **ưu tiên cấu hình Directus**; không tự viết hệ graph/Flow/sổ phụ. Khi Field/UI/DOT/Master đổi, DOT/bộ rà truy nơi liên quan, ghi/hiển thị `CẦN_RÀ_LẠI` và số ảnh hưởng đã/ chưa kiểm; không tự khẳng định Directus tự sửa nội dung chuyên môn của nơi dùng. Mỗi thay đổi chỉ khép khi không còn nơi ảnh hưởng bắt buộc chưa đối chiếu.
- R53 🔴 **LUẬT NHÀ — MỌI ĐỐI TƯỢNG (Owner 15/10 18:03 + 18:14; Field chỉ là một loại).** *Mọi thứ đều có nhà. Nhà = sổ = Master List = collection. Việc chỉ xong khi mọi đối tượng nó tạo, sửa hoặc dùng mới trả lời đủ 5 câu.* Đối tượng = bất cứ thứ gì đặt được mã: quy trình, bước, màn UI, Field, DOT, Tool, collection, quyền/tài khoản, bookmark, tài liệu, luật, PROMPT/RUN, test, bằng chứng, nợ/vấn đề, quyết định, thay đổi, và chính mỗi sổ. ① **Nhà của bạn ở đâu?** Loại của bạn đã có dòng trong Sổ của các sổ chưa? Chưa có nhà ⇒ ghi nhà mới vào Sổ của các sổ ở «cần làm» kèm cột đề xuất → Owner duyệt cột lần đầu → DOT dựng nhà; không ghi tạm ở chỗ khác. ② **SSOT của bạn ở đâu?** Đúng 1 dòng gốc ở nhà; mọi nơi khác (màn, nhà khác, tài liệu, báo cáo, chat) chỉ trỏ bằng mã, không chép lại; gặp bản chép ⇒ thay bằng mã. Vật nằm ngoài Directus (tệp DOT, tài liệu GitHub) thì vật ở đâu giữ ở đó, nhà giữ 1 dòng ghi danh trỏ tới vật. ③ **Đã ghi danh ở nhà chưa?** Tra mã + tên + mô tả. Chưa có, chưa làm ⇒ ghi danh «cần làm» **trước khi làm**; đã làm từ trước mà chưa ghi ⇒ ghi bù đúng trạng thái thật. ④ **Ghi đúng chưa?** đúng nhà · không trùng · đủ cột đã duyệt · nối với việc sinh ra nó và các đối tượng nó dùng. ⑤ **Trạng thái?** chốt cần làm → đã làm xong → đã test xong (tối thiểu; mọi nhà dùng chung 1 định nghĩa; vòng đời Field R36 là trường hợp riêng); sửa sau khi test ⇒ về «cần test lại». **Ví dụ:** viết DOT `dot-master-apply` ⇒ ① nhà = sổ DOT ② mã nguồn ở `/opt/incomex/dot/bin/`, tài liệu chỉ ghi mã DOT ③ ghi danh «cần làm» trước khi viết ④ không trùng tên DOT nào, nối việc TQT ⑤ bài `thu` PASS ⇒ đã test. Màn UI, nợ, quyết định, luật… hỏi y hệt. **Hỏi khi nào:** cuối mỗi bước của mọi khuôn (005/006/007) và khi đóng việc. **Áp ngược 1 lần (B1):** điểm danh mọi loại đối tượng đang có, kể cả đồ của chính hội đồng (luật R, quyết định 3.4, đề xuất P, PROMPT/RUN, nợ TQT-ISS) — loại nào cũng có dòng nhà; loại đang nằm nhiều chỗ (vd định nghĩa sổ ở `master-of-master-v1.html` · `definition-master-registry-v1.js` · `field-origin-snapshot.json`; quy trình ở `view.html` · COLLAB · `MOW-TH-006.md`) phải gom về 1 gốc, chỗ cũ ghi «lịch sử, gốc ở …»; nhà chưa dựng collection thì dòng nhà ghi «cần làm» kèm nơi đang ở — không chặn việc. **Gốc của gốc:** Sổ của các sổ là nhà của các nhà, nhà của nó là chính nó (1 dòng tự mô tả). **Dữ liệu gốc của nhà nháp:** tệp `master/<nhà>.json` trên GitHub; DOT chép 1 chiều sang collection; sửa thẳng Directus bị chặn — nên nhà chưa dựng vẫn ghi danh được ngay trong tệp. **Máy trả lời thay phần đếm được (`kiem`, đây là phép đối chiếu R51 ⑥):** vô gia cư (loại không có dòng trong Sổ của các sổ) · thiếu ghi danh (vật có, dòng không) · ghi khống (dòng «đã làm», vật không) · chép trùng (cùng thông tin ở 2 nơi không qua mã) · cần test lại (sửa sau test, kéo theo đối tượng nối tới; dùng ngày sửa tự động của Directus, không Flow). Phần máy không thấy (nợ, quyết định…) AI tự trả lời, Reviewer khác hãng kiểm khi rà KQ. **Nhà trước, vật sau:** DOT chỉ dựng từ dòng đã ghi danh, nên thứ DOT làm ra không thể thiếu nhà; đếm 2 chiều để bắt thứ làm ngoài DOT. Nhà đã có thật (vd sổ DOT do `dot-dot-catalog` sinh) thì dùng lại, không dựng bản nháp trùng. Bảng ánh xạ R50 chính là các dòng của Sổ của các sổ. **Thứ tự:** điểm danh + Sổ của các sổ + Owner duyệt cột lần đầu (B1) → dựng các nhà (B2) → QT001 (B3); có nhà rồi mới hợp đồng thông tin, nhà đã duyệt mới đưa PG. Số collection không đặt trần.
**Đạt G1 theo Owner 17:40 (dự thảo cần chốt):** (1) các Master cần thiết có đường ghi/tra/soát trên Directus và nguồn GitHub; (2) phát sinh ↔ bản ghi đầy đủ 100%, có bằng chứng đọc lại; (3) UI/Field/Hợp đồng/Config QT001 đầy đủ theo `kiem --du`; (4) nơi dùng bị ảnh hưởng đã rà; (5) Owner duyệt. Thứ tự chuẩn: **Master/Sổ → Phát sinh → Ghi đủ & nối → UI/Field/Hợp đồng/Config → Rà ảnh hưởng → Nghiệm thu**. Không phát RUN bản r2.

Phạm vi: chưa làm quy trình nghiệp vụ (phái cử, tuyển dụng…), là sản phẩm của cỗ máy thuộc Chuỗi 3, để sau. Không làm lúc này: MOW002 · T2.5 · đổi CT-005 · chạy PG thật từ bản thiết kế.

#### 3.2 Tiêu chí kiểm một quy trình (Host nội dung soạn 09/10, dùng cho ô 2)
- Khai báo đủ: mã/phiên bản, mục tiêu, đầu vào/ra, việc con có thứ tự, người làm/giữ, nguồn đọc/nơi ghi, trigger/điều kiện, báo cáo, nơi nhận/trả và điều kiện kết thúc.
- Trả lời đủ: câu hỏi áp dụng có đáp án và căn cứ; ghi chú riêng có phạm vi. Đối chiếu hai chiều yêu cầu ↔ UI/Config ↔ ca kiểm; không có chỗ thừa vô căn cứ hoặc yêu cầu bắt buộc bị bỏ sót.
- Nối kín: các nhánh thành công, thiếu, lỗi, từ chối, chưa nhận/quá hạn đều có cách xử lý và người chịu trách nhiệm. Hồ sơ sửa xong phải trả về đúng nơi phát hiện và kiểm lại; kết thúc không thực hiện phải ghi rõ mục tiêu chưa đạt.
- Kiểm được và dùng lại được: lưu mã ca/lần chạy, nguồn/phiên bản, bằng chứng, mức kiểm, kết quả, hiệu lực. Nguồn đổi thì xét lại phần ảnh hưởng; dữ liệu có mã/quan hệ để chuyển PG và quản lý vòng đời.
- Nghiệm thu đúng mức: người/AI thực hiện xác nhận làm được/một phần/chưa làm được bằng ca áp dụng. Tách nghiệm thu thiết kế, triển khai và vận hành; mục không áp dụng phải có lý do. Việc bắt buộc còn hở thì giữ mở, không nhận toàn quy trình đã thành công.

#### 3.3 Khung đang dùng (rút gọn; nguyên văn đầy đủ ở Vòng trước › Ô 3 trước D25)
- Ba lớp (TQT-LAYERS): design = thiết kế sáng tạo (vẽ UI, lên danh sách, config): đủ câu hỏi, lựa chọn, quyết định · execute = agent làm lặp: điều kiện bắt đầu, câu xác minh, thứ tự bước, nhánh khi mắc, đầu ra, nơi bàn giao, xong khi · DOT/script = máy tự chạy: mục tiêu, trigger, vào/ra, thành công/thất bại, xong khi; áp AGENTS A10-R3/R4. Không bắt buộc mọi quy trình đủ ba lớp.
- Làm theo là phải xong (TQT-QUALITY): rõ ai làm, bắt đầu từ đâu, điều kiện, sản phẩm, nơi nhận, bằng chứng · câu hỏi → đáp án → bước → sản phẩm → bằng chứng truy được về nhau · có văn bản mới chỉ là đã soạn · làm đúng mà vẫn mắc: ghi tình huống, sửa bản chuẩn, thêm ca kiểm, chạy lại, kiểm lại phần bị ảnh hưởng · chưa sửa ngay thì ghi sổ trước khi hết lượt; chỉ đóng khi kiểm đạt; tái diễn thì mở lại cùng mã.
- Sổ (TQT-REGISTER): sổ của task ở view.html#so-van-de, mã TQT-ISS-nnn; hồ sơ task khác giữ mã gốc. Vòng đời Ghi nhận → Phân loại → Giao → Đang xử lý → Chờ kiểm → Đóng, có nhánh Bị chặn · Để sau · Trùng · Mở lại. Chưa có người nhận ghi "Chưa giao". Ổn định mới chuyển PG qua DOT, giữ mã và lịch sử.
- Nguồn (TQT-SOURCES): nguồn Owner chỉ là trang Công thức MMIM. Hướng dẫn chuẩn nằm ở tools-quy-trinh; Tools cũ (ML-DEF-023) là lịch sử hướng dẫn; hồ sơ sản phẩm vẫn ở nguồn gốc. "Xét nguyên tắc giao việc" thuộc MOT, phải đối chiếu nguồn MOT thật.
- Quyền sửa (TQT-HOST-GATE): view.html (nội dung + sổ), README (cửa vào) và phần COLLAB dưới §0 do Host nội dung sửa; §0 (Bảng, ô 1–3) do Host Kiểm soát sửa. Host nội dung được cập nhật các dòng trạng thái của Bảng (📍 ✅ ■ ⬜ ➡) đúng sự thật, kèm mục P; Host Kiểm soát giữ 🎯 🏁 ⛔ và ô 1–3, rà lại Bảng mỗi lượt. AI khác chỉ tạo file riêng proposals/TQT-PR-YYYYMMDD-<ghế>-<số>.md: mã · đã thử và kết quả thật · câu/bước thiếu hoặc sai · đề xuất sửa · nguồn và bằng chứng. Host đúng phần ghi ACCEPT / REQUEST_CHANGES / REJECT ở mục P/D. Chưa có khoá kỹ thuật, TQT-ISS-006 mở.
- Hội đồng: Astra-Codex (OpenAI) Host nội dung · Claude-review (Anthropic) Host Kiểm soát + phản biện · GPT Chat (OpenAI) góp ý/phản biện · **Gemini (Google, `google-main`) ghế dự bị** (Owner 15/10 16:53): Owner tự chuyển tay khi cần, không gửi thì là ghế trống; ý kiến để tham khảo, không tính quorum, không thay chữ ký Claude/GPT, vắng không chặn; không ghi repo — Claude/GPT tiếp nhận ý kiến vào P49. **Claude + GPT là chính.** Mode=COUNCIL · Automation_Level=AUTO0. Đường gọi hội đồng chưa đo.

#### 3.4 Nguyên văn chỉ đạo Owner
- 15/10/2026 18:14 · phiên Claude (nguyên văn, giữ lỗi gõ) → R53 viết lại thành Luật Nhà cho mọi đối tượng, P49 V12.9:
  > Tôi muốn quy trình và nguyên tắc và những câu hỏi đấy không chỉ là field đâu. Phải là MỌI ĐỐI TƯỢNG. Mọi thứ đều phải có "nhà" (chính là "sổ" = masterlist = collections). Mọi đối tượng phải trả lời được câu hỏi: nhà của bạn ở đâu? SSOT của bạn ở đâu? Đã được ghi danh ở nhà chưa? Có nhà chưa để mà ghi danh? => có rồi thì kiểm tra xem ghi đúng chưa? Chưa có bất cứ cái nào thì => phải tạo mới => trước khi tạo mới thì phải ghi vào sổ sẽ làm (nếu chưa làm) field chỉ làm là 1 đối tượng hẹp. Phải ra nguyên tắc là mọi đối tượng. Trả lời từng câu hỏi đó.
  > Một việc làm xong là phải đảm bảo các câu hỏi này được trả lời xong? Đơn giản có thế thôi. Bạn rà soát lại và làm triệt để, chúng ta làm 1 lần để lần sau không phải làm lại. Tại sao lần trước thất bại là bởi vì tư duy chưa rõ ràng
- 15/10/2026 18:03 · phiên Claude (nguyên văn phần mới, giữ lỗi gõ; phần sau trùng dòng 17:40) → R53, P49 V12.8:
  > Viết sai của những lần trước là các bạn chưa hình dung hết ra vấn đề. Đúng là mục tiêu của chúng ta chỉ làm ra 3 thứ như đã nói. Nhưng quy trình là phải đi đến tận cùng. Nguyên tắc đơn giản là bạn gặp bất cứ cái gì mới? Phải kiểm tra nó đã có trong sổ chưa (sổ chính là các master list), nếu chưa thì phải ghi bổ sung vào? Bất cứ sổ nào cũng phải có 3 tình trạng: chúng ta chốt là cần làm => chúng ta đã làm xong => chúng ta đã test xong. Tối thiểu phải có ban tình trạng này để theo dõi dòng đời. Và tất cả những việc này phải đưa vào quy trình thì thông tin chi tiết nó mới in được vào sổ. Các bạn bàn xong lại chỉ tính đến chuyện là ghi có 5 cái collection => rồi mai làm xong nó lại đi ra lại từ đầu thì còn nói chuyện gì nữa.
  > Tất cả các master list => giờ chính là các collection phải ghi chép đầy đủ và phải duyệt số cột => tương lai nó sẽ là table trong PG.
  > Mặc dù đánh nháp nhưng nên tận dụng tối đa các tính năng của Directus hiện tại để kết nối, làm sao mỗi 1 thông tin chỉ có 1 nơi (nguyên tắc 1 SSOT duy nhất) để khi sửa thì chỉ sửa 1 chỗ thôi và các chỗ khác tự động cập nhật theo. Tránh mỗi lần sửa lại đi kiểm tra 10 chỗ, quên 1 cái là lại lệch thông tin....
  > Ngay kể cả danh sách SSOT, thông tin nào? Chỗ nào là gốc => cũng lại cần 1 Master list ("sổ") vì vậy câu hỏi luôn thường trực là: thông tin này SSOT ở đâu? Có sổ chưa? đã ghi vào sổ chưa? Đã ghi đúng quy định SSOT duy nhất chưa?..... và tất cả những việc này, tất cả những câu hỏi này => đều phải ghi thành quy trình chi tiết để bất cứ AI nào cũng phải triển khai y như vậy. => nếu không làm được điều này chi tiết thì mọi chuyện sẽ rơi vào hỗn loạn.
  > Chúng ta mới đang bàn nhiều về mô hình. Chúng ta chưa thực sự tính toán đến chi tiết triển khai theo quy trình, cái gì không có quy trình là cái đó sẽ hỗn loạn và sẽ phải trả giá. Giống như việc chúng ta phải trả giá cả tuần qua và bây giờ đang phải làm lại.
  > Chốt lại là có gì thì phải ghi ra, còn nó là 20 collection, hay 90 collection không quan trọng. Bạn viết 1 nguyên tắc rất đơn giản => trả lời các câu hỏi để đảm bảo những thứ vừa làm đã nằm trong "sổ"? Sổ đã được duyệt lần đầu. Và cái này nằm ở trong quy trình, trả lời đủ câu hỏi thì mới gọi là xong.
- 15/10/2026 17:40 · Owner trực tiếp GPT Chat · PHẠM VI G1 CHƯA OK: mọi phát sinh phải đăng ký Master, kiểm đếm và theo dõi quan hệ. Nội dung chính: “Tóm lại bất cứ một cái gì khi nó phát sinh ra thì chúng ta phải ghi nó vào master list tương ứng.”; “chúng ta phải đi đến việc là chúng ta ghi các thông tin vào các sổ phát sinh.”; “Phải ghi ... phát sinh năm cái ... mới ghi có ba ... đã ghi đủ năm rồi”; “cái quy trình triển khai đó chưa ok”. → cập nhật R49–R52, hủy hiệu lực READY r2; chờ rà và Owner chốt lại.
- 15/10/2026 16:53 · phiên Claude (nguyên văn, giữ lỗi gõ) → ghế dự bị Gemini (3.3 + bảng HỘI ĐỒNG), Bảng ➡:
  > Về ghế của Gemini như đề xuất thì sao? Có thể bố trí cho Gem 1 ghế không? tôi đang điều hành nên cần thì tôi gửi, không thì coi như là ghế trống chưa có người ngồi. Bạn và GPT mới là chính.
  > Chưa chạy vội, lần này tôi sẽ rà soát rất kỹ kế hoạch trước
- 15/10/2026 16:45 · phiên Claude (nguyên văn, giữ lỗi gõ) → PROMPT r2, R40/R43/R45/R48, P49 V12.7:
  > Đầu tiên bạn sửa vào đi, Ngoài ra Gem chat cũng có ý kiến dài (trước là Gem Task) tôi đang test. => Bạn tổng hợp cả ý kiến của GPT/ và Gem lại. Rà soát cho đúng. Cái đúng nhất là phải nhận ra mọi thứ nó thật sự đơn giản, vì thực tế nó đơn giản thật. Càng phức tạp nên lại càng ngớ ngẩn.
- 15/10/2026 · Owner trực tiếp GPT Chat · GẬT CẢ 3, ưu tiên UI Chuỗi Chế tạo cỗ máy → quyết định có hiệu lực Q1+Q2+R48:
  > Tôi gật cả 3 việc. Bạn chốt để làm sao giữ sự đơ giản, triển khai nhanh, trước hết là vẽ ra UI theo quy trình cho chế tạo cỗ máy. Nhắc lain là cần duy trì sự đơn giản
HUMAN_DIRECTIVE@TQT-OWNER-20261015-Q1Q2R48 EFFECTIVE · task=tools-quy-trinh · scope=G1_DIRECTUS_NHAP · step=B0/B1+B2/B3 · recorded_by=GPT Chat · quote=«Tôi gật cả 3 việc. Bạn chốt để làm sao giữ sự đơ giản, triển khai nhanh, trước hết là vẽ ra UI theo quy trình cho chế tạo cỗ máy. Nhắc lain là cần duy trì sự đơn giản» · text=Q1 tài khoản chỉ xem NHÁP APPROVED; Q2 DOT lâu dài APPROVED; MOW-TH-007 7 bước APPROVED; GPT được Owner giao chốt lệnh ưu tiên vẽ UI CHẾ TẠO CỖ MÁY · audit=Owner chỉ đạo trực tiếp trong chat 15/10/2026.
- 15/10/2026 15:47 · phiên Claude (nguyên văn, giữ lỗi gõ) → R48 chốt MOW-TH-007, P49 V12.6:
  > Tiếp tục rà soát thêm để có quy trình ngắn gọn để triển khai. Vẽ mấy cái UI, điền trường và thông tin thiếu. Việc đợn giản, rà soát để đảm bảo đơn giản nhưng vẫn khả thi nhé.
- 15/10/2026 15:00 · phiên Claude (nguyên văn, giữ lỗi gõ) → R47 (khoá đơn giản), R48 (quy trình 7 bước), P49 V12:
  > Quy trình thì các bạn bàn. làm sao để ghi vào Directus/PG cần thêm key (như vậy Dot được cấu hình đọc sẵn key, còn agent thì phải nhớ key => khó nhớ để hạn chế làm sai ban đầu cho nó đơn giản đi đã nếu quá phức tạp không chuẩn bị trở lại mất thời gian.
  >
  > Cái chính là quy trình thực hiện, 001 trước đây, Codex có thể có 1 quy trình rất cồng kềnh => cho nên em mất nhiều thời gian như vậy. Bây giờ phải rà soát lại. Để làm 3 bước đó thì bước 1,2,3 cần làm gì?
  >
  > Có làm theo 71 bước cũ không? Hay đơn giản hơn. Tất cả những sai sót đều bắt nguồn từ 1 quy trình không rõ rõ ràng. Chúng ta lần đầu làm cho nên cũng chưa biết thế nào là tối ưu => bây giờ có kinh nghiệm hơn => rà soát lại quy trình đó.
  >
  > Việc làm thử 001 thì đơn giản => nhưng việc quy trình hóa nó để làm sao không quá cồng kềnh (Ý tôi là ngắn gọn nhất có thể) mới là vấn đề. Bởi vì có hàng nghìn quy trình đằng sau. Điều quan trọng không phải là làm xong 1 quy trình => mà điều quan trọng là tìm ra quy trình để tối ưu khách làm quy trình.
  >
  > Xem lại cả từ quy trình, tôi nghĩ công thức là những thành phần cơ bản => tạm chấp nhận được rồi. Nếu cần thì chúng ta sinh ra thêm 1 vài thành phần mới, bổ sung thêm công thức. Nhưng các quy trình tổng hợp hiện nay tôi thấy cũng đã bao quát.
  >
  > Cái chính là từng bước chi tiết hiện nay chưa được quy trình hóa, mỗi ông làm 1 kiểu. Rồi mục tiêu hay bị trượt đi. Việc bé thành việc to => Hậu quả thì bạn thấy rồi đấy. Mất rất nhiều thời gian.
  >
  > Rà soát lại tổng thể xem. 6 quy trình tổng hợp. các bước thực hiện đã hợp lý chưa? Với 3 mục tiêu như tôi nói đã viết rõ rõ ràng chưa? Chuyện này các bạn phải bàn với nhau và đồng thuận. Miễn là đừng trả lời lệch câu hỏi là được.
- 15/10/2026 14:34 · phiên Claude (nguyên văn, giữ lỗi gõ) → R40, R43, R45, R47, Đạt G1, Bảng 14:55:
  > Đây là ý kiến của tôi. Tôi nghĩ vấn đề nó chỉ đơn giản như thế này: Giờ bạn cho ý kiến. Làm mãi chúng ta chỉ đi giải quyết mối 1 việc: 1. Vẽ cái UI cho đủ => 2. Liệt kê các trường cho đủ (làm hợp đồng thông tin) 3. rà config cho khả thi (đúng trường, đúng chỗ). Công thức thì có rồi => ra được danh sách. Giờ vẽ UI. Thiếu gì thì ghi vào master tương ứng. Vậy mà 1 quy trình 001, vẽ mấy cái UI mà làm vài ngày không xong. Chúng ta có 10 ngàn việc.
  >
  > Còn đây là ý kiến của GPT. vẽ lô UI của cỗ máy, hiện giờ có hơn trăm quy trình => các quy trình này cần có UI đầu tiên và lắp vào là chạy. Tất cả những thứ này Directus có thể giải quyết ngon lành, chúng ta chỉ khai báo đủ trên collection nháp là xong. Đừng phức tạp hóa vấn đề lên.
  >
  > It có thể kiểm tra luôn xem cơ chế bảo vệ để cấm Ai/Agent có thể đụng vào Directus/PG (DOT 100%) đã an toàn chưa? Nguyên tắc là muốn làm cũng không làm được => chỉ có DOT được cấp phép.
  >
  > hãy thống nhất cách tiếp cận, giữ nó ở mức đơn giản. Đừng lan man vào chi tiết rồi như chúng ta có 1 đống thử., Hiện nay làm sao để việc thêm các bản ghi trong các collection phải đơn giản, tận dụng các tính năng của Directus kết nối tự động với nhau. Điều mà khi chúng ta dựng tay chúng ta không làm được. (chủ yếu trước mắt là phục vụ soát xét, tránh trùng, phát hiện thiếu....) => còn chuẩn thì phải đưa vào PG sẽ bàn sau
- 14/10/2026 21:39 · phiên Claude (nguyên văn, giữ lỗi gõ) → R41 (4 luật), R44, Đạt G1 ⑥, Bảng 21:55:
  > Ý kiến của GPT. Có 1 vấn đề. DOT đang có sẵn làm sao để hạn chế phải sửa dot để theo mô hình tạm hiện nay và sau khi đã triển khai xong, xoá phần tạm => DOT vẫn dùng được Nên bàn kỹ về việc này, rà soát lại các mục tiêu/kế hoạch trên repo lần nữa trước khi triển khai.
- 14/10/2026 16:21 · phiên Claude (nguyên văn, giữ lỗi gõ; bỏ câu mở đầu về phiên) → R45, R46, Bảng 16:45:
  > GPT đã đưa dự thảo kế hoạch lên, tôi muốn lưu ý về cơ chế đặt thông tin của DOT cho các bản nháp collection. Bản chất thì chúng ta đã có 1 hệ thống các master list => đó chính là các collection. Công cụ thì nguyên tắc là DOT 100%, nghiêm cấm ai động vào directus và PG. Tuy nhiên cơ chế DOT ghi vào các bảng sau mỗi lượt thì cần làm. DOT không phải là ai, nó rất cứng nhắc. Làm chính xác nhưng chúng ta phải đưa ra quy trình cung cấp thông tin cho nó để ghi vào collection.
  >
  > Codex đã từng copy website chỉ trong 1 đêm, tất cả những công cụ cần thiết tôi nghĩ là gần như đủ hết. Tất cả các master of master giờ cũng thiết kế tập trung trên collection hết.
  >
  > Bạn rà soát phiên cũ và ý kiến của GPT để thống nhất trước về các chi tiết kĩ thuật. Nhắc lại là mọi thứ phải cực kỳ đơn giản. Cách tiếp cận là chúng ta tập trung vào tư duy quy trình, field, UI, còn lại các vấn đề kỹ thuật thì tận dụng hệ thống của directus đã ổn định.
  >
  > Khoanh vùng chặt chẽ vùng Nháp này. Sau khi xong, chạy 1 lệnh là cô lập hoặc xóa đi luôn đảm bảo không xung đột với các vùng khác.
- 14/10/2026 · Owner giao GPT sửa mục tiêu/kế hoạch, Claude hiệu chỉnh rồi Owner chốt (nguyên văn, bổ sung R40–R44):
  > Đây là ý kiến của Claudia. Về cơ bản như vậy là đồng thuận về giải pháp. Bây giờ còn lại tập trung là triển khai. Trong hình dung của tôi là chúng ta tạo khoảng độ hơn 100 cái collection theo đúng những cái master list mà chúng ta đã đưa ra, chốt, sau đó UI vẽ trực tiếp trên Directus rất nhanh. Và tất cả những khu vực này cần có một mã, có chữ nháp ở đầu, sau khi copy và sử dụng xong hoặc là sẽ cô lập lại hoặc xóa cái hết sạch luôn để đỡ lỗi. Việc rất ngắn gọn đơn giản, đừng tiếp cận cồng kềnh phức tạp. Tôi đã yêu cầu là phải tận dụng tối đa những gì đang có, đi từ cái đơn giản đến cái phức tạp, đừng bàn lung tung nữa nhé.
  >
  > Giờ bạn sửa luôn các mục tiêu và kế hoạch cho rõ ràng, sau đó Cloudia hiệu chỉnh lại, tôi chốt, xong là triển khai. Cách làm và khuôn khổ theo hướng tôi nói, còn chi tiết cho nó đúng hay nó sai thì các bạn hiệu chỉnh, nhưng không phức tạp. Vẫn chốt GitHub là SSOT về thông tin.
- 14/10/2026 16:00 · phiên Claude (nguyên văn, giữ lỗi gõ) → R40–R42, Bảng đổi hướng:
  > Các bạn có nhiều ý kiến quá nhưng mà toàn tập trung vào những vấn đề vụn vặt, trong khi đó tổng quan về cách tiếp cận thì lại không ai bàn. Cuối cùng chúng ta đang đi đường vòng. Vẫn là câu chuyện chúng ta có cả một cái hệ thống Directus rất tốt, nhưng để thử vài cái UI chúng ta lại đi xây dựng cả một cái bộ thử rất phiền phức. Ban đầu tôi thấy nó nhanh, tôi cũng tưởng việc này đơn giản, nhưng chưa làm mới có 1/1000 vấn đề mà đã đơ thế này thì làm làm sao được, scale làm sao được. Cho nên là bây giờ chuyển sang tập trung thảo luận cái vùng nháp trên Directus. Quy định rõ là các collection là phải là collection nháp. Sau đó thì hoặc là chúng ta sẽ sửa tên hoặc là chúng ta sẽ copy và xóa cái vùng nháp này đi. Chỉ cần xong UI, chỉ cần xong quy trình, chỉ cần khả thi trên việc đấy là xong, rồi chúng ta xóa đi sau. Nếu như bạn cũng đồng ý với GPT và tôi thì chúng ta chốt lại, sửa lại kế hoạch, sửa lại các mục tiêu, sửa lại những cái nội dung cần phải đạt được rõ ràng để làm tiếp phần tiếp theo, không đi lan man vào những chuyện vụn vặt nữa.
  >
  > thế này nhé, tôi không hiểu về DB nhiều lắm. Nhưng hình dung của tôi là có thể tạo ra các collection tạm thời rồi sau đó xóa đi. Bản chất là chúng ta tạo ra các table từ PG, sau đó chuyển sang collection của Directus. Và khi mà production thì mô hình đấy OK. Nhưng bây giờ thử nghiệm, cách đơn giản là chúng ta chỉ viết ra một số cái dot mà phần lớn dot đã có rồi. Chúng ta tạo ra các collection nháp. Tôi lấy ví dụ như danh sách các trường, chúng ta đưa thẳng vào một collection nháp bằng dot, sau đó thì rúc lên Directus. Nếu mọi chuyện ổn thì sau đó chúng ta sẽ lấy đúng cái format đó để đưa vào PG và từ PG sẽ tạo ra một collection mới trên Directus. Còn phần nháp này chúng ta sẽ xóa đi. Vậy thì cách tiếp cận chỉ là tạo ra một vùng nháp trên Directus để xử lý. Trong thời gian trước mắt, cách tiếp cận như vậy có khả thi không? Và nếu khả thi thì tôi thấy mọi việc nó đơn giản, tại sao các bạn lại làm nó phức tạp lên như thế nhỉ?
- 14/10/2026 15:38 · phiên Claude (nguyên văn, giữ lỗi gõ) → R39:
  > Giờ tôi muốn bạn giám sát tool này để bàn tiếp một số nội dung. Về cơ bản thì chúng ta đang xây các quy trình, con đường để đi. Nhưng vấn đề là quy mô triển khai chưa lớn, hiện nay là cái thao tác rất là chậm, đợi nhiều tiếng mới xong một luân lượt. Tất nhiên là ban đầu thì phải chấp nhận, nhưng tôi muốn đặt ra vấn đề về cấu trúc kỹ thuật. Liệu chúng ta đang tự xây dựng một hệ thống để thử, thế này đã phải là tối ưu chưa? Việc mà đã chốt, tức là không đưa vào PG sớm do hệ thống còn phải điều chỉnh rất nhiều, thì việc này vẫn chốt và không thay đổi. Nhưng câu hỏi là chúng ta có cả một hệ thống Directus rất lớn. Việc vẽ ra mấy UI trên hệ thống đấy xử lý rất nhanh, chỉ còn là môi trường chung, tức là SSOT làm việc trên GitHub thôi. Thế thì câu hỏi là cái cấu trúc về mặt kỹ thuật mà chúng ta đang dựng lên rất còng kềnh như thế này đã phải tối ưu chưa? Có thể tận dụng được Directus ở một vùng nháp nào đấy để dựng lên UI thật để làm nhưng mang tính nhẹ hơn được không? Tức là Directus sẽ lấy các nguồn từ GitHub và để show thẳng lên trên đó. Thế hiện nay chúng ta đi dựng lại một bộ công nghệ rất là nặng nề và thao tác rất lâu. Nghiên cứu về vấn đề này và tìm ra giải pháp để xử lý vấn đề nhanh hơn. Việc của chúng ta là quy trình, là logic, là UI chứ không phải đi tập trung vào vấn đề kỹ thuật.
- 14/10/2026 10:43 · phiên Claude (nguyên văn, giữ lỗi gõ) → R33–R38:
  > Tôi đồng ý với các ý kiến của bạn nhưng chúng ta vẫn còn những việc nữa phải làm => bạn tổng hợp lại tất cả các ý kiến rồi sau đó chúng ta sửa 1 thể nhé.
  >
  > 1. Tôi có hỏi thế nào là hoàn thành 1 việc. Bạn chưa trả lời cụ thể, có thể do codex viết ở đâu đó chưa rõ rõ ràng => chính bạn là người đọc nhiều lần còn chưa đọc được. Vậy 1 phiên mới/1 AI mới sẽ bỏ qua. Việc của chúng ta là viết cụ thể quy trình để muốn làm sai cũng không làm được. Tôi nhắc lại các mục tiêu lớn (để con người đánh giá) còn những việc chi tiết để cho AI làm đúng bên trên thì bạn nói rất đúng chúng ta phải tiếp tục sửa (đó là tại sao tôi chưa ký lệnh để làm thử 002). Các mục tiêu là:
  >    1. Thế nào là hoàn thành cho cả việc đó? Phải định nghĩa rõ ràng.
  >    2. Cần tạo bổ sung bao nhiêu field mới, đã ghi cần tạo bổ sung chưa?
  >    3. GPT và claude đã ký toàn bô chưa?
  > (Khi tôi nhìn vào 1 việc, tôi sẽ nhìn nhanh mục tiêu) và có tích xanh là ok. Cái này chưa được viết ra 1 cách rõ ràng, dễ nhìn cho cả con người và AI. Việc này phải biết rõ trong phần QTTH 006 cũng như trong hồ sơ để nhìn cái hiểu ngay.
  > 2. Master tiến trình công việc (DEF 00.1 · MASTER TIẾN TRÌNH CÔNG VIỆC https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/process-work-master-v1.html?master=DEF00.1) hiện nay bị sai nguyên tắc có UI nhưng lai không có mã của bảng này. Nguyên tắc đã có master list thì phải có mã riêng. Những việc này là hậu quả của việc trình bày chưa rõ rõ ràng lắm, cho nên người sau làm dễ bị sai. Trong khi mục tiêu là không thể hiểu nhầm và không thể làm sai thì chưa đạt được.
  > 3. https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=8 trong danh sách Master Field này cần sửa lại khá nhiều, vì những việc này là chúng ta thiết kế chuẩn để cứ thế đưa vào PG luôn. Các vấn đề của master này gồm:
  >    1. Thứ nhất là thiếu cột tên kiểu mã để đưa vào DB. Nếu dùng cột ID thì cả người và AI đọc không hiểu gì, hơn nữa ID không hiểu đang dựng theo nguyên tắc nào nhưng quá dài. Tất nhiên việc dài chưa phải là cấp bách cần sửa nhưng tên đặt trong PG thì tôi nghĩ đang là vấn đề. => cần có ý kiến thống nhất xem việc này nên giải quyết thế nào để làm chuẩn 1 lượt ngay từ đầu.
  >    2. Cột "Tên" hiện tại đặt chung chung và chưa có hướng dẫn. Nguyên tắc tôi hiểu đây là tên hiển thị. Tên hiển thị cần đầy đủ nhưng cũng ngắn gọn bởi vì đôi khi diện tích Web không cho phép. Tên hiển thị là dành cho con người đọc => nó phải mang bao hàm nội dung bên trong để ít phải hỏi lại. Chỗ này cần phải dùng cơ chế "?" để hướng dẫn ngay tại cột 1 cách rất rõ ràng, việc ban đầu đang làm là tương đối ẩu. Vì chỉ dựng khung cho nên tôi tạm chấp nhận để chạy cho qua 001. Nhưng giờ là lúc phải rà soát.
  >    3. Chúng ta thiếu mã của "DEF 00.1 · MASTER TIẾN TRÌNH CÔNG VIỆC", cho nên không kết nối được yêu cầu thêm trường đó sinh ta từ công việc nào => cần tìm lại rất khó khăn.
  >    4. Chúng ta thiếu 1 cột: mô tả về bản trường đó để làm gì. Việc này rất dễ bị bỏ quên khi làm bởi vì trong phạm vi nhỏ thì thấy không cần thiết, nhưng khi tích lũy lại theo số nhiều ngàn và trong thời gian rất dài => việc không có mô tả rõ ràng chi tiết sẽ dẫn đến dễ trùng (tức là có rồi mà vẫn tạo lại) các AI/công cụ tự động sẽ khó tìm kiếm hơn trong các trường hợp vùng xám (tức là xác suất quyết định không cao khoảng từ 50 đến 65% chẳng hạn)
  >    5. Chúng ta thiếu 3 tình trạng quan trọng của field để quản lý vòng đời sau này: cần tạo mới, đã tạo, đã nghiệm thu. Nếu không có vòng đời này PG rất khó hỗ trợ trong việc tự động quản lý vòng đời.
  >
  > Đây là 1 loại vấn đề cần phải xử lý ngay. Bạn tổng hợp với các ý kiến của bạn bên trên, đưa ra 1 danh sách yêu cầu codex xử lý tiếp và bạn tiếp tục giám sát.
  >
  > Ngoài ra, nếu bạn thấy còn vấn đề nào cần phải bổ sung ít nhất là về mặt kĩ thuật thì đưa ra ý kiến.
  > Tôi thấy rất đồng ý là chúng ta đã bổ nhỏ đến từng việc. Tức là xác suất làm nhầm (đi lạc đường) là thấp. Nhưng từng việc cần phải làm theo 1 quy chuẩn nào? Cái gì làm trước cái gì làm sau? Thế nào là hoàn thành? Thế nào thì phải báo cáo? .... Lại chưa có quy chuẩn từ những việc chi tiết. Bản chất thì là trả lời 1 bộ câu hỏi chuẩn. Và làm xong tích việc đã làm.
  >
  > Nhắc lại: bản chất là chúng ta đang thiết kế 1 con đường độc đạo, để khi bất cứ ai nào thực hiện, vào đường đó cũng chỉ có 1 lối đi. Không thể lạc đường, muốn làm sai cũng không được. Đấy là mục tiêu tổng quát cuối cùng.
  >
  > Nguyên tắc cơ bản tôi mô tả lại nếu cần bạn đưa vào luôn thiết kế của 006. Cho bất cứ thiết kế nào cũng chỉ cần đảm bảo nguyên tắc:
  >
  > 1. Cần làm thế nào thì phải viết rõ (có thứ tự).
  > 2. Thực hiện đúng theo thứ tự đã viết (và phải đảm bảo làm xong, nếu không xong quay lại sửa quy định/sửa luật)
  > 3. Làm thì phải để lại bằng chứng. Làm xong phải có checkbok, có thông tin để chứng minh là đã làm (chính là hồ sơ hiện nay). Và khi cần tìm lại để nâng cấp sửa chữa sẽ dễ dàng.
  >
  > Thêm nữa: về phần hồ sơ thực hiện (thi công) thì đang tiến dần đến bước đủ, nhưng hồ sơ sửa chữa thì gần như chưa thiết kế? Nếu sau này sửa=> Ghi vào đâu? Làm thế nào để biết là đã sửa bao nhiêu lần? Sửa cái gì? Sửa vào lúc nào? Ai chịu trách nhiệm sửa?...... tất cả những việc này hồ sơ phải trả lời và chúng ta phải thiết kế từ đầu. Ai thực hiện đơn giản là điền đủ thông tin vào các lỗ đã có sẵn.
- 13/10/2026 16:21 · phiên Claude · D28 (nguyên văn, giữ lỗi gõ): “Chúng ta lập ra tool quy trình để giải quyết bài toán của mow-mot-moit-mout
Khi mới bắt đầu chúng ta chưa tính toán tối ưu về xử lý các dữ liệu và chia sẻ nguồn lực tính toán. Giờ khi bắt đầu nở ra thì vấn đề xuất hiện. Đây là ý kiến của GPT.

Bạn cho ý kiến và chúng ta cần thống nhất đưa vào phần mục tiêu bổ sung, các việc cần làm việc bổ sung. Và những quy định làm sao phải ngắn gọn hiệu quả để chính AI có thể đọc và tuân thủ được. Hiện nay viết quá dài, tôi thấy chính codex cũng vi phạm liên tục.

Tôi nghĩ hướng chúng ta đang đi là đúng, tạm thời phải xây dựng 1 mô hình ở bên ngoài để hiệu chỉnh trước, đưa thứ gì đó vào PG lúc này (khi mà mọi chuyện vẫn thay đổi liên tục) sẽ tạo ra công việc không cần thiết và sửa nhiều lần trong PG lại có thể tạo ra những lỗi tiềm ẩn không đáng có.

Bạn có ý kiến để chúng ta thiết kế 1 cấu trúc tối ưu hơn tận dụng cả khả năng tính toán của MacBook để xử lý vấn đề.
Hai thứ cần giữ là: 

1. Tất cả ai vẫn làm việc chung 1 nơi trên Github để quá trình trao đổi thông tin là nhanh nhất.
2. User cần nhìn được view. Vì tôi là người sáng tại, quyết cầu trúc cuối cùng => tôi phải hiểu. Tôi cần nhìn thấy UI cuối cùng đơn giản.


bạn cho ý kiến nhé.” → R25–R28, PR-22, Q03.
- 13/10/2026 · Owner gửi phiên GPT, Owner chuyển kèm cho Claude (nguyên văn phần Owner viết): “Hiện nay bắt đầu có hiện tượng nặng và chậm. Đây là ý kiến của 1 phiên khác. Tôi muôn bạn xem xét, Claude cũng đang tôi ưu để VPS chạy nhanh hơn. Nhưng nếu có cấu trúc nào nhanh hơn, tận dụng được khả năng tính toán của macbook thì chúng ta nên làm.
Bạn hình duy quy mô của cỗ máy quy trình. Có 1 ngàn vấn đề, chúng ta mới bàn có 1. Vậy mà hệ thống đã "đơ" rồi => thế này thì không thể scale được.

Các cái phần quy trình rồi biểu mẫu của phần CTCM. Hiện tại tôi vẫn muốn duy trì hướng là làm xong, hiệu chỉnh. Khi cảm thấy tương đối ổn thì mới đưa vào PG. Vì vậy là cái phần cái nhu cầu thử nghiệm ở bên ngoài vẫn còn rất lớn. Cần bàn kỹ về cái phương án xử lý dữ liệu ở bên ngoài để làm sao mà không bị tiếp tục chậm xuống. Vì cái quy mô khi mà triển khai các cái bảng này đầy đủ thì quy mô cái cấu trúc nó sẽ rất phức tạp. Và nếu nó tiếp tục nặng như thế này thì sẽ rất chậm.

Bạn cho ý kiến về ý kiến. Chúng ta cần bàn với cả claude nữa để chốt mô hình tối ưu hơn để giải quyết mow-mot-moit-mout. Còn rất nhiều UI cần thiết kế, rất nhiều quy trình cần chạy, làm sao vẫn có VPS nói chuyện chung, bản cuối cùng User vẫn nhìn được trên VPS nhưng tính toán cần nhanh nhất.” → R26, R28.
- 12–13/10/2026 · phiên Codex · P34–P46 (Codex ghi; Host Kiểm soát chuyển nguyên văn từ đầu ô 3 ngày 13/10) → R29–R32:
**Owner P46 · 13/10:** thêm cột thời gian hoàn thành87bước; thực hiện thật từ đầu đến cuối001 (hoặc002), điền hồ sơ, đo toàn việc/từng việc, sửa lỗiDOT; ngoàiPG, khôngTESTthay thật. Phạm vi lượt này: làm lại MOW001G1 với bước006, giữ lịch sửG1.
**Owner P45 · 13/10:** “Bây giờ bạn thử đóng vai AI mới, làm theo QTTH 06 từng bước cho một việc thật (làm lại chính quy trình 001) để xem còn tắc ở đâu thì sửa và ghi vào Master liên quan. Vẫn ngoài PG, không lấy TEST thay việc thật, làm đến đâu dọn gọn đến đó nhé.”
**Owner P44 · 13/10:** Chuẩn là "?" — thao tác ở đâu hướng dẫn đúng ở đó, không cần nhớ, không cần hỏi. Áp dụng đồng bộ phần 11 mục hồ sơ.
**Owner P43:** hồ sơ điền ít nhất; ô chưa làm/chưa có/chưa đối chiếu để trống; hướng dẫn bằng ? tại cột và bước; bước bổ sung mã riêng, không đổi mã chuẩn.
**Owner13/10 · P42:** Overview là nơi chứa luật7mốc/11mục/87bước, thu gọn; hồ sơ ghi thực tế, không điền sẵn tool/kết quả, có xác nhận đã làm/không làm. AI làm xong dọn phần mình, trả server ngay. Claude dọn server song song; kiểm commit mới trước ghi, xung đột thì dừng và đọc lại.
**Owner 13/10/2026 · QTTH06:** “Nếu cần thừa thiếu gộp tách các bước này thì bạn có thể quyết định xử lý luôn.”; “hồ sơ của quy trình 05 và hồ sơ của quy trình 06 là cùng một trang luôn”. Phạm vi P40: rà theo thứ tự, hiệu chỉnh định nghĩa và ghép khối thu/mở vào hồ sơ; ngoài PG, không mở lại G1 hay tự duyệt production PROOT03. URL Owner: process-work-master-v1.html?master=DEF00.1&chi-tiet=TQT-VIEC-001 → /opt/incomex/docs/mcp-writes/process-work-master-v1.js; nguồn chung view.html và MOW-TH-006.md, bản chiếu qtth006-overview-v1.js.
**Owner 12/10/2026 · P38, nguyên văn:** “Bạn tiếp tục làm nhẹ hồ sơ mà không mất lịch sử,, các tich xong rồi nên dùng tich xanh để con người dễ nhận biết”. Phạm vi: định dạng lưu vật lý có khôi phục chính xác, nâng bộ đọc/cửa ghi hiện hữu; không đổi nội dung G1, lịch sử, quyết định/ACK hay PG. Nguồn UI: process-work-master-v1.html → process-work-master-v1.js; dữ liệu: tools-quy-trinh/view.html → application_preview từ MOW001. Bậc3: ghép JSON +SHA256 có sẵn trong engine, không thêm dịch vụ/kho ngoài; CHECK004 giữ pack/expand/verify dùng lại.
**Owner 12/10/2026 · P36, nguyên văn:** “Bạn tiếp tục sửa điểm tắc ở mốc 3, nối bằng chứng quyền ghi–đọc từ máy chủ rồi đi tiếp MOW001 thật đến cuối nhé. Vẫn ngoài PG, không lấy TEST thay việc thật và cập nhật các Master liên quan.”
**Owner 12/10/2026 · P35, nguyên văn:** “Bạn tiếp tục áp dụng vào MOW001 thật, đi từng bước từ đầu đến cuối xem còn tắc ở đâu thì sửa và ghi vào các Master liên quan nhé. Vẫn làm ngoài PG, không lấy kết quả TEST thay cho việc thật đã đạt.”
“Bạn xử lý tiếp nhé, ngoài ra cũng rà soát xem còn gì thực sự chưa ghi chép đầy đủ vào các master list không? giống như DOT và tool vừa rồi. Bạn đầu là có 6 với 9, còn giờ thì lôi ra nhiều trăm.”
“À, với bất cứ DOT hoặc tool nào cần có 2 cột chữ ký ở cuối nhé: 1. GPT duyệt (bạn hoặc GPT chat cần xác nhận đã duyệt - tóm lại bên Open AI duyệt) 2. Claude duyệt (hoặc chat hoăc cwork hoặc claud code cli duyệt - tóm lai bên Anthopic duyệt. Đưa các giải thích vào \"?\". Nguyên tắc của tôi là đồng thuận. 2 hãng cùng xác nhận là tôi yên tâm đồng ý. Rà soát cho 1 số vấn đề về kỹ thuật như các khâu test sau này.... cũng làm theo cơ chế đồng thuận này.”
- 11/10/2026 18:02 · phiên Claude · D27 · cách đi tới PG (nguyên văn, giữ lỗi gõ): “Không, cách tiép cận của tôi là: 1. thiết kế hệ thống đúng. 2. Chay thử 1 số để hiệu chỉnh thiết kế, bổ sung các cột cho phù hợp. (mới đầu làm tay không sao) 3. Sau khi chạy ổn, mới rà soát đưa vào PG 1 lần, vì mỗi lần sửa chữa PG mất thời gian hơn rất nhiều cho nên là phải thử nghiệm bên ngoài ổn thì mới đưa luôn 1 lần vào PG. Bạn thử rà soát xem còn vấn đề gì cần bổ sung thì tổng hợp lại 2 lần trước của lần này rồi cho tôi ý kiến. Các ý kiến của bạn vừa rồi tôi vẫn chưa chuyển cho codex” → R09, R04a, R18; bác PR-12 v1 A1.
- 11/10/2026 17:44 · phiên Claude · giao phản biện khả thi (nguyên văn theo bản ghi phiên; dấu … giữ như bản ghi): “Tiếp tục review cho tools-quy-trinh. Với tư cách là giám sát phản biện, bạn kiểm tra cho tôi tính tính khả thi của các quy trình tổng hợp, đặc biệt là QTTH 05 trong việc chuẩn bị cho triển khai… Vấn đề là hiện nay triển khai còn đang vướng gì không? các tool quản lý và viết ra như vậy có ok không? Bạn đưa ra tất cả những ý kiến để host codex xem xét và bổ sung. Không chỉ đứng dưới góc độ phản biện những gì đã làm, từ mục tiêu này còn có những gì cần thay đổi về cách tiếp cận, cần bổ sung những gì nữa…” → PR-12, P27.
- 11/10/2026 · phiên Codex · D26: nguyên văn ở đầu §0, ngay dưới Bảng.
- 10/10/2026 07:38 · phiên Claude · D25 (nguyên văn, giữ cả lỗi gõ; phần "ý kiến của gpt chat" Owner định dán kèm không có trong tin nhắn):
“Toi và codex / GPT vẫn tiếp tục sửa. Bạn thấy đã có nhiều thứ khác hơn so với lần trước. Nhưng mục tiêu ban đầu, ngắn gọn nhất là: User chỉ cần đưa ra ý tưởng, AI biến nó thành quy trình chạy được thì chưa khả thi. Tôi đang yêu cầu bổ sung thêm các thông tin dưới đây.
Bạn rà soát lại và có lẽ nên chuyển phần lớn các chi tiết xuống những điều cần đạt.
Trên mục tiêu: Chỉ cần đơn giản là:
1. Xây dựng 1 cỗ máy sản xuất quy trình, mà ở đó, con người đưa ra ý tưởng => AI + cỗ máy đó biến thành quy trình chạy được, tự động tối đa.
2. Tất cả mọi thứ phải viết thành quy trình, kể cả quy trình thực hiện quy trình... không có thứ gì là không có quy trình. Cứ 2 danh mục trở nên là phải có matser list.
3. Yêu cầu phải trình bày và cực kỳ đơn giản: Con người nhìn cái hiểu ngay.
4.
=> còn lại tất cả nên đưa vào phần chi tiết. Mục tiêu dài lê thê không ai đọc được.
Bạn được làm host phần kiểm soát/mục tiêu/ thế nào là hoàn thành/ chi tiết cần đạt.. => diễn đạt lai giúp tôi để mục tiêu ngắn gọn, và các chi tiết không thiếu nhưng có cấu trúc tốt nhé. AI đọc không xót.
---------
5. Đây là ý kiến bổ sung của GPT chat.
Tôi thì suy nghĩ đơn giản hơn thế này. Bắt đầu vào bất cứ 1 việc gì? nhỏ hay lớn => chúng ta nên có 1 quy trình tổng hợp toàn diện chung nhất. Quy trình TH này vừa là khuôn thức cho cách làm, vừa là khuôn thước cho kiểm tra, vừa là khuôn thước để lập kế hoạch, tự động hoá, giám sát, theo dõi để biết sai ở đâu. Quy trình tổng hợp cần trả lời các câu hỏi đại loại như:
   1. Việc gì?
   2. Bắt đầu từ đâu? (=> xử lý và test phần kết nối hiện hữu vào việc mới)
   3. Kết thúc ở đâu? (=> xử lý và test phần kết nối việc mới vào hệ thống hiện hữu) => danh sách công việc có viẹc 2 và 3.
   4. Điều kiện đầu vào cần những gì? (= > kiểm đủ thiếu + chuẩn bị) => kế hoạch chuẩn bị => chỉ bắt đầu khi có đủ điều kiện đầu vào => cần 1 xác nhận trước triển khai
   5. Điều kiện để thực hiện?
   6. Kế hoạch thì ghi vào đâu?
   7. Kết quả thì ghi vào đâu?
   8. Sai thiếu, yêu cầu bổ sung về điều kiện đầu vào, kết nối => ghi vào những đâu?
   9. Ai làm, làm xong báo cáo thế nào?
   10. Ai test (theo tiêu chí thế nào là đạt) => test xong ghi vào đâu?
   11. Thủ tục và tình trạng phê duyệt đưa vào sử dụng.
   12. Bạn đầu AI chạy kiểm tra, cần có 1 form để ghi thiếu đủ, cập nhật trạng thái....
   13. các trạng thái vòng đời của 1 việc (ví dụ thôi nhé):
      1. Mã việc + tên việc trong master list tương ứng (phù hợp)
      2. Điều kiện đầu vào?
      3. Danh sách khai báo đủ/thiếu (các sổ) xem còn chỗ nào chưa đủ? Vi dụ sai thiếu chưa có chỗ khai, test xong chưa có chỗ báo cáo...
      4. Đã triển khai chưa? test ok chưa? đưa vào sử dụng chưa? có cần sửa thêm không.
Nhắc lại nguyên tắc: nhìn cái phải hiểu ngay => tôi vẫn nghĩ cần 1 quy trình tổng hợp hơn nữa, Vẫn là quy trình tổng hợp, nhưng rõ ràng cái này là tổng hợp của tổng hợp có thể là TH 6.
AI chỉ cần chạy cái là hiểu ngay => có chỗ ghi lại, nhìn vào bảng đó ai cũng hiểu cần làm gì? Đã làm được gì? Cần phải làm tiếp cái gì? Tình trạng triển khai đến đâu? Tắc ở chỗ nào? Lý do là gì? ...... Mọi chuyện phải bắt đầu từ 1 quy trình như vậy, và khi có quy trình như vậy thì đảm bảo tất cả những chỗ ghi chép đều phải có, AI biết ngày làm thế nào và không tự sáng tạo => bằng cách đó thì mới xong được. Còn hiện tại chúng ta đã làm được nhiều việc tốt, nhưng tôi nghĩ chưa đủ để khả thi. Đúng theo mong muốn là User chỉ cần mục tiêu => phần còn lại, tự chạy ra kết quả.
=> Bạn căn cứ và các ý kiến của GPT chat dưới đây và ý kiến của user bên trên, xem xét sửa lại thêm 1 quy trình nào đó để đạt được những yêu cầu như tôi đưa ra bên trên, hoặc thêm quy trình TH 06 để giải quyết vấn đề này. Mục tiêu cuối cùng phải đúng nghĩa nghĩa là, AI hiểu phải làm gì theo quy trình, và làm đúng theo thì phải ra kết quả. Không cần sáng tạo gì cả. Sáng tạo là cách sửa đổi quy trình chứ không phải AI tự sáng tạo trong những công việc lặp đi gặp lại hàng ngàn lần như vậy. Chuẩn hóa từng chi tiết là cách duy nhất.
----- ý kiến của gpt chat”
- Từ 07/10 đến 10/10 trước đó: nguyên văn ở Vòng trước (ô 1 bản 08/10 và các khối bổ sung; Ô 3 trước D25 › TQT-DIR) và Quyết định Owner D01–D24.

#### 3.5 Bằng chứng và hồ sơ
- Bằng chứng từng lượt: mục "Ý kiến và bằng chứng" (P01–P48). Ý kiến AI: proposals/ (PR-01…22); kết luận Host ở README › Ý kiến hội đồng. Nhật ký kiểm cũ của ô 3: Vòng trước › Ô 3 trước D25.

### Vòng trước
#### Dọn 13/10 · Host Kiểm soát chuyển nguyên văn, không sửa chữ (P48)
Bảng 13/10 15:23 · Codex · P46 — các dòng ✅ gốc (Bảng hiện hành gộp thành 1 dòng theo khuôn 8 dòng):
- ✅ Đã làm P29: dùng lại CAT-206*, khai hợp đồng áp dụng 3 MOT/5 giao bước và ca nghiệm thu; siết ghim phiên/nội dung xuyên kiểm–duyệt–ACK, sửa lỗi thiếu dòng kiểm, thêm kiểm trước–sau vào DOT hiện hữu. P30 sửa trùng DOT còn 47 Master, giữ ⑤/7 mốc; ca thật chưa qua mốc nào.
- ✅ Đã làm P31: bịt lỗi hợp đồng/gói giao P01, thêm schema và kiểm tập bắt buộc, lịch sử toàn bằng chứng; thử ghi–đọc hai tiến trình TEST. Chưa có quyền endpoint/người kiểm độc lập thật, MOW001 0/7.
- ✅ Đã làm P32: chặn gói trả cuối/đánh giá cũ; P04 đọc nội dung thiết kế TEST; phục hồi khóa và nhật ký; ngân sách DOT theo danh mục. Cửa ghi đã bật cho tệp kho thử trên VPS; 10 ca quyền thật/gate đạt. Quyền 34 endpoint và phiên Host riêng còn mở.
- ✅ P33: kiểm kê305DOT/34Tool, nối biên nhận và bản đồ dùng lại; bộ tổng VPS đạt. P34: bổ sung bộ nhớ cùng khuôn, hai duyệt có phiên; đi thử QT001 và ghi4chỗ vướng.
- ✅ Đã xong P38: hồ sơ100MB→12.9MB, không mất lịch sử; tích xanh; bộ tổng1GiB đạt. Giữ G1 đã duyệt7/7, ngoài PG.
- ✅ P40: QTTH006 v0.3 có87bước/7mốc, đăng ký Master và ghép cùng hồ sơ; 11mục +7nhóm thu/mở đã kiểm thật; CHECK006 native PASS. Chưa thực hiện thật theo006.

Ô 3 — nhật ký lượt chạy và ghi chú Codex đặt ở đầu ô 3 (12–13/10); lời Owner kèm theo đã chuyển vào 3.4:

STARTED@TQT-P46-REAL 2026-10-13T08:23:27.929489+00:00 · executor=Codex Host · bắt đầu đo toàn lượt từ2026-10-13T08:18:56Z; lịch sửG1 giữ riêng.
KQ@TQT-P46-REAL DỪNG · 2026-10-13T08:51:21.360488+00:00 · VPS_BẬN · executor=Codex Host · UI cột thời gian đã ghi tx=d115410e8c6c41b1995003fd6632ac67; hồ sơ/checker mới chỉ local. Đã đo tìm thường/nâng cao: thiếu nguồn/evaluator; hủy→caller nhận phiên3. Fullsuite local PASS92,052s; không nghiệm thu87/87. Dọn:0/0 tiến trình nền,0/0 lease riêng,0 tệp tạm tạo trênVPS; kiểm08:47:48Z khôngcóprocessP46/index.lock/HEAD.lock. Giữ STARTED; không nhả cờ VPS-GHI củaVPSC. Tổng đo hồ sơ đến08:49:24Z:30,48phút; thời gian đóng báo cáo ghi riêng. Áp:SAME_COMMIT.

STARTED@TQT-P45-REAL 2026-10-13T08:01:26.200656+00:00 · executor=Codex Host · đi từ cửa đọc luật; không giả reviewer độc lập.

KQ@TQT-P45-REAL DỪNG · 2026-10-13T08:04:34.247398+00:00 · executor=Codex Host · CP01.01–03 đã đọc/đối chiếu; CP01.04 chưa có cửa ghi vòng mới được xác minh. Sửa F01/F02 bằng CHECK005, F03 còn mở; không PG/runtime; trả busy. Áp:SAME_COMMIT.

STARTED@TQT-P44-HELP 2026-10-13T07:43:28.205280+00:00 · executor=Codex Host · UI/hướng dẫn; không PG/runtime.

KQ@TQT-P44-HELP XONG · 2026-10-13T07:46:48.232086+00:00 · executor=Codex Host · 11 mục và 87 bước cùng cơ chế ?; CHECK005+browser đạt; không PG/runtime; trả busy, không giữ process/lease. Áp:SAME_COMMIT.

STARTED@TQT-P43-HELP 2026-10-13T07:25:34.359751+00:00 · executor=Codex Host · chỉ UI/hướng dẫn/kiểm, không runtime/PG.

KQ@TQT-P43-HELP XONG · 2026-10-13T07:34:19.591238+00:00 · executor=Codex Host · Dấu hỏi tại cột/bước; ô thực tế trống; CHECK005 và browser đạt; không PG/runtime; không giữ process/lease. Áp:SAME_COMMIT.

STARTED@TQT-P42-UI 2026-10-13T04:35:18.222361+00:00 · executor=Codex Host · chỉ nội dung và2UI modules; không runtime/Guard/PG, không giữ lease trong lúc soạn local.

KQ@TQT-P42-UI XONG · 2026-10-13T04:48:42.825024+00:00 · executor=Codex Host · Overview chuẩn7/11/87 và hồ sơ thực tế đã kiểm; CHECK005PASS,browserPASS,không PG/runtime. Đã kết thúc kiểm local và đóng caller giao dịch mất phản hồi sau khi journal xác nhận committed/pushed; không để RUN chờ. Áp:SAME_COMMIT.

STARTED@TQT-P40-QT006 2026-10-13T03:09:03.879435+00:00 · executor=Codex Host · rà QTTH006 và UI hồ sơ theo chỉ đạo trực tiếp; không runtime/Guard/baseline/PG.

KQ@TQT-P40-QT006 XONG · 2026-10-13T03:45:15.353098+00:00 · executor=Codex Host · phạm vi rà định nghĩa + bản chiếu hồ sơ đọc-only đã kiểm. Native f6870e95c8014ed3bedd5a2fcaae80ab PASS, UI thu/mở thật; G1/sourcehash không đổi. QTTH006 chưa nghiệm thu chạy thật/biến thể, chưa gateway step receipts, không PG/runtime/Guard mutation. Nhả cờ P40, không giữ process/lease chờ chỉ đạo. Áp: SAME_COMMIT. Đối soát P41: KQ được gửi trực tiếp qua gateway để sổ lifecycle nhận cùng kết quả; không phát lại RUN.

#### P38 · Hồ sơ nhẹ, giữ nguyên lịch sử

Kho vật lý dùng `TQT-HISTORY-POOL-1` trong cùng tệp, không mở kho/Master khác. Mỗi khối lặp lưu một lần theo SHA256; CHECK004 kiểm hash và giải mã trước khi đối chiếu. Nội dung G1/18 sự kiện/20lần kiểm/7mốc không đổi. Đã ghi thật và đọc lại có chữ ký; bộ tổng native PASS trong1GiB, task budget đã trả. Biên nhận tại aggregate#host_review_P38.

**Cho AI:** Tra Master DOT rồi dùng CHECK004 `--compact-history SOURCE` (dry-run); thêm `--execute --output CANDIDATE` chỉ tạo ứng viên mới. Kiểm `--check-history` và `--validate-transition BEFORE AFTER`; ghi qua upload/transaction có expected_version và cửa ghi hiện hành; đọc lại có chữ ký trước khi chốt. Khi cần bản JSON đầy đủ, dùng `--expand-history SOURCE --execute --output EXPANDED` ở vùng tạm; không nhân thành nguồn chuẩn. Sau sửa nghiệp vụ phải pack lại và vẫn tuân phiên/lịch sử cũ. Trước khi lùi runtime cũ phải expand qua cổng hiện hành, không tráo bộ đọc cũ vào dữ liệu mới. Bộ tổng kho nhẹ đã chạy trong1GiB; không tự tăng ngân sách. Dùng tác vụ bền vững cho thao tác dài; tệp vận chuyển nằm trong thư mục con riêng, không lẫn thư mục nhật ký phục hồi. Ghép đủ các trang JSON rồi mới giải mã một lần.

**Cho người dùng:** ô xong có tích xanh, ô chưa xong màu xám; tự tổng hợp từ bằng chứng, không tích tay. Lịch sử vẫn là các sự kiện cũ trong Master lịch sử.

STARTED@MOW001-P36-REAL 2026-10-12T07:34:36.793236+00:00 · executor=Codex Host · phạm vi kho tệp MOW001/G1; không PG. Dùng lại CHECK004/005/006 và bộ prepare/activate/probe đã đăng ký. Reviewer kỹ thuật đọc mã/bằng chứng, không ký hộ Anthropic; quyết định/ACK Owner cuối vẫn cần nguồn thật.

KQ@MOW001-P36-REAL DỪNG · 2026-10-13T02:50:54.519143+00:00 · executor=Codex Host · kết thúc thực thi/nhả busy; G1 P37/P38 đã được Owner duyệt/nhận 7/7, không mở lại. DỪNG vì independent production code/image review và bảo vệ PROOT03 còn thiếu, không ghi XONG toàn RUN giả. Kiểm runtime 2026-10-13T02:43–02:47Z: 0 jobs queued/running, 0 container workspace-job, 0 process TQT prepare/activate/probe/CHECK; khóa chỉ có supervisor thường trực, không có khóa thực thi TQT. Không có process RUN để cancel; không gỡ khóa dịch vụ. Chi tiết/bằng chứng và NEXT_TRIGGER: P39. Áp: SAME_COMMIT.

**Trạng thái P37 hiện hành:** Owner đã duyệt và xác nhận nhận G1 trực tiếp. Quyết định/P05/ACK lưu commit b9917118 và đọc ký task456ea8c9; chốt7/7,31/31nghĩa vụ phát sinh tại commit8ac40578, task0a72d0f4. Mục lục bằng chứng: aggregateP37. P37 bộ tổng native đã PASS job 43e4948f9c5c4c27b7b868b47483bcd3; nguồn/UI/hồ sơ đã đối chiếu. Không mở MOW002/PG. Các đoạn P36/P35 dưới đây là lịch sử.

#### Chỉ đạo bổ sung Owner 12/10/2026 · P34 — phần ghi chú Codex:
Chi tiết thực hiện theo yêu cầu cùng lượt: bộ nhớ tiến trình/phiên/nâng cấp dùng chung hai Master; đi thử TQT-QT-001 theo khung hiện có và ghi chỗ tắc; chưa làm nhật ký vài trăm bước. Phạm vi đã giao trực tiếp, không mở Master/DOT mới.

Các khối dưới đây là bản trước D25 (10/10/2026), giữ nguyên văn để đối chiếu. Hiện hành chỉ là đầu §0, Bảng và ô 1–3 phía trên.

#### Đầu §0 và Bảng điều khiển trước D25 (nguyên văn)
Xác nhận cũ: ĐÃ XÁC NHẬN — Owner chốt mục tiêu ô 1–2 ngày 08/10/2026 07:16 (D04/D05); D06 trước đây giao GPT Chat; sau đó Owner trực tiếp giao Astra Codex làm Host ngày 08/10/2026 (D17, thay phân công cũ). Giữ nguyên lời Owner trong ô 1–2; ngày 09/10/2026 Owner yêu cầu Host bổ sung làm rõ mục tiêu và rà lại Kiểm soát, không viết lại mục tiêu gốc. Quyết định Owner mới ngày 09/10/2026 giao GPT Chat làm Host lại để tổ chức tab Over view (D19), đã thay D17 trong vòng Overview; nay D22 giao lại Astra Codex, mục tiêu ô 1–2 giữ nguyên.
Host cũ: Astra Codex — Owner giao lại trực tiếp ngày 09/10/2026 (D22)
Host_ID cũ: Astra-Codex
Host_Surface cũ: Codex · cuộc trò chuyện hiện tại của Owner
Xác nhận bổ sung (vẫn hiệu lực, đã chép lên đầu §0): Owner giao trực tiếp dựng ma trận và UI câu hỏi, giữ nội dung cũ, tiếp nhận ý kiến qua Host. Chỉ đạo này thay phần Host/PROMPT READ-ONLY cũ trong phạm vi tools-quy-trinh.

#### BẢNG ĐIỀU KHIỂN CŨ · cập nhật 2026-10-10 · Astra Codex · P23
- 🎯 Mục tiêu: việc gì lặp lại cũng có quy trình chuẩn → người mới, phiên AI mới làm theo là ra đúng sản phẩm, hướng tới muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể. Vì sao: người nhìn rõ mới cùng phát hiện và sửa được vấn đề.
- 🏁 Xong khi: đạt tiêu chí ô 2; quy trình được làm theo ra đúng sản phẩm, có bằng chứng và đường xử lý sai/thiếu tới cuối.
- 📍 Tiến độ: [■ Thiết kế và khả thi] → [□ Triển khai] → [□ Vận hành]
- ✅ Đã xong (thiết kế): 29 Master theo định nghĩa + 1 Master Config = **30 danh sách**; `ML-MOW-TH-001` STT 29 có **5 quy trình thiết kế; ⑤ đã chốt áp thử**; 12 Quy trình thành phần, 17 chú giải chung nguồn, 159 câu/53 nhóm, 87 ca mô phỏng đã qua. Bằng chứng P16–P20; **chưa nghiệm thu vận hành**.
- ✅ P33: kiểm kê305DOT/34Tool, nối biên nhận và bản đồ dùng lại; bộ tổng VPS đạt. P34: bổ sung bộ nhớ cùng khuôn, hai duyệt có phiên; đi thử QT001 và ghi4chỗ vướng.
- ■ Đang làm: — · 0 RUN active
- ⬜ Còn lại: áp thử thiết kế MOW001, kiểm UI/Config/Test và hiệu chỉnh khi vướng. Riêng triển khai: 5 chốt thực thi → một vòng sai/thiếu → PG staging đúng quyền. TQT-ISS-007 giữ mở; không chặn thử thiết kế thủ công.
- ➡ Kế tiếp: Claude rà delta P51 và tự ghi phiếu CAT025; NEXT_TRIGGER=CLAUDE_P51_REVIEW_RECORDED. Codex đối chiếu; cả hai OK mới trình Owner. Không giữ RUN/lease chờ.
- ⛔ Không làm/để sau: MOW002 · T2.5 · đổi CT-005 · chạy PG thật từ bản thiết kế · tự áp mục tiêu PR-07 chưa duyệt.

#### Ô 1 bản 08/10/2026 (D04/D05) và các khối bổ sung 08–10/10 — thay bằng ô 1 ngày 10/10/2026 (D25); giữ nguyên văn, nội dung đã vào ô 3 mới
**Đích:** việc gì lặp lại cũng có quy trình chuẩn → người mới, phiên AI mới làm theo là ra đúng sản phẩm, hướng tới muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể.

**Công thức**

1. Tool quy trình = các bước + đủ câu hỏi phải trả lời + thế nào là xong.
2. Danh mục = 3 Chuỗi × nhóm chuyên môn × 3 lớp.
3. Đạt = làm theo là xong, ra sản phẩm. Còn mắc → sửa quy trình → làm lại.
4. Chuẩn mực = chuẩn tốt nhất của ngành IT làm nền + phần riêng Incomex thêm sau.

**Giải nghĩa**

5. 3 Chuỗi: CTCM Chế tạo cỗ máy · VHCM Vận hành cỗ máy · CMSXQT Cỗ máy sản xuất quy trình.
6. Nhóm chuyên môn: thiết kế UI · config · xét nguyên tắc giao việc (của MOT)… → người dễ nhận diện, đánh giá, góp ý.
7. Lớp design = đủ câu hỏi → thiết kế thành công. Cho việc sáng tạo ban đầu: vẽ UI, lên danh sách, config.
8. Lớp execute = câu hỏi + thứ tự bước + thế nào là xong. Cho agent làm lặp lại.
9. Lớp DOT/script = mục tiêu + thế nào là xong + trigger. Máy tự chạy.
10. Phần sẽ viết thành DOT → DOT là trạng thái cuối. Chạm Directus/PG → bắt buộc DOT.
11. Phần còn lại: ở design hoặc execute mãi, không lên DOT — DOT mất thời gian, kém linh hoạt. Vd thiết kế UI: design là đủ.

**Cách làm**

12. Hội đồng AI hiệu chỉnh, bổ sung liên tục → quy trình ngày càng hoàn thiện.
13. Sai sót hoặc thiếu mà chưa sửa ngay → ghi một sổ, theo vòng đời tới khi xong.
14. Giờ AI ghi tay trên repo/VPS cho nhanh → sau mọi thứ vào PG (lấy quan hệ, vòng đời tự động).
15. Cho người đọc: chuẩn mực, dễ nhìn, một khuôn. Nửa phút biết có gì, thiếu gì, tắc ở đâu.

**Chưa làm lúc này:** quy trình nghiệp vụ (phái cử, tuyển dụng…). Chúng thuộc Chuỗi 3 CMSXQT; để sau cho đỡ lan man.

(Owner chốt 08/10/2026. AI không sửa chữ ô này.)

#### Owner bổ sung trực tiếp · 10/10/2026 · D24
“Bắt đầu vào bất cứ 1 việc gì? nhỏ hay lớn => chúng ta nên có 1 quy trình tổng hợp toàn diện chung nhất. Quy trình TH này vừa là khuôn thức cho cách làm, vừa là khuôn thước cho kiểm tra, vừa là khuôn thước để lập kế hoạch, tự động hoá, giám sát, theo dõi để biết sai ở đâu.”
“User chỉ cần mục tiêu => phần còn lại, tự chạy ra kết quả.” “Sáng tạo là cách sửa đổi quy trình chứ không phải AI tự sáng tạo trong những công việc lặp đi gặp lại hàng ngàn lần như vậy.”
Phạm vi cụ thể Owner nêu: việc/mã/Master; bắt đầu và kết thúc có kiểm kết nối; điều kiện đầu vào và thực hiện; kế hoạch/kết quả/sai thiếu/test ghi đâu; người làm/kiểm/duyệt/nhận; xác nhận trước triển khai; phiếu đủ/thiếu và vòng đời. Owner giao Host nâng cấp quy trình hiện có hoặc thêm TH06 nếu cần; ưu tiên nhìn là hiểu.


#### Bổ sung trực tiếp Owner · 09/10/2026 · rà khả thi hướng PG
“Chúng ta cần tư duy để thực sự lắp chuẩn vào PG. Và rà soát theo hướng đó (kiểu mô phỏng) thì mới phát hiện ra lỗi được. Bạn rà soát tiếp tục để hoàn thiện, đảm bảo khả thi.”

#### Làm rõ mục tiêu theo yêu cầu Owner · 09/10/2026
Giữ nguyên 15 ý trên. Host bổ sung để AI hiểu đủ đích phải làm:

1. **Có quy trình để làm được việc:** quy trình con giải quyết từng việc; quy trình tổng hợp nối chúng tới mục tiêu. Quy về MOW/MOT theo công thức hiện hữu, có tên, mã và nơi đăng ký; phân biệt mã tài liệu, bản nháp và quy trình đã được phép gọi.
2. **Đủ câu hỏi đúng, theo đúng thứ tự:** ghép câu hỏi Chuỗi/Tầng/Bước, khai báo MOW/MOT đang làm, đối tượng xử lý và nghiệp vụ UI/Config/Test; thêm ghi chú riêng đúng phạm vi. Mỗi câu có chỗ ghi đáp án, căn cứ và tiêu chí đạt; thiếu ở đâu sửa nguồn đó.
3. **Biết cách thực hiện và bàn giao:** làm gì trước/sau, ai làm, bắt đầu khi nào, đọc đâu, ghi đâu, báo cáo ai/khi nào, gọi quy trình nào, đưa gì và nhận gì; khi nào đi tiếp, quay lại, dừng hoặc kết thúc.
4. **Khép kín cả sai/thiếu:** phát hiện → xác minh → xử lý → đấu lại → kiểm tại nơi phát hiện → kết thúc. Mọi nhánh có người giữ, nơi nhận/trả và tiêu chí đóng; gửi chưa đồng nghĩa đã nhận, bị từ chối không đồng nghĩa mục tiêu đã đạt. Rà cả chỗ hở và chồng lấn.
5. **Tính đến khi chạy:** thiết kế và đánh giá khả thi → config/triển khai và kiểm kỹ thuật, AI thao tác UI → vận hành thực tế, log/phản hồi và hiệu chỉnh. Mỗi giai đoạn có nghiệm thu; bàn giao theo dõi dài hạn để lần chế tạo có điểm kết thúc.
6. **Chuẩn bị dữ liệu ngay từ ngoài PG:** mọi đối tượng/bản ghi cần quản lý đều có mã, quan hệ và nơi lưu chuẩn; tách định nghĩa, phiên bản, lần chạy, vòng chạy và kết quả kiểm. Giữ mã/quan hệ khi chuyển PG; tách mức kiểm, kết quả và hiệu lực để chỉ kiểm lại phần bị ảnh hưởng.
7. **Chứng minh bằng việc làm theo:** người/AI mới đọc, trả lời và đi hết ca áp dụng để ra đúng sản phẩm. Còn mắc phải ghi rõ câu, bước, nguồn hoặc chỗ nối cần sửa rồi thử lại. Trình bày một nguồn chuẩn, nhìn nhanh biết có gì, thiếu gì, ai xử lý và bước tiếp theo.

#### Bổ sung của Owner · 08/10/2026 · giao trực tiếp Astra Codex làm Host
Nguyên văn yêu cầu triển khai mới; áp dụng từ lượt này. Nội dung mục tiêu cũ phía trên giữ nguyên.

Giờ bạn Astra codex cần làm gì?

1. trong tools-quy-trinh (tạm thời giữ nguyên cái đống rác AI đang tạo ra để đó) nhưng bạn làm cho tôi tab đầu tiên là các câu hỏi cơ bản: Bước lớn cần trả lời câu hỏi gì? từng bước con cần trả lời câu hỏi gì? Từng tầng cần trả lời những câu hỏi gì? từng chuỗi cần trả lời các câu hỏi gì?
2. Hãy trình bày sao cho cùng 1 logic với bước tầng và chuỗi của công thức. Cái này giúp con người có hình dung rõ nhất. => Tôi đề nghị: Thiết kế UI đúng như bên công thức, bấm vào từng cái thì có danh sách câu hỏi cần trả lời (cái này rất tiện cho con người nhưng có thể hơi khó khăn cho AI ) bạn làm thế nào tiện cho con người tư duy nhưng vẫn tiện cho AI quét danh sách thì làm.
3. Các câu hỏi này ngắn gọn, và làm đến đâu chúng ta tiếp tục hiệu chỉnh đến đó. Có thêm ý kiến hội đồng để điều chỉnh.
4. Bạn là host của task này đi. Các ý kiến khác không được ghi thẳng, bạn xem xét có đồng ý bổ sung thêm không rồi mới bổ sung.
5. Chúng ta gọi nhóm câu hỏi của Bướg, tầng, chuỗi là câu hỏi về chuyên môn. Còn ghép với nghiệp vụ như: thiết kế UI, test, UI, config... thì ghép với bộ câu hỏi chuyên môn là xong. Làm chuyên mô gì => có bộ câu hỏi của chuyên môn đó. và như vậy, ghép lại được ma trận rất phức tạp nhưng tư duy lại đơn giản.

Ngắn gọn lại có mấy chuyện:

1. Thiết kế giống hệt bên took quy trình và nhét câu hỏi chuyên môn vào. Và làm thê nào các câu hỏi chuyên mộn này từ bảng mà nó chạy vào thì tốt. Ý tôi là làm SSOT trên 1 ma trận câu hỏi chuyên (nó tiện cho nhìn số lượng lớn và tiện cho AI) nhưng có thể ghép để ma trận này là SSOT và chạy vào từng miếng trong thiết kế để con người dễ tư duy. Vì khi bàn đến 1 việc thì tôi cần nó rất đơn giản thì mới nghĩ được.
2. Bổ sung 1 thiết kế về các câu hỏi chuyên môn, những chuyên môn mình đã chốt, và chờ thời gian chỗ chuyên môn đấy sẽ kéo dài dài ra.

#### Bổ sung Owner · 09/10/2026
1. Ý kiến cuối của gpt. Bạn kiểm tra lại lần nữa và hoàn thiện quy trình
2. Sau đó bạn rà lại thử với QT 001 (làm lại) xem với bộ câu hỏi ghép như vậy còn vướng gì không? Chúng ta tiếp tục rà soát các quy trình nghiệp vụ như vẽ UI, config

Tôi có 1 lưu ý riêng: Bạn nên quy định thêm trong readme hoặc đâu đó để các AI dế đọc.

Ở mỗi bước con, mỗi tầng ngoài các câu hỏi chính nên có có ghi chú riêng. Ví dụ, bước con 1.1 khi ghép vpwis T0 có thể cần ghi chú riêng, T0,5 cần ghi chú riêng, T1, T2 có những gi chú riêng. Các ghi chú này không thể đưa vào câu hỏi chung, quy định chung và chỉ mang tính chất đặc thù ở mỗi T1. => nói cách khác, cái chúng ta làm vừa rồi là quy định chung để ghép chung, và giờ cần thiết kế ở dưới đó là quy định riêng. Những quy định nào phổ quát được thì đưa luôn vào tầng (T) nhưng không thể đưa được vào bước con/bước ra, không thể đưa được vào (T0-T2) => thì sẽ đưa vào ghi chú của bước cha/bước con.

#### Bổ sung Owner · 09/10/2026 · Quy trình tổng hợp

Nếu, thông tin trình bày nó đủ đơn giản, tôi-con người có thể giúp sáng tạo đưa ra những phương pháp hiệu quả và đơn giản. Nhưng điều quan trọng nhất là thông tin đến chỗ tôi nó phải đơn giản, bạn phải giúp tôi để tổng hợp được vấn đề nó đơn giản thì tôi mới xử lý được.

Bước tiếp theo:

Rõ ràng chúng ta cần 1 quy trình để vận hành các quy trình chế tạo cỗ máy: "Quy trình thiết kế - xây dựng một chi tiết/ chức năng trong chế tạo cỗ máy" - Tên hơi lạ và hơi dài nhưng trước hết cùng nhau hiểu đúng vấn đề cái đã.

Quy trình này sẽ lắp ráp hoá lại các bước rời rạc mà chúng ta đang làm: Bắt đầu từ việc:

1. đặt tên nó trong master list (đã làm)
2. Thiết kế ra UI (đang làm) - Bản chất là vận hành các bước / trả lời các câu hỏi của thiêt kế UI.
3. Giả định chạy thử các quy trình tiếp theo theo thứ tự => Cái chúng ta đang lần mò xem làm việc gì trước việc gì sau. => Và giờ cần làm bao nhiêu việc (vận hành bao nhiêu quy trình con) => quy trình nào trước, quy trình nào sau, khi nào thì đến quy trình tiếp theo, khi nào phải quay lại đâu?...===>>> Đích đến cuối của nó là được thông qua và yên tâm nó chạy, hoặc phải ghi những sai thiếu vào sổ và khi giải quyết các vấn đề sai thiếu đó => hệ thống sẽ chạy và khả thi như ý muốn.
4. Nên chia ra làm các giai đoạn chính:
   1. Giai đoạn thiêt kế và đánh giá khả thi (đang làm), bao gồm cả dự kiến config, đủ trường hoặc ghi đủ danh sách
   2. Giai đoạn config thực tế, đưa vào PG và test kỹ thuật, bao gồm cả AI/Agent test thực tế trên UI, làm thử giả lập như người.
   3. Giai đoạn vận hành thực tế, đọc log + nhận phản hồi từ người dùng => hiệu chỉnh.
   4. ===>>> Cả 3 giai đoạn đều có checkpoint nghiêm thu.
5. Quy trình này về bản chất là sắp xếp các thứ tự của các quy trình khác, bổ sung các quy trình còn thiếu để nhất quán hoá 1 quy trình chuẩn làm ra 1 việc đơn giản như thiết kế 1 cái UI. Vì rõ ràng là chỉ thiết kế 1 cái UI thì chẳng có nghĩa gì bởi vì nó không chạy. Còn muốn nó chạy tới cuối cùng => thì tất cả các câu hỏi, quy trình phía sau phải được trả lời đầy đủ.
6. Vị trí của quy trình này nằm ngay trên đầu các quy trình khác (rõ ràng nó quản lý các quy trình khác) => Bạn đặt tên 1 thư mục ngay trến đầu của https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh thành tab đầu tiên (thu gọn/xổ ra được) và đặt tên tab là: List quy trình tổng hợp. Đây chỉ là quy trình tổng hợp đầu tiên. Cố gắng giữ style trình bày dễ hiểu cho con người nhé. Tôi chỉ cần nhìn nhanh để nhận ra vấn đề thì tôi sẽ giúp các bạn sáng tạo và đi về đích. Nếu chỉ để cho AI làm không thì sẽ tạo ra 1 mớ rác giống như chúng ta đã từng làm.

#### Bổ sung Owner · 09/10/2026 · Khép kín quy trình (tiếp tục cùng mục tiêu)
> Rất ngắn gọn lại thì nó chỉ quanh quẩn ở:
> 1. Trả lời đủ các câu hỏi, từ đủ các góc độ
> 2. Có trình tự trả lời câu hỏi, cái gì trước cái gì sau?
> 3. Câu nào đạt phải có chỗ ghi đạt (gồm nhiều trạng thái tăng dần, chứ không chỉ yes or no) => Lần kiểm tiếp theo chỉ xét những cái chưa đạt, tránh việc lần nào cũng làm lại từ đầu mất thời gian. rồi đang đạt => thành chưa đạt => chưa đạt thành đạt..... làm sao để tự động hoá bớt các quá trình này (Dự vào PG/ DOT/Jev..... cuối cùng mới là agent. Vì Agent làm rất mất thời gian, xác suất sai vẫn có, và tốn kém nữa.
> 4. Có quy trình rà soát để biết quãng nào đang gãy (thiếu quy trình kết nối) quãng nào đang chồng lấn (nhiều hơn 1 quy trình đang giải quyết 1 việc), rà soát trạng thái nào, thông tin nào chưa có chỗ ghi, trạng thái nào chưa đấu vào vòng đời theo dõi đến tận cùng? Trạng thái nào chưa có câu trả lời là thế nào là đạt, khi nào kết thúc hay vẫn open? chưa có chỗ gho chép? chưa đấu vào quy trình hiện hữu để giải quyêt đến cùng? chưa có quy trình giải quyêt tiếp theo?

Các ý tưởng T2.5/Master riêng và vòng đời thấy thiếu→xác minh→đề xuất được Owner nêu để xem xét, không phải lệnh tự đổi khái niệm. Giữ MOW tổng hợp là MOW; phần đăng ký Master còn hở phải hiện rõ.

#### Bổ sung Owner · 09/10/2026 · Chuẩn dữ liệu ngoài PG
Đây là chúng ta mới phác thảo về mô hình => sau này khi chuẩn hóa mọi thứ sẽ đưa vào PG, nó còn những mô hình như phiên bản, bước chạy, vòng chạy...... cho nên việc thiết kế bây giờ phải tính đến phù hợp khi chuẩn là bê nguyên vào PG vì xử lý trong PG mất thời gian hơn rất nhiều => cách nhanh là xử lý chuẩn thông tin bên ngoài rồi bê nguyên cả khối vào. Mọi thiết kế phải hướng đến việc đó, phải có mã để giải quyết vấn đề khoá chính / khoá phụ trong DB.

Nắm cách nôm na ngắn gọn là hãy gói hết vào; Quy trình, để gọi và quản lý, Không gì là không có mã. Như vậy tổng cả bức tranh chúng ta giải quyết vấn đề mới nhanh và chính xác được. Chúng ta mới chỉ giải quyết vấn đề công thức, vấn đề nó chưa phức tạp. Khi ghép và dữ liệu thực, quy mô nó sẽ nhân lên hàng chục nghìn lần, thậm chí hàng triệu lần => nếu kiến trúc không rõ ràng và tường minh từ đầu để sẵn sàng cho scale thì khi đổ dữ liệu vào sẽ thất bại.

Bạn rà soát tiếp. Cố gắng giữ cho vấn đề thật đơn giản để user nhìn cái hiểu ngay thì mới phát hiện ra vấn đề nó nằm ở đâu.

Một nguyên tắc Owner bổ sung 09/10/2026 (D22): “tất cả các trình tự thực ra là quy trình, nên đưa hết vào quy trình để giữ quản lý. Các luồng, các hướng dẫn... => về bản chất là thành quy trình. Chúng ta chỉ quản lý 1 đối tượng đã quy trình (MOW và MOT thôi). Hạn chế sinh ra khái niệm mới.”

#### Ô 2 bản 08/10/2026 (D04) và tiêu chí Host — nguyên văn
Một quy trình đạt = người mới hoặc phiên AI mới làm theo, không hỏi thêm, ra đúng sản phẩm thật.
Chưa đạt → sửa quy trình, thêm câu hỏi còn thiếu → chạy lại.

(Owner duyệt 08/10/2026.)

#### Tiêu chí kiểm soát bổ sung · Host theo yêu cầu Owner 09/10/2026
Áp dụng cho từng quy trình và phạm vi sản phẩm đã khai báo:

- **Khai báo đủ:** mã/phiên bản, mục tiêu, đầu vào/ra, việc con có thứ tự, người làm/giữ, nguồn đọc/nơi ghi, trigger/điều kiện, báo cáo, nơi nhận/trả và điều kiện kết thúc.
- **Trả lời đủ:** câu hỏi áp dụng có đáp án và căn cứ; ghi chú riêng có phạm vi. Đối chiếu hai chiều yêu cầu ↔ UI/Config ↔ ca kiểm; không có chỗ thừa vô căn cứ hoặc yêu cầu bắt buộc bị bỏ sót.
- **Nối kín:** các nhánh thành công, thiếu, lỗi, từ chối, chưa nhận/quá hạn đều có cách xử lý và người chịu trách nhiệm. Hồ sơ sửa xong phải trả về đúng nơi phát hiện và kiểm lại; kết thúc không thực hiện phải ghi rõ mục tiêu chưa đạt.
- **Kiểm được và dùng lại được:** lưu mã ca/lần chạy, nguồn/phiên bản, bằng chứng, mức kiểm, kết quả, hiệu lực. Nguồn đổi thì xét lại phần ảnh hưởng; dữ liệu có mã/quan hệ để chuyển PG và quản lý vòng đời.
- **Nghiệm thu đúng mức:** người/AI thực hiện xác nhận làm được/một phần/chưa làm được bằng ca áp dụng. Tách nghiệm thu thiết kế, triển khai và vận hành; mục không áp dụng phải có lý do. Việc bắt buộc còn hở thì giữ mở, không nhận toàn quy trình đã thành công.

#### Ô 3 trước D25 — nhật ký kiểm/tiếp nhận, TQT-REQ, TQT-DIR và các khung (nguyên văn; bản hiện hành ở ô 3 mới)

#### P16 · Master quy trình tổng hợp và tiếp nhận PR-07 · 09/10/2026
§0.3: đã đối chiếu. Owner trực tiếp yêu cầu Master list riêng theo UI cha, có tên/mã, đồng thời giữ trong tools-quy-trinh để bàn khi dưới 10 quy trình.
Định nghĩa Owner: “quy trình tổng hợp là để giải quyết các mục tiêu lớn, khép kín. Trong khi, quy trình bình thường là để giải quyết các nhiệm vu nhỏ hơn. Một Quy trình tổng hơp gồm nhiều quy trình thường nhưng vẫn nhỏ hơn chuyên môn. Còn chuyện có đưa ra tầng 2.5 hay không thì bàn sau.”
Nguồn duy nhất: `view.html#tqt-composite-processes.catalog`. ML-MOW-TH-001; 4 MOW-TH-001…004. UI.MASTER.MOW.TH dùng nguyên master-list.js và khuôn UI cha; trang bàn luận là cách xem cùng nguồn. 9 quy trình Tool hiện có + triển khai/khôi phục + quan sát/bàn giao + khai/kiểm câu hỏi; không cộng thành 16 quy trình tổng hợp.
C1: TH001 gọi MOW-TH-002 ở 1.4/2.3/3.2; Tool008 là bước ghi nhận của cùng vòng, không tự đóng vòng riêng. C2: 20 tham chiếu typed code/version (đã gộp trùng), tách nguồn đọc khỏi lời gọi; href suy từ catalog; chuyển phần đang dùng khỏi tab tạm bằng cùng DOM, giữ neo cũ.
C3: giữ mức0–4, thêm điều kiện theo giai đoạn/context; mốc Vận hành cần đủ quan sát/log/phản hồi/nhận bàn giao. Hàm kiểm thiết kế có ca âm; chưa thay các PG guard đang mở. C4: đưa 5 ý khép kín lên đầu tab. PR-07 mục2–3 chưa áp, giữ lời Owner ô1–2.
Kết luận/nguồn kiểm ở README và UI-REVIEW-AGGREGATE.json. Chưa nhận quy trình đã chạy thật, chưa đóng TQT-ISS-007.


#### Lưu vết kiểm giao diện trước khi cập nhật mục tiêu
- Kiểm TQT-TH-001 ngày 09/10: bản nội dung `87212f520d3251b5f13738222094278046a92512` đã hiện trên trang thật. Đã kiểm tab đầu trong Nội dung công việc; thu/xổ quy trình; mở giai đoạn 1 và bước 1.2; liên kết Config sang nguồn cũ; URL mở thẳng giai đoạn 2; URL câu hỏi B1→1.2 cũ; màn 390px không tràn ngang trong tài liệu (295/295px). Đã thu gọn thanh tab màn nhỏ để không che nội dung. URL chỉ có task vẫn vào Kiểm soát theo cơ chế chung; link bàn giao có view=content&section=list-quy-trinh-tong-hop. Console trang chứa có thông báo Directus Auth/Sentry; không dùng kết quả kiểm hiển thị này để khẳng định backend hoặc toàn quy trình đã chạy đạt. Chưa triển khai PG hay nghiệm thu ba giai đoạn.
- Kiểm tra giao diện: đã kiểm trên trang thật bản nội dung 7a4c0717eebd0c074635a2a5e8dab63e9fa56d18: B1→1.2 và mở lại URL, B8/B9 chưa tách, MOIT, CMSXQT, lọc không dấu, Config→mục cũ, bộ ghép 27 câu không trùng; màn hẹp 390px không tràn ngang. Đây là kiểm giao diện, chưa nghiệm thu tính đầy đủ của bộ câu hỏi.


#### Rà chuẩn ngoài PG · tiếp nhận proposal05 · 09/10/2026
- Đã tái hiện lỗi cũ: đóng danh sách rỗng/thiếu quyền, cổng sẵn sàng rỗng và payload rỗng đều lọt. Đã sửa tại SSOT và checker; không thay câu hỏi hay công thức.
- Mô hình v2 gồm 18 bảng (thêm phiếu/quyền/outbox), khóa ghép/typed reference, hợp đồng trường và nguồn cấp, luật–cơ chế chặn, ghi nguyên tử, bất biến bằng chứng, tách schema và dữ liệu SIM. Giữ sáu ô.
- Bằng chứng: 83 ca mô phỏng đạt; phiếu 70 lượt đọc lại đầy đủ và dump/nạp lại; đường sáu ô có sáu call SENT/ACK/RETURN, hai nơi kiểm lại rồi đóng; từ chối giữ UNMET, trả muộn không hồi sinh việc. SQL/PLpgSQL đã kiểm cú pháp; không chạy PG. Hash mô hình: `f2e5b358eedac180c4f17aa0594f27d687fe145ba4843e82fbba6ee8ec32f471`.
- DOER_CONFIRM: làm được sửa hợp đồng/kiểm ca sai/lưu–đọc lại và vòng mô phỏng; chưa xác nhận PostgreSQL, concurrency, scale hoặc gọi B3–B7 thật. Gói NOT_FROZEN và TQT-ISS-007 mở: chốt Master, quyền DOT/actor, triển khai adapter, kiểm staging/restore; thay guard quét toàn mô hình bằng kiểm theo phạm vi trước production.
- Kiểm sau lưu: snapshot repo `871115917f97810e84ebcf591eaa884bf581ec6e`, job `cfc46e5004004a129fdbba040a598271`, exit 0, 83 ca đạt, hash khớp; production_ready=false/NOT_FROZEN. Browser bản xuất cùng commit hiển thị đủ sáu ô và mục “83 phép kiểm…”, mở chi tiết bằng chứng/giới hạn được. Kiểm bản xuất trực tiếp, không suy ra cổng modules hay PG đã đạt.
- Trạng thái/giới hạn hiện hành đọc mục v2 trong README và `package` của mô hình. Các kết quả v1 bên dưới là lịch sử, không là tiêu chí áp dụng v2.

#### Mô hình có mã hướng PG · 09/10/2026 · Host tiếp nhận proposal04
- JSON tqt-process-model là SSOT bản phác thảo TQT-MODEL-001: 15 bảng hỗ trợ định nghĩa/phiên/lần/vòng/việc chạy/call/vấn đề/nơi ảnh hưởng/đáp án/kết quả/phụ thuộc/event; PK/FK/UNIQUE/CHECK có thể xuất SQL nguyên mã. DRAFT/SIM không phải Master được phép gọi.
- Đã ghép phiếu MOW/MOT + đối tượng + nghiệp vụ; CTCM+B1.3+FIELD+UI có 70 lượt theo phạm vi/54 mã câu, không thêm câu (159/53). Tách level/result/validity; các mức kiểm/vòng đời vẫn là thiết kế.
- Kiểm: 27 phép mô phỏng/SQLite đạt ở local và snapshot repo a91f229 (job b2c2769d009746fb98872bf1dade16a4, exit0); hash gói a3ce244dd473a71919ba07f723c1c005853fa9f3419007da98a07fba862e0b6d. Renderer kiểm cú pháp đạt. Browser bản79fa9e35: phiếu CTCM+B1.3+FIELD+UI 70 lượt/54 mã, PROCESS17/TASK17, target vẫn FIELD và đáp án null hiện chưa khai; mở chi tiết rộng1200px; bảng kết quả/hiệu lực đúng; màn390px không tràn (375/375). Mũi tên lấy trạng thái call từ dữ liệu, không tự giả đã gửi khi chưa khai call. Cổng modules vẫn báo chưa snapshot, bản xuất trực tiếp đọc được. Chưa PostgreSQL/concurrency/tải lớn; chưa Field hoặc B3–B7 thật. DOER_CONFIRM: làm được chuẩn bị mô hình có mã/kiểm/xuất gói SQL nháp; chưa xác nhận nhập PG hoặc chạy nghiệp vụ.
- Trình sáu ô có mã/người giữ/chỗ ghi/kết quả; nguồn riêng của gói chỉ trong view.html. check-process-model.py là bộ kiểm/đường xuất, không là runtime production. TQT-ISS-007 còn mở; kết thúc chế tạo cần ACK VHCM, chưa có người/quy trình nhận thật trong ca này.

#### Rà khép kín · 09/10/2026
- Đã xác định TQT-TH-001 chỉ là mã tài liệu, chưa là dòng Master CTCM. CT-005/ML-DEF-004 đang một-một Nhóm cha; quan hệ MOW tổng hợp gọi con cần chốt, không tự tạo T2.5/nhóm giả.
- Tab đầu có bốn chỗ hở, thứ tự khai báo, bộ câu hỏi dẫn nguồn, đường thiếu Field, hợp đồng chỗ nối và thiết kế kiểm lại theo phiên bản. Thêm 19 câu (159/53), không nhân bản câu ở bộ tổng hợp.
- Mở TQT-ISS-007 cùng sổ hiện có; hồ sơ SSOT ở closure_review.issue, UI sổ dẫn cùng dữ liệu. PG/DOT/JEV tự động chỉ ở mức thiết kế; chưa đăng ký MOW, chưa hoàn tất ca xuyên B3–B7.
- Kiểm trước ghi: mã câu duy nhất/owner tồn tại/30 tham chiếu câu hợp lệ; cú pháp renderer đạt. Kiểm browser bản xuất `d60306d2871ecacc082e9e92a1e4955f0ad0501d`: mở bộ câu dùng chung; lọc Q-MOW-08 đúng 1/159; mở TQT-ISS-007 và quay về sơ đồ; đường thiếu Field có nhánh dùng/sửa/tạo mới/chưa rõ; màn390px không tràn (375/375). Đã sửa liên kết tới hồ sơ để tự xổ đúng mục. Cổng /knowledge/modules đang báo chưa có snapshot khi kiểm; bản xuất trực tiếp vẫn mở và hoạt động. Đây là giới hạn kiểm cổng, không phải mất tài liệu; chưa xác nhận khắc phục. DOER_CONFIRM: làm được phần thiết kế/rà nguồn/trình bày; chưa đăng ký MOW, chưa vận hành một ca xuyên B3–B7 hay PG/DOT tự động.

#### TQT-TH-001 · quy trình tổng hợp đầu tiên · 09/10/2026
- Theo chỉ đạo bổ sung của Owner: tab đầu tiên “List quy trình tổng hợp”, mặc định khi vào nội dung không có section. Có thu/xổ quy trình, giai đoạn và từng bước; đường cũ tới câu hỏi/legacy giữ nguyên.
- Nguồn duy nhất: JSON `tqt-composite-processes` trong view.html. Một quy trình, 3 giai đoạn, 9 bước phối hợp và 3 checkpoint; gọi quy trình con bằng tham chiếu, không nhân bộ câu hỏi/sổ.
- Thiết kế/khả thi → Config/PG/test kỹ thuật + Agent UI → vận hành/log/phản hồi. Mỗi bước có đầu ra, điều kiện đi tiếp và đường quay lại; checkpoint phân biệt đạt/có điều kiện/chưa đạt, không coi ghi sổ là chạy đạt.
- Hai hướng dẫn con còn thiếu (triển khai/khôi phục, log/phản hồi) được bổ sung ngay trong quy trình tổng hợp, ghi rõ khung mới cần áp thử, không cấp quyền PG hay nhận đã tự động hóa.
- Gom việc lặp theo nguyên nhân, dùng mã sổ gốc; đề xuất công thức chung phải được duyệt/kiểm trên ca đại diện và phần ảnh hưởng. Bản trình Owner gói trong ba câu: đang ở đâu, vướng gốc nào, cần quyết định gì.
- Đây là soạn quy trình và giao diện; chưa phát chạy PG, chưa mở vận hành/automation, chưa nghiệm thu quy trình tổng hợp bằng một lượt đầu–cuối. MOW001 chỉ làm ví dụ đọc theo phiếu09/10, trạng thái chuẩn vẫn ở phiếu sản phẩm.

#### TQT-HOST-APPLY-MOW001-20261009
- Tiếp nhận có kiểm chứng [phiếu GPT vòng3](proposals/TQT-PR-20261009-gptchat-mow001-walkthrough-03.md) @229c74a. Host tự đọc nguồn và bấm lại trình duyệt; không dùng kết quả GPT như bằng chứng thao tác của Host.
- Đã bổ sung note_policy/notes vào cùng JSON câu hỏi: tầng, bước và giao bước×tầng; phạm vi AND, bước con kế thừa cha, không tự ghi đè. Có 8 ghi chú được tiếp nhận từ nguồn đã đọc/lượt áp dụng; không tự tạo ghi chú giả cho T0.5/T1/T2. Ma trận vẫn 140 câu/53 nhóm.
- Bổ sung hướng dẫn thực hành UI/Config bằng ghi chú nghiệp vụ, cùng nguồn; README dẫn quy tắc và phiếu áp dụng. Ý kiến khác vẫn ghi riêng qua Host.
- **Phiếu đáp án và kết quả duy nhất:** [UI-REVIEW-MOW001.json](../mow-mot-moit-mout/UI-REVIEW-MOW001.json), mục process_trial_20261009. 44 mã câu/120 lần áp dụng +7 Config×3 +24 ô UI cũ. Hợp đồng A/B/C đã chốt cho thiết kế; không gọi là backend thật đã có.
- Host bấm 14 ca: nguồn live chưa nối; demo SĐT→2, lọc MOIT→1; mô tả chưa semantic; 1.3 không có JEV nhưng checkbox tạo receipt → FAIL theo hợp đồng. Back/input/clear/Enter và 390px đã kiểm; console không có lỗi trong phiên đo.
- **DOER_CONFIRM=PARTIAL** cho toàn lượt rà UI: đọc/ghép/trả lời và chẩn đoán làm được; UI001 và runtime chưa nghiệm thu. Check-ui-review vẫn BLOCKED; không hạ gate. Ghi đúng OPEN-03/04/08/05/09; OPEN-10 ngoài B1, không ép tạo mới.
- Kiểm sau đồng bộ 5ada3e0: trang thật giữ140/140 câu, 8 ghi chú; B1.1+FIELD+UI nhận5 mục; đổi MOIT chỉ còn B1 và UI, không nhận ghi chú Field; B2+FIELD+UI chỉ còn Field/UI; B1.2+FIELD+CONFIG nhận đúng ghi chú riêng1.2 vàConfig. Catalog hiển thị8 mục. Phiếu và toàn bộ9 bộ ghép đã kiểm khớp44 Q_ID/120 lần áp dụng. Gate repo job c6f58d35b17749019bcd1084444a623a vẫn BLOCKED đúng với trạng thái sản phẩm.
- Còn làm: sửa UI001/Config theo đáp án A/B/C, hòa giải nghĩa màu cũ tại NHCN-003 rồi kiểm lại; nối nguồn/rule thật trước khi báo live đạt. Lượt này rà, không sửa runtime hoặc Master; MOW002 chưa làm.

#### TQT-HOST-REVIEW-GPTPRO-R2-20261008
- Tiếp nhận góp ý [vòng 2](proposals/TQT-PR-20261008-gptchat-review-questions-02.md), nguồn 7984be5; Host quyết định, không tính là nghiệm thu hoặc phiếu khác hãng.
- Sửa tại Q-B1-03, Q-B1.3-02 và Q-CTCM-01 để bộ ghép Tìm không bắt thực hiện Dùng/Tạo/Sửa/Vô hiệu. Lỗi nguồn hoặc chưa đủ dữ kiện không được suy thành đối tượng không tồn tại. Không đổi Công thức hay sơ đồ vòng đời tổng.
- Config: thêm required_reference trên nhóm CONFIG, chỉ tham chiếu 7 câu gốc theo vị trí và đáp án có thể đối chiếu; không sao chép câu vào ma trận. Bộ ghép hiển thị yêu cầu 4 câu bổ sung + 7 câu gốc và đường đọc; danh sách đối chiếu lấy chữ từ #tqt-7-cau đã có. Nguồn sửa legacy vẫn CONFIG_PRINCIPLES; chưa cắt chuyển. Cặp reuse_candidates chỉ là ứng viên kiểm, không tự nhận tương đương/đã trả lời.
- R-PROVE kiểm hai chiều yêu cầu ↔ UI/Config ↔ ca kiểm; R-ANSWER phân biệt giá trị lúc chạy với thiếu nguồn/tiêu chí; R-INHERIT giữ phạm vi đáp án từng MOT. Vẫn 140 câu/53 nhóm; không thêm Bước con.
- Kiểm trang thật fe7ed5c: CTCM+B1.3+FIELD+CONFIG hiện 31 câu trong ma trận và đủ 7 tham chiếu nguồn; đường “Mở 7 câu Config gốc” mở đúng tab cũ/mục tqt-7-cau. Đổi sang UI còn 32 câu, không mang khối Config; ba câu sửa hiện đúng trong bộ ghép. Đây là kiểm cấu trúc/giao diện, chưa phải ca sản phẩm MOW001.
- Tiếp nhận cách thử tiếp theo: một phiếu ở task sản phẩm cho 3 MOT MOW001, mã câu → đáp án hoặc nguồn cấp lúc chạy → căn cứ → phần UI/Config → ca kiểm → kết quả/chỗ thiếu. DOER_CONFIRM theo kết quả thật. Lượt này xét/sửa góp ý và kiểm bộ ghép; chưa phải hoàn thành phiếu MOW001. MOW002 chưa làm.

#### TQT-HOST-REVIEW-GPTPRO-20261008 · đã tiếp nhận có chọn lọc
- Nguồn góp ý: Owner chuyển nguyên văn ý kiến GPT Pro trong phiên Host; yêu cầu “Chỉ có bạn là xem xét cuối cùng và xem cần bổ sung những gì giúp tôi.” Host quyết định tiếp nhận vào bản đang hiệu chỉnh, không coi đây là Owner nghiệm thu bộ câu hỏi.
- Đã có: ba thành phần Bước/Tầng/Chuỗi, 9 bước lớn/23 bước con, 5 loại đối tượng chính + T3–T7, 3 chuỗi; JSON SSOT, kế thừa, UI/Test/Config/NTGV. Không dựng lại hoặc nhân bản.
- Tiếp nhận: bổ sung Q-STEP-04 (nhánh), Q-CHILD-03/04 (việc/người hoặc máy/điều kiện/bằng chứng), Q-LAYER-04/05 (thuộc tính/điều kiện hợp lệ); làm rõ Q-STEP-01, Q-LAYER-03, Q-CHAIN-01. Tổng 140 câu, giữ 53 nhóm và toàn bộ mã cũ; tất cả vẫn draft.
- Quy tắc chuẩn nằm duy nhất trong JSON `rules`, UI đọc cùng nguồn: Bước con thuộc Bước; chỉ tách khi cần kiểm riêng; kế thừa không tự ghi đè; kiểm chỗ bàn giao sau ghép; đáp án có nguồn/phạm vi; sản phẩm truy về đáp án. Không thêm thành phần gốc hoặc Master.
- Không tiếp nhận như lệnh hiện hành: phần GPT Pro giao Codex READ-ONLY rồi trả GPT Chat xét, dựa commit b7139d4. Chủ sở hữu đã giao Astra Codex làm Host. Giữ cách gọi hiện hành: chuyên môn = Bước/Tầng/Chuỗi; nghiệp vụ = UI/Test/Config…
- JEV Reference đã được dùng kiểm chéo nội dung chung còn thiếu; quyết định trên do Host. Đây không phải một vòng hội đồng hoặc bằng chứng bộ câu hỏi đã đủ.
- Đã kiểm trên trang thật commit 00f473ed147ead69d568acef91cebd8797423131: ma trận hiển thị 140/140; lọc Q-CHILD thấy đủ 4 câu; ghép CTCM+B1.2+FIELD+UI cho 32 mã câu duy nhất, gồm 5 câu mới; hướng dẫn ghép hiển thị đúng từ JSON. Ảnh tools-quy-trinh-quy-tac-ghep.jpg trong outputs của phiên Host. Đây chỉ là kiểm thay đổi nội dung/giao diện, chưa phải thử MOW001.
- Còn mở: thử toàn bộ bộ câu hỏi áp dụng cho MOW-NHC-001; chỉ ra câu chưa trả lời được, nguồn cần sửa, chỗ nối không khớp và căn cứ cho từng phần UI. Đề xuất bước con chỉ khi qua quy tắc tách. Chưa có kết quả thử mới ở lượt xét ý kiến này; không phát DOER_CONFIRM=YES, không làm MOW 002.

#### TQT-ROOT-QUESTIONS-20261008 · triển khai theo chỉ đạo bổ sung ô 1
- Một JSON trong view.html sinh sơ đồ, bảng câu hỏi và bộ ghép; câu mới = draft. Bốn tab: Câu hỏi cơ bản, Câu hỏi nghiệp vụ, Ma trận câu hỏi, Quy trình hiện có.
- Bằng chứng 08/10: ma trận thật 135/135 câu, 53 nhóm; chọn CTCM + B1.2 + Field + UI → 27 câu/27 mã duy nhất. B1→1.2 hiện câu riêng + kế thừa, URL q-B1-2 tải lại đúng; B8/B9 không tự sinh con; MOIT và CMSXQT mở đúng câu; tìm 'nang cao' → 2 câu, 'de xuat' → 11 câu, 'giao viec' + Nghiệp vụ → 4 câu NTGV; Config→#tqt-7-cau mở tab cũ. Bàn phím đổi tab; 390px: body clientWidth=scrollWidth=375. Các câu đều còn draft.
- Source nội dung: commit 7a4c0717eebd0c074635a2a5e8dab63e9fa56d18. Renderer VPS: a03174bffe3e65f6b9f2729257427a5808c16717. Phát hiện: trang chứa trước đây chỉ nhận section cho MOW; nay TQT dùng cùng cơ chế, vẫn kiểm nguồn iframe và mã mục. Source/kiểm/hoàn tác: /opt/incomex/work/tools-quy-trinh/TQT-QUESTIONS-20261008/; rollback --check PASS, chưa chạy rollback.
- Nguồn runtime tại scripts/hvu-b2/README.md trên VPS; báo cáo dẫn nguồn: knowledge/current-state/reports/tqt-question-matrix-20261008.md. Ảnh kiểm chứng nằm trong output của phiên Host; không phải bản chuẩn mới.
- Còn mở: áp dụng thật để hiệu chỉnh câu hỏi; ý kiến hội đồng gửi riêng để Host quyết; không tự sinh bước con B8/B9 hoặc công nhận nghiệm thu.

#### TQT-REQ — bảng kiểm từng mục tiêu ở ô 1 · 07/10/2026
Mục tiêu chỉ có một nguồn là ô 1 (bản Owner chốt 08/10 · D04). Bảng chỉ là chỉ mục từ mã kiểm đến dòng mục tiêu Owner; ô 1 luôn là nguồn chuẩn, không tạo mục tiêu thứ hai. Trỏ về dòng của ô 1: REQ-01 → dòng 2, 5 · REQ-02 → dòng 3 · REQ-03 → dòng 1, 12 · REQ-04 → dòng 6 · REQ-05 → dòng 7–11 · REQ-06 → dòng 13–14 (sổ ghi cả sai sót lẫn chỗ thiếu) · REQ-07 → dòng 4 · REQ-08 → dòng 15 · REQ-09 → Đích và “Chưa làm lúc này”.
Nhiệm vụ/phạm vi lượt này: tạo đúng một task tên `tools-quy-trinh` trên incomex-workspace, tập hợp đầu mối để làm việc dài hạn. Việc tạo task hoàn tất không đồng nghĩa toàn bộ quy trình đã đạt tiêu chí tại ô 2.

| Mã | Căn cứ mục tiêu Owner trong ô 1 | Cách kiểm khi chuẩn hóa |
|---|---|---|
| TQT-REQ-01 | Ô 1 dòng 2, 5 — Ba Chuỗi CTCM / VHCM / CMSXQT, chia chuyên môn. | Danh mục thể hiện rõ phạm vi và nhóm chuyên môn, không chỉ có UI/CTCM. |
| TQT-REQ-02 | Ô 1 dòng 3 — làm theo ra sản phẩm, còn mắc thì sửa và làm lại. | Có đầu vào/điều kiện áp dụng, đích nhận sản phẩm, tiêu chí và bằng chứng. Ca mắc dẫn về đúng câu/bước cần sửa rồi kiểm lại. |
| TQT-REQ-03 | Ô 1 dòng 1, 12 — câu hỏi đủ và hội đồng cải tiến liên tục. | Mỗi câu có đáp án/bằng chứng hoặc được nêu rõ còn mở; câu không áp dụng có lý do. Chưa giải quyết câu chặn thì chưa được công nhận đạt. |
| TQT-REQ-04 | Ô 1 dòng 6 — nhóm chuyên môn, ví dụ xét nguyên tắc giao việc của MOT. | Tên dễ hiểu, mã ổn định, danh sách ngắn theo nhóm; góp ý chỉ được chính quy trình/câu/bước. Nhóm được bổ sung khi cần. |
| TQT-REQ-05 | Ô 1 dòng 7–11 — Design, Execute, DOT/script; có quy trình dừng ở Design/Execute. | Giữ đủ hợp đồng riêng của từng lớp tại TQT-LAYERS; có liên kết giữa các lớp, không tự coi bản thiết kế là bản tự động hóa. |
| TQT-REQ-06 | Ô 1 dòng 13–14 — sai sót HOẶC thiếu chưa sửa ngay phải vào sổ; khi ổn định chuyển PG. | Sổ có mã, nguồn, người theo dõi/xử lý/kiểm, trạng thái, bước tiếp, điều kiện đóng, bằng chứng và lịch sử; việc hoãn vẫn được theo dõi. Chuyển PG về sau giữ mã/lịch sử và chỉ một nguồn hiện hành. |
| TQT-REQ-07 | Ô 1 dòng 4 — nền chuẩn IT, sau đó phần riêng Incomex. | Mỗi chuẩn/mẫu/khung của task ghi một dòng `Nền: <chuẩn ngành IT> · Riêng Incomex: <thêm gì, vì sao chuẩn ngành chưa đủ>`. Chọn nền theo thước AGENTS A10-R1: có sẵn · nhiều người dùng · còn được duy trì · vừa cỡ Incomex (lấy khung, không bê cả bộ). Chưa tìm được chuẩn ngành ⇒ ghi `Nền: CHƯA TÌM` và tính là chưa đạt; không tự dựng rồi gọi là chuẩn. Phần đã phác thảo trước mục 7 (TQT-LAYERS, TQT-REGISTER, 9 Tools nguồn, khung trang nội dung) phải được đối chiếu lại theo dòng này. |
| TQT-REQ-08 | Ô 1 dòng 15: cho người đọc — chuẩn mực, dễ nhìn, một khuôn. | Một khuôn trình bày chung cho mọi quy trình; lớp trên cùng trả lời được ba câu có gì · thiếu gì · tắc ở đâu; thử với một người đọc mới trong nửa phút. |
| TQT-REQ-09 | Ô 1 Đích và “Chưa làm lúc này”. | Quy trình chỉ ghi đạt khi có một lượt người mới hoặc phiên AI mới làm theo ra sản phẩm thật (ô 2). Quy trình nghiệp vụ của Chuỗi 3 (phái cử, tuyển dụng…) chưa đưa vào cho tới khi Owner mở. Vế “làm sai cũng khó / không thể” của Đích: mỗi quy trình ghi rõ bước nào đã có chốt chặn làm sai, bước nào mới là lời dặn (nối AGENTS A10-R2). |

#### TQT-DIR — chỉ đạo Owner về phần mục tiêu · 08/10/2026 05:44 (nguyên văn)
Trạng thái: **ĐÃ DUYỆT — Owner 08/10/2026 07:16; bản viết lại đã lên ô 1–2 (D04).** Nguyên văn lời duyệt: “Ok bạn đưa lên thay phần này cho mục tiêu từ Owner. Có sửa thêm chút. "1.2. Sai sót chưa sửa ngay → ghi một sổ, theo vòng đời tới khi xong. " => Sai xót hoặc thiếu mà chưa sửa ngay -> Còn lại đồng ý cách viết và nôi dung của bạn => bạn đưa lên repo giúp tôi nhé. Đây là Mục tiêu user chốt => cần làm theo và đạt mục tiêu.”
- Ba lớp: “phải hiểu theo cả 2 nghĩa. Với những phần sẽ viết thành DOT thì đúng, bản chất đây sẽ là trạng thái cuối cùng, nhưng sẽ có những quy trình mà mãi chỉ ở lớp design hoặc execute không lên DOT (trừ những quy trình bắt buộc tương tác với Dirrectus/PG thì phải lên theo luật vì phải DOT 100%. Lý do dot mất thời gian, kém linh hoạt. Ví dụ thiêt kê UI chỉ cần ở mức design là đủ, không cần mức cao hơn.”
- Ranh giới: “tạm thời trước như ý bạn đã để đỡ lan man. Thực ra chúng ta đã chia 3 chuỗi, quy trình nghiệp vụ thuộc chuỗi thứ 3 "cỗ máy sản xuất quy trình" => "(phái cử, tuyển dụng…)," thuộc chuỗi cuối CMSXQT này.”
- Sổ và PG: “bản chất là giờ thì làm sổ cho nhanh, sau này mọi thứ sẽ đưa vào PG hết để lấy quan hệ, theo dõi vòng đời tự động... phức tạp thì chỉ có PG mới giải quyết được. Nhưng giờ AI "chép tay" cho nhanh.”
- Cách viết ô mục tiêu: “nên viết lại thành gjach đầu dòng, sao cho ý không bị sai đi. và cần ngắn gọn, dài quá con người bắt đầu cũng không nhớ. Nếu có thể, bạn hãy viết lại phần chỉ đạo của user trước. Tôi sửa/duyệt xong thì coi như đó thành lời User đưa lên. User chỉ đọc phần đó => viết sao để dễ nhìn, AI hay viết dài xong rồi các bạn cũng chẳng đọc kỹ hay sai. Con người cần nhìn vào đơn gỉan (kiểu công thức ) mới tư duy được.”
- Owner đã gật trong cùng tin: nối mục 1 với ba Chuỗi đã định nghĩa ở MMIM (D158 · CH-001/002/003 · SSOT VPS `ui/chuoi-data-v1.js`, Master Chuỗi ML-DEF-028) kèm định nghĩa tool; sửa lỗi gõ; thêm câu đích tổng; đưa “dễ nhìn với con người” thành mục tiêu; “xét nguyên tắc giao việc” là luật giao việc của MOT, không phải luật hội đồng AI.
- Owner 08/10/2026 07:30, nguyên văn: “Bô sung thêm thêm nôi dung này: […] => Đích: việc gì lặp lại cũng có quy trình chuẩn → người mới, phiên AI mới làm theo là ra đúng sản phẩm, hướng tơi muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể. Việc host tôi chỉ đinh sau, việc ban phải nhắc tôi tức là quy trình đang bắt đầu tốt dần rối đó” — đã lên ô 1 (D05; “tơi” ghi là “tới” theo phép sửa lỗi gõ Owner đã cho). Nối luật: AGENTS A10-R2.
- Owner 08/10/2026 10:41 (phiên Claude Chat), nguyên văn: “Tôi cho GPT chuyển các nội dung bên từ khu công thức trong repo đang làm lên và để codex thử đọc xem có làm theo được chưa? đây là ý kiến của codex. Ngoài ra tôi thấy việc trình bày quy trình đang hơi khó hiểu, phức tạp với con người, bạn xem xét trình bày lại và đảm bảo đẩy đủ từ phàn công thức của repo cũ để có thể tiếp tục việc này 1 cách liền mạch nhé.” Câu Owner hỏi Codex trong cùng ý kiến chuyển kèm (P08): “Xác nhận sau khi chuyển xong chúng ta xóa bớt ở phần công thức đi (1 SSOT cho đỡ nhầm lẫn)”. Áp: trang một khuôn dễ nhìn (ô 1 dòng 15); chép đủ khu cũ có phiên bản, rồi cắt chuyển một nơi sửa; thu khu cũ là sửa file task khác/VPS nên cần Owner duyệt riêng (D07).

#### TQT-LAYERS — ba lớp Owner yêu cầu
| Lớp | Dùng cho | Nội dung bắt buộc | Đích hoàn thành |
|---|---|---|---|
| for design | Thiết kế sáng tạo ban đầu: vẽ UI, lên danh sách, config… | Mục tiêu/sản phẩm thiết kế, đầu vào/ràng buộc; tập trung đầy đủ câu hỏi cần trả lời, các lựa chọn/nhánh và quyết định. | Thiết kế đáp ứng mục tiêu, các câu hỏi cần thiết đã xử lý; áp dụng chưa thành công thì bổ sung/sửa quy trình và kiểm lại. |
| for execute | Agent thực hiện công việc lặp lại. | Điều kiện bắt đầu, câu hỏi cần xác minh, thứ tự bước, nhánh xử lý khi mắc, đầu ra và nơi bàn giao. | Định nghĩa rõ thế nào hoàn thành, kiểm gì và bằng chứng nào chứng minh đã ra sản phẩm đúng. |
| for DOT/script | Thực hiện tự động bằng DOT/script. | Mục tiêu; điều kiện/trigger; input/output; hành vi thành công, thất bại; định nghĩa hoàn thành; DOT/script thực thi. | Có kết quả tự động kiểm chứng theo hợp đồng và đường xử lý lỗi. Áp AGENTS A10-R3/R4 khi triển khai, không chép lại luật nền. |

Ba chiều độc lập theo ô 1 dòng 2: **Chuỗi × nhóm chuyên môn × lớp** (Chuỗi = CH-001/002/003 của MMIM D158; trước 08/10 ghi là “phạm vi phục vụ”). Lên lớp theo ô 1 dòng 10–11: phần sẽ viết thành DOT thì DOT là trạng thái cuối, chạm Directus/PG bắt buộc DOT; phần còn lại ở design hoặc execute lâu dài là hợp lệ. Một quy trình có mã ổn định; dùng cho nhiều phạm vi thì liên kết/nhãn, không nhân bản nội dung. Không bắt buộc mọi quy trình phải có ngay đủ ba lớp. Tên nhóm/mẫu chi tiết tại trang nội dung là khung ghi nhận ban đầu để hội đồng hoàn thiện.

#### TQT-QUALITY — cách áp nguyên tắc “làm theo là phải xong”
- Xác định rõ ai làm, bắt đầu từ đâu, điều kiện áp dụng, sản phẩm cần tạo, nơi nhận và bằng chứng nhận được.
- Câu hỏi → đáp án/quyết định → bước/nhánh → sản phẩm → bằng chứng phải truy được về nhau. Người hoặc agent không cần tự đoán phần quy trình bỏ trống.
- Có đủ văn bản chỉ là đã soạn. Chỉ công nhận sẵn sàng trong phạm vi đã kiểm chứng; phần chưa phủ/chưa đo phải hiện rõ.
- Làm đúng mà vẫn mắc/sai: ghi tình huống thật, tìm câu/bước/đầu vào thiếu, sửa bản chuẩn, thêm ca kiểm và chạy lại. Phần đã đạt cũng cần được kiểm lại nếu bản sửa ảnh hưởng.
- Sửa ngay khi đủ căn cứ và đúng quyền/phạm vi; nếu chưa sửa thì ghi sổ trước khi kết thúc lượt. Sửa ngay vẫn để dấu vết. Chỉ đóng hồ sơ sau khi kiểm chứng đạt; lỗi tái diễn mở lại cùng mã.
- Hội đồng góp ý ở đúng task và đúng mã/phiên bản/câu/bước; Host ghi xử lý ý kiến và con trỏ bản sửa. Vai trò, vòng thảo luận và quyền giao việc theo AGENTS A2/A3/A5; không tạo quy chế hội đồng thứ hai.

#### TQT-SOURCES — nguồn đã có và ranh giới tiếp nhận
- Nguồn Owner chỉ: [Quy trình - Tools CTCM · Công thức](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=matrix-view-formula).
- Đã đọc `work/mow-mot-moit-mout/README.md#tools--ctcm--quy-trình-thiết-kế-và-kiểm-ui`, các mục Tools ngày 07/10 trong COLLAB nguồn và kiểm trang [Tools CTCM](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html) thật: có 9 mục TOOL-CTCM-001…009, đang là quy trình đề xuất/áp thử.
- Nội dung Tools hiện hành ở VPS, root `ui`, `definition-master-data-v1.js` → `ML-DEF-023`; renderer `tools-catalog-v1.js`. Không lấy trang chụp/copy làm bản chuẩn mới.
- Sổ MOW hiện hành: cùng dữ liệu trên, `TOOL-CTCM-001.pilot.issues`; kết quả từng lượt: `pilot.runs`. Trang mới liên kết tới sổ này, không chép trạng thái từng hồ sơ sang một sổ cạnh tranh. *(Cập nhật theo D07 · Owner 08/10 10:41: chép đủ sang `view.html` để làm liền mạch, ghi rõ phiên bản; sổ MOW vẫn là nơi sửa tới khi Host cắt chuyển, sau đó chỉ còn một sổ ở task này.)*
- Task mới là đầu mối tập hợp/chuẩn hóa quy trình tools cho cả ba phạm vi. Thiết kế sản phẩm MOW và lỗi của lượt MOW vẫn có nơi xử lý hiện hành; tiếp nhận/chuyển nguồn phải giữ mã, lịch sử, đường đọc và xác định một nguồn chuẩn trước khi chuyển.
- Các nguồn khác sẽ được kiểm kê trong phạm vi mục tiêu; chưa được coi danh mục 9 Tools CTCM là toàn bộ tài nguyên Incomex.
- Nhóm chuyên môn “xét nguyên tắc giao việc” thuộc MOT theo ô 1 dòng 6, phải đối chiếu nguồn MOT thật trước khi đặt câu/bước. AGENTS/root COLLAB chỉ là luật nền phối hợp AI, không được dùng thay nội dung chuyên môn của MOT.

#### TQT-REGISTER — sổ tổng hợp trước mắt
- **Sổ của task: `view.html#so-van-de`.** Sổ nằm ngay trong HTML chính trên repo để con người đọc cùng nguồn AI cập nhật; không có bản nhập localStorage hay sổ Markdown song song.
- Mỗi hồ sơ mới có mã `TQT-ISS-nnn`; hồ sơ ở task khác giữ mã gốc và liên kết tới sổ gốc, không tạo bản trạng thái thứ hai. TQT-ISS-001 ghi đúng khoảng trống Owner nêu. *(D07: OPEN-01…10 có bản chép ở `view.html#so-van-de`, chỉ để đọc tới khi cắt chuyển.)*
- Vòng đời cần quản lý: Ghi nhận → Phân loại → Giao xử lý → Đang xử lý → Chờ kiểm → Đóng; có nhánh Bị chặn / Để sau / Trùng / Mở lại. Chỉ ghi Đang xử lý khi đã có người nhận thật.
- Trường cần giữ: mã; ngày/nguồn phát hiện; quy trình/phiên bản/câu/bước; tình huống/bằng chứng; ảnh hưởng; người theo dõi; người xử lý; người kiểm; trạng thái; bước tiếp; mốc rà; lý do hoãn; tiêu chí đóng; bản sửa/kết quả kiểm; lịch sử.
- Host được chỉ định có trách nhiệm rà sổ đầu/cuối lượt và khi bàn giao; assignee sửa, verifier kiểm. Chưa có người nhận thì ghi “Chưa giao”, không bịa phân công.
- Khi ổn định mới thiết kế chuyển sang bảng PG riêng qua DOT; phải kiểm migration/mapping và chuyển nguồn một lần, giữ nguyên mã/lịch sử. Chưa tạo bảng hay tự bật nhắc việc nền trong lượt khởi tạo.

#### TQT-HOST-GATE — nộp đề xuất riêng, Host mới nhập chuẩn (D08/D09 · 08/10/2026; Host chuyển theo D19)
**Hiệu lực vai hiện tại (Owner 15/10, P63/P64):** các dòng phân công D19/GPT Host cũ dưới đây là lịch sử. Task còn Astra Codex Host nội dung, Claude Host Kiểm soát/Reviewer, GPT Chat được Owner giao Host chốt READY B1+B2 và rà nguồn P64; Gemini là ghế dự bị. Quyền thực thi theo AGENTS và Bảng ở đầu §0, không suy tự có RUN từ việc sửa văn bản.
- **Mục tiêu của Owner vẫn chỉ ở §0 ô 1–2**. Mục tiêu nghiệm thu của từng Tool: một phiên Codex/agent mới đọc, thực hiện thật, giao được sản phẩm đúng. Nếu không thể: báo rõ ca lỗi, câu hỏi/bước thiếu, bằng chứng, không tự báo ĐẠT. Một vài ca đạt không bằng cả hành trình đạt.
- **Nguồn chuẩn trong task này:** `view.html` (nội dung quy trình và sổ TQT), `COLLAB.md` (quyết định Host và trạng thái), `README.md` (cửa vào); chỉ Host GPT Chat (phiên Owner chỉ định 09/10, D19) áp sửa chính. Không nhân thêm sổ thứ hai, không chỉnh ô mục tiêu Owner.
- **Các AI ngoài phiên Host (Astra Codex, Claude, Codex khác, Claude Code…):** chỉ tạo một đề xuất **riêng** tại `work/tools-quy-trinh/proposals/TQT-PR-YYYYMMDD-<seat>-<so>.md` bằng gateway có expected-version/atomic transaction. Không sửa `view.html`, `COLLAB.md`, `README.md` và các hồ sơ TQT/OPEN được chép ở đó; không tự merge hoặc ghi “đã nhận”. Mỗi đề xuất khác mã/path, không cùng viết một file. Nếu worker thuộc task UI/MOW, bằng chứng thực hiện vẫn ghi ở task sản phẩm theo quyền task đó.
- **Khuôn đề xuất ngắn:** `Mã Tool hoặc issue · Đã thử và kết quả thật (PASS phạm vi nào / BLOCKED vì sao) · Câu/bước hiện thiếu hoặc sai · Đề xuất sửa cụ thể · Nguồn phiên bản + link bằng chứng`. Không được tự sửa mục tiêu, không mở task mới. Khi thấy vấn đề chưa sửa, AI nộp đề xuất; Host vào sổ chuẩn cùng mã sau duyệt.
- **Host duyệt:** đối chiếu mục tiêu + nguồn hiện hành + tác động tới Tool/sổ + bằng chứng kiểm, lấy phản biện Reviewer nếu cần; `ACCEPT`/ `REQUEST_CHANGES`/ `REJECT` ghi mã đề xuất vào P/D của COLLAB. Chỉ Host ghi cập nhật chính bằng **một transaction** với expected version/head; kiểm mirror và bàn giao đường đọc cho agent. Không ghi xanh khi mới chỉ thử một phần.
- **Chuyển nguồn cũ:** tới khi hoàn tất TQT-ISS-004, `ML-DEF-023`, 8/7 câu và `OPEN-01…10` tại MOW vẫn là nguồn sửa *legacy*; bản chép tại task chỉ để đọc có gắn phiên bản. Nội dung/sổ **mới của task** chỉ Host nhận qua proposals. Host phải hòa giải thay đổi legacy ngay trước khi tuyên bố chuyển một SSOT; không tự sửa mã/runtime VPS hay thu khu Công thức của task khác.
- **Cổng kỹ thuật còn thiếu:** đây là quy trình proposal/merge theo vai, **chưa phải branch protection cưỡng chế quyền Host**. Đã kiểm GitHub ruleset `23976991 gateway-only-writes` đang active cho mọi branch, chỉ DeployKey bypass; GitHub app không mở đường push branch chuẩn. Gateway hiện chưa có bằng chứng rule riêng khóa write của các AI không phải Host vào các path chính. TQT-ISS-006 tiếp tục mở để kiểm guard và phép thử từ chối ghi thật; không thay ruleset toàn repo.

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| Astra-Codex | OpenAI | Astra Codex — Owner giao lại trực tiếp D22 | Host | Cuộc trò chuyện hiện tại của Owner · đường gọi hội đồng CHƯA ĐO |
| Claude-review | Anthropic | Claude Chat | Reviewer | CHƯA ĐO |
| Gemini | Google | Gemini (identity `google-main`) | Council · dự bị, tham khảo | Owner chuyển tay khi cần; không gửi = ghế trống · không tính quorum · không ghi repo (Owner 15/10 16:53, 3.4) |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: —
**Ủy quyền B1+B2 theo Owner 15/10:** GPT Chat chốt PROMPT/READY của node B1+B2, không thay Host nội dung Astra-Codex; Claude-review (Anthropic) đã đồng thuận V12.6 và soạn PROMPT cuối commit c286349b. Chủ trương Q1/Q2/007 Owner phê duyệt trực tiếp; không cần mở thêm vòng lập luận kiến trúc. Executor = Claude Code CLI do Owner dán.

**Roster hiện hành D22:** Astra Codex giữ Host theo yêu cầu trực tiếp Owner; GPT Chat/Claude góp ý riêng, không ghi nguồn chính. Đường gọi Reviewer vẫn CHƯA ĐO; không giả định quorum hay cấp RUN. Lượt này rà và hiệu chỉnh nguồn thiết kế/Overview, chưa PG, chưa đổi công thức hoặc triển khai quy trình nghiệp vụ.

#### Vòng trước cũ (trước D25)
Chỉ đạo READ-ONLY P15/D16 và Host GPT Chat dưới đây là lịch sử trước khi Owner giao lại Astra Codex. Không dùng lịch sử này để ghi đè vai trò/phạm vi hiện hành ở đầu §0.

#### BẢNG ĐIỀU KHIỂN CŨ · cập nhật 2026-10-08 · GPT Chat · P15
- 🎯 Mục tiêu: Owner chốt 08/10 — “việc gì lặp lại cũng có quy trình chuẩn → người mới, phiên AI mới làm theo là ra đúng sản phẩm, hướng tới muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể.” Đủ 15 dòng đọc ở ô 1. Vì sao (Owner): “số quy trình sẽ rất nhiều => chúng ta sẽ tập hợp toàn bộ các tools quy trình lên 1 task để có thể làm việc xuyên suốt, dài hạn, hội đồng AI dễ dàng có ý kiến đóng góp.”
- 🏁 Xong khi: theo ô 2 — một quy trình đạt khi người mới hoặc phiên AI mới làm theo, không hỏi thêm, ra đúng sản phẩm thật. Mốc của cả việc do hội đồng chốt ở bước kế hoạch.
- 📍 Tiến độ: ■ Khởi tạo / chỉ định Host → □ Chuẩn hóa → □ Áp dụng, kiểm chứng → □ Mở rộng và cải tiến.
- ✅ Đã xong: mục tiêu Owner D04/D05; Host D06; 9 Tools nguồn P06, Rà một UI P09, Claude trình bày 6 phần P10; Host tiếp nhận P11. Theo D11/P12: có bản thử TQT-QT-001, mẫu phản hồi 5 loại blocker và README đọc ngay khi muốn sửa/bị chặn. Đây là tài liệu chuẩn bị thử, chưa có KQ người mới cho quy trình meta.
- ✅ P33: kiểm kê305DOT/34Tool, nối biên nhận và bản đồ dùng lại; bộ tổng VPS đạt. P34: bổ sung bộ nhớ cùng khuôn, hai duyệt có phiên; đi thử QT001 và ghi4chỗ vướng.
- ■ Đang làm: — · 0 RUN active. D15 ưu tiên kiểm kê bộ câu hỏi gốc Chuỗi/Tầng/Bước+Bước con; đã soạn đề bài Codex READ-ONLY P15, thử ghép MOW001 sau khi có đề xuất. DRAFT vẽ UI P14 đã SUPERSEDED; MOW002 chưa làm.
- ⬜ Còn lại: kiểm độc lập agent đọc rồi làm ra sản phẩm thật; phản biện và bổ sung bước/câu hỏi còn thiếu; thử đề xuất mini-PR; kiểm khóa kỹ thuật Host-only (TQT-ISS-006); chuyển một SSOT từ MOW có bằng chứng; nền chuẩn IT và mở rộng Chuỗi khác theo mục tiêu.
- ➡ Kế tiếp: Claude rà delta P51 và tự ghi phiếu CAT025; NEXT_TRIGGER=CLAUDE_P51_REVIEW_RECORDED. Codex đối chiếu; cả hai OK mới trình Owner. Không giữ RUN/lease chờ.
- ⛔ Không làm/để sau: tạo task không bao gồm triển khai DOT/script, bảng PG, đổi runtime/UI production hay chuyển dữ liệu đang dùng ở MOW.


Bản 08/10 07:16 của ô 1: câu Đích kết thúc ở “ra đúng sản phẩm.”; Owner thêm vế “hướng tới muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể” lúc 07:30 (D05). Các dòng khác không đổi.

#### Bản mục tiêu 07/10/2026 — Owner gõ gốc; đã thay bằng bản Owner duyệt 08/10 (D04). Giữ nguyên văn, kể cả lỗi gõ.
(07/10) Mục tiêu:
Owner nguyên văn 07/10/2026 — 6 mục tiêu chốt + 1 mục tiêu bổ sung. Giữ nguyên từng chữ, kể cả lỗi gõ; AI không rút gọn, không viết lại (AGENTS MT3 · DROOT51).

1. Quy trình hoá các tool Chế tạo cỗ máy, Vận hành cỗ máy, Cỗ máy sản xuất quy trình, có chia theo các nhóm nhỏ.
2. Nguyên tắc: Làm theo quy trình phải không sai => đạt được mục tiêu, ra được sản phẩm. Nếu vẫn mắc, hiệu chỉnh quy trình cho bằng đạt. (Tức làm theo quy trình là phải xong.
3. Quy trình phải liệt kê được tất cả các câu hỏi cần thiết để hoàn thiện (quá trình làm, hội đồng AI cho ý kiến để hiệu chỉnh, bổ sung liên tục cho đến khi hoàn thiện và ngày càng hoàn thiện hơn)
4. List các quy trình chia theo nhóm nhỏ các chuyên môn để cả con người dễ nhận diện, đánh giá và choi ý kiến. Ví dụ như: Thiết kế UI, config, xét các nguyên tăc giao việc...
5. tools-quy-trinh sẽ chia làm 3 nhóm/lớp:
   1. for design: Dành cho quá trình thiết kế sáng tạọ ban đầu như vẽ UI, lên danh sách, conffig....=> cần tập trung liệt kê đầy đủ các câu hỏi cần trả lời. Mục tiêu cuối làm theo quy trình là thiết kế thành công, chưa thành công => tiếp tục hiệu chỉnh quy trình
   2. for excecute: Danh cho các agent thực hiện lặp lại, tập trung vào các câu hỏi cần trả lời và thứ tự các bước cần thực hiện, định nghĩa rõ ràng thế nào là hoàn thành?
   3. for DOT/scrip. Định nghĩa rõ mục tiêu, thế nào là hoàn thành, điều kiện/trigger thực hiện và viết DOT/Scrip để thực hiện tự động
6. Những phát hiện sai xót, nếu chưa sửa ngay thì cần ghi lại vào 1 sổ tổng hợp, có theo dõi tiến trình/vòng đời của vấn đề đến khi xong. (khi ổn đinh, sổ này sẽ ghi trong PG table riêng, trước mắt có thể để sổ trên repo/vps.
7. Mục tiêu bổ sung (Owner 07/10/2026 22:15): Các chuẩn mực này được ứng dụng các chuẩn mực tốt nhất của ngày [ngành] IT làm nền cơ bản. Sau đó mới bổ sung các phần riêng của incomex.

Bối cảnh — Owner nguyên văn: “Hiện tại đã bắt đầu phác thảo 1 phần nhỏ tại: Quy trình - "Tools CTCM · Các bước phải làm và câu hỏi phải trả lời" … Các nội đã phác thảo là những bước đầu tiên nhưng còn chưa sẵn sàng trên diện rộng. => Cần thiết kế chuẩn mực hơn, dễ nhìn hơn với con người => Vì số quy trình sẽ rất nhiều => chúng ta sẽ tập hợp toàn bộ các tools quy trình lên 1 task để có thể làm việc xuyên suốt, dài hạn, hội đồng AI dễ dàng có ý kiến đóng góp.”

(07/10) Thế nào là hoàn thành:
Owner nguyên văn (mục tiêu 2): “Làm theo quy trình phải không sai => đạt được mục tiêu, ra được sản phẩm. Nếu vẫn mắc, hiệu chỉnh quy trình cho bằng đạt. (Tức làm theo quy trình là phải xong.”
(đề xuất — hội đồng chốt ở bước kế hoạch theo AGENTS A5; Owner sửa lúc nào cũng được)
Một: có một danh mục duy nhất liệt kê mọi quy trình tools theo ba cỗ máy và theo nhóm chuyên môn; người nhìn nửa phút biết đã có gì, thiếu gì, tắc ở đâu.
Hai: mỗi quy trình ghi rõ thuộc lớp nào trong ba lớp và có đủ phần bắt buộc của lớp đó như Owner nêu ở mục 5.
Ba: một quy trình chỉ được ghi là đạt khi một người hoặc agent chưa biết việc làm đúng theo nó, không phải hỏi thêm, ra được sản phẩm thật. Chưa ra thì sửa quy trình, thêm câu hỏi còn thiếu rồi chạy lại.
Bốn: sai sót chưa sửa ngay đều nằm trong một sổ, có người lo và có trạng thái, theo tới khi đóng.
Năm: mỗi chuẩn và mỗi mẫu ghi rõ nền là chuẩn nào của ngành IT, phần nào Incomex thêm và vì sao.

Trước 07/10: chưa có vòng nào; task tạo lần đầu theo lệnh Owner 07/10/2026.

## Cửa vào và nguồn chuẩn
- Tên việc: xem dòng ngay dưới tiêu đề file.
- Task-id: `tools-quy-trinh` · thư mục: `work/tools-quy-trinh/`.
- HTML chính: `view.html`.
- Owner View: https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh
- AI vào việc: `AGENTS.md` → §0/Bảng trên → `README.md` → đúng mục nguồn/quy trình/sổ cần xử lý.
- Mục tiêu/tiêu chí/trạng thái chỉ ở §0; trang Owner rút tự động. `view.html` giữ danh mục nguồn, cấu trúc tra cứu, sổ vấn đề và hướng dẫn góp ý, không chép mục tiêu/trạng thái điều hành.

## Quyết định Owner
- **D01 · 2026-10-07 · EFFECTIVE:** tạo đúng task `tools-quy-trinh`; toàn bộ 6 yêu cầu được ghi tại TQT-REQ; nguồn xuất phát là Tools CTCM Owner dẫn. Phạm vi lượt hiện tại là tạo đầu mối công việc, chưa phải lệnh chạy toàn bộ chương trình.
- HUMAN_DIRECTIVE@TQT-CREATE-20261007 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/ · step=khởi tạo · recorded_by=OpenAI-main · quote="tạo cho tôi một task: tools-quy-trinh trên incomex workspace repo." · text=Tạo task và ghi đầy đủ mục tiêu/chi tiết Owner giao trong cùng tin nhắn. · audit=Tin nhắn trực tiếp Owner tại phiên tạo task, 2026-10-07; commit khởi tạo.
- **D02 · 2026-10-07 22:15 · EFFECTIVE:** Owner chốt mục tiêu — 6 mục đã liệt kê là mục tiêu chốt, cộng một mục tiêu bổ sung (nền là chuẩn tốt nhất của ngành IT, sau đó mới thêm phần riêng Incomex). Ô 1 chép đủ, nguyên văn; TQT-REQ chỉ là bảng kiểm trỏ về ô 1 (thay câu “toàn bộ 6 yêu cầu được ghi tại TQT-REQ” của D01). Phần còn lại các AI bàn với nhau trên repo. Áp: SAME_COMMIT.
- HUMAN_DIRECTIVE@TQT-GOALS-20261007 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/ §0 + mục tiêu bổ sung · step=chốt mục tiêu · recorded_by=Claude-review · quote="Đây là yêu cầu của tôi. Nguyên tắc AI phải đưa rõ ràng các mục tiêu user chốt lên. Đằng này GPT lại không đưa lên. bạn rà soát và sửa lại, coi các mục tiêu tôi đã liệt ở đây là mục tiêu chốt. Phải đưa lên để các AI hiểu. từ đó các bạn muốn viết gì thì bàn với nhau. Tôi chỉ bổ sung thêm 1 ý nữa (mục tiêu bổ sung): Các chuẩn mực này được ứng dụng các chuẩn mực tốt nhất của ngày IT làm nền cơ bản. Sau đó mới bổ sung các phần riêng của incomex. Bạn xem xét lại và sửa đổi thêm giúp tôi nhé. GPT rõ ràng không đọc hết luật của repo" · text=Đưa đủ các mục tiêu Owner đã chốt lên ô 1 nguyên văn; thêm mục tiêu bổ sung về chuẩn ngành IT; rà và sửa các chỗ P01 lệch luật repo. · audit=Tin nhắn trực tiếp Owner tại phiên Claude Chat, 2026-10-07 22:15 +07; commit P02.
- **D03 · 2026-10-08 05:44 · EFFECTIVE:** Owner yêu cầu viết lại ô 1 thành gạch đầu dòng ngắn, kiểu công thức, không sai ý; Claude soạn trong chat, **Owner sửa/duyệt xong mới thành lời Owner và đưa lên ô 1**. Các làm rõ về ba lớp, ranh giới, sổ/PG: nguyên văn ở TQT-DIR.
- HUMAN_DIRECTIVE@TQT-REWRITE-20261008 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/ §0 ô 1–2 · step=chốt mục tiêu · recorded_by=Claude-review · quote="Nếu có thể, bạn hãy viết lại phần chỉ đạo của user trước. Tôi sửa/duyệt xong thì coi như đó thành lời User đưa lên. […] => Viết lại toàn bộ dưới chat phần mục tiêu giúp tôi. Ok hãy đưa lên nhé." · text=Viết lại ô mục tiêu ngắn, kiểu công thức; chỉ đưa lên repo sau khi Owner sửa/duyệt. · audit=Tin nhắn trực tiếp Owner tại phiên Claude Chat, 2026-10-08 05:44 +07; nguyên văn đầy đủ ở TQT-DIR.
- **D04 · 2026-10-08 07:16 · EFFECTIVE:** Owner duyệt bản viết lại mục tiêu, sửa một dòng (“Sai sót hoặc thiếu mà chưa sửa ngay”) ⇒ ô 1–2 hiện hành là bản này và là lời Owner: “Đây là Mục tiêu user chốt => cần làm theo và đạt mục tiêu.” Bản 07/10 giữ nguyên văn ở Vòng trước (thay phần “ô 1 chép 6 + 1 mục” của D02). Áp: SAME_COMMIT.
- HUMAN_DIRECTIVE@TQT-GOALS-20261008 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/ §0 ô 1–2 · step=chốt mục tiêu · recorded_by=Claude-review · quote="Ok bạn đưa lên thay phần này cho mục tiêu từ Owner. Có sửa thêm chút. […] Sai xót hoặc thiếu mà chưa sửa ngay -> […] Còn lại đồng ý cách viết và nôi dung của bạn => bạn đưa lên repo giúp tôi nhé. Đây là Mục tiêu user chốt => cần làm theo và đạt mục tiêu." · text=Đưa bản viết lại lên ô 1–2 thành lời Owner; sửa dòng 13 theo chữ Owner. · audit=Tin nhắn trực tiếp Owner tại phiên Claude Chat, 2026-10-08 07:16 +07; commit P04; nguyên văn đầy đủ ở TQT-DIR.
- **D05 · 2026-10-08 07:30 · EFFECTIVE:** Owner bổ sung câu Đích ở ô 1: thêm vế “hướng tới muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể”. Về Host: “Việc host tôi chỉ đinh sau” — AI không nhắc lại Q01, Owner sẽ chủ động. Nguyên văn ở TQT-DIR. Áp: SAME_COMMIT.
- HUMAN_DIRECTIVE@TQT-DICH-20261008 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/ §0 ô 1 câu Đích · step=chốt mục tiêu · recorded_by=Claude-review · quote="Đích: việc gì lặp lại cũng có quy trình chuẩn → người mới, phiên AI mới làm theo là ra đúng sản phẩm, hướng tơi muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể." · text=Thêm vế cuối vào câu Đích của ô 1. · audit=Tin nhắn trực tiếp Owner tại phiên Claude Chat, 2026-10-08 07:30 +07; commit P05.

- **D06 · 2026-10-08 09:19 +07 · EFFECTIVE:** Owner chỉ định GPT Chat (OpenAI-main) là Host của `tools-quy-trinh`, đồng thời giao rà nội dung liên quan và đưa bộ quy trình từ Tools CTCM tại `mow-mot-moit-mout` vào trang nội dung task, phân loại đúng/dễ nhìn. Chỉ tiếp nhận và biên tập tài liệu task; không tự thay đổi SSOT runtime/MOW, chưa công nhận các quy trình đã nghiệm thu.
- HUMAN_DIRECTIVE@TQT-HOST-IMPORT-20261008 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/{COLLAB.md,view.html,README.md} · step=tiếp nhận quy trình CTCM · recorded_by=OpenAI-main · quote="Tôi chỉ đỉnh bạn làm host" · text=Host GPT Chat; đối chiếu mục tiêu mới và đưa quy trình CTCM lên nội dung task, phân loại dễ nhìn · audit=Tin nhắn trực tiếp Owner tại phiên GPT Chat 08/10/2026 09:19 +07; commit D06.
- **D07 · 2026-10-08 10:41 +07 · EFFECTIVE:** Owner giao Claude Chat (Reviewer) trình bày lại trang quy trình cho dễ hiểu với con người và chép đủ nội dung khu Công thức cũ để làm tiếp liền mạch (nguyên văn ở TQT-DIR). Phạm vi: tài liệu task; không sửa nguồn cũ/VPS. Thu gọn khu cũ (Owner đã nêu: “sau khi chuyển xong … xóa bớt ở phần công thức”) là sửa file task khác/VPS ⇒ Host trình, Owner duyệt riêng. Áp: P10.
- HUMAN_DIRECTIVE@TQT-VIEW-20261008 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/{view.html,README.md,COLLAB.md} · step=chuẩn hóa trình bày + chuyển nguồn · recorded_by=Claude-review · quote="Ngoài ra tôi thấy việc trình bày quy trình đang hơi khó hiểu, phức tạp với con người, bạn xem xét trình bày lại và đảm bảo đẩy đủ từ phàn công thức của repo cũ để có thể tiếp tục việc này 1 cách liền mạch nhé." · text=Trình bày lại view.html một khuôn dễ nhìn; chép đủ khu Công thức cũ kèm phiên bản; không sửa nguồn cũ. · audit=Tin nhắn trực tiếp Owner tại phiên Claude Chat, 2026-10-08 10:41 +07; commits P10.

- **D08 · 2026-10-08 11:45 +07 · EFFECTIVE · chỉ đạo Owner:** Owner giữ đúng hai thứ: (1) mục tiêu đã duyệt, (2) agent đọc và làm ra kết quả thật/đặt câu hỏi khi không làm được. Owner giao GPT Chat làm Host điều hành dài hạn, **mọi AI khác chỉ được đề xuất, Host duyệt rồi mới đưa vào nguồn chuẩn**, đặc biệt đối với sổ theo dõi; không yêu cầu Owner đọc nghiệp vụ nội bộ. Áp riêng `tools-quy-trinh`; ghi quy trình tại TQT-HOST-GATE, không sửa chữ §0 ô 1–2.
- HUMAN_DIRECTIVE@TQT-PROPOSAL-ONLY-20261008 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/ · step=quản trị thay đổi và chạy thực tế · recorded_by=OpenAI-main · quote="Nghĩa là các AI khác ngoài host chỉ được đề xuất, Host duyệt rồi mới cho vào." · text=Host duy nhất quyết nhận vào tài liệu/sổ chính; agent khác gửi đề xuất có bằng chứng · audit=Tin nhắn Owner trực tiếp ở GPT Chat 08/10/2026 11:45 +07.

- **D11 · 2026-10-08 · EFFECTIVE · Owner tham gia trực tiếp:** Owner đặt tên quy trình tiêu biểu `TQT-QT-001 · Quy trình hiệu chỉnh hướng dẫn và quy trình`, yêu cầu nổi bật đầu trang Nội dung công việc; mục đích: lấy phản hồi người làm (Codex) → bổ sung hướng dẫn → agent mới thử lại, lặp đến khi đọc và làm được. Owner tham gia trực tiếp phát triển **quy trình này**, Host điều hành và ghi giúp; không chuyển nhiệm vụ đọc/trông sổ kỹ thuật cho Owner.
- HUMAN_DIRECTIVE@TQT-FEEDBACK-LOOP-20261008 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/{README.md,view.html,COLLAB.md} · step=hiệu chỉnh có thử lại · recorded_by=OpenAI-main · quote="Quy trình hiệu chỉnh hướng dẫn và quy trình" · text=Ưu tiên quy trình mẫu tự hiệu chỉnh, Owner trực tiếp tham gia; AI bị chặn phải được dẫn về README; trở lại vòng Codex phản hồi và thử lại · audit=Tin nhắn Owner trong GPT Chat, 08/10/2026 (sau P11).

- **D14 · 2026-10-08 · EFFECTIVE · Owner giao kiểm nghiệm thiết kế UI theo công thức:** Giữ SSOT công thức CT-005/005.1 và các Master hiện có; bất cứ đối tượng có ≥2 trong hệ thống cần Master List, bổ sung dần. Công việc thực tế tiếp theo là (1) hoàn thiện quy trình vẽ UI cho `MOW-NHC-001` (3 MOT) và chính thiết kế UI theo quy trình đó; (2) sau đó đưa cho một Codex mới vẽ thử UI `MOW-NHC-002` (2 MOT) để kiểm chứng quy trình có thể làm theo mà không cần chat giải thích. Mục tiêu chính vẫn §0 Owner chốt, không chuyển sang thiết kế lại công thức/master hay nghiên cứu ngoại lệ 2% lúc này. Kế hoạch Host P14 và prompt DRAFT; chưa mutation/READY/RUN.
- HUMAN_DIRECTIVE@TQT-MOW001-002-20261008 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/ + thử nghiệm UI trong work/mow-mot-moit-mout/ui root theo quyền task MOW · step=đặt ca thử UI áp quy trình · recorded_by=OpenAI-main · quote="hoàn thiện nốt quy trình vẽ UI cho Mow 001" / "Sau đó cho vẽ thử UI cho MOW 002" · text=đúc kết quy trình UI từ 001, kiểm bằng 002; AI sửa tools qua proposal/Host duyệt · audit=Tin nhắn Owner trực tiếp GPT Chat 08/10/2026.

- **D15 · 2026-10-08 · EFFECTIVE · Owner đổi thứ tự ưu tiên nhưng chưa duyệt đổi công thức:** Ba nguyên liệu gốc là Bước (bao gồm Bước con), Tầng, Chuỗi. Phải đặt bộ câu hỏi bắt buộc riêng cho Bước lớn/Bước con, Tầng, Chuỗi trước; rồi ghép để hình thành MOW/MOT; sau ghép thêm câu hỏi nghiệp vụ thiết kế UI, Config. Thêm Bước con phải có bộ câu hỏi tương ứng; làm xong từng chuyện nhỏ rồi thử ghép, chỉ rõ lỗi thừa/thiếu/xung đột từ nguồn. Owner giao Codex tổ chức đề xuất trước, không chỉ đạo ngay mutation CT/ML/UI. MOW001 vẫn là ca thử; MOW002 giữ nguyên cho đến khi quy trình hoàn thiện.
- HUMAN_DIRECTIVE@TQT-ROOT-QUESTIONS-20261008 EFFECTIVE · task=tools-quy-trinh · scope=kiểm kê/đề xuất câu hỏi CT-001, CT-002, CT-002.1 và thử ghép; không mutation nguồn công thức/ML/UI · step=soạn bộ câu hỏi gốc trước vẽ UI · recorded_by=OpenAI-main · quote="chúng ta đưa ra bộ câu hỏi trước, thêm bước con => thêm bộ câu hỏi" · text=Codex tổ chức đề xuất câu hỏi riêng từng nguồn, ghép trước khi thiết kế UI/Config; ưu tiên MOW001, tạm dừng MOW002 · audit=Owner trực tiếp tại GPT Chat ngày 08/10/2026.

## Quyết định Host
- **D09 · 2026-10-08 · EFFECTIVE · không đụng luật toàn repo:** thực hiện mini-PR trong task bằng `proposals/TQT-PR-...` độc lập. Host là người duy nhất nhập vào `view.html`/sổ/`COLLAB.md`/`README.md` sau duyệt và kiểm đầu ra, với một transaction; lời đề xuất hoặc commit proposals không thay SSOT. Chưa sử dụng GitHub branch/PR chuẩn vì ruleset `gateway-only-writes` active với mọi branch và chỉ DeployKey bypass; chưa có host-only gateway guard đã kiểm. Giữ TQT-ISS-006 mở, không tuyên bố enforcement đã đạt.
- **D10 · 2026-10-08 · EFFECTIVE · nghiệm thu có phạm vi:** P08 chỉ ra nội dung nguồn còn thiếu; P09 có 18 quan sát, 3 ca viết độc lập và 5 ca kiểm lại trong phạm vi nhưng chưa đạt hành trình thật; P10 bố cục 6 phần và chép đủ theo phiên nguồn, chưa kiểm độc lập toàn quy trình. Host nhận phần đã có chứng cứ; **không** chứng nhận 10/10 đạt hoặc cắt nguồn OPEN/MOW khi chưa kiểm đầu cuối. Sổ legacy OPEN giữ nơi sửa MOW; kết quả sản phẩm UI nằm task UI; task TQT nhận đề xuất và quản quy trình.

- **D12 · 2026-10-08 · ACTIVE DRAFT, chưa nghiệm thu:** đặt `TQT-QT-001` ở vị trí nổi bật đầu `view.html` với năm bước: xác định đầu ra → agent mới làm → lấy feedback có bằng chứng/phân loại → Host duyệt và sửa một nguồn → agent mới thử lại từ đầu. Kết quả đạt khi có sản phẩm thật độc lập; thiếu sản phẩm/quyền/quyết định thì ghi BLOCKED đúng loại, không tô PASS; quy trình này cũng phải tự qua chu kỳ thử. Chủ ý không tăng số 10 Tools nguồn vì đây là quy trình mẫu đang xây dựng.
- **D13 · 2026-10-08 · ROUTING READ-ME-FIRST:** hướng dẫn fail-closed đặt ở **đầu README**. Khi AI không phải Host muốn sửa hoặc ghi bị từ chối → đọc README, không retry main, tạo proposal `TQT-PR-...` theo đúng nguồn. `HOST_APPROVAL_REQUIRED + readme_path` chỉ là **contract phản hồi gateway cần triển khai/kiểm chứng**, chưa có thực thi; TQT-ISS-006 mở. Không được nói các AI đã bị khóa kỹ thuật.

- **D16 · 2026-10-08 · HOST DRAFT / REORDER:** P14 và `PROMPT.md` vẽ UI001→002 cũ bị **SUPERSEDED TRƯỚC READY/RUN**, giữ nguyên trong Git history. `PROMPT.md` hiện hành dành cho Codex **READ-ONLY REVIEW**, không cấp READY/RUN sửa công thức, Master hay UI. Khuôn Q_ID, OWNER_LEVEL, SOURCE, ANSWER, CHECK và GAP chỉ là đề xuất chờ Codex/Reviewer kiểm. 3 nguyên liệu/4 cấp đọc; ghép theo CT003/004/005/005.1; overlay chuyên môn UI/Config, không nhân câu ở mọi MOW/MOT.
- Cổng tiếp: Codex nộp proposal riêng hoặc toàn văn trong chat → Host so nguồn và mời Reviewer → quyết tiếp nhận theo đúng thẩm quyền; thay nghĩa gốc/công thức phải qua Owner và Host MOW trước mutation. Chưa sửa 1.4 hay đổi CT; MOW002 không mở.

- **D17 · 08/10/2026 · HUMAN_DIRECTIVE:** Owner: “Bạn là host của task này đi. Các ý kiến khác không được ghi thẳng, bạn xem xét có đồng ý bổ sung thêm không rồi mới bổ sung.” Astra Codex là Host hiện hành; giữ D06/D16 làm lịch sử.
- **D18 · 09/10/2026 · HUMAN_DIRECTIVE:** Owner yêu cầu Master riêng có tên/mã cho quy trình tổng hợp, theo UI cha và đồng thời có trong tools-quy-trinh khi dưới10; định nghĩa tổng hợp nhỏ hơn chuyên môn, T2.5 bàn sau. Thực hiện trong P16; không tự áp mục tiêu ngắn PR-07.
- **D19 · 09/10/2026 · HUMAN_DIRECTIVE · HIỆU LỰC:** Owner chỉ định lại GPT Chat làm Host của `tools-quy-trinh`, yêu cầu tab đầu tiên tên chính xác `Over view`, đứng trước `List quy trình tổng hợp`. Tab trình bày quan hệ **4 Quy trình tổng hợp** ↔ **12 Quy trình thành phần**, mã nhỏ và mờ cạnh tên, từ ngữ nhất quán để Owner nhìn là hiểu. Không đổi mã, công thức, danh mục, workflow hoặc runtime; Host Codex theo D17 là lịch sử, không còn quyền Host hiện hành.
- HUMAN_DIRECTIVE@TQT-OVERVIEW-HOST-20261009 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/{view.html,COLLAB.md,README.md,PROMPT.md} · step=Host và trình bày Over view · recorded_by=OpenAI-main/GPT Chat · quote="bạn lập giúp tôi 1 tab đầu tiên. (bạn được làm host) trước cả List quy trình tổng hợp tên tab là: Over view" · text=Giao GPT Chat làm Host, dựng sơ đồ quan hệ 4 Quy trình tổng hợp / 12 Quy trình thành phần nhất quán, giữ nguồn chuẩn · audit=Tin nhắn trực tiếp Owner trong GPT Chat 09/10/2026.

- **D20 · 09/10/2026 · HUMAN_DIRECTIVE · HIỆU LỰC:** Owner yêu cầu số vòng của 4 Quy trình tổng hợp lớn hơn, Quy trình thành phần hiển thị **STT đầu tiên**, và chuyển nội dung của **hai ảnh tổng quan Owner gửi** thành **hai bố cục HTML đặt phía dưới Over view**, chủ yếu mô tả những gì đã có, không tạo ảnh. Host chỉ chỉnh phần trình bày; mã/danh mục/luật không đổi.
- HUMAN_DIRECTIVE@TQT-OVERVIEW-HTML-20261009 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/{view.html,README.md,COLLAB.md} · step=Over view · recorded_by=OpenAI-main/GPT Chat · quote="Các vòng số hơi nhỏ , cho to ra 1 chút (của quy trình tổng hợp) / Quy trình thành phần chốt đầu tiên cho tôi STT / Cho tôi cả các hình này xuống bên dưới ... bạn tạo ra dạng HTML cho nhẹ." · text=Tăng vòng số; STT 1–12; 2 sơ đồ HTML bên dưới, không làm ảnh; chỉ mô tả nguồn hiện có · audit=Owner trực tiếp tại GPT Chat ngày 09/10/2026.

- **D28 · 13/10/2026 16:21 +07 · HUMAN_DIRECTIVE · HIỆU LỰC:** Owner giữ hướng dựng mô hình ngoài PG để hiệu chỉnh trước (đưa vào PG khi còn đổi liên tục tạo việc thừa và lỗi tiềm ẩn). Hai điều phải giữ: mọi AI làm chung một nơi trên GitHub; Owner nhìn được view, UI cuối đơn giản. Yêu cầu: cấu trúc tối ưu hơn, tận dụng MacBook; quy định ngắn gọn để AI đọc và tuân thủ (Codex đang vi phạm liên tục); thống nhất mục tiêu bổ sung và việc bổ sung. Ô 3: R25–R28; nguyên văn 3.4. Đề xuất: PR-22, Q03. Áp: SAME_COMMIT.
- HUMAN_DIRECTIVE@TQT-SCALE-20261013 EFFECTIVE · task=tools-quy-trinh · scope=cách lưu/ghi dữ liệu thử ngoài PG, vai GitHub/MacBook/VPS, luật cho AI · step=thiết kế cấu trúc · recorded_by=Claude-review · quote="Hai thứ cần giữ là: 1. Tất cả ai vẫn làm việc chung 1 nơi trên Github ... 2. User cần nhìn được view" · text=Ngoài PG trước; GitHub chung; Owner xem view; tận dụng MacBook; luật ngắn. · audit=Tin nhắn trực tiếp Owner tại phiên Claude 13/10/2026 16:21 +07; nguyên văn ở ô 3 mục 3.4.
- **D27 · 11/10/2026 18:02 +07 · HUMAN_DIRECTIVE · HIỆU LỰC:** Owner chốt cách đi tới PG: ① thiết kế hệ thống đúng → ② chạy thử một số ca để hiệu chỉnh thiết kế, bổ sung cột (làm tay được) → ③ chạy ổn mới rà và đưa vào PG một lần, vì sửa PG tốn hơn rất nhiều. Bác PR-12 v1 A1 (dùng bảng PG ngay làm nơi ghi). Khi chạy thử, nơi ghi là kho thử ngoài PG (R04a); bảng PG đang chạy chỉ dùng chọn đích ở ③ (R18). Ô 3: R04a, R09, R18; nguyên văn ở 3.4. Owner chưa chuyển PR-12 cho Codex; Host nội dung xét PR-12 v2. Áp: SAME_COMMIT.
- HUMAN_DIRECTIVE@TQT-PG-ONCE-20261011 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/ (nơi ghi khi chạy thử, đường vào PG) · step=thiết kế → chạy thử → vào PG · recorded_by=Claude-review · quote="thiết kế hệ thống đúng ... Sau khi chạy ổn, mới rà soát đưa vào PG 1 lần" · text=Chạy thử ngoài PG, ổn mới vào PG một lần; bác A1. · audit=Tin nhắn trực tiếp Owner tại phiên Claude 11/10/2026 18:02 +07; nguyên văn ở ô 3 mục 3.4.
- **D25 · 10/10/2026 07:38 +07 · HUMAN_DIRECTIVE · HIỆU LỰC:** Owner viết lại ô 1 còn 3 ý: cỗ máy sản xuất quy trình (ý tưởng → quy trình chạy được, tự động tối đa) · mọi thứ là quy trình, từ 2 trở lên có Master List · nhìn là hiểu. Mọi chi tiết khác chuyển xuống ô 3, có cấu trúc để AI đọc không sót. Owner giao Claude làm Host phần Kiểm soát (Bảng điều khiển, ô 1 Mục tiêu, ô 2 Thế nào là hoàn thành, ô 3 Chi tiết cần đạt); Astra Codex giữ Host nội dung theo D22. Về khuôn chung cho mọi việc (cùng chỉ đạo, Host nội dung đã làm ở D24): Host Kiểm soát xác nhận dùng MOW-TH-005@1.1, không thêm TH-06; yêu cầu và chỗ còn thiếu ghi ở ô 3 R01–R04, R11. Ô 1–2 cũ, 8 khối bổ sung và ô 3 cũ giữ nguyên văn ở Vòng trước. Áp: SAME_COMMIT.
- HUMAN_DIRECTIVE@TQT-GOAL-HOST-20261010 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/COLLAB.md §0 (Bảng, ô 1–3) · step=chốt mục tiêu + kiểm soát · recorded_by=Claude-review · quote="Bạn được làm host phần kiểm soát/mục tiêu/ thế nào là hoàn thành/ chi tiết cần đạt.. => diễn đạt lai giúp tôi để mục tiêu ngắn gọn, và các chi tiết không thiếu nhưng có cấu trúc tốt nhé. AI đọc không xót." · text=Ô 1 = 3 ý Owner viết; chi tiết vào ô 3; Claude giữ §0, Astra Codex giữ nội dung. · audit=Tin nhắn trực tiếp Owner tại phiên Claude Chat 10/10/2026 07:38 +07; nguyên văn đầy đủ ở ô 3 mục 3.4.
- **D24 · 10/10/2026 · HUMAN_DIRECTIVE + HOST_DECISION:** Owner yêu cầu khuôn chung cho bất cứ việc lớn/nhỏ. Host nâng cấp MOW-TH-005@1.1-design (không thêm 006 trùng vai), 13 mục khai báo cùng phiếu hiện hữu; xác nhận đủ trước S3, kiểm hai đầu nối, duyệt đúng phạm vi và ACK mới đóng. Tiếp nhận PR08: sửa chỉ dẫn Host, mẫu MOW001/G1, trường issue không ép lỗi giả, kiểm nhánh/trường bắt buộc/nguồn, 003 có bước công bố. Mục tiêu tự chạy là đích kiến trúc, chưa là năng lực đã nghiệm thu. Nguồn Host duy nhất ở §0; nguồn hướng dẫn ở tools-quy-trinh, hồ sơ sản phẩm tại nguồn gốc.
- **D23 · 09/10/2026 · HUMAN_DIRECTIVE + HOST_DECISION · HIỆU LỰC:** Owner yêu cầu Host sửa nốt, tự quyết ⑤ để quay lại thử quy trình/UI. Host chốt MOW-TH-005@1.0-design, CH-001 CTCM, dùng cho một lượt chọn–thực hiện–kiểm–bàn giao; mọi sai/thiếu có người nhận hoặc kết thúc hợp lệ. Cho áp thử thiết kế, không duyệt runtime/PG. Thay phần chờ Owner duyệt ⑤ của D21/D22/P21. Chốt hướng dẫn ở tools-quy-trinh; bản Tool cũ là lịch sử, hồ sơ sản phẩm chưa di chuyển. Mục tiêu 15 ý Owner giữ nguyên.
- **D22 · 09/10/2026 · HUMAN_DIRECTIVE · HIỆU LỰC:** Owner giao: “Bạn cầm lại cờ host và tiếp tục nhé.” Rà Overview, 005, quan hệ chéo và quản lý mọi trình tự/hướng dẫn bằng MOW/MOT trước áp thử. Astra Codex nhận lại Host, thay D19; không tự coi Owner đã duyệt 005 hoặc quyền PG.

- **D21 · 09/10/2026 · HUMAN_DIRECTIVE · HIỆU LỰC:** Owner yêu cầu **một nơi duy nhất viết chú giải ngắn cho mọi quy trình** để người/AI cùng đọc mà không tạo rác tài liệu. Đồng thời Owner yêu cầu chấm dứt "Luồng làm việc chung" trôi nổi, một hướng dẫn thực hiện bắt buộc phải có quy trình sở hữu. Host chốt đưa 6 thao tác vào **dự thảo Quy trình tổng hợp MOW-TH-005 · Áp dụng một quy trình từ chọn đến bàn giao**, với nhánh ĐẠT/CHƯA ĐẠT và điều kiện xong, giữ quy trình hiện có CHUNG.APQUYTRINH là cổng đầu vào, không coi đó là toàn hành trình. Đây là **bản thiết kế đề xuất**, chưa phải Owner phê duyệt phạm vi/quy trình ⑤; 4 mã trước và 12 thành phần không thay.
- HUMAN_DIRECTIVE@TQT-GUIDE-AND-FLOW-20261009 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/{view.html,README.md,COLLAB.md} · step=hiệu chỉnh Over view và phân loại quy trình · recorded_by=OpenAI-main/GPT Chat · quote="thiết kế 1 nơi để viết chú giải và đưa luôn vào đó ... luồng làm việc đó cuối cùng đưa vào đâu?" · text=Chú giải ngắn một nguồn, luồng có quy trình sở hữu, không chạy khi chưa phê duyệt · audit=Owner trực tiếp GPT Chat ngày 09/10/2026.
 
## Owner cần quyết
- Q03 · 13/10 · Cấu trúc dữ liệu cho 1.000 việc + luật 1 trang (PR-22). Đề xuất: gật → ngay từ nay không nhúng thêm dữ liệu việc vào view.html, không chép định nghĩa (V0); Codex làm phép thử PT-01 có số đo (MacBook + repo, không PG, không đổi VPS); dữ liệu cho máy chia theo việc như từng dòng trong bảng, tài liệu cho người vẫn 1 trang.
- — Q02 · ĐÃ GIẢI QUYẾT D23: Owner giao Host quyết ⑤; Astra Codex chốt 1.0-design/CH-001 cho áp thử thiết kế. Không chờ phê duyệt riêng; chưa quyền PG.
- — Q01 · ĐÃ GIẢI QUYẾT D22/D25: Astra Codex là Host nội dung; Claude là Host Kiểm soát (Bảng, ô 1–3). Mục tiêu ngắn: Owner tự viết ô 1 ngày 10/10 (D25), đã áp; PR-07 đóng. Không có câu hỏi Owner đang mở.

## Ý kiến và bằng chứng
### P40 · Astra Codex · QTTH006 theo thứ tự và cùng hồ sơ · 13/10/2026
- Ghế: Astra-Codex · Host nội dung · Bước/vòng: rà + ghép theo chỉ đạo trực tiếp · 1/1. Based_on: P39, PR20/PR21, MOW-TH-006@0.2, catalog và G1 P37/P38. Bảng: ghi RUN riêng, không mở lại P36; Ô 1–2 giữ nguyên. §0.3 đã đối chiếu. Owner cho tự gộp/tách và ghép ngay khi rà ổn; không giao áp dụng thật một việc mới trong lượt này.
- **Kết quả rà:** 85→87 (12/23/11/19/10/5/7). Bổ sung CP02.23 quyền trước ghi P01; CP07.08 khép RUN/nhả busy. Dời CP07.05@0.2→CP05.10@0.3 trước duyệt/ACK. CP01.05 chọn phiên khác CP01.11 khởi tạo binding. Sửa Master ghi kết quả kiểm (CP03.06/CP05.01/CP07.02→CAT015; CP03.10→CAT025). P01→P02/P03→P04→P05 đúng checkpoint; không đóng P04/P05 trước CP04, không đóng P05 trước ACK. Nhánh lỗi xử lý tại nơi phát sinh, không đợi đến dòng bảng.
- **Nguồn và Master:** MOW-TH-006.md là SSOT định nghĩa; catalog.detailed_workflow là bản sinh kiểm từng dòng/hash. Mã006 duy nhất trong Master quy trình tổng hợp, relation operational_detail_for005; không đổi 005/selected_process. CAT227/DEF00.1 giữ binding+sự kiện theo từng việc, không tạo Master tiến độ thứ hai. Các mã CAT có ?/* là alias thiết kế hiện hữu có link; chỉ xác minh catalog/UI, không chứng minh bảng PG/endpoint hoặc quyền toàn hệ. Từng lần ghi phải dùng cửa/quyền đúng scope.
- **UI:** dùng đúng process-work-master-v1.js nguồn UI hiện hữu; 11 mục thu/mở, 006 đặt ngay bên dưới, 7 nhóm thu/mở. Overview bỏ danh sách85 nhập riêng, đọc cùng catalog sinh từ Markdown. Hồ sơ MOW001 ghim v0.3 ở REFERENCE_ONLY, events trống, G1 không thay đổi; MOW002 chưa mở chỉ xem mẫu. Chưa có nhận thực theo006, không giả 87/87.
- **Kiểm dùng lại:** mở rộng TQT-CHECK-005 (CAT012 ca, CAT015 kết quả), cập nhật hash/pin trong Master DOT hiện hữu. Ca nguồn/phiên/hash sai và khai DONE/N/A không bằng chứng không tạo tích xanh. CHECK006 giữ runner. JEV tham khảo cách tổ chức: gen-dec-1791860979-brVdzYj0sC5nlUhOfJAZ; không thay kiểm kỹ thuật, chữ ký Claude hoặc Owner.
- **Phần chưa chứng minh:** schema bước006 cưỡng chế tại cửa ghi; +/−/↔ và item_key đầy đủ trên việc thật; AI mới đọc và thực hiện một việc cơ bản + một biến thể. Không nâng runtime/PG/Config Guard trong lượt này. Các thay đổi ở đây là thiết kế và bản chiếu đọc-only; không tuyên bố nghiệm thu vận hành độc lập. PROOT03/P39 vẫn là scope review production riêng.
- Kiểm/bản xuất/commit: xem `UI-REVIEW-AGGREGATE.json#host_review_P40`; KQ ghi sau đọc lại UI. Áp: SAME_COMMIT.

### P39 · Astra Codex · khép cờ P36 và tiếp nhận PROOT03/P140 · 2026-10-13 09:50 +07
- Ghế: Astra-Codex · Host nội dung + executor P36 · Bước/vòng: khép RUN cũ/chuẩn bị review · 1/1. Based_on: workspace `c401c8063fa3d3bed0dac11be18b462ca9bedab5`, Graph P139–P140, root PROOT03, P37/P38. Bảng: đã sửa lệch thiếu KQ; Ô 1–2: giữ nguyên. Owner trực tiếp giao ngày13/10: “Bạn tự kiểm tra theo nội dung dưới đây và xử lý gọn gẽ giúp tôi để các AI khác bắt đầu thực hiện công việc của họ.” Phạm vi chỉ khép RUN đúng sự thật và chuẩn bị review/protected apply; CHƯA sửa production, baseline, rollback, restart; không suy Owner đã duyệt giữ mã.
- **KQ DỪNG sạch, không mở lại G1:** dòng STARTED gốc giữ nguyên; KQ cùng RUN_ID ở §0.3. Task queue read-only lúc02:43Z có0 queued/running; hai job `43e4948f9c5c4c27b7b868b47483bcd3` (P37), `33e0d023071d48799b68a7dfa7a26f96` (P38) completed/exit0; task `66c06663083a4506ba1e877bb429a2cf` completed, commit `0993347400a9318c97b659a3e53b7b46ae61496c`. `/proc` không còn executor TQT, docker ps không có workspace-job/TQT test container. `lslocks --notruncate` chỉ thấy task/exec-supervisor.lock thường trực trong workspace, không có root/write/upload lease TQT; queue không có bảng scoped lease, không khẳng định đã đo lease của mọi hệ khác. Không gọi kill/cancel hay xóa lock vì không có RUN sống. Các việc khác phải kiểm S0/lease riêng; nhả cờ TQT không có nghĩa Guard toàn hệ xanh.
- **Bằng chứng nghiệp vụ giữ nguyên:** aggregate `host_review_P37.state=G1_CLOSED_TECHNICAL_VERIFIED`; P38 `LOSSLESS_STORAGE_AND_GREEN_TICKS_VERIFIED`; tệp MOW001 hiện SHA256 `c68c20ecfdfaaa01cefc13f474331e36b395a3212c3cb540595abe7302608dae`. P38 nguồn bàn giao `09933474`; đọc sổ `work/tools-quy-trinh/UI-REVIEW-AGGREGATE.json#host_review_P38`, không chạy lại G1 hay lấy TEST thay nghiệm thu. Thiếu independent code review/POST-PROTECT không được che bằng G1 đã đạt.
- **Tiếp nhận 6/6 target thuộc TQT.** Đo chỉ đọc 13/10 ~02:45Z từ registry/baseline và SHA256 file live; MATCH chỉ là khớp byte, KHÔNG APPROVED. Không sửa baseline. Image thực hiện tại `agent-data-hvu:tqt-p38-20261012`, content image ID `sha256:2d36c21a1e4e15fafde5b60b6ba03bf4504e119e99ed5f553d508464438aa804`; ảnh P36 trong P140 là lịch sử. Reviewer phải bao gồm P38 codec/pins/compose và P37 trả resource, không chỉ ba commit P32–P36.

| Target Config Guard | Baseline SHA256 | Live SHA256 | Đo hiện tại |
|---|---|---|---|
| agent-data-workspace-tools-py | 5adea01aab4a737eae186ee45db28b19c982685606710cb662dffc3320213fbc | ec72e33ea0a519220610c843ee7d18c5e6b5d2aeefab73d5e153998bd587e5d7 | DRIFT |
| agent-data-lifecycle-py | d5e36e885efba1c0bfaf90ac8fdbaf739bc570eefb1ebe14e95443a6eb4b2ed9 | acf5262b75e4e9b07b36c7baed2437269ab99af833586b8eb33393d9d0b70c2b | DRIFT |
| r7-docker-agent-data-repo-agent-data-hvu-signals-py-ecd5ab | cfa846f455c5ea31dc1c5a7785b93c02e02a0cae2c1c3fcad335883c86c819e1 | f8192e118ed32c9df1db9e06d33fb0840b562252802afbec5dd99503a67afe4e | DRIFT |
| vpsup-docker-compose | 0bdafc8ff6f796731709353d5863efa9da007e15fce8f4a0b14ab61fb9fe83cc | 0bdafc8ff6f796731709353d5863efa9da007e15fce8f4a0b14ab61fb9fe83cc | MATCH |
| mcpw-workspace-tools-config | c3b97e8a3169c8c56ded4523d3c64bc22c21738ae43f055e2c1f60fcacf04ca4 | c3b97e8a3169c8c56ded4523d3c64bc22c21738ae43f055e2c1f60fcacf04ca4 | MATCH |
| r7-config-workspace-exec-json-8430b7 | f8d5981d24c6628f546c11b7d45816f518b12de5ae957ca9d1de301de26120ae | f8d5981d24c6628f546c11b7d45816f518b12de5ae957ca9d1de301de26120ae | MATCH |

**Reviewer Claude khác hãng cần xác nhận — READ-ONLY, chưa READY/RUN production:**
1. Đọc AGENTS → Bảng/README TQT → P39 → aggregate P32/P33/P36/P37/P38 → Graph P139/P140/root PROOT03. Đối chiếu live+baseline cả6target; registry path tại `/var/lib/incomex-config-guard-v0/registry.tsv`. Rà delta `7cad52b`, `9cc075b`, `1b76843` trong `/opt/incomex/docker/agent-data-repo`, rồi P38 build/pins `/opt/incomex/staging/tqt-p36/p38/manifest.json`, `deployment.json`, mã `/opt/tqt-p38/` trong image thực. Chỉ đọc trường cần, không công bố secret.
2. So nguồn với byte trong image theo digest, không dùng HEAD/tag thay provenance. Hai commit VPSC `9457406`, `8fe2ea8` có trong image hay không vẫn **UNKNOWN** tới khi Reviewer đo. Rà cửa ghi/ACL/chữ ký, codec không mất lịch sử, hồi quy/bằng chứng P38 và coverage Điều30/31/watchdog/rollback; chưa coi fullsuite G1 là phê chuẩn deployment.
3. Kết luận ACCEPT/PARTIAL/REJECT có exact hashes/image digest, phạm vi được giữ, blocker và khả năng lùi tương thích hồ sơ đã đóng gói. Reviewer ghi mục P kế tiếp ngay COLLAB này qua gateway; không ký hộ, không sửa runtime/baseline. Đường gọi Claude hiện CHƯA ĐO; chưa phát lời mời qua dịch vụ ngoài trong lượt này, không giả đã có receipt/ý kiến.

**Đường protected apply chuẩn bị, KHÔNG thực thi:** Reviewer ACCEPT đúng byte/digest → Host chốt → Owner chỉ đạo giữ/lùi nguyên văn → Host READY phạm vi exact + S0 no-conflict/lease/Guard mới → dùng `incomex-config-apply-v0` hiện hữu, candidate ở đúng mutation-id, expected-baseline mới đo; chỉ target thực còn DRIFT và đã được duyệt. Không rebaseline các MATCH cho đủ số. Nếu giữ byte thì không tự restart; nếu cần đổi image/runtime thì phải có scope riêng trong lệnh được duyệt. HJW giữ quyền connector-sync promote/apply theo approved image digest và Hermes YAML; VPSC #11/R10 do Host tương ứng. POST-PROTECT/negative/watchdog/rollback/delivery theo luật, thiếu thì KQ DỪNG sạch. **Rollback P38:** không đặt bộ đọc cũ lên hồ sơ TQT-HISTORY-POOL-1; cần phương án giải mã qua cửa ghi hiện hành, đối chiếu toàn bộ và duyệt trước, không rollback mù.
- Bậc1: dùng KQ/Bảng/root, gateway transaction và Config Guard hiện hữu. Không tạo DOT/guard/Master/task mới. Phần còn mở là review và quyền production, không giữ busy/terminal để chờ. `NEXT_TRIGGER=CLAUDE_INDEPENDENT_REVIEW_P39_ALL6_RECEIVED`. Áp: SAME_COMMIT.

### P31 · Host xét PR14 · ACCEPT CÓ GIỚI HẠN, MOW001 VẪN 0/7
- Nguồn PR14: proposals/TQT-PR-20261011-gptchat-p29-contract-chain-review-14.md (17096db); Host tái hiện mẫu 7/7 thiếu scope cả 5 kết quả, bỏ P01 vẫn canStart, bỏ PRODUCT_SPEC vẫn contract.ready. Đây là lỗi kiểm thực, không phải chỉ thiếu runtime.
- R14-01 ACCEPT: kiểm payload giao và trường bước nhận trên chính bản đọc lại; scope và dữ liệu chuẩn bị P01 bắt buộc, sổ đối chiếu khớp ID/phiên/địa chỉ/token nội dung. Lát hai tiến trình ghi–đọc TEST đã thêm vào CHECK-004; chưa nhận là ca MOW001 thật.
- R14-02 ACCEPT: tập bắt buộc từ schema logic CAT-206 theo nguồn luật/phiên/phạm vi MOT, không dựa số 51 hoặc 66. Xóa PRODUCT_SPEC/requestId/đầu nối bị chặn.
- R14-03 ACCEPT: kiểu, cardinality/null/đơn vị, trường nguồn–đích, application/process/MOT/rule version so với schema có cấu trúc; schema được ghim SHA256. Trường gộp tách riêng, mapping request/response/cancellation và sự kiện hủy rõ. Đây là bản thiết kế 1.2, cần kiểm độc lập, chưa khẳng định đã nối schema PG.
- R14-04 ACCEPT: kết quả PREPARE phải được đọc/đối chiếu từ CP02; mất P01 không thể vào CP03.
- R14-05 ACCEPT: giữ lịch sử append-only và snapshot toàn bằng chứng trước đổi, tăng revision; không xóa record/checkpoint/decision/receipt, không đổi output_ref cùng phiên. Đường so trước–sau đã sửa; máy chủ chưa bắt buộc mọi lần ghi đi qua nó.
- R14-06 ACCEPT / CÒN MỞ TÍCH HỢP: phân giải schema/khóa và không tin PASS tự khai. Phép ghi–đọc tệp TEST có bằng chứng độc lập hai tiến trình; ACL endpoint thật, adapter sinh trust và server write hook chưa triển khai. Không dùng TEST để cấp access_check thật.
- R14-07 ACCEPT / CÒN CHỜ CHỈ ĐỊNH: reviewer độc lập phải khớp assignment và principal được bên thực thi xác minh; người TEST/P04 phải đúng danh tính. Không tự chỉ định người khác hoặc thay tự kiểm Host thành kiểm độc lập. Giữ assignment thật UNASSIGNED và chặn CP03.
- Giữ ⑤/7 mốc, 47 Master và 6 DOT; sửa CHECK-003/004 hiện hữu, không nhân bộ. Bằng chứng ở UI-REVIEW-AGGREGATE.json#host_review_P31. JEV tham khảo gen-dec-1791728386-qeMLRHnijlndRhYJd6d1; không thay nghiệm thu độc lập.

### P30 · Owner chỉ ra trùng Master DOT / Danh mục DOT · HOST SỬA VÀ THÊM KIỂM TỰ ĐỘNG
- Host nhận lỗi: kiểm riêng từng nguồn bỏ sót trùng khi ghép. ML-DEF-024/KNI-020 đã tồn tại; CAT-006 không được làm thành Master thứ hai.
- Dùng lại ML-DEF-024, ghi alias CAT-006 có căn cứ tại catalog.master_identity; 6 công cụ cùng nguồn catalog.tool_registry. Giữ liên kết chi tiết cũ; sửa record_source sai từ work_schedule về tool_registry. Danh sách 48 dòng trước thành 47 Master, không mất bản ghi.
- Bổ sung vào TQT-CHECK-005/006 hiện hữu: kiểm danh tính sau ghép, ca tái hiện lỗi, kiểm nguồn/chức năng/hash trùng; UI dừng khi phát hiện xung đột chưa có quyết định. Không thêm script/DOT/Master.
- Tiền kiểm dùng registry vừa đọc, báo hash/thiếu nguồn; đọc lại sau ghi. Phạm vi hiện là các Master thiết kế và script task; chưa kiểm kê toàn VPS/PG, chưa cưỡng chế tại workspace_transaction. Nghĩa tương đương mà metadata thiếu vẫn cần bổ sung trước khi kết luận khác nhau.
- Kết quả và phiên nguồn: UI-REVIEW-AGGREGATE.json#host_review_P30; JEV tham khảo gen-dec-1791727233-pEcPAL9xUp4Z4c9GqFZk không thay bằng chứng hay quyền duyệt.

### P29 · Host đi bộ hợp đồng thông tin theo PR-13 · ĐÃ SỬA CHỐT THIẾT KẾ, CHƯA NGHIỆM THU G1
- Bảng: cập nhật trạng thái theo §0.3.3; Ô 1–2 và chi tiết Claude giữ: không sửa. §0.3: đã đối chiếu. Owner yêu cầu lượt này: “hợp đồng thông tin thì ghi từng cái việc theo từng cái nốt sẽ ghi những cái thông tin gì, như thế nào. Master list của nó là bản nào và có những trường, cột và thông tin gì. Cách tổ chức ghi hợp đồng thông tin để xác nhận. Thế nào là hoàn thành, sẽ được ghi như thế nào.” Đề nghị Host Kiểm soát ghi bổ sung chỉ đạo vào ô 3 ở lượt được gọi, không cần Owner nhắc lại.
- Bằng chứng gốc PR-13 a7b2fbd4b84a64208492c8af7c179c05acf036f2ca04e51d95f765d2f2363839. Tái hiện C13-01: xóa CAT-206*, fixture vẫn7/7; C13-02: xóa FIELD-identity, TypeError. Phán quyết từng C13 và giới hạn tại catalog.host_review_PR13.
- Dùng lại CAT-206* schema1.1-design, nguồn phiếu sản phẩm hiện hữu; 51 dòng/3MOT, 5 giao bước P01–P05, 11 ca khai trước. Phân biệt đầu bài DESIGN_TASK và PRODUCT_SPEC; thêm đầu vào phản hồi thật/cancelled của MOT1.3, không lấy checkbox hoặc câu hỏi thay kết quả. Khóa gồm MOT/giao điểm/phiên hợp đồng. Giữ mã có dấu theo nguồn hiện tại, không tự đổi danh tính toàn hệ thống.
- Máy chặn thiếu hợp đồng/Master/MOT/giao bước; đổi nghĩa/số lượng/đích cùng phiên làm mất hiệu lực binding; kiểm/duyệt/ACK phải cùng hợp đồng và sản phẩm/phiên. Bản ghi null/thiếu/sai cấu trúc trả lỗi và không qua mốc, không làm hỏng toàn UI. Quy trình QT-CTCM-012 và Tool001/004/006 cập nhật ngay tại nguồn bước.
- DOT dùng lại TQT-CHECK-004/005/006, không thêm script chuẩn. Kiểm trước–sau đòi phiên tăng và giữ chính xác bản trước, không cho sửa lịch sử. Đã dùng trước transaction lượt này, hash trước/sau trong evidence. Chưa gắn server hook: trực tiếp gọi transaction vẫn có thể bỏ qua; không nhận đã cưỡng chế toàn hệ thống.
- C13-04 mới lập danh sách 34 endpoint cho đường đã chọn, schema/access chưa đủ; giữ NOT_TESTED và CP03 chặn. 7 nghĩa vụ đến hạn thiếu bản ghi ≠ 7 Master. Không tạo kết quả/duyệt/ACK giả; 13 câu khai chưa kiểm, 51 dòng hợp đồng nháp chưa kiểm độc lập; 0/7 mốc thật. Plan v2 ghi người kiểm P04 chưa chỉ định.
- Kiểm sau ghi: bộ cục bộ đủ 5 suite PASS,44 ca hợp đồng mới; VPS đọc nguồn và luật khớp, inventory đúng, bộ đầy đủ BLOCKED vì thiếu Node. Overview0/7, CAT206 hiện51 dòng nháp và chi tiết đọc được; không nhận PASS nghiệp vụ/PG. Commit nội dung57b2156, hiển thị67b67d8; bằng chứng cuối ở host_review_P29.
- Đường vào/SSOT giữ nguyên: knowledge/modules?task=tools-quy-trinh&view=content&section=over-view → view.html; Master CAT-206* lấy cùng catalog qua process-work-master-v1.js. Bằng chứng: UI-REVIEW-AGGREGATE.json#host_review_P29. JEV gen-dec-1791724462-JAI7JcIAg6GrH1tF4Dv2 chỉ tham khảo lựa chọn dùng lại Master, không thay duyệt độc lập. Không ghi PG.

### P28 · Host xét PR-12 v2 · TIẾP NHẬN CÓ HIỆU CHỈNH / TRIỂN KHAI LÁT C1
- Bảng: đã cập nhật dòng trạng thái theo quyền §0.3.3; Ô 1–2: giữ nguyên. §0.3: đã đối chiếu D27; đề nghị Host Kiểm soát cập nhật R04a/R09/R11/R18 theo kết luận này, không tự đổi chữ phần Claude giữ.
- Nhận D27: thiết kế → thử ngoài PG → ổn mới cắt chuyển. Không nhận suy luận “nơi lưu thật chỉ có PG”: repo bền vững cũng là kho thử nếu có hợp đồng, mã/phiên và máy đọc lại được. Thiếu kho có hợp đồng là một chỗ kẹt; 13 câu còn NOT_TESTED và kiểm độc lập vẫn là điều kiện riêng.
- Quyết định từng T/C/P tại catalog.host_review_PR12 (nguồn duy nhất). T1 gộp chỉ mục/ánh xạ, không ép cùng tên = cùng bảng; T2 giữ khóa nguồn CAT-227* và alias DEF 00.1, chưa tự đổi mã toàn hệ thống; T3 tách schema_version/record_version; C1 dùng lại file sản phẩm, không nhân bản; C5 ba ca là tối thiểu, không thay phủ nhánh và nghiệm thu staging; P2 kiểm file không bảo đảm quyền/đồng thời PG; P4 lưu kho thử chỉ đọc tới hết cửa rollback.
- Đã làm: catalog.trial_storage_contract + data_contract_index; 13 dòng declarations ở application_D24 có mã/phiên và trở thành dữ liệu kho thử; cùng bộ tính đọc dòng thật, kiểm mã/phiên/cột/địa chỉ; Python kiểm bản chiếu bằng file nguồn. Không tự tăng mốc hoặc kết quả nghiệp vụ; không viết PG, không tạo Master/script/file nguồn mới.
- C1 mới khép lát khai báo; MOW/MOT, kế hoạch, kết quả và nhánh khác còn cần binding, không nhận đã hoàn thiện kho thử toàn việc. CAT-006 cập nhật hash bộ kiểm, ca mới dùng lại checker hiện hữu. TQT-ISS-007 tiếp tục mở.
- Bằng chứng: UI-REVIEW-AGGREGATE.json#host_review_P28; không nhận tự kiểm Host là kiểm độc lập. JEV gen-dec-1791720791-8MbAAgYxDMyi2zfOLpje là tham khảo cho cách nối thiết kế/dùng lại nguồn, không là phê duyệt.
- Kiểm sau ghi: commit ed8e0e72/f1e6a321; VPS runner job 2cf644186b274d0a8eaca12e2b1bda6b đọc lại đúng file sản phẩm, projection_equal=true, 13 câu khai. Cục bộ 5 suite PASS, 59 ca cũ + 15 ca kho thử, runner 13 ca. VPS full-suite vẫn BLOCKED thiếu Node; đọc nguồn PASS không đổi trạng thái nghiệp vụ. Browser: 13/20 đến hạn đã ghi, 14 chưa đến hạn, 0 đối chiếu, 0/7 mốc; không PG. Áp: SAME_COMMIT.

### P27 · Claude phản biện khả thi QTTH 05 · bản v2 theo cách đi 3 bước của Owner (D27) · ĐỀ XUẤT, CHỜ HOST QUYẾT
Ghế: Claude-review · Host Kiểm soát + phản biện. Based_on: @dfaa160; chỉ đạo Owner 11/10 18:02 (D27); PR-07; PR-12 v1; phiếu application_D24 (34/34 record_ref = null).
- v2 (18:15) thay v1: Owner bác hướng "dùng bảng PG ngay làm nơi ghi" (A1) — trái cách đi ① thiết kế đúng → ② chạy thử ngoài PG, làm tay được → ③ ổn mới vào PG một lần. Gốc kẹt không đổi: luật ghi đòi nơi lưu thật + chưa có nơi lưu = ca thử không qua được mốc 3.
- Đề xuất v2 trong [PR-12](proposals/TQT-PR-20261011-claude-feasibility-qtth05-12.md): bước ① T1–T8 (gộp 3 bản thiết kế dữ liệu · chốt mã · phiên Master · đích PG dự kiến · bảng gốc 7 dòng · đường ý tưởng → quy trình · Over view 1 dòng/việc · tiêu chí đủ để thử) · bước ② C1–C6 (kho thử ngoài PG làm ngay · 3 ca khác loại · người làm ≠ người kiểm · sổ đổi cột · tiêu chí xong) · bước ③ P1–P4. JEV: tự khoá 0,88 · C1 gỡ khoá số 1 0,86 · hợp cách đi Owner 0,90 · rủi ro 3 bản thiết kế 0,97.
- Host Kiểm soát sửa §0 cùng commit: Bảng, R04, R04a, R09, R11, R18, 3.4 (thêm nguyên văn 17:44, 18:02), 3.5; ghi D27. Không sửa view/README/phiếu. Áp: SAME_COMMIT.
Bản v1 · 17:55 · ĐÃ THAY bởi v2 ở trên (A1 bị Owner bác 18:02), giữ đối chiếu:
Ghế: Claude-review · Host Kiểm soát + phản biện. Based_on: @64bfc31; P25–P26; PR-09/10/11; phiếu application_D24; schema + đếm dòng PG thật (chỉ SELECT).
- Tự chạy run-tqt-checks --verify: 5 suite + runner PASS cục bộ, pg NOT_RUN. Ca MOW001/G1: CHUAN_BI, mốc 2/7, 5/5 việc TODO, 0/34 đã ghi, start_confirmation PENDING từ 10/10; lịch sử 1 sự kiện.
- Kết luận: kiến trúc ⑤ khả thi; triển khai chưa khả thi vì 0 nơi ghi thật và chưa ai đi hết một lượt; thiết kế nở ra (442→868 KB view, +8 Master, +2 checker) trong khi ca thật đứng yên. PG đang chạy đã có bảng tương đương 5/11 nhóm ghi.
- Đề xuất đầy đủ: [PR-12](proposals/TQT-PR-20261011-claude-feasibility-qtth05-12.md): F01–F10, A1–A5 (dùng bảng PG có sẵn · đóng băng thiết kế · tách người làm/người kiểm · một bảng ánh xạ · Over view 1 dòng/ca), lộ trình B1–B7. JEV: gốc rễ no_store/scope, hướng B 0,72.
- Host Kiểm soát đã cập nhật Bảng, R04a, R18 theo bằng chứng. Không sửa view/README/phiếu. Áp: SAME_COMMIT.

### P26 · Host đi bộ 7 mốc và đăng ký công cụ dùng lại · KIỂM THIẾT KẾ
Ghế: Codex · Host nội dung · Bước/vòng: rà/sửa theo chỉ đạo trực tiếp Owner 11/10 · 1/5. Based_on: 7d4cedfad44832288b57eff9524b742361d8971e + bản phản biện GPT Pro Owner dán. Không giả là đã có Reviewer khác hãng nghiệm thu.
- Đường vào Owner: `/knowledge/modules?task=tools-quy-trinh&view=content&section=over-view`; nguồn `work/tools-quy-trinh/view.html`. Master nạp catalog và hàm kiểm từ cùng bản xuất qua tqt-catalog-source-v1.js; adapter `ui/process-work-master-v1.js`.
- A–D/F/G: nối bộ kiểm Python + Overview + Master vào một bộ tính; chống xóa nghĩa vụ/đổi phiên/FAIL đọc lại; mốc có dependency + revision, lỗi sau không xóa bằng chứng trước; quyết định đúng người/phạm vi/phiên, ACK đúng quyết định/người nhận.
- E: nơi ghi nhánh chỉ bắt buộc khi phát sinh. Thử file TEST có mã Master bằng runner (ghi–đọc–restore); chưa nhận đã có mapping/ghi–đọc Master thật của MOW001. Giữ TQT-ISS-007 mở, không đổi tiến độ MOW001.
- CAT-006 dùng lại mã; catalog.tool_registry quản lý 5 bộ kiểm + 1 runner, hash/lệnh/chủ quản/đầu vào-ra/giới hạn. CAT-012 bộ ca; CAT-015 kết quả. Quét hai chiều source↔danh mục. CAT-006 thêm vào danh sách thiết kế, giữ các Master trước đó; chưa nạp PG.
- Kết quả P26: cục bộ đạt các suite, 59 ca kiểm hồ sơ/mốc; UI live đúng 20 mục đến hạn/14 mục tương lai, CAT-006 hiển thị 6 công cụ. Snapshot VPS chạy mô hình 87 ca + thử file TEST đạt, nhưng thiếu Node.js nên toàn bộ suite chưa đạt trên VPS. Runner đã thêm preflight BLOCKED (exit 3); bước tiếp hạ tầng là bổ sung Node trong image thực thi được quản lý và chạy lại, không tự sửa runtime sản xuất.
- Bằng chứng: UI-REVIEW-AGGREGATE.json#host_review_P26. Nền dùng lại Node assert/Python/subprocess/JSON và workspace snapshot; code mỏng chỉ ghép kiểm hiện có và kiểm đăng ký, không service mới.
- Còn mở: MOW001 Master mapping/quyền/PG; toàn bộ DOT VPS; Reviewer độc lập và người/AI mới đi trọn sản phẩm. Áp: SAME_COMMIT.


### P25 · GPT Chat trình bày hai bảng đầu Over view theo Owner · ĐÃ KIỂM HIỂN THỊ
HUMAN_DIRECTIVE@TQT-OWNER-TWO-BOARDS-20261010 EFFECTIVE · task=tools-quy-trinh · scope=view.html phần Over view + README đường vào + mục P25 này · step=chỉ trình bày · recorded_by=GPT Chat · quote="Tôi muốn nhìn thấy 2 việc này đơn giản trên overview. Bản đồ bổ sung cho tôi và nó phải khớp với những gì codex đang làm." · audit=Owner giao trực tiếp trong cuộc trò chuyện GPT Chat 10/10/2026.
- Giữ Astra Codex làm Host nội dung/Claude kiểm soát theo D25. Không sửa §0, PROMPT, catalog, mô hình, phiếu MOW001, quyền, Master hoặc trạng thái thực thi. Thay khối tóm tắt cũ bằng hai bảng luôn hiện: 7 mốc của ⑤ (chiếu từ 6 MOT) và 8 chức năng nơi ghi từ phiếu nguồn.
- Mỗi mốc có hành động/điều kiện qua, mã MOT, nơi ghi và trạng thái việc đang xem. Mỗi sổ có đã có gì, nguồn mở được, thiếu phần nào; có chỗ ghi không đồng nghĩa đã kiểm quyền ghi/đọc lại. Phiếu hiện có lịch sử nhưng chưa chỉ kết quả chi tiết từng MOT và mục ca kiểm cho lượt mới: hiển thị thiếu, không tạo sổ giả hoặc tô xanh.
- Based_on: view SHA256 `79ab0ee1312601e03ea6f100016c1298e64eba2b8c2e64113f4030a423ec834d`; `catalog.application_preview` khớp `UI-REVIEW-MOW001.json#/application_D24`; 13 khai báo, 0 bằng chứng kiểm, trạng thái CHUAN_BI, start_confirmation chưa xác nhận. Phần kiểm JS trước ghi: 7 hàng/8 hàng, mất phiên/thiếu bằng chứng không cho xanh, escape dữ liệu. Kiểm sau commit `73d2a6ea`: Desktop 1280 mở đủ 7 mốc/8 nơi ghi, tất cả trạng thái chính hiện sẵn; mobile 390 có khung rộng362px không tràn ngang; HTTP200, console_errors=0. Bản mirror fresh, source=published. Snapshot job `12f0e656069747efa555d91c769b8bb5`: 150 ID tĩnh duy nhất; checker nguồn 3 ca đúng/34 ca sai đạt, preview MATCH_EXISTING_PRODUCT_RECEIPT/can_start=false; danh mục 5/12, refs-only PASS (checkpoint Node không chạy); mô hình87 SIMULATION_ONLY/NOT_FROZEN. Phiếu/các JSON nghiệp vụ không đổi. Không kết luận đã thiết kế xong mọi sổ hoặc đã kiểm quyền ghi; những chỗ thiếu được hiển thị, Host nội dung tiếp tục xử lý. Áp: SAME_COMMIT.

### P24 · Host Kiểm soát dựng lại §0 theo D25 · XONG phần tài liệu
Ghế: Claude-review · Host Kiểm soát (D25). Based_on: COLLAB @29f59d9; D22–D24; P16–P23; PR-07, PR-08; view.html catalog (MOW-TH-005@1.1: work_form 13 trường, 11 trạng thái, application_preview).
- Ô 1 = 3 ý Owner viết 10/10, chỉ sửa lỗi gõ. Ô 2 = 2 dòng Owner 08/10 + câu Owner 10/10 về "User chỉ cần mục tiêu, AI làm đúng theo là ra kết quả, không tự sáng tạo".
- Ô 3 dựng lại: 25 yêu cầu R00–R24 theo M1/M2/M3 và Cách làm, mỗi dòng có trạng thái; tiêu chí kiểm 5 mục; khung đang dùng rút gọn; nguyên văn chỉ đạo 10/10; đường tới bằng chứng.
- Không xoá chữ nào: đầu §0 cũ, Bảng P23, ô 1 bản 08/10 + 8 khối bổ sung, ô 2 + tiêu chí Host, toàn bộ ô 3 cũ (nhật ký kiểm, TQT-REQ, TQT-DIR, các khung) chuyển nguyên văn xuống Vòng trước.
- Khuôn chung mọi việc: xác nhận MOW-TH-005@1.1 thay cho TH-06 (13 câu khai khớp 13 ý Owner; có 11 trạng thái và bảng "đang tới đâu, ai làm tiếp"). Ba chỗ còn thiếu so với mục tiêu mới, giao Host nội dung: R04 chưa có ca thật "ý tưởng → quy trình chạy được"; R11 các danh sách trong quy trình chưa thành Master; R02 bảng mới có 1 phiếu.
- Sửa cờ giả "Chờ Owner" trên trang Owner: 2 dòng ở "Owner cần quyết" đổi sang dạng "- —". Bảng đủ 8 dòng theo MT4, có dòng ⛔.
- Ý kiến GPT Chat mà Owner định dán kèm không có trong tin nhắn; đã đối chiếu PR-08 (trước D24). Khi có, GPT nộp proposal riêng.
- DOER_CONFIRM: làm xong phần tài liệu §0; chưa phải nghiệm thu nội dung.
- Kiểm sau ghi: commit 9704bed trùng từng byte với bản dựng trước (sha256 538e19ae…). Bộ đọc §0 của trang Owner (chạy lại logic sync.py): mỗi tiêu đề ô 1–3 đúng 1 lần, Bảng 8 dòng có ⛔, "Owner cần quyết" không còn cờ chờ. Trang Kiểm soát thật lúc 08:0x: hết cảnh báo "thiếu dòng ⛔", ô 1 hiện 3 ý, ô 2 hiện 3 dòng, thanh Tiến độ không còn đỏ "Chờ Owner". Rà 2 vòng có JEV: phủ đủ các ý cũ (điểm 1,95/2), ô 1 giữ nguyên ý Owner.

### P23 · Khuôn chung ⑤ và phiếu MOW001/G1 · CHUẨN BỊ ÁP THỬ
- Tiếp nhận PR08 + Owner D24: ⑤ 1.1-design với 6 MOT giữ mã; 13 mục đủ/thiếu; kế hoạch, nơi ghi và vòng đời rõ. Mẫu thật thêm trong UI-REVIEW-MOW001.json/application_D24, bảng Overview dẫn xuất và kiểm khớp nguồn, không tạo sổ mới.
- MOW001/G1: Astra Codex làm/tự kiểm kỹ thuật; Owner nhận/duyệt thiết kế. Chưa có kiểm độc lập, chưa xác nhận điều kiện bắt đầu, chưa sửa UI lượt mới. 5 việc gồm chuẩn bị → đầu nối vào → thiết kế → UI/đầu nối ra → duyệt/bàn giao. Không G2/G3 hoặc PG.
- Sửa nguồn theo id ở PG/OPS, kiểm toàn đường dẫn thay vì chỉ đuôi; kiểm nhánh và bộ trường bắt buộc; issue_register bắt buộc, issue_ref có thể null. 003 thêm MOT công bố đúng phiên/kiểm nơi dùng/ngừng bản cũ.
- DOER_CONFIRM: hoàn tất khuôn khai báo và chuẩn bị mẫu; chưa xác nhận AI mới thực hiện toàn ca MOW001. Bộ kiểm khai báo không thay chốt PG hoặc bằng chứng sản phẩm. Tiếp tục cùng TQT-ISS-007/003, không tăng câu hỏi theo chỉ tiêu.

### P22 · Host chốt ⑤ và hoàn tất công cụ áp thử · DESIGN_TRIAL
- D23 trực tiếp: 5 MOW tổng hợp, 12 MOW thành phần; 50 việc thành phần được định danh MOT và trỏ nguồn gốc, 6 MOT của ⑤ chốt cùng phiên. Không thêm quy trình thứ 18 hoặc loại đối tượng mới.
- Hợp đồng áp thử thuộc ⑤: mã lần làm/đối tượng/phiên, người làm/kiểm/nhận, nguồn đọc/ghi, bằng chứng, đích trả, chống gửi trùng, điều kiện xong/dừng; mỗi MOT kế thừa. Đây là quy định thủ công, không tuyên bố chốt máy đã cưỡng chế.
- Tool008 chỉ ghi/đọc/bàn giao; 002 giữ vòng xử lý; 003 sửa hướng dẫn khi cần, cùng hồ sơ. Nguồn Tool hướng dẫn chuyển về repo; sổ sản phẩm giữ nguyên, ISS004 còn phần chuyển dữ liệu.
- Kiểm: danh mục/nguồn/MOT/quan hệ/nhánh và hồi quy mô hình; kiểm UI bản xuất. DOER_CONFIRM: hoàn tất chuẩn bị áp thử thiết kế; chưa xác nhận MOW001 chạy đầu-cuối hoặc PG. Giữ TQT-ISS-007 mở. Bước tiếp: Owner rà cuối → thử MOW001; không kéo dài mở rộng công cụ trước ca thử.

### P21 · Host rà Overview và ranh giới quy trình · THIẾT KẾ ĐÃ HIỆU CHỈNH
- Based_on: 44a960a; D22 trực tiếp. Giữ 5 dòng tổng hợp (4 thiết kế + 1 đề xuất), 12 thành phần và 159 câu/53 nhóm. Không đổi mục tiêu gốc, Công thức hay T2.5.
- Tiếp thu 005 về nội hàm một lượt áp dụng: chọn một quy trình; khai 6 MOT đề xuất và đường PASS/FAIL/BLOCKED/REJECTED/CANCELLED; tách ứng viên khỏi lời gọi có điều kiện. Giữ 005 chưa duyệt, chưa chốt Chuỗi, chưa quyền chạy.
- Sửa chú giải 004 cho phép 001 gọi rà UI; 003 chỉ gọi 004 khi ca là UI; câu hỏi dùng lại phiếu cùng phạm vi/phiên. Sửa phần Tool008 từng còn trùng sửa–kiểm–đóng: bản cũ nằm lịch sử, phần hiện hành chỉ ghi/đọc/bàn giao vào 002.
- Gắn 14 phần hướng dẫn/tiêu chí/câu hỏi vào MOW sở hữu; 12 thành phần khai object_type=MOW ở danh mục thiết kế, không tạo loại Tool/luồng riêng. Mapping MOT/runtime của các phần này chưa được chứng minh đầy đủ.
- Overview đưa 005 ra cửa áp dụng riêng, không nằm dưới mũi tên của 001; trạng thái và đếm đọc từ catalog. Hai HTML tham khảo giữ nguyên vai trò trình bày, không là nguồn thứ hai.
- Kiểm: 54 tham chiếu; 17 chú giải; 20 ca checkpoint; 87 ca mô phỏng nền. Kiểm mới check-overview-consistency.py: một mẫu hợp lệ và 8 tình huống sai bị từ chối. Tất cả là kiểm thiết kế, chưa PG.
- Chưa khép kín: TQT-ISS-004 cắt chuyển nguồn Tool/sổ; TQT-ISS-007 gồm 5 chốt thực thi + MOT/hợp đồng gọi. Đồng bộ danh mục không phải đồng bộ đầy đủ nội dung/hợp đồng. JEV tham khảo gen-dec-1791559006-Ne77oJBdFexGl7Hooi5P; Host giữ quyết định cuối.

### P20 · Rà đồng bộ nguồn và danh sách Master · ĐÃ XÁC NHẬN PHẠM VI THIẾT KẾ
Ghế: GPT Chat · phạm vi chỉ tài liệu/nhãn/UI đọc; không sửa Công thức, quyền RUN, backend hoặc PG.
- Nguồn: `view.html#tqt-composite-processes.catalog` gồm 4 thiết kế + 1 dự thảo 005, 12 Quy trình thành phần, 17 chú giải. `ui/tqt-catalog-source-v1.js` đọc bản đã xuất theo publishedRevision, không có kho dữ liệu mới.
- Danh sách Master: `ui/definition-master-registry-v1.js` có 29 Master theo định nghĩa STT 1–29; `ui-child-content-v1.js` thêm 1 Master Config nên tổng danh sách **30**. `ML-MOW-TH-001` ở STT29; màn Master Quy trình tổng hợp đã hiện 5 hàng, ⑤ vẫn **ĐỀ XUẤT · chưa phê duyệt**.
- Đã chỉnh tiêu đề/nhãn xưởng Master từ tổng cũ sang 30, README xưởng bỏ số bốn đóng đinh; adapter đọc Host GPT Chat + bốn trường guide từ cùng catalog, giữ chi tiết kỹ thuật ở phần mở. README/PROMPT task và phiếu UI review được cập nhật; bằng chứng cũ bốn bản ghi giữ làm lịch sử, không báo lại như hiện hành.
- Giới hạn: kiểm nguồn/sync/list theo thiết kế, chưa nghiệm thu PG/production, chưa đầy đủ parity mobile và tương tác của tất cả 30 Master. TQT-ISS-007 giữ OPEN, Owner chưa chấp thuận MOW-TH-005, không READY/RUN.

### P19 · Một nguồn chú giải; dự thảo Quy trình tổng hợp ⑤ sở hữu sáu bước · ĐÃ KIỂM THIẾT KẾ, CHỜ OWNER
Ghế: GPT Chat (OpenAI-main). Việc hôm nay chỉ thiết kế và trình bày, không RUN, không mutation ở Công thức/MOW nguồn, UI runtime hoặc PostgreSQL.
- Based_on: mục tiêu §0 đã xác nhận, chỉ đạo trực tiếp D21, 4 Quy trình tổng hợp/12 thành phần trong `tqt-composite-processes.catalog`, quy trình cổng `CHUNG.APQUYTRINH` ở `work/mow-mot-moit-mout/ban-duyet.html`, và `QT-CTCM-012` vốn lo câu hỏi.
- Mỗi record có **một trường guide** 4 giá trị ngắn: `purpose/when/avoid/done`; UI chỉ mở khi nhấn "Chú giải", không tạo file/table/hướng dẫn thứ hai. Đổi mỗi lời giải thích tại nguồn này.
- `MOW-TH-005` trạng thái **ĐỀ XUẤT · chưa phê duyệt**, `version=0.1-draft`, `chainId=null` (chưa chốt thuộc Chuỗi nào), 6 bước có ref, nhánh PASS→bàn giao, FAIL→sửa và kiểm lại, BLOCKED→DỪNG; một lượt điều phối, không tự gọi lại ở quy trình con. Mã đăng trong catalog để đọc/đối chiếu thiết kế; **chưa là quyền chạy, chưa có Master/PG lifecycle approval**.
- Giữ 12 Quy trình thành phần; không mở thêm thứ 13, không thay nội hàm `CHUNG.APQUYTRINH` hoặc `QT-CTCM-012`. **Đã kiểm:** trực tiếp #over-view desktop 1280 và mobile 390 HTTP 200/console 0; xem #MOW-TH-005 revision 8b1a96e HTTP 200/console 0, đã phân nhánh ĐẠT/CHƯA ĐẠT (sau đó rút gọn nhãn lặp). Master độc lập hiển thị mã 001…005, 005 ghi ĐỀ XUẤT. Checker catalog 5/12, 54 tham chiếu, exit0; checker model 87/87 SIMULATION_ONLY, gói NOT_FROZEN. Bản cập nhật cuối `759e1b10609ba07bab893e2401d9058022804176`; giai đoạn này chỉ đạt thiết kế, chưa chứng minh agent mới làm theo, chưa PG hay duyệt 005.
 
### P18 · Over view: vòng số rõ, STT thành phần và 2 sơ đồ HTML · ĐÃ KIỂM HIỂN THỊ
Ghế: GPT Chat (OpenAI-main) · Phạm vi: chỉ trình bày, đọc cùng một catalog, không sửa nghiệp vụ.
- Based_on: Owner D20, hai ảnh đính kèm chat; `view.html#tqt-composite-processes.catalog`, nhóm `normal_processes`, `tqt-question-matrix`, README/COLLAB nguồn ngày 09/10.
- Thực hiện: CSS `ov-bigbadge` 46px desktop / 42px mobile cho Quy trình tổng hợp; cột **STT** đứng trước tên và mã 12 Quy trình thành phần (trên mobile số ở đầu mỗi hàng); hai khối HTML thật, thu/mở được, `ov-html-reference-1` và `ov-html-reference-2` nằm **dưới** sơ đồ/bảng gốc. Poster 1 hiện trạng đầy đủ, poster 2 bản rút gọn; cùng đọc `R.records`, `R.normal_processes` và `Q.questions/groups` gốc; MOW001/002 là ví dụ dẫn link, không cộng thành quy trình tổng hợp mới.
- Commit tạo source `174d337baef5f0b8bb6802c4bd704f2e46b0c63b`; browser desktop 1280 và mobile 390 HTTP 200, 0 console errors, khung mobile x14/w362. Browser kiểm bảng STT đúng 1…12, cả 2 khối sơ đồ HTML và số 1…4 hiển thị; không có PNG/img được nhúng.
- Snapshot read-only: HTML 111 ID không trùng; catalog checker `--references-only` exit0, 4 aggregate / 12 normal / 49 tham chiếu, full checkpoint NOT_RUN (snapshot không có Node); model checker 87/87 SIMULATION_ONLY, production_ready=false. Không đổi JSON câu hỏi/công thức/PG hay tuyên bố sản phẩm đã nghiệm thu. Nếu Owner còn muốn đơn giản hơn, chỉnh trình bày từ đúng HTML, không mở luồng mới.

### P17 · Host dựng tab Over view từ một catalog · ĐÃ KIỂM GIAO DIỆN / CHƯA NGHIỆM THU NGHIỆP VỤ
Ghế: GPT Chat (OpenAI-main) · Phạm vi: riêng màn tổng quan + đồng bộ vai Host, không sửa quy trình gốc.
- Based_on: Owner giao trực tiếp D19, dữ liệu `view.html#tqt-composite-processes.catalog`, Master `ML-MOW-TH-001` có 4 mã MOW-TH, danh mục `normal_processes` có 12 mã (9 Tool + 3 quy trình bổ sung), ma trận câu hỏi 159/53 trong JSON hiện hữu; bản kiểm UI-REVIEW-AGGREGATE.json.
- Trình bày `Over view` ở đầu dải tab: sơ đồ gọi giữa 4 Quy trình tổng hợp và bảng tick gọi trực tiếp 12 Quy trình thành phần. Mã nhỏ/mờ ngay cạnh tên. Liên kết tên trỏ tới chi tiết đã có; không sao chép SSOT; không đụng CT-005, Master nguồn, PG, UI runtime, sổ.
- Host ghi theo D19, đồng bộ COLLAB/README/PROMPT và metadata Host trong 2 JSON, giữ các cổng/chốt kỹ thuật chưa nghiệm thu. UI source commits `d4a060469b1ad56018f394b07e9275b3dfda753a` + sửa số thứ tự `680be06860b254c5f4994033aa6c5187e322d672`; mirror `fresh`, source=published, lỗi liên tiếp 0. Browser trực tiếp desktop 1280/mobile 390 HTTP 200, 0 console errors; mobile `#over-view` bounds x14/w362 không tràn, desktop card/matrix đầy đủ; direct `#MOW-TH-001` mở chi tiết thật. Snapshot HTML có 110 ID không trùng, tab Over view đầu tiên; model checker 87/87 SIMULATION_ONLY, `production_ready=false`; kiểm catalog `--references-only` PASS 4 tổng hợp/12 thành phần/49 tham chiếu; test checkpoint đầy đủ KHÔNG chạy vì snapshot thiếu Node.js, không báo PASS cho phần đó. Không có phép thử AI mới hoặc RUN; TQT-ISS-007 giữ mở.

### P15 · Host giao đề bài Codex rà câu hỏi gốc trước khi vẽ UI · OPEN
Ghế: OpenAI-main · Vòng: 1/5, READ-ONLY REVIEW, chưa Reviewer/READY/RUN sửa nguồn.
- Based_on: Owner trao đổi 08/10 về nền ba nguyên liệu và bộ câu hỏi ghép; nguồn `ui/definition-master-data-v1.js` CT-001/002/002.1/003–005.1, `ui/chuoi-data-v1.js`, `work/mow-mot-moit-mout/FORMULA-AI-README.md` D153/D158; `work/tools-quy-trinh/view.html#ra-ui`.
- Bằng chứng tồn tại: CT-001 có 9 Bước lớn, 23 Bước con B1–B7; CT-002 có Field/MOIT/MOUT/MOT/MOW; CT-002.1 có 3 Chuỗi. Nội dung đã có mô tả, nhánh và điều kiện nhưng chưa có bằng chứng đầy đủ bộ câu hỏi gốc theo cấp và quy tắc kế thừa qua phép ghép. 8 câu/MOT hiện nay chỉ là câu chuyên môn rà UI, 7 câu Config chỉ chuyên môn Config; không thay thế câu hỏi của ba nguyên liệu.
- Hướng Host: mỗi Q_ID có owner nguồn, câu hỏi, nơi có câu trả lời, yêu cầu/NA, cách kiểm, xong khi, issue. Khi ghép CT003/004/005/005.1 chỉ tham chiếu ID, không sao chép 3×5×23 thành hàng nghìn phiên bản. Nếu Bước con chỉ là nhánh lặp → thêm câu hỏi/nhánh, không thêm bước mới. B1 Tìm phải dừng ở tìm được/chưa tìm được/chưa chắc, không kéo B2 Dùng vào.
- `PROMPT.md` P14 (thiết kế UI001→002) thay bằng đề bài READ-ONLY, lịch sử còn trong Git. MOW001 là ca thử ghép, MOW002 vẫn đóng. Codex được giao **đề xuất** không ghi canonical; Host nhận rồi phản biện độc lập trước khi thay nguồn SSOT.
- Bản prompt chỉ đọc được kiểm lại; định dạng link/code đã sửa, không thay nghĩa/quyền; mọi phiên Codex lấy bản current sau format, không dùng cache.
- Chưa có nhận xét Codex cho bộ câu hỏi mới; chưa có câu hỏi canonical được duyệt; chưa có phép thử AI mới làm theo, không công nhận ĐẠT. NEXT_TRIGGER=CODEX_ROOT_QUESTION_PROPOSAL. Áp: SAME_COMMIT.

### P14 · Host chốt mô hình CT-005/005.1 và plan MOW001 → MOW002 · SUPERSEDED DRAFT (D15, chưa RUN)
Ghế: OpenAI-main · Bước/vòng: Kế hoạch + PROMPT node đầu · 1/5 (đề nghị Claude-review, chưa quorum/READY)
- Based_on: Owner giao 08/10; nguồn công thức `work/mow-mot-moit-mout/ban-duyet.html#formula-ct-005/#formula-ct-005-1`; Master MOW `definition-master-v1.html?stt=4` tại VPS; `UI-DESIGN-STANDARD.md`; `UI-REVIEW-MOW001.json` PARTIAL; `mow-ui-walkthrough-v1.js`; nguồn `master-design-review-v1.html` 29 Master đang rà, reuse trước, tạo sau. Đã đọc README/AGENTS cả task MOW và tools.
- **Công thức đã có, không thiết kế lại:** CT-005 = Chuỗi+Bước+Tầng+Nhóm cha ⇒ MOW; CT-005.1 = Chuỗi+Nhóm con ⇒ MOT, dữ liệu dẫn xuất 35 MOW từ 7 bước × 5 tầng, mỗi dòng có parentGroupId. Số MOT trong Master là số bước con/task. ≥2 object ⇒ Master List là nguyên tắc Owner, không tự sinh Master cho các ngoại lệ lúc này. ~98% là phạm vi kỳ vọng, không phải % đã đo.
- **Đã đọc live:** MOW-NHC-001 CTCM B1 T0 Field = 3 MOT (Tìm Field / Tìm kiếm nâng cao / Xác nhận phù hợp), có REVIEW UI nhưng chưa chứng minh production; MOW-NHC-002 CTCM B2 T0 Field = 2 MOT `TSK-NHCN-004` người chọn Dùng, `TSK-NHCN-005` máy áp dụng & xác nhận, 0/2 bước có UI. Live MOW002 mở HTTP 200, không console error. Master design review HTTP 200, hiển thị 5 ưu tiên, 29 Master đang rà. Portal Công thức bị 401 sandbox khi kiểm browser, đã đối chiếu công thức gốc trong `ban-duyet.html` và README.
- **Chốt phương án 2 lượt không chồng:** Node A Codex làm đúng UI MOW001 ở REVIEW + đo câu hỏi/nhánh/phiếu; phải có DOER_CONFIRM và đề xuất đúng đường cho Host. Host duyệt/sửa quy trình trong TQT; chỉ sau KQ + review mới cấp Node B cho **phiên Codex mới**, làm MOW002 từ nguồn đã chuẩn hóa để thử tính tái sử dụng thật.
- **Tách nghiệm thu:** DESIGN_DONE ≠ PRODUCTION_READY. Dùng UI cha/renderer hiện có, không giả Field/JEV/nơi nhận; không tự cấp canonical hay ghi PG/Directus. MOW receipt/sổ cũ giữ nguồn sản phẩm, TQT nhận chỉ **proposal** cải tiến quy trình, Host mới nhập chuẩn. Không động sản phẩm 002 trong Node A.
- **Kiểm cổng:** Đề nghị Claude-review rà plan, đặc biệt phạm vi UI production/REVIEW, STEP_WALK, parent UI reuse và xung đột mutation với MOW. `PROMPT.md` của task này đã chuẩn bị ở trạng thái **DRAFT**. Chưa đủ phản biện/quorum & READY nên không phát RUN mutation; Codex có thể đọc, báo DELTA/proposal. Host phải chốt trước khi chuyển READY. Không tạo task mới, không đụng MOW PROMPT.md active cũ.
- **Lưu ý nguồn feedback:** đoạn Codex mới Owner dán về `vps-clean-20-9-26`, không liên quan UI MOW/TQT, không dùng làm bằng chứng kỹ thuật/bình chọn cho Node A. Ý kiến áp thử UI hiện có là Codex P09 tại tools-quy-trinh và UI-REVIEW-MOW001.json. Áp: SAME_COMMIT.

### P13 · Host rà độc lập bằng chứng Codex và xác lập phiếu xác nhận người làm · OPEN
Ghế: OpenAI-main · Bước/vòng: Chốt câu hỏi/tiêu chí cho lượt thử lại · 0/5 (chưa phát RUN)
- Based_on: hướng dẫn `view.html#ra-ui` với 6 bước, 8 câu Q1–Q8/MOT, 7 câu Config, nhánh/Given–When–Then; phiếu `work/mow-mot-moit-mout/UI-REVIEW-MOW001.json`, `tools_application_review.run_id=TQT-UI-20261008-MOW001-STEP2`, `retry_after_amendment`; P09 Codex, P12; §0 Owner. Scope chỉ `work/tools-quy-trinh/{README.md,COLLAB.md,view.html}`. Không sửa UI/runtime/PG, không phát RUN.
- **Đã kiểm được:** nguồn có 8/8 câu MOT và 7/7 câu Config, 6 bước rõ nơi lưu; phiếu có 18 quan sát màn 2 + minh họa, 3 ca R01–R03 và 2 ca độc lập CR-02/03 kiểm lại PASS phạm vi. `independent_reader` tự viết 3 ca an toàn, chỉ ra thiếu hướng tìm README từ URL, đã bổ sung. Phiếu và gate của MOW vẫn `PARTIAL/BLOCKED`: responsive, parent parity, nguồn Field thật, nơi nhận/JEV và các nhánh chưa phủ không được tự đổi xanh.
- **Khoảng trống làm quy trình chưa nghiệm thu:** 8+7 là khung câu hỏi nhưng chưa có kiểm đầy đủ câu/nhánh bằng chứng trên một lượt trọn; từng Tool vẫn ghi `Xong khi: riêng Tool chưa ghi`; chưa có xác nhận bắt buộc từ **người thực hiện** `DOER_CONFIRM YES/NO/PARTIAL` gắn commit, phạm vi, phiếu, số câu/ca, nơi lưu, bằng chứng đọc lại. PASS ca thử không phải PASS quá trình và càng không phải UI đạt production.
- **Tách hai điều kiện:** (A) quy trình rà soát thành công = agent mới làm đủ phạm vi từ README và xuất phiếu báo cáo chính xác, bao gồm các trạng thái bị chặn và sổ theo dõi; (B) UI sản phẩm thành công = tất cả các điều kiện người dùng/nơi nhận có bằng chứng thật. Một UI lỗi không đồng nghĩa quy trình rà sai; không được coi UI đạt nếu phiếu kiểm đầy đủ nhưng vẫn có blocker.
- **Lệnh kế tiếp khi Owner giao Codex:** trước tiên yêu cầu Codex đọc lại tài liệu, dùng chứng cứ thật xác nhận `DOER_CONFIRM`, nêu thiếu câu/bước cụ thể theo mẫu README và đề xuất dưới `proposals/TQT-PR-...`; không sửa ba file chuẩn. Host tiếp nhận, sửa thiếu sót vào nguồn chuẩn, rồi giao **phiên AI mới độc lập** thực hiện từ trạng thái đầu không được hướng dẫn miệng; lặp đến khi YES và kết quả phiếu được xác minh. Không cần Owner kiểm sổ hoặc làm sửa chi tiết. NEXT_TRIGGER=CODEX_CONFIRMATION_RECEIVED.
- **Chưa xong:** chưa có xác nhận lượt mới từ Codex, chưa có kiểm đầy đủ mọi nhánh, chưa có phép thử tất cả 9 Tool, chưa chứng minh gateway tự chặn ghi. Giữ TQT-ISS-003 và TQT-ISS-006 mở. Áp: SAME_COMMIT.

### P12 · Host đưa quy trình hiệu chỉnh lên đầu trang và làm rõ đường bị chặn · OPEN
Ghế: OpenAI-main · Bước/vòng: Phương án tài liệu + lượt thử đầu · 0/5 (chưa gọi worker RUN mới)
- Based_on: yêu cầu Owner mới; P08/P09 Codex (thiếu 8/7 câu, đường tìm nguồn, khuôn ca/nơi lưu; 18 quan sát và 5 ca kiểm lại phạm vi); P10 Claude (trang 6 phần); ruleset GitHub gateway-only-writes và TQT-ISS-006. Scope: chỉ ba file trong `work/tools-quy-trinh/`; không sửa MOW/PG/Directus/VPS runtime hay AGENTS.
- Nội dung mới: `TQT-QT-001` v0.1 ở `view.html#quy-trinh-hieu-chinh`, Owner tham gia trực tiếp; mỗi vòng phải có câu/bước thiếu, bằng chứng worker, phân loại blocker, quyết Host và test độc lập không cần giải thích miệng. Không công nhận hoàn thành khi chỉ có vài ca đạt.
- README mới ưu tiên câu lệnh cho mọi AI, nhất là tình huống bị chặn: dừng ghi đích chính → đọc README → nộp proposal riêng → Host nhận và thử. Error `HOST_APPROVAL_REQUIRED` mới là yêu cầu kỹ thuật tương lai, **không giả rằng máy đã chặn**; TQT-ISS-006 là blocker.
- Vòng 1: dùng phản hồi Codex P09 đã có, không bắt Owner lặp lại; phần thiếu hướng dẫn trước đó đã bổ sung nhưng chưa kiểm chứng quy trình trọn đầu ra; thiếu sản phẩm thật phải tách task sản phẩm. Chờ mẫu phản hồi mới từ Codex hoặc worker được giao hợp lệ; sau đó Host viết v0.2 rồi agent mới thử lại. Reviewer Claude xem v0.1 và góp ý theo mã bước, **chỉ đề xuất**.
- Tiêu chí nghiệm thu chính TQT-QT-001: một phiên AI mới làm đủ 5 bước trên ít nhất một hướng dẫn bị thiếu thực tế, có proposal, Host duyệt, có bản sửa và lượt agent độc lập làm ra sản phẩm đúng; phiên bị blocker không gắn ĐẠT. Điều kiện guard kỹ thuật TQT-ISS-006 cần test riêng.
- Kiểm tài liệu 08/10: VPS publish commit `93ee5edbe136860b35907829f2e53fd48389a781` `fresh`, source=published; UI inspect phần nổi bật 1280px/390px HTTP 200, title và Owner/Codex đúng, console_errors=0; kiểm Python snapshot có **57 id duy nhất, 167 neo nội bộ hợp lệ, README có định tuyến** (exit 0, source_head đúng commit). Đây chỉ là PASS cấu trúc/hiển thị, **không** phải lượt Codex mới làm ra sản phẩm.
- Lưu ý guard: Host_ID OpenAI-main dùng chung nhiều bề mặt; gate kỹ thuật sau này phải kiểm identity/bề mặt từ server, không suy từ tên commit/chữ khai. Cần kiểm trường hợp GPT Work khác GPT Chat khi triển khai.
- Chưa có phiếu độc lập về quy trình meta và chưa có enforcement/rejection proof; trạng thái **CHƯA ĐẠT**. Áp: SAME_COMMIT.

### P11 · Host tiếp nhận P08–P10 và mở cổng đề xuất · PARTIAL
Ghế: OpenAI-main · Bước/vòng: Host xem kết quả tài liệu/áp thử hiện có, chưa phát RUN worker · 0/5
- Based_on: P08/P09 Codex, P10 Claude tại repo `e1273358df5c419eca041b6b7600e12df1925bc8`; Master Tool VPS phiên `93eae888106544e7905751a15cc72b360971f3d8bda437887bfbf3f5c07b044c` còn đúng lúc đọc 11:45; GitHub active ruleset `23976991`.
- Scope: `work/tools-quy-trinh/`; không sửa MOW, runtime VPS/PG/Directus, AGENTS hay quyền GitHub toàn repo.
- **P08: ACCEPT phần phát hiện thiếu** 8/7 câu, khuôn ca và SSOT. **P09: PARTIAL** nghiệm thu 18 quan sát + 5 kiểm lại trong phạm vi; hành trình thật chưa đạt, chưa có test độc lập đầy đủ. **P10: ACCEPT bố cục/đối chiếu bản sao**, nhưng **PARTIAL chuyển nguồn** vì Master Tool OPEN vẫn là nơi cập nhật và các nơi gọi chưa chuyển.
- D08/D09: áp ngay giao tiếp nội bộ `AI đề xuất bằng file riêng → Host duyệt → ghi một nguồn chuẩn → test → đóng hoặc cải tiến`. Test thực tế của cơ chế đề xuất và enforcement cổng kỹ thuật chưa chạy, ghi TQT-ISS-006; không gọi quy trình an toàn tuyệt đối.
- Việc tiếp theo Host chịu trách nhiệm: nhận đề xuất đầu tiên từ Claude/Codex đúng mẫu, thử nhập và test; sau đó kiểm toàn bộ bản chuyển nguồn/đường dẫn, quyết cắt chuyển một SSOT mà không làm hỏng MOW; chỉ hỏi Owner khi chạm sửa task khác hoặc quyền toàn hệ.
- Đã đồng bộ chỉ dẫn trực tiếp cho AI tại cả mục Sổ ⑤ và Góp ý: chỉ nộp proposal riêng, Host mới ghi nguồn chính; sửa nhãn P08–P10 thành PARTIAL và phản hồi tại P11.
- Không phát RUN mới, không giữ phiên chờ, không đề xuất lịch tự chạy. Áp: SAME_COMMIT.

### P10 · Trình bày lại trang quy trình + chép đủ khu Công thức cũ theo chỉ đạo Owner 10:41 · PARTIAL
Ghế: Claude-review · Bước/vòng: chuẩn hóa trình bày theo HUMAN_DIRECTIVE D07 · 0/5 (không thay Host; không nghiệm thu quy trình)
- Bảng: lệch — dòng ■ ghi “chờ…” thay `— · 0 RUN active` (DROOT50), tiêu đề thiếu `cập nhật <giờ>` (MT4) → sửa cùng commit. Ô 1–2: khớp, không sửa. §0.3: đã đối chiếu (ô 1 dòng 15: một khuôn, nửa phút biết có gì, thiếu gì, tắc ở đâu).
- Based_on: repo `47bd414`; view `2524713f` (sau Codex P09 `427c1704`/`7cafa6e2`/`bb61d6f9`); nguồn VPS `ui/definition-master-data-v1.js` bản `93eae888106544e7` (đầu lượt `844f47b1`, Codex sửa giữa lượt: OPEN-02/09, Q1/Q4, thêm lượt TQT-UI-20261008-MOW001-STEP2), `ui/config-master-data-v1.js` `8cdde9db9832bf15`, trang `tools-playbook-v1.html`, Rules R46–R48 ở `work/mow-mot-moit-mout/ban-duyet.html`. JEV `gen-dec-1791431412-V60L886Mn3ooOYYFBPC0`: bố cục 3 tầng 1,00; chép đủ + ghi rõ chưa cắt chuyển 1,00.
- Scope: chỉ `work/tools-quy-trinh/{view.html,README.md,COLLAB.md}`. Không sửa VPS `ui`, Master Tool, MOW, runtime; không thu/xóa khu Công thức.
- Trang mới (5 commit `f262252` → `bcbad09` → `0e409e2` → `898ab5f` → commit này; mỗi phần đối chiếu byte với bản dựng): ① Bảng 30 giây — 3 Chuỗi, 10 quy trình × ra gì × lớp × kết quả áp thử màu, “tắc ở đâu”, “còn thiếu”; ② Rà một UI 6 bước (Codex P09 giữ nguyên chữ) + bộ 8/7 câu để ngoài mục thu + 9 thẻ Tool cùng thứ tự 🎯/📥/📦/🔢/để đâu/✅; ③ Dùng chung — CT-TOOLS-UI/CFG, thứ tự AI làm, xong khi chung, cấm, đi tới đích 8 câu, vòng cải tiến 6 câu, sửa hay ghi sổ, Tool→DOT, phân loại, R46–R48; ④ Áp thử MOW-NHC-001 — 3 MOT, 24 ô, 16 nhánh, 3 lượt chạy; ⑤ Sổ — bảng chỉ mục 15 hồ sơ + hồ sơ đủ trường một khuôn; ⑥ Chuyển nguồn — đối chiếu 10 nguồn, nơi gọi, 3 bước cắt chuyển. Giữ mọi id cũ; không dùng script (trang xem tài liệu không chạy script, theo Codex `bb61d6f9`).
- Kiểm: 39/39 bước và 9/9 câu trọng tâm/cách làm/đầu vào/ra khớp bản trước; tìm nguyên văn trên nguồn VPS: Config 10/10, công thức + 24 ô 40/40, nhánh 32/32, đi tới đích + vòng cải tiến + sửa/ghi sổ + vòng đời 31/31, sổ OPEN 36/36 trường + OPEN-02/09 đọc lại bản mới, lượt chạy 9/9 + bằng chứng/lịch sử 24/24; R46–R48 khớp repo. HTML 0 lỗi thẻ, 0 id trùng, 0 neo gãy, 0 neo nằm trong mục thu; NFC; ảnh 1280/390 không tràn ngang.
- Lệch cần Host chốt: Codex P09 ghi “dẫn hồ sơ MOW, không chép trạng thái thành sổ thứ hai”; Owner 10:41 yêu cầu chép đủ để làm liền mạch rồi thu khu cũ. Trang ghi rõ bản chép có phiên bản/giờ và nơi sửa hiện hành; chính lượt này nguồn đã đổi 2 lần trong khoảng 20 phút ⇒ cần cắt chuyển sớm, không để hai bản sống song song.
- Đề xuất Host (một phương án): (1) so nguồn với `93eae888`, chép phần đổi; (2) ghi D: từ giờ X nơi sửa duy nhất của Tools, bộ 8/7 câu, sổ OPEN và lượt chạy = `view.html`; phiếu kiểm sản phẩm (vd `UI-REVIEW-MOW001.json`) ở lại task UI; báo phiên MOW; (3) trình Owner duyệt riêng việc thu thanh “Quy trình - Tools” ở Công thức + trang Tools thành một liên kết, giữ lịch sử.
- Chưa kiểm: người đọc mới 30 giây; TQT-ISS-002 cần ghế chưa viết trang đối chiếu; “xong khi” riêng từng Tool (TQT-ISS-003).
- Phản hồi Host P11: chấp nhận bản trình bày/đối chiếu nhưng không coi việc chuyển nguồn hay nghiệm thu đầu-cuối đã hoàn thành. Áp: SAME_COMMIT.

### P09 · Áp Tools repo để rà MOW-NHC-001 màn 2; bổ sung hướng dẫn còn thiếu · PARTIAL
Ghế: Codex · Bước/vòng: Áp thử theo yêu cầu trực tiếp Owner · 0/5 (không thay Host, không nghiệm thu toàn bộ)
- Owner yêu cầu tại chat tiếp nối: đọc quy trình trên repo để rà UI màn 2; đọc là làm được, làm chưa được bổ sung quy trình.
- Based_on: repo `3a4fb961f647a4a0bfea66ec3b16bed2e9091bca`; view `1f937281a6a2ffe8f6b46c6307b80b26b10347f8c0973326594da81b6eb116ee`; nguồn Master Tool `844f47b1bb5f216a380cfb27fef0cdb24f7b99e4d0a2062e2e1d9aa078d2bcaa`.
- Scope: hướng dẫn thực hành trong view chính, README, TQT-ISS-003; phiếu UI/README MOW và cập nhật lượt/sổ gốc. Giữ ô 1–2; không sửa runtime UI, nối backend, thêm canonical UI, chuyển SSOT hay thu/xóa Công thức.
- Vướng từ repo: Tool002 thiếu bộ 8 câu cụ thể; Tool004 thiếu bộ 7 câu Config; Tool007/008 thiếu khuôn ca, đường ghi kết quả và cách xử lý chưa có nơi lưu. Bổ sung tại `view.html#ra-ui`, câu gốc đọc nhập có nguồn riêng, không tự chốt nghiệp vụ.
- Đã thực hiện: mở UI từ trạng thái trống; 11 quan sát màn làm việc (rỗng, tìm, thử lại, Enter, giữ dữ liệu/quay lại/xóa, mô tả, xác nhận thiếu Field) và 7 quan sát minh hoạ (lọc/rỗng, bỏ lọc, 3 Field MOIT, JEV trống, chọn/xác nhận). Phiếu hiện có giữ từng ca, 8 câu trả lời, khoảng trống Config và phạm vi còn mở.
- Kết quả: các điều khiển được thử cho phản hồi/giữ dữ liệu; tìm thật và tìm mô tả chưa sẵn sàng, JEV chưa có; xác nhận minh hoạ chỉ hiển thị, không lưu/gửi. OPEN-03/04/08/10 còn mở. OPEN-09 hết blocker truy cập browser trong lượt này nhưng còn parity/phạm vi UI chưa phủ; giữ lịch sử cũ.
- Kiểm lại sau bổ sung: R01 trống/R02 yêu cầu input/R03 khóa xác nhận thiếu Field đạt phạm vi ca. Phiên đọc độc lập chỉ dùng repo mới + UI đã lập CR-01/02/03, chỉ ra bước tìm README từ URL còn thiếu; đã bổ sung. Chạy CR-02 xóa hai ô và CR-03 chưa bấm Tìm thì chưa tìm đều khớp mong đợi. Kiểm link 8 câu phát hiện target nằm trong mục thu; đưa bộ 8/7 câu về khu đọc sẵn ngay hướng dẫn. Tool002/004 dẫn cùng mục, không nhân bản; không phụ thuộc script trong trang xem tài liệu. Bằng chứng trong phiếu/lượt; chưa lấy quan sát này làm PASS toàn hành trình hoặc nghiệm thu 9 Tools. TQT-ISS-003 giữ Đang xử lý, TQT-ISS-004 chuyển SSOT vẫn mở.
- JEV bằng chứng phụ `gen-dec-1791431808-HXTlQrzQs8Ow7r1jToaJ`: repo cần bổ sung 0,99; lượt đạt một phần 0,90. Không thay kiểm thực tế/quyết định hội đồng.
- Kiểm ghi: commit hướng dẫn `427c1704` pushed, không warning; đọc lại repo đúng. Trình duyệt portal hiện revision `427c1704`, thấy hướng dẫn mới và TQT-ISS-003 Đang xử lý. Kiểm HTML không trùng ID/thiếu đích neo; JSON phiếu hợp lệ. Gate UI exit 1 đúng phần còn thiếu, không sửa gate cho qua. Nguồn sổ MOW ghi phiên bản `9250a3277b8340530e590de0a850891ba61c94853b7cf41cae96dc60b36e3018`; Node CLI chưa có trong môi trường kiểm UI, xác minh cấu trúc JSON/renderer đọc lại thay thế.
- Phần chưa phủ: responsive, so UI cha, focus/tooltip, timeout/không quyền/dữ liệu đổi/bấm lặp và hành trình thật tới nơi nhận; cần nguồn/tiêu chí và lượt kiểm tiếp. Áp: SAME_COMMIT.

### P08 · Codex rà tính đầy đủ, sổ và cách trình bày theo yêu cầu Owner 08/10 · PARTIAL
Ghế: Codex · Bước/vòng: Ý kiến rà tài liệu theo yêu cầu trực tiếp Owner · 0/5 (chưa phát RUN; không thay Host)
- Người góp ý: Codex tại chat tiếp nối phiên D; Owner yêu cầu kiểm quy trình/sổ đã lên repo, tính chính xác và cách trình bày, xác nhận điều kiện thu gọn phần Công thức để một SSOT.
- Based_on: `c898b740618de4ffb851cce747b467bd56addfe1`; COLLAB version `e102bc02f232f7ed9bbd39f8bc219ca708708984536a61163ce6f26af681e617`; view version `1f937281a6a2ffe8f6b46c6307b80b26b10347f8c0973326594da81b6eb116ee`.
- Scope: ý kiến P08 tại COLLAB; đối chiếu README, view (001…009, TQT-ISS-001…005), nguồn `ui/definition-master-data-v1.js → ML-DEF-023`, trang Owner. Ô 1–2 giữ nguyên; không chốt roadmap, chuyển SSOT hay xóa nội dung MOW trong lượt rà này.
- Bảng: khớp với tình trạng bản nhập/chưa nghiệm thu; Ô 1–2: khớp. Cần cập nhật sổ tiến trình theo P07: ISS001/002 còn nói Host “sau khi Owner chỉ định”; ISS002 còn “Chưa giao/Chưa có bằng chứng” dù Host đã sửa ở `8c854489`. Giữ mở, ghi bản sửa và bước kiểm độc lập.
- Đối chiếu chuyển nguồn: đủ **9 Tools / 39 bước** ở `view.html` (001…007: 4 bước mỗi Tool; 008: 7; 009: 4). **5 TQT-ISS** đã nằm trên repo. Nguồn MOW hiện có **10 OPEN-01…OPEN-10** (1 Đóng, 2 Chưa giao, 4 Đang xử lý, 3 Bị chặn) và **2 lượt áp thử** `TOOLS-20261007-CLOSE-LOOP`, `TOOLS-20261007-THREE-SCREENS`; README/view mới dẫn về nguồn cũ, chưa nhập hai sổ này. Không dùng số 7 hồ sơ của báo cáo chat trước làm số hiện tại.
- Vướng cụ thể (TQT-ISS-003): Tool002 nhắc “Phiếu 8 câu hỏi/MOT” nhưng chưa liệt kê tám câu/đường dẫn đúng phiếu; Tool004 nhắc “7 câu Config” nhưng chưa liệt kê/dẫn đúng bộ bảy câu. Đầu ra từng Tool còn thiếu khuôn tối thiểu, nơi lưu/bàn giao và cách kiểm đủ. Nguồn còn có checklist/phần hướng dẫn và dữ liệu áp thử; nhập đủ số bước không chứng minh đã nhập đủ mọi nội dung hỗ trợ. Chưa có bằng chứng người/phiên AI mới làm theo ra sản phẩm thật.
- Đề xuất SSOT (TQT-ISS-004): kiểm kê đủ quy trình, hướng dẫn hỗ trợ, vấn đề, lượt áp thử và lịch sử; giữ mã/liên kết. Xác lập đúng một nguồn sửa trên repo và nối những trang đang dùng đọc cùng nguồn. Chỉ sau đọc lại khớp nội dung/sổ và kiểm các nơi gọi mới thu phần “Quy trình - Tools” ở Công thức thành một liên kết tới task; giữ công thức UI/Config còn dùng và bằng chứng lịch sử. Đây là đề xuất, chưa phải chuyển nguồn đã triển khai.
- Đề xuất cho người đọc: giữ cách thu/mở quen thuộc; một danh mục chính theo chuyên môn ở đầu với **Tên quy trình · Sản phẩm cần ra · Lớp · Tình trạng · Việc còn thiếu**. Mở từng Tool thấy **Cần chuẩn bị → Bước/câu hỏi → Sản phẩm/nơi lưu → Kiểm thế nào là xong**; sổ tóm tắt **Vấn đề · Người giữ việc · Bước tiếp · Điều kiện đóng**, mở mới xem lịch sử/bằng chứng. Phần phân loại, nguồn và phương pháp đưa xuống khu tham khảo thu gọn, bỏ danh mục giới thiệu trùng. Không đổi mục tiêu Owner.
- Bằng chứng xem thật: mở đúng task bằng trình duyệt, chọn “Nội dung công việc”; thấy đủ 9 cards, trạng thái bản đề xuất, các link về nguồn cũ, 5 hồ sơ TQT và phần phân loại đứng trước danh mục. JEV tham khảo `gen-dec-1791430452-vF2YmWEapzU8ghVphcPw` ủng hộ danh mục trước và kiểm chuyển/nối nguồn trước khi thu phần cũ; đây không phải phiếu hội đồng khác hãng hay nghiệm thu.
- Phần chưa kiểm: chưa thử một người/phiên AI mới hoàn tất sản phẩm; chưa đối chiếu bản gốc các chuẩn IT; chưa thực hiện/kiểm chuyển nguồn hay nghiệm thu UI tiếp theo.
- Phản hồi Host P11: tiếp nhận các điểm thiếu; vẫn cần kiểm độc lập và khóa một SSOT trước khi chuyển nguồn. Áp: SAME_COMMIT.

### P07 · Host chỉnh chữ lệch mục tiêu đã có trong TQT-ISS-002 · OPEN
Ghế: OpenAI-main · Bước/vòng: Chỉnh trang theo mục tiêu đã chốt · 0/5 (chờ xác nhận khác hãng)
- Owner giao rà nội dung liên quan. Chỉ sửa phần AI diễn giải, không sửa chữ ô 1–2.
- Đã chỉnh thẻ 01 thành ba Chuỗi CTCM/VHCM/CMSXQT; chuyên môn MOT thay “giao việc/hội đồng”; REQ-01…07 thành chỉ mục dòng ô 1; TQT-SOURCES phân định MOT/AGENTS; còn 9 Tools/39 bước và sổ MOW không đổi.
- Issue TQT-ISS-002 vẫn MỞ cho tới khi Claude-review đối chiếu và có bằng chứng người đọc mới không hiểu sai; không tự ghi ĐÓNG. Áp: SAME_COMMIT.
- Kiểm sau sửa: VPS sync-status `publishedRevision=8c854489133636cc75f5aafede6f2fcea19b0406`, `status=fresh`, lỗi đồng bộ=0. UI-inspect HTML tại `#phan-loai` HTTP 200, đủ CTCM/VHCM/CMSXQT, console_errors=0. Chưa kiểm người đọc mới hiểu đúng trong 30 giây.

### P06 · Host nhập 9 Tools CTCM / đề xuất phân loại · OPEN
Ghế: OpenAI-main · Bước/vòng: Đề xuất cấu trúc/roadmap · 0/5 (chưa phát chuông do đường gọi Reviewer CHƯA ĐO)
- Người soạn: GPT Chat, Host D06. Based_on: nguồn VPS `ui/definition-master-data-v1.js` bản `844f47b1bb5f216a380cfb27fef0cdb24f7b99e4d0a2062e2e1d9aa078d2bcaa`, mục tiêu D04/D05.
- Scope: chỉ `work/tools-quy-trinh/{COLLAB.md,view.html,README.md}`; KHÔNG sửa MOW/Master Tool, runtime, UI production, PG/Directus.
- Nội dung nhập: 9 Tool và 39 bước, câu hỏi, đầu ra; phân lớp CTCM: 6 Design (001–006), 3 Execute (007–009), 0 DOT thực. Tool 005 là thiết kế bộ ca dữ liệu; Tool 009 là Execute đóng gói DOT, không giả là DOT tự động.
- Mới là bản đọc/snapshot: Master Tool hiện vẫn là nguồn sửa; không chỉnh hai SSOT. Phương pháp `method` của nguồn chưa chứng minh đạt chuẩn IT; không có phép thử người mới/phiên AI mới thành công.
- Ghi sổ TQT-ISS-003 áp thử, 004 chuyển nguồn một SSOT, 005 nhóm nguyên tắc giao việc MOT chưa kiểm kê. Giữ sổ MOW gốc không nhân trạng thái.
- Mời Claude-review cho ý kiến: phân lớp 005/009, nhóm phù hợp, các câu hỏi/nhánh thiếu, chuẩn IT làm nền và phương án chuyển nguồn không phá Master Tool; gắn mã Tool/bước. Chưa có phiếu/quorum của vòng mới. Áp: SAME_COMMIT.


### P01 · Ghi nhận và tạo task theo yêu cầu trực tiếp · OPEN
Ghế: OpenAI-main · Bước/vòng: Khởi tạo · 0/5
- Người soạn: GPT Chat, chưa nhận Host.
- Based_on: `438dd878d9544862240d6fe28d684d1628b3d730`; AGENTS version `612c33ebf0771a66ed7d7b58b869b8ba669b69f8c530074d1d1fadfb08b118ef`.
- Scope: `work/tools-quy-trinh/` · §0/TQT-REQ, README, view.html; chỉ tài liệu khởi tạo.
- Đã đối chiếu đủ 6 yêu cầu. Tách ba chiều phân loại để không trộn phạm vi cỗ máy với lớp sử dụng. Sổ mới có một khoảng trống Owner đã nêu; sổ MOW giữ con trỏ gốc.
- Đọc/kiểm nguồn: README và các mục Tools ngày 07/10 trong COLLAB MOW; `ui/definition-master-data-v1.js` version `844f47b1bb5f216a380cfb27fef0cdb24f7b99e4d0a2062e2e1d9aa078d2bcaa`; trang Tools CTCM HTTP 200, hiển thị đúng 9 Tools, không có console error trong lần kiểm.
- Phần chưa đọc/kiểm: không rà toàn bộ COLLAB MOW/lịch sử và toàn bộ quy trình của Incomex; không kiểm chứng production của các Tools. Chưa dùng kết quả kiểm tài liệu để kết luận các quy trình đã đạt.
- Kết quả ghi: `5299be93672f1cbfe7dde06dbd706d4319621a02`, pushed=true, không warning; diff chỉ ba file trong task, 246 dòng thêm; workspace_list đọc lại đủ ba file, git_status sạch.
- Kiểm live 07/10/2026 22:00–22:02 +07: mở đúng Owner View `https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content`, HTTP 200; ảnh thật thấy task được chọn trong danh sách 7 việc Now, đúng Bảng, ô mục tiêu và tiêu chí. HTML do pipeline chuẩn publish tại `data/revisions/5299be93672f1cbfe7dde06dbd706d4319621a02/documents/tools-quy-trinh/view.html` trả HTTP 200; ui_inspect đọc đủ ba chiều, các nhóm, 9 Tools và TQT-ISS-001; trang nội dung không có console error. Đã nhìn ảnh bố cục desktop.
- Giới hạn phép kiểm: ảnh từ engine kiểm có glyph tiếng Việt thiếu ở cả khung portal và trang nội dung; văn bản UTF-8 do ui_inspect đọc đúng. Khung portal có lỗi auth 401/serviceWorker cũng quan sát được khi đọc nguồn trước khởi tạo; không sửa nền tảng trong task này. Chưa kiểm responsive, chưa kiểm chứng các quy trình production. Nghiệm thu ở đây chỉ là tạo task/nguồn/sổ và đường đọc hiện hữu.
- Phản hồi Host: chưa có Host được Owner chỉ định.

### P02 · Rà và sửa §0 theo chỉ đạo trực tiếp Owner 22:15 · OPEN
Ghế: Claude-review · Bước/vòng: Khởi tạo · 0/5
- Bảng: lệch · Ô 1–2: lệch — đã sửa trong chính commit này.
- Người góp ý: Claude Chat, nhận lời Owner trực tiếp (chỉ đạo ghi ở mục Quyết định Owner, mã TQT-GOALS-20261007). Based_on: `1199c8f9d9b9cb4ff07292895052b37385546a6b`; AGENTS version `458199c8234b268ade41ed1a5d28e67fa2020e5a2d03b40a450e2166db82f71e`, đọc đủ A0–A10.
- Scope: `work/tools-quy-trinh/COLLAB.md` §0, Quyết định Owner, Q01 · root `COLLAB.md` một dòng Đang làm + DROOT51 · `AGENTS.md` một câu tại MT3. Không sửa `view.html`, `README.md`; không lập kế hoạch, không PROMPT (cổng A0 còn đóng vì chưa có Host).
- **Bốn chỗ P01 lệch luật, đã sửa:**
  1. MT3 + MT4 «một nguồn cho Owner»: Owner liệt kê 6 mục tiêu; ô 1 chỉ có mục 1, ô 2 chỉ có mục 2, mục 3–6 bị viết lại bằng lời AI trong bảng TQT-REQ ở ô 3. Hậu quả: trang Owner chỉ hiện một câu mục tiêu, repo có một bản mục tiêu thứ hai. Sửa: ô 1 chép đủ nguyên văn; TQT-REQ ghi rõ là bảng kiểm, trỏ về số mục.
  2. MT4 dòng 🎯: không phải lời Owner. Sửa: trích nguyên văn + câu “vì sao” của chính Owner.
  3. MT4 + DROOT50 dòng ■: ghi «chờ Owner chỉ định Host». Sửa: `— · 0 RUN active`, điều kiện tương lai thành `NEXT_TRIGGER` ở ➡.
  4. A9 + DROOT18: thiếu dòng `Tên việc:` dưới tiêu đề (trang hiện tên máy `tools-quy-trinh`); root `## Đang làm` chưa có việc này. Sửa cả hai.
- **Mục 7 (bổ sung) — ứng viên nền chuẩn ngành IT để hội đồng bàn ở vòng 1. CHƯA ĐỐI CHIẾU bản gốc, chưa chốt:**
  - Khung quy trình + cải tiến liên tục: ISO 9001 (PDCA; mục 10.2 hành động khắc phục) · ITIL 4 (continual improvement).
  - Diễn đạt quy trình và luật quyết định: BPMN 2.0 · DMN (bảng quyết định — hợp nhóm “xét nguyên tắc giao việc”).
  - Lớp design: ISO 9241-210 (thiết kế lấy người dùng làm trung tâm) · WCAG 2.2 · ADR (ghi quyết định thiết kế) · Definition of Ready.
  - Lớp execute: SOP/runbook kiểu SRE · Definition of Done (Scrum) · tiêu chí nghiệm thu Given–When–Then · RACI.
  - Lớp DOT/script: Infrastructure as Code, idempotent, dry-run, exit code, CI/CD — phần lớn đã là AGENTS A10-R3/R4, chỉ cần ghi rõ nền.
  - Sổ sai sót: ITIL incident/problem management (known error) · ISO 9001 mục 10.2 · postmortem không đổ lỗi (SRE).
  - Viết cho người đọc: Diátaxis (tutorial · how-to · reference · explanation). Phân nhóm quy trình: APQC Process Classification Framework.
  - Lưu ý cỡ Incomex: lấy khung và tên gọi chuẩn, không bê cả bộ tiêu chuẩn; nền nào chọn xong thì ghi theo khuôn TQT-REQ-07.
- **Gốc rễ (vì sao lệch):** (a) chữ «ngắn» trong MT3 bị hiểu thành «chọn một câu» khi Owner liệt kê nhiều mục ⇒ thêm đúng một câu tại MT3 (DROOT51). (b) P01 tự kiểm «đủ 6 yêu cầu» theo sự có mặt trong file, không theo vị trí ô 1 ⇒ không thêm luật; chốt có sẵn là trang Owner hiện đúng ô 1 và Reviewer khác hãng mở lượt bằng `Ô 1–2: khớp | lệch`. (c) Máy không biết Owner đã nói mấy mục ⇒ không dựng guard mới (A10-R1).
- JEV `gen-dec-1791386534-1UaFcq9UIFMZ0AioXyhI` (bằng chứng phụ): Host GPT + Claude giữ §0 và trang cho người 0,97 · sửa task + một câu luật 0,76 · ô 2 = lời Owner + đề xuất có nhãn 0,72 · ứng viên chuẩn để trong mục P 0,89 · «luật có chỗ hiểu nhầm» 0,53 (không chắc).
- Kiểm trang Owner sau commit `b85e59dc4d665d9266853ccf5bfc568f0cfeef7d` (07/10 22:34–22:36 +07): đồng bộ sau 20 giây; đúng URL `…/knowledge/modules?task=tools-quy-trinh` hiện tên việc mới, Bảng P02 và ô Mục tiêu đủ 7 mục; dữ liệu trang không có cảnh báo §0; giai đoạn Mục tiêu hiện «Chờ Owner» đúng với Q01. Đã nhìn ảnh chụp thật. Ô Mục tiêu trên trang cao tối đa khoảng 9 dòng nên mục 5–7 phải cuộn trong ô mới thấy → việc hpml-view-for-user (chỉ ghi nhận, không điều hành hộ).
- Phần chưa đọc/kiểm: chưa rà toàn bộ COLLAB MOW và nội dung 9 Tools trên VPS; chưa mở bản gốc các chuẩn ngành nêu trên; chưa đánh giá lại bố cục `view.html`.
- Đề nghị Host (khi có): vòng 1 chốt ô 2 và nền chuẩn cho ba lớp + sổ trước khi vẽ lại trang; GPT Chat xác nhận DROOT51 với tư cách Founder.
- Phản hồi Host: chưa có Host được Owner chỉ định.

### P03 · Nháp viết lại ô 1 theo chỉ đạo Owner 08/10 05:44 · ACCEPTED
- Kết quả: Owner duyệt 08/10 07:16, sửa dòng 13; bản hiện hành ở ô 1–2 (D04). Khối nháp bên dưới là lịch sử trước khi duyệt, **không phải mục tiêu** — lệch thì ô 1 thắng.
Ghế: Claude-review · Bước/vòng: Chốt mục tiêu · 0/5
- Bảng: khớp · Ô 1–2: khớp (bản 07/10 vẫn hiện hành cho tới khi Owner duyệt nháp dưới đây).
- Based_on: `cd12611b085a9d32a333ccd2605a2bc606d44d95`. Scope: §0 ô 1–2 của việc này; chưa sửa hai ô. Đây là **NHÁP — chưa phải mục tiêu**; AI không làm theo nháp.
- Đã đối chiếu nguồn: ba tên ở mục 1 là ba Chuỗi của MMIM D158 (`ui/chuoi-data-v1.js`: CH-001 CTCM · CH-002 VHCM · CH-003 CMSXQT) — P01 và P02 đều chưa nối; “nguyên tắc giao việc” trong MMIM là hàm luật của MOT (COLLAB MMIM dòng Owner 26/09), P01 xếp nhầm sang nhóm “Giao việc / hội đồng”.
- JEV `gen-dec-1791413306-Nm4Mt5gjEBIcE16xt5bW` + `gen-dec-1791413401-gIrhDj0rPBnHFr3l0fhT` (bằng chứng phụ): Owner duyệt trước rồi mới đưa lên 0,93; giữ đúng ý 7 mục gốc 0,84–0,92; phần ba lớp 0,55 và ranh giới 0,47 kém chắc ⇒ đã viết lại hai dòng đó sát chữ Owner; dễ nhìn 2,1/3.
- Nháp ô 1 (chữ thường, không bảng; 5 dòng đầu để nhớ, phần dưới để tra):

```text
Đích: việc gì lặp lại cũng có quy trình chuẩn → người mới, phiên AI mới làm theo là ra đúng sản phẩm.

Công thức
1. Tool quy trình = các bước + đủ câu hỏi phải trả lời + thế nào là xong.
2. Danh mục = 3 Chuỗi × nhóm chuyên môn × 3 lớp.
3. Đạt = làm theo là xong, ra sản phẩm. Còn mắc → sửa quy trình → làm lại.
4. Chuẩn mực = chuẩn tốt nhất của ngành IT làm nền + phần riêng Incomex thêm sau.

Giải nghĩa
5. 3 Chuỗi: CTCM Chế tạo cỗ máy · VHCM Vận hành cỗ máy · CMSXQT Cỗ máy sản xuất quy trình.
6. Nhóm chuyên môn: thiết kế UI · config · xét nguyên tắc giao việc (của MOT)… → người dễ nhận diện, đánh giá, góp ý.
7. Lớp design = đủ câu hỏi → thiết kế thành công. Cho việc sáng tạo ban đầu: vẽ UI, lên danh sách, config.
8. Lớp execute = câu hỏi + thứ tự bước + thế nào là xong. Cho agent làm lặp lại.
9. Lớp DOT/script = mục tiêu + thế nào là xong + trigger. Máy tự chạy.
10. Phần sẽ viết thành DOT → DOT là trạng thái cuối. Chạm Directus/PG → bắt buộc DOT.
11. Phần còn lại: ở design hoặc execute mãi, không lên DOT — DOT mất thời gian, kém linh hoạt. Vd thiết kế UI: design là đủ.

Cách làm
12. Hội đồng AI hiệu chỉnh, bổ sung liên tục → quy trình ngày càng hoàn thiện.
13. Sai sót chưa sửa ngay → ghi một sổ, theo vòng đời tới khi xong.
14. Giờ AI ghi tay trên repo/VPS cho nhanh → sau mọi thứ vào PG (lấy quan hệ, vòng đời tự động).
15. Cho người đọc: chuẩn mực, dễ nhìn, một khuôn. Nửa phút biết có gì, thiếu gì, tắc ở đâu.

Chưa làm lúc này: quy trình nghiệp vụ (phái cử, tuyển dụng…). Chúng thuộc Chuỗi 3 CMSXQT; để sau cho đỡ lan man.
```

- Nháp ô 2 rút gọn (đề xuất — mốc của cả việc do hội đồng chốt): `Một quy trình đạt = người mới hoặc phiên AI mới làm theo, không hỏi thêm, ra đúng sản phẩm thật. Chưa đạt → sửa quy trình, thêm câu hỏi còn thiếu → chạy lại.`
- Khi Owner duyệt: thay ô 1–2 bằng bản Owner đã sửa; bản 07/10 chuyển nguyên văn xuống `Vòng trước`; cập nhật Bảng 🎯 và cột trỏ của TQT-REQ; đóng Q02.
- Phản hồi Host: chưa có Host được Owner chỉ định.

### P04 · Đưa mục tiêu Owner duyệt 08/10 lên ô 1–2 · OPEN
Ghế: Claude-review · Bước/vòng: Chốt mục tiêu · 0/5
- Bảng: lệch · Ô 1–2: lệch — sửa trong chính commit này theo D04.
- Based_on: `82df244572779a523a50511b47b982bfae0b1af6`. Scope: §0 (dòng Xác nhận, Bảng, ô 1–2, Vòng trước, TQT-REQ, TQT-DIR, TQT-LAYERS), Quyết định Owner, Q02 · `view.html` chỉ thêm một hồ sơ sổ TQT-ISS-002 · root `COLLAB.md` một dòng Đang làm. Không sửa `README.md`, không lập kế hoạch.
- Đã làm: ô 1 = bản Owner duyệt (Đích + 15 dòng + “Chưa làm lúc này”), dòng 13 theo chữ Owner sửa; ô 2 = hai câu Owner duyệt; bản 07/10 chuyển nguyên văn xuống Vòng trước; TQT-REQ thêm dòng trỏ số dòng + REQ-08, REQ-09; TQT-LAYERS đổi “phạm vi phục vụ” thành Chuỗi và ghi luật lên lớp; đóng Q02.
- Chưa sửa, đã ghi sổ TQT-ISS-002 (theo ô 1 dòng 13): trang nội dung còn thẻ “Phạm vi phục vụ” và nhóm “Giao việc / hội đồng”; cột tóm tắt TQT-REQ-01…07 và một câu ở TQT-SOURCES còn theo cách hiểu cũ. Sửa các chỗ này là việc của vòng 1 sau khi có Host.
- Kiểm trang Owner sau commit `b49524e943a91122b018edc9aa390b00cfdefccd` (08/10 07:25 +07): đồng bộ sau khoảng 45 giây; đúng URL `…/knowledge/modules?task=tools-quy-trinh` hiện Bảng P04, ô Mục tiêu mở ra thấy ngay Đích + 4 công thức không cần cuộn (dòng 5–15 cuộn trong ô), ô Thế nào là hoàn thành hai câu, có mục Vòng trước. Đã nhìn ảnh chụp thật. Giờ Bảng ban đầu ghi nhầm 07:35, đã sửa về 07:24 ở lượt ghi này.
- Phần chưa đọc/kiểm: như P02.
- Phản hồi Host: chưa có Host được Owner chỉ định.

### P05 · Owner bổ sung câu Đích 08/10 07:30 · OPEN
Ghế: Claude-review · Bước/vòng: Chốt mục tiêu · 0/5
- Bảng: lệch · Ô 1–2: lệch — sửa trong chính commit này theo D05: câu Đích ở ô 1 và dòng 🎯 của Bảng thêm vế “hướng tới muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể”; một dòng lịch sử ở Vòng trước; TQT-REQ-09 thêm cách kiểm; Q01 ghi lời Owner “chỉ định sau”.
- Based_on: `720cfebad7bd50f77aed8fc7c7fbe97d648ff746`. Scope: chỉ `work/tools-quy-trinh/COLLAB.md`.
- Phản hồi Host: chưa có Host được Owner chỉ định.


## P32 · 12/10/2026 · Host tiếp nhận PR15 và ưu tiên cửa ghi

Owner yêu cầu tiếp tục điểm mở, ưu tiên kiểm bắt buộc ở cửa ghi và quyền ghi–đọc kho thử; dùng DOT hiện có, chưa PG, không tính TEST là MOW001 đạt. Phản biện: PR15 @26d6fa3. Quyết định ACCEPT các bốn điểm hở và vấn đề ngân sách chạy; không làm lại PR14 đã đạt.

Đã sửa tại nguồn theo README P32 và `catalog.host_review_PR15`: hợp đồng v3/schema1.3, lưu lịch sử v2; CHECK004 kiểm cuối + đánh giá hiện hành + mở bản thiết kế + phục hồi sau chết/lỗi nhật ký; CHECK006 dùng ngân sách trong registry. Các phiên TEST/đọc thiết kế tổng hợp không có giá trị nghiệm thu MOW001. Giữ nguyên 34 access_check NOT_TESTED, người kiểm thật chưa chỉ định, 0/7.

C13-03 **đã cưỡng chế trong phạm vi tệp kho thử**: CHECK004 gọi tại chốt commit; 10 ca thật kiểm đọc/ghi, sửa sai, mất lịch sử, upload và đổi tên. Lỗi đổi tên được phát hiện khi thử, tệp đã khôi phục đúng hash bằng commit 1b818fa4; sửa nhận diện cả nguồn–đích, kiểm lại đạt. C13-04 vẫn PARTIAL: không nâng 34 endpoint lên PASS từ quyền một tệp. Chưa ràng buộc phiên Host riêng.

Owner xác nhận trực tiếp: “Đúng: GitHub cũ, VPS đang dùng là SSOT”. Host triển khai hẹp từ image VPS, không dùng main cũ, không đẩy agent-data-test; chặn xuất GitHub trước đó không còn là việc cần xin. Node 22.16.0 và bộ ghim đã vào image quản lý. 32 hồi quy gateway + 7 ca gate tập trung đạt (ca đổi tên bổ sung); bộ đầy đủ VPS đạt, job 24cf5bd5084f4778b67a46ed9d206c5d, khoảng 145 giây, CHECK004 107/180 giây. Nguồn gateway lưu tại VPS commit 7cad52b; không push GitHub cũ. NEXT_TRIGGER=REAL_ENDPOINT_CONTRACT_EVIDENCE_AND_INDEPENDENT_REVIEW.

Bằng chứng: `UI-REVIEW-AGGREGATE.json#host_review_P32`; Host tự kiểm kỹ thuật, không thay kiểm độc lập.


## P33 · Host rà kiểm kê và dùng lại DOT/Tool · 12/10/2026

Owner yêu cầu hai lối vào thụt dưới Master tiến trình; kiểm kê nhiều vòng theo công cụ thực sự đã dùng; AI phải tra và dùng lại trước khi tạo. Giữ Master hiện hữu, CAT-006 alias ML-DEF-024, không PG, MOW001 0/7.

Host nhận ý kiến GPT Pro A/B/C: dùng lại dot-dot-catalog và nhật ký lc_event/jobs; phân biệt công cụ tìm thấy, có dấu vết gọi và có biên nhận kết quả. Sáu DOT QTTH giữ mã; chín phương pháp Tool giữ nguyên. Ma trận sinh từ catalog/biên nhận. Điểm còn mở và bằng chứng tại README P33 và UI-REVIEW-AGGREGATE.json#host_review_P33. JEV gen-dec-1791771432-gKeZ3qw9gSvHh3ZKtX6u là nguồn tham khảo; Host chọn nối danh mục có nguồn, không cấp DOT cho từng lệnh/ca thử.

P33 đã áp dụng trên VPS: hai lối vào dưới Master tiến trình; dùng lại sổ DOT, quét 250 DOT + 49 script ngoài sổ chính, sáu bộ kiểm giữ mã; Master Tool giữ 9 phương pháp và ghi 25 năng lực kết nối. Nhật ký hiện hữu đã bổ sung biên nhận; kiểm runtime 64 đạt/1 bỏ qua, 5 phép thử live đọc–chặn ghi đạt và hồ sơ MOW001 nguyên byte. Lượt tổng VPS 60fa41f5926e4a9cbfb83545f13c6489 PASS (173.854 giây). Master vẫn 47, không thêm quy trình hay PG; MOW001 vẫn 0/7.
Còn mở có chủ đích: không phục dựng PASS cho lịch sử thiếu phiên/kết quả; chưa thu tự động đủ mọi nền tảng; 49 script cần đối chiếu hợp đồng/đăng ký trước khi dùng; chưa đo tỷ lệ tự động hóa hay nghiệm thu toàn đường. Cách cập nhật tiếp đã có trong CHECK-006 --audit-vps → --audit-patch → workspace_transaction.

Đối chiếu schema công cụ thực ở bước chốt: loại workspace_append/workspace_write/workspace_sync vì không tồn tại trong connector; thêm ui_screenshot và ba hành động tải tệp đã dùng ở P32. Master Tool: 9 phương pháp + 25 năng lực; 34 dòng. Ca tích hợp trước thiếu nguồn đã được chạy bổ sung và đạt. Một lượt worker EXECUTION_FAILED không có output được giữ lại cùng lượt thử lại PASS; không gán lỗi đó thành kết quả kiểm DOT.


## P34 · 12/10/2026 · Bộ nhớ tiến trình và đồng thuận DOT/Tool; đi thử QT001

Chỉ đạo trực tiếp Owner: tổ chức trạng thái/phiên/nâng cấp để AI đọc và dùng lại; bổ sung Master Tool; làm theo QT001 tìm thiếu sổ/trường/bước; chưa làm nhật ký hàng trăm bước. Mọi DOT/Tool có hai cột cuối “GPT duyệt”, “Claude duyệt”, giải thích tại ?. Đồng thuận hai hãng, không ký hộ. Host thực hiện trong phạm vi nguồn đã được giao, không tạo task/Master/DOT mới.

Nguồn chuẩn và đường vào vẫn hai Master dưới Master tiến trình ở trang chủ VPS. Hồ sơ máy/người cùng đọc tại `view.html → catalog.tool_registry.walkthrough`; bằng chứng `UI-REVIEW-AGGREGATE.json#host_review_P34`; hướng dẫn ở README P34. JEV gen-dec-1791777819-iewqP3YUVkHZLpuL1YOj chỉ tham khảo cách tổ chức.

Đi bộ: QT001 là MOW-TH-003, sáu bước. Chọn ca bộ nhớDOT/Tool → đọc đúng cửa vào → thấy thiếu cấu trúc cùng khuôn và sổ chưa nối bằng chứng → hiệu chỉnh nguồn/kiểm. Các Master CAT012/015/016/025/229/069 chiếu nguồn hiện có. Lịch sử trước chỉ đạo bổ sung Owner: chưa có agent khác/phiếuClaude nên lượt đầu ghi PARTIAL. Trạng thái hiện hành lấy hồ sơ P34: Host đã đi hết đường áp thử trong phạm vi Owner cho phép; không tuyên bố AI mới độc lập nghiệm thu toàn bộ QT001. Giữ47Master,6DOT; chưaPG/MOW0010/7.

Owner bổ sung trực tiếp trong lượt P34: “Bạn cứ già đi, coi như không có anthropic duyệt. Đó không phải blocker. Điều quan trọng là khi áp dụng vào quy trình thì chạy được từ đầu đến cuối. Không cần máy móc việc thủ tục hành chính đâu”. Hiệu lực: không gửi bộ nguồn sang Anthropic; tiếp tục đường áp thử, ghi Claude chưa duyệt riêng; không tuyên bố đã đồng thuận hoặc có agent mới độc lập.

KQ P34: bộ tổng VPS cuối PASS, job8ea318dd00a14af88252e6a9050a0735,157.370giây. Đã đi đường áp thử Host ghi→kiểm ở tiến trình khác→đọc Master→ghi2phiếuGPT→bàn giao nguồn. 6Master đã nối trong task; chưa xác nhận toàn bộ Master toàn hệ hay AI mới độc lập làm cả QT001. Claude chưa duyệt không chặn theo Owner. Bằng chứng/điểm thiếu chỉ ở hồ sơ P34; MOW001 nguyên byte,0/7,khôngPG.

Đọc lại phát hiện mã bộ ca sai: đã sửa đúng TQT-CASE-MASTER, đưa6bộ và5nhóm ca vào CAT012; CHECK005 chặn kết quả/ca trỏ bộ chưa đăng ký. Lượt tổng cuối8ea318dd00a14af88252e6a9050a0735 PASS157.370giây. Chữ ký005cũ đã mất hiệu lực đúng khi đổi nguồn; ghi phiếuGPT mới, giữ lịch sử.


## P35 · 12/10/2026 · Áp dụng MOW001 thật ngoài PG
STARTED@MOW001-P35-REAL-20261012 2026-10-12T04:50:44.142551+00:00 · executor=Codex Host

Đường vào Owner: Master tiến trình DEF00.1 → hồ sơ MOW001; nguồn sản phẩm duy nhất vẫn UI-REVIEW-MOW001.json#/application_D24. Không sửa UI sản phẩm trước CP03. Đã đối chiếu phiên walkthrough giữ nguyên, Master ML-DEF004 có MOW-NHC-001 và ML-DEF005 có TSK-NHCN001/002/003 cùng chain/parent. Hồ sơ trước thiếu con trỏ, không thiếu các mã này. CP01 dùng bằng chứng thật, 13 câu khai đọc lại chỉ chứng minh đúng dữ liệu, chưa PASS nội dung.

Hai lỗi khung đã sửa: CHECK004/005 cố định tiến độ ca thật ở0/7; CAT012/015/229/069 chỉ chiếu P34. Giữ6DOT/47Master, cập nhật nguồn/hash và chiếu lượt thật từ cùng phiếu. Biên nhận duyệt công cụ cũ mất hiệu lực khi mã/phụ thuộc đổi; không điền Claude.

Điểm tắc kế tiếp: P01 chưa đối chiếu đầy đủ nguồn/câu hỏi hiện hành; máy chủ gọi write-gate không truyền trust context nên CP03 không thể đạt bằng access_check tự khai; P02/P03 thiết kế thật/P04 đọc thật chưa có. Mốc6/7 chưa có quyết định/nhận của Owner. Hồ sơ chi tiết ở execution_walk, aggregate#host_review_P35. JEV gen-dec-1791780265-OUvezA9L7ZFEcjSwoPTW chỉ tham khảo phạm vi G1, không là duyệt.

KQ@MOW001-P35-REAL-20261012 DỪNG · 2026-10-12T05:03:08.852814+00:00 · CP01/CP02 có bằng chứng thật, CP03 thiếu trust context ở cửa ghi. P01 đã bổ sung6 câu thiếu (50/50); lưu rồi tiến trình khác đọc lại PASS, job37c06c47ab39465ba5a0816163dd6121; không phải người kiểm độc lập hoặc sản phẩm nghiệm thu. P02–P05 chưa thực hiện. NEXT_TRIGGER=SERVER_TRUST_ADAPTER_READY_FOR_SAME_FILE_G1; Host xử lý tiếp, không yêu cầu Owner khai lại câu hỏi hay thao tác kỹ thuật.


P35 · Bổ sung biên nhận cuối: lượt tổng VPS d0383433093a41dbaecd3e40f5d78848 PASS172.684giây; sau sửa hiển thị việc tiếp, CHECK005 đúng phiên hiện hành PASS, job989847ed92cf40fb89319df8992af407. CHECK004 đọc P01 thật jobe02137945da649c88074d2ba4398d51f:50/50,thiếu0; không phải AI kiểm độc lập. Master DOT/Tool được làm mới bằng CHECK006 từ nhật ký giữ lại; không thêm DOT. MOW001 giữ2/7,20/34; CP03 còn mở, P02–P05 chưa làm, chưa PG.

P36 · Cửa ghi triển khai1b7684368ef7c982cf8dbccfe5020f00774d863e;78PASS1skip và20caP36PASS; sáu probe quyền thậtPASS, sản phẩm nguyên byte. Hợp đồngv4 đã được /root/review_mow001 ACCEPT kỹ thuật (1a022f), P01v2/plan3; hủy hiệu lực CP02 cũ để đọc lại. Source/pin/runbook tiếp tục thuộc CHECK004, không DOT/Master mới. Chưa PG.


## P36 · Kết quả thực G1 và bài học dùng lại
Owner đã giao đi MOW001 đến cuối ngoài PG, không dùng TEST thay việc thật. Đã nối server receipts P36-2, CP03v5 commitdf12545; P02/P03 thật commitc54ec8c; Reviewer f742f5/89044e đọc đúnghash và ACCEPT kỹ thuật G1,16quan sátUI+24model. P04/11tiêuchí đang ghi–đọc đểchốtCP05; CP06/07 dành cho quyếtđịnh/nhậnOwner thật. Lỗi HTTP hồsơlớn được xửlý bằngworkspace_task_start hiệncó; outcome được đối chiếu hash/log trước retry. Master projection sửaP35cốđịnh và action bịchiếu thànhactual. Chi tiết/phiên cuối tại aggregate#host_review_P36 và phiếu MOW001; không PG, không gửiAnthropic, không thêmDOT/Master.

P36 · Phát sinh khi chạy hồ sơ thật lớn: native tổng b51e59 exit137, không tính PASS; phát hiện exporter giới hạn50MiB giữ HTMLcũ dù revision tổng mới. Đã sửa qua Config Guard targethvu-sync-py,48kiểm VPSđạt; đang kiểm lại native/đọc UI. Host cũng sửa nhầm trường hash(application khác hash tệp), không sửa sản phẩm/tiến độ đểnékiểm. Theo dõi tại Master điểm hở và aggregateP36.

P36 · Chốt bằng chứng 2026-10-12T10:30:47.193507+00:00: nativefull1GiB PASS job1912451206cb4dd28b30f4447cdfcfc3 tại nguồn276f1ac4; Master xuất available, hash khớp25f4c02b..., trình duyệt đọc đúng5/7,28/34,CHO_DUYET. Công cụHVU hiện hữu48ca đạt, liên kếtalias khôngDOTtrùng. Giữ biên nhận worker lỗi ca08...; đề xuất chẩn đoán worker và tối ưu độ lớn lịch sử vẫn mở. MOW001 chỉG1 thiết kế, chưa nốiG2/PG; Owner duyệtvàxácnhậnnhận thực tế mới ghiCAT025/CAT232 vàquaCP06/07.


### P41 · Codex Host · kiểm cờ/khóa và giao Claude Code rà độc lập PROOT03
- Ghế: Astra-Codex · Host nội dung · Bước/vòng: đối soát chỉ đọc và giao review · 1/1. Bảng: cập nhật · Ô1–2: giữ nguyên · §0.3: đã đối chiếu. Thời điểm đo: 2026-10-13T04:09:25.623436+00:00. Scope: TQT05/06, không mở G1. Bậc1: dùng sổ RUN/KQ, queue/lifecycle, gateway và apply-v0 hiện có; không tạo tool/Master mới.
- Ba STARTED TQT (P35/P36/P40) đều có KQ; không xóa lịch sử. Queue: 0 queued/running (500completed,19failed,7cancelled), disk_pressure=0. /proc không có runner/checker/activate TQT đang chạy. Không có root/write/upload/config-apply lock TQT bị giữ; supervisor là khóa dịch vụ thường trực, cache refresh ngắn là hoạt động đọc, không xóa. Container node tạm thấy trong lần đo đầu đã tự kết thúc ở lần đọc tiếp, không giết việc của AI khác. Không khẳng định mọi hệ thống khác đã hết blocker.
- Lệch cần xử lý: lifecycle P40 còn ACTIVE dù KQ đã được commit qua background; P36 REPORTED. Đã đối soát qua gateway trực tiếp cùng danh tính codex: commit7ef7d55, lifecycle P40=REPORTED và lc_report trỏ đúng commit; P36=REPORTED. Đọc lại sau commit: queue0active,0STARTED thiếuKQ,không có khóa ghi TQT; OwnerView fresh cùng commit. Không sửa SQL hay xóa lock. Số turn_open cũ của hook P36 vẫn1 nhưng stateREPORTED,waiting0,không executor; không giả đóng hook của phiên khác. Đây là dấu phiên, không phải bằng chứng có khóa ghi sống. Quyền/busy thật phải kiểm ngay trước lượt apply.
- Sáu target đo lại: đúng bảng hash P39,3DRIFT(ba tệp mã),3MATCH(compose/hai resourceconfig). Image đang chạy giữ `sha256:2d36c21a1e4e15fafde5b60b6ba03bf4504e119e99ed5f553d508464438aa804`, tag `agent-data-hvu:tqt-p38-20261012`, started2026-10-12T15:05:49.692699534Z. Không thay runtime/baseline. Owner đã quyết trước có điều kiện; không yêu cầu Owner duyệt giữ lần nữa nếu ACCEPT đúng phạm vi.

**CLAUDE-P41-REVIEW-ONLY — đề bài Host giao, Owner chuyển tay**
1. Vai Reviewer độc lập Anthropic/Claude Code; đọc AGENTS.md → TQT Bảng/README/P39/P40/P41 → root PROOT03 + Graph P139–P140. VPS là SSOT mã. Chỉ đọc runtime; không apply/register/baseline, restart/build/deploy, rollback, đổi byte, xóa khóa hay kích hoạt RUN khác. Không giữ shared lease/terminal sau khi giao báo cáo. Chỉ được ghi kết quả review vào mục P tiếp theo của COLLAB TQT qua gateway có expected version; không sửa kết luận Host/nguồn sản phẩm. Nếu không có gateway ghi, trả báo cáo trong chat cho Owner, không bypass.
2. Rà đúng ba target: `agent-data-workspace-tools-py`, `agent-data-lifecycle-py`, `r7-docker-agent-data-repo-agent-data-hvu-signals-py-ecd5ab`. Đường dẫn/baseline/live SHA256 đầy đủ tại P39; đo lại độc lập từ registry `/var/lib/incomex-config-guard-v0/registry.tsv`. Ba target còn lại chỉ đọc đối chứng, KHÔNG đề nghị đăng ký lại mục MATCH. Nếu khác hash P39 hoặc digest image P41, nêu thay đổi và PARTIAL, không tự duyệt phạm vi mới.
3. Rà delta nguồn tại `/opt/incomex/docker/agent-data-repo` (7cad52b/9cc075b/1b76843), baseline → live và live → byte thực trong container/image tqt-p38; không dùng HEAD hay tag thay digest. Đọc aggregate P32/P33/P36/P37/P38; manifest/deployment tại `/opt/incomex/staging/tqt-p36/p38/`; codec/pins `/opt/tqt-p38/` trong image. Xác minh hai commit VPSC9457406/8fe2ea8 có/không trong image bằng nội dung; không ghi UNKNOWN thành PASS.
4. Rà writegate/ACL/signature, idempotency/lock/journal recovery, codec không mất lịch sử, các giới hạn TEST; rà lifecycle background KQ không tự chốt P40 như quan sát P41. Phân biệt lỗi blocker giữ mã hiện tại với nợ không chặn, mỗi kết luận có chứng cứ. Chỉ dùng test cách ly an toàn, không ghi kho thật; không chạy selftest có mutation production. Giữ nguyên G1 7/7 và PG.
5. Rà đường giữ nguyên byte bằng incomex-config-apply-v0 hiện hữu: registry post_action=NONE cho cả3, candidate byte-identical, expected-baseline dùng theo semantics wrapper (đọc mã chốt live sau lock), serialized một lượt, PRE/POST hash+image+startedAt không đổi, Điều30/31 và audit/rollback artifact. Không chạy apply trong lượt review. HJW connector-sync/INV20 là dependency riêng, không cấp quyền promote từ báo cáo TQT. Không yêu cầu tất cả Guard xanh như điều kiện vòng tròn để sửa chính drift, nhưng mọi bypass/exception phải đúng cơ chế được phép, không tự tắt guard.
6. Trả ACCEPT/PARTIAL/REJECT rõ ràng, người/hãng/thời điểm, exact3 livehash + baselinehash + imageID, source/image mapping,2VPSC status, bằng chứng tests, blocker/nợ còn lại, phạm vi ACCEPT và protected-apply readiness. ACCEPT chỉ khi có đủ căn cứ giữ đúng mã đang chạy; không lấy G1/fullsuite hay GPT cùng hãng thay review. PARTIAL/REJECT: Codex dừng và báo Owner, không tự rollback. Xong báo cáo thì kết thúc phiên review, không giữ khóa chờ Host.

**Sau review (chưa thực thi):** Codex kiểm receipt Claude thật/exact bytes → cập nhật READY/STARTED lượt ngắn → S0 fresh no conflicting process/lease → apply-v0 đúng3target tuần tự, mỗi candidate byte-identical và post_actionNONE → kiểm hash/image/containerStartedAt không đổi + baselineMATCH + audit/POST-PROTECT → KQ cùng lượt, nhảbusy. Nếu gate/byte thay đổi hoặc cần sửa khác scope: DỪNG sạch, không mở rộng. Điều kiện Owner đã được ghi §0.3. NEXT_TRIGGER=CLAUDE_P41_ACCEPT_EXACT_BYTES. Không giữ RUN sống trong lúc Owner chuyển lệnh.
**Owner 13/10/2026 · P41 · giải phóng đường chung:** “Bạn rà soát tất cả những thứ liên quan đến việc đang làm của quy trình tổng hợp 05, 06, dọn dẹp hết các blocker để các chương trình khác còn triển khai, giúp tôi.” Quyết định trực tiếp: “nếu Claude ACCEPT thì giữ bản đang chạy — anh đăng ký đúng 3 tệp bằng incomex-config-apply-v0, không đổi nội dung tệp, không khởi động lại dịch vụ, mỗi lúc chỉ một lượt ghi trên VPS. Nếu Claude không ACCEPT thì dừng và báo tôi, không tự lùi bản.” Phạm vi đăng ký chỉ có hiệu lực cho đúng byte/image Reviewer đã ACCEPT và S0 hợp lệ; không dùng để mở quyền HJW/Graph/PG.


### P42 · Host đưa luật vào Overview, hồ sơ chỉ ghi thực tế
- Ghế: Astra-Codex · Host nội dung · Bước/vòng: thiết kế và UI/1. Owner trực tiếp giao; §0.3 đã đối chiếu. Luật006v0.4: một nguồnMarkdown, catalog sinh theohash; Overview gom7mốc/11mục/87bước thu/mở, không còn bản hồ sơMOW001 lặp ở đây.
- Hồ sơ giữ mã/tên bước chuẩn; xác nhận đã làm/không làm, việc làm/lý do,tool,kếtquả,người/thờiđiểm chỉ lấy event thực tế đúng binding.87dòng hiện trống đúng thực tế; không biến gợi ý thành đã dùng.11mục giữ lịch sử vàtích xanhG1; cách ghi nối về luật. Chưa có adapter ký/xác thực bước; khai báo không tô đạt.
- Dùng lại CHECK005: kiểm87dòng,7nhóm,6canegativeP40+caP42(blank,DONE,NOT_DONE,saiapplication); suiteexit0. Browser đúngOwnerURL kiểm7/11/87,thu/mở và87dòngactualrỗng; G1giữ7/7. Bằng chứng: aggregate#host_review_P42. Nguồn d80b8ad; UI09b303fe/b5a9aaa2; không dùngTESTnâng việc thật.
- Phối hợp: đã đọcrootPROOT04/commitClaude debe769; Claude đo chỉđọc,không chiếmVPS-GHI. Từng ghiCAS; không sửaClaudeP41review/PROOT04/runtime/Guard. Giao dịchnguồn bịmất phản hồi; đã xác minhjournalCOMMITTED+pushed trước ghiUI,không ghi lặp; callerđãđóng. KQqua directgateway đểlifecycle nhận,không giữkhóa. NEXT_TRIGGER=OWNER_NEXT_QT006_APPLICATION; ClaudeP41review/protectedapply theo phạm vi đãduyệt riêng.

### P43 · Hồ sơ ngắn gọn, hướng dẫn đúng nơi
- Ghế Astra-Codex · Host nội dung · §0.3 đã đối chiếu; Owner giao trực tiếp. Cột Bước/Tình trạng/Thực hiện-lý do/Tool đã dùng/Kết quả-nơi đã ghi/Người-thời điểm có dấu ?. Từng CP có điều kiện xong trong ?. Bỏ điều chỉnh +/−, bước riêng BS-001… có lý do, không đổi CP chuẩn.
- Không ghi sẵn tool, kết quả, trạng thái; chưa có/chưa đối chiếu để trống, cả bảng11mục. G1 đã nghiệm thu giữ nguyên, không hồi tố87bước. Bộ kiểm hiện hữu CHECK005 đạt; browser87dòng,0ô thực tế có nội dung, mở hướng dẫn tình trạng đúng. Bằng chứng aggregate#host_review_P43; UI transaction1570f426e8c64d3886cd35b0db02406d.
- Đã kiểm root mới nhất: Claude PROOT04 chỉ đọc; không sửa phạm vi đó. Ghi CAS qua gateway từng lượt; test local đã kết thúc; KQ trực tiếp và trả busy. Không PG, không restart, không xử lý Guard P41 trong lượt này. NEXT_TRIGGER=Owner giao áp QT006 hoặc CLAUDE_P41_ACCEPT_EXACT_BYTES theo phạm vi riêng.

### P44 · Hướng dẫn ngay nơi sử dụng
- Owner giao đồng bộ dấu ? tại phần11mục; §0.3 đã đối chiếu. Sáu cột có hướng dẫn,11RG lấy nội dung chuẩn trực tiếp từ catalog. Dùng cùng helper với87bước, giữ bản ghi/bằng chứng thực tế và lịch sửG1. Không còn đường Quy định cách ghi lặp từng dòng; phạm vi đối chiếu nằm trong ? tại ô chi tiết.
- CHECK005 dùng lại, thêm kiểm đủ11hướng dẫn và6cột; exit0. Browser mở hướng dẫn tại cột vàRG01,11mục vẫn thu/mở; bằng chứng aggregate#host_review_P44. Không PG/runtime, không đăng kýDOT mới.
- KQ khép cùng lượt; NEXT_TRIGGER=Owner giao việc tiếp hoặc CLAUDE_P41_ACCEPT_EXACT_BYTES trong phạm vi riêng. Không giữ lease chờ, không chạm công việcClaude.

### P45 · Lượt thật theo006 phát hiện cửa khai vòng mới chưa kín
- Ghế Astra-Codex · Host đóng vai AI mới · vòng1; §0.3 đã đối chiếu. Đích làm lại MOW001 theo lịch sử việc001, giữ mãTQT-VIEC-001 và G1đã nhận. Không tự nhận là agent/reviewer độc lập.
- CAT229 ghi MOW001-QT006-P45-REAL và từng thao tác thực tế; DEF00.1 nối attempt_ref; CAT069 ghi F01 luật/UI lệch, F02 bộ kiểm chỉ choG1, F03 quyền/cửa ghi cho vòng mới chưa có bằng chứng. CP01.04 DỪNG trước tạo hồ sơ, không giả hoàn thành87bước.
- F01: nguồn006v0.5 khớp P43/P44 (?/BS/BLOCKED); bindingG1 chỉREFERENCE_ONLY khôngevent được ghi lịch sử trước ghim bản chỉ dẫn mới. F02: CHECK005 kiểm pool nhiều hồ sơ, đúngID/phiên/nguồn, chống trùng; TEST không thay lần thật. F03: live config workspace-tools trial_record_guard chỉ ghim MOW001-G1-P36-2/application cũ; không mở rộng runtime khi chưa qua đường kiểm hiện hữu. Evidence aggregate#host_review_P45/live_guard.
- Không bypass guard bằng sửa tệp chung, không xóa lịch sử, không mởMOW002. NEXT_TRIGGER=NEW_CYCLE_WRITE_CONTRACT_VERIFIED, quay lạiCP01.04. KQ/nhả busy cùng commit, không giữ process chờ.

### P46 · Hồ sơ có số đo thật, nhánh thành công còn tắc
- Owner yêu cầu làm lại001 và điền87bước/thời gian. Host đã đọc50/50đáp án, tái lậpP01–03 từnguồn thật và thao tácUI3MOT với yêu cầu “Thời gian hoàn thành”. Tìm thường/nângcao: nguồn/evaluatorchưa nối; không có kết luận phù hợp. Hủy→nơi gọiUI nhận đúngphiên3; không làOwnerACK.
- Cột thời gian hoàn thành + thời lượng UI v1 đã ghi. Sau đọc lại root phát hiệnVPSC giữVPS-GHI từ08:30Z đến dự kiến10:30Z ⇒ không ghi sản phẩm tiếp. Việc ghiUItrước khi đọc lại cờ là thiếu sót phối hợpP46; không che lịch sử, không chiếm/xóa cờVPSC. RegistryUIpin chưa đồngbộ, phải xử lý đầu lượt được ghi; không nhận fullsuiteVPSđangPASS.
- Hồ sơ local có87bước được xét:48 hành động đã ghi nhận,10 nhánh khôngthực hiện,29 bịchặn; đây không là48bước nghiệmthu. Thời lượng riêng chỉ nơi cóđo thật; ghiJSON không tínhthờigianlaođộng. Nội dung và sốđo ở aggregate#host_review_P46; bản xem dànhOwner tại local work/p46/Ho-so-MOW001-P46.html.
- CHECK005 ứngviên bổsung ràngbuộc cycle/thời gian và đọc nộidungP02/P03/hash; caâm thiếufield bịchặn. Bộ006 sau chuẩnbịđủ snapshotPASS:0010,665s;0020,412s;0035,269s;00449,471s;00535,713s; toànrunner92,052s. Hai lỗi đầu là snapshotthiếuaggregate/2UIinputs, đã sửa local; không giấu lần lỗi. TEST không thay việc thật.
- Bản ghiMaster đã chuẩn bị trong cùng hồ sơDEF00.1:CAT228/229/015/069/244/238/025/232/233/016; chưa phát hành và chưa chốt ghi/đọcCP02.23. KhôngmởMaster/DOT mới. Chốt006toàngateway còn mở; metadata ghi được không đồng nghĩa cócưỡngchế. G1cũ giữ nguyên7/7.
- NEXT_TRIGGER=VPS_GHI_FREE: nhậnlượtghi quaCASroot, đọc nguồn mới→kiểmứngviên→ghihồsơ+registry+CHECK005→đọclại→UI; sauđó giải quyết nguồn/evaluator ngoàiPG theohợpđồng hiệncó. KQnày là thu cờ/báo cáo theoDROOT54(b,d), khôngsửa production trong lượtVPSC.

### P47 · Đưa hồ sơ về đúng DEF00.1 theo Owner
STARTED@TQT-P47-RECORD-PLACEMENT 2026-10-13T09:00:40Z · Codex Host · cập nhật tài liệu/hồ sơ, không giữ lượt đổi hệ thống.
- Owner yêu cầu đưa P46 về nơi chuẩn. Đã đọc root và VPSC: VPSC bước1/7 lúc08:33Z ghi rõ “TQT-P46 Codex chỉ ghi tài liệu, không VPS-GHI”. Nhận định P46 phải dừng mọi ghi hồ sơ là quá rộng; P47 chỉ ghi workspace tài liệu qua CAS, không sửa UI/runtime/PG hoặc nhả khóa VPSC.
- Nguồn duy nhất: catalog.work_schedule.records[TQT-VIEC-001].detail_tracking. 87 bước giữ sự kiện/thời điểm; thời lượng ghi nhật ký không coi thời lượng làm bước. Bản chiếu Master nối cùng cycle. CHECK005 bổ sung đọc nội dung/hash/phiên và xử lý khoảng chưa đo; pinUI khớp đúng mã đang phục vụ.
- Tổng P46 đến KQ32phút25giây là thời gian lượt đã dừng, không phải thời gian hoàn thành nghiệp vụ. G1cũgiữ7/7; nhánh tìm thành công thiếu nguồn/evaluator, không tô đạt.
- Kiểm ứngviên trước ghi: CHECK006 chạy001–005 đúng mã UI đang phục vụ, xem biên nhận local placement-suite; TEST chỉ kiểm công cụ và cấu trúc. Sau giao dịch phải đọc lại và mở UI đúng việc trước báo bàn giao.
KQ@TQT-P47-RECORD-PLACEMENT XONG · 2026-10-13T09:06:31.601839+00:00 · khép lượt ghi hồ sơ; không khép nghiệp vụP46. Không tạo tiến trình nền/container/lease/tệp tạm trênVPS; không chạm cờVPSC. Áp:SAME_COMMIT.

### P48 · Claude phản biện cấu trúc dữ liệu cho 1.000 việc · ĐỀ XUẤT, CHỜ OWNER GẬT (Q03)
Ghế: Claude-review · Host Kiểm soát + phản biện. Based_on: @4da3dbd; D28; PROOT04; P38–P47; đề xuất GPT do Owner chuyển 13/10.
- Đo (chỉ đọc): view.html 0,6 → 101,7 → 16,3 MB (10–13/10), chứa nguyên hồ sơ MOW001 8,65 MB (2 bản cùng dữ liệu); ~34% hồ sơ là chép trùng; cổng đọc 3,06 GB để trả 80 MB; 1.459 giao dịch TB 6,7 s, lỗi 14%; CPU VPS bận 20–31%, swap đầy ⇒ chậm vì hình dạng dữ liệu, không vì VPS yếu.
- Mô phỏng tách theo việc trên MOW001 (cục bộ): trạng thái 195 KB, bản ghi trung vị 0,55 KB; nội dung dùng chung 3,2 MB lưu 1 lần.
- Đề xuất GPT: REQUEST_CHANGES — bỏ SQLite, không dựng kho thứ hai trên VPS, Mac đọc tại chỗ, luật có máy chặn, danh sách việc cho Owner do máy sinh. Chi tiết, luật 1 trang 8 dòng, phép thử PT-01: [PR-22](proposals/TQT-PR-20261013-claude-scale-data-architecture-22.md).
- Host Kiểm soát cùng commit: D28 + nguyên văn 3.4; thêm R25–R32; dọn ô 3 (lời Owner Codex ghi → 3.4; nhật ký STARTED/KQ, khối P38/P37 → Vòng trước, nguyên văn); Bảng về 8 dòng (dòng ✅ gốc ở Vòng trước); Q03. Không sửa view/README/hồ sơ/VPS/PG. Áp: SAME_COMMIT.

### P49 · Owner giao Claude Cowork rà độc lập công thức, quy trình và hồ sơ87bước

**Vai trò:** Claude Cowork — Reviewer độc lập khác hãng. Host nội dung vẫn là Codex; không chuyển Host. Owner giao: đọc công thức, các quy trình tổng hợp, Master và từng bước đã ghi để đánh giá khách quan khả năng thực hiện/tối ưu; chỉ ghi ý kiến trên task, không sửa nguồn chính. Đây là đề bài để Owner chuyển cho Cowork, chưa phải kết quả review hay chữ ký Claude.

**Đích báo cáo duy nhất:** `work/tools-quy-trinh/proposals/TQT-PR-20261013-claude-cowork-87steps-P49.md`. Đây là ý kiến phản biện của task, không phải hồ sơ thực hiện thứ hai. Nếu tệp đã có, đọc trước rồi nối vòng review của mình, không ghi đè lịch sử/người khác. Trả Owner link báo cáo + commit + tối đa5 phát hiện quan trọng. Không chỉ trả trong chat, không lưu báo cáo chuẩn ở Mac/Drive hoặc mở task/Master mới.

**Đọc đúng nguồn, theo thứ tự:**
1. `AGENTS.md` → root `COLLAB.md` (trạng thái hiện hành/luật phối hợp) → `work/tools-quy-trinh/COLLAB.md` §0, P38–P49 → `README.md`. Đọc nguồn workspace trên VPS qua connector hiện có; không mặc định bản GitHub/cache/local là mới nhất. Ghi HEAD, phiên/hash và thời điểm lấy dữ liệu, đọc đúng phần cần thiết; tránh tải lại toàn bộ HTML lớn nhiều lần.
2. `work/tools-quy-trinh/view.html`: mục `#dung-chung` (công thức/luật dùng chung), `#quy-trinh-hieu-chinh`, các quy trình tổng hợp trong `catalog.records`, `catalog.work_form.record_control`; đọc kỹ QTTH005 và các quy trình được gọi khi sai/sửa/hủy. `MOW-TH-006.md` là định nghĩa87bước hiện hành; so bản chiếu `catalog.detailed_workflow` theo phiên/hash. Cửa đọc luật: https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=over-view . Nếu “công thức” có nguồn được dẫn tiếp, lần tới đúng nguồn, không tự đoán nghĩa.
3. Hồ sơ chuẩn: https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/process-work-master-v1.html?master=DEF00.1&chi-tiet=TQT-VIEC-001 . Nguồn `catalog.work_schedule.records[record_id=TQT-VIEC-001].detail_tracking`: `events`, `cycle.observations`, `cycle.products`, `cycle.product_hashes`, `cycle.tool_runs`, `cycle.fullsuite`, `cycle.master_records`, `cycle.issues`, `cycle.publication`. G1 gốc tại `catalog.application_preview.record` và nguồn được dẫn `work/mow-mot-moit-mout/UI-REVIEW-MOW001.json`. Không coi bản local P46 là nơi bàn giao.
4. Tra Master đúng mã từ `catalog.work_master_designs` và `work_form.record_control.masters`; kiểm ít nhất DEF00.1, CAT206/228/229/012/015/025/232/233/238/239/244/069/016 theo mã thực trong registry (giữ dấu */? nếu nguồn còn có). Master DOT: https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=24 ; Master Tool: cùng URL `?stt=23`. CAT006 và ML-DEF-024 là cùng danh mục, không đề xuất mở lại một bản trùng.
5. Đối chiếu mã/đầu vào/đầu ra/giới hạn của CHECK001–006 đã đăng ký; bằng chứng P46/P47 và `UI-REVIEW-AGGREGATE.json#host_review_P46`. Đọc P48/PR22 về dữ liệu1.000việc như **ý kiến đang chờ quyết định**, kiểm chứng số liệu khi sử dụng, không coi là luật đã áp dụng.

**Cách rà bắt buộc:**
- Đi đủ87mã CP theo thứ tự và các phiên sự kiện của từng mã, không chỉ xem có chữ/DONE. Một dòng review mỗi bước: `Mã bước | Yêu cầu/điều kiện xong | Thực tế và nguồn bằng chứng | Đạt/Thiếu/Sai/Không áp dụng/Chưa xác minh | Vấn đề/đề xuất tối thiểu`. Với bước lặp theo plan/MOT/field, kiểm đủ item_key và sự kiện áp dụng; không gộp cho mất nghĩa vụ. Không có bằng chứng thì ghi thiếu, không đoán.
- Kiểm công thức/điều kiện chuyển mốc: nghĩa, kiểu, trường bắt buộc, nguồn–đích, phiên, caller/recipient, quyền, nhận/đọc/dùng được sản phẩm, xử lý stale/trùng/hủy. Tích G1 cũ, TEST đạt và lời khai của Host không thay nghiệm thu lượt mới. Đánh giá cả chỗ Codex đánh DONE có thực sự làm đủ hay chỉ tra/ghi nhãn, gói tái lập có tạo sản phẩm mới hay chỉ chép nguồn cũ.
- Rà tính liên tục từ đầu đến cuối: bước nào thực tế dừng, bước sau đã làm độc lập hợp lệ hay vượt gate; thời điểm thật/giờ nhập hồ sơ, thời lượng đo riêng/đo chung/thời gian chờ, có cộng lặp hoặc bỏ chi phí không. Con số P46 “32phút25giây” là thời gian đến khép RUN, chưa chứng minh thời gian hoàn thành toàn việc. Xác minh lại từ nguồn; nêu rõ phần chưa đo được, không suy thành chuẩn năng suất.
- Rà11nhóm ghi và mọi Master đích: thiếu sổ hay thiếu trường/bản ghi/quyền; liên kết mở được; hiển thị và dữ liệu khớp; có trùng bản, sự kiện bị ghi đè, trạng thái cũ hiện như mới, bằng chứng nằm sai nơi, báo cáo đã ghi nhưng không nhìn thấy không. Kiểm bản chiếu có bảo toàn hồ sơ G1, không chỉ P46. Đánh giá mức dễ hiểu của cột, dấu ?, thu/mở và lượng thông tin con người phải đọc.
- Tra việc dùng lại DOT/Tool: có lượt thật/phiên/hash/kết quả và phạm vi; lỗi công cụ hay lỗi chuẩn bị snapshot; phần nào tự động kiểm được nhưng đang bắt AI làm tay. Đánh giá tối ưu theo thời gian/công sức/khả năng AI mới làm đúng, không chỉ sốbước hay sốtool. Không ép giữ87 nếu cần gộp/tách/bổ sung, nhưng đề xuất phải chỉ đúng CP và tác động tới005/006/Master/hồ sơ.

**Kết quả cần nộp:** (a) kết luận riêng về thiết kế quy trình, chất lượng ghi hồ sơ, khả năng chạy thật toàn đường và khả năng tái dùng; (b) bảng87bước; (c) bảng phát hiện gồm mức ưu tiên, nguồn/đường dẫn chính xác, bằng chứng/tái hiện, ảnh hưởng, sửa tối thiểu, nơi sửa và phép kiểm sau sửa; (d) bảng thiếu/trùng Master hoặc trường và hướng giải quyết trong nguồn hiện có; (e) thời gian đã xác minh/chưa đo được và3–5 cải tiến có lợi nhất, kèm điều cần giữ nguyên. Phân biệt quan sát với suy luận/đề xuất; nhận xét cả phần đúng và phần chưa đủ. Không nhận “đã tối ưu” chỉ vì bộ kiểmPASS; không buộc kết luận theo báo cáo Codex.

**Phạm vi quyền:** chỉ đọc nguồn và ghi báo cáo đề xuất nêu trên bằng gateway được phép, có kiểm phiên. Không sửa `view.html`, định nghĩa005/006, README/COLLAB, hồ sơ/Master, mãDOT, UI, runtime; khôngPG, restart, deploy, baseline, xóa hoặc giữ khóa chờ. Nếu cần phép thử, ưu tiên DOT hiện có trên bản sao cách ly local, ghi TEST và thời gian; không chạy bộ tải nặng trênVPS. Báo thiếu quyền/nguồn cụ thể, không vượt cổng. Ghi STARTED/KQ của lượt review và việc đã dọn ngay trong báo cáo của mình; khép sạch dù PARTIAL/BLOCKED. Nếu nguồn thay đổi trong khi rà, ghi based_on và đánh dấu phần phải rà lại; không xóa thay đổi của AI khác.

**Thông tin bàn giao để đối chiếu, không phải sự thật mặc định:** nguồn P47 commit `3b7bad917758021afeac58f4d1ad7d85ac0a98c8`, biên nhận bổ sung `52ba4254f4c35cea565d049ea758fe38567aefe4`;87dòng/91sự kiện, phân loại Host48đã làm/10không làm/29bị chặn. UI thử thật: tìm thường/nângcao thiếu nguồnField/evaluator; nhánh hủy trảUIcallerphiên3. G1cũ7/7 và P46 chưa hoàn thành phải được phân biệt. Reviewer tự đối chiếu nguồn hiện hành, không cấp ACCEPT dựa vào đoạn này.


### P50 · Tiếp nhận phản biện Claude P49, đính chính hồ sơ
STARTED@TQT-P50-CORRECTIONS 2026-10-13T10:50:05.019442+00:00 · Codex Host · Owner giao trực tiếp; §0.3 đã đối chiếu. Phạm vi UI process-work-master-v1.js và hồ sơ chuẩn view.html/CHECK005/README; không đổi nguồn G1/PG/dịch vụ. Đường vào: DEF00.1 → TQT-VIEC-001; SSOT UI /opt/incomex/docs/mcp-writes/process-work-master-v1.js, dữ liệu catalog.work_schedule.records[].detail_tracking.
- Bản sửa và phản hồi: [P50](proposals/TQT-PR-20261013-host-response-P50.md). Giữ nguyên G1 và91event, bổ sung45revision;12issue mới ởCAT069; CHECK005/006 dùng lại, có ca âm bảo toàn lịch sử/giờ/blocker. P46 chưa nghiệm thu. UI mới áp qua gateway riêng, hash 1b6ae447d56d3a1904cc69f90535ce0460d6a3d578e8906379c4efbc064b6d0a. Áp:SAME_COMMIT.
- Đọc lại VPS: commit6aea645053c15ac711e75fa4f6064fc2f360d9e6; view232edd313eb9729162614c028f7bf99218d350cd38fc56d1b15428259f7b2d92, CHECK0051dd76a1f, UI1b6ae447. 136event/12issueP50, G1/91event cũ đã kiểm giữ nguyên. Final CHECK005 exit0 trên đúng snapshot; CHECK006 lần đầu PASS (TEST). Bản đồ xử lý đủ13phát hiện ở đề bàiP50. Không tuyên bố đồng thuận Claude hoặc nghiệmthuP46.
- Browser kiểm URL hồ sơ bằng tab21 chỉ trả trang trắng, DOM rỗng/không lỗi console kể cả reload; chưa có xác nhận UI nhìn trực tiếp. Reviewer cần kiểm mục này; readback file không thay UI PASS. Không giữ RUN để đợi trình duyệt/Reviewer.
- Owner chọn tự chuyển nội dung review ra ngoài; không gọi lại CLI. Tự động duyệt đã từ chối gửi payloadP49/P50 qua Anthropic; lần gọi sandbox trước đó ENOTFOUND,0token/0USD theo CLI, không nhận review.
KQ@TQT-P50-CORRECTIONS DỪNG · 2026-10-13T10:56:30.873261+00:00 · đính chính/ghi phản hồi xong, còn UI trực tiếp và review độc lập; không khép nghiệp vụP46. Chỉ đọc SSH đã exit; không tạo tiến trình nền/container/lease VPS, git index.lock=false khi đọc lại. Trả đúng cờ VPS-GHI củaRUNnày trong cùng giao dịch. Giữ STARTED lịch sử. Áp:SAME_COMMIT.


### P51 · Hoàn thiện001 trước khi trình hai hãng và Owner
STARTED@TQT-P51-001-CORRECTIONS 2026-10-13T13:37:14.419327+00:00 · Codex Host · Owner giao trực tiếp; §0.3 đã đối chiếu. Chỉ luật/hồ sơ/DOT/UI ngoài PG; không thay cấu hình máy chủ, không phát RUN QT002. Đường chuẩn DEF00.1 → TQT-VIEC-001; UI /opt/incomex/docs/mcp-writes/process-work-master-v1.js; dữ liệu task/view.html.

**Owner chỉ đạo lượt này:** “Tôi nghĩ bạn nên tiếp tục hoàn thiện các vấn đề của 001 để đồng thuận với claude. Tôi cần cả 2 bên xác nhận ok.” “bạn xác nhận OK, claude xác nhận ok. Lúc đó tôi mới có ý kiến.” Chưa có quyền chạy QT002.

**Tiếp nhận P49 VÒNG 2:** Claude ACCEPT_CORRECTIONS cho P50 và ACCEPT_PLAN có điều kiện; đã xem đủ 87 dòng trên UI. Không dùng chữ ký P50 thay chữ ký P51. G1 đã nhận giữ nguyên; P46 chưa nghiệm thu.

| Phần | Đã sửa P51 | Giới hạn |
|---|---|---|
| B1/R2 | CHECK005 kiểm mọi hồ sơ: thông tin blocker, căn cứ Không làm, người rà khác người làm, manifest đủ ID/phiên, đọc lại, khép RUN và nhánh sửa | Kiểm bởi Host; chưa cưỡng chế tại gateway toàn hệ |
| B2 | 006 §8: kiểm ứng viên → CAS đúng quyền → receipt → đọc lại; HOST_CHECK ghi rõ server_enforced=false | Không cấp quyền endpoint; ENTRY-b là thay đổi máy chủ để sau |
| B3 | CHECK005 --commit-receipt đọc sự kiện trong commit và giờ Git trên VPS; đo STARTED/KQ theo 7 mốc, bước tay đo chung, tool giữ số đo riêng | JSON receipt tự khai không đủ; Host/Reviewer phải đọc repo chuẩn. Chưa đo một việc mới thật |
| B4 | 002@1.1 có sáu bước, điều kiện xong, nơi ghi, trạng thái issue và cách quay lại nơi phát hiện | SUPERSEDED cần ánh xạ nghĩa vụ được kiểm, không tự đóng ba issue P46 |
| R1/R3/R5 | Giữ số đo/tool qua correction_of cùng bước/item; CP03.05 Bị chặn; lọc JSON mảng/đối tượng khỏi ô kết quả | Giữ 136 sự kiện cũ; thêm 7 revision; không bịa giờ |
| U1/U2/phiên | G1 mặc định thu gọn; giờ Việt Nam; 006@0.6 mới và định nghĩa0.5 lịch sử tách rõ; tham chiếu002 khớp phiên | Khung005 vẫn bảy mốc; chưa thay kiến trúc PR22 |

**Hai bên ký ở đâu:** sổ CAT-025 hiện hữu, phiếu `TQT-P51-CONSENSUS` trong `catalog.work_schedule.records[record_id=TQT-VIEC-001].detail_tracking.cycle.master_records['CAT-025']`. Hồ sơ001 hiển thị hai cột cuối **GPT duyệt / Claude duyệt**, có dấu ?. Scope và binding xem ngay phiếu; manifest ghim luật006, định nghĩa002, tham chiếu quy trình, CHECK005, UI, bản chiếu006 và143 sự kiện. OpenAI APPROVE bởi Codex cho bộ sửa kỹ thuật; Anthropic chưa ký, ô để trống. Cả hai cùng binding/phạm vi mới trình Owner; không suy thành Owner duyệt. DOT/Tool đã có hai cột từ P34; CHECK005 nâng P51.1 có chữ ký OpenAI riêng, chưa có Claude.

**Kiểm:** CHECK006 `TQT-95e82628c0834bafac92a94cffb5162c` chạy001–005 PASS trên Mac: 0,645 / 0,378 / 5,129 / 48,332 / 36,370 giây. CHECK005 có **21 ca chung** trên hồ sơ TEST mới, có đối chứng và ca âm; thêm hai ca CLI đọc commit trên repo Git TEST tự dọn. Sau bổ sung metadata chữ ký, CHECK005 chạy lại đạt. Hai lượt tổng trước thất bại do tham chiếu phiên002 cũ và bản ghi nâng cấp DOT thiếu trường; đã sửa nguồn, không nới kiểm. TEST không nghiệm thu P46 hay002. Nguồn kết quả ở CAT015, hash/phiên ở Master DOT. Không thêm DOT/Master.

**Giao Claude rà và tự ký — chưa giao thi hành002:**
1. Đọc AGENTS → root/task COLLAB P51 → P49 VÒNG 2 → diff P51. Rà006 §8, 002.execution_contract, CHECK005 và UI. Dùng lại CHECK005/006 trên bản sao cách ly; ghi rõ TEST; không chạy bộ nặng trên VPS.
2. Rà đúng B1–B4/R1–R5: hồ sơ mới không historyproof/hậu tốP50; ca âm thiếu blocker, skip, reviewer, manifest, thời gian, khép việc. Kiểm mức HOST_CHECK, không giả bảo vệ máy chủ. Mở UI: hai ô ký, năm dòng giữ số đo/tool, CP03.05 Bị chặn, G1 thu gọn.
3. Nối báo cáo **VÒNG 3 vào tệp P49 hiện hữu**. Nếu OK, tự nối review vào phiếu CAT025 trên: `vendor=Anthropic, reviewer=<bề mặt Claude>, decision=APPROVE, reviewed_at=<giờ thực>, binding=<đúng binding P51>, scope=<nguyên scope phiếu>, evidence_ref=<P49 VÒNG3/commit>`. Chưa OK thì REJECT và chỉ rõ delta. Không ghi đè chữ ký OpenAI hoặc lịch sử. Owner giao hai bên tự xác nhận; dùng gateway CAS, đọc lại; không dùng SSH ghi vòng qua cổng.
4. Nếu duyệt CHECK005, ghi thêm review Anthropic trong `tool_registry.reviews`, đúng target_code/binding P51.1/scope hiện hữu và evidence của mình. `receipt_verified=true` chỉ sau đối chiếu bằng chứng thật. Không ký các DOT chưa rà. Chưa đủ hai hãng thì không phát RUN002.
5. Không sửa mã, luật, G1, cấu hình máy chủ hay PG; không baseline/restart/dọn việc khác. Ghi KQ và nhả tài nguyên của mình ngay. Trả link + commit + ACCEPT hoặc đúng chỗ cần sửa.

**Bước sau:** Codex đọc chữ ký Claude và delta. Hai bên OK mới trình Owner quyết ca thử QT002; Owner duyệt mới soạn READY cho Claude thực hiện, phía OpenAI kiểm sản phẩm. Không lấy đồng ý hướng sửa thành đồng ý chạy.

Binding của bộ sửa: `666343031d3959c9ac6eadcc5966111d74931b9d41d99d7b78fd3e9b6f2513e2`.

- Bổ sung chốt cuối: application mới không được chọn định nghĩa cũ để né luật0.6; CLI đối chứng phiên hiện hành PASS và phiên cũ bị từ chối `NEW_APPLICATION_REQUIRES_CURRENT_DEFINITION`. CHECK005 phiên cuối chạy lại đạt. Fullsuite trước đó vẫn giữ biên nhận; không thay giờ chạy hay nói đã chạy lại các bộ không đổi.
- Giao diện thật đã kiểm qua ui_inspect, HTTP200, phiếu CAT025 hiện GPT ✅ OK và Claude trống; G1/phiên cũ giữ riêng. Có cảnh báo font Google bị CSP chặn, không nới CSP. Readback trước chốt cuối:143event,006@0.6, hồ sơP46 ghim0.5, đúng hash UI/luật/bộ kiểm. Binding cuối trong phiếu và dòng trên; ký phải lấy đúng phiếu hiện hành, không lấy binding lần kiểm trước.
KQ@TQT-P51-001-CORRECTIONS DỪNG · 2026-10-13T13:46:27.373731+00:00 · Phần sửa/kiểm/bàn giao của Codex đã xong; chưa có chữ ký Claude và chưa được Owner duyệt ca thử. Giữ STARTED lịch sử. Không tạo tiến trình nền/container/lease VPS; các lượt SSH chỉ đọc đã exit, index.lock=false khi kiểm. Trả đúng VPS-GHI của lượt này cùng giao dịch, không giữ tài nguyên đợi review. Áp:SAME_COMMIT.


### P52 · Codex Host · D1/D2 và hợp đồng hoàn thành / nợ / Field
- Bảng: sửa lệch P51 chưa ghi REJECT của Claude; Ô 1–2 giữ nguyên. Đã đối chiếu §0.3, P49 VÒNG 3, HEAD db094cef5754924793a997a53b55c020b465bc94.
- Owner giao trực tiếp: “Thế nào đạt để GPT và Claude ký hoàn thành”; “Danh sách cụ thể những điều ghi nợ lại để thực hiện tiếp (cái này cả GPT và Claude cũng cần ký)”; “phải điền danh sách field vào master field … tình trạng cần tạo thêm, đã tạo trong PG”. Đây là bổ sung chi tiết nghiệm thu; không đổi mục tiêu ô 1–2.
- SSOT: luật MOW-TH-006.md §9; hồ sơ DEF00.1/TQT-VIEC-001; nợ cycle.issues → CAT-069; ba phiếu CAT-025 TQT-P52-CORRECTIONS / TQT-P52-DEBTS / TQT-P52-FIELDS; Master Field ML-DEF-008 (stt=8) đọc catalog.field_registry. Không tạo Master mới.
- STARTED@TQT-P52-FIX 2026-10-13T14:30:37.095535+00:00 · executor=Codex Host · một lượt ghi tài liệu/UI ngoài PG; không cấu hình, restart hoặc chạy QT002.
- Sửa D1: CHECK005 mặc định/CLI cùng xác minh commit Git thuộc HEAD và sự kiện đúng việc/mốc/loại/giờ; không tin JSON receipt tự khai. Không Git → UNVERIFIED, cấm nghiệm thu. Sửa D2: review.subject_vendor / reviewer_vendor phải khác hãng. Giữ 143 events P46 và G1 nguyên trạng.
- Luật006 0.7 §9 có 8 điều kiện ký nghiệm thu, tách khép RUN/G1/G2/G3, nợ không thay nghĩa vụ bắt buộc. Ba phiếu CAT-025 có manifest/binding riêng và hai ô ký; giữ nguyên phiếu P51/REJECT Claude. OpenAI ký bản sửa/kiểm kê có giới hạn; chưa ký nghiệm thu P46.
- Master Field stt8 trước rỗng, nay đọc 327 lượt dùng/18 Master → 233 định nghĩa theo toàn bộ nội dung định nghĩa (khác nghĩa/kiểu không tự gộp), thêm 2 field hãng và 7 field quản lý = 242. Trạng thái PG là Chưa xác minh, số cần tạo PG chưa biết. Dấu ? tại từng cột, chữ ký hai hãng cuối bảng; danh mục Master cùng nguồn đếm. Chưa phủ hết runtime sản phẩm G1: ghi TQT-P52-FIELD-COVERAGE, không nhận toàn bộ field đã đủ.
- Nợ: 18 dòng lịch sử được bổ sung đường xử lý; thêm D1/D2 chờ rà và FIELD-COVERAGE. OPEN chưa phải DEFERRED; không giả nhận nợ thay Owner. CAT-069 chỉ trỏ cycle.issues, phiếu nợ ghim hash toàn danh sách.
- Phát hiện thêm: audit_projection.last_checks của nguồn P51 lệch nhật ký audit P33; đã dựng lại projection từ nguồn audit đúng như CHECK006 yêu cầu. Không ghi đè nguồn audit hoặc giả kết quả mới vào cache. Kết quả P52 ở CAT-015; không DOT mới.
- Kiểm: TQT-a2c49283817b4306890a82761001a90e · CHECK006 PASS, các bộ 001–005 exit0; thời gian TQT-CHECK-001=0.655s, TQT-CHECK-002=0.389s, TQT-CHECK-003=5.023s, TQT-CHECK-004=48.483s, TQT-CHECK-005=37.549s. CHECK005 thêm8ca Git thật/giả/giờ sai/offline/strict/cùng hãng/khác hãng/thiếu hãng. Chạy CHECK005 mặc định trên khoGit TEST có milestone thật exit0. Chỉ TEST, không nghiệm thu MOW001. Lần tổng đầu lỗi AUDIT_PROJECTION_DRIFT, đã sửa nguồn chiếu và chạy lại PASS.
- Handoff Claude (Owner chuyển tay): đọc AGENTS/Bảng/README → P49 VÒNG3 → P52 → MOW-TH-006 §9. Rà delta D1/D2 bằng5phép V3.2 (8 ca đã tích hợp CHECK005) + kiểm mặc định với commit thật; xem hồ sơ001 và Master Field stt8; rà ba yêu cầu mới Owner. Không sửa nguồn chính. Nối VÒNG4 vào P49; tự ghi APPROVE/REJECT đúng binding/scope vào từng phiếu TQT-P52-CORRECTIONS, TQT-P52-DEBTS, TQT-P52-FIELDS. Ký nợ là đồng ý danh sách/phạm vi, không ghi nợ đã sửa. Nếu thiếu field/runtime còn chặn thì nêu rõ không ký hoàn tấtQT001; không ký thay Owner. Chưa chạyQT002, chưaPG/config. Khép lượt ngay, không giữ khóa chờ.
- Đọc lại nguồn/UI: commit `9a45e548e781bb37bd09b1e42eb36ba15c3f9ba0`, pushed; UI tx `d9dc0e745aec46c881af7a5124dc8da4`. 8 hash khớp; G1 và143events không đổi. Trình duyệt VPS đọc hồ sơ001 thấy3phiếu/GPT OK/Claude trống, MasterField thấy10cột động và dấu? ở từngcột, hai hãng cuối. Lỗi fontGoogle CSP có sẵn, không nớiCSP. Một lượt UI song song bịkhóa_screenshot; đã chạy tuần tự đạt, không giữlock.
KQ@TQT-P52-FIX XONG · 2026-10-13T14:37:48.880544+00:00 · phạm vi sửa D1/D2 + luật nghiệm thu/nợ/Field và công bố; không phải XONG QT001/P46. Dọn:0tệp tạm trênVPS,0process nền doP52,0gitlock tại lần đọc lại; giao dịch đãcommit/push. NhảVPS-GHI cùngcommit; STARTED giữnguyên. Claude/Owner quyết ở lượt sau, không có RUN chờ.

## P53 · Rút gọn006, hồ sơ và nợ/Field sau Claude VÒNG5
STARTED@TQT-P53-COMPACT 2026-10-13T15:29:22.823712+00:00 · Executor=Codex Host · Write_Path=workspace_transaction CAS · chỉ publish bản sửa và đọc lại; local đã chuẩn bị, không chạy002/PG.
- Tiếp nhận Claude P49 VÒNG5: P52 CORRECTIONS đã có hai hãngOK, DEBTS/FIELDS REJECT. Giữ nguyên chữ ký/lịch sử; không tự ký thayClaude hoặc chuyển chữ ký sang bản mới.
- N1–N4: ba trạng thái ngoài chuẩn→VERIFYING; TIMING/ITEMS/SKIP/CHANGE→VERIFYING; D1/D2→CLOSED với bằng chứngClaudeV5; thêm COMPACT/FIELDS/AUTOMATION, tổng24nợ. Mỗi mục có scope/đường xử lý; trạng thái schemaCAT069 sửa đúng8trạng tháiQT002. Chưa nhận tất cả nợ là được hoãn.
- F1–F3: 242−11 định nghĩa trùng nghĩa=231; tách1 miền state củaissue + đăng ký21 trườnghợpđồng/metadata=253định nghĩa/357lượtdùng. Giữ327lượtthiếtkế+9lượtP52. Cóold_to_new/usage_labels; không gộp target_version sản phẩm vớiSHAnguồn. Đây là sốđăngký, không phải253cộtPG mới; PG chưa xácminh, FIELD-COVERAGE vẫn mở. JEVgen-dec-1791905169-LnRtvvuK3R1HHtbjOMO6 đồngýapplication_id0.88; câuOwner/vendor khôngchắc0.41, Host tựchịutráchnhiệmgiữOwnerduyệtriêng.
- 006@0.8:71bước,7mốc (8/18/11/15/8/4/7),11nhómgộp giảm17+1resume, bảng87/87. M3rút lại: CP01.08ghi nguồnmộtlần, CP02.03kiểmnguồnấy. Quyền/phạmvi trước mở. Ghiantoàn có4nghĩavụriêng; không gộpACKbênnhận. CP06.04làOwnerduyệt, bỏ luậtreviewerAI khác hãng ở bước này. ReviewerCP03.05/CP05.03 vẫnkháchãng.
- Tựđộngchỉ làvai dựkiến; NO_COMMAND phảiMANUAL_ASSISTED/nợ. Khôngtuyênbố26bướctựđộnghay29dòngđãđo. Điều kiệnAPPLIES/NOT_APPLICABLE/UNKNOWN; NA chỉẩnkhicóreceiptmáyđúngviệc,UNKNOWNhiện. DONE bướcgộp phảikiểmđủmembers. Resumeởmốcthựctế, kiểmphiên/quyềntrướctiếptục. KhônglấyrevisionDONEcũ thayrevisionBLOCKEDmới.
- Hồsơ001: bảnxemgộp71, cómở87dònggốc, giữnguyên143events/G1. Khôngchuyểnphiênthựcthi hoặc tôxanhbảnmới. Overview71bướccó? tại8cột;11mụcvẫnthu/mở. SửavídụmãBS vàhướngdẫnserver_receiptscũ. QT0021.2chỉđổithamchiếu phùhợp006, chưa chạy.
- Kiểm: TQT-c492ee79f24a42e6b4427b3153bf23c6 PASS; TQT-CHECK-001=0.658s, TQT-CHECK-002=0.391s, TQT-CHECK-003=5.134s, TQT-CHECK-004=48.497s, TQT-CHECK-005=37.31s. CHECK005 thêm15ca compact (đúng/sai nghĩa vụ, mode/receipt, NA/UNKNOWN, thời gian, resume, revision) + kiểmFieldtrùng/327coverage; giữ19caP51+8caP52. LượtđầuCHECK003 bắtthamchiếuQT002cũ, đãsửavàchạytổngPASS. TấtcảTEST, chưa nghiêmthuviệcthật.
- Dùnglại005/006; cậpnhậthash,phiên,nhậtkýnângcấp,OpenAIreview đúngscope. 006ghim5UIinputs gồmOverview; khôngDOT/Mastermới. CAT015lưukếtquả, CAT229lưulượttool/JEV; audit_projection giữnguồnP33, khônggiảkếtquảvàocache.
- Handoff Claude doOwner chuyển tay: đọcP53, MOW-TH-006§10, P49VÒNG5; ràdeltaN1–N4/F1–F3, bảng87→71/11nhóm, phânbiệtvaiOwner, nghĩa vụgộp/nhánh/resume/máychưa cólệnh. ChạyCHECK006 --verify --vps-ui (có đủhash5UI), đọcOverview/hồsơ001/MasterField. NốiýkiếnvàoP49; tựkýAPPROVE/REJECT đúngbinding từngphiếuTQT-P53-CORRECTIONS/DEBTS/FIELDS. KhôngkýnghiệmthuQT001/P46 haythayOwner. Chưa chạyQT002/PG/config. XongKQ/nhảbusy, khônggiữkhóachờ.

- Công bố: workspacecommit `88449902e26cb72139c966e77fd939bd5611b4eb`, pushed; UItransaction `6b306669a55445c49d45be83738b9d48`. Đọc lại7hash khớp,71bước/253field/143events,0gitlock. TrìnhduyệtVPS: hồsơ001 thấy71bước; MasterField cónhãnởnơidùng/PGriêng/GPTOK/Claude trống. Lỗi fontGoogleCSP cũ khôngđổi. Overviewđãghimhash/cậpnhậtnguồn; lượtkiểmtrìnhduyệt cửaKnowledge trảBROWSER_UNAVAILABLE nên chưa xác minh hiển thị trang này, Claude cần xem lại khi ràdelta. Không nhận lỗi côngcụ là lỗiquytrình, không tuyênbố đãxemđạt.
KQ@TQT-P53-COMPACT XONG · 2026-10-13T22:22:32.369830+00:00 · chỉ phạm vi sửa/công bố006,nợ,Field/hồsơ; không là XONGQT001/P46. STARTEDgiữ nguyên. Khôngtạo processnền,lease,tệptạm trênVPS; giao dịchđãcommit/push,nhảVPS-GHI cùngcommit. KhôngPG/config/restart; chưaQT002.

## P54 · Sửa C1/F4 sau Claude VÒNG6
STARTED@TQT-P54-PUBLISH 2026-10-14T00:49:05.073201+00:00 · Executor=Codex Host · Write_Path=workspace_transaction CAS · bản local đã kiểm; lần xin cờ trước bị VERSION_CONFLICT nên không có RUN P54 mở trênVPS. Nay Owner giao công bố sau VPSC khép.
- Tiếp nhận Claude P49 VÒNG6: đồng thuận71 bước; P53DEBTS đã có hai hãngOK. C1 là lỗi thật: máy chưa có lệnh mà luật buộc biên nhận máy. Đã sửa 006@0.9 §11 và CHECK005, không đổi71 bước/87 nghĩa vụ.
- C1: NO_COMMAND cho AI đánh giá MANUAL_ASSISTED, có căn cứ/người/hãng/phiên; chưa rà giữUNKNOWN. Reviewer khác hãng tự ghi CAT015 ởCP05.03, APPROVE đúng assessment_binding; thiếu rà/cùng hãng/sai hồsơ/đổi căn cứ bị chặn. HAS_COMMAND vẫn bắt máy. Nghĩa vụ LUÔN không đượcNA. Áp cả nhánh và nghĩa vụ có điều kiện trong bước gộp. Bộ đánh giá thuộc nợAUTOMATION hiện có, không mở nợ trùng hay sửa danh sách24nợ đã ký.
- Dùng CHECK005 --assessment-binding để tạo binding, không nhập tuple tay. --validate-dossier trả manual_assessments, số thật từ hồsơ; không khai trước. Shared predicate giữa bộkiểm/UI; chỉ thu nhánh đã đủ căn cứ và review. Đây là HOST_CHECK, không giả máy chủ đã chứng thực danh tính/đánh giá nghiệp vụ.
- F4: quyết đủ24nhóm:12MERGE/12KEEP, mỗi nhóm có IDs/lýdo/người quyết. Giảm18định nghĩa:253−18+4trường quản lý=239định nghĩa/361lượt; giữ327lượt thiết kế. 4trường:review_ref,assessment_binding,collision_decisions,manual_assessments. MasterField hiển thị quyết định tại nơi dùng; CHECK005 chặn thiếu quyết định/thêmID vào nhóm đã ký. Khác vai/đối tượngthamchiếu giữ riêng. JEVgen-dec-1791936307-89p0GHGrRhChjUllvjQ5 thamkhảo; version_ref0.54 chưa chắc, Host quyết giữ riêng theo nghĩa. Chưa biết sốcộtPG cần tạo, nợFIELD-COVERAGE không tự đóng.
- UI: tiêu đề/chipOverview lấy step_count cùngnguồn, không còn87cứng. Preview100 cũ thành trang chỉ dẫn vềOverview, bỏscript hỏng và không tạo nguồn chuẩn thứhai. Giữ143events/G1. Hiện hai phiếuP54 mới cùng phiếuP53DEBTS đã hai hãngOK; cácREJECTcũ giữ lịch sử.
- Kiểm cuối: TQT-675fbba33d314917a74b307441e58a97 PASS; TQT-CHECK-001=0.643s, TQT-CHECK-002=0.393s, TQT-CHECK-003=5.079s, TQT-CHECK-004=48.326s, TQT-CHECK-005=37.302s. Thêm13ca C1/F4/UI, gồm ca hoàn tất71bước với27nhánh đánh giá tay đãrà; thiếu/sai/cùnghãng/đổi chứng cứ/đãcólệnh/UNKNOWN/LUÔN đều chặn. Đây là TEST, không nghiệmthu việc thật. Giữ19caP51/8caP52/15caP53; không thêmDOT.
- Handoff Claude (Owner chuyển tay): đọcP54, 006§11 và P49VÒNG6; chạy CHECK005 với5UIinputs đúnghash. Có thể lấy inputs qua workspace_read vào snapshot rồi dùng CHECK006 --verify --ui-adapter <process-work-master-v1.js> --master-registry <definition-master-registry-v1.js>, tránh phụ thuộc lượt tải --vps-ui bịtreo trongV6. Rà C1/F4/tiêuđề/preview; không mở lại cấu trúc71bước hoặc24nợ đã ký. Nối ýkiến vàoP49; tự ký hai phiếu TQT-P54-CORRECTIONS/FIELDS đúngbinding/scope. Không ký thayOwner, chưaQT002/PG. Xong khépRUN/nhảcờ ngay.

- Công bố P54: commit `17727296d3a837fe97b7a1ab0212022635f9dbde`, pushed; UI transaction `28c1737e070c4a34b83aa3cc8328cc71`. Đọc lại 6 hash nguồn/UI và nội dung COLLAB khớp ứng viên đã kiểm; 71 bước, 239 Field, 24 quyết định, 24 nợ. Hồ sơ chuẩn HTTP200 thấy hai phiếu P54 OpenAI OK/Claude trống; P53-DEBTS giữ hai hãng OK. Preview cũ HTTP200, chỉ liên kết về Overview, 0 lỗi console. Overview: công cụ trình duyệt trả BROWSER_UNAVAILABLE; đã kiểm nguồn/syntax nhưng chưa xác nhận hiển thị lượt này, đề nghị Claude kiểm khi rà. Không nới CSP font cũ.
KQ@TQT-P54-PUBLISH XONG · 2026-10-14T00:55:39.040171+00:00 · chỉ sửa/kiểm/công bố P54, không nghiệm thu QT001/P46 và chưa chạy QT002. STARTED giữ nguyên. Git sạch, 0 gitlock khi đọc lại; không tạo process nền/container/lease/tệp tạm VPS. Trả VPS-GHI cùng commit; không giữ cờ chờ Claude. NEXT_TRIGGER=CLAUDE_P54_REVIEW_RECORDED.

## P55 · Duy trì thanh 4 Mẹ + Master
STARTED@TQT-P55-NAV 2026-10-14T02:30:00.761458+00:00 · Codex Host · Owner yêu cầu duy trì thanh dưới ở mọi UI đang dùng. SSOT thanh: /ui-preview/mcp-writes/eco-nav.js; Overview: work/tools-quy-trinh/view.html qua /knowledge/modules?task=tools-quy-trinh&view=content&section=over-view. Không PG/config/restart.

- Đã nối Overview vào eco-nav.js hiện hữu, không chép menu. Sửa liên kết tuyệt đối/target _top để dùng đúng từ trang nhúng; chỉ phục hồi instance thanh hiện hành khi nội dung vẽ lại. Rà 29 URL menu: có thanh hoặc kế thừa mẫu cha. Hồ sơ chuẩn đã có thanh; bản nội dung Overview sau sửa HTTP200, thanh ở y736/800, đủ6 nút, 0 console errors; trình duyệt mở menu MOW, các7liên kết đúng /ui-preview/mcp-writes/ và _top, sau tự đồng bộ đúng1thanh. Lượt đầu thấy2thanh do callback phiên cũ, đã sửa/đọc lại bản cuối.
- Commit nguồn `331ce559f052958f71fb3134dc9f347aaf106f3f`; UI transaction cuối `06d6e27a90c5414884bcfaeabd66b156`; hash eco-nav `f57acaff6b33cbc2f5dfc06d97d60ec87ee73dddc586e02dcd9219dd08182b26`. Syntax PASS, đọc lại hash/loader khớp. Không đổi catalog, phiếu kýP54, CHECK005 hoặc nghĩa vụ71bước. README bổ sung kiểm .eco-bar trong lượt ui_inspect hiện hữu, không DOT mới.
- Giới hạn riêng đường Knowledge: trình duyệt Mac thấy khung ngoài báo chưa có snapshot; sync-status trênVPS fresh đúng331ce559. Đã kiểm trực tiếp URL nội dung xuất chuẩn có thanh; chưa kết luận lỗi khung ngoài đã hết. Ghi tạiP55 để rà tiếp đường nạp, không sửa ngoài phạm vi thanh.
KQ@TQT-P55-NAV XONG · 2026-10-14T02:34:14.977021+00:00 · phạm vi thanh chung và hướng dẫn; không nghiệm thu QT001. Không process nền/tệp tạm VPS do lượt này; gitlock0 khi đọc lại; trả VPS-GHI cùngcommit, đóng tab kiểm. NEXT_TRIGGER=CLAUDE_P54_REVIEW_RECORDED.

## P56 · Thanh dưới mặc định cho mọi Master/UI
STARTED@TQT-P56-NAV-DEFAULT 2026-10-14T02:38:54.209152+00:00 · Codex Host · Owner: “Bạn đưa thanh này mặc định vào tất cả các master list, tất cả mọi nơi mà chúng ta đang làm.”
- Nguồn chung: master-list.js có CSS .ml-embedded .eco-bar display:none; design-navigation-v1.js chưa nạp thanh dưới. Sửa tại mẫu dùng chung; giữ menu eco-nav.js hiện hữu. Không PG/config/restart, không sửa dữ liệu/chữ kýP54.

- Đã sửa tại master-list.js và design-navigation-v1.js: tự nạp eco-nav chung khi chưa có; bỏ CSS ẩn .eco-bar trong ml-embedded. Mọi Master kế thừa và mọi UI dùng thanh thiết kế được mặc định có thanh dưới, không cần gắn riêng; giữ menu/nguồn/nhãn hiện hữu. Master tổng hợp dùng tqt-master-adapter kế thừa mot-master nên cũng được phủ; trang quy-trinh-detail chuyển về Master hiện hữu.
- UI tx `a33e5e325a844138be148c63c2603519`; docs commit `5335134084a7c076b48a2851d3d0c6e63c43f741`. Hai JS node --check PASS; hash đọc lại khớp, không còn selector ẩn thanh. Browser Mac Master DEF00.1 embedded=1: đúng1thanh, display:flex, bounds y656.73 h47.27 trong viewport720. Master Duyệt thiết kế ui_inspect HTTP200, thanh y736.73/800 đủ6nút. Cảnh báo fontCSP cũ giữ nguyên. Không đổi catalog/phiếu P54/luật006/bộkiểm; đây là sửa mẫu UI chung.
KQ@TQT-P56-NAV-DEFAULT XONG · 2026-10-14T02:41:54.312361+00:00 · mặc định thanh dưới tại mẫu Master và UI thiết kế; không nghiệm thu QT001. Không process nền/tệp tạm VPS; gitlock0, đóng tab kiểm và trả cờ cùngcommit. NEXT_TRIGGER=CLAUDE_P54_REVIEW_RECORDED.

## P57 · Lối vào Master Field
STARTED@TQT-P57-FIELD-LINK 2026-10-14T02:45:27.955Z · Codex Host · Owner yêu cầu thêm Master Field ngay dưới Master Tool tại master-home-v1.html, thụt3cấp kiểu cây. Dùng Master hiện hữu definition-master-v1.html?stt=8; không tạo danh mục mới.
- Đã thêm liên kết Master Field ngay dưới Master Tool, margin-left84px = 3 cấp28px theo cây hiện hữu. URL chuẩn stt=8, không tạo Master mới; giữ thanh4Mẹ. UI transaction851d46fdb04a416193052e4ab8d7e9bb; ui_inspect HTTP200, thấy thứ tựDOT→Tool→Field và đúngURL, 0consoleerror.
KQ@TQT-P57-FIELD-LINK XONG · 2026-10-14T02:46:25.245Z · trả cờ cùngcommit; không tạo process/tệp tạm VPS. ChưaQT002/PG. NEXT_TRIGGER=CLAUDE_P54_REVIEW_RECORDED.

## P58 · Hoàn thiện sổ việc cần xử lý tiếp
STARTED@TQT-P58-DEBTS 2026-10-14T03:35:33.815325+00:00 · Codex Host · Owner giao thêm dòng dướiField và ghi đủ sổ, GPT rà/ký rồi Claude kiểm. Phạm vi nguồnTQT và tham chiếu cũ đã kê; không tự mở nghiệm thuQT001/PG.
- Rà nguồn: 24issueQT001 +16findingsP34–38 +3findingsP45 +14findingsG1 =57. BảncacheCAT06928dòng gồm4alias P46 trùng; không xóa lịch sử, UI bỏ alias khi issuechuẩn có. 28dòng cache thiếu problem và F01 trạng tháiFIXED cũ được sửa bằng đọc issuehiện hành, không chép lại. Thêm17yêu cầu đối chiếu sổtrướcP34 (7TQT/10MOWTools, chưa cắt chuyển), P55Knowledge thiếu snapshot và P58projection cầnClauderà. Tổng76dòng/76mã;43issue tại cycle,33findings nguồnkhác. Đây là danh sách có phạmvi, không tổng việc còn mở/không toànserver.
- CHECK005 hiện hữu nângP58.1: đủ trường hiển thị, mỗiissue1dòng, trạng thái/nội dung/việc tiếp đúngnguồn, thêm/đổi nguồn tự truyền. Lượtđầu caTEST thiếu khôi phục liveCycleBindings nênlỗi; đã sửa fixture và chạy lại cảCHECK005 PASS, giữP51/52/53/54 và G1. TESTkhông nghiệmthuQT001. HASH trong MasterDOT, kếtquảCAT015/TQT-P58-CHECK.
- Lối vào đặt ngay dướiMasterField/cùng mh-field-leaf. Hai cột cuốiGPT/Claude lấyphiếuCAT025 TQT-P58-DEBTS; CodexAPPROVE scope/binding cụthể, Claude trống. Giữ nguyên24issue/chữkýP53,143events/G1, P54ClaudeAPPROVE V7. PhiếuP53 nay là lịch sử, phiếuP58 hiện hành cho sổ mở rộng. Không kýxong nhữngviệcchưaxong.
- Handoff Claude (Owner chuyển): đọcP58/README và diff; mởhome→Việc cần xử lý tiếp; đốichiếu76mã với4nguồn/17thamchiếu+2mục bổsung, kiểm nguyên24issueP53/143events/G1; thửđổi state/next nguồn, thêmissue mới và aliascũ chỉ có1dòng. DùngCHECK005 với5UIinputs đúnghash; không cần chạy lại bộnặngkhác. NốiVÒNG8 vàoP49, tựkýAPPROVE/REJECT TQT-P58-DEBTS đúngbinding/scope, khôngkýthayOwner/khôngnghiệmthuQT001. Nếu còn thiếu nguồn nêu đúng nguồn/mã, không kýđầyđủtoànserver. Xongnhảcờngay.
- Công bố: commit `47a804be9c86991295e5570fd6c6d7843255e5f1` pushed; UI transaction `7bb61028c2974d6a87116c467918fc2b`. Đọc lại trang chủ HTTP200/0 lỗi console: đường dẫn dưới Field đúng CAT-069?. Sổ thật HTTP200 hiển thị76dòng, đủ mô tả/người nhận/trạng thái/việc tiếp và hai cột ký; GPT hiện Codex Host, Claude trống. Cảnh báo font CSP cũ không đổi. CHECK005 chạy lại toàn bộ PASS.
KQ@TQT-P58-DEBTS XONG · 2026-10-14T03:40:05.908736+00:00 · hoàn thiện/kiểm/công bố và GPT ký phạm vi sổ TQT đã kê; 17 tham chiếu cũ vẫn cần đối chiếu nguồn, không tuyên bố đã xử lý xong việc nợ hay phủ toàn VPS. STARTED và lịch sử giữ nguyên. Không tạo process nền/lease/container/tệp tạm trên VPS; trả VPS-GHI cùng commit, không giữ cờ chờ Claude. Chưa PG, chưa nghiệm thu QT001. NEXT_TRIGGER=CLAUDE_P58_DEBTS_REVIEW_RECORDED.

## P59 · Mã việc và liên kết sổ cần xử lý tiếp
STARTED@TQT-P59-IDS 2026-10-14T03:53:34.458989+00:00 · Codex Host · Owner giao hai cột mã và làm rõ luật mã/duyệt lần đầu. SSOT UI process-work-master-v1.js; nguồn record_id/work_id hiện có, không thêm mã thay thế, không PG.
- Công bố nguồn/luật commit e2d3118e608282bb25635530ec8df93cf16ce542; UI transaction667fe0136c754f2ba34940969a80f73c. Hai cột dùng record_id/work_id đã có, không sinh mã mới hoặc sửa chữ ký. Hash adapter đã cập nhật tại registry.
- Kiểm trực tiếp hàm hiện hữu: 2mã việc duy nhất,76dòng,60liên kết hợp lệ/16trống do nguồn P34 chưa khai work_id. Không gán đại16dòng vào TQT-VIEC-001; cần rà nguồn/khai đúng hồ sơ trong lượt tổng hợp Claude tiếp. Syntax PASS; UI cả hai trang HTTP200 hiện đúng cột mã và dấu ?. Cảnh báo fontCSP cũ giữ nguyên. Đây là kiểm sửa UI, không nghiệm thuQT001.
- AGENTS/README đã ghi luật hai mục phải có danh sách, Master/bản ghi có mã riêng ổn định; User duyệt lần đầu đúng mã/phiên/phạm vi/bằng chứng, AI không tự duyệt thay. User duyệt không đóng băng thiết kế. Cơ chế nút và cổng cưỡng chế duyệt lần đầu chưa triển khai; đưa vào lượt rà tiếp, không coi các Master cũ đã được User duyệt.
KQ@TQT-P59-IDS XONG · 2026-10-14T03:55:55.666687+00:00 · đúng phạm vi hai cột mã và luật; 16liên kết cũ còn thiếu đã kê ở trên. Giữ STARTED; trả cờ cùngcommit, không process nền/lease/tệp tạm VPS. ChưaPG. NEXT_TRIGGER=OWNER_SENDS_CLAUDE_FINDINGS.

## P60 · VÒNG 8: mã, Field và hợp đồng thực hiện
STARTED@TQT-P60-PUBLISH 2026-10-14T04:38:55.612957+00:00 · Codex Host · công bố bản đã kiểm local; đường nguồn UI process-work-master-v1.js / qtth006-overview-v1.js / master-list.js; luật tại MOW-TH-006.md; dữ liệu trong view.html. Không PG, không QT002.
- Phạm vi Owner mới nhất: chuẩn hóa ngoài PG; đã phản biện Q1/D5 ở P49 trước triển khai (f8d0b754). DESIGN đếm thiết kế dự kiến, không đòi PG để nghiệm thu thiết kế. Chưa có căn cứ số cột PG thực sự cần tạo.
- C/D: mã Master chính thức không dấu trạng thái, bí danh/kho lịch sử giữ nguyên; CV là mã việc ngắn, FLD ID ngắn. 239 định nghĩa cũ chuyển mã, thêm 11 định nghĩa quản lý =250; không tạo PG. Mã DB riêng/không trùng; tên hiển thị ưu tiên30, tối đa60 để không cắt mất nghĩa. UI có nguồn gốc, mô tả, vòng đời, bí danh và ô ký. Master chưa có bằng chứng User duyệt hiện chưa xác minh, không tự tích.
- B/E: 5 ô dự thảo CV-001 chưa Owner duyệt. Thẻ3 dòng tính từ bằng chứng, không xanh vì TEST/G1 cũ. 71 thẻ bước có9 câu tại dấu?; đường chính kiểm phụ thuộc, nhánh xử lý tại điểm phát sinh. CHECK005 có --validate-control, --milestone-report, --validate-governance-before; --validate-dossier vẫn kiểm biên nhận và hợp đồng. HOST_CHECK, chưa cưỡng chế mọi endpoint/định danh máy chủ.
- F/A/G: CAT-016 dùng lại cho9 bản ghi sửa, lịch sử truy hồi chưa đủ giờ/kiểm ghi HISTORICAL_UNVERIFIED; không bịa. 006 viết lại theo chủ đề/trang đầu/71 bước/luật chung; phiên0.5–0.9 và143 sự kiện/G1 giữ nguyên. Hướng dẫn ký chỉ đúng phiếu CAT-025, ký chat không thay phiếu. Giờ hiển thị Việt Nam, nguồn ISO giữ nguyên.
- K: CHECK006 --ui-snapshot chạy độc lập với5 đầu vào ghim hash. Tổng PASS trên bản sao:001 0.707s,002 0.448s,003 5.448s,004 49.657s,005 39.425s. CHECK005 kiểm lại sau các thay đổi UI/metadata cuối;27 ca mới PASS (không nghiệm thu QT001). Lỗi thử ban đầu: fixture cũ dùng luật mới; ca âm nhân lịch sử gây vượt512MB; đã sửa fixture, không tăng bộ nhớ. 10 bước DOT dự kiến tại governance.automation_plan trỏ nợ AUTOMATION; chưa có lệnh trọn bước.
- Phiếu mới TQT-P60-CORRECTIONS chỉ duyệt bản thiết kế/quy định/bộ kiểm; không nghiệm thu QT001, không duyệt5 ô thay Owner. Chữ ký P54/P58 giữ lịch sử. Còn mở: Claude VÒNG9; Owner duyệt5 ô; 16 liên kết nguồn cũ CAT069; biên nhận thiếu trong lịch sử truy hồi; thử AI mới/PG/định danh chữ ký/tách tệp lớn.
- Handoff Claude: đọc P60 + README hiện hành + 006 trang đầu; rà V8 A–K theo phần Host phản biện. Chạy CHECK006 --verify --ui-snapshot bằng5 tệp đúnghash; kiểm trang CAT227/CAT069/Field/Overview, thử sửa sai qua CHECK005. Ghi VÒNG9 vào P49 và tự ký APPROVE/REJECT TQT-P60-CORRECTIONS đúngbinding/scope tại CAT025. Không ký bằng lời trong báo cáo; không ký thayOwner/không coi TEST là nghiệm thu. Khép lượt, trả cờ ngay.

### P60 · Đọc lại và khép lượt 2026-10-14T04:53:00.897221+00:00
- Bước 1/3: công bố nguồn 3d49f42b; bộ nạp/mã được ghim ở 4b3727cd. UI giao dịch tqt-p60-ui, tqt-p60-home-code, tqt-p60-loader-alias. Mã nguồn trên VPS là chuẩn.
- Bước 2/3: phát hiện trên trình duyệt đường CAT-227 chưa qua bộ nạp cũ; sửa nhận cả mã chuẩn/bí danh, 56 ca + mã lạ bị từ chối. Đọc lại CV-001: CAT-227, ba dòng đỏ đúng thực tế, hai ô ký; Field 250 với Tên hiển thị/Mã DB/Nguồn/Vòng đời/?; Overview 71 bước và thanh 4 Mẹ còn nguyên. Hai lượt ui_inspect không có browser; dùng trình duyệt thật Codex IAB để kiểm, không coi lỗi công cụ là lỗi sản phẩm.
- Bước 3/3: CHECK006 cuối PASS run TQT-af16c7b99aa6421aa3fb0ae1d0436df2; hash nguồn 0b37ace124e663d487d80a7f3c8c8b65b2e9ebb116a9c68674e7c168e5effcbc; 001/002/003/004/005 = 0.696/0.437/5.462/53.606/39.225 giây; 27 ca P60 và các ca hồi quy đạt. Bằng chứng đầy đủ work/tools-quy-trinh/evidence/TQT-P60-checks.json. Chữ ký OpenAI tại CAT-025/TQT-P60-CORRECTIONS, binding cdbc013ce9003271222d3c0b042140da00142f028a16bfe67fd1f7aec01cc856; Claude/Owner trống. Không lấy TEST thay việc thật.
- ĐÈN 04:50Z: 19 xanh · 3 đỏ: #11 Disk Usage (VPSC), #21 Hermes (HJW), #22 Protection Guard (TQT/HJW, drift có trước). Đây là duyệt thiết kế ngoài PG; chưa nghiệm thu runtime/protection toàn hệ, không tự sửa baseline/restart.
- KQ@TQT-P60-PUBLISH DỪNG 2026-10-14T04:53:00.897221+00:00 · đã công bố và kiểm P60; khép sạch để Claude rà, chưa có đồng thuận hai hãng và Owner. Dọn: 0 tiến trình/khóa/container/tệp tạm tạo trên VPS; báo cáo kiểm là bằng chứng bền trong repo. Bản sao kiểm local không là hồ sơ chuẩn.
- Phần còn mở có nguồn: 16 liên kết việc cũ chưa xác minh tại CAT-069; 10 bước tự động dự kiến trỏ nợ TQT-P53-AUTOMATION; lịch sử sửa thiếu biên nhận vẫn HISTORICAL_UNVERIFIED; PG/định danh ký/server enforcement/tách tệp lớn theo nợ hiện có. Chưa tuyên bố tất cả các điều kiện nghiệm thu V8.2 đã đạt.
- Claude: rà VÒNG 9 trên P60 (gồm bổ sung bộ nạp), ký APPROVE/REJECT đúng phiếu/binding/scope, nhận xét vào P49. Không chỉ ký trong chat. Chưa chạy QT002/PG.

## KQ P61 · Codex đối chiếu và ký REJECT bản đang sống · 14/10/2026
- Hai phiếu P60/P58: OpenAI đã rút kết luận thông qua bản hiện hành bằng review REJECT nối sau, cùng binding/phạm vi; không sửa hoặc xóa chữ ký cũ. Anthropic đã REJECT VÒNG 9. Hai bên chưa thông qua quy trình chuẩn.
- Ứng viên P61 đã sửa và kiểm local: CHECK006 PASS 001–005; 36 ca chữ ký, 29 ca Field, 11 ca fixture dừng sớm và 3 ca chữ dính. Ca cũ vẫn đạt; G1/143 sự kiện giữ nguyên. Chi tiết evidence/TQT-P61-draft-checks.json.
- Điều chỉnh đã ghi trước sửa: Hộp dùng lại CV-001; REJECT khép lượt rà nhưng chặn chuẩn; Owner/historical/ngoài phạm vi giữ riêng; không gán 250 Field thành số mới. K9.4 còn 24 nghĩa nghiệp vụ cần đối chiếu tại FIELD-COVERAGE.
- DỪNG công bố: VPS-GHI đang do VPSC-N2C-CODE-BACKUP-GPG-20261014-01 giữ. Không sửa UI/runtime, không lấy hoặc trả cờ của VPSC; chưa kiểm UI thật P61, chưa ký APPROVE ứng viên.
- Gói ứng viên duy nhất: /Users/nmhuyen/Documents/Codex/2026-10-14/ch-ng-ta-ang-d-phi/outputs/TQT-P61-candidate.zip. Có nguồn/fixture/biên nhận để giải nén vào nơi thử và chạy CHECK006 mặc định; chưa là SSOT runtime hoặc chuẩn. Khi công bố phải đọc lại nguồn/hash/cờ, giữ các review vừa ghi, CAS tại nguồn sống; không deploy mã từ GitHub.
- NEXT_TRIGGER=VPS-GHI_TRONG; công bố và kiểm UI thật rồi mới ký OpenAI trên bản công bố; sau đó Owner chuyển Claude mở Hộp chờ ký của Anthropic. Không PG/QT002; không giữ process để đợi.
KQ@TQT-P61-V9 DỪNG · 2026-10-14T08:09:09Z · VPS_BẬN_VPSC_N2C · đã khép rà và chuẩn bị ứng viên, 0 RUN/cờ TQT.

## Tiếp tục P61 · cờ VPSC đã trả
STARTED@TQT-P61-PUBLISH 2026-10-14T08:22:19Z · executor=Codex · read-gate: root dfc4fb06, VPS-GHI trống; task/P49 và hash sống đã đọc lại. Ứng viên P61 PASS và đúng scope; giữ review REJECT P60/P58 vừa ghi. Không PG/QT002.
- Áp P61: SAME_COMMIT · nguồn/code và fixture đã CAS cùng lượt; UI transaction e064ebdae60543f4ade8d23e545c81ff. Chưa ký APPROVE P61, đang đọc UI thật. Không PG/QT002.
KQ@TQT-P61-PUBLISH DỪNG · CỜ_BỎ_QUÊN · 2026-10-14T10:27Z · ghi bởi Claude Code CLI theo D04 + HUMAN_DIRECTIVE-07 của việc gemini-join-workflow (Owner ủy quyền trực tiếp, Host GPT ghi `316e231`); không phải chữ ký Codex, không phải nghiệm thu P61.
- Bằng chứng (chỉ đọc, 10:22–10:26Z): (1) phiên Codex chạy P61 (root turn `01a13940-5788-7672-b8be-254f00e6a975`) kết thúc `turn_aborted · reason=interrupted` lúc 09:14:15Z (ngắt có chủ đích), các luồng con cùng lúc; không sự kiện mới sau đó. (2) Commit P61 cuối `bf3ba8d` 09:10Z; Bảng 16:45 +07 ghi P61 đóng băng từ 16:00 và yêu cầu nhả cờ. (3) VPS: 0 tiến trình tqt/p61; 0 tệp đổi trong thư mục hồ sơ VPS của việc này và vùng UI mcp-writes sau 09:15Z (ghi cuối 08:27:55Z); log agent-data 0 dòng ghi codex/gpt-web sau 09:14Z; 12 phiên ssh root đều là MCP Graph chỉ đọc.
- Giữ nguyên toàn bộ thành quả P61 (nguồn/code/fixture/UI tx e064ebdae60543f4ade8d23e545c81ff, review, gói ứng viên); không dừng/xoá tiến trình hay artifact nào; ký APPROVE P61 và bước kế vẫn là việc của TQT. Dòng VPS-GHI gốc trả `trống` ngay sau commit này bằng CAS.

## P62 · GPT Chat · B0 CHỐT / READY node B1+B2 · 15/10/2026
Ghế: GPT Chat (Owner giao chốt lệnh B1+B2) · Bước/vòng: B0 cuối 1/1 · Based_on: PROMPT.md last-touch `c286349b28374b906cf8f6d1ae56180d538a04df`, Claude phản biện ACCEPT tại P49 V12.6 (`9dc1bb4`), Owner gật cả ba theo HUMAN_DIRECTIVE@TQT-OWNER-20261015-Q1Q2R48 · Scope: `work/tools-quy-trinh/` B1+B2 NHÁP, không G2.
Kết luận: ACCEPT — ưu tiên **hai UI thật nhìn được** của bàn làm việc, rồi QT001 UI–Field–Config theo MOW-TH-007; GitHub SSOT, DOT ghi, Directus xem, giữ kết quả G1/P61. Q1/Q2/R48 được Owner duyệt; không sửa PROMPT sau V12.6 để khỏi mở vòng ký lại. Cờ VPS-GHI phải kiểm LIVE tại S0, không suy trạng thái từ bản ghi này. Điều 30/31, Guard và quyền xem giới hạn giữ nguyên.
**READY@c286349b28374b906cf8f6d1ae56180d538a04df** · RUN_ID=TQT-B12-DRAFT-ZONE-20261015-01 · Executor_Surface=Claude Code CLI (Mac, Owner kích hoạt tay) · Write_Path=workspace_* gateway (repo) + DOT/script-wrapper theo R41 (Directus/PG) + Config Guard apply-v0. Trạng thái `DRAFT` ở header PROMPT là nhãn trước khi Owner gật; từ thời điểm READY này, `COLLAB` là nơi xác nhận quyền RUN theo A6. **Chưa STARTED, chưa RUN; không tự kích hoạt.**
Áp: SAME_COMMIT.

## P63 · GPT Chat · CHỐT R2 SAU GEMINI ACCEPT · 15/10/2026
Ghế: GPT Chat (Host READY B1+B2 do Owner giao) · Bước/vòng: B0 chốt cuối, không vòng kiến trúc mới · Based_on: PROMPT last-touch `914580c442c57e74e2c462a7ca6fc1a823027e84`, Claude P49 V12.7, Gemini đọc r2 tại HEAD `43450f7b23ddb5f731abea984c60da04e7a827d4` và ACCEPT (Owner chuyển vào chat) · Scope: `work/tools-quy-trinh/` B1+B2 NHÁP; không G2, không RUN.
**Kết luận: ACCEPT, KHÔNG SỬA PROMPT r2.** G1 chỉ có ba mục tiêu: UI, hợp đồng Field, Config khả thi; 5 bảng lõi + MOW-TH-007 đủ để thiết kế, Guard chỉ kiểm lỗi an toàn, THIẾU lưu/hiển thị và kiểm độ phủ nghiêm cho **từng quy trình khi nghiệm thu**. B1+B2 chứng minh 5 bảng + hai bookmark + màn/form thử, nạp 3 bản ghi màn QT001 nhưng **chưa tuyên bố cả ba là UI hoạt động hoàn chỉnh**; B3 mới dựng/rà đủ UI QT001. Không tự viết UI HTML/JS, không tạo bảng Master hàng loạt, không phục hồi 71 bước cho G1.
**Lưu ý thực thi trong phạm vi PROMPT đã duyệt, không mở scope:** Directus `/schema/snapshot` kiểm cấu trúc Collections/Fields/Relations; riêng `directus_presets`, dashboards/panels, account/policy/permissions là metadata/dữ liệu hệ thống cần đối chiếu bằng API/sổ sở hữu và tài khoản chỉ-xem thật ở S3–S6, không dựa duy nhất vào schema snapshot. Phân biệt CHẶN vs THIẾU, chỉ `kiem --du <mã>` mới chặn độ phủ; so SHA nguồn trước khi áp; xoá/dựng lại chỉ tài nguyên TQT NHÁP owned, giữ nguyên production. Đây là cách xác minh yêu cầu Luật 5 và S5–S7 hiện hành, **không phải một bước kiểm mới**.
**READY@914580c442c57e74e2c462a7ca6fc1a823027e84 (LỊCH SỬ · MẤT HIỆU LỰC 15/10 17:40 do Owner đổi phạm vi)** · RUN_ID=TQT-B12-DRAFT-ZONE-20261015-01 · Executor_Surface=Claude Code CLI trên Mac (Owner giao thủ công) · Write_Path=workspace_* gateway (tài liệu GitHub) + dot-master-apply/DOT qua GSM + Config Guard apply-v0 (runtime) · Reviewer = Claude (P49 V12.7); Gemini ghế dự bị góp ý, không thay quorum. S0 bắt buộc kiểm LIVE mọi cổng, không suy READY đồng nghĩa RUN hoặc an toàn runtime đã PASS.
**OWNER CHƯA CHO CHẠY**: giữ nguyên PROMPT r2; chờ chỉ đạo tiếp, không STARTED, không phát RUN. Áp: SAME_COMMIT.

## P65 · GPT Chat · OWNER ĐÍNH CHÍNH G1: SỔ MASTER PHÁT SINH + ĐỐI SOÁT · 15/10/2026 17:40
Owner trực tiếp bác cách coi **5 Collection lõi đủ để làm G1** và bản triển khai MOW-TH-007 r2: phát sinh nào cũng cần Master List tương ứng, mã, bản ghi, số lượng cần/đã/thiếu và quan hệ nơi dùng; thay đổi phải rà tất cả nơi bị ảnh hưởng. Ví dụ 5 phát sinh mới chỉ ghi 3 phải báo thiếu 2; 10 Field cần dùng phải phân biệt cũ/mới/chưa đăng ký. Đây là cập nhật mục tiêu/phạm vi thật (AGENTS A0/DROOT30), **PROMPT r2 và READY@914580c4 cũ không được chạy**; chưa STARTED, chưa mutation. Kết quả rà source: `definition-master-registry-v1.js` có 28 ML-DEF + 1 Master tổng hợp; `field-origin-snapshot.json` có 18 nhóm thiết kế Master (một số mã *, ? chưa xác minh thực trạng). **Không kết luận số Collection vật lý/đủ nội dung trước khi đo Directus thật.** R49–R52 là phương án hiệu chỉnh để Host/Claude rà một vòng và Owner chốt, không phải READY. Giữ nguyên các quyết định Q1 tài khoản chỉ-xem, Q2 DOT lâu dài, GitHub SSOT/Guard; chỉ hiệu chỉnh phạm vi G1/007/roadmap và PROMPT sau khi thống nhất. 0 RUN, không sửa VPS/Directus/PG.
HUMAN_DIRECTIVE@TQT-OWNER-20261015-REGISTER-ALL EFFECTIVE · task=tools-quy-trinh · scope=G1_DIRECTUS_NHAP · step=B0/ROADMAP/MOW-TH-007 · recorded_by=GPT Chat · quote=“Tóm lại bất cứ một cái gì khi nó phát sinh ra thì chúng ta phải ghi nó vào master list tương ứng.” · text=Không giới hạn 5 bảng lõi, bắt buộc sổ đúng loại và số cần/đã/thiếu, quan hệ tác động thay đổi; prompt cũ chưa OK · audit=Owner trực tiếp trong chat 15/10/2026.


## P64 · GPT Chat · RÀ LẠI SSOT CHO NGƯỜI MỚI ĐỌC · 15/10/2026 17:26 +07
Owner giao GPT Chat rà và viết rõ mục tiêu/nguyên tắc/cách làm/đồng thuận; chỉ sửa cách tổ chức thông tin trên `COLLAB.md` và cửa đọc `README.md`, **không đổi PROMPT r2/READY**, không giao RUN. Đã giữ nguyên ba mục tiêu gốc, cập nhật phạm vi G1 mới ở ô 1–2, đánh dấu phương án “100+ bảng trước” là lịch sử; R40 sửa nhầm lẫn “thiếu thì không lưu” thành “thiếu được lưu, CHẶN lỗi an toàn”; tách đường hồ sơ 71 bước khỏi G1 nhưng giữ R30/R36/R37 cho 007, 005/006 không phải thủ tục G1. Đồng thuận: Owner Q1/Q2/MOW-TH-007; Claude P49 V12.7; Gemini vòng cuối ACCEPT; GPT P63. Người đọc mới xem `README.md` trước; chi tiết kiểm R40–R48, khi Owner phát RUN mới đọc `PROMPT.md` S0–S7. 0 RUN, không tạo hoặc sửa Directus/PG/VPS.



