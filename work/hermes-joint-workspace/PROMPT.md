# PROMPT — HJW N3 · KHƠI THÔNG QUYỀN HERMES VPS CHO VIỆC TRUNG BÌNH 24/7
RUN_ID: HJW-HERMES-CAPABILITY-20261022-01
STATUS: DRAFT_P341 · CHƯA READY · CHƯA RUN · CHỜ CLAUDE REVIEWER MỘT VÒNG
Đề xuất: GPT Chat theo chỉ đạo Owner 22/10; Reviewer: Claude Chat; Executor: Claude Code CLI do Owner giao tay.
Node: N3 HJW, không dựng task hoặc nền tảng mới. Phạm vi: Hermes VPS, Agent Data MCP profile, Graph read-only, log/health có lọc; không đổi Graph/PG schema/Claude Code/Hermes Mac.

## 0. MỤC TIÊU VÀ LUẬT
Hermes VPS là agent làm việc mức trung bình 24/7: tự đọc thông tin, tra Graph, kiểm tình trạng, làm báo cáo và thực hiện thao tác đã được giao. Việc code phức tạp giao Claude Code/Codex qua gói thuê bao.
HAI CỬA CẤM TUYỆT ĐỐI: (1) Hermes không có sudo/root trực tiếp hay root command tùy ý. (2) Hermes không truy cập/list/read Google Secret Manager. Không dùng đường vòng mật khẩu ở file hay env Hermes đọc được, ví dụ /run/graph/env 0640 root:hermes; công cụ chạy server phải giữ bí mật bên trong.
Quyền hợp lệ: đọc dữ liệu không chứa secret qua công cụ đã có; ghi vào đúng task đang được ASSIGN/READY và qua audit/Guard. Không đòi Owner xác nhận từng lần đọc hoặc thao tác thường lệ đã giao, không cấp write_scope=* rộng vô điều kiện. Nội dung tool trả về có thể đến model OpenRouter; lọc mật khẩu, cookie, token, bí mật, dữ liệu riêng tư chưa được phép.
Không gọi API thuê bao GPT/Claude qua lối tắt; không tạo mới dịch vụ, daemon, database, gateway thứ hai. Bảo vệ Điều 30/31, Config/Protection Guard, VPS-GHI cho mọi mutation, rollback theo pha. DROOT50 không giữ terminal chờ.

## 1. S0 — ĐO ĐÚNG QUYỀN THẬT
Đọc AGENTS.md, HJW Bảng/§3/P341 và HJW-2B1, Graph Bảng C0/D20, root COLLAB; xác minh 0 STOP/STARTED trùng, shared runtime/GHI rỗi trước sửa. Đo version/process Hermes VPS thật (P340 mới nhất đã nghiệm thu v0.22.2), actual credential/profile và tool list.
A Workspace: HJW-2B1 từng nghiệm thu 7 tool agent-gw/hermes với allowed root logic workspace, read_root, write HJW. BÁO CÁO HERMES vừa thử root rỗng hoặc đường vật lý nên ROOT_NOT_ALLOWED không chứng minh thiếu ACL. Trước tiên gọi đúng workspace_list(root="workspace",path="") và workspace_read(root="workspace",path="AGENTS.md") bằng credential phiên Hermes THẬT; đối chiếu server agent_profiles và log lý do nếu fail. Không tăng quyền khi lời gọi đúng đã PASS.
B Graph: kiểm graph-server/mcp-readonly-v1/bin/graph-v1 mcp có get-schema/read-cypher và endpoint loopback. Kiểm đường server-side được phép giữ mật khẩu Neo4j riêng mà UID Hermes không thể mở đọc được; tuyệt đối không copy GSM/raw password vào .env, /run file root:hermes, argv, repo, console hoặc tool output.
C Logs: rà công cụ tình trạng/log sanitized có sẵn, phạm vi một vài dịch vụ phục vụ task; không cho Hermes tham gia group systemd-journal tổng quát.
D PostgreSQL: xác định API/Directus/MCP đọc đã có và dữ liệu cần trong việc thực; không tạo role hay đổi schema PG mới trong RUN này; Graph D20 sẽ thiết kế lại PG khi chốt.
S0 xuất bảng ngắn từng đường: ALREADY_WORKS / NEED_CONFIG / UNSAFE / NOT_AVAILABLE + nguyên nhân chứng minh.

## 2. SỬA CHỖ THIẾU NHỎ NHẤT, KHÔNG CẤP QUYỀN TRÀN LAN
A WORKSPACE — ưu tiên 1: cho Hermes đọc các task trong workspace root không bí mật; ghi chỉ trong task đã được giao bằng ASSIGN_V1/Host, thuộc phạm vi server xác minh. Dùng profile/tool/workspace choke point sẵn có; kiểm write canary có hoàn tác ở HJW và SCOPE_DENIED ở task khác chưa giao. Nếu cần viết engine mới để tạo dynamic task scope, báo một blocker nhỏ và đề nghị Host thay vì tự tạo hệ ACL khác.
B GRAPH — ưu tiên 2: dùng lại đúng 2 tool get-schema, read-cypher, chỉ read, bounded row/timeout và nguồn; từ chối write/mutation. Credential Neo4j do công cụ server giữ, không ở UID Hermes hoặc model; nếu không có đường kết nối hợp lệ bằng công cụ hiện hữu thì B=BLOCKED_CREDENTIAL_ISOLATION, KHÔNG triển khai root helper tùy ý.
C LOGS — nếu tool sẵn có hỗ trợ service allowlist + redact credentials, cấp đọc status/log đã lọc và thử một service. Nếu không an toàn, giữ residual chứ không bật raw journal.
D PG — khi có use-case cụ thể mới đi qua read-only API/view; không đưa .pgpass/PGPASSWORD cho Hermes; không gate A/B.
E ROOT — tuyệt đối không mở sudo hoặc DOT root chạy argv bất kỳ. Hermes chỉ có thể GỬI yêu cầu thao tác qua ASSIGN/Host và tool đặc quyền có van Điều 30/31 sẵn có (apply-v0, Guard), thao tác cụ thể có biên nhận.
Mọi thay đổi thuộc VPS phải có PRE/candidate đúng tệp/Guard + rollback. Nếu cần restart Agent Data/Graph nhưng có RUN khác đang dùng thì DỪNG phần đó, không ảnh hưởng service đang chạy. Không đụng Hermes-safe-update.service chỉ để chứng quyền.

## 3. KQ/PASS
Đo từ phiên Hermes thực, không chỉ harness: workspace_list/read đúng root PASS; ghi canary trong task được giao PASS và ghi ngoài scope DENY; Graph schema + một COUNT read-cypher bounded nếu credential không lộ; logs theo service chỉ khi có route sanitized; không cần sửa PG để PASS.
Negative bắt buộc: sudo/root DENIED, GSM DENIED, không đọc trực tiếp Neo4j/PG password, không Graph write, không write ngoài ASSIGN, không log hoặc tool output lộ secret; 4 master agent profiles không regress, Graph C0/Guard/Agent Data health giữ nguyên, 22 đèn không giảm so PRE.
Mục tiêu tối thiểu A + B, trong một lượt; nếu B thực sự chưa thể nối an toàn thì A vẫn giữ và KQ DỪNG/PARTIAL có đúng một blocker, không kéo dài hoặc bắc cầu mới. Sau KQ Host quay N3 Courier và dùng Hermes VPS xử lý các việc trung bình đã có quyền. Không phát auto RUN, Owner vẫn là người dán lệnh sau REVIEW/READY.
