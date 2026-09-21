# PROMPT — HVU.B2 · Đường ống dữ liệu tự đổ cho UI03

RUN_ID: HVU-B2-20260921-01
Host: GPT Chat · `GPT-HVU-20260921-A`
Mục tiêu đã xác nhận tại `work/hpml-view-for-user/COLLAB.md` §0. Trạng thái/giấy phép chỉ tin `COLLAB.md`, không tin câu chữ trong prompt nếu có xung đột.

## 0. Cổng trước mutation — trách nhiệm Host/Agent
1. Đọc theo thứ tự: root `AGENTS.md` → `work/hpml-view-for-user/COLLAB.md` §0 → prompt này → README §11–§12.
2. Kiểm commit cuối chạm `PROMPT.md` phải khớp `READY@<40 SHA>` trong COLLAB. Thiếu/lệch → **DỪNG**, không mutation.
3. Kiểm workspace đang ở bản mới nhất và không có thay đổi chen ngang vào các file sẽ sửa. Không ghi đè công việc khác.
4. Khảo sát runtime thật trước khi sửa. Các đường Claude Chat đã thấy là **đầu mối**, không được giả định tuyệt đối: Nuxt có `web/components/navigation/TheHeader.vue`, `pages/knowledge/modules/*`; nginx có khối `/ui-preview/`; clone connector `/opt/incomex/mcp-roots/gh` có quyền ghi/push nên **không dùng làm clone Owner View**.
5. MÃ/runtime của KB/nginx là VPS SSOT theo README §11: sửa/build/test/deploy tại VPS rồi đẩy bản sao về đúng repo mã hiện hành theo cơ chế đang dùng. **Cấm deploy mã/runtime từ incomex-workspace/GitHub xuống VPS.** Riêng TÀI LIỆU Owner View được pull theo README §12.

Nếu một đầu vào cụ thể ở trên không đúng thực địa, chọn phương án ít thay đổi nhất vẫn giữ §0; ghi rõ sai khác trong báo cáo cuối, không tự mở rộng kiến trúc.

## 1. Phạm vi B2 — chỉ đấu dữ liệu, không thiết kế lại UI
UI03 hiện đang chạy tại `/knowledge/modules`; coi layout/visual là **đã chốt cho lượt này**. B2 chỉ thay fixture hard-code bằng dữ liệu thật và thêm scheduler/snapshot.

**CẤM tự thêm:** webhook, database/task manager mới, GitHub Projects/Actions, full-text HTML, auto-dispatch, heartbeat/current actor, sửa cổng ghi Surface (đó là B3), hoặc redesign UI.

Mọi commit mới trên `main` đều là revision dữ liệu hợp lệ để mirror; không cần marker publish riêng. Chỉ DỮ LIỆU/tài liệu tự đổ. `view.html` app/KB/nginx/script/timer là runtime theo README §11 và phải sửa/deploy tại VPS rồi mirror mã theo quy trình runtime hiện hữu.

## 2. Đường ống tự đổ bắt buộc
### A. Nguồn và trigger
- Dùng **một clone chỉ-đọc riêng** của `Huyen1974/incomex-workspace`, ngoài web root và ngoài clone connector ghi/push. Không credential có quyền push; ưu tiên anonymous read nếu repo vẫn public.
- Tái dùng scheduler hiện hữu nếu phù hợp; nếu không có, thêm tối đa **một systemd oneshot + timer** cho B2. Mỗi 60 giây: lock → kiểm/fetch `origin/main` → nếu HEAD bằng revision đã xử lý thì thoát nhanh, không rebuild/copy documents → nếu HEAD mới thì dựng snapshot từ đúng HEAD đó.
- Nút **Cập nhật** trên UI không cần backend riêng ở B2: nó đọc lại snapshot/health ngay. UI đang mở tự poll dữ liệu khoảng 60 giây. Webhook để B4 nếu độ trễ này thực tế không đủ.

### B. Tự phát hiện task + parser
- Task discovery = mọi thư mục `work/*/` có `COLLAB.md`. Không phụ thuộc root `## Đang làm` để task mới xuất hiện.
- Root `## Đã xong` chỉ đánh dấu Done; task không nằm `Đã xong` mặc định bucket `Now`.
- Parse A0, P, READY, `RUN_ID`, `KQ@<RUN_ID>`, HTML chính đã khai báo/default và Git log. **Bảng trạng thái duy nhất là AGENTS A9**; script không tạo bảng luật thứ hai khác nghĩa.
- `KQ` chỉ tính khi RUN_ID khớp prompt hiện hành. READY/KQ cũ không được làm task Done đổi ngược trạng thái.
- `lastActors`: B2 chỉ dùng actor/surface có bằng chứng rõ trong COLLAB/commit prefix hiện hữu; không chắc → không sáng. `activeActors=null` ở B2. Không suy 6 surface từ Git author/pusher dùng chung.

### C. Snapshot/publication
Sinh dữ liệu dưới vùng static hiện hữu của `hpml-view-for-user`, tối thiểu:
- `data/tasks.json`: revision nguồn + danh sách task + goal nguyên A0 + 4 stages/currentStage + lastActors/activeActors + document URL/status + warnings/evidence cần cho UI.
- `data/sync-status.json`: `lastCheckedAt`, `lastSuccessAt`, `sourceRevision`, `publishedRevision`, `status=fresh|stale|error`, `consecutiveFailures`, lỗi đã sanitize.
- mirror HTML chính của từng task vào vùng documents; không public `.git`, `COLLAB.md`, `PROMPT.md`, evidence hay directory listing. Task thiếu HTML vẫn xuất hiện và UI ghi `Chưa có view`.

**Không được để mixed/half snapshot:** dùng staging + validate + publish nguyên tử hoặc cơ chế tương đương; tasks JSON/document references phải cùng revision logic. Không hạ revision nếu lượt cũ/trễ hoàn tất sau lượt mới.

### D. Lỗi và tự phục hồi
- Remote/fetch lỗi, parse lỗi toàn snapshot, copy/validate lỗi → **không thay last-good**; cập nhật health `error/stale` bằng ghi nguyên tử, tự retry ở phút kế tiếp.
- HEAD không đổi nhưng timer chạy thành công → được cập nhật `lastCheckedAt`/health nhỏ; không rebuild documents.
- Một task hỏng mà vẫn cô lập được → publish các task khác, task đó `unknown` + warning và giữ document last-good nếu có; không làm trắng dashboard.
- Nếu scheduler không chạy/health không đổi quá khoảng 3 phút → UI phải hiển thị `stale`; dữ liệu cũ vẫn xem được.
- Không force reset, không `rsync --delete` repo, không để lỗi mạng làm xoá document đang phục vụ.

## 3. Nối UI03 hiện có vào snapshot
Giữ nguyên UI03 (2 tab, sidebar, 4 thanh, 6 actor × 2 cột). Chỉ thay nguồn dữ liệu:
- bỏ mảng 6 task/mục tiêu/stage/snapshot/documents hard-code trong `ui-assembly/app.vue`;
- fetch snapshot + health static với cache-bust/no-cache phù hợp; poll khoảng 60 giây;
- task mới trong JSON tự xuất hiện, không cần sửa app;
- mục tiêu/stages/currentStage lấy từ JSON; không diễn giải lại bằng AI;
- tab Nội dung dùng `documentPath` của task; thiếu file → `Chưa có view`;
- `lastActors` thay nguyên snapshot mới, không cộng dồn; `activeActors` null/không tín hiệu thì xám;
- hiển thị badge nhỏ `fresh/stale/error` + revision/thời điểm khi cần để Owner biết dữ liệu có lạc hậu không;
- nút Cập nhật chỉ force refetch static JSON trong browser ở B2, không tạo endpoint ghi mới.

## 4. Kiểm thử bắt buộc
1. Production `/knowledge/modules` vẫn giữ UI03, nhưng không còn fixture hard-code; console không có lỗi mới do B2.
2. 6 task hiện có được tự discover; task thiếu HTML vẫn hiện. Danh sách không phụ thuộc root `Đang làm`.
3. A0 và 4 thanh của ít nhất các trạng thái khác nhau khớp AGENTS A9; `KQ` sai RUN_ID không được dùng.
4. HEAD không đổi: hai lượt timer liên tiếp không rebuild/copy documents; chứng minh bằng log/hash/mtime thích hợp.
5. Tạo một commit workspace vô hại/đã có thật sau mốc baseline rồi xác nhận trong ≤ khoảng 60–120 giây `sourceRevision`/mục tiêu hoặc metadata tương ứng cập nhật trên VPS mà không bấm tay.
6. UI đang mở tự nhận revision mới mà không reload toàn trang.
7. HTML lớn MMIM vẫn mở được; ảnh ngoài Git chưa có không chặn B2.
8. Failure test **chỉ trong môi trường/cấu hình cô lập hoặc cách an toàn không phá production**: sync lỗi phải giữ last-good; lượt sau thành công tự hồi phục. Không cố gây outage thật chỉ để test.
9. Nếu health không cập nhật >3 phút, UI hiển thị stale nhưng vẫn đọc được last-good.
10. `nginx -t`, build/test/health check PASS trước/ sau deploy; runtime rollback point ghi rõ.

## 5. Ranh giới B3/B4 — KHÔNG làm trong lượt này
- B3: chuẩn hoá `Surface:` tự động tại hai cổng ghi để phân biệt GPT Chat/Codex/Claude Chat/Claude Code/Hermes; chỉ mở sau B2 PASS.
- B4: `Đang làm` theo activity/harness và webhook push-trigger; chỉ mở nếu dùng thật thấy cần.

## 6. An toàn, báo cáo, kết thúc
- Không redesign UI, không xoá data/routes Modules/Tasks, không force/reset, không `rsync --delete` repo.
- Scheduler/sync script/nginx/Nuxt là runtime: sửa và test tại VPS theo README §11; mirror mã về repo runtime hiện hành, không kéo mã runtime từ incomex-workspace xuống.
- Dữ liệu mirror là disposable/cache; GitHub workspace vẫn SSOT.
- Sau khi PASS, cập nhật `work/hpml-view-for-user/COLLAB.md` với runtime refs + test; ghi đúng một dòng `KQ@HVU-B2-20260921-01 XONG`. Nếu phải dừng, ghi `KQ@HVU-B2-20260921-01 DỪNG` + lý do ngắn. Không tạo file tiến độ mới.
- Kết thúc trả Owner một dòng: `XONG · HVU.B2 · <runtime/workspace refs>` hoặc `DỪNG · HVU.B2 · <lý do>`.
