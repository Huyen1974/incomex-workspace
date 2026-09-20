# PROMPT — R03 · Lượt đóng cuối: vá nốt các lỗ còn lại + đồng bộ image = mã, rồi đóng băng backend trước khi tạo/connect client một lần

RUN_ID: R03-FINAL-CLOSE-20260920-01
Soạn: Claude Chat, sau khi tự kiểm MACHINE_DONE của R03-NAME-TWIN-REPAIR-20260920-01 (KB §13.11.2). Owner giao 2026-09-20: "còn gì nữa giao Claude Code xử lý 1 lần để đóng việc này; công cụ phải làm được việc". Trạng thái KHÔNG ghi ở file này: chỉ tin giấy phép trong `work/mcp-workspace/COLLAB.md`.
Chỉ chạy khi `work/mcp-workspace/COLLAB.md` có `REVIEWED@` của Founder không soạn + Host `READY@` (hoặc `OWNER_APPROVED@`) đúng full SHA commit cuối chạm file này, cộng lệnh RUN hợp lệ kèm commit của giấy phép.
Luật nền giữ nguyên, đọc bằng `git show` trong bản sao /tmp: §1 luật schema + §6 cấm của `7d05219:PROMPT.md`; §2 luật tên sinh đôi của `8114352:PROMPT.md`.

## 0. Trước khi làm
1. Clone repo công khai vào /tmp mới; kiểm giấy phép đủ 40 ký tự; không có hoặc lệch → DỪNG.
2. Đọc `AGENTS.md`, `work/mcp-workspace/COLLAB.md`, KB §13.11.1 + §13.11.2 (mục F là nguồn của lượt này).
3. PL1–PL3 của P10 (đính chính 7159559) vẫn áp. Test ĐỎ trước, XANH sau. MỌI commit, kể cả commit smoke trên workspace, có tiền tố `[Claude Code]` (lượt trước 3 commit smoke thiếu).
4. Mọi path thử: `work/mcp-workspace/_thu-nghiem/R03/`; không tạo gì ở root.

## 1. Đúng 4 việc, không hơn

| Mã | Việc | Xong khi |
|---|---|---|
| E1 (F.3) | **Image = mã.** Với MỌI module Python hai container `claude-mcp` và `agent-data` thực chạy, so byte giữa tệp TRONG container và tệp ở commit HEAD của repo mã tương ứng. Lập bảng tệp × {giống · image cũ hơn HEAD · cây làm việc có thay đổi CHƯA commit}. Tệp của hai đầu nối đã commit mà image chưa có (ví dụ `workspace_transfer.py` mang G4, đã chấm 🟢 ở §13.11.1 nhưng production chưa từng có) → đưa vào overlay nếu toàn bộ test hai phía xanh với nó. Thay đổi CHƯA commit, hoặc module ngoài hai đầu nối (KB…) → KHÔNG deploy, chỉ ghi. | Trong phạm vi hai đầu nối không còn dòng "image cũ hơn HEAD"; G4 chạy thật |
| E2 (F.1) | **Restore (#28) không được sinh tên sinh đôi**, cả hai phía: trợ lý `act_gh_revert_commit_push` + GPT `restore_transaction` so mọi tên thêm/đổi (`git diff --cached --name-status -M`) với cây ở HEAD theo luật §2 bản 8114352 (ngoại lệ duy nhất: nguồn của rename ngược); `archive_dir` đi qua cùng cổng, bỏ `os.makedirs` trần. Dùng lại ca đỏ đã soạn rồi rút ra ở lượt trước. | Ca đỏ → xanh cả hai phía; #28 sạch #24 |
| E3 (F.2) | `workspace_upload_begin` kiểm sinh đôi ngay ở `begin` (cùng hàm `name_twin`), không đợi tới `commit` | Begin vào tên sinh đôi ⇒ từ chối trước khi nhận byte |
| E4 (F.4) | **Mốc kiểm cấu hình.** Sau deploy ở §3, so baseline `/var/lib/incomex-config-guard-v0/baseline/` với cấu hình thật, liệt kê từng dòng lệch. Nếu MỌI dòng lệch chỉ là dòng image/build của các lần deploy R02–R03 và lượt này → sao lưu baseline cũ ngay cạnh nó, bless lại, `incomex-config-drift-check` về MATCH. Có bất kỳ dòng lệch nào khác → KHÔNG bless, dừng riêng mục này, ghi KB (không chặn E1–E3). | Drift-check MATCH toàn bộ; baseline cũ còn bản sao |

Owner đã quyết (2026-09-20) việc bless E4 trong đúng điều kiện trên; ngoài điều kiện đó Agent không tự quyết.

## 2. Giữ nguyên
Không thêm/đổi tên tool, không đổi input schema: vân tay Claude `4f1000e9aad3` và hash GPT `dbbfc590a969` phải giữ nguyên, đổi ⇒ DỪNG trước deploy. Mô tả tool chỉ sửa nếu đang nói sai. Không tạo/connect/reconnect client. Không sửa `AGENTS.md`, `README.md`, `COLLAB.md` (gốc và `work/mcp-workspace/`), `PROMPT.md`, `DANH-MUC-CONG-CU.md`. Không dọn `_thu-nghiem/`, không xoá gì (5 tệp `.payload` mồ côi trong `queue/in`: để nguyên).

## 3. Deploy — lần cuối của R03
Tag rollback = image đang chạy (theo §13.11.2: `claude-mcp-local:r03-nametwin-20260920`, `agent-data-r03:20260920-nametwin`; kiểm bằng docker inspect). Deploy bên có đổi (+ trợ lý host nếu E2 đổi nó, đúng điều kiện PL2). Healthy ≤ 180 s tính từ `State.StartedAt`; quá → rollback + DỪNG. Sau deploy: `run_acceptance.py` hai bên PASS + toàn bộ hồi quy hai bên + bảng E1 chạy lại trên image MỚI (trong phạm vi đầu nối phải toàn "giống"). E4 chạy SAU deploy để baseline gồm cả lượt này.

## 4. Smoke sống (qua chính hai đầu nối, trong `work/mcp-workspace/_thu-nghiem/R03/`)
Mỗi phía: restore một commit đổi tên khi tên cũ đã có bản khác hoa-thường ⇒ từ chối, không ghi gì; một restore bình thường ⇒ được. GPT: `upload_begin` vào tên sinh đôi ⇒ từ chối; `upload_begin` cùng `operation_id` sau khi đã commit ⇒ REPLAY, không `FILE_EXISTS` (G4). Lỡ tạo bản sinh đôi ⇒ FAIL, DỪNG, không xoá.

## 5. Báo cáo — KB §13.11.3, ghi TRƯỚC khi trả Owner
Bảng E1 (trước/sau), đỏ → xanh E2/E3, deploy (healthy từng container), E4 (từng dòng lệch, bless hay không), cập nhật dòng #18/#21/#24/#28 và cờ: `TOOL_LIST_CHANGED=NO` · `TOOL_INPUT_SCHEMA_CHANGED=NO` · `TOOL_METADATA_CHANGED=<thực tế>` · build-id mới · vân tay/hash.
Trả Owner đúng một dòng: `R03-FINAL-CLOSE-20260920-01: MACHINE_DONE — backend đóng băng, chờ tạo/connect client một lần · KB §13.11.3` hoặc `R03-FINAL-CLOSE-20260920-01: DỪNG ở <mã> — lý do ở KB §13.11.3`.
Từ MACHINE_DONE: backend R03 ĐÓNG BĂNG, không deploy gì nữa (trừ rollback) cho tới khi nghiệm thu client xong.

## 6. Sau Agent (không phải việc của Agent)
Chỉ khi Agent đã `MACHINE_DONE` và backend đã đóng băng:
1. **ChatGPT Pro của Owner:** không có Refresh app. Tạo đúng **một MCP app mới** từ MCP server Full All hiện hữu; không đổi URL/auth/secret. Scan Tools trước Connect; đối chiếu tool list, input schema, metadata/build và 29 capability trong `work/mcp-workspace/DANH-MUC-CONG-CU.md`. Thiếu/sai bất kỳ mục nào thì DỪNG trước Connect và sửa ở server, không tạo app nối tiếp.
2. Owner Connect app mới bằng tay. Giữ app cũ làm rollback tới khi app mới PASS. GPT Chat + GPT Work mở phiên mới trên app mới. Claude ngắt/kết nối lại connector và mở chat mới; Claude Code mở phiên MỚI (phiên đã chạy repair giữ danh sách tool cũ).
3. Nghiệm thu cùng một bài 9 bước tại `work/mcp-workspace/_thu-nghiem/R03/<surface>/`: tạo tệp lồng → replace_all có expected_count → copy thư mục → move thư mục kèm tree/version guard → diff hai phiên bản → đọc ref cũ → restore commit replace_all → tự đổi tên hoa-thường phải được → copy sang tên sinh đôi phải bị từ chối. Chạy trên GPT Chat, GPT Work, Claude Chat, Claude Code.
4. VPS: cả GPT và Claude ghi → sửa → đọc lại thật tại root `ui`, path `_thu-nghiem/R03/`, rồi một ca CROSS hai chiều. Không chạm mã/runtime VPS.
5. PASS toàn bộ → Host cập nhật `DANH-MUC-CONG-CU.md` §2 về kết quả cuối (bảng hiện vẫn là bản trước R03) rồi đóng R03. Lỗi độc lập ngoài phạm vi ghi nợ, không mở thêm capability trong R03.
