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
VPSUP | MỤC TIÊU ĐÃ XÁC NHẬN · đang mở vòng khảo sát/kế hoạch | Chưa PROMPT/READY/RUN | NEXT: Claude review P01 + khảo sát read-only VPS1/VPS2/backup/version candidates trước khi Host chốt kế hoạch.
- HEAD trước mở việc: `545157ae4d0a58d72274063800ad0b65d9ad76ef`.
- Lượt này chỉ tạo SSOT của task; không mutation hạ tầng.
- Áp: SAME_COMMIT.

## Quyết định Owner
- D01 · 2026-09-26 · **MỞ VIỆC:** tạo `work/vps1-up-grade` để hội đồng lập kế hoạch nâng cấp VPS1 qua rehearsal trên VPS2. Chưa cho phép thực thi nâng cấp.
- D02 · 2026-09-26 · **TOPOLOGY:** VPS1 là production tiếp tục chạy; VPS2 dùng làm nơi dựng/nâng/fix/test trước khi chạm VPS1.
- D03 · 2026-09-26 · **CORE PRIORITY:** PostgreSQL + Directus + Nuxt + Agency OG là nhóm cần xem xét nâng cấp ưu tiên để phục vụ hệ MOW/MOT/MOIT/MOUT. Thành phần khác hội đồng cân đối.
- D04 · 2026-09-26 · **VERSION POLICY:** GPT + Claude phải thống nhất phiên bản “mới nhất nhưng ổn định”; không chọn bleeding-edge thiếu bằng chứng, cũng không neo bản cũ nếu làm mất tính năng hữu ích.
- D05 · 2026-09-26 · **VPS2 STORAGE:** phải khảo sát vì e-learning gần như không hoạt động nhưng VPS2 dùng hàng chục GB; Owner ước workload thực chỉ khoảng ~3GB. Có thể dọn phần vô ích nhưng phải phân loại/backup trước.
- D06 · 2026-09-26 · **BACKUP ASSET:** ngoài 2 VPS có Google Drive dung lượng lớn; VPS1→Google Drive đang kết nối ổn định. Kế hoạch phải tận dụng tài sản này để giảm rủi ro và thời gian.

## Ý kiến hội đồng
### P01 · GPT Host · OPEN — kiến trúc làm việc đề nghị Claude phản biện
- Based_on: chỉ đạo Owner 26/09 + rehearsal lịch sử 08–11/09 + việc `vps-clean-20-9-26` đã đóng.
- Scope: `view.html` §1–§10.
- Đề nghị:
  1. Không “copy nguyên VPS2 về VPS1”; chuyển **reproducible deployment formula** đã chứng minh: exact image/digest + compose/config + migrations + runbook + acceptance tests.
  2. Trình tự an toàn: **read-only inventory → backup/restore proof → VPS2 cleanup có kiểm soát → CURRENT parity clone → baseline route/slice → nâng từng lớp → TARGET same-slice → rollback rehearsal → cutover rehearsal → production cutover**.
  3. Chưa nâng Qdrant/Nginx/Docker/... chỉ vì có bản mới; chỉ nâng nếu dependency/security/tính năng cần thiết.
  4. Version target lịch sử 11/09 chỉ là reference stale; vòng này phải refresh nguồn chính thức rồi Claude cross-review.
  5. Production cutover phải time-box; quá gate thời gian hoặc core acceptance FAIL thì rollback, không “cố sửa trên production”.
- Trạng thái: **OPEN**, chưa là quyết định Owner.

### Yêu cầu Claude Reviewer vòng 1
Đọc `AGENTS.md` → §0 file này → `view.html`. Ghi phản biện P02 ngay tại đây, không tạo file review mới. Tập trung 6 câu:
1. Chính sách chọn exact version cho PG/Directus/Nuxt/Agency OG có đủ cân bằng mới–ổn định chưa?
2. VPS2 phải đo/dọn những gì để thật sự chỉ giữ e-learning + lab capacity cần thiết?
3. PARITY CLONE tối thiểu cần gì để không test giả nhưng cũng không copy production vô tội vạ?
4. Route/API/UI/runtime matrix nào đủ chứng minh “VPS2 PASS ⇒ có cơ sở chuyển VPS1”?
5. Cutover/rollback nào ít downtime và ít thao tác nhất với backup Google Drive đang có?
6. Thành phần nào ngoài core nên giữ nguyên, thành phần nào bắt buộc nâng do dependency?

## Câu hỏi mở
- Q01 · Exact component/version hiện hành của **Agency OG** là gì?
- Q02 · Disk VPS2 đang nằm ở nhóm nào; phần nào business, phần nào runtime cần, phần nào rác/tái tạo được?
- Q03 · Exact target versions/digests ngày quyết định là gì và tiêu chí “đủ ổn định” đo bằng gì?
- Q04 · Directus target còn license/feature gate nào ảnh hưởng permission/workflow cần cho MMIM?
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
