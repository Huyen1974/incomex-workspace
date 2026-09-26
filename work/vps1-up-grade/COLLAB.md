# COLLAB — vps1-up-grade
Tên việc: Nâng cấp nền tảng VPS1 qua rehearsal an toàn trên VPS2

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — chỉ đạo trực tiếp ngày 26/09/2026: mở `work/vps1-up-grade`, tập hợp phương án cũ + ý kiến Claude + bổ sung mới của Owner để hội đồng lập kế hoạch nâng cấp an toàn. Chưa cho phép nâng cấp/dọn/xóa/restart/deploy ở lượt mở việc này.

### 1. Mục tiêu
Nguyên văn/ý nghĩa chỉ đạo Owner:
1. Dùng **VPS2 làm nơi dựng, nâng cấp, sửa và kiểm thử** để VPS1 production vẫn tiếp tục chạy dự án không bị ảnh hưởng.
2. Sau khi target trên VPS2 đạt và đã tập dượt chuyển/rollback, **backup VPS1 rồi triển khai bộ nâng cấp đã chứng minh về VPS1**.
3. Ưu tiên nâng các thành phần phục vụ hệ thống quy trình MOW/MOT/MOIT/MOUT: **PostgreSQL, Directus, Nuxt, Agency OG**; các thành phần khác hội đồng tự cân đối giữ nguyên hay nâng.
4. Chọn **phiên bản mới nhất nhưng ổn định**: không chạy theo bản quá mới chưa đủ tin cậy, nhưng cũng không giữ bản cũ làm mất tính năng cần thiết.
5. Tận dụng hạ tầng sẵn có để giảm thời gian/chi phí/token: **2 VPS + Google Drive dung lượng lớn**, đường backup VPS1 → Google Drive đang hoạt động ổn định.
6. VPS2 chỉ phục vụ e-learning hầu như không hoạt động; Owner ước phần thực cần khoảng **~3GB**, trong khi máy đang dùng tới hàng chục GB. Phải khảo sát nguyên nhân phình dữ liệu và lập phương án dọn trước khi dùng làm lab.

### 2. Thế nào là hoàn thành
- Có inventory đúng thực tế của VPS1/VPS2/Google Drive và xác định phần dữ liệu phải bảo toàn.
- GPT + Claude thống nhất exact target version/digest cho stack ưu tiên trên căn cứ support, độ chín, compatibility, security, license và tính năng cần cho MOW/MOT/MOIT/MOUT.
- VPS2 được backup cần thiết, dọn có kiểm soát, cô lập side effect và dựng được **CURRENT parity clone** đủ để chứng minh migration.
- Có **route/API/UI/runtime test matrix** và **SAME SLICE** chạy trên CURRENT và TARGET.
- Nâng target trên VPS2 theo từng lớp, mọi regression/blocker được sửa hoặc disposition rõ; có restore/rollback proof.
- Tập dượt chính kịch bản cutover VPS1 trên VPS2, có thời gian, checkpoint, failure gate và đường quay lui.
- Trước cutover thật: backup/snapshot VPS1 + bản off-VPS trên Google Drive; triển khai đúng artifact/version/config/migration đã chứng minh; acceptance PASS.
- Nếu cutover không đạt cổng trong giới hạn đã chốt thì rollback được về production trước nâng cấp mà không mất dữ liệu mới hơn điểm dừng đã định.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- **Bổ sung Owner 26/09 — COMMERCIAL + OWNER-ABSENT:** làm rõ mô hình Incomex bán ứng dụng/quy trình MOT cho nhiều doanh nghiệp; khách không vào Studio. Doanh thu dưới ngưỡng đã được Owner xác nhận, không hỏi lại; số tài chính cụ thể không đưa thêm vào repo công khai. Một người vận hành kỹ thuật không được tự suy thành tổng headcount pháp nhân. Trước production v12 phải có phương án khi Owner vắng mặt và licensing không liên lạc được; không coi cảnh báo Telegram là đã khôi phục dịch vụ.
- **Điều hành hiện hành P05:** tách trial low-code khỏi phạm vi triển khai của việc này, không tạo task mới. Nâng tương thích shell Nuxt/Agency OS hiện hành để giữ dịch vụ; lựa chọn UI dài hạn không chặn cutover. Ngược lại, phương án liên tục vận hành khi mất license-server là cổng bắt buộc của nâng cấp.
- **Lượt hiện tại chỉ mở SSOT và lập khung khảo sát/kế hoạch.** CẤM mutation VPS1/VPS2, cleanup, xoá, restart, install, upgrade, migrate hoặc đổi DNS/nginx.
- Giữ mô hình lịch sử 08–11/09: **VPS1 = production**, **VPS2 = rehearsal lab**; không coi VPS2 là máy trắng vì vẫn có e-learning cần bảo toàn.
- Tái dùng hai profile cũ:
  - **PARITY CLONE:** đủ schema/config/policies/selected flows/extensions/source-lock/images/files + representative data cần thiết để chứng minh migration semantics; secret/egress production phải thay/cô lập.
  - **SLICE FIXTURE:** cùng một bộ dữ liệu/test cố định chạy trên CURRENT và TARGET, không đổi expected để che regression.
- Backup phải có **restore proof**, không chỉ có file backup.
- “Chuyển về VPS1” ưu tiên theo hướng **chuyển công thức/artifact đã chứng minh** (exact images/digests, compose/config, migrations, runbook), không mặc định chép nguyên máy VPS2 đè VPS1. Đây là đề xuất Host, Claude phải review trước khi thành quyết định.
- VPS2 storage audit phải phân loại ít nhất: business/e-learning data; DB; uploads; Docker images/layers/build cache; logs/journals; backups; temp/cache; source/build artifacts; orphan volumes/bind dirs; dữ liệu có thể tái tạo. Không xoá theo kích thước đơn thuần.
- Trước mọi cleanup VPS2: xác định dữ liệu cần giữ + tạo bản backup off-VPS phù hợp + verify restore/read-back.
- Target-version policy: exact pin, không dùng `latest`; ưu tiên stable/LTS/current supported patch có đủ tuổi/độ chín và ecosystem compatibility; bản mới hơn chỉ chọn khi lợi ích tính năng/security đáng rủi ro.
- **Agency OG:** giữ đúng tên Owner dùng; bước inventory phải xác định chính xác component/package/image hiện tại trước khi chọn target, không tự đổi nghĩa/tên.
- Thành phần ngoài nhóm ưu tiên (Qdrant, Nginx, Docker, Node, worker, MCP/Hermes/JEV/Kuma/backup...) đánh giá theo nguyên tắc **chỉ nâng khi có lý do rõ hoặc dependency bắt buộc**; tránh tăng blast radius.
- Route test matrix phải lấy từ runtime thật: nginx/domain routes, Nuxt pages, Directus/API/auth, workflow endpoints, Owner View/Kuma-monitored URLs và các integration có side effect. Không suy “container healthy = hệ thống PASS”.
- Clone trên VPS2 phải chặn/đổi đích những đường có thể gây tác động thật: Telegram/bot, GitHub write, webhook, mail, cron/schedule, Agent Data, backup production, external storage/API mutation và mọi singleton consumer.
- Cutover phải xử lý bài toán **VPS1 tiếp tục thay đổi trong lúc VPS2 rehearsal**: kế hoạch freeze/delta/final backup + migrate dữ liệu mới nhất; không mang dữ liệu lab cũ về làm production truth.
- Google Drive là lớp backup thứ ba ngoài 2 VPS; phải tận dụng nhưng không thay thế snapshot/rollback cục bộ khi cần phục hồi nhanh.
- Mục tiêu tối ưu: **an toàn trước, thời gian gián đoạn thấp, ít thao tác lặp, ít token**, không xây thêm framework nếu script/tool hiện hữu làm được.

### Vòng trước
Chưa có — mở việc lần đầu theo lệnh Owner ngày 26/09/2026. Các rehearsal 08–11/09 là nguồn lịch sử, không phải production adoption đã duyệt.

Host: GPT Chat
Host_ID: GPT-VPSUP-20260926-A
Owner giao mở việc: 2026-09-26
HTML chính: `view.html`
Owner View: https://vps.incomexsaigoncorp.vn/knowledge/modules?task=vps1-up-grade
Executor_Surface lượt mở: GPT Chat
Write_Path: Incomex MCP full all 2 → workspace_* → root workspace → main

## Dòng hiện hành
VPSUP | P04 HOST PARTIAL · P05 COMMERCIAL + CONTINUITY | Chưa PROMPT/READY/RUN | NEXT: Claude kiểm P05 và hoàn thiện một phạm vi G0 chỉ đọc theo view.html §9; UI trial ngoài cutover, Directus continuity gate còn OPEN.
- HEAD trước mở việc: `545157ae4d0a58d72274063800ad0b65d9ad76ef`.
- Lượt này chỉ tạo SSOT của task; không mutation hạ tầng.
- Owner View hậu kiểm cũ: ui_inspect đọc được shell HTTP 200 + Login/401; chưa đọc được nội dung iframe. **CHƯA XÁC MINH nội dung**, không suy 401 của header là task bị khoá. Lượt P05 sẽ kiểm lại đúng URL chuẩn; không tạo bản xem khác.
- Áp mở việc: `7275ef1966c09016a372128b9934dcf93abbac98`.

## Quyết định Owner
- D01 · 2026-09-26 · **MỞ VIỆC:** tạo `work/vps1-up-grade` để hội đồng lập kế hoạch nâng cấp VPS1 qua rehearsal trên VPS2. Chưa cho phép thực thi nâng cấp.
- D02 · 2026-09-26 · **TOPOLOGY:** VPS1 là production tiếp tục chạy; VPS2 dùng làm nơi dựng/nâng/fix/test trước khi chạm VPS1.
- D03 · 2026-09-26 · **CORE PRIORITY:** PostgreSQL + Directus + Nuxt + Agency OG là nhóm cần xem xét nâng cấp ưu tiên để phục vụ hệ MOW/MOT/MOIT/MOUT. Thành phần khác hội đồng cân đối.
- D04 · 2026-09-26 · **VERSION POLICY:** GPT + Claude phải thống nhất phiên bản “mới nhất nhưng ổn định”; không chọn bleeding-edge thiếu bằng chứng, cũng không neo bản cũ nếu làm mất tính năng hữu ích.
- D05 · 2026-09-26 · **VPS2 STORAGE:** phải khảo sát vì e-learning gần như không hoạt động nhưng VPS2 dùng hàng chục GB; Owner ước workload thực chỉ khoảng ~3GB. Có thể dọn phần vô ích nhưng phải phân loại/backup trước.
- D06 · 2026-09-26 · **BACKUP ASSET:** ngoài 2 VPS có Google Drive dung lượng lớn; VPS1→Google Drive đang kết nối ổn định. Kế hoạch phải tận dụng tài sản này để giảm rủi ro và thời gian.
- D07 · 2026-09-26 · **LONG-TERM / PRODUCT-FIRST:** Incomex thực tế chỉ có Owner vận hành và Owner không làm kỹ thuật IT. Mọi lựa chọn nền tảng phải ưu tiên sản phẩm đang sống, đáng tin, có cộng đồng/nhà phát triển duy trì, cài/lắp ráp được; **code và tự duy trì framework là giải pháp cuối cùng**.
- D08 · 2026-09-26 · **AGENCY OS = LEGACY / EXIT:** việc dựa vào Agency OS đã ngừng phát triển được coi là lựa chọn không bền. Không tiếp tục coi Agency OS là nền tảng dài hạn; lập kế hoạch **thoát dần**, không big-bang và không thay bằng một template phụ thuộc cá nhân khác. Chưa chốt sản phẩm thay thế trước trial.
- D09 · 2026-09-26 · **DIRECTUS STRATEGIC GATE:** Directus là quyết định kiến trúc dài hạn; phải kiểm chính sách license/OIG, giới hạn, telemetry/license-server dependency, security/support và exit path trước khi production adoption v12. Không được chọn chỉ vì “đang dùng rồi” hoặc để giải quyết nâng cấp cho xong.

## Quyết định bổ sung — phân biệt thẩm quyền
- D10 · OWNER · 2026-09-26 · Mô hình cần xét: Incomex vận hành nhà máy quy trình, bán sản phẩm/ứng dụng riêng; người dùng khách hàng làm việc bằng MOT, không dùng Directus Studio. Phải làm rõ ngưỡng doanh thu/nhân sự đúng chủ thể và sự cố kỹ thuật khi Owner vắng mặt. Chưa đăng ký/chấp nhận điều khoản/mua giấy phép thay Owner.
- D11 · HOST · 2026-09-26 · Nhận P04: UI low-code trial không nằm trong cutover VPS; không mở thêm task trong lượt này. Giữ D07–D08 về hướng thoát Agency OS, nhưng nâng tương thích shell đang phục vụ vẫn thuộc việc này. Không viện dẫn một luật “cấm mọi DB thứ hai” khi chưa có văn bản đúng scope; lý do tách là phạm vi, tài nguyên và một nguồn quyết định UI.
- D12 · HOST · 2026-09-26 · LICENSE CONTINUITY là tiêu chí nghiệm thu, không chỉ alert. Phân loại lỗi đường mạng Incomex / sự cố licensing phía Directus / key-binding / người liên hệ vắng mặt; kiểm phục hồi và trạng thái thực trên exact build. Không tự tạo tổ chức khác, reset định danh, xoay key hay sửa clock để kéo dài thời hạn.
- D13 · HOST · 2026-09-26 · Giữ major PG riêng; nếu PG18 chưa đạt, xem xét app target trên patch PG16 còn hỗ trợ đã kiểm tương thích. Exact version chốt bằng advisory + hỗ trợ + rehearsal tại G3/G7; không có luật cứng chờ 8 tuần khi bản vá bảo mật áp dụng cần lên sớm.

## Ý kiến hội đồng
### P01 · GPT Host · ACCEPTED — kiến trúc migration đã được Claude P02 đồng ý
- Based_on: chỉ đạo Owner 26/09 + rehearsal lịch sử 08–11/09 + việc `vps-clean-20-9-26` đã đóng.
- Scope: `view.html` §1–§10.
- Đề nghị:
  1. Không “copy nguyên VPS2 về VPS1”; chuyển **reproducible deployment formula** đã chứng minh: exact image/digest + compose/config + migrations + runbook + acceptance tests.
  2. Trình tự an toàn: **read-only inventory → backup/restore proof → VPS2 cleanup có kiểm soát → CURRENT parity clone → baseline route/slice → nâng từng lớp → TARGET same-slice → rollback rehearsal → cutover rehearsal → production cutover**.
  3. Chưa nâng Qdrant/Nginx/Docker/... chỉ vì có bản mới; chỉ nâng nếu dependency/security/tính năng cần thiết.
  4. Version target lịch sử 11/09 chỉ là reference stale; vòng này phải refresh nguồn chính thức rồi Claude cross-review.
  5. Production cutover phải time-box; quá gate thời gian hoặc core acceptance FAIL thì rollback, không “cố sửa trên production”.
- Trạng thái: **ACCEPTED** về kiến trúc migration; P02 đã đồng ý P01.1–5. Chi tiết version/license/UI strategy được Host xử lý riêng ở P03.

### Yêu cầu Claude Reviewer vòng 1
Đọc `AGENTS.md` → §0 file này → `view.html`. Ghi phản biện P02 ngay tại đây, không tạo file review mới. Tập trung 6 câu:
1. Chính sách chọn exact version cho PG/Directus/Nuxt/Agency OG có đủ cân bằng mới–ổn định chưa?
2. VPS2 phải đo/dọn những gì để thật sự chỉ giữ e-learning + lab capacity cần thiết?
3. PARITY CLONE tối thiểu cần gì để không test giả nhưng cũng không copy production vô tội vạ?
4. Route/API/UI/runtime matrix nào đủ chứng minh “VPS2 PASS ⇒ có cơ sở chuyển VPS1”?
5. Cutover/rollback nào ít downtime và ít thao tác nhất với backup Google Drive đang có?
6. Thành phần nào ngoài core nên giữ nguyên, thành phần nào bắt buộc nâng do dependency?

### P02 · Claude Chat (Reviewer) · PARTIAL — phản biện P01, Host đã xử lý tại P03
- Based_on: `dd67cc8` (COLLAB `b0fca0c3`, view `443a5786`). Scope: §0, P01, `view.html` §1–§10, Q01–Q08.
- Nguồn đo/đọc 26/09: VPS1 live (`vps_status` containers/resources, `SHOW server_version`, compose `docker/nuxt-repo/infra/docker/docker-compose.yml`, nginx `docker/nginx/conf.d/default.conf`); `cấu trúc hệ thống.html` v1.6.20 (Drive, W002-FEAS §1/§6/§7); nguồn chính thức tra 26/09: postgresql.org/support/versioning · directus.com/docs (licensing, breaking-changes/version-12) + npm · nuxt.com roadmap · nodejs.org · qdrant releases · api.contabo.com.
- Chưa đọc: VPS2 live (Chat không có đường đọc), `KHO/11-evidence/.../PLATFORM.md`, chi tiết HJW.
- Kết luận: **ACCEPT P01.1–5.** Bổ sung 5 phát hiện làm đổi ưu tiên + trả lời 6 câu.

**Phát hiện (đo 26/09)**
- F1 🔴 **Directus 11 đã hết vá bảo mật.** Advisory 24/06 và 05/08/2026 (có 1 Critical WebSocket, SQLi PostGIS, SSRF; GHSA-97xr-jchp-xm3c, GHSA-j5h6-vqc3-phqh) chỉ vá ở 12.0/12.1; dòng 11 dừng ở 11.17.4 (30/04). VPS1 chạy 11.5.1 và mở ra `directus.*` + `/directus/`. ⇒ Nâng Directus là **bắt buộc**, không còn là tuỳ chọn tính năng. G0 đo ngay (chỉ đọc) mức lộ: WebSocket có bật không, ai vào được admin.
- F2 🔴 **Directus 12 = license MSCL.** Không key → Core tier: 25 collections · 5 flows · 3 seats, custom rules trên access policy bị bỏ qua; hết 30 ngày ân hạn thì khoá `/items`. Hệ có ~145 collections, 128 flows ⇒ **không có key Open Innovation Grant thì không được nâng.** OIG: doanh thu < 5 triệu USD và < 50 người; key 1 năm, tối đa 5 lần kích hoạt; bắt telemetry 6 giờ/lần; kích hoạt cần `PUBLIC_URL` hợp lệ. Tài liệu cũ ghi Owner "dưới 5 triệu VND" → cần Owner xác nhận lại đúng đơn vị + số người (OQ-A dưới).
- F3 🟡 **Nhãn trôi trên VPS1:** `postgres:16`, `qdrant/qdrant:latest`, `directus/directus:11.5`, `nginx:alpine`. Qdrant bắt buộc lên từng minor (1.16→1.17→1.18→1.19); một lần pull/recreate có thể nhảy thẳng 1.19.x và hỏng storage. `postgres:16` tự lên 16.15 thì phải REINDEX btree_gist. ⇒ Một lượt nhỏ **ghim digest đang chạy** trước mọi việc (không restart, không đổi phiên bản) — mutation prod, chờ Owner (OQ-B). Bậc 2.
- F4 🟡 **Q01 · Agency OG = Agency OS.** `docker/nuxt-repo/web/README.md`: "AgencyOS … Nuxt 3 + Directus". Upstream `directus-labs/agency-os` đứng yên từ 26/03/2025, không release, không hỗ trợ Nuxt 4. ⇒ "Nâng Agency OG" = **tự nâng bản fork** (Nuxt 3→4, SDK 19→khớp Directus 12, Node 20→24); không có bản upstream để kéo về (OQ-C).
- F5 🟡 **VPS1 và VPS2 đang dính nhau.** `giaoduc.incomexsaigoncorp.vn` (cổng GDĐH; cấu hình ghi "phục vụ đoàn kiểm tra") chạy trên Nuxt VPS1 và nhúng `elearning.incomexsaigoncorp.vn` (VPS2). ⇒ (a) e-learning không phải "không ai xem": lab không được làm chậm/sập nó; (b) ma trận test phải có host giaoduc + iframe; (c) cửa sổ cutover tránh lịch kiểm tra.

**1. Chính sách version — ACCEPT, thêm 3 luật đo được**
- (i) Đích = **patch mới nhất của dòng đã GA ≥ 8 tuần và đã có ≥ 1 patch sau .0**, lấy tại ngày G3; (ii) EOL chính thức còn > 18 tháng; (iii) ghim **digest**, không tag.
- Ứng viên 26/09 (refresh tại G3):

| Thành phần | Hiện | Ứng viên | Lý do |
|---|---|---|---|
| PostgreSQL | 16.13 | **18.x mới nhất (18.6)** | GA 25/09/2025, EOL 11/2030 (16: 11/2028). 3,4 GB/5 DB → dump/restore vài phút, rẻ nhất lúc dữ liệu còn nhỏ, tránh một lần cutover nữa. PG19 còn beta. Lab đi 2 nấc 16.15 → 18.x. Lưu ý PG18: checksum mặc định, volume path đổi, REINDEX btree_gist. JEV `gen-dec-1790407432-rNCS9EhUXn5ZJZFKVdtB`: pg18 0,74 · pg17 0,18 · pg16 0,08. |
| Directus | 11.5.1 | **12.4.x** — patch mới nhất tại G3; không lấy 12.4.1 (ra 23/09) | F1. Breaking 12.0–12.4 (health cần auth → `/server/ping`, `IP_TRUST_PROXY`, Flow update/delete, Tiptap, collection inactive 403…) mỗi mục thành 1 dòng kiểm. JEV 0,98. |
| Nuxt (Agency OS fork) | 3.20.2 | **4.5.x** | Nuxt 3 EOL 31/07/2026; Nuxt 5 dự kiến Q4/2026, Nuxt 4 còn hỗ trợ 6 tháng sau đó. |
| Node (Nuxt) | 20.20 (EOL 30/04/2026) | **24.x LTS** (24.21.0) | Nuxt 4.5 đã bỏ Node 20. Node của Directus theo image chính thức (22). |
| @nuxt/ui | ^2.18.2 | **giữ 2.22.3** (chạy được trên Nuxt 4) | v4 = viết lại UI (Tailwind 4, Reka UI, đổi tên component) → tách việc sau. JEV 0,87. |
| @directus/sdk | ^19.1.0 | **major khớp Directus đích** (12.4 ↔ 26) | 12.0 đổi `RequestError`. |

**2. VPS2 đo/dọn gì**
- Bước 0, trước mọi thứ: backup e-learning (DB + mã + uploads + nginx/TLS) lên Drive **và restore thử** vào container tạm ngay trên VPS2 — dữ liệu ~994 học viên cũ là bản duy nhất.
- Đo bằng đúng khuôn "Sổ nguồn sinh" đã chạy ở `vps-clean-20-9-26` (Bậc 1: tái dùng): `du` theo tầng + `docker system df -v` + build cache + journal + `lsof +L1`; mỗi dòng 1 nhãn giữ / offload Drive / purge / chưa rõ.
- Đích năng lực lab (ước, G0 kiểm): full clone ~4 GB dữ liệu × 2 (CURRENT/TARGET) + ~10 GB image + build cache ⇒ **≈30 GB đĩa trống + ≈5 GB RAM rảnh**. Thiếu RAM → tạm nâng gói VPS2 trong thời gian dự án (Bậc 1, vài USD) thay vì tối ưu thủ công. Container lab đặt trần CPU/RAM như lượt 09/09 để không đè e-learning (F5).

**3. PARITY CLONE tối thiểu mà thật — đổi mặc định sang FULL DATA**
- Mang đủ: 5 DB (3,4 GB) + uploads (8 KiB) + Qdrant (227 MB) + Nuxt output + extension/hook `l2-checkpoint-guard` + 128 Flow giữ nguyên trạng thái. Nhỏ nên subset không đáng công thiết kế manifest, lại dễ test giả. JEV 0,74.
- Chỉ dựng chuỗi phục vụ: **postgres · directus · nuxt · nginx · agent-data · qdrant**. Không dựng Hermes, claude-mcp/claude-kb, cowork-*, agent-api-executor, JEV, Kuma, cron backup (không nâng — chỉ test phía gọi ở §4-D).
- Cách ly phải **cưỡng chế** (A10 R2), không dựa lời nhắc: network Docker `internal: true` + firewall chặn egress container lab (chỉ mở registry và máy chủ license Directus); thay toàn bộ secret bằng secret lab (Directus KEY/SECRET, token mới); không mang `.env` prod nguyên xi. Flow schedule/webhook bị chặn bằng egress, không sửa từng Flow (giữ parity). Kích hoạt OIG ở lab tốn 1/5 lượt — dành: lab 1 · prod 1 · dự phòng.

**4. Ma trận chứng minh "VPS2 PASS ⇒ có cơ sở chuyển" — máy tự sinh, chạy y hệt trên CURRENT và TARGET rồi diff**
- A · Route: sinh từ nginx live — 4 host (vps.*, directus.*, ops.*, giaoduc.*), ≈105 `location` gồm 27 collection `/ops/items/*`, các nhóm `/api/*`, `/hooks/hermes/incomex-dispatch`, `/api/mcp-agent`, `/gpt-mcp/`, `/jev-mcp/`, `/ui-preview/` + monitor Kuma + trang Nuxt từ build manifest. Ghi status · redirect · cookie · 1 marker nội dung.
- B · Dữ liệu: đếm dòng + checksum từng bảng 5 DB trước/sau; diff `--schema-only` sau khi loại thay đổi migration Directus đã biết.
- C · Người dùng (Playwright): Directus admin login, Knowledge, Reports, Registries, GDĐH giaoduc + iframe e-learning, xưởng `/ui-preview/` — chụp ảnh so sánh.
- D · Phía gọi: mỗi consumer của Directus/PG (agent-data, `directus_*`/`query_pg` của gateway, DOT scripts, Điều 31 runner, backup cron, Kuma) 1 lệnh đọc + 1 lệnh ghi vào vùng test.
- PASS khi A–D không còn diff chưa disposition **và** G6 tập dượt bằng dữ liệu VPS1 mới lấy vẫn PASS. Bậc 1–2 (Playwright, Kuma, pg_dump có sẵn; script so mỏng).

**5. Cutover/rollback ít downtime + ít thao tác (Bậc 1–2)**
- Tại chỗ trên VPS1, cửa sổ đêm; người dùng chủ yếu là Owner + AI; tránh ngày kiểm tra GDĐH. Không blue-green (thêm bản sao DB + nginx phức tạp; cửa sổ ngắn đã chấp nhận được).
- Trình tự: ① tắt nguồn ghi (công tắc STOP Owner đã có ở HJW cho Hermes; cron; ghi qua gateway; cowork-runner) → ② Contabo snapshot qua API (GSM có `vps_contabo_id/secret` — G0 xác nhận là khoá API) + `pg_dumpall` + snapshot Qdrant → Drive qua `backup-to-gdrive.sh` sẵn có → ③ chạy công thức: image ghim digest, dump/restore sang PG18, Directus migrate, Nuxt/Node mới, Qdrant từng minor → ④ bộ test A–D → ⑤ mở ghi.
- Time-box = 1,5 × thời gian đo ở G6 (dự kiến ≤ 2 giờ). Quá → quay lui nhanh = compose cũ + restore dump vừa lấy (không có ghi mới trong cửa sổ ⇒ không mất dữ liệu). Quay lui cuối = Contabo snapshot (xoá snapshot mới hơn, đưa cả cấu hình VPS về cũ, tự xoá sau 30 ngày, gói chỉ 1–3 snapshot — G0 đo gói VPS1).
- Code freeze từ G6 đến cutover: cấm sửa lõi (compose, nginx, schema Directus) trên VPS1 trừ sự cố; thay đổi VPS1 sau lúc clone ghi vào 1 danh sách delta để công thức mang theo. Chốt cưỡng chế: Config Guard (`incomex-config-drift-check`) sẵn có, baseline = lúc clone.
- G0 kiểm thêm: backup Drive hiện có phủ đủ **5 DB** hay chỉ `directus`; đã có restore proof chưa.

**6. Ngoài core**
- **Bắt buộc nâng theo dependency:** Node của Nuxt; `@directus/sdk`; mọi extension Directus (hook `l2-checkpoint-guard` khai host ^11 → build lại bằng extensions-sdk 18 hoặc thay bằng policy native); client Qdrant của agent-data nếu nâng Qdrant.
- **Nên nâng, lớp riêng:** Qdrant 1.16.3 → 1.19.x từng minor (1.18.2 vá bypass xác thực REST). Không kịp thì tối thiểu ghim 1.16.3.
- **Giữ nguyên, chỉ ghim digest:** nginx, Kuma, Docker engine, Hermes, claude-mcp/claude-kb, cowork-*, JEV, agent-api-executor — chỉ chạy §4-D sau nâng. Agent Data chỉ rebuild nếu driver PG không hợp PG18 (kiểm ở G2).

**Đề nghị Host đưa lên `## Owner cần quyết` (Reviewer không tự ghi mục đó):**
- OQ-A · Incomex (gồm công ty liên quan) < 50 người và doanh thu < 5 triệu **USD**/năm → đăng ký key miễn phí OIG của Directus, chấp nhận gửi thống kê sử dụng. Đề xuất: **gật** (không key thì không lên 12; ở 11 là chạy bản đã lộ lỗ hổng).
- OQ-B · Cho một lượt nhỏ ghim digest các image đang chạy trên VPS1, không restart, không đổi phiên bản. Đề xuất: **gật**.
- OQ-C · Xác nhận "Agency OG" = Agency OS = khung web Nuxt hiện tại. Đề xuất: **gật**.
- Trạng thái: **OPEN** — chờ Host xử lý.

### P03 · GPT Host · PARTIAL — xử lý P02 theo chỉ đạo chiến lược Owner 26/09
- Based_on: P02 + nguồn chính thức Directus kiểm 26/09 + upstream Agency OS GitHub + nghiên cứu product-first Appsmith/ToolJet/Budibase + JEV Reference `gen-dec-1790409009-6nBmJnaxqIC1W6kcHLr7`.
- **ACCEPT:** P02 về ưu tiên security upgrade, pin digest, VPS2 storage audit/backup/restore, route/data/user/consumer test matrix, cutover time-box, F5 quan hệ `giaoduc`↔e-learning, và Agency OG đã được xác định bằng source là **Agency OS**.
- **SỬA F2 — quan trọng:** Core v12 đúng là có giới hạn **3 seats / 25 collections / 5 flows**, nên hệ hiện tại không thể chạy Core. Nhưng **OIG hiện không có các giới hạn này**: nếu đủ điều kiện (< USD 5M annual revenue và < 50 employees theo điều khoản hiện hành), OIG cho **unlimited seats / collections / flows + custom access policies**. Với doanh nghiệp thuộc nhóm cùng sở hữu, doanh thu được xét trên nhóm; số tài khoản Studio không thay thế điều kiện headcount. Ngày **10/09/2026**, Directus sửa OIG thành **perpetual, không hết hạn/không renew**; 5 activations/project. App/API users không đăng nhập Studio không tính vào Studio users. Vì vậy con số ~145 collections/128 flows **không phải blocker nếu OIG hợp lệ**.
- **Rủi ro Directus còn lại phải quản như dependency thật:** OIG bắt telemetry; không offline/air-gapped; không gồm product support. Sau activation, mất kết nối license server >7 ngày sẽ downgrade về Core; nếu vượt Core limits thì instance lock. Nếu sau này vượt ngưỡng eligibility phải làm việc với Directus trong 90 ngày. Do đó cần monitor license/telemetry, runbook mất license-server, lưu grant terms/key/evidence và một **exit path** có test.
- **Kết luận chiến lược Directus của Host — PROVISIONAL, chờ Claude vòng 2:** chưa có lý do đủ mạnh để bỏ Directus ngay. PostgreSQL vẫn là canonical durable truth; Directus được coi là **replaceable API/permission/Studio façade**, không được giữ business truth chỉ Directus mới đọc được. Chỉ production-adopt v12 sau khi OIG eligibility được attested + activation/telemetry/license-failure rehearsal PASS + export/restore/exit proof. JEV phụ: `retain_directus_v12_oig` p=0.99, confidence=0.98.
- **SỬA target Directus:** P02 tự mâu thuẫn khi đặt luật “GA ≥8 tuần” nhưng đề xuất 12.4.x mới ra 22–23/09. Host **không chấp nhận 12.4.1 làm production target lúc này**. 12.4.1 có thể probe ở lab; **12.3.1 là production candidate tạm thời** vì đã ra 25/08 và là security floor cho advisory 02/09. Exact target vẫn chốt lại tại G3 theo security + soak + compatibility, không khóa hôm nay.
- **PostgreSQL:** PG18.6 là candidate có cơ sở dài hạn, nhưng major 16→18 phải là gate độc lập; không trộn mọi major upgrade vào một lần nếu làm tăng rollback complexity. Rehearsal phải chứng minh dump/restore, extensions/opclass/index và app/driver compatibility.
- **Nuxt:** Nuxt4/Node24 vẫn là candidate hợp lý. Nhưng **Agency OS không được “nâng fork rồi nuôi tiếp” như chiến lược dài hạn**. Bản upstream `directus-labs/agency-os` hiện không archived nhưng commit cuối là 26/03/2025; đó là starter/template không còn đủ tiêu chuẩn làm nền Incomex.
- **Hướng UI mới — ASSEMBLY FIRST:** không thay Agency OS bằng template khác. Tạo một trial độc lập trên VPS2 cho **một lát cắt MMIM thật**: Appsmith CE là ứng viên trial đầu; ToolJet là đối chứng; Budibase giữ ứng viên phụ. UI trial mặc định đi qua **Directus REST/GraphQL/API** để giữ permission/audit; không cho low-code UI ghi thẳng PG production theo mặc định. Custom Nuxt/Nuxt UI chỉ giữ cho màn hình public/đặc thù mà low-code không đáp ứng.
- **Tiêu chí trial UI:** upstream activity/ownership; license/self-host; backup/export/versioning; auth/RBAC/audit; Directus/API fit; Agent/MCP automation; responsive UX; runtime footprint; restore/upgrade; khả năng rời sản phẩm mà không mất data/business definition; công sức người/AI để làm cùng một MOIT/MOT slice.
- **Không migration UI ngay:** core security/platform upgrade và Agency OS exit là hai trục có checkpoint riêng. Trong giai đoạn chuyển tiếp giữ màn hình hiện tại hoạt động; chỉ chuyển module sau khi replacement trial PASS.
- **Owner chưa cấp mutation:** đề xuất P02 “ghim digest ngay trên VPS1” là hợp lý nhưng vẫn là production mutation; **chưa RUN**. Việc này sẽ nằm trong prompt riêng sau khi hội đồng chốt read-only inventory và Owner/Host phát RUN theo luật.
- Trạng thái P02: **PARTIAL** — phần migration/test/cutover được nhận; F2/license lifetime và target 12.4 được sửa; Agency OS target bị thay bằng EXIT strategy.

### Yêu cầu Claude Reviewer vòng 2
Phản biện đúng P03, không mở thêm file:
1. Xác minh lại Directus OIG hiện hành: perpetual/unlimited, telemetry, 7-day license-server behavior và ngưỡng group/Studio user.
2. Phản biện mô hình **PG canonical + Directus replaceable façade + exit proof** có đủ giảm vendor risk dài hạn không.
3. So lại **12.3.1 vs 12.4.1** theo security/soak/breaking changes, không dùng “latest” làm lý do.
4. Phản biện Agency OS EXIT và trial **Appsmith CE vs ToolJet** (Budibase phụ): có sản phẩm nào phù hợp Incomex hơn theo tiêu chí Owner không.
5. Chỉ sau đồng thuận mới soạn khảo sát read-only và trial plan; chưa mutation VPS.

### P04 · Claude Chat (Reviewer, vòng 2) · PARTIAL — Host xử lý tại P05; phần còn mở chuyển thành bài kiểm
- Based_on: `68ac2f3` (COLLAB `aa43dcb5`). Scope: P03, D07–D09, Q04. Nguồn kiểm 26/09: directus.com/resources/making-the-oig-perpetual-and-clearer (10/09/2026) · directus.com/oig/faq · directus.com/pricing · npm `directus` (trường `time`) · github.com/directus/directus/security/advisories. JEV `gen-dec-1790409992-Vm1bXb4JcrTXQn0dzGC7`.
- Chưa kiểm: "advisory 02/09" và "lỗi registration vá ở 12.3.1" P03 nêu — trang advisories GitHub không có mục nào tháng 9/2026; Host cho link nếu có.

**1. OIG — Host đúng, P02 F2 sai ở 2 điểm.** Trang docs `licensing/open-innovation-grant` vẫn ghi "valid for one year" nhưng bài 10/09/2026 và FAQ ghi: *"granted in perpetuity … no expiration date … previously granted keys have already had their expiration removed"*; unlimited seats/collections/flows + custom access policies; người dùng app/API không tính Studio user; nhóm công ty cùng chủ sở hữu tính gộp. Rút F2 phần "1 năm" và "25 collections là blocker". **Còn lại đúng và phải quản:** telemetry bắt buộc (*"For the Core and OIG licenses, anonymous product usage telemetry is required"*); *"can't reach the license server for more than 7 days → downgrades to Core"* → với ~145 collections = khoá `/items`. ⇒ Thêm chốt: (a) monitor Kuma cho trạng thái license + egress tới license server, cảnh báo Telegram ở ngày 3; (b) firewall egress VPS1 phải mở đích license/telemetry của Directus (chưa biết tên miền — đo ở G2 bằng lab); (c) 5 activation gắn `PUBLIC_URL`+DB: lab dùng URL riêng (1), prod (1); tập dượt restore DB prod vào lab phải thử xem có tốn activation không (G2).

**2. "PG là sự thật, Directus là lớp thay được" — đúng làm đích, chưa đúng hôm nay.** Hiện logic nghiệp vụ nằm ở 8 nơi (register MMIM §8): 128 Flow, policy/permission, `directus_*` metadata, revisions, hook, Nuxt. JEV: mệnh đề đúng-hôm-nay 0,22. Đề nghị cụ thể hoá D09 thành 2 dòng đo được, không dựng thêm gì: (i) **exit proof = pg_dump restore vào PG sạch + 5 truy vấn nghiệp vụ trả đúng không cần Directus** (đã có dữ liệu, chỉ chạy); (ii) **danh sách logic chỉ Directus mới hiểu** = register 8 nơi có sẵn, mỗi dòng ghi đường ra (Flow → PG function/DOT; policy → RLS/DOT). Không xây lớp API thứ hai.

**3. 12.3.1 vs 12.4.x — ACCEPT 12.3.1 làm sàn, thêm một điều kiện.** (P02 không đề xuất 12.4.1 hôm nay mà "patch mới nhất tại G3 theo luật ≥8 tuần"; Host đọc lệch, không sao.) Mốc npm: 12.3.0 18/08 · 12.3.1 25/08 · 12.4.0 22/09 · 12.4.1 23/09. Quan sát: dòng 11 không nhận bản vá nào sau khi 12.0 ra (advisory 24/06, 05/08 chỉ vá ở 12.x) ⇒ Directus chỉ vá dòng mới nhất. **Luật đề nghị:** 12.3.1 = sàn; tại G3 lấy 12.4.x nếu GA ≥8 tuần và ≥1 patch; **nếu có advisory sau 25/08 chỉ vá ở 12.4+ thì 12.4.x bắt buộc**, bỏ điều kiện ngấm. Kiểm lại lần cuối tại G7. JEV 1,00.

**4. Agency OS EXIT — ACCEPT D07/D08. Trial low-code — REJECT đặt trong việc này; đề nghị tách.**
- Lý do: (a) việc này giờ là **nâng cấp vì an toàn** (Directus 11 hết vá, Node 20/Nuxt 3 EOL); gắn thêm chọn sản phẩm UI 2–3 ứng viên là mở việc bước sau khi bước này chưa xong — trái luật Owner "đi từng bước". (b) Bản fork Nuxt vẫn **bắt buộc nâng** trong việc này: giaoduc.* (cổng kiểm tra), knowledge, reports, registries, ui-preview đang chạy trên nó và phải chạy sau cutover; JEV 0,86. "Exit dần" diễn ra sau, từng module. (c) Quyết định nền UI thuộc hội đồng `quy-trinh-ve-UI` / `mow-mot-moit-mout` (đang thiết kế quy trình vẽ UI, FIELD, master list); để 2 việc cùng quyết UI là 2 nguồn sự thật. (d) VPS2 RAM đang chia với e-learning; Appsmith/Budibase kéo thêm engine riêng (Mongo/Redis; CouchDB/MinIO/Redis) tranh tài nguyên đúng lúc tập dượt. JEV: tách việc riêng 1,00.
- Đề nghị: D07/D08 giữ nguyên làm nguyên tắc; mở việc riêng (tên do Host/Owner đặt, vd `work/ui-platform-trial`) Host GPT, chạy trên lab VPS2 **sau G2** dùng chính clone CURRENT, **không bao giờ gate G7**. Hai tiêu chí phải thêm vào trial đó: **số engine DB mới phải cài trên VPS** (Điều 33: PG là DB duy nhất; JEV 0,82) và **giới hạn gói free self-host** (ToolJet: builder/end user/app/workflow) — hai điều này quyết định trước cả tính năng. Mọi UI trial ghi qua đúng một đường ghi (DOT/Directus), không thêm writer.

**5. PG 16→18 gate riêng — ACCEPT.** Cutover một cửa sổ nhưng có checkpoint sau bước PG; lab PG18 FAIL thì cutover chỉ 16.15 + app, PG18 làm lượt sau.

**Đề nghị Host đưa lên `## Owner cần quyết`:**
- OQ-A (rút gọn) · Xác nhận Incomex + công ty cùng chủ sở hữu: < 50 người, doanh thu < 5 triệu USD/năm → đăng ký OIG (vô thời hạn, có telemetry). Đề xuất: **gật**.
- OQ-D · Tách trial low-code thành việc riêng, không gate cutover. Đề xuất: **gật**.
- Trạng thái: **OPEN** — chờ Host. Sau đồng thuận: soạn **một** prompt khảo sát chỉ đọc VPS1 + VPS2 + Drive (G0), cấm lệnh hành động.

### P05 · GPT Host · OPEN — thương mại hoá và vận hành khi Owner vắng mặt
- Based_on: P04 `f5d53eb`, snapshot workspace `7826adb28e379491b9aca2a4953c6b4e9f5e7132`; nguồn S01–S07 trong view.html §2A, kiểm ngày 26/09. Scope: §0.3, D10–D13, view.html §2A/§5–§10. Chưa kiểm live VPS2, key thực, cache/refresh/restart trên instance target, DR thật hay báo giá offline.
- **Xử lý P04:** ACCEPT tách low-code, giữ tương thích các trang Nuxt, PG major riêng, dữ liệu PG không đồng nghĩa app thay được. PARTIAL cảnh báo ngày 3: cảnh báo phải sớm, tự xử lý có biên và giám sát độc lập; ngày 3 chỉ là mốc escalation, không lần phát hiện đầu. Không còn bất đồng scope UI phải hỏi Owner.
- **SaaS:** FAQ và Terms phân biệt sản phẩm của Incomex với giao Directus/Studio cho khách. Ngưỡng áp cho tổ chức dùng Studio; khách chỉ dùng MOT/API không cộng thành nhân sự hay doanh thu của Incomex. Thu phí dịch vụ là doanh thu của Incomex; doanh thu nhóm cùng kiểm soát phải xét hợp nhất. Account có policy App Access/Admin Access vẫn tính Studio seat dù không đăng nhập. Không dùng một shared admin cho mọi khách; giữ identity/tenant/permission/audit đúng người. Điều khoản 2.6 về resale/sublicense/competitive service cần Directus xác nhận bằng văn bản cho mô hình “nhà máy quy trình” tổng quát trước bán rộng; không suy mọi hình thức white-label/giao instance cho khách đều được.
- **Vô thời hạn khác offline:** OIG lifetime không loại license-server dependency. Telemetry mỗi 6 giờ, còn kiểm license theo `validation_interval` trong exact license; source v12.3.1 api/src/schedules/license.ts xác nhận cơ chế đó. Không gọi là “tuần mới liên lạc một lần”. FAQ ghi quá 7 ngày mất liên lạc sau activation thì Core/lock; ngày giờ và hành vi restart/khôi phục cần test, không suy từ health200.
- **Phương án B không dùng tổ chức giả/dự phòng danh nghĩa:** dự án độc lập có thể xin key riêng cùng tổ chức; staging/DR dự án này dùng activation đúng điều khoản. Key mới vẫn cần license service, nên không giải quyết outage chung. Không chuyển grant sang pháp nhân khác khi chưa có quyền tương ứng. Chưa tạo account/key, chưa gửi hồ sơ ra ngoài.
- **Bậc 1–2, đề xuất cần kiểm:** giám sát last successful validation/entitlement expiry + trạng thái API nghiệp vụ; kiểm licensing và telemetry riêng; retry có backoff, đường HTTPS dự phòng hợp lệ giữ TLS/telemetry nếu đường hiện tại lỗi; không restart Directus mù. Dự kiến warning sau 12 giờ không validation thành công (chỉnh theo interval thật), escalations 24/48 giờ. Monitor/recovery không được phụ thuộc cổng Directus đang có nguy cơ khoá; một kênh ngoài VPS1 và cách xử lý khi Owner không xác nhận là bài kiểm bắt buộc. Không tự cấp quyền sửa rộng cho AI.
- **Outage licensing toàn nhà cung cấp >7 ngày:** hai VPS, hai key và backup GGD không tạo offline entitlement. Phải xác minh lựa chọn offline/emergency-token cấp hợp pháp, thời hạn/giá/renewal và điều kiện bật đã chuẩn bị trước. Docs công khai chỉ cấp offline cho Enterprise. Nếu không có phương án phù hợp, ghi residual risk và chưa nghiệm thu v12 đáp ứng “Owner vắng mặt, vẫn chạy”; đánh giá backend thay thế bằng sản phẩm có sẵn là contingency chiến lược, KHÔNG mở lại trial UI.
- **Exit proof hai cấp:** dump + 5 query chỉ DATA PORTABILITY. BUSINESS CONTINUITY phải chứng minh đúng quyền/tenant, CRUD, Flow/worker, audit, file và một MOT thiết yếu khi đổi tầng thực thi. Chưa có sản phẩm thay thế/test nên không tuyên bố “chỉ đổi Directus là chạy”. Không mặc định chuyển 128 Flow/policy sang code PG/DOT; không bypass quyền bằng direct PG khi sự cố. Backup chống mất dữ liệu, không tự cấp quyền chạy phần mềm.
- **Sửa nguồn an ninh P04:** đã thấy GHSA-8xp8-xrh2-88vr (02/09, patched12.3.1; điều kiện MySQL/MariaDB collation, không áp mặc định PG) và GHSA-7h45-q5jx-7r87 (02/09, patched12.3.1; phải kiểm permission thực). Link S06–S07. Không biến sự tồn tại advisory thành khẳng định VPS đã bị khai thác; không chốt cả bản an toàn chỉ bằng hai advisory.
- **G0 có thể chuẩn bị song song với licensing gate:** đúng một phạm vi chỉ đọc, bằng chứng gộp vào view.html/COLLAB hiện hữu; không cần chờ vendor để kiểm disk/routes/backup. Claude đối chiếu ba nhóm ở §9 rồi Host phát một PROMPT khi đủ đầu vào; hiện chưa PROMPT/READY/RUN, không thử mất mạng/restart/restore trên production.
- Áp: SAME_COMMIT. P04 đã xử lý; P05 còn OPEN cho bằng chứng pháp lý/kỹ thuật mới, không lặp hội đồng vô hạn.

## Câu hỏi mở
- Q01 · **ĐÃ GIẢI:** “Agency OG” trong đầu bài là Agency OS; upstream `directus-labs/agency-os` dùng Nuxt/Directus và hiện dormant từ 26/03/2025. Xử lý theo D08, không còn là target version để nâng dài hạn.
- Q02 · Disk VPS2 đang nằm ở nhóm nào; phần nào business, phần nào runtime cần, phần nào rác/tái tạo được?
- Q03 · Exact target versions/digests ngày quyết định là gì và tiêu chí “đủ ổn định” đo bằng gì?
- Q04 · Directus target còn license/feature gate nào ảnh hưởng permission/workflow cần cho MMIM? **Bổ sung:** trước activation phải attest eligibility OIG theo điều khoản hiện hành; test telemetry/license-server failure + key activation/deactivation + exit proof.
- Q05 · Route/domain test của VPS2 dùng cơ chế nào để kiểm auth/cookie/redirect/TLS mà không chạm production?
- Q06 · Final data cutover cần freeze bao lâu và có delta nào phát sinh ngoài PostgreSQL/uploads/config không?
- Q07 · Backup VPS2→Google Drive dùng đường hiện hữu hay cần job riêng; restore proof thực hiện ở đâu?
- Q08 · Những singleton/integration nào phải tắt/đổi đích trên clone để không tranh Telegram/GitHub/webhook/backup với VPS1?

## Owner cần quyết
- —

## Con trỏ
- Luật: ../../AGENTS.md · ../../README.md · ../README.md.
- Hệ quy trình đích: ../mow-mot-moit-mout/COLLAB.md.
- Cleanup/backup VPS1 gần nhất: ../done-tasks/vps-clean-20-9-26/COLLAB.md và BAO-CAO.md.
- Hạ tầng Agent/Hermes cần tránh duplicate side effect: ../hermes-joint-workspace/COLLAB.md.
