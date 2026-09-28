# Council Ledger · GPT-MMIM-CHAT2-260928-A

Role: **COUNCIL / IDEA / REVIEW**  
Host hiện hành: `GPT-MMIM-260920-A`  
Luật: parent `../COLLAB.md` D72–D73 + `REGISTRY.md`.

## Current coordination

- NOW: chọn và nghiên cứu topic không trùng Reserved_Targets A05/B03/C02; phản biện bằng evidence/JEV khi phù hợp.
- NEXT: append proposal `READY_FOR_HOST` vào file này; Host quyết promote hay không.
- BLOCKED_BY: topic trùng Reserved_Targets → ghi `CONFLICT_WITH`, không chuẩn bị mutation cùng vùng.
- RESERVED_TARGETS: none.
- LAST_SYNC: D72–D73.

## P-CHAT2-001 · Governance nhiều surface

- STATUS: **ACCEPTED**
- BASE_HEAD: proposal được nêu khi A04 vừa XONG; Host đã re-read repo trước promote.
- TARGETS: parent governance + Council Registry.
- TOPIC: một Host + nhiều Council/Executor để tăng song song mà không tạo nhiều trung tâm điều hành.
- EVIDENCE: repo dùng expected_head/version; root ui không có Git HEAD; A/B/C đã cần write-zone tách; Owner yêu cầu có thể mở rộng thêm GPT/Claude/Hermes.
- OVERLAP_CHECK: không sửa A04 product; governance được promote sau A04 KQ.
- PROPOSAL ACCEPTED:
  1. Owner là quyền cuối; Chat.1 là Host/Integrator duy nhất trong phạm vi Owner giao.
  2. STALE theo target/evidence version/hash, không theo HEAD đơn độc.
  3. Proposal lifecycle tách khỏi RUN/KQ lifecycle.
  4. Registry có `Surface_ID · Role · Scope · Write_Zone · Active_RUN · Reserved_Targets · Base_Target_Version · State`.
  5. Một ledger file mỗi Council surface; không file-per-proposal.
- HOST ADDITION ACCEPTED: mọi surface phải công khai `NOW/NEXT/BLOCKED_BY/RESERVED_TARGETS/LAST_SYNC` để chia sẻ ý định sắp làm và tránh đụng nhau.
- PROMOTED_TO: D72–D73 + `REGISTRY.md`.
- NEXT_FOR_HOST: none.

## Template proposal tiếp theo

### P-CHAT2-XXX · <topic>
- STATUS: IDEA | READY_FOR_HOST | ...
- BASE_HEAD:
- TARGETS:
  - `path` · TARGET_VERSION/HASH:
- TOPIC:
- EVIDENCE:
- OVERLAP_CHECK:
- CONFLICT_WITH:
- PROPOSAL:
- FILES_AFFECTED:
- NEXT_FOR_HOST:
