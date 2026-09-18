# AGENTS.md — Incomex Workspace

**Luật phối hợp chung — FOUNDERS_CONSENSUS_V1 (GPT Chat + Claude Chat), 18/09/2026.**
`AGENTS.md` quy định vai trò/workflow. [`README.md`](README.md), mục **Shared Workspace Technical Contract**, quy định cơ chế kỹ thuật. `COLLAB.md` của từng project giữ trạng thái hiện hành. Không chép cùng một luật sang nhiều nơi.

## A1_ENTRY — Cửa vào
- Chat/Agent không được giả định đã tự nạp luật. Khi nhận câu `WS <thư mục|gốc> · <Host|Review> · <việc> · đọc AGENTS.md → <COLLAB.md>`, đọc file này trước, rồi `COLLAB.md` của project, sau đó chỉ đọc đúng scope cần làm.
- Tài liệu chính là sản phẩm; `COLLAB.md` là trạng thái; Git giữ lịch sử; `PROMPT.md` chỉ có khi thật sự cần giao Agent.
- Mỗi thư mục/project dùng một `COLLAB.md`. Gốc repo là một project riêng cho luật/môi trường chung.

## A2_ROLES — Vai trò và quyền
- **Owner** có quyền quyết định cuối cùng và giữ riêng ba quyền: **RUN/giao chạy**, **đổi Host**, **hành động phá huỷ**. Không Founder/Agent nào được tự nới ba quyền này.
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
- Chỉ tạo `PROMPT.md` khi cần thực thi. `READY@<commit cuối chạm PROMPT.md>` chỉ được đặt khi không còn P OPEN/OWNER liên quan.
- Sửa `PROMPT.md` sau READY làm READY cũ vô hiệu. Đổi phạm vi/hành động phải review lại.
- READY **không phải RUN**. Owner mới có quyền giao chạy. Hành động phá huỷ phải được nêu rõ và Owner duyệt.
- Agent trước khi chạy phải kiểm commit hiện tại của `PROMPT.md` đúng với READY.

## A7_TECH — Hợp đồng kỹ thuật
- Lock, version/head, transaction, `operation_id`, các đường ghi, quyền xoá, file lớn/Unicode và giới hạn connector nằm trong **README Shared Workspace Technical Contract**; không lặp lại tại đây.
