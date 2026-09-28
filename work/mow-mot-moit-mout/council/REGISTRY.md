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
- Active_RUN: batch `A05 / B03 / C02` = READY_TO_RUN.
- Reserved_Targets: điều phối toàn batch; không trực tiếp tranh target đã reserve cho Executor.
- Base_Target_Version: re-read trước mỗi Host mutation.
- NOW: giám sát A05/B03/C02; tích hợp governance Chat.1/Chat.2; giữ checkpoint Owner nhìn thấy Master→List→Detail.
- NEXT: nghiệm thu KQ A05/B03/C02; promote proposal Council nào được ACCEPTED; cập nhật Registry.
- BLOCKED_BY: không.
- State: ACTIVE.
- LAST_SYNC: D72–D73.

### GPT-MMIM-CHAT2-260928-A
- Role: **COUNCIL / IDEA / REVIEW**
- Write_Zone: `council/GPT-CHAT-2.md` only, trừ khi Host/Owner giao khác bằng quyết định mới.
- Active_RUN: none.
- Reserved_Targets: none.
- Base_Target_Version: proposal phải ghi version/hash target/evidence cụ thể.
- NOW: nghiên cứu ý tưởng/gap/trùng/chồng/xung đột ngoài Reserved_Targets; phản biện Host/Executor; proposal đầu tiên về governance đã ACCEPTED vào D72–D73.
- NEXT: chọn topic không chồng A05/B03/C02; ghi proposal READY_FOR_HOST theo template ledger.
- BLOCKED_BY: nếu topic trùng Reserved_Targets thì chỉ ghi CONFLICT_WITH, không chuẩn bị mutation cùng vùng.
- State: ACTIVE.
- LAST_SYNC: D72–D73.

### CODEX-MMIM-A
- Role: **EXECUTOR**
- Write_Zone: theo `lane-a/PROMPT.md`.
- Active_RUN: `MMIM-LANE-A05-20260928-01` = READY_TO_RUN.
- Reserved_Targets: root ui `master-of-master-v1.html`, `master-home-v1.html`, `ui-child-content-v1.js` khi cần + `lane-a/COLLAB.md`.
- Base_Target_Version: prompt SHA `bfe603411d82391a32daa3987b6f124436641e969c623249b5441f8c1c412658`; READY base `1bd42c508d18fb747a0aeeb16f16886d18edec9a`; re-read own target trước mutation.
- NOW: Field List acceptance + kiểm đường 5 List.
- NEXT: KQ A05; dừng.
- BLOCKED_BY: PARALLEL_CONFLICT nếu own target bị surface khác chạm.
- State: READY_TO_RUN.
- LAST_SYNC: D74–D75.

### CODEX-MMIM-B
- Role: **EXECUTOR**
- Write_Zone: theo `lane-b/PROMPT.md`.
- Active_RUN: `MMIM-LANE-B03-20260928-01` = READY_TO_RUN.
- Reserved_Targets: `ban-duyet.html` + `lane-b/COLLAB.md`.
- Base_Target_Version: prompt SHA `fed4bdbf55897530f58c41876ee1fcbc900c093427148e12551398252512d590`; READY base `1bd42c508d18fb747a0aeeb16f16886d18edec9a`; canonical B02R1 12-contract snapshot phải giữ.
- NOW: opt-in contract cho tối đa 13 candidate FIELD/FORM/MOT đủ evidence.
- NEXT: KQ B03; dừng.
- BLOCKED_BY: thiếu evidence hoặc PARALLEL_CONFLICT own target.
- State: READY_TO_RUN.
- LAST_SYNC: D74–D75.

### CODEX-MMIM-C
- Role: **EXECUTOR**
- Write_Zone: `lane-c/COLLAB.md` only.
- Active_RUN: `MMIM-LANE-C02-20260928-01` = READY_TO_RUN.
- Reserved_Targets: `lane-c/COLLAB.md`; canonical/ui READ-ONLY.
- Base_Target_Version: prompt SHA `f7d12de568042f39f4806bc60adc3a94e6640b792b97abd4dcba9d44486f636b`; READY base `1bd42c508d18fb747a0aeeb16f16886d18edec9a`; phụ thuộc 12 contract B02R1 không đổi.
- NOW: chốt `H_MOW / U_MOW / UI_MISSING` từ 25 instance + 12 contract.
- NEXT: KQ C02; dừng.
- BLOCKED_BY: 12 contract B02R1 bị thay hoặc evidence UI không đủ.
- State: READY_TO_RUN.
- LAST_SYNC: D74–D75.

## Proposal contract

Mỗi proposal Council append vào ledger riêng, tối thiểu:

`P-ID · STATUS · BASE_HEAD · TARGETS + TARGET_VERSION/HASH · TOPIC · EVIDENCE · OVERLAP_CHECK · CONFLICT_WITH · PROPOSAL · FILES_AFFECTED · NEXT_FOR_HOST`

Lifecycle:
`IDEA → READY_FOR_HOST → ACCEPTED | PARTIAL | REJECTED | STALE | SUPERSEDED`.

Sau ACCEPTED/PARTIAL: Host promote phần được nhận vào parent decision/canonical/PROMPT. RUN/KQ thuộc hệ thực thi chính, **không** tiếp tục quản trong proposal.
