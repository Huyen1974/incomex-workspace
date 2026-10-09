# COLLAB — tools-quy-trinh
Tên việc: Tools quy trình — làm theo quy trình ra được sản phẩm

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner chốt mục tiêu ô 1–2 ngày 08/10/2026 07:16 (D04/D05); D06 trước đây giao GPT Chat; sau đó Owner trực tiếp giao Astra Codex làm Host ngày 08/10/2026 (D17, thay phân công cũ). Giữ nguyên lời Owner trong ô 1–2; ngày 09/10/2026 Owner yêu cầu Host bổ sung làm rõ mục tiêu và rà lại Kiểm soát, không viết lại mục tiêu gốc. Quyết định Owner mới ngày 09/10/2026 giao GPT Chat làm Host lại để tổ chức tab Over view (D19), supersede D17 đối với Host hiện hành; mục tiêu ô 1–2 giữ nguyên.
Host: GPT Chat — phiên Owner chỉ định trực tiếp ngày 09/10/2026 (D19)
Host_ID: OpenAI-main
Host_Surface: GPT Chat · cuộc trò chuyện hiện tại của Owner
Xác nhận bổ sung: Owner giao trực tiếp dựng ma trận và UI câu hỏi, giữ nội dung cũ, tiếp nhận ý kiến qua Host. Chỉ đạo này thay phần Host/PROMPT READ-ONLY cũ trong phạm vi tools-quy-trinh.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-09 · GPT Chat · P17
- 🎯 Mục tiêu: việc gì lặp lại cũng có quy trình chuẩn → người mới, phiên AI mới làm theo là ra đúng sản phẩm, hướng tới muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể. Vì sao: người nhìn rõ mới cùng phát hiện và sửa được vấn đề.
- 🏁 Xong khi: đạt tiêu chí ô 2; quy trình được làm theo ra đúng sản phẩm, có bằng chứng và đường xử lý sai/thiếu tới cuối.
- 📍 Tiến độ: [■ Thiết kế và khả thi] → [□ Triển khai] → [□ Vận hành]
- ✅ Đã xong: ma trận 159 câu/53 nhóm; đăng ký danh mục thiết kế ML-MOW-TH-001 với 4 mã MOW-TH-001…004; 9 Tool + 3 quy trình bổ sung; liên kết quy trình có mã/phiên. Mô hình có 87 ca mô phỏng đạt, còn 5 chốt chưa kín. Theo D19/P17: tạo Over view là tab đầu, bố trí 4 Quy trình tổng hợp và ma trận 12 Quy trình thành phần từ cùng catalog, mã nhỏ/mờ. Phần này là trình bày, không nghiệm thu nghiệp vụ.
- ■ Đang làm: — · 0 RUN active
- ⬜ Còn lại: kiểm/hoàn thiện 5 chốt thực thi → áp một vòng sai/thiếu → PG staging đúng quyền → kiểm UI/Config/Test và bàn giao. TQT-ISS-007 giữ mở.
- ➡ Kế tiếp: Owner xem tab Over view và góp ý cách hiểu; phần kỹ thuật còn 5 chốt TQT-ISS-007 và trạng thái DRAFT cũ giữ nguyên, không tự phát RUN. NEXT_TRIGGER=OWNER_OVERVIEW_FEEDBACK_OR_HOST_CONTRACT_FIX.
- ⛔ Không làm/để sau: MOW002 · T2.5 · đổi CT-005 · chạy PG thật từ bản thiết kế · tự áp mục tiêu PR-07 chưa duyệt.

### 1. Mục tiêu
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

### 2. Thế nào là hoàn thành
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

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

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
| OpenAI-main | OpenAI | GPT Chat — phiên Owner chỉ định trực tiếp 09/10 | Host | Cuộc trò chuyện hiện tại của Owner · đường gọi hội đồng CHƯA ĐO |
| Claude-review | Anthropic | Claude Chat | Reviewer | CHƯA ĐO |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: —

**Roster cập nhật theo D19, 09/10:** GPT Chat là Host hiện hành; Astra Codex từng làm Host theo D17 và nay không được tự sửa nguồn chính. Claude Chat giữ ghế Reviewer khác hãng. Đường gọi Reviewer còn `CHƯA ĐO`; chưa có phiếu/quorum hay lệnh READY/RUN cho worker. Host được giao trực tiếp cập nhật nội dung tài liệu task, không mở rộng sang runtime, PG/Directus, hoặc dữ liệu nguồn UI hiện hành. Reviewer góp ý theo vòng AGENTS A5 sau khi có bản nháp/đề xuất.

### Vòng trước
Chỉ đạo READ-ONLY P15/D16 và Host GPT Chat dưới đây là lịch sử trước khi Owner giao lại Astra Codex. Không dùng lịch sử này để ghi đè vai trò/phạm vi hiện hành ở đầu §0.

#### BẢNG ĐIỀU KHIỂN CŨ · cập nhật 2026-10-08 · GPT Chat · P15
- 🎯 Mục tiêu: Owner chốt 08/10 — “việc gì lặp lại cũng có quy trình chuẩn → người mới, phiên AI mới làm theo là ra đúng sản phẩm, hướng tới muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể.” Đủ 15 dòng đọc ở ô 1. Vì sao (Owner): “số quy trình sẽ rất nhiều => chúng ta sẽ tập hợp toàn bộ các tools quy trình lên 1 task để có thể làm việc xuyên suốt, dài hạn, hội đồng AI dễ dàng có ý kiến đóng góp.”
- 🏁 Xong khi: theo ô 2 — một quy trình đạt khi người mới hoặc phiên AI mới làm theo, không hỏi thêm, ra đúng sản phẩm thật. Mốc của cả việc do hội đồng chốt ở bước kế hoạch.
- 📍 Tiến độ: ■ Khởi tạo / chỉ định Host → □ Chuẩn hóa → □ Áp dụng, kiểm chứng → □ Mở rộng và cải tiến.
- ✅ Đã xong: mục tiêu Owner D04/D05; Host D06; 9 Tools nguồn P06, Rà một UI P09, Claude trình bày 6 phần P10; Host tiếp nhận P11. Theo D11/P12: có bản thử TQT-QT-001, mẫu phản hồi 5 loại blocker và README đọc ngay khi muốn sửa/bị chặn. Đây là tài liệu chuẩn bị thử, chưa có KQ người mới cho quy trình meta.
- ■ Đang làm: — · 0 RUN active. D15 ưu tiên kiểm kê bộ câu hỏi gốc Chuỗi/Tầng/Bước+Bước con; đã soạn đề bài Codex READ-ONLY P15, thử ghép MOW001 sau khi có đề xuất. DRAFT vẽ UI P14 đã SUPERSEDED; MOW002 chưa làm.
- ⬜ Còn lại: kiểm độc lập agent đọc rồi làm ra sản phẩm thật; phản biện và bổ sung bước/câu hỏi còn thiếu; thử đề xuất mini-PR; kiểm khóa kỹ thuật Host-only (TQT-ISS-006); chuyển một SSOT từ MOW có bằng chứng; nền chuẩn IT và mở rộng Chuỗi khác theo mục tiêu.
- ➡ Kế tiếp: Owner chuyển Codex đọc PROMPT.md DRAFT để đề xuất bộ câu hỏi gốc và ca ghép MOW001 READ-ONLY; Host tiếp nhận → Reviewer khác hãng phản biện → chốt chuẩn/Owner quyết nghĩa gốc nếu cần → mới cho vẽ UI MOW001. NEXT_TRIGGER=CODEX_ROOT_QUESTION_PROPOSAL; không giữ terminal chờ.
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

## Owner cần quyết
- Q01 đã chốt theo D19: GPT Chat là Host hiện hành (09/10); D17 giao Astra Codex và D06 giao GPT Chat trước đó giữ làm lịch sử. Mục tiêu ngắn trong PR-07 vẫn do Owner/Claude bàn, Host chưa áp.

## Ý kiến và bằng chứng
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
