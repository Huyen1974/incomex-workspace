# PROMPT — GHM C1B · KST CHỐT NGUỒN, MANUAL DEPLOY + ROLLBACK, CHUYỂN 3 AUDIT

RUN_ID: GHM-C1B-KST-BASELINE-MANUAL-CD-20261026-01
STATUS: READY_VIA_COLLAB — Claude Chat Reviewer P50 đã đánh giá và sửa 6 điểm; GPT Host chấp nhận, **chữ ký duyệt duy nhất là READY@full last-touch PROMPT SHA trong COLLAB của task theo DROOT58**. Không cần Reviewer ký. **Chưa STARTED**; chỉ sau Owner RUN đúng RUN_ID cho Claude Code CLI/KST, S0/Guard/VPS-GHI PASS mới được mutation. C1A scoped đã XONG, không dùng PROMPT P22 cũ.

EXECUTOR_SURFACE: **Claude Code CLI, kỹ sư trưởng (KST)**. Claude Chat chỉ là Reviewer; Codex C1A đã hoàn thành scoped.
WRITE_PATH: chỉ 2 kho PRIVATE Huyen1974/agent-data-test và Huyen1974/web-test (KST clone/refs/nhánh main); chỉ công cụ triển khai thủ công được bảo vệ trên VPS cho hai ứng dụng Agent Data, Nuxt; chỉ 3 nhóm audit active ghi P17; hồ sơ work/github-management. Không cho runner CI/PR cầm Docker/root/socket, admin token hoặc đường deploy. Thao tác VPS qua cờ VPS-GHI CAS và DOT/apply-v0 Đ30/31.

**Giấy phép thực thi:** Owner 25/10 đã cho phép phục hồi CI/CD đúng 2 repo qua DROOT56; **Owner RUN đúng lệnh C1B này** là sự chấp thuận giới hạn cho KST cập nhật main an toàn, build, thử deploy ứng viên và rollback, chỉ có **TỐI ĐA 4 lần restart ứng dụng cho diễn tập** (Agent Data 2, Nuxt 2), lần lượt và có health/rollback; **ngoại lệ đúng 1 lần khôi phục known-good khẩn cấp tại S4.3 chỉ khi rollback chưa khỏe, tuyệt đối không dùng để thử thêm candidate**. Không phải quyền mở auto-CD, mua Pro, thay DB/compose/nginx hoặc ảnh hưởng task khác. Chưa Owner RUN thì tuyệt đối không mutate.

**Mục tiêu XONG:** hai repo có main giữ đúng mã nguồn ứng viên đã xác minh từ VPS, không mất main cũ/history; candidate được build ngoài runtime, **deploy bằng một script local KST bấm tay**, health đạt, diễn tập rollback trở lại **runtime cũ** đạt; ba nhóm audit vốn chạy GitHub-hosted được chuyển sang runner VPS với nội dung kiểm tương đương. C1A đã XONG scoped: CI Agent Data run 40199854696 (6/6), Web run 40200962649 (16/16), INV25/cgroup no-swap, 2 volume 8/8. Không chạy lại C1A.

## S0 — ĐỌC ĐÚNG NGUỒN, CỔNG TRƯỚC MUTATION
1. Đọc AGENTS, root COLLAB (VPS-GHI, DROOT29–31/35/50/54/56–58), task COLLAB §0 + P17/P22/P35/P42/P48/P49, ROADMAP/KE-HOACH, bằng chứng private P48, S0/PRE Guard, tình trạng hai repo GitHub & hai runner. Kiểm Host/READY exact last-touch, Owner RUN, không STOP/COUNCIL_ALERT, không có writer khác cùng nguồn. Lấy VPS-GHI bằng CAS trước ghi, recheck trước mọi nhóm mutation; bận/thiếu quyền thì KQ DỪNG sạch, không giữ cờ chờ.
2. Cho mỗi repo lập bảng 3 cột **SOURCE_VPS_HEAD / GITHUB_MAIN_OLD / RUNTIME_RELEASE_ACTUAL** với SHA/digest/bằng chứng riêng. Agent Data image đang phục vụ có thể không phải VPS HEAD; Nuxt output cũng có thể khác Web source HEAD. **UNKNOWN phải ghi UNKNOWN**, không được đoán mã đang chạy = source cây VPS. Chụp app image/output cũ, mounts, runtime config, health, count/contract và disk/memory/swap baseline. Không đọc/in secrets.
3. Kiểm workflow cũ (SSH/rsync/SQL, 15 BỎ disabled) **không thể tự deploy khi main đổi**; ba nhóm audit P17 đang active. Kiểm toàn account budget Actions $0 + Stop. Trần build phù hợp tải VPS; chỉ 1 việc nặng. GLOBAL_GUARD của C1A vẫn PARTIAL 23/25, thống kê 24h phân loại mới chưa đủ: giữ nợ/chủ, không tự làm xanh; bất kỳ RED mới do C1B phải DỪNG/rollback.

## S1 — BASELINE KST: BẢO TOÀN VPS, GITHUB MAIN CŨ
1. Dùng **clone KST biệt lập**, ngoài cây mã/runtime VPS và ngoài workspace runner; VPS vẫn SSOT cho source cho tới khi baseline mới được chứng minh. Không pull/reset/checkout vào cây source đang phục vụ, không đổi origin sentinel DROOT56. Phần sửa chưa commit trên VPS (kể cả submodule pointer Web): quét bí mật rồi commit **một** commit «baseline VPS» trong clone, ghi danh sách tệp vào bằng chứng — không cần truy chủ từng diff (VPS là SSOT); không ghi trực tiếp vào cây sống.
2. Đối chiếu main cũ từ GitHub, tạo ref/tag archive bất biến có readback, hash và đường khôi phục; xác minh source tree ứng viên VPS đúng, đã quét secret/license/đường migration và workflow. Report Directus lịch sử không được đem một credential còn hiệu lực lên main; không in giá trị.
3. Tạo commit ứng viên có main cũ làm tổ tiên, cây mã ứng viên byte/tree khớp source VPS đã chọn (ngoại lệ được kiểm riêng cho workflow/archive). Cách duy nhất (P22/R3): từ commit baseline VPS chạy `git merge -s ours <main cũ>` ⇒ cây kết quả = đúng cây VPS, main cũ là tổ tiên, main tiến thẳng; **chứng minh `git diff <baseline VPS> <main mới>` rỗng (trừ archive/workflow đã kê) trước push**. KHÔNG merge 3 chiều trộn mã cũ vào; tuyệt đối không force-push, rewrite history, reset main hay mất commit của người khác.

## S2 — KST PROMOTE MAIN HAI REPO AN TOÀN
1. Trước push đối chiếu lại remote main HEAD (CAS/expected SHA), ba audit và mọi trigger: **deploy cũ vẫn disabled**, không có workflow main tự chạy quyền SSH/host. Nếu main thay đổi bởi actor khác thì dừng push của repo đó, reconcile clone riêng; không giữ VPS-GHI vô ích.
2. Push main chỉ khi owner authorization đúng C1B, qua đúng đường/thẻ ghi sẵn có của job sao lưu `git-push-gh-daily-v2.sh` (không đổi origin sentinel, không dùng token admin/runner); trước push kiểm thẻ có quyền cập nhật tệp workflow (classic: scope `workflow`; fine-grained: Workflows write) — thiếu ⇒ DỪNG đúng 1 blocker, không tự đổi thẻ; tag main cũ giữ nguyên, new main fast-forward ancestry. Không đẩy trực tiếp các file nhạy cảm hoặc migration SQL chưa duyệt. 15 workflow BỎ chỉ chuyển archive nếu cần để ngăn kích hoạt khi promotion và đã đối chiếu disabled; không thay ba audit khi chưa có test tương đương.
3. Ghi cặp MAIN_NEW_SOURCE_SHA vs RUNTIME_OLD_DIGEST khác nhau nếu có; không claim hai repo "đang chạy main" chỉ vì main source đã cập nhật. Giữ checkpoint main an toàn nếu deploy sau đó fail, không đập ngược main.

## S3 — TẠO CỔNG TRIỂN KHAI THỦ CÔNG & BUILD THỬ
1. Dùng DOT/script-wrapper root/KST **đã quản lý hoặc nâng đúng cổng hiện có**: --help, --dry-run, deploy exact approved main SHA, health, --rollback, known-good; không cấp docker group hoặc mount host cho runner CI. Chỉ KST/host gọi thủ công. Script/clone/release config ghi vào Config Guard/code-ledger/Kuma và self-test/rollback Điều 30/31 cùng lượt.
2. Build image Agent Data và Nuxt .output **ngoài runtime live** theo lockfile/version xác minh, trần tài nguyên nhỏ để VPS không thrash. Lưu image digest và output/config snapshot đang chạy làm known-good, bảo đảm restore được chính xác không cần pull mạng. Nếu SOURCE_HEAD và RUNTIME_RELEASE_ACTUAL khác, không tự kéo source GitHub vào cây đang chạy; candidate vẫn phải canary/contract PASS, nếu rollback không xác minh được thì dừng trước restart.
3. Không copy compose/nginx từ GitHub, không SQL/DB migration/restore, không rsync DOT, không restart Directus/PG/Qdrant/nginx hay bất kỳ dịch vụ khác. Không bật deploy tự động khi main đổi.

## S4 — THỬ DEPLOY THẬT TỪNG APP VÀ LÙI VỀ BẢN CŨ
1. **Agent Data:** trước restart so cấu hình compose của riêng dịch vụ agent-data với container đang chạy (config-hash); khác ⇒ KHÔNG restart Agent Data (lùi không về được đúng bản cũ), ghi blocker riêng repo này, Web vẫn làm. Bằng script KST chuyển riêng từ image old digest (đã gắn tag known-good, không bị prune) sang candidate image SHA, tạo lại CHỈ agent-data (`docker compose up -d --no-deps --no-build agent-data`) (1); kiểm /info, /api/health, số tài liệu và contract so với PRE; **rollback ngay về old digest/config**, restart cùng dịch vụ (1), health/contract phải như PRE. Lỗi thì auto rollback; nếu app cũ chưa khỏe thì FAIL_WITH_ROLLBACK, không lấy xanh giả.
2. **Nuxt:** build output candidate riêng, snapshot .output old có checksum; switch atomically, restart riêng nuxt (1), smoke /knowledge và nội dung/route chính; rollback output cũ, restart nuxt (1), xác nhận health & checksum. Sau mỗi lần restart nuxt/agent-data được `nginx -s reload` (không đổi cấu hình, không tính là restart — y quy trình cũ đã chạy, để nginx nhận IP mới của container); không đổi cấu hình nginx.
3. Tổng **tối đa 4 restart ứng dụng**, không restart VPS; nếu bước lùi cần khác giới hạn hoặc thiếu dữ liệu bảo vệ, STOP trước deploy, báo Host. Nếu sau lùi app cũ chưa khoẻ: được thêm **1** lần khôi phục về known-good (ngoài 4), rồi DỪNG và báo Owner ngay. Kết thúc diễn tập **runtime = bản old khỏe**, dù main mới chứa mã nguồn ứng viên; ghi rõ release SHA/digest và không báo "production đã lên main" khi thực tế vừa rollback.

## S5 — CHUYỂN 3 NHÓM AUDIT HOSTED SANG RUNNER VPS
1. Lấy **đúng danh mục P17** và trạng thái GitHub hiện tại: 1 nhóm Agent Data + 2 nhóm Web; không tự đoán tên, không kích hoạt workflow Dependabot/bị cấm, không bật lại 15 workflow thừa. Với từng nhóm, branch thử chạy cùng test/scripts/triggers trên runner CI riêng của repo, permissions contents:read, không secrets/DB/host root. Persistent runner chỉ nhận code trusted, không PR không tin cậy.
2. Chỉ thay runs-on sang self-hosted sau khi kiểm log SHA, test semantics tương đương và runner GitHub thực nhận job; nếu cần Docker/DB secret/admin, không mở quyền để ép xanh. Nợ phải nêu đúng workflow, nguyên nhân, đường tiếp, giữ workflow cũ an toàn. Ghi số phút hosted giảm theo dữ liệu GitHub; **không coi billable={} vài run là tổng account $0**.
3. Khi 3 nhóm có run kiểm thật success, promote workflow cùng main KST duyệt, xác minh 3 nhóm còn active và tất cả vẫn được giám sát; không bật auto deploy trước C2.

## S6 — POST, BÀN GIAO C3
- KQ XONG C1B chỉ khi **cả 2 repo** có (1) main candidate đúng VPS source/tree, old main tag/readback, không force; (2) build ngoài runtime PASS; (3) manual deploy candidate, health PASS, rollback về old runtime PASS; (4) ba nhóm audit chuyển sang VPS không giảm test; (5) Điều 30/31 + receipt và VPS-GHI trả, app cũ khỏe. Không cần nâng permanent runtime lên SHA mới trong C1B; khi C3 KST muốn deploy phải bấm tay.
- Nếu bước nào FAIL, báo bảng PASS/DỪNG từng repo + NEXT_TRIGGER; giữ checkpoint an toàn, không rollback hủy tiến độ repo khác, không thêm vòng bàn nếu đã có proof. C1B_SCOPED=PASS|FAIL; GLOBAL_GUARD=PASS|PARTIAL riêng, không gắn cả hai.
- Báo STARTED theo bước, KQ + Bảng/ROADMAP/README cùng commit, private evidence có hash, không in secret. Trả VPS-GHI, dọn sampler/build tạm, giữ rollback image/output đã cần. Không tự C3/C2/C4.
- Bàn giao C3: từ sau C1B mọi sửa mã đi nhánh → PR → KST; sửa thẳng trên thư mục mã VPS là trái luật — KST phát hiện sửa mới trên VPS thì đưa lên main trước khi deploy.

STEP_WALK_V1:
| Bước | Executor | Cổng | Bằng chứng | Fail/next |
| S0 | Claude Code CLI | READY/Owner RUN/VPS-GHI | source/main/runtime/Guard PRE | DỪNG trước mutation |
| S1 | KST | S0 PASS | clone, old main tag, source tree, scan | DỪNG giữ source cũ |
| S2 | KST | S1 PASS | main ancestry+tree SHA/old tag | DỪNG không force |
| S3 | KST | S2 PASS | build candidate/dry-run/rollback artifact | DỪNG nếu chưa an toàn |
| S4 | KST | S3 PASS | 2 app: deploy+rollback/health thật | auto rollback, KQ nếu fail |
| S5 | KST | S4 PASS | 3 audit runner VPS/log+URL/test | giữ audit an toàn, nợ đúng |
| S6 | KST | S5 PASS | POST Đ30/31/receipt/KQ/cờ trả | Host nghiệm thu |

CẤM: GitHub Actions deploy/SSH/rsync như P22 cũ; CI runner Docker socket/root/secret; deploy do push main trước C2; force-push/history rewrite, DB SQL/compose/nginx copy, reboot VPS, vượt 4 lần restart diễn tập hoặc dùng ngoại lệ 1 lần ngoài mục đích khôi phục khẩn cấp known-good ở S4.3, mua Pro/khóa main/auto-CD, tự chạy C3.
