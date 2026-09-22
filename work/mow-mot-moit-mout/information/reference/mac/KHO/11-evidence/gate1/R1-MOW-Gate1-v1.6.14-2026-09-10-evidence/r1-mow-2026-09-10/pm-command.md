# Lệnh giao Codex — PM đóng Gate 0, mở R1/Gate 1 và cập nhật SSOT một lần

**PM: GPT Chat · 10/09/2026**  
**SSOT duy nhất phải cập nhật:** `/Users/nmhuyen/Desktop/quy trình/cấu trúc hệ thống.html`  
**Current trước lượt này:** v1.6.13  
**Nguồn evidence:** `Proof-Gate0-UI-Runtime-2026-09-10-evidence.zip` và các evidence Proof A/B/cổng ghi đã có trong workspace.

Đây là **một lệnh duy nhất** gồm:
1. ghi nhận quyết định PM đóng Gate 0;
2. thực hiện R1/Gate 1 cho riêng MOW bằng actual evidence;
3. cập nhật SSOT đúng **một lần ở cuối**.

Không tạo tài liệu kiến trúc song song.

---

# 1. QUYẾT ĐỊNH PM — CÓ HIỆU LỰC NGAY

Sau khi PM kiểm gói `Proof-Gate0-UI-Runtime-2026-09-10-evidence.zip`:

- manifest: 199/199 file kiểm được khớp SHA-256;
- UI declaration V1→V2: PASS;
- browser write/read-back/422/409/replay: PASS trong bounded lab;
- write-gate scoped authority/write/audit: PM ACCEPT từ lượt trước;
- autonomous runtime: event→Instance→Attempt→safe AUTO effect→result→native completion/ACK chạy không Agent ở giữa;
- duplicate occurrence không tạo effect thứ hai;
- ba occurrence hợp lệ cùng case tạo ba lượt hợp lệ;
- immutable TEST release V1 vẫn được Instance cũ dùng sau khi binding chuyển V2;
- queued work được xử lý sau restart worker;
- service identity/audit correlation có evidence;
- lab cleanup và demo safety có evidence;
- product candidate code vẫn generic, không per-MOW/per-Field branch.

## PM VERDICT

### Gate 0 · Feasibility

**ACCEPT / DONE trong phạm vi Gate 0.**

Ý nghĩa chính xác:

> Đã có đủ actual evidence để kết luận kiến trúc có **một đường triển khai tối thiểu khả thi** trên stack hiện tại, với PG giữ truth, Directus làm API/quyền/audit và Nuxt render/tương tác; phần nối custom chỉ xuất hiện tại gap đã có evidence.

Không có nghĩa:

- production-ready;
- O1/O2/O3 VERIFIED;
- full HMITL/NTGV;
- full release governance;
- production login/auth/delegation hoàn tất;
- crash/load/backpressure/DR đã PASS;
- Directus/Nuxt target upgrade đã rehearsal;
- mọi 21 capability đã PROVEN.

### W002-FEAS

**PM Verdict: ACCEPT WITH FOLLOW-UP / DONE cho accepted Gate0 scope.**

Follow-up không giữ Gate0 mở; route đúng Gate sau.

### Proof A

**PM ACCEPT cho Gate0 bounded scope:**
- retrieval path;
- bounded reuse/admission behavior đã đo;
- draft/write/read-back;
- fresh-Agent resume;
- declaration-only change làm UI thay đổi.

Full catalog/admission scale, full authoring lifecycle, publish governance → Gate3–7.

### Proof B

**PM ACCEPT cho Gate0 bounded authority/write/audit scope.**

Full production identity/delegation/security coverage → Gate3–6.

### Proof C

**PM ACCEPT cho Gate0 bounded autonomous runtime scope.**

`pg-boss 12.30.0` là **FEASIBILITY RUNTIME CANDIDATE**, không production architecture cuối cùng.

Full failure matrix, kill giữa effect/ACK, terminal fail, load/backpressure, DR, retention/telemetry → Gate5–7.

### Custom candidates

Giữ đúng phân loại:

- write guard Directus: feasibility candidate;
- generic UI submit adapter: feasibility candidate;
- pg-boss + generic worker: feasibility runtime candidate.

Không promote thành production-final chỉ vì Gate0 DONE.

Trước canonical build/deploy phải tiếp tục Reuse Ladder, kể cả **TARGET-VERSION BUILT-IN**.

---

# 2. MỘT LƯU Ý QUAN TRỌNG TỪ PM REVIEW

Runtime candidate hiện tại được chấp nhận vì worker rất mỏng:

```text
event
→ immutable release pin
→ pg-boss delivery
→ Instance/Attempt
→ registered generic Capability
→ guarded write
→ result
→ pg-boss completion/ACK
```

Business truth vẫn ở PG/release/declaration.

Không được phát triển worker thành nơi chứa:

- branch nghiệp vụ;
- NTGV;
- approval;
- per-workflow code;
- “latest version” resolution;
- business validation song song.

Nếu các thứ trên xuất hiện trong worker ở Gate sau → phải REOPEN architecture fit.

UI adapter cũng chỉ là generic transport. `localStorage`, production auth/session, multi-account behavior và conflict UX đầy đủ chưa được chứng minh production; route đúng Gate sau, không giữ Gate0 mở.

---

# 3. SAU KHI GATE 0 ĐÓNG — MỞ GATE 1

## Gate 1 · Canonical UI

Chuyển:

- Gate0 → **DONE**
- Gate1 → **DOING**
- W003 / R1 → **ASSIGNED/DOING** trong lượt này
- R2–R9 vẫn BACKLOG
- Gate2–7 chưa bắt đầu
- O1–O3 vẫn NOT VERIFIED

Không mở Gate2.

Không build UI.

Không deploy production.

---

# 4. NHIỆM VỤ THỰC THI DUY NHẤT SAU GATE0: R1 · MOW

R1 chỉ rà **MOW**, không rà toàn hệ thống.

Nguồn candidate hiện đã ghi trong SSOT:

- U02;
- U03;
- U04;
- MOW Master;
- Canvas / Unified Canvas;
- MODW;
- các route/component/Help hiện hữu liên quan trực tiếp MOW.

Mục tiêu R1:

> Chọn được **đề xuất canonical human path cho MOW** phù hợp kiến trúc AI-declarative-first, hoặc chỉ ra chính xác gap khiến PM chưa thể chọn.

Agent **không tự quyết D03 cuối cùng**. Agent nộp candidate + evidence; GPT Chat/PM quyết.

---

# 5. CÁCH RÀ R1 — KHÔNG ĐỂ UI KÉO SẢN PHẨM QUAY VỀ MANUAL-FIRST

North Star vẫn giữ:

> User nêu ý tưởng → AI dựng/tra/khai phần lớn → máy kiểm → người chỉ review nghĩa/quyền/ngoại lệ → UI phản ánh cùng dữ liệu → runtime dùng đúng version.

Vì vậy khi rà từng UI MOW, phải hỏi:

### 5.1. Vai trò

UI đó phù hợp nhất là:

- primary Workspace;
- expert editor;
- library/master;
- graph visualizer;
- runtime monitor;
- legacy/demo/fallback?

Không mặc định UI có nhiều control nhất là primary.

### 5.2. Human path

Người có bị bắt:

- tự tìm từng MOT/Field;
- tự gõ lại ID;
- tự cấu hình từng step;
- nhớ tool kế tiếp;
- chuyển qua nhiều Master để hoàn tất;
- chạy test thủ công?

Nếu có, ghi rõ đó là expert/fallback hoặc GAP so với default path.

### 5.3. Agent path

Kiểm UI có thể:

- đọc MOW do Agent tạo từ canonical data;
- hiển thị đúng ID/version/revision;
- refresh sau Agent write;
- không giữ JSON/business truth riêng;
- không yêu cầu Agent click UI để khai báo.

### 5.4. Ownership

MOW UI chỉ sửa phần MOW sở hữu:

- graph/order/dependency;
- branch/join;
- MOW-level trigger/binding/routing/handoff/timing/error.

Không sửa trực tiếp Definition của:

- MOT;
- MOIT/MOUT;
- Field;
- Trigger/Condition dùng chung;
- NTGV/People.

Màn gộp được phép mở đúng editor chủ quản nhưng không đổi ownership.

### 5.5. Golden Path fit

Map candidate vào G1–G8:

- Intent;
- Reuse;
- Draft;
- Resolve/readiness;
- Decision;
- Test;
- Approval;
- Publish/Activate.

Không cần tám màn.

Phải chỉ ra:

- stage nào UI phục vụ;
- stage nào Agent/system tự làm;
- stage nào cần một view;
- gap nào thuộc Gate2.

### 5.6. Reuse

Kiểm candidate có thể phục vụ:

- tìm existing MOW;
- exact/near candidate;
- where-used/impact;
- diff/version;
- không CREATE trước rồi mới tìm duplicate.

Nếu hiện chỉ mock → ghi MOCK / NOT CONNECTED.

### 5.7. Data truth

Phân biệt bằng actual evidence:

- đọc data thật;
- write data thật;
- mock/static/local state;
- UI preview;
- source tồn tại nhưng chưa deploy.

Không suy từ giao diện đẹp.

---

# 6. EVIDENCE R1 PHẢI THU

Ưu tiên actual current environment và source hiện hữu.

Không sửa UI.

Với mỗi candidate U02–U04/MOW-related path, nộp tối thiểu:

1. URL/route;
2. screenshot/browser evidence current;
3. Help/text semantics;
4. source/component nếu cần để xác định behavior;
5. data/API calls nếu quan sát an toàn được;
6. đọc thật hay mock;
7. write thật hay mock;
8. actor/authority path nếu có;
9. vai trò đề nghị;
10. gap so với AI-declarative-first path.

Không cần quét toàn repo.

Không gọi save/approve/activate nguy hiểm trên production.

Read-only trước.

Nếu cần thử write để xác định behavior, chỉ trên fixture/lab được phép và phải bảo toàn demo như các proof trước.

---

# 7. OUTPUT R1 CHO PM

Lập một bảng ngắn:

| Candidate | Vai trò phù hợp | Actual connected? | Điểm mạnh | Gap | Giữ / ghép / fallback / retire-candidate | Evidence |
|---|---|---|---|---|---|---|

Sau đó đề nghị:

### `R1 CANONICAL CANDIDATE`

Một trong:

- `CANDIDATE READY FOR PM DECISION`
- `PARTIAL — cần đúng evidence X`
- `NO CURRENT CANDIDATE FIT — Gate2 cần generic gap Y`

Không tự quyết D03.

Không build gap.

---

# 8. CẬP NHẬT SSOT — BẮT BUỘC, CHỈ MỘT LẦN Ở CUỐI

Sau khi R1 có actual evidence, cập nhật **chính file**:

`/Users/nmhuyen/Desktop/quy trình/cấu trúc hệ thống.html`

lên version kế tiếp, dự kiến **v1.6.14**.

Backup v1.6.13 trước khi ghi.

Không tạo một “SSOT mới”.

Archive snapshot read-only chỉ là evidence.

## 8.1. Phải nhập đầy đủ quyết định Gate0 mới

Cập nhật đồng bộ:

- Owner Cockpit;
- gate strip;
- Current Review;
- PM Control Panel;
- Work Queue;
- CURRENT STATE;
- W002-FEAS;
- Proof A;
- Proof B;
- Proof C;
- Gate0 active/exit;
- Custom Code Register;
- Capability Matrix các hàng đã có bounded evidence;
- RUN-01;
- findings FEA-F02/FEA-F05 nếu current conclusion đổi;
- Decision Log;
- History;
- footer.

Thêm acceptance record rõ:

```text
Gate0 / W002-FEAS
PM Verdict: ACCEPT WITH FOLLOW-UP
Accepted Scope: bounded feasibility implementation path
Evidence: Proof A + scoped write gate + UI/runtime Gate0 package
Accepted by: GPT Chat / PM
Accepted date: 10/09/2026
Follow-up: Gate1–7 theo đúng scope; target platform rehearsal trước canonical build khi đến dependency
```

## 8.2. Sweep câu current bị stale

Tìm toàn file và xử lý current occurrences như:

- `Gate0 DOING`;
- `READY FOR PM GATE0 EXIT REVIEW`;
- `PM REVIEW / PARTIAL` của A/B/C nếu đang nói current Gate0 scope;
- `SUBMITTED` của proof đã PM nhận;
- `runtime chưa nghiệm thu` nếu đang nói bounded Gate0;
- `chưa mở rà UI`;
- `NEXT: PM review Gate0`;
- `0 năng lực đã chứng minh trọn vẹn` ở Owner summary nếu diễn đạt này gây hiểu sai sau bounded proof.

Không xóa lịch sử.

Dòng historical giữ ngày/version/HISTORICAL.

D1/D2 hoặc capability nào vẫn PARTIAL cho **full target contract** có thể giữ PARTIAL; chỉ phải ghi rõ nó không còn là Gate0 blocker.

## 8.3. Capability Matrix

Không tô cả 21 nhóm PROVEN.

Chỉ cập nhật exact evidence:

- Input/form: bounded declarative render + submit;
- Permission/write/audit: bounded proven path;
- AUTO executor: bounded pg-boss candidate;
- Runtime Instance/Attempt: bounded proof;
- Retry/idempotency: duplicate/replay bounded proof;
- Event/correlation: bounded proof;
- version/pin: immutable TEST fixture proof.

Cột “Missing / proof” phải giữ production/full-scope gaps.

Nếu Fit của toàn capability vẫn PLAUSIBLE thì giữ PLAUSIBLE và ghi **bounded sub-contract PROVEN** trong evidence.

## 8.4. Gate states mới

Sau PM acceptance:

- Gate0 = DONE;
- Gate1 = DOING;
- W003/R1 = PM REVIEW hoặc SUBMITTED sau khi Agent hoàn tất R1;
- Gate2–7 = NOT STARTED;
- O1–O3 = NOT VERIFIED.

Không chuyển O1/O2 thành VERIFIED từ Gate0 lab.

## 8.5. R1 evidence

Nhập R1 actual evidence vào đúng:

- Current Review;
- W003 card;
- U02–U04 evidence rows;
- D03 current status;
- MOW object card;
- UI evidence section;
- Decision/Risk nếu có;
- Next Action.

Không append correction chồng câu cũ; sửa câu current tại nguồn và giữ history.

---

# 9. PLATFORM / CODE DISCIPLINE SAU GATE0

Gate1 là review/chọn UI, **không build**.

`PLATFORM FREEZE` vẫn phải giải trước Gate2 bulk UI work.

`RULE-SYNC-01` vẫn phải hoàn thành trước build thật.

Target-stack rehearsal/MIG1 không được xóa chỉ vì current lab PASS.

Nhưng cũng không kéo MIG1 ngược lại thành blocker để mở lại Gate0 đã được PM ACCEPT.

Code mới trong R1 = **0**, trừ harness/viewer read-only thật sự cần cho evidence; nếu có phải kê riêng, không product code.

---

# 10. BÁO CÁO CHO OWNER — TỐI ĐA 10 Ý

Báo ngắn:

1. Gate0 đã được PM ACCEPT/DONE chưa ghi ở đâu.
2. SSOT version sau update.
3. Gate1/R1 đã kiểm candidate MOW nào.
4. Candidate nào phù hợp nhất và vai trò gì.
5. Candidate nào chỉ nên expert/fallback.
6. UI nào đang mock/chưa nối thật.
7. Human path có chỗ nào manual-first không.
8. Agent path có đọc cùng data/revision không.
9. D03: READY FOR PM DECISION hay còn blocker gì.
10. Next action duy nhất đề nghị cho PM.

Không gửi Owner danh sách hàng trăm file/log.

---

# 11. STOP RULE

Lượt này **không được**:

- sửa/build MOW UI;
- mở R2–R9;
- mở Gate2;
- nâng Directus/Nuxt;
- deploy worker/guard;
- production schema;
- full MIG1;
- chuẩn hóa toàn catalog;
- thêm framework/tool mới;
- sửa outcome thành VERIFIED;
- tự quyết D03.

Nếu phát hiện candidate UI không fit, nộp gap thật.

Không xây ngay để che gap.

---

## Kết luận điều hành

Gate0 đã hoàn thành mục tiêu của nó:

> chứng minh rằng kiến trúc **có thể triển khai được thật** bằng PG + Directus + Nuxt, với phần custom generic tối thiểu tại các gap đã được đo.

Từ đây không tiếp tục chứng minh lại feasibility.

Bắt đầu Gate1 bằng câu hỏi sản phẩm cụ thể:

> **Trong những UI MOW đã có, đâu là cửa mặc định tốt nhất để con người review/ngoại lệ trong một hệ mà AI khai phần lớn — và các UI còn lại nên giữ vai trò gì?**

R1 phải trả lời câu đó bằng actual evidence; GPT Chat/PM mới quyết canonical.
