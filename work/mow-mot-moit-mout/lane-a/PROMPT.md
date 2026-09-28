# PROMPT — LANE A06 · Audit 4 Master List cốt lõi

RUN_ID: MMIM-LANE-A06-20260928-01
PROCESS: VEUI.MOW
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex

Write_Path:
- root=ui: chỉ `master-of-master-v1.html`, `master-home-v1.html`, `ui-child-content-v1.js` nếu cần để hiển thị audit;
- root=workspace: chỉ append KQ vào `work/mow-mot-moit-mout/lane-a/COLLAB.md`.
Canonical nghiệp vụ/process/tool/step/UI registry: READ-ONLY.

## 0. Registry / concurrency
Đọc `../council/REGISTRY.md` READ-ONLY.
Entry CODEX-MMIM-A phải đúng RUN A06 + Reserved_Targets. Mismatch → DỪNG COORD_CONFLICT.
Không sửa Registry.
Không nghiên cứu/phát triển phương pháp reuse/create hoặc Step→UI; topic đó đang reserved cho Council Chat.2.

## 1. Mục tiêu duy nhất
Làm cho Owner **nhìn cái hiểu ngay vấn đề nằm ở đâu** đối với đúng 4 Master List:
1. Process: `CAT-003?`
2. Tool: `CAT-006`
3. Step: `CAT-004`
4. UI inventory: `CAT-235*`

Không tạo list mới. Không “làm đẹp” bằng cách gắn ✓.
Chỉ audit nội dung thật hiện có và hiển thị verdict/evidence.

## 2. Luật verdict
- ✓ = có một nghĩa rõ, có list thật, row có nội dung chính, mở detail/source được.
- ◐ = có evidence/list một phần nhưng thiếu detail hoặc chưa canonical/chưa đủ nguồn.
- ! = có xung đột nghĩa/population khiến một Master đang đại diện hai thứ khác nhau.
- ○ = chưa có list/evidence.

Tên/mã/link/UI route tồn tại không đủ ✓.

## 3. Evidence bắt buộc
### Process CAT-003?
So sánh riêng:
- UI-001 List MOW baseline 7 row;
- canonical process definitions tại `ban-duyet.html#ml5-cho-ai` hiện 39 process;
- Master label/purpose hiện hành.
Nếu đây là hai population/meaning khác nhau, phải hiện rõ conflict; không tự gộp.

### Tool CAT-006
Kiểm:
- `ban-duyet.html#mom-tool-catalog` hiện 29 ứng viên;
- file thật `cong-cu/`;
- row/detail/source/cách chạy/status có hay chưa.
Không gọi 29 ứng viên là 29 tool production.

### Step CAT-004
Kiểm riêng:
- `workflow_steps 105` đang là gì;
- C02 có 25 instance → 15 Human Step chuẩn **chỉ cho MOW**;
- có/không một canonical Step List mà người dùng mở từng dòng được.
Không biến 105 hoặc 15 thành “toàn hệ thống” nếu source không chứng minh.

### UI inventory CAT-235*
Kiểm:
- `child-ui-registry.json` / directory thực;
- số UI/frames/routes/detail;
- phân biệt **UI inventory hiện có** với **UI cần cho Human Step** (C02 đang UNKNOWN).

## 4. Hiển thị
Trong Master of Master / Master Home, với đúng 4 record, thêm/refresh audit metadata ngắn:
`List <✓|◐|!|○> · count/evidence · một câu vấn đề`.
Drill-down phải có:
- What exists
- What it means
- Source + hash/version
- Conflict/gap
- NEXT

Không copy toàn catalog vào Master of Master.
Không đổi code/name Master trong RUN này.

## 5. Acceptance
- 84 Master giữ đủ.
- Chỉ 4 record audit được chạm.
- Owner nhìn Master of Master thấy ngay 4 trạng thái + vấn đề.
- CAT-003? nếu 7 MOW và 39 process khác nghĩa thì không được ✓.
- CAT-006 không ✓ nếu chưa có row/detail Master thật.
- CAT-004 không ✓ nếu chưa có canonical Step List đáng tin.
- CAT-235* chỉ ✓ nếu UI inventory thực sự có list/detail; vẫn phải ghi `required-from-Step = UNKNOWN`.
- 390/1280 không overflow; console functional error=0.
- Không sửa parent renderer/hashes.

## 6. KQ
`KQ@MMIM-LANE-A06-20260928-01 XONG|DỪNG`
`KQ@LANE-A A06 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS|BLOCK · audited=4/4 · verdicts=<...> · false_green=0 · NEXT=<one thing>`
`COORD · NOW=XONG|DỪNG · NEXT=<...> · BLOCKED_BY=<...> · RESERVED_TARGETS=<A06 targets> · LAST_SYNC=D76-D77/A06`

Dừng.
