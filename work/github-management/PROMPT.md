# PROMPT — GHM C1A · CODEX TIẾP TỤC RUNNER/CI, TÁCH ĐÚNG CỔNG WEB
RUN_ID: GHM-C1A-RESUME-20261025-02
STATUS: DRAFT_NOT_READY. Codex P27 đã KQ DỪNG RUN trước; đây là lượt phục hồi mới. Claude ký ACCEPT đúng last-touch SHA sau khi rà delta, GPT Host READY cùng SHA, Owner RUN mới được STARTED. Thao tác/giới hạn runner của C1A P24 giữ nguyên.

**EXECUTOR: CODEX CLI/DESKTOP**, chạy từ Mac qua quyền GitHub + đường SSH/VPS đã được Owner cấp. Codex tự triển khai toàn bộ C1A, Claude chỉ Reviewer/KST cho các thao tác ghi main ở C1B/C2. Nếu Codex thiếu quyền ghi VPS hợp lệ ⇒ KQ DỪNG đúng blocker; không tự chuyển nhiệm vụ sang Claude.

**MỤC TIÊU NGHIỆM THU:** đăng ký self-hosted runner GitHub trên VPS cho cả **hai repo PRIVATE** `Huyen1974/agent-data-test` và `Huyen1974/web-test`, chạy tối thiểu 1 workflow **kiểm thử thực có giá trị** mỗi repo trên runner VPS, GitHub trả GREEN và có URL run + SHA. **Không coi runner ONLINE là XONG.** C1A là đường CI phát triển thực tế; C1B tiếp ngay sau để thử CD dev/rollback, C2 mới mở auto-deploy sau khóa main.

**GIỚI HẠN OWNER GO:** Owner cho phép **cài runner/thử CI trên VPS giai đoạn phát triển** theo DROOT56, không mặc nhiên cho phép push baseline sai vào main, xóa/sửa cây mã đang phục vụ, khôi phục SSH secret hoặc tự restart live Agent Data/Nuxt. Không coi các container dịch vụ đang chạy là vô giá trị chỉ vì chưa production.

ENTRY: root AGENTS.md/Đ30–31/DROOT56 → root COLLAB PROOT08/09 & VPS-GHI → work/github-management COLLAB §0/Bảng/P12/P17/P22/P23/P24/P25/P26/P27/P28 → ROADMAP/PROMPT. PRE/POST đều phải có evidence. Cờ VPS-GHI thuộc phạm vi ghi hệ thống; đọc trạng thái không giữ cờ. Chỉ ghi STARTED sau Owner RUN.

## S0 — CỔNG VÀ TÀI NGUYÊN
1. Đọc lại bằng chứng R0/P12/P17/P22, **không làm lại khảo sát 33 workflows**. GitHub Actions Account budget $0 + Stop còn ON, 15 workflow thừa vẫn disabled, ba kiểm nghiệp vụ còn nguyên. Kiểm mã VPS/backup daily HEAD, GitHub main và bản code/runtime, ghi UNKNOWN nếu lệch (nhất là Web submodule). KHÔNG sửa `origin` sentinel DROOT56 hay Config Guard.
2. Kiểm VPS-GHI, các RUN đang ghi Docker/2 code repo, container health, swap gần đầy, `docker info` hỗ trợ giới hạn memory/CPU qua cgroup. Nếu không đảm bảo khóa/trần tài nguyên hay Codex thiếu SSH/VPS quyền ghi đã duyệt thì DỪNG; không chiếm khóa để chờ.
3. Ở nhánh thử GitHub, kiểm YAML deploy cũ còn disabled. Không kích hoạt `workflow_dispatch` deploy để “thử kết nối”.
4. Đầu vào P27: dùng đúng ref/tên tệp/hash ở báo cáo PRIVATE để xác định report login Web có thuộc Git tree mà runner checkout không; **không đọc/in/gọi** token. Trạng thái chỉ MOCK_CONFIRMED (fixture có bằng chứng), REVOKED_CONFIRMED (quản trị/provider xác nhận vô hiệu), hoặc SUSPECTED_UNRESOLVED. HTTP200/64 ký tự/tệp cũ không chứng minh vô hiệu. Mặc định Web SOURCE_HOLD; Agent Data và hạ tầng runner KHÔNG HOLD theo.
5. Trước in tool output phải che tên khóa access_token, refresh_token, id_token, authorization, cookie, client_secret và biến thể; thử đúng bộ lọc bằng dữ liệu GIẢ tự tạo. Không đăng bản token lên workspace public.

## S1 — CÀI 2 RUNNER CI TÁCH BIỆT, GIỚI HẠN QUYỀN
1. Cài binary `actions/runner` chính thức, pin release version + kiểm SHA256 chính hãng. Nếu đóng vào container thì ảnh do Codex tạo từ binary hãng; đừng ghi là official image nếu chưa xác minh.
- Thứ tự bắt buộc: cài runner CI Agent Data trước và chạy Agent Data S2; có thể chuẩn bị runner Web nhưng để OFFLINE/không nhận job cho tới khi source Web SAFE. Hai đăng ký GitHub chỉ dùng registration token ngắn hạn, không PAT admin thường trú VPS; tổng trần CI vẫn 2 CPU/3 GiB và chỉ 1 build nặng tại một thời điểm.
2. **Một registration runner/repo** (tài khoản GitHub cá nhân). Codex lấy registration token *ngắn hạn* bằng phiên GitHub admin trên Mac/Owner UI; đưa một lần qua kết nối mã hóa; KHÔNG chuyển PAT admin/backup vào VPS, không in token vào chat, log, script, systemd hoặc repo. Credentials runner lưu ở volume riêng chỉ runner đọc được.
3. Runner thực thi code **không phải root, không ở nhóm docker, không dùng `docker.sock`, không `--privileged`**, không mount host root hay `/opt/incomex`/PG/GSM/.env/SSH/backup, không host-network/compose network; volume chỉ config runner và workspace CI riêng. Workflow `permissions: contents: read`, checkout không lưu credentials. Repo vẫn PRIVATE.
4. Runner mỗi repo có label riêng; **tổng CPU CI ≤2 vCPU, RAM CI ≤3 GiB**, tối đa 1 build nặng mỗi lúc. Codex phải chứng minh giới hạn bằng container/cgroup thực; nếu 2 runner có thể chạy song song vượt trần thì tạm bật lần lượt 1 runner để test, không để tài nguyên VPS bị tranh. Mất tài nguyên ⇒ dừng CI trước, không dừng dịch vụ đang dùng. Không dùng job hook thay thế giới hạn quyền Docker/root.
5. Có biên nhận 2 runner online từ GitHub UI/API; runner persistent + dọn workspace sau job chỉ được báo PILOT có giới hạn, **không** báo ephemeral/isolated tuyệt đối.

## S2 — CI THẬT TRÊN 2 NHÁNH THỬ, KHÔNG GHI MAIN
1. **Chạy Agent Data độc lập trước:** tạo nhánh `dev/codex/ghm-c1a-resume-ad` từ vps-daily Agent Data đã đối chiếu HEAD VPS và kiểm source an toàn trên GitHub; không đọc/ghi cây VPS phục vụ. Khi Agent Data có CI thật GREEN thì ghi riêng milestone PASS và GIỮ lại runner/kết quả. Với Web: chỉ tạo `dev/codex/ghm-c1a-resume-web` và checkout khi Web source được chứng minh MOCK_CONFIRMED hoặc REVOKED_CONFIRMED và tree được thay dữ liệu test bằng fixture giả, không còn token hoạt động. Nếu còn nghi Web thì DỪNG **riêng Web**, giữ runner Web OFFLINE, không checkout/chạy workflow; không dừng hoặc rollback Agent Data đã đạt. Không tự xoay token, không rewrite history/force-push để vượt cổng.
2. Tạo `.github/workflows/ghm-ci-vps-probe.yml` trên nhánh thử, `on: push` CHỈ nhánh này, `runs-on` đúng CI runner label; không dùng `workflow_dispatch` (đòi file trên default branch), không có bước deploy, không đụng các YAML cũ trên main.
3. Chạy thật: Agent Data pytest nhóm test unit không cần DB thật; Web dùng pnpm/node theo `package.json`, install lockfile và một lệnh lint/typecheck/test có thật. Không bịa test; phải có test thực hữu ích trên cả hai repo chứ không chỉ echo version. Nếu phụ thuộc DB/secret hoặc tài nguyên không đủ thì ghi FAILED/UNKNOWN, không “sửa” bằng cách gắn DB/secret thật.
4. Ghi URL GitHub run, SHA nguồn, runner label/ID, kết quả các bước, peak RAM/CPU, phút GitHub-hosted cho **probe**. Không tuyên bố tổng tài khoản 0 hosted-minutes vì ba audit cũ vẫn có thể chạy.

## S3 — POST, DỌN VÀ BÀN GIAO
- Kiểm 2 repo: runner online, probe workflow đã chạy từ GitHub trên VPS và test có kết quả, GitHub Actions budget $0+Stop còn, ba audit nguyên vẹn, 15 workflows thừa vẫn disabled; Git top-level VPS/Guard và container ứng dụng không bị thay. Tránh đẩy đường dẫn/actor/secret nhạy cảm lên task PUBLIC; bằng chứng chi tiết cất vùng root-only của việc.
- **Điều 30/31 cùng lượt (Owner):** runner tự chạy lại khi VPS khởi động lại; đăng ký container/dịch vụ runner + cấu hình vào bảo vệ hiện có (code-ledger/Config Guard), Kuma theo dõi runner online; lưu script cài/gỡ runner vào repo + bảng công cụ để lần sau dùng lại.
- **KQ XONG khi 2/2 repo có run GitHub chạy THẬT trên runner VPS, cài phụ thuộc xong và ít nhất 1 lệnh test/lint/typecheck có thật chạy GREEN; không thay đổi runtime mã/dịch vụ cũ.** Lỗi nằm ở MÃ đang thử (test cũ đỏ) mà runner/môi trường chạy đúng ⇒ chọn nhóm test đang xanh để làm GREEN, ghi test đỏ thành nợ mã — KHÔNG báo DỪNG vì mã cũ. Nếu Web đang SOURCE_HOLD, báo `AgentData=PASS/FAIL; Web=SOURCE_HOLD; tổng C1A=CHƯA ĐẠT` với một NEXT_TRIGGER Owner/provider revoke/rotate credential đúng hệ thống; không bỏ phần Agent Data PASS. Nếu runner/môi trường của một repo còn lỗi thì KQ DỪNG/PARTIAL đúng repo, nêu blocker và đường rollback riêng runner mới. Trả cờ/không giữ phiên chờ.
- Kết quả đã PASS của từng repo được giữ nguyên giữa các lượt, không lặp thao tác/hồi phục nếu không có lỗi mới. Khi XONG: giữ hai CI runner cô lập, ghi bước kế `GHM_C1B_BASELINE_DEV_CD`. **C1B** Codex chuẩn bị code baseline và dev CD thử local trên vùng riêng, Chief quyết nhập main, diễn tập rollback; **C2** Owner mua Pro nếu private + khóa main/Chief-only rồi mới cho auto-deploy khi main đổi. C1A KHÔNG tự RUN C1B/C2.

STEP_WALK_V1 (bước · executor · hạn tham chiếu · chứng cứ · lỗi/ai nhận · bước kế):
| S0 | Codex/Owner RUN | ≤15 phút | cờ/quyền/source metadata Web + redactor fixture | thiếu quyền hạ tầng: DỪNG Host | S1 |
| S1 | Codex/S0 hạ tầng PASS | ≤45 phút | runner CI cách ly, cgroup, Guard/Kuma | lỗi hạ tầng: KQ Host | S2 |
| S2 | Codex/Runner Agent Data | ≤25 phút | CI run URL/SHA/test GREEN Agent Data | nợ mã riêng | S3 |
| S3 | Codex/Web source gate | ≤25 phút | Web CI run hoặc SOURCE_HOLD có bằng chứng | Owner/provider revoke khi cần | END/KQ |

CẤM: sử dụng runner nhận job PR có quyền root/docker.sock, đăng ký deploy runner đặc quyền trên VPS, phục hồi secret SSH GitHub→VPS cũ, bật workflow deploy cũ, force-push/merge main, sửa/đổi `origin`, ghép mã cũ vào mã sống, `rsync --delete`, SQL migration, copy compose/nginx, restart container ứng dụng/DB, mua Pro. Mọi đổi khác ngoài runner + nhánh/probe/STARTED/KQ ⇒ DỪNG và báo Host.
