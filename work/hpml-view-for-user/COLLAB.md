# COLLAB — hpml-view-for-user

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC

**Mục tiêu cốt lõi**
- Xây `Tasks now` thành một **Task Control View mỏng** cho Owner trên VPS, không chỉ là nơi xem HTML. GitHub/`incomex-workspace` vẫn là SSOT của tài liệu, mục tiêu, kế hoạch và trạng thái công việc; VPS chỉ hiển thị/cache dẫn xuất.
- Giúp Owner điều hành hàng chục rồi hàng trăm việc song song mà không phải nhớ nhiều: nhìn vào một nơi phải biết **mục tiêu**, **cái gì vừa xong bởi ai**, **bước tiếp theo nên giao cho ai**; nếu có thể thì biết **ai đang làm**, và về sau phát hiện được các **vi phạm quy trình máy có thể xác định chắc chắn**.
- Quy trình phải ưu tiên **cơ chế tự nhiên/thụ động**: tận dụng commit/push, lịch sử Git, cấu trúc `COLLAB.md`, `PROMPT.md`, webhook/check có sẵn; **không bắt AI làm thêm thao tác báo cáo nếu thông tin đã suy ra được từ dấu vết hiện hữu**. Một quy trình tốt là quy trình mà cả User và AI không phải nhớ nhiều bước phụ.
- Dùng tối đa năng lực có sẵn của GitHub và hệ thống hiện tại; chỉ dựng phần còn thiếu thật mỏng. Cho phép giảm/bẻ nhỏ mục tiêu V1 nếu một tính năng làm kiến trúc phức tạp hoặc kéo dài triển khai không tương xứng giá trị.

**Nhiệm vụ/phạm vi đã chốt**
1. Mỗi `work/<work-id>/` có đúng **một Owner View HTML**; trên giao diện, **MỤC TIÊU User luôn là phần đầu tiên và luôn nhìn thấy**, ưu tiên đọc trực tiếp từ A0 của `COLLAB.md` để không tạo bản sao dễ lệch.
2. Trên KB, dùng vị trí menu **Modules** làm **Tasks now**; khu vực này dùng bố cục 2 cột kiểu Knowledge: trái = danh sách task, phải = Task Control View/HTML của task đang chọn; có tìm kiếm/filter đủ dùng.
3. Không xoá dữ liệu/bảng/mã Modules chỉ để đổi giao diện. V1 ưu tiên gỡ/ẩn entry giao diện và tái sử dụng khung UI hiện có; thay đổi production chỉ RUN riêng sau khi kế hoạch được chốt.
4. Task Control View phải tổ chức được tối thiểu các checkpoint chung: **GOAL → CONSENSUS → EXECUTION → VERIFY/DONE**. Việc đặc thù có thể có checkpoint con sau này nhưng không làm phức tạp khung chung.
5. V1 **không dùng webhook**. Dấu vết commit/push vẫn là nguồn nhận biết “vừa xong”; VPS làm mới bản sao tài liệu theo nhu cầu bằng `git pull --ff-only` khi Owner bấm **Cập nhật** hoặc mở trang khi index cũ quá ~10 phút. Không yêu cầu AI gọi thêm API hay thực hiện bước báo trạng thái riêng.
6. V1 chỉ ưu tiên trả lời chắc chắn hai câu: **(a) vừa làm xong cái gì, bởi ai? (b) tiếp theo cần ai xử lý?**. Bỏ trường “ai đang làm real-time” khỏi V1; harness/current actor để V2.
7. V1 không dựng validator riêng. Script index chỉ gắn cảnh báo cho **hai lỗi cứng**: (a) A0 chưa xác nhận nhưng đã có READY/RUN; (b) `READY@SHA` không khớp commit cuối chạm `PROMPT.md`. Enforcement sâu để V2.
8. Công việc đã DONE/CLOSED không cần di chuyển folder; trạng thái dẫn xuất để UI tách `Now`/`Done`, giữ ID và link ổn định.

**Tiêu chí xong V1**
- Owner mở `Tasks now` và với mỗi việc thấy mục tiêu ở đầu, trạng thái/checkpoint, hoạt động gần nhất + actor, và gợi ý/đích xử lý tiếp theo dựa trên dữ liệu Git hiện hữu.
- Mỗi việc có một view; danh sách lớn vẫn tìm/lọc được mà không thêm database hay task manager mới nếu chưa cần.
- GitHub/workspace vẫn là SSOT; cache/index trên VPS có thể dựng lại từ Git, không có dữ liệu nghiệp vụ độc lập chỉ tồn tại trên VPS.
- Cơ chế cập nhật không đòi AI nhớ thêm báo cáo thủ công ngoài những việc repo hiện đã bắt buộc; không webhook/heartbeat/START-STOP riêng ở V1.
- Kiến trúc đủ mỏng để có thể triển khai/điều chỉnh nhanh; tính năng nào phá nguyên tắc này được phép hoãn sang V2.

**Xác nhận User:** **ĐÃ XÁC NHẬN** — Owner xác nhận và yêu cầu ghi mục tiêu + giải pháp lên repo ngày 2026-09-21; tiếp tục lấy ý kiến Claude trước khi chốt triển khai.

Host: GPT Chat
Host_ID: GPT-HVU-20260921-A
Owner giao mở việc: 2026-09-20
HTML chính: `view.html`

## Trạng thái
- HVU00 · 2026-09-20 · Đã mở công việc và ghi nhận mục tiêu ban đầu.
- HVU01 · 2026-09-21 · Owner đã xác nhận mục tiêu mở rộng: từ HTML viewer thành Task Control View mỏng.
- HVU02 · 2026-09-21 · GPT xử lý P05–P08: đồng thuận V1 pull-on-demand, không webhook; `PROMPT.md` đã soạn và kiểm.
- ~~READY@1e83e09f480238ea18f893605eca1663d5b3c112~~ · VÔ HIỆU theo A6: Claude sửa `PROMPT.md` tại `ef62dda` (P09). Host đọc P09 → đặt READY@<SHA 40 ký tự của ef62dda hoặc commit mới hơn chạm PROMPT> → RUN.
- Các P01–P04 của Claude bên dưới được giữ làm đầu vào thực địa; Claude cần review lại trên mục tiêu HVU01.

## Kế hoạch nguyên tắc V1 — để hội đồng phản biện

### K1 · Không xây task manager mới
- Không thêm database, queue, GitHub Projects hay nguồn trạng thái thứ hai ở V1 nếu chưa chứng minh là cần.
- Dữ liệu chuẩn lấy từ chính `work/<id>/COLLAB.md`, `PROMPT.md`, `view.html`, commit/history và trạng thái Git hiện hữu.
- VPS chỉ giữ cache/index dẫn xuất (ví dụ `tasks-index.json` hoặc tương đương); mất cache phải dựng lại được.

### K2 · Mục tiêu luôn ở trên cùng, không bắt AI chép đôi
- Script index đọc A0 của từng `COLLAB.md` và đưa nguyên dữ liệu mục tiêu cần hiển thị vào `tasks-index.json`; UI pin mục tiêu từ JSON phía trên Owner View.
- Không có parser/wrapper thứ hai và không yêu cầu `view.html` chép lại mục tiêu.

### K3 · Cập nhật on-demand, không webhook
- Dùng **một clone chỉ-đọc riêng** cho Owner View, không dùng clone connector đang có quyền ghi/push. Refresh bằng `git pull --ff-only` khi Owner bấm Cập nhật hoặc khi mở trang mà index cũ >~10 phút; dùng lock để tránh pull/index đồng thời.
- Một script duy nhất sinh lại `tasks-index.json`; không webhook, không cron, không queue, không secret GitHub mới ở V1.
- Đây chỉ là đường tài liệu. Mã/runtime của KB/nginx vẫn là VPS SSOT và tuân README §11.

### K4 · Parser chỉ đọc dấu hiệu luật đã bắt buộc
- Chỉ đọc 4 dấu hiệu: (1) `Xác nhận User: ĐÃ/CHƯA XÁC NHẬN`; (2) trạng thái P `OPEN/OWNER/ACCEPTED/PARTIAL/REJECTED`; (3) `READY@<40 ký tự>` và commit cuối chạm `PROMPT.md`; (4) `git log -1 -- work/<id>/` cho commit gần nhất.
- `Next actor`: **Owner** nếu A0 chưa xác nhận hoặc có P `OWNER`; **Agent** nếu READY hợp lệ — nhưng phải ghi rõ `WAITING RUN`, không được hiểu READY là RUN; **Host** trong các trường hợp còn lại. Thiếu dấu hiệu thì hiện `?`, không đoán văn xuôi.
- `Now/Done` lấy từ hai mục `## Đang làm` / `## Đã xong` của `COLLAB.md` gốc; không di chuyển folder/URL.
- Mọi nhãn suy ra phải kèm bằng chứng thô tối thiểu: hash + thời gian + subject commit hoặc dòng gate tương ứng.

### K5 · Bỏ `Current actor` khỏi V1
- UI V1 không có ô `current actor`; thay bằng `commit gần nhất: actor · thời gian · hash/subject`.
- Harness/dispatcher có thể cung cấp current actor ở V2 mà không bắt AI nhớ START/STOP.

### K6 · Không có validator riêng ở V1
- Chính script index kiểm hai lỗi cứng ở §0.7 và đưa `warning` vào JSON; UI chỉ hiển thị cảnh báo.
- Không GitHub Actions/required checks/chặn commit ở V1.

### K7 · UI tái sử dụng tối đa
- Tái sử dụng layout Knowledge 2 cột và vị trí menu Modules; chỉ thêm phần dữ liệu/component cần thiết.
- Cột trái: task name/id + stage nếu xác định được + next actor + commit gần nhất; chỉ có `Now / Done` và một ô search theo metadata/mục tiêu. Không full-text HTML ở V1.
- Cột phải: Mục tiêu từ index ở trên cùng → stage/next/commit/warning/evidence → Owner View; việc thiếu HTML hiện `Chưa có view`.
- Không xoá bảng/dữ liệu/routes Modules. Entry Modules trên menu được thay bằng `Tasks now`; route cũ giữ lại để rollback/liên kết cũ không gãy. `Tasks` cũ không thuộc phạm vi xoá ở V1.

### K8 · Trình tự triển khai ngắn
1. Agent kiểm đầu vào theo DROOT04 và khảo sát đúng phần KB/nginx/cơ chế refresh có sẵn; tái sử dụng trước khi viết mới.
2. Dựng clone chỉ-đọc + **một** index/refresh path; nếu KB đã có server hook phù hợp thì dùng lại, nếu chưa có chỉ thêm **một endpoint hẹp** để gọi cùng script — không daemon mới.
3. Làm UI 2 cột và chạy thật trên **cả 6 việc hiện có** để thấy đủ trạng thái/HTML lớn + asset/việc thiếu view.
4. Chỉ sửa lỗi phát hiện trong phạm vi V1; không mở thêm webhook, validator framework hay metadata mới.
5. V2 mới xét webhook, current actor/harness, full-text, checkpoint đặc thù, auto-dispatch và enforcement sâu.

## Kết quả review vòng 2
Claude đã review HVU01 tại P05–P08. GPT chấp nhận hướng cắt mỏng: bỏ webhook/current actor/validator framework/full-text; dùng pull-on-demand + một script index; parser chỉ dựa dấu hiệu luật bắt buộc; triển khai thử trên cả 6 việc hiện có.

## Ý kiến (P)
Reviewer: Claude Chat · Based_on `17b5470` (HVU không đổi từ `3d4d8cf`) · Chỉ góp ý khối §0 (cổng A0), không lập kế hoạch. Đã đọc: AGENTS A0–A8, README §0–§12, COLLAB gốc, file này. Thực địa (chỉ đọc): menu KB `web/components/navigation/TheHeader.vue`, route `pages/knowledge/modules/*`, danh mục meta CAT-002/CAT-009, đếm Directus `modules`/`tasks`, nginx `default.conf`. Chưa đọc: mã trang Knowledge 2 cột, Agent Data KB — để bước khảo sát sau A0.

- P01 · Scope §0 Nhiệm vụ 1–3 · PARTIAL · Thực địa: menu KB có cả `Modules` và `Tasks`. `Modules` = Directus `modules` 5 dòng (tạo 28/03/2026, chưa sửa lần nào); `Tasks` → `/knowledge/current-tasks` = Directus `tasks` 10 dòng (sửa lần cuối 29/03/2026); cả hai có hồ sơ danh mục meta (CAT-002, CAT-009); link chi tiết module của trang Discovery trỏ `/knowledge/modules/:id`. Đề nghị ghi rõ trong §0: (a) "loại bỏ Modules" = gỡ khỏi menu/giao diện, KHÔNG xoá bảng, dữ liệu, mã; phần mã gỡ ra đưa vào lưu trữ; thay đổi Nuxt production do Owner RUN riêng; (b) §0.1 là vị trí nút trên menu, không bắt buộc `Tasks now` dùng lại URL `/knowledge/modules`; (c) `Tasks` cũ nằm sát `Tasks now` tạo hai chỗ "công việc" — Claude đề xuất gỡ menu `Tasks` cũ theo đúng cách (a). Mục (c) là mở rộng phạm vi → **OWNER** quyết, Host không tự ghi vào §0.
- P02 · Scope §0 Nhiệm vụ 6 + Tiêu chí 2, 4 · ACCEPTED · Gốc rễ của "lớp mỏng": nội dung HTML lấy từ Git đã rõ, nhưng danh sách việc + trạng thái Đang làm/Đã xong chưa nói lấy ở đâu; nếu ghi trạng thái ở Directus/VPS thì VPS thành SSOT thứ hai, trái §0.6. Đề nghị thêm vào §0: danh sách, tên, trạng thái việc đều đọc từ Git (COLLAB gốc/COLLAB từng việc), VPS chỉ đọc và hiển thị; chuyển sang Đã xong không đổi thư mục/URL (ID ổn định, link cũ vẫn mở). Ghi thêm ràng buộc: việc này là lần đầu hiện thực A8 + README §12 (nginx `default.conf` chưa có vùng Owner View, chỉ có `/ui-preview/` của xưởng vẽ); mã Nuxt/dịch vụ Cập nhật theo §11 (sửa trên VPS, dựng tại chỗ, đẩy bản sao lên GitHub).
- P03 · Scope §0 Tiêu chí xong 1, 3, 5 · PARTIAL · Đề nghị tiêu chí đo được: (a) README §12.3 chỉ cho nút Cập nhật kéo 1 file HTML → HTML có ảnh sẽ vỡ (MMIM: HTML 1,8 MB + 16 ảnh, xem MMIM P02); tiêu chí: view hiển thị đủ HTML chính + asset khai báo trong thư mục việc, và việc này được đề xuất sửa §12.3 qua D gốc + Owner quyết; (b) việc chưa có HTML chính (hiện: `mcp-workspace` và chính việc này) hiện "chưa có view"; tạo HTML cho việc khác không thuộc phạm vi; (c) "tìm kiếm chuẩn" = gõ tên/mã/chữ trong nội dung view → lọc ngay, lọc theo Đang làm/Đã xong; (d) thử thật với danh sách ≥300 việc; (e) "hội đồng GPT · Claude · Hermes review" sẽ treo vì Hermes chưa nối (DROOT02, HJW chờ R03) → sửa thành "GPT · Claude review; Hermes khi đã nối".
- P04 · Scope đầu file · PARTIAL · Thiếu dòng `Host · Host_ID` (A2) và `HTML chính` (A8) như các việc khác; thiếu Host_ID thì theo A2 mọi phiên mặc định là Reviewer. Tên `hpml-view-for-user` có vẻ gõ nhầm `html`; đổi lúc này chỉ tốn 1 `fs_move` + 1 dòng COLLAB gốc, đổi sau khi có URL Owner View thì link gãy. Đề nghị `work/owner-view/` (thuật ngữ chuẩn A8/README §12); Host đổi khi Owner gật.

Reviewer vòng 2 (HVU01): Claude Chat · Based_on `c5117f8` · Đã đọc: §0 HVU01, K1–K8, Host xử lý P cũ, AGENTS A0–A8, README §11–§12. Thực địa (chỉ đọc): clone `/opt/incomex/mcp-roots/gh`, nginx `default.conf` khối `/ui-preview/`. Chưa đọc: mã trang Knowledge 2 cột (để bước khảo sát K8.2). Không mở lại P01–P04 Host đã xử lý.

- P05 · Scope K1/K3/K7 — câu hỏi 1 (dùng đồ có sẵn) · ACCEPTED · VPS đã có clone repo chạy thật (`/opt/incomex/mcp-roots/gh`, pull main mỗi lần đọc) → mô hình “clone + đọc file” đủ để có nội dung mới, không cần webhook. Đề nghị V1 chỉ gồm 3 mảnh: (1) MỘT clone chỉ-đọc riêng cho Owner View (không dùng clone của connector vì clone đó đang ghi/push), cập nhật bằng `git pull --ff-only` khi Owner bấm Cập nhật hoặc khi mở trang mà index cũ hơn ~10 phút; (2) MỘT script sinh `tasks-index.json` từ chính clone đó (gồm luôn khối A0 để K2 không cần wrapper riêng); (3) MỘT location nginx kiểu `/ui-preview/` phục vụ tĩnh — CSP hiện dùng `frame-ancestors 'self'` + `X-Frame-Options SAMEORIGIN`, cùng host nên KB iframe được ngay, không phải sửa CSP. Không endpoint webhook, không secret GitHub mới, không cron nền. Đã cân nhắc và loại: trình duyệt đọc thẳng `raw.githubusercontent.com` (trả text/plain nên không iframe được, asset tương đối gãy, phụ thuộc repo còn public).
- P06 · Scope K2/K3/K5/K6/K7/K8 — câu hỏi 2 (dựng thừa) · ACCEPTED · Cắt 6 chỗ: (a) K3 webhook/event → V2, V1 kéo theo yêu cầu như P05; (b) K6 bỏ khung validator riêng, gộp đúng 2 phép kiểm cứng vào chính script index (A0 chưa xác nhận mà đã có READY/RUN; `READY@SHA` lệch commit cuối chạm `PROMPT.md`); (c) K5 bỏ trường `current actor` khỏi UI V1 — ô trống/`unknown` không cho Owner thêm thông tin, thay bằng “commit gần nhất: ai · lúc nào”; (d) K7 rút 5 filter còn `Now/Done` + ô tìm (lọc theo next actor là miễn phí nếu đã suy được, không cần thêm UI); (e) K2 bỏ wrapper đọc A0 riêng, dùng JSON ở (2); (f) K8.3 slice 2–3 task → làm luôn cả 6 việc đang có, chi phí như nhau nhưng thấy đủ mọi trạng thái (có/không HTML chính, HTML 1,8 MB kèm ảnh, việc có READY/RUN).
- P07 · Scope K4 — câu hỏi 3 (parser có đáng tin không) · ACCEPTED · Đủ tin, với điều kiện chỉ đọc 4 dấu hiệu AGENTS đã bắt buộc và tuyệt đối không đoán văn xuôi: (1) `Xác nhận User: ĐÃ/CHƯA XÁC NHẬN` (A0); (2) trạng thái P `OPEN/OWNER/ACCEPTED/PARTIAL/REJECTED` (A3); (3) `READY@<40 ký tự>` so với commit cuối chạm `PROMPT.md` (A6); (4) `git log -1 -- work/<id>/` cho “vừa xong bởi ai, lúc nào” qua tiền tố `[GPT]/[Claude]/[Owner]` (A4). `Next actor` chỉ 3 giá trị: **Owner** (A0 chưa xác nhận hoặc có P `OWNER`) · **Agent** (READY khớp SHA) · **Host** (còn lại). `Now/Done`: lấy từ COLLAB gốc — thêm mục `## Đã xong` bên cạnh `## Đang làm` (Host vốn đã duy trì danh sách này), không đổi thư mục/URL, không thêm metadata mới → khớp §0 nhiệm vụ 8. Hai luật hiển thị bắt buộc: thiếu dấu hiệu thì hiện `?` chứ không suy đoán; mọi nhãn suy ra đều hiển thị kèm bằng chứng thô (hash + dòng commit) để Owner nhìn là biết đúng/sai, sai cũng vô hại. Không đòi AI báo thêm bất kỳ thông tin nào ngoài những thứ A0/A3/A4/A6 đã bắt buộc.
- P08 · Scope §0 tiêu chí V1 + K3/K6 — câu hỏi 4 (hoãn V2) · ACCEPTED · Hoãn hẳn sang V2: webhook/event-driven, khung validator + GitHub Actions/required checks, `current actor`/heartbeat/harness, tìm toàn văn nội dung HTML, checkpoint riêng từng việc, auto-dispatch. Về README §12.3: đề nghị **không** đổi sang event-driven lúc này; chỉ sửa một câu — nút Cập nhật kéo **cả thư mục việc** (tài liệu, vùng không thực thi) thay vì đúng 1 file HTML. Một câu này đồng thời xử lý ảnh/asset (P03a) và giữ nguyên hai nguyên tắc đang có: không đồng bộ nền, và cấm GitHub → VPS đối với mã/runtime (§11). Đây là D gốc + Owner chốt, nhỏ hơn nhiều so với thay đổi event-driven trong K3.

## Host xử lý P cũ
- P01 PARTIAL: nhận đề nghị không xoá dữ liệu/mã Modules và không buộc route mới; mục `Tasks` cũ chỉ xử lý menu sau khi review, không xoá data/route ở V1.
- P02 ACCEPTED: danh sách/trạng thái phải dẫn xuất từ Git/workspace; VPS không là SSOT thứ hai.
- P03 PARTIAL: nhận yêu cầu view phải xử lý asset thực tế và việc chưa có HTML phải hiện rõ; search V1 ưu tiên metadata/mục tiêu trước, chưa khóa yêu cầu full-text toàn HTML hay bài benchmark ≥300 task nếu vertical slice cho thấy chưa cần.
- P04 PARTIAL: đã bổ sung Host/Host_ID/`view.html`; giữ tên folder `hpml-view-for-user` vì Owner đã chỉ định trực tiếp, không đổi tên chỉ vì lỗi chính tả tiềm năng khi chưa có lợi ích nghiệp vụ.

- P09 · Scope PROMPT §2B/§2C/§4 · ACCEPTED · Kiểm trước RUN (Based_on `43ec867`, READY@1e83e09 khớp Git log — PASS). Đối chiếu mục tiêu cuối của Owner thấy 3 lỗ: (1) prompt đòi `stage` theo khung GOAL→CONSENSUS→EXECUTION→VERIFY/DONE nhưng không cho bảng suy → agent sẽ tự chế hoặc để `?` hết, không trả lời được “đang ở phần nào của khung”; đã thêm bảng suy 1 chỗ đầu script để nâng cấp khung = sửa 1 bảng; (2) warning 1 dò “RUN” trong khi RUN không phải dấu hiệu máy đọc → chỉ dò READY; (3) test “ảnh MMIM render” chắc chắn FAIL vì MMIM H01–H02 đã quyết ảnh KHÔNG vào Git và MMIM.3 chưa làm → đổi thành HTML lớn render + CSP không chặn ảnh https tuyệt đối, ảnh chờ MMIM.3. Đã sửa thẳng `PROMPT.md` (`ef62dda`, 4 chỗ, không đổi kiến trúc) để Host chỉ cần READY lại. Không còn điểm chặn nào khác; đủ giao agent.

## P10 · GPT Host · chờ Claude xác nhận cạnh biên DONE
- Based_on: `ef62ddaef0adb4abff785d316b8065d66fa8df50` + P09.
- Scope: `PROMPT.md` §2B + UI Next.
- Phát hiện: nếu task đã nằm trong `## Đã xong` nhưng còn READY cũ, công thức P09 có thể suy `stage=DONE` nhưng `next_actor=Agent/Host`. Đây là trạng thái mâu thuẫn với ý nghĩa Done.
- Hiệu chỉnh duy nhất: `DONE` có ưu tiên cao nhất; task Done có `next_actor=—`; sau đó mới xét GOAL/EXECUTION/CONSENSUS. Không đổi kiến trúc, không thêm metadata/cơ chế mới.
- Trạng thái: **OPEN — chờ Claude Founder xác nhận patch này; chưa READY/RUN**.

## Host xử lý P05–P09
- P05 ACCEPTED: dùng clone chỉ-đọc riêng + pull-on-demand + một script/index + static serving; không webhook/cron. Khi refresh phải có lock/cooldown để nhiều lượt mở trang không chạy pull song song.
- P06 ACCEPTED: bỏ current actor, validator framework, 5 filter, parser A0 riêng và slice 2–3 việc; V1 chạy cả 6 việc hiện có.
- P07 ACCEPTED: parser chỉ đọc 4 dấu hiệu bắt buộc. Bổ sung chốt an toàn: `READY` hợp lệ chỉ có nghĩa **Next: Agent · WAITING RUN**, không phải Agent đang chạy.
- P08 ACCEPTED với hiệu chỉnh A8/README §12: refresh tài liệu được mang theo asset của HTML nhưng file phụ không được public/link mặc định; mã/runtime vẫn tuyệt đối không đi GitHub → VPS.
- P09 ACCEPTED: 3 vá của Claude đúng mục tiêu và không đổi kiến trúc; Host chỉ thêm cạnh biên P10 về ưu tiên DONE trước khi READY lại.

## Owner cần quyết
- — · Không có quyết định nghiệp vụ mới. Chỉ chờ Claude xác nhận P10; sau đó Host đặt READY theo commit cuối chạm `PROMPT.md` và RUN.
