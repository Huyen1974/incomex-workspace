# PROMPT — GJW-G1B-CLAUDE-SUPPORT-20261014-01
RUN_ID: GJW-G1B-CLAUDE-SUPPORT-20261014-01
Status: DRAFT — Reviewer Claude Chat sửa thẳng theo P08 (A6/DROOT53). GPT Host READY đúng SHA commit cuối chạm tệp này. Bước S2c (khởi động lại container) CHỈ chạy khi COLLAB việc này có dòng `HUMAN_DIRECTIVE@GJW-20261014-06 EFFECTIVE` (Owner gật Q02); không có ⇒ bỏ S2c, S2d.
Task: work/gemini-join-workflow · Host: GPT Chat · Reviewer: Claude Chat · Executor: Claude Code CLI trên MacBook Owner, Terminal thường, HOME=/Users/nmhuyen · AUTO0
Ghi repo: chỉ `fs_*`/`workspace_*` có expected_version. Cấm `git push`, cấm ghi bằng danh tính ghế khác.

## MỤC TIÊU — làm xong G1 trong MỘT lượt
Owner 14/10 15:44: «những gì nó không thể thì chúng ta làm giúp cho nhanh (giao claude code cli) để nhanh có thêm thành viên vào hội đồng làm việc. Nguyên tắc là kết nối tối đa, mức cao nhất có thể giống claude và gpt nhé.»
Dựng cho ghế Google đúng cách GPT/Codex/Claude Code đã có: một `master_profiles` riêng `google-main` trên agent-data (cùng bộ tool như gpt-web), KB, JEV; `agy` đăng nhập Google; rồi để CHÍNH Gemini (qua `agy -p`) tự gọi thử và tự ghi một P bằng danh tính Google. Không thiết kế lại gateway, không thêm cổng/bước ngoài danh sách này.

## Sự thật đã biết — không đo lại
- `agent_data/workspace_tools.py` (dòng ~210–249): `master_profiles` đọc từ `workspace-tools.json` mỗi request, nhưng khoá so với `os.environ[credential_env]` ⇒ thêm thành viên = thêm profile + thêm biến env + khởi động lại container agent-data một lần. Đây là cách gpt-web, codex, claude-code đã được thêm.
- Gemini.app Task Mode chạy sandbox `HOME=~/.gemini/users/user1`, bị macOS TCC chặn `~/.ssh`, `~/.gemini` ⇒ bề mặt ghế Google là `agy` ở Terminal thường (`/Applications/Gemini.app/Contents/Helpers/agy` 1.3.4 hoặc bản trên PATH). Task Mode không phải đường chính.
- `/.well-known/oauth-*` trả 404.

## S0 · Kiểm cửa (chỉ đọc, ≤10 phút)
- Read-gate A6: READY đúng SHA; không STOP; G1 đã có KQ DỪNG; không có STARTED G1B chưa KQ. Thiếu ⇒ DỪNG.
- Ghi `STARTED@GJW-G1B-CLAUDE-SUPPORT-20261014-01 <UTC> · executor=Claude Code CLI` dưới P09 (Claude Code tạo P09) qua gateway.
- Đo: đèn trước (`logs/bang-den.json`); dòng `VPS-GHI` root; RUN khác đang STARTED dùng agent-data; TÊN (không giá trị) các biến env đã nạp trong container agent-data; `MASTER_LABEL_RX`; jev-gw nhận khoá client thế nào (một khoá chung hay danh sách); 4 tệp `~/.gemini` cũ còn công cụ nào đọc.

## S1 · Mac (không phụ thuộc VPS)
1. `agy` đăng nhập Google: thử Keychain im lặng; không được thì chạy đăng nhập của chính `agy` ⇒ Owner bấm đồng ý Google đúng một lần (thao tác duy nhất của Owner). `agy models` ra danh sách; ghim mô hình họ Gemini mạnh nhất có; ghi có Argon hay không.
2. Sao lưu nguyên `~/.gemini/config/mcp_config.json`. Các mục Incomex mang khoá chết thay bằng mục mới: agent-data (`serverUrl` + header khoá google-main), JEV, KB nếu route riêng; mục không phải Incomex giữ nguyên; tệp 0600; khoá đọc từ GSM, không in. Ưu tiên `agy mcp add` nếu đặt được header; `agy mcp list` xác nhận.
3. Dọn Gemini cũ (Owner: «dọn dẹp lại mọi thứ cho chuẩn chỉ»): tệp `~/.gemini` chỉ phục vụ Gemini CLI đã ngừng ⇒ CHUYỂN, không xoá, vào `~/.gemini/_luu-tru-gjw-20261014/` kèm `INDEX.md` (tệp gì · vì sao · khôi phục thế nào). Tệp còn công cụ đọc ⇒ giữ nguyên. Không gỡ cài gói nào.

## S2 · Danh tính Google trên VPS
a. Root `VPS-GHI: trống` ⇒ ghi khoá cho RUN này (expected_version). Bận ⇒ xong S1, ghi KQ DỪNG · NEXT_TRIGGER=VPS_GHI_TRONG (lượt sau chạy lại chỉ S2–S4 với cùng READY), không ngồi chờ.
b. Tạo secret GSM mới cho google-main (đủ độ dài tối thiểu, không in). Thêm `master_profiles.google-main = {enabled: true, credential_env: <tên biến mới>, label: <khớp MASTER_LABEL_RX, ví dụ "gemini-agy [auth:google-main]">}` vào `workspace-tools.json` và biến env vào nguồn env của compose cho service agent-data — cả hai qua đường Config Guard chính thức (`incomex-config-apply-v0`), có `.pre` rollback.
c. (chỉ khi có HUMAN_DIRECTIVE-06) Trước: không RUN nào khác đang STARTED dùng agent-data; ghi một dòng báo trước dưới mục VPS-GHI ở COLLAB gốc. Khởi động lại RIÊNG service agent-data bằng compose (`up -d --no-deps <service>`), không đụng service khác. Sau: `/health` xanh; gpt-web, codex, claude-code, hermes vẫn xác thực (một lệnh đọc mỗi profile hoặc log xác thực); đèn trở về như trước (đỏ chớp vài phút lúc khởi động là dự kiến, ghi giờ).
d. JEV: jev-gw nhận danh sách khoá ⇒ thêm khoá Google cùng cách (khởi động lại jev-gw chỉ khi HUMAN_DIRECTIVE-06 nêu jev-gw). Chỉ một khoá chung ⇒ ghi PARITY_GAP + đề xuất, không mượn khoá.
e. Trả `VPS-GHI: trống` ngay sau c/d, cùng lượt.

## S3 · Gemini tự chứng minh (Claude Code chỉ bấm nút)
Chạy `agy -p "Đọc mục SMOKE trong work/gemini-join-workflow/PROMPT.md (GitHub, đúng SHA READY) và làm đúng." --output-format json` với mô hình đã ghim. Lưu json (status, model, usage). Bằng chứng chính: commit P10 có tác giả mang nhãn google-main. Thử âm: gọi gateway bằng khoá sai ⇒ bị từ chối.

## SMOKE — phần Gemini đọc
Bạn là Gemini, ghế google-main. Dùng MCP Incomex đã cấu hình, chỉ làm 4 việc: (1) `workspace_read` 5 dòng đầu `AGENTS.md`; (2) `search_knowledge` câu «hội đồng AI»; (3) JEV `evaluate` với state `{"x":"test"}`, câu hỏi noul «Is x equal to "test"?»; (4) thêm P10 ngay dưới `## Nhật ký P` của `work/gemini-join-workflow/COLLAB.md` (đọc version trước, ghi có expected_version): tên mô hình, kết quả 1–3 (đạt/lỗi thật), giờ UTC. Không làm gì khác.

## S4 · Kết quả (P09) — DROOT31/50/54
- Mỗi bước xong một dòng `<RUN_ID> · bước k/5 · <đã xong gì> · <UTC> · dự kiến xong <UTC>`.
- Bảng parity: GPT/Claude đang có → Google có chưa: agent-data (bộ tool như gpt-web) · KB · JEV · `fs_*` (route Anthropic ⇒ N/A, ghi lý do) · connector khác GPT/Claude đang dùng · Chrome (native Antigravity) · đưa thư (G3). Mỗi dòng VERIFIED | GAP + đề xuất.
- Hash trước/sau các tệp cấu hình; tên secret GSM (không giá trị); rollback; đèn trước/sau.
- Đồ lượt này tạo (DROOT54 c): bản sao lưu cấu hình Mac (giữ) · thư mục lưu trữ `~/.gemini/_luu-tru-gjw-20261014/` (giữ, có INDEX) · thư mục tạm `$TMPDIR/gjw-g1b-*` (xoá trước KQ) · `.pre` của apply-v0 (giữ). Không tiến trình nền, không cổng mở.
- `KQ@GJW-G1B-CLAUDE-SUPPORT-20261014-01 XONG|DỪNG` · `Dọn: <đã gỡ>/<đã tạo> · còn lại: …` · `VPS-GHI` đã trả.
XONG khi: `agy` đăng nhập + mô hình Gemini ghim · P10 có tác giả google-main · KB và JEV gọi thật (JEV GAP có đề xuất cũng được nếu jev-gw chỉ có khoá chung) · 4 profile cũ vẫn chạy · đèn không xấu hơn trước.
Không mở G2/G3; không đụng Graph/HJW/VPSC/TQT; không ghi PG/Directus; không in bí mật; không gỡ gói, không xoá tệp.
