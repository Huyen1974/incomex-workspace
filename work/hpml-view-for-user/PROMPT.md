# PROMPT — HVU.ARCHIVE01 · RUN done-tasks archive

RUN_ID: HVU-ARCHIVE01-RUN-20260922-01
Host: GPT Chat
Reviewer: Claude Chat · P24 ACCEPT
Executor_Surface: Codex/GPT Work
Write_Path: runtime VPS theo README §11 + workspace MCP cho Git docs/move

## 0. Gate trước mutation
1. Đọc AGENTS.md → root COLLAB.md → work/hpml-view-for-user/COLLAB.md → PROMPT này → README §11–§12.
2. Commit cuối chạm PROMPT phải khớp READY trong COLLAB; lệch → DỪNG.
3. P23 + P24 + Host P25 là consensus bắt buộc. Không redesign B2/B3 ngoài archive scope.
4. Baseline trước sửa: source HEAD, sync-status/tasks.json, số task/bucket, document URLs, retention=3, webhook/backstop health, B3 presence, runtime commits + rollback point.
5. Không đổi hai gateway/MCP schema/version/auth. Không restart gateway; P24 yêu cầu guard ở publisher/presence layer.

## 1. Contract mới đã đồng thuận
Một nguồn trạng thái duy nhất = vị trí folder:
- `work/<task-id>/` = **Now / Đang làm**.
- `work/done-tasks/<task-id>/` = **Done / Đã xong**.
- `done-tasks` là reserved container, không bao giờ là task-id.
- GitHub/workspace là SSOT. VPS source clone tự phản ánh Git; không có lệnh move riêng bên VPS.
- Owner View tìm/xem được cả Now và Done. Public document/cache URL tiếp tục key theo `task-id`, không theo source folder, để move không gãy link.
- Root `## Đã xong` sau migration không còn là state source; chỉ để đúng một dòng chỉ sang `work/done-tasks/`.

## 2. B2 sync.py — bắt buộc sửa đủ các hard-code P24
### 2.1 Discovery
Không recursive scan.
- Now: đúng regex một tầng `work/[^/]+/COLLAB.md`, nhưng loại `work/done-tasks/COLLAB.md`/reserved container.
- Done: đúng regex một tầng `work/done-tasks/[^/]+/COLLAB.md`.
- Discovery phải trả record tối thiểu `{id, folder, bucket}`; mọi bước sau dùng `folder`, không dựng lại `'work/'+task_id+'/'`.
- Nếu cùng task-id xuất hiện ở cả Now và Done: **Now thắng + warning**, không fail toàn publish.

### 2.2 Ba chỗ hard-code đã nêu ở P24
Rà mã thật và sửa mọi chỗ tương đương, tối thiểu:
- build/parser đang dựng `work/<id>/...`;
- `copy_document`/HTML/asset path;
- loại trừ app HVU.
Không patch theo số dòng cứng; patch theo semantics để source hiện hành có thể lệch dòng.

### 2.3 HTML chính / document copy
- `HTML chính` có thể là tên file tương đối hoặc path đầy đủ ở cả hai vùng.
- Normalize/strip đúng prefix task folder thật; không giả định prefix `work/<id>/`.
- Public output vẫn `documents/<task-id>/...`.
- Done task phải giữ HTML/assets/history như trước move.

### 2.4 HVU app exclusion
Không dùng hằng path `work/hpml-view-for-user/view.html`.
Nhận diện app runtime theo **task-id == hpml-view-for-user AND filename == view.html** (hoặc semantic tương đương độc lập bucket).
Khi HVU vào Done, app không được copy nhầm thành document.

### 2.5 Bucket / root legacy
- `bucket=Now|Done` lấy từ folder.
- Bỏ root `## Đã xong` khỏi logic state.
- READY/KQ/A0/parser dùng COLLAB/PROMPT ở `folder` hiện tại.
- READY hợp lệ = SHA trùng commit cuối chạm PROMPT tại path hiện tại.
- Move archive/reopen chạm PROMPT → READY cũ tự invalid, không thêm heuristic.

## 3. Presence publisher — guard archive, KHÔNG đụng gateway
P24 đã xác nhận gateway parse `work/done-tasks/X` thành work_id `done-tasks`; không sửa gateway vì frozen.

Sửa lớp `presence.py`/publisher:
- chỉ xuất active entry nếu `work_id` tồn tại trong `tasks.json` **và bucket=Now**;
- do đó tự loại `done-tasks`, Done task, id lạ;
- Done task luôn `Đang làm = null`;
- `Vừa làm` Done vẫn đọc từ Git commit của **folder thật** để có thể hiện người vừa đóng.
- Reopen về `work/<id>` thì future activity lại hiện bình thường.
Giữ latest-only/no-resurrection semantics hiện hành.

## 4. UI
Tái dùng UI hiện tại:
- Search phải tìm xuyên cả Now + Done.
- Danh sách/master list giữ cả hai; xếp Now trước, Done sau hoặc nhóm rõ ràng bằng nhãn hiện có.
- Không tạo page/database/archive UI mới.
- Bấm task Done vẫn mở đúng detail/document URL theo task-id.
- Không thay actor naming/presence semantics.

## 5. A9 / README / root rules — chỉ cập nhật sau cutover thành công
Sau khi runtime hỗ trợ archive và pilot PASS:
- A9/README: discovery = hai glob tường minh; `done-tasks` reserved; Done = folder location.
- Root DROOT07/luật liên quan: bỏ “root Đã xong đánh dấu Done”; thêm quyết định archive folder-state.
- Root `## Đã xong`: không duy trì danh sách task; để đúng một dòng hướng dẫn kiểu:
  `- Archive: work/done-tasks/ · vị trí folder là trạng thái Done.`
- Không dùng root Done list làm fallback lâu dài.

## 6. Thứ tự triển khai bắt buộc — không để trạng thái sai tạm thời
### Phase A · Test candidate trước production
- Unit/regression với fixture đủ:
  1. active task bình thường;
  2. done task có PROMPT + HTML + asset;
  3. duplicate id Now+Done → Now thắng + warning;
  4. HVU active/done không copy app thành document;
  5. READY current-path;
  6. presence done-tasks/id-lạ bị lọc; Now latest-only vẫn đúng;
  7. public URL task-id ổn định qua move;
  8. retention/last-good/webhook regressions.
- Synthetic move chỉ trong temp clone/fixture, không main.

### Phase B · Deploy runtime support TRƯỚC move
- Deploy sync/presence/UI patch với rollback.
- Vì workspace Git HEAD chưa đổi, **không ép rebuild/publish dữ liệu theo logic mới**; backstop HEAD-unchanged phải no-op như thiết kế.
- Health/nginx/unit/regression PASS. Nếu runtime lỗi → rollback, DỪNG; chưa move task nào.

### Phase C · Pilot migration thật
Trong **một Git commit/mutation logic thống nhất**:
- move `work/mcp-workspace/` → `work/done-tasks/mcp-workspace/`;
- cập nhật root `## Đã xong` sang pointer archive và cập nhật A9/README/root decisions cần thiết.
Webhook bằng runtime mới phải publish:
- mcp-workspace bucket Done;
- task-id giữ `mcp-workspace`;
- document/history nếu có không mất;
- không có active presence;
- search tìm được và detail mở được;
- các task còn lại giữ bucket/trạng thái đúng.
Nếu pilot fail → rollback **cả runtime và Git move theo forward restore**, DỪNG.

### Phase D · Đóng chính HVU làm acceptance thật
Chỉ sau pilot PASS:
1. ghi báo cáo + `KQ@HVU-ARCHIVE01-RUN-20260922-01 XONG` vào COLLAB khi HVU còn ở active folder;
2. commit/push báo cáo;
3. final Git move nguyên `work/hpml-view-for-user/` → `work/done-tasks/hpml-view-for-user/`.
Webhook phải cho thấy:
- HVU bucket Done;
- URL/detail vẫn mở;
- app runtime vẫn phục vụ;
- HVU Done có `Đang làm=null`;
- `Vừa làm` là actor của move/close theo Git author;
- root không còn task-list Done song song.

Sau final move không sửa thêm nội dung HVU trừ khi rollback.

## 7. Reopen acceptance
Không cần reopen HVU production chỉ để test.
Dùng fixture/temp clone để chứng minh:
- move Done A → Now A giữ task-id/history;
- READY cũ mismatch path-current commit → không tự cấp phép RUN;
- activity sau reopen được publisher cho hiện lại.
Nếu có một task thật cần reopen trong quá trình làm thì dùng làm bằng chứng thay fixture.

## 8. Acceptance bắt buộc
- B2/B2.1 regression + webhook/backstop/last-good/retention=3 PASS.
- Không mất HTML/assets của task Done.
- Search/master list thấy cả Now/Done.
- Link public key task-id ổn định qua move.
- No duplicate state source: folder là state; root Done list không còn.
- B3 gateway untouched; MCP contract/version/auth unchanged.
- Presence không xuất `done-tasks`; Done activeActors null.
- Current Now signals không regression.
- Git history preserved; không reset/rewrite.
- VPS source clone có đúng `work/done-tasks/<id>` sau fetch; không manual VPS move.
- Rollback script/evidence rõ.

## 9. Báo cáo
- Cập nhật chính COLLAB; không tạo progress file mới.
- Ghi runtime refs, Git move refs, tests, rollback.
- KQ:
  `KQ@HVU-ARCHIVE01-RUN-20260922-01 XONG|DỪNG`
- Trả đúng một dòng:
  `XONG · HVU.ARCHIVE01 · <refs>`
  hoặc
  `DỪNG · HVU.ARCHIVE01 · <lý do>`.
