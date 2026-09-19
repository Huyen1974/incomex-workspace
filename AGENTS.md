# AGENTS.md — Incomex Workspace

**Luật phối hợp chung — FOUNDERS_CONSENSUS_V1 (GPT Chat + Claude Chat), 18/09/2026.**
`AGENTS.md` quy định vai trò/workflow. [`README.md`](README.md), mục **Shared Workspace Technical Contract**, quy định cơ chế kỹ thuật. `COLLAB.md` của từng project giữ trạng thái hiện hành. Không chép cùng một luật sang nhiều nơi.

## A1_ENTRY — Cửa vào
- Chat/Agent không được giả định đã tự nạp luật. Khi nhận câu `WS <thư mục|gốc> · <Host|Review> · <việc> · đọc AGENTS.md → <COLLAB.md>`, đọc file này trước, rồi `COLLAB.md` của project, sau đó chỉ đọc đúng scope cần làm.
- Tài liệu chính là sản phẩm; `COLLAB.md` là trạng thái; Git giữ lịch sử; `PROMPT.md` chỉ có khi thật sự cần giao Agent.
- Mỗi thư mục/project dùng một `COLLAB.md`. Gốc repo là một project riêng cho luật/môi trường chung.

## A2_ROLES — Vai trò và quyền
- **Owner** có quyền quyết định cuối cùng. **Đổi Host** và **hành động phá huỷ** chỉ Owner quyết, trừ khi Owner giao rõ từng việc.
- **GPT Chat = Editor/Executive Assistant của Owner**: là đầu mối làm việc trực tiếp với Owner, biên tập/chốt nội dung và truyền lệnh thực thi cuối cho Agent. Trong **phạm vi công việc Owner đã giao**, lệnh RUN/thực thi do GPT Chat phát ra được coi là lệnh của Owner. GPT Chat không tự mở rộng phạm vi ủy quyền.
- **Host** do Owner giao. Khi nhận Host ở phiên mới, Host tự sinh một `Host_ID` dễ phân biệt và ghi vào `COLLAB.md`; không được giả là ID hệ thống. Phiên không khớp Host/Host_ID hiện hành mặc định là Reviewer.
- **Reviewer** đọc/phản biện và tạo P; mặc định không sửa tài liệu chính nếu chưa được giao rõ phạm vi sửa.
- **Agent thực thi** chỉ chạy prompt đã READY và sau lệnh RUN của Owner; không tự coi việc nhìn thấy prompt là được giao.
- **Founders = GPT Chat + Claude Chat.** Founders duy trì/diễn giải luật nền. Claude Code, Codex, Cowork và Agent khác phải theo luật hiện hành; được đề xuất nhưng không tự sửa luật nền.
- Thay đổi luật nền phải ghi thành D trong `COLLAB.md` gốc và đưa một dòng vào **Owner cần quyết**. Đồng thuận Founders không vượt quyền riêng của Owner.

## A3_COLLAB — Trạng thái chung
- Dùng mã ổn định: `Dxx` quyết định, `Qxx` câu hỏi, `Pxx` ý kiến. Không đổi mã chỉ vì sửa câu chữ.
- Mỗi P có: người góp ý, `Based_on` commit, `Scope` = path + ID mục/khối, phần chưa đọc, đề nghị/lý do và phản hồi Host.
- Trạng thái P: `OPEN · ACCEPTED · PARTIAL · REJECTED · OWNER`.
- Không có ý kiến thì không tạo P và không tạo commit rỗng; báo trong chat.
- P đã đóng được thu thành một dòng, không xoá dấu vết; lý do dài hạn nâng thành D. Khi thu gọn P, thay `SAME_COMMIT` bằng hash thật tra từ Git log theo mã P.
- Tài liệu nên có ID mục/khối ổn định; sửa chữ không đổi ID.

## A4_WRITE — Ghi an toàn và bằng chứng
- Trước khi ghi: lấy version/SHA/HEAD hiện tại; ghi bằng expected version/head; có thay đổi chen ngang thì đọc lại và hoà giải, không ghi đè.
- Khi có transaction: sửa sản phẩm + cập nhật `COLLAB.md` trong **một commit**. Dòng trạng thái được tạo cùng commit ghi `Áp: SAME_COMMIT`.
- Khi không thể transaction: sửa sản phẩm trước, lấy hash thật, rồi cập nhật `COLLAB.md` với `Áp: <hash>`. Không có hash thì không ghi “đã sửa”.
- Commit nghiệp vụ dùng tiền tố `[GPT]`, `[Claude]`, `[Owner]`: `[actor] <mã> · <scope> · <tóm tắt>`. Đây là nhãn nghiệp vụ, không phải chứng minh danh tính.
- Chỉ báo PASS khi đã gọi/kiểm thật; phân biệt bằng chứng backend với client.

## A5_REVIEW — Bất đồng
- Host xử lý P và ghi ACCEPTED/PARTIAL/REJECTED cùng lý do.
- Reviewer được phản biện thêm **một vòng**. Còn vênh → P chuyển `OWNER` và một dòng lên **Owner cần quyết**; phần khác vẫn tiếp tục.
- Một scope đủ đồng thuận khi không còn P `OPEN` hoặc `OWNER` liên quan.

## A6_PROMPT — Giao Agent
- Mỗi project dùng **một `PROMPT.md` đang hoạt động**; sửa chính file đó cho việc mới, Git giữ lịch sử. Không tạo `v2/final/archive/progress/handoff` chỉ để lưu phiên bản hay tiến độ.
- Founder/Reviewer có thể cùng sửa khi còn DRAFT; **Host** đặt `READY@<full SHA 40 ký tự cuối chạm PROMPT.md>` trong `COLLAB.md`. Sửa `PROMPT.md` sau READY làm READY cũ vô hiệu và phải review/READY lại.
- READY **không phải RUN**. Owner được RUN; **GPT Chat với vai Editor/Executive Assistant được truyền RUN thay Owner trong phạm vi Owner đã giao**. Agent coi RUN hợp lệ từ GPT Chat trong phạm vi đó là lệnh của Owner. Agent vẫn phải lấy bản mới, kiểm full SHA READY rồi mới chạy; lệch thì DỪNG.
- Agent không sửa luật nền. Khi chạy: đọc `PROMPT.md`, thực hiện; tiến độ nằm ở commit công việc và **một báo cáo hiện hữu/đích báo cáo do prompt chỉ định**, không tạo file tiến độ riêng. Kết thúc chỉ báo Owner một dòng `XONG` hoặc `DỪNG`; Host/Reviewer tự đọc Git + báo cáo để nghiệm thu.

## A7_TECH — Hợp đồng kỹ thuật
- Lock, version/head, transaction, `operation_id`, các đường ghi, quyền xoá, file lớn/Unicode và giới hạn connector nằm trong **README Shared Workspace Technical Contract**; không lặp lại tại đây.

## A8_OWNER_VIEW — Một việc, một HTML chính
- Mỗi việc có **một thư mục riêng** và đúng **một file HTML chính dành cho Owner**. Mặc định dùng `view.html`; nếu dùng tên khác thì phải khai báo rõ trong `COLLAB.md` của việc.
- HTML chính là màn hình/sản phẩm Owner dùng để nhìn, duyệt và chỉ đạo. AI có thể dùng `COLLAB.md`, `PROMPT.md`, evidence, assets và file kỹ thuật phụ ở phía sau, nhưng không yêu cầu Owner đọc chúng nếu Owner không hỏi.
- Khi Owner yêu cầu thay đổi, AI sửa **HTML chính trong workspace/Git**. Bản hiển thị trên VPS chỉ là **mirror dẫn xuất** để Owner xem; không tạo thêm một nguồn nội dung độc lập trên VPS.
- Owner xem HTML qua URL trên VPS. Nút **Cập nhật** của từng việc chỉ kéo bản HTML chính mới nhất đã khai báo xuống vùng view tĩnh của VPS rồi tải lại trang. Không được dùng nút này để thay đổi mã/runtime, đồng bộ cả repo hay ghi đè file khác.
- Quy tắc kỹ thuật chi tiết của lớp Owner View nằm trong README; mọi AI/Agent làm việc trên repo này phải giữ mô hình **một việc → một thư mục → một HTML chính → một URL Owner View**.
