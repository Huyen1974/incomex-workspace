# PROMPT — MCPW-LOCK · Khoá cứng đường ghi repo: chỉ 2 cổng gateway được đẩy lên GitHub

RUN_ID: MCPW-LOCK-20260924-01
Soạn: Claude Chat — Host `CLAUDE-MCPW-260924-A`, 24/09/2026. Owner duyệt: “Đúng vậy chúng ta khóa lại để bắt buộc làm theo 1 con đường giúp tôi.” (A0 của `work/mcp-workspace/COLLAB.md`; COLLAB gốc DROOT20).
Executor_Surface: **Claude Code CLI trên Mac của Owner**, dùng: (a) `gh` đã đăng nhập tài khoản GitHub của Owner (quyền admin repo); (b) `ssh contabo` **chỉ đọc**; (c) MCP “Incomex VPS” `fs_*` để ghi báo cáo.
Write_Path báo cáo: `fs_*`, root `gh`. **CẤM** `git commit`/`git push` trực tiếp và cấm ghi repo bằng `gh api .../contents` — trừ đúng phép thử T1 (một lần ghi PHẢI bị từ chối).

## 0. Vì sao (nôm na)
Luật README D12: AI chỉ được ghi repo `Huyen1974/incomex-workspace` qua 2 cổng — `fs_*` (Incomex VPS) và `workspace_*` (Agent Data). Luật chưa có khoá: đo 24/09 có 18/758 commit đi cửa sau (GitHub connector của GPT ghi dưới tài khoản Owner; git push từ Mac). Việc này bật khoá có sẵn của GitHub: **Repository Ruleset** chặn mọi lần tạo/cập nhật/xoá nhánh, chỉ miễn trừ **deploy key** (chìa của cổng). Mọi tài khoản người — kể cả Owner — bị GitHub từ chối.

## 1. Gate G0 — đọc và khớp READY (không đạt → DỪNG, không làm gì thêm)
1. `fs_read` lần lượt `AGENTS.md` → `work/mcp-workspace/COLLAB.md` → `work/mcp-workspace/PROMPT.md` (root `gh`).
2. `fs_log(root=gh, path=work/mcp-workspace/PROMPT.md, n=1)` → SHA đầy đủ phải bằng `READY@<SHA>` trong COLLAB.md. Lệch hoặc chưa có READY → DỪNG.

## 2. Gate G1 — CHỈ ĐỌC (một mục FAIL → ghi KQ DỪNG, KHÔNG bật ruleset)
- G1.1 `gh auth status`; `gh api repos/Huyen1974/incomex-workspace --jq '.permissions.admin, .visibility'` → phải `true` và `public`.
- G1.2 `gh api repos/Huyen1974/incomex-workspace/rulesets` → ghi danh sách hiện có (dự kiến rỗng). Đã có ruleset tên `gateway-only-writes` → DỪNG (không tạo trùng).
- G1.3 `gh api repos/Huyen1974/incomex-workspace/keys` → mỗi deploy key: `id`, `title`, `read_only`, `created_at`, fingerprint SHA256 (ghi trường `key` — khoá CÔNG KHAI — vào file tạm trên Mac → `ssh-keygen -lf` → xoá file tạm).
- G1.4 Cổng `fs_*`: `ssh contabo` chỉ đọc: `ssh-keygen -y -f /run/incomex-mcp-helper/gh_deploy_key | ssh-keygen -lf -` → chỉ lấy fingerprint. **Tuyệt đối không in/copy/di chuyển khoá riêng.**
- G1.5 Cổng `workspace_*` (container `incomex-agent-data`), chỉ đọc: đường dẫn clone của root `workspace` trong file do biến `WORKSPACE_CONFIG` trỏ tới; `git -C <clone> remote get-url origin`; `git -C <clone> config --get core.sshCommand`; **chỉ TÊN** (không giá trị) các biến `GIT_SSH*` trong môi trường container; nếu xác thực bằng khoá SSH → fingerprint như G1.4. Remote `https://` kèm token/PAT, hoặc khoá SSH gắn tài khoản người → **FAIL G1.5**.
- G1.6 Fingerprint ở G1.4 và G1.5 mỗi cái phải trùng một deploy key ở G1.3 có `read_only=false`. Deploy key ghi-được khác (không thuộc 2 cổng) không làm FAIL nhưng phải liệt kê trong KQ (mọi deploy key sẽ được miễn trừ).
- G1.7 Repo không có `.github/workflows` (xác nhận không có GitHub Actions phải đẩy lên).

## 3. Mutation duy nhất (chỉ khi G1 PASS toàn bộ)
`gh api -X POST repos/Huyen1974/incomex-workspace/rulesets --input -` với JSON:
```json
{"name":"gateway-only-writes","target":"branch","enforcement":"active",
 "conditions":{"ref_name":{"include":["~ALL"],"exclude":[]}},
 "rules":[{"type":"creation"},{"type":"update","parameters":{"update_allows_fetch_and_merge":false}},{"type":"deletion"},{"type":"non_fast_forward"}],
 "bypass_actors":[{"actor_id":null,"actor_type":"DeployKey","bypass_mode":"always"}]}
```
- API chỉ từ chối vì `actor_id` → thử lại **một lần** với `"actor_id":0`. Lỗi khác → ghi nguyên văn, DỪNG; không thử cấu hình khác.
- **Cấm** thêm vào miễn trừ bất kỳ vai trò (admin/maintain/write), người dùng hay app nào — làm vậy là mở lại lỗ.
- Không đụng branch protection cổ điển, không đổi bất kỳ setting GitHub nào khác.

## 4. Phép thử ngay sau khi bật
- **T1 · Đường người phải bị chặn:** `gh api -X PUT repos/Huyen1974/incomex-workspace/contents/work/mcp-workspace/COLLAB.md` với nội dung = bản hiện tại + **đúng một dòng cuối** `probe-native MCPW-LOCK-20260924-01` (không xoá/đổi gì khác) và `sha` hiện tại → PHẢI bị từ chối (ghi mã HTTP + thông điệp, ví dụ “Repository rule violations”). Nếu THÀNH CÔNG → FAIL T1: không sửa/xoá gì thêm, ghi KQ DỪNG.
- **T2 · Cổng `fs_*` vẫn ghi:** chính lần ghi khối KQ ở mục 6 bằng `fs_edit`/`fs_transaction` → push OK.
- **T3 · Cổng `workspace_*` vẫn ghi:** nếu phiên này bind `workspace_*` (Agent Data) → thêm một dòng `T3 workspace_* PASS <thời điểm UTC>` vào đúng khối KQ bằng `workspace_edit`. Không bind → ghi `T3 chưa thử — Host thử` (Host Claude Chat thử ngay sau).
- **Rollback — Owner đã duyệt trước, không cần hỏi:** T2 hoặc T3 thất bại vì push bị từ chối → `gh api -X PUT repos/Huyen1974/incomex-workspace/rulesets/<id>` đặt `"enforcement":"disabled"` (**không xoá** ruleset), rồi mới ghi KQ DỪNG bằng `fs_*`. T1 thất bại → để nguyên ruleset, KQ DỪNG.

## 5. Cấm
- In, copy, di chuyển, đổi khoá riêng/token/secret nào — chỉ fingerprint khoá công khai.
- Sửa bất cứ gì trên VPS, restart dịch vụ (ssh chỉ đọc).
- Tạo file mới trong repo; git push/commit trực tiếp; đổi setting GitHub nào ngoài ruleset này; xoá ruleset/nhánh/file.
- Sửa README/AGENTS — phần luật do Host sửa sau khi tự nghiệm thu.

## 6. Báo cáo — một khối trong `work/mcp-workspace/COLLAB.md`, mục `## KQ — MCPW-LOCK-20260924-01` (thêm cuối file)
- G1.1–G1.7: PASS/FAIL + số liệu (deploy key: id · title · read_only · fingerprint 16 ký tự đầu; cổng nào khớp key nào; deploy key ghi-được khác nếu có).
- Ruleset: id + JSON đã gửi. T1: mã HTTP + thông điệp. T2: commit. T3: kết quả. Rollback nếu có.
- Dòng cuối đúng khuôn máy đọc: `KQ@MCPW-LOCK-20260924-01 XONG` hoặc `KQ@MCPW-LOCK-20260924-01 DỪNG · <lý do một dòng>`.
- Trả Owner một dòng: `XONG` hoặc `DỪNG`.
