# HJW · N3 HERMES VPS CAPABILITY V2 — KHÉP A3/A4 + B/C/D/E
RUN_ID: HJW-HERMES-CAPABILITY-20261022-02
STATUS: DRAFT_HOST_P348 · CHƯA REVIEW/READY/RUN.
Host: GPT Chat · Reviewer độc lập: Claude Chat (không phải Claude Code executor) · Executor tương lai: Claude Code CLI qua Owner chuyển tay.
Based_on: P347 KQ DỪNG/PARTIAL commit a23e8fc4c1336c3a97ad3b46d4908e1c1e0f4ddf.
Scope: N3 Hermes VPS thực dụng; HUMAN_DIRECTIVE@HJW-OWNER-20261022-02 bỏ Hermes Mac/Courier, không điều khiển GPT/Claude qua Hermes.

## 0. Điều kiện đã đạt — KHÔNG làm lại
- P347 A1 đọc Workspace 7 tool PASS, bad-key 401; F hermes-safe-update PASS, exit10 báo có bản v0.22.4 nhưng Hermes vẫn v0.22.2 (KHÔNG tự nâng); SUDO/root tuỳ ý + GSM trực tiếp bị chặn, Neo4j/PG raw secrets không nằm ở môi trường Hermes; Guard POST 22/22, mid260; VPS-GHI trả, 0 RUN active.
- Chưa đạt: A3/4 write guard; B Graph kết nối an toàn; C log thật đã lọc; D PG dữ liệu được phép; E tác vụ qua helper. Vé canary HJW ghi HPML sai rule cùng task, chưa có thẻ, chưa có write Hermes thật.
- N3 chưa hoàn thành; không mở N4–N6 và không tự bật AUTO. READY cũ 7038d93b đã KQ DỪNG, không được dùng lại.

## S0 — Read-gate và chụp sự thật sống
Đọc AGENTS.md, root COLLAB, HJW Bảng/mục 0.9, 1–3/P343–P348, hjw_gate.py + v1_check, agent_data/workspace_tools.py, workspace-tools.json, helper/priv.conf, graph-v1 doctor, PG roles/views, collector status, Guard INV7/INV19, 22 đèn. PRE đo 0 STARTED/STOP xung đột, VPS-GHI sẵn sàng, 4 master profiles, Hermes 7 tool, danh sách write_scope đang có, vé được dispatcher phục vụ, baseline gateway/Graph/PG/Directus/updater. Không quét lại F/A1. Chỉ chiếm VPS-GHI sát mutation, dùng CAS/backup/rollback và nhả sạch.
Mọi dấu vết credential chỉ là tên/identity/scope, không in key/secret, địa chỉ riêng hoặc dữ liệu nghiệp vụ vào repo công khai.

## S1 — P0 ĐÓNG QUYỀN GHI HIỆN HỮU TRƯỚC KHI MỞ CAPABILITY
P347 đã đo: hjw_gate.py chạy UID hermes và dùng cùng HERMES_AGENT_GW_KEY với model; key root:hermes 0640/UID hermes đọc được. Đây là CHUNG một security principal, model có thể giả lệnh Host, READY@, KQ@, ASSIGN_V1/RESULT_V1. Wildcard work/*/COLLAB.md cộng quyền cả thư mục HJW/TQT đang mở trước lượt này — chỉ gỡ wildcard mà giữ write thư mục rộng vẫn không khép an toàn.
1. Tách THẬT bộ điều phối khỏi model: đưa ghi state/RESULT_V1 của dispatcher vào identity/backend trusted server-owned (ưu tiên reuse incomex-mcp-helper/agent-data), credential/sudo/machine-zone writer model UID hermes KHÔNG đọc/gọi tùy ý; không chỉ tạo 2 tên profile hoặc 2 key đều nằm trong env/tệp của cùng UID. Server chứng minh trusted caller bằng credential/UID/cửa số hữu hạn, không tin clientInfo/author/agent-provided text. Giữ luồng Owner approve→claim→result, không xây gateway mới.
2. Trước mutation bảo đảm rollback, kiểm toàn bộ active assignment của HJW/TQT và consumer thực; không làm gãy 4 master profiles. Sau khi dispatcher tách và smoke PASS, cắt quyền MODEL wildcard và scope cả folder quá rộng; đúng file COLLAB của đúng task có ASSIGN Host/server-authorized mới được edit. Không để key MODEL sửa PROMPT.md, AGENTS, root COLLAB, code, Guard, machine zone, trạng thái.
3. Trong gateway handler dưới cùng CAS/lock, dựng hậu ảnh sau MỌI op và kiểm diff trước commit: model chỉ được append một mục P phi điều hành trong task được phép, không đổi byte cũ, không thể đổi state=open→done, không ghép token Host/ASSIGN/KQ qua nhiều lời gọi. old_str/new_str denylist chỉ là lớp nhanh. workspace_transaction chỉ op edit; copy/move/write_new, exec/task/admin denied. Dispatcher trusted mới có quyền cập nhật machine assignments, không thể bị model gọi giả.
4. Test âm gồm giả Host/READY/KQ/ASSIGN/RESULT/SPEC, sửa trạng thái, nhiều edit ghép chuỗi cấm, edit ngoài task/PROMPT/done-tasks, mượn dispatcher key/queue, bypass qua transaction; không mutation. Test dương append P từ model được phép, 4 master profiles/Guard không regress.
5. Nếu không tách được identity hoặc guard không khép: **không cấp thêm B/C/D/E/A4**; đưa model về quyền đọc hoặc phạm vi đã cô lập tối thiểu và ghi rõ ảnh hưởng dispatcher, tránh rollback mù thành cấu hình wildcard không guard; kết thúc KQ DỪNG với blocker một chủ/trigger, không để nửa vời.

## S2 — Canary THẬT, đúng vùng máy
Vé cũ HJW-HERMES-CAP-WRITE-CANARY-20261022-01 ở HJW mà target HPML ⇒ v1_check INVALID; không tái sử dụng, không phát từ vé invalid. Tạo ticket mới với ASSIGN_V1+SPEC_V1 cùng MACHINE_ASSIGNMENTS_V1 của HJW, write[] CHỈ work/hermes-joint-workspace/COLLAB.md, task role Reviewer, sau S1 PASS. Owner bấm một lần; Hermes phiên thật tự append P vô hại bằng danh tính MODEL; dispatcher identity trusted cập nhật claim/state/RESULT. Executor không mượn Hermes credential/author. Positive write và negative của S1 phải có receipt.
**A4 đa task** chỉ PASS nếu có một ticket đúng vùng máy của TASK KHÁC, task không RUN và chính Host/Owner của task đích cho phép; nếu chỉ HJW canary đạt thì A3 PASS có giới hạn và A4 vẫn PARTIAL. Không tự tạo machine-zone/vé ở HPML hay làm bẩn TQT để tô xanh. Thiếu nút/Owner không duyệt ⇒ KQ DỪNG, không chờ/hẹn/poll model.

## S3 — B/C/E: REUSE helper-priv + một delta gateway bảo vệ chặt
Không cấp thêm tool Hermes trước khi S1/S2 đạt. Dựng adapter và test ở phía server trước rồi expose có feature gate chỉ sau canary. Sửa mã Agent Data một pha, thử rollback trước khi bật, cập nhật Guard INV7/INV19 theo chính tập tool đã duyệt (không bỏ kiểm/không nới mọi profile), kiểm lại master profiles.
B GRAPH: graph-v1 doctor P347 PASS nhưng Neo4j host loopback/mạng riêng không reachable từ container agent-data. Dùng đúng host helper root thực đơn cố định + priv.conf và queue bounded vào agent-data, không chia credential Neo4j/GSM cho Hermes. Chỉ get-schema/read-cypher thực sự read-only, có validation cho cú pháp cho phép, giới hạn row/time/query resources cưỡng chế host + kill, chặn CREATE/MERGE/write-CALL và đường vượt LIMIT/secret/loop/timeout. Đọc schema, COUNT node/edge và một quan hệ thực được phép. Giữ Graph C0/C1/PG schema.
C LOG: profile agent hiện không thể chỉ bật vps_status bằng config. Bổ sung code gateway chặn tham số section/service, bộ thu phải lấy log THẬT của hermes-serve/gateway/safe-update và service allowlist khác có ích (20–100 dòng, mốc mới, có dòng khác rỗng), redaction TỪNG DÒNG trước model, thử chuỗi hình dạng secret cố ý phải biến mất. Không cấp journal/raw file quyền toàn hệ, ngoài allowlist DENIED.
E OPS: qua cùng helper-priv với menu cố định/dry-run/receipt, Host/Owner có quyền mới phê thao tác ảnh hưởng prod; Hermes không tự có sudo/root/argv/shell hay docker.sock. Chứng minh một dry-run/an toàn và một negative hành động ngoài allowlist; không restart production chỉ để test.

## S4 — D PostgreSQL: whitelist nghiệp vụ MỘT LẦN, KHÔNG đọc tràn
P347: context_pack_readonly đọc được directus_users/sessions/settings/shares nên KHÔNG cấp nguyên role cho Hermes. Không đưa token Directus hoặc PGPASSWORD/.pgpass cho UID hermes.
S0 inventory catalog chỉ-read; đề xuất danh sách CỤ THỂ các view/bảng thống kê vận hành không chứa PII/secret (ưu tiên COUNT/metadata/quan hệ công việc đúng nhu cầu), Host/Owner chốt whitelist một lần trước activation. Mặc định deny directus_* liên quan người dùng, session, settings, shares, auth, dữ liệu khách hàng/PII. Một service role SELECT đúng whitelist, query typed/fixed-template trên gateway host-held auth, bounded time/rows, SQL negative DML/DDL/read ngoài whitelist. Nếu không có whitelist chứng minh được/Owner chưa duyệt ⇒ D=BLOCKED_DATA_POLICY, không dùng role rộng để giả PASS và không kéo tụt B/C/E nếu an toàn.

## S5 — KQ/ĐO/ROLLBACK
Một STARTED và một KQ XONG/DỪNG của RUN 02. Bảng A1/F=PASS_BROUGHT_FORWARD; A3_IDENTITY_GUARD, A4_OTHER_TASK, CANARY_REAL, B_GRAPH, C_LOG, D_PG, E_OPS, SUDO_GSM_NO_RAW_SECRET, GUARD/22LIGHTS, có PASS/PARTIAL/BLOCKED và evidence. Giữ máy sạch, no leaks, 4 master profiles đúng, Guard PRE/POST/receipt, watchdog+rollback; không giữ VPS-GHI/terminal/job/model sau KQ. Nếu S1 đỏ/danh tính không tách ⇒ không bật capability, KQ DỪNG; nếu canary chưa chạy thật ⇒ không expose tools.
CẤM: Hermes Mac/Courier/điều khiển GPT/Claude, tự nâng Hermes v0.22.4, root/sudo tùy ý, GSM trực tiếp, raw secret, PG write/schema, Graph C0/C1 write, AUTO tự phát, lịch chờ, nới phạm vi ngoài A3/A4/B/C/D/E.

## CLAUDE CHAT REVIEW MỘT VÒNG — CHỈ REVIEW, KHÔNG RUN
Claude Chat khác với Claude Code executor rà kỹ P347 + mã đang chạy, cho ý kiến hoặc SỬA THẲNG DRAFT bằng dấu [R]:
(1) tách UID/key backend trusted sao cho UID hermes/model không đọc được và dispatcher N3 vẫn hoạt động;
(2) thu wildcard và folder write quá rộng: danh sách consumer bị ảnh hưởng, thứ tự apply/rollback giữ dịch vụ;
(3) v1_check canary ở HJW và test khác task đúng Host/Owner, không tạo vé invalid;
(4) B/C/E helper/Guard thực tế và danh sách PG whitelist cụ thể có chứng cứ.
Nếu 0 blocker trọng yếu, Claude Chat ghi P349 REVIEWED@<exact-last-touch> ACCEPT; nếu blocker thì sửa DRAFT một lần và ký SHA mới, hoặc PARTIAL nêu đúng blocker. Sau ACCEPT chỉ GPT Host READY exact SHA, Owner mới dán CLI; DRAFT này không cho phép chạy.
