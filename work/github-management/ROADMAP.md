# ROADMAP — github-management V0.2 · 24/10/2026
**Trạng thái: REVIEW_REQUESTED / CHƯA ĐỒNG THUẬN / KHÔNG RUN.**  
Kế hoạch thực hiện chi tiết và đề bài Claude: [KE-HOACH.md](KE-HOACH.md). Phải có Claude phản biện, GPT đồng thuận, Owner duyệt trước khi chạy.
Ưu tiên 1: nhân không gian làm việc để 3–5 agent viết mã song song trên hai repo hiện hữu, Claude Code CLI làm kỹ sư trưởng review/merge; sau đó mới tự động giao batch ban đêm. Không dựng thêm repo hay máy chủ chỉ để được code song song.

## 0. Giới hạn trước khi triển khai
- Hai kho: Huyen1974/agent-data-test và Huyen1974/web-test, hiện PRIVATE. Không tự chuyển public khi chưa rà toàn bộ lịch sử/secret. Mua Pro sau khi có bằng chứng cần hard-lock private, không phải bước đầu.
- Chỉ có Codex là executor đề xuất xuyên suốt roadmap sau khi Owner cấp RUN. Claude Code CLI là Chief/reviewer khác ghế, GPT Host chốt prompt và điều hành, Owner duyệt các mutation production.
- Không thay đổi VPS runtime, remote Git, deploy, secrets, cron, Guard, mã main hoặc GitHub Actions khi roadmap chưa được Owner thống nhất.
- GitHub Actions sẽ OFF hoàn toàn. Kiểm thử unit ở máy riêng agent/Mac/sandbox; kiểm tích hợp/staging có giới hạn tài nguyên, không dồn toàn bộ lên VPS1.

## I. Bảng công việc (R0 chỉ đọc; R1 là thay đổi đầu tiên)
| Mốc | Việc Codex thực hiện sau RUN riêng | Đạt khi / Bằng chứng | Giới hạn |
|---|---|---|---|
| **R0 — Khảo sát Git VPS** | Chỉ đọc 3 worktree, remotes, upstream, HEAD, tracked/untracked, cron/hook/job backup ngược; đối chiếu mã Git với image/runtime đang phục vụ, và các workflow GH còn gánh chức năng quan trọng. | Manifest: từng nguồn VPS → chức năng → path GitHub/ngoài Git → độ mới → hash/commit, danh sách Actions được phép tắt ngay. | Không gọi deploy/pull/reset/restart/script ghi; không in credential. |
| **R1 — Tắt Actions hai repo** | Sau R0, tắt Actions ở cấp repo (tất cả push/PR/schedule/dispatch), xử lý run đang dở và required checks, bảo đảm đường canh/backup thiết yếu có thay thế nếu cần; không xóa YAML hay phục hồi SSH root key. | Settings hai kho = Disabled, push/PR không khởi chạy workflow mới; 0 phút Actions phát sinh mới; không gián đoạn production. | Nếu workflow thiết yếu chưa có đường thay, NO-GO phần tương ứng; không tắt bừa. |
| **R2 — Vai trò và chuẩn giao việc** | Codex tạo bản đề xuất trong branch riêng ở 2 repo: AGENTS.md, README scope, CONTRIBUTING, mẫu Issue/PR, CODEOWNERS nếu phù hợp; chuẩn 6 ô (TASK_ID · mục tiêu+DoD/test · scope · dependency · worker/Chief · budget/điều cấm), nhánh dev/<seat>/<task-id>, quyền actor. Thử đăng nhập độc lập. | 3 agent đọc và biết nhận việc/test/nộp PR, Claude biết 4 kết luận NHẬN/SỬA/TRẢ/BỎ; luật khóa main có kết quả thử thực; chưa ghi main cũ. | CODEOWNERS/đọc luật không thay quyền cưỡng chế. Nếu private Free chưa khóa main thì giữ NO-GO merge chính thức; không tự public. |
| **R3 — Phân phạm vi + mã nền mới nhất** | Chốt module/path cho 2 kho; nhận diện DOT/Graph/systemd/nginx/Guard/config khác chưa có nhà. Đóng dấu HEAD main cũ bằng nhánh/tag archive. Lấy snapshot tracked code từ VPS thực đang chạy, loại secret/.env/data/dump/backup/build sinh, tạo branch baseline-candidate và manifest so từng file/hash. | Mọi path có chủ hoặc OUT-OF-SCOPE; bản nguồn được xác minh là đang phục vụ; candidate sạch, có điểm quay lại main cũ; GitHub không đưa mã cũ xuống VPS. | **Không xóa main, không force-push, không reset --hard hay tự động kéo xuống VPS.** Chỉ chuẩn bị ứng viên, chưa đổi SSOT. |
| **R4 — Thử CI/CD không Actions** | Từ candidate cho 3 worker độc lập clone/worktree, nhận 3 việc khác vùng, đẩy 3 branch/PR thật; Chief lấy HEAD mới nhất, dựng merge-candidate, test DoD+regression, xử lý conflict, quyết định; chạy CD dry-run/staging, kiểm rollback. | 3 agent/3 workspace/3 PR, ≥2 PR được Chief nhận, giữ đủ mã cũ/mới, Actions 0; kiểm thử thật và staging/dry-run PASS. | Dry-run không tương đương deploy production. Môi trường test phải cô lập; VPS1 swap hiện gần cạn. |
| **R5 — Chuyển mã/nguồn deploy** | Chỉ sau Owner GO: đưa baseline đã kiểm vào main theo **forward commit** có rollback, không phá lịch sử. Bật/test hard-lock main bằng actor thực; VPS fetch đúng release SHA bằng quyền read-only qua deploy gate, smoke/rollback thật; chỉ tắt backup ngược VPS→GH khi xác minh mã đã khớp. Sau đó mới chuyển viết mã hàng loạt qua GitHub và thử ca đêm DOT→Codex. | 2 main chứa đúng mã được chốt, bảo vệ branch có phép thử âm, VPS không thể pull nhầm mã cũ, một bản release có thể quay lại; 3–5 agent code song song, sáng có bảng kết quả. | Không auto-deploy mỗi push, không đổi production ngoài RUN và Guard, không xóa nhánh/lịch sử cũ. |
| **R6 — Thử vận hành ban đêm sau R5** | Kết nối DOT→Codex→worker bằng hội đồng hiện có, giao batch 3–5 việc, có biên nhận, thời hạn và báo cáo PR/test sáng. | Ca đêm không cần Owner canh, có trạng thái và receipt từng việc, không tự deploy. | Thiếu đường gọi/receipt ⇒ NO-GO R6, không chạy nền giả. |

## II. Ba điều chỉnh quan trọng
1. “Tắt Actions đầu tiên”: R0 read-only là bước kiểm an toàn, **R1 là thay đổi thật đầu tiên** sau khi Owner ký kế hoạch; không làm mất monitoring/backup đang phụ thuộc Actions.
2. “Xóa mã main hiện tại”: không xóa lịch sử hoặc force-push. Tạo archive HEAD cũ + candidate bản VPS, kiểm hash, thử CI/CD, rồi thay cây mã trên main bằng một commit tiến lên khi Owner GO. Backup cũ và đường VPS vẫn giữ nguyên đến mốc cuối.
3. “Repo mở”: hiện hai repo đang private. Nếu muốn public thì phải rà cả lịch sử và tệp cũ, không chỉ snapshot hiện tại. Chưa cần quyết ở roadmap V0.1.

## III. Ranh giới repo cần Codex kiểm chứng tại R3
| Repo / vùng | Dự kiến sở hữu | Ngoài phạm vi |
|---|---|---|
| agent-data-test | Ứng dụng Agent Data/RAG, code truy vấn/ingest, adapter vector/PG, MCP/backend thuộc Agent Data, test liên quan | Dữ liệu PG/Qdrant, env, secret, backup, cấu hình hệ điều hành |
| web-test | UI/Nuxt, frontend, web integration/Directus interface, frontend tests | Data Directus/PG, secrets, RAG core, cấu hình runtime chưa phân nhà |
| OUT-OF-SCOPE | DOT runtime, Graph, nginx, systemd, Guard, scripts/compose chung chưa rõ chủ | Không tự ép vào 2 kho, không tự mở repo ops mới |

## IV. Quy trình nhận việc / review / chạy đêm (dùng lại hội đồng hiện có)
- Host chuẩn bị sẵn batch nhiệm vụ có 6 ô; Owner duyệt batch và quyền. Agent đọc AGENTS.md, Issue/PR contract và COLLAB liên quan; mỗi agent có branch và môi trường độc lập, không cần lấy cờ VPS-GHI khi viết mã.
- Chief lần lượt xử lý PR: kiểm đúng scope, phiên bản main mới nhất, test trên ứng viên merge, phát NHẬN/SỬA/TRẢ LẠI/BỎ; xung đột phải trả cụ thể, không auto ours/theirs; nếu main thay đổi sau khi kiểm thì kiểm lại. Tác giả không được tự review độc lập.
- Chỉ sau khi đường gọi có receipt mới cho DOT nhắc Codex điều phối ban đêm; trước đó giao/nhận thử trực tiếp, không nhận vơ “tự chạy”. Sáng báo TASK_ID, worker, PR/SHA, test, Chief, blocker, release/deploy status.

## V. Bằng chứng đọc trực tiếp 24/10/2026 (không mutation)
- VPS: agent-data branch claude/gpt-operation-id-20260918 HEAD 75ed0e80; UI master HEAD af8d1404; workspace main HEAD a329c68f; cả 3 worktree sạch. Chưa đo git remote/upstream hay mã đang chạy theo image.
- GitHub: agent-data-test main 0a26280b, web-test main 07caed3b; cả 2 private và main chưa protected. 17 + 11 tệp workflow hiện hữu, Actions web còn chạy 24/10. Ruleset trên private repo chưa khả dụng với plan đang có (API yêu cầu Pro/public).
- Trước mỗi RUN phải lấy lại HEAD/manifest tại thời điểm đó. Trạng thái DRAFT không cấp quyền thay đổi bất cứ thứ gì.
