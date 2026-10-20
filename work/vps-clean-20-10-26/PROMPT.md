# PROMPT — VPSC2-R3-LOAD-ATTRIBUTION-20261021-01

DRAFT / KHÔNG RUN. Claude Chat Reviewer ACCEPT đúng last-touch SHA PROMPT.md → GPT Host READY cùng SHA → Owner dán cho Codex mới được chạy.
Executor_Surface=Codex Desktop (KHÔNG phải Claude Code CLI).
Repository_Write_Path=Incomex workspace_* root=workspace (chỉ STARTED/KQ/Bảng).
VPS_Read_Path=SSH/VPS read-only đã duyệt, nice -n 19 ionice -c3 khi phù hợp.
RUN_ID=VPSC2-R3-LOAD-ATTRIBUTION-20261021-01.
Đọc AGENTS.md → work/vps-clean-20-10-26/COLLAB.md §0/Bảng/P08–P11 → PROMPT.md → R1 BAO-CAO §PROOT11-R1. Graph P161/P163 chỉ là mốc, không dọn/kiểm kê lại.

MỤC TIÊU: quy nguồn mẫu load 5,7–6,6 trên 6 vCPU; swap ~1,87/2GiB khi MemAvailable~6,3GiB; kiểm CPU/swap/I/O thực tế, tách tải nghiệp vụ hợp lệ khỏi lãng phí; đọc sơ bộ hiệu quả timer R2 qua nhật ký có sẵn. Không mặc định load cao là CPU nghẽn hoặc swap gần đầy là thrashing. Nếu không thấy áp lực/tác vụ thừa có chứng cứ thì NO_ACTION, không mở RUN sửa cho đủ việc.

HẠN: tối đa 15 phút từ STARTED; không giữ terminal/máy/phiên chờ approval/24h. Tuyệt đối KHÔNG mutation VPS, chiếm VPS-GHI, sửa/dừng/restart/xoá, swapoff, clear cache, buildx, thêm monitor/cron/Guard/log, gọi Telegram, quét toàn ổ hoặc DB, in secrets/token/argv chứa khóa. Không workspace_exec gây container tạm trên VPS. Thiếu quyền thì CHƯA ĐO, không tự bypass.

S0 (<=2′): kiểm AGENTS/COUNCIL, ACCEPT/READY full last-touch PROMPT, không STOP/STARTED trùng, đọc root VPS-GHI và Graph P163. Gate sai ⇒ KQ DỪNG. Gate PASS ⇒ ghi STARTED+Bảng trong cùng commit. R3 chỉ đọc, không lấy VPS-GHI; nếu RUN ghi production khác đang hoạt động, ghi rõ để không quy tải của nó cho rác.

S1 (<=5′): đo ít nhất 2 mốc cách nhau 60–120 giây nếu đang tải, bằng sar/vmstat/PSI/pidstat/iostat/cgroup cpu.stat/io.stat/memory.events/số liệu đã có. Ghi CPU user/system/idle/iowait/steal, load1/5/15, MemAvailable, swap si/so, CPU/MEM/IO PSI, disk await/util, CPU throttled/oom (delta). TOP5 dịch vụ/cgroup theo CPU-giây delta và I/O thật; phân biệt task hữu ích với cron/Guard/helper/nhiễu, không tính toàn containerd/dockerd là rác. Không ghi full process cmdline/environment. Nếu tải đã xuống, nói đúng như thế.

S2 (<=4′): đọc journal systemd của mcpw-presence-import và incomex-config-drift-check từ R2 KQ 2026-10-20T13:40Z đến hiện tại; so PRE 24h đã ghi tại P08/R1. Đếm lượt, CPU-s tổng, CPU-s/lượt, CPU-s/giờ và mức dao động, chỉ trong cửa sổ có thật (<24h sau R2 thì ghi CHƯA ĐỦ 24H). Nếu drift-check/lượt tăng từ ~12 lên ~25s, thử giải thích theo lượng việc tích lũy giữa nhịp hoặc tải cùng mốc mà không chạy profiling nặng. Xác nhận bằng nguồn đã có drop_caches/fstrim hourly no-op, 3 cron OFF, weekly fstrim còn, không chỉnh gì.

S3 (<=2′): đọc sự kiện Kuma/Guard có sẵn xem #6/#22 còn đỏ hay tự UP sau Graph POST, timestamp/reason, nếu lặp lại giao CWEB/TQT; không phát probe liên tục hoặc gửi Telegram test. Flow Count Refresh R2-6 còn active là nợ đúng chủ DOT/TQT, không sửa tool/status trong R3.

S4 (<=2′): KQ+Bảng đúng task này, tối đa 12 dòng và TOP3 ứng viên có chi phí chứng minh/consumer/rủi ro/rollback, hoặc NO_ACTION nếu không thấy lợi ích an toàn. Không nhân chi phí unit ra savings. Nếu nguyên nhân là ứng dụng active thì ghi owner CWEB/TQT/HJW/... chứ không sửa chéo. Không tạo file báo cáo mới, không sửa root/Graph. Dọn mọi đồ của lượt, 0 process/SSH nền, KQ XONG/DỪNG ngay.

STEP_WALK_V1 (DROOT48):
| Bước | Ai | Trigger | SLA | Bằng chứng | Hỏng/next |
|---|---|---|---|---|---|
| S0 | Codex | Owner RUN sau READY | <=2′ | SHA/gate/STARTED | KQ DỪNG hoặc S1 |
| S1 | Codex | S0 PASS | <=5′ | tải 2 mẫu, PSI/vmstat/cgroup | CHƯA ĐO hoặc S2 |
| S2 | Codex | S1 xong | <=4′ | journal timer R2 delta thật | S3 |
| S3 | Codex | S2 xong | <=2′ | #6/#22 và chủ có mốc | S4 |
| S4 | Codex | S3 xong | <=2′ | KQ/Bảng/cleanup | GPT Host nhận KQ |

Báo Owner một dòng: XONG|DỪNG · VPSC2-R3 · áp lực thật/không · TOP3 hoặc NO_ACTION · #6/#22 · commit.
