# GHM — HAI AGENT VIẾT MÃ SONG SONG TRÊN GITHUB
RUN_ID: GHM-PARALLEL-CODE-20261031-16
TASK: work/github-management
EXECUTOR: Claude Code CLI trên Mac; làm quản lý một phiên, mở hai dev context/worktree độc lập bằng tính năng có sẵn. Codex không tham gia.
STATUS: HOST_FINAL; chỉ chạy sau GPT Host ký READY@last-touch PROMPT SHA trong COLLAB và Owner chuyển lệnh.
REVIEW_REUSED: Claude P157 — nhiều nhánh/PR, KST review; Owner 31/10 trực tiếp đổi ưu tiên về code song song.

## Đích: 2 kết quả mã thật, không phải 2 báo cáo
Hai agent chạy **đồng thời** trên hai repo hiện hữu, mỗi agent một nhánh Git riêng và một thay đổi có ích còn thiếu trong backlog hiện hữu; mở tối thiểu **2 PR có code/test thực**, CI gate xanh đúng HEAD. KST là phiên thứ ba không viết mã trong hai PR, review độc lập và merge tối thiểu 1 PR nếu không kích hoạt deploy. Nếu không có việc thật: báo thiếu việc, KHÔNG tạo commit giả. C4 tự giao ca đêm chưa phải điều kiện nghiệm thu lượt coding đầu tiên.

## Đầu vào GPT Host đã kiểm
- Repos: Huyen1974/agent-data-test main 6160f9ad6e5d16012dfe20bb59949abf5ffadad2 và Huyen1974/web-test main 8100ae6fee828c51be6e1ac3a4fd3a7d78b6e6e0; private/main protected/CI đã đạt. Agent kiểm SHA tươi lúc làm, không ghim cứng đã lỗi thời.
- CLI có thể dùng native Git worktree hoặc hai Claude Code sessions cách ly; KHÔNG tạo dịch vụ, gateway, account, runner, ứng dụng mới.
- Loại khỏi pilot: AD PR357/358 (HJW P493 NO_GO_RELEASE), Web PR686 (NDW P119 chưa release), Web PR327 (blob đã trùng main), PROD/DB/VPS/Graph mutations.
- Ưu tiên việc từ backlog thật: AD CONN-REPAIR PR353 (test flaky; chỉ còn việc sửa khi test chứng minh cần), Web GS-UC1 PR683 nếu Chủ task Graph đã cho phép chỉnh mã; không thì lấy bug/test nhỏ có issue/task cũ, xác nhận còn sai và file không chồng. Không cần mở task mới.

## Làm một lượt, không chia lệnh
1. S0: đọc AGENTS L1/L2, task GHM hiện hành, READY/STOP; kiểm hai repo/git auth và đường viết branch/PR. Không kiểm VPS-GHI, HJW release, Directus, RAM vì không deploy.
2. Mở **2 worktree/Claude dev sessions độc lập chạy song song**, mỗi bên từ main mới; nhánh trusted `dev/claude-code-ad/*`, `dev/claude-code-web/*`. Mỗi agent tự tìm bug/DoD thuộc task hiện hữu, sửa tối thiểu + test + commit + PR, không sửa main trực tiếp. Không tính PR cũ hoặc code trùng làm sản phẩm mới.
3. CI chạy đúng HEAD cho từng PR; fail do phần mình sửa thì mỗi dev tự khắc phục trong nhánh. Dừng sửa ngay khi qua mục tiêu; không lôi nợ cả hệ thống vào.
4. Phiên KST độc lập đọc diff + CI + test. KST chỉ merge PR đạt nếu xác minh `deploy-vps.yml` và các đường phát hành liên quan **không tự deploy khi merge**; nếu có khả năng deploy, giữ PR và báo, không bypass. Không PR đỏ, không admin merge. Không tự review chính mã vừa viết.
5. KQ chỉ **một báo cáo**, ghi cùng lượt vào GHM COLLAB+ROADMAP: 2 dev contexts có thực và khoảng chạy trùng nhau, PR/HEAD/CI, KST quyết, có merge hay lý do chưa; NEXT_TRIGGER. Mục tiêu coding chứng minh khi 2 agents thực cùng lúc + 2 PR thật GREEN + KST chấp nhận ≥1. C4/triển khai VPS ghi việc riêng, không chặn lượt này.

CẤM mở task/repo/account/workflow/runner/gateway mới, không deploy/SSH VPS, không đụng secrets, ACL, PG, Directus, DOT/Graph. Không mở lại RUN15, không dựng harness/CI/giấy tờ mới để chứng minh việc Git có sẵn. Nếu không thể chạy hai Claude sessions do quota/quyền, ghi đúng **một blocker thực**; không làm giả song song.
