# PROMPT — R03 · Sửa lớp lỗi #24 "tên sinh đôi" ở MỌI đường tạo tên, trước lần làm mới client cuối (không thêm tool, không đổi tên tool, không đổi input schema)

RUN_ID: R03-NAME-TWIN-REPAIR-20260920-01
Soạn: Claude Chat — gộp đề xuất repair của GPT (Owner chuyển 2026-09-20) + 3 lỗi cùng loại Claude tìm thêm từ mã. Trạng thái KHÔNG ghi ở file này: chỉ tin `READY@<full-sha>` trong COLLAB.md.
Chỉ chạy khi `work/mcp-workspace/COLLAB.md` có MỘT trong hai giấy phép, đúng full SHA commit cuối chạm file này: (a) `REVIEWED@` của Founder không soạn + Host `READY@`; hoặc (b) `OWNER_APPROVED@` (Owner override, COLLAB P09) — cộng lệnh RUN hợp lệ.
Bản PROMPT R03 đã chạy (MACHINE_DONE) là `7d0521916bbc9705eade326b3dcbb00c30f81c53`; đọc bằng `git show 7d05219:PROMPT.md` trong bản sao /tmp. Điều gì file này không nói thì theo bản đó (§1 luật schema, §2 cổng 29 dòng, §4 client, §6 cấm).

## 0. Trước khi làm
1. Clone repo công khai vào một thư mục /tmp mới; kiểm giấy phép (a) hoặc (b) ở trên, đủ 40 ký tự; không có hoặc lệch → DỪNG.
2. Đọc `AGENTS.md`, `work/mcp-workspace/COLLAB.md`, KB §13.11.1.
3. PL1–PL3 của P10 (đính chính 7159559) vẫn áp; riêng mốc healthy theo §4 dưới đây.
4. Mỗi lỗi: test ĐỎ trước (repo tạm), sửa, test XANH. Mọi commit dùng tiền tố `[Claude Code]`.

## 1. Vì sao có lượt này
Tầng máy R03 chưa xanh: dòng #24 được chấm PASS nhưng chỉ đo ở MỘT đường tạo tên (tạo tệp mới). D09 + #24 áp cho MỌI đường làm xuất hiện tên mới. Bốn lỗi cùng một loại:

| Mã | Phía | Lỗi | Bằng chứng |
|---|---|---|---|
| D1 | Claude | Đổi tên CHÍNH một tệp chỉ khác hoa-thường (`ban-sao.txt` → `Ban-Sao.txt`) bị từ chối `name_collision_case`: `_nfc_guard` (claude-mcp/app/fsroots.py) không biết đâu là nguồn nên coi chính nguồn là bản sinh đôi. Cũng chặn luôn đổi tên NFD → NFC chủ động. Áp cho fs_move và op move của fs_transaction | gọi thật 2 lần từ Claude Chat, 2026-09-20 |
| D2 | GPT | `name_twin` chỉ được gọi ở write_new (workspace_tools.py ~872) và op write-new của transaction (workspace_operations.py ~224). Copy/move tệp và thư mục (`move_noreplace`, `expand_directories`), op copy/move của transaction, `workspace_import_file`, commit upload (workspace_transfer.py) KHÔNG kiểm ⇒ tạo được bản sinh đôi | đọc mã |
| D3 | cả hai | Chỉ kiểm tên LÁ trong thư mục cha ĐÃ CÓ: `_nfc_guard` return khi cha chưa có (fsroots.py ~660); `name_twin` return khi listdir lỗi. Thư mục cha tự sinh (G1) không bao giờ được kiểm ⇒ đã có `cay/` vẫn tạo được `Cay/x.txt` (thư mục sinh đôi) | đọc mã |
| D4 | Claude | op `write` tạo tệp MỚI trong `fs_transaction` (fsroots.py ~2185) không gọi `_nfc_guard`, trong khi fs_write, copy, move đều gọi | đọc mã |

D2–D4 cố ý chưa gọi thật từ chat: gọi thành công là tạo đúng bản sinh đôi trên repo công khai. Agent chứng minh bằng test đỏ trong repo tạm trước, rồi mới smoke sống.

## 2. Luật đúng — một câu, áp mọi nơi, hai phía như nhau
Mọi thao tác làm xuất hiện một tên mới trong gốc Git SSOT (tệp hay thư mục, KỂ CẢ thư mục cha tự sinh) phải so TỪNG thành phần mới của path với tên anh em trong cùng thư mục: trùng NFC mà khác byte, hoặc chỉ khác hoa-thường ⇒ từ chối, nêu tên đang có, không ghi gì. Ngoại lệ DUY NHẤT: thao tác MOVE (fs_move, workspace_move, op move của transaction, move ngược trong restore) bỏ qua đúng một tên — tên của chính nguồn trong thư mục cha của nguồn — nên tự đổi tên hoa-thường hoặc NFD → NFC được phép. COPY không bao giờ bỏ qua nguồn (nguồn còn nguyên ⇒ thành sinh đôi). Không tự normalize, không tự đổi tên, không đổi byte tên có sẵn. Hàm kiểm dùng chung cho mọi gốc ghi; nghiệm thu trên Git SSOT (Claude `gh`, GPT `workspace`), `ui` = N/A(D08).

## 3. Việc phải làm
1. **Liệt kê đường tạo tên từ MÃ, không từ trí nhớ**: grep mọi chỗ rename / makedirs / ghi tệp mới / write_blob ở cả hai đầu nối + trợ lý host. Lập bảng `entry point × {#24 sinh đôi mọi thành phần path, #23 path nguy hiểm, #10 bắt version khi thay tệp có sẵn, #25 chỉ text UTF-8 + quét bí mật}`; mỗi ô có test hoặc dòng mã làm bằng chứng. Ô #24 FAIL → sửa. Ô khác FAIL → sửa nếu chỉ cần backend; cần đổi schema → không sửa, DỪNG, ghi KB.
2. **Test đỏ** (repo tạm, cả hai phía), tối thiểu:
   - (a) move tệp tự đổi hoa-thường `ban-sao.txt` → `Ban-Sao.txt` ⇒ được; (b) move THƯ MỤC tự đổi hoa-thường `thu-muc/` → `Thu-Muc/` ⇒ được; (c) move tự đổi NFD → NFC ⇒ được.
   - (d) move sang tên sinh đôi của một tệp KHÁC ⇒ từ chối; (e) COPY `ban-sao.txt` → `Ban-Sao.txt` ⇒ từ chối (đối chứng âm: copy không được bỏ qua nguồn).
   - (f) tạo / copy / move / import / upload / op transaction vào `Cay/x.txt` khi đã có `cay/` ⇒ từ chối; tương tự thư mục khác nhau chỉ ở NFD/NFC.
   - (g) op write tạo tệp mới sinh đôi trong transaction ⇒ từ chối; (h) op move trong transaction tự đổi hoa-thường ⇒ được.
   - (i) gọi lại ca (a) cùng `operation_id` ⇒ REPLAY, không commit thứ hai; (j) mọi ca từ chối: HEAD, cây làm việc, journal y nguyên, không thư mục ma.
3. **Sửa**: chỉ hàm kiểm + chỗ gọi. Không đổi tên tool, không đổi input schema. Mô tả tool chỉ sửa nếu đang nói sai (client chưa làm mới nên sửa mô tả lúc này không tốn thêm lần làm mới); báo đúng thực tế.
4. `run_acceptance.py` hai phía + toàn bộ ca mới ⇒ PASS.

## 4. Deploy lần hai — chỉ cho đúng lượt này
READY của file này là sự cho phép thay câu "Không deploy lần hai trong R03" của bản 7d05219, CHỈ cho lượt này. Gắn tag rollback mới cho image đang chạy mỗi bên (theo §13.11.1 là `claude-mcp-local:r03-20260920` và `agent-data-r03:20260920-lifecycle`; kiểm lại bằng docker inspect). Chỉ deploy bên có đổi mã (+ trợ lý host nếu đổi, đúng điều kiện PL2). Mốc healthy: ≤ 180 s tính từ `State.StartedAt` tới `Health.Status=healthy` (docker inspect/events, không tính thời gian build); ghi cả cấu hình healthcheck thật của từng container. Quá mốc → hoàn nguyên về tag rollback và DỪNG, không tự quyết "gần đủ". Sau deploy chạy lại `run_acceptance.py` hai bên ⇒ PASS.

## 5. Smoke sống sau deploy (chỉ trong `work/mcp-workspace/_thu-nghiem/R03/`, qua chính hai đầu nối)
Chỉ chạy khi test đơn vị đã xanh. Claude `fs_move` `_thu-nghiem/R03/ban-sao.txt` → `_thu-nghiem/R03/Ban-Sao.txt` ⇒ được; GPT `workspace_move` một tệp tương tự do chính GPT tạo ⇒ được; mỗi phía ít nhất một ca từ chối thuộc D2/D3/D4 ⇒ từ chối, không tạo gì. Lỡ tạo ra bản sinh đôi ⇒ FAIL, DỪNG, KHÔNG xoá (xoá là quyền Owner).

## 6. Báo cáo — ghi TRƯỚC khi trả Owner
KB §13.11.2 (nối tiếp, không sửa §13.11.1): bảng entry point, đỏ → xanh, deploy (thời gian healthy từng container), cập nhật các dòng bảng 29 bị chạm (#8, #11–#15, #17, #18, #24, #28) và cờ:
`TOOL_LIST_CHANGED=NO` · `TOOL_INPUT_SCHEMA_CHANGED=NO` (lượt này) · `TOOL_METADATA_CHANGED=<thực tế>` · build-id/vân tay mới · `CLIENT_REBIND_REQUIRED=YES` (do đợt R03, CHƯA làm).
Trả Owner đúng một dòng: `R03-NAME-TWIN-REPAIR-20260920-01: MACHINE_DONE — chờ tạo/connect client mới một lần · KB §13.11.2` hoặc `R03-NAME-TWIN-REPAIR-20260920-01: DỪNG ở <mã> — lý do ở KB §13.11.2`.

## 7. Cấm
Như §6 bản 7d05219. Thêm: không tạo/connect/reconnect bất kỳ client nào; không sửa `AGENTS.md`, `README.md`, `work/mcp-workspace/COLLAB.md`, `work/mcp-workspace/PROMPT.md`, `work/mcp-workspace/DANH-MUC-CONG-CU.md`; không dọn `work/mcp-workspace/_thu-nghiem/`; không mở rộng ngoài §2–§3. Gặp gì ngoài dự kiến → DỪNG, ghi KB.

## 8. Sau Agent (không phải việc của Agent)
Chỉ khi Agent đã `MACHINE_DONE` và backend/build không còn thay đổi:
1. **ChatGPT Pro của Owner:** không có Refresh app. Tạo đúng **một MCP app mới** từ MCP server Full All hiện hữu; không đổi URL/auth/secret. Scan Tools trước Connect; đối chiếu tool list, input schema, metadata/build và 29 capability trong `work/mcp-workspace/DANH-MUC-CONG-CU.md`. Thiếu/sai bất kỳ mục nào thì DỪNG trước Connect và sửa ở server, không tạo app nối tiếp.
2. Owner Connect app mới bằng tay. Giữ app cũ làm rollback cho tới khi app mới PASS. GPT Chat + GPT Work phải mở phiên mới trên app mới. Claude reconnect connector và mở phiên mới; Claude Code mở phiên mới sau repair.
3. Nghiệm thu cùng một bài 9 bước tại `work/mcp-workspace/_thu-nghiem/R03/<surface>/`: tạo tệp lồng → replace_all có expected_count → copy thư mục → move thư mục kèm tree/version guard → diff hai phiên bản → đọc ref cũ → restore commit replace_all → tự đổi tên hoa-thường phải được → copy sang tên sinh đôi phải bị từ chối. Chạy trên GPT Chat, GPT Work, Claude Chat, Claude Code.
4. VPS: cả GPT và Claude ghi → sửa → đọc lại thật tại root `ui`, path `_thu-nghiem/R03/`, rồi một ca CROSS hai chiều. Không chạm mã/runtime VPS.
PASS toàn bộ mới đóng R03; lỗi độc lập ngoài phạm vi ghi nợ, không mở thêm capability trong R03.
