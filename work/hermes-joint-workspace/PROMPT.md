# PROMPT — HJW CONTROL · Kiểm Hermes + nút duyệt Telegram

RUN_ID: HJW-CONTROL-20260926-01
STATUS: Chỉ thực thi khi Host ghi READY đúng commit cuối chạm PROMPT này và phát RUN trong COLLAB.
Host: GPT Chat · GPT-HJW-260922-A
Executor_Surface: Claude Code CLI phiên mới trên Mac Owner.
Report_Write_Path: gateway `workspace_*` root `workspace` hoặc `fs_*` root `gh`, repo Huyen1974/incomex-workspace, branch main.
Runtime_Write_Path: SSH/operator VPS hiện hữu; mã/runtime VPS là SSOT, không deploy mã từ GitHub.
Căn cứ: HJW §0.3 HJW-CONTROL S1–S7 + P37; Claude P38 tại 8f12e6cd5acf5f88198e404238b00dcfc1492049, B1–B6; MCPW N1–N7/P18–P19; Điều 30/31 + DROOT22.

## 0. Đích và ranh giới
Một luồng duy nhất: phát hiện việc → lọc không cần AI → chờ Owner bấm nếu MANUAL → claim/run → báo cáo/Telegram → Host đánh giá. Mặc định MANUAL; AUTO chỉ theo loại việc/phạm vi/phiên bản quy trình được Owner bật. Cài cả hai chế độ nhưng AUTO allowlist production ban đầu RỖNG. Không gọi mô hình để xin phép/nhắc lượt/đếm/kiểm trạng thái.

Lượt này: kiểm khả năng thật → ghép tối thiểu theo thiết kế đã duyệt → kiểm máy → gửi đúng một thẻ thử có ích → chờ Owner bấm → nghiệm thu. Không làm lại P02/HJW.3B. Không triển khai toàn bộ scoped lease/MCPW, không đổi model/tự cập nhật Hermes, không promote luật L1/L2 hoặc đóng toàn bộ HJW trong RUN này.

Auto-mode của Claude Code chỉ trong scope này. Không bypassPermissions, không tự mở rộng allowlist/quyền hoặc đổi cách gọi để lách chặn của nền tảng. Chặn thật ⇒ checkpoint và báo Host. Không bắt Owner gõ lại chi tiết kỹ thuật đã duyệt; lần bấm Cho chạy trên Telegram là phê duyệt RIÊNG cho lượt Hermes, không được thay bằng lệnh RUN cho Claude Code.

## 1. G0 — Audit chỉ đọc, rồi mới quyết định được triển khai
Đọc AGENTS → root COLLAB → HJW §0/P34–P38 → PROMPT → MCPW §0.3 N1–N7. Dùng cửa sổ nhỏ, không đọc lại toàn bộ lịch sử. Kiểm RUN/READY bằng gateway, source_head/freshness và content-version; nếu có thay đổi liên quan thì diff/reconcile. READY cũ HJW.3B không dùng cho lượt này.

Kiểm thực tế qua SSH, không suy từ tên tài liệu:
- Version/SHA Hermes, cấu hình đã che bí mật; vị trí thực của hjw_gate.py, ws-dispatch, cron/no_agent/pre-script, callback handler Telegram, ledger/metadata store, runner, STOP và safe-update/lock hiện hữu.
- Bot/Owner user_id/chat_id hiện hành; một consumer nhận Telegram updates. Không in token, header X-API-Key, env values, URL chứa secret; chỉ presence/hash khi an toàn.
- Điểm mở rộng/cấu hình nhận callback TRƯỚC model call; clarify/exec approval sau khi model đã chạy KHÔNG đáp ứng. Source có nhánh pre-script fail-open/im lặng thì phải chứng minh chốt cuối không wake khi lỗi; không chỉ thêm lời dặn.
- MỘT sổ bền hiện hữu có thể giữ cùng bản ghi từ pending approval tới kết quả. Ghi đúng path/schema/owner, primitive atomic update/claim, ai được sửa trường approval, cách MCPW dùng cùng ID. MCPW lifecycle còn thiếu phần nào phải nói rõ; không gọi thiết kế chưa cài là đã có.
- Baseline: hai MCP gateway/P02, Hermes 7 tool + scope/auth/attribution, Telegram thông thường, webhook, cron/STOP, Kuma, config-guard, image/source/StartedAt và tài nguyên. Tái dùng evidence/Guard có sẵn, so tập mã test lỗi cũ/mới, không chỉ số đếm. Bài health có model call phải tách: chưa duyệt thì chỉ chạy phần 0-token, ghi phần chưa chạy.

Ghi G0 ngắn vào HJW COLLAB và hồ sơ hiện hữu /opt/incomex/work/hermes-joint-workspace/: bảng năng lực `ĐÃ KIỂM / CHỈ CÓ TRONG DOC / CHƯA CÓ`, path+hash, sơ đồ callback→gate→ledger→runner, danh sách file/unit thực sự cần sửa và rollback.

G0 PASS mới được sửa, khi đồng thời: dùng extension/config/script hiện hữu; một ledger; một Telegram consumer; gate trước LLM có thể enforce trên mọi ingress của workspace automation; có backup/rollback tương thích; không vượt scope dưới đây. Nếu thiếu: DỪNG trước runtime mutation, báo đúng blocker + delta nhỏ nhất. Không ép triển khai bằng cách vá lõi, dựng kho pending/bot/service mới hoặc mở rộng quyền.

## 2. Phạm vi thay đổi
Được sửa cấu hình/script tích hợp/test HIỆN HỮU của HJW tại các path G0 xác nhận; mở rộng metadata bằng giao diện sẵn có của sổ hiện hữu. Trong repo chỉ sửa HJW COLLAB và nội dung view.html hiện hữu (không thêm tab/bố cục); PROMPT không do executor sửa. Báo cáo nhạy cảm/checkpoint/backup nằm trong hồ sơ VPS của HJW, không là nguồn trạng thái thứ hai.

Cấm sửa lõi/upstream Hermes trong RUN này. Nếu extension không đủ và phải vá lõi: báo patch tối thiểu + cách áp lại/kiểm sau update cho Host review riêng, chưa apply. Cấm DB/pipeline/daemon/service/bot/poller/token/route công khai mới; cấm file/task/project repo mới; không sửa Agent Data/fs_* core, P02, nginx hoặc quyền SSH/root. Không rotate key; không đọc/in secret. Không cấp thêm tool hoặc scope Hermes ngoài HJW.

Không đổi global Telegram conversation/approval hiện hữu. Prefix callback riêng cho HJW, không chiếm callback của clarify/exec approval. Không tắt Kuma/nhắc việc tất định hoặc toàn Hermes. Khi cần chặn chuyển tiếp trong deploy, chỉ dùng STOP-DISPATCH hiện hữu cho workspace automation; lưu trạng thái trước và chỉ resume khi gate mới PASS. Nếu rollback, giữ workspace dispatch fail-closed, không tự khôi phục auto-wake cũ bỏ qua duyệt.

## 3. B1 — Một bản ghi vòng đời, không thêm kho duyệt
Git giữ assignment/nội dung/phạm vi và kết quả; sổ hiện hữu giữ sự kiện runtime/approval. Cùng assignment_id và execution_id xuyên suốt, một nơi quyết định trạng thái; view/điểm số chỉ dẫn xuất.

Luồng chuẩn: PENDING_APPROVAL → APPROVED → CLAIMED → DONE hoặc BLOCKED; hết hạn → EXPIRED; từ chối lưu quyết định DENIED tương đương trong cùng sổ, không tự phát lại cùng generation. Giữ tên trạng thái chuẩn của sổ nếu đã có và ghi mapping, không tạo state machine song song.

Vé gắn hash NỘI DUNG CÔNG VIỆC + scope + role + READY khi cần + generation + expiry. Không hash cả COLLAB hoặc toàn HEAD vì commit claim/báo cáo/task khác sẽ gây duyệt lại giả. Thay nội dung/phạm vi thực thì vô hiệu vé cũ. Không dùng marker trong repo do LLM ghi để giả Owner approval.

Claim/consume vé phải atomic, ràng buộc identity/execution; hai trigger/click chỉ một model invocation. Ghi START trước tác dụng phụ; crash/outcome unknown không retry mù. Khi đang chờ không có model turn/process LLM/lease ghi giữ lâu. Chưa có enforcement scoped lease toàn MCPW thì ghi giới hạn, chỉ dùng exclusion/version/scope hiện hữu đã chứng minh cho lượt HJW này, không tuyên bố đã giải quyết toàn MCPW.

## 4. S1–S3, B2/B4 — Nút, công tắc và chống ngập
Nút `Cho chạy`, `Không chạy`, `Xem việc`; thẻ ghi tên task, câu hỏi, đầu ra, đọc/ghi, lý do cần Hermes, thời hạn. callback_data chỉ chứa mã vé ngẫu nhiên ngắn + action, tổng UTF-8 ≤64 byte; chi tiết tra sổ. Verify callback.from.id + chat/message binding với Owner cấu hình, không dựa username/text. Trả lời callback nhanh bằng handler tất định; click không đưa vào LLM.

Kiểm lại trước claim/model: vé chưa dùng/chưa hết hạn, người hợp lệ, assignment/hash/generation/role/scope/READY còn đúng, mode và STOP. Nút cũ/giả/bấm lặp/sai người đều không chạy. Pending qua restart vẫn còn nhưng phải revalidate; không tự approve khi khởi động lại. API/cron/webhook/direct-dispatch của WORKSPACE AUTOMATION cùng gate; không nhầm với chat thủ công Owner đang dùng.

Công tắc MANUAL/AUTO theo loại việc dùng cùng callback/ledger; chỉ Owner được bật AUTO, phạm vi+phiên bản phải khớp, STOP luôn thắng. Kết thúc RUN giữ MANUAL và auto_allowlist rỗng; test nhánh AUTO bằng fixture, không tự bật thật.

Mặc định vận hành do Host chốt cho giai đoạn đầu: TTL vé 24 giờ; tối đa 10 THẺ DUYỆT MỚI/ngày theo giờ Việt Nam; cùng loại cập nhật/gom một tin, nhưng mỗi việc vẫn có vé riêng, không gom thành duyệt hàng loạt ẩn. Hết hạn/từ chối không tự tái gửi; backlog được thấy trong tin tổng hợp, không bị xoá. Giới hạn này chỉ cho thẻ duyệt, không chặn báo sự cố/START/kết quả. Cấu hình lại được qua cơ chế hiện hữu; không thêm cap chi phí vì D10 ngoài scope.

## 5. S4/S5, B5 — Telegram và phiếu điểm
Ba mốc tất định, không dựa AI nhớ tự báo:
1. CHỜ DUYỆT: thẻ và nút, không LLM.
2. ĐÃ NHẬN/BẮT ĐẦU: mục tiêu + scope + link task; phải có Telegram API receipt trước model. Gửi lỗi/unknown thì giữ chờ, không wake âm thầm.
3. KẾT QUẢ hoặc BLOCKED: đã làm gì, phát hiện mới/không mới, phần thiếu, commit/báo cáo, thời lượng, usage/cost provider nếu có, ai tiếp theo. Không báo DONE nếu báo cáo chưa được push/xác nhận. Duy trì ba dòng STATUS / COMMIT / NEXT hiện hữu, đưa tóm tắt có ích vào STATUS/NEXT; phần chi tiết ở task, không spam từng tool.

Lưu message_id, send status, timestamps và result cùng record. Receipt là API nhận gửi, không chứng minh Owner đã đọc. Nếu kết quả đã có mà Telegram lỗi: chỉ retry gửi có giới hạn/chống trùng, không chạy lại LLM/tác dụng phụ. Timeout gửi không chứng minh không gửi: xử lý như delivery unknown, không hứa exactly-once notification tuyệt đối.

Phiếu điểm dẫn xuất theo LOẠI VIỆC: số lượt, số đã Host đánh giá, tỷ lệ ACCEPT (nêu mẫu số), số/tỷ lệ có phát hiện mới được Host xác nhận, chi phí thật trung vị (kèm số mẫu thiếu), thời gian chờ duyệt. Hermes tự chấm không thay Host; thiếu cost thì ghi chưa xác nhận, không tính 0. Chỉ dùng provider usage/ledger đã có, không cấp management key mới.

Ngưỡng GỢI Ý để Host đề xuất Owner bật AUTO: ≥5 lượt đã đánh giá, ≥80% ACCEPT, 0 sự cố an toàn; không phải điều kiện máy tự bật. Có ít mẫu thì hiển thị đúng, không chạy đủ 5 lần chỉ để đủ điểm.

## 6. Triển khai và bảo vệ Điều 30/31
PRE PASS + baseline/backup/rollback trước mỗi mutation/runtime restart. Mã thử trong fixture/cách ly; không cấy pending/circuit giả, kill hay fault-inject production.

Cố gắng hot-config/extension đang hỗ trợ. Nếu cần restart, chỉ đúng Hermes gateway/unit tích hợp G0 đã khai; không restart serve/nginx/MCP vì tiện. Tránh safe-update đồng thời. Chờ lượt thật đang chạy xong, không cắt ngang; khối chuyển đổi/health/rollback chạy phía VPS bằng runner hiện hữu, không phụ thuộc Mac/SSH. Health STARTING tối đa 5 phút theo DROOT10; POST semantic + config-guard, rollback delta nếu fail. Không giữ lock mà health/runner cần để khởi động, không mở ghi chỉ vì process giữ lock đã chết.

Rollback không xóa ledger/approval/kết quả, không làm vé đã dùng sống lại; schema/metadata phải backward-compatible với bản quay về. Nếu không chứng minh được rollback an toàn, dừng trước deploy. Tái dùng giám sát để cảnh báo mất callback/runner/gửi tin; không heartbeat bằng LLM hoặc commit. Ngoài scope: source/config/image/StartedAt không đổi; metrics CPU/RAM/disk và tốc độ read P02 trước/sau được ghi, không benchmark/tối ưu thêm P02.

Checkpoint sau G0, PRE, TEST, DEPLOY, POST, WAIT_OWNER_CLICK, TRIAL, FINAL trong hồ sơ HJW hiện hữu; không ghi từng tool. Tất cả service phải ổn trước khi chờ click, không giữ terminal/SSH/root lock để chờ Owner. Ngắt phiên thì phiên mới đọc checkpoint, không chạy lại phần đã xong.

## 7. Nghiệm thu C1–C10 — trước và sau click phải tách rõ
C1. G0 chứng minh extension/config, một sổ, một Telegram consumer; chưa đủ thì NO-GO đúng, không dựng thay.
C2. Idle/không cần AI/pending/denied/expired = 0 model call. Pre-script lỗi/im lặng/malformed/network/STOP unreadable vẫn không bypass; test ở cách ly.
C3. Đúng Owner/còn hạn/đúng hash click một lần ⇒ một claim/run. Sai người, replay, hai click đồng thời, changed scope/READY, generation cũ ⇒ không chạy. Commit không liên quan không làm vé vô hiệu.
C4. Cron/webhook/direct workspace dispatch cùng gate; callback cũng không tự bypass. STOP và MANUAL/AUTO theo loại việc hoạt động; production cuối cùng vẫn MANUAL.
C5. Restart/crash tại pending, approved, claimed, result-committed giữ trạng thái/chống chạy đôi. UNKNOWN không auto retry; mất Telegram sau result chỉ retry notification.
C6. Ba mốc Telegram đúng task/assignment/execution, receipt và report/commit thật; completion không tự đánh PASS. Không soi secret/không đưa input webhook tự do vào prompt.
C7. TTL/cap/gom thẻ/backlog/denied không spam; scorecard đúng mẫu số, thiếu cost không tính 0, không auto-promote.
C8. Phiên/scope/identity và dấu bắt đầu/kết thúc có audit; không có ledger thứ hai; view dùng nguồn dẫn xuất có revision, không đổi layout. Không đồng nhất Git commit bất kỳ với hoàn thành task.
C9. Regression các khả năng đã chạy: MCP/P02, 7 tool Hermes, auth/scope/attribution, Telegram chat/clarify/exec approval, webhook/STOP/monitor, file/unit ngoài scope. So tập mã test; negative controls phải FAIL trong fixture. Không cần gọi LLM production để đếm tool.
C10. Một lượt Hermes thật sau Owner click, đầu ra mới có ích hoặc trung thực NO_NEW_VALUE, report/commit/Telegram/usage evidence; Host đánh giá riêng. Trước click C10 = CHỜ OWNER, không 10/10 PASS giả.

## 8. B6 — Một lượt thử thật, không giao tóm tắt cũ
Sau C1–C9 PASS, Host uỷ quyền executor materialize ĐÚNG MỘT đề nghị thử `HJW-CONTROL-TRIAL-20260926-01` vào HJW, qua gate mới ở PENDING_APPROVAL. Không ghi ASSIGN open khi gate cũ còn có thể wake. Đây là đề nghị chờ bấm, không phải quyền chạy mô hình ngay.

Câu hỏi thử: “Từ sơ đồ trạng thái/callback/dispatch và kết quả thử đã che bí mật vừa triển khai, tìm tối đa một chuỗi sự kiện cạnh tranh hoặc mất kết nối CHƯA được bộ ca hiện tại bao phủ, có thể gây chạy hai lần hoặc chạy sau khi bị từ chối. Chỉ ra evidence/điều kiện tái hiện và cách bổ sung kiểm nhỏ nhất; không sửa gì. Không tìm được thì trả NO_NEW_VALUE, không bịa lỗi.”

Trước gửi thẻ: kiểm trong repo câu hỏi/chính đáp án chưa được kết luận; input tối thiểu đã có trong HJW COLLAB/G0 và Hermes đọc được bằng 7 tool. Không gửi raw source/secret hoặc mở thêm quyền chỉ để thử. Nếu không có câu hỏi mới hợp lệ hoặc đầu vào chưa đủ, ghi TRIAL_NOT_READY cho Host, không đốt token làm tóm tắt thay thế.

Hermes chỉ đọc/phân tích, được ghi duy nhất P báo cáo + chuyển assignment trong HJW bằng gateway; không mutation runtime, không tạo file, không tự giao lượt sau. Chỉ Owner click thật mới chạy; Claude Code không click hộ, không giả callback Owner production. Sau khi gửi thẻ: ghi WAIT_OWNER_CLICK + message_id, trả “Đã lắp, đang chờ bấm” và kết thúc lượt CLI bình thường. Cơ chế VPS phải sẵn sàng nhận click sau đó mà không cần Owner gõ tiếp. Hết hạn/Không chạy thì không tạo trial mới tự động.

## 9. KQ và bàn giao
Ghi vào CHÍNH HJW COLLAB: G0 paths/SHA/bảng năng lực; runtime/config delta; ledger dùng chung; C1–C10 với artifact; PRE/POST và rollback; message_id/status; MANUAL/allowlist rỗng; model_calls trước click; scorecard; phần thiếu. Cập nhật nội dung view.html hiện hữu đúng trạng thái và kiểm bản xuất bản, không trang/URL khác. KQ chỉ qua gateway, không git push thẳng.

Khi chờ click: checkpoint WAIT_OWNER_CLICK, dòng Owner cần quyết chỉ ghi bấm nút đang có; KHÔNG KQ XONG. Khi bị chặn thật: `KQ@HJW-CONTROL-20260926-01 DỪNG` + nguyên nhân/scope đã đổi/rollback. Chỉ sau C1–C10 đạt và evidence đủ mới ghi `KQ@HJW-CONTROL-20260926-01 XONG`; Host/Reviewer nghiệm thu riêng. Nếu CLI đã dừng ở checkpoint, lượt kiểm tiếp chỉ đọc ledger/commit/receipt rồi hoàn thiện KQ, không chạy lại trial.

HJW.4 L1/L2, HJW.5 T1–T10 và scope/lifecycle toàn MCPW chuyển vòng sau; không gộp đổi luật hoặc dọn fixture. P02 giữ nguyên. PROMPT HJW.3B cũ ở lịch sử Git (9b62bf46…), không tái thực thi.

## Tham chiếu ngoài — chỉ xác minh khả năng, không thay audit bản đang chạy
- Telegram Bot API InlineKeyboardButton/CallbackQuery: https://core.telegram.org/bots/api (callback_data 1–64 byte).
- Hermes Telegram: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram/ (clarify/exec approval không tự chứng minh gate trước LLM).
