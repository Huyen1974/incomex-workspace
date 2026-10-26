# CODEX — HJW-N2-DOT-NATIVE-FIRST-20261026-03

RUN_ID: HJW-N2-DOT-NATIVE-FIRST-20261026-03
STATUS: DRAFT — CHƯA READY, CHƯA OWNER RUN, CHƯA ĐỔI TIÊU CHÍ NGHIỆM THU N2.
Executor_Surface: Codex Mac, nghiệm thu thực từ Dot/Owner.
Task: work/hermes-joint-workspace; Repo: Huyen1974/incomex-workspace.
Write_Path: workspace gateway đúng D12 cho hồ sơ; Dot/Work/Codex cloud/local theo công cụ HÃNG có sẵn. KHÔNG ghi VPS/production.

## 0 — Nguồn và phạm vi

Đọc AGENTS, HJW COLLAB §1–§3, P398/P407/P408/P410/P413/P415/P416 và HUMAN_DIRECTIVE HJW-OWNER-20261026-07 (26/10 23:00). Mục tiêu Owner cũ chưa bị hủy: Dot có danh tính riêng, ghế độc lập/quorum không trùng, đủ capability, báo cáo tiến độ bằng thoại. Chỉ đạo mới ưu tiên: Dot làm người điều phối, đọc/ghi báo cáo, nhắc hội đồng, giao công việc nặng cho Codex/Work; tận dụng công cụ hãng, KHÔNG tự dựng thêm cầu nối/connector phức tạp. Phần gợi ý tạm không coi Graph/PG/Directus/Lark/root là gate cho giai đoạn đầu là ý kiến Claude, CHƯA được Owner chốt thay §1–§2.

Bản này chỉ là native capability CANARY với chứng cứ thực, không triển khai root/GSM, không sửa Plugin Gmail, không cấp/đổi secret, không dùng một forward recreate Agent Data còn lại. Không khởi chạy khi GitHub C1B P65 hoặc việc khác đang dùng resource; phần đọc repo có thể tiến hành không tranh VPS-GHI khi Host và Owner đã giao đúng RUN.

Căn cứ hãng: https://help.openai.com/en/articles/20001530-getting-started-with-your-dot
Codex Cloud: https://help.openai.com/en/articles/20001545-using-codex-cloud

## S0 — Check vào đúng nguồn

Đọc và kiểm HEAD, Host, roster, trạng thái READY/Owner GO mới. Không dùng READY của S1-CLOSE đã KQ DỪNG. Phần chỉ đọc không cần VPS-GHI. Nếu thao tác cần người dùng/Plugin confirmation, không giữ terminal/cờ chờ, gom thành một danh sách ngắn ở KQ. Nếu phần Mac còn bận GitHub C1B thì không chen ngang.

## S1 — Dot thật đọc/ghi SSOT và thoại

Kiểm Dot có thể sử dụng Plugin/GitHub/Incomex MCP hiện có để đọc AGENTS, HJW COLLAB/Bảng/HEAD và trả báo cáo có commit/timestamp. Owner khởi tạo cuộc gọi Live để kiểm tiếng nói; Dot không tự gọi Owner. Không lấy GPT/Codex thực hiện thay để báo Dot PASS.

Chỉ khi có quyền giao hợp lệ, Dot thử một ý kiến vô hại trong HJW qua workspace gateway với operation_id + commit/receipt. Kiểm identity do máy chủ ghi; client tự ghi tên Dot KHÔNG chứng minh ghế khác. Nếu shared OpenAI identity, chỉ ghi COORDINATION_CANARY_SHARED_ID; KHÔNG thêm ghế hoặc phiếu độc lập, không đổi Host. Nếu máy chủ thực sự xác minh openai-dot thì mới ghi INDEPENDENT_SEAT_PASS.

Nếu thiếu identity riêng nhưng vẫn làm được việc điều phối, giữ canary ở mức điều phối. Nếu một profile B1 nhỏ đã có sẵn đủ dùng, ghi rõ; không triển khai candidate P415 hay xin thêm gateway/bridge để có identity trong bước này.

## S2 — Dot giao Codex/Work bằng đường có sẵn

Dot có thể tạo Codex Cloud task trong environment đã publish, hoặc tạo Work/Codex local task khi Owner đã bật truy cập máy và máy đang online. Tách Cloud vs Local, không hứa gọi được một phiên GPT/Claude Chat đang mở. Làm canary bằng một việc chỉ đọc hoặc fixture vô hại, không gửi lệnh root/ghi production.

Ghi ID của tác vụ, điều kiện môi trường, cách Codex đưa kết quả về đúng repo A qua gateway D12 nếu là một việc ghi đã được Host/Owner cho phép, và cách Dot tự đối chiếu commit. Không dùng native GitHub push trái quy trình đang áp dụng. Nếu môi trường hãng hoặc quyền máy chưa bật, ghi CLIENT_ONLY_PENDING và đúng thao tác Owner cần làm sau, không tự xây dịch vụ thay thế.

## S3 — Không đuổi lỗi cũ làm blocker giả

P415 TQT signed-read/no-change đã PASS baseline và candidate, fixture cũ invalid cả hai; candidate offline 328 PASS/3 FAIL/1 collection error, không có failure ID mới theo báo cáo Codex, nhưng KHÔNG gọi full-suite PASS. Native canary không sửa mã nên không chạy lại bộ TQT/suite dài để cầu xanh.

P415 Guard POST 24/25 FAIL do #11 heartbeat, footprint 0; không đổi chữ thành PASS. DROOT59: ghi trạng thái và chủ giám sát, nếu có bằng chứng sự cố thật thì báo đúng luồng, không tự mở RUN HJW chạy theo đèn đỏ của việc khác. Không coi 37 tools Agent Data là đủ Directus/Graph/Lark; các họ ấy giữ status BLOCKED/CHƯA THỬ trong roadmap mà không ép giải quyết trước điều phối thử.

## S4 — Đóng canary đúng cấp

KQ bảng gọn: Dot read HJW; Dot write receipt; actor riêng/chung; Owner voice; Dot→Codex/Work task; kết quả Codex đúng repo A; Owner chỉ cần bấm gì. Ghi một trạng thái:
- COORDINATION_CANARY_PASS chỉ khi các chức năng điều phối đã thử từ Dot thật, KHÔNG gọi ghế độc lập.
- INDEPENDENT_SEAT_PASS chỉ khi có identity máy chủ riêng + receipt/quorum không trùng.
- CLIENT_ONLY_PENDING hoặc NOT_TESTED nếu chưa có quyền bề mặt/chưa thử.
Không sửa §1–§2, không thông báo N2 FULL_PASS khi Owner chưa chốt scope và nghiệm thu.

Bảo toàn candidate P415/source/image/rollback, +1 recreate UNUSED, Gmail đã có quyền đọc tự do/hỏi trước ghi, S4/root/GSM Owner 25/10 vẫn lưu yêu cầu lịch sử, không thu hồi. Trả mọi resource đã dùng, KQ XONG/DỪNG của riêng canary và một NEXT_TRIGGER.

STEP_WALK_V1: S0=Codex/Owner RUN/READY, HEAD/roster; S1=Dot thực hiện read/P/Voice và có receipt; S2=Dot→Codex native task + repo kết quả; S3=Codex disposition P415/DROOT59; S4=KQ, trả tài nguyên.
CẤM: tự sửa app/backend/credential hoặc mở MCP server/gateway mới; tự recreate Agent Data; dùng root/GSM trong canary; giả danh Dot bằng GPT/CLI; xem shared OpenAI identity thành hai phiếu; giữ VPS-GHI chờ Owner gọi thoại.
