# PROMPT — ACK N0 VERIFY-GAPS: XÁC MINH CỔNG HỘI ĐỒNG CHUNG TRÊN HỆ ĐÃ CÓ (CHỈ ĐỌC)
RUN_ID: ACK-N0-VERIFY-GAPS-20261028-03
Trạng thái: CANONICAL; thay N0 GAP-ONLY -02. Chỉ thi hành khi `COLLAB.md` có READY@full last-touch SHA của PROMPT này do GPT Host ký và Owner dispatch thủ công (AUTO0). Không tự gọi Agent hoặc giữ phiên chờ.
Executor_Surface: **Codex Desktop/CLI trên Mac**, ghế `openai-codex` (Worker N0), KHÔNG phải Reviewer của KQ mình.
Review_After_KQ: **Claude Chat (Anthropic)** độc lập khác hãng với Host GPT và Worker Codex; Host GPT nghiệm thu/chốt bước.
Root: `Huyen1974/incomex-workspace`; phạm vi đọc: `AGENTS.md`, `COLLAB.md`/§3.8/§3.9/P08/P09, HJW P444, GHM P99, MCPW D12, HVU UI + source runtime/API chỉ đọc của Gateway/Web/Code khi quyền thực có.
Write_Path: DUY NHẤT `work/ai-council-karpathy/COLLAB.md` để ghi STARTED/P/KQ/Bảng, **qua `workspace_*` hoặc `fs_*` đã audit**. Không direct GitHub/API/CLI write trong Workspace; không ghi mã, VPS, Directus/PG, root luật hay task khác.
Budget: 1 lượt ≤2 giờ, read-only kỹ thuật; không VPS-GHI, không tạo process nền, không sửa service/secret/ruleset, không Pro, không chờ approval trong terminal. KQ DỪNG sạch nếu blocker.

## 0. Cổng S0 (bắt buộc, không đoán)
- Owner thực sự dispatch N0; đọc AGENTS A0/A2/A5/A6/A9 → Bảng + `§3.8/§3.9/P09` của ACK → PROMPT, xác nhận RUN_ID/Host/roster/không STOP/alert/chưa STARTED; READY SHA phải khớp **commit cuối chạm PROMPT.md này**, không nhầm global HEAD khi task khác ghi.
- Kiểm đúng identity và `Write_Path` tại surface Codex từ đường đã audit; nếu không có, KQ DỪNG qua đường hợp lệ hoặc báo trong chat, KHÔNG chuyển sang direct GitHub write.
- Chỉ sau gate PASS mới ghi `STARTED@ACK-N0-VERIFY-GAPS-20261028-03 <UTC> · executor=Codex Desktop/CLI` và sửa Bảng trong cùng lượt. Sau đó mọi hoạt động với VPS/repos khác là CHỈ ĐỌC.

## 1. S1 — Dùng bản đồ §3.8 làm index, KHÔNG quét lại 115 mục
Ưu tiên đúng 7 nhóm cần phân biệt thực tế:
1. **C2 Hội đồng**: `C2.1–C2.10, C2.17, C2.20`: máy đã thật sự chặn thiếu roster, sai Host, sai vòng/quorum/VERDICT/cùng hãng, sai SHA và alert ở đường GHI/DISPATCH nào? Phân biệt cổng Hermes-only với cổng chung đa AI. Chỉ đọc code/live config và log đã có; không thử ghi sai.
2. **C4 Gateway/identity**: `C4.1–C4.8`; đặc biệt **HJW P444** = Codex đã `KQ XONG` audit `declared_actor` (không vé/token bổ sung) nhưng chưa thi công. Đọc biên nhận P444 và nơi adapter sẽ thay; KHÔNG lặp audit/đưa thêm ticket cạnh tranh.
3. **C5 Chuông**: `C5.1/C5.3/C5.5/C5.9`: COUNCIL_ALERT về Telegram, ai được đóng, alarm có chặn chuyển bước TRƯỚC mutation hay chỉ thông báo? Tách Kuma/Guard đã chạy khỏi Supervisor hội đồng mới có chữ.
4. **C1.3 Bảng stale và Đ2/Đ4 luật**: đối chiếu DROOT33, AGENTS A5/A6/DROOT57–58, HJW policy/M1 và TQT CT-000.1. Đánh dấu chính xác câu nào thật sự đang áp mà xung đột; không đề xuất sửa toàn bộ luật/88 KB; CT-000.1 là công thức ngành, A5/A6 là Council chung.
5. **C7 GitHub**: lấy kết quả **GHM P99 C2-A đã nghiệm thu ở các PR**, C2-B chưa chạy vì GitHub Pro chưa active; chỉ readback trạng thái, không làm lại PR/CI/ruleset/thử âm. Đ1 không phụ thuộc Pro để chạy N0.
6. **C8 Task View**: lần theo **đúng runtime VPS source**/Nuxt shell/HVU từ URL Owner đang dùng, xác định bước sẵn có, dữ liệu/actor/HTML, nơi chèn 3 tầng Karpathy+Vue Flow. `view.html` ACK là **snapshot P08, không live**, không suy từ giao diện minh họa rằng Vue Flow đã cài.
7. **Đ1 & quyền chủ**: kiểm HJW N4 dormant và vùng kiểm máy Council chung chưa Owner GO, các chỗ chặn có thật; trình đề xuất **một cửa code/owner mỗi delta**, không đưa ACK thành owner mã runtime khác hay tạo engine/scanner/policy song song.

## 2. S2 — Báo cáo duy nhất trong ACK
Tạo **một P mới trong chính `work/ai-council-karpathy/COLLAB.md`**, bảng ≤12 hàng:
`ID từ §3.8 | Owner/Source (task/file/commit) | Chặn thật ở đâu | Trạng thái LIVE: ENFORCED/PARTIAL/NOT_ENFORCED/UNKNOWN | Evidence/giới hạn | Delta tối thiểu/next trigger`.
- Nếu nguồn chỉ báo có luật/chỉ thị hoặc bảng màu, **không ghi ENFORCED**; nếu HJW/GHM có KQ rồi thì dẫn nguồn không chạy lại; không biết ⇒ UNKNOWN.
- Danh sách Đ1–Đ7: xác định cái nào chặn vận hành Council và cái nào thuộc task độc lập, không ôm hết backlog cũ.
- Sau N0, đề xuất N1/N2 **trên code/luật có sẵn**: AGENTS A5/A6, HJW policy/event/scanner/ASSIGN/RESULT, MCPW gateway, GHM PR/CI, HVU Task View. Không tạo `NODE_V1`, `DECISION_V1`, `WRITE_TICKET` mới nếu cơ chế hiện hữu đủ.
- Không sửa ma trận P08/view.html trong N0 bằng tay khi chưa có full evidence; đề xuất cách derive UI từ một source cho N2.

## STEP_WALK_V1
| Bước | Ai | Trigger | Budget | Evidence | Lỗi/ai nhận | Kế |
|---|---|---|---|---|---|---|
| S0 Gate/STARTED | Codex | Owner dispatch + READY đúng | ≤2h toàn N0 | identity, host, SHA, path ghi | DỪNG → GPT Host | S1 |
| S1 Đo đúng delta | Codex | S0 PASS | ≤2h | source/code/log đã có của 7 nhóm, không mutation | UNKNOWN/DEPENDENCY → GPT Host | S2 |
| S2 Báo delta | Codex | S1 đủ hoặc hết budget | ≤2h | ≤12 hàng, Đ1–Đ7, next/owner | sai scope ⇒ DỪNG | S3 |
| S3 KQ | Codex | S2 | ≤2h | một P + `KQ@ACK-N0-VERIFY-GAPS-20261028-03 XONG|DỪNG` + Bảng cùng commit | Host/Claude tiếp nhận | Review KQ |

## XONG/DỪNG
- XONG = N0 **khảo sát có chứng cứ** theo 7 nhóm, nêu rõ thiếu số đo và owner/trigger, không có mã/luật/runtime nào bị đổi. Không đòi mọi chốt ENFORCED để kết thúc audit.
- DỪNG = thiếu cổng đọc hoặc báo cáo, STOP, rủi ro cần Owner, quá ngân sách; ghi rõ blocker và nhả resource, không giữ session.
- CẤM: đổi AGENTS/PG/Directus/Graph, gateway/CI/permission/secret/runners, sửa task HJW/GHM, tạo repo/task/file phụ, cài Vue Flow, gọi API trả phí, tự RUN N1/N2; không có phép thử âm mutation.
- Sau KQ: **GPT Host đọc evidence → Claude Chat (khác hãng cả Host/Worker) nhận xét → GPT Host chốt prompt N1 hoặc đo bổ sung**, không thêm vòng nếu không còn bất đồng kỹ thuật.
NEXT_TRIGGER_AFTER_N0=HOST_REVIEW_ACK_N0_VERIFY_GAPS
