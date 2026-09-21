# AGENTS.md — Incomex Workspace

**Luật phối hợp chung — FOUNDERS_CONSENSUS_V1 (GPT Chat + Claude Chat), 18/09/2026.**
`AGENTS.md` quy định vai trò/workflow. [`README.md`](README.md), mục **Shared Workspace Technical Contract**, quy định cơ chế kỹ thuật. `COLLAB.md` của từng project giữ trạng thái hiện hành. Không chép cùng một luật sang nhiều nơi.

## A0_OBJECTIVE — Cổng mục tiêu/nhiệm vụ User (BẮT BUỘC trước mọi việc)
- Trong quy trình này, **User giao việc = Owner**. Mỗi `work/<work-id>/COLLAB.md` phải có **khối đầu tiên ngay sau tiêu đề** tên `## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC`, gồm tối thiểu: `Mục tiêu`, `Nhiệm vụ/phạm vi`, `Tiêu chí xong`, `Xác nhận User`.
- **AI mở việc / AI được giao soạn thảo** có trách nhiệm nhắc lại mục tiêu + nhiệm vụ cho User và nhận **xác nhận rõ ràng của User** trước khi bắt đầu lập kế hoạch, thảo luận phương án, tạo `PROMPT.md`, phát RUN hoặc thực thi. Trước khi được xác nhận, AI chỉ được ghi nhận yêu cầu và hỏi/làm rõ dữ kiện cần thiết; không được tự suy diễn mục tiêu hay đi tiếp sang kế hoạch/thực thi.
- Bất kỳ AI nào được chỉ định tham gia một việc đều phải đọc `AGENTS.md` rồi đọc **khối mục tiêu/nhiệm vụ ở đầu `COLLAB.md` của việc đó trước tiên**. Nếu `Xác nhận User = CHƯA XÁC NHẬN` thì dừng tại cổng A0.
- Nếu User đổi mục tiêu/nhiệm vụ/phạm vi, Host phải cập nhật khối A0 của việc và xác nhận lại với User trước khi tiếp tục. Kế hoạch/PROMPT/READY/RUN nào mâu thuẫn với mục tiêu mới thì mất hiệu lực và phải rà lại.
- Không được đẩy khối mục tiêu xuống dưới phần kế hoạch/trạng thái; mục tiêu của User luôn là phần nghiệp vụ đầu tiên mọi AI nhìn thấy trong từng thư mục công việc.

## A1_ENTRY — Cửa vào
- Chat/Agent không được giả định đã tự nạp luật. Khi nhận câu `WS <thư mục|gốc> · <Host|Review> · <việc> · đọc AGENTS.md → <COLLAB.md>`, đọc file này trước, rồi `COLLAB.md` của project, sau đó chỉ đọc đúng scope cần làm.
- Tài liệu chính là sản phẩm; `COLLAB.md` là trạng thái; Git giữ lịch sử; `PROMPT.md` chỉ có khi thật sự cần giao Agent.
- Mỗi công việc/project nằm dưới `work/<work-id>/` và dùng một `COLLAB.md` riêng. `PROMPT.md`, test, evidence, assets và archive của việc phải nằm trong đúng thư mục đó.
- Root repo chỉ dùng cho điều phối chung và **chỉ được có** `AGENTS.md`, `README.md`, `COLLAB.md`, `work/`. Không đặt file nghiệp vụ, prompt, test hay chứng tích của một việc ở root.

## A2_ROLES — Vai trò và quyền
- **Owner** có quyền quyết định cuối cùng. **Đổi Host** và **hành động phá huỷ** chỉ Owner quyết, trừ khi Owner giao rõ từng việc.
- **GPT Chat = Editor/Executive Assistant của Owner**: là đầu mối làm việc trực tiếp với Owner, biên tập/chốt nội dung và truyền lệnh thực thi cuối cho Agent. Trong **phạm vi công việc Owner đã giao**, lệnh RUN/thực thi do GPT Chat phát ra được coi là lệnh của Owner. GPT Chat không tự mở rộng phạm vi ủy quyền.
- **Vai trò tách khỏi năng lực kỹ thuật.** Vai trò được gán theo **bề mặt/phiên cụ thể** trong từng việc: ví dụ GPT Chat, GPT Work, Codex, Claude Chat, Claude Cowork, Claude Code CLI, Hermes… có thể lần lượt làm Host/Reviewer/Agent theo phân công. Quyền kỹ thuật không suy từ hãng/model/vai trò; nó đi theo **tool/connector đã audit thực sự bind ở bề mặt đó**.
- **Hạ tầng dùng chung.** Một đường/tool đã được Owner thiết lập và nghiệm thu là năng lực chung của hệ thống; bất kỳ bề mặt nào thực sự bind được đường/tool đó đều dùng theo cùng guardrail. Không viết luật kiểu “tool của GPT” hay “tool của Claude”; chỉ ghi tên capability/path.
- **Host** do Owner giao. Khi nhận Host ở phiên mới, Host tự sinh một `Host_ID` dễ phân biệt và ghi vào `COLLAB.md`; không được giả là ID hệ thống. Phiên không khớp Host/Host_ID hiện hành mặc định là Reviewer.
- **Reviewer** đọc/phản biện và tạo P; mặc định không sửa tài liệu chính nếu chưa được giao rõ phạm vi sửa.
- **Agent thực thi** chỉ chạy prompt đã READY và sau lệnh RUN của Owner; không tự coi việc nhìn thấy prompt là được giao.
- **Founders = GPT Chat + Claude Chat.** Founders duy trì/diễn giải luật nền. Claude Code, Codex, Cowork và Agent khác phải theo luật hiện hành; được đề xuất nhưng không tự sửa luật nền.
- Thay đổi luật nền phải ghi thành D trong `COLLAB.md` gốc và đưa một dòng vào **Owner cần quyết** nếu chưa được Owner quyết. Đồng thuận Founders không vượt quyền riêng của Owner.

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
- Mỗi `work/<work-id>/` dùng tối đa **một `PROMPT.md` đang hoạt động** trong chính thư mục công việc; sửa chính file đó cho việc mới, Git giữ lịch sử. Không tạo `v2/final/archive/progress/handoff` chỉ để lưu phiên bản hay tiến độ.
- Founder/Reviewer có thể cùng sửa khi còn DRAFT; **Host** đặt `READY@<full SHA 40 ký tự cuối chạm PROMPT.md>` trong `COLLAB.md`. Sửa `PROMPT.md` sau READY làm READY cũ vô hiệu và phải review/READY lại.
- **HOST INPUT GATE là trách nhiệm bắt buộc trước khi agent được mutation.** Host phải bảo đảm đầu vào đã tồn tại ở SSOT, prompt chỉ đúng nguồn/đích, ghi rõ **Executor_Surface** và **Write_Path** (capability/tool family, không phải hãng), và agent được đưa về đúng repo/workspace/ref trước khi làm. Với môi trường quen thuộc đã dùng nhiều lần, không bắt buộc tách một lượt PRECHECK riêng: RUN có thể bắt đầu bằng đúng **một read-gate của Write_Path đã chọn** rồi đọc `AGENTS.md` → `COLLAB.md` → `PROMPT.md`; chỉ sau khi gate PASS agent mới được mutation. Nếu gate FAIL thì DỪNG trước mọi thay đổi.
- Host không được coi việc “file có trong MCP/clone của Host” là đủ nếu lệnh giao không chỉ rõ cách agent vào đúng workspace. Ngược lại, không tạo thủ tục kiểm tra lặp lại cho năng lực môi trường đã nghiệm thu: chỉ kiểm binding của Write_Path đã chọn + đầu vào cụ thể có thể thiếu/lệch/xung đột.
- **Host phải giám sát việc đã giao qua SSOT/hạ tầng chung.** Tối thiểu Host kiểm: gate đầu vào/Write_Path, thay đổi thực tế trên repo hoặc báo cáo đích, commit/diff cuối và điều kiện nghiệm thu trước khi đánh DONE. Agent báo XONG không tự động đồng nghĩa Host nghiệm thu; lệch scope thì Host dừng/hòa giải trước bước tiếp.
- READY **không phải RUN**. Owner được RUN; **GPT Chat với vai Editor/Executive Assistant được truyền RUN thay Owner trong phạm vi Owner đã giao**. Agent coi RUN hợp lệ từ GPT Chat trong phạm vi đó là lệnh của Owner. Agent vẫn phải lấy bản mới, kiểm full SHA READY rồi mới chạy; lệch thì DỪNG.
- Agent không sửa luật nền. Khi chạy: đọc `PROMPT.md`, thực hiện; tiến độ nằm ở commit công việc và **một báo cáo hiện hữu/đích báo cáo do prompt chỉ định**, không tạo file tiến độ riêng. Kết thúc chỉ báo Owner một dòng `XONG` hoặc `DỪNG`; Host/Reviewer tự đọc Git + báo cáo để nghiệm thu.

## A7_TECH — Hợp đồng kỹ thuật
- Lock, version/head, transaction, `operation_id`, các đường ghi, quyền xoá, file lớn/Unicode và giới hạn connector nằm trong **README Shared Workspace Technical Contract**; không lặp lại tại đây.

## A8_OWNER_VIEW — Một việc, một HTML chính
- **Tách SSOT tuyệt đối:** **MÃ/runtime: VPS là SSOT; NGHIÊM CẤM GitHub → VPS** dưới mọi hình thức pull/deploy/sync/ghi đè. **TÀI LIỆU công việc: GitHub/workspace là SSOT; VPS chỉ là view/mirror**, không sửa nguồn tài liệu tại VPS.
- Mỗi việc có **một thư mục riêng** và đúng **một file HTML chính dành cho Owner**. Mặc định dùng `view.html`; nếu dùng tên khác thì phải khai báo rõ trong `COLLAB.md` của việc.
- HTML chính là màn hình/sản phẩm Owner dùng để nhìn, duyệt và chỉ đạo. AI có thể dùng `COLLAB.md`, `PROMPT.md`, evidence, assets và file kỹ thuật phụ ở phía sau, nhưng không yêu cầu Owner đọc chúng nếu Owner không hỏi.
- Khi Owner yêu cầu thay đổi, AI sửa **HTML chính trong workspace/Git**. Bản hiển thị trên VPS chỉ là **mirror dẫn xuất** để Owner xem; không tạo thêm một nguồn nội dung độc lập trên VPS.
- Owner xem HTML qua URL trên VPS. Cơ chế **Cập nhật** chỉ được làm mới gói tài liệu Owner View của đúng công việc theo README §12; tuyệt đối không dùng để thay đổi mã/runtime, deploy từ GitHub hay ghi đè vùng dịch vụ.
- Quy tắc kỹ thuật chi tiết của lớp Owner View nằm trong README; mọi AI/Agent làm việc trên repo này phải giữ mô hình **một việc → một thư mục → một HTML chính → một URL Owner View**.

## A9_TASK_SIGNAL — Khung tín hiệu máy đọc cho Task Control View
- Mục đích: User nhìn dashboard biết việc đang ở đâu mà **không bắt AI nhớ thêm nhiều thao tác báo cáo**. Bộ đồng bộ tự phát hiện mọi `work/*/COLLAB.md`; tạo đúng thư mục việc + A0 là đủ để việc xuất hiện. Root `COLLAB.md` chỉ là dấu `Đã xong`/điều phối, không phải điều kiện để task mới được phát hiện.
- Khung chung có 4 giai đoạn, dùng đúng 5 trạng thái UI: `pending · done · blocked · changing · unknown`. Không suy từ văn xuôi ngoài dấu hiệu quy định:
  1. **Mục tiêu**: A0 `ĐÃ XÁC NHẬN` → `done`; `CHƯA XÁC NHẬN` → `changing`; thiếu/không đọc được → `unknown`.
  2. **Kế hoạch**: nếu Mục tiêu chưa `done` → `pending`; `READY@<SHA>` hợp lệ theo A6 → `done`; còn lại → `changing`. Không đọc trạng thái P (P được ghi nhiều kiểu khác nhau giữa các việc — đọc P là đoán văn xuôi).
  3. **Triển khai**: nếu Kế hoạch chưa `done` → `pending`; `KQ@<RUN_ID> XONG` → `done`; `KQ@<RUN_ID> DỪNG` → `blocked`; còn lại → `changing`.
  4. **Nghiệm thu**: Triển khai `done` → `changing`; chưa → `pending`. Việc nằm trong root `## Đã xong` → cả 4 giai đoạn `done`, ưu tiên cao nhất.
  5. **Chờ Owner**: mục `## Owner cần quyết` của việc có dòng không bắt đầu bằng `- —` → giai đoạn hiện hành chuyển `blocked` (đỏ = đang chờ Owner), trừ việc đã Done.
- `KQ@<RUN_ID> XONG|DỪNG` là **dấu hiệu mới duy nhất**. `<RUN_ID>` phải khớp RUN_ID hiện hành trong `PROMPT.md`; kết quả RUN cũ không được dùng cho prompt mới. Agent ghi/cập nhật dòng KQ trong cùng lượt hoàn tất/báo cáo đã được prompt yêu cầu, không tạo thêm file tiến độ hay một lượt báo riêng; sau đó vẫn trả Owner một dòng XONG/DỪNG theo A6.
- Định nghĩa dấu hiệu — máy đọc đúng chữ, không suy: **A0** = dòng đầu tiên chứa `Xác nhận User:` kèm `ĐÃ XÁC NHẬN`/`CHƯA XÁC NHẬN`. **READY hợp lệ** = dòng `READY@<40 hex>` cuối cùng không nằm trong `~~…~~`, khớp commit cuối chạm `work/<id>/PROMPT.md`. **RUN_ID hiện hành** = dòng `RUN_ID: <id>` trong `PROMPT.md`. **KQ** = dòng cuối cùng chứa `KQ@<RUN_ID hiện hành> XONG|DỪNG`. **Đã xong** = dòng dưới root `## Đã xong` chứa `` `work/<id>/` ``. **Chờ Owner** = dòng dưới `## Owner cần quyết` của việc.
- `currentStage` là giai đoạn đầu tiên chưa `done`; `Đã xong` ở root luôn thắng mọi READY/KQ cũ. Dấu hiệu có nhưng sai định dạng/không đọc được → `unknown` + cảnh báo, không đoán.
- `Vừa làm` chỉ sáng khi có bằng chứng actor/surface rõ ràng; không suy actor từ Git author/pusher dùng chung. `Đang làm` không suy từ commit. Chuẩn hoá surface tự động tại cổng ghi là việc riêng sau khi đường ống dữ liệu ổn định.
