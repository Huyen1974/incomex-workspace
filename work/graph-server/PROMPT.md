# PROMPT — GS-R8C-MAC-CLIENT-FINAL-20261009-14

## 0. TRẠNG THÁI VÀ ĐÍCH (DRAFT — CHƯA READY/RUN)
RUN_ID: GS-R8C-MAC-CLIENT-FINAL-20261009-14
Task: `work/graph-server/` · **chỉ hoàn tất client Mac của R8**, không mở R9/task mới.
Executor: Claude Code CLI mới trên Mac; Owner dán thủ công khi Host READY đúng commit SHA.
Write_Path: Incomex MCP full all 2 `workspace_*` root `workspace` chỉ cho trạng thái Graph/root; HJW source registry **chỉ HJW Host/worker** xử lý ở lượt HJW riêng.
Status: DRAFT · cần Claude Reviewer exact-SHA ACCEPT → HJW source đăng ký xong + shared VPS free → GPT Host READY → Owner dán RUN. PROMPT này không tự kích hoạt.

Nguồn authority: Owner 09/10 chọn **GIỮ phần Graph VPS đạt**, P86 `KQ@GS-R8R2-PINS-GUARDED-MCP-20261009-13 DỪNG` tại đúng E7/E8. E1–E6/E4 phần VPS đã chứng minh: Graph 3.596 nút/6.823 cạnh giữ nguyên, Neo4j URL-blocklist, MCP 1.6.0 read-only, Guard đủ 5 tệp, B8 production 13/13, Telegram #165, 22/22 lúc P86. Claude Code và Codex đã đọc thử Graph; Mac user-scope entries được trả **nguyên byte PRE** vì INV20 `MAC_AHEAD` (#22 đỏ 09:05–09:20Z) khi thiếu sổ nguồn HJW. **Không dùng KQ DỪNG cũ làm KQ XONG, không đánh dấu R8 DONE trước client thật và Guard.**

Mục tiêu Owner vẫn là (1) Business Graph hữu hạn/có thể phát hiện quan hệ mới; (2) Graph × JEV; (3) official JEV skills; (4) Code Graph. R8 chỉ là agent read-path; R9 business refresh → R10 JEV shadow → R11 code coverage đứng sau R8. Không dùng RUN này để sửa vấn đề HJW false-slow-alert, disk/swap VPSC hoặc cài Hermes.

## 1. PHẠM VI ĐÓNG
**Chỉ được thay cấu hình MCP user-scope của hai client trên Mac**: Claude Code và Codex đúng ứng dụng thực tế đã test. Bản source connector HJW `graph-v1` phải được HJW ghi/duyệt **trước** Mac mutation. Không tự làm `dot-connector-sync promote`, không sửa `connectors.json` hay INV20/Config Guard HJW từ Graph RUN.

Server Neo4j/Graph ở trạng thái đã đạt là **READ-ONLY/IMMUTABLE CHO RUN NÀY**: không re-run E1–E6, không apply compose/pins, không recreate Neo4j, không touch 5 file Guard, code-ledger, registry, wrapper hoặc DB. Không gọi `rollback-r7.sh` hoặc `r8r2-apply.sh rollback` (vì giữ server theo Owner). Hỏng phía Mac chỉ lùi Mac client về PRE, bảo toàn VPS.

Command MCP hiện hữu cho cả hai client (xác minh `--help` và evidence trước ghi):
`ssh contabo /opt/incomex/graph-server/mcp-readonly-v1/bin/graph-v1 mcp`
stdio only; không public port, không secret vào argv/repo/log.

## 2. S0 — GATES TRƯỚC MỌI THAY ĐỔI MAC
1. Đọc `AGENTS.md` → root `COLLAB.md` → Graph Bảng/P84–P88/P86 KQ → Graph PROMPT active → HJW Bảng/handoff connector và kết quả thực tế. Exact Reviewer ACCEPT + Host READY **cùng PROMPT last-touch SHA mới**; RUN_ID mới duy nhất; không STOP/STARTED trùng, ghi STARTED/root busy atomically khi cần theo A6. Nếu shared mutation HJW/VPSC khác STARTED hoặc cần lệnh HJW chưa xong ⇒ KQ DỪNG trước mutation (không HOLD/chờ). HJW -03 có RUN riêng, không nhập chung.
2. **Bằng chứng nguồn HJW INV20:** HJW Host đã ghi KQ terminal `graph-v1` source registration/promote (theo chính CLI `dot-connector-sync --help` tại phiên chạy), sổ `connectors.json`/release đúng `graph-v1`, phục vụ **cả claude-code và codex**; Guard/fingerprint trạng thái nguồn không mismatch; cần explicit approved change receipt. Chỉ thấy bản nháp/handoff/READY, chưa có KQ ⇒ DỪNG. Không tự promote từ Graph.
3. READ-ONLY Graph production recheck: Neo4j service healthy, counts 3.596/6.823, `prod-v1/bin/graph-v1 status` và `watch --guard` PASS, native URL blocklist, wrapper SHA/Config Guard five-file baseline unchanged vs P86, small safe read MCP; `INV20`/đèn/Guard hiện hành không có lỗi mới do Graph. Nếu Graph server fail, DỪNG báo Host; **không rollback sản phẩm đã giữ**.
4. Trên Mac inspect `claude mcp --help` và Codex **đúng ChatGPT.app Codex 0.162 alpha đã thử P86 hoặc phiên tương đương có evidence**. CLI Homebrew Codex 0.133 trước đây không nhận config, không dùng để nghiệm thu; chưa xác định surface thực thì DỪNG. Xác định config user-scope/file path theo runtime help, 0 entry `graph-v1` cũ; backup byte nguyên vẹn + SHA cả hai trước mutation, xác định chính xác 2 diffs dự kiến. Không đụng Claude Desktop/Hermes plugin hoặc cấu hình hệ thống.

## 3. S1–S3 — REGISTERED SOURCE → MAC INSTALL → REAL READ
S1. Sau khi S0 PASS, cài đúng hai user-scope entries `graph-v1` qua lệnh/client config **được hỗ trợ trong runtime**, backup trước và không tạo duplicate. Không thêm connector khác hoặc token/server thứ hai; secret chỉ fetch bên VPS wrapper đã Guard bảo vệ.
S2. Từ Claude Code client THẬT và ChatGPT.app Codex client THẬT, xác minh MCP `get-schema` + `read-cypher` có, `write-cypher` KHÔNG có. Mỗi client phải chạy một schema read và ít nhất một câu Cypher bounded `LIMIT` đọc non-PII có chứng cứ trả về Graph production; đối chiếu count/edge không đổi. `codex exec` đóng stdin nếu dùng để xác minh, không chấm PASS bằng shell substitute/cached test P86.
S3. Ngay sau lần ghi Mac, chạy `dot-connector-sync status/fingerprint` bằng cú pháp `--help` đúng để INV20 ghi đúng sự đồng bộ Mac↔source; kiểm fresh Guard POST, #22 không bị đỏ, Config Guard CLEAN, không tạo cờ/nguồn lạ. Nếu INV20/MAC_AHEAD/MAC_BEHIND/#22 bất thường hoặc client thực không đọc được: **lùi NGAY đúng hai client files về PRE byte/SHA, cập nhật fingerprint để chứng minh Guard phục hồi và KQ DỪNG**, không giữ Mac config nửa vời, không sửa HJW Guard/registry. Nếu rollback Mac mà Guard chưa về CLEAN, báo Host/Owner ngay, không nói DONE.

## 4. NGHIỆM THU VÀ BÀN GIAO
R8 XONG **chỉ nếu**: (a) KQ HJW source registration được HJW Host nhận; (b) Claude Code và Codex/ChatGPT.app `graph-v1` entries thật user-scope vẫn còn; (c) cả hai MCP đọc schema + bounded Graph query thành công, tool catalogue KHÔNG write; (d) HJW INV20/fingerprint và Graph Guard/Đèn #22/Config Guard POST đạt; (e) Graph 3.596/6.823, 5-file baseline và URL denial vẫn nguyên; (f) scoped Mac rollback proof và receipt, no new lights. Nếu không ⇒ KQ DỪNG cùng chính node R8, **server production vẫn giữ**.
Residual `NATIVE_QUERY_LIMIT=UNKNOWN`, `HERMES_ENTRY=NOT_INSTALLED` giữ nguyên; không tự mở R9, JEV runtime hay code mutation. KQ terminal XONG|DỪNG, gỡ busy root cùng commit và đóng CLI (không hỏi Owner các chi tiết đã có authority, không giữ VPS để chờ).

Evidence mới: `/opt/incomex/work/graph-server/evidence/GS-R8C-MAC-CLIENT-FINAL-20261009-14/` hoặc evidence Mac local do worker chứng minh rồi chỉ ghi đường dẫn/sanitized summary vào Graph COLLAB. Không in secret, cấu hình nhạy cảm, URI chứa token, hoặc PII.
Final `KQ@GS-R8C-MAC-CLIENT-FINAL-20261009-14 XONG|DỪNG`; tiếp theo nếu XONG: Host + Claude review P86+KQ mới rồi quyết R9; nếu DỪNG: một NEXT_TRIGGER, không hẹn giờ/schedule tự động.
