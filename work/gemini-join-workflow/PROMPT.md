# PROMPT — GJW-R1-ROUTE-MEASURE-20261017-01
RUN_ID: GJW-R1-ROUTE-MEASURE-20261017-01
Status: DRAFT — Claude Chat soạn theo Owner 17/10 (P29). Reviewer khác hãng (GPT Host) rà một lượt, READY đúng SHA commit cuối chạm tệp này. Thay PROMPT B1 (B1 Task Mode đã VERIFIED qua Codex, P24).
Task: work/gemini-join-workflow · Host: GPT Chat · Reviewer: Claude Chat · Executor: Claude Code CLI trên MacBook (SSH `contabo`) · AUTO0
LOẠI LƯỢT: **CHỈ ĐỌC.** Không sửa tệp, không reload/restart, không apply-v0, không giữ `VPS-GHI`. Lượt nhẹ: `nice`/`ionice`, không quét cả đĩa (DROOT54 d). Không đụng phần HJW (`hermes-config-yaml`, INV20).

## MỤC TIÊU
Owner 17/10: «không được để lại tình trạng lỗi, cả server bị ảnh hưởng»; «chỉ cần Gemini tham gia đầy đủ … hiện nay cũng đã có ghế và tham gia đầy đủ».
Hai đỏ của GJW đang làm Guard tổng FAIL cho MỌI việc (biên nhận Telegram của việc khác không gửi được):
1. INV24 `badkey=400` — INV24 (G1C-MAX 14/10) gọi `https://…/gemini-mcp/mcp` với `X-API-Key` sai, đòi **401**.
2. INV5_6 lệch Config Guard đích `nginx-route-gemini-mcp` (`/opt/incomex/docker/nginx/secrets/gemini-mcp-route.conf`).
Giả thuyết (JEV 0,87): ngày 15/10 khoảng 03:00–04:00Z, lúc gắn Gemini Chat (Spark custom app — chỉ nhận URL, không nhận header), có người sửa tệp route để thêm đường dẫn chứa khoá rồi reload nginx ngoài Config Guard. Gemini Chat đang chạy nhờ đường đó (commit `f0009df`) ⇒ lùi mù về baseline có thể làm Gemini Chat mất kết nối (JEV 0,79). Lượt này đo để quyết đúng, KHÔNG sửa.

## BÍ MẬT
Không in khoá, đường dẫn chứa khoá, nội dung `.env`. Khi cần so tệp: thay mọi chuỗi ≥16 ký tự `[A-Za-z0-9_-]` bằng `<SECRET-n>` (cùng chuỗi ⇒ cùng n) trước khi in. Curl chỉ in mã HTTP, header `Server`, 120 ký tự đầu thân lỗi, hoặc SỐ tool.

## S0 · Cửa (≤5')
Read-gate A6 (READY đúng SHA, không STOP, không STARTED treo). Ghi `STARTED@GJW-R1-ROUTE-MEASURE-20261017-01` dưới P30 (Claude Code tạo P30) qua gateway.

## S1 · Lệch là gì (≤10')
- Tìm trong registry Config Guard dòng `nginx-route-gemini-mcp`: nơi lưu baseline, sha baseline, sha live.
- So baseline ↔ live đã che bí mật (S-BÍ MẬT): dòng thêm/bớt, location nào, `proxy_set_header` nào, `return` nào.
- Trạng thái đích anh em `nginx-http-gemini-mcp` và 8 đích Gemini còn lại: MATCH hay không.
- `nginx -T` đang nạp có đúng bản live không (đã che).

## S2 · Ai, khi nào (≤10')
mtime/ctime tệp live; mốc nginx reload (log container nginx từ 14/10); log apply-v0 cho đích này; lần đầu drift-check báo MISMATCH; phiên SSH trong ±30' quanh mtime (user, IP nguồn, giờ — không in lệnh). Ghép với mốc: G1C-MAX (14/10), Codex S2b (15/10 ~03:00–04:00Z), Gemini Task Mode.

## S3 · Vì sao 400 (≤10')
Ma trận curl (không in khoá): A `/gemini-mcp/mcp` + khoá đúng → số tool · B + khoá sai → mã, `Server`, thân · C không khoá → mã · D đường chứa khoá (nếu có trong live) → số tool · E đường chứa khoá sai → mã. Xem log container `incomex-gemini-mcp` cùng phút để biết 400 do nginx hay ứng dụng.

## S4 · Phân loại + đề xuất lượt sửa R2 (KHÔNG làm)
Kết luận một trong: `INTENDED_S2B` (chỉ thêm đường cho Spark) · `UNINTENDED` · `MIXED`. Đề xuất R2 nhỏ nhất, đủ 4 điều: (a) Gemini Chat vẫn chạy (D = 23 tool); (b) đường header sai khoá trả lại 401; (c) Config Guard khớp qua apply-v0 với lý do ghi rõ, không rebaseline để che phần không chủ đích; (d) INV24 kiểm cả A–E và có phép thử hỏng. Nêu rollback.

## S5 · Dấu chân GJW còn trên máy (≤5')
Container `incomex-gemini-mcp` (health, RAM); 10 đích Config Guard của Gemini; dòng INV24 mới nhất; cron/timer nào của GJW. Mac: daemon `agy remote-control` còn chạy không; tệp `~/.local/share/gemini-incomex-mcp/mcp_config.json` (Codex P24) có trong canh vân tay không — chỉ báo.

## KẾT QUẢ (P30)
Mỗi bước một dòng tiến độ (DROOT54). Bảng S1–S5 + kết luận S4 + đề xuất R2. `KQ@GJW-R1-ROUTE-MEASURE-20261017-01 XONG|DỪNG` · `Dọn: tệp tạm đã xoá · 0 tiến trình nền` · `0 ghi VPS`.
