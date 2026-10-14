# PROMPT — GJW-G1C-MAX-20261014-01
RUN_ID: GJW-G1C-MAX-20261014-01
Status: DRAFT — Claude Chat P16 thay bản G1C `GJW-G1C-JEV-MAC-G2-COUNCIL-20261014-01` (READY a975a68 nhưng CHƯA STARTED, còn lệnh cấm trái HUMAN_DIRECTIVE-09/10 ⇒ huỷ, không chạy). GPT Host READY đúng SHA commit cuối chạm tệp này. Bước ⚑ chỉ chạy khi COLLAB có `HUMAN_DIRECTIVE@GJW-20261014-11 EFFECTIVE` (Owner gật Q03); không có ⇒ ghi BLOCKED(Owner) và đi tiếp.
Task: work/gemini-join-workflow · Host GPT Chat · Reviewer Claude Chat · Executor: Claude Code CLI trên MacBook (Terminal thường, HOME=/Users/nmhuyen) dựng; CHÍNH Gemini (`agy` + Gemini Mac) tự chứng minh · AUTO0.

## MỤC TIÊU — một lượt
Owner 14/10 22:18: «CẤM đặt ra bất cứ hạn chế nào, kết nối tối đa cho gemini để tận dụng khả năng tốt nhất của từng hãng.»
Đích: Gemini dùng được MỌI công cụ Claude và GPT đang dùng + MỌI khả năng riêng của Google. Mỗi khả năng kết thúc ở VERIFIED (một thao tác thật) hoặc BLOCKED (lỗi thật đúng tài khoản/app/thao tác, hoặc văn bản giới hạn của hãng). Không còn NOT_TESTED, không «N/A» tự đặt.

## LUẬT — chỉ luật chung, áp y như GPT/Claude
- Ghi repo qua gateway bằng `google-main`, có expected_version. Không `git push`.
- Thay đổi VPS: dòng `VPS-GHI` + Config Guard + rollback + đèn Guard trước/sau không xấu hơn. Không in bí mật vào chat/log/repo (repo CÔNG KHAI: không ghi nội dung email/tệp/lịch của Owner, chỉ ghi số lượng/ĐẠT).
- Ghi Directus/PG chỉ qua DOT (luật Owner cho mọi AI). Xoá dữ liệu, dừng dịch vụ đang chạy, phát sinh chi phí mới ⇒ cần Owner gật.
- Giới hạn của hãng khác: không cho bot vào claude.ai (điều khoản Anthropic).
- Ngoài các điều trên KHÔNG có cấm nào: Turbo/auto-approve, Terminal, SSH, quyền ngoài workspace, dịch vụ nền, Chrome, Gmail/Drive/Calendar, API/SDK đều được dùng và phải thử.

## ĐÃ CÓ — không làm lại
`google-main` trên agent-data (bộ tool như gpt-web) + KB = VERIFIED (P10, commit 24a965c). `agy` đăng nhập Keychain, ghim `gemini-3.8-flash-high`. Sao lưu `~/.gemini` cũ có INDEX.

## S0 · Kiểm cửa + kiểm kê (≤10')
Read-gate A6 (READY đúng SHA, không STOP, không STARTED treo). Ghi `STARTED@GJW-G1C-MAX-20261014-01` dưới P17 (Claude Code tạo P17). Lập danh sách ĐỦ: mọi connector/MCP mà Claude Chat, Claude Code (remote + local Mac) và GPT đang dùng; mọi khả năng Google của Antigravity/`agy`/Gemini Mac. Mỗi dòng: Gemini có chưa.

## S1 · Gắn những gì dùng chung — chỉ Mac (≤30')
1. JEV: path-secret chung `jev-mcp-path-secret` từ GSM (như Claude Code), thêm vào cấu hình `agy`.
2. Graph `graph-v1` (stdio qua ssh như Claude Code đang khai), Lark (cùng cách Claude/GPT đang nối; nếu cần danh tính ghi riêng thì làm như agent-data), mọi MCP khác Claude Code đang dùng trên Mac ⇒ khai cho `agy`. Directus: chỉ đúng phạm vi mà connector Claude đang có (`tac_*`), không dùng creds admin.
3. Gemini Mac (Task Mode, HOME `~/.gemini/users/user1`): khai cùng các MCP qua cấu hình/Connected Folders native. Quyền ngoài sandbox: mở đúng màn System Settings › Privacy & Security › Full Disk Access để Owner bật Gemini (một công tắc), rồi kiểm đọc được `~/.gemini`, `~/.ssh`.
4. Quyền Antigravity/`agy`: preset cao nhất (Turbo/auto-approve), Terminal/Network/Files/MCP/Web bật; danh sách chặn chỉ gồm đúng các luật chung ở trên. Ghi lại cài đặt.
5. Sao lưu mọi tệp cấu hình trước khi sửa, tệp chứa khoá 0600.

## S2 · Khả năng riêng của Google (≤30')
Chrome browser agent (hồ sơ Chrome riêng) · Google Drive / Gmail / Calendar / NotebookLM qua connector/MCP chính thức bằng tài khoản Owner (Owner bấm đồng ý khi Google hỏi) · Remote Control (`agy remote-control start`, Owner thấy trên điện thoại) · đường gọi vào Gemini: `agy -p` (đã có), trigger SDK, Gemini Tasks/theo dõi email nếu có · Gemini API: tạo khoá gói miễn phí nếu tạo được không cần billing (bật billing = Owner gật).

## S3 ⚑ · Cổng Incomex VPS ngang Claude (≤40', ghi giờ dự kiến trước khi làm)
Sự thật: `claude-mcp` chỉ nhận MỘT khoá, nhãn cố định `Anthropic/ClaudeAI` (`claude-mcp/app/server.py` dòng 37–39) ⇒ Gemini chưa có `query_pg`, `pg_schema`, `directus_*` (`tac_*`), gốc `code`/`ui`/`docs`, `ui_act`/`ui_screenshot`.
Chỉ khi có HUMAN_DIRECTIVE-11: sửa nhỏ nhất để nhãn + khoá đọc từ env (mặc định giữ y nguyên Anthropic); dựng THÊM một container cùng mã cho Google (khoá GSM mới, nhãn `gemini-agy [auth:google-main]`); thêm route path-secret cho Google ở nginx rồi reload. Container `claude-mcp` đang chạy KHÔNG đụng. Giữ `VPS-GHI`, Config Guard, mã nguồn đúng SSOT. Kiểm: connector Claude vẫn 23 tool + nhãn Anthropic; Google gọi được, khoá sai 401; rollback sẵn; trả `VPS-GHI` ngay sau bước này.

## S4 · Gemini tự chứng minh + phản biện (≤30')
Chạy `agy -p "Đọc mục SMOKE trong work/gemini-join-workflow/PROMPT.md và làm đúng." --output-format json`; Owner dán đúng câu đó một lần vào Gemini Mac. Lưu json (status, usage).

## SMOKE — phần Gemini đọc
Bạn là Gemini, ghế google-main. Với MỖI công cụ/kênh có trong cấu hình của bạn, làm MỘT thao tác chỉ đọc thật: repo đọc 5 dòng `AGENTS.md`; KB một câu; JEV một câu noul; Graph đếm nút; Lark liệt kê bảng; PG `SELECT 1`; Directus đọc 1 item `tac_*`; Drive/Gmail/Calendar đếm 3 mục (KHÔNG ghi nội dung); Chrome mở trang Owner view của task và chụp màn hình (không đưa ảnh lên repo); Remote Control status. Rồi thêm một P vào `work/gemini-join-workflow/COLLAB.md` (đọc version trước, ghi có expected_version): bề mặt (agy hoặc Gemini Mac), tên mô hình, giờ UTC, bảng khả năng VERIFIED/BLOCKED (lỗi nguyên văn), và một ý kiến phản biện độc lập về hướng G3 (Gemini làm người đưa thư) có tham khảo JEV. Không ghi gì khác.

## S5 · Bảo vệ + kết quả (≤10')
- Điều 30/31 cho mọi thứ đã chạm: hash cấu hình Mac + kiểm lúc gọi `agy`; Config Guard cho đích VPS mới (nếu S3 chạy). 6 danh tính cũ + connector Claude + Hermes vẫn sống.
- Báo từng bước `<RUN_ID> · bước k/6 · … · <UTC> · dự kiến xong <UTC>` (DROOT54).
- Đồ lượt này tạo: bản sao lưu cấu hình (giữ) · container + route Google nếu S3 chạy (giữ, có rollback) · tệp tạm `$TMPDIR/gjw-max-*` (xoá trước KQ) · dịch vụ nền Remote Control (giữ, ghi tên).
- `KQ@GJW-G1C-MAX-20261014-01 XONG|DỪNG` · `Dọn: …` · `VPS-GHI` đã trả.
XONG khi: bảng khả năng không còn NOT_TESTED; P của Gemini có tác giả `gemini-agy [auth:google-main]`; Claude/GPT/Hermes không bị ảnh hưởng.
Không làm trong lượt này: G3 (Gemini nhắc GPT/Claude vào việc) — chỉ chứng minh Chrome chạy được.
