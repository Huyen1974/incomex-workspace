# PROMPT — VPSC · V1 Codex thẩm tra độc lập báo cáo R1 (AUDIT / NO PRODUCTION MUTATION)

RUN_ID: VPSC-V1-20260921-01
Soạn: Claude Chat (Host), 2026-09-21, theo D06 (Owner giao Host chỉ đạo Codex trực tiếp). Trạng thái chỉ tin `work/vps-clean-20-9-26/COLLAB.md`. Chỉ chạy khi COLLAB có `READY@`/`OWNER_APPROVED@` đúng full SHA commit cuối chạm file này + lệnh RUN.
**Executor_Surface = Codex CLI chạy trên VPS (có shell).** Không có shell VPS → DỪNG.
**Write_Path:** `workspace_*` (Agent Data); phiên không bind thì `fs_*` ("Incomex VPS"). Cấm git/GitHub native để ghi; không clone repo.
**Mục đích:** biết CHẮC điều gì đang làm đầy đĩa trước khi dọn. Bạn là người chấm độc lập: tự đo lại, KHÔNG chép số của R1, KHÔNG coi kết luận R1 là đúng.

## 0. Cổng
1. `df -h /` trước tiên; Used ≥90% hoặc trống <8GB → chỉ đo nhẹ, báo số.
2. Đúng một read-gate: đọc `work/vps-clean-20-9-26/COLLAB.md` qua Write_Path; fail → DỪNG, nêu tool đã thử.
3. Giấy phép: full SHA commit cuối chạm file này (không so HEAD repo) phải khớp COLLAB; lệch → DỪNG.
4. Đọc `work/vps-clean-20-9-26/BAO-CAO.md` mục R1 — đối tượng thẩm tra.

## 1. Luật cứng
- CẤM: rm/mv/truncate/ghi đè file; mọi docker rm/rmi/prune/save/tag/build; compose up/down/restart; DROP/VACUUM; sửa cron/systemd/config; gọi API xoá của Qdrant; kill tiến trình hệ thống; tải backup về VPS; giải mã backup.
- KHÔNG chờ/sleep, không đo lặp theo thời gian: mỗi phép đo làm một lần (D05).
- Không in secret, nội dung .env/config, nội dung dump. Bằng chứng thô (nếu cần) ở `/var/lib/incomex-audit/VPSC-V1-20260921/`, ≤50MB, ngoài mọi cây Git.
- Chỉ ghi repo 2 chỗ: mục mới trong `BAO-CAO.md` + dòng `VPSC.3` trong COLLAB. Không sửa mục R1, `PROMPT.md`, `view.html`.
- Mục tiêu thời lượng ≤45 phút.

## 2. Việc cần thẩm tra
A. **Tổng:** df; du tầng 1; lớp ghi của `incomex-qdrant`, `postgres`, `incomex-directus` trong kho containerd. Tổng có khớp df không.
B. **4 nguyên nhân rò R1 nêu** — tự chứng minh hoặc bác bằng số + đọc script:
  1. Bản chụp Qdrant kẹt trong container: đếm + GB; `scripts/qdrant-backup.sh` có/không xoá bản chụp server-side (so với `backup-to-gdrive.sh`).
  2. Bản sao Nuxt `deploys/nuxt-output.*`: đếm + GB; script deploy có/không tỉa.
  3. Log pm2 trong container Directus: GB + tốc độ.
  4. `context-pack.tmp`: đếm + GB; có/không dọn.
  Thêm: có nguồn tăng nào ≥0,5GB mà R1 bỏ sót?
C. **Chấm từng nhóm N1–N15** của manifest R1: PASS / REVISE / BLOCK + một câu lý do. Bắt buộc:
  - N1: xác nhận bản Qdrant mới nhất có ở host (7 ngày) VÀ có trong gói Drive gần nhất (đọc meta/log, không tải về); xác nhận xoá qua API không cần restart.
  - N3, N9, N11: grep TỪNG tên/đường dẫn trong `/opt/incomex`, `/etc`, crontab mọi user, unit systemd; có tham chiếu đang chạy → BLOCK phần đó.
  - N7, N8: xác nhận không phải cha của image đang chạy (so RootFS).
  - N13 (DB thử): chỉ xác nhận vẫn `UNKNOWN_HOLD`; không đo theo thời gian.
D. **Con số thu hồi:** R1 ghi `DELETE_PROVEN_SAFE` ~34,4GB — tính lại theo các nhóm bạn PASS.

## 3. Báo cáo — ghi TRƯỚC khi trả Owner
- Chèn lên ĐẦU `BAO-CAO.md` mục "V1 — Codex thẩm tra · <ngày> · executor=Codex CLI · write_path=<…>", giữ nguyên mục R1.
- Thứ tự: (1) CHO OWNER ≤10 dòng: R1 đúng/sai ở đâu; 4 nguyên nhân xác nhận hay bác; GB thu hồi an toàn đã kiểm. (2) Bảng N1–N15: Nhóm · GB R1 · GB V1 · Kết luận · Lý do; chênh >10% hoặc >0,5GB phải nói rõ. (3) Bỏ sót (nếu có). (4) Kho bằng chứng.
- Repo công khai: không secret/token, IP/tên miền nội bộ, ID Google Drive, tên tài khoản, output lệnh thô.
- Sửa dòng `VPSC.3` trong COLLAB thành `MACHINE_DONE · V1 · xem BAO-CAO.md` (có expected_version; không gộp được thì tách 2 commit theo A4).
- Trả đúng một dòng: `XONG · VPSC-V1 · executor=Codex CLI · write_path=<…> · PASS <n> / REVISE <n> / BLOCK <n> · thu hồi đã kiểm <GB> · xem BAO-CAO.md` hoặc `DỪNG · VPSC-V1 · <mục> · <lý do>`.

## 4. Sau Codex (không phải việc của Codex)
Host đối chiếu R1 + V1, đưa phần đã thống nhất lên `view.html`; hội đồng chốt; Owner duyệt; lượt dọn thật là PROMPT sau.
