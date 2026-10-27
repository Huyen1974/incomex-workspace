# CODEX — HJW-N2-DOT-SEAT-IDENTITY-FIRST-20261027-04

RUN_ID: HJW-N2-DOT-SEAT-IDENTITY-FIRST-20261027-04
STATUS: DRAFT_FOR_CLAUDE · CHƯA READY · CHƯA OWNER RUN · CHƯA THỰC THI.
Executor_Surface: Codex Mac; Dot thật chỉ tham gia những phép thử do Owner chủ động giao.
Task: work/hermes-joint-workspace · Repo: Huyen1974/incomex-workspace.
Write_Path: đọc/ghi sổ qua workspace gateway D12; hồ sơ hội đồng AGENTS/COLLAB/roster theo quy trình hiện hành. ƯU TIÊN công cụ Dot/ChatGPT/Codex/Work của OpenAI, KHÔNG thay đổi VPS production hoặc xây gateway mới.

## 0. MỤC TIÊU ĐỢT NÀY — HAI TIÊU CHÍ BẮT BUỘC

Đọc AGENTS.md, HJW COLLAB §1–§3, roadmap 0.9, P398, P407–P408, P415–P418, Owner directive 26/10 23:00, và PROMPT hiện hành.

**M1. GHẾ ĐẦY ĐỦ:** Dot có thể đọc cùng một vấn đề hội đồng, phát biểu ý kiến và bỏ MỘT phiếu độc lập. Hệ thống xác định Dot là ghế khác GPT, không đếm hai lần từ cùng một danh tính kỹ thuật. Chỉ sau PASS thực tế mới thêm chính thức vào roster/A2/A9/COUNCIL_BOOTSTRAP và Task View theo luật hiện hành. Không cho Dot vai Host mặc định.

**M2. ĐỊNH DANH & TRUY VẾT:** Với bất kỳ thao tác nào của Dot, chứng cứ kiểm tra được phải nối đúng người/agent thực hiện với việc, hành động, nội dung/tham chiếu dữ liệu, mốc thời gian, kết quả và receipt. Nguồn định danh phải từ nhà cung cấp hoặc công cụ thực thi tin cậy, KHÔNG chỉ từ tên tự điền trong văn bản, profile nickname, prompt hoặc client-supplied actor.

**Thứ tự:** chứng minh M1+M2 TRƯỚC; sau khi đạt mới kiểm Voice giao tiếp Owner và Dot giao việc/điều phối Codex Cloud/Work. Native voice/codex hỗ trợ là ưu thế giai đoạn sau, KHÔNG đặt làm gate hoặc workload trong RUN này.

**Không tự giảm mục tiêu Owner:** các quyền nghiệp vụ/S4 root-GSM và Directus/PG/Graph/Lark từng yêu cầu vẫn lưu backlog, không mặc nhiên bị xóa. Nhưng KHÔNG buộc phải triển khai các connector đó để chứng minh M1/M2; chỉ đưa vào khi một trường hợp thực tế chứng minh thiếu và Owner chọn phương án.

## 1. NGUYÊN TẮC CHỌN ĐƯỜNG — HÃNG TRƯỚC, TỰ LÀM CUỐI CÙNG

(1) Kiểm các khả năng CHÍNH THỨC đang có của Dot: profile/handle riêng, task history/task-id, cloud computer, các Plugin kết nối, Codex Cloud. Các khả năng này được OpenAI mô tả nhưng CHƯA đủ để kết luận Incomex nhìn thấy actor=Dot khác actor=GPT.
    Tài liệu: https://help.openai.com/en/articles/20001530-getting-started-with-your-dot
    Codex Cloud: https://help.openai.com/en/articles/20001545-using-codex-cloud

(2) Nếu hãng/native app cung cấp một nguồn danh tính Dot đáng tin và nó được công cụ Incomex nhận diện/ghi nhận, dùng ngay. Không bắt cấp key/SSH/root hay xây thêm bridge chỉ vì các chức năng ấy tồn tại trong yêu cầu cũ.

(3) Nếu native chưa đủ, kiểm khả năng MỨC CẤU HÌNH của B1/master_profiles và workspace gateway hiện hữu để có Dot actor riêng với binding được máy kiểm chứng, không sửa nguồn mã nếu không cần. Việc cấp mã/credential/chỉnh gateway phát sinh phải được ghi thành đề xuất rõ, chưa tự apply.

(4) Chỉ khi hai đường trên KHÔNG đáp ứng M1/M2, ghi 2–3 phương án tối thiểu, tác động, chi phí bảo trì, đường lùi và quyết định cần Owner chốt. KHÔNG tự dựng gateway/HTTP proxy/MCP server/SSH relay, không cài thêm stack.

## 2. TRÌNH TỰ KIỂM CHỨNG M1/M2 — BẰNG DOT THẬT

S0 — READ GATE: đối chiếu mục tiêu, roster/quorum, HEAD, READY đúng SHA, Owner RUN; xem Plugin/Dot client đang có. Chỉ đọc thì không lấy VPS-GHI; không chen vào GitHub/Graph hoặc RUN đang ghi. Không chạy Agent Data recreate, không thay permission Gmail/root/GSM.

S1 — CHỨNG CỨ ĐỊNH DANH: Dot thật đọc AGENTS + HJW COLLAB/Bảng mới nhất, báo lại HEAD. Thu Dot profile/agent-or-task identifier do phía hãng cung cấp (nếu có) và danh tính actor mà gateway ghi từ authenticated principal. Phân biệt tên hiển thị của Dot, tên GPT account dùng chung và actor đáng tin cậy của server. Không gọi nickname là định danh bảo đảm.

S2 — MỘT Ý KIẾN / MỘT PHIẾU THỬ: một câu hỏi hội đồng vô hại, được đánh dấu CANARY/NOT_COUNTED trước khi xác minh. Dot thật đưa một ý kiến và một phiếu thử vào HJW bằng đường ghi D12 hiện có, lưu operation_id, request origin nếu được cung cấp đáng tin, commit/receipt và timestamp máy chủ. Không dùng Codex/GPT viết hộ rồi gắn nhãn Dot.

S3 — KIỂM ĐỘC LẬP / CHỐNG GIẢ MẠO: đối chiếu receipt với roster/actor GPT đã tồn tại, kiểm không đếm trùng. Dùng fixture âm để xác minh client tự khai tên Dot hoặc GPT dùng cùng credential không tự được tính thành ghế khác. Không tạo vote thật tác động quyết định production. Mọi sửa quorum/roster chỉ sau chứng cứ PASS đúng luật AGENTS.

S4 — PHÁN QUYẾT:
  A. IDENTITY_VERIFIED_AND_VOTE_PASS: server/provider proof chứng minh actor Dot riêng; ý kiến + phiếu 1 lần có receipt, không trùng GPT. Codex có thể cập nhật roster/Task View/COUNCIL_BOOTSTRAP trong cùng lượt khi mọi luật Author/Host/Owner và kiểm thử được đáp ứng; báo trạng thái ghế chính thức sau khi đọc lại đủ chứng cứ.
  B. DOT_NATIVE_COORDINATOR_ONLY: Dot đọc/báo/đề xuất được, nhưng actor trên Gateway là gpt-web/openai-main shared hoặc chưa có trusted binding. KHÔNG đăng ký ghế độc lập, KHÔNG tính phiếu; đưa đúng một đề xuất cấu hình tối thiểu cho Host/Owner thay vì lập lại dự án connector.
  C. CLIENT_ONLY_PENDING hoặc VENDOR_LIMIT: thiếu thao tác Owner/khả năng hãng thì nêu chính xác, không nói PASS. Nếu cần Owner xác nhận trên Dot UI, gom thành MỘT yêu cầu ngắn, không giữ lease/terminal chờ.

S5 — KQ & BÀN GIAO: ghi bảng ngắn: Dot thật dùng bề mặt nào; issuer/identity; đọc repo/head; P/receipt; vote có được tính không; kiểm không giả danh; còn gì vướng. KQ XONG của riêng RUN chỉ khi phép thử đúng phạm vi đạt; N2 FULL_PASS chỉ khi các tiêu chí Owner sau nghiệm thu được thỏa. Nếu thiếu identity, KQ DỪNG/CANARY_ONLY chính xác, một NEXT_TRIGGER.

## 3. PHẦN KHÔNG LÀM TRONG LƯỢT NÀY

- Không thử điều phối Codex/Work, không thử thoại như một gate bắt buộc M1/M2; sau PASS mới mở lượt tiếp theo để Owner nói trực tiếp với Dot và giao Codex Cloud native.
- Không triển khai candidate Agent Data P415, không tiêu lượt +1 forward recreate UNUSED, không sửa Directus/PG/Graph/Lark/KB/TQT/Guard, không chạy theo #11 heartbeat chỉ để xanh.
- Không cấp/đổi SSH/root/GSM hoặc sửa tài khoản Gmail đã được cấu hình read-free/ask-before-writes. Không tạo credential Dot mới trước khi chứng minh chức năng hãng không đáp ứng.
- Không bỏ luật D12, Điều 30/31, A2/A9, quorum và nguồn sổ. Không dán kết quả giả, không xóa evidence/rollback trước.
- Không xóa yêu cầu năng lực rộng/điều phối của Owner, chỉ trì hoãn đến khi ghế + định danh đạt hoặc Owner chọn mức chấp nhận giới hạn.

## STEP_WALK_V1

| Bước | Ai / Trigger | Bằng chứng bắt buộc | Nếu thiếu |
|---|---|---|---|
| S0 | Codex · sau Host READY + Owner RUN | HEAD, roster, tool surface | DỪNG sạch |
| S1 | Dot thật/Codex kiểm độc lập | Dot task/provider record + backend actor | UNKNOWN, không nhận danh tính |
| S2 | Dot thật · canary được giao | P + vote thử + operation_id/receipt | chưa tính phiếu |
| S3 | Codex/Host kiểm | khác GPT, không spoof/đếm trùng | giữ roster, nêu blocker |
| S4 | Host/Codex theo vai | PASS hoặc shared-id, đúng dấu vết | trình Owner nếu cần cấu hình |
| S5 | Codex · đóng lượt | KQ, commit, 0 VPS mutation, NEXT_TRIGGER | DỪNG có bằng chứng |

**Đầu ra cho Owner**: ĐÃ CÓ GHẾ ĐỘC LẬP CHƯA? AI ĐỊNH DANH ĐƯỢC AI? Nếu CHƯA, cần đúng một quyết định về cấu hình tối thiểu nào; không tự phát sinh việc xây hạ tầng.

**Trạng thái:** DRAFT cho Claude phản biện một vòng. Không READY/STARTED, không tác động production.
