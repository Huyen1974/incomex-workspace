# PROMPT — VPSC · V1b Codex hoàn tất thẩm tra (AUDIT / NO PRODUCTION MUTATION)

RUN_ID: VPSC-V1B-20260921-01
Soạn: Claude Chat (Host), 21/09/2026, theo D06 + D07. Trạng thái chỉ tin `work/vps-clean-20-9-26/COLLAB.md`. Chỉ chạy khi COLLAB có `OWNER_APPROVED@`/`READY@` đúng full SHA commit cuối chạm file này + lệnh RUN.
**Executor_Surface = Codex Desktop điều khiển shell VPS qua SSH** (đúng bề mặt V1 đã dùng).
**Write_Path = `workspace_*`** (V1 đã ghi thành công qua đường này); dự phòng `fs_*`. Cấm git/GitHub native để ghi; không clone.
**Vì sao có lượt này:** V1 dừng ở chế độ đo nhẹ vì đĩa 91% chạm ngưỡng 90% Host đặt. Ngưỡng đó đặt sai chỗ: quét chỉ đọc (du/find/grep/inspect) không làm đầy đĩa; thứ phải chặn khi đĩa gần đầy là GHI. D07 sửa như §1. Lượt này CHỈ làm phần V1 còn dở, không lặp phần V1 đã xác nhận.

## 0. Cổng
1. `df -h /` và `df -B1 /` một lần. Available <3GiB → DỪNG ngay, báo số.
2. Đúng một read-gate: đọc `work/vps-clean-20-9-26/COLLAB.md` qua Write_Path; fail → DỪNG.
3. Giấy phép: full SHA commit cuối chạm file này (không so HEAD repo) khớp COLLAB; lệch → DỪNG.
4. Đọc `BAO-CAO.md` mục V1 (việc còn dở) và mục R1 (đối tượng thẩm tra).

## 1. Luật cứng
- Giữ nguyên danh sách CẤM của V1: không xoá/sửa/truncate/restart/DROP/prune/save/tag/build; không gọi API xoá Qdrant; không tải/giải mã backup; không sửa cron/systemd/config; không kill tiến trình hệ thống.
- Ngưỡng (D07): quét chỉ đọc được phép tới khi Available còn ≥3GiB. KHÔNG ghi file nào lên VPS, kể cả bằng chứng thô (giữ trong output phiên như V1). Mọi du/find chạy `nice -n 19 ionice -c3`, luôn `-x`, có timeout.
- Không chờ/sleep; mỗi phép đo một lần.
- Chỉ ghi repo: chèn mục V1b lên đầu `BAO-CAO.md` + dòng `VPSC.3` trong COLLAB. Không sửa mục V1, R1, `PROMPT.md`, `view.html`.
- Mục tiêu ≤45 phút.

## 2. Việc còn dở của V1
A. **Đối soát tổng:** `du -x` tầng 1; tách trong `/var/lib/containerd`: lớp ghi `incomex-qdrant`, `postgres`, `incomex-directus`, snapshot image, blob; `lsof +L1`. Tổng khớp df (lệch >3GiB phải giải thích).
B. **Phần tăng +2,94GiB từ 04:10Z đến 07:48Z ngày 21/09:** `find / -xdev -newermt '2026-09-21 04:10Z'` (và `-newerct`) cộng theo thư mục; nêu nguồn sinh (script/mission/việc nào — kể cả build/deploy web và lớp view của việc khác sáng 21/09). Nếu là nguồn mới chưa có trong R1 → thêm vào sổ nguồn sinh.
C. **GB đo độc lập** cho N3 (mọi dạng tên `nuxt-output.*` và `nuxt-output-*`), N4, N5.
D. **Grep TỪNG tên/đường dẫn** của N3, N9, N11 trong `/opt/incomex` (trừ chính thư mục đích và `context-pack*`), `/etc`, crontab mọi user, unit systemd. Kết quả theo từng tên: 0 tham chiếu / có tham chiếu (file:dòng). N11 phải ra danh sách tên cụ thể, không wildcard.
E. **Chấm lại N1–N15** khi đã có số đủ. N1 giữ BLOCK nếu chưa có bằng chứng bản Qdrant ngoài VPS — việc làm ra bằng chứng đó (V1-01) thuộc lượt dọn, không phải lượt này.
F. **Con số:** tổng thu hồi đã kiểm (chỉ nhóm PASS) và số GiB cần thu hồi để đạt 45GiB trống từ df hiện tại.

## 3. Báo cáo
- Chèn lên ĐẦU `BAO-CAO.md` mục "V1b — Codex hoàn tất thẩm tra · <ngày> · executor=Codex Desktop qua SSH · write_path=<…>".
- Thứ tự: (1) CHO OWNER ≤10 dòng; (2) bảng N1–N15 cập nhật: GB V1b · Kết luận · Lý do; (3) nguồn của +2,94GiB; (4) bằng chứng.
- Repo công khai: không secret/token, IP/tên miền nội bộ, ID Google Drive, tên tài khoản, output lệnh thô.
- Sửa dòng `VPSC.3` trong COLLAB thành `MACHINE_DONE · V1b · xem BAO-CAO.md` (hoặc `STOPPED · <lý do>`), có expected_version.
- Trả đúng một dòng: `XONG · VPSC-V1B · executor=Codex Desktop qua SSH · write_path=<…> · PASS <n> / REVISE <n> / BLOCK <n> · thu hồi đã kiểm <GiB> · nguồn +2,94GiB: <…> · xem BAO-CAO.md` hoặc `DỪNG · VPSC-V1B · <mục> · <lý do>`.

## 4. Sau Codex (không phải việc của Codex)
Host gộp R1 + V1 + V1b và V1-01…V1-06 thành đề bài lượt dọn; hội đồng chốt; Owner duyệt.
