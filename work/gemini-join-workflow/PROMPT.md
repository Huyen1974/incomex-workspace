# PROMPT — GJW-G1B-CLAUDE-SUPPORT-20261014-01
RUN_ID: GJW-G1B-CLAUDE-SUPPORT-20261014-01
Status: DRAFT · CHƯA READY / CHƯA RUN; Claude Chat Reviewer rà đúng SHA, GPT Host ghi READY theo A6, Owner chuyển cho Claude Code CLI.
Task: work/gemini-join-workflow
Host: GPT Chat · Reviewer: Claude Chat · Executor_Surface: Claude Code CLI trên MacBook Owner · Role: fallback đúng BC01–BC03; **Google Antigravity vẫn là executor chính G1** · AUTO0.
Write_Path: tài liệu repo chỉ qua gateway Incomex `fs_*`/`workspace_*` với expected_version; cấu hình local chỉ đúng file Antigravity thực dùng; VPS chỉ theo `VPS-GHI`/GSM/`incomex-config-apply-v0` nếu không restart và được guard. Cấm GitHub native/direct git push.

## Mục tiêu
Giải **đúng 3 blocker có bằng chứng** của G1 P07: BC02 cấu hình MCP/TCC Mac; BC03 xác thực `agy` qua cách chính thức; BC01 đăng ký danh tính Google riêng cho gateway nếu có đường no-restart, no-guard-regression. Tận dụng hệ thống sẵn có, **không tái thiết kế MCP/Gateway**. Hoàn tất Mac trước, **không chờ VPS-GHI**. Sau hỗ trợ, Antigravity tự gọi thật các tool và nghiệm thu G1.

## Read-gate & STEP_WALK (AGENTS A6, DROOT30/31/48/50/54)
- Đọc AGENTS.md → root COLLAB.md (`VPS-GHI`, Guard) → `work/gemini-join-workflow/COLLAB.md` (§0/Bảng/P07/C1–C7) → PROMPT này. Kiểm PROMPT last-touch, Reviewer ACCEPT cùng SHA và Host READY, G1 cũ đã KQ DỪNG, không có STARTED G1B, không STOP. Thiếu ⇒ DỪNG trước mutation.
- Khi pass, ghi `STARTED@GJW-G1B-CLAUDE-SUPPORT-20261014-01 <UTC> · executor=Claude Code CLI` qua gateway; từng bước ghi ngắn và cuối lượt `KQ@` XONG/DỪNG trong COLLAB. Không giữ terminal để chờ, không sửa PROMPT giữa lượt.

| Bước | Ai/trigger | Evidence/đích | Nếu lỗi | Bước sau |
|---|---|---|---|---|
| S0 | Claude Code, Owner giao khi READY | read-gate, versions, lock/Guard baseline và inventory metadata (chỉ đọc) | Ghi DỪNG, báo GPT Host | S1 |
| S1 BC02 | Claude Code sau S0 | client config thực dùng, before/after hash, agy mcp list, không phá legacy | ghi BLOCKED_CAPABILITY nhỏ nhất | S2 |
| S2 BC03 | Claude Code sau S0, không phụ thuộc BC01 | native OAuth login/Keychain, agy models + agy -p thật model Gemini | một thao tác Owner consent nếu cần; DỪNG sạch | S3 |
| S3 BC01 | Claude Code khi root `VPS-GHI: trống` và no-restart path đủ bằng chứng | Google identity riêng, gateway auth real + Guard same-or-better | không restart, báo delta còn thiếu | S4 |
| S4 | Claude Code sau các bước đo | KQ evidence + manifest dọn + giao lại Antigravity | GPT Host/Reviewer nhận KQ | Google tiếp tục G1 |

## S1 · BC02 — Môi trường Mac + MCP cấu hình đúng client
- Kiểm metadata `~/.ssh/config`, bốn file `~/.gemini` cũ, `HOME=~/.gemini/users/user1`, `~/.gemini/config/mcp_config.json` và `.agents/mcp_config.json` nếu hiện hữu, không hiển thị nội dung secret/token/private SSH key.
- Xác định `agy` 1.3.4/Gemini.app Task Mode đọc cấu hình MCP nào bằng **thử nghiệm thực**, ưu tiên công cụ native `agy mcp add/list` hoặc giao diện MCP Settings. Thêm chỉ những server đã audit; không viết song song hai HOME theo phỏng đoán, không tạo symlink chia sẻ credential, không bypass TCC/sandbox.
- Sao lưu file thực sửa và hash before/after, chỉ THÊM mục mới, giữ tất cả mục cũ không đổi; quyền file 0600 nếu chứa credential. Đăng ký endpoint `workspace_*`+KB, `fs_*`, JEV theo route/transport thực được kiểm tra; chưa có credential thì để trạng thái cấu hình `AUTH_NOT_READY`, tuyệt đối không điền khóa hãng khác.

## S2 · BC03 — OAuth agy official
- Theo tài liệu Google CLI: `agy` thử Apple Keychain silent authentication; nếu thiếu, chạy interactive auth/browser của chính CLI tại HOME/user được phép, người dùng chỉ bấm consent Google nếu bắt buộc. Không lấy/chép credential từ Gemini.app hoặc HOME khác, không in OAuth URL chứa token/code vào repo/log.
- Kiểm `agy models` trả danh sách mô hình thật, pin model họ Gemini và `agy -p <pointer-only> --output-format json|stream-json` chạy thật. Ghi version/model/method auth/trạng thái, không ghi thông tin tài khoản nhạy cảm.
- Không đổi provider, không kích hoạt Gemini API trả phí, không cài/upgrade/viết service/LaunchAgent.

## S3 · BC01 — Google identity gateway, chỉ nếu no-restart + VPS-GHI
- Đo lại root `VPS-GHI` tại thời điểm chạy. **VPSC trả 08:18Z nhưng TQT-P61 tiếp nhận từ 08:22Z**; không suy khóa đang rảnh. Nếu busy, bỏ VPS mutation, thực hiện Mac và KQ DỪNG với NEXT_TRIGGER rõ; không chờ đến giờ.
- Read-only xác định có OAuth/client registration ở đúng route hay không: 404 well-known ở vài URL chưa là bằng chứng toàn hệ không có OAuth. GET `/api/mcp` 200 chỉ là schema, không phải authenticated tool PASS.
- Từ `wtools.py`, `workspace-tools.json` và live process metadata, xác minh master_profiles + `credential_env` trong `os.environ`. Chỉ đọc **tên** env đã inject, không in value. Không thay key/profiles hiện hữu. Chỉ nhận Google profile khi có credential distinct với **slot chưa dùng thực**, hợp lệ ở process hiện hành, và không cần container restart/recreate/reload/code change; secret theo GSM/profile chính thức đã audit, rollback + guard.
- Có `VPS-GHI: trống` và no-restart path thật thì lấy khóa root qua gateway với expected_version, kiểm Guard before, áp config bằng cơ chế `incomex-config-apply-v0`, thử auth Google real, negative test quyền ngoài scope, check Guard after same-or-better rồi trả khóa trong cùng lượt. `fs_*`, `workspace_*`+KB, JEV có thể là route/credential riêng — **không nói PASS 4 cổng chỉ từ một đường**.
- Nếu thiếu slot riêng hoặc bắt buộc restart: BC01 = BLOCKED; ghi chính xác một đề nghị có scope, impact, rollback để Host/Owner duyệt lượt riêng. **Không tự restart container/nginx/compose, không tạo secret mà process không đọc**, không mượn master key của GPT/Claude/Hermes.

## Giới hạn, dọn và KQ
- Không ghi PG/Directus, sửa Graph/HJW/VPSC/TQT, tắt/khởi động Docker/nginx/cron/systemd, mở cổng public, sửa nguồn runtime/Guard; không quét/cleanup ổ, xóa/di chuyển 4 file `~/.gemini` cũ. Chỉ dọn temp/process **G1B tự tạo** có manifest; giữ backup cần phục hồi có INDEX/hash, 0 background processes. Không lộ token/key/header vào chat/repo/log.
- Đầu ra một mục KQ tại COLLAB (không tạo file mới): `BC01/02/03 | VERIFIED_LOCAL/PASS/BLOCKED | evidence | paths+hash | guard | rollback | NEXT_TRIGGER`, các dòng tiến độ DROOT54, `KQ@GJW-G1B-CLAUDE-SUPPORT-20261014-01 XONG|DỪNG`. Chỉ XONG khi có OAuth `agy` + config Mac đúng và identity Google authenticated thật; còn BC01 bị chặn thì DỪNG nhưng giữ thành quả local.
- Bàn giao Antigravity chạy lại authenticated G1 S1 (Google tự đọc repo, gateway write test, KB/JEV, headless). Không tự mở G2/G3, không biến Claude Code thành agent Google.
