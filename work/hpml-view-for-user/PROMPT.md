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

## 2. Việc 1 — Dời bản xem sai chỗ vào archive
Claude trước đó tự tạo sai file:
- root runtime/UI: `ui:mow-mot-moit-mout.html`
- file tương ứng: `mow-mot-moit-mout.html` trong root `ui`

Không có delete tool trong các đường ghi đã audit. Owner cho phép **gỡ đúng bản sai này khỏi nơi đang phục vụ**; thực hiện bằng move có kiểm soát, không xoá.

Trình tự:
1. `fs_stat` + hash/path;
2. xác nhận đây là file ngoài §12 do incident 23/09 tạo, **không phải HTML chuẩn trong incomex-workspace**;
3. dùng `fs_move` dời đúng file đó vào:
   `ui:archive/2026-09-23-ban-xem-sai-cho/mow-mot-moit-mout.html`
4. trong cùng thư mục archive, tạo/cập nhật `INDEX.md` một dòng: `Bản ngoài §12 · không dùng · nguồn chuẩn = work/mow-mot-moit-mout/mow-mot-moit-mout.html`;
5. nếu file đã không còn: ghi `ALREADY_ABSENT`, không tạo lại.

Cấm move/xoá file khác. Cấm chạm HTML chuẩn:
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

## 4. Việc 3 — Whitelist hành động được tự làm trong RUN này
Agent chỉ được tự làm ngay các việc sau:
1. đọc log/trạng thái/config hiện hữu của pipeline §12;
2. chạy lại **một** lượt sync/publisher bằng cơ chế hiện hữu;
3. nếu pipeline đã có lệnh/cơ chế an toàn để rebuild/repair **dữ liệu dẫn xuất** (`data/tasks.json`, `data/documents/`, snapshot/cache) mà **không sửa code, không đổi service, không đổi auth**, được chạy đúng cơ chế đó một lượt;
4. dời file sai vào archive theo §2.

Không được vá tay `tasks.json`/document snapshot để che parser/code bug; dữ liệu dẫn xuất phải sinh lại từ cơ chế chuẩn.

**Ngoài whitelist trên phải DỪNG và xin Owner.** Cụ thể, nếu root cause cần bất kỳ việc nào sau thì không tự làm:
- sửa mã runtime;
- build/rebuild ứng dụng;
- restart/reload/stop service;
- sửa nginx/compose/systemd;
- nới/tắt auth;
- thay schema/pipeline hoặc tạo endpoint/path mới.

Khi DỪNG phải báo: root cause + file/service dự kiến phải sửa + thay đổi tối thiểu đề xuất + rủi ro/rollback. Chỉ sau Owner gật mới mở lượt sửa production riêng.

Giữ nguyên: không GitHub → VPS cho mã/runtime; không sửa MMIM để né lỗi viewer; không tạo pipeline thứ hai.

## 5. Nghiệm thu bắt buộc
Chỉ được ghi XONG nếu đủ:
1. file sai `ui:mow-mot-moit-mout.html` đã được **ARCHIVED** theo §2 hoặc `ALREADY_ABSENT`; đường cũ không còn phục vụ bản đó;
2. không có pipeline/bản xem thứ hai;
3. canonical pipeline §12 publish được task `mow-mot-moit-mout`;
4. snapshot revision = revision cần publish mới nhất tại thời điểm test;
5. snapshot chứa đúng HTML chính + hash đối chiếu được với Git/workspace;
6. **Nghiệm thu máy không cần đăng nhập:** đọc đúng artifact mà viewer hiện hành đang tiêu thụ — `data/tasks.json` + file tương ứng trong `data/documents/` (resolve absolute path từ runtime/config hiện hữu, không tự invent path). Kiểm task-id, bucket Now, main HTML path, `sourceRevision`/revision publish và SHA-256 HTML khớp Git/workspace. Nếu runtime đã có endpoint localhost nội bộ phục vụ chính snapshot này thì được dùng thêm; **không tạo endpoint mới**. Canonical URL để Owner mở mắt kiểm cuối là:
   `https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout`
   Agent không được claim đã mở qua browser nếu không có session auth; việc Owner nhìn thấy là xác nhận người dùng cuối, không phải lý do nới auth hay tạo đường tạm;
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
`XONG · HVU-OWNERVIEW01 · root_cause=<ngắn> · wrong_view=ARCHIVED|ALREADY_ABSENT · snapshot_rev=<sha> · snapshot_hash=<sha256> · owner_view=https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout`

Hoặc:
`DỪNG · HVU-OWNERVIEW01 · <lý do cụ thể>`
