# NDW · P0 REPORTS — OWNER-ONLY CUTOVER, MỘT GÓI
RUN_ID: NDW-P0-OWNERONLY-CUTOVER-20261031-04
TASK: work/nhap-directus-for-workflow
EXECUTOR: Claude Code CLI, DOT là actor duy nhất ghi PG/Directus.
STATUS: DRAFT — CHƯA OWNER GO · CHƯA READY · KHÔNG ĐƯỢC CHẠY. READY RUN03 đã tiêu thụ, không dùng lại.
SOURCE: NDW P118 · Web PR686/a353b64e0252e667ffd5a3ea0f89119ff86aaa38 · CI41143018991 GREEN auth19/19 · Web main8100ae6fee828c51be6e1ac3a4fd3a7d78b6e6e0.

## Owner cần GO một gói có điều kiện
1. DOT tạo MỘT user người thật không admin, không static token, chỉ đọc Reports; Owner tự đặt mật khẩu/đăng nhập /auth/signin, AI không đọc/giữ.
2. DOT sửa CẢ HAI public Directus policies: v_report_home, v_report_pg, balo_thuc_the chỉ Owner; table_registry giữ đúng 21 dòng công khai, ẩn 7 dòng Reports và view_sql; entity_species và public /knowledge đang dùng giữ nguyên. Không đụng public 163 collection khác.
3. KST merge đúng HEAD PR686 và deploy Web GitHub main qua ghm-manual-deploy.py Nuxt4 Node24, private env NUXT_REPORTS_OWNER_USER_ID, Guard/lease. Sửa đúng 2 DOT verifiers dot-table-ui-verify và dot-verify-loai-report, kiểm hai callers dot-report-publish/dot-list-publish; thêm 2 Kuma checks phát hiện anonymous đọc Reports, receipt và rollback.
4. Cho phép tạm dừng CHỈ NONCORE đã biết, idle, whitelisted và phục hồi cùng lượt nếu RAM thiếu; không dừng core/Graph queue. T3 VPS code lock vẫn HOÃN. Không mua license hay tạo tài khoản GitHub/repo/task khác.
**Trước khi Owner GO rõ ràng và Host ký READY full SHA, mọi thao tác production đều CẤM.**

## DROOT60 — không để executor dừng ngay ở S0
- **Licensing Directus12 — CHƯA ĐO:** Core có thể bỏ qua custom row/field filter; phải xác minh effective entitlement/feature trước READY; không chỉ nhìn dữ liệu policy. Hai public policies additive: row OR, field union. Phải kiểm thực tế rằng cả hai hết wildcard mở 7 dòng và view_sql. Nếu license không đủ, STOP trước bất kỳ mutation; trình một phương án native/permission hợp lệ, không tự mua license.
- **Access — CHƯA ĐỦ:** P118 Claude SSH bị quyền chặn; chưa đọc root crontab, deploys/web-test, Nuxt compose/env, Kuma list, nginx candidate và rollback artifact. Host/Owner phải đảm bảo Actor/DOT/apply-v0/VPS-GHI/Guard có đường ghi thật được phép trước READY. Không vượt quyền qua query_pg hay verifier login/logout/POST/DELETE.
- **Resources — CHƯA ĐỦ:** snapshot 31/10 MemAvailable~3.1GiB, swap hầu như hết; build floor>=3.5GiB. Có phương án whitelist noncore idle hoặc không ký READY, không merge trước khi bảo đảm deploy và lùi.
- **Identity — CHƯA CÓ:** admin Directus đang là máy DOT, không dùng làm Owner. New human account cần /users/me id/status/role thật (không chỉ fixture), scope minimum; Owner tự đặt password, không giữ RUN chờ người dùng.
- **Rollback:** snapshot chính xác hai public policies, current Web artifact/config/Guard, prepare candidate nginx DENY chỉ /reports và /api/reports trước khi dùng binary Web cũ; không lùi ACL về mở công khai. Build/deploy/monitor phải đồng bộ.
- **Security debt ngoài P0:** context_pack_readonly/directus/incomex SELECT directus_users.token (P118). Không đọc token hay đưa vào public task; chuyển SECCRED/CONN-REPAIR hiện hữu, không tự revoke làm gãy DOT. Nếu chứng minh được đường khai thác public thật thì dừng release.
- **Monitoring:** measurement_log/PG-driven integrity ngừng từ tháng 7 là nợ trước đó; hai Kuma checks chỉ chứng minh cảnh báo từ chối anonymous trong phạm vi P0, không được tuyên Điều31 toàn hệ hồi phục.

## STEP_WALK (một gói, các bước là nội bộ)
S0 · TRƯỚC GHI: đọc AGENTS + NDW P118/P119 + PROMPT + Owner GO/READY, kiểm STOP, actor, GitHub branch/PR/CI, DIRECTUS LICENSE/ACL effective, DOT writer+VPS quyền, RAM, backup/Guard/nginx rollback và khả năng Owner đăng nhập. Nếu bất kỳ điểm cần ghi nào chưa thể chứng minh ⇒ báo một blocker và DỪNG TRƯỚC mutation. Không chờ trong RUN.
S1 · CHUẨN BỊ: snapshot ACL cả hai policies và Web SHA/artifact/config; soạn đúng 3 tables private + registry 21 public/7 private/view_sql; soạn Web build và config private, 2 DOT verifiers+2 Kuma, nginx fallback. Tạo user least privilege chỉ sau GO; Owner tự đặt mật khẩu và đăng nhập; nếu Owner chưa sẵn sàng thì KQ checkpoint an toàn, nhả lease, không giữ terminal.
S2 · CUTOVER: khi tất cả preconditions đạt, KST merge approved HEAD/CI, ghi main SHA, build/deploy chính SHA bằng Nuxt4 approved path và cập nhật env; DOT sửa policy đúng footprint theo Config Guard trong cửa sổ phối hợp ngắn, không để Web mới kín nhưng Directus nguồn còn công khai. Không sửa data/schema ngoài scope, không dùng Nuxt3 deploy.
S3 · DOT/ALERT & LIVE: verifier DOT phải kiểm anonymous không thấy dữ liệu, lấy số qua đường máy read-only có quyền, KHÔNG mượn token Owner; kiểm cả hai publishers. Kuma đo đúng negative status (401 hoặc 403 theo hiệu lực API), alert hoạt động. Verify Owner session thực200 SSR/SPA/refresh, anon401, nonowner403, empty config503, Directus /items/Web proxy deny 3 tables+7 rows/view_sql, 21 public+entity_species+/knowledge vẫn chạy, Guard POST và bản build đúng SHA.
S4 · ROLLBACK/ĐÓNG: nếu Web lỗi, ưu tiên giữ Reports fail-closed, không dùng artifact cũ công khai khi thiếu nginx narrow deny; ACL private phải giữ, backup dùng để phục hồi có kiểm soát. Phục hồi noncore, trả cờ. Một KQ PASS hoặc XONG CÓ GIỚI HẠN với bằng chứng + một NEXT_TRIGGER; không mở các RUN lẻ.
## Rào
Không tự mua license, đóng 166 collections, mở rộng 3 pivot API, sửa Graph, đụng Agent Data, khóa source VPS, phá Guard/role, hay sửa MONITOR PG-wide đã chết. Không biến rollback chức năng thành rollback bảo mật PASS. Owner GO=NO nghĩa là KHÔNG STARTED.
