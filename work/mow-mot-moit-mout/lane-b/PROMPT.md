# PROMPT — LANE B01 · Rà 39 Process + Model + JEV

RUN_ID: MMIM-LANE-B01-20260928-01
PROCESS: CHUNG.TIM
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor: Codex
Write scope: chỉ `work/mow-mot-moit-mout/lane-b/COLLAB.md`.
Canonical parent: READ-ONLY.

## 0. Gate
Đọc `AGENTS.md` → parent `COLLAB.md` D36/D56–D59 → lane-b/COLLAB.md → file này.
Đọc canonical:
- `../ban-duyet.html#ml5-cho-ai` = 39 process definitions.
- `../ban-duyet.html#ml5-qt` = khung/dự tính ≈98, không phải process đã viết.
- `../ban-duyet.html#mom-tool-catalog` + K01–K18.
- `../cong-cu/dot-process-gate.py`.

Trước mutation lane-b/COLLAB, tự chạy:
`python3 ../cong-cu/dot-process-gate.py --prompt PROMPT.md --catalog ../ban-duyet.html --json`.
FAIL → KQ DỪNG, không ghi canonical.

## 1. Việc B01
Rà 39 process hiện có, không nghiên cứu lại toàn bộ repo.

Với mỗi process, rút chữ ký:
`code · name · Thuộc · object · verb/intent · input/trigger · human steps · machine steps · process calls · Master đọc · Master ghi`.

Sau đó:
1. Gom thành tối đa 10 cụm chức năng để người đọc không phải nhìn 39 dòng rời.
2. Tìm:
   - trùng exact (đã có gate);
   - semantic-overlap candidate;
   - cùng việc nhưng tên/mã khác;
   - process gọi nhau vòng/không rõ;
   - lifecycle thiếu (tạo/dùng/sửa/ngừng...);
   - process đã nêu ở ≈98 nhưng chưa có definition;
   - process definition không đủ để C suy Human Step/UI.
3. Mỗi vấn đề ghi: `mã liên quan · loại · evidence · ảnh hưởng · đề xuất ngắn · confidence`.
4. Chỉ đưa **tối đa 10 vấn đề ưu tiên** ở tầng đầu; phần còn lại gập dưới.

## 2. JEV
Chỉ dùng JEV cho case mơ hồ hữu hạn, ví dụ:
- A/B nên gộp hay tách;
- candidate thuộc process hiện có hay process mới;
- overlap thực hay chỉ dùng chung process con.

State phải là evidence thô/faithful condensation, không nhét kết luận.
Không dùng JEV thay exact check/tool cứng.
Nếu phiên không bind JEV: ghi `JEV_UNAVAILABLE`, không giả kết quả.

## 3. Không làm
- không sửa `../ban-duyet.html`;
- không thêm/sửa process canonical;
- không sửa Tool/Step/UI;
- không cấp mã mới;
- không mở 79 Master;
- không tạo file ngoài lane-b/COLLAB.md.

## 4. Output
Append vào lane-b/COLLAB:
- bảng ≤10 cụm process;
- top ≤10 overlap/gap;
- danh sách case đã hỏi JEV + result id/confidence;
- số process đủ/thiếu để C suy Step/UI;
- đề xuất NEXT đúng 1 batch.

KQ:
`KQ@MMIM-LANE-B01-20260928-01 XONG|DỪNG`
`KQ@LANE-B B01 · PROCESS=CHUNG.TIM · PROCESS_GATE=PASS|BLOCK · HEAD=<sha> · process=39 · overlap=<n> · gaps=<n> · NEXT=<một việc>`

Dừng. Không tự B02, không sửa canonical.
