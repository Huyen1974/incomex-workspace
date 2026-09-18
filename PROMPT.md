# PROMPT — Gói B: sửa gốc 2 lỗi "im lặng" của đầu nối (P03, P05)

Trạng thái: DRAFT · Người soạn: Claude Chat · 2026-09-18
Chỉ chạy khi `COLLAB.md` ở gốc repo ghi `READY@<commit>` khớp commit cuối chạm file này VÀ Owner ra lệnh RUN.

## 0. Kiểm trước khi làm (bắt buộc)
1. Clone riêng để kiểm, không cần khoá (repo công khai): `git clone --depth 50 https://github.com/Huyen1974/incomex-workspace /tmp/iw-ready`. Trong đó lấy `git log -1 --format=%H -- PROMPT.md` và dòng `READY@...` trong `COLLAB.md`. Khớp tiền tố → làm tiếp; lệch hoặc chưa có READY → DỪNG, báo lại.
2. Đọc từ chính clone đó: `AGENTS.md`, `README.md` (§0–§11, nhất là §11: mã trên VPS là nguồn gốc duy nhất), `COLLAB.md` mục P03, P05, P06.
3. KHÔNG fetch/pull/sửa hai clone làm việc của đầu nối (`/opt/incomex/mcp-roots/gh`, `/opt/incomex/data/workspace-tools/github-workspace`): chúng do dịch vụ khác quản lý, chạy git bằng user khác có thể làm hỏng quyền file.

## 1. Bối cảnh
Repo chung `Huyen1974/incomex-workspace` có hai đầu nối tự viết, chạy trên VPS:
- Claude: `/opt/incomex/claude-mcp` (container `incomex-claude-mcp`), gốc `gh` = clone `/opt/incomex/mcp-roots/gh`.
- GPT: `/opt/incomex/docker/agent-data-repo/agent_data/workspace_*.py` (container `incomex-agent-data`).
Hai lỗi cùng một gốc "im lặng": một công cụ đọc bản cũ mà không báo, một công cụ từ chối mà không nói lý do.

## 2. Việc 1 — Claude: fs_log/fs_diff phải kéo bản mới như các công cụ đọc khác (P03)
- `claude-mcp/app/fsroots.py`: `fs_list`, `fs_read`, `fs_stat`, `fs_search` gọi `_freshen(root, cfg)` (dòng ~273) trước khi đọc; `fs_log` (dòng ~1338) và `fs_diff` (dòng ~1361) KHÔNG gọi.
- Sửa: gọi `_freshen` ở đầu hai hàm này và nối chuỗi cảnh báo nó trả về vào kết quả, đúng cách `fs_read` đang làm. Không đổi gì khác (tham số, định dạng, giới hạn).
- Vì sao quan trọng: nội dung đọc bản mới mà lịch sử đọc bản cũ thì phép kiểm READY có thể khớp nhầm, Agent chạy bản PROMPT chưa duyệt.

## 3. Việc 2 — GPT: GIT_OPERATION_FAILED phải nói bước nào hỏng (P05)
- `agent_data/workspace_tools.py`, hàm `git()` (dòng ~136–158): lỗi nào cũng trả chung `GIT_OPERATION_FAILED`, bỏ stderr, không ghi log. Write (`workspace_tools.py` dòng ~446) và transaction (`workspace_operations.py` dòng ~110) chạy `git diff --cached --check`, nên nội dung có dấu cách cuối dòng, dòng trống thừa cuối file hoặc dòng bảy dấu bằng bị từ chối mà client không biết vì sao.
- Sửa: giữ nguyên mã lỗi `GIT_OPERATION_FAILED` (không vỡ client); thêm vào `detail` tên lệnh git con thật (bỏ qua các cặp `-c key=value` đứng trước). Với lệnh cục bộ (không phải fetch/push/ls-remote) kèm stderr đã qua `safe_content`, cắt tối đa 600 ký tự; với `diff --check` đó là các dòng `path:line: trailing whitespace`. Lệnh mạng giữ nguyên che output. Ghi cùng thông tin (không credential) vào nhật ký của container.
- Không tự sửa hay chuẩn hoá nội dung người dùng; chỉ báo rõ.

## 4. Triển khai và quyền (Owner cấp qua lệnh RUN)
- Sửa trên VPS, dựng tại chỗ (README §11); không kéo mã từ GitHub. Trước khi dựng, xác định container đang chạy mã bằng mount hay image rồi làm đúng cách đó; đọc `claude-mcp/00-NHAN-THU-MUC.md`.
- Được phép: restart `incomex-claude-mcp`; restart `incomex-agent-data` chỉ khi không có tác vụ hoặc giao dịch đang chạy (hàng đợi job rỗng, không manifest `prepared`/`push_unknown`/`rollback_conflict`). Còn bận thì chờ tối đa 10 phút; vẫn bận → DỪNG, báo.
- Container không healthy trong 2 phút sau restart → hoàn nguyên đúng commit mã của mình, dựng lại, báo. Đây là hoàn nguyên duy nhất được phép.
- Commit thay đổi mã vào git sẵn có của từng thư mục mã, message bắt đầu `[Claude Code] P03` hoặc `[Claude Code] P05`.

## 5. Kiểm (bằng chứng gọi thật, README §10)
- K1 (GPT, không đụng clone thật): tạo repo git tạm trong /tmp, dùng `git()` với nội dung có dấu cách cuối dòng rồi `diff --cached --check` → detail có "diff" và "trailing whitespace"; gọi một fetch tới remote giả hỏng → detail KHÔNG chứa URL, credential hay output thô.
- K2 (Claude): diff mã chỉ đổi đúng hai hàm; container healthy sau restart; `fs_log`, `fs_diff` vẫn trả kết quả bình thường.
- K3: hai container healthy; log hai service không có lỗi mới trong 10 phút sau restart.
- K4: hai clone làm việc sạch và HEAD trùng GitHub — chỉ đọc, dùng `GIT_OPTIONAL_LOCKS=0 git status --porcelain` và `git rev-parse HEAD` với đúng user sở hữu thư mục.
- Nghiệm thu ở client (không phải việc của Agent): Claude Chat gọi `fs_log` ngay sau một commit mới của GPT mà không đọc gì trước; GPT thấy lỗi khoảng trắng được báo rõ file và dòng.

## 6. Cấm
Không xoá file. Không sửa repo `incomex-workspace` (AGENTS/README/COLLAB do Host sửa). Không đổi schema hay tên tool. Không đụng service, cấu hình, dữ liệu nào ngoài mục 4. Không mở rộng phạm vi. Gặp gì ngoài dự kiến → DỪNG, báo.

## 7. Báo cáo
Mở đầu bằng bảng: Việc 1, Việc 2, K1–K4 × 🟢🟡🔴 + bằng chứng một dòng. Sau đó: file và dòng đã đổi, commit mã, lệnh restart đã chạy và lúc nào, mục nào còn chờ client nghiệm thu. Chỉ báo PASS với thứ đã gọi thật.
