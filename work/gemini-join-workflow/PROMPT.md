# PROMPT — GJW-B1-GEMINI-MAC-MCP-RUNTIME-20261015-01
RUN_ID: GJW-B1-GEMINI-MAC-MCP-RUNTIME-20261015-01
Status: DRAFT · Reviewer Claude Chat đã sửa thẳng theo P22 và ACCEPT commit last-touch; GPT Host READY; chưa RUN.
Task: work/gemini-join-workflow · Host GPT Chat · Reviewer Claude Chat · Executor_Surface: Claude Code CLI trên Mac · Đích xác nhận: **chính Gemini.app Task Mode** · Write_Path: gateway workspace_* expected_version cho COLLAB, local macOS/native Gemini UI/config có backup · 0 mutation VPS.
Owner: «Vấn đề là Gemini xác nhận nó chưa vào được. Phải xác định nguyên nhân tại sao Gemini lại chưa vào được.» Owner 15/10 09:13: «giống như GPT và claude, chúng ta phải thiết lập MCP server trên chính app (bằng tay) thì có thể mới chạy».

## CÁCH LÀM VIỆC VỚI OWNER (bắt buộc)
Mọi thao tác trong giao diện Gemini do Owner bấm. Claude Code mở sẵn đúng màn hình (`open -a Gemini`, `open https://gemini.google.com/apps`), rồi đưa Owner MỘT bước mỗi lần bằng tiếng Việt: bấm vào đâu (tên nút đúng như trên màn hình), thấy gì là đúng; Owner trả «xong» hoặc ảnh chụp. URL có bí mật: Claude Code chép thẳng vào clipboard (`pbcopy`), KHÔNG in ra màn hình/chat/repo; Owner chỉ dán.

## PRE FACTS
P19 commit b3dde68 do `gemini-agy [auth:google-main]` đã thử thành công bằng CLI `agy`. Gemini Mac hiện nói: file có 12 MCP nhưng phiên app chỉ có `git`, `obsidian`; `agent-data`, `incomex-vps` trả `Unknown MCP server`; thư mục/SSH bị `Operation not permitted`. Đừng chấm Gemini Mac PASS từ kết quả CLI, đừng đoán một nguyên nhân duy nhất, đừng chạy lại G1C-MAX hay sửa VPS.
Google MCP docs: https://antigravity.google/docs/mcp — Antigravity app Settings > Customizations > Installed MCP Servers (Enable, Refresh); CLI `/mcp` tool registry/log; `mcp_config.json` global/project.

## RUN B1 — đúng chỗ hỏng, một lượt
| Bước | Ai/khi nào | Ràng buộc | Bằng chứng / kết quả |
|---|---|---|---|
| S0 read-gate | Claude Code trước RUN | AGENTS → root COLLAB → task COLLAB/P20–P21 → PROMPT; ACCEPT+READY đúng SHA, không STOP/STARTED treo | Ghi STARTED, baseline 12 khai báo vs 2 nạp, không in secret. |
| S1 xác định runtime | Claude Code sau S0 | Chỉ đọc; đúng phiên Gemini Mac đang mở | Xác nhận Chat hay Task Mode, đăng nhập, HOME thực, file MCP mà app đọc (hash/schema/disabled), active project, Settings Installed MCP Servers, log init/load/registration; so với CLI `agy`. Chỉ xuất tên server/status; redaction URL JEV/khóa. |
| S2 Task Mode — đăng ký trong app | Owner bấm theo Claude Code, sau S1 | Backup rồi sửa **chỉ** nguyên nhân xác minh được | Gemini Mac › Settings (góc dưới trái) › Customizations › Installed MCP Servers: có 12 server chưa? Tắt ⇒ bật công tắc + Refresh; không có ⇒ bấm View raw config để lộ ĐÚNG tệp app đọc, Claude Code ghi vào tệp đó (ưu tiên `incomex-vps` + `agent-data`), Refresh, mở TASK MỚI. Phân biệt lỗi đăng ký và lỗi transport/auth; không rebuild gateway hay restart VPS. |
| S2b Gemini Spark — «Add a custom app» | Owner bấm theo Claude Code (độc lập S2) | Bản tương đương connector Claude.ai / Developer Mode ChatGPT; dùng route bí mật của `incomex-gemini-mcp` (23 tool, nhãn google-main) | Chrome › gemini.google.com › Settings & help › Connected Apps › Custom apps for Spark › Add a custom app › dán URL từ clipboard › Next › tích ô chấp nhận rủi ro › đặt tên «Incomex». Không thấy mục này ⇒ kiểm Keep Activity BẬT + ngôn ngữ English rồi thử lại; vẫn không có ⇒ `BLOCKED_BY_PROVIDER` (gói/quốc gia/tài khoản) kèm ảnh, không tìm đường vòng. |
| S3 thử thật trong Gemini Mac | **chính Gemini Mac** sau S2/S2b: Task Mode (S2) và chat thường với app «Incomex» (S2b, kể cả trên điện thoại nếu Owner tiện) | Tối thiểu 2 remote tool mỗi bề mặt, không dùng CLI thay | `agent-data.workspace_read` 5 dòng AGENTS GitHub SSOT và `incomex-vps.vps_status` read-only. Ghi tool result/identity và thời gian của **app**, không suy từ `HOME=user1 agy -p`. Nếu app không cung cấp tool, mã lỗi và danh sách loaded server thật. |
| S4 khoanh riêng folder/SSH | Claude Code nếu S3 PASS hoặc có lỗi riêng | Chỉ Mac; no VPS write | Nếu remote PASS nhưng local fail, kiểm Connected Folders, app TCC, PATH, SSH_AUTH_SOCK; cấp quyền native đúng nơi rồi thử `graph-v1`/folder. Kiểm Điều 30/31, backup/rollback, dọn mọi cờ/đồ. |

## PHÂN LOẠI & KQ
- `XONG` khi **chính app Gemini Mac** gọi được tool Incomex thật, có biên nhận: Task Mode (`agent-data` + `incomex-vps`) VÀ chat thường qua custom app «Incomex» — mỗi bề mặt VERIFIED hoặc BLOCKED có bằng chứng thật. `agy` HOME user1 chỉ là đối chứng, không đủ.
- `DỪNG · ROOT_CAUSE_FOUND` nếu đã xác định file/session/tool registration/TCC/auth lỗi gì nhưng app cần một thao tác Owner hoặc giới hạn nhà cung cấp; chỉ trả một bước cần Owner thực hiện (nếu bắt buộc).
- `DỪNG · ROOT_CAUSE_NOT_PROVEN` nếu chưa truy được trạng thái app: nêu chính xác dữ kiện còn thiếu, không công nhận PASS.
- Đừng làm lại JEV/Graph/Lark/agent-data trên VPS. Không xử lý Kuma, Directus DNS, Figma OAuth, xoay JEV. Không ép cấm capability Gemini; quyền native test theo Owner. Không xuất bí mật trong `agy mcp list`/log (đã từng lộ URL JEV ra Terminal). Không làm hỏng các config đang PASS.
- Kết thúc ghi đúng 1 P/KQ vào COLLAB bằng gateway expected_version, cho Gemini Mac tự ghi thêm P nếu thực sự có connector, với author `google-main`; dọn, 0 khóa/daemon mới. Không tự chốt G3.
