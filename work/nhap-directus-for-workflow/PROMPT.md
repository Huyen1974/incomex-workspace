# NDW · P0 REPORTS — RELEASE READINESS ONE-PASS
RUN_ID: NDW-P0-RELEASE-READINESS-20261031-03
TASK: work/nhap-directus-for-workflow
EXECUTOR: Claude Code CLI (KHÔNG dùng Codex; Owner quyết định 31/10)
STATUS: DRAFT — chỉ thực thi sau Host ký READY full commit SHA và Owner chuyển lệnh.
REVIEW_REUSED: P114 (Claude KST review mã Codex cùng phạm vi), không mở lại vòng phản biện chỉ vì đổi executor.

## Mục tiêu
Hoàn tất trọn một đợt chuẩn bị RELEASE cho Reports P0 bằng chứng thật; hoặc lập đúng MỘT quyết định Owner/DOT để phá blocker không thể tự xử lý. Tránh chia RUN riêng cho auth/ACL/pivot/monitor. Không thực hiện mutation production trong lệnh này.

## Input đã xác minh (DROOT60)
- Web PR #686 OPEN, HEAD a353b64e0252e667ffd5a3ea0f89119ff86aaa38, base/main 8100ae6fee828c51be6e1ac3a4fd3a7d78b6e6e0, CI 41143018991 completed/success đúng HEAD. Required gate chạy 19/19 auth PASS; P114 Claude CLI review độc lập, code-ready. Chỉ replay tests/build nếu code mới thay hoặc chứng cứ mâu thuẫn.
- Nuxt4.5.2 build và Nitro/Chromium fixture P114 PASS. Owner 200 chỉ fixture; full-project Vue typecheck có lỗi plugin, KHÔNG claim PASS.
- External Directus /items, generic Web /api/directus proxy và 3 /api/registries-pivot có read 200 theo P114; PUBLIC_POLICY và NONOWNER_ACL chưa chứng minh.
- Owner immutable user ID + phiên active chưa xác minh. Verifier lịch sử có login/logout/smoke POST/DELETE: **CẤM gọi như công cụ chỉ đọc**.
- Runtime PG-driven measurement_registry thực sự ảnh hưởng monitor; source/expectation cụ thể chưa kiểm. Đó là mục tiêu đo, không là điều kiện bắt Agent phải đoán trước. Nếu không có đường DOT read-only an toàn, KHÔNG gọi PG/Directus trực tiếp.
- Quyền phát hành: N/A. Owner chưa GO merge/deploy/ACL/secret/VPS, vì vậy RUN chỉ thực hiện readonly/code PR và lập kế hoạch.

## STEP_WALK — Một RUN, làm hết nhánh độc lập
| Bước | Claude CLI làm gì | Bằng chứng/đầu ra | Nếu có blocker |
|---|---|---|---|
| S0 | Đọc AGENTS, NDW §0/P114/P115, GHM P153/P154, PR686/CI; kiểm current SHA/main, Council alert/STOP/0 RUN active; ghi STARTED | HEAD/base/CI/test chuẩn, lỗi nào thật | Nếu main moved thì reconcile; chỉ dừng nếu quyền/STOP thật |
| S1 | Tận dụng handoff DOT P114, xác định đường **chỉ đọc thật** cho binding Owner/phiên active, ACL Directus anonymous/nonOwner/Owner đối với table_registry, 7 Reports targets, relation/fields, external items, generic proxy và 3 pivot. Kiểm định nghĩa fn_registries_pivot_node_substrate và view_sql được gắn ngoài Reports | Bảng từng nguồn/route: PUBLIC đúng nghiệp vụ hay OWNER_ONLY hay UNKNOWN, ACL hiệu lực, evidence nguồn/thời điểm; KHÔNG chép ID/token/rows | Nếu chưa có quyền DOT readonly, KHÔNG dùng verifier có ghi; ghi đúng MỘT đề nghị Owner/DOT tối thiểu, rồi tiếp S2/S3 |
| S2 | Đọc mã & nguồn sẵn: PG-driven measurement_registry target_query, runner integrity, contract Web, monitor health đang áp dụng; xác định Web mới+contract/runner đồng bộ ra sao; kiểm phát hiện lỗi không báo issue | Bảng monitor effective + candidate fix nếu có lỗi thật. Không bật lại workflow/cron, không sửa PG/VPS | Thiếu PG quyền ⇒ ghi UNKNOWN đúng nơi, vẫn hoàn tất code/rollback plan |
| S3 | Nếu S1/S2 phát hiện lỗi code do PR686 gây ra, vá tối thiểu trên **PR686 hiện hữu**, chạy CI đúng HEAD. Không sửa hoặc chạy lại test không cần thiết. Nếu Claude là tác giả sửa delta mới, xin GPT Host review độc lập delta đó, KHÔNG tự KST_ACCEPT phần mình sửa | Code SHA mới hoặc chứng nhận giữ a353b64; test/gate và phần cần Host xem | Repo/code scope vượt quyền ⇒ không sửa, ghi change proposal hẹp |
| S4 | Chuẩn bị một gói merge/release đúng SHA, xác minh điều kiện Owner session thật/ACL/public, Web+contract+integrity runner, SPA/refresh/SSR, config server-private, health, rollback artifact+config. Bản cũ có thể tái mở lỗ hổng: phải nêu giải pháp fail-closed, không lấy rollback chức năng thay bảo mật | CODE_READY, IDENTITY_VERIFIED, ACL_VERIFIED, MONITOR_READY, RELEASE_READY/RELEASE_HOLD; duy nhất NEXT_TRIGGER | Chờ Owner GO không giữ RUN, terminal hoặc VPS-GHI |

## Ranh giới bắt buộc
- Cấm: merge PR686, deploy/restart VPS, thay secrets/ACL/roles, ghi PG/Directus/Guard/measurement_registry, khóa Web VPS, mở repo/task/RUN mới, chạy verifier có login/logout/smoke mutation, công bố ID/token/secret.
- Không mặc định khóa /knowledge hoặc catalog công khai; cần phân loại dữ liệu chính xác. Missing evidence = UNKNOWN/RELEASE_HOLD, không giả secure.
- Claude CLI là executor thay Codex. Không tự tính review của chính mình nếu có commit mới; Host/GPT rà delta theo GitHub, không mở thêm Council vòng nếu không cần.
- F2/R4 code branch/PR của GitHub không chờ P0 production; T3 VPS write-lock vẫn HOÃN theo Owner.

## KQ đầu cuối
Một báo cáo NDW COLLAB cập nhật Bảng, có receipt vào GHM chỉ dẫn chiếu. Không dừng giữa chừng chỉ vì một nguồn chưa đọc được; tiếp tục tất cả phần độc lập. Cuối lượt KQ XONG-CÓ-GIỚI-HẠN hoặc DỪNG đúng hard-safety, ghi một NEXT_TRIGGER và nhả mọi cờ. Nếu RELEASE_READY chưa đủ, nói đúng còn quyết định nào và một đường xử lý nhỏ nhất, không ra nhiều prompt khảo sát kế tiếp.

Lịch sử PROMPT TS4 đã KQ P104; phiên bản cũ được Git giữ ở commit 9ac3923308eff225a9e4e8b92a36046065338b04, CẤM chạy lại TS4.
