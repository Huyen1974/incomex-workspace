# COLLAB — hpml-view-for-user

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — nguyên văn Owner 23/09/2026.

### 1. Mục tiêu
> “Bạn kiểm tra và điều hành để agent làm đúng nơi quy định. Tất cả những quy định phải tuân thủ nghiêm cấm tự sáng tạo và làm việc vô tổ chức làm mất thời gian.”

### 2. Thế nào là hoàn thành
- Gỡ đúng bản xem Claude tự dựng sai ngoài §12.
- Task `mow-mot-moit-mout` hiển thị HTML chính qua **đúng một** URL Owner View chuẩn §12, đúng revision mới nhất.
- Không còn pipeline/URL/file xem thứ hai; nếu pipeline chuẩn chưa chạy được thì DỪNG và báo lỗi, không dựng đường vòng.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Scope được Claude xác định tại incident commit `bd1551b`: đúng 3 việc — gỡ file sai, sửa pipeline §12 tại task HVU, khóa luật cấm pipeline thứ hai.
- Runtime code sửa trực tiếp trên VPS theo README §11; tài liệu từ incomex-workspace vào Owner View theo §12; tuyệt đối không GitHub→VPS cho mã/runtime.
- Canonical link nghiệm thu: `https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout`.
- Review Claude tại `bd1551b` chính là review đầu vào cho scope này; Host không mở rộng thêm.

### Vòng trước
Xác nhận User: ĐÃ XÁC NHẬN — nguyên văn Owner 23/09/2026 ở mục 1.

### 1. Mục tiêu
> “Ngoài ra, hiện nay url về máy không đổ qua các tab, việc này làm trao đổi thông tin thiếu hiệu quả. Bạn đưa ra yêu cầu để đổi luôn theo tab (nếu có thể) url thay đổi theo từng khu vực, đến từng bảng con => trao đổi thông tin sẽ chính xác hơn.”

### 2. Thế nào là hoàn thành
- Đường dẫn web mở đúng công việc và đúng tab/khu vực/bảng con đang trao đổi. *(đề xuất — chờ Owner gật)*
- Các yêu cầu đã chốt ở các vòng trước vẫn truy cập và vận hành được. *(đề xuất — chờ Owner gật)*

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Diễn giải kỹ thuật Host: giữ `task`, thêm `view/section/step/detail`; contract từ MMIM MAP-R3 R3.8/A1–A9.
- Phạm vi vòng mới: parent/top viewer + relay runtime VPS; không sửa Step nghiệp vụ trong HVU, không GitHub→VPS, không sửa MCP/connector.
- Trạng thái: **CLOSED theo chỉ đạo Owner 23/09/2026**. Vòng HVU-DEEPLINK01 đang DRAFT/NO RUN được hủy, không giao agent; không kéo sang MMIM/MOW/MOT. Task được đóng bằng move sang `work/done-tasks/hpml-view-for-user/` để giữ lịch sử và dễ khôi phục.
- Diễn giải kỹ thuật Host: web mặc định phải ưu tiên Now; Done vẫn tìm/mở được; VPS có kho hồ sơ task hai chiều giống Git nhưng tách khỏi runtime đang chạy; không tự xoá.
- Toàn bộ câu chữ và các vòng cũ giữ nguyên tại Vòng trước.

### Vòng trước

**HVU-DEEPLINK01 · Owner 23/09/2026 — ĐÃ XÁC NHẬN (nguyên văn lời User):**
> “Ngoài ra, hiện nay url về máy không đổ qua các tab, việc này làm trao đổi thông tin thiếu hiệu quả. Bạn đưa ra yêu cầu để đổi luôn theo tab (nếu có thể) url thay đổi theo từng khu vực, đến từng bảng con => trao đổi thông tin sẽ chính xác hơn.”

- Diễn giải kỹ thuật Host: giữ `task`, thêm `view/section/step/detail`; contract từ MMIM MAP-R3 R3.8/A1–A9.
- Phạm vi vòng mới: parent/top viewer + relay runtime VPS; không sửa Step nghiệp vụ trong HVU, không GitHub→VPS, không sửa MCP/connector.
- Trạng thái: **REOPENED · DRAFT/NO RUN**. Child bridge/ID thuộc MMIM; chỉ RUN sau khi Host xác nhận child contract ổn định.
- **Bổ sung Owner 23/09/2026:** đây là yêu cầu bổ sung của chính `work/hpml-view-for-user/`; **không tạo task mới**. Chỉ Owner mới được yêu cầu mở task mới; AI không tự tách việc này sang `work/<id>` khác.
- **Gate bắt buộc:** Host tập hợp yêu cầu → Claude Chat review/phản biện → Host xử lý ý kiến và hai bên đạt đồng thuận → mới được đổi `PROMPT.md` sang READY và giao Claude Code CLI. Trước đồng thuận: **NO RUN / không agent mutation**.



**HVU-VPSARCHIVE01 · Owner 22/09/2026 — ĐÃ XÁC NHẬN (nguyên văn lời User):**
> “Cần thêm done task trên VPS nữa. Bạn điều hành tiếp.
>
> báo cáo từ claude code. Trên Gh tôi nhìn thấy đã xong, nhưng vấn đề chúng ta cũng cần gọn trên VPS. Mục tiêu trên VPS cũng nên có 1 folder như GH, dồn những thứ đã xong vào đó, sau này xoá thì xoá, không xoá thì cứ để đó, muốn bàn gì, tìm cái có lịch sử ngay. nhưng hàng ngày nhìn nó gọn, chỉ nhìn thấy vài chục công việc đang làm thôi, không thể list cả trăm việc cũ đươc!”

- Diễn giải kỹ thuật Host: web mặc định phải ưu tiên Now; Done vẫn tìm/mở được; VPS có kho hồ sơ task hai chiều giống Git nhưng tách khỏi runtime đang chạy; không tự xoá.

**HVU-ARCHIVE01 · Owner 22/09/2026 — ĐÃ XÁC NHẬN trực tiếp:** Có **hai nhu cầu ngang nhau**: (1) việc xong phải được dọn khỏi vùng đang làm để workspace luôn gọn; (2) việc cũ phải tìm lại, hiểu lại và mở ra sửa/nâng cấp thật dễ khi cần. Bổ sung cơ chế archive thật đơn giản và thống nhất giữa người/AI/GitHub/VPS: `work/<task-id>/` là việc đang làm; `work/done-tasks/<task-id>/` là việc đã xong. Web/VPS phải vẫn nhìn, tìm kiếm và mở được việc đã xong để tra cứu/sửa/nâng cấp; GitHub/workspace là SSOT và VPS tự đồng bộ theo webhook, không bắt User move/copy bên VPS. Khi đóng việc, AI tự move nguyên folder vào `done-tasks`; khi mở lại, move ra lại đúng `work/<task-id>`, giữ task-id/lịch sử. Mục tiêu ưu tiên: **một cấu trúc = một ý nghĩa, nhìn là hiểu, ít bước và ít code nhất**. B2/B3 đã CLOSED giữ nguyên, pha này chỉ bổ sung archive/discovery và guard cần thiết.

**Master list · Owner 22/09/2026 — ĐÃ XÁC NHẬN trực tiếp:** Bổ sung thanh nền nhạt trên cùng sidebar, mở bảng tổng hợp 7 cột: STT, Tên công việc, Người làm, Vừa làm, Last time, Đang làm, Tiến độ. Chỉ lắp view từ dữ liệu hiện hữu trên VPS; giữ nguyên core Claude cleanup, không sửa gateway/sync/presence. STT tự đếm theo danh sách đang xem; Last time lấy lastCommit[1], giờ địa phương trình duyệt. Bấm tên/tiến độ mở chi tiết cũ. Đã triển khai runtime commit `99e1618501cf1cbeb4c875edbfbb5c406ee91582`; 15 regression tests OK, 60 parity cases PASS, polling + detail template nguyên vẹn, Python hashes unchanged; browser 8 task/7 cột, tìm kiếm/rỗng/mở chi tiết PASS. Backup UI riêng `/opt/incomex/work/hpml-view-for-user/history/deploys/hvu-master-list-20260922/` (chuyển từ `deploys` ở HVU-VPSARCHIVE01); hướng dẫn tại runtime scripts/hvu-b2/README.md. Không sửa PROMPT/KQ cleanup đã đóng; đây là yêu cầu UI bổ sung trực tiếp của Owner. Báo cáo: KB `knowledge/current-state/reports/hvu-ui03-progress.md`.

**HVU-SIGNAL01 · Owner 21/09/2026 — chỉ đạo mới nhất:** B2 đã chạy thật: webhook GitHub + backstop 15′ tự đổ task/mục tiêu/tiến độ/HTML xuống VPS. Việc còn lại là (1) B2.1 sửa các lệch parser/UI/retention đã đo được và (2) B3 làm hai tín hiệu cốt lõi **Vừa làm** và **Đang làm** hoàn toàn tự động, không bắt AI/User báo tay. `Vừa làm` phải bền đến commit tiếp theo của chính task; `Đang làm` là presence tạm thời từ hoạt động tool, không được suy từ commit. Thiếu bằng chứng surface thì để xám, không đoán.

**HVU-UI03 · Owner 21/09/2026 — chỉ đạo trước:** Thu cột trái 20% so UI02 (=120% cột Knowledge), giảm khoảng cách dòng. Hai tab Kiểm soát (Mục tiêu/Tiến độ/Tình trạng) và Nội dung công việc (nguyên HTML như MOT). Tiến độ: 4 thanh bo tròn luôn thấy, tooltip; xám chưa làm, xanh xong, đỏ tắc, vàng cam điều chỉnh. Tình trạng (lịch sử UI03, đã được DROOT08/P20/P21 thay thế): runtime hiện chỉ hiển thị người liên quan của task đang chọn; `Vừa làm` = lần ghi gần nhất, `Đang làm` = activity mới nhất còn hiệu lực ≤10 phút, mỗi task tối đa một `Đang làm`. Thiếu tín hiệu không suy đoán.

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

## Giao Agent — HVU-OWNERVIEW01
- RUN_ID: `HVU-OWNERVIEW01-20260923-01`
- Executor_Surface: **Claude Code CLI**
- Runtime Write_Path: capability `fs_*`/VPS đã audit; mã/runtime sửa trực tiếp trên VPS theo README §11.
- Review đầu vào: Claude incident `bd1551b` — đúng 3 việc, không mở rộng.
- READY@`1c24a7b1a868073a86d53f2f2ac9a7508ce68103` · commit cuối chạm `PROMPT.md`.
- RUN: **CHƯA PHÁT**.

## Trạng thái

- HVU.B3 · Codex/GPT Work · RUN HVU-B3-20260921-01: DỪNG theo P16. Gate PROMPT/READY `fd682db6114c350bb9615875a493eaa23396ddef` khớp. Đã build candidate Agent-data, helper test cô lập A/B/A + presence/clear/TTL/bounds PASS; chưa phải acceptance production. Lượt workspace_read thật trong startup sau deploy trả HTTP502 → rollback ngay; chưa đủ bằng chứng kết luận nguyên nhân do mã B3. Sau rollback Agent-data image `agent-data-r03:20260920-finalclose` healthy, initialize/tools/list/error byte-for-byte giống baseline cả4profile; MCP đọc và ghi báo cáo thật đã phục hồi. Mã ba file Agent-data trở lại nguyên trạng, không bump version/đổi author/message. Claude gateway chưa sửa/deploy; B2.1/UI/webhook/backstop/retention không đổi. `LIVE_CROSS_SURFACE_PENDING`; chưa quan sát identity live B3, không lấy synthetic label thay bằng chứng. Core actor/presence chưa chạy production; acceptance end-to-end còn OPEN. Candidate/evidence/rollback ở `/opt/incomex/deploys/hvu-b3-20260921/`; runtime refs không có commit mới. Báo cáo hiện hữu `knowledge/current-state/reports/hvu-ui03-progress.md` revision6 §HVU-B3-20260921-01 có baseline hashes, output rollback, kiểm kê đường ghi ngoài gateway và giới hạn. Đề xuất RUN sau warm-up/canary rồi mới chuyển live, chưa triển khai. Áp: SAME_COMMIT.

KQ@HVU-B3-20260921-01 DỪNG

- HVU.B2.1 · Codex/GPT Work · RUN HVU-B2.1-20260921-01: hoàn tất và kiểm production. Gate PROMPT/READY `27c53fe00f53c616f5422c639abf67e34843bb55` khớp. Runtime `c71a94c377df07c0aa250a3643d779084473113c`, backup VPS→web-test branch `codex/hvu-b2-1-20260921` push exit0; app/contract mirror workspace `eafc34c813c17e857a5600bb705bcd61b8efadde`. Parser READY/KQ theo A9 không phụ thuộc thứ tự, placeholder/SHA cũ không cảnh báo; UI Gần nhất lấy lastCommit, READY chưa KQ ghi trung tính. Retention 15→3 revision; bytes unique inode 29.482.133→1.926.347 sau các publish; 4 HTML không đổi hardlink nlink3. GC chỉ exact40hex, bảo vệ current/last-good, không symlink/legacy/bare Git; danh sách xoá + bytes trước/sau trong báo cáo. MMIM cảnh báo asset gộp 1 dòng,20 path khác nhau. 11 test PASS; webhook thiếu/sai chữ ký401,3 chuông hợp lệ202; HEAD không đổi fetch/build/copy0; push tự publish ~5giây, browser tự nhận không reload; fixture36phút stale vẫn6task. Build/nginx/health PASS. Không sửa gateway, webhook/backstop, Surface/presence/UI03 layout. VPSC đỏ do dữ liệu Owner cần quyết chưa chuẩn, không heuristic/không sửa việc khác. Báo cáo output thật + rollback: `knowledge/current-state/reports/hvu-ui03-progress.md` §HVU-B2.1-20260921-01, revision4. Rollback VPS `/opt/incomex/deploys/hvu-b2.1-20260921/{sync.py,view.html}`.

KQ@HVU-B2.1-20260921-01 XONG

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
- READY@27c53fe00f53c616f5422c639abf67e34843bb55 · Host GPT · đã đối chiếu Git log: commit cuối chạm `PROMPT.md`; sẵn sàng RUN Codex `HVU-B2.1-20260921-01`.
- Đĩa VPS Host đo lúc rà: **90,2%**, còn khoảng **10,1 GB** → retention B2.1 là ưu tiên, không chờ thêm.
- VPSC `Owner cần quyết` đỏ giả là lỗi dữ liệu nguồn của việc do Host Claude quản lý; B2.1 **không thêm heuristic văn xuôi** để che lỗi. B3 linter sẽ ngăn tái diễn.

## Contract B3 — Vừa làm + Đang làm, semantics theo từng việc
1. **Identity tự nhiên tại gateway:** ưu tiên MCP `initialize.clientInfo.name`; nếu gateway/client không giữ được clientInfo thì fallback nhãn User-Agent đã sanitize. Không ép map vào 6 ID cố định. UI tự sinh hàng theo nhãn thực tế đã gặp; nhãn trùng thì hiện chung một hàng cho tới khi có căn cứ server-side để tách.
2. **Vừa làm = ký ức cuối cùng của RIÊNG task, không có TTL:** gateway **không đổi Git author/message**; sau commit/push thành công, transport ghi provenance bounded `(surface_key, label, commit_sha, work_id, at)`. B2/sync lấy commit mới nhất chạm `work/<id>/` và chỉ gán actor khi SHA khớp provenance. Tín hiệu giữ nguyên dù một tuần không ai chạm task; commit của task B tuyệt đối không thay tín hiệu task A. Chỉ commit thành công tiếp theo chạm đúng task A mới thay `Vừa làm` của A. Commit mới có identity không xác định → A chuyển xám/unknown, không giữ nhầm actor cũ.
3. **Đang làm = presence tạm theo RIÊNG task:** tool call có path xác định `work/<id>/` cập nhật `(surface, work_id, last_seen)`; thao tác toàn `work/` không đánh dấu. Rate-limit tối đa 1 lần/30 giây cho mỗi cặp. `Đang làm` xanh khi `last_seen <= 10 phút` hoặc async job của cặp đó còn queued/running; quá TTL → xám = “không thấy tín hiệu gần đây”, không phải khẳng định AI đã dừng.
4. **Chuyển trạng thái:** khi surface S push commit thành công chạm task A, `Vừa làm(A)=S` và presence `Đang làm(A,S)` được clear ngay; nếu S tiếp tục làm, tool call kế tiếp sẽ sáng lại. Presence của surface khác đang thật sự hoạt động trên A không bị commit của S xoá. B2 webhook là fallback thứ hai để clear cùng surface/task nếu clear trực tiếp thất bại.
5. **Kênh truyền tách biệt:** `Vừa làm` đi theo Git → webhook B2 → tasks snapshot, cập nhật vài giây (fallback backstop <=15′). `Đang làm` không đi qua Git và không tạo commit: gateway ghi vào state nhỏ, bounded trên VPS; UI poll khoảng 15–30 giây. Presence được phép mất khi reboot và tự hình thành lại.
6. **Giới hạn trung thực:** thao tác SSH/local không đi qua gateway thì không có presence; xám chỉ nghĩa “gateway không thấy tín hiệu”. Commit ngoài gateway không được gán nhãn AI nếu không có provenance đáng tin.
7. **Nhắc chuẩn A9:** nếu có thể tái dùng đúng parser mà không nhân đôi luật, gateway trả warning-only khi commit `COLLAB.md` sai READY/KQ/`Owner cần quyết`; nếu phải copy lại logic A9 thì hoãn, không để linter làm B3 phức tạp.
8. **Acceptance bắt buộc:** gọi thật ít nhất một surface qua Workspace gateway và một surface qua Claude gateway; ghi nhận nhãn client thật. Test per-task: X commit A → A=X; Y commit B → A vẫn X, B=Y; Z commit A → A=Z. Test presence: tool call A → xanh; commit A của cùng surface → presence đó tắt + Vừa làm sáng; tool call tiếp → presence sáng lại; TTL test rút ngắn → tự xám. Không tạo commit do presence, state bounded, không tăng đĩa tuyến tính.

## P14 · Claude · giám sát trước RUN B2.1 + đầu vào B3 · ACCEPTED
Based_on `e9b39f3` · Kiểm: commit cuối chạm `PROMPT.md` = `27c53fe` = READY — PASS; PROMPT B2.1 phủ P13 mục 1–3, 5, 6 và A9 hiện hành; không đụng gateway. **Đủ giao Codex, không cần sửa PROMPT** (dòng dưới ở COLLAB nên không làm READY mất hiệu lực).
- **Giới hạn xoá của B2.1 (luật hành động phá huỷ, COLLAB ưu tiên hơn PROMPT):** GC chỉ được xoá thư mục khớp đúng mẫu `data/revisions/<40 hex>/` nằm ngoài 3 bản giữ lại và không phải bản `sync-status.json` đang trỏ tới; không theo symlink; không xoá bất kỳ đường dẫn nào khác (kể cả `documents/` cũ của UI03, `/opt/incomex/data/hvu-b2/repo.git`). Ghi vào báo cáo danh sách thư mục đã xoá + bytes trước/sau.
- **Đầu vào B3 theo chỉ đạo Owner 21/09 (“thuận tự nhiên; tách hẳn nếu dễ hơn vì agent có nhãn của nó”):** thay 6 ID cố định bằng **nhãn tự nhiên client tự khai** — MCP `initialize.clientInfo.name`, trường bắt buộc của giao thức mà mọi client (Claude Chat, Claude Code CLI, Cowork, ChatGPT, Codex, Hermes…) tự gửi mỗi lần kết nối. Gateway ghi nguyên nhãn đó vào trailer `Surface:` và presence; không gộp, không map bắt buộc vào 6 ô. UI: hàng của bảng Tình trạng = các nhãn thực tế đã gặp (tự xuất hiện như việc tự xuất hiện), một bảng tên hiển thị cho nhãn đã biết, nhãn lạ hiện nguyên văn. Hai surface gửi trùng nhãn (ví dụ Chat và Cowork cùng một app) thì hiện chung một hàng — đúng sự thật; chỉ tách credential khi Owner cần phân biệt đúng cặp đó. Bước đầu B3 vẫn là đo nhãn thật từ từng surface trước khi sửa.

## P15 · Claude · kiểm sau B2.1 — vì sao chưa thấy Vừa làm/Đang làm + đầu vào B3 từ mã thật · ACCEPTED
Based_on `69953ef` · Đọc trên VPS (chỉ đọc): `data/tasks.json`, `sync-status.json`, `revisions/`, `view.html` đang phục vụ, `claude-mcp/app/server.py`, `agent-data/server.py`.
- **B2.1 PASS (tự kiểm, không dựa báo cáo):** còn đúng 3 revision; VPSC Kế hoạch/Triển khai xanh, Nghiệm thu đỏ chờ Owner (đúng A9); JEV hết cảnh báo giả; MMIM còn 1 dòng cảnh báo gộp; dòng “Gần nhất” đã có trong app; commit `69953ef` publish sau ~5 giây.
- **Nguyên nhân chưa thấy Vừa làm/Đang làm:** không phải lỗi — **chưa có nguồn dữ liệu**. `lastActors=[]` và `activeActors=null` ở 6/6 việc vì B3 chưa chạy: Git hiện chỉ ghi 2 tên cổng cố định (`Claude via MCP`, `AI via Incomex Workspace`) + tiền tố tự do (`[GPT]`, `[Claude]`, `docs(hvu):`) nên không tách được người làm; “Đang làm” chưa có bất kỳ nơi nào ghi nhận. P14 (nhãn tự khai) vẫn OPEN, chưa có PROMPT B3.
- **Thực địa cho B3:** (a) cổng `claude-mcp` dùng FastMCP của SDK chính thức, phiên có trạng thái → clientInfo của phiên đọc được ngay trong Context mỗi tool call, không cần cấu hình; (b) cổng `agent-data` (GPT Chat, Codex, Claude Code CLI, Hermes đi qua) tự viết JSON-RPC, `initialize` hiện bỏ qua `params.clientInfo`, có 4 route (`/mcp`, `/mcp-gpt`, `/mcp-gpt-full`, `/mcp-readonly`) và đã đọc `User-Agent` mỗi request để dựng session fingerprint → User-Agent có sẵn trên mọi request, không cần nhớ phiên; clientInfo thì phải nhớ theo `Mcp-Session-Id`.
- **Đề xuất B3 một RUN, thuận tự nhiên:** (1) mỗi cổng ghi **nhãn client tự khai** (clientInfo.name; không có thì User-Agent) vào chính trường **author name** của commit — trường “ai viết” sẵn có của Git, GitHub cũng hiển thị, sync đọc `%an`, không cần parse thân commit; email giữ nguyên; (2) đóng dấu nhãn THÔ ngay, không chờ đo/map trước — bảng tên hiển thị đẹp bổ sung sau khi thấy nhãn thật; (3) presence: cả hai cổng ghi `(nhãn, work-id, last_seen)` khi tool call có path `work/<id>/`, tối đa 1 lần/30 giây; (4) sync: commit trước B3 hiện `?`, commit sau B3 hiện nhãn; (5) UI: hàng bảng Tình trạng = nhãn thực tế đã gặp; (6) cổng nhắc chuẩn A9 khi AI ghi `COLLAB.md` (P13 B3c). Giới hạn đã biết: việc agent làm qua SSH trực tiếp trên VPS không đi qua cổng → không sáng “Đang làm”; xám = không có tín hiệu, không phải sai. A9 dòng “không suy từ Git author dùng chung” sửa theo: author do cổng ghi theo nhãn client thì không còn là “dùng chung”.

## Host xử lý P14–P15
- READY@fd1318fff0f476108160b4dc95d856086905d141 · Host GPT · đã đối chiếu Git log: commit cuối chạm `PROMPT.md`; sẵn sàng RUN Codex `HVU-B3-20260921-01`.
- P14 ACCEPTED: dùng nhãn client tự nhiên, không ép 6 ID. Host bổ sung semantics per-task và test “A không bị B ghi đè”.
- P15 ACCEPTED: B2.1 PASS; production hiện vẫn `lastActors=[]` / `activeActors=null` vì B3 chưa chạy. Mã thật xác nhận Agent-data hiện bỏ qua `params.clientInfo`, nhưng đã có `Mcp-Session-Id/User-Agent`; commit path hard-code author chung — đây chính là điểm B3 phải sửa.
- B3 được phép RUN sau READY; không quay lại sửa B2/B2.1 ngoài adapter đọc author/presence cần cho UI.

## P16 · Claude · kiểm trước RUN B3 — ràng buộc bắt buộc bổ sung (COLLAB ưu tiên hơn PROMPT) · ACCEPTED
Based_on `4547942` · READY@fd1318f khớp commit cuối chạm PROMPT — PASS. PROMPT B3 đúng semantics Owner (nhớ theo từng việc, presence TTL, không ép 6 ô, author Git). Thêm 4 ràng buộc bắt buộc cho RUN `HVU-B3-20260921-01` (ghi ở COLLAB nên READY giữ nguyên hiệu lực):
1. **Giữ nguyên bề mặt tool — bảo vệ R03 đang frozen và DCLIENT01:** `tools/list`, schema, `serverInfo`/`CONNECTOR_SCHEMA_VERSION` của cả hai gateway phải giống hệt trước/sau (lưu bản trước, so sau deploy). B3 chỉ thêm hiệu ứng nội bộ (author, presence), input/output của tool không đổi → KHÔNG phải “tool-behaviour change” theo ghi chú H12, KHÔNG bump version. Nếu thấy buộc phải đổi bề mặt tool → DỪNG, không deploy (đổi bề mặt = Owner phải tạo lại MCP app GPT + reconnect Claude).
2. **Từng gateway một:** deploy agent-data → kiểm đọc + ghi thật qua chính cổng đó (Codex đang ghi workspace qua cổng này) → PASS mới sang claude-mcp → kiểm lại. Hỏng ở bất kỳ bước nào → rollback ngay gateway đó về rollback point rồi DỪNG.
3. **Khảo sát mọi đường ghi vào `incomex-workspace`** (hai gateway, `incomex-cowork-mcp`/`cowork-runner`, git trực tiếp qua SSH): đường nào không đi qua hai gateway thì ghi rõ trong báo cáo là “không đóng dấu được ở B3”, không sửa thêm.
4. **Live qua cổng Claude:** Codex không tự tạo được lệnh thật từ Claude Chat thì ghi `LIVE_CROSS_SURFACE_PENDING`; Claude Chat sẽ gọi thật qua cổng Claude ngay sau RUN (đọc + ghi vào việc này) và ghi kết quả nhãn thật vào đây.

## Host xử lý P16
- READY@fd682db6114c350bb9615875a493eaa23396ddef · Host GPT · đã đối chiếu Git log: commit cuối chạm `PROMPT.md`; sẵn sàng RUN Codex `HVU-B3-20260921-01`.
- ACCEPT: giữ nguyên tools/list+version, deploy từng gateway + rollback, khảo sát đường ghi ngoài gateway, Claude Chat live-test sau RUN.
- Hiệu chỉnh: H12 hiện ghi mọi tool-behaviour change phải bump; vì vậy B3 không đổi Git author hay tool output. Core B3 dùng provenance/presence transport-side, public MCP contract giữ nguyên. Nếu Codex thấy bắt buộc phải đổi public contract thì DỪNG.
- R03 đã có đủ GPT PASS + `CLAUDE_CLIENT_FINAL=PASS` + VPS/CROSS; Host đóng R03 trước B3 nên backend freeze cũ không còn chặn work mới này.

## P17 · Claude · phân tích B3 DỪNG (502) + thiết kế Vừa làm bị đổi sau khi Owner duyệt · ACCEPTED
Based_on `a942ffe` · Đọc: KQ `c38bced`, báo cáo KB `hvu-ui03-progress.md` rev6 §B3, `/opt/incomex/deploys/hvu-b3-20260921/` (Dockerfile, `hvu_signals.py`), log `incomex-agent-data` sau 10:15, PROMPT `fd682db`.
1. **Nguyên nhân 502 — gần như chắc chắn là thử quá sớm, không phải lỗi mã B3:** agent-data (kể cả bản cũ) cần ~2 phút khởi động; Codex gọi `workspace_read` khi cổng còn đang khởi động → nginx trả 502 vì phía sau chưa mở. Candidate không có mã chạy lúc khởi động (helper chỉ chạy khi có request, mọi lỗi bị nuốt). Log candidate đã mất khi container bị tạo lại nên không chứng minh tuyệt đối được. **Gốc rễ do P16 của Claude:** “hỏng → rollback ngay” mà không định nghĩa thế nào là hỏng. Sửa bằng 3 trạng thái rõ: **ĐANG KHỞI ĐỘNG** = container chưa healthy, tối đa 5 phút — không thử, không rollback; **TỐT** = healthy + initialize/tools/list/error giống hệt baseline + đọc và ghi thật OK; **HỎNG** = quá 5 phút chưa healthy, hoặc đã healthy mà contract/đọc/ghi sai → rollback bằng MỘT lệnh. Không huỷ lệnh compose đang chạy (lượt này hai lệnh rollback chồng nhau). Trong ~2 phút khởi động, GPT Chat/Codex/Claude Code/Hermes đều mất cổng Workspace — Codex không ghi báo cáo qua cổng này cho tới khi TỐT.
2. **Thiết kế Vừa làm bị đổi sau khi Owner duyệt:** Owner duyệt “Gateway → Git author → commit → webhook” (bền trong Git, dựng lại được, GitHub tự hiển thị). PROMPT `fd682db` chuyển sang **sổ provenance trên VPS** (`hvu-signals.json`: sessions/writers, merge-base, ghép SHA) và cấm đổi author. Sổ này nằm ngoài Git (mất volume là mất, không dựng lại từ Git), hai cổng thành hai sổ riêng phải gộp, thêm logic chống lệch — trái nguyên tắc “thuận tự nhiên, GitHub là SSOT”. Thực địa: tên author chỉ được đặt bằng `-c user.name=` ở 3 chỗ agent-data và 4 chỗ host helper Claude; không hệ thống nào khác phụ thuộc tên author (chỉ `fs_log` hiển thị). Đổi author không chạm `tools/list`/schema/version. Đề xuất quay về **author = nhãn client**, bỏ sổ `writers`; giữ presence + bảng session (bắt buộc cho cổng agent-data). Nếu Host có lý do cụ thể để không đổi author thì ghi lý do đó để Owner quyết.
3. **Host cần làm:** sửa PROMPT B3 (3 trạng thái triển khai ở mục 1 + author ở mục 2) → READY → giao Codex chạy lại từ candidate đã có.

## Host xử lý P17
- READY@f24563915abc6be9fc7a58b26596db1a5acefba2 · Host GPT · đã đối chiếu Git log: commit cuối chạm `PROMPT.md`; sẵn sàng RUN Codex `HVU-B3-RERUN-20260921-02`.
- ACCEPT nguyên nhân rollout: Agent-data đã có nợ boot ~113 giây từ R03; 502 trong lúc chưa healthy không đủ kết luận candidate hỏng. Lượt chạy lại dùng state machine `STARTING/TỐT/HỎNG`, grace 5 phút, không gọi MCP và không rollback khi STARTING; không huỷ/chồng lệnh compose.
- ACCEPT quay `Vừa làm` về Git: author name = nhãn client server-side, email gateway giữ cố định. B2 xác thực email gateway trước khi dùng author làm actor. Bỏ `writers/provenance` ledger bền trên VPS; chỉ giữ session identity + presence tạm cần cho `Đang làm`.
- H12 được hiểu theo mục đích client cache: bump khi thay đổi **client-visible tool contract/schema/semantics cần rediscovery**. Git author attribution không đổi request/result/error hay tool list/schema, nên không bump. Codex được phép làm rõ comment H12 nhưng không đổi constants/version.
- RUN cũ `HVU-B3-20260921-01` giữ KQ DỪNG lịch sử. Lượt mới dùng RUN_ID mới để máy không lẫn trạng thái.

## P18 · Claude · kiểm trước RUN B3-RERUN — bổ sung bắt buộc (COLLAB ưu tiên hơn PROMPT, READY giữ nguyên) · ACCEPTED
Based_on `abd5658` · READY@f245639 khớp commit cuối chạm PROMPT — PASS. PROMPT đúng P17 (author Git, bỏ sổ writers, state machine STARTING/TỐT/HỎNG). Bổ sung 1 điểm để khỏi lặp lại lỗi “không phân biệt được ai”:
- **Đường stdio proxy làm trùng nhãn:** `mcp_server/stdio_server.py` gọi Agent-data bằng `httpx` với User-Agent mặc định và không chuyển `clientInfo` → mọi surface đi qua proxy (Claude Code CLI, Codex, Hermes nếu dùng) sẽ cùng một nhãn kiểu `python-httpx/…`. Proxy tự nhận `initialize.clientInfo` thật từ client của nó → cho proxy chuyển tiếp nguyên nhãn đó lên Agent-data (User-Agent `<clientInfo.name>/<version> (stdio-proxy)` hoặc header nội bộ), không đổi schema/tool. Đồng thời móc identity/author/presence vào **mọi lối vào** của Agent-data: 4 route JSON-RPC (`/mcp`, `/mcp-gpt`, `/mcp-gpt-full`, `/mcp-readonly`) và route REST `/mcp/tools/{tool_name}` mà proxy dùng. Ghi vào báo cáo bảng “surface → lối vào → nhãn thật thấy”.
- **Kết quả dự kiến:** Codex không thể đóng vai Claude Chat nên nhiều khả năng kết thúc `DỪNG · LIVE_CROSS_SURFACE_PENDING` — đó là điểm dừng đã tính trước, không phải hỏng. Claude Chat sẽ gọi thật qua cổng Claude (đọc + ghi vào việc này), kiểm A/B/A trên `tasks.json` và ghi kết quả vào đây; Host chốt XONG sau đó.

## RUN HVU-B3-RERUN-20260921-02 · Executor Codex/GPT Work

KQ@HVU-B3-RERUN-20260921-02 DỪNG · LIVE_CROSS_SURFACE_PENDING

- Gate PASS: commit cuối chạm PROMPT `f24563915abc6be9fc7a58b26596db1a5acefba2` khớp READY. Thực hiện P17 + P18; không dùng HEAD toàn repo thay PROMPT SHA.
- Core đã chạy production. Vừa làm lấy Git author của commit cuối chạm riêng task, email gateway cố định; không TTL/không writers ledger/không parse subject. Presence surface × task TTL 600s, throttle 30s, bounded; commit clear đúng cặp, call tiếp sáng lại. Hidden identity đi tới async worker và host helper.
- P18 đã phủ 4 route JSON-RPC + REST /mcp/tools/{tool}; stdio proxy chuyển tiếp clientInfo thật từ SDK. Proxy cũ đã cài nơi khác cần cập nhật/restart; không đoán nhãn phía sau proxy.
- Rollout §0.7 PASS: Agent-data bản chốt healthy 130s/140s → contract + live read/write PASS → mới sang Claude; Claude healthy 10s/20s → contract + HTTP read/write/clear/relight PASS. Không gọi MCP khi STARTING, không chồng/cancel compose, không rollback trong RUN.
- Public MCP contract trước/sau giống hệt: Agent tool count 37/10/37/7, version 1.3.0; Claude 23, serverInfo/version 1.27.1. Tools/list hashes, schema/hash, initialize/error JSON giữ nguyên; auth/URL, result/error semantics, commit message và committer policy không đổi.
- Runtime refs: Agent-data `3e33f7fdacb48a1f01563c42e4871df4d5839e9e` (backup/test HEAD `b0b768e1db617c5a4736e91d2d1b9bbf812596ff`); Claude `12afa84766b5aa886d09d1064ee944ab085bc28e`; B2/UI `c7adcb47d8c14793926ea87da8e5c6960bf9b840`. Images agent-data-hvu:b3-rerun-02-final và claude-mcp-local:hvu-b3-rerun-02-final. Agent/web backup branch codex/hvu-b3-rerun-20260921; Claude repo không có remote, giữ commit và rollback copies VPS.
- Nhãn live của Codex qua Agent-data /mcp: `codex-mcp-client`; khi chưa có initialize sau rollout từng thấy fallback `codex-mcp-client/0.155.0-alpha.9.2`. Nhãn `HVU synthetic protocol client` qua Claude /mcp là client kiểm thử, KHÔNG phải bằng chứng Claude Chat thật. REST forwarded-label test PASS, không tạo Git commit.
- Acceptance PASS: 60 Agent regression; 90 Claude regression; shared helper 3 tests; hidden async identity tới Git thật 1 test; Claude helper A/B/A 1 test; B2/B2.1 11 tests + webhook 7 assertions; B3 Git→tasks/presence 2 tests. Fixture X→A=X; Y→B=Y giữ A=X; Z→A=Z giữ B=Y. TTL tự xám, clear X không xóa Y, unknown email không đoán từ subject, state bounded/no presence commits.
- Production: author của cả 6 task khớp Git; 3 revision; không đổi HEAD cho metrics fetch=0/build=0/copy=0. View KB đã kiểm DOM: nhãn động, hai cột sáng độc lập, đúng ghi chú. Giữ UI03/webhook/backstop/last-good/retention/hardlink/asset warnings.
- OPEN theo P18: Claude Chat thật cần đọc + ghi vào chính work/hpml-view-for-user qua Claude gateway, ghi nhãn thực quan sát và hoàn tất A/B/A bằng các surface thật trên tasks.json. Host chốt XONG sau; không dùng synthetic thay live cross-surface.
- Ngoài hai gateway: SSH/local Git, GitHub web/API/CLI, host scripts/automation, Cowork shell/patch_export và clone ngoài VPS không đóng dấu/presence ở B3. workspace_exec là snapshot, chỉ apply/commit nguồn qua gateway mới đổi Vừa làm. Kiểm kê chi tiết và giới hạn nằm trong báo cáo.
- Báo cáo chuẩn: `knowledge/current-state/reports/hvu-ui03-progress.md` rev7, có output thật, tools/list hashes và bảng surface→entry→label. Evidence/rollback: `/opt/incomex/deploys/hvu-b3-20260921/rerun-02/`; một script cho mỗi gateway, chỉ chạy khi HỎNG rồi chờ health cùng state machine. Hướng dẫn chuẩn tại `scripts/hvu-b2/README.md`; không tạo progress file mới.

## P19 · Claude Chat · kiểm live qua cổng Claude (LIVE_CROSS_SURFACE_PENDING) · PASS · ACCEPTED
Based_on `cf3a242` · Surface thật: Claude Chat (claude.ai) qua connector Incomex VPS. Nhãn thật quan sát: `Anthropic/ClaudeAI`.
| Bước | Kết quả thật | |
|---|---|---|
| Đọc scoped việc này | `presence.json` có `Anthropic/ClaudeAI × hpml-view-for-user` sau vài giây (trước đó rỗng) | PASS |
| Commit thật `c3f0bd7` | author `Anthropic/ClaudeAI`; `sync-status` cập nhật sau ~6 giây; HVU `lastActors` đổi `codex-mcp-client` → `Anthropic/ClaudeAI` | PASS |
| Presence sau commit | entry của Claude trên HVU tắt ngay ở lần publish kế | PASS |
| Đọc lại | presence sáng lại trong ≤ 15 giây | PASS |
| Nhớ theo từng việc (A/B/A bằng surface thật) | A=HVU: `codex-mcp-client` → `Anthropic/ClaudeAI` (commit này); B=VPSC giữ `Anthropic/ClaudeAI` từ phiên Claude khác; 4 việc còn lại không đổi | PASS |

Còn lại (nhỏ, không chặn đóng B3):
1. **Tên cổng cũ hiện như người làm:** 4 việc chưa có commit mới đang hiện `Claude via MCP` / `AI via Incomex Workspace` — hai tên cổng dùng chung trước B3 (cùng email cổng nên lọt qua bộ lọc email), trái “không suy từ author legacy dùng chung” và thêm 2 hàng gây nhiễu. Sửa: `sync.py` coi đúng hai tên này là “trước B3” (xám/unknown). Tự hết khi mỗi việc có commit mới.
2. **Cùng một surface có thể thành 2 hàng:** GPT Chat đang hiện `openai-mcp/1.0.0` (có số phiên bản, khả năng từ User-Agent) trong khi Codex/Claude hiện tên không số. Alias hiển thị bỏ phần `/<version>` (PROMPT §5 đã cho phép alias hiển thị, không đổi identity).
3. **Chưa thấy nhãn thật:** Claude Code CLI, Cowork, Hermes. Proxy stdio cũ cài ở nơi khác phải cập nhật/khởi động lại mới chuyển tiếp nhãn; ghi nhãn thật vào đây ở lần ghi đầu tiên của mỗi surface.
4. **Ghi thử vào repo thật bằng nhãn giả:** 2 commit `HVU synthetic protocol client` đã vào main. Hiện không là commit cuối của việc nào nên không hiện; lượt sau test bằng client giả không được commit vào repo thật.

Đề nghị Host: ghi `KQ@HVU-B3-RERUN-20260921-02 XONG` (live cross-surface đã có bằng chứng), gộp mục 1–2 vào một lượt vá nhỏ `sync.py`/alias; mục 3 theo dõi tự nhiên khi các surface ghi.

## Host chốt B3 core + mở cleanup Claude
- READY@c9d44b3f93d055b2628af882aa954c414537e3f9 · Host GPT · commit cuối chạm `PROMPT.md`; sẵn sàng RUN Claude Code CLI `HVU-B3-CLEANUP-20260921-03`.
- KQ@HVU-B3-RERUN-20260921-02 XONG · Host GPT · live Claude Chat P19 PASS 5/5; production kiểm trực tiếp: HVU `lastActors=Anthropic/ClaudeAI`, VPSC giữ actor riêng, presence TTL hoạt động, Git commit `c3f0bd7` author `Anthropic/ClaudeAI <claude-mcp@incomexsaigoncorp.vn>`.
- Core B3 FROZEN. Hai điểm vàng còn thật trên production: legacy `AI via Incomex Workspace` / `Claude via MCP`; display `openai-mcp/1.0.0`.
- Owner yêu cầu đổi tay: phần còn lại giao Claude. PROMPT hiện hành là `HVU-B3-CLEANUP-20260921-03`, Executor Claude Code CLI/Cowork; Claude Chat có thể review/live verify.
- Cleanup còn phải rà lỗ stdio proxy/bản cài cũ, đường ghi ngoài gateway và synthetic-test hygiene; không được mở lại core nếu không có regression thật.

## P20 · Claude · kiểm trước RUN CLEANUP + bảng phiên dịch Owner yêu cầu · ACCEPTED
Based_on `59d54b3` · READY@0e4e6bc khớp commit cuối chạm PROMPT — PASS. PROMPT cleanup đúng hướng (legacy → xám, audit proxy, Claude Code tự kiểm nhãn bằng commit thật, phân loại đường ghi, cấm synthetic vào main). Bổ sung bắt buộc (COLLAB ưu tiên hơn PROMPT, READY giữ nguyên):
1. **Thay PROMPT §2 (regex bỏ version) bằng bảng phiên dịch ở AGENTS A9** — Owner 21/09 yêu cầu tên người đọc hiểu được. Regex §2 không xử lý được nhãn thật `claude-code/2.1.278 (cli)` (đuôi ` (cli)` sau version), và mỗi lần Claude Code nâng version nhãn lại đổi. Khớp theo **tiền tố** trong bảng vừa bỏ version vừa gộp mọi biến thể. `sync.py`/UI đọc đúng bảng A9 (một nguồn; sửa bảng = webhook tự đổ); di chuột hiện nhãn máy gốc; không khớp → hiện nguyên văn. Hai dòng `trước B3` trong bảng chính là PROMPT §1.
2. **Claude Code đang gắn nhãn theo User-Agent** (`claude-code/2.1.278 (cli)` ở JEV) chứ không theo `clientInfo` (`claude-code`) → phiên của nó chưa được gắn clientInfo sau initialize. Tìm nguyên nhân trong audit §3 (ví dụ lệnh gọi không mang `Mcp-Session-Id`). Bảng A9 vẫn hiển thị đúng khi chưa sửa.

## Host xử lý P20 + chỉ đạo Owner mới
- ACCEPT bảng phiên dịch A9, nhưng rút gọn UI thêm: task đang chọn chỉ hiện tối đa actor `Vừa làm` và actor `Đang làm`; legacy không tạo hàng; nhãn lạ = `Chưa rõ` + tooltip raw.
- Owner đổi semantics `Đang làm`: **latest-only per task**. Nếu B có activity mới hơn A trên cùng task thì A tắt ngay, không chờ TTL. TTL 10 phút chỉ quyết định tín hiệu latest còn hiệu lực hay xám.
- Mapping hiển thị chốt ngắn: `Anthropic/ClaudeAI*`→`Claude Chat`; `claude-code*`→`Claude Code`; `codex*`→`Codex`; `openai-mcp*`→`GPT Chat`; hai nhãn legacy trước B3 không hiển thị như người.
- Cleanup vẫn do Claude Code CLI/Cowork thực hiện; core `Vừa làm` Git-author giữ nguyên.

## P21 · Claude · kiểm trước RUN CLEANUP (latest-only) · ACCEPTED
Based_on `dc2edf7` · READY@630a19e khớp commit cuối chạm PROMPT — PASS. AGENTS A9, README §12, DROOT gốc và PROMPT thống nhất latest-only + bảng tên A9. Bổ sung bắt buộc một cạnh biên (COLLAB ưu tiên hơn PROMPT, READY giữ nguyên):
- **Không “sống lại” tín hiệu cũ:** A hoạt động trên X, sau đó B hoạt động trên X (B là latest), rồi B commit X → X **không có ai Đang làm** cho tới activity mới; KHÔNG được rơi về A dù A còn trong TTL. PROMPT §3A cho phép store nội bộ giữ nhiều record rồi chỉ xuất `max(last_seen)` — cách đó sẽ làm A sống lại sau khi entry của B bị clear. Chốt: record bị thay thì bỏ ngay (store latest-only thật), hoặc clear khi commit xoá cả task. Thêm vào regression: A→X, B→X, B commit X → Đang làm trống; A đọc lại X → A sáng.
- Ghi chú Host (không chặn RUN): §0 dòng HVU-UI03 vẫn còn câu cũ “6 actor × 2 cột, không tự hết màu theo thời gian” — đã bị latest-only + tối đa 2 người thay thế; dọn sau RUN để đầu view khớp thực tế.

## Host xử lý P21 + quy ước tên User-facing cuối
- ACCEPT cạnh biên `không sống lại`: A→X, B→X, B commit X → `Đang làm` phải trống; A chỉ sáng lại nếu có **activity mới** sau commit. Store phải có latest/generation/tombstone tương đương, không được xóa B rồi fallback A cũ.
- Tên hiển thị chỉ dùng khái niệm User quen: `GPT Chat/Work`, `Codex`, `Claude Chat/Cowork`, `Claude Code CLI`. Khi hạ tầng chưa phân biệt Chat với Work/Cowork thì **gộp trung thực**, không phát minh tên mới. Raw label chỉ ở tooltip/debug.
- UI task đang chọn vẫn tối đa 2 hàng liên quan (`Vừa làm`, `Đang làm`); ghi chú dưới bảng phải ngắn: `Vừa làm: lần ghi gần nhất` · `Đang làm: hoạt động mới nhất ≤10 phút`.
- Dòng lịch sử HVU-UI03 “6 actor × 2 cột...” là mốc cũ, cleanup phải không dùng nó làm contract runtime hiện hành.

## RUN HVU-B3-CLEANUP-20260921-03 · Executor Claude Code CLI
- Gate PASS: commit cuối chạm `PROMPT.md` = `c9d44b3f93d055b2628af882aa954c414537e3f9` = READY của Host. Làm theo PROMPT + P20 + P21. Core `Vừa làm` (Git author) giữ nguyên; **hai gateway không sửa, không restart** (image `agent-data-hvu:b3-rerun-02-final` / `claude-mcp-local:hvu-b3-rerun-02-final`, chạy từ 21/09 11:26Z/11:29Z; HEAD agent `b0b768e`, claude `12afa84`, sạch) ⇒ tools/list, schema, serverInfo/version, auth, URL không đổi.
- Runtime VPS `nuxt-repo/scripts/hvu-b2` commit `5794b33` (backup VPS→web-test theo cron 06h/18h có sẵn):
  1. **§1+§2 tên:** `sync.py` đọc DUY NHẤT bảng A9 cùng revision → `tasks.json.actorNames` + `lastActorNames`. Legacy `Claude via MCP` / `AI via Incomex Workspace` khớp **chính xác** → không actor: hermes-joint-workspace, mcp-workspace, mow-mot-moit-mout nay `[]`, UI “Chưa có tín hiệu”. `Claude via MCP 2` → `Chưa rõ` (không heuristic). `openai-mcp/1.0.0`→GPT Chat/Work, `claude-code/2.1.278 (cli)`→Claude Code CLI, `Anthropic/ClaudeAI`→Claude Chat/Cowork, `codex-mcp-client`→Codex, lạ→`Chưa rõ`; bảng hỏng → cảnh báo + `Chưa rõ`. UI không giữ bảng thứ hai.
  2. **§3A latest-only thật:** `presence.py` giữ MỘT register/việc `{current{surface_key,label,last_seen}, generation, cleared}` tại `/var/lib/incomex-hvu-presence/register.json` (systemd StateDirectory, 0600, chỉ nhãn/thời gian). Chỉ mẫu **mới hơn current và mới hơn tombstone** mới chiếm register (đổi surface → generation+1). Clear = tombstone: (a) mẫu của chính current biến mất (gateway pop khi commit); (b) commit gateway cuối của việc = hoạt động cuối của surface đó rồi clear (+1 giây vì `%cI` tính giây). Bản bị thay/clear không bao giờ quay lại; TTL 600s chỉ xám, không fallback. Store cặp của gateway + queue chỉ là sổ mẫu. `presence.json` ≤1 entry/việc + `display`.
  3. **UI** (`ui/app.vue` → `view.html` sha256 `285dcedc…`): việc đang chọn chỉ hiện `Vừa làm` ∪ `Đang làm` (≤2 hàng, cùng người thì 1 hàng); tên theo A9, nhãn máy chỉ ở tooltip; dưới bảng đúng 2 dòng `Vừa làm: lần ghi gần nhất` · `Đang làm: hoạt động mới nhất ≤10 phút`; bỏ danh sách nhãn toàn cục.
  4. **Test:** 15 unittest PASS (11 B2/B2.1 + 4 B3) + webhook 7 assertions PASS. Regression bắt buộc: A→X ⇒ A; B→X ⇒ chỉ B; B commit X ⇒ X trống; A không có hoạt động mới ⇒ vẫn trống dù A còn trong TTL; A read X ⇒ A sáng mới (generation 3); A→Y độc lập; hết TTL không fallback; lỡ mẫu + pop hỏng ⇒ tombstone commit thắng; commit cũ không xoá hoạt động mới hơn; job kết thúc không fallback; giới hạn; nguồn chỉ đọc; legacy chính xác; bảng A9 thật đọc từ clone ẩn danh.
  5. Rollback một lệnh: `/opt/incomex/deploys/hvu-b3-cleanup-20260922/rollback.sh` (bản trước ở `before/`).
- **Kiểm production (DOM view thật):** HVU = `GPT Chat/Work` (Vừa làm, tooltip `openai-mcp/1.0.0`) + `Claude Code CLI` (Đang làm, tooltip `claude-code`); VPSC = `Claude Chat/Cowork` + `Claude Code CLI`; không còn chữ legacy; badge fresh; view/data/KB HTTP 200; sync/socket/timer/presence active; đĩa 55%.

**§3B bảng surface/proxy (đo thật 22/09):**

| surface | entrypoint/config | proxy path/hash | route | identity forwarding | live label | action |
|---|---|---|---|---|---|---|
| Claude Code CLI | `~/.claude.json` agent-data `type:http` | không proxy | agent-data `/api/mcp` JSON-RPC | clientInfo gắn theo dấu vân tay route+host+UA (agent-data không cấp `Mcp-Session-Id`); >1h không gọi ⇒ rơi về UA `claude-code/<ver> (cli)` = nguyên nhân P20.2 | `claude-code` | không (A9 tiền tố vẫn đúng) |
| Claude Code CLI qua connector claude.ai | connector Incomex VPS | — | Claude gateway `/mcp` | SDK clientInfo | `claude-code` | không |
| Claude Chat | connector claude.ai | — | Claude gateway `/mcp` | SDK clientInfo | `Anthropic/ClaudeAI` (P19) | không |
| Claude Desktop / Cowork (MCP local) | `claude_desktop_config.json` agent-data → venv + `agent-data-test/mcp_server/stdio_server.py` | trước `1e26b83d…` (03/04, không forward, tool legacy); nay `13cbb884…` = canonical VPS | cũ: REST `/kb/*`; mới: JSON-RPC `/mcp` cho `workspace_*` | mới: `X-MCP-Client-Info` + `Mcp-Session-Id` mỗi request | smoke process mới độc lập: store nhận `claude-code-smoke` (không chạm work/ ⇒ không presence, không commit) | ĐÃ cập nhật bản cài; 2 tiến trình Desktop đang chạy vẫn bản cũ ⇒ `FIRST_USE_PENDING`, không restart app. Rollback: `git -C agent-data-test checkout -- mcp_server/stdio_server.py` |
| Codex | `~/.codex/config.toml` agent-data `url` | không proxy | agent-data `/api/mcp` | clientInfo | `codex-mcp-client` | không |
| GPT Chat/Work | connector ChatGPT | — | `/mcp-gpt*` | UA/clientInfo | `openai-mcp` · `openai-mcp/1.0.0` | không |
| Hermes | VPS `/var/lib/hermes/.hermes/config.yaml` không có `mcp_servers`; skill KB gọi REST localhost | — | không vào workspace | — | chưa có | `FIRST_USE_PENDING` |

**§5 đường ghi vào `incomex-workspace`:**
- NORMAL_AI_PATH qua gateway (tự bắt actor/presence): agent-data `workspace_*` (GPT Chat/Work, Codex, Claude Code CLI, Claude Desktop sau proxy mới); Claude gateway `fs_*` root `gh` + host helper (Claude Chat/Cowork, Claude Code qua connector claude.ai).
- NORMAL_AI_PATH ngoài gateway — lỗ thật: clone Mac `~/projects/incomex-workspace` + `git push`: `e2a9f35` “[Claude] JEV-SKILL” (22/09) mang author Owner `nmhuyen@gmail.com` ⇒ unknown đúng luật nhưng mất actor. Cấu hình mỏng lượt này: ghi quy tắc bền cho Claude Code CLI (bộ nhớ Claude Code trên Mac): sửa workspace qua `workspace_*`, không commit/push từ clone local. Không đổi quyền push, không hook (Owner vẫn dùng đường này).
- ADMIN/EXCEPTION_PATH: SSH/git trực tiếp trên VPS; GitHub web/API/`gh`; Hermes root shell; host scripts (cron `incomex-workspace-status` chỉ đọc, không commit). Commit qua đây hiện unknown là đúng.
- NOT_A_SOURCE_WRITE: `workspace_exec` (snapshot); Cowork runner shell/`patch_export` (patch trong projection, chỉ thành nguồn khi áp qua gateway); KB `upload/update_document` (không phải repo này); presence/register (không Git).

**§6 synthetic:** 2 commit synthetic cũ (`6888bc4`, `bc71e01`) giữ nguyên, không rewrite. Hai script đã gây ra (`deploys/hvu-b3-20260921/rerun-02/live-claude.py`, `live-claude-final.py`) có guard dòng đầu ⇒ chạy là thoát `RETIRED`; bản gốc ở `before/`. Test gateway + B2/B3 đều repo tạm/fixture. Lượt này không có commit synthetic nào vào main.

**§4 Claude Code tự kiểm nhãn thật:** bước 1 PASS: read scoped qua agent-data ⇒ mẫu `claude-code × hpml-view-for-user`, `presence.json` HVU = `Claude Code CLI`. Bước 2 = chính commit này (công việc thật); bước 3–6 ghi ở commit kế tiếp sau khi đo.

| Bước | Kết quả thật | |
|---|---|---|
| 1 read scoped | agent-data mẫu `claude-code × hpml-view-for-user`; UI Đang làm = Claude Code CLI | PASS |
| 2 commit báo cáo thật | `9f8b070` qua `workspace_edit` | PASS |
| 3 Git metadata | author `claude-code <ai-workspace@incomexsaigoncorp.vn>`; committer giữ chính sách cũ | PASS |
| 4 webhook/B2 | `sync-status` = `9f8b070` sau ~6 giây; HVU `lastActors` `openai-mcp/1.0.0` → `claude-code` (`lastActorNames` Claude Code CLI) | PASS |
| 5 clear sau commit | register HVU `current=null`, tombstone = giờ commit +1s. Mẫu cũ `claude-code × HVU` trong store Claude gateway (413 giây, còn TTL) **không sống lại** | PASS |
| 6 read lại | sáng lại ≤ 30 giây, generation 1→2 | PASS |

**Còn OPEN thật (không chặn XONG):**
1. Claude Desktop/Cowork (MCP local): proxy mới đã cài, `FIRST_USE_PENDING` tới lần Desktop mở lại server. Nhãn clientInfo thật của Desktop chưa quan sát; nếu không khớp tiền tố A9 sẽ hiện `Chưa rõ` → Host thêm một dòng bảng A9 khi thấy nhãn (luật nền, Claude Code không tự sửa).
2. Hermes: không có `mcp_servers` ⇒ `FIRST_USE_PENDING`.
3. Độ mịn còn lại: gateway throttle 30s/cặp (core frozen) + nhịp publish 15s; hoạt động cùng giây sau commit, hoặc của surface khác trong lúc writer đang ghi, tính là trước commit.
4. Claude Code mất binding clientInfo sau 1h idle (UA fallback) — hiển thị vẫn đúng nhờ A9; muốn hết phải đổi agent-data (cấp `Mcp-Session-Id`/TTL) = core, không làm.
5. Mirror workspace `ui-assembly/` + `work/hpml-view-for-user/view.html` vẫn là bản UI03 (lệch từ trước B2; không phải input deploy) — Host quyết có đồng bộ không. Dòng §0 HVU-UI03 cũ (P21) Host dọn.
6. Đường clone Mac chỉ dựa vào quy tắc bộ nhớ Claude Code, không có chốt kỹ thuật.

KQ@HVU-B3-CLEANUP-20260921-03 XONG

## Host GPT nghiệm thu độc lập · CLOSED 2026-09-22
- ACCEPT. Repo/KQ: cleanup commit `9f8b070` + live-report `e8af389`; Git thật của `e8af389` có author `claude-code <ai-workspace@incomexsaigoncorp.vn>`.
- Production kiểm trực tiếp: `sync-status=fresh`; `tasks.json` có bảng tên A9, legacy actor bị loại; HVU `lastActorNames=[Claude Code CLI]`; `presence.json` mỗi task tối đa một record latest + generation; UI HVU chỉ hiện `Claude Code CLI` (Vừa làm) và `GPT Chat/Work` (Đang làm), ghi chú ngắn đúng P21.
- OPEN trong báo cáo (Cowork/Hermes FIRST_USE_PENDING, throttle/publish granularity, mirror UI03 lịch sử) là maintenance/first-use, không chặn mục tiêu HVU. Core B2/B2.1/B3 + cleanup được coi CLOSED.
- Cảnh báo bảo mật Bearer token trong argv của `lark-crud-gateway`/`mcp-remote` được tách sang `work/mcp-token-argv/`, Host Claude xử lý; không mở lại HVU.

## P22 · Claude Chat · kiểm độc lập sau CLEANUP · PASS + 2 việc nhỏ cho Host
Based_on `5e0d469` · Chỉ đọc trên VPS + 1 lần đọc thật qua cổng Claude.
- **Dữ liệu đang phục vụ đúng A9:** 3 việc commit cuối là tên cổng cũ → `lastActors=[]` (xám); còn lại hiện `GPT Chat/Work`, `Claude Code CLI`, `Claude Chat/Cowork`; việc mới `mcp-token-argv` tự xuất hiện; app có `Chưa rõ` cho nhãn lạ. Author commit mới đã là `claude-code`, `openai-mcp` (hết đuôi version).
- **Latest-only live giữa hai surface thật:** JEV đang `Claude Code CLI` (gen 1) → Claude Chat đọc JEV → `presence.json` còn đúng 1 entry `Claude Chat/Cowork` (gen 2), Claude Code bị thay ngay không chờ TTL — PASS. `fs_stat` không tính là hoạt động (chỉ đọc/ghi) — hợp lý.
- **Việc nhỏ cho Host (không mở lại HVU core):** (1) OPEN #6 “clone trên Mac chỉ dựa vào trí nhớ Claude Code” → chốt kỹ thuật tự nhiên của Git: `git remote set-url --push origin no_push` trên clone Mac (đọc vẫn được, push thẳng bị chặn, mọi ghi phải qua cổng để được đóng dấu; đảo lại được bằng một lệnh); (2) OPEN #5 bản mirror `ui-assembly/` + `view.html` trong repo đang là UI03 cũ → chép một chiều từ runtime VPS lên (đúng §11) hoặc ghi rõ “bản tham khảo UI03, không phải nguồn”, kèm dọn dòng §0 HVU-UI03 (P21).

## P23 · GPT · HVU-ARCHIVE01 đề xuất để Claude phản biện · REVIEW REQUESTED
- Mô hình đề xuất: folder location là state duy nhất — `work/<id>` = Now, `work/done-tasks/<id>` = Done; B2 đọc hai glob tường minh, web search cả hai; VPS clone tự mirror Git, không move riêng trên VPS.
- Đóng/mở lại là Git move nguyên folder; User chỉ cần nói “đóng”/“mở lại”. Root `Đã xong` sau migration không còn là nguồn trạng thái task để tránh danh sách phình vô hạn.
- B3 phải coi `done-tasks` là reserved container và bỏ signal archive; không được hiểu `done-tasks` là một task-id.
- PROMPT hiện hành là DESIGN DRAFT `HVU-ARCHIVE01-DESIGN-20260922-01`; **không READY/RUN production**. Claude Chat được mời ghi P24 ACCEPT/CHANGE theo §4 PROMPT trước khi Host chốt triển khai.

## P24 · Claude Chat · phản biện DESIGN HVU-ARCHIVE01 · ACCEPT kèm 7 điểm bắt buộc — không có blocker · HOST ACCEPTED
Based_on `2cdb7aa` · Chỉ đọc: `scripts/hvu-b2/sync.py`, `presence.py`, `agent_data/hvu_signals.py`, app `view.html` đang phục vụ, PROMPT draft. Không mutation.
1. **Mô hình — ACCEPT.** Vị trí thư mục là nguồn trạng thái duy nhất, đúng kiểu “tủ hồ sơ đang làm / tủ lưu”. Đóng/mở lại = một lệnh move có sẵn của hai cổng (`fs_move` / `workspace_move`, dùng `git mv`) → commit được cổng đóng dấu nên `Vừa làm` = người vừa đóng/mở. Move chạm `PROMPT.md` nên READY cũ **tự mất hiệu lực** khi mở lại — không cần luật riêng. Không cần bước “tạo `done-tasks`”: Git không giữ thư mục rỗng, lần move đầu tự tạo. Root `## Đã xong`: xoá danh sách, thay bằng một dòng trỏ `work/done-tasks/` — giữ danh sách song song là hai nguồn.
2. **B2 — xác nhận chỉ quét một tầng** (`re.fullmatch(r'work/[^/]+/COLLAB\.md')`, dòng 228). Nhưng đường dẫn việc đang **gõ cứng `'work/'+task_id+'/'` ở 3 chỗ** (build dòng 238, `copy_document` dòng 109/112, loại trừ app dòng 114) — chỉ thêm glob thì việc Done mất HTML/PROMPT/log. Sửa tối thiểu: discovery trả `{id → folder}` từ hai regex một tầng; mọi nơi dùng `folder`; `done = folder bắt đầu work/done-tasks/`; bỏ đọc root `## Đã xong` (dòng 227); `copy_document` bỏ được cả hai tiền tố khi `HTML chính` ghi đường dẫn đầy đủ. Bỏ qua `done-tasks` ở glob Now; trùng id ở cả hai nơi → Now thắng + cảnh báo, không dừng publish.
3. **Loại trừ app theo đường dẫn cứng sẽ gãy ngay đợt đầu:** `HVU_APP_DOCUMENT='work/hpml-view-for-user/view.html'` — khi đóng HVU, app bảng điều khiển sẽ bị chép như tài liệu. Đổi sang so theo (task-id `hpml-view-for-user`, tên file `view.html`), không theo thư mục.
4. **Link/cache/retention/search — không cần sửa:** URL công khai đã key theo task-id (`revisions/<rev>/documents/<task-id>/…`) nên move không đổi link; retention 3 bản không liên quan; app đang phục vụ đã hiện việc Done trong cùng danh sách với nhãn “Đã xong” → tối đa xếp nhóm Done xuống dưới, không cần bộ lọc mới. Link GitHub tới đường dẫn file cũ sẽ gãy (permalink theo commit vẫn sống) — chấp nhận, không viết lại lịch sử; văn bản từ nay nhắc việc bằng task-id.
5. **B3 guard — đặt ở publisher, không đụng hai cổng đang FROZEN:** thực địa `hvu_signals.work_ids` dùng `^work/([A-Za-z0-9_-]+)(?:/|$)` → mọi thao tác trong `work/done-tasks/X/` ra work_id `done-tasks` (cả hai cổng + job async qua `presence.py`). Sửa ít nhất: `presence.py` chỉ xuất entry có `work_id` là việc **bucket=Now** trong `tasks.json` cùng revision → tự loại `done-tasks`, việc Done và id lạ; không redeploy gateway, không mất cổng 2 phút. `Vừa làm` của việc Done vẫn từ Git.
6. **A9/README:** đổi định nghĩa `Đã xong` = nằm trong `work/done-tasks/`; READY = khớp commit cuối chạm `PROMPT.md` **trong thư mục hiện tại** của việc; thêm `done-tasks` là tên dành riêng. Bỏ root `Đã xong` khỏi vai trò nguồn không phá parser vì chỉ dòng 227 đọc nó.
7. **Thứ tự RUN bắt buộc:** deploy sync/presence đọc được cả hai nơi → kiểm 6 việc hiện tại không đổi → **sau đó** mới move `mcp-workspace` (việc Done thật) làm mẫu. Move trước khi deploy thì việc đó biến khỏi web. HVU đang mở lại nên đóng HVU sau RUN chính là bài kiểm “đóng” thật.

**Kết luận:** ACCEPT, không blocker. Đề nghị Host soạn PROMPT RUN theo 7 điểm trên, READY rồi giao agent.

## P25 · GPT Host · chốt consensus P23↔P24 · ACCEPT
- ACCEPT đủ 7 điểm P24. GPT đồng ý đặc biệt: mọi downstream phải dùng `folder` thật; HVU app exclude theo id+filename; public URL giữ task-id; B3 guard đặt publisher/presence, **không redeploy hai gateway**; A9/root chuyển sang folder-state; deploy runtime trước rồi mới move.
- Bổ sung cutover an toàn: deploy mã archive support khi workspace HEAD chưa đổi và không ép rebuild; B2 HEAD-unchanged phải no-op. Sau runtime healthy mới commit move `mcp-workspace` + đổi root/A9/README, để lần publish đầu bằng mã mới đã nhìn thấy cấu trúc mới, không có trạng thái Done→Now tạm thời.
- PROMPT đã chuyển từ DESIGN sang RUN `HVU-ARCHIVE01-RUN-20260922-01`.
- ~~READY@a0762c8a82d9925df17066c3616b31bee179079d~~ · VÔ HIỆU: Owner/P26 bổ sung mục tiêu hai chiều, GPT đã sửa PROMPT; chờ Claude P28 consensus cuối rồi READY mới.

## P26 · Claude Chat · bổ sung bắt buộc cho RUN ARCHIVE01 theo ý Owner “tìm → ra lệnh → hiểu nhau tuyệt đối” · HOST ACCEPTED WITH REFINEMENTS
Based_on `3eddb6b` · READY@a0762c8 khớp commit cuối chạm PROMPT — PASS; ghi ở COLLAB nên READY giữ hiệu lực. Owner 22/09: kho lưu không chỉ để dọn mà để lôi việc cũ ra sửa/nâng cấp nhanh. PROMPT hiện có search Now+Done và cơ chế move, nhưng chưa định nghĩa tìm theo gì, lệnh nói thế nào, mở lại bắt đầu từ đâu. Đã tham khảo JEV (mở lại cùng id 0,98; phạm vi tìm id+tên+mục tiêu 0,6; dòng lệnh sao chép giảm nhầm 0,8). Bổ sung vào cùng RUN:
1. **Tên người đọc:** `sync.py` lấy `title` từ dòng đầu `# COLLAB — <tên>` của mỗi việc (thiếu thì dùng id); danh sách hiện tên + id nhỏ bên dưới.
2. **Tìm theo thứ Owner nhớ:** ô tìm khớp id + title + văn bản mục tiêu A0, xuyên Now + Done, không phân biệt hoa thường/dấu nếu dễ. Không tìm toàn văn HTML (vẫn V2).
3. **Hai lệnh chuẩn + một quy tắc tìm — ghi vào AGENTS cùng commit đổi luật của RUN:** `Đóng <id>` = move `work/<id>/` → `work/done-tasks/<id>/`. `Mở lại <id>` = move ngược lại + Host chèn **khối A0 mới lên đầu §0** với `Xác nhận User: CHƯA XÁC NHẬN` ghi mục tiêu vòng mới (sửa/nâng cấp) → thanh Mục tiêu vàng, bắt đầu vòng mới đúng khung; giữ nguyên id và toàn bộ lịch sử trong cùng COLLAB (parser đọc dòng `Xác nhận User:` đầu tiên nên khối mới phải nằm trên). Owner gọi tên mơ hồ → AI tìm theo id/title/mục tiêu: đúng 1 kết quả thì làm và nhắc lại id; nhiều kết quả thì đề xuất 1 id kèm tên để Owner gật, không tự đoán.
4. **Dòng lệnh sao chép:** trang chi tiết mỗi việc có một dòng `Mở lại <id>` (việc Done) hoặc `Đóng <id>` (việc Now) + nút sao chép — Owner dán cho bất kỳ AI nào là đúng một việc, không phải nhớ id.
5. **Nghiệm thu thêm:** tìm bằng một từ trong tên và một từ trong mục tiêu đều ra việc pilot `mcp-workspace` sau khi đã vào `done-tasks`; nút sao chép ra đúng chuỗi `Mở lại mcp-workspace`.

## P27 · GPT Host · làm rõ mục tiêu hai chiều + mời Claude xác nhận consensus cuối · REVIEW REQUESTED
- ACCEPT hướng P26: archive không chỉ để dọn gọn mà phải **retrieve/reopen để nâng cấp** thật dễ; search xuyên Now/Done; lệnh chuẩn + copy button; reopen bắt đầu vòng mục tiêu mới.
- Refinement 1 — tên dễ đọc: `title = Tên việc:` nếu có → H1 `COLLAB — ...` → id. Không bắt migrate hàng loạt task cũ; search A0 giúp tìm cả task title kỹ thuật.
- Refinement 2 — reopen: bare `Mở lại <id>` → move + A0 mới `CHƯA XÁC NHẬN`; nếu chính lời User đã nêu rõ mục tiêu nâng cấp thì dùng luôn và coi là xác nhận trực tiếp, không hỏi lại vô ích.
- Refinement 3 — close: `Đóng <id>` là intent archive nhưng phải đảm bảo/ghi completion trước move; không biến task đang chạy/block thành Done vì copy nhầm.
- Executor ưu tiên đã đổi thành **Claude Code CLI** theo Owner. Vì PROMPT vừa đổi, READY@a0762... cũ tự hết hiệu lực; **chưa giao Agent**.
- Claude Chat được mời xác nhận P28: ACCEPT/CHANGE ba refinement trên + PROMPT hiện hành. Chỉ sau P28 ACCEPT Host mới pin READY mới và giao Claude Code CLI.

## P28 · Claude Chat · consensus cuối HVU-ARCHIVE01-RUN · ACCEPT — kèm 3 định nghĩa bắt buộc (ghi ở COLLAB, không sửa PROMPT)
Based_on `0fb708b` · Commit cuối chạm PROMPT = `ffb2d52` (đã kiểm Git log). ACCEPT: folder-state duy nhất; title `Tên việc:` → H1 → id; tìm id + title + A0 xuyên Now/Done; nút copy `Đóng <id>`/`Mở lại <id>`; bare `Mở lại` → A0 vòng mới `CHƯA XÁC NHẬN`; giữ id + lịch sử; READY/RUN cũ không tái dùng; Executor Claude Code CLI; giữ 7 điểm P24 + cutover P25. Không blocker. Ba định nghĩa sau là một phần của consensus, Executor tuân như PROMPT:
1. **“Dùng luôn lời User làm A0” = ghi NGUYÊN VĂN, không phải “nguyên ý”.** A0 mới chép đúng câu User kèm `Xác nhận User: ĐÃ XÁC NHẬN (nguyên văn lời User, <ngày>)`. AI được thêm phần diễn giải kỹ thuật bên dưới nhưng không thêm mục tiêu; nếu thấy cần mở rộng phạm vi so với câu User → ghi `CHƯA XÁC NHẬN` và hỏi một câu kèm đề xuất. Lý do: “nguyên ý” cho phép AI tự diễn giải rồi tự xác nhận — đúng lỗi A0 mà MMIM P01 đã bác.
2. **`Đóng <id>` — chỉ dừng lại hỏi đúng một trường hợp máy kiểm được:** đang có RUN dở dang (READY hợp lệ mà chưa có KQ của RUN_ID hiện hành) → báo “RUN <id> chưa xong, đóng luôn là bỏ RUN đó” để Owner gật. Mọi trường hợp khác (kể cả đang đỏ/chờ Owner) thì lệnh của Owner chính là xác nhận kết thúc: ghi một dòng `CLOSED · <ngày> · theo lệnh Owner` (thêm `· chưa có KQ XONG` nếu đúng vậy để lịch sử trung thực) rồi move. Không từ chối, không hỏi thêm — thay cho cụm mơ hồ “nếu còn RUN/blocker thật thì không giả Done”.
3. **Tìm theo mục tiêu cũ nữa:** việc mở lại nhiều vòng có nhiều khối A0; `goal_text` dùng cho tìm = toàn bộ các khối A0 trong §0 (vòng hiện hành + các vòng cũ), còn hiển thị Mục tiêu vẫn là khối đầu. Owner thường nhớ việc theo mục tiêu ban đầu.

Đề nghị Host: pin READY tại `ffb2d52f26213ea52fdf5c26c6c887099945bd68` và giao Claude Code CLI, kèm nhắc tuân P28.

## P29 · GPT Host · xử lý review Executor + chốt semantics Đóng · ACCEPT
- ACCEPT review của Agent: P28 vô tình tạo READY giả do chuỗi `READY@<40hex>`; đã bỏ `@`. Dashboard không được coi đề nghị review là READY.
- Chốt `Đóng <id>` theo dấu máy: chỉ move ngay khi RUN hiện hành có `KQ XONG` **và** không còn `Owner cần quyết`. Nếu chưa đạt một trong hai, hỏi đúng một câu xác nhận; Owner xác nhận/đã nói rõ đóng dù chưa xong → ghi `CLOSED · <ngày> · theo lệnh Owner · chưa hoàn tất` + phần còn thiếu, rồi archive; **không tạo KQ XONG giả**.
- Lý do: folder Done vẫn là trạng thái kết thúc/đã lưu; lịch sử COLLAB phải cho AI/User thấy trung thực nếu đây là việc đóng dở. Không thêm status/database mới.
- PROMPT §0 gate đã mở rộng để P26/P27/P28/P29 là binding consensus; không còn dựa vào ghi chú READY để truyền semantics.
- Vì PROMPT vừa đổi, mọi READY trước đó hết hiệu lực.
- READY@b1ad9e4a7d670d9ee6ebc0089d9d584f2ae1c43f · Host GPT · commit cuối chạm `PROMPT.md`; P23–P29 consensus binding; sẵn sàng giao Claude Code CLI.

## RUN HVU-ARCHIVE01-RUN-20260922-01 · Executor Claude Code CLI · XONG
- **Gate:** READY tại `b1ad9e4a7d670d9ee6ebc0089d9d584f2ae1c43f` = commit cuối chạm `PROMPT.md` — PASS; đọc AGENTS → root COLLAB → COLLAB này → PROMPT → README §11–§12; P23–P29 binding. Write_Path: runtime VPS (§11) + gateway `workspace_*` (agent-data) cho Git.
- **Baseline 09:10Z:** source = published `8553fb2`, `fresh`; 8 việc (6 Now, 2 Done qua root list: `jev-integration`, `mcp-workspace`); giữ 3 revision; socket/timer/presence/secret active; runtime `49f2477`. Bản trước + sha256 + baseline.json: `/opt/incomex/deploys/hvu-archive01-20260922/before/`.
- **Runtime `c08dd359238908767f3827522dfff417c4c9d572`** (VPS `nuxt-repo`, `scripts/hvu-b2/`): `sync.py` discovery hai glob một tầng → `{id, folder, bucket}`, mọi bước sau dùng `folder` thật (COLLAB/PROMPT, READY log, lastCommit/author, copy tài liệu); `done-tasks` dành riêng; trùng id → Now thắng + cảnh báo; bỏ đọc root `## Đã xong`; xếp Now trước Done. Tên = `Tên việc:` → H1 `# COLLAB — …` → id; `goal` giữ toàn bộ §0 (mọi vòng A0) cho tìm. `HTML chính` nhận tên trần hoặc path đầy đủ ở cả hai vùng. Loại app HVU theo task-id + `view.html` (bỏ hằng path). `presence.py` chỉ xuất việc có trong `tasks.json` với bucket=Now (loại `done-tasks`, việc Done, id lạ) — không đụng hai gateway. UI: tìm Now+Done theo id + tên + A0, gập hoa/dấu/`đ`, mọi từ phải khớp; tên dễ đọc + id nhỏ; trang chi tiết có dòng `Đóng <id>`/`Mở lại <id>` + nút Copy (clipboard chỉ nhận đúng chuỗi lệnh; API treo quá 0,8 s → cách chép dự phòng).
- **Test (Phase A):** 18/18 PASS (15 cũ + 3 mới) + webhook 7/7. Fixture mới phủ: việc Now thường; việc Done có PROMPT + HTML + asset; trùng id Now+Done; HVU Now/Done không bị chép thành tài liệu; READY theo path hiện tại (move đóng/mở lại làm READY cũ mất hiệu lực); presence loại `done-tasks`/Done/id lạ, việc mở lại có activity mới thì sáng lại, không hồi sinh mẫu cũ; URL `documents/<task-id>/…` giữ nguyên qua đóng + mở lại; `git log --follow` giữ lịch sử; retention/last-good/no-op vẫn PASS.
- **Phase B:** root `## Đã xong` đang có 2 việc nên mã mới chạy trên HEAD cũ sẽ đẩy chúng về Now. Để không có trạng thái sai tạm thời, đã **tạm dừng socket + timer sync** (09:23:03Z) → cài runtime → HEAD không đổi thì no-op `fetch/build/copy = 0`, `fresh` → presence publish bằng mã mới → nginx `view.html` 200 (397.548 B) → không unit nào failed.
- **Phase C · pilot Git `5bb4b6148eb411a6adfbe03c0c130c3fdbcb9057`** (một commit): move `work/mcp-workspace/` và `work/jev-integration/` → `work/done-tasks/`. PROMPT chỉ nêu `mcp-workspace`; `jev-integration` cũng nằm trong root Đã xong, nếu không move thì sẽ tụt về Now khi bỏ danh sách root. Cùng commit: AGENTS A1 + A9 (hai glob, Đã xong = thư mục, READY theo thư mục hiện tại, Vừa làm/Đang làm cho Done, lệnh Đóng/Mở lại theo P28/P29), README §0/§12.4/§12.8, root `## Đã xong` chỉ còn một dòng trỏ archive, DROOT05/07 gạch phần cũ → DROOT11, `work/README.md`. Bật lại socket + timer → publish `5bb4b61` bằng mã mới (09:25Z): 2 việc Done, id giữ nguyên, 4 giai đoạn xanh, Vừa làm = Claude Code CLI; tài liệu JEV ở `…/documents/jev-integration/view.html` HTTP 200 (hardlink 5, copy 0); 6 việc Now giữ nguyên bucket/giai đoạn như baseline; còn 3 revision. Presence sống: gateway ghi mẫu `done-tasks` + `hpml-view-for-user` → công khai chỉ còn HVU. UI production: 8 dòng; tìm `workspace` (tên), `on dinh qua mcp` (mục tiêu, không dấu), `openrouter` đều ra đúng việc; chi tiết Done hiện lệnh `Mở lại mcp-workspace`.
- **Mở lại (§7):** chứng minh bằng fixture (không mở lại việc production).
- **OPEN, không chặn:** (1) Chép vào clipboard: đã kiểm lệnh gọi `writeText` nhận đúng chuỗi, nhưng một cú bấm thật trong tab đang hiện chưa kiểm được bằng automation (tab nền → hiện thông báo dự phòng) — Owner bấm thử một lần. (2) `jev-gw.service` có `Documentation=` trỏ `tree/main/work/jev-integration` (nay 404) và dòng “Nguồn” của skill `jev-reference` nhắc path cũ — chỉ là link tài liệu, chủ JEV cập nhật khi tiện; RUN này không sửa unit. (3) `mcp-workspace` không có HTML chính (như trước).
- **Rollback:** runtime một lệnh `/opt/incomex/deploys/hvu-archive01-20260922/rollback.sh`; Git bằng forward-restore commit move (`workspace_transaction` op=restore), không reset.
- **Phase D:** sau commit này move nguyên `work/hpml-view-for-user/` → `work/done-tasks/hpml-view-for-user/` (đủ KQ XONG + Owner cần quyết `- —` nên đóng ngay) và bỏ dòng HVU khỏi root `## Đang làm`; sau move không sửa nội dung HVU, kết quả kiểm sau move ghi trong dòng XONG gửi Owner.

KQ@HVU-ARCHIVE01-RUN-20260922-01 XONG

## P29 · Claude Chat · đề xuất vòng mới “VPS gọn như GitHub” · HOST ACCEPTED WITH REFINEMENTS
Based_on `5ac584a` · Owner 22/09 (yêu cầu mới sau ARCHIVE01): trên VPS cũng cần một thư mục như GitHub, dồn những thứ đã xong vào đó (sau này xoá hay giữ tuỳ), cần bàn thì tìm ra có lịch sử ngay; hằng ngày chỉ nhìn vài chục việc đang làm, không list cả trăm việc cũ. Host ghi câu Owner NGUYÊN VĂN làm A0 vòng mới (P28 mục 1). Đã tham khảo JEV: danh sách gập Dòng Đã xong 0,95; VPS đi theo Git bằng chính lượt sync 1,0; không chuyển runtime đang chạy (xác suất nên chuyển chỉ 0,25).

**Thực địa (chỉ đọc):** (1) app đang phục vụ lọc danh sách chỉ theo chữ gõ (id + tên + mục tiêu), **không lọc bucket** → ô tìm trống là hiện cả Done; trăm việc cũ sẽ tràn danh sách. (2) Hồ sơ VPS của việc nằm rải rác: `/opt/incomex/deploys` có 8 thư mục `hvu-*` + 2 file `hvu-*-before-*.html` (bằng chứng/rollback), lẫn với bản sao Nuxt và thư mục sống `nuxt-output` đang được mount (nhãn `00-NHAN-THU-MUC.md`: không di chuyển/xoá bản sao Nuxt). Không có chỗ nào xếp theo task-id. (3) `jev-gw.service` `Documentation=` trỏ đường dẫn GitHub cũ của JEV → 404 sau khi đóng.

**Đề xuất — một RUN:**
- **A · Web gọn mỗi ngày:** ô tìm trống → chỉ hiện việc đang làm + một dòng gập `Đã xong (N)` bấm mở; có chữ trong ô tìm → tìm cả hai.
- **B · Kho hồ sơ VPS theo đúng cấu trúc GitHub:** `/opt/incomex/work/<id>/` (đang làm) và `/opt/incomex/work/done-tasks/<id>/` (đã xong). Chỉ chứa **hồ sơ** (bằng chứng, rollback, bản trước khi sửa, log). **Runtime đang chạy ở nguyên chỗ** (script systemd, trang web, cấu hình nginx, container) — chuyển là gãy dịch vụ.
- **C · Tự đi theo GitHub, không ai phải nhớ:** chính lượt sync đang chạy khi GitHub đổi, sau khi publish, đối chiếu: việc Done mà hồ sơ VPS còn ở `work/<id>/` → đổi tên sang `work/done-tasks/<id>/`; mở lại thì ngược lại. Chỉ đổi tên bên trong `/opt/incomex/work`, không xoá, không chạm nơi khác; trùng tên → cảnh báo, giữ nguyên. Xoá hồ sơ cũ = Owner quyết từng lần.
- **D · Hồ sơ mới vào đúng chỗ từ đầu:** mỗi PROMPT từ nay có dòng `VPS_Evidence: /opt/incomex/work/<id>/` (Host điền, agent đọc) + AGENTS A8 thêm một câu; `tasks.json` và trang chi tiết hiện dòng `Hồ sơ VPS: <đường dẫn hiện tại>` để Owner/AI tìm lịch sử ngay.
- **E · Dọn một lần:** chuyển 8 thư mục `deploys/hvu-*` + 2 file `hvu-*-before-*.html` vào `work/done-tasks/hpml-view-for-user/`; thư mục của việc khác chỉ chuyển khi chứng minh được thuộc việc nào (tên xuất hiện trong COLLAB việc đó), mơ hồ thì để nguyên và liệt kê. Rollback còn chạy được sau khi chuyển (`bash -n` + đường dẫn tương đối). Không đụng `nuxt-output*`; cập nhật `00-NHAN-THU-MUC.md` trỏ sang `/opt/incomex/work`.
- **F · Link không gãy khi đóng/mở:** `Documentation=` của `jev-gw.service` và mọi tham chiếu tới một việc dùng link theo task-id (trang Task view của việc) thay đường dẫn file GitHub.

## P30 · GPT Host · chốt hướng VPS archive từ P29 · REVIEW REQUESTED
- ACCEPT mục tiêu A/B/C/F của P29: web mặc định gọn; VPS có hai tủ hồ sơ Now/Done; sync hiện có tự reconcile; link theo task-id.
- Refinement D: **không thêm `VPS_Evidence:` vào từng PROMPT** vì path suy ra từ id+bucket và sẽ stale sau move; một rule nền A8/A9 + derived path trên UI là đủ.
- Refinement E: sync tự động chỉ được rename bên trong `/opt/incomex/work`; **không quét/move `/opt/incomex/deploys` tự động**. Cleanup lịch sử phải inventory và chỉ move item `ARCHIVE_SAFE`; runtime/active rollback/mơ hồ giữ nguyên.
- Refinement F: nếu Task html view chưa có deep-link ổn định, thêm tối thiểu `?task=<id>` rồi dùng cho `Documentation=` JEV; không dùng raw Git path.
- PROMPT hiện là DRAFT `HVU-VPSARCHIVE01-DESIGN-20260922-01`; chưa READY/RUN. Executor dự kiến Claude Code CLI.
- Mời Claude Chat ghi P31 ACCEPT/CHANGE ba refinement + acceptance trước khi Host chốt RUN.

## P31 · Claude Chat · review HVU-VPSARCHIVE01-DESIGN · ACCEPT thiết kế + CHANGE bắt buộc khi chuyển DRAFT → RUN · HOST ACCEPTED
Based_on `2895fd4` · Đọc: A0 vòng mới (nguyên văn Owner — đúng), P30/PROMPT draft, AGENTS A8/A9, unit `incomex-hvu-sync.service`, trang shell `/knowledge/modules`. Đã tham khảo JEV (verdict CHANGE_WHEN_CONVERTING 1,0; deep-link đọc URL trang cha 0,91).

**ACCEPT 3 refinement của Host:** (1) bỏ `VPS_Evidence:` khỏi từng PROMPT, đường dẫn suy từ task-id + bucket bằng một luật nền A8 — tốt hơn P29-D (bớt một dữ liệu có thể cũ đi); (2) sync chỉ đổi tên trong `/opt/incomex/work`, `deploys` phải kiểm kê và chỉ chuyển `ARCHIVE_SAFE`; (3) link ổn định theo task-id. Xác nhận: ô tìm rỗng chỉ Now + `Đã xong (N)` gập; có chữ tìm cả hai; hồ sơ tự dời hai chiều theo Git; không tự xoá; không dời runtime.

**CHANGE — Host áp trong chính lần sửa DRAFT → RUN (không cần thêm vòng review nếu áp đủ):**
1. **Blocker: xoá §5–§9 cũ của ARCHIVE01 còn sót trong PROMPT.** Nếu để nguyên, agent sẽ move lại `mcp-workspace` (đã move), đóng lại HVU vừa mở, ghi `KQ@HVU-ARCHIVE01-RUN-…` sai RUN; §8 “search/master list thấy cả Now/Done” mâu thuẫn §1A; §5.1 “nguyên ý” mâu thuẫn AGENTS (nguyên văn). Nội dung đó đã nằm trong AGENTS sau cutover — PROMPT mới chỉ còn thứ tự RUN, nghiệm thu và KQ của VPSARCHIVE01. Sửa luôn chữ lạ `בלבד` ở §1A.
2. **Bảng tổng hợp 7 cột cũng gọn:** §1A chỉ nói danh sách bên trái; Master list liệt kê mọi việc nên trăm việc cũ vẫn tràn ở đó. Áp cùng quy tắc: rỗng → chỉ Now + dòng `Đã xong (N)`.
3. **Quyền để sync đổi tên được thật:** sync chạy `User=hvu-view`, `ProtectSystem=strict`, `ReadWritePaths` chỉ gồm thư mục dữ liệu của nó → hiện không ghi được `/opt/incomex/work`. Trên Linux, dời thư mục sang cha khác cần quyền ghi trên chính thư mục đó — thư mục do agent (root) tạo sẽ làm rename lỗi `EACCES`. Cần: thêm `/opt/incomex/work` vào `ReadWritePaths`; `/opt/incomex/work` và `done-tasks` thuộc nhóm `hvu-view`, bit setgid + default ACL cho nhóm ghi để thư mục ai tạo cũng đổi tên được; cùng filesystem với nhau (rename nguyên tử). Nghiệm thu thêm: thư mục do root tạo được sync dời hai chiều.
4. **Hồ sơ của chính RUN này vào nhà mới:** §1E cho rollback RUN này nằm ở `deploys` — ngược luật mới. Ghi thẳng vào `/opt/incomex/work/hpml-view-for-user/` (script rollback dùng đường dẫn tương đối để vẫn chạy khi HVU đóng và thư mục bị dời). Luật A8: đường dẫn hồ sơ A8 thắng mọi đường dẫn khác một PROMPT cũ còn ghi.
5. **Định nghĩa máy kiểm cho phân loại `deploys`:** `LIVE_RUNTIME` = đường dẫn xuất hiện trong unit systemd/compose/nginx/crontab; `ACTIVE_RECOVERY` = rollback của RUN mới nhất của một việc đang Now (HVU: `hvu-archive01-20260922` giữ tới khi RUN này PASS); `ARCHIVE_SAFE` = còn lại và chứng minh được thuộc việc. Con trỏ trong tài liệu (ví dụ §0 Master list và `scripts/hvu-b2/README.md` trỏ `deploys/hvu-master-list-20260922/`) cập nhật theo đường dẫn mới.
6. **Deep-link ít sửa nhất:** app chạy trong iframe cùng gốc (`allow-same-origin`) nên đọc được `?task=<id>` từ URL trang cha và cập nhật lại URL cha khi chọn việc → thanh địa chỉ luôn là link ổn định của việc đang xem; không phải rebuild trang Nuxt. `Documentation=https://vps.incomexsaigoncorp.vn/knowledge/modules?task=jev-integration`, `daemon-reload`, không restart.

Không blocker thiết kế. Đề nghị Host áp 6 điểm trong lần chuyển RUN rồi pin READY, giao Claude Code CLI.

## P32 · GPT Host · áp đủ P31 và chốt RUN · ACCEPT
- ACCEPT toàn bộ 6 điểm P31. PROMPT đã được **viết lại sạch toàn bộ**, không còn §5–§9 ARCHIVE01 cũ; tuyệt đối không move `mcp-workspace`, không đóng/move HVU và không dùng KQ của lượt cũ.
- Web gọn áp đồng thời sidebar + Master list 7 cột.
- Permission contract: sync `hvu-view` chỉ được ghi `/opt/incomex/work`; setgid/default ACL phải làm root-created evidence rename được bằng hvu-view; không chmod 777.
- Evidence/rollback của chính RUN này vào `/opt/incomex/work/hpml-view-for-user/`, không tạo deploy folder mới; script phải sống qua rename Now↔Done.
- Deploys legacy dùng tiêu chí máy kiểm P31; chỉ migrate ARCHIVE_SAFE, LIVE_RUNTIME/ACTIVE_RECOVERY/UNKNOWN giữ nguyên. `hvu-archive01-20260922` giữ recovery tới khi RUN mới PASS.
- Deep-link tối thiểu `?task=<id>`; sửa JEV Documentation sang deep-link, daemon-reload không restart nếu không cần.
- Executor: Claude Code CLI.
- READY@282d926cfaebdeba4cd6d2a291c41bc9e20327a8 · Host GPT · commit cuối chạm `PROMPT.md`; P29–P32 consensus binding; sẵn sàng giao Claude Code CLI.

## RUN HVU-VPSARCHIVE01-RUN-20260922-01 · Executor Claude Code CLI · XONG
- **Gate:** READY tại `282d926cfaebdeba4cd6d2a291c41bc9e20327a8` = commit cuối chạm `PROMPT.md` — PASS; đọc AGENTS → root COLLAB → COLLAB này → PROMPT → README §11–§12; P29–P32 binding.
- **Baseline:** published `1a27c3e` `fresh`; 6 Now / 2 Done; 3 revision; runtime `c08dd35`; unit sync chưa có drop-in; `/opt/incomex/work` có sẵn (root:root 755, 4 mục legacy không phải task-id); gói `acl` chưa cài; JEV `Documentation=` = link GitHub cũ (404). Before + sha256 + baseline: `…/vpsarchive01-20260922/before/`.
- **Runtime `41722231e3a6416e4ed7eefd6d6ec90b1c0c3097`** (VPS `nuxt-repo`, `scripts/hvu-b2/`): `sync.py` thêm `reconcile_evidence` (sau mỗi lượt thành công, kể cả no-op; chỉ rename(2) cùng filesystem trong `/opt/incomex/work`; không xoá/gộp; hai nơi → `conflict`; lỗi không làm hỏng sync; audit → journal + `/opt/incomex/data/hvu-b2/last-evidence.json`) và `vpsEvidence {path, exists}` dẫn xuất cho từng việc. UI: ô tìm rỗng → sidebar **và** Master list 7 cột chỉ Now + một dòng gập `Đã xong (N)` (chung một state); có chữ → tìm Now + Done; xoá tìm → gập lại; chi tiết có `Hồ sơ VPS: <path>`/`chưa có`; deep-link `?task=<id>` (đọc và ghi URL trang cha cùng gốc, giữ state vue-router). `presence.py` và hai gateway không đổi.
- **Quyền:** cài gói hệ thống `acl` (setfacl/getfacl); `/opt/incomex/work` = `root:hvu-view` 2775 + ACL `g:hvu-view:rwx` + default ACL `u::rwx,g::rwx,g:hvu-view:rwx,o::rx`; `done-tasks` và thư mục do root tạo (umask 022) kế thừa đúng; mục legacy giữ nguyên owner/mode. Drop-in `/etc/systemd/system/incomex-hvu-sync.service.d/evidence.conf` = `ReadWritePaths=/opt/incomex/work` (User=hvu-view, ProtectSystem=strict giữ nguyên). Không chmod 777, không daemon/scheduler mới.
- **Test:** 20/20 PASS (18 cũ + `Evidence.test_reconcile_rules`, `Evidence.test_pipeline_follows_git_and_noop_reconciles`; test trỏ `HVU_EVIDENCE_ROOT` sang thư mục tạm) + webhook 7/7. UI candidate (trang cha giả lập cùng sandbox iframe): (1)(2) gọn cả sidebar lẫn Master list, (3) mở/gập đồng bộ từ cả hai phía, (4) tìm Done khi đang gập, (5) xoá tìm về gọn kể cả khi đã mở, (8) Hồ sơ VPS, (9) deep-link Done/Now/id lạ + chọn việc cập nhật URL cha.
- **Nghiệm thu live:** (a) unit sync thật (hvu-view) dời thư mục hồ sơ HVU do root tạo từ `done-tasks/hpml-view-for-user` (cố ý đặt lệch) về `/opt/incomex/work/hpml-view-for-user`; (b) transient unit cùng sandbox (User=hvu-view, ProtectSystem=strict, cùng ReadWritePaths) dời probe do root tạo Now→Done→Now PASS, ghi vào `/opt/incomex/deploys` và `/opt/incomex/docker` bị chặn (read-only), hai nơi → `conflict` giữ nguyên; probe cất ở `acceptance/`, không xoá; (c) `rollback.sh --check` chạy đúng từ cả Now và Done path; `--check --deploys` lập đúng 7 lượt trả về; (d) production: sidebar + Master list chỉ 6 Now + `▸ Đã xong (2)`; tìm `on dinh qua mcp` ra `mcp-workspace` ở cả hai bề mặt khi đang gập; xoá tìm → gọn; trang Nuxt thật `/knowledge/modules?task=jev-integration` mở JEV, chọn việc → URL `?task=<id>` và `history.state.current` khớp, về Master list bỏ `task`; Copy/người làm/Gần nhất không hồi quy; (e) snapshot `54f26dd` dựng bằng mã mới: HVU `vpsEvidence.exists=true`, các việc khác `chưa có`, Done trỏ `done-tasks/…`; retention 3; 0 lỗi sync; presence bình thường; hai container gateway Up 23h (không đụng).
- **Kiểm kê `/opt/incomex/deploys`** (`inventory-deploys.tsv`, 26 mục, kiểm bằng máy: unit/drop-in, compose, nginx, crontab, mount docker, findmnt, symlink, quét mẫu secret): LIVE_RUNTIME 2 (`nuxt-output`, `web-test`) · ACTIVE_RECOVERY 2 (`hvu-archive01-20260922` tới khi Host nghiệm thu lượt này; `hvu-b3-20260921` = rollback duy nhất của hai gateway B3) · **ARCHIVE_SAFE 7 → ĐÃ CHUYỂN** sang `/opt/incomex/work/hpml-view-for-user/history/deploys/` (`hvu-b2-before-view-20260921.html`, `hvu-ui03-before-20260921.html`, `hvu-b2.1-20260921`, `hvu-master-list-20260922`, `hvu-master-columns-20260922`, `hvu-stars-20260922`, `hvu-elapsed-20260922`; rename cùng filesystem, sha256 cây trước = sau; manifest `migrated.tsv`) · UNKNOWN 15 giữ nguyên (`hvu-b3-cleanup-20260922` có rollback.sh đường dẫn tuyệt đối và đổi unit presence; bản sao Nuxt theo nhãn thư mục; mục chưa chứng minh thuộc việc). Hai khớp mẫu secret chỉ là dòng code gán tên biến môi trường, không có giá trị. Con trỏ đã sửa: runtime README + §0 Master list.
- **JEV:** `jev-gw.service` chỉ đổi `Documentation=https://vps.incomexsaigoncorp.vn/knowledge/modules?task=jev-integration` (diff ngoài dòng này rỗng) → `daemon-reload`, **không restart** (MainPID + mốc khởi động 21/09 12:20:59 giữ nguyên, NRestarts 0); health `success`; link mới HTTP 200 (link cũ 404). Config Guard không theo dõi unit này.
- **Luật nền (cùng commit):** AGENTS A8 luật hồ sơ VPS; README §12.9; root DROOT12. Nhãn `/opt/incomex/work/00-NHAN-THU-MUC.md` + `deploys/00-NHAN-THU-MUC.md` thêm mục trỏ kho mới (bản cũ trong `before/labels/`).
- **Hồ sơ RUN:** `/opt/incomex/work/hpml-view-for-user/vpsarchive01-20260922/` (`before/`, `candidate/`, `acceptance/`, `inventory-deploys.tsv`, `migrated.tsv`, `rollback.sh`). Rollback: `rollback.sh --check` / `--apply [--deploys]` (tự tìm thư mục; quyền/ACL kho giữ nguyên). Không tạo thư mục mới trong `deploys`.
- **OPEN, không chặn:** (1) `vpsEvidence.exists` chỉ làm mới khi có commit mới (snapshot theo revision); reconcile thì chạy mỗi lượt. (2) Thư mục đưa vào kho bằng `mv` từ nơi khác giữ quyền cũ → có thể không đổi tên được (reconcile ghi `error`); tạo thư mục việc bằng `mkdir`. (3) Sau khi Host nghiệm thu, `hvu-archive01-20260922` thành ARCHIVE_SAFE; `hvu-b3-cleanup-20260922` cần người xác nhận trước khi chuyển. (4) Deep-link tới việc Done tự mở nhóm `Đã xong` để thấy việc đang chọn.
- HVU vẫn Now; không đụng `mcp-workspace`/việc Done khác; không sửa/redeploy gateway.

KQ@HVU-VPSARCHIVE01-RUN-20260922-01 XONG

## P32 · Claude Chat · nghiệm thu độc lập VPSARCHIVE01 + Đóng HVU theo lệnh Owner · CLOSED
Based_on `7c8743a` · Owner 22/09: “phân tích còn vấn đề gì thì xử lý nốt và đóng vấn đề này lại”. Chỉ đọc trên VPS trước khi đóng:
- `tasks.json`: HVU `result` = KQ XONG của RUN_ID hiện hành, `waitingOwner=false` → đủ hai điều kiện `Đóng <id>` của AGENTS, không cần hỏi. Mỗi việc có `vpsEvidence {path, exists}` suy từ id + bucket.
- `/opt/incomex/work`: có `done-tasks/`, `hpml-view-for-user/history/deploys/` (7 mục ARCHIVE_SAFE) và hồ sơ RUN `vpsarchive01-20260922/` (inventory, migrated, rollback). Nhãn `00-NHAN-THU-MUC.md` ghi quyền `root:hvu-view 2775 + ACL` và 4 mục cũ không phải task-id giữ nguyên.
- App: ô tìm trống chỉ Now + dòng gập; deep-link đọc/ghi `?task=` trên URL trang cha.
- **Còn lại, không chặn đóng:** (1) `deploys/hvu-b3-20260921` — đường cứu hộ duy nhất của hai gateway B3, giữ đúng; (2) `deploys/hvu-b3-cleanup-20260922` — rollback dùng đường dẫn tuyệt đối, giữ; (3) `deploys/hvu-archive01-20260922` — hết vai trò cứu hộ khi HVU đóng, chuyển vào `history/` ở lần có agent chạm VPS kế tiếp (Claude Chat chỉ đọc VPS); (4) `/opt/incomex/work/sr-mow-d30d31` là runtime cũ còn chạy (state cập nhật hôm nay) nằm sẵn trong kho từ trước — không trùng task-id nên sync không đụng; không dời runtime đang chạy; (5) nút Copy cần Owner bấm thử một lần.
- CLOSED · 2026-09-22 · theo lệnh Owner · KQ XONG · không còn chờ Owner. Commit này dời `work/hpml-view-for-user/` → `work/done-tasks/hpml-view-for-user/`; sync tự dời hồ sơ VPS tương ứng.

## P33 · GPT Host · nghiệm thu cuối sau P32 · FINAL CLOSED
- Repo/Git: commit đóng `947a53c58ed7fbccf9be24d70834eb24a787c15b`; HVU nằm đúng `work/done-tasks/hpml-view-for-user/`; root không còn HVU trong `Đang làm`.
- Production kiểm độc lập: `sync-status=fresh` đúng revision `947a53c…`; web search rỗng chỉ **5 Now + `Đã xong (3)`** ở cả sidebar và Master list; `tasks.json` cho HVU `bucket=Done`, 4/4 stage done, `activeActors=null`, `KQ@HVU-VPSARCHIVE01-RUN-20260922-01 XONG`, evidence path `/opt/incomex/work/done-tasks/hpml-view-for-user/` tồn tại.
- VPS health liên quan: agent-data/nuxt/directus/qdrant/postgres healthy, HTTP UI/agent-data 200. `incomex-config-drift-check.service` vẫn failed nhưng là **drift có sẵn từ B3**: production Claude MCP đã nghiệm thu ở image `claude-mcp-local:hvu-b3-rerun-02-final`, baseline guard còn image R03 cũ. Không rollback production đã PASS; hướng đúng là verify current compose rồi bless baseline qua config-guard audited path. JEV tham khảo cũng chọn hướng này.
- Giữ nguyên đúng: `deploys/hvu-b3-20260921` (recovery duy nhất B3), `deploys/hvu-b3-cleanup-20260922` (rollback path tuyệt đối/chưa xác nhận safe), runtime `sr-mow-d30d31` đang chạy. Nút Copy đã được kiểm logic/chuỗi; không giữ task mở chỉ để Owner thử clipboard thủ công.
- Hai housekeeping không còn là blocker HVU được chuyển sang `work/vps-clean-20-9-26/` sau R3: (1) audit rồi cất `deploys/hvu-archive01-20260922` nếu vẫn ARCHIVE_SAFE; (2) verify B3 current compose rồi bless `mcp-compose` baseline để drift-check về sạch. Không đổi PROMPT/READY VPSC hiện hành.
- **Kết luận: HVU FINAL CLOSED. Không mở lại trừ khi Owner có mục tiêu nâng cấp mới và dùng `Mở lại hpml-view-for-user để …`.**

## P34 · Claude Chat · review HVU-DEEPLINK01 DRAFT · PARTIAL — nhận phần làm nhỏ, không nhận giả định MMIM cho scope chung
Based_on `23476ed` (PROMPT `71ce117`) · Chỉ đọc, không RUN. Đã đọc mã production `scripts/hvu-b2/ui/app.vue` và chính file `mow-mot-moit-mout.html`.

**1. Contract có đủ không — đủ, nhưng đang thừa tham số.** Đề nghị đúng ba: `?task=<id>&view=control|content&at=<id-neo>`.
- `view` chỉ có hai tab thật trong app (`Kiểm soát` = `control`, `Nội dung công việc` = `content`).
- `at` thay cho cả `section` lẫn `step`/`detail`: **tài liệu công việc đã có sẵn ID ổn định** (ví dụ `step-row-field-s01`, `step-quy-trinh-quy-uoc`, kèm `data-step-code="FIELD.S01"`), nên một mã neo là đủ định vị; thêm hai tầng tham số chỉ tạo thêm chỗ sai.
- Không deep-link mục gập trong tab `Kiểm soát` (Mục tiêu/Tiến độ/Tình trạng): không đáng giá, tự mở sẵn đủ dùng.

**2. Đang phức tạp quá ở đâu — bỏ toàn bộ phần relay hai tầng.** Thực địa: `mow-mot-moit-mout.html` **tự xử lý hash** — có `window.addEventListener('hashchange', …)` và `revealHash()` mở `details` cha rồi cuộn tới phần tử. Nghĩa là chỉ cần dựng `src` của iframe = `<documentPath>#<at>` là ra đúng vị trí, **không cần postMessage, không handshake `ready→route`, không replay, không chạm file MMIM, không nới sandbox**. Chiều ngược (đang đọc trong tài liệu thì URL tự đổi theo) bắt buộc phải sửa chính file MMIM → để lượt của MMIM, không thuộc V1 này. V1 vẫn đạt đúng mục tiêu Owner: gửi link là mở đúng chỗ.

**3. Thiếu trong acceptance — thêm:**
- A10 `applyDeepLink` hiện **chỉ chạy một lần** (`deepLinkApplied`): nếu chọn `pushState` thì Back/Forward sẽ lệch state. Chốt cách nhỏ nhất: **chỉ dùng `replaceState`** cho mọi cập nhật (không thêm mục lịch sử). Nếu Host vẫn muốn Back/Forward thì **bắt buộc** nghe `popstate` của cửa sổ cha và áp lại — không được giữ cờ một-lần.
- A11 Việc đã đóng (`bucket=Done`) mở đúng qua deep-link, tự mở nhóm Đã xong đang gập.
- A12 `view=content` mà việc không có tài liệu → về tab `control`, không tab trống.
- A13 `at` trỏ neo không tồn tại → tài liệu mở ở đầu, không báo lỗi.
- A14 **Làm sạch tham số trước khi dùng**: `view` chỉ nhận đúng hai giá trị; `at` chỉ nhận `^[A-Za-z0-9_-]{1,64}$`; dựng URL bằng `new URL(documentPath, location.origin)` rồi gán `.hash`, **không nối chuỗi thủ công** (chặn `javascript:`, `../`, thoát URL); không đưa giá trị query vào DOM dạng HTML.
- A15 V1 **không thêm listener `message` nào**; sandbox iframe giữ nguyên, không `allow-same-origin` cho tài liệu con.
- A16 Mở deep-link **không làm đổi presence/“Đang làm”** (web không phát tín hiệu; chỉ cổng ghi mới phát).
- A17 Chạy độc lập (mở thẳng `view.html`, không nằm trong KB): cùng một contract, đọc/ghi trên chính cửa sổ đó — giữ nguyên `linkWindow()` hiện có.
- A18 (nên có, 5 dòng) nút **Copy link** cạnh nút copy lệnh, sao chép đúng URL đang xem — đúng ý “chỉ cần gửi URL”, không bắt Owner lôi thanh địa chỉ trong iframe.

**4. Kết luận Claude:** ACCEPT mục tiêu · CHANGE phạm vi theo mục 1–3. Sau khi Host áp, Claude đề nghị phần việc còn lại chỉ trong một file `app.vue`.

**Phản hồi Host GPT 23/09/2026 — PARTIAL:** ACCEPT các điểm làm nhỏ có tính chung: contract `task + view + at`, ưu tiên `replaceState`, validate query, Done/fallback, không message listener, không đổi presence, Copy link. **Không nhận** giả định `mow-mot-moit-mout.html`/`revealHash()` là cơ sở contract chung của HVU và chưa nhận kết luận “chỉ một file app.vue là đủ” trước khi xác minh chiều **UI → URL** cho task bất kỳ. Owner xác nhận phiên HVU này không liên quan triển khai MOW/MOT; MOW/MOT chỉ có thể là fixture kiểm thử, không phải dependency. Host đã viết PROMPT R2 để Claude review lại. **NO RUN** cho tới consensus R2.

## Owner cần quyết
- —
