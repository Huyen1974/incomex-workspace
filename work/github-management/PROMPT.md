# PROMPT — GHM P1-A · Khởi tạo môi trường mã song song
RUN_ID: GHM-P1A-GITHUB-SANDBOX-20261023-01
STATUS: DRAFT_NOT_READY. Chỉ chạy khi Claude Reviewer ACCEPT SHA cuối chạm PROMPT, GPT Host READY@SHA đúng trong COLLAB, và Owner giao RUN.
Executor_Surface: Codex CLI/Desktop Mac. Write_Path: GitHub qua gh CLI/GitHub API được phép, Incomex workspace_* root=workspace ghi STARTED/KQ. Không shell/deploy/sửa secret trên VPS production.

ĐỌC AGENTS.md root → work/github-management/COLLAB.md §0/Bảng/P1/P2 → README.md → PROMPT.md. Kiểm READY/Owner RUN, quyền/credential thật, ghi STARTED trước mutation theo A6/DROOT30/31. Nếu thiếu chặn thì KQ DỪNG sạch.

S0 — KIỂM ĐẦU VÀO READ-ONLY:
- Kiểm repo Huyen1974/agent-parallel-pilot chưa tồn tại; gh CLI có quyền tạo repo, quản lý Actions/ruleset; không hiển thị secret; ba agent dự kiến Codex, Hermes, Claude có bề mặt riêng hay chưa. Nếu không có quyền thì DỪNG, không tạo đường vòng.
- Không đọc, xuất, sao chép bất kỳ phần production Agent Data/VPS nào vào public.

S1 — DỰNG REPO MỚI CÓ GIÁ TRỊ:
- Tạo duy nhất một repo mới PUBLIC Huyen1974/agent-parallel-pilot, lịch sử Git mới; chưa chạm repo cũ. Tắt GitHub Actions ở settings TRƯỚC khi push; không tạo workflow.
- Commit scaffold Python stdlib unittest, README vai trò/DoD, .gitignore; ba thư mục riêng task_contract/, pr_scope/, pr_report/ và tests tương ứng. Chỉ dữ liệu giả, không có host/IP/địa chỉ/đường production, secret hoặc cấu hình nội bộ. Ghi commit SHA, URL repo.

S2 — CỔNG CƯỠNG CHẾ:
- Ruleset áp dụng CHỈ default branch/main (~DEFAULT_BRANCH hoặc match main chính xác), chống dev update/delete/force push; tuyệt đối không ~ALL. Chỉ actor Chief đủ quyền vào main; không phát key cho worker. Nếu bypass loại DeployKey thì đếm các write deploy key và chứng minh worker không thể đọc key KST.
- Thử trên sandbox và ghi bằng chứng: dev push main bị chặn, dev tạo/push branch rồi mở PR được, dev sửa ruleset bị chặn, dev xóa/force-push main bị chặn, Chief dùng đường ký duyệt thật push main được, Actions không chạy.
- Chưa có identity độc lập để đo một test: ghi UNKNOWN, KHÔNG giả PASS; hardlock FAIL không được quảng cáo đủ an toàn production nhưng không cấm báo chứng cứ về coding song song.

S3 — BA VIỆC THẬT, CÓ TEST:
- GHMP-01 | task_contract/ + tests/task_contract/: hàm kiểm phiếu JSON có task_id, goal, done_when, worker, allowed_paths, deadline; báo lỗi rõ. Test python3 -m unittest discover -s tests/task_contract -v. Worker: Codex.
- GHMP-02 | pr_scope/ + tests/pr_scope/: nhận changed_paths + allowlist, từ chối path vượt phạm vi và dạng ../; test python3 -m unittest discover -s tests/pr_scope -v. Worker: Hermes.
- GHMP-03 | pr_report/ + tests/pr_report/: đọc danh sách kết quả PR từ JSON giả và xuất bảng Markdown buổi sáng, mỗi PR một dòng; test python3 -m unittest discover -s tests/pr_report -v. Worker: Claude cloud.
- Mỗi việc thành một GitHub Issue với sáu ô Mã; mục tiêu/DoD+test; khu tệp được sửa; phụ thuộc; ghế; giới hạn/điều cấm. Mỗi ghế clone/worktree riêng, nhánh dev/<seat>/<task-id>, PR liên kết Issue; không ai được sửa cùng root config. Nếu Claude đồng thời giữ vai Chief, phải có reviewer khác hãng độc lập cho PR Claude.
- Nếu Codex có đường gọi thật thì giao và thu receipt. Nếu không, báo Owner BA lệnh ngắn có link Issue để Owner chuyển cho các ghế; không giả lập việc đã giao. Không giữ RUN chờ họ hoàn thành.

S4 — KẾT QUẢ:
- Kiểm repo, SHA, Actions OFF, ba Issue, quyền main theo từng test, 1 nhánh dev tạo được; biên nhận URL và test. Ghi vào work/github-management/COLLAB.md P3 + Bảng + KQ@GHM-P1A-GITHUB-SANDBOX-20261023-01 XONG|DỪNG. XONG chỉ là bootstrap, KHÔNG nhận vơ P1-B và không tự merge/deploy.
- Bất kỳ blocker: DỪNG rõ chỗ nào, NEXT_TRIGGER, nhả busy, không đổi mục tiêu, không mở project con.

STEP_WALK_V1 (giới hạn ngân sách từng bước, không giữ task chờ):
| Bước | Ai/trigger | SLA | Evidence | Lỗi ai biết | Tiếp |
|---|---|---|---|---|---|
| S0 | Codex sau Owner RUN | 15 phút | repo, quyền/identity | KQ DỪNG báo Host | S1 |
| S1 | Codex/S0 PASS | 35 phút | GitHub repo, SHA, Actions OFF | DỪNG/Host | S2 |
| S2 | Codex/S1 PASS | 30 phút | ruleset chỉ main + tests quyền | Hardlock FAIL riêng, Host nhận | S3 nếu nhánh dev hoạt động |
| S3 | Codex/S2 branch PASS | 25 phút | 3 Issues và tin giao/receipts | DỪNG/Host | S4 |
| S4 | Codex/S3 xong | 15 phút | KQ, Bảng, URL/SHA | Host/Owner | END |

CẤM công khai code thực từ VPS, đụng prod, chạy Actions, mua Pro, tạo lịch/daemon, tự mở RUN mới; không giả danh agent khác và không báo hoàn thành đêm khi chưa thử.
