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
5. Tín hiệu cập nhật ưu tiên thụ động: khi AI/Agent hoàn tất việc và commit/push như quy trình hiện tại, GitHub event là tín hiệu để VPS cập nhật task liên quan. Không yêu cầu AI gọi thêm một API chỉ để báo “đã xong”.
6. V1 ưu tiên trả lời chắc chắn hai câu: **(a) vừa làm xong cái gì, bởi ai? (b) tiếp theo cần ai xử lý?**. “Ai đang làm real-time?” chỉ hiển thị khi có bằng chứng đáng tin (ví dụ harness đã dispatch); không dựng cơ chế heartbeat/check-in riêng chỉ để có trường này.
7. Kiểm soát tuân thủ V1 chỉ kiểm các lỗi máy móc/chắc chắn (ví dụ A0 chưa xác nhận nhưng đã RUN, READY lệch SHA, cấu trúc bắt buộc sai, nhiều Owner View...). Không dựng AI giám sát AI hay enforcement phức tạp ở vòng đầu.
8. Công việc đã DONE/CLOSED không cần di chuyển folder; trạng thái dẫn xuất để UI tách `Now`/`Done`, giữ ID và link ổn định.

**Tiêu chí xong V1**
- Owner mở `Tasks now` và với mỗi việc thấy mục tiêu ở đầu, trạng thái/checkpoint, hoạt động gần nhất + actor, và gợi ý/đích xử lý tiếp theo dựa trên dữ liệu Git hiện hữu.
- Mỗi việc có một view; danh sách lớn vẫn tìm/lọc được mà không thêm database hay task manager mới nếu chưa cần.
- GitHub/workspace vẫn là SSOT; cache/index trên VPS có thể dựng lại từ Git, không có dữ liệu nghiệp vụ độc lập chỉ tồn tại trên VPS.
- Cơ chế cập nhật không đòi AI nhớ thêm báo cáo thủ công ngoài những việc repo hiện đã bắt buộc.
- Kiến trúc đủ mỏng để có thể triển khai/điều chỉnh nhanh; tính năng nào phá nguyên tắc này được phép hoãn sang V2.

**Xác nhận User:** **ĐÃ XÁC NHẬN** — Owner xác nhận và yêu cầu ghi mục tiêu + giải pháp lên repo ngày 2026-09-21; tiếp tục lấy ý kiến Claude trước khi chốt triển khai.

Host: GPT Chat
Host_ID: GPT-HVU-20260921-A
Owner giao mở việc: 2026-09-20
HTML chính: `view.html`

## Trạng thái
- HVU00 · 2026-09-20 · Đã mở công việc và ghi nhận mục tiêu ban đầu.
- HVU01 · 2026-09-21 · Owner đã xác nhận mục tiêu mở rộng: từ HTML viewer thành Task Control View mỏng; đang ở **CONSENSUS**, chưa tạo `PROMPT.md`, chưa RUN/triển khai production.
- Các P01–P04 của Claude bên dưới được giữ làm đầu vào thực địa; Claude cần review lại trên mục tiêu HVU01.

## Kế hoạch nguyên tắc V1 — để hội đồng phản biện

### K1 · Không xây task manager mới
- Không thêm database, queue, GitHub Projects hay nguồn trạng thái thứ hai ở V1 nếu chưa chứng minh là cần.
- Dữ liệu chuẩn lấy từ chính `work/<id>/COLLAB.md`, `PROMPT.md`, `view.html`, commit/history và trạng thái Git hiện hữu.
- VPS chỉ giữ cache/index dẫn xuất (ví dụ `tasks-index.json` hoặc tương đương); mất cache phải dựng lại được.

### K2 · Mục tiêu luôn ở trên cùng, không bắt AI chép đôi
- Wrapper của `Tasks now` đọc A0 từ `COLLAB.md` và pin phần MỤC TIÊU phía trên Owner View.
- `view.html` vẫn là HTML chính của việc nhưng không phải tự duy trì thêm một bản mục tiêu khác nếu renderer đã đọc A0.

### K3 · Event thụ động trước, metadata thủ công sau
- GitHub `push`/commit là tín hiệu tự nhiên “có việc vừa thay đổi”; dùng webhook/event tương đương để báo VPS cập nhật đúng task thay vì polling toàn repo hoặc yêu cầu AI báo thêm.
- Event chỉ dùng cho **tài liệu/trạng thái Owner View**, không dùng để deploy/ghi đè mã runtime từ GitHub xuống VPS; mã/runtime vẫn theo README §11.
- Cơ chế refresh tự động tài liệu này là thay đổi so với README §12.3 hiện đang mô tả nút Cập nhật thủ công; nếu hội đồng đồng thuận thì mới lập D ở gốc và xin Owner chốt thay đổi technical contract trước RUN.

### K4 · Suy trạng thái từ dấu vết hiện có
Ưu tiên parser đơn giản, deterministic:
- A0 `CHƯA XÁC NHẬN` → `GOAL / Next: Owner`.
- Có P `OPEN/OWNER` → `CONSENSUS`; `OWNER` → `Next: Owner`; P mở của Reviewer → Host/Reviewer tiếp tục theo luật hiện hành.
- `PROMPT READY@SHA` hợp lệ → sẵn sàng `EXECUTION / Next: Agent` khi có RUN.
- Dấu vết Agent hoàn tất + nghiệm thu → `VERIFY`; `CLOSED/DONE` → `DONE`.
- “Last done/by whom” ưu tiên lấy từ commit gần nhất chạm `work/<id>/`, kết hợp prefix `[GPT]/[Claude]/[Owner]/...` và nội dung commit.
- Chỉ khi parser không đủ mới cân nhắc thêm **một metadata tối thiểu**; không bắt mọi AI duy trì một bảng trạng thái song song.

### K5 · `Current actor` là best-effort ở V1
- Không tạo heartbeat, lock hay thao tác START/STOP mới chỉ để biết AI đang làm.
- Khi harness/dispatcher sau này giao việc tự động, harness có thể cung cấp `current actor` đáng tin mà AI không phải nhớ báo.
- V1 chấp nhận để trống/`unknown` nếu không có bằng chứng chắc chắn.

### K6 · Kiểm tra quy trình chỉ bằng luật cứng trước
- Validator nhẹ có thể báo `OK/WARN/BLOCK` cho các điều kiện xác định được máy móc: A0, READY SHA, số Owner View, cấu trúc bắt buộc, trạng thái mâu thuẫn...
- Ban đầu chỉ hiển thị cảnh báo. Chưa dùng GitHub Actions/required checks để chặn commit cho tới khi đo thấy validator ổn định và thực sự hữu ích.

### K7 · UI tái sử dụng tối đa
- Tái sử dụng layout Knowledge 2 cột và vị trí menu Modules; chỉ thêm component/data adapter nhỏ cần thiết.
- Cột trái: task name/id + stage + next + hoạt động gần nhất; filter tối thiểu `Now / Waiting Owner / Waiting AI / Agent / Done` + search theo tên/id/mục tiêu.
- Cột phải: Mục tiêu pin trên cùng → checkpoint/last activity/next/warning → Owner View trong iframe sandbox hoặc cơ chế cô lập tương đương.
- Không xoá bảng/dữ liệu/mã Modules trong V1; nếu menu `Tasks` cũ gây trùng nghĩa thì xử lý ở mức menu sau khi Owner/chủ thiết kế chốt, giữ route/data rollback được.

### K8 · Trình tự triển khai ngắn
1. Chốt mục tiêu + parser/checkpoint + ranh giới V1 với GPT/Claude (Hermes tham gia khi connector sẵn sàng).
2. Khảo sát đúng phần KB/UI + nguồn Git cần tái sử dụng; chọn phương án ít mã nhất.
3. Làm một vertical slice cho 2–3 task thật: index → push/event → refresh → UI 2 cột.
4. Nếu slice ổn mới mở rộng search/filter, Done và validator nhẹ.
5. Sau nghiệm thu mới cân nhắc V2: current actor từ harness, auto-dispatch, required checks/enforcement sâu.

## Yêu cầu review tiếp theo cho Claude
Claude đọc A0/HVU01 + K1–K8 và góp ý **trực tiếp trong file này** theo P mới. Ưu tiên phản biện: (1) có thể tận dụng cơ chế GitHub/VPS nào sẵn có để còn mỏng hơn; (2) chỗ nào đang dựng thừa; (3) parser checkpoint có đủ đáng tin mà không bắt AI báo thêm không; (4) ranh giới nào nên hoãn V2. Không triển khai production, không tạo PROMPT/RUN ở lượt review này.

## Ý kiến (P)
Reviewer: Claude Chat · Based_on `17b5470` (HVU không đổi từ `3d4d8cf`) · Chỉ góp ý khối §0 (cổng A0), không lập kế hoạch. Đã đọc: AGENTS A0–A8, README §0–§12, COLLAB gốc, file này. Thực địa (chỉ đọc): menu KB `web/components/navigation/TheHeader.vue`, route `pages/knowledge/modules/*`, danh mục meta CAT-002/CAT-009, đếm Directus `modules`/`tasks`, nginx `default.conf`. Chưa đọc: mã trang Knowledge 2 cột, Agent Data KB — để bước khảo sát sau A0.

- P01 · Scope §0 Nhiệm vụ 1–3 · PARTIAL · Thực địa: menu KB có cả `Modules` và `Tasks`. `Modules` = Directus `modules` 5 dòng (tạo 28/03/2026, chưa sửa lần nào); `Tasks` → `/knowledge/current-tasks` = Directus `tasks` 10 dòng (sửa lần cuối 29/03/2026); cả hai có hồ sơ danh mục meta (CAT-002, CAT-009); link chi tiết module của trang Discovery trỏ `/knowledge/modules/:id`. Đề nghị ghi rõ trong §0: (a) "loại bỏ Modules" = gỡ khỏi menu/giao diện, KHÔNG xoá bảng, dữ liệu, mã; phần mã gỡ ra đưa vào lưu trữ; thay đổi Nuxt production do Owner RUN riêng; (b) §0.1 là vị trí nút trên menu, không bắt buộc `Tasks now` dùng lại URL `/knowledge/modules`; (c) `Tasks` cũ nằm sát `Tasks now` tạo hai chỗ "công việc" — Claude đề xuất gỡ menu `Tasks` cũ theo đúng cách (a). Mục (c) là mở rộng phạm vi → **OWNER** quyết, Host không tự ghi vào §0.
- P02 · Scope §0 Nhiệm vụ 6 + Tiêu chí 2, 4 · ACCEPTED · Gốc rễ của "lớp mỏng": nội dung HTML lấy từ Git đã rõ, nhưng danh sách việc + trạng thái Đang làm/Đã xong chưa nói lấy ở đâu; nếu ghi trạng thái ở Directus/VPS thì VPS thành SSOT thứ hai, trái §0.6. Đề nghị thêm vào §0: danh sách, tên, trạng thái việc đều đọc từ Git (COLLAB gốc/COLLAB từng việc), VPS chỉ đọc và hiển thị; chuyển sang Đã xong không đổi thư mục/URL (ID ổn định, link cũ vẫn mở). Ghi thêm ràng buộc: việc này là lần đầu hiện thực A8 + README §12 (nginx `default.conf` chưa có vùng Owner View, chỉ có `/ui-preview/` của xưởng vẽ); mã Nuxt/dịch vụ Cập nhật theo §11 (sửa trên VPS, dựng tại chỗ, đẩy bản sao lên GitHub).
- P03 · Scope §0 Tiêu chí xong 1, 3, 5 · PARTIAL · Đề nghị tiêu chí đo được: (a) README §12.3 chỉ cho nút Cập nhật kéo 1 file HTML → HTML có ảnh sẽ vỡ (MMIM: HTML 1,8 MB + 16 ảnh, xem MMIM P02); tiêu chí: view hiển thị đủ HTML chính + asset khai báo trong thư mục việc, và việc này được đề xuất sửa §12.3 qua D gốc + Owner quyết; (b) việc chưa có HTML chính (hiện: `mcp-workspace` và chính việc này) hiện "chưa có view"; tạo HTML cho việc khác không thuộc phạm vi; (c) "tìm kiếm chuẩn" = gõ tên/mã/chữ trong nội dung view → lọc ngay, lọc theo Đang làm/Đã xong; (d) thử thật với danh sách ≥300 việc; (e) "hội đồng GPT · Claude · Hermes review" sẽ treo vì Hermes chưa nối (DROOT02, HJW chờ R03) → sửa thành "GPT · Claude review; Hermes khi đã nối".
- P04 · Scope đầu file · PARTIAL · Thiếu dòng `Host · Host_ID` (A2) và `HTML chính` (A8) như các việc khác; thiếu Host_ID thì theo A2 mọi phiên mặc định là Reviewer. Tên `hpml-view-for-user` có vẻ gõ nhầm `html`; đổi lúc này chỉ tốn 1 `fs_move` + 1 dòng COLLAB gốc, đổi sau khi có URL Owner View thì link gãy. Đề nghị `work/owner-view/` (thuật ngữ chuẩn A8/README §12); Host đổi khi Owner gật.

Reviewer vòng 2 (HVU01): Claude Chat · Based_on `c5117f8` · Đã đọc: §0 HVU01, K1–K8, Host xử lý P cũ, AGENTS A0–A8, README §11–§12. Thực địa (chỉ đọc): clone `/opt/incomex/mcp-roots/gh`, nginx `default.conf` khối `/ui-preview/`. Chưa đọc: mã trang Knowledge 2 cột (để bước khảo sát K8.2). Không mở lại P01–P04 Host đã xử lý.

- P05 · Scope K1/K3/K7 — câu hỏi 1 (dùng đồ có sẵn) · OPEN · VPS đã có clone repo chạy thật (`/opt/incomex/mcp-roots/gh`, pull main mỗi lần đọc) → mô hình “clone + đọc file” đủ để có nội dung mới, không cần webhook. Đề nghị V1 chỉ gồm 3 mảnh: (1) MỘT clone chỉ-đọc riêng cho Owner View (không dùng clone của connector vì clone đó đang ghi/push), cập nhật bằng `git pull --ff-only` khi Owner bấm Cập nhật hoặc khi mở trang mà index cũ hơn ~10 phút; (2) MỘT script sinh `tasks-index.json` từ chính clone đó (gồm luôn khối A0 để K2 không cần wrapper riêng); (3) MỘT location nginx kiểu `/ui-preview/` phục vụ tĩnh — CSP hiện dùng `frame-ancestors 'self'` + `X-Frame-Options SAMEORIGIN`, cùng host nên KB iframe được ngay, không phải sửa CSP. Không endpoint webhook, không secret GitHub mới, không cron nền. Đã cân nhắc và loại: trình duyệt đọc thẳng `raw.githubusercontent.com` (trả text/plain nên không iframe được, asset tương đối gãy, phụ thuộc repo còn public).
- P06 · Scope K2/K3/K5/K6/K7/K8 — câu hỏi 2 (dựng thừa) · OPEN · Cắt 6 chỗ: (a) K3 webhook/event → V2, V1 kéo theo yêu cầu như P05; (b) K6 bỏ khung validator riêng, gộp đúng 2 phép kiểm cứng vào chính script index (A0 chưa xác nhận mà đã có READY/RUN; `READY@SHA` lệch commit cuối chạm `PROMPT.md`); (c) K5 bỏ trường `current actor` khỏi UI V1 — ô trống/`unknown` không cho Owner thêm thông tin, thay bằng “commit gần nhất: ai · lúc nào”; (d) K7 rút 5 filter còn `Now/Done` + ô tìm (lọc theo next actor là miễn phí nếu đã suy được, không cần thêm UI); (e) K2 bỏ wrapper đọc A0 riêng, dùng JSON ở (2); (f) K8.3 slice 2–3 task → làm luôn cả 6 việc đang có, chi phí như nhau nhưng thấy đủ mọi trạng thái (có/không HTML chính, HTML 1,8 MB kèm ảnh, việc có READY/RUN).
- P07 · Scope K4 — câu hỏi 3 (parser có đáng tin không) · OPEN · Đủ tin, với điều kiện chỉ đọc 4 dấu hiệu AGENTS đã bắt buộc và tuyệt đối không đoán văn xuôi: (1) `Xác nhận User: ĐÃ/CHƯA XÁC NHẬN` (A0); (2) trạng thái P `OPEN/OWNER/ACCEPTED/PARTIAL/REJECTED` (A3); (3) `READY@<40 ký tự>` so với commit cuối chạm `PROMPT.md` (A6); (4) `git log -1 -- work/<id>/` cho “vừa xong bởi ai, lúc nào” qua tiền tố `[GPT]/[Claude]/[Owner]` (A4). `Next actor` chỉ 3 giá trị: **Owner** (A0 chưa xác nhận hoặc có P `OWNER`) · **Agent** (READY khớp SHA) · **Host** (còn lại). `Now/Done`: lấy từ COLLAB gốc — thêm mục `## Đã xong` bên cạnh `## Đang làm` (Host vốn đã duy trì danh sách này), không đổi thư mục/URL, không thêm metadata mới → khớp §0 nhiệm vụ 8. Hai luật hiển thị bắt buộc: thiếu dấu hiệu thì hiện `?` chứ không suy đoán; mọi nhãn suy ra đều hiển thị kèm bằng chứng thô (hash + dòng commit) để Owner nhìn là biết đúng/sai, sai cũng vô hại. Không đòi AI báo thêm bất kỳ thông tin nào ngoài những thứ A0/A3/A4/A6 đã bắt buộc.
- P08 · Scope §0 tiêu chí V1 + K3/K6 — câu hỏi 4 (hoãn V2) · OPEN · Hoãn hẳn sang V2: webhook/event-driven, khung validator + GitHub Actions/required checks, `current actor`/heartbeat/harness, tìm toàn văn nội dung HTML, checkpoint riêng từng việc, auto-dispatch. Về README §12.3: đề nghị **không** đổi sang event-driven lúc này; chỉ sửa một câu — nút Cập nhật kéo **cả thư mục việc** (tài liệu, vùng không thực thi) thay vì đúng 1 file HTML. Một câu này đồng thời xử lý ảnh/asset (P03a) và giữ nguyên hai nguyên tắc đang có: không đồng bộ nền, và cấm GitHub → VPS đối với mã/runtime (§11). Đây là D gốc + Owner chốt, nhỏ hơn nhiều so với thay đổi event-driven trong K3.

## Host xử lý P cũ
- P01 PARTIAL: nhận đề nghị không xoá dữ liệu/mã Modules và không buộc route mới; mục `Tasks` cũ chỉ xử lý menu sau khi review, không xoá data/route ở V1.
- P02 ACCEPTED: danh sách/trạng thái phải dẫn xuất từ Git/workspace; VPS không là SSOT thứ hai.
- P03 PARTIAL: nhận yêu cầu view phải xử lý asset thực tế và việc chưa có HTML phải hiện rõ; search V1 ưu tiên metadata/mục tiêu trước, chưa khóa yêu cầu full-text toàn HTML hay bài benchmark ≥300 task nếu vertical slice cho thấy chưa cần.
- P04 PARTIAL: đã bổ sung Host/Host_ID/`view.html`; giữ tên folder `hpml-view-for-user` vì Owner đã chỉ định trực tiếp, không đổi tên chỉ vì lỗi chính tả tiềm năng khi chưa có lợi ích nghiệp vụ.

## Owner cần quyết
- Chưa có quyết định mới bắt buộc trước vòng review Claude. Nếu K3 được đồng thuận, bước sau phải ghi D gốc để Owner chốt việc đổi README §12.3 từ refresh thủ công sang refresh tài liệu theo event, vẫn giữ tuyệt đối cấm GitHub → VPS đối với mã/runtime.
