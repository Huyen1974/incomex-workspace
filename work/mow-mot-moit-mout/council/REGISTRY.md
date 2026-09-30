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
- Active_RUN: batch `A07 / B05 / C04` = READY_TO_RUN.
- Reserved_Targets: B05 = `ban-duyet.html`; A07/C04 read-only + lane ledgers.
- Base_Target_Version: READY base `626769a87a786abfeb410ea3e85b8a48d9ff8846`.
- NOW: giám sát FORMULA-01; B sửa mặt Công thức, A/C song song audit.
- NEXT: nghiệm thu B05 bằng mắt Owner + nhận A07/C04 để mở patch/load và chốt 2-view formula.
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
- Active_RUN: `MMIM-LANE-A07-20260930-01` = READY_TO_RUN.
- Reserved_Targets: `lane-a/COLLAB.md`; `ban-duyet.html` READ-ONLY.
- Base_Target_Version: prompt SHA `eda0373320a09b1e732393c6613324bf95d8702a06f6adcfc7d5facc03aac37d`; READY base `626769a87a786abfeb410ea3e85b8a48d9ff8846`.
- NOW: chẩn đoán tab/load/reload Owner View; không patch.
- NEXT: KQ A07 → A08 patch sau B05.
- BLOCKED_BY: none.
- State: READY_TO_RUN.
- LAST_SYNC: D76–D77.

### CODEX-MMIM-B
- Role: **EXECUTOR**
- Write_Zone: `ban-duyet.html` + `lane-b/COLLAB.md`.
- Active_RUN: `MMIM-LANE-B05-20260930-01` = READY_TO_RUN.
- Reserved_Targets: `ban-duyet.html + lane-b/COLLAB.md` (writer duy nhất canonical trong batch).
- Base_Target_Version: prompt SHA `a0c9108bb4de0b775c65936c6525e7056c89e6a1bf15a4aa0d55a53f63b9f993`; READY base `626769a87a786abfeb410ea3e85b8a48d9ff8846`.
- NOW: sửa mặt ★ Công thức theo D91.
- NEXT: KQ B05 → OWNER_LOOK.
- BLOCKED_BY: PARALLEL_CONFLICT nếu canonical bị surface khác chạm.
- State: READY_TO_RUN.
- LAST_SYNC: D76–D77.

### CODEX-MMIM-C
- Role: **EXECUTOR**
- Write_Zone: `lane-c/COLLAB.md` only; canonical/ui read-only.
- Active_RUN: `MMIM-LANE-C04-20260930-01` = READY_TO_RUN.
- Reserved_Targets: `lane-c/COLLAB.md`; canonical/root ui READ-ONLY.
- Base_Target_Version: prompt SHA `c0fae2b41af054534af335d9802272e1e3c899f962d9791f50f385a71bc1cc38`; READY base `626769a87a786abfeb410ea3e85b8a48d9ff8846`.
- NOW: kiểm công thức 1 Đối tượng = Master List + Kanban và ý nghĩa 6 khuôn cha.
- NEXT: KQ C04.
- BLOCKED_BY: none.
- State: READY_TO_RUN.
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
