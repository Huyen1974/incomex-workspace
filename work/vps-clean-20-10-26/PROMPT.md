# PROMPT — VPSC2-R2-LEAN-OPS-20261020-01

DRAFT — KHÔNG CHẠY khi chưa có Claude Chat Reviewer ACCEPT + GPT Host READY đúng full SHA last-touch của PROMPT.md trong COLLAB.md, Owner mới là người dán giao Claude Code CLI.
Executor_Surface: Claude Code CLI (Mac Owner).
Write_Path: Git workspace thông qua Incomex workspace_* gateway; VPS1 bằng đường quản lý được duyệt, `incomex-config-apply-v0` (cron/script/systemd), DOT wrapper approved (Directus flow). Không đi vòng ruleset GitHub/ConfigGuard.
RUN_ID: VPSC2-R2-LEAN-OPS-20261020-01.
SSOT: AGENTS.md → work/vps-clean-20-10-26/COLLAB.md §0, Bảng, P03–P05 → PROMPT.md → R1 tại work/done-tasks/vps-clean-20-9-26/BAO-CAO.md §PROOT11-R1. Không chạy R1b, không ghi trạng thái mới vào root PROOT11.

ĐÍCH: dọn lịch cũ và giảm chi phí canh; ưu tiên sự kiện/lỗi đẩy vào Kuma/Telegram hiện hữu. Theo Owner B3, presence nền 10 phút (sự kiện hook Claude Code/Codex đã ghi tức thời sẵn; nút Cập nhật chỉ tải lại số mới nhất, Owner chấp nhận trễ ≤ 10′); quét cấu hình đầy đủ mục tiêu 20 phút (tối đa30 phút nếu đủ bằng chứng) + phát cảnh báo lỗi/tamper bằng cơ chế hiện có. Những mục này KHÔNG đồng nghĩa hạ chuẩn Đ30/31 hoặc bỏ cơ chế bắt lỗi khi không ai dùng giao diện. Nếu không chứng minh được, giữ nhịp hiện hành và SKIP mục đó. Ngưỡng tuổi/cửa sổ là tham số của nhịp: đổi theo nhịp Owner đã chốt trong cùng mục, bắt buộc kèm phép thử âm trên bản sao; cấm đổi ngưỡng mà không có phép thử (đó mới là tô xanh).

S0 — Cổng bắt buộc: kiểm AGENTS/COUNCIL, lời Owner B3, ACCEPT/READY cùng last-touch full SHA, không STOP/STARTED trùng; đọc hiện trạng VPS-GHI CAS + RUN GS-CLEAN/HJW khác. Nếu VPS-GHI bận => KQ DỪNG sạch, không ngồi chờ. Nếu PASS, chiếm VPS-GHI rồi ghi STARTED + Bảng trong cùng commit. PRE chụp 22 Kuma theo ID/status/reason, Guard/Config Guard/backup/rollback, các unit/flow/lịch và nguồn chi phí 24h sẵn có. Runtime mutation chỉ sau read-gate và kiểm freshness lại.

S1 — Sáu hạng mục tách độc lập, từng mục đều phải có PRE current + consumer + baseline + một phép lùi tương đương. Mục không chứng minh an toàn => SKIP đúng mục; đừng vì mục tiêu 6/6 mà OFF nhầm. Thứ tự chạy: R2-1 → R2-2 → R2-3 → R2-6 (độc lập, không chạm Guard) → R2-4 → R2-5 (có sửa Guard); mỗi mục lùi độc lập, mục sau hỏng không kéo lùi mục trước đã PASS.

R2-1: xác minh `/etc/cron.hourly/free` thực sự chạy `drop_caches`, không có caller/consumer cần hành vi này. Chỉ ngừng chạy bởi cron.hourly qua apply-v0 và bảo vệ đúng target ConfigGuard (đăng ký target trong lớp hiện hữu theo luật nếu cần), KHÔNG xoá script/dữ liệu. Kiểm `run-parts --test` và lịch khác không đổi. Không khẳng định đã chữa tận gốc Nuxt.

R2-2: xác minh hourly `/etc/cron.hourly/fstrim` trùng tuần; `fstrim.timer` ACTIVE, last SUCCESS và đúng filesystem. Nếu PASS mới ngừng chạy script hourly qua apply-v0, không xoá tệp/không chạy `fstrim` tay; weekly timer giữ. Không đủ proof weekly => SKIP.

R2-3: xác minh đúng 3 legacy cron (`watchdog-monitor.sh` /1h, `cron-integrity.sh` /6h, `scanner-counts.sh` /3h) độc lập với Guard/SR-MOW/backup đang dùng, không có reader còn cần. Chỉ comment đúng các dòng hết nhiệm vụ bằng apply-v0 target `cron-root-crontab`; giữ script/đường hồi phục, không chạm cron khác; nếu một dòng còn làm bảo vệ thì SKIP riêng nó. Test Config Guard/Điều30/31.

R2-4 (OWNER B3: kiểm cấu hình 20–30′ · sửa bởi Claude P06): đổi `incomex-config-drift-check.timer` 5′ → 20′ VÀ cùng mục đổi ngưỡng theo nhịp: Guard `mcpw-protection-guard` cả 2 chỗ `--since '-15min'` (đọc mã 20/10: dòng ~680 và ~1725) → `-45min` (= 2 × nhịp + 5′); mô tả B18 «(5′)» → «(20′)»; mọi sổ ghi nhịp cũ của phép kiểm này (sổ TIN_BAO nếu có) sửa theo. Qua apply-v0 + code-ledger/Config Guard baseline mới + Guard SELFTEST PASS. Cổng bắt buộc, phép thử âm trên BẢN SAO: (a) sửa lệch 1 đích ⇒ STATUS=DRIFT ⇒ Guard đỏ; (b) không có lượt drift-check trong 45′ ⇒ Guard đỏ «no run»; (c) bản nguyên ⇒ xanh. «Đẩy lỗi khi hỏng»: dùng đường đã có (STATUS → Guard 5′ → Kuma #22 → Telegram, trễ tối đa ~25′); có sẵn OnFailure/push thì dùng, không có thì KHÔNG xây daemon/inotify mới. Một phép thử FAIL ⇒ lùi cả mục (timer + Guard) về bản cũ, SKIP, báo rõ phép thử nào. Không dùng 10′ của P04.

R2-5 (OWNER B3: cập nhật 10′ · sửa bởi Claude P06): đổi `mcpw-presence-import.timer` 30″ → 10′ VÀ cùng mục đổi ngưỡng theo nhịp: `docker/nuxt-repo/scripts/hvu-b2/presence.py` `LEDGER_MAX_AGE` 180 → 1500 s, Guard `LIFECYCLE_MAX_AGE` 600 → 1500 s, câu báo «export >180 s old» → «>1500 s»; chú thích «refreshed every 30 s» sửa theo. Qua apply-v0 + baseline mới + Guard SELFTEST PASS. Sự thật Reviewer đã đọc mã: sự kiện hook Claude Code/Codex đã ghi tức thời vào agent-data (`agent_data/lifecycle.py`), importer chỉ thêm sshd/claude-mcp/commit/Hermes và xuất snapshot; nút Cập nhật = `window.location.reload()` (README hvu-b2), không ép import — Owner chấp nhận trễ ≤ 10′, KHÔNG xây nút/đường sự kiện mới. Cổng bắt buộc: (a) importer đọc nguồn theo con trỏ/offset, không mất sự kiện khi giãn nhịp — nếu đọc theo cửa sổ thời gian cố định ngắn hơn 10′ thì nới cửa sổ đó cùng mục hoặc SKIP; (b) không consumer nào khác của `lifecycle-snapshot.json`/`presence.json` có ngưỡng tuổi < 1500 s (grep toàn nguồn đang chạy); (c) phép thử âm trên BẢN SAO: snapshot 1501 s ⇒ khối lifecycle bị bỏ ⇒ INV12 đỏ; 900 s ⇒ xanh; importer dừng (mô phỏng) ⇒ đỏ ≤ 25′. Không đổi `incomex-hvu-presence` 15″ hay hợp đồng claim. Một cổng FAIL ⇒ lùi cả mục, SKIP, báo rõ. Không dùng 90″ của P04.

R2-6: xác minh flow id + status đúng duy nhất `[DOT-REG] Count Refresh (6h)`, không có consumer/route/PG count thật cần output; lỗi PATCH bị Guard chặn, đã có restore status. Nếu PASS dùng DOT approved đổi ACTIVE→INACTIVE (không xoá flow, không tắt Watchdog/trigger khác), kiểm smoke Directus/PG/Agent Data/Guard; nếu còn dependency => SKIP.

S2 — POST/Đ30/31: sau mỗi APPLIED kiểm diff đúng allowlist + Config Guard C3 MATCH, functionality/smoke; negative test trên bản sao, canh báo lỗi thật, rollback từng mục khi tạo đỏ mới. Cuối RUN 22 Kuma theo ID/status/reason so PRE; không tô xanh global nếu đã có lỗi cũ; không gửi Telegram test spam, biên nhận chỉ khi có thật. Đổi script/cron/status phải có beforeimage và đường đảo tương đương. Không purge/retention, restart container/swapoff, đổi RAM hay sửa app khác. 0 tiến trình nền/tệp tạm còn lại, trả VPS-GHI cùng KQ.

S3 — KQ chỉ ghi vào task này + cập nhật Bảng cùng commit, một bảng 6 hàng: APPLIED/SKIP + lý do + thay đổi/chi phí trước/sau có đo (không lấy toàn CPU job làm số tiết kiệm) + trễ phát hiện tối đa + chủ bảo vệ + rollback + trạng thái Guard/Kuma. Không giữ CLI/terminal chờ 20 phút/24h; journal/Kuma/08:00 sẵn có quan sát số sau, chưa đủ ghi CHƯA ĐO. Mục ngoài phạm vi trỏ Host đúng việc.

STEP_WALK_V1 (DROOT48 · Claude P06):

| Bước | Ai làm | Trigger | SLA | Evidence phải đo | Hỏng thì ai biết, bao lâu | Bước kế |
|---|---|---|---|---|---|---|
| S0 | Claude Code | Owner dán sau READY | ≤ 10′ | ACCEPT+READY cùng SHA, VPS-GHI CAS, PRE 22 đèn theo ID | Code ghi KQ DỪNG ngay trên task | R2-1 |
| R2-1 → R2-2 → R2-3 → R2-6 | Claude Code | S0 PASS | ≤ 25′ | diff đúng allowlist, Config Guard MATCH, `run-parts --test`, crontab, flow status, smoke | Guard 5′ → Kuma #22 → Telegram ≤ 10′ | R2-4 |
| R2-4 | Claude Code | mục trước xong | ≤ 15′ | phép thử âm (a)(b)(c) + SELFTEST | Guard đỏ ≤ 45′ + 5′ | R2-5 |
| R2-5 | Claude Code | R2-4 xong/SKIP | ≤ 15′ | cổng (a)(b)(c) + INV12 PASS + SELFTEST | Guard đỏ ≤ 25′ | S2 |
| S2 → S3 | Claude Code | mục cuối xong | ≤ 10′ | POST 22 đèn so PRE, 0 tiến trình nền, KQ + trả VPS-GHI cùng commit | GPT Host + Claude đọc KQ | GPT nhận KQ |

Tổng ≤ 75′. Số «tiết kiệm sau» không đo trong RUN: đọc từ journal/Kuma/bản tin 08:00 sẵn có, không hẹn giờ.

BÁO OWNER MỘT DÒNG: XONG/DỪNG · VPSC2-R2 · APPLIED=[...] SKIP=[mã:lý do] · Guard ... · 22 Kuma ... · VPS-GHI trả · commit.
