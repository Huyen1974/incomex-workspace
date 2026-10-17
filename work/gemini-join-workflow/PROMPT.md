# PROMPT — GJW-R2-CLOSE-HOLE-20261017-01
RUN_ID: GJW-R2-CLOSE-HOLE-20261017-01
Status: DRAFT — Claude Chat P32. Read-gate: READY của Host GPT đúng SHA commit cuối chạm tệp này. Nếu Host không ghi được repo: chạy khi COLLAB có `HUMAN_DIRECTIVE@GJW-20261017-18` do executor ghi NGUYÊN VĂN câu Owner cho chạy khẩn (SAFETY, AGENTS dòng 117). Bước S3 chỉ chạy khi COLLAB có Owner GẬT Q04.
Task: work/gemini-join-workflow · Host GPT Chat · Reviewer Claude Chat · Executor Claude Code CLI trên Mac (SSH `contabo`) · AUTO0 · chuông `COUNCIL_ALERT@GJW-20261017-01` SAFETY đang mở.

## MỤC TIÊU
Owner 17/10: «Chúng ta từ bỏ chuyện VPS gọi vào Gemini … Giờ cần VPS kín kẽ và không lỗi. Không để lại vấn đề cho VPS và các chương trình khác.»
Đóng lỗ hở cổng Gemini (P31 S3), xanh phần GJW của đèn #22, dọn dấu chân thừa. KHÔNG mở đường bí mật mới cho Gemini Chat (Owner chấp nhận Gemini Chat mất kết nối VPS). agy · Gemini Mac · Task Mode tự gửi header nên vẫn chạy.

## LUẬT LƯỢT NÀY
Giữ `VPS-GHI` đúng luật gốc, trả ngay khi xong. Mọi thay đổi VPS qua `incomex-config-apply-v0`, có `.pre`. Không in khoá/đường chứa khoá. Không đụng HJW (`hermes-config-yaml`, INV20), route GPT/Claude/Hermes, `mcpw-protection-guard`. Không xoá tệp (chỉ chuyển vào hồ sơ có INDEX). Không restart container nào ngoài `incomex-gemini-mcp` ở S3.

## S0 · Cửa (≤5')
Read-gate trên. `VPS-GHI` trống ⇒ giữ; bận ⇒ KQ DỪNG · NEXT_TRIGGER=VPS_GHI_TRONG. Guard PRE (đèn, INV24, INV5_6). Ghi STARTED dưới P33.

## S1 · Đóng lỗ hở (≤10')
apply-v0 đích `nginx-route-gemini-mcp` về ĐÚNG baseline `a1a8f251…` (đã nghiệm thu G1C-MAX; bỏ dòng nginx tự chèn khoá; log bật lại như baseline). Lý do apply-v0: «R2 GJW: lùi sửa tay Codex 15/10 03:52Z — đóng lỗi an toàn; không rebaseline bản 15/10». `nginx -t` rồi reload qua post_action. Không sửa tệp nào khác ở bước này.

## S2 · Kiểm cổng (≤10')
Khuôn đầy đủ (initialize → mcp-session-id): không header = 401 · header sai = 401 · header đúng = 23 tool. Khuôn INV24 cũ (không phiên, khoá sai) = 401. Chạy INV24 thật = PASS. drift-check: 10/10 đích Gemini MATCH. Connector GPT/Claude/Hermes giữ như PRE.

## S3 · Xoay khoá cổng Gemini — chỉ khi Owner GẬT Q04 (≤15')
Khoá `MCP_KEY_GEMINI_VPS` đã bị chép vào tệp route 15/10 và có thể nằm trong transcript Codex. Tạo phiên bản GSM mới (không in) → cập nhật `.env` của `incomex-gemini-mcp` qua apply-v0 → khởi động lại RIÊNG container này → cập nhật khoá trong cấu hình Mac của agy, Task Mode (`~/.local/share/gemini-incomex-mcp/mcp_config.json`), Gemini Mac (sao lưu trước, 0600). Kiểm: khoá cũ = 401, khoá mới = 23 tool; INV24 PASS. Không có Q04 ⇒ bỏ S3, ghi lý do.

## S4 · Dọn + Điều 30/31 (≤10')
- Bản sao Codex `gemini-mcp-route.conf.bak-gjw-20261015-035214-475520` CHUYỂN vào `/opt/incomex/work/gemini-join-workflow/evidence/` (root 600) + một dòng INDEX.
- Mac: dừng và gỡ nạp LaunchAgent `com.google.antigravity-cli-daemon` (`agy remote-control`) — hướng gọi vào Gemini đã bỏ; giữ tệp plist, ghi cách bật lại.
- Phép thử hỏng trên BẢN SAO: route kiểu 15/10 (nginx chèn khoá) ⇒ drift-check MISMATCH và INV24 khuôn cũ FAIL; bản thật PASS.
- Guard POST: footprint đúng các mục đã chạm; same_or_better so PRE.

## S5 · Rà dấu vết (chỉ đọc, ≤10')
Audit container `incomex-gemini-mcp` từ 15/10 03:52Z tới lúc đóng: đếm theo TÊN tool × nguồn; mọi `directus_*` ghi và `query_pg` liệt kê (nguồn, giờ, bảng — không in dữ liệu). Commit tác giả `gemini-agy [auth:google-main]` từ 15/10 03:53Z (kỳ vọng `f0009df` + 5 vào TQT proposals). Thấy nguồn lạ hoặc ghi lạ ⇒ báo Owner, không tự xử lý.

## KẾT QUẢ (P33)
Tiến độ từng bước (DROOT54). `KQ@GJW-R2-CLOSE-HOLE-20261017-01 XONG|DỪNG` · Dọn · trả `VPS-GHI`. XONG khi: S2 đủ 401/401/23 · INV24 PASS · 10/10 Gemini MATCH · S5 không có gì lạ · đèn không xấu hơn PRE. Ghi «R2 PASS» để Reviewer Claude xác nhận bằng chứng và Host đóng chuông.
Rollback: chỉ khi `nginx -t`/reload hỏng ⇒ `.pre` của apply-v0; known-good = baseline `a1a8f251`; tuyệt đối không quay về bản 15/10.
