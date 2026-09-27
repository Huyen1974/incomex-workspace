# PROMPT — LANE B02 · MOW Human-Step Contract v1

RUN_ID: MMIM-LANE-B02-20260928-01
PROCESS: CHUNG.APQUYTRINH
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor: Codex
Write scope:
- `work/mow-mot-moit-mout/ban-duyet.html`
- `work/mow-mot-moit-mout/lane-b/COLLAB.md`
Không sửa gate tool, Step/UI/VPS UI.

## 0. Gate
Đọc AGENTS → parent COLLAB D56–D61 → B01 KQ → C01 KQ → lane-b/COLLAB → file này.
Trước mutation chạy current dot-process-gate trên prompt+catalog. FAIL → DỪNG.

## 1. Vì sao B02
C01 có 25 Human Step instance nhưng không thể gộp vì thiếu:
`quyền · state-in/out · điểm quay về`.
B01 cũng xác nhận CHUNG.TIM thiếu target/search contract.

B02 **không tạo Step/UI**. B02 version Process contract để C02 có căn cứ.

## 2. Batch contract-v1
Chỉ opt-in đúng các process:
- CHUNG.TIM
- CHUNG.NEU
- CHUNG.DUYET
- CHUNG.BAT
- CHUNG.NGUNG
- MOW.TAO
- MOW.LAP
- MOW.KHAI
- MOW.SUA
- MOW.XOA
- MOW.CHAY
- MOT.CHAY

Giữ mã + tên + thứ tự process.
Không sửa 27 process còn lại.

Mỗi definition trên thêm process attrs:
`data-contract-v="1" data-when="..." data-input-contract="..." data-output-contract="..." data-return-contract="..." data-contract-source="B02/D61"`.

Mỗi direct human step thêm span rỗng:
`proc-contract + step-key + right-class + state-in + state-out + return + ui-intent`.

### Controlled vocabulary
right-class:
`REQUESTER|APPROVER|EDITOR|CONFIGURATOR|ACTIVATOR|ASSIGNEE|CONTRIBUTOR|VIEWER`

ui-intent:
`SEARCH|REQUEST|REVIEW|EDIT|CONFIGURE|ACTIVATE|EXECUTE|ATTACH|VIEW`

State là **semantic process state**, không giả là DB enum.
Return là step-key tiếp theo hoặc `CALLER` / `PROCESS_END`.

## 3. Contract bắt buộc của CHUNG.TIM
Input contract phải tối thiểu:
`target_catalog_code · object_type · query/name/meaning/label · scope(optional) · status/version constraints(optional)`.

Output contract phải phân biệt:
`FOUND_EXACT | FOUND_CANDIDATES | NOT_FOUND | SEARCH_INCOMPLETE`
+ candidate ids/versions + coverage/evidence.

Luật:
- NOT_FOUND chỉ hợp lệ khi coverage đủ theo contract;
- SEARCH_INCOMPLETE không được biến thành “tạo mới”;
- mọi outcome trả về caller.

Không tự thiết kế semantic search engine trong B02; chỉ contract.

## 4. Human-step contract từ evidence C01/B01
Chuẩn hóa đủ để C02 so chữ ký, không bịa người cụ thể:
- tìm → REQUESTER · SEARCH;
- nêu nhu cầu → REQUESTER · REQUEST;
- duyệt/trả → APPROVER · REVIEW;
- khai/sửa định nghĩa → EDITOR · EDIT;
- cấu hình → CONFIGURATOR · CONFIGURE;
- bật → ACTIVATOR · ACTIVATE;
- nhận/làm/gửi việc → ASSIGNEE · EXECUTE;
- tệp/bình luận → CONTRIBUTOR · ATTACH;
- theo dõi → VIEWER · VIEW.

Nếu một step không khớp chắc một class trên → DỪNG step đó, ghi OPEN; không ép.

## 5. State/return
Dùng chính thứ tự process hiện hành + C01 evidence.
Ví dụ semantic:
- SEARCH_REQUESTED → SEARCH_RESULT → CALLER
- REVIEW_PENDING → APPROVED|RETURNED → CALLER
- DRAFT_DEFINED → STEPS_SELECTED → ...
- CONFIGURED → ACTIVE
- ASSIGNED → OPENED → SUBMITTED
- VIEW chỉ quan sát: RUNNING → RUNNING

Không đổi logic process để “làm đẹp” state.
Không thêm Human Step mới.

## 6. Hiển thị nhìn-thấy-thật
Trong vùng Process hiện hành thêm **một summary gọn**:
`Contract v1: 12/39 process · human step metadata=<n> · nguồn B02/C01`
và ghi rõ đây là **TẠM CHỐT để C02 suy Step/UI**, chưa final.

Không tạo trang/file UI mới trong B02.

## 7. Acceptance
- process count vẫn 39; code/name 39 giữ nguyên;
- 12 process opt-in contract-v1;
- direct human steps trong 12 process có metadata đầy đủ;
- textual process arrows/read/write giữ logic cũ;
- CHUNG.TIM có input/output search contract nêu trên;
- C01 25 instances phải trace được về step-key contract tương ứng (direct/called);
- dot-walk-check exit 0;
- current gate v1 vẫn PASS;
- nếu A02 đã merge trong lúc chạy: chạy thêm `--audit-contracts`; nếu chưa có option thì ghi `A02_NOT_YET`, không chờ vô hạn.
- không sửa CAT-004/UI.

## 8. KQ
Append lane-b/COLLAB:
- coverage 12 process;
- step-key list;
- mapping C01 25 instance → contract source;
- OPEN còn lại;
- NEXT = C02 nếu đủ.

`KQ@MMIM-LANE-B02-20260928-01 XONG|DỪNG`
`KQ@LANE-B B02 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS|BLOCK · contract_process=12 · mapped_C01=<n>/25 · NEXT=<...>`

Dừng.
