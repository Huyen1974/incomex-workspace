# PROMPT — VPSC · R4 Khép việc: khoá build cache + báo image + dọn dấu vết SEC-01 (CÓ MUTATION nhỏ)

RUN_ID: VPSC-R4-20260922-01
Soạn: Claude Chat (Host), 22/09/2026, sau R3 (`KQ@VPSC-R3-20260921-01 XONG`). Theo D08 (Owner uỷ quyền). Tham khảo JEV (`typesafe/jev-1.13`): build cache → tự tỉa có trần (0,99); image → chỉ báo cho tới khi chủ R03 đặt luật (0,79); khoá thứ hai Qdrant → không cần (0,47, tin cậy thấp; Host chốt: đủ vì 2 khoá nơi sinh fail-closed đã PASS lượt thật + cảnh báo đĩa 80%). Trạng thái chỉ tin COLLAB. Chỉ chạy khi COLLAB có `OWNER_APPROVED@` + Host `READY@` đúng full SHA commit cuối chạm file này + lệnh RUN.
**Executor_Surface = Claude Code CLI trên Mac → shell root VPS qua SSH.** **Write_Path = `workspace_*`**; dự phòng `fs_*`. Không clone, không ghi repo bằng git.
**Chế độ (D08):** không hỏi quyền từng lệnh; luật cứng dưới đây thay cho van tự động. Trước mỗi thay đổi ghi trạng thái cũ + cách lùi; sau đó kiểm health; xấu đi → lùi ngay và DỪNG. Không làm hỏng thứ đang chạy là ưu tiên số 1.

## 0. Cổng
1. `df -B1 /`; read-gate COLLAB; giấy phép khớp SHA (commit cuối chạm PROMPT, không so HEAD); lệch → DỪNG.
2. NO_CONCURRENT: không có `docker build/compose/pull`; không RUN khác đang đụng VPS; không build đang chạy. Không đạt → chờ ≤15 phút rồi DỪNG.
3. Chụp trạng thái trước: df; 12 container + health; web 200; Directus health; Qdrant green.

## 1. Luật cứng
- KHÔNG xoá/tag/untag bất kỳ image nào; không `docker image prune`, `docker system prune`; không restart/recreate container. Không đụng image rollback R03 hay image đang chạy (kể cả image không tag của Nuxt).
- Luật bí mật như R3: không in token/khoá; bí mật chỉ qua biến/pipe; chỉ dừng tiến trình theo PID.
- Sửa script: commit git cục bộ `/opt/incomex` trước/sau, `bash -n`, mô phỏng nhánh lỗi.

## A — Khoá build cache (loại tái tạo được)
A1 Đo build cache hiện tại (tổng + phần có thể thu hồi).
A2 Thêm luật (j) vào `scripts/vps-retention.sh`: mỗi Chủ nhật lúc 04:xx, nếu không có build đang chạy → tỉa build cache giữ tối đa **5GiB** (lệnh prune của builder với giới hạn giữ dung lượng; chỉ build cache, không image/container/volume). Ghi log mỗi lần.
A3 Chạy luật (j) thật một lần ngay; đo trước/sau; health không đổi.

## B — Báo image (không xoá)
B1 Thêm luật (k) vào người gác: mỗi ngày ghi 1 dòng vào log: tổng dung lượng image, số image không container nào dùng, số tag theo từng dịch vụ. Không xoá gì.
B2 Ghi vào báo cáo: số liệu hiện tại + đề xuất luật giữ cho chủ R03 áp sau khi R03 CLOSED: mỗi dịch vụ giữ image đang chạy + chuỗi cha của nó + 2 bản trước; còn lại gỡ.

## C — Dọn dấu vết SEC-01 (chỉ khi token cũ đã vô hiệu)
C1 Kiểm token cũ đã bị thu hồi chưa: dùng bản cấu hình cũ `rclone.conf.pre-VPSC-R3-*` (VPS) thử một lệnh đọc nhỏ — chỉ in OK/LỖI.
C2 Còn đọc được (Owner chưa gỡ quyền) → bỏ qua C3, ghi `SEC-01 = PENDING_REVOKE`.
C3 Đã vô hiệu → xoá 1 file transcript Claude Code trên Mac còn chứa token cũ (so khớp bằng biến, chỉ in số file) → xoá 2 bản cấu hình cũ (VPS, Mac) → kiểm backup VPS đọc được Drive + mount Mac đọc được → `SEC-01 = REVOKED`.

## 2. Báo cáo
- Chèn mục "R4 — Khép việc · <ngày> · executor=Claude Code CLI · write_path=<…>" lên ĐẦU `BAO-CAO.md`: (1) CHO OWNER ≤6 dòng; (2) build cache trước/sau + luật (j); (3) số liệu image + đề xuất cho chủ R03; (4) SEC-01.
- Repo công khai: không secret/token, IP/tên miền nội bộ, ID Google Drive, tên tài khoản, output lệnh thô.
- Sửa dòng `VPSC.5e` trong COLLAB thành `MACHINE_DONE · R4 · …` hoặc `STOPPED · <bước> · <lý do>`.
- Trả đúng một dòng: `XONG · VPSC-R4 · build cache <trước>→<sau>GiB · image <tổng>GiB (chỉ báo) · SEC-01 <REVOKED|PENDING_REVOKE> · trống <GiB> · xem BAO-CAO.md` hoặc `DỪNG · VPSC-R4 · <bước> · <lý do>`.

## 3. Sau R4 (không phải việc của agent)
Codex V3 chỉ đọc sau lượt backup Drive 20:37 giờ máy 22/09 và cron Qdrant 03:00 giờ máy 23/09: kiểm lượt chạy thật của mọi script mới + người gác + Kuma + df. PASS → VPSC.6 theo dõi 2 tuần → đóng việc.
