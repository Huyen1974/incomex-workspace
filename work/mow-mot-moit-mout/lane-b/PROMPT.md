# PROMPT — LANE B04 · Resolve 2 OPEN process contracts

RUN_ID: MMIM-LANE-B04-20260928-01
PROCESS: CHUNG.APQUYTRINH
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex

Write_Path:
- `work/mow-mot-moit-mout/ban-duyet.html`
- `work/mow-mot-moit-mout/lane-b/COLLAB.md`

## 0. Registry / concurrency
Đọc `../council/REGISTRY.md` READ-ONLY.
Entry CODEX-MMIM-B phải đúng B04 + Reserved_Targets.
Không sửa Registry.
Không đụng topic phương pháp reuse/create / Step→UI đang Council Chat.2 thảo luận.
Không tự thiết kế **mô hình phân tầng**, bộ câu hỏi chuẩn theo tầng, confidence framework, gray-zone policy hay phương pháp chứng minh. B04 chỉ giải quyết 2 contract bằng source hiện có.

## 1. Giữ nguyên 23 contract đã đạt
23/39 contract hiện hành + 27 direct Human Step phải giữ nguyên từng byte ở attrs/spans, trừ đúng hai process OPEN dưới đây nếu được opt-in.

## 2. Chỉ xử lý 2 OPEN
### CHUNG.KIEM
B03 blocker:
- chưa rõ hợp đồng kết quả/đường trả khi **business check không đạt** so với **lỗi máy/system**;
- đầu vào object/check-set chưa đủ rõ.

Đọc NT21 + process definition + error/incident sources hiện có.
Chỉ opt-in nếu source phân biệt được tối thiểu:
`PASS | BUSINESS_BLOCK | SYSTEM_ERROR`
hoặc equivalent đã thực sự có trong nguồn, cùng input/output/return rõ.
Không invent enum nếu source không đủ.

### FORM.TAO
B03 blocker:
- bước `MOUT: định nghĩa đếm · chỉ số` chỉ dành MOUT;
- nhánh MOIT bỏ qua và điểm quay lại chưa rõ.

Đọc process/form sources hiện có.
Chỉ opt-in nếu có thể mô tả branch MOIT/MOUT + return path không mơ hồ bằng evidence.
Nếu chưa đủ, giữ OPEN và nêu **một câu quyết định còn thiếu** để Host/Owner/Chat.2 xử lý.

## 3. JEV
Chỉ dùng nếu source đưa ra 2–5 lựa chọn hữu hạn thật.
State = evidence thô/faithful condensation.
JEV không được tạo semantic branch mới thay nguồn.

## 4. Acceptance
- walk 39 / 0 lỗi.
- contract audit 0 lỗi.
- 23 contract cũ byte-equivalent.
- `resolved=0..2`; total_contract=23+resolved.
- OPEN còn lại có blocker tối giản, rõ yes/no hoặc choice cần chốt.
- không CAT-004/UI.

## 5. KQ
`KQ@MMIM-LANE-B04-20260928-01 XONG|DỪNG`
`KQ@LANE-B B04 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS|BLOCK · resolved=<n>/2 · total_contract=<n>/39 · open=<n> · NEXT=<one thing>`
`COORD · NOW=XONG|DỪNG · NEXT=<...> · BLOCKED_BY=<...> · RESERVED_TARGETS=ban-duyet.html+lane-b/COLLAB.md · LAST_SYNC=D76-D77/B04`

Dừng.
