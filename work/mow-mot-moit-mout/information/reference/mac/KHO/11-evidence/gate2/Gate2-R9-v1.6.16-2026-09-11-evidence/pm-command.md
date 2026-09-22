# LỆNH GIAO CODEX — PM ĐÓNG GATE1, GIẢI PLATFORM FREEZE, HOÀN TẤT GATE2 DESIGN + R9 TRONG MỘT GÓI

**PM: GPT Chat · 11/09/2026**  
**SSOT duy nhất:** `/Users/nmhuyen/Desktop/quy trình/cấu trúc hệ thống.html`  
**Current:** v1.6.15  
**Evidence đầu vào:** gói `Gate1-R2-R8-v1.6.15-2026-09-10-evidence.zip` + toàn bộ evidence Gate0/R1 đã có trong workspace.

Đây là **một gói việc lớn, tuần tự**, không chia thành các prompt nhỏ.

**Không báo cáo giữa chừng.**  
Chỉ báo PM khi:
1. Gate1 acceptance đã được nhập vào staging SSOT;
2. platform technical rehearsal đã hoàn thành hoặc có blocker thật không thể vượt qua;
3. RULE-SYNC-01 đã xử lý trong phạm vi được phép;
4. toàn bộ 8 nhóm Gate2 đã có design/composition hoàn chỉnh;
5. R9 E2E design walkthrough đã đi hết cả happy path và các đường lỗi chính;
6. self-QA completeness PASS;
7. SSOT được cập nhật đúng **một lần ở cuối**;
8. kết quả là `READY FOR PM GATE2 EXIT REVIEW` hoặc `PARTIAL/BLOCKED` với đúng blocker vật chất còn lại.

Không dừng để hỏi PM vì một candidate lỗi, một URL hỏng, một built-in không fit hoặc một hướng kỹ thuật bị loại. Tiếp tục các phần độc lập và thu evidence.

---

# 1. QUYẾT ĐỊNH PM CÓ HIỆU LỰC

## 1.1. Gate1 · ACCEPT / DONE

PM đã kiểm gói Gate1:

- manifest 689/689 tệp khớp SHA-256;
- 41/41 candidate trong frozen set đã có review/disposition/evidence;
- U01/U05–U28 có coverage; R1 MOW đã PM ACCEPT trước;
- role map hội tụ thành 5 pattern;
- 8 capability gap groups đã nén;
- duplicate/legacy có disposition;
- AI-first/manual-first assessment đã có;
- cross-object ownership A–F đủ để chọn vai trò UI;
- không product code/build/deploy được thực hiện trong Gate1.

**PM VERDICT: GATE1 ACCEPT / DONE trong phạm vi lựa chọn/phân vai UI.**

Ý nghĩa:

> Đã đủ căn cứ để biết mỗi UI/pattern nên đóng vai trò gì và Gate2 cần bù những capability dùng chung nào.

Không có nghĩa:

- các UI hiện tại đã connected/production;
- authority enforcement đã PASS toàn hệ;
- O1–O3 VERIFIED;
- Gate2/Contract/Data/Pilot đã PASS.

## 1.2. Canonical UI role map được PM nhận

Giữ 5 pattern:

1. **P01 · Library/Master**
2. **P02 · Review Workspace**
3. **P03 · Expert Editor**
4. **P04 · Runtime Workbench**
5. **P05 · Shared lifecycle/context panels**

Giữ D03 MOW composition đã quyết:
- Nháp2 drawer pattern = primary human review pattern;
- MOW Master = library;
- Unified Canvas = contextual graph/expert view;
- MODW/New MODT = expert/fallback;
- Nháp1 = reference;
- duplicate Master list = retire-candidate.

Các role R2–R8 trong `canonical-role-map.md` được PM ACCEPT làm **design-role baseline** cho Gate2.

## 1.3. Tám Gate2 capability groups được PM nhận làm phạm vi

- G01 Context và định danh thống nhất
- G02 Library/reuse/where-used/request-resume
- G03 Agent declaration → generic render/refetch
- G04 Review/readiness/diff/impact/test một nguồn
- G05 Owner-editor handoff + authority/lifecycle
- G06 Giao việc đúng nghĩa + nguồn người
- G07 Runtime HMITL/AUTO + exception
- G08 Guidance/Help drift/feedback trace

Không tách thành 28 ticket UI.

## 1.4. D04 không chặn Gate1/Gate2 design

D04 vẫn là **OWNER DECISION REQUIRED**, nhưng PM đổi dependency:

> D04 phải được Owner quyết trước khi khóa semantic responsibility/Contract tại Gate3 và trước Pilot giao việc thật; **không chặn Gate2 design**.

Gate2 phải thiết kế theo hướng **không trộn các nghĩa**:
- executor task hiện tại;
- delegate/làm thay theo ủy quyền;
- next-task recipient/executor do MOT đích/NTGV phân giải;
- report/notification recipient;
- handoff contact nếu nghiệp vụ cần.

Không cấp quyền hoặc quyết policy thay Owner.

**PM recommendation giữ phương án A** trong `d04-owner-proposal.md`; chưa đánh Owner ACCEPT.

---

# 2. NGUYÊN TẮC ĐIỀU HÀNH GÓI NÀY

## 2.1. Dùng lại trước, code sau

Mọi gap phải đi theo:

`I0 existing → I1 PG native → I2 Directus built-in → I3 internal Nuxt/Vue → I4 ecosystem → I5 composition → I6 generic adapter → I7 custom last`

Và bắt buộc kiểm **TARGET-VERSION BUILT-IN** trước khi giữ/customize code candidate Gate0.

Không dùng chữ “config” để che:
- SQL function;
- Flow exec;
- hook;
- Nuxt server code;
- extension;
- worker.

Tất cả đều là code nếu có logic phải bảo trì.

## 2.2. Gate2 là DESIGN / COMPOSITION, không production build

Được:
- lab/rehearsal cô lập;
- đọc source;
- target-stack compatibility proof;
- workshop/clickable prototype nếu cần để chứng minh luồng;
- config/fixture TEST ONLY;
- screenshots/automated walkthrough;
- rule-source sync được PM cho phép ở §4.

Không được:
- deploy production;
- migrate production;
- schema production;
- dọn/xóa legacy;
- bulk rewrite UI thật;
- formal Pilot A/B;
- đổi O1–O3 VERIFIED.

---

# 3. PHASE A — PLATFORM TECHNICAL FREEZE / REHEARSAL

Mục tiêu: không để Gate2 thiết kế/bù UI trên nền sẽ bỏ ngay sau đó.

## 3.1. Refresh nguồn chính thức trước khi chạy

Xác minh lại stable candidates tại thời điểm thực thi từ official sources.

Candidate baseline từ Gate1:
- PostgreSQL 16.15
- Directus 12.3.1
- Nuxt 4.5.2
- Node phù hợp riêng cho Directus/worker và Nuxt
- pg-boss 12.30.0 / pg 8.23.0 chỉ là accepted runtime candidate

Nếu official stable patch đổi sau 10/09:
- ghi candidate mới;
- không tự nhảy major;
- ưu tiên ít biến số;
- giải thích nếu giữ pinned candidate cũ cho rehearsal.

## 3.2. Hai trạng thái khác nhau: technical freeze và license precondition

Không để license business fact chặn toàn bộ design.

### Technical Platform Freeze
Trả lời:
- target stack có chạy được accepted Gate0 slice không?
- custom candidate nào còn cần?
- built-in target có thay được custom nào?
- dependency/module nào vỡ?

### License / activation precondition
Owner đã xác nhận revenue dưới ngưỡng; **không hỏi lại revenue**.

Chưa có evidence headcount/phạm vi pháp nhân/Studio users/key.

Không suy đoán.

Không tự đăng ký OIG, chấp nhận agreement hoặc gửi thông tin thay Owner.

Nếu license fact/key chưa có:
- ghi `DEPLOYMENT LICENSE PRECONDITION OPEN`;
- tiếp tục tất cả compatibility/design hợp pháp có thể thực hiện;
- không gọi production deployment ready.

Gate2 design **không bị dừng chỉ vì headcount chưa được cung cấp**.

## 3.3. Rehearsal môi trường cô lập

Dùng VPS2 hoặc lab khác chỉ khi:
- demo e-learning không bị replace/restart;
- network/volume/DB/credential riêng;
- không dùng business/student data;
- backup/restore path rõ;
- cleanup theo ownership label.

Chạy **same bounded slice** trên target:

### Directus
Kiểm:
- extension load;
- hook/endpoint;
- ItemsService;
- accountability;
- transaction;
- 422/409/conflict;
- audit/replay;
- native version/draft/publish capability liên quan;
- target built-ins có thay được phần guard/custom nào.

### Nuxt
Kiểm:
- Form/UForm/FormCustom;
- SharedDirectusTable;
- generic guarded submit/refetch adapter;
- SSR/session/cookie;
- 422/409/conflict;
- declaration V1→V2 generic render;
- query-prefill/context;
- không per-form code.

### Runtime
Kiểm:
- worker Node compatibility;
- pg-boss;
- duplicate;
- immutable pin fixture;
- restart smoke;
- service identity → guarded effect;
- không nhét business rule vào worker.

### PG
Kiểm:
- minor update implications;
- actual extensions/index/slot material;
- không major migration.

## 3.4. Kết luận Platform

Một trong:

- `TARGET STACK TECHNICAL REHEARSAL PASS — RECOMMEND ADOPT`
- `TARGET STACK PARTIAL — exact follow-up`
- `TARGET STACK NOT FIT — recommend bounded OLD STACK CONTINUE with expiry`

Không tự PM ACCEPT production platform.

Nếu TARGET pass kỹ thuật nhưng license còn mở:
- vẫn có thể dùng TARGET làm Gate2 design baseline;
- production/deploy remains blocked by license/key.

---

# 4. PHASE B — RULE-SYNC-01: ÁP DỤNG THẬT, KHÔNG ĐỂ CHỈ NẰM TRONG SSOT

Owner đã lặp lại nhiều lần hai nguyên tắc này; PM cho phép đồng bộ chúng vào source rule.

## 4.1. Hai nguyên tắc phải đồng bộ

1. **PG-first ≠ PG-only**  
   Trước custom SQL/function/trigger/code phải xét:
   PG native → Directus built-in → internal component → ecosystem → composition → generic adapter → custom cuối.

2. **Code là code**  
   Flow exec / SQL function / Nuxt server / extension / worker đều tính là code, không đổi tên “config” để né reuse gate.

## 4.2. Source targets

Dùng exact targets đã chuẩn bị:
- local `incomex-rules.md`;
- Foundation principles / NT13;
- Constitution summary NT13.

Re-read actual source/revision/hash ngay trước patch.

Apply qua đúng governance/native write path có thẩm quyền.

Backup/version/provenance đầy đủ.

## 4.3. AGENTS conflict

Sau khi technical platform direction rõ:
- sửa hard-lock version policy trong `AGENTS.md` thành CURRENT vs TARGET rõ ràng;
- không ghi `latest`;
- không làm TARGET thành production-installed nếu chưa deploy.

Giải xung đột Nuxt “no code tuyệt đối”:
- cấm business logic/per-workflow logic/bypass authority trong Nuxt;
- **không cấm generic renderer/transport/component đã qua reuse gate**.

Không mở rộng quyền approval/publish.

Nếu KB governance không cho phép Agent tự publish:
- tạo pending change đúng cơ chế;
- vẫn hoàn tất các Phase khác;
- báo rõ `RULE-SYNC PENDING AUTHORITY`, không giả đã áp.

---

# 5. PHASE C — HOÀN TẤT GATE2 DESIGN CHO 8 NHÓM GAP

Không sửa từng màn.

Mục tiêu: 5 pattern + 8 groups thành **một đường AI-first liền mạch, không ngõ cụt**.

Cho mỗi G01–G08 phải có:

1. requirement;
2. current reusable assets;
3. target interaction;
4. Agent path;
5. Human H1–H5 touch;
6. ownership;
7. read/write/context/version behavior;
8. negative/error states;
9. target built-in/reuse ladder;
10. Gate3/4 contract/data dependencies;
11. acceptance test cho Gate2;
12. code likelihood / what must NOT be custom.

## G01 · Context / ID / version / revision

Thiết kế một context envelope dùng xuyên:
Library → Review → Expert Editor → lifecycle → Runtime.

Không raw table-name identity.

Phải giữ:
- object ID;
- definition/version;
- revision;
- scope;
- owner;
- return context;
- stale/conflict.

## G02 · Library / reuse / where-used / request-resume

Một search/reuse pattern cho nhiều object family.

Phải phân biệt:
- exact;
- near;
- ambiguous;
- incomplete search;
- none found;
- create/version/variant;
- request new ingredient;
- resume package sau khi ingredient có.

Không duplicate Master engines.

## G03 · Agent declaration → generic render/refetch

Default path:
Idea → Agent → declaration → generic UI review.

Không bắt Agent click UI để khai.

Không per-object/per-form renderer khi generic pattern đủ.

## G04 · Review/readiness/diff/impact/test

P02 + P05 dùng cùng artifact/revision.

Không readiness badge/test dấu ✓/local JS riêng.

Máy sinh/đọc evidence; người chỉ quyết semantic/risk/authority.

## G05 · Owner editor + lifecycle/authority

P02 mở P03 đúng owner, giữ context.

Design:
- Draft;
- version;
- test;
- approval;
- publish;
- activate;
- retire.

Không lấy sessionStorage/approve→published mock làm authority.

Chi tiết authority/contract → Gate3.

## G06 · Assignment / People

UI phải giữ riêng semantic slots của D04, chưa quyết policy.

Hiển thị:
- resolved executor;
- source/rule/version;
- delegation;
- missing/expired/ambiguous;
- reason.

Không copy People truth vào NTGV/MOT.

## G07 · Runtime HMITL/AUTO / exception

P04:

HMITL:
- đúng task/context;
- MOIT/MOUT/Guidance;
- complete/result;
- handoff;
- return/revise/wait/error.

AUTO:
- result;
- attempt;
- status;
- error;
- retry;
- compensation/reconciliation view;
- không fake Done.

Không thiết kế queue engine ở UI.

## G08 · Guidance / Help / feedback

Một Help/Guidance pattern:
- owner;
- version;
- applies-to;
- currentness;
- provenance.

Feedback một dòng:
- auto attach object/version/scope;
- trace Proposal→Version→Test→Run→Before/After;
- không copy Help cũ thành architecture truth.

---

# 6. PHASE D — WORKSHOP/PROTOTYPE ĐỂ CON NGƯỜI NHÌN ĐƯỢC

UI dùng để nhìn ra sai sót; Gate2 phải có visual evidence.

Tạo/update **Workshop prototype**, không production UI, cho 5 pattern:

- P01 Library
- P02 Review
- P03 Expert Editor handoff
- P04 Runtime Workbench
- P05 Shared lifecycle

Ưu tiên reuse asset hiện có; không vẽ lại từ trắng nếu có component.

Workshop phải dùng **một context fixture chung**, không năm bộ dữ liệu mẫu không liên quan.

### Quy tắc
- data fixture có ID/version/revision thật trong workshop;
- same object xuyên các view;
- không badge hard-code mâu thuẫn;
- không copy business truth vào JS nếu có fixture source chung;
- Human default thấy ít;
- expert controls nằm sâu;
- AUTO không có Done button.

Không gọi workshop là production.

---

# 7. PHASE E — R9 E2E DESIGN WALKTHROUGH

R9 ở Gate2 là **design walkthrough**, không formal runtime Pilot.

Dùng một scenario duy nhất đủ giàu:

> User nêu một quy trình nhỏ có ít nhất:
> - 1 HMITL task;
> - 1 AUTO task;
> - 1 MOIT;
> - 1 MOUT/context;
> - 1 NTGV/People resolution;
> - 1 Trigger;
> - 1 Condition hoặc handoff;
> - 1 reusable Field;
> - 1 missing ingredient/resume case.

## Happy path

Đi từ:

Idea
→ Agent Search/Reuse
→ Draft
→ missing ingredient
→ request
→ resume
→ Review
→ Expert handoff nếu cần
→ readiness/diff
→ machine test
→ approval
→ publish/activate design
→ event
→ HMITL Workbench
→ result
→ AUTO monitor/result
→ end
→ feedback
→ proposed improvement/version.

Không có dead end.

## Negative paths bắt buộc

1. search incomplete / ambiguous;
2. ingredient thiếu;
3. stale revision / conflict;
4. caller không quyền;
5. assignee missing/delegation expired;
6. test fail;
7. approval denied/expired;
8. AUTO error/retry;
9. output contract thiếu cho bước kế;
10. retire/deactivate đang có where-used.

Mỗi đường phải chỉ:
- view/pattern nào;
- Agent làm gì;
- máy làm gì;
- người quyết gì;
- quay lại/resume ở đâu;
- evidence nào cần.

---

# 8. HUMAN-EFFORT CHECK — KHÔNG CHỈ VẼ ĐẸP

Cho R9 workshop, đếm:

- số human decisions;
- số manual navigation;
- số lần phải tự tìm nguyên liệu;
- số raw IDs phải gõ;
- số cấu hình machine-resolvable nhưng vẫn bắt human nhập;
- số Agent/tool stages;
- số context loss.

Không đặt %98 giả.

Gate2 target:

> Default user chỉ tham gia H1–H5 và nhập dữ liệu nghiệp vụ thật ở HMITL; không làm công việc điều phối/config lặp mà máy có thể làm.

Mọi manual lặp ngoài phạm vi đó → gap chưa đóng.

---

# 9. GATE2 EXIT CRITERIA

Chỉ được báo `READY FOR PM GATE2 EXIT REVIEW` khi:

## Platform
- có technical platform recommendation dựa trên rehearsal/evidence;
- nếu license precondition mở, nó được tách khỏi design và ghi đúng nơi;
- không build dài hạn trên stack EOL một cách vô thức.

## UI/flow
- 8 groups có design outcome;
- 5 patterns cover được toàn đường;
- workshop same-context hoàn chỉnh;
- R9 happy + negative walkthrough không dead-end;
- owner/editor boundaries rõ;
- AI-first default rõ;
- missing/request/resume rõ;
- test/approval/publish visible nhưng không giả authority.

## Reuse/code
- mỗi gap có I0–I7 path;
- target built-in đã được xét;
- không tạo new framework vô cớ;
- product code mới trong Gate2 chỉ workshop/prototype generic nếu thật cần, kê riêng;
- không production deploy.

## Governance
- RULE-SYNC outcome rõ;
- D04 vẫn WAITING OWNER nếu chưa được quyết;
- D04 không bị mã hóa quyền ngầm;
- D05–D07 giữ đúng authority.

---

# 10. NẾU PLATFORM REHEARSAL BỊ BLOCK

Không dừng toàn gói.

Nếu blocker chỉ là OIG key/headcount/activation:
- tiếp tục Gate2 design/workshop theo technical candidates + CURRENT-compatible contracts;
- không deploy Directus12 production;
- ghi exact remaining owner fact.

Nếu target technical incompatibility thật:
- chứng minh cụ thể;
- chọn bounded compatibility strategy;
- vẫn hoàn tất Gate2 design platform-neutral;
- không tự rewrite framework.

Chỉ báo toàn gói BLOCKED nếu thiếu platform fact làm **không thể** xác định contract/interaction Gate2.

---

# 11. SSOT — GHI ĐÚNG MỘT LẦN Ở CUỐI

Backup v1.6.15.

Dự kiến **v1.6.16**.

Phải cập nhật đồng bộ:

- Owner cockpit;
- Gate strip;
- Current Review;
- PM Control Panel;
- Work Queue;
- W003/Gate1 acceptance;
- D03;
- D04 dependency mới;
- R2–R8 acceptance;
- canonical role map;
- Gate2 8 groups;
- Platform Freeze/rehearsal;
- RULE-SYNC;
- Gate2 work card;
- R9;
- UI evidence;
- object cards;
- risk/issue;
- decision log;
- current state;
- history/footer.

### Gate1 acceptance record

```text
Gate1 · Canonical UI
PM Verdict: ACCEPT / DONE
Accepted Scope: R1–R8 role selection, 41-candidate frozen review, 5 canonical role patterns, 8 Gate2 capability groups
Accepted by: GPT Chat / PM
Accepted date: 11/09/2026
Limit: role/design acceptance; current mocks not production/connected
Follow-up: Gate2 design/composition; Gate3/4 contracts/data; pilots Gate5/6
```

### D04

Ghi:
- `WAITING OWNER — due before Gate3 semantic contract lock`
- PM recommendation A
- **not Gate2 blocker**

Không ghi Owner accepted nếu Owner chưa trả lời.

### Gate states

Sau PM acceptance:
- Gate0 DONE
- Gate1 DONE
- Gate2 DOING/SUBMITTED hoặc PM REVIEW tùy work status khi nộp
- Gate3–7 NOT STARTED
- O1–O3 NOT VERIFIED

Codex không tự đóng Gate2.

---

# 12. QA TRƯỚC KHI BÁO CÁO

Bắt buộc tự kiểm:

1. all source/evidence hashes;
2. no production mutation;
3. demo unchanged;
4. SSOT one write;
5. no stale Gate1 DOING current statements;
6. R2–R8 PM acceptance current state đồng bộ;
7. D04 chỉ một current status;
8. 8 Gate2 groups đủ;
9. 5 patterns đủ;
10. R9 happy +10 negatives đủ;
11. workshop links/screenshots hoạt động;
12. platform recommendation/evidence links đủ;
13. RULE-SYNC source outcomes đúng;
14. no O1–O3 false VERIFIED;
15. no Gate2 false DONE.

---

# 13. BÁO CÁO CUỐI — TỐI ĐA 12 Ý

Chỉ báo sau khi toàn gói xong:

1. Gate1 PM ACCEPT đã ghi.
2. SSOT version/hash.
3. Platform rehearsal kết luận.
4. License precondition còn gì.
5. RULE-SYNC kết quả.
6. Gate2: 8 groups đã xử lý bao nhiêu.
7. Workshop 5 pattern.
8. R9 happy/negative walkthrough.
9. Human effort/manual smell còn lại.
10. Product/prototype code/dependency mới.
11. D04 status.
12. `READY FOR PM GATE2 EXIT REVIEW` hoặc blocker material còn lại.

Nộp evidence ZIP + manifest + SSOT snapshot.

Không gửi Owner hàng trăm chi tiết trừ khi PM yêu cầu.

---

# KẾT LUẬN ĐIỀU HÀNH

Gate1 đã hoàn thành việc **chọn vai trò**.

Gói này phải hoàn thành việc **nối vai trò thành một trải nghiệm thiết kế đầu–cuối có thể nhìn, kiểm và chuẩn bị build**, đồng thời khóa nền kỹ thuật đủ để không làm lại.

Không còn xử lý từng màn.

Mục tiêu cuối của Gate2:

> **Một con người nhìn vào hệ thống và thấy một đường đơn giản; một Agent có thể khai báo qua cùng contract; UI không tạo truth riêng; không có ngõ cụt; và mọi chỗ thiếu đã được quy về contract/data/capability cụ thể cho Gate3–4.**
