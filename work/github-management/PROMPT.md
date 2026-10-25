# PROMPT — GHM R2-P(A) · PILOT 3 AGENT TRÊN GITHUB FREE, CHƯA MUA PRO
RUN_ID: GHM-R2P-FREE-20261025-01
STATUS: DRAFT_NOT_READY. Chỉ khi Claude Reviewer ACCEPT last-touch full SHA, GPT Host READY@cùng SHA, Owner chuyển RUN thì Codex mới thực thi. PROMPT R2-A Pro/private P19 đã PARKED_UNRUN.

Executor: Codex CLI/Desktop; GitHub/gh API; chỉ ghi 1 repo sandbox mới `Huyen1974/agent-parallel-pilot` và task `work/github-management` cho STARTED/KQ. TUYỆT ĐỐI không mutate `agent-data-test`, `web-test`, `incomex-workspace` rulesets, VPS, production, GitHub Billing/payment.
ENTRY: AGENTS.md gốc → root COLLAB → github-management COLLAB §0/Bảng/P19/P20 → ROADMAP/KE-HOACH → PROMPT này. Tuân A6/DROOT30/31. Thiếu READY/Owner RUN thì DỪNG.

## S0: Kiểm điều kiện READ-ONLY
- Xác nhận tên repo pilot chưa tồn tại; GitHub Free cho ruleset branch ở repo public; người tạo có quyền. Actions account budget $0 + Stop giữ nguyên, không sửa Billing.
- Có bề mặt thi hành thật cho 3 agent (Codex, Hermes, Claude/cloud hoặc ghế tương đương) với 3 workspace/clone khác nhau, có đường nhận lệnh/commit/push. Chưa chứng minh ghi UNKNOWN, không giả đã giao việc. Không dựa vào khả năng Claude Code Web chưa đo.
- Mỗi worker dùng credential chỉ repo thử, không Administration và không dùng token Owner. Người thực hiện merge (Chief) phải có identity/đường bypass riêng; Codex không giữ private key Chief.

## S1: Mở duy nhất 1 kho thử PUBLIC sạch
- Tạo `Huyen1974/agent-parallel-pilot` public mới, history mới; tuyệt đối KHÔNG sao chép git history hoặc mã production/secret/env/backup/webhook/IP nội bộ từ 2 kho private/VPS.
- Tắt GitHub Actions **chỉ tại repo pilot** trước khi commit scaffold. Tạo README giới hạn pilot, AGENTS.md ≤1 trang, .gitignore, mẫu phiếu 6 ô (TASK_ID, Goal/Done_When/test, Allowed_Paths, Dependency/Base_SHA, Worker+Chief, Budget/Stop), 3 thư mục độc lập và tests Python unittest; commit scaffold lên main trước khi khóa.

## S2: Hard-lock main trên GitHub Free, rồi test bằng dev riêng
- Tạo branch ruleset ACTIVE **CHỈ `main` / `~DEFAULT_BRANCH`**, KHÔNG dùng `~ALL`. Chặn direct update/delete/nonfastforward ngoại trừ đường Chief được Owner chốt; trước/sau kiểm số write DeployKey và quyền actor, không grant bypass admin/dev tùy tiện.
- Thử bằng danh tính worker thực **không admin**: push thử main phải bị reject; tạo/push dev/<seat>/<task> phải PASS, mở PR phải PASS. Test admin bị chặn chỉ là phụ, không thay test worker. Nếu dev đang dùng Owner admin hoặc ruleset chặn mọi nhánh thì DỪNG, không nới luật cũ.
- Nếu Chief chưa có private key riêng: giữ main khóa, bước Chief-key/merge thuộc lượt R2-P(B); không báo pilot code/merge đã đạt.

## S3: Tạo 3 Issue có giá trị sử dụng
- GHMP-01 worker Codex: `task_contract/`, `tests/task_contract/`: kiểm JSON 6 ô, DoD/test.
- GHMP-02 worker Hermes: `pr_scope/`, `tests/pr_scope/`: kiểm đường tệp changed_paths so với allowlist, cấm ../.
- GHMP-03 worker Claude/ghế thứ ba: `pr_report/`, `tests/pr_report/`: tạo bảng PR sáng từ JSON giả (TASK, Worker, SHA, test, Chief decision).
- 1 việc = 1 Issue, 1 branch, 1 PR, scope không giao nhau; chỉ stdlib Python, không phụ thuộc GitHub Actions/runners mới.

## S4: KQ bootstrap và giao ca thử
- Biên nhận public: repo URL, commit SHA, ruleset nhắm main, test quyền worker push main DENIED/dev branch PASS/PR PASS, 3 Issue URLs, worker surface đã đo. Biên nhận credential/key cụ thể không đưa lên workspace public.
- Codex tạo 3 câu giao việc ngắn với Issue link để Owner gửi 3 agent đồng thời. Nếu có dispatcher đã chứng minh receipt mới được giao qua máy; không tuyên bố agent đang chạy khi chưa có thực.
- Ghi STARTED và KQ@GHM-R2P-FREE-20261025-01 XONG|DỪNG cùng Bảng theo luật; XONG chỉ nghĩa bootstrap. Trả mọi phiên/lock, không tự chạy R2-P(B), không tạo Pro, không deploy.

**Cửa nghiệm thu sau bootstrap R2-P(B):** 3 agents thật cùng code trên workspace/branch riêng, có 3 PR & test; Chief kiểm latest main và merge từng PR, ít nhất 2/3 NHẬN, 0 dev được push main, không ảnh hưởng VPS/2 repo private, report sáng theo 6 ô. Nếu chưa đủ đường gọi ba agent, báo UNKNOWN và đề xuất cách Owner giao tay; không giả PASS.
