# CODEX — HJW-N2-DOT-WAKE-WORK-MAC-20261027-08

RUN_ID: HJW-N2-DOT-WAKE-WORK-MAC-20261027-08
STATUS: DRAFT until GPT Host READY exact last-touch SHA and Owner dispatch; do not self-start.
Executor_Surface: Codex Mac for evidence; Dot and Work themselves execute native actions.
Task: work/hermes-joint-workspace in Huyen1974/incomex-workspace.
Write_Path: workspace_* / fs_* D12 for P/KQ. No VPS/GitHub production mutation or new gateway.

## 0. ĐÍCH CUỐI CÙNG, HIỂU MỘT CÁCH

Đọc AGENTS, HJW COLLAB §1–§3/roadmap và P425–P431. Owner đã thử GPT Work LOCAL Mac điều khiển đúng các phiên GPT Chat/Claude Chat nhiều lần; đó là lý do bỏ Hermes Mac. KHÔNG kiểm lại cả chuỗi thao tác đã chứng minh.

ĐÍCH: Hội đồng/Host báo đến lượt ghế X tại task A → Dot đọc assignment hợp lệ → DOT ĐÁNH THỨC ĐÚNG WORK LOCAL trên MacBook/Mac mini → Work nhắc đúng phiên GPT/Claude X đã gắn với task A → phiên X ghi P/KQ vào đúng repo → Work/Dot nhận ACK.

MẮT XÍCH DUY NHẤT CẦN CHỐT TRONG RUN: làm sao Dot đánh thức Work LOCAL đúng task, không Owner gõ tay. Không thay câu hỏi này bằng "MCP có Events?" hay "Dot tạo được Codex Cloud?" vì đó là hai vấn đề khác.

PA2 PUSH (ưu tiên): Dot gửi native vào phiên Work đã gắn task nếu hãng có route; nếu không, Dot tạo NEW Work LOCAL task trên đúng máy và truyền đủ task_path, assignment, target_chat_session_ref. NEW task không phải Work chat cũ và không tự kế thừa context; Work CLOUD task không chứng minh Work LOCAL đã thức.
PA1 PULL (dự phòng sau PA2 fail): Work/Dot native Scheduled Tasks tự đọc hàng chờ HJW COLLAB/ASSIGN_V1 khi Mac bật, rồi thực sự kích hoạt Work LOCAL. Work CLOUD chỉ tự đọc repo chưa đóng vòng; không tự viết cron/launchd/relay.

MCP Events phục vụ Hội đồng/VPS/GitHub→Dot hoặc Work CLOUD nếu có, KHÔNG mặc nhiên là tín hiệu tới Work LOCAL. Mac offline thì WAITING_DEVICE, không tuyên chạy 24/7. Giữ Native-Max A/B/C và A2 1 trusted identity = 1 quorum vote.

Nguồn hãng:
https://help.openai.com/en/articles/20001530-getting-started-with-your-dot
https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt
https://developers.openai.com/plugins/build/mcp-events

## 1. HỢP ĐỒNG ĐÚNG ĐÍCH — DÙNG SỔ ĐANG CÓ

Không tạo registry hay router mới. Mỗi yêu cầu tới lượt phải xác định: task_path/assignment/Host GO/HEAD; intended Work existing_session_ref hoặc NEW work_task_id; device_ref; đúng target GPT_CHAT hoặc CLAUDE_CHAT session_ref đã có nguồn hợp lệ; trigger_id, deadline, actual_receiver_ref, ACK và P/KQ receipt. Nếu thiếu đúng session_ref thì KHÔNG gửi vào tab gần nhất hoặc phiên cùng tên.

NEW Work task phải tự đọc đủ task_path, assignment, target_chat_session_ref; CONTEXT_NOT_BOUND nếu không có. Trạng thái độc lập: DOT_SIGNALLED; WORK_LOCAL_STARTED (đúng máy/task); CHAT_DELIVERED (đúng session với ACK); REPO_KQ_COMMITTED. Tạo Cloud task/HTTP 2xx KHÔNG thay được chứng cứ Work LOCAL. Không đổi Host/Owner authorization hay tự tính phiếu thứ hai.

## W0. ĐỌC MỘT LẦN

Codex kiểm HEAD, READY đúng SHA, Owner RUN, STOP/active sessions, Mac online/ChatGPT app và quyền Dot Computers > Your computer > Allow access, Work task/session ref và một GPT/Claude TEST session-ref nếu có. Nếu thiếu quyền chính chủ, báo đúng một bước cần bấm; không giữ terminal/lease đợi.

Kiểm phụ MCP Incomex có server/discover 2026-07-28, events/list thật chưa nếu có quyền, ghi PROVEN/TOOLS_ONLY/UNKNOWN. Không để Events (Dot/Work CLOUD, không chứng minh Local) thành gate W1.

## W1. THỬ PA2 TRƯỚC — TỐI ĐA MỘT CANARY

Owner trực tiếp cho Dot một canary chỉ đọc hoặc Dot dùng quyền đã được hãng xác minh; Codex không giả Owner. Dot thử route chính thức tới existing Work chat đúng task (nếu có), hoặc tạo NEW Work LOCAL task ở đúng Mac đã cấp quyền. Ghi Work task ID/activation ref, device, start-time và Work đọc đúng assignment/session ref. NEW Work chỉ PASS khi đúng Mac/context; NEW Cloud task = CLOUD_ONLY_NOT_LOCAL.

Nếu có phiên GPT/Claude TEST được Owner chỉ định, Work gửi một nhắc vô hại vào đúng session, kiểm ACK/P-KQ. Nếu chưa có session_ref, không gửi, chỉ đo Work LOCAL_STARTED. PA2_LOCAL_WAKE_PASS khi Work Local thực sự chạy đúng task, PA2_END_TO_END_PASS khi có thêm Chat ACK/KQ. PA2 không có native route → PA2_NO_NATIVE_ROUTE và chuyển W2, không chế gateway.

## W2. PA1 CHỈ NẾU PA2 KHÔNG ĐẠT

Xác minh Scheduled Tasks Work/Dot native có thể tự phát một lượt kiểm HJW COLLAB/ASSIGN_V1 không người gõ, VÀ khi Mac online thực sự làm Work LOCAL chạy. Chỉ thử một scheduled canary nếu tài khoản và Owner cho phép; không cài recurrence vô hạn. Ghi schedule ID, thời gian fire, Work LOCAL task ID và độ trễ.

Nếu chỉ Work CLOUD scheduled đọc repo = DISCOVERY_ONLY, không gọi fallback khép vòng. Không hứa 1–5 phút: lịch native hãng có giới hạn (công bố không quá một lần/giờ và có thể pause). Thiếu native Local wake thì PA1_NOT_PROVEN, báo thật; không viết cron/launchd.

## W3. KHẢ NĂNG PHỤ KHÔNG CHẶN W1

MCP Events/GitHub nếu có báo tới Dot/Work CLOUD; không sửa Owner View webhook hay triển khai MCP 2.0 chỉ để thử. Dot tạo Codex LOCAL/CLOUD NEW task chỉ kiểm một ca đọc HEAD nếu đã sẵn có, không thay Work Local, không ảnh hưởng Codex đang làm việc. Work điều khiển phiên Chat đã Owner thử nhiều, không diễn tập dài.

## W4. BÁO BẰNG CHỨNG VÀ ĐÓNG

Bảng sáu hàng: nguồn→Dot, Dot→Work existing, Dot→NEW Work LOCAL đúng Mac/context, Work→đúng GPT/Claude TEST session/ACK, PA1 scheduled repo pull→Work LOCAL, Dot→Codex phụ. Nhãn: PA2_END_TO_END_PASS; PA2_LOCAL_WAKE_PASS_WITH_LIMITS; PA2_NO_NATIVE_ROUTE_PA1_TESTED; PA1_NOT_PROVEN; CLIENT_PENDING. Không gọi full automation khi chỉ task Cloud. Ghi P/KQ/Bảng/roadmap/NEXT_TRIGGER duy nhất. 0 VPS mutation, không giữ job chờ Owner, +1 Agent Data recreate UNUSED.

CẤM thêm key/bridge/webhook/router/Hermes Mac/launchd/cron, chỉnh production/nginx/PG/Directus/Graph/Lark/root/GSM/Gmail/GitHub webhook, đổi A2/quorum hoặc gửi nhầm GPT/Claude phiên chat.

STEP_WALK_V1:
| Step | Executor/trigger | Evidence | If missing |
|---|---|---|---|
| W0 | Codex; Host READY/Owner GO | HEAD, rights, device, refs | CLIENT_PENDING |
| W1 | Dot→Work LOCAL | task, Mac, context and ACK if possible | PA2_FAIL→W2 |
| W2 | Native Work/Dot scheduler if W1 fails | scheduled fire AND Work Local start | PA1_NOT_PROVEN |
| W3 | Codex optional RO | Events/Codex native result | SKIP |
| W4 | Codex | six statuses, repo KQ, one NEXT | stop honestly |
