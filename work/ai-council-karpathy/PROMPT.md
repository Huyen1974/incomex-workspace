# PROMPT — ACK N0 GAP-ONLY: ĐỐI CHIẾU KHOẢNG TRỐNG SAU TÍCH HỢP
RUN_ID: ACK-N0-GAP-ONLY-20261028-02
Status: canonical; thay `ACK-N0-READONLY-20261028-01`. Chỉ chạy khi Host ký READY@full last-touch SHA mới trong COLLAB và Owner dispatch AUTO0.
Executor_Surface: Claude Code CLI trên Mac; Worker N0, không là Reviewer độc lập của chính KQ.
Read scope: incomex-workspace, agent-data-test, web-test; VPS source/config **chỉ đọc** theo quyền đã có.
Write_Path: **chỉ** `work/ai-council-karpathy/COLLAB.md` qua `fs_*`/`workspace_*` đã audit, để ghi STARTED/P/KQ; cấm direct Github write ở Workspace.
Budget ≤2 giờ một lượt; không VPS-GHI/runner lease, không treo để chờ, không tự chạy N1.

## S0 — Chỉ bắt đầu sau Owner dispatch
Đọc AGENTS → Bảng task ACK/§3.7 D03/P07 → PROMPT canonical; kiểm RUN_ID, Host, đúng READY@SHA last-touch, STOP/COUNCIL_ALERT, capability ghi báo cáo đã audit; thiếu ⇒ DỪNG trước mutation. Sau PASS ghi STARTED vào COLLAB qua gateway và sửa Bảng trong cùng lượt.

## S1 — CHỈ KHAI THÁC THỨ ĐÃ CÓ, KHÔNG LÀM LẠI
1. AGENTS A0–A9, HJW HĐ/M1/N4: `TASK_POLICY_V1` / `FLOW_EVENT_V1` / `ASSIGN_V1/RESULT_V1` / scanner / chuông và N4 chưa đạt. **Không đề nghị xây Council Engine riêng**.
2. HJW P443: một cửa xưng danh, `declared_actor` vs `authenticated_actor`; **đã có lệnh audit Codex riêng**. Đọc KQ hiện hành; nếu chưa KQ ⇒ `DEPENDENCY_PENDING`, không làm lại audit P443 hay viết `WRITE_TICKET` song song.
3. MCPW D12: đã nghiệm thu gateway-only + CAS/version/operation_id/presence. Ghi nhận bằng chứng, chỉ phát hiện delta chưa kiểm.
4. GHM C2: chỉ đọc kết quả đã đo, yêu cầu bảo vệ main/merge và tình trạng Pro. **Không chạy lại PR test/C2, không thay ruleset**; chưa hoàn tất ⇒ `DEPENDENCY_PENDING`.
5. HVU: kiểm source Task View thực (VPS code SSOT) và dữ liệu từ COLLAB/cache; chỉ xác định nơi thêm Stage1–3 (học từ Karpathy) + Vue Flow (MIT riêng). Không tạo app/trang mới.
6. D03.B 16 mã K1–K10/L1–L6: đối chiếu từng phần với các mục trên, không chụp lại 16 phép thử mới; ghi **đã có / có thể copy khung / cần adapter / không copy**.

## S2 — Một bảng delta (không báo cáo rời)
Trả một mục P mới trong đúng COLLAB:
`Thành phần | code/path hoặc task chủ | hiện có & evidence | delta thật | chịu trách nhiệm | BLOCK/CHƯA ĐO`; số hàng <=12; tách rõ “đã là luật”, “đã cưỡng chế”, “đang được task khác làm”. Các nơi đã có chủ HJW P443/GHM C2/MCPW/HVU chỉ **link**, không nhận việc.
Đề xuất N1–N2 tối thiểu chỉ bằng các thay đổi thực sự thiếu trong hợp đồng hiện có; không tự đề nghị `NODE_V1`/`DECISION_V1` hay DB/dispatcher/sổ ghế mới. Ghi các mẫu Karpathy chỉ tham khảo mã nguồn, không chép React/FPGA/GPU/OpenRouter không phù hợp. Nếu nguồn live khác GitHub, dùng live làm đúng và ghi sai lệch.

## STEP_WALK_V1
| Bước | Ai | Trigger | Ngân sách | Evidence | Lỗi | Kế |
|---|---|---|---|---|---|---|
| S0 gate/STARTED | Claude Code CLI | Owner dispatch + READY SHA mới | ≤2h | read-gate và write-path audit | KQ DỪNG, Host biết | S1 |
| S1 inventory delta | Claude Code CLI | S0 PASS | ≤2h | task chủ và source chính xác | CHƯA ĐO/DEPENDENCY_PENDING | S2 |
| S2 map Karpathy | Claude Code CLI | S1 đủ | ≤2h | mỗi delta đúng source/hợp đồng | không tạo hệ mới | S3 |
| S3 P/KQ | Claude Code CLI | đủ/đến trần | ≤2h | một P + Bảng + KQ@RUN_ID XONG/DỪNG trong COLLAB | dừng, nhả mọi lease | Host review |

## DoD
XONG N0 chỉ khi có ma trận delta và vị trí UI thật, **không đòi 8 cổng phải PASS**; thiếu chứng cứ phải ghi CHƯA ĐO, task khác chưa KQ phải ghi DEPENDENCY_PENDING. Không tạo file báo cáo, không sửa code/CI/AGENTS/runtime/keys/gateway/PG/Directus; không cài Vue Flow, không động tài nguyên đang bận, không tự làm N1–N4. Kết thúc Host GPT + Reviewer khác hãng rà KQ trước bước kế.
NEXT_TRIGGER_AFTER_N0=HOST_REVIEW_ACK_N0_GAP_ONLY
