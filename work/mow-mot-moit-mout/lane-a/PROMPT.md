# PROMPT — LANE A07 · Rà lỗi tải/tab Owner View

RUN_ID: MMIM-LANE-A07-20260930-01
PROCESS: VEUI.MOW
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex

Write_Path: chỉ append KQ vào `work/mow-mot-moit-mout/lane-a/COLLAB.md`.
`ban-duyet.html`, root ui, canonical khác: **READ-ONLY**.

## 0. Registry / concurrency
Đọc `../council/REGISTRY.md` READ-ONLY.
Entry CODEX-MMIM-A phải đúng A07.
B05 là writer duy nhất của `ban-duyet.html`; A07 tuyệt đối không sửa file đó.

## 1. Vấn đề Owner báo
Mở/chuyển các tab con, đặc biệt ★ Công thức, đôi lúc rất chậm hoặc có cảm giác load/reload nhiều lần.

## 2. Rà kỹ đúng root cause
Đọc current `ban-duyet.html` và kiểm UI thật.
Bắt buộc kiểm ít nhất:
1. kích thước HTML / DOM;
2. hidden tab có iframe/srcdoc/tài nguyên nặng vẫn load từ đầu hay không;
3. logic tab: `show / write / restore / hashchange / popstate / scrollIntoView`;
4. `details toggle` có ghi hash/history quá nhiều hay gây restore/scroll lặp;
5. iframe/srcdoc trong Step quy trình 2 và các panel khác có làm tăng thời gian parse/load;
6. click tab có thực sự reload network/document hay chỉ DOM/hash/scroll khiến Owner cảm giác reload.

Không đoán. Mỗi root cause phải có source/measurement/evidence.

## 3. Output
Mặt đầu tối đa 8 dòng:
- Root cause 1/2/3 theo mức ảnh hưởng;
- cái nào PROVEN, cái nào SUSPECT;
- patch nhỏ nhất đề nghị;
- rủi ro patch.

Sau đó đưa patch plan chính xác theo vùng/hàm, **không áp patch trong A07**.

## 4. Acceptance
- Không sửa canonical/UI.
- Phân biệt rõ reload thật vs re-render/hash/scroll.
- Có before metrics tối thiểu: file bytes, iframe count, srcdoc count, details count, listener/hash behavior.
- Đề xuất patch không làm mất deep-link/tab state.
- NEXT duy nhất = A08 patch sau khi B05 xong.

## 5. KQ
`KQ@MMIM-LANE-A07-20260930-01 XONG|DỪNG`
`KQ@LANE-A A07 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS|BLOCK · causes=<n> · proven=<n> · suspect=<n> · NEXT=A08_PATCH_AFTER_B05`
`COORD · NOW=XONG|DỪNG · NEXT=A08_PATCH_AFTER_B05 · BLOCKED_BY=<...> · RESERVED_TARGETS=lane-a/COLLAB.md · LAST_SYNC=FORMULA-01/A07`

Dừng.
