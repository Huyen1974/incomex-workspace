# PROMPT — VPSC2-R2-LEAN-OPS-20261020-01

DRAFT — KHÔNG CHẠY khi chưa có Claude Chat Reviewer ACCEPT + GPT Host READY đúng full SHA last-touch của PROMPT.md trong COLLAB.md, Owner mới là người dán giao Claude Code CLI.
Executor_Surface: Claude Code CLI (Mac Owner).
Write_Path: Git workspace thông qua Incomex workspace_* gateway; VPS1 bằng đường quản lý được duyệt, `incomex-config-apply-v0` (cron/script/systemd), DOT wrapper approved (Directus flow). Không đi vòng ruleset GitHub/ConfigGuard.
RUN_ID: VPSC2-R2-LEAN-OPS-20261020-01.
SSOT: AGENTS.md → work/vps-clean-20-10-26/COLLAB.md §0, Bảng, P03–P05 → PROMPT.md → R1 tại work/done-tasks/vps-clean-20-9-26/BAO-CAO.md §PROOT11-R1. Không chạy R1b, không ghi trạng thái mới vào root PROOT11.

ĐÍCH: dọn lịch cũ và giảm chi phí canh; ưu tiên sự kiện/lỗi đẩy vào Kuma/Telegram hiện hữu. Theo Owner B3, presence nền mục tiêu 10 phút + cập nhật tức thời khi có sự kiện hoặc bấm Refresh; quét cấu hình đầy đủ mục tiêu 20 phút (tối đa30 phút nếu đủ bằng chứng) + phát cảnh báo lỗi/tamper bằng cơ chế hiện có. Những mục này KHÔNG đồng nghĩa hạ chuẩn Đ30/31 hoặc bỏ cơ chế bắt lỗi khi không ai dùng giao diện. Nếu không chứng minh được, giữ nhịp hiện hành và SKIP mục đó. Không sửa cứng ngưỡng để tô xanh.

S0 — Cổng bắt buộc: kiểm AGENTS/COUNCIL, lời Owner B3, ACCEPT/READY cùng last-touch full SHA, không STOP/STARTED trùng; đọc hiện trạng VPS-GHI CAS + RUN GS-CLEAN/HJW khác. Nếu VPS-GHI bận => KQ DỪNG sạch, không ngồi chờ. Nếu PASS, chiếm VPS-GHI rồi ghi STARTED + Bảng trong cùng commit. PRE chụp 22 Kuma theo ID/status/reason, Guard/Config Guard/backup/rollback, các unit/flow/lịch và nguồn chi phí 24h sẵn có. Runtime mutation chỉ sau read-gate và kiểm freshness lại.

S1 — Sáu hạng mục tách độc lập, từng mục đều phải có PRE current + consumer + baseline + một phép lùi tương đương. Mục không chứng minh an toàn => SKIP đúng mục; đừng vì mục tiêu 6/6 mà OFF nhầm.

R2-1: xác minh `/etc/cron.hourly/free` thực sự chạy `drop_caches`, không có caller/consumer cần hành vi này. Chỉ ngừng chạy bởi cron.hourly qua apply-v0 và bảo vệ đúng target ConfigGuard (đăng ký target trong lớp hiện hữu theo luật nếu cần), KHÔNG xoá script/dữ liệu. Kiểm `run-parts --test` và lịch khác không đổi. Không khẳng định đã chữa tận gốc Nuxt.

R2-2: xác minh hourly `/etc/cron.hourly/fstrim` trùng tuần; `fstrim.timer` ACTIVE, last SUCCESS và đúng filesystem. Nếu PASS mới ngừng chạy script hourly qua apply-v0, không xoá tệp/không chạy `fstrim` tay; weekly timer giữ. Không đủ proof weekly => SKIP.

R2-3: xác minh đúng 3 legacy cron (`watchdog-monitor.sh` /1h, `cron-integrity.sh` /6h, `scanner-counts.sh` /3h) độc lập với Guard/SR-MOW/backup đang dùng, không có reader còn cần. Chỉ comment đúng các dòng hết nhiệm vụ bằng apply-v0 target `cron-root-crontab`; giữ script/đường hồi phục, không chạm cron khác; nếu một dòng còn làm bảo vệ thì SKIP riêng nó. Test Config Guard/Điều30/31.

R2-4 (OWNER B3 MỚI): `incomex-config-drift-check.timer` hiện 5 phút, Guard freshness drift ≤15 phút. Xem kiến trúc đã có event push khi ghi config/sửa trái phép, canh khi producer chết, và consumer dùng kết quả trong SLA. Nếu chứng minh được bằng negative test trên BẢN SAO + chứng cứ cảnh báo thật mà không giảm coverage Đ30/31, dùng apply-v0 giãn full scan tới 20 phút (30 chỉ nếu proof tương đương) và giữ cảnh báo lỗi/thay đổi tức thời. Nếu chỉ có thông báo khi sửa bằng đường hợp lệ hoặc phải nới Guard ≤15 phút/disable cảnh báo/thiết kế daemon mới thì SKIP, giữ 5 phút. Không thay thành 10 phút theo P04 vì Owner nói 20–30.

R2-5 (OWNER B3 MỚI): `mcpw-presence-import.timer` hiện 30 giây; consumer `LEDGER_MAX_AGE=180s`, `LIFECYCLE_MAX_AGE=600s` và INV12. Kiểm sự kiện state/claim/lifecycle của phiên thực và nút Refresh có ghi dữ liệu mới NGAY cả khi chưa đến timer, actor chết không bị im lặng; không giả event-driven bằng hiển thị stale. Chỉ đổi periodic nền sang 10 phút qua apply-v0 nếu hot-path bảo đảm freshness active <=180s, Guard/INV12 và negative case PASS. Không thay `incomex-hvu-presence` 15s hoặc contract claim ngoài scope. Chưa có proof => SKIP, giữ timer30s, báo NEEDS_DESIGN thay vì nới LEDGER_MAX_AGE; không thay thành90s theo P04.

R2-6: xác minh flow id + status đúng duy nhất `[DOT-REG] Count Refresh (6h)`, không có consumer/route/PG count thật cần output; lỗi PATCH bị Guard chặn, đã có restore status. Nếu PASS dùng DOT approved đổi ACTIVE→INACTIVE (không xoá flow, không tắt Watchdog/trigger khác), kiểm smoke Directus/PG/Agent Data/Guard; nếu còn dependency => SKIP.

S2 — POST/Đ30/31: sau mỗi APPLIED kiểm diff đúng allowlist + Config Guard C3 MATCH, functionality/smoke; negative test trên bản sao, canh báo lỗi thật, rollback từng mục khi tạo đỏ mới. Cuối RUN 22 Kuma theo ID/status/reason so PRE; không tô xanh global nếu đã có lỗi cũ; không gửi Telegram test spam, biên nhận chỉ khi có thật. Đổi script/cron/status phải có beforeimage và đường đảo tương đương. Không purge/retention, restart container/swapoff, đổi RAM hay sửa app khác. 0 tiến trình nền/tệp tạm còn lại, trả VPS-GHI cùng KQ.

S3 — KQ chỉ ghi vào task này + cập nhật Bảng cùng commit, một bảng 6 hàng: APPLIED/SKIP + lý do + thay đổi/chi phí trước/sau có đo (không lấy toàn CPU job làm số tiết kiệm) + trễ phát hiện tối đa + chủ bảo vệ + rollback + trạng thái Guard/Kuma. Không giữ CLI/terminal chờ 20 phút/24h; journal/Kuma/08:00 sẵn có quan sát số sau, chưa đủ ghi CHƯA ĐO. Mục ngoài phạm vi trỏ Host đúng việc.

BÁO OWNER MỘT DÒNG: XONG/DỪNG · VPSC2-R2 · APPLIED=[...] SKIP=[mã:lý do] · Guard ... · 22 Kuma ... · VPS-GHI trả · commit.
