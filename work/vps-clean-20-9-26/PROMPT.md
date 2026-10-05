# PROMPT — VPSC R6W · WORKER WRITE-IDLE FINAL CLOSEOUT 06/10/2026

STATUS: **FINAL DRAFT — Host chốt theo P44; phát READY trên đúng last-touch của file này**
RUN_ID: VPSC-R6W-WORKER-CLOSE-20261006-01
Executor_Surface: Claude Code CLI trên Mac → host worker VPS qua đường hiện hữu
Write_Path: repo SSOT qua `workspace_*`; runtime chỉ phần host worker đã được phép
Evidence_Dir: `/opt/incomex/work/vps-clean-20-9-26/R6W-20261006/`

## 0 · Đích duy nhất
Khép đúng blocker còn lại của VPSC: worker đã hết restart/lock nhưng vẫn tạo write-churn lúc rỗi.

**Không làm lại** cleanup, PLAN_T/D, checker M15, APR, storage-watch/#11, logrotate, CWEB, HJW, Graph hay phần R6 đã PASS.

Acceptance worker:
- 0 restart / 0 database-lock crash / 0 duplicate job;
- chức năng không regression;
- median 3 mẫu × 5 s sau nạp: `syscw ≤168` **và** `write_bytes ≤0,666 MB/5 s` (giảm ≥80% so canonical P29: 840 syscw / 3,33 MB);
- chỉ host worker; **không rebuild/recreate `incomex-agent-data` trong mọi nhánh**.

## 1 · PRE
1. Đọc `AGENTS.md → root COLLAB.md → work/vps-clean-20-9-26/COLLAB.md P42–P45 → BAO-CAO.md R6 → PROMPT này`.
2. Fresh-check shared mutation. HJW chỉ được acceptance/read-only; nếu có server mutation/recreate agent-data thật đang chạy ⇒ `DỪNG · CONCURRENCY`, 0 mutation.
3. Xác nhận v1 đang chạy = host worker commit/hash `9457406` hoặc exact current equivalent đã ghi P42; lưu rollback exact hash.
4. Chụp baseline: MainPID worker, restart counter, queue running jobs, load đầu, WAL size, 3 mẫu I/O ×5 s bằng đúng `io5.py`.
5. Nếu có job của phiên khác đang **running** trong queue ngay trước restart worker ⇒ chờ bounded tới sạch; không huỷ job người khác.

## 2 · Cổng test v2 — so với đúng v1 đang chạy, không chặn theo load
Ghi load đầu/cuối để giải thích, nhưng **không dùng load<2 làm cổng**.

### 2.1 Lượt đủ
- Chạy đúng tệp 23 test `tests/continuation/test_p02_snapshot_k8.py` trên v2.
- Nếu **23/23** ⇒ v2 đủ cổng, sang §3.
- Nếu có **1–3 test đỏ** ⇒ sang 2.2.
- Nếu >3 test đỏ ⇒ `DỪNG · TEST_REGRESSION`, không nạp, không viết v3.

### 2.2 Phân xử từng test đỏ
Với mỗi test đỏ, chạy **5 cặp xen kẽ** trên cùng cửa sổ:
`v1 đang chạy → v2 → v1 → v2 ...`

Ghi từng lượt: PASS/FAIL · duration · load.

V2 được coi **không tệ hơn** khi với **mọi test đỏ**:
`green(v2) ≥ green(v1) - 1`.

Nếu bất kỳ test nào không đạt ⇒ `DỪNG · V2_WORSE_THAN_V1`, không nạp.
Không viết v3 trong RUN này.

## 3 · Nạp v2 host worker
Chỉ khi §2 PASS.

1. Fresh-check queue không có running job của phiên khác.
2. Nạp **host worker only** bằng đường hiện hữu; giữ rollback v1 exact.
3. Tuyệt đối không rebuild/recreate container `incomex-agent-data`.
4. Smoke bắt buộc:
   - queue/status/cancel/recovery;
   - 0 duplicate;
   - 0 database-lock crash;
   - restart counter không tăng;
   - core Agent Data/UI health same-or-better.
5. Ghi `queue.sqlite-wal` size:
   - ngay sau nạp;
   - sau smoke;
   - ở lượt watcher-day.
   Nếu **>64 MB** ở bất kỳ điểm nào ⇒ rollback v1 và `DỪNG · WAL_CAP`.

## 4 · Đo write-idle
Sau settle ngắn, cùng MainPID và cùng phương pháp R6:
- 3 mẫu × 5 s;
- ghi `syscw`, `write_bytes`, `cancelled_write_bytes`, CPU time/load.

**PASS** khi median:
- `syscw ≤168/5s`;
- `write_bytes ≤0,666 MB/5s`;
- smoke/health không regression.

Nếu giảm <80% nhưng chức năng PASS và I/O **không tệ hơn v1**:
- **giữ v2**;
- KQ = `DỪNG · WRITE_IDLE_NOT_MET`;
- không v3, không rebuild container.

Nếu có regression chức năng/health:
- rollback v1 ngay;
- KQ DỪNG với exact failure.

## 5 · POST-PROTECT
Chỉ phần worker R6W:
- before/after hash + rollback;
- test/smoke evidence;
- Guard/Config Guard phần liên quan same-or-better;
- Telegram receipt nếu production mutation;
- cập nhật Bảng + BAO-CAO.

Không reset hoặc tính lại đồng hồ storage-watch ngày vì R6W không xoá dung lượng lớn.

## 6 · Điểm dừng cuối
### PASS worker
Ghi:
`KQ@VPSC-R6W-WORKER-CLOSE-20261006-01 XONG · TEST=<...> · WRITE=<...> · WAL=<...> · HEALTH=<...>`

Sau đó chỉ còn watcher-day.

### FAIL worker
Không mở RUN thứ ba, không viết v3 trong VPSC.

Ghi:
`KQ@VPSC-R6W-WORKER-CLOSE-20261006-01 DỪNG · CHƯA ĐẠT: worker write-idle · <exact reason>`

Chuyển residual cho **chủ mã agent-data / Host GPT** để xử lý sau khi ràng buộc N1 cho phép rebuild nếu thật sự cần. VPSC vẫn đi tới watcher-day và đóng với residual công khai; không gọi đó là PASS worker.

## 7 · “Ngày xanh” để đóng VPSC
Đọc dòng `DISKWATCH` **sau 02:00 +07 ngày 07/10/2026**.

Ngày xanh = đồng thời:
- `d24` là số và <2 GiB;
- 0 unknown path >24h;
- 0 quá cap / quá TTL;
- Kuma #11 xanh suốt;
- worker restart counter không tăng.

`d7` còn bị đợt cleanup che tới khoảng 13/10: ghi residual quan sát, **không chặn CLOSE**.

Đèn #6 Nuxt 404 chập chờn là residual của CWEB/chủ khác, không tính vào ngày xanh VPSC.

## 8 · Không làm
- Không rebuild/recreate agent-data.
- Không Docker prune/build/restart.
- Không sửa cleanup/checker/APR/storage-watch.
- Không HJW mutation, Graph, DNS/CWEB, knowledge build.
- Không viết v3.
- Không mở task/RUN tiếp theo ngoài R6W trong VPSC.
