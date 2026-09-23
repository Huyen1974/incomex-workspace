# PROMPT — HVU-OWNERVIEW01 · Khôi phục đúng Owner View §12

RUN_ID: HVU-OWNERVIEW01-20260923-01

## 0. Gate bắt buộc
- Executor_Surface: **Claude Code CLI**.
- Đọc: `AGENTS.md` → `README.md` §11–§12 → `work/hpml-view-for-user/COLLAB.md` → prompt này.
- Runtime/mã trên VPS là SSOT. **Cấm GitHub → VPS** cho mã/runtime.
- Chỉ dùng capability/runtime path đã audit. Không tự tạo task mới, URL mới, bản xem mới hay pipeline mới.
- READY phải là commit cuối chạm `PROMPT.md`.
- Review/consensus đầu vào đã có tại incident `bd1551b`: đúng 3 việc dưới đây, không mở rộng.

## 1. Mục tiêu
Khôi phục đúng **một** đường Owner View theo README §12 cho task:

`https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout`

Kết quả cuối phải là link trên mở đúng HTML chính của task ở revision mới nhất đã publish qua pipeline §12. Không chấp nhận đường xem tạm.

## 2. Việc 1 — Gỡ đúng bản xem sai chỗ
Claude trước đó tự tạo sai file:
- root runtime/UI: `ui:mow-mot-moit-mout.html`
- file tương ứng: `mow-mot-moit-mout.html` trong root `ui`

Owner đã cho phép xoá **đúng file sai này**.

Trước xoá:
1. `fs_stat` + hash/path;
2. xác nhận đây là file ngoài §12 do incident 23/09 tạo, **không phải HTML chuẩn trong incomex-workspace**;
3. nếu file đã không còn: ghi `ALREADY_ABSENT`, không tạo lại.

Cấm xoá file khác. Cấm chạm HTML chuẩn:
`work/mow-mot-moit-mout/mow-mot-moit-mout.html`.

## 3. Việc 2 — Truy nguyên pipeline §12 cho đúng task
Không sửa trước khi xác định nguyên nhân.

Kiểm theo đúng chuỗi duy nhất:
1. Git/workspace hiện có task `work/mow-mot-moit-mout/`;
2. COLLAB khai HTML chính là `mow-mot-moit-mout.html`;
3. revision Git/main hiện hành;
4. webhook/backstop có ghi nhận revision mới không;
5. snapshot publisher có phát hiện task không;
6. `tasks.json`/snapshot có record task, đúng bucket Now và đúng main HTML path không;
7. snapshot đã copy HTML chính chưa, hash/revision nào;
8. Task view có đọc đúng snapshot đó không;
9. xác định vì sao các lượt FIELD01–FIELD03 đều bị `VIEW_PENDING_REVISION`;
10. xác định việc “đòi đăng nhập” là hành vi bảo vệ đúng hay regression. **Không được tắt/nới auth chỉ để pass test.**

Ghi một kết luận root cause duy nhất, có evidence path/log/revision.

## 4. Việc 3 — Sửa đúng nơi quy định
Nếu lỗi nằm ở mã/runtime Owner View:
- sửa **trực tiếp trên VPS** trong mã runtime của `hpml-view-for-user` theo README §11;
- build/test tại chỗ;
- backup/rollback theo cơ chế hiện hữu;
- chỉ restart/reload service thực sự cần;
- không kéo mã từ GitHub xuống VPS;
- không sửa MMIM để “né” lỗi viewer;
- không tạo endpoint/path/pipeline thứ hai.

Nếu lỗi chỉ là dữ liệu/snapshot/scheduler:
- sửa đúng component đó trong pipeline §12;
- không redesign, không mở scope deep-link;
- giữ webhook + backstop 15′ + last-good + atomic publish hiện có.

Nếu runtime code thay đổi, ghi rõ file runtime đã sửa và cách backup/mirror VPS→Git theo quy trình hiện hữu; **không tự phát minh quy trình mirror mới**.

## 5. Nghiệm thu bắt buộc
Chỉ được ghi XONG nếu đủ:
1. file sai `ui:mow-mot-moit-mout.html` đã gỡ hoặc `ALREADY_ABSENT`;
2. không có pipeline/bản xem thứ hai;
3. canonical pipeline §12 publish được task `mow-mot-moit-mout`;
4. snapshot revision = revision cần publish mới nhất tại thời điểm test;
5. snapshot chứa đúng HTML chính + hash đối chiếu được với Git/workspace;
6. canonical URL:
   `https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout`
   mở đúng task và HTML chính;
7. nút `Cập nhật` chỉ reload snapshot, không tạo/publish bằng đường khác;
8. auth giữ đúng chính sách hiện hữu; không nới auth;
9. regression tối thiểu: Tasks Now/Done + một task khác vẫn mở bình thường;
10. không chạm MCP/connector, MMIM content, sync/presence ngoài nguyên nhân gốc;
11. COLLAB ghi root cause + before/after revision/hash + canonical Owner View link;
12. ghi:
   `KQ@HVU-OWNERVIEW01-20260923-01 XONG`.

Nếu canonical Owner View chưa hiển thị đúng revision/HTML:
- ghi `KQ@HVU-OWNERVIEW01-20260923-01 DỪNG`;
- báo root cause/evidence;
- **không** dùng `PENDING` như PASS;
- **không** dựng URL/file tạm thay thế.

## 6. Báo cáo
XONG:
`XONG · HVU-OWNERVIEW01 · root_cause=<ngắn> · wrong_view=REMOVED|ALREADY_ABSENT · snapshot_rev=<sha> · owner_view=https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout`

Hoặc:
`DỪNG · HVU-OWNERVIEW01 · <lý do cụ thể>`
