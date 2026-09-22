# Lệnh giao Codex — hoàn tất toàn bộ Gate 1 (R2–R8), chốt bản đồ UI toàn hệ và chuẩn bị điều kiện vào Gate 2

**PM: GPT Chat · 10/09/2026**  
**SSOT duy nhất:** `/Users/nmhuyen/Desktop/quy trình/cấu trúc hệ thống.html`  
**Current:** v1.6.14  
**Nguồn evidence mới nhất:** `R1-MOW-Gate1-v1.6.14-2026-09-10-evidence.zip` và toàn bộ evidence Gate0 đang có trong workspace.

Đây là **một gói việc lớn, trọn vẹn**.  
Không chia thành nhiều prompt nhỏ. Không gửi báo cáo tiến độ từng phần.

**Chỉ báo cáo PM khi:**
1. toàn bộ R2–R8 đã được kiểm xong trong phạm vi freeze;
2. tự QA completeness đã đạt;
3. SSOT đã cập nhật đúng một lần ở cuối;
4. có kết luận `READY FOR PM GATE1 EXIT REVIEW` hoặc một blocker thật sự khiến Gate1 chưa thể khép.

Nếu một candidate hoặc URL lỗi, tiếp tục kiểm các phần còn lại; không dừng giữa chừng để hỏi PM trừ khi có vấn đề an toàn/quyền truy cập khiến toàn gói không thể tiếp tục.

---

# 1. QUYẾT ĐỊNH PM TRƯỚC KHI THỰC HIỆN

## 1.1. PM nhận R1 MOW

**W003 / R1: PM ACCEPT trong phạm vi Gate1 review.**

R1 đã đủ evidence để kết luận:

- 7 URL/vùng MOW đã được rà;
- 139/139 file trong manifest của gói R1 khớp hash khi PM kiểm;
- không candidate hiện tại nào fit nguyên trạng vì đều MOCK / NOT CONNECTED với canonical MOW;
- việc không có candidate fit nguyên trạng **không phải FAIL Gate1**: Gate1 có nhiệm vụ phân vai UI và xác định gap phải ghép ở Gate2, không bắt một mock hiện có tự nhiên trở thành production UI;
- 5 nhóm gap R1 được PM nhận làm input Gate2:
  1. canonical data/context;
  2. intent/reuse/admission;
  3. readiness/diff/test một nguồn;
  4. graph + ownership boundary;
  5. authority/publish + Help drift.

Không build các gap này trong lượt hiện tại.

## 1.2. PM quyết D03 · MOW UI roles

**D03 = DECIDED ở mức vai trò/canonical composition.**

Không chọn nguyên một app mock làm “bản chính”.

Canonical composition cho MOW:

### A. Primary human review pattern
**Drawer ba câu hỏi của Nháp2** là **canonical review pattern** cho con người:

- người xem “có được phát hành không?”;
- “đã nối đủ để chạy chưa?”;
- “chạy xong biết tốt/xấu bằng gì?”;
- mở sâu diff/readiness/graph khi cần.

Đây là **pattern được chọn**, không có nghĩa toàn ứng dụng Nháp2 hiện tại đã production-ready.

### B. MOW Master
**Canonical library / browse / entry khi cần tra cứu MOW hiện có.**

Vai trò:
- tìm/list/filter;
- nơi dùng/version/health sau khi nối thật;
- mở review context.

Không biến Master thành nơi người phải tự lắp workflow bằng tay.

### C. Unified Canvas
**Canonical contextual graph view / expert graph editor candidate.**

Vai trò:
- nhìn topology;
- inspect dependency/branch/join/handoff;
- expert edit khi cần và khi quyền cho phép.

Không là default manual authoring path.

### D. MODW + New MODT T2
**EXPERT / FALLBACK / owner-editor handoff**, không default MOW workspace.

Giữ nội dung hữu ích; không để chúng trở thành nơi sở hữu business truth thứ hai.

### E. Nháp1
**REFERENCE / LEGACY-REFERENCE có chọn lọc**, giữ Help/ý tưởng còn giá trị, không default.

### F. Master list quy trình trùng
**RETIRE-CANDIDATE**, chưa xóa.  
Phải bảo toàn nội dung/đường dùng thật nếu phát hiện consumer trước khi retire ở Gate sau.

## 1.3. Nguyên tắc UI toàn Gate1

North Star không đổi:

> User nêu ý tưởng → AI tìm/reuse/dựng/kiểm phần lớn → người chỉ review nghĩa/quyền/ngoại lệ → UI phản ánh cùng canonical data → hệ thống chạy đúng version.

Do đó:

- UI nhiều control nhất không mặc nhiên canonical;
- một chức năng có thể là library, review, expert editor, runtime workspace hoặc fallback;
- một logical Workspace có thể ghép nhiều view;
- không cần một URL duy nhất;
- default path không được quay về manual-first;
- ownership của MOW/MOT/MOIT/MOUT/Field/Trigger/Condition/NTGV/People phải giữ đúng.

---

# 2. MỤC TIÊU LỚN CỦA GÓI VIỆC

**Hoàn tất TOÀN BỘ Gate1 UI review còn lại trong một lượt: R2 → R8.**

Sau gói này PM phải có đủ evidence để trả lời:

> Với toàn bộ UI hiện có, đâu là UI/pattern giữ làm canonical default, đâu là library, đâu là review, đâu là expert/fallback/runtime, đâu là retire-candidate; và Gate2 thực sự chỉ cần bù những capability UI dùng chung nào?

Không giao tiếp từng R sau khi xong.

Agent tự đi hết R2–R8 theo dependency và checklist dưới đây.

---

# 3. PHẠM VI R2–R8 PHẢI HOÀN THÀNH

## R2 · MOT

Kiểm đầy đủ các candidate liên quan:

- U05 · MOT Master;
- U06 · thiết kế task / New MODT T1 / MODT builder;
- U07 · MOT Dashboard;
- mọi Help/component/source trực tiếp cần để hiểu vai trò thật.

Phải kết luận:
- library MOT;
- review/edit MOT;
- runtime task workspace;
- HMITL/AUTO thể hiện ở đâu;
- input/output/result/MOIT/MOUT/NTGV/context có giữ ownership đúng không;
- đâu là mock vs canonical-connected;
- manual-first smell;
- Agent path/read-back/revision path.

## R3 · MOIT + MOUT

Kiểm:

- U08–U13;
- list/master;
- form/layout/builder;
- report/reference builder;
- renderer hiện có;
- Help/source/data paths liên quan trực tiếp.

Phải kết luận:
- canonical library cho MOIT/MOUT;
- generic renderer nào giữ;
- expert editor nào giữ;
- source/target/read/write context;
- có duplicate builders không;
- form/report có thể đọc declaration chung hay giữ config riêng;
- những gì Gate0 generic renderer/write adapter đã chứng minh có thể reuse, nhưng không suy candidate UI đã nối nếu chưa có evidence.

## R4 · Field + Table

Kiểm:

- U14;
- U18;
- registry/list/request UI liên quan;
- nơi xem where-used/meaning/owner nếu có;
- Help/source trực tiếp.

Phải kết luận:
- library/search/request/review cho Field;
- Table/schema expert management;
- không để user/Agent tạo duplicate vì không tìm thấy;
- không để raw physical table name trở thành business identity;
- boundary: Field meaning ≠ MOIT layout; Table schema ≠ UI design.

## R5 · Trigger + Condition

Kiểm:

- U15–U16;
- registry/builder/binding UI;
- Help/source trực tiếp.

Phải phân biệt:
- Definition registry;
- Binding tại MOW/step;
- runtime occurrence/status;
- technical Directus Flow config.

Không hợp nhất chỉ vì cùng chữ “trigger/condition”.

## R6 · NTGV + People

Kiểm:

- U17;
- U19;
- New MODT/Help/people selector/role/delegation sources liên quan trực tiếp.

Phải kết luận:
- NTGV rule editor/library;
- People/Role/Delegation authoritative source;
- HMITL assignment view;
- màn gộp không đổi ownership;
- “người chuyển tiếp/làm thay/người nhận bước sau” nếu vẫn nhập nhằng.

### D04 rule

Không dừng gói việc để hỏi Owner.

Nếu actual evidence cho thấy D04 thật sự ảnh hưởng trách nhiệm con người:
- chuẩn bị đúng 1 đề xuất PM/Owner với lựa chọn + khuyến nghị + tác động;
- đánh `OWNER DECISION REQUIRED`;
- tiếp tục hoàn tất R7/R8.

Nếu chỉ là bố cục/technical mapping có thể đảo ngược → PM-level recommendation, không escalate.

## R7 · Quản trị chung

Kiểm các vùng tương ứng U20–U23, U26–U28 và các UI/Help liên quan:

- Guidance;
- organization tree/context;
- test;
- approval;
- publish/activate;
- feedback/improvement;
- version/history;
- readiness/missing ingredients nếu thuộc vùng chung.

Phải xác định:
- cái nào cần shared panel dùng cho nhiều object;
- cái nào là object-specific;
- Help nào đang lệch current SSOT;
- test/approval/publish UI nào chỉ mock;
- không để một loại object tự viết hệ approval/test riêng.

## R8 · Vận hành

Kiểm:

- U07;
- U24–U25;
- runtime list/monitor/task dashboard/handoff UI;
- source/Help trực tiếp.

Phải phân biệt rõ:
- Definition Master;
- Workflow Instance;
- Task Instance;
- Attempt;
- HMITL inbox/workbench;
- AUTO monitor/result;
- handoff/exception/retry.

Không biến AUTO thành card giả bắt người bấm Done.

Gate0 runtime proof là feasibility evidence; R8 phải đánh giá UI hiện hữu, không suy runtime UI đã đạt.

---

# 4. FREEZE SCOPE MỘT LẦN, SAU ĐÓ TỰ LÀM HẾT

Trước khi rà chi tiết:

1. đọc U01, U05–U28 current trong SSOT;
2. đọc navigation/menu/current URLs;
3. discovery bounded để tìm candidate trực tiếp liên quan R2–R8;
4. lập `FROZEN GATE1 CANDIDATE SET`:
   - URL;
   - object/review;
   - reason included;
   - expected candidate count.

Sau freeze:
- kiểm hết 100%;
- discovered extra candidate sau freeze đưa `OVERFLOW / follow-up`, trừ khi thiếu nó sẽ làm kết luận Gate1 sai material thì được add với lý do;
- không mở search vô hạn.

U02–U04 không rà lại trừ khi cần đối chiếu cross-object pattern.

---

# 5. MỖI CANDIDATE PHẢI TRẢ LỜI CÙNG MỘT BỘ CÂU HỎI

Không viết essay riêng mỗi màn.

Cho mỗi candidate, ghi structured row:

1. **Object / stage phục vụ**
2. **Role đề nghị**
   - PRIMARY REVIEW
   - LIBRARY/MASTER
   - EXPERT EDITOR
   - RUNTIME WORKSPACE
   - CONTEXTUAL VIEW
   - FALLBACK
   - LEGACY/REFERENCE
   - RETIRE-CANDIDATE
3. **Implementation truth**
   - connected canonical
   - partial
   - mock/static/local
   - source-only/unproven
4. **Reads from đâu**
5. **Writes to đâu**
6. **ID/version/revision/context có giữ không**
7. **Human path**
8. **Agent path**
9. **Ownership đúng/sai/chưa chứng minh**
10. **Reuse/where-used/diff/readiness support**
11. **Gap**
12. **Disposition**
13. **Evidence**

Không dùng label trong UI như “production/real/10/10/SSOT” làm evidence.

---

# 6. QUAN TRỌNG: TỪ NHIỀU UI PHẢI HỘI TỤ THÀNH ÍT PATTERN

Mục tiêu không phải chọn 28 màn.

Sau R2–R8, bắt buộc tạo **CANONICAL UI ROLE MAP TOÀN HỆ**.

Ưu tiên hội tụ vào các pattern dùng chung nếu evidence cho phép, ví dụ:

### Pattern P-01 · Library/Master
Dùng chung cấu trúc:
- MOW;
- MOT;
- MOIT;
- MOUT;
- Field;
- Trigger;
- Condition;
- NTGV;
- Guidance...

Không clone một Master implementation riêng chỉ vì object khác tên.

### Pattern P-02 · Review Workspace
Một shell/pattern cho:
- summary;
- diff;
- readiness;
- missing;
- test;
- approval state;
- decision points;
- impact.

Object-specific content render theo declaration/metadata.

### Pattern P-03 · Expert Editor
Chỉ khi người cần sửa sâu:
- graph;
- task contract;
- form layout;
- report query;
- assignment rule;
- schema.

Mở đúng editor chủ quản với same context; không copy business truth vào Workspace.

### Pattern P-04 · Runtime Workbench
HMITL:
- đúng việc/người/context;
- MOIT/MOUT;
- result/handoff/exception.

AUTO:
- monitor/result/error/attempt;
- không fake human task.

### Pattern P-05 · Shared lifecycle panels
Where useful:
- Test;
- Diff/Impact;
- Approval;
- Publish/Activate;
- Version/History;
- Health/Findings.

**Không bắt buộc chính xác 5 pattern.**
Nếu actual evidence cho thấy nên gộp/tách khác, được đề xuất.
Nhưng cuối Gate1 phải giảm được “rừng UI” thành một số ít vai trò có lý do.

---

# 7. PHẢI CHỐT DISPOSITION CHO UI TRÙNG

Không xóa code.

Mỗi duplicate/candidate cũ phải có một trong:

- KEEP CANONICAL ROLE;
- KEEP EXPERT;
- KEEP REFERENCE;
- MERGE CAPABILITY INTO PATTERN;
- RETIRE-CANDIDATE;
- UNKNOWN — NEED EVIDENCE.

Mọi RETIRE-CANDIDATE phải ghi:
- consumer known/unknown;
- nội dung nào cần preserve;
- điều kiện retire;
- Gate thực hiện retire.

Không dọn production trong Gate1.

---

# 8. CROSS-OBJECT OWNERSHIP TEST

Sau khi phân vai UI, chạy một review ngang:

### Case A · MOW mở MOT
MOW Workspace được inspect MOT nhưng sửa MOT phải đi đúng MOT owner/editor.

### Case B · MOT mở MOIT/MOUT
Task review nhìn được form/report; chỉnh Definition phải chuyển đúng editor với context giữ nguyên.

### Case C · MOIT dùng Field
Form layout thay required/order không tự đổi meaning Field.

### Case D · MOW dùng Trigger/Condition
Binding MOW không sửa global Trigger/Condition Definition.

### Case E · MOT dùng NTGV/People
NTGV rule khác People/Role/Delegation source.

### Case F · Runtime
Task Instance UI không sửa Definition để “sửa nhanh việc đang làm”.

PASS nếu UI role map không tạo competing truth hoặc quyền sửa chéo.

---

# 9. HUMAN-FIRST HAY AI-FIRST — PHẢI CÓ KẾT LUẬN TOÀN GATE1

Sau khi rà hết, không chỉ ghi từng control.

Bắt buộc trả lời:

> Nếu một người muốn tạo/sửa quy trình theo target architecture, UI hiện tại có bắt họ tự điều phối công cụ và tự cấu hình phần máy có thể làm không?

Phân loại:

- **DEFAULT AI-FIRST FIT**
- **AI-FIRST WITH GATE2 GAPS**
- **MANUAL-FIRST / EXPERT ONLY**

Cho từng pattern/object family.

Mọi thao tác manual lặp phải chỉ ra:
- có thật sự cần H1–H5 không;
- nếu không → Gate2 gap cho automation/AI declaration, không coi đó là feature người dùng.

Không đặt %98 giả nếu chưa đo.

---

# 10. GATE2 GAP COMPRESSION — KHÔNG ĐEM 28 GAP SANG GATE2

Đây là deliverable bắt buộc.

Từ tất cả gap R1–R8, **gom thành số ít capability gap dùng chung**.

Mục tiêu: khoảng **5–8 nhóm**, không hard quota.

Ví dụ loại nhóm có thể xuất hiện:

- canonical context + object/version/revision navigation;
- generic Agent→UI read/refetch;
- common Library/reuse/where-used;
- shared Review/diff/readiness/test;
- owner-aware expert editor handoff;
- common authority/approval/publish controls;
- runtime HMITL/AUTO workbench;
- Help/documentation alignment.

Không tạo 28 ticket “sửa màn X”.

Với mỗi group:
- requirement;
- object families affected;
- existing reusable assets;
- what is missing;
- Gate2 design outcome;
- Gate3/4 contract/data dependency;
- code likelihood I0–I7;
- evidence.

---

# 11. CHUẨN BỊ LUÔN GATE2 ENTRY — KHÔNG UPGRADE, KHÔNG BUILD

Để giảm một vòng trao đổi, sau khi hoàn tất R2–R8, thực hiện thêm **Gate2 Entry Readiness review**.

## 11.1. PLATFORM FREEZE evidence package

Không thay đổi platform.

Chỉ:
- xác minh exact CURRENT versions từ evidence/current environment;
- xác minh từ nguồn chính thức các stable TARGET candidates hiện hành cho:
  - PostgreSQL supported 16 minor;
  - Directus stable target;
  - Nuxt 4;
  - Node pair;
- kiểm compatibility material của:
  - write guard;
  - generic UI adapter;
  - runtime worker/pg-boss;
  - SDK/packages liên quan;
- kiểm Directus target licensing bằng official terms + Owner facts đã có;
- nếu còn thiếu một fact thật sự material, ghi đúng fact thiếu, không đoán.

Kết luận đề nghị một trong:
- `TARGET STACK ADOPT — READY FOR PM DECISION`
- `OLD STACK CONTINUE — READY FOR PM DECISION`
- `PLATFORM FREEZE BLOCKED BY <exact fact/evidence>`

Không tự upgrade/rehearse.

## 11.2. RULE-SYNC-01 preparation

Không sửa luật nguồn trong lượt này nếu chưa được PM cho quyền build.

Nhưng phải xác định:
- exact rule source file(s);
- exact two principles cần propagate;
- proposed minimal patch;
- conflict nếu có.

Để PM có thể giao cùng Gate2 mà không discovery lại.

---

# 12. ĐIỀU KIỆN PASS TOÀN GÓI

Chỉ được báo:

## `READY FOR PM GATE1 EXIT REVIEW`

khi thỏa tất cả:

### Completeness
- R2–R8 đều hoàn thành;
- frozen candidate set 100% có disposition/evidence/gap;
- U01/U05–U28 không còn current row “chưa rà” mà không có lý do;
- R1 acceptance + D03 decision đã được đưa vào SSOT.

### Canonical UI map
- có role map toàn hệ;
- default AI-first path rõ;
- expert/fallback/legacy/retire roles rõ;
- cross-object ownership test hoàn tất;
- duplicate UI có disposition.

### Gate2 input
- gap đã compression thành shared capability groups;
- không 28 việc lặt vặt;
- mỗi gap biết reuse gì trước code;
- platform freeze có evidence/recommendation;
- RULE-SYNC source/patch target đã xác định.

### Safety / truth
- không build/deploy;
- không production mutation;
- không gọi mock thành connected;
- không gọi source tồn tại thành runtime PASS;
- không tự VERIFIED O1–O3.

Nếu một vài UI inaccessible nhưng đã có evidence đủ từ source/Help để kết luận role/gap, được complete với limitation rõ.

Chỉ `BLOCKED` nếu thiếu đó làm PM không thể chọn canonical role hoặc không thể xác định Gate2 scope.

---

# 13. SSOT — CẬP NHẬT ĐÚNG MỘT LẦN SAU KHI TOÀN GÓI XONG

Backup v1.6.14 trước khi ghi.

Dự kiến lên **v1.6.15**.

Không ghi từng R một.

Cập nhật đồng bộ:

- Owner Cockpit;
- Current Review;
- Gate strip;
- PM Control Panel;
- Work Queue;
- W003;
- D03;
- D04 nếu có actual finding;
- D05–D07 nếu review cho thêm evidence nhưng không tự quyết quyền Owner;
- Object cards MOW/MOT/MOIT/MOUT/Field/Table/Trigger/Condition/NTGV/People/Guidance/Tree;
- U01–U28;
- UI evidence;
- Gate1 section;
- risk/issue register;
- decision log;
- Current State;
- next action;
- history;
- footer.

### Ghi R1 acceptance + D03

Phải có:

```text
W003/R1 MOW
PM Verdict: ACCEPT
Accepted Scope: MOW UI role review
Accepted by: GPT Chat / PM
Accepted date: 10/09/2026

D03: DECIDED
MOW canonical composition:
- Nháp2 drawer pattern = primary human review pattern
- MOW Master = library
- Unified Canvas = contextual graph/expert view
- MODW/New MODT = expert/fallback
- Nháp1 = reference
- duplicate Master list = retire-candidate
Implementation gaps route Gate2; decision does not claim current connected UI.
```

### Sau R2–R8

Agent chỉ ghi:
- evidence;
- recommendation;
- role map;
- gap groups;
- `SUBMITTED / READY FOR PM REVIEW`.

**Không tự đóng Gate1.**

Gate1 vẫn DOING cho tới GPT Chat/PM review.

---

# 14. KHÔNG ĐƯỢC LÀM

- Không build/fix UI.
- Không sửa product source.
- Không deploy.
- Không schema migration.
- Không upgrade stack.
- Không cài thêm runtime.
- Không chỉnh production data.
- Không mở Gate2 implementation.
- Không mở formal Pilot A/B.
- Không tự đóng Gate1.
- Không tự quyết Owner-level D04 nếu actual responsibility ambiguity tồn tại.
- Không tạo framework UI mới trên giấy nếu existing patterns có thể hội tụ.
- Không gửi report sau từng R.

---

# 15. BÁO CÁO CUỐI CHO OWNER — CHỈ SAU KHI TOÀN BỘ GÓI XONG

Tối đa 12 ý:

1. R1 PM acceptance + D03 đã ghi chưa.
2. Tổng candidate Gate1 frozen / đã kiểm / overflow.
3. R2 MOT kết luận.
4. R3 MOIT/MOUT kết luận.
5. R4 Field/Table kết luận.
6. R5 Trigger/Condition kết luận.
7. R6 NTGV/People + D04 có cần Owner không.
8. R7 governance/shared lifecycle kết luận.
9. R8 runtime UI kết luận.
10. Canonical UI Role Map còn bao nhiêu pattern chính.
11. Gate2 gaps đã nén thành bao nhiêu nhóm + platform freeze recommendation.
12. Kết luận:
   - `READY FOR PM GATE1 EXIT REVIEW`, hoặc
   - blocker duy nhất/các blocker material còn lại.

Nộp kèm:
- detailed evidence README;
- structured summary;
- screenshots/source evidence cần thiết;
- manifest/hash;
- SSOT v1.6.15 read-only snapshot;
- evidence ZIP.

Không yêu cầu Owner đọc toàn bộ evidence.

---

# KẾT LUẬN ĐIỀU HÀNH

Lượt này không còn là “xem thêm một màn”.

Mục tiêu là:

> **Kết thúc toàn bộ việc lựa chọn/phân vai UI của Gate1, biến hàng chục UI hiện có thành một bản đồ vai trò nhỏ, rõ, AI-first; đồng thời nén tất cả thiếu sót thành một số ít capability gap đủ lớn để Gate2 xử lý trọn gói.**

Chỉ khi làm xong toàn bộ và tự kiểm đủ mới báo lại PM.
