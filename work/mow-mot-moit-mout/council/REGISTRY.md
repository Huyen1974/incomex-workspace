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
- Active_RUN: none.
- Reserved_Targets: none.
- Base_Target_Version: `definition-master-registry-v1.js` SHA `19aa669e5e1706f6082c4a9062194cdda7161a54d010b53779594d6108d9cf1b`; `master-design-review-v1.html` SHA `7672ce1305bb858cae1600551294bfcfc92101d877b69ee84adf9793652c4280`; `master-list.js` SHA `3043a7119a4003301d7c5e3cae557c4663913791b6508bf794bee0996759c118`.
- NOW: D151 đã trả đúng một bảng Master duy nhất: 28 dòng; Quy trình/MOW row 4 xanh UI-001, UI con row 18, Config row 28 xanh. D150 iframe over-correction đã bỏ; PRIMARY_OWNER_SURFACE = dòng trong bảng đã chốt.
- NEXT: tiếp tục rà/bổ sung Master bằng cách thêm/sửa dòng trong bảng này; không dựng view song song. Codex Change Propagation audit vẫn PENDING nhưng không chặn chỉ đạo trực tiếp.
- BLOCKED_BY: Phạm vi chuyên môn + semantics Config A/B/C là concept OPEN; MOW migration cần map trước khi đổi canonical.
- State: ACTIVE.
- LAST_SYNC: D151.

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
- Active_RUN: none.
- Reserved_Targets: none.
- Base_Target_Version: A09R1 KQ final; prompt SHA `5c72ff994d5354c9462060a1043d4d859b23ee357eabdd708d8a2fefe04f9b27`; READY base `a3e422ed434704a1415446386311fe0e86f53410`.
- NOW: A09R1 XONG và đã Host ACCEPT.
- NEXT: chờ RUN mới.
- BLOCKED_BY: none.
- State: IDLE.
- LAST_SYNC: D102.

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

### CODEX-MMIM-CONFIG-20261006
- Role: **OWNER-DIRECTED DESIGN / IMPLEMENTATION**; không thay Host.
- Write_Zone: D152 Master Config và phụ thuộc UI; metadata MMIM; HJW con trỏ.
- Active_RUN: none · D152 triển khai XONG, chờ Owner review.
- Reserved_Targets: none.
- NOW: Master Config dùng UI cha; 6 cột quản lý, drawer giữ đủ dữ liệu; list/detail/index/regression đã kiểm.
- NEXT: Owner góp ý; bổ sung config thực tế. Audit Change Propagation PENDING là RUN riêng.
- BLOCKED_BY: none; FC-002 giữ OPEN.
- State: IDLE.
- LAST_SYNC: 2026-10-06T08:26:33.850Z · D152 KQ.

### CODEX-MMIM-GROUPS-20261006
- Role: OWNER-DIRECTED IMPLEMENTATION · D153.
- Write_Zone: ML-DEF-001/002 và mapping/sourceHint/cache; docs MMIM.
- Active_RUN: none · D153 XONG.
- Reserved_Targets: none.
- NOW: PASS · đủ 35 cha/115 con; bảo toàn 10 dòng cũ; coverage/quan hệ/UI đã kiểm.
- NEXT: Owner xem hai Master; hoàn thiện chuẩn/config từng nhóm.
- BLOCKED_BY: none; không tự chốt Chuyên môn.
- State: IDLE.
- LAST_SYNC: 2026-10-06 · D153.

### CODEX-MMIM-CT001-LAYOUT-20261006
- Role: OWNER-DIRECTED IMPLEMENTATION · D154; không thay Host.
- Write_Zone: ban-duyet.html#formula-ct-001 layout + metadata COLLAB/Registry.
- Active_RUN: none · D154 XONG.
- Reserved_Targets: none.
- Base_Target_Version: 5abe7de59b7e02f20ea3c08ffa173a679dbb0b6e35656354eceb2ed7da5a24f7.
- NOW: PASS · 3→7/mũi tên cùng hàng ở 375/600/690/768/1024/1440 px; cuộn cục bộ, bàn phím và link7 PASS; đúng URL Owner fresh.
- NEXT: Owner xem; chỉ làm tiếp khi có yêu cầu mới.
- BLOCKED_BY: none.
- State: IDLE.
- LAST_SYNC: 2026-10-06T08:59:16Z · D154 KQ/COORD.

### CODEX-MMIM-TOTAL-20261006
- Role: OWNER-DIRECTED IMPLEMENTATION · D155.
- Write_Zone: Master index Total + loader/shared mapping; docs MMIM.
- Active_RUN: none · D155 XONG.
- Reserved_Targets: none.
- NOW: PASS · Total tự đếm sau Tên; live đủ 28 dòng và số 35/115 đúng.
- NEXT: Owner dùng bảng; số tự cập nhật khi mở/tải lại.
- BLOCKED_BY: none.
- State: IDLE.
- LAST_SYNC: 2026-10-06 · D155.

### CODEX-MMIM-CT0051-20261006
- Role: OWNER-DIRECTED IMPLEMENTATION · D156.
- Write_Zone: CT-005/005.1; Gộp/Tách nhóm con và MOT/Task; dependent labels/cache/docs.
- Active_RUN: none · D156 XONG.
- Reserved_Targets: none.
- NOW: PASS · CT-005 Nhóm cha, CT-005.1 Task; hai cột ngoại lệ ở Nhóm con/MOT; Total 8.
- NEXT: Owner xem; hồ sơ ngoại lệ triển khai theo ca thật, chưa có backend CRUD.
- BLOCKED_BY: none; semantics khác giữ nguyên.
- State: IDLE.
- LAST_SYNC: 2026-10-06 · D156.

### CODEX-MMIM-D157
- Role: OWNER-DIRECTED IMPLEMENTATION; không thay Host.
- Active_RUN: none · D157 phần công thức XONG.
- Reserved_Targets: none.
- NOW: công thức/ghi chú và Total10 đã kiểm; SSOT dữ liệu chưa mapping/migration.
- NEXT: Owner góp ý ba ngữ cảnh theo đầu ra; một bức tranh chung + chọn ngữ cảnh là đề xuất.
- BLOCKED_BY: mapping dữ liệu hiện có cần evidence; không bịa quan hệ.
- State: IDLE.
- LAST_SYNC: 2026-10-06 · D157 KQ.

### CODEX-MMIM-D158
- Role: OWNER-DIRECTED IMPLEMENTATION.
- Active_RUN: none · D158 XONG thiết kế/UI.
- Reserved_Targets: none.
- NOW: Master Quy trình35 dòng CH-001 từ Nhóm cha, coverage7×5 và Total35 PASS; seed FIELD.KHAI/legacy giữ nguyên. Tên 35 cha/115 con có Chuỗi; Task/MOIT/MOUT mỗi loại115 dẫn xuất từ Nhóm con, Total tự đếm. VM propagation và live index/list PASS; 11 công thức/29 Master giữ nguyên.
- NEXT: Owner rà tên/cột, hoàn thiện cấu hình từng loại. Danh mục UI đã đồng bộ; mapping demo/backend giữ riêng, chưa migrate.
- State: IDLE.
- LAST_SYNC: 2026-10-06 · D158 KQ; follow-up thay 3 SVG vector Owner (29.600 bytes), kiểm ảnh hiển thị và console PASS.

## Proposal contract

Mỗi proposal Council append vào ledger riêng, tối thiểu:

`P-ID · STATUS · BASE_HEAD · TARGETS + TARGET_VERSION/HASH · TOPIC · EVIDENCE · OVERLAP_CHECK · CONFLICT_WITH · PROPOSAL · FILES_AFFECTED · NEXT_FOR_HOST`

Lifecycle:
`IDEA → READY_FOR_HOST → ACCEPTED | PARTIAL | REJECTED | STALE | SUPERSEDED`.

Sau ACCEPTED/PARTIAL: Host promote phần được nhận vào parent decision/canonical/PROMPT. RUN/KQ thuộc hệ thực thi chính, **không** tiếp tục quản trong proposal.
