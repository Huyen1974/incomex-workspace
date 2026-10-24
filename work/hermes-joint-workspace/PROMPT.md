# HJW · Một lần sửa cơ chế, những lần nâng sau chỉ bấm
RUN_ID: HJW-HERMES-SIMPLE-20261024-01
STATUS: P382_HOST_DRAFT — chỉ thực thi khi có READY@full-SHA last-touch PROMPT và Owner chuyển cho Claude Code.
Host: GPT Chat · Reviewer: Claude Chat P381 ACCEPT hướng hợp nhất có 6 sửa (d05480ee0ede1db48f31b39c81ac7cd742db1066).
Executor_Surface: Claude Code CLI (Owner dán tay).
Write_Path: Incomex MCP workspace_* cho SSOT; runtime VPS qua quyền quản trị/apply-v0 được duyệt và VPS-GHI; thao tác BotFather bởi Owner; Mac chỉ theo cơ chế cập nhật app của hãng. Không dùng READY P370 của Codex; P380 đã KQ DỪNG.

**Mục tiêu:** giải quyết một lần ba việc trong thứ tự: (A) credential legacy, (B) hai cổng sudo/GSM + quyền ghi, (C) cập nhật Hermes đơn giản. Hermes **chạy chính trên VPS**, Desktop Mac chủ yếu là màn hình. Không tạo plugin/Guard/daemon/launchd/SSH-key mới; không tự nâng phiên bản trong RUN này nếu Owner chưa giao rõ bản stable.

## S0 — Read-gate, một lần PRE
Đọc AGENTS, root/HJW COLLAB mục tiêu và roadmap N1–N6, P364/P367/P370/P377/P378/P380/P381, PROMPT này; soát roster, READY, STOP, active RUN/VPS-GHI, Guard và hiện trạng; backup *những file cấu hình thực sự sửa* + đường lùi từng phần. P380 đã đo: script legacy mode 0755 chứa chuỗi giống token, updater chạy root không cần sáu sudo grant, quyền Google Hermes hiện không có grant đã thấy. Dùng bằng chứng đó, chỉ kiểm freshness/metadata; **cấm đọc/in lại mã secret hoặc raw env**. Guard/đường apply từ chối thì KQ DỪNG, không tìm cách lách.

## A — Xử lý token Telegram trước
Định vị bot và những consumer thực tế **qua tên đường/cấu hình và quyền file, không lấy giá trị token**; bảo toàn kênh thông báo đang dùng. Chuẩn bị đường đọc token root-only bằng kho secret/loader **đã có**, chương trình đọc khóa không còn literal, thử fixture giả (không ghi bí mật thật); bảo đảm script chạy bằng đúng user, mode và ACL phù hợp.
**Checkpoint Owner:** BotFather `/revoke` thay token và vô hiệu hóa token cũ *ngay lúc cấp token mới*. Vì vậy không viết kế hoạch “tạo mới → thử → thu hồi cũ”. Chỉ khi đường nhận kín đã sẵn sàng, hướng dẫn Owner thao tác BotFather; nhập token mới **trực tiếp vào cơ chế root-only**, không qua chat, prompt, command argv, Git hay log. Kích hoạt cấu hình, thử một cảnh báo thật (không log credential), kiểm các consumer, giữ bản chứng cứ đã che; xác nhận credential cũ không còn trong mã chạy, siết script thành root:root 0750 hoặc quyền hẹp tương đương. Không xóa/sửa lịch sử sự cố P380. Chưa có Owner/token an toàn thì báo BLOCKED, trả VPS-GHI, không giả PASS hoặc chuyển bừa qua phần sau.

## B — Cấm sudo/GSM, trả quyền ghi hợp lệ
P380 đã đối chiếu mã updater và phần nhật ký còn lưu từ 14/10, nên **không mở khảo sát sudo 30 ngày từ đầu**. Kiểm đúng caller/grant sát khi áp, thu hồi một grant `HERMES_UPDATE_UNITS` cho user hermes bằng đường quản trị đã có; kiểm sudo policy và root-owned updater vẫn hoạt động, không cấp root proxy. IAM không có grant Hermes cần gỡ thì không sửa IAM. Kiểm UID không đọc Google/root/backend credential; gcloud/ADC rỗng; unit/env không chỉ đến Google credential; UID không thuộc docker/socket. Gắn bốn nhóm boolean vào canh cấu hình đang chạy, không xuất secret.
Mở write_scope Hermes từ đúng 5 file thành **chỉ `work/*/COLLAB.md`** (loại trừ done-tasks), sửa INV19 với guard hậu ảnh giữ nguyên; giữ cron không người trực chỉ đọc. Thử lại 33 ca âm + cross-task và một ghi chú hợp lệ bằng danh tính Hermes thật; cấm giả Host/READY/KQ/ASSIGN/RESULT. Mỗi thay đổi có rollback độc lập, không sửa Guard để tô xanh.

## C — Nâng cấp Hermes theo bản nhỏ
**Không gỡ managed scope của VPS.** Desktop Mac không được tự nâng backend VPS hoặc gateway khác; chỉ dùng hành động *cập nhật Desktop riêng* của hãng sau khi xác nhận đúng phạm vi. VPS dùng `hermes-safe-update` root-owned đã có. Timer stable hiện tại phát hiện bản mới; chỉ nối vào cơ chế thẻ Telegram/“Cho chạy” đã có: Owner bấm Nâng/Để sau → root chạy đúng version stable đã xác minh qua menu cố định (chỉ bổ sung tối thiểu nếu thiếu); không cho Hermes generic root exec. Nếu không thể bảo đảm nút an toàn, giữ lệnh nâng root hiện có và báo blocker, không mở remote self-update.
Vá cùng số giữa: dùng **snapshot nhanh + rollback của hãng/root updater**, không chụp toàn cây 6,2 GB, không Drive, không dùng full fixture #21 chỉ vì hãng đổi version. Kiểm tối thiểu kết quả update, health, quyền cấm root/GSM và một lượt chat/công cụ; giữ Guard thường trực/cảnh báo drift. Sửa xử lý active_agents thật sự bận và counter kẹt: chỉ nâng lúc không có phiên hoạt động, chờ có hạn; không giết lượt model, không auto-restart tùy tiện. Dùng mutex/VPS-GHI **do máy tự nhận/trả** để tránh tranh chấp production, không bỏ khóa bảo vệ.
Thay điều kiện cứng Mac=VPS cùng commit bằng kiểm **tương thích chức năng**, sau khi thử đúng cơ chế Guard/INV14: remote connected, status hai version, chat thật, gọi công cụ. Đừng hạ Guard hay sửa proof cũ để che FAIL; thay tiêu chí chỉ trong phạm vi đã nghiệm thu. **KQ nâng VPS không phải chờ Mac**; app Mac cập nhật khi Owner rảnh. Đổi số giữa lớn/migration: dùng bảo vệ bổ sung theo rủi ro có chứng cứ, không áp máy móc quy trình 3 giờ. Chưa bật auto-update vào giờ vắng trong lượt này.

## S4 — KQ một lượt
Thử thẻ bấm bằng dry-run/sandbox xác thực đúng Owner, idempotency, chỉ tác động bản stable/đích VPS; nếu chưa có bản mới được duyệt thì không nâng thật, ghi PILOT/CHƯA THỬ phần live. Kiểm lại token đã thay + cảnh báo thật; zero sudo grant; 4 nhóm GSM canh; COLLAB được ghi đúng vai, âm chặn; health Hermes VPS; nút Desktop chỉ cập nhật Mac; Điều 30/31, Config Guard/Protection Guard và rollback cho **phần code/config thay đổi**, không quét fixture cũ mỗi bản vá về sau.
Dọn ba báo cáo rời chỉ nếu đã giữ chứng cứ và liên kết trong COLLAB/Owner View; bảng PG chưa duyệt phải bảo tồn, không xóa audit hoặc xem dọn file là điều kiện PASS. N2 Dot/N4–N6, Graph/PG/Directus khác scope giữ nguyên. Ghi một STARTED và một KQ XONG/DỪNG có kết quả A/B/C riêng, commit/đọc kiểm, trả VPS-GHI, dọn fixture tạm, báo Owner ngắn.

STEP_WALK (một RUN; lỗi báo Host/Owner ngay, không giữ VPS-GHI chờ Owner):
| Bước | Actor / trigger | SLA / checkpoint | Evidence / fail-next |
|---|---|---|---|
| S0 | Claude Code · Owner dán READY | ngay trước mutation | freshness, PRE, quyền/lease; sai → DỪNG |
| A | Claude Code + Owner BotFather | chuẩn bị an toàn trước khi Owner đổi | secret path root-only + cảnh báo thật; Owner chưa sẵn → checkpoint/trả khóa |
| B | Claude Code · A đạt | sau A, không lặp khảo sát cũ | sudo=0, IAM/ACL, Guard/33 âm; lỗi → rollback B |
| C | Claude Code · B đạt | sau B, không cần đợi phiên hãng mới | nút pilot/đường tự nâng + quick rollback/compatibility; lỗi → lùi C |
| S4 | Claude Code · các pha xong/dừng | ngay cuối lượt | POST, KQ A/B/C, nhả cờ |
