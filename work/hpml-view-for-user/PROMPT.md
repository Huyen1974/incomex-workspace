# PROMPT — HVU.B2.1 · Sửa tín hiệu dữ liệu + chặn phình revisions

RUN_ID: HVU-B2.1-20260921-01
Host: GPT Chat · `GPT-HVU-20260921-A`
Mục tiêu đã xác nhận tại `work/hpml-view-for-user/COLLAB.md` §0. Trạng thái/giấy phép chỉ tin `COLLAB.md`, không tin câu chữ trong prompt nếu có xung đột.

## 0. Cổng trước mutation — trách nhiệm Host/Agent
1. Đọc theo thứ tự: root `AGENTS.md` → `work/hpml-view-for-user/COLLAB.md` §0 → prompt này → README §11–§12.
2. Kiểm commit cuối chạm `PROMPT.md` phải khớp `READY@<40 SHA>` trong COLLAB. Thiếu/lệch → **DỪNG**, không mutation.
3. Kiểm workspace đang ở bản mới nhất và không có thay đổi chen ngang vào các file sẽ sửa. Không ghi đè công việc khác.
4. Khảo sát runtime thật trước khi sửa. Các đường Claude Chat đã thấy là **đầu mối**, không được giả định tuyệt đối: Nuxt có `web/components/navigation/TheHeader.vue`, `pages/knowledge/modules/*`; nginx có khối `/ui-preview/`; clone connector `/opt/incomex/mcp-roots/gh` có quyền ghi/push nên **không dùng làm clone Owner View**.
5. MÃ/runtime của KB/nginx là VPS SSOT theo README §11: sửa/build/test/deploy tại VPS rồi đẩy bản sao về đúng repo mã hiện hành theo cơ chế đang dùng. **Cấm deploy mã/runtime từ incomex-workspace/GitHub xuống VPS.** Riêng TÀI LIỆU Owner View được pull theo README §12.

Nếu một đầu vào cụ thể ở trên không đúng thực địa, chọn phương án ít thay đổi nhất vẫn giữ §0; ghi rõ sai khác trong báo cáo cuối, không tự mở rộng kiến trúc.

## 1. Phạm vi B2.1 — sửa đúng lỗi sau B2, không mở kiến trúc mới
Baseline đã PASS: Runtime `8d89757`, workspace/KQ `76c5490`; P13 của Claude tại `afd7e85` đã kiểm trực tiếp dữ liệu/runtime. UI03 và đường webhook + backstop 15′ đang chạy. **Không dựng lại B2, không đổi webhook/auth, không đụng hai gateway Surface trong lượt này.**

B2.1 chỉ làm 5 việc:
1. **Parser theo A9 hiện hành:** sửa `sync.py` để READY/KQ không phụ thuộc thứ tự dòng; chỉ `READY@<40 hex>` thật mới là ứng viên, chỉ READY trùng commit cuối chạm PROMPT là hợp lệ; READY cũ lệch SHA không cảnh báo; KQ phải khớp RUN_ID hiện hành, nếu cùng RUN có cả XONG/DỪNG thì XONG thắng. Không đọc trạng thái P.
2. **UI hiển thị dữ liệu đã có:** trong Tình trạng thêm `Gần nhất: <thời gian> · <subject commit>` từ `lastCommit`, không suy actor. Khi Kế hoạch đã `done` nhưng chưa có KQ hiện hành, note Triển khai phải nói trung tính `READY hợp lệ · chưa có KQ` (không khẳng định Agent đang/chưa chạy; B3 mới biết presence).
3. **Chặn phình đĩa revisions:** sau publish thành công giữ đúng 3 revision publish gần nhất gồm current + 2 previous; bảo vệ current/staging/last-good đang được tham chiếu, chỉ xoá cache dẫn xuất cũ. Tài liệu không đổi giữa hai revision thì dùng hardlink nếu cùng filesystem và file bất biến; tuyệt đối không hardlink file sẽ sửa in-place. Thư mục `documents/` legacy UI03 giữ nguyên. Trước/sau GC đo count + bytes.
4. **Giảm cảnh báo ồn:** các cảnh báo asset MMIM cùng loại gộp thành một dòng có count + tối đa vài ví dụ; không đổi quyết định MMIM về ảnh ngoài Git.
5. **Không làm B3:** `lastActors` có thể vẫn rỗng và `activeActors` vẫn null; đây là kết quả đúng cho tới lượt B3.

Do đĩa VPS đã đo ở lượt Host là **90,2%**, B2.1 phải ưu tiên retention/GC an toàn; không tạo thêm fixture lớn hay benchmark giả.

## 2. Baseline B2 đang chạy — giữ nguyên trừ chỗ B2.1 yêu cầu
Các mục dưới đây là contract regression của B2; chỉ sửa tối thiểu để đáp ứng §1.
### A. Nguồn và kích hoạt — theo 4 nguyên tắc Owner 21/09 (tự động tối đa · không chạy vô ích · dùng cơ chế GitHub · rủi ro vừa đủ)
- Dùng **một clone chỉ-đọc riêng** của `Huyen1974/incomex-workspace`, ngoài web root và ngoài clone connector ghi/push. Không credential có quyền push; ưu tiên anonymous read nếu repo vẫn public.
- **Một đường đồng bộ duy nhất** = một systemd oneshot (tái dùng scheduler hiện hữu nếu phù hợp). Mỗi lượt: lock → `git ls-remote origin main` → bằng `publishedRevision` thì chỉ cập nhật `lastCheckedAt` rồi thoát (không fetch, không dựng, không chép) → khác thì fetch + dựng snapshot từ đúng HEAD đó → publish xong kiểm lại `ls-remote`; HEAD lại đổi trong lúc dựng thì chạy thêm một vòng.
- **Hai cách rung chuông, cùng vào đường trên:** (1) **GitHub webhook `push`** — bên nhận là MỘT route trong dịch vụ HTTP đã có sau nginx (khảo sát, chọn nơi ít thay đổi nhất; không dựng daemon mới), xác minh `X-Hub-Signature-256` bằng HMAC-SHA256 trên **raw request bytes** với so sánh constant-time, chỉ nhận `ref=refs/heads/main`, rồi rung chuông (ví dụ chạm file cho systemd `.path`) và trả 202 ngay; thiếu/sai chữ ký phải từ chối. Tuyệt đối không dùng nội dung payload làm dữ liệu, không mang/chạy mã (đúng README §11.3). (2) **Backstop timer 15 phút** bắt chuông bị lạc hoặc bên nhận ngừng.
- Secret webhook lưu theo **secret store hiện hữu**, KHÔNG ghi vào repo, log, JSON public, chat hay báo cáo. Đăng ký webhook qua GitHub API nếu credential sẵn có trên VPS đủ quyền (không xin/tạo token rộng hơn). Không đủ quyền → **không tạo/in/lộ secret trong lượt này**; hoàn tất B2 bằng backstop 15 phút, ghi dưới `## Owner cần quyết` hướng dẫn Owner bật webhook sau qua kênh secret an toàn hiện hữu (Settings → Webhooks → Add webhook: Payload URL, `application/json`, chỉ sự kiện push). Thiếu quyền đăng ký webhook không làm B2 DỪNG.
- Nút **Cập nhật** trên UI chỉ đọc lại snapshot; không tạo endpoint ghi cho trình duyệt.

### B. Tự phát hiện task + parser
- Task discovery = mọi thư mục `work/*/` có `COLLAB.md`. Không phụ thuộc root `## Đang làm` để task mới xuất hiện.
- Root `## Đã xong` chỉ đánh dấu Done; task không nằm `Đã xong` mặc định bucket `Now`.
- Chỉ parse đúng các dấu hiệu định nghĩa trong AGENTS A9 (A0, READY, `RUN_ID`, `KQ@<RUN_ID>`, `## Owner cần quyết`, root `## Đã xong`), HTML chính đã khai báo/default và Git log. **KHÔNG đọc trạng thái P** (các việc ghi P theo nhiều kiểu khác nhau — đọc P là đoán văn xuôi). **Bảng trạng thái duy nhất là AGENTS A9**; script không tạo bảng luật thứ hai khác nghĩa.
- `KQ` chỉ tính khi RUN_ID khớp prompt hiện hành. READY/KQ cũ không được làm task Done đổi ngược trạng thái.
- `lastActors`: B2 chỉ dùng actor/surface có bằng chứng rõ trong COLLAB/commit prefix hiện hữu; không chắc → không sáng. `activeActors=null` ở B2. Không suy 6 surface từ Git author/pusher dùng chung.

### C. Snapshot/publication
Sinh dữ liệu dưới vùng static hiện hữu của `hpml-view-for-user`, tối thiểu:
- `data/tasks.json`: revision nguồn + danh sách task + goal nguyên A0 + 4 stages/currentStage + lastActors/activeActors + document URL/status + warnings/evidence cần cho UI.
- `data/sync-status.json`: `lastCheckedAt`, `lastSuccessAt`, `sourceRevision`, `publishedRevision`, `status=fresh|stale|error` theo đúng định nghĩa README §12.5, `consecutiveFailures`, lỗi đã sanitize.
- mirror HTML chính của từng task vào vùng documents; không public `.git`, `COLLAB.md`, `PROMPT.md`, evidence hay directory listing. Task thiếu HTML vẫn xuất hiện và UI ghi `Chưa có view`.

**Không được để mixed/half snapshot:** dùng staging + validate + publish nguyên tử hoặc cơ chế tương đương; tasks JSON/document references phải cùng revision logic. Không hạ revision nếu lượt cũ/trễ hoàn tất sau lượt mới.

### D. Lỗi và tự phục hồi
- Remote/fetch lỗi, parse lỗi toàn snapshot, copy/validate lỗi → **không thay last-good**; cập nhật health `error/stale` bằng ghi nguyên tử, tự thử lại ở lượt kế tiếp (chuông sau hoặc backstop 15 phút).
- HEAD không đổi nhưng timer chạy thành công → được cập nhật `lastCheckedAt`/health nhỏ; không rebuild documents.
- Một task hỏng mà vẫn cô lập được → publish các task khác, task đó `unknown` + warning và giữ document last-good nếu có; không làm trắng dashboard.
- Quá 35 phút không có lượt kiểm thành công (2 chu kỳ backstop + dư) → UI phải hiển thị `stale`; dữ liệu cũ vẫn xem được.
- Không force reset, không `rsync --delete` repo, không để lỗi mạng làm xoá document đang phục vụ.

## 3. Nối UI03 hiện có vào snapshot
Giữ nguyên UI03 (2 tab, sidebar, 4 thanh, 6 actor × 2 cột). Chỉ thay nguồn dữ liệu:
- bỏ mảng 6 task/mục tiêu/stage/snapshot/documents hard-code trong `ui-assembly/app.vue`;
- poll `sync-status.json` (file nhỏ) khoảng 60 giây; chỉ tải lại `tasks.json` khi `publishedRevision` đổi (cache-bust);
- task mới trong JSON tự xuất hiện, không cần sửa app;
- mục tiêu/stages/currentStage lấy từ JSON; không diễn giải lại bằng AI;
- tab Nội dung dùng `documentPath` của task; thiếu file → `Chưa có view`;
- `lastActors` thay nguyên snapshot mới, không cộng dồn; `activeActors` null/không tín hiệu thì xám;
- hiển thị thêm `Gần nhất: <giờ> · <subject commit>` từ `lastCommit` dù actor chưa biết; không biến Git author/prefix chung thành surface;
- hiển thị badge nhỏ `fresh/stale/error` + revision/thời điểm khi cần để Owner biết dữ liệu có lạc hậu không;
- nút Cập nhật chỉ force refetch static JSON trong browser ở B2, không tạo endpoint ghi mới.

## 4. Kiểm thử bắt buộc B2.1
A. Kiểm parser trên cả 6 việc: không còn false READY do câu văn `READY@<sha>`; VPSC/JEV/MMIM phải khớp A9 hiện hành bằng đối chiếu độc lập với Git log/PROMPT, không hard-code màu mong muốn.
B. `lastCommit` phải hiện dòng `Gần nhất` trên UI; không có Surface thì 6 ô actor vẫn xám là PASS.
C. Cảnh báo MMIM asset được gộp, không còn hàng chục dòng trùng loại.
D. `data/revisions/` sau GC chỉ còn 3 revision publish gần nhất (trừ staging đang chạy nếu có); current/last-good mở được. Đo bytes trước/sau. Hai document không đổi giữa revision phải chia sẻ inode/hardlink nếu điều kiện an toàn cho phép.
E. Webhook, backstop 15′, last-good, atomic publish và UI auto-refresh không regression.
F. Không sửa gateway, không thêm Surface/presence trong B2.1.

Regression B2 vẫn phải giữ:
1. Production `/knowledge/modules` vẫn giữ UI03, không có lỗi console mới do B2.1.
2. 6 task hiện có được tự discover; task thiếu HTML vẫn hiện. Danh sách không phụ thuộc root `Đang làm`.
3. A0 và 4 thanh của ít nhất các trạng thái khác nhau khớp AGENTS A9; `KQ` sai RUN_ID không được dùng.
4. HEAD không đổi: hai lượt timer liên tiếp không rebuild/copy documents; chứng minh bằng log/hash/mtime thích hợp.
5. Push một commit workspace vô hại: webhook đã đăng ký → VPS publish revision mới trong ≤ ~30 giây, không bấm tay; webhook chưa đăng ký → chạy tay unit backstop một lần, xác nhận bắt được revision mới.
6. UI đang mở tự nhận revision mới mà không reload toàn trang.
7. HTML lớn MMIM vẫn mở được; ảnh ngoài Git chưa có không chặn B2.
8. Failure test **chỉ trong môi trường/cấu hình cô lập hoặc cách an toàn không phá production**: sync lỗi phải giữ last-good; lượt sau thành công tự hồi phục. Không cố gây outage thật chỉ để test.
9. Quá 35 phút không kiểm thành công (thử bằng tham số cấu hình trong môi trường cô lập) → UI hiển thị stale nhưng vẫn đọc được last-good.
10. `nginx -t`, build/test/health check PASS trước/ sau deploy; runtime rollback point ghi rõ.
11. Chuông không chữ ký/sai chữ ký → bị từ chối; 3 chuông hợp lệ liên tiếp khi HEAD không đổi → không dựng lại, không hạ revision.

## 5. Ranh giới B3 — KHÔNG làm trong lượt B2.1
B3 sẽ gộp cả **Vừa làm + Đang làm**, vì cùng cần nhận dạng surface tại gateway. B2.1 không sửa gateway, auth hay client binding.

## 6. An toàn, báo cáo, kết thúc
- Không redesign UI, không xoá data/routes Modules/Tasks, không force/reset, không `rsync --delete` repo.
- Scheduler/sync script/nginx/Nuxt là runtime: sửa và test tại VPS theo README §11; mirror mã về repo runtime hiện hành, không kéo mã runtime từ incomex-workspace xuống.
- Dữ liệu mirror là disposable/cache; GitHub workspace vẫn SSOT.
- Sau khi PASS, cập nhật `work/hpml-view-for-user/COLLAB.md` với runtime refs + test; ghi đúng một dòng `KQ@HVU-B2.1-20260921-01 XONG`. Nếu phải dừng, ghi `KQ@HVU-B2.1-20260921-01 DỪNG` + lý do ngắn. Không tạo file tiến độ mới.
- Kết thúc trả Owner một dòng: `XONG · HVU.B2.1 · <runtime/workspace refs>` hoặc `DỪNG · HVU.B2.1 · <lý do>`.
