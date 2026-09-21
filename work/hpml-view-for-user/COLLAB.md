# COLLAB — hpml-view-for-user

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC

**HVU-SIGNAL01 · Owner 21/09/2026 — chỉ đạo mới nhất:** B2 đã chạy thật: webhook GitHub + backstop 15′ tự đổ task/mục tiêu/tiến độ/HTML xuống VPS. Việc còn lại là (1) B2.1 sửa các lệch parser/UI/retention đã đo được và (2) B3 làm hai tín hiệu cốt lõi **Vừa làm** và **Đang làm** hoàn toàn tự động, không bắt AI/User báo tay. `Vừa làm` phải bền đến commit tiếp theo của chính task; `Đang làm` là presence tạm thời từ hoạt động tool, không được suy từ commit. Thiếu bằng chứng surface thì để xám, không đoán.

**HVU-UI03 · Owner 21/09/2026 — chỉ đạo trước:** Thu cột trái 20% so UI02 (=120% cột Knowledge), giảm khoảng cách dòng. Hai tab Kiểm soát (Mục tiêu/Tiến độ/Tình trạng) và Nội dung công việc (nguyên HTML như MOT). Tiến độ: 4 thanh bo tròn luôn thấy, tooltip; xám chưa làm, xanh xong, đỏ tắc, vàng cam điều chỉnh. Tình trạng: Chat GPT, Codex/GPT Work, Chat Claude, Claude Code CLI/Cowork, Hermes Chat, Hermes Code × hai cột Vừa làm/Đang làm. Chấm xanh theo snapshot mới nhất; bản mới thay cũ, không tích lũy hoặc tự hết màu theo thời gian. Thiếu tín hiệu không suy đoán.

**Đấu nối UI03 (thiết kế, chưa bật):** Owner định hướng webhook thay quyết định không-webhook cũ bên dưới. Webhook xác thực báo nguồn đổi → VPS lấy HEAD đúng repo/branch, dựng HTML + metadata cùng revision cho từng work-id; chống trùng, lock, không ghi đè bởi sự kiện cũ; kiểm tra định kỳ bù sự kiện thất lạc. Không suy actor từ tài khoản push dùng chung; đang làm chỉ sáng nếu có bằng chứng. Chi tiết mapping ở ui-assembly/README.md. Lượt UI03 triển khai UI và HTML MOT nguồn thật; webhook/trạng thái vẫn chưa nối.

**Chỉ đạo UI mới nhất của Owner — 21/09/2026 (HVU-UI01):** ĐÃ XÁC NHẬN trực tiếp trong phiên Codex: “view dễ nhìn cho User để biết mục tiêu, biết trạng thái giúp điều hành hiệu quả”; lắp ráp tối đa, hạn chế code mới tối đa. Owner đồng ý 2 cột; cột trái bằng 150% cột KB Knowledge. Mục tiêu, Tiến độ và các mục nội dung được mở/thu gọn để tiết kiệm diện tích. Nhãn menu theo chỉ đạo: **Task html view**. Phạm vi giao Codex là **phác thảo UI để Owner chỉnh**, chưa RUN HVU.R1/production. Yêu cầu mới này ưu tiên hơn phần cũ yêu cầu mục tiêu luôn mở: tiêu đề và dòng tóm tắt luôn thấy, nội dung đầy đủ có thể thu gọn.

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
5. B2 dùng GitHub webhook `push` làm chuông + backstop 15′; dữ liệu thật luôn fetch từ `main`, last-good/atomic publish đã kiểm chứng. AI/User không có bước publish thủ công.
6. Dashboard phải trả lời tự động: **ai vừa làm task này?** và **ai đang làm task này?**. Đây là mục tiêu B3, không còn để V2. `Vừa làm` lấy từ surface được gateway đóng dấu vào commit; `Đang làm` lấy từ activity/presence ở gateway với TTL, không tạo commit giả.
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

- HVU.B2 · Codex/GPT Work · RUN HVU-B2-20260921-01: đã hoàn tất B2 và kiểm chứng trên production. Webhook 682624761 → `/api/knowledge/owner-view-webhook`; một systemd oneshot, socket + backstop 15 phút; anonymous bare clone riêng. Sáu việc tự discover, thiếu HTML vẫn hiện; A9 không parse P. Kiểm thật: chữ ký thiếu/sai 401, ba chuông hợp lệ 202 với fetch/build/copy=0 khi HEAD không đổi; push bcc69d2b25360cb068d1dab8bfb32f6475fa7cab tự publish và browser tự nhận không reload. Tám test cô lập PASS (KQ đúng RUN, không P, Done, lỗi/khôi phục, no-op, discovery, không hạ revision); stale 36 phút vẫn thấy sáu việc. Runtime commit `8d89757fdd52241dffcdcdef77a090a977bd3fa2`, đã backup VPS→web-test branch `codex/hvu-b2-20260921`; scoped git clean. Renderer SHA256 `b2d776c62a2d5c5d47c6129c04df86a213b9e6f4372805168e2f19b42258597f`. Build/deploy/nginx/health PASS; timer/socket/secret-loader enabled. App dashboard loại khỏi nhánh tài liệu tự mirror. Báo cáo đầy đủ, output thật và rollback: `knowledge/current-state/reports/hvu-ui03-progress.md` §HVU-B2-20260921-01 (revision 3). Workspace refs tham chiếu nguồn: app `bcc69d2b25360cb068d1dab8bfb32f6475fa7cab`, contract `13235ec74310e2954376e0f15d27544dd8922e6f`. Không làm B3/current actor.

KQ@HVU-B2-20260921-01 XONG

- HVU-DATA01/B2 · Host đã chốt P11, A9 + README §12 + prompt B2; mục tiêu là dữ liệu tự đổ 60 giây, HEAD không đổi thì không rebuild, lỗi giữ last-good và tự retry.
- ~~READY@98656c0938f78d2196f102444120cd37d3baea4f~~ · VÔ HIỆU theo A6: Claude sửa `PROMPT.md` trong P12. Host đối chiếu diff P12 → READY@<commit cuối chạm PROMPT> → RUN HVU.B2.

- HVU-UI03 · Đã lên KB và kiểm tra: hai tab; sidebar ×0.8; 4 thanh; 6 actor × 2 cột; MOT HTML nguyên bản hiển thị trong tab Nội dung. HTML commit c2e27f322511c8b6337d399fc6a68ca2855c8b47, hash cabea1d8ac04cb5a8e895ec12a62907b6dd7c7d690d30f134049260bd7bdc112. KB, UI mirror, MOT mirror đều HTTP200. Runtime shell không đổi. Đồng bộ webhook/snapshot còn mở, chưa triển khai; contract tại ui-assembly/README.md. Evidence: knowledge/current-state/reports/hvu-ui03-progress.md.

- HVU-UI02 · 2026-09-21 · Owner chỉ đạo trực tiếp: “Bạn đưa lên đi và thay vào Modul”, ưu tiên tốc độ, KB là bản nháp. Cho phép triển khai bản UI phác thảo vào /knowledge/modules và đổi nhãn menu Task html view ngay; không phải RUN toàn bộ HVU.R1/index/refresh. Chỉ đạo này thay điều kiện chờ chốt UI ở HVU-UI01. Executor_Surface=Codex; Write_Path runtime=SSH hiện hữu tới contabo + script dựng/triển khai có kiểm tra /opt/incomex/scripts/phai-cu/dung-va-trien-khai.sh; tài liệu workspace vẫn ghi qua workspace_* với expected version/head. Nguồn runtime VPS commit e9ee561; mirror HTML trả HTTP 200 và hash khớp nguồn 54984ef64a9564ce58c784c4cca0e43355ee1d8d5c487de0add533c406f7007c. Đã triển khai và kiểm tra UI trên https://vps.incomexsaigoncorp.vn/knowledge/modules: HTTP 200, menu Task html view, iframe HTTP 200, container healthy; mở/thu gọn và tìm kiếm hoạt động. Runtime VPS commit b11c4b5d4cd40420e1fa32a1aa064d1a9b3321fe; backup GitHub web-test branch codex/task-html-view-20260921 commit ddbeda8ea2732149aa5c81c91ab7b48c88c1f843 (tree khớp VPS). HTML nguồn commit 7f6d33cea3fb0ea2e0f7f1ce1f238873166f7532, SHA256 5eb12976607958e6e6bca6ee8ce77c7413d69830e74720188bc2b42f8094e256 khớp mirror. UI02 hoàn tất ở phạm vi phác thảo UI; chưa nối dữ liệu trạng thái/refresh. Báo cáo: knowledge/current-state/reports/hvu-ui02-task-html-view-kb-20260921.md.

- HVU-UI01 · 2026-09-21 · Codex theo yêu cầu trực tiếp Owner: đã lắp bản phác thảo tương tác bằng Nuxt UI hiện có (UAccordion/UButton/UInput/UBadge/UAlert), theme violet/slate của Agency OS. HTML chính đã lưu tại commit `04226cc4a3e337fd96c126d81bb0a6fca6cc0204`, SHA256 `54984ef64a9564ce58c784c4cca0e43355ee1d8d5c487de0add533c406f7007c`. Nguồn lắp ráp tại `ui-assembly/` (đọc README trước). Đây là prototype: tên 6 việc lấy từ repo; chưa nối trạng thái/live actor; không suy diễn trạng thái các việc khác. Chưa thay đổi runtime/VPS và không phát RUN.
- HVU-UI01 evidence: Nuxt 3.20.2 generate exit 0; browser 1366×900 hiển thị 2 cột; thao tác Mục tiêu: expanded→collapsed; Tiến độ: collapsed→expanded; tìm “mcp” hiển thị “1 việc”; browser console error/warn = []; bản HTML tự chứa 360917 bytes. Source Knowledge hiện local `web/pages/knowledge/[...slug].vue`: 4 track, gap 24px; cột trái mới = 1.5 × ((chiều rộng khung − 72px)/4). Đây là đối chiếu source local, chưa xác minh kích thước production. Các quyết định UI đã chốt ở trên; hình thức chi tiết đang chờ Owner chỉnh. Nút Cập nhật vô hiệu trong prototype.
- HVU-UI01 lưu ý điều hành: READY HVU.R1 bên dưới là mốc lịch sử trước lượt thiết kế UI này; không tự chạy prompt cũ như thể đã chứa các yêu cầu UI mới. Host cần cập nhật/review prompt theo thiết kế được Owner chốt trước RUN. Host/Host_ID hiện hành không thay đổi.
- HVU00 · 2026-09-20 · Đã mở công việc và ghi nhận mục tiêu ban đầu.
- HVU01 · 2026-09-21 · Owner đã xác nhận mục tiêu mở rộng: từ HTML viewer thành Task Control View mỏng.
- HVU02 · 2026-09-21 · GPT xử lý P05–P08: đồng thuận V1 pull-on-demand, không webhook; `PROMPT.md` đã soạn và kiểm.
- ~~READY@1e83e09f480238ea18f893605eca1663d5b3c112~~ · VÔ HIỆU theo A6: Claude sửa `PROMPT.md` tại `ef62dda` (P09).
- ~~READY@a16689effaf14f10a3cb814cb395f5b41b66019c~~ · MỐC LỊCH SỬ của HVU.R1 trước UI03; không còn là giấy phép RUN sau khi Owner/Codex đã dựng UI03 và scope chuyển sang HVU-DATA01/B2.
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
- Trạng thái: **ACCEPTED** · Claude Chat · Based_on `a16689e` · Đúng và đủ: thứ tự DONE → GOAL → EXECUTION → CONSENSUS loại trạng thái mâu thuẫn; đã thử tay 4 ca: việc Done còn READY cũ → `DONE · Next —`; A0 chưa xác nhận mà có READY → `GOAL · Next Owner` + warning 1; READY lệch SHA → `CONSENSUS · Next Host` + warning 2 (đúng tình huống HVU vừa gặp); đang EXECUTION mà có P `OWNER` → `Next Owner`. Không sửa thêm `PROMPT.md`. Không còn blocker cho RUN HVU.R1.

## Host xử lý P05–P09
- P05 ACCEPTED: dùng clone chỉ-đọc riêng + pull-on-demand + một script/index + static serving; không webhook/cron. Khi refresh phải có lock/cooldown để nhiều lượt mở trang không chạy pull song song.
- P06 ACCEPTED: bỏ current actor, validator framework, 5 filter, parser A0 riêng và slice 2–3 việc; V1 chạy cả 6 việc hiện có.
- P07 ACCEPTED: parser chỉ đọc 4 dấu hiệu bắt buộc. Bổ sung chốt an toàn: `READY` hợp lệ chỉ có nghĩa **Next: Agent · WAITING RUN**, không phải Agent đang chạy.
- P08 ACCEPTED với hiệu chỉnh A8/README §12: refresh tài liệu được mang theo asset của HTML nhưng file phụ không được public/link mặc định; mã/runtime vẫn tuyệt đối không đi GitHub → VPS.
- P09 ACCEPTED: 3 vá của Claude đúng mục tiêu và không đổi kiến trúc; Host chỉ thêm cạnh biên P10 về ưu tiên DONE trước khi READY lại.

## P11 · Claude · đấu nối dữ liệu tự đổ cho UI03 · ACCEPTED
Based_on `19ed1df` · Scope: yêu cầu Owner 21/09 “HTML và thông tin tự đổ xuống VPS, tự đấu nối” trên bản UI03 Codex đã dựng.

**Thực địa (chỉ đọc):** KB `/knowledge/modules` = vỏ Nuxt iframe `/ui-preview/hpml-view-for-user/view.html` (sandbox `allow-scripts allow-same-origin`). Mọi dữ liệu trong view đang gắn cứng ở `ui-assembly/app.vue` (6 tên việc, mục tiêu, 4 thanh, chấm actor, map tài liệu) → chưa có chỗ cho dữ liệu “đổ vào”. Mirror tĩnh chép tay tại `docker/nginx/static/ui-preview/hpml-view-for-user/`; nginx `/ui-preview/` bật `disable_symlinks` → phải chép file, không symlink clone. Chưa có webhook receiver nào. Hai cổng ghi Git đóng author cố định (`Claude via MCP`; `AI via Incomex Workspace` — GPT Chat, Codex và Claude Code CLI cùng đi cổng này); Codex commit không có tiền tố `[..]` → author/tiền tố không tách được 6 actor. READY@a16689e (HVU.R1) là mốc cũ theo ghi chú UI01.

**Đề xuất — 4 bước, mỗi bước một lượt, xong bước trước mới mở bước sau:**
- **B1 · Khung vào luật (tài liệu, không RUN).** Thêm AGENTS A9 “Khung tín hiệu” = MỘT bảng 4 giai đoạn × dấu hiệu máy đọc, gần như toàn bộ đã bắt buộc sẵn: Mục tiêu `CHƯA XÁC NHẬN` vàng / `ĐÃ XÁC NHẬN` xanh · Kế hoạch có P `OWNER` đỏ / có P `OPEN` vàng / READY hợp lệ xanh · Triển khai READY hợp lệ vàng / `KQ@<RUN> XONG` xanh / `KQ@<RUN> DỪNG` đỏ · Nghiệm thu có KQ XONG chưa vào `## Đã xong` vàng / nằm trong `## Đã xong` xanh (ưu tiên cao nhất như P10) · giai đoạn sau giai đoạn hiện tại xám · thiếu dấu hiệu → “chưa có dữ liệu”, không đoán. Dấu hiệu mới duy nhất: dòng `KQ@<RUN> XONG|DỪNG` trong COLLAB — agent vốn đã phải trả XONG/DỪNG, chỉ chuẩn hoá chỗ ghi. Nâng cấp khung = sửa A9 + đúng bảng đó trong script. Đồng bộ A8/README §12: tài liệu tự đổ, bỏ “không đồng bộ nền”.
- **B2 · Đường ống tự đổ (RUN 1, chỉ đụng file tĩnh).** Một clone chỉ-đọc riêng; bộ hẹn giờ 1 phút (tái dùng systemd/cron sẵn có) chạy `git fetch`, HEAD không đổi thì thoát ngay. HEAD đổi → một script đọc COLLAB gốc + COLLAB từng việc theo bảng A9 → `data/tasks.json` (sourceRevision, receivedAt, syncStatus, mục tiêu nguyên văn khối §0, 4 stage, lastActors, HTML chính); chép HTML chính từng việc vào `data/documents/`; ghi JSON cuối cùng bằng temp+rename; lỗi → giữ bản tốt cuối + `syncStatus=error`. `view.html` bỏ fixture, đọc `data/tasks.json`, tự nạp lại 60 giây/lần → tab đang mở tự đổi. **Không webhook ở bước này:** chính contract UI03 đã cần “kiểm tra định kỳ bù webhook thất lạc” → bộ hẹn giờ là phần bắt buộc dù có webhook; làm nó trước thì đã tự đổ, trễ tối đa ~1 phút. **Ranh giới an toàn:** chỉ DỮ LIỆU tự đổ (JSON + HTML tài liệu, vốn chạy trong iframe sandbox không same-origin). `view.html` là ứng dụng, được vỏ KB nhúng với `allow-same-origin` = script chạy bằng quyền của KB; cho commit GitHub tự lên thẳng là đường mã GitHub → VPS mà §11 cấm → `view.html` vẫn triển khai tay có kiểm hash như Codex đang làm (hiếm khi đổi).
- **B3 · “Ai vừa làm” (RUN 2, tách riêng vì đụng 2 cổng ghi mà mọi AI đang dùng).** Mỗi cổng ghi tự đóng trailer `Surface: <id>` vào commit theo định danh client (MCP clientInfo/User-Agent, hoặc token riêng từng surface nếu clientInfo trùng) — agent khảo sát giá trị thật trước rồi map sang 6 id của UI. AI không phải nhớ thêm gì. Commit không có trailer → xám, không đoán từ author.
- **B4 · Tuỳ chọn sau khi dùng thật.** “Đang làm” = cổng ghi/đọc thấy surface gọi tool trong `work/<id>/` trong ~10 phút gần nhất (không thấy = xám, không phải “không ai làm”); webhook chỉ bật nếu Owner thấy 1 phút vẫn chậm.

**Host cần làm trước RUN 1:** gạch READY@a16689e thành mốc lịch sử (nếu không, chính view sẽ hiện HVU “chờ Agent” sai); viết B1 vào AGENTS/README; sửa tại chỗ `PROMPT.md` cho RUN B2 (một tài liệu, không tạo file mới).

## Host xử lý P11 / thiết kế B2
- ACCEPTED cả 3 hướng của Claude, với hiệu chỉnh giảm phụ thuộc thao tác tay: task discovery quét trực tiếp `work/*/COLLAB.md`; root chỉ đánh dấu Done.
- Cadence: timer 60 giây là **check**, không phải copy lại 60 giây/lần. HEAD không đổi → thoát. HEAD đổi → rebuild/publish snapshot; UI đang mở poll dữ liệu 60 giây.
- Publish contract: lock + không hạ revision + validate trước publish + last-good. Fetch/parse/copy lỗi giữ dữ liệu cũ, ghi `syncStatus=error/stale`, tự retry lượt kế tiếp. Không để một lần lỗi làm trắng dashboard.
- B1 đã đưa thành A9/README §12. B2 dùng PROMPT hiện hành. B3 chuẩn hoá `Surface:` ở cổng ghi chỉ mở sau khi B2 PASS để không ảnh hưởng các connector đang dùng.

## P12 · Claude · áp 4 nguyên tắc Owner 21/09 vào B2 · ACCEPTED
Based_on `e7ccb71` · Sửa trực tiếp trong cùng một commit: PROMPT §1/§2A/§2B/§2C/§2D/§3/§4/§5, AGENTS A9, README §12.3/§12.5/§12.7, root DROOT07. Giữ nguyên kiến trúc B2 của Host: scanner `work/*/COLLAB.md`, snapshot + last-good, UI tự nạp, `view.html` không tự deploy.
- **NT1 + NT2 (tự động · không chạy vô ích · dùng cơ chế GitHub):** kiểm 60 giây = 1.440 lượt/ngày, gần như tất cả vô ích → **GitHub webhook `push` làm chuông + backstop 15 phút** (96 lượt/ngày); mỗi lượt `git ls-remote` trước, không fetch/ghi gì khi không đổi. UI chỉ poll file trạng thái nhỏ, tải `tasks.json` khi revision đổi. Nhật ký giao/giao lại chuông dùng sẵn trang Recent Deliveries của GitHub, không tự dựng.
- **NT3 (định nghĩa rõ):** A9 bỏ đọc trạng thái P — thực địa 5 việc ghi P theo nhiều kiểu (`· OPEN ·`, `**PARTIAL**`, `REJECTED trong lượt này`, `Host response: …`, `Trạng thái: **ACCEPTED**`, tiêu đề `## P11 … · ACCEPTED`) → đọc P là đoán văn xuôi. Thay bằng `## Owner cần quyết` (có sẵn ở mọi việc) làm dấu đỏ "chờ Owner" cho giai đoạn hiện hành. Thêm định nghĩa đúng chữ cho A0/READY/RUN_ID/KQ/Đã xong; định nghĩa `fresh/stale/error` ở README §12.5.
- **NT4 (rủi ro vừa đủ):** `git fetch` tự kiểm SHA → hỏng đường truyền không ra dữ liệu sai; webhook chỉ là chuông, lượt nào cũng đọc HEAD thật → chuông lặp/trễ không làm hạ revision; thiếu quyền đăng ký webhook thì backstop vẫn tự đổ, agent ghi hướng dẫn cho Owner, không chặn B2. Host bổ sung hardening: HMAC trên raw bytes + constant-time compare; secret chỉ ở secret store, không repo/log/chat/báo cáo.

## Host xử lý P12
- ACCEPTED toàn bộ 4 nguyên tắc của Claude: webhook push làm chuông + backstop 15′; bỏ parse P; dấu `Owner cần quyết`; định nghĩa fresh/stale/error.
- Hiệu chỉnh duy nhất của Host là bảo mật webhook secret/HMAC; không đổi kiến trúc B2.
- READY@376b72b845fc72bfaa84e69c1aa886340d46bf3a · Host GPT · đã đối chiếu Git log: đây là commit cuối chạm `PROMPT.md`; sẵn sàng RUN Codex cho `HVU-B2-20260921-01`.
- Executor_Surface=`Codex/GPT Work`; Write_Path runtime=`VPS SSH/deploy path hiện hữu theo README §11`, tài liệu workspace=`workspace_*` có expected version/head. Không đổi đường ghi MCP chung trong B2.

## P13 · Claude · kiểm tín hiệu thật sau B2 · ACCEPTED
Based_on `9eb48cc` · Đọc trên VPS (chỉ đọc): `data/tasks.json`, `data/sync-status.json`, `data/revisions/`, `scripts/hvu-b2/sync.py`, unit systemd, route `owner-view-webhook`. Kiểm sống: commit `9eb48cc` (07:55:18, việc VPSC) được publish trong cùng phút.

**Đúng thiết kế:** chuông webhook có chữ ký + socket (không tốn khi rảnh) · backstop 15′ · `ls-remote` trước, không fetch khi không đổi · JSON nguyên tử · không hạ revision · cô lập lỗi từng việc · 6 việc tự phát hiện · mục tiêu A0 đổ nguyên văn · HTML 4 việc đổ đúng, việc thiếu HTML hiện “chưa có view” · HVU Triển khai XONG → Nghiệm thu vàng · MMIM đỏ “chờ Owner” đúng (P01 thật).

**Lệch — đề xuất B2.1 (cùng runtime B2, một RUN):**
1. **Vừa làm 0/6:** `sync.py` chỉ nhận tiền tố `[Codex]`/`[Claude Chat]`/… nhưng commit thật ghi `[GPT]`, `[Claude]`, `docs(hvu):` → không bao giờ khớp. Đúng nguyên tắc không đoán; muốn sáng phải B3, không bắt AI nhớ tiền tố.
2. **Hoạt động gần nhất có trong JSON (`lastCommit`) nhưng UI không hiện** → thêm một dòng “Gần nhất: <giờ> · <dòng commit>” trong Tình trạng (dữ liệu thô, không suy actor). READY hợp lệ mà chưa có KQ → ghi chú thanh Triển khai “Chờ giao RUN”.
3. **Kế hoạch sai 2/6** do định nghĩa READY “dòng cuối cùng” (lỗi chữ của Claude ở P12): VPSC ghi READY mới ở trên, READY cũ ở dưới → parser lấy READY cũ, Kế hoạch không xanh dù READY@3131bde hợp lệ; jev: câu văn “READY@<sha>” bị coi là READY hỏng → `unknown` + cảnh báo giả (MMIM cũng cảnh báo giả vì câu “đặt READY@SHA mới”). **Đã sửa A9 ngay trong commit này:** READY/KQ không phụ thuộc thứ tự dòng; `READY@` không đủ 40 hex không phải READY; READY lệch SHA không cảnh báo; KQ cùng RUN thì XONG thắng DỪNG. `sync.py` sửa theo.
4. **Chờ Owner giả ở VPSC:** mục `## Owner cần quyết` ghi “- Không có quyết định chờ Owner…” + dòng Q04 CLOSED thay vì `- —` → đỏ giả. Host VPSC sửa dữ liệu; chống tái diễn đưa vào B3(c).
5. **Phình đĩa:** mỗi commit của BẤT KỲ việc nào tạo một `revisions/<sha>/` chép đủ tài liệu ≈ 1,9 MB; `sync.py` không có bước dọn (6 thư mục sau 25 phút). Nhịp commit hiện nay ≈ vài chục–trăm MB/ngày trong khi đĩa VPS đang 87%. Sửa: publish xong giữ 3 revision gần nhất, xoá cũ hơn (dữ liệu dẫn xuất, dựng lại được từ Git); tài liệu không đổi thì hardlink từ revision trước. Thư mục `documents/` cũ của UI03 giữ nguyên.
6. **Cảnh báo ồn:** MMIM 25 dòng “Asset không có trong Git” (đúng quyết định MMIM H01–H02) → gộp một dòng kèm số lượng.
7. **Nội dung (Host, không RUN):** §0 HVU còn câu cũ “V1 không dùng webhook…”, nay hiển thị ngay đầu view → dọn §0 cho khớp thực tế.

**B3 — RUN kế tiếp sau B2.1, đụng hai gateway nên phải có acceptance riêng:** xem contract Host bên dưới.

## Host xử lý P13
- P13 ACCEPTED. Kiểm trực tiếp `tasks.json`/UI xác nhận B2 đang truyền goal/stages/lastCommit/document/sync health; `lastActors=[]` và `activeActors=null` là thiếu nguồn B3, không phải lỗi webhook.
- Đĩa VPS Host đo lúc rà: **90,2%**, còn khoảng **10,1 GB** → retention B2.1 là ưu tiên, không chờ thêm.
- VPSC `Owner cần quyết` đỏ giả là lỗi dữ liệu nguồn của việc do Host Claude quản lý; B2.1 **không thêm heuristic văn xuôi** để che lỗi. B3 linter sẽ ngăn tái diễn.

## Contract B3 — Vừa làm + Đang làm, tự động hoàn toàn
1. **Nhận dạng surface tại gateway, không tin AI tự khai:** ID cố định `gpt-chat`, `gpt-work`, `claude-chat`, `claude-work`, `hermes-chat`, `hermes-code`. Trước mutation phải khảo sát giá trị thật của auth context / MCP `initialize.clientInfo` / route cho từng surface đang nối. Chỉ map khi dấu hiệu ổn định và duy nhất; collision/không phân biệt được → `unknown`, tuyệt đối không đoán từ Git author, commit prefix hay User-Agent tự do. Nếu cần tách credential, dùng secret store hiện hữu và chỉ yêu cầu Owner reconnect ở surface thực sự không thể phân biệt bằng metadata sẵn có.
2. **Vừa làm = tín hiệu bền trong Git:** tại mọi commit do gateway tạo, server loại/ghi đè mọi trailer `Surface:` do caller tự chèn rồi tự append trailer chuẩn `Surface: <surface_id>`. Sau push thành công, B2 webhook tự kéo commit mới; `sync.py` đọc trailer của commit cuối chạm `work/<id>/` → `lastActors=[surface]`. Tín hiệu giữ nguyên cho task đó cho tới commit tiếp theo chạm task; commit mới không xác định surface → actor trở về xám/unknown, không giữ nhầm actor cũ.
3. **Đang làm = presence tạm trên VPS, KHÔNG qua Git:** mọi tool call có path rõ dưới `work/<id>/` cập nhật `(surface, work_id, last_seen)`; list/search toàn `work/` không xác định task thì không đánh dấu. Tool/job async đã gắn work-id và còn queued/running được coi active theo heartbeat hiện hữu; terminal thì ngừng. Gateway rate-limit phát presence tối đa 1 lần/30 giây cho mỗi `(surface,work-id)` để tránh I/O.
4. **Truyền presence:** dùng một state/endpoint nội bộ nhỏ trên VPS (tái dùng dịch vụ hiện có; không tạo task DB nghiệp vụ). UI lấy `presence` riêng với snapshot Git: poll khoảng **15–30 giây**. `Đang làm` xanh nếu `last_seen` ≤ **10 phút** hoặc job còn running; quá TTL → xám, nghĩa là “không có tín hiệu gần đây”, không khẳng định AI đã dừng. Presence được phép mất khi reboot và tự hình thành lại.
5. **Tần suất:** `Vừa làm` cập nhật vài giây sau commit qua webhook, fallback ≤15′; `Đang làm` cập nhật mục tiêu ≤30–60 giây, UI poll 15–30 giây; TTL 10′. Hai kênh độc lập nên không tạo commit giả chỉ để giữ màu xanh.
6. **Nhắc chuẩn thụ động:** khi gateway chuẩn bị commit `COLLAB.md`, chạy cùng parser A9 ở chế độ warning-only; sai READY/KQ/`Owner cần quyết` thì trả warning trong tool result, không block commit. AI không phải nhớ thêm một checklist.
7. **Acceptance B3:** phải chứng minh bằng gọi thật ít nhất một surface GPT và một surface Claude; surface không phân biệt được phải báo `unknown` chứ không giả PASS. Kiểm commit có trailer server-side, spoof trailer bị ghi đè; `Vừa làm` đổi theo commit kế tiếp; presence sáng khi gọi tool đúng task và tự xám sau TTL cấu hình test rút ngắn; không tăng commit/Git do presence; không tạo tăng trưởng đĩa tuyến tính.

## Owner cần quyết
- — · Không có quyết định nghiệp vụ chặn B2.1. B3 đã có contract nhưng chỉ tạo PROMPT/RUN sau B2.1 PASS.
