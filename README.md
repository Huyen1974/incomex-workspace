# incomex-workspace

Kho làm việc CÔNG KHAI (PUBLIC từ 17/09/2026 — không commit secret; secret scanning + push protection đang bật) để Claude/ChatGPT đọc–sửa file qua đầu nối MCP "Incomex VPS" (gốc `gh`).
Commit từ GPT workspace dùng tác giả "AI via Incomex Workspace"; connector Claude hiện hữu giữ tác giả riêng. Không force-push lên `main`.

GPT dùng app "Incomex AgentData MCP — GPT Full b1gdc", root `workspace`: đọc cửa sổ nhỏ → exact edit với expected_version → commit/push → kiểm diff. File lớn hoặc HTML một dòng dùng workspace_read/search/edit; GitHub native dùng browse, PR/review và file nhỏ.

Các file `acceptance/gpt-*` là bản sao kiểm thử ngày 17/09/2026, không phải nguồn ứng dụng business.

**File thử — agent đừng đọc cả file:** `acceptance/gpt-*`, `acceptance/moved/*`, `acceptance-20260918-*.html` (~2,2 MB), `chatgpt-direct-upload-*.html` (~1,8 MB) là file thử của GPT (tác giả "AI via Incomex Workspace"), giữ nguyên chỗ vì GPT có thể còn dùng; chứng tích thử của Claude đã gom vào `_luu-tru-chung-tich-claude/` (xem INDEX.md trong đó, cũng không đọc). Đã kiểm file 314 KB và một dòng 2,21 MB, stale HEAD/SHA và commit chen ngang. App GPT cần Refresh để nhận đủ 20 tool; giữ nguyên URL/secret.

## Shared Workspace Technical Contract — v1.3, 2026-09-18

> **Phân vai nguồn chuẩn:** `AGENTS.md` = luật phối hợp/vai trò/workflow; README mục này = hợp đồng **kỹ thuật** của workspace/connector; `COLLAB.md` = trạng thái hiện hành của project. Không chép cùng một luật giữa các file.
> Đổi so với v1.2 (cùng ngày): áp dụng `FOUNDERS_CONSENSUS_V1`, chuyển luật phối hợp sang `AGENTS.md`, giữ README làm technical contract; tạo `COLLAB.md` gốc để lưu quyết định/trạng thái. Các §0–§11 bên dưới vẫn là nguồn chuẩn cho cơ chế kỹ thuật.
> Đổi so với v1.1 (cùng ngày): thêm §11 — VPS là nguồn gốc duy nhất của MÃ; GitHub không còn đường ghi xuống VPS.
> Đổi so với v1.0 (cùng ngày): thêm §0 ba đường ghi (kể cả GitHub native ghi thẳng), §7 quyền xoá, §8 file lớn/Unicode và §10 báo kết quả; §3 thêm luật thay-chuỗi; §4 ghi kết quả đo bảo vệ nhánh; §9 thêm hai dòng chi phí đo thật.

Hai đầu nối độc lập (GPT: AgentData `workspace_*`; Claude: "Incomex VPS" `fs_*`) dùng chung nơi làm việc theo MỘT hợp đồng. Phạm vi SSOT của GitHub là các file **thuộc repo này**; KB, source các repo khác và file UI chưa quản lý trong repo không phải cùng nguồn.

**0. Ba đường ghi — không phải đường nào cũng có cùng chốt chặn.**

| Đường ghi | Qua VPS | Khoá chung `ui` | Máy quét bí mật | `expected_head` | Khoá chống ghi đôi |
|---|---|---|---|---|---|
| (1) GPT — app AgentData `workspace_*` | có | có | có | `expected_HEAD` | `upload_id` + commit idempotent + `operation_id` cho cả 5 tool ghi (XONG 18/09/2026) |
| (2) Claude — đầu nối "Incomex VPS" `fs_*` | có | có | có | `expected_head` | `operation_id` |
| (3) GitHub native — đầu nối GitHub gắn sẵn của ChatGPT | **KHÔNG** | **KHÔNG** | **KHÔNG** | **KHÔNG** | **KHÔNG** |

Đường (3) ghi THẲNG vào `Huyen1974/incomex-workspace`, không đi qua VPS. Nó tiện cho browse/PR/review và file nhỏ, nhưng thiếu ba chốt chặn ở trên, nên khi dùng nó:

- Sửa file hiện hữu **bắt buộc dùng SHA hiện tại của chính file đó**. SHA của blob chỉ chống ghi đè trên CÙNG một file — nó KHÔNG thay được `expected_head` và không thấy việc người khác vừa đổi file khác.
- Việc phối hợp quan trọng: **biết HEAD trước khi ghi và kiểm diff sau khi ghi**.
- HEAD hoặc file đổi ngoài dự kiến → **đọc lại và hoà giải, không ghi đè**.
- **Không** dùng các thao tác file rời của GitHub native để thay cho một **giao dịch nhiều file nguyên tử**; chỉ đường (1)/(2) mới có một-commit-hoặc-không-gì.
- Repo này PUBLIC và trên đường này **không ai chặn hộ**: tự kiểm bí mật trước khi ghi.

1. **Tài nguyên** — `workspace`/`gh` = hai clone riêng của repo này, cùng nhánh `main`; `ui` = MỘT thư mục vật lý trên VPS (`/opt/incomex/docs/mcp-writes`, phục vụ tại `/ui-preview/mcp-writes/`); `docs` chỉ đọc.
2. **Khoá** — `ui`: một khoá `flock` chung (cùng inode) cho cả hai bên: ghi giữ exclusive, đọc giữ shared; chờ ngắn rồi trả BUSY (`WORKSPACE_BUSY` / `[DENIED:busy]`) kèm retry, không treo. Snapshot 5 phút của sổ git `ui` là **người ghi thứ ba trên cùng thư mục**: nó cũng lấy đúng khoá chung đó, chờ tối đa ~15 s rồi **bỏ lượt** (lượt sau chụp bù) — không bao giờ commit nửa vời giữa lúc bên kia đang thay nhiều file. Ảnh chụp gom cả thay đổi do GPT ghi thẳng: đó là **lịch sử chung**, không phải rác để rollback. `main`: không cần khoá chung — bảo vệ bằng push non-force + kiểm HEAD.
3. **Phiên bản** — mọi sửa/ghi đè/di chuyển/sao chép mang `expected_version` (hash nội dung đã đọc) và, với Git, `expected_head`/`expected_HEAD` (commit đã đọc). Lệch → từ chối có mã (`VERSION_CONFLICT` / `[DENIED:version_mismatch|head_mismatch]`), đọc lại rồi sửa trên bản mới; không lấy HEAD mới để hợp thức hoá yêu cầu cũ. Thay chuỗi: xác nhận target đúng và DUY NHẤT trước khi replace; giữ nguyên phần ngoài phạm vi yêu cầu, không dựng lại phần chưa đọc; sửa xong đọc lại/diff, thấy thay đổi ngoài dự kiến thì dừng hoặc hoàn nguyên.
4. **Commit/push** — trong vùng khoá: fetch/pull → kiểm HEAD + phiên bản → chuẩn bị → guard → commit ĐÚNG các file của thao tác (không commit lẫn file người khác) → push fast-forward, không bao giờ force. Giao dịch nhiều file = validate tất cả trước, một commit, lỗi ở op nào báo op đó và không đổi gì. Thử nghiệm dùng branch/path riêng, không chạm production nếu chưa được giao rõ. Đã đo 18/09/2026 bằng API quyền admin: `main` có bảo vệ THẬT — `allow_force_pushes=false`, `allow_deletions=false`, `enforce_admins=true` (áp cả cho chủ repo), secret scanning + push protection bật; ruleset mới rỗng là bình thường, chốt chặn nằm ở branch protection cổ điển.
5. **Retry & mất phản hồi** — mỗi thao tác ghi có khoá idempotency (Claude: `operation_id`; GPT: `upload_id`/commit idempotent + `operation_id` cho cả 5 tool ghi, XONG 18/09/2026): cùng id + cùng payload = trả kết quả cũ, không commit lần hai; khác payload = từ chối. Push bị từ chối chắc chắn → chỉ phục hồi thay đổi của chính thao tác. Mất mạng/timeout → `OUTCOME_UNKNOWN`/`RECOVERY_REQUIRED` + id; kiểm journal/commit/remote trước, không rollback hay push lại mù.
6. **Xuất công khai** — repo này PUBLIC và `ui` là trang web: nội dung đi vào bằng bất kỳ đường nào (write/edit/copy/import/transaction) đều qua kiểm bí mật; gốc `code` (mã hạ tầng) không bao giờ là nguồn sao chép. Trên đường (3) không có máy quét — người gọi tự chịu trách nhiệm kiểm trước khi ghi.
7. **Quyền xoá** — hai đầu nối qua VPS **cố ý không có công cụ xoá** (chỉ `fs_move`/rename): đó là luật nền của chủ. GitHub native thì CÓ `delete_file`. Trên repo chung: `delete_file` **chỉ dùng khi chủ duyệt TỪNG LẦN**; dọn dẹp thì **chuyển vào `_luu-tru-chung-tich-*/` bằng rename**, không xoá. Nhánh phụ đã dùng xong cũng hỏi trước khi xoá. Chứng tích thử của bên kia không phải rác của mình.
8. **File lớn, Unicode, assets** — chỉ cần một phần thì đừng đưa cả file lớn vào ngữ cảnh. Qua VPS: đọc theo cửa sổ (`fs_read` với `max_bytes`/`start_line`/`start_char`) và định vị bằng `fs_search` trước. Qua GitHub native, file >1 MB: `fetch_file` lấy metadata/SHA → `fetch_blob` → cắt/tìm trong tool → chỉ đưa đoạn liên quan cho mô hình (`fetch_file(start_line/end_line)` có thể trả content RỖNG với file >1 MB — dùng blob thay thế). Giữ nguyên path/tên file Unicode kể cả dạng NFD: không tự normalize/rename; giữ relative path, assets và manifest liên quan nếu nhiệm vụ không yêu cầu đổi; không nhúng binary/base64 vào file text lớn.
9. **Chi phí** — tìm rồi sửa ngay khi đủ ngữ cảnh; đọc theo cửa sổ; copy/move/transaction chạy server-side; kết quả dài có cursor/continuation, chỉ đọc tiếp khi cần. Đo thật 24 h (18/09/2026: 352 lượt gọi, 10,8 MB dữ liệu trả về): **soi bằng CHỮ trước, chỉ chụp ảnh khi thật sự phải nhìn hình** — `ui_screenshot` 479 KB/lần (16 ảnh = 7,5 MB ≈ 69% toàn bộ dữ liệu trả về) so với `ui_inspect` 2 KB/lần, rẻ hơn ~240 lần. **Ưu tiên thao tác chạy trên máy chủ** (`fs_stat` 293 B, `fs_copy` 261 B, `fs_transaction` 337 B) thay vì chuyển nội dung qua mô hình.
10. **Báo kết quả** — chỉ báo PASS khi đã GỌI THẬT; không suy từ mã nguồn hay từ báo cáo cũ. Phân biệt rõ ba loại bằng chứng: (a) backend/CLI, (b) client Claude Chat/Cowork, (c) client ChatGPT/Work/Codex — gọi được qua CLI KHÔNG phải là PASS ở client thật. Nêu ngắn: file/path, branch/ref, version hoặc SHA trước/sau, phần đã đổi, kiểm tra đã chạy. Có giới hạn công cụ thì nói đúng giới hạn và cách đi vòng đã kiểm chứng.
11. **Mã và runtime trên VPS — VPS là NGUỒN GỐC DUY NHẤT (chốt của chủ, 18/09/2026).** Mục này nói về MÃ, khác với §17 nói về file của chính repo này.

    1. Mã và runtime trên VPS là nguồn gốc duy nhất. Mã trên VPS mới hơn GitHub rất nhiều.
    2. Kho mã trên GitHub (`agent-data-test`, `web-test`) chỉ là **bản sao lưu · lịch sử tham khảo · nơi đọc lại**.
    3. Không một workflow, webhook, runner hay lệnh kéo nào được triển khai hoặc ghi đè mã trên VPS.
    4. Chiều **VPS → GitHub** được phép sau khi quét bí mật (cron `git-push-gh-daily-v2.sh`, 06:00 và 18:00, đẩy nhánh `vps-daily-*`).
    5. Chiều **GitHub → VPS** chỉ được phép với repo này, vào đúng hai clone file làm việc dưới đây, và chỉ vào vùng KHÔNG thực thi.
    6. VPS và GitHub khác nhau → **VPS là bản đúng**; không tự đồng bộ từ GitHub xuống.
    7. Không `rsync --delete` từ GitHub vào vùng mã.
    8. Không thông tin đăng nhập GitHub nào được có quyền root hay quyền ghi vào VPS.

    **Muốn đổi mã thì làm thế nào?** Sửa trên VPS → dựng tại chỗ → đẩy bản sao lên GitHub. Không có đường nào khác.

    **Ngoại lệ, nêu đích danh:** `Huyen1974/incomex-workspace` → `/opt/incomex/mcp-roots/gh` (đầu nối Claude) và `/opt/incomex/data/workspace-tools/github-workspace` (đầu nối GPT). Quyền đọc-ghi file làm việc; không thực thi; không chạm `/opt/incomex/docker`, compose, systemd hay runtime. Không mở rộng ngoại lệ sang kho khác.

    **Trạng thái đường cắt 18/09/2026:** bí mật `VPS_SSH_KEY` đã xoá khỏi cả `agent-data-test` và `web-test` (không còn ở cấp kho, environment, dependabot, codespaces; không có tổ chức, không webhook, không self-hosted runner, không deploy key). Sáu workflow ghi xuống VPS đều `disabled_manually`. **File workflow và `VPS_HOST` được GIỮ NGUYÊN có chủ ý** theo yêu cầu của chủ: đấu lại = nạp lại một bí mật `VPS_SSH_KEY` + bật workflow, không phải dựng lại từ đầu.

Hướng dẫn riêng từng đầu nối: GPT `docs/WORKSPACE_TOOLS.md` (repo agent-data); Claude `claude-mcp/00-NHAN-THU-MUC.md` + báo cáo KB `knowledge/current-state/reports/mcp-incomex-vps-nang-cap-fs-roots-2026-09-17.md` §12.

12. **Owner View — mirror HTML từ workspace ra VPS.** Quy tắc này áp cho artifact công việc của `incomex-workspace`, không thay đổi §11 về mã/runtime VPS.

    1. Mỗi việc có một thư mục riêng và đúng một HTML chính đã khai báo (`view.html` mặc định hoặc path ghi trong `COLLAB.md`). Bản trong workspace/Git là bản nội dung chuẩn của việc.
    2. VPS chỉ giữ **bản mirror tĩnh** của HTML chính để Owner xem bằng URL; mirror không phải nguồn chỉnh sửa thứ hai và không được dùng làm nơi AI sửa nội dung nghiệp vụ.
    3. Nút **Cập nhật** là thao tác pull thủ công theo từng việc: chỉ lấy đúng HTML chính đã allowlist từ workspace/Git sang vùng Owner View rồi reload. Không tự đồng bộ nền, không kéo cả repo, không `rsync --delete`.
    4. Vùng Owner View không được có quyền ghi vào mã/runtime, systemd, compose, secret hoặc thư mục dịch vụ. Nếu cần mã cho dịch vụ refresh/view thì mã đó tuân §11: sửa và vận hành trên VPS, không kéo mã runtime từ GitHub xuống.
    5. File phụ (`COLLAB.md`, `PROMPT.md`, evidence, assets kỹ thuật) phục vụ AI/Agent; giao diện Owner mặc định chỉ cần dẫn tới HTML chính. Chỉ lộ thêm khi Owner yêu cầu.
    6. Mẫu đích của mọi việc: **một việc → một thư mục → một HTML chính → một URL Owner View → một nút Cập nhật**.
