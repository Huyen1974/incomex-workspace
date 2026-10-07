# COLLAB — tools-quy-trinh

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: CHƯA XÁC NHẬN — chỉ còn chỉ định Host theo AGENTS MT3-C/A2. Owner đã giao trực tiếp việc tạo task, tên task và toàn bộ mục tiêu/phạm vi tại tin nhắn ngày 07/10/2026; không yêu cầu xác nhận lại các nội dung đã giao.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-07 22:03 +07 · GPT Chat · P01
- 🎯 Mục tiêu: theo ô 1 bên dưới; gom đầu mối để con người và hội đồng AI làm việc xuyên suốt.
- 🏁 Xong khi: theo ô 2 bên dưới. Riêng lượt tạo task: đúng tên, đủ yêu cầu, có cửa đọc, danh mục nguồn và sổ vấn đề.
- 📍 Tiến độ: ■ Khởi tạo / chỉ định Host → □ Chuẩn hóa → □ Áp dụng, kiểm chứng → □ Mở rộng và cải tiến.
- ✅ Đã xong: tạo task và ba file tại `5299be93672f1cbfe7dde06dbd706d4319621a02`; đủ 6 yêu cầu, nối 9 Tools nguồn/sổ MOW và mở sổ task. Đã kiểm task xuất hiện trên Owner View, đọc được đúng mục tiêu/tiêu chí và trang nội dung.
- ■ Đang làm: Bước khởi tạo · vòng 0/5 · gọi: chưa gọi ghế · chờ Owner chỉ định Host; chưa mở vòng hội đồng chính thức.
- ⬜ Còn lại: hoàn thiện cách phân nhóm/mẫu ba lớp; kiểm kê và nối nguồn; áp thử để sửa quy trình; chuẩn hóa phần lặp lại; tự động hóa phần đủ điều kiện; theo dõi sai sót đến khi đóng. Đây là các đầu việc cần đạt, chưa phải roadmap đã duyệt.
- ➡ Kế tiếp: 😊 Owner chỉ định Host; Host nhận việc và tổ chức hội đồng theo AGENTS; Reviewer đối chiếu 6 yêu cầu; 🤖 agent chưa có lượt thực thi.
- ⛔ Không làm/để sau: tạo task không bao gồm triển khai DOT/script, bảng PG, đổi runtime/UI production hay chuyển dữ liệu đang dùng ở MOW.

### 1. Mục tiêu
Quy trình hoá các tool Chế tạo cỗ máy, Vận hành cỗ máy, Cỗ máy sản xuất quy trình, có chia theo các nhóm nhỏ.

### 2. Thế nào là hoàn thành
Làm theo quy trình phải không sai => đạt được mục tiêu, ra được sản phẩm. Nếu vẫn mắc, hiệu chỉnh quy trình cho bằng đạt.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

#### TQT-REQ — yêu cầu trực tiếp Owner · 07/10/2026
Nhiệm vụ/phạm vi lượt này: tạo đúng một task tên `tools-quy-trinh` trên incomex-workspace, tập hợp đầu mối để làm việc dài hạn. Việc tạo task hoàn tất không đồng nghĩa toàn bộ quy trình đã đạt tiêu chí tại ô 2.

| Mã | Yêu cầu cần giữ | Cách kiểm khi chuẩn hóa |
|---|---|---|
| TQT-REQ-01 | Quy trình hóa tools của Chế tạo cỗ máy, Vận hành cỗ máy, Cỗ máy sản xuất quy trình; chia nhóm nhỏ. | Danh mục thể hiện rõ phạm vi và nhóm chuyên môn, không chỉ có UI/CTCM. |
| TQT-REQ-02 | Làm đúng quy trình phải đạt mục tiêu và ra sản phẩm; còn mắc thì hiệu chỉnh đến khi đạt. | Có đầu vào/điều kiện áp dụng, đích nhận sản phẩm, tiêu chí và bằng chứng. Ca mắc dẫn về đúng câu/bước cần sửa rồi kiểm lại. |
| TQT-REQ-03 | Liệt kê tất cả câu hỏi cần thiết để hoàn thiện; hội đồng AI liên tục góp ý, hiệu chỉnh, bổ sung. | Mỗi câu có đáp án/bằng chứng hoặc được nêu rõ còn mở; câu không áp dụng có lý do. Chưa giải quyết câu chặn thì chưa được công nhận đạt. |
| TQT-REQ-04 | Chia nhóm chuyên môn cho con người dễ nhận diện, đánh giá, góp ý; ví dụ Thiết kế UI, config, xét nguyên tắc giao việc. | Tên dễ hiểu, mã ổn định, danh sách ngắn theo nhóm; góp ý chỉ được chính quy trình/câu/bước. Nhóm được bổ sung khi cần. |
| TQT-REQ-05 | Ba lớp: for design; for execute; for DOT/script. | Giữ đủ hợp đồng riêng của từng lớp tại TQT-LAYERS; có liên kết giữa các lớp, không tự coi bản thiết kế là bản tự động hóa. |
| TQT-REQ-06 | Sai sót chưa sửa ngay phải vào một sổ tổng hợp, theo dõi tiến trình/vòng đời đến khi xong; trước mắt repo/VPS, khi ổn định chuyển bảng PG riêng. | Sổ có mã, nguồn, người theo dõi/xử lý/kiểm, trạng thái, bước tiếp, điều kiện đóng, bằng chứng và lịch sử; việc hoãn vẫn được theo dõi. Chuyển PG về sau giữ mã/lịch sử và chỉ một nguồn hiện hành. |

#### TQT-LAYERS — ba lớp Owner yêu cầu
| Lớp | Dùng cho | Nội dung bắt buộc | Đích hoàn thành |
|---|---|---|---|
| for design | Thiết kế sáng tạo ban đầu: vẽ UI, lên danh sách, config… | Mục tiêu/sản phẩm thiết kế, đầu vào/ràng buộc; tập trung đầy đủ câu hỏi cần trả lời, các lựa chọn/nhánh và quyết định. | Thiết kế đáp ứng mục tiêu, các câu hỏi cần thiết đã xử lý; áp dụng chưa thành công thì bổ sung/sửa quy trình và kiểm lại. |
| for execute | Agent thực hiện công việc lặp lại. | Điều kiện bắt đầu, câu hỏi cần xác minh, thứ tự bước, nhánh xử lý khi mắc, đầu ra và nơi bàn giao. | Định nghĩa rõ thế nào hoàn thành, kiểm gì và bằng chứng nào chứng minh đã ra sản phẩm đúng. |
| for DOT/script | Thực hiện tự động bằng DOT/script. | Mục tiêu; điều kiện/trigger; input/output; hành vi thành công, thất bại; định nghĩa hoàn thành; DOT/script thực thi. | Có kết quả tự động kiểm chứng theo hợp đồng và đường xử lý lỗi. Áp AGENTS A10-R3/R4 khi triển khai, không chép lại luật nền. |

Ba chiều độc lập: **phạm vi phục vụ × nhóm chuyên môn × lớp quy trình**. Một quy trình có mã ổn định; dùng cho nhiều phạm vi thì liên kết/nhãn, không nhân bản nội dung. Không bắt buộc mọi quy trình phải có ngay đủ ba lớp. Tên nhóm/mẫu chi tiết tại trang nội dung là khung ghi nhận ban đầu để hội đồng hoàn thiện.

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
| OpenAI-main | OpenAI | GPT Chat — phiên tạo task này | Host | CHƯA ĐO |
| Claude-review | Anthropic | Claude Chat | Reviewer | CHƯA ĐO |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: —

**Roster đề xuất, chưa kích hoạt.** Đề xuất Host: GPT Chat tại phiên này, vì đang nhận trực tiếp mục tiêu và lập đầu mối task. Owner chưa chỉ định Host; chưa ghi dấu máy `Host:`, chưa gọi hội đồng, chưa có phiếu/quorum, PROMPT, READY, RUN hay assignment. Sau chỉ định, Host nhận vai và hoàn thiện đường gọi/roster theo AGENTS. Subagent hỗ trợ kiểm nội dung trong phiên soạn không phải một ghế hội đồng độc lập.

### Vòng trước
Chưa có. Đây là lần tạo task đầu tiên theo lệnh Owner 07/10/2026.

## Cửa vào và nguồn chuẩn
- Tên việc: Tools quy trình — làm theo quy trình ra được sản phẩm.
- Task-id: `tools-quy-trinh` · thư mục: `work/tools-quy-trinh/`.
- HTML chính: `view.html`.
- Owner View: https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh
- AI vào việc: `AGENTS.md` → §0/Bảng trên → `README.md` → đúng mục nguồn/quy trình/sổ cần xử lý.
- Mục tiêu/tiêu chí/trạng thái chỉ ở §0; trang Owner rút tự động. `view.html` giữ danh mục nguồn, cấu trúc tra cứu, sổ vấn đề và hướng dẫn góp ý, không chép mục tiêu/trạng thái điều hành.

## Quyết định Owner
- **D01 · 2026-10-07 · EFFECTIVE:** tạo đúng task `tools-quy-trinh`; toàn bộ 6 yêu cầu được ghi tại TQT-REQ; nguồn xuất phát là Tools CTCM Owner dẫn. Phạm vi lượt hiện tại là tạo đầu mối công việc, chưa phải lệnh chạy toàn bộ chương trình.
- HUMAN_DIRECTIVE@TQT-CREATE-20261007 EFFECTIVE · task=tools-quy-trinh · scope=work/tools-quy-trinh/ · step=khởi tạo · recorded_by=OpenAI-main · quote="tạo cho tôi một task: tools-quy-trinh trên incomex workspace repo." · text=Tạo task và ghi đầy đủ mục tiêu/chi tiết Owner giao trong cùng tin nhắn. · audit=Tin nhắn trực tiếp Owner tại phiên tạo task, 2026-10-07; commit khởi tạo.

## Owner cần quyết
- **Q01 — Chỉ định Host của tools-quy-trinh.** Đề xuất GPT Chat tại phiên tạo task. Theo AGENTS MT3-C/A2 và DROOT46, quyền chỉ định Host thuộc Owner; không cần xác nhận lại tên task hay 6 yêu cầu.

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
