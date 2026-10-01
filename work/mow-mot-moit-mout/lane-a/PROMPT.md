# PROMPT — LANE A09 · Sửa lỗi Owner View tự reload / nhảy tab

RUN_ID: MMIM-LANE-A09-20261001-01
PROCESS: CHUNG.APQUYTRINH
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex

## 0. Mục tiêu
Fix triệt để lỗi Owner View:
- đang ở tab con như `★ Công thức` thỉnh thoảng tự nhảy về `UI Master`;
- có cảm giác document/iframe reload khi revision chung đổi;
- giảm remount/tải lại không cần thiết nhưng vẫn nhận tài liệu mới thật.

Không sửa nội dung nghiệp vụ `ban-duyet.html` trong RUN này.

## 1. Nguồn SSOT / authority phải đọc trước
A08 đã tìm được pointer nhưng ChatGPT connector không có quyền đọc VPS source.
Dùng **đúng quyền VPS đã được Owner cấp sẵn**, không xin/đoán secret mới.

Bắt buộc đọc tại VPS:
- `/opt/incomex/docker/nuxt-repo/scripts/hvu-b2/README.md`
- `/opt/incomex/docker/nuxt-repo/scripts/hvu-b2/ui/app.vue`
- `ui/nuxt.config.ts`
- `ui/pack.mjs`
- source publisher/sync liên quan `documentPath/documentRevision/tasksPath/publishedRevision`
- mapping/deploy đang phục vụ `/ui-preview/hpml-view-for-user/view.html`

Trước write ghi:
- repo/path;
- branch/HEAD;
- dirty state;
- SHA/hash từng file sẽ sửa;
- lệnh build/deploy từ README.

Nếu source/repo dirty bởi thay đổi không thuộc RUN hoặc authority không rõ → DỪNG, không vá mù.

## 2. Bằng chứng đã có
A07 PROVEN:
- `publishedRevision` có thể đổi vì commit không liên quan;
- document HTML của task hiện tại có thể byte-identical;
- Owner View vẫn remount iframe → state/details/tab bị mất.

A08 runtime live xác nhận logic:
- poll sync-status khoảng 60s;
- update tasks theo publishedRevision;
- document src/key thay theo snapshot path/revision;
- source mirror trong incomex-workspace chỉ tham khảo, KHÔNG deploy.

## 3. Yêu cầu thiết kế patch
Tách **metadata revision** khỏi **loaded document identity**.

### Luật bắt buộc
1. `publishedRevision` đổi **không đủ** để remount document.
2. Chỉ thay iframe/document khi tài liệu của **task đang chọn** thực sự đổi.
3. Ưu tiên identity đã có trong data contract như `documentRevision` / content hash.
4. Nếu data contract hiện không có identity ổn định cho bytes document:
   - bổ sung fingerprint/hash tối thiểu tại publisher;
   - không dùng mtime/global HEAD làm proxy.
5. Khi tài liệu thật đổi:
   - reload đúng một lần;
   - giữ task đang chọn;
   - giữ section/tab con hiện tại, ví dụ `matrix-view-formula`;
   - không rơi về `matrix-view-master`.
6. Back/Forward/deep-link vẫn hoạt động.
7. Poll status/presence vẫn hoạt động; không tắt cơ chế cập nhật để “hết reload”.

## 4. Ca test bắt buộc
### T1 · unrelated revision
- đang mở task `mow-mot-moit-mout` + section `matrix-view-formula`;
- publishedRevision đổi vì một task/file khác;
- document content identity của MOW không đổi;
- PASS khi iframe DOM không remount, tab vẫn Công thức, scroll/details/filter state không mất.

### T2 · real document change
- MOW document identity đổi thật;
- PASS khi document cập nhật đúng một lần và vẫn vào section đang chọn.

### T3 · navigation
- click các tab con;
- Back / Forward;
- deep-link section;
- reload chủ động;
- không tự nhảy về UI Master ngoài trường hợp URL thật yêu cầu master.

### T4 · load
- không tăng số request/poll ngoài baseline;
- không tạo vòng reload;
- không làm trắng document khi sync lỗi/stale.

## 5. Build / deploy / rollback
Theo README runtime:
`nuxt generate → node pack.mjs → .output/public/view.html → deploy mirror/runtime`
(chỉ dùng lệnh thực tế trong README hiện hành, không tin dòng này nếu source đã đổi).

Trước deploy giữ backup/hash last-good.
Sau deploy kiểm:
- live buildId/hash;
- Owner URL thật;
- console functional errors;
- rollback command/path.

Không push GitHub trực tiếp nếu runtime governance không cho phép.

## 6. KQ
Ghi vào `work/mow-mot-moit-mout/lane-a/COLLAB.md` qua cổng workspace đã duyệt:
`KQ@MMIM-LANE-A09-20261001-01 XONG|DỪNG`
`KQ@LANE-A A09 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS|BLOCK · source=FOUND|BLOCKED · unrelated_remount=PASS|BLOCK · real_change=PASS|BLOCK · section_preserved=PASS|BLOCK · NEXT=<one thing>`

Kèm:
- source HEAD/hash;
- files sửa;
- build/deploy hash;
- before/after evidence;
- rollback.

Dừng.
