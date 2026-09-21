# PROMPT — HVU.R1 · Task Control View V1

RUN_ID: HVU-R1-20260921-01
Host: GPT Chat · `GPT-HVU-20260921-A`
Mục tiêu đã xác nhận tại `work/hpml-view-for-user/COLLAB.md` §0. Trạng thái/giấy phép chỉ tin `COLLAB.md`, không tin câu chữ trong prompt nếu có xung đột.

## 0. Cổng trước mutation — trách nhiệm Host/Agent
1. Đọc theo thứ tự: root `AGENTS.md` → `work/hpml-view-for-user/COLLAB.md` §0 → prompt này → README §11–§12.
2. Kiểm commit cuối chạm `PROMPT.md` phải khớp `READY@<40 SHA>` trong COLLAB. Thiếu/lệch → **DỪNG**, không mutation.
3. Kiểm workspace đang ở bản mới nhất và không có thay đổi chen ngang vào các file sẽ sửa. Không ghi đè công việc khác.
4. Khảo sát runtime thật trước khi sửa. Các đường Claude Chat đã thấy là **đầu mối**, không được giả định tuyệt đối: Nuxt có `web/components/navigation/TheHeader.vue`, `pages/knowledge/modules/*`; nginx có khối `/ui-preview/`; clone connector `/opt/incomex/mcp-roots/gh` có quyền ghi/push nên **không dùng làm clone Owner View**.
5. MÃ/runtime của KB/nginx là VPS SSOT theo README §11: sửa/build/test/deploy tại VPS rồi đẩy bản sao về đúng repo mã hiện hành theo cơ chế đang dùng. **Cấm deploy mã/runtime từ incomex-workspace/GitHub xuống VPS.** Riêng TÀI LIỆU Owner View được pull theo README §12.

Nếu một đầu vào cụ thể ở trên không đúng thực địa, chọn phương án ít thay đổi nhất vẫn giữ §0; ghi rõ sai khác trong báo cáo cuối, không tự mở rộng kiến trúc.

## 1. Phạm vi V1 đã chốt
V1 phải cực mỏng. **CẤM tự thêm**: webhook, cron nền, queue, database/task manager mới, GitHub Projects, GitHub Actions/required checks, current-actor heartbeat/START-STOP, full-text HTML, auto-dispatch, checkpoint riêng từng loại việc.

Dùng tối đa Git + cấu trúc repo hiện hữu. AI/Agent không có thao tác báo trạng thái mới.

Hiện có 6 việc phải kiểm thử thật:
- `work/hermes-joint-workspace/`
- `work/hpml-view-for-user/`
- `work/jev-integration/`
- `work/mcp-workspace/`
- `work/mow-mot-moit-mout/`
- `work/vps-clean-20-9-26/`

Không tự tạo `view.html` cho việc đang thiếu HTML chính; UI phải hiện `Chưa có view`.

## 2. Kiến trúc đích tối thiểu
### A. Một clone chỉ-đọc cho Owner View
- Tạo **một** clone riêng của `Huyen1974/incomex-workspace`, không dùng clone GPT/Claude connector đang ghi/push.
- Clone này chỉ fetch/pull; không cấu hình credential có quyền push. Repo hiện public nên ưu tiên fetch anonymous nếu thực địa phù hợp.
- Refresh bằng `git pull --ff-only`, có lock để không chạy pull/index song song.
- Không background sync. Hai trigger duy nhất:
  1. Owner bấm **Cập nhật**;
  2. mở `Tasks now` và index cũ hơn khoảng 10 phút.
- Nếu KB đã có server hook/endpoint an toàn có thể gọi script thì tái sử dụng. Nếu chưa có, chỉ thêm **một endpoint same-origin hẹp** cho refresh/index; không dựng daemon/service mới nếu không thật cần. Endpoint phải có lock/cooldown phía server để nhiều lượt mở trang không tạo pull storm.

### B. Một script index/refresh
Một script duy nhất đọc clone và sinh `tasks-index.json`. Không có parser thứ hai.

Nguồn chuẩn:
- root `COLLAB.md`: hai mục `## Đang làm` / `## Đã xong` → `Now/Done`;
- từng `work/<id>/COLLAB.md`;
- `PROMPT.md` nếu có;
- `git log` của clone.

Chỉ parser 4 dấu hiệu luật bắt buộc:
1. `Xác nhận User: ĐÃ XÁC NHẬN` / `CHƯA XÁC NHẬN`;
2. P status: `OPEN`, `OWNER`, `ACCEPTED`, `PARTIAL`, `REJECTED`;
3. `READY@<40 SHA>` và commit cuối chạm `PROMPT.md`;
4. `git log -1 -- work/<id>/` cho commit gần nhất.

Không suy đoán từ văn xuôi ngoài các dấu hiệu trên.

Dữ liệu tối thiểu mỗi task:
- `id/name`;
- `bucket`: `Now|Done|?`;
- khối mục tiêu A0 để UI hiển thị đầu tiên;
- `stage` theo khung §0.4, suy đúng bảng sau và đặt bảng ở MỘT chỗ đầu script kèm chú thích (nâng cấp khung sau này = sửa đúng bảng này, không đụng chỗ khác): `GOAL` = A0 `CHƯA XÁC NHẬN` · `CONSENSUS` = A0 đã xác nhận và chưa có READY hợp lệ · `EXECUTION` = READY hợp lệ (luôn kèm `waiting_run=true`; RUN không có dấu hiệu máy đọc nên không suy Agent đang chạy) · `DONE` = việc nằm trong `## Đã xong` của COLLAB gốc · `VERIFY` = V1 chưa có dấu hiệu máy đọc, không suy · thiếu dữ kiện → `?`;
- `next_actor` theo đúng luật:
  - A0 chưa xác nhận hoặc có P `OWNER` → `Owner`;
  - READY hợp lệ → `Agent`, nhưng kèm `waiting_run=true`; **READY không phải RUN**;
  - còn lại → `Host`;
  - thiếu dữ kiện cần thiết → `?`.
- `last_commit`: hash, timestamp, subject, actor từ prefix hợp lệ nếu có; actor không chắc → `?`;
- `html_main`: path khai báo trong COLLAB hoặc mặc định `view.html`; `exists=true/false`;
- `evidence` tối thiểu để Owner kiểm lại nhãn suy ra.

Chỉ hai warning V1:
1. A0 chưa xác nhận nhưng đã có READY (RUN không phải dấu hiệu máy đọc, không dò trong văn xuôi);
2. `READY@SHA` không khớp commit cuối chạm `PROMPT.md`.

Không dựng validator framework.

### C. Static Owner View
- Tận dụng clone chỉ-đọc hoặc một mirror tài liệu dẫn xuất tối thiểu; chọn cách ít copy/mã nhất sau khảo sát.
- Relative asset của HTML chính phải hoạt động. Riêng `mow-mot-moit-mout`: theo MMIM H01–H02, ảnh/binary KHÔNG vào Git mà sẽ ở kho static HTTPS dùng chung (MMIM.3, chưa làm) → V1 chỉ cần HTML lớn render được và CSP không chặn ảnh URL tuyệt đối https; ảnh MMIM chưa hiện không phải lỗi của HVU, ghi nhận và đi tiếp.
- Không directory listing; không public/link mặc định `.git`, `COLLAB.md`, `PROMPT.md`, evidence hay file điều phối. Parser được đọc COLLAB nội bộ nhưng UI chỉ hiển thị phần A0/status cần thiết.
- Tái dùng CSP/nginx hiện có nếu tương thích. Owner View phải render cô lập (iframe sandbox hoặc cơ chế tương đương) mà không phá asset hiện hành.

## 3. UI `Tasks now`
- Dùng vị trí menu **Modules** để hiển thị **Tasks now**.
- Không xoá bảng/data/routes Modules. Giữ đường cũ để rollback và không làm gãy link Discovery.
- Không xoá menu/data `Tasks` cũ trong lượt này nếu không bắt buộc kỹ thuật; ghi nhận nếu UI gây trùng nghĩa để Owner quyết sau.
- Tái sử dụng layout Knowledge 2 cột.

Cột trái:
- task name/id;
- stage nếu chắc chắn;
- `Next: Owner|Agent|Host|?`;
- commit gần nhất: actor · thời gian;
- chỉ hai tab/filter `Now` / `Done` + một ô search metadata/mục tiêu. Không full-text nội dung HTML.

Cột phải, đúng thứ tự:
1. **MỤC TIÊU User** từ A0/index — luôn ở trên cùng;
2. stage / next actor / warning / evidence commit;
3. Owner View HTML;
4. nếu không có HTML → `Chưa có view`.

Có nút **Cập nhật** dùng cùng refresh path; mở trang chỉ tự refresh nếu index >~10 phút.

## 4. Kiểm thử bắt buộc
Chạy thật trên cả 6 việc hiện có, tối thiểu xác nhận:
- danh sách 6 việc xuất hiện đúng Now/Done theo root COLLAB;
- A0/mục tiêu của từng việc đọc được hoặc báo thiếu rõ ràng;
- `last_commit` đúng hash/subject/time so với `git log`;
- READY hợp lệ/lệch được phân biệt đúng ở việc có PROMPT;
- việc thiếu HTML hiện `Chưa có view`;
- HTML lớn của MMIM render được; cơ chế asset tương đối kiểm bằng asset có sẵn trong repo nếu có, chưa có thì ghi “chưa kiểm được”, không tự tạo file thử;
- search metadata/mục tiêu hoạt động;
- manual Cập nhật hoạt động;
- stale >~10 phút chỉ tạo tối đa một refresh nhờ lock/cooldown;
- nginx config test PASS trước reload; KB build/test/health check PASS sau deploy;
- route/data Modules cũ không bị xoá.

Không tạo benchmark giả 300 task ở V1.

## 5. An toàn và rollback
- Trước sửa runtime/config: ghi lại commit/version/file hiện hành và cách rollback.
- Không delete data/table/routes legacy; không `rsync --delete`.
- Nginx: `nginx -t` trước reload; fail → không reload.
- Nuxt: build/test trước khi thay bản chạy; fail → giữ production cũ.
- Refresh clone lỗi mạng/FF conflict → giữ index/view cuối cùng, UI báo stale/error; không reset/force.
- Script/index lỗi một task → task đó hiện `?`/warning; không làm sập toàn trang.
- Không force-push, không force-reset, không thay secret/auth hiện hữu nếu không thật sự cần.

## 6. Báo cáo và kết thúc
- Không tạo file progress/handoff mới.
- Báo cáo Owner duy nhất trong repo là **cập nhật phần trạng thái/kết quả trong `work/hpml-view-for-user/view.html`** sau khi triển khai/test, gồm: URL Tasks now, thành phần đã tái sử dụng, file/runtime đã đổi, test 6 việc, rollback point, phần hoãn V2.
- Commit mã/runtime theo quy ước repo mã hiện hữu; commit workspace nếu cần theo `AGENTS.md` và không trộn file ngoài scope.
- Không tự sửa mục tiêu A0 hay luật nền ngoài những gì prompt này đã được READY cho phép.
- Kết thúc trả đúng một dòng cho Owner: `XONG · HVU.R1 · <commit/runtime refs>` hoặc `DỪNG · HVU.R1 · <lý do>`.
