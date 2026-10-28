# DOT + CODEX — HJW-N2-FOUR-FRESH-SESSIONS-20261027-09

RUN_ID: HJW-N2-FOUR-FRESH-SESSIONS-20261027-09
STATUS: SUPERSEDED_BY_OWNER_DIRECTION_P438; NOT_READY; CHƯA RUN; KHÔNG PHÁT LỆNH RUN09. Owner đổi hướng sang Hermes trên MacBook → CUA → Codex; xem COLLAB P438. Giữ phần dưới làm lịch sử phép thử cũ.
Repo/task: Huyen1974/incomex-workspace · work/hermes-joint-workspace.
Executor_Surface: Dot thật -> tối đa 4 Work tasks MỚI trên MacBook -> 4 ứng dụng/phiên MỚI. Codex chỉ giám sát bằng chứng và ghi P/KQ qua workspace_* D12.
Write_Path: Native desktop/browser/CLI được hãng và Owner đã cấp; không mutation production, không gateway/script mới.

## ĐỀ BÀI CỰC NGẮN

B1 Owner: Dot gọi GPT Work trên MacBook để mở phiên Work mới; Work mở phiên MỚI cho GPT Chat, Claude Chat, Claude Code CLI và Codex app; gửi mỗi nơi đúng một tin CANARY đơn giản. **Mỗi đích dùng một Work task MỚI riêng** (tối đa 4). Không cần phiên Work cũ, không cần session_ref đích trước khi mở; mã phiên chỉ ghi SAU khi đã tạo.

RUN08 P434 đã DỪNG vì Dot không chấp nhận Codex relay như xác nhận Owner. Chưa có bằng chứng Dot -> Work không được. **Không lặp Codex relay**, Owner tự gửi scope một lần vào Your dot.

Chấp nhận Work Local hoặc Work Cloud dùng local computer execution theo khả năng chính thức. Đích chứng minh là **Work thật sự thao tác được MacBook**, không phải chỉ tạo Work task ở máy Cloud. MacBook online, ChatGPT desktop app mở và Dot Computers > Your computer > Allow access đã được Owner chấp thuận khi cần.

Nguồn: https://help.openai.com/en/articles/20001530-getting-started-with-your-dot ; https://learn.chatgpt.com/docs/dots/computers-and-apps ; https://learn.chatgpt.com/docs/enterprise/cloud-local-access .

## T0. MỘT LỆNH OWNER GỬI TRỰC TIẾP DOT

Sau Host READY, Owner gửi chính Your dot:
"Tôi trực tiếp cho phép RUN09: tạo tối đa 4 GPT Work task MỚI trên MacBook đã kết nối. Mỗi Work task mở một phiên MỚI ở đúng một đích: GPT Chat, Claude Chat, Claude Code CLI, Codex app; gửi một câu kiểm tra đơn giản. Không nhắn phiên cũ, không làm nghiệp vụ, không thay quyền/cấu hình. Cho tôi biết Work task ID, ứng dụng/phiên mới, tin đã gửi/ACK hoặc lỗi. Nếu Work đầu tiên không vào được máy Mac thì dừng."

Dot cần thêm xác nhận quyền máy thì hỏi trực tiếp Owner trong app; Codex không giả danh Owner. Không giữ terminal chờ.

## T1–T4. BỐN CANARY RỜI NHAU

| Thử | Work task mới | Thao tác trên Mac | Bằng chứng |
|---|---|---|---|
| T1 | W-GPT | ChatGPT app/browser -> New Chat GPT -> gửi "RUN09 GPT CANARY. Chỉ đáp ĐÃ NHẬN GPT." | Work task ID, GPT chat mới, SENT/ACK |
| T2 | W-CLAUDE | Claude app/browser -> New Chat -> gửi "RUN09 CLAUDE CANARY. Chỉ đáp ĐÃ NHẬN CLAUDE." | Work task ID, Claude chat mới, SENT/ACK |
| T3 | W-CLAUDE-CLI | Terminal mới -> khởi động Claude Code CLI đã cài sẵn -> gửi một lời nhắn CANARY không code/không lệnh nghiệp vụ | Work task ID, terminal/CLI mới, SENT/ACK |
| T4 | W-CODEX | ChatGPT/Codex desktop app -> Codex New Task/New Chat -> gửi CANARY chỉ xác nhận đã nhận, không chạy tool/code | Work task ID, Codex task mới, SENT/ACK |

Mỗi Work task chỉ mở MỘT đích, không cần gắn vào phiên hội đồng hiện hữu. Claude/Terminal/Codex có thể là các ứng dụng riêng, không được ép tất cả nằm trong một cửa sổ ChatGPT. Không tự cài đặt hay sửa môi trường để ép xanh; không tác động các phiên sản xuất đang mở.

Chạy lần lượt từng Work canary để không tranh điều khiển cùng Mac. Nếu công cụ hãng từ chối Terminal/Claude Code CLI hoặc Codex app, ghi NOT_AVAILABLE cùng lỗi thật cho đúng đích; không dùng shell/API/ứng dụng khác để vượt lệnh chặn, không lấy Codex do Dot tạo trực tiếp thay chuỗi Work→Codex. Quyền máy không bảo đảm mọi ứng dụng đều điều khiển được. T3/T4 cũng chỉ gửi câu cố định: “RUN09 CLI CANARY. Chỉ đáp ĐÃ NHẬN CLI.” / “RUN09 CODEX CANARY. Chỉ đáp ĐÃ NHẬN CODEX.”

Thứ tự T1 trước. Nếu T1 không tạo được Work thật sự sử dụng Mac thì dừng T2–T4 và báo lý do, không lặp. Nếu đã có Work thật trên Mac nhưng một đích riêng bị chặn, ghi lỗi riêng và tiếp tục các đích khác trong quyền đã có.

## T5. NHẬN KQ VÀ DỪNG

Mỗi đích ghi ba mốc OPENED_NEW, MESSAGE_SENT, ACK_RECEIVED (hoặc NOT_AVAILABLE/ERROR); Work task ID/Activity ref, local_device, app, new session ID/link nếu hãng lộ, timestamp. Không tự đoán ID, không gán Cloud-only là Mac PASS.
Bằng chứng Mac phải là quan sát/thao tác từ công cụ trên máy được kết nối của chính Work, gắn với Work task/Activity; tên task có chữ Local hay câu tự báo không đủ. T1/T2 dùng browser thì đó phải là browser trên Mac, không phải browser cloud của Dot. Không cần tạo thêm phép thử, registry hoặc yêu cầu Owner cung cấp ID trước.

Báo Owner 3 câu: Dot -> Work trên Mac có thật không? Bốn app đạt đến đâu? Còn đúng một thao tác gì nếu cần?

Chỉ là **native capability canary**, chưa chứng minh Hội đồng tự phát tín hiệu hay tự động khép vòng. PA1 Schedule/MCP Events/GitHub webhook giữ làm việc sau, KHÔNG thêm vào RUN09. Không thêm key/gateway/cron/bridge, không sửa VPS, production, Gmail, PG, Directus, Graph, Lark, root/GSM, AGENTS A2/roster/quorum. +1 Agent Data recreate vẫn UNUSED.

STEP_WALK_V1: T0 Owner->Dot DIRECT; T1 Dot->Work NEW->GPT NEW; T2->Claude NEW; T3->Claude Code CLI NEW; T4->Codex NEW; T5 Codex/Host ghi P/KQ/Bảng/NEXT_TRIGGER theo bằng chứng. Không giữ job chờ, không tự RUN khi còn DRAFT.
