# PROMPT — GHM R1 · ĐÁNH GIÁ SELF-HOSTED RUNNER THAY GIẢI PHÁP S1.4
RUN_ID: GHM-R1-SELFHOST-FIT-20261025-01
STATUS: DRAFT_NOT_READY — KHÔNG RUN. Chỉ sau Claude Reviewer ACCEPT đúng last-touch SHA và GPT Host READY cùng SHA, Owner mới giao Codex. KQ R0R1-20261024-01 đã DỪNG; không tái sử dụng RUN_ID.

Executor_Surface: Codex CLI/Desktop · Write_Path: Incomex workspace_* root=workspace cho STARTED/KQ/Bảng, GitHub API/UI **CHỈ ĐỌC**; VPS đọc theo cổng hiện có (không sudo/SSH ghi). Báo cáo bảo mật chi tiết chỉ đọc tại khu root-only được P12 chấp thuận nếu có quyền; không sao chép sang repo public.

ENTRY: AGENTS.md → root COLLAB → github-management COLLAB §0/Bảng/P12/P13 → ROADMAP V0.3 + KE-HOACH → PROMPT này. Tuân A6/DROOT30/31; thiếu READY/Owner RUN ⇒ DỪNG.

## S0 — NHẬN KẾT QUẢ P12 (≤10 phút)
- Tái sử dụng toàn bộ P12 và `/opt/incomex/work/github-management/GHM-R0R1-20261024-01/R0-R1-report.json` nếu có quyền đọc; không dò credential, không mở quyền root, không lặp kiểm kê 33 workflow.
- Xác minh ba NHÓM MIGRATE_BLOCKED bằng tên workflow/ID, đích kiểm, run/trigger, đầu vào/bằng chứng thành công và sai lệch `connection refused` (chỉ trong báo cáo root-only). GitHub đang Actions ON; không đổi cấu hình.

## S1 — ĐO KHẢ NĂNG CHẠY TRÊN MÁY CỦA MÌNH (≤20 phút)
- Kiểm máy có sẵn nào thật sự có thể nhận self-hosted runner (ưu tiên VPS2 tách biệt, hoặc máy 24/7 khác): hệ điều hành/CPU/RAM/swap trống, outbound HTTPS 443 tới GitHub, đường đọc tối thiểu tới ba audit, process/service runner hiện có, cách cô lập. Không giả định VPS2 đang chạy. Chỉ metadata/khả năng, không kết nối mới tới dữ liệu nhạy cảm.
- Loại trừ VPS1 sản xuất đang swap gần cạn và mọi phương án cần chạy runner bằng root, truy cập Docker socket hay mount thư mục secret production. Repo cá nhân: xác định cần bao nhiêu registration runner cấp repo (agent-data-test và web-test) trên máy được chọn; không chuyển các repo sang org.
- Kiểm các nguồn workflow YAML/trigger/`runs-on` của 3 nhóm được bảo toàn; còn bao nhiêu workflow ACTIVE không cần thiết phải `gh workflow disable`; kiểm các branch/push/PR chưa bảo vệ có thể gây job hosted. Không sửa file YAML/branch/settings.

## S2 — KIỂM KHẢ NĂNG TƯƠNG ĐƯƠNG (≤15 phút)
- So yêu cầu của 3 nhóm kiểm đang có với môi trường runner mới: công cụ/runtime cần thiết, đường mạng, credential đọc giới hạn, dữ liệu mà kiểm tra thực sử dụng, thời hạn kiểm, giới hạn CPU/RAM, test kết quả chính xác và cách khôi phục khi runner down.
- Hai phương án: A GitHub Actions ON + self-hosted `actions/runner` + 3 nhóm kiểm; B Actions OFF + script/test/timer của VPS đang có sau khi sửa lỗi. Cân độ phức tạp nhỏ nhất cho mục tiêu 0 hosted compute, tránh tự dựng scheduler/runner controller.
- Ghi rõ nếu không có máy tách biệt hoặc kiểm semantic/vector vẫn FAIL ⇒ NO-GO cài runner; không đẩy lỗi sang VPS1.

## S3 — KQ ĐỂ HOST GIAO LỆNH CÀI (≤10 phút)
- Trên COLLAB public chỉ ghi: A/B khuyến nghị, runner host khả thi CÓ/KHÔNG/UNKNOWN, số workflow cần giữ/tắt, hosted-minute risk CÓ/KHÔNG, blocker, Owner phải quyết đúng một câu. Chi tiết hostname, actor, credential locations, mạng đặc quyền, runner registration lưu ở khu root-only, không in public.
- Trả rõ kế hoạch RUN triển khai sau: Codex cài/cấu hình runner trên host đã Owner duyệt, từng workflow thừa disable qua GitHub UI/API, Chief kiểm/merge YAML `runs-on: self-hosted`, so kết quả audit, kiểm billing, rollback — KHÔNG tự thi hành bước đó trong RUN này.
- KQ@GHM-R1-SELFHOST-FIT-20261025-01 XONG|DỪNG và Bảng cùng commit, nhả tài nguyên; không tự READY/RUN mới.

CẤM: cài runner, bật/tắt Actions, disable workflows, sửa branch/YAML/code/main, mua Pro, đổi secrets/SSH/Docker socket/Guard, restart/build/đụng production, tạo cron/systemd, hoặc dùng root trên VPS1. Nếu thiếu quyền hoặc dữ kiện ⇒ UNKNOWN/DỪNG sạch, không ngồi chờ.
