# COLLAB — tools-quy-trinh
Tên việc: Tools quy trình — làm theo quy trình ra được sản phẩm

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner chốt mục tiêu ô 1–2 ngày 08/10/2026 07:16 (D04/D05); chỉ định trực tiếp GPT Chat làm Host và giao bắt đầu tiếp nhận các quy trình Tools CTCM vào nội dung task ngày 08/10/2026 09:19 +07 (D06). AI không sửa chữ ô 1–2.
Host: GPT Chat
Host_ID: OpenAI-main

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-08 07:32 +07 · Claude Chat · P05
- 🎯 Mục tiêu: Owner chốt 08/10 — “việc gì lặp lại cũng có quy trình chuẩn → người mới, phiên AI mới làm theo là ra đúng sản phẩm, hướng tới muốn làm sai cũng khó, lý tưởng là muốn làm sai cũng không thể.” Đủ 15 dòng đọc ở ô 1. Vì sao (Owner): “số quy trình sẽ rất nhiều => chúng ta sẽ tập hợp toàn bộ các tools quy trình lên 1 task để có thể làm việc xuyên suốt, dài hạn, hội đồng AI dễ dàng có ý kiến đóng góp.”
- 🏁 Xong khi: theo ô 2 — một quy trình đạt khi người mới hoặc phiên AI mới làm theo, không hỏi thêm, ra đúng sản phẩm thật. Mốc của cả việc do hội đồng chốt ở bước kế hoạch.
- 📍 Tiến độ: ■ Khởi tạo / chỉ định Host → □ Chuẩn hóa → □ Áp dụng, kiểm chứng → □ Mở rộng và cải tiến.
- ✅ Đã xong: tạo task (P01 · GPT) · sửa §0 đúng luật (P02 · Claude) · Owner duyệt mục tiêu bản viết lại 08/10 07:16, đã lên ô 1–2 (P04 · D04); bản 07/10 giữ ở Vòng trước.
- ■ Đang làm: Host GPT Chat đã nhận D06; đang tiếp nhận nội dung 9 Tools CTCM vào trang task · 0 RUN worker active.
- ⬜ Còn lại: chọn nền chuẩn ngành IT cho ba lớp và sổ (ô 1 dòng 4); hoàn thiện cách phân nhóm/mẫu ba lớp; kiểm kê và nối nguồn; áp thử để sửa quy trình; chuẩn hóa phần lặp lại; tự động hóa phần đủ điều kiện; theo dõi sai sót đến khi đóng. Đây là các đầu việc cần đạt, chưa phải roadmap đã duyệt.
- ➡ Kế tiếp: Host tiếp nhận thực chất 9 Tools CTCM vào `view.html`, phân loại ba chiều; ghi đề xuất/nguồn/chỗ thiếu tại P06 và đề nghị Claude-review phản biện theo AGENTS A5. Chưa phát READY/RUN hay thay nguồn runtime.
- ⛔ Không làm/để sau: tạo task không bao gồm triển khai DOT/script, bảng PG, đổi runtime/UI production hay chuyển dữ liệu đang dùng ở MOW.

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

### 2. Thế nào là hoàn thành
Một quy trình đạt = người mới hoặc phiên AI mới làm theo, không hỏi thêm, ra đúng sản phẩm thật.
Chưa đạt → sửa quy trình, thêm câu hỏi còn thiếu → chạy lại.

(Owner duyệt 08/10/2026.)

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

#### TQT-REQ — bảng kiểm từng mục tiêu ở ô 1 · 07/10/2026
Mục tiêu chỉ có một nguồn là ô 1 (bản Owner chốt 08/10 · D04). Bảng này không phải bản mục tiêu thứ hai: cột giữa là tóm tắt cũ của AI, lệch chữ thì ô 1 thắng. Trỏ về dòng của ô 1: REQ-01 → dòng 2, 5 · REQ-02 → dòng 3 · REQ-03 → dòng 1, 12 · REQ-04 → dòng 6 · REQ-05 → dòng 7–11 · REQ-06 → dòng 13–14 (sổ ghi cả sai sót lẫn chỗ thiếu) · REQ-07 → dòng 4 · REQ-08 → dòng 15 · REQ-09 → Đích và “Chưa làm lúc này”.
Nhiệm vụ/phạm vi lượt này: tạo đúng một task tên `tools-quy-trinh` trên incomex-workspace, tập hợp đầu mối để làm việc dài hạn. Việc tạo task hoàn tất không đồng nghĩa toàn bộ quy trình đã đạt tiêu chí tại ô 2.

| Mã | Tóm tắt của AI — nguyên văn đọc ở ô 1 | Cách kiểm khi chuẩn hóa |
|---|---|---|
| TQT-REQ-01 | Quy trình hóa tools của Chế tạo cỗ máy, Vận hành cỗ máy, Cỗ máy sản xuất quy trình; chia nhóm nhỏ. | Danh mục thể hiện rõ phạm vi và nhóm chuyên môn, không chỉ có UI/CTCM. |
| TQT-REQ-02 | Làm đúng quy trình phải đạt mục tiêu và ra sản phẩm; còn mắc thì hiệu chỉnh đến khi đạt. | Có đầu vào/điều kiện áp dụng, đích nhận sản phẩm, tiêu chí và bằng chứng. Ca mắc dẫn về đúng câu/bước cần sửa rồi kiểm lại. |
| TQT-REQ-03 | Liệt kê tất cả câu hỏi cần thiết để hoàn thiện; hội đồng AI liên tục góp ý, hiệu chỉnh, bổ sung. | Mỗi câu có đáp án/bằng chứng hoặc được nêu rõ còn mở; câu không áp dụng có lý do. Chưa giải quyết câu chặn thì chưa được công nhận đạt. |
| TQT-REQ-04 | Chia nhóm chuyên môn cho con người dễ nhận diện, đánh giá, góp ý; ví dụ Thiết kế UI, config, xét nguyên tắc giao việc. | Tên dễ hiểu, mã ổn định, danh sách ngắn theo nhóm; góp ý chỉ được chính quy trình/câu/bước. Nhóm được bổ sung khi cần. |
| TQT-REQ-05 | Ba lớp: for design; for execute; for DOT/script. | Giữ đủ hợp đồng riêng của từng lớp tại TQT-LAYERS; có liên kết giữa các lớp, không tự coi bản thiết kế là bản tự động hóa. |
| TQT-REQ-06 | Sai sót chưa sửa ngay phải vào một sổ tổng hợp, theo dõi tiến trình/vòng đời đến khi xong; trước mắt repo/VPS, khi ổn định chuyển bảng PG riêng. | Sổ có mã, nguồn, người theo dõi/xử lý/kiểm, trạng thái, bước tiếp, điều kiện đóng, bằng chứng và lịch sử; việc hoãn vẫn được theo dõi. Chuyển PG về sau giữ mã/lịch sử và chỉ một nguồn hiện hành. |
| TQT-REQ-07 | Mục 7 (bổ sung): nền là chuẩn tốt nhất của ngành IT, sau đó mới thêm phần riêng Incomex. | Mỗi chuẩn/mẫu/khung của task ghi một dòng `Nền: <chuẩn ngành IT> · Riêng Incomex: <thêm gì, vì sao chuẩn ngành chưa đủ>`. Chọn nền theo thước AGENTS A10-R1: có sẵn · nhiều người dùng · còn được duy trì · vừa cỡ Incomex (lấy khung, không bê cả bộ). Chưa tìm được chuẩn ngành ⇒ ghi `Nền: CHƯA TÌM` và tính là chưa đạt; không tự dựng rồi gọi là chuẩn. Phần đã phác thảo trước mục 7 (TQT-LAYERS, TQT-REGISTER, 9 Tools nguồn, khung trang nội dung) phải được đối chiếu lại theo dòng này. |
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
- Sổ MOW hiện hành: cùng dữ liệu trên, `TOOL-CTCM-001.pilot.issues`; kết quả từng lượt: `pilot.runs`. Trang mới liên kết tới sổ này, không chép trạng thái từng hồ sơ sang một sổ cạnh tranh.
- Task mới là đầu mối tập hợp/chuẩn hóa quy trình tools cho cả ba phạm vi. Thiết kế sản phẩm MOW và lỗi của lượt MOW vẫn có nơi xử lý hiện hành; tiếp nhận/chuyển nguồn phải giữ mã, lịch sử, đường đọc và xác định một nguồn chuẩn trước khi chuyển.
- Các nguồn khác sẽ được kiểm kê trong phạm vi mục tiêu; chưa được coi danh mục 9 Tools CTCM là toàn bộ tài nguyên Incomex.
- Luật nền về giao việc chỉ tham chiếu AGENTS/root COLLAB. Quy trình chuyên môn “xét nguyên tắc giao việc” không tự thay các luật đó.

#### TQT-REGISTER — sổ tổng hợp trước mắt
- **Sổ của task: `view.html#so-van-de`.** Sổ nằm ngay trong HTML chính trên repo để con người đọc cùng nguồn AI cập nhật; không có bản nhập localStorage hay sổ Markdown song song.
- Mỗi hồ sơ mới có mã `TQT-ISS-nnn`; hồ sơ ở task khác giữ mã gốc và liên kết tới sổ gốc, không tạo bản trạng thái thứ hai. TQT-ISS-001 ghi đúng khoảng trống Owner nêu.
- Vòng đời cần quản lý: Ghi nhận → Phân loại → Giao xử lý → Đang xử lý → Chờ kiểm → Đóng; có nhánh Bị chặn / Để sau / Trùng / Mở lại. Chỉ ghi Đang xử lý khi đã có người nhận thật.
- Trường cần giữ: mã; ngày/nguồn phát hiện; quy trình/phiên bản/câu/bước; tình huống/bằng chứng; ảnh hưởng; người theo dõi; người xử lý; người kiểm; trạng thái; bước tiếp; mốc rà; lý do hoãn; tiêu chí đóng; bản sửa/kết quả kiểm; lịch sử.
- Host được chỉ định có trách nhiệm rà sổ đầu/cuối lượt và khi bàn giao; assignee sửa, verifier kiểm. Chưa có người nhận thì ghi “Chưa giao”, không bịa phân công.
- Khi ổn định mới thiết kế chuyển sang bảng PG riêng qua DOT; phải kiểm migration/mapping và chuyển nguồn một lần, giữ nguyên mã/lịch sử. Chưa tạo bảng hay tự bật nhắc việc nền trong lượt khởi tạo.

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| OpenAI-main | OpenAI | GPT Chat — phiên Owner chỉ định 08/10 | Host | Phiên Chat trực tiếp · đường gọi hội đồng CHƯA ĐO |
| Claude-review | Anthropic | Claude Chat | Reviewer | CHƯA ĐO |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: —

**Roster hiệu lực từ D06:** GPT Chat là Host do Owner chỉ định trực tiếp; Claude Chat giữ ghế Reviewer khác hãng. Đường gọi Reviewer còn `CHƯA ĐO`; chưa có phiếu/quorum hay lệnh READY/RUN cho worker. Host được giao trực tiếp cập nhật nội dung tài liệu task, không mở rộng sang runtime, PG/Directus, hoặc dữ liệu nguồn UI hiện hành. Reviewer góp ý theo vòng AGENTS A5 sau khi có bản nháp/đề xuất.

### Vòng trước
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

## Owner cần quyết
- **Q01 — ĐÃ CHỐT 08/10/2026 09:19 +07:** Owner trực tiếp chỉ định GPT Chat làm Host (D06). Không có câu hỏi Owner còn mở trong phạm vi lượt tiếp nhận tài liệu này.

## Ý kiến và bằng chứng
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
