# PROMPT — LANE C03 · Chứng minh công thức 25 → 15 Human Step

RUN_ID: MMIM-LANE-C03-20260928-01
PROCESS: CHUNG.APQUYTRINH
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex
Write_Path: chỉ `work/mow-mot-moit-mout/lane-c/COLLAB.md`.
Canonical + root ui: READ-ONLY.

## 0. Registry / phạm vi
Đọc `../council/REGISTRY.md` READ-ONLY.
Entry CODEX-MMIM-C phải đúng C03 + Reserved_Targets.
Không sửa Registry.
Không bind Step→UI, không thiết kế reuse/create, không xử lý gray-zone methodology của Chat.2.
Không suy rộng DERIVATION_RULE_V1 thành mô hình phân tầng hay phương pháp luận tổng quát; C03 chỉ là **một phép thử tái lập cụ thể** để cung cấp evidence cho Chat.2.

## 1. Câu hỏi duy nhất
C02 nói 25 Human Step instance → 15 Human Step chuẩn.
C03 phải trả lời:
**“Công thức nào tạo ra số 15 và một agent khác có tái lập được mà không dựa vào trí nhớ/ý kiến của C02 hay không?”**

## 2. Nguồn cố định
- C01: 25 instance.
- B02R1: map 25/25 → contract source.
- 12 B02R1 contract-v1 / 15 direct step-key nguồn của MOW.
- C02 table 15 groups chỉ dùng để **đối chiếu kết quả**, không làm input cho grouping.

B03/B04 contract ngoài 12 nguồn này không được làm thay đổi kết quả C03.

## 3. DERIVATION_RULE_V1
Viết ngắn gọn, máy/người đều hiểu:
1. **Expand** call graph: cách một instance được tạo, optional branch xử lý thế nào.
2. **Extract signature** đúng 6 thành phần:
   `intent · human_input · output · state_transition · right_class · return_point`.
3. **Normalize**: chỉ các chuẩn hóa cú pháp được phép; cấm semantic merge bằng tên gần giống.
4. **Group equality**: hai instance cùng canonical H khi và chỉ khi 6-tuple tương đương theo rule đã khai báo.
5. **Stable ID/source**: ưu tiên step-key nguồn; nếu nhiều step-key cùng signature phải ghi evidence riêng.
6. **Stable ordering**: quy tắc thứ tự output để hai lần chạy cho cùng kết quả.

## 4. Reproduction test
Dùng scratch/temp, không tạo source file mới.
Từ **input evidence trước C02 grouping**, tạo bảng machine-readable rồi áp DERIVATION_RULE_V1.
Phải báo:
- instances_in=25;
- groups_out;
- member coverage=25/25;
- duplicate/orphan;
- hash của input normalized + output normalized;
- so với C02: match 15/15 hay mismatch cụ thể.

Nếu cần bất kỳ phán đoán semantic thủ công để đạt 15 → **không được tuyên bố deterministic**; phải chỉ ra đúng chỗ human/JEV decision còn chen vào.

## 5. Độ tin cậy
Phân biệt:
- deterministic/exact;
- evidence-backed but semantic;
- unresolved.

Không dùng JEV nếu equality rule đủ.
Không suy UI.

## 6. Output nhìn cái hiểu ngay
Mặt đầu KQ tối đa 8 dòng:
`25 instance → [rule] → 15 group`
+ 6-tuple
+ coverage
+ deterministic YES/NO
+ số điểm còn cần judgment.

Chi tiết gập dưới.

## 7. KQ
`KQ@MMIM-LANE-C03-20260928-01 XONG|DỪNG`
`KQ@LANE-C C03 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS|BLOCK · instances=25 · groups=<n> · deterministic=YES|NO · judgments=<n> · match_C02=<n>/15 · NEXT=<one thing>`
`COORD · NOW=XONG|DỪNG · NEXT=<...> · BLOCKED_BY=<...> · RESERVED_TARGETS=lane-c/COLLAB.md · LAST_SYNC=D76-D77/C03`

Dừng.
