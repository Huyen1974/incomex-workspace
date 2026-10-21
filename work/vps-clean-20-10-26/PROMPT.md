# PROMPT — VPSC2-R3-LOAD-ATTRIBUTION-20261021-01

TRẠNG THÁI: DRAFT — CẤM RUN. Chỉ chạy khi Claude Chat (khác hãng Codex/GPT) đã ACCEPT exact last-touch SHA PROMPT.md, GPT Host ghi READY cùng SHA ở COLLAB và Owner giao thủ công cho CODEX DESKTOP, không phải Claude Code CLI.
RUN_ID: VPSC2-R3-LOAD-ATTRIBUTION-20261021-01.
Executor_Surface: Codex Desktop trên Mac Owner.
Write_Path: Incomex workspace_* root=workspace, CHỈ nhật ký STARTED/KQ/Bảng trong work/vps-clean-20-10-26/COLLAB.md. VPS_Read_Path: SSH/approved read-only nhẹ, nice -n19 ionice -c3 khi phù hợp; không workspace_exec/container tạm.
SSOT: AGENTS.md → root COLLAB.md current → task COLLAB §0/Bảng/P08–P12 → PROMPT.md → BAO-CAO VPSC tháng9 §PROOT11-R1; Graph P161/P163 + D18 mới chỉ làm ranh giới, KHÔNG khảo sát/xóa Graph.

OWNER MỤC TIÊU: giải phóng tối đa CPU/RAM/I/O VPS cho PG, Agent Data, Graph (R10B–R11), MCP/Hermes/backup và việc thật sự dùng. Không bật thêm lớp quan sát để "đo quan sát".

DỮ LIỆU CỬA VÀO 21/10 14:38+07 (chỉ snapshot, không làm số hiện hành): host 6 vCPU, load1/5/15 5,34/4,49/4,52; SwapFree=512 KiB/SwapTotal 2.097.148 KiB, MemAvailable=6.504.772 KiB (~6,20 GiB), disk_free 45.987.004.416B (~46GB), HTTP AgentData và UI 200, 0 failed unit. R2 đã OFF đúng 3 cron + drop_caches/fstrim hourly no-op, drift-check20′/no-run45′, presence-import10′/age1500s. Graph GS-CLEAN 9/9 đã xong. Không dùng snapshot 20/10 Graph "chưa chạy". Không coi swap USED gần max = đang thrashing, hoặc load>=6 = CPU luôn bão hòa.

CHỐT: 1 lượt đọc <=15 phút tính từ STARTED, không VPS-GHI, KHÔNG mutation/runtime writes, stop/restart/disable/install/buildx/swapoff/drop_caches, không chạm timer/config/Kuma/Guard/Graph/PG production, không gửi Telegram, quét toàn ổ/bảng lớn, không in key/argv/cmdline có token, không tạo tệp/log/process nền trên VPS; chỉ dùng sar/journal/cgroup/sysstat đã có. Nếu Graph/TQT/HJW có RUN ghi nặng đang diễn ra, phân tải cho đúng chủ, không cản và không giả đo tĩnh. Không đợi lịch/24h, không tạo monitor mới.

S0 (≤2 phút) — Read-gate A6: AGENTS/§0+Bảng/P08–P12/PROMPT, ACCEPT+READY full SHA last-touch, STOP/STARTED mới, bootstrap/quorum. Gate FAIL → KQ DỪNG sạch. PASS → ghi STARTED và cập nhật Bảng (repo ONLY, SAME_COMMIT); xác nhận root VPS-GHI và Graph 0/active theo nguồn mới, không chiếm cờ.

S1 (≤5 phút) — QUY NGUỒN SWAP + CPU/IO, ưu tiên:
- Hai mẫu cách 60–120s khi có tải: CPU user/system/idle/iowait/steal, load1/5/15, MemAvailable, SwapUsed, vmstat si/so, CPU/memory/io PSI, disk await/util, cgroup cpu.stat/throttling, memory.events max/oom/oom_kill delta, io.stat delta.
- Top 5 container/service/cgroup theo memory.swap.current và memory.current/max, file/anon cache nếu có; tiến trình host theo VmSwap (chỉ PID+service/owner, không in argv/secret), so sức ép memory.limit/psi. Phân biệt swap LƯU TRỮ CŨ so với swap-in/out ACTIVE; không suy swap gần hết => restart. Top5 theo CPU-giây delta / I/O read/write. Nếu có Graph workload/AI client, xác định nó thuộc RUN hữu ích, không quy thành rác.
- Chỉ báo đỏ khi thấy áp lực thực (PSI stall/si-so/oom/throttle/disk queue/latency cùng mẫu); thiếu số ghi CHƯA ĐO.

S2 (≤4 phút) — HIỆU QUẢ R2 & ỨNG VIÊN NỀN:
- Đọc systemd journal đã có từ KQ R2 20/10 13:40Z: mcpw-presence-import.timer và incomex-config-drift-check.timer; lượt thật, CPU-s/lượt, CPU-s/giờ, độ rộng mẫu, so PRE. Nếu <24h POST, ghi thiếu. Kiểm bất thường drift-check/lượt ~25s so ~12s trước có phải làm nhiều vì kỳ dài hơn hay tải nền, KHÔNG profiler/chạy tay job.
- Chỉ khi log/timer sẵn đủ, ước lượng nhóm 13 Docker HEALTHCHECK 10–60s, dot-directus-license-watch */5 (~288 lượt/ngày, có container tạm R1), storage-watch walk 1.213.822 entries/153s và hvu-presence15s. Mỗi mục: lần chạy, consumer, CPU/I/O attributable có nguồn; không có cost rõ ⇒ CHƯA ĐO, không đề xuất TẮT do "nhịp dày".
- Xác nhận ba Runner cũ OFF và hourly drop_caches/fstrim no-op qua config/journal hiện hữu, không chạy thử. R2-6 Count Refresh flow còn active: lỗi 4 lần/ngày có chủ DOT/TQT, KHÔNG thêm công cụ status/disable ở R3. Directus retention/purge và dọn đĩa rộng nằm ngoài (disk còn đủ, mất audit có rủi ro).

S3 (≤2 phút) — CẢNH BÁO/CHỦ: xem các sự kiện sẵn có của Kuma/Guard #6/#22; Graph POST 22/22 PASS nhưng #6/INV18 từng tái diễn, chỉ coi còn lỗi nếu mốc hiện hành; giao đúng CWEB/TQT, đừng sửa web/Guard. Không probe dày hoặc gửi tin thử, không tự nhân vào ngân sách CPU của rác.

S4 (≤2 phút) — KQ/Bảng DUY NHẤT tại task: (1) PRESSURE YES/NO/UNKNOWN (cpu/PSI/swap si-so), (2) Top5 CPU/swap/I/O theo chủ cùng cửa sổ, (3) chi phí POST R2 thật & độ tin, (4) nợ nhỏ chính xác, (5) tối đa TOP3 hạng mục có tài nguyên thu hồi được đo/consumer/risk/rollback và phân chủ; nếu không có cơ hội an toàn đáng làm ghi NO_ACTION, không phát R4. Không gán savings bằng toàn CPU của unit. Không tạo báo cáo mới/sửa root/Graph. Dọn mọi đồ phía Codex, 0 SSH/background, KQ XONG/DỪNG ngay, không giữ phiên đợi ngày mai.

STEP_WALK_V1 (DROOT48):
| Bước | Ai | Trigger | SLA | Evidence | Fail/Next |
|---|---|---|---|---|---|
| S0 | Codex | Owner dán sau READY | ≤2′ | gate full SHA + STARTED repo | KQ DỪNG hoặc S1 |
| S1 | Codex | S0 PASS | ≤5′ | CPU/PSI/si-so + per-cgroup swap/memory/cpu/io 2 mốc | UNKNOWN hay S2 |
| S2 | Codex | S1 xong | ≤4′ | timer R2 delta + 2–3 job còn hoạt động từ logs sẵn | S3 |
| S3 | Codex | S2 xong | ≤2′ | Guard/Kuma #6/#22 latest và chủ | S4 |
| S4 | Codex | S3 xong | ≤2′ | KQ/Bảng/cleanup TOP3 hay NO_ACTION | GPT Host tiếp |

Báo Owner 1 dòng: XONG|DỪNG · VPSC2-R3 · pressure=... · swap culprit=... · TOP3/NO_ACTION · #6/#22 · commit KQ.
