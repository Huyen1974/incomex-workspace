# Lệnh giao Codex — PM nhận Gate2, thực hiện trọn Gate3 + Gate4 (Contract & Data Lock), xử lý các blocker kỹ thuật cốt lõi và cập nhật SSOT một lần

**PM: GPT Chat · 11/09/2026**  
**SSOT duy nhất:** `/Users/nmhuyen/Desktop/quy trình/cấu trúc hệ thống.html`  
**Current:** v1.6.16  
**Nguồn evidence:** `Gate2-R9-v1.6.16-2026-09-11-evidence.zip` + toàn bộ evidence Gate0/Gate1 hiện có trong workspace.

Đây là **một gói việc lớn, hoàn chỉnh**. Không chia thành nhiều prompt nhỏ.  
Agent có quyền tự tổ chức subtask, chạy lại test và sửa lỗi trong phạm vi được giao.

## Quy tắc báo cáo

**KHÔNG gửi báo cáo tiến độ giữa chừng.**

Chỉ báo PM sau khi:

1. toàn bộ phạm vi Gate3 + Gate4 bên dưới đã được thực hiện;
2. các lỗi phát hiện trong phạm vi đã được xử lý và regression lại, hoặc đã chứng minh là material blocker không thể xử lý an toàn trong phạm vi;
3. QA checklist cuối đạt;
4. SSOT đã cập nhật đúng **một lần ở cuối**;
5. kết luận cuối là một trong:
   - `READY FOR PM GATE3+4 EXIT REVIEW`, hoặc
   - `READY FOR PM GATE3+4 EXIT REVIEW — OWNER D04 LOCK PENDING`, hoặc
   - `BLOCKED BY <material blocker đã có evidence>`.

Không dừng giữa chừng để hỏi PM về chi tiết kỹ thuật có thể đảo ngược.  
Không tạo 30 ticket nhỏ thay cho việc giải quyết gốc.

---

# 1. QUYẾT ĐỊNH PM CÓ HIỆU LỰC NGAY

## 1.1. Gate2

**W004-GATE2 / Gate2: PM ACCEPT WITH FOLLOW-UP / DONE trong phạm vi design/composition.**

PM đã kiểm:

- ZIP: 494/494 mục manifest khớp SHA-256;
- SSOT v1.6.16 đính kèm và snapshot trong ZIP byte-identical, SHA256 `e802f944e6c5ddfe4067947468145021e77e4164244e1d4ad59bd55252bad3f5`;
- 8/8 nhóm, mỗi nhóm 12 thuộc tính;
- 5 canonical patterns cùng context;
- R9 happy + 10/10 negative walkthrough kết thúc được sau block/resume;
- human-effort được phân biệt rõ giữa quyết định nghiệp vụ và click harness;
- workshop được ghi đúng là design simulation;
- O1–O3 vẫn NOT VERIFIED;
- production deploy/schema/data = 0;
- RULE-SYNC có read-back evidence.

### Accepted Scope

Gate2 chứng minh:

> Đường đi UI/composition đã đủ rõ để bước sang Contract/Data mà không cần tiếp tục thiết kế màn hình rời rạc.

Gate2 **không** chứng minh:

- production UI/runtime;
- Directus12 full-target PASS;
- full Agent factory;
- full auth/session;
- full release governance;
- O1/O2/O3;
- Pilot A/B.

### Follow-up được route sang Gate3–4 / Gate5–7

Ba finding kỹ thuật chính:

1. Directus12 scoped permission cần entitlement/license hợp lệ;
2. Nuxt target module/session/prefill/dirty-state còn follow-up;
3. **release-aware pin chưa đúng:** Instance đã pin release vẫn phụ thuộc Form `main`.

Các finding này **không reopen Gate2**.

---

# 2. PHÁT HIỆN PM BẮT BUỘC PHẢI ĐƯỢC XỬ LÝ TRONG GÓI NÀY

## 2.1. Release pin counterexample — ưu tiên số 1

Actual event4:

- Instance giữ release V2;
- Form `main` revision đổi;
- worker chạy 2 attempts;
- cả hai `FORM_REVISION_CONFLICT`;
- effect = 0.

Kết luận:

> Release snapshot hiện tại **chưa tạo immutable semantic closure**. Runtime vẫn phụ thuộc một material current/editable.

Gate3 phải khóa semantics. Gate4 phải map data/source. Lab phải chứng minh cách xử lý.

Không được giải quyết bằng:

- bỏ kiểm revision;
- resolve `latest/main`;
- copy tùy tiện mọi JSON vào release;
- retry nhiều lần cùng một permanent conflict;
- tắt validation để demo chạy.

## 2.2. Retry taxonomy

`FORM_REVISION_CONFLICT` đã bị retry 2 lần.

Gate3 phải phân biệt ít nhất ở mức contract:

- TRANSIENT / RETRYABLE;
- PERMANENT / NON-RETRYABLE;
- AUTH/POLICY BLOCK;
- NEEDS_RECONCILIATION / EFFECT_UNKNOWN;
- BUSINESS/VALIDATION REJECT.

Không cần tạo enum DB nếu chưa cần.

Mỗi lỗi runtime/action phải trả đủ để worker biết:

- retry?
- retry when?
- same effect key?
- effect known/unknown?
- needs human/owner?
- terminal result hay wait/reconcile?

Unknown external effect **không retry mù**.

## 2.3. Authority hiện hành khác semantic pin

Phải tách rõ:

### Pin theo release
Những gì định nghĩa **nghĩa và hành vi đã được duyệt**:
- MOW/MOT;
- MOIT/MOUT;
- Field/Condition/Trigger/NTGV semantic versions;
- contract/profile/validator semantics;
- Capability version;
- relevant Binding parameters;
- test/evidence digest theo policy.

### Recheck tại thời điểm chạy
Những gì phải còn hiệu lực hiện tại:
- authenticated service/user identity;
- permission/action scope;
- credential validity/revocation;
- delegation validity nếu dùng;
- hard safety policy được thiết kế là current-check.

Không được dùng “recheck quyền hiện hành” để reinterpret business semantics của Instance cũ.

---

# 3. MỤC TIÊU LỚN CỦA GÓI VIỆC

Hoàn tất **Gate3 Contract + Gate4 Data** như một package thống nhất:

```text
Gate2 design
→ machine-readable semantic contracts
→ exact authority/action/error contracts
→ exact release closure
→ mapping từng contract fact vào data/source thật
→ typed relations / integrity / where-used
→ bounded executable proof trên critical contracts
→ readiness cho Formal Pilot A/B
```

Sau gói này, PM phải có thể trả lời:

1. Mỗi object/action/event/runtime record có contract gì?
2. Ai sở hữu/sửa?
3. ID/version/revision nào được pin?
4. Đọc từ đâu, ghi vào đâu?
5. Quan hệ nào là authoritative?
6. Quyền nào kiểm ở đâu?
7. Error/retry/resume thế nào?
8. UI và Agent dùng cùng contract bằng cách nào?
9. Runtime dùng exact released material bằng cách nào?
10. Còn cần tạo mới chính xác data/adapter nào và tại sao không reuse được?

Không được kết thúc Gate3/4 bằng “sau này thiết kế tiếp”.

---

# 4. GATE3 — CONTRACT LOCK

## 4.1. Contract families bắt buộc

Không tạo framework mới nếu các contract hiện có có thể gom.

Phải khóa tối thiểu các logical contract sau.

### C01 · Identity / Version / Revision / Status

Cho:
- Definition;
- Version;
- Binding;
- Instance;
- Attempt;
- Release;
- Package/Draft.

Phân biệt:
- stable identity;
- immutable business version;
- editable revision;
- lifecycle status;
- active binding;
- runtime instance.

Không dùng Directus revision làm business Version nếu semantics khác.

### C02 · Context Envelope

Tối thiểu:
- object/family;
- package;
- parent/slot;
- scope/org;
- authenticated actor;
- executing service;
- on-behalf-of/delegation nếu có;
- version/revision;
- return context;
- instance/attempt khi runtime;
- provenance.

Client URL/query chỉ là prefill/selector, không authority.

### C03 · Machine/Human Action Envelope

Một contract dùng chung cho Human UI, Agent và service:

- action;
- target;
- expected revision;
- idempotency key;
- context;
- parameters/patch;
- actor/executor;
- authority scope;
- result;
- evidence;
- error;
- read-back revision;
- correlation.

Không cho caller tự chọn physical table/profile để vượt policy.

### C04 · Reuse / Admission

Per reusable family:
- Search Brief;
- scope;
- candidates;
- contract diff;
- coverage;
- REUSE / NEW VERSION / VARIANT / NEW / NEEDS_DECISION / REJECT_DUPLICATE;
- evidence/provenance.

Giữ lexical-first đã được nhận. Không vector project mới.

### C05 · Definition contracts

Khóa semantic contract tối thiểu cho:

- MOW;
- MOT;
- MOIT;
- MOUT;
- Field;
- Trigger;
- Condition;
- NTGV;
- Guidance;
- Capability/Action.

Mỗi family phải có:
- meaning;
- owner;
- supported fields;
- type/unit/domain;
- required/N/A;
- refs;
- parameter surface;
- version compatibility;
- validation;
- examples positive/negative.

Không biến UI form thành contract.

### C06 · Release / Activation / Pin Contract

Phải trả lời exact:

- một Release chứa/ref cái gì;
- closure được resolve khi nào;
- material nào snapshot, material nào exact immutable Version ref;
- hash/digest dùng cho gì;
- test/approval gắn với closure nào;
- Active Binding trỏ gì;
- Instance pin gì;
- current permissions recheck thế nào;
- retire/supersede ảnh hưởng Instance cũ ra sao.

**Không được để runtime đọc `main/latest` cho semantic material đã pin.**

### C07 · Runtime Event / Instance / Attempt / Result

Tối thiểu:

- occurrence ID;
- business case/correlation;
- dedup semantics;
- Active Binding resolution;
- exact Release/Effective Version Set;
- Instance;
- Task Instance;
- Attempt;
- executor/capability version;
- input/context;
- output/result;
- handoff;
- receipt;
- error;
- retry/reconciliation;
- completion/ACK.

Case ID ≠ occurrence ID ≠ idempotency key.

### C08 · Error / Retry / Reconciliation

Khóa error envelope và classification nói ở §2.2.

Test rõ:
- validation conflict;
- stale revision;
- permission expired;
- provider unavailable;
- transient technical failure;
- external effect unknown;
- output incomplete;
- duplicate request/event.

### C09 · Test / Diff / Readiness / Approval / Publish / Activate

Phân biệt:
- test evidence;
- business review;
- approval;
- publish;
- activate.

Evidence phải pin đúng revision/release/dependency digest.

Sửa material → test/approval cũ stale theo policy.

### C10 · Audit / Provenance

Một audit contract, nhiều producer.

Phải trace:
`intent/request → actor/executor → object/version/revision → action → result/error → runtime/effect`.

Không bắt tất cả write đi Directus nếu cổng khác có contract tương đương; nhưng không để write material mất correlation.

---

# 5. D04 / D05 / D06 / D07

## 5.1. D04 — Owner authority, KHÔNG tự quyết

Owner chưa ACCEPT.

PM recommendation hiện hành:

**D04-A**
- `executor`: người/service chịu trách nhiệm thực hiện Task Instance;
- `delegate`: người được ủy quyền làm thay executor trong phạm vi/thời hạn;
- `next_task_executor / recipient`: người nhận trách nhiệm Task tiếp theo;
- `report_recipient`: người nhận MOUT/thông báo, không mặc nhiên chịu trách nhiệm task;
- `handoff_contact`: đầu mối bàn giao/liên hệ, không mặc nhiên executor.

People / Role / Delegation là nguồn riêng; NTGV chỉ resolve assignment.

Agent:

- không hỏi Owner giữa chừng;
- hoàn tất mọi phần Gate3/4 không phụ thuộc D04;
- giữ D04 semantic slots explicit;
- nếu chưa có Owner acceptance khi kết thúc, báo:
  `READY FOR PM GATE3+4 EXIT REVIEW — OWNER D04 LOCK PENDING`.

Không âm thầm chọn A là quyết định Owner.

## 5.2. D05 — khóa semantics, chưa tự đặt người ký

PM khóa:

`REVIEW ≠ TEST ≠ APPROVE ≠ PUBLISH ≠ ACTIVATE`.

Contract phải cho policy cấu hình:
- ai được action nào;
- materiality/risk nào cần action nào;
- expiry/revocation;
- separation-of-duties khi policy yêu cầu.

Không tự gán tên người/chức danh chưa có căn cứ.

Nếu actual requirement buộc đổi trách nhiệm con người → trình Owner một decision card, không dừng package.

## 5.3. D06 — PM decision cho contract

Default:

- feedback một dòng luôn có theo context/quyền;
- người có quyền có thể mở Draft mới trực tiếp nếu ghi reason + source version/provenance;
- feedback không sửa Published;
- Draft từ feedback đi lại Test/Approval/Publish bình thường.

Ghi D06 `DECIDED · PM` nếu evidence không phát hiện contradiction material.

## 5.4. D07 — PM decision cho contract

Default:

- retire/deactivate = **stop new use / stop new activation** theo action cụ thể;
- Instance đang chạy tiếp tục với exact pinned set theo policy;
- không hard-delete Definition/Version còn references/history;
- cancel/migrate/compensate là explicit action có quyền + impact/evidence;
- rollback Binding không tự đảo external effect.

Ghi D07 `DECIDED · PM` nếu evidence không phát hiện contradiction material.

---

# 6. GATE4 — DATA LOCK / ACTUAL MAPPING

Không thiết kế data từ tên UI.

## 6.1. Lập Contract → Data Matrix

Cho mọi field material của C01–C10, map một trong:

- `REUSE_EXISTING_AUTHORITATIVE`
- `REUSE_WITH_MAPPING`
- `DERIVED_VIEW`
- `NEW_REQUIRED`
- `UNKNOWN_NEEDS_EVIDENCE`

Mỗi dòng phải có:

- semantic key;
- contract owner;
- actual DB/schema/collection/field hoặc source;
- stable ID;
- datatype/unit;
- read path;
- write path;
- permission authority;
- physical integrity;
- version/revision behavior;
- where-used relation;
- current consumer;
- target disposition;
- evidence.

Không map bằng label gần giống.

## 6.2. Typed Relation Map

Ít nhất:

- Definition→Versions;
- MOW Version→Step Bindings;
- Step→MOT Version;
- MOT→MOIT/MOUT/NTGV/Capability refs;
- MOIT/MOUT/Condition→Field refs;
- Trigger/Condition/NTGV Definitions→Bindings;
- People/Role/Delegation;
- Release→material closure;
- Binding→Release/Definition Version;
- Instance→Binding/Release;
- Task Instance→MOT Version;
- Attempt→Task Instance + Capability Version;
- output→consumer/handoff;
- request/missing ingredient→parent/slot/revision;
- supersedes/replaces;
- where-used.

Mỗi relation phải phân loại:

- authoritative hard relation;
- accepted equivalent enforcement;
- Directus metadata only;
- discovered/inferred;
- missing.

Không gọi Directus relation metadata là FK thật.

## 6.3. Data authority

Cho mỗi business fact:

> đúng một nơi là authority.

Nếu cùng một semantic rule xuất hiện ở:
- PG function;
- Directus validation;
- Flow;
- Nuxt;
- extension;
- worker;

phải chỉ ra:
- authority;
- mirror/cache/UX;
- migration/retire candidate;
- consumer.

Không cần refactor toàn bộ trong Gate4, nhưng không được để UNKNOWN vô chủ nếu nó chặn Pilot.

## 6.4. Catalog / resolver

Không chuẩn hóa toàn 1.497/3.968.

Chỉ map/canonicalize lazy đúng materials của representative vertical slice.

Phải chứng minh:
- lần dùng thứ hai reuse mapping;
- không tạo duplicate;
- mapping Field semantic ↔ physical column ↔ usage;
- provenance/owner/version.

Full catalog scale vẫn Gate7.

---

# 7. CRITICAL EXECUTABLE PROOF TRONG GATE3–4

Thiết kế/data lock phải có bounded actual proof cho những chỗ nếu sai sẽ làm Pilot thất bại.

## P1 · Release-aware semantic pin

Dùng isolated lab.

1. tạo Release V1 với exact material closure;
2. tạo event/Instance V1;
3. khi event/Instance còn chờ, sửa Form/main hoặc Draft current;
4. runtime Instance V1 vẫn phải:
   - đọc exact V1 semantic material;
   - không lấy current main;
   - tạo đúng effect/result theo V1;
5. event mới theo Binding V2 dùng V2;
6. không double effect.

Nếu release design chọn exact immutable refs thay snapshot, test đúng đường đó.

Nếu native Directus Content Version đủ một phần, reuse; không dựng full custom release DB trước khi loại I0–I6.

## P2 · Current authorization recheck

Giữ semantic V1 pin, nhưng revoke quyền/service/delegation phù hợp trước action.

Expected:
- semantic version không đổi;
- action bị chặn bởi current authority;
- no effect;
- audit/correlation rõ;
- không reinterpret release.

## P3 · Retry classification

Chạy ít nhất:

- transient failure → retry và cuối success;
- permanent validation/version error → không retry vòng lặp vô ích;
- unknown effect → reconcile trước retry;
- auth block → wait/deny theo contract, không blind retry.

## P4 · Contract stale / profile change

Sau release:
- current profile/validator revision đổi.

Instance V1 phải dùng pinned semantic validator/profile version hoặc đường compatibility đã định nghĩa.

Không lấy current profile mới để làm lịch sử V1 tự hỏng, trừ policy safety current-check được contract chỉ rõ.

## P5 · Late missing-ingredient result

Request sinh ở Draft revision X.

Draft đổi/cancel/slot đổi trước khi resource hoàn tất.

Khi result về:
- re-read parent/revision/slot;
- không gắn nhầm;
- giữ provenance;
- route review/resume đúng.

## P6 · Cross-object ownership

Actual/tool-level test tối thiểu:

- MOW binding không sửa MOT Definition;
- MOT binding không sửa MOIT/MOUT Definition;
- MOIT layout không sửa Field meaning;
- MOW binding không sửa global Trigger/Condition;
- NTGV không sửa People identity/delegation source.

---

# 8. IMPLEMENTATION DISCIPLINE CHO PROOF

Mục tiêu là chứng minh contract/data fit, **không build production product**.

Thứ tự bắt buộc:

1. I0 Existing exact;
2. I1 PG native/config;
3. I2 Directus built-in/config;
4. I3 existing Nuxt/internal;
5. I4 ecosystem;
6. I5 compose;
7. I6 thin generic adapter;
8. I7 only with PM disposition.

Trong gói này Agent được:

- thêm TEST fixture;
- thêm lab-only relation/constraint/view;
- thêm minimal generic proof adapter nếu I0–I5 đã có evidence không đủ;
- sửa harness.

Agent **không được**:

- per-workflow code;
- release engine lớn;
- auth engine mới;
- permission engine mới;
- queue algorithm mới;
- catalog DB thứ hai;
- production DDL;
- production deploy;
- rewrite UI.

Mọi code/SQL/Flow script/hook/worker đều kê thật.

---

# 9. PLATFORM CONVERGENCE — LÀM ĐỦ ĐỂ GATE5 KHÔNG BỊ BẤT NGỜ

Không để platform discovery lại từ đầu.

## 9.1. Current public version facts

Refresh official sources tại thời điểm chạy.

Current PM web verification 11/09/2026 cho thấy:
- PostgreSQL 16.15 phát hành 13/08/2026;
- Directus 12.3.1 là current 12.x package candidate;
- Nuxt 4.5.2 current docs/release;
- Node 24.21.0 LTS và 22.23.2 LTS.

Nếu nguồn chính thức thay đổi trước lúc Agent chạy:
- pin latest stable candidate có lý do;
- không chase release vô hạn;
- ghi date/source.

## 9.2. Directus v12 licensing — sửa cách hiểu trong SSOT

Official current model:

- OIG: under $5M annual revenue **và fewer than 50 employees**;
- OIG full platform, cần registration/software key;
- Core không key nhưng bị feature/usage limits;
- OIG eligibility có liên quan **ai là end user của Directus Studio**: nếu client/đơn vị ngoài dùng Studio, eligibility của entity đó có thể material.

Owner đã cung cấp fact revenue dưới ngưỡng; **không hỏi lại revenue**.

Chưa có:
- headcount;
- exact legal/entity scope;
- Studio end-user scope nếu có bên ngoài;
- OIG/software key.

Không được:
- tự apply OIG;
- chấp nhận legal terms;
- gửi company data;
- bypass feature;
- nhập key không được Owner cung cấp.

Sửa SSOT để không diễn đạt “Studio users” như một ngưỡng số thứ ba. Nó là fact để xác định entity/end-user scope.

Directus12 full permission suite giữ `PENDING LICENSE PRECONDITION`, không làm Gate3/4 semantic/data blocker nếu contracts platform-neutral và current bridge evidence đủ.

## 9.3. Nuxt modules

Bounded target compatibility decision:

- kiểm @nuxt/ui / @nuxt/image current target candidates và audit;
- ưu tiên config/reuse;
- không force major chỉ để audit đẹp;
- test FormCustom + DirectusTable + SSR/session + build;
- nếu target major module làm product rewrite lớn, ghi NOT FIT/DEFER và exact reason;
- không production upgrade.

Kết luận một trong:
- TARGET MODULE SET READY CANDIDATE;
- CURRENT MODULE BRIDGE WITH KNOWN RISK;
- BLOCKED BY exact incompatibility.

## 9.4. PG 16.15 minor plan

Read-only production material inspection:

- btree_gist affected opclasses/types;
- NaN relevance;
- ltree use;
- backup/restore/rollback;
- maintenance window assumptions.

Không reindex/upgrade production.

Nộp exact production minor plan để Gate5 không discovery lại.

---

# 10. CONTRACT TEST SUITE — MACHINE CHECKABLE

Không chỉ viết prose.

Tạo structured contract fixtures + validator/test table cho representative slice.

Mỗi material contract phải có:

- valid case;
- missing required;
- wrong type/unit;
- wrong owner/ref;
- stale revision;
- wrong version;
- forbidden scope;
- unknown reference;
- duplicate/replay;
- current-vs-pinned conflict khi áp dụng.

Các case ưu tiên:

1. fake contract ref;
2. stale expected_revision;
3. actor spoof;
4. cross-scope;
5. Field wrong unit;
6. Form current drift vs release pin;
7. profile version drift;
8. revoked permission;
9. duplicate event;
10. same case new occurrence;
11. late missing ingredient;
12. retired component with in-flight Instance;
13. output incomplete;
14. permanent vs transient retry;
15. effect unknown/reconcile;
16. approval/test stale after material change.

Không hard quota nếu contract phát hiện thêm ca material.

---

# 11. GATE3 PASS CRITERIA

Agent chỉ được đề nghị Gate3 ready khi:

- C01–C10 có semantic owner và machine-readable schema/profile/fixture;
- object/action/error/version vocabulary không mâu thuẫn;
- Human UI/Agent/service cùng envelope;
- release closure rõ;
- pin vs current authority rõ;
- retry taxonomy rõ;
- D05 semantics không nhập nhằng;
- D06/D07 có disposition PM hợp lệ;
- D04 là duy nhất có thể còn Owner lock;
- contract tests chạy và không còn material contradiction;
- no business truth in UI/worker;
- platform-specific detail không làm contract phụ thuộc Directus implementation vô lý.

Nếu D04 chưa Owner quyết:
`Gate3 semantic contract READY EXCEPT D04`, không giả DONE.

---

# 12. GATE4 PASS CRITERIA

Agent chỉ đề nghị Gate4 ready khi:

- mọi material contract fact có Data Matrix disposition;
- critical relationships có source/integrity classification;
- every write path có authority + audit + concurrency behavior;
- every read path biết scope/version;
- release closure có actual data representation rõ;
- runtime Instance/Attempt/effect/correlation mapping rõ;
- lazy catalog mapping proof không duplicate;
- business-rule authority register cập nhật;
- NEW_REQUIRED chỉ tồn tại khi reuse I0–I5 đã được loại bằng evidence;
- không có “table TBD” cho material Pilot fact mà không có blocker/owner;
- P1–P6 bounded proofs kết thúc với expected results hoặc material blocker thật.

---

# 13. DỮ LIỆU PRODUCTION / AN TOÀN

Production:

- read-only metadata/source/config khi cần;
- không DML/DDL;
- không restart;
- không Flow trigger;
- không apply permission;
- không license activation;
- không reindex/upgrade;
- không gửi external effect.

Lab:

- synthetic;
- isolated;
- no public port;
- no production mail/webhook;
- own credentials/volumes/networks;
- cleanup + proof demo unchanged.

Không gọi safe GET là full regression.

---

# 14. SSOT — BẮT BUỘC KIỂM TOÀN FILE VÀ GHI MỘT LẦN Ở CUỐI

Backup v1.6.16.

Dự kiến version tiếp theo **v1.6.17**.

Trước write cuối:
- generate staged copy;
- run static consistency sweep;
- browser/DOM check Owner/Gates;
- compare IDs/anchors/scripts/styles;
- then one final write.

## 14.1. Ghi PM Gate2 acceptance

Cập nhật đồng bộ:

- Owner Cockpit;
- gate strip;
- Current Review;
- PM Control Panel;
- Work Queue;
- W004;
- Gate control;
- Current State;
- Decision Log;
- History;
- footer.

Acceptance record:

```text
W004-GATE2 / Gate2
PM Verdict: ACCEPT WITH FOLLOW-UP / DONE
Accepted Scope: 8 capability groups ×12 attributes; 5 canonical patterns; R9 happy +10 negative design walkthroughs; platform/rule findings correctly scoped
Evidence: Gate2-R9-v1.6.16-2026-09-11-evidence.zip (494/494 manifest items verified)
Accepted by: GPT Chat / PM
Accepted date: 11/09/2026
Follow-up: Gate3 Contract + Gate4 Data; platform adoption prerequisites; Pilot Gate5/6
Limit: design/composition acceptance, not production or O1–O3 verification
```

Gate3/Gate4 trở thành active/submitted theo actual work.

## 14.2. Ghi Gate3/Gate4 evidence

Thêm:
- contract suite;
- Contract→Data Matrix;
- relation map;
- action/error taxonomy;
- release closure;
- P1–P6 proof;
- platform convergence;
- D05–D07 dispositions;
- D04 current state;
- blockers/follow-up.

Không paste toàn JSON vào Owner layer.

## 14.3. Sửa các điểm stale đã PM phát hiện trong v1.6.16

Ít nhất:

### S1
`Custom Code Register · Current v1.6.15`
→ sửa thành current version phù hợp và bổ sung Gate2 lab/workshop code burden, không chỉ Gate0.

### S2
`TEXT-ONLY FREEZE`
hiện dừng ở v1.6.14.
→ cập nhật lịch sử v1.6.15/v1.6.16 và quy tắc current.

### S3
Accepted architecture reference còn câu:
`R2–R8 đã nộp, PM xét Gate1 exit`
→ Gate1 đã PM ACCEPT/DONE; sửa current sentence, giữ historical source riêng.

### S4
Các câu kiểu:
`Đầu ra ngay sau bản tổng hợp này: rà MOW...`
nếu nằm trong phần current-looking nhưng thực chất roadmap v1.1:
→ ghi HISTORICAL rõ hoặc sửa để không cạnh tranh Next Action current.

### S5
MEM01/source wording kiểu:
`Không sửa các nguồn kia trong lượt này`
phải làm rõ đây là phạm vi W002-MEM lịch sử, **không phải cấm vĩnh viễn**, vì RULE-SYNC 11/09 đã được authorized và có receipts.

### S6
License wording:
- revenue fact giữ OWNER-PROVIDED;
- qualification còn headcount/entity scope;
- Studio end users dùng xác định entity scope, không là ngưỡng số độc lập;
- Core vs OIG feature limit rõ;
- key required cho OIG;
- không giả eligible/activated.

### S7
Release pin:
đưa counterexample event4 thành current architecture/data requirement, không chỉ link buried trong Platform section.

## 14.4. Full current-status sweep

Tìm toàn file:

- Gate2 SUBMITTED / PM REVIEW;
- READY FOR PM GATE2 EXIT REVIEW;
- Gate3 NOT STARTED;
- Gate4 NOT STARTED;
- PM xét Gate1 exit;
- v1.6.15 current;
- stale Next action;
- stale platform/license statement;
- stale D06/D07 OPEN nếu PM decision đã khóa;
- old “current” descriptions không có HISTORICAL marker.

Historical rows giữ nguyên trạng thái theo ngày, có nhãn HISTORICAL.

## 14.5. SSOT quality rule

SSOT vẫn là **CURRENT PROJECT MEMORY duy nhất**.

Không tạo tài liệu kiến trúc thứ hai thay SSOT.

Evidence ZIP/README chỉ là evidence.

Sau write, phải kiểm:
- no duplicate IDs;
- no broken internal anchors;
- Owner layer phản ánh state đúng;
- Gate/work/decision/footer khớp nhau;
- no stale current status;
- backup hash = old current;
- read-back = staged bytes.

---

# 15. FINAL SELF-QA TRƯỚC KHI ĐƯỢC BÁO CÁO

Bắt buộc tự trả lời PASS/FAIL từng mục:

## A · Gate2 PM merge
- [ ] PM acceptance đã ghi đủ current sections.
- [ ] Không tự biến Gate2 thành production PASS.

## B · Contract
- [ ] C01–C10 complete.
- [ ] vocabulary/version/error không mâu thuẫn.
- [ ] same Human/Agent/service action contract.
- [ ] release pin semantics complete.
- [ ] retry taxonomy complete.

## C · Data
- [ ] Contract→Data matrix complete.
- [ ] typed relation map complete.
- [ ] write/read authorities complete.
- [ ] where-used/provenance complete for vertical slice.
- [ ] NEW_REQUIRED có evidence loại reuse.

## D · Critical proofs
- [ ] P1 main drift vẫn chạy old pinned semantics.
- [ ] P2 permission revoke blocks current action.
- [ ] P3 retry taxonomy actual.
- [ ] P4 profile/contract drift handled.
- [ ] P5 late ingredient safe.
- [ ] P6 ownership boundaries safe.

## E · Platform
- [ ] Official version facts refreshed.
- [ ] Directus license facts corrected.
- [ ] no entitlement bypass.
- [ ] Nuxt target module disposition evidence.
- [ ] PG minor production plan evidence.
- [ ] target/full-current distinctions không trộn.

## F · Code minimal
- [ ] I0–I5 inspected before I6/I7.
- [ ] no per-workflow code.
- [ ] no competing truth.
- [ ] every code/SQL/Flow/worker counted.
- [ ] maintenance/exit stated.

## G · Safety
- [ ] no production DML/DDL/deploy/restart.
- [ ] lab cleaned.
- [ ] demo process/safe smoke unchanged with stated limitation.
- [ ] secrets/private data absent evidence.

## H · SSOT
- [ ] v1.6.16 backup.
- [ ] one final current write.
- [ ] known stale S1–S7 fixed.
- [ ] full current-status sweep pass.
- [ ] IDs/anchors/style/script integrity pass.
- [ ] snapshot byte-identical current after write.

Chỉ báo PM khi checklist đã hoàn tất.

---

# 16. OUTPUT / EVIDENCE PACKAGE

Nộp một ZIP có:

- `README.md` — báo cáo PM;
- `summary.json`;
- contract schemas/profiles/fixtures;
- contract test results;
- Contract→Data Matrix;
- typed relation map;
- data authority/business-rule register;
- release closure decision;
- P1–P6 raw results;
- platform verdict;
- official-source receipts;
- Nuxt module compatibility result;
- PG minor plan;
- code/dependency inventory;
- cleanup results;
- SSOT snapshot;
- SSOT write receipt;
- static QA;
- manifest SHA256.

Không cần Owner đọc từng file.

---

# 17. BÁO CÁO OWNER — TỐI ĐA 12 Ý, CHỈ SAU KHI XONG

1. Gate2 PM acceptance đã nhập SSOT chưa.
2. Gate3 contracts đã khóa được gì.
3. Gate4 actual data mapping đã khóa được gì.
4. Release-pin counterexample đã được giải thế nào.
5. Retry/permanent/unknown-effect đã chứng minh ra sao.
6. Contract Human/Agent/service có thật sự một đường không.
7. Bao nhiêu existing data/relation reuse; bao nhiêu NEW_REQUIRED; bao nhiêu UNKNOWN.
8. Business truth còn nằm bao nhiêu nơi và disposition.
9. Platform target current verdict.
10. Tổng custom code/dependency/process mới của **gói này**.
11. D04/D05/D06/D07 final states.
12. Kết luận duy nhất:
   - `READY FOR PM GATE3+4 EXIT REVIEW`,
   - `READY ... — OWNER D04 LOCK PENDING`,
   - hoặc material blocker.

Không báo các subtask lẻ.

---

# 18. STOP / ESCALATION RULE

Agent được tự sửa/rerun trong lab cho đến khi đạt.

Dừng và báo blocker chỉ nếu:

- requirement buộc per-workflow custom logic;
- release closure không thể bảo toàn mà không tạo competing truth;
- actual data source không xác định được cho material Pilot fact;
- authority cần Owner/legal decision;
- target feature bị license/entitlement ngăn và không có đường platform-neutral để hoàn thành contract/data;
- giải pháp cần production mutation;
- cost/risk vượt phạm vi có thể đảo ngược.

Không gọi “BLOCKED” vì một test đầu tiên fail; phải điều tra, sửa trong phạm vi và rerun trước.

---

## KẾT LUẬN ĐIỀU HÀNH

Gate2 đã trả lời:

> **Con người và máy sẽ đi qua hệ thống theo những pattern nào.**

Gói này phải trả lời dứt điểm:

> **Mỗi bước nói cùng một ngôn ngữ contract nào, sự thật nằm ở dữ liệu nào, và runtime làm sao giữ đúng phiên bản đã duyệt mà vẫn recheck quyền hiện hành.**

Sau đó mới đáng mở Formal Pilot A/B.

Không xây thêm trước khi Contract/Data thật sự khóa.


---

# Nhận xét PM kèm theo

Tôi đã kiểm trực tiếp cả ZIP bằng chứng lẫn file cấu trúc hệ thống.html v1.6.16 anh gửi, không chỉ dựa trên báo cáo Codex.
Tôi chốt:
Gate2 / W004: ACCEPT WITH FOLLOW-UP / DONE trong phạm vi thiết kế/composition.
Căn cứ chính:
- 494/494 file được liệt kê trong manifest khớp SHA-256. 
-  File SSOT anh đính kèm byte-identical với snapshot trong ZIP, SHA256 e802f944...bad3f5. 
-  8 nhóm đều có đủ 12 thuộc tính, tức 96 phần thiết kế. 
-  Happy path + 10/10 negative cases đều đi từ block → xử lý → tiếp tục đến cuối. 
-  QA của Agent 15/15 trong phạm vi họ tự định nghĩa; tôi kiểm lại các bằng chứng trọng yếu và không thấy việc họ đánh tráo workshop thành production proof. 
-  O1–O3 vẫn giữ NOT VERIFIED, đúng. SSOT cũng đang thể hiện Gate0/Gate1 DONE nhưng Gate2 mới SUBMITTED để chờ PM, tức Agent không tự nghiệm thu mình.  
Ba vấn đề kỹ thuật còn lại không phải lý do giữ Gate2 mở. Chúng được route đúng sang Contract/Data/production preparation.
Event4 chứng minh một lỗ hổng kiến trúc thực sự đáng giá:
Instance đã pin Release V2 nhưng runtime vẫn đọc Form main; khi main đổi revision, job thất bại hai lần với FORM_REVISION_CONFLICT.
Điều đó có nghĩa “release snapshot” hiện nay chưa thực sự cô lập semantic material của lượt chạy. Đây sẽ là yêu cầu cứng số 1 của Gate3+4. Tôi không cho phép chữa bằng cách bỏ kiểm revision hay dùng latest/main.
File đính kèm đúng là v1.6.16. 
Và chính tài liệu vẫn quy định rõ cấu trúc hệ thống.html là CURRENT PROJECT MEMORY, giữ kiến trúc, quyết định, vấn đề mở, trạng thái và traceability hiện hành. 
Như vậy cách chúng ta đang làm là đúng:
Chat chỉ dùng để PM phân tích/quyết định. Mọi kết luận có giá trị lâu dài cuối cùng phải được nhập trở lại chính file này.
Nó đã có Gate2/R9, 8 groups, 5 patterns, platform rehearsal, RULE-SYNC, counterexample release pin, Directus12 license issue, target versions và D04. 
Nhưng tôi không xác nhận rằng v1.6.16 đã sạch 100% current-state. Tôi tìm thấy vài chỗ cần sửa ở lần cập nhật tiếp theo:
- Custom Code Register vẫn ghi “Current v1.6.15” mặc dù tài liệu là v1.6.16.  
- TEXT-ONLY FREEZE mới kể lịch sử đến v1.6.14, thiếu v1.6.15/v1.6.16.  
-  Một đoạn accepted architecture vẫn ghi “R2–R8 đã nộp, PM xét Gate1 exit”, trong khi Gate1 đã được PM ACCEPT/DONE.  
-  Một số câu lịch sử như “đầu ra ngay sau bản tổng hợp này…” vẫn có dáng câu current và cần đánh HISTORICAL rõ hơn. 
-  MEM01 có câu “không sửa các nguồn kia trong lượt này”; cần làm rõ đó là scope lịch sử của W002-MEM, không phải lệnh cấm vĩnh viễn, vì RULE-SYNC 11/09 đã được phép sửa các nguồn rule. 
Tôi đã đưa toàn bộ yêu cầu sweep này vào lệnh Codex tiếp theo, để không phải sửa riêng thêm một revision chỉ vì câu chữ.
Các version Codex dùng là hợp lý và tôi đã kiểm độc lập bằng nguồn hiện hành:
-  PostgreSQL 16.15, phát hành 13/08/2026.  
-  Directus 12.3.1 hiện là bản 12.x package mới nhất được surfaced.  
-  Nuxt 4.5.2 hiện hành.  
-  Node 24.21.0 LTS và 22.23.2 LTS đều hiện hành.  
Có một điểm tôi đã sửa trong lệnh tiếp theo về Directus license: OIG hiện yêu cầu dưới $5M doanh thu năm và dưới 50 nhân viên, và cần software/registration key. Việc ai đăng nhập Directus Studio quyết định entity nào phải đáp ứng điều kiện, chứ “số Studio users” không phải một ngưỡng eligibility thứ ba. OIG cho toàn bộ platform; Core không key thì bị giới hạn tính năng. 
Do anh mới xác nhận doanh thu, chúng ta chưa xác nhận OIG eligibility toàn phần vì chưa có headcount/entity scope. Việc này không cản Contract/Data, nhưng cản việc tuyên bố Directus12 full-target production-ready.
Tôi không giao riêng “hãy sửa release pin”, rồi quay lại “hãy lập contract”, rồi lại “hãy map data”.
Codex được giao một package duy nhất:
Khóa đồng bộ toàn bộ:
Identity/version/revision → Context → Human/Agent/service action → reuse/admission → contracts MOW/MOT/MOIT/MOUT/... → Release/Activation → Event/Instance/Attempt → error/retry/reconcile → Test/Approval/Publish → Audit.
Sau đó map toàn bộ semantic contract xuống:
PG/Directus source thật → field/type/unit → read/write → quyền → typed relations → FK/enforcement → where-used → version/pin → audit → disposition reuse/new/unknown.
Không chuẩn hóa cả 4.000 cột. Chỉ khóa đủ cho representative vertical slice.
Đặc biệt:
1.  Instance V1 vẫn chạy đúng semantic V1 sau khi Form main bị sửa. 
2.  Nhưng nếu quyền hiện hành bị thu hồi thì action vẫn phải bị chặn. 
3.  Permanent error không bị retry vô ích. 
4.  Transient error mới retry. 
5.  Effect không rõ thì reconcile trước retry. 
6.  Result của missing ingredient về muộn không được gắn vào Draft đã thay đổi. 
7.  MOW/MOT/MOIT/Field/NTGV không sửa chéo ownership. 
Codex không được báo cáo sau từng phần. Nó phải tự sửa/rerun cho tới khi cả package đạt checklist hoặc chỉ còn một blocker thực sự có evidence.
Tôi giữ khuyến nghị D04-A:
- executor = người/service thực hiện task hiện tại; 
- delegate = người làm thay theo ủy quyền; 
- next-task executor/recipient = người chịu trách nhiệm công việc kế tiếp; 
- report recipient = người nhận báo cáo/thông tin; 
- handoff contact = đầu mối bàn giao/liên hệ. 
Năm nghĩa này không được dùng lẫn nhau.
Đây là quyết định liên quan trách nhiệm con người nên tôi không tự ghi “Owner ACCEPT”. Codex được yêu cầu làm toàn bộ Gate3+4 mà không dừng chờ câu này; nếu đến cuối anh chưa quyết, nó chỉ được báo:
READY FOR PM GATE3+4 EXIT REVIEW — OWNER D04 LOCK PENDING
Tôi khuyến nghị anh chọn A. Đây là cách ít nhập nhằng nhất và giữ NTGV, People, Delegation đúng ownership.
Lệnh Codex — thực hiện trọn Gate3 + Gate4 Contract & Data Lock
Không cần gửi thêm file nào khác nếu vẫn là workspace Codex hiện tại.
Lệnh này cũng bắt Codex cuối lượt phải cập nhật chính cấu trúc hệ thống.html đúng một lần, gồm PM acceptance Gate2, toàn bộ Contract/Data mới, findings/proofs mới và sweep sạch những câu current bị stale mà tôi vừa chỉ ra.
Như vậy vòng tiếp theo, mục tiêu của chúng ta không phải “xem thêm một phần thiết kế”, mà là có đủ Contract + Data để quyết định mở Formal Pilot A/B hay chưa. 