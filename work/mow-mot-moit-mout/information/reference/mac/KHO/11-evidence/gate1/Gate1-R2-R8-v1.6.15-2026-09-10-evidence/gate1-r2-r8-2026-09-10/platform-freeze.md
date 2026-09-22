# PLATFORM FREEZE — evidence package, chưa quyết/upgrade

**Verdict đề nghị: PLATFORM FREEZE BLOCKED BY OIG eligibility scope/headcount + target compatibility evidence.** Gate1 UI review vẫn có thể nộp PM; Gate2 chưa được mở. PM không nên tự mặc định tiếp tục build trên nền cũ trong lúc chờ. TARGET dưới đây là bộ ứng viên cụ thể cho quyết định/rehearsal sau, không hệ đã cài.

## CURRENT và TARGET tại 10/09/2026

| Thành phần | CURRENT từ evidence | TARGET stable candidate / căn cứ |
|---|---|---|
| PostgreSQL | **16.13**, production `source-database.json`, cùng snapshot actual-stack E01 trong SSOT; không lấy image tag thay version | **16.15**, released 13/08/2026; giữ major 16 để giảm đổi kiến trúc. [Versioning](https://www.postgresql.org/support/versioning/) / [16.15 notes](https://www.postgresql.org/docs/16/release-16-15.html). |
| Directus | **11.5.1**; tag 11.5; Node**22.14.0**; exact pinned image cùng lab được đo trong Gate0 | **12.3.1**, official latest 25/08; API package 39.1.0, SDK 25.0.1. [Release](https://github.com/directus/directus/releases/tag/v12.3.1), [official latest metadata](https://api.github.com/repos/directus/directus/releases/latest). |
| Nuxt / Nitro | **3.20.2 / 2.12.8**, actual mounted build 04/09; server Node**20.20.0**. Không suy `nuxt:^3.20.1` là installed | **Nuxt 4.5.2**, release 05/08. [Release](https://github.com/nuxt/nuxt/releases/tag/v4.5.2), [pinned package](https://raw.githubusercontent.com/nuxt/nuxt/v4.5.2/packages/nuxt/package.json). Nitro target exact phải lấy từ target lockfile sau khi PM cho rehearsal, chưa đoán. |
| Node pair | Directus/worker 22.14.0; Nuxt 20.20.0; local UI lab 20.19.6 là khác môi trường | Đề nghị **22.23.2 cho Directus/worker; 24.21.0 cho Nuxt**. Nuxt target chấp nhận `^24.11.0`; worker chấp nhận `>=22.12.0`; Directus official build chọn 22. Giữ hai nhánh runtime riêng như CURRENT, Nuxt chuyển từ 20 đã EOL lên 24 LTS; không ép Directus lên 24 hoặc buộc chung Node. [Official dist index](https://nodejs.org/dist/index.json), [Directus Dockerfile](https://raw.githubusercontent.com/directus/directus/v12.3.1/Dockerfile). |
| Runtime candidate | pg-boss**12.30.0**, pg**8.23.0**, schema 40, 21 locked packages, Node 22.14.0 | **Giữ candidate versions** cho first comparison; không nâng dependency cùng lúc nếu không có capability gap. TARGET integration vẫn chưa chạy. |

CURRENT là evidence đã có, được PM cho phép sử dụng, không phải đo lại production toàn bộ hôm nay. File receipts/hash nguồn ở [platform-current-evidence.json](platform-current-evidence.json). Chính thức đã tải được toàn bộ version/tag trên; 404 ở đường SDK monorepo đoán sai được giữ trong limitation, không dùng làm căn cứ SDK thiếu.

Nuxt 3 đã hết hỗ trợ theo lịch **31/07/2026**, không dùng lịch Jan cũ; Node 20 cũng EOL. Vì vậy OLD STACK CONTINUE chỉ có thể là quyết định PM với thời hạn/giới hạn, không mặc định đường build dài hạn. [Nuxt 4.5 announcement](https://nuxt.com/blog/v4-5), [Node release status](https://nodejs.org/en/about/previous-releases).

## Compatibility material — chưa rehearsal

| Asset | Evidence hiện có | Ảnh hưởng TARGET / việc phải chứng minh sau khi giao |
|---|---|---|
| Write guard candidate | Bundle 0.0.3 `host:11.5.1`; 163 dòng core + 2 entry + 50 SQL; các ca authority/conflict/audit đạt CURRENT bounded | **Manifest hiện không chấp nhận 12.3.1**. Không sửa host rồi coi PASS. Kiểm extension loading, hook/endpoint context, ItemsService errors, accountability và transaction/audit/replay trên target; so built-ins v12 trước giữ code. |
| Legacy L2 hook | Source E03 host`^11.0.0`, mirror client logic | Đây là hook khác candidate guard; cũng không bao phủ 12. Không trộn 2 scope, không tự xóa; cần consumer/authority disposition. |
| UI adapter + UForm | Gate0 generic adapter 87 dòng, UForm+9/−1; FormCustom source / 36 unchanged UI hashes trong declaration-only proof | Nuxt 4 thay data fetching/reactivity/layers/directory conventions; custom transport phải kiểm SSR/session/cookie, refresh/cache, 422/409/replay, query-prefill và profile validation. Không ép rewrite all pages. [Upgrade guide](https://nuxt.com/docs/4.x/getting-started/upgrade). |
| SDK / Nuxt packages | Source ranges SDK`^19.1.0`, NuxtUI`^2.18.2`, VueUse 13, ajv 8, diff 8; range không exact deployed resolution | Release Directus 12.3.1 có SDK 25.0.1 không chứng minh SDK 19 transport tương thích hoặc bắt buộc nâng. Cần lockfile target, peer/module compatibility của Nuxt UI 2/FormCustom/custom components; tận dụng current asset trước Nuxt UI major rewrite. |
| Worker / pg-boss / pg | Accepted bounded events→instances→attempts→guarded effects→ACK, duplicate/restart/pins trên CURRENT; engines pg-boss>=22.12, pg>=16 | Node 22.23.2 đáp ứng declared engine; PG 16.15 cùng major. Đây chỉ static compatibility. Chạy lại pinned-version/restart/duplicate/error/permission regressions sau authorization; không tính package-engine pass thành runtime pass. |
| PG minor | Production 16.13 →16.15 | Không cần dump/restore cho 16.x theo release notes; nhưng có thay đổi logical-decoding plugin allowlist, security cleanup và reindex liên quan btree_gist/ltree. Phải đối chiếu production extensions/slots/index usage khi rehearsal; không suy 3 extensions của lab bao phủ VPS. |
| License/config/native features | v12 thêm license enforcement; 12.3 native CLI sync + safer Update/Delete Flow defaults | TARGET built-in có thể giảm custom sync, nhưng không thay canonical release bundle/authority/missing-resume bằng CLI hoặc Flow label. Cần so theo contract, nhận định trên là candidate reuse. [12.3 notes](https://directus.com/resources/12.3-release-notes). |

## License: facts đã có và fact thiếu

Owner đã xác nhận doanh thu dưới ngưỡng miễn phí; **không hỏi lại số doanh thu này**. Chưa có evidence về tổng nhân viên full-time/part-time, pháp nhân/phạm vi nhóm chung kiểm soát và nhóm người trực tiếp đăng nhập Studio.

[OIG agreement cập nhật 28/08/2026](https://directus.com/terms/open-innovation-grant) quy định điều kiện doanh thu gross theo năm tài chính đã kết thúc/phạm vi hợp nhất, dưới 50 nhân viên, license key và nghĩa vụ telemetry. Marketing “ARR”/FAQ không thay bản điều khoản này. Chưa có key/activation evidence hoặc chấp thuận áp dụng điều khoản cho đúng deployment. Do đó **chưa kết luận miễn phí đủ điều kiện cho TARGET**. Không đăng ký grant, chấp thuận hợp đồng hay thay license config trong lượt này. [License overview](https://directus.com/license).

Fact/evidence cần để bỏ BLOCK: (1) Owner/PM xác nhận headcount + phạm vi pháp nhân và Studio users có phù hợp terms hiện hành, dùng lại doanh thu đã cung cấp; (2) trạng thái key/điều khoản deployment được xử lý đúng thẩm quyền; (3) target image/lockfile/module/guard compatibility và rehearsal được PM giao, gồm chọn Node exact trong image. Nếu PM quyết OLD STACK CONTINUE thì phải ghi quyết định rõ và giới hạn, không tự suy từ TARGET pending. R1/D03 và role map 5 pattern không phụ thuộc cần viết code mới vì các fact này.
