# PROMPT — AI-COUNCIL-KARPATHY N0 · KHẢO SÁT CỔNG CƯỠNG CHẾ & UI, CHỈ ĐỌC
RUN_ID: ACK-N0-READONLY-20261028-01
Status: bản canonical; chỉ chạy khi COLLAB có READY@full last-touch PROMPT SHA do GPT Host ký và Owner chuyển lệnh thủ công (AUTO0).
Executor_Surface: Claude Code CLI trên Mac của Owner · Worker anthropic-cc-worker.
Read scope: Huyen1974/incomex-workspace; Huyen1974/agent-data-test; Huyen1974/web-test; source/config VPS liên quan bằng quyền chỉ đọc đã có.
Write_Path: duy nhất `work/ai-council-karpathy/COLLAB.md` qua `fs_*` hoặc `workspace_*` đã audit để ghi STARTED/P/KQ. Direct GitHub/API/CLI **chỉ đọc** đối với Workspace. Không ghi repo mã hay VPS.
Ngân sách: 1 lượt, tối đa 2 giờ; không lấy VPS-GHI, không giữ shell/terminal để chờ. Quá hạn hoặc blocker ⇒ KQ DỪNG sạch.

## Mục tiêu và điều kiện XONG
Tìm **tình trạng CƯỠNG CHẾ THẬT** của 8 cổng hiện có, đường nào còn đi vòng, việc phải viết thêm, và đúng nguồn mã UI Task đang chạy. N0 chỉ khảo sát; KHÔNG cài Vue Flow, sửa gateway, luật, CI, permission hay production. Đầu ra 1 P báo cáo trong COLLAB task (không file report mới), bảng 8 luật, link nguồn/căn cứ an toàn, trạng thái ENFORCED/PARTIAL/NOT_ENFORCED/CHƯA ĐO; xong chỉ nghĩa khảo sát đủ, không có code mới PASS.

## Cổng S0 bắt buộc
1. Đọc `AGENTS.md` Workspace → §0/Bảng + P04/P05/P06 `work/ai-council-karpathy/COLLAB.md` → PROMPT canonical. Xác minh Owner đã thực sự dispatch, đúng `RUN_ID`, `Host_ID`, roster, READY full SHA trùng commit cuối chạm PROMPT, không STOP/STARTED trùng, không COUNCIL_ALERT mở.
2. Kiểm binding `fs_*` hoặc `workspace_*` đã audit và khả năng ghi COLLAB theo phép đọc/gate, không sử dụng GitHub native để ghi. Nếu sai quyền hoặc phiên điều hành không rõ ⇒ DỪNG trước mọi mutation.
3. Chỉ sau read-gate PASS, qua đường được audit ghi `STARTED@ACK-N0-READONLY-20261028-01 <UTC> · executor=Claude Code CLI` trong COLLAB task; cập nhật Bảng theo A6. Mọi phép khám sát VPS/GitHub khác chỉ đọc.

## S1 — Ma trận 8 luật
Lập 8 hàng sau với cột `Luật | cổng kiểm thật + source/path | đường bypass | bằng chứng đo/giới hạn | còn phải làm + mức`:
1) Định danh seat/Host/worker và server-side actor; 2) READY/signature gắn SHA và đổi phiên bản; 3) VERDICT/quorum khác hãng; 4) vé ghi một lần/scope/replay; 5) KQ/bằng chứng máy; 6) COUNCIL_ALERT/Supervisor và Telegram; 7) các đường ghi Workspace `workspace_*`, `fs_*`, GitHub/SSH/admin và ruleset; 8) merge/required check/CI/ruleset của `agent-data-test`, `web-test`.
Chỉ dựa code/config/GET API read-only có chứng cứ; nếu chỉ có quy định trên giấy thì PARTIAL/NOT_ENFORCED, không viết ENFORCED. Không chạy thử âm có mutation.

## S2 — UI và phương án nhỏ nhất
Truy `https://vps.incomexsaigoncorp.vn/knowledge/modules?task=ai-council-karpathy` → đúng code server/UI của Task/Owner View và `view.html` trong Workspace. Chỉ ra đoạn đang hiển thị thanh bước, seat, từ đâu nhận COLLAB, chỗ nào có thể nhúng màn 3 tầng và Vue Flow (nếu phù hợp); kiểm bản quyền và nhu cầu pin version, không cài/chạy code nguồn ngoài, không thêm bản xem khác.
Đề nghị N1/N2 với khối lượng dự kiến theo bằng chứng, nêu tác động phụ thuộc GHM/HJW/MCPW; không tự sửa task khác hay giữ tài nguyên chung.

## STEP_WALK_V1
| Bước | Ai | Trigger | Deadline / budget | Evidence | Lỗi thì ai nhận | Bước kế |
|---|---|---|---|---|---|---|
| S0 | Claude Code CLI | Owner dispatch + READY đúng | N0 ≤2 giờ | quyền đọc và đường ghi task đã audit | KQ DỪNG → Host | S1 |
| S1 | Claude Code CLI | S0 PASS | N0 ≤2 giờ | đủ 8 hàng gắn source, trạng thái | CHƯA ĐO, Host nhận | S2 |
| S2 | Claude Code CLI | S1 đủ phạm vi | N0 ≤2 giờ | source UI thật, điểm tái dùng và rủi ro | UNKNOWN, Host nhận | S3 |
| S3 | Claude Code CLI | đủ bằng chứng/hết budget | N0 ≤2 giờ | P báo cáo + KQ cùng Bảng qua gateway | Host nhận KQ DỪNG nếu không thể ghi | Host review |

## S3 — Kết thúc
Một P tại COLLAB nêu 8 hàng + tình trạng UI + phần code cần làm và giới hạn đo; cùng commit ghi `KQ@ACK-N0-READONLY-20261028-01 XONG|DỪNG` và Bảng. Nếu không có đường ghi hợp lệ, báo Owner/Host trong chat, KHÔNG dùng direct GitHub write để lách D12.
**CẤM:** sửa runtime, code, AGENTS, secrets/keys, GSM, Directus/PG, workflow, CI, runner, quyền, branch/PR/merge, tạo repo/task/file khác, cài dependency, SSH sudo, tạo session nền hoặc tự khởi chạy N1–N4.
Sau KQ: Host GPT đọc bằng chứng, Reviewer khác hãng có ý kiến, Host quyết node tiếp theo hoặc DỪNG. NEXT_TRIGGER=HOST_REVIEW_N0.
