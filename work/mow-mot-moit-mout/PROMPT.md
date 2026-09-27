# PROMPT — LANE A01 · P0 + Process Gate

RUN_ID: MMIM-LANE-A01-20260928-01
PROCESS: CHUNG.APQUYTRINH
STATUS: Bootstrap duy nhất được Owner D56 cho phép trước khi PROCESS này đã nằm trong catalog. Sau RUN này không còn bootstrap exception.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor: Codex
Write: `workspace_*` root `workspace`
GitHub native/App/API/CLI: READ-ONLY.

## 0. Đọc trước

Đọc:
1. `AGENTS.md` + README D12.
2. `work/mow-mot-moit-mout/COLLAB.md` §0, D36, **D56 P0 + LANE A/B/C**, KQ MOM04.
3. `work/mow-mot-moit-mout/ban-duyet.html`: các vùng `ml3`, `ml5-qt`, `ml5-cho-ai`, tool catalog + K01–K17.
4. `cong-cu/dot-walk-check.py` + 3 tool còn lại để giữ đúng khuôn tool hiện có.
5. File này.

Không đụng UI VPS, Step/UI/79 Master. Đây là Lane A.

### MOM04 baseline đã nghiệm thu — chỉ là evidence inventory

KQ `MMIM-MOM04-20260928-01 XONG` được Host chấp nhận làm baseline:
- 16/16 UI xanh đã kế thừa;
- 84/84 Master;
- help 10/10 + Home;
- ★ browser-only;
- 5 pilot có **470 detailRequirements**;
- false_green=0; loop PASS; regression 3/3.

**Khóa nghĩa:** 470 `detailRequirements` = **kho chi tiết/evidence để tiếp tục làm đầy 5 pilot**. Chúng **KHÔNG phải** 470 Process, KHÔNG phải Human Step, KHÔNG phải UI unique và KHÔNG phải backlog để người đọc/duyệt từng dòng. Lane A không được biến chúng thành catalog/process/tool. Lane B/C sau này chỉ dùng làm nguồn/evidence để suy ra Process/Step/UI và phải gộp theo quy luật.

## 1. Mục tiêu

Biến nguyên tắc Owner thành chuỗi có thể tuân thủ:

`Yêu cầu → PROCESS hợp lệ → Tool bắt buộc → Gate PASS → READY/RUN → KQ/evidence`.

Nếu không có process hoặc process sai → **BLOCK**, sửa/tạo process trước rồi mới làm việc.

## 2. P0 — đăng ký process mỏ neo

Đăng ký trong **CAT-003 / khối process live `ml5-cho-ai`**:

- Mã: `CHUNG.APQUYTRINH`
- Tên cố định: `Áp dụng quy trình trước khi làm`
- Thuộc: `🔁`
- Trạng thái: `TẠM CHỐT · v1`
- Nguồn quyết định: `D56 · Owner 28/09/2026`
- Tool bắt buộc: `dot-process-gate`

Nội dung v1, không được làm phức tạp hơn:

1. 🤖 Đọc yêu cầu/RUN; tra CAT-003 process + CAT-006 tool.
2. 🤖 Có process phù hợp → kiểm tool bắt buộc.
3. 👤/🤖 Không có process → DỪNG; rà trùng/chồng; đề xuất + tạm chốt process rồi quay lại.
4. 👤/🤖 Process sai/lạc hậu/chồng chéo → DỪNG; sửa/version, giữ mã+tên+lịch sử rồi quay lại.
5. 🤖 Gate PASS → mới được READY/RUN.
6. 🤖 Sau thực thi ghi KQ/evidence/gap; nếu thực tế không khớp process → quay lại bước 4.

Khi biểu diễn theo khuôn `ml5-cho-ai`, dùng các dòng master hiện có phù hợp. Không invent dòng master chỉ để tool walk PASS. Mỗi bước phải ít nhất đọc CAT-003/CAT-006 hoặc ghi đúng nơi đã có.

### Số đếm live

Vì thêm process thật:
- nhóm `🔁 Dùng chung`: 7 → **8**;
- process catalog hiện hành: 38 → **39** ở các summary live/current.
- Chỉ sửa **summary hiện hành**, KHÔNG thay số 38 trong báo cáo lịch sử/KQ cũ.
- Cập nhật comment expected của `dot-walk-check.py` nếu chỉ là mô tả baseline; không hardcode kiểm số 39 vào logic.

Chạy `dot-walk-check.py` sau sửa; phải exit 0.

## 3. Tool mới — dot-process-gate

Được tạo đúng 1 file:
`work/mow-mot-moit-mout/cong-cu/dot-process-gate.py`

Khuôn header giống 4 tool hiện có.

### Input

```
python3 dot-process-gate.py --prompt <PROMPT.md> --catalog <ban-duyet.html> [--json]
```

### Gate v1 bắt buộc kiểm

1. PROMPT có **đúng một** dòng `PROCESS: <CODE>`.
2. CODE đúng format `[A-Z0-9_]+\.[A-Z0-9_]+`.
3. CODE tồn tại **đúng một lần như process definition** trong `ml5-cho-ai`.
4. Process có nhãn `Thuộc` hợp lệ 🏗/⚙️/🔁/📦.
5. Process có ít nhất 1 step parse được.
6. Nếu prompt dùng `PROCESS: CHUNG.APQUYTRINH`, sau bootstrap tool phải PASS chính RUN này.
7. Không tìm process bằng text tự do ngoài catalog canonical.

Output người:
`PROCESS_GATE PASS|BLOCK · process=<code> · catalog=<sha256> · reason=<...>`

`--json`: ít nhất
`status, process, catalog_sha256, prompt_sha256, reason, process_count`.

Exit:
- 0 PASS
- 1 BLOCK nghiệp vụ/gate
- 2 lỗi input/parse.

Không network, không secret, chỉ stdlib, không ghi file.

### Exact duplicate tối thiểu

Tool phải BLOCK nếu:
- process code trùng;
- cùng một **tên process chuẩn hóa** xuất hiện >1 process definition.

**Semantic overlap không được giả vờ đã giải quyết.** Ghi rõ K11 còn thiếu tool/decision sâu cho overlap phạm vi/ý nghĩa.

## 4. Đăng ký tool + phạm vi cưỡng chế

Trong tool catalog hiện hành:
- thêm `dot-process-gate*`;
- Thuộc: `🔁`;
- trạng thái sau RUN: `đã thử` nếu acceptance đạt, chưa được tự nâng `sẵn dùng`.

Thêm phạm vi kiểm mới:
- `K18 · Tuân thủ quy trình trước RUN`
- miền: `governance.process · gate`
- tool: `dot-process-gate*`.

K11 `Trùng quy trình (tên · phạm vi)`:
- sau tool này có thể ghi **exact code/name = có tool**;
- semantic overlap vẫn OPEN, chưa được tô đủ/sẵn dùng.

Cập nhật số phạm vi hiện hành 17 → **18** nơi live/current; không sửa lịch sử cũ.

## 5. E1 — cơ chế cưỡng chế từ RUN sau

Ghi vào COLLAB ở D57/KQ:

**Từ RUN kế tiếp của task này:**
- Host không được ghi READY nếu PROMPT thiếu `PROCESS:`.
- Trước READY, Host/Executor phải chạy `dot-process-gate.py`; chỉ PASS mới READY.
- Codex/Agent khi nhận RUN phải tự chạy gate trước mutation; FAIL → KQ DỪNG.
- KQ phải chứa `PROCESS=<code>` + `PROCESS_GATE=PASS`.

Đây là E1. **Không tự sửa root AGENTS/gateway trong RUN này.**
E2/E3 là lượt sau sau khi E1 được kiểm thật.

## 6. Lane persistence

Giữ D56:
- A = nền/cưỡng chế/catalog/tool.
- B = process/model/JEV.
- C = Step/UI.

Bổ sung dòng trạng thái hiện hành:
- `LANE A = A01 đang bootstrap P0/gate`
- `LANE B = BLOCKED_BY_A01`
- `LANE C = BLOCKED_BY_A01`.

Không phát RUN B/C.

## 7. Acceptance

1. `CHUNG.APQUYTRINH` có đúng 1 definition trong catalog, mã/tên cố định.
2. `dot-walk-check.py ban-duyet.html --json` exit 0; process count=39; 🔁=8.
3. `dot-process-gate.py --prompt PROMPT.md --catalog ban-duyet.html` PASS.
4. Negative test: prompt không PROCESS → BLOCK exit 1.
5. Negative test: PROCESS không tồn tại → BLOCK exit 1.
6. Negative test: duplicate exact code/name fixture in-memory/temp → BLOCK; không mutation repo.
7. Tool catalog có dot-process-gate, trạng thái không cao hơn `đã thử`.
8. K18 tồn tại; tổng live scope=18.
9. K11 ghi đúng: exact duplicate có kiểm; semantic overlap OPEN.
10. Không đổi UI/Step/Master code/name.
11. Không file mới ngoài `cong-cu/dot-process-gate.py`.
12. Ghi:
`KQ@MMIM-LANE-A01-20260928-01 XONG`
hoặc DỪNG.
13. KQ line:
`KQ@LANE-A A01 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS|BLOCK · HEAD=<sha> · NEXT=<một việc>`.

Báo Owner:
`XONG · A01 · P0=PASS · process=39 · shared=8 · gate=PASS · scopes=18 · K11_semantic=OPEN · NEXT=<...>`

## 8. Dừng

XONG cũng dừng.
Không tự làm A02/B/C.
