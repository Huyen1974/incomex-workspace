# CODEX — HJW-N2-EVENT-CODEX-NATIVE-20261027-06

RUN_ID: HJW-N2-EVENT-CODEX-NATIVE-20261027-06
STATUS: DRAFT_NOT_READY; chờ Claude review, GPT Host READY đúng last-touch và Owner dispatch. CHƯA RUN.
Executor_Surface: Codex Mac; Dot phải tự thực hiện các phép thử client thật; Codex không đóng giả Dot.
Task: work/hermes-joint-workspace; repo Huyen1974/incomex-workspace.
Write_Path: hồ sơ HJW qua workspace tools D12; đọc/đo MCP 2.0 bằng client/endpoint có quyền sẵn. KHÔNG sửa production, GitHub settings, hay cấu hình Dot.

## MỤC TIÊU: ĐÚNG BA VẤN ĐỀ OWNER 27/10

(1) MCP Incomex có EVENT để Dot được gọi chủ động không? (2) VPS và GitHub có thể gửi event/webhook đến Dot theo hãng không, có thể chia một nguồn event với GPT/Codex không? (3) Dot có tạo MỖI TASK MỘT PHIÊN CODEx local mới được không?

KHÔNG tự triển khai cổng/hệ thống; chỉ thử đường có sẵn rồi báo bằng chứng. Giữ N2 Native-Max A/B/C, phiếu A2 một trusted identity = một quorum; không dùng event làm Host READY/GO. P425 CLIENT_PENDING đã đóng; sau P425 có hai commit canary Dot ghi/xóa theo Owner voice, nhưng lúc ghi actor còn UNKNOWN pending receipt, không coi đó là proof danh tính riêng.

Căn cứ chính thức: https://developers.openai.com/plugins/build/mcp-events ; https://help.openai.com/en/articles/20001530-getting-started-with-your-dot ; https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex .

## E0 — KIỂM ĐÚNG KHẢ NĂNG MCP LIVE, KHÔNG SUY TỪ SỐ TOOL

Đọc AGENTS, HJW COLLAB §1–§3 P423–P426, PROMPT, HEAD, STOP/active Codex/GH, DROOT59. Kiểm MCP server đang kết nối từ Dot/Work qua trang Plugin hoặc read-only protocol call có auth hiện hữu:
- MCP server/discover có supportedVersions 2026-07-28 và capabilities.events không?
- events/list có tên/filter/schema, delivery webhook không? Có events/subscribe, events/unsubscribe không?
- plugin ChatGPT đã rescan và hiện tab Events hay chỉ Tools? Có subscription nào của Dot thật không?
Định dạng KQ: EVENTS_AVAILABLE_PROVEN / TOOLS_ONLY_CONFIRMED / UNKNOWN_NO_ACCESS. Repo tìm kiếm chưa thấy events/subscribe, đó KHÔNG đủ kết luận runtime chưa hỗ trợ. Không in token, subscription secret hoặc URL cá nhân lên repo.

OpenAI MCP Events hỗ trợ Dot và Work Cloud, callback HTTPS do ChatGPT cấp sau sự kiện đăng ký, giao thức MCP 2.0 2026-07-28; không phải polling, SSE hay công cụ thường. ChatGPT/GPT Chat thường và Codex Desktop KHÔNG mặc nhiên là hai MCP Events subscribers chỉ vì đang dùng chung công cụ.

## E1 — THỬ 1 EVENT/WEBHOOK NẾU ĐÃ CÓ ĐƯỜNG CHÍNH THỨC

Nếu Events tồn tại và Owner đã trực tiếp cho Dot subscribe: kiểm một subscription riêng của Dot, filter HJW, callback URL/secret do ChatGPT gửi từ events/subscribe. Kiểm callback verification challenge và Standard Webhooks signature; phát duy nhất một event CANARY nhẹ mang task_id, commit, eventId, timestamp, không có secret và không có lệnh ghi production. 2xx mới là nhận HTTP; Dot phải thực sự phản hồi bằng đọc repo/HEAD mới tính live PASS. EventId lặp không được tạo trùng task. Ngăn event loop do chính tác vụ sinh ra.

GitHub: đường native event-triggered Work task của OpenAI hỗ trợ GitHub PR activity; đó là Work trigger, CHƯA phải Dot event trực tiếp. Xem GH Plugin event catalog thực tế trước. Owner View đã có webhook GitHub push vào /api/knowledge/owner-view-webhook, tuyệt đối không sửa/chiếm endpoint này. Không tự post thẳng vào URL trang Dot; phương án VPS -> MCP Events -> callback ChatGPT chỉ hoạt động sau subscription thực.

Nếu E0 không thấy Events, E1 ghi NOT_IMPLEMENTED/UNVERIFIED, không viết MCP v2 handler, không tạo listener, proxy, timer hoặc server mới. Nếu Owner thật sự cần VPS gọi Dot, trình đúng một phương án sửa tối thiểu endpoint MCP HIỆN HỮU theo tài liệu hãng, chỉ thi công sau Owner phê duyệt.

## E2 — DOT TẠO CODEX NEW TASK, MỖI TASK MỘT PHIÊN ĐỘC LẬP

Nhờ Dot THẬT tạo một Codex task CHỈ ĐỌC: lấy HEAD HJW và tóm tắt 3 dòng. Không điều khiển phiên Codex hiện đang làm GitHub.
- Local: chỉ thử khi Owner đã bật Computers > Your computer > Allow access trong ChatGPT desktop và Mac/ChatGPT app online. Kiểm tác vụ Codex riêng mới ở sidebar, có task ID, thời điểm, kết quả, không trộn history của các task khác.
- Cloud: nếu environment Codex Cloud đã publish, Dot có thể tạo một task cloud riêng; kiểm task ID và output. Không yêu cầu Mac bật.
- Phân biệt rõ Dot TẠO TASK MỚI (được tài liệu hãng hỗ trợ) với Dot ĐIỀU KHIỂN GUI CODEx Desktop / gửi lệnh vào phiên đang mở (CHƯA chứng minh). Không dùng CLI app-server, AppleScript, SDK tự dựng chỉ để thử, không giả login/Owner approval. Nếu thiếu quyền local, ghi CLIENT_ONLY_PENDING với một nút cần bấm và kết thúc sạch, không giữ terminal chờ.

## E3 — MỘT NGUỒN EVENT, CÁC SUBSCRIBER ĐỘC LẬP

Có thể tái sử dụng cùng nguồn/tên event cho Dot và Work khi được hãng hỗ trợ, nhưng mỗi subscriber PHẢI có subscription_id, callback URL, signing secret, filters, quyền và biên nhận riêng. Không gom chung secret/callback hay tạo phiếu quorum thứ hai từ cùng server identity. Event chỉ báo tình trạng, không tự cấp Host GO, không tự tạo lệnh worker. Codex được Dot giao bằng native task, không coi Codex là subscriber MCP Events nếu chưa có chứng cứ.

## E4 — ĐÓNG CÓ BẰNG CHỨNG

Báo 4 dòng: (1) MCP Events trạng thái và proof live, (2) GitHub PR/Owner View vs Dot/VPS webhook canary, (3) Dot tạo Codex local NEW TASK / Cloud task ID riêng, (4) một việc tối thiểu tiếp theo (hoặc NONE). Dùng PASS / PARTIAL / UNKNOWN / CLIENT_PENDING đúng thực, không khai LIVE_PASS chỉ từ tài liệu/HTTP 2xx. Ghi HJW P/KQ, Bảng, NEXT_TRIGGER; giữ +1 Agent Data recreate UNUSED và N3–N6. Không đổi quorum/roster, không sửa production.

STEP_WALK_V1: E0 read-only discovery -> E1 một signed event nếu đã hỗ trợ và Dot đã subscribe -> E2 một new Codex native read-only task từ Dot -> E3 fanout/security judgement -> E4 evidence/KQ. Thiếu điều kiện thì SKIP đúng nhánh, không mở job chờ.

CẤM: tự nâng MCP server, đổi nginx/GH webhook/Owner View, cài bridge/proxy/SDK, lập script trigger Dot không chính thức, tạo credential/key mới, cấp root/GSM, in secret, gửi email, tự điều khiển phiên Codex đang làm việc, lập event lặp gây spam.
