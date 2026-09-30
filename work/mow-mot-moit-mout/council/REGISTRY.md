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
- Active_RUN: none · **OWNER_REVIEW_DEF01**.
- Reserved_Targets: Host trực tiếp giữ `ban-duyet.html#matrix-view-formula` cho bản nháp định nghĩa; Executor không ghi canonical.
- Base_Target_Version: DEF-01 trên current HEAD.
- NOW: chờ Owner xem Phần II Định nghĩa; giữ A08 BLOCKED_SOURCE và B06 XONG.
- NEXT: Owner sửa/đồng thuận khái niệm → cập nhật Master Khái niệm → rồi mới lắp lại Công thức Phần I.
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
- Active_RUN: `MMIM-LANE-A08-20260930-01` = DỪNG · SOURCE_BLOCKED.
- Reserved_Targets: none.
- Base_Target_Version: KQ A08 đã ghi.
- NOW: chờ Host có nguồn authority HPML; không patch runtime mù.
- NEXT: HOST_EXPOSE_SOURCE → mới mở A09.
- BLOCKED_BY: HPML source authority chưa được expose.
- State: BLOCKED.
- LAST_SYNC: D76–D77.

### CODEX-MMIM-B
- Role: **EXECUTOR**
- Write_Zone: `ban-duyet.html` + `lane-b/COLLAB.md`.
- Active_RUN: `MMIM-LANE-B06-20260930-01` = XONG.
- Reserved_Targets: none.
- Base_Target_Version: KQ B06 legacy 7/7 · missing=0 · duplicates=0.
- NOW: chờ Owner review DEF-01.
- NEXT: chỉ nhận RUN mới sau khi Owner chốt định nghĩa.
- BLOCKED_BY: none.
- State: IDLE.
- LAST_SYNC: D76–D77.

### CODEX-MMIM-C
- Role: **EXECUTOR**
- Write_Zone: `lane-c/COLLAB.md` only; canonical/ui read-only.
- Active_RUN: next `MMIM-LANE-C05-20260930-01` = WAIT_B06.
- Reserved_Targets: none until B06 completes.
- Base_Target_Version: sẽ lấy B06 result + PRE_B05_REF.
- NOW: chờ B06; không ghi canonical.
- NEXT: C05 verify Git rằng nội dung cũ không mất ngoài scope Owner thay.
- BLOCKED_BY: B06 chưa xong.
- State: WAITING.
- LAST_SYNC: D76–D77.


### CODEX-MMIM-D
- Role: **EXECUTOR · EVIDENCE HARVEST**
- Write_Zone: `lane-d/COLLAB.md` only; mọi source khác READ-ONLY.
- Active_RUN: `MMIM-LANE-D01-20260928-01` = **HOLD_PENDING_METHOD_V0_1**.
- Reserved_Targets: lane-d/COLLAB.
- Base_Target_Version: prompt SHA `745737438e10436d51b8299514870a43112b7cf991a588fad4a5248877d0ae4e`; READY base `c48c877992fea2ec0acd26f7f02a20c6c9ca9ab6`.
- NOW: harvest facts của case Tạo MOW theo source hiện có, không thiết kế methodology.
- NEXT: KQ D01 → CHAT2_REVIEW.
- BLOCKED_BY: nếu cần invent layer/question/model mới.
- State: READY_TO_RUN.
- LAST_SYNC: D79.

### CODEX-MMIM-E
- Role: **EXECUTOR · EVIDENCE AUDIT**
- Write_Zone: `lane-e/COLLAB.md` only; canonical/UI/tools READ-ONLY.
- Active_RUN: `MMIM-LANE-E01-20260928-01` = **HOLD_PENDING_METHOD_V0_1**.
- Reserved_Targets: lane-e/COLLAB.
- Base_Target_Version: prompt SHA `f51272c3ad238497f4b54d14760739d194999402618d0330ec61eab4b0724557`; READY base `c48c877992fea2ec0acd26f7f02a20c6c9ca9ab6`.
- NOW: audit capability/tool/evidence hiện có cho `đã có/dùng lại/tạo mới`, không đặt policy.
- NEXT: KQ E01 → CHAT2_REVIEW.
- BLOCKED_BY: nếu cần invent threshold/gray-zone policy.
- State: READY_TO_RUN.
- LAST_SYNC: D79.

## Proposal contract

Mỗi proposal Council append vào ledger riêng, tối thiểu:

`P-ID · STATUS · BASE_HEAD · TARGETS + TARGET_VERSION/HASH · TOPIC · EVIDENCE · OVERLAP_CHECK · CONFLICT_WITH · PROPOSAL · FILES_AFFECTED · NEXT_FOR_HOST`

Lifecycle:
`IDEA → READY_FOR_HOST → ACCEPTED | PARTIAL | REJECTED | STALE | SUPERSEDED`.

Sau ACCEPTED/PARTIAL: Host promote phần được nhận vào parent decision/canonical/PROMPT. RUN/KQ thuộc hệ thực thi chính, **không** tiếp tục quản trong proposal.
