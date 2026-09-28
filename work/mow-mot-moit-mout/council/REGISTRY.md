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
- Active_RUN: preparing `A06 / B04 / C03`.
- Reserved_Targets: điều phối batch; không tranh target Executor.
- Base_Target_Version: re-read trước Host mutation.
- NOW: nghiệm thu A05/B03/C02 xong; mở batch evidence/audit không đụng methodology Chat.2.
- NEXT: gate + READY A06/B04/C03; chờ proposal phương pháp luận Chat.2.
- BLOCKED_BY: none.
- State: ACTIVE.
- LAST_SYNC: D76–D77.

### GPT-MMIM-CHAT2-260928-A
- Role: **COUNCIL / IDEA / REVIEW**
- Write_Zone: `council/GPT-CHAT-2.md` only.
- Active_RUN: none.
- Reserved_Targets: **METHODOLOGY_TOPIC** = Process→Step→UI · reuse-or-create · gray-zone decision · evidence/model/check process.
- Base_Target_Version: proposal phải ghi target/evidence hash khi chốt.
- NOW: thảo luận phương pháp luận đáng tin cậy: công thức tạo Step/UI, mô hình dữ liệu để kiểm `đã có / dùng lại / tạo mới`, cách xử lý vùng xám và bằng chứng cho quyết định.
- NEXT: khi thống nhất trong chat, ghi proposal READY_FOR_HOST; chưa chốt thì chưa promote canonical.
- BLOCKED_BY: none; Executor A/B/C bị cấm tự thiết kế lại topic này.
- State: ACTIVE.
- LAST_SYNC: D76–D77.

### CODEX-MMIM-A
- Role: **EXECUTOR**
- Write_Zone: root ui audit metadata + `lane-a/COLLAB.md`.
- Active_RUN: `MMIM-LANE-A06-20260928-01` = PREPARED.
- Reserved_Targets: root ui `master-of-master-v1.html`, `master-home-v1.html`, `ui-child-content-v1.js` if needed + lane-a/COLLAB.
- Base_Target_Version: prompt to be gated.
- NOW: audit 4 core Master Lists Process/Tool/Step/UI; expose conflict/gap, no new catalog.
- NEXT: KQ A06.
- BLOCKED_BY: COORD/PARALLEL conflict only.
- State: PREPARED.
- LAST_SYNC: D76–D77.

### CODEX-MMIM-B
- Role: **EXECUTOR**
- Write_Zone: `ban-duyet.html` + `lane-b/COLLAB.md`.
- Active_RUN: `MMIM-LANE-B04-20260928-01` = PREPARED.
- Reserved_Targets: ban-duyet + lane-b.
- Base_Target_Version: 23-contract canonical from B03 must stay except CHUNG.KIEM/FORM.TAO.
- NOW: resolve or prove-blocked exactly 2 OPEN contracts.
- NEXT: KQ B04.
- BLOCKED_BY: insufficient source.
- State: PREPARED.
- LAST_SYNC: D76–D77.

### CODEX-MMIM-C
- Role: **EXECUTOR**
- Write_Zone: `lane-c/COLLAB.md` only; canonical/ui read-only.
- Active_RUN: `MMIM-LANE-C03-20260928-01` = PREPARED.
- Reserved_Targets: lane-c/COLLAB.
- Base_Target_Version: C01+B02R1 evidence + C02 only as comparison.
- NOW: prove reproducibility of 25→15 Human Step with explicit 6-tuple rule.
- NEXT: KQ C03.
- BLOCKED_BY: if 15 requires hidden/manual semantic judgment.
- State: PREPARED.
- LAST_SYNC: D76–D77.

## Proposal contract

Mỗi proposal Council append vào ledger riêng, tối thiểu:

`P-ID · STATUS · BASE_HEAD · TARGETS + TARGET_VERSION/HASH · TOPIC · EVIDENCE · OVERLAP_CHECK · CONFLICT_WITH · PROPOSAL · FILES_AFFECTED · NEXT_FOR_HOST`

Lifecycle:
`IDEA → READY_FOR_HOST → ACCEPTED | PARTIAL | REJECTED | STALE | SUPERSEDED`.

Sau ACCEPTED/PARTIAL: Host promote phần được nhận vào parent decision/canonical/PROMPT. RUN/KQ thuộc hệ thực thi chính, **không** tiếp tục quản trong proposal.
