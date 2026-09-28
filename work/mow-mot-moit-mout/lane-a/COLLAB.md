# COLLAB — MMIM Lane A · Gate / Catalog Law / Tool

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — Owner 28/09/2026 yêu cầu Lane A/B/C bền qua phiên; Lane A phụ trách nền tích lũy, gate, tool và luật catalog.

### 1. Mục tiêu
Biến Process/Tool đã chốt thành dữ liệu có thể kiểm bằng máy; không phụ thuộc trí nhớ phiên.

### 2. Thế nào là hoàn thành
A02 nâng process-gate để kiểm được contract metadata của Human Step mà B02 chuẩn hóa, nhưng không phá E1 và không sửa canonical Process.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Canonical Process: `../ban-duyet.html#ml5-cho-ai`.
- Tool source: `../cong-cu/dot-process-gate.py`.
- A02 chỉ sửa tool + COLLAB lane A.
- KQ mới nhất: **A02 XONG · Host nghiệm thu; mở A03 tương thích parser**, bằng chứng A02 bên dưới.
- A03: sửa duy nhất `dot-walk-check` để chấp nhận process attrs trên `p`; canonical READ-ONLY.
- HOST GATE · PASS · PROCESS=`CHUNG.APQUYTRINH` · catalog=`ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7` · prompt=`7e2a3446298e206c2e649445d2fe5cd30d22737e8cf5dac55b2c79e16ce9ad53`.
- READY@f69af7bbacd92b3c46bbcb873059054a83ab655a · RUN_ID `MMIM-LANE-A03-20260928-01`.
- RUN ISSUED · chỉ sửa dot-walk-check + lane-a/COLLAB; B/C chờ; XONG/DỪNG rồi dừng.
- HOST GATE · PASS · PROCESS=`CHUNG.APQUYTRINH` · catalog=`ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7` · prompt=`af0cd3aa4b889507becb0334c6a2ad2bff090da202f0bf751b03c7a7dbc7b14e`.
- READY@f39ca2ded193af84048937452c937923348ec6b1 · RUN_ID `MMIM-LANE-A02-20260928-01`.
- RUN ISSUED · chỉ gate tool + lane-a/COLLAB; canonical ban-duyet READ-ONLY; XONG/DỪNG rồi dừng.

### Vòng trước
A01 đã PASS: process=39 · shared=8 · scopes=18 · E1 gate PASS.

### A02 · KQ · 2026-09-28
KQ@MMIM-LANE-A02-20260928-01 XONG
KQ@LANE-A A02 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS · contract_gate=PASS · NEXT=Host nghiệm thu A02 cùng B02, rồi mới xét C02.

- Áp: `8fc042022fa93deedfa3e37e8973f02f1e6d9fda` (lượt đầu) + SAME_COMMIT (đính chính); chỉ sửa `../cong-cu/dot-process-gate.py` và COLLAB Lane A; `../ban-duyet.html` read-only.
- Gate trước ghi: `CHUNG.APQUYTRINH` PASS · process_count=39 · step_count=6 · catalog `ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7` · PROMPT `af0cd3aa4b889507becb0334c6a2ad2bff090da202f0bf751b03c7a7dbc7b14e`.
- Công cụ v2: chỉ process `data-contract-v="1"` mới bị kiểm 5 thuộc tính process, 6 thuộc tính cho từng Human Step trực tiếp, mã bước duy nhất toàn catalog, quyền/UI-intent theo bộ giá trị; `--audit-contracts` chỉ đọc và xuất coverage/lỗi.
- Thử thật trên bản nguồn trước ghi: E1 v1/v2 cho catalog hiện hành **trùng kết quả JSON và exit 0**; 13/13 fixture PASS (đủ metadata, thiếu từng loại, trùng mã bước, quyền/UI-intent sai, machine-only, old process, audit coverage/lỗi); ca máy→người→máy PASS 3 bước/1 Human Step; `py_compile` PASS.
- Audit catalog hiện hành: process=39 · opt-in=0 · Human Step opt-in=0 · errors=0 · unversioned=39. Đây là kiểm tương thích; contract thật do B02 gắn vào canonical và Host nghiệm thu sau.
- Giới hạn: kiểm **sự có mặt/hình thức**, chưa xác nhận đúng nghĩa quyền/state/đường quay về; không E3 hard block. Không ghi PG/VPS.
- Đính chính sau đọc lại: lượt đầu lưu thiếu 2 chỉnh sửa cuối; bản đính chính giữ JSON E1 v1 nguyên dạng và trả `contract_errors` khi opt-in BLOCK. Đã kiểm lại SHA source và chạy gate sau lưu.
