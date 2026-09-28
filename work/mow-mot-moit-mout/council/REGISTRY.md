# MMIM · Council / Surface Registry

Nguồn điều hành: parent `../COLLAB.md` D72–D73. Registry này là **bảng phối hợp**, không phải canonical nghiệp vụ và không thay PROMPT/KQ.

## Luật đọc nhanh

- Owner = quyền cuối.
- `GPT-MMIM-260920-A` = Host/Dispatcher/Integrator duy nhất trong phạm vi Owner giao.
- Council không phát RUN, không sửa active PROMPT/canonical, chỉ ghi proposal trong Write_Zone riêng.
- Executor chỉ làm RUN đã READY.
- Một target chỉ có một writer/reservation chủ động.
- HEAD đổi do việc khác không tự làm stale; kiểm `TARGET_VERSION/HASH` của đúng target/evidence.
- Mọi surface phải giữ `NOW / NEXT / BLOCKED_BY / RESERVED_TARGETS / LAST_SYNC` hiện hành.
- Trước khi nghiên cứu/nhận việc mới: đọc file này.

## Active surfaces · 2026-09-28

### GPT-MMIM-CHAT1-260928-A
- Role: **HOST / DISPATCHER / INTEGRATOR**
- Host_ID: `GPT-MMIM-260920-A`
- Write_Zone: parent COLLAB · PROMPT/lane prompts khi điều hành · canonical theo Owner scope.
- Active_RUN: preparing batch `A06 / B04 / C03 / D01 / E01`.
- Reserved_Targets: điều phối 5 Executor; không tranh target riêng.
- Base_Target_Version: READY D78 superseded; re-read trước Host mutation.
- NOW: khóa methodology scope cho Chat.2; thêm D/E evidence-only; chuẩn bị gate/READY 5 lane.
- NEXT: gate + READY 5 lane; nghiệm thu KQ; chuyển raw evidence D/E cho Chat.2.
- BLOCKED_BY: none.
- State: ACTIVE.
- LAST_SYNC: D76–D77.

### GPT-MMIM-CHAT2-260928-A
- Role: **COUNCIL / IDEA / REVIEW**
- Write_Zone: `council/GPT-CHAT-2.md` only.
- Active_RUN: none.
- Reserved_Targets: **METHODOLOGY_TOPIC** = multi-layer decomposition · mandatory questions per layer · Process→Step→UI · reuse-or-create · gray-zone/confidence/evidence model · clarification process/tool/DOT/technology · proof of reliability.
- Base_Target_Version: proposal phải ghi target/evidence hash khi chốt.
- NOW: thiết kế lại phương pháp luận nhiều tầng cho case phức tạp như Tạo MOW: mỗi tầng trả lời gì, đọc/ghi đâu, process/tool/DOT nào, bằng chứng gì, thế nào là chắc/mơ hồ, làm rõ ra sao, chứng minh cải thiện thế nào.
- NEXT: khi thống nhất trong chat, ghi proposal READY_FOR_HOST; dùng D01/E01 như raw evidence, không để Executor quyết methodology thay Council.
- BLOCKED_BY: none; Executor A/B/C/D/E bị cấm tự thiết kế lại METHODOLOGY_TOPIC.
- State: ACTIVE.
- LAST_SYNC: D76–D77.

### CODEX-MMIM-A
- Role: **EXECUTOR**
- Write_Zone: root ui audit metadata + `lane-a/COLLAB.md`.
- Active_RUN: `MMIM-LANE-A06-20260928-01` = READY_TO_RUN.
- Reserved_Targets: root ui `master-of-master-v1.html`, `master-home-v1.html`, `ui-child-content-v1.js` if needed + lane-a/COLLAB.
- Base_Target_Version: prompt SHA `35b2e59d549be357e5b78081001b37fb7dc89421f3129496a64992e54ac08434`; READY base `903b34c4dc7103a7dc88a84d3f59d4ac5d6b3aee`.
- NOW: audit 4 core Master Lists Process/Tool/Step/UI; expose conflict/gap, no new catalog.
- NEXT: KQ A06.
- BLOCKED_BY: COORD/PARALLEL conflict only.
- State: READY_TO_RUN.
- LAST_SYNC: D76–D77.

### CODEX-MMIM-B
- Role: **EXECUTOR**
- Write_Zone: `ban-duyet.html` + `lane-b/COLLAB.md`.
- Active_RUN: `MMIM-LANE-B04-20260928-01` = READY_TO_RUN.
- Reserved_Targets: ban-duyet + lane-b.
- Base_Target_Version: prompt SHA `ac891028bbc3d051add2da090631b1370e25909e8d137b7e0c4e49d59c4722c2`; READY base `903b34c4dc7103a7dc88a84d3f59d4ac5d6b3aee`; 23-contract canonical from B03 must stay except CHUNG.KIEM/FORM.TAO.
- NOW: resolve or prove-blocked exactly 2 OPEN contracts.
- NEXT: KQ B04.
- BLOCKED_BY: insufficient source.
- State: READY_TO_RUN.
- LAST_SYNC: D76–D77.

### CODEX-MMIM-C
- Role: **EXECUTOR**
- Write_Zone: `lane-c/COLLAB.md` only; canonical/ui read-only.
- Active_RUN: `MMIM-LANE-C03-20260928-01` = READY_TO_RUN.
- Reserved_Targets: lane-c/COLLAB.
- Base_Target_Version: prompt SHA `3a1219ecdb4b9e3c060dd8b5a9c0c37a5590337cac3c1ea9088357fa88fee3e0`; READY base `903b34c4dc7103a7dc88a84d3f59d4ac5d6b3aee`; C01+B02R1 evidence + C02 only as comparison.
- NOW: prove reproducibility of 25→15 Human Step with explicit 6-tuple rule.
- NEXT: KQ C03.
- BLOCKED_BY: if 15 requires hidden/manual semantic judgment.
- State: READY_TO_RUN.
- LAST_SYNC: D76–D77.


### CODEX-MMIM-D
- Role: **EXECUTOR · EVIDENCE HARVEST**
- Write_Zone: `lane-d/COLLAB.md` only; mọi source khác READ-ONLY.
- Active_RUN: `MMIM-LANE-D01-20260928-01` = PREPARED.
- Reserved_Targets: lane-d/COLLAB.
- Base_Target_Version: prompt to be gated.
- NOW: harvest facts của case Tạo MOW theo source hiện có, không thiết kế methodology.
- NEXT: KQ D01 → CHAT2_REVIEW.
- BLOCKED_BY: nếu cần invent layer/question/model mới.
- State: PREPARED.
- LAST_SYNC: D79.

### CODEX-MMIM-E
- Role: **EXECUTOR · EVIDENCE AUDIT**
- Write_Zone: `lane-e/COLLAB.md` only; canonical/UI/tools READ-ONLY.
- Active_RUN: `MMIM-LANE-E01-20260928-01` = PREPARED.
- Reserved_Targets: lane-e/COLLAB.
- Base_Target_Version: prompt to be gated.
- NOW: audit capability/tool/evidence hiện có cho `đã có/dùng lại/tạo mới`, không đặt policy.
- NEXT: KQ E01 → CHAT2_REVIEW.
- BLOCKED_BY: nếu cần invent threshold/gray-zone policy.
- State: PREPARED.
- LAST_SYNC: D79.

## Proposal contract

Mỗi proposal Council append vào ledger riêng, tối thiểu:

`P-ID · STATUS · BASE_HEAD · TARGETS + TARGET_VERSION/HASH · TOPIC · EVIDENCE · OVERLAP_CHECK · CONFLICT_WITH · PROPOSAL · FILES_AFFECTED · NEXT_FOR_HOST`

Lifecycle:
`IDEA → READY_FOR_HOST → ACCEPTED | PARTIAL | REJECTED | STALE | SUPERSEDED`.

Sau ACCEPTED/PARTIAL: Host promote phần được nhận vào parent decision/canonical/PROMPT. RUN/KQ thuộc hệ thực thi chính, **không** tiếp tục quản trong proposal.
