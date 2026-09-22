# Lệnh giao Codex — đóng Gate 0 bằng một lát cắt UI + Runtime thực

**PM: GPT Chat · 10/09/2026**  
**Nguồn current:** `/Users/nmhuyen/Desktop/quy trình/cấu trúc hệ thống.html` — hiện v1.6.12.  
**Bằng chứng đã có:** gói `Proof-Cong-Ghi-2026-09-10-evidence.zip` và các output liên quan trong workspace hiện tại.

Đây là **lệnh thực thi proof**, không phải vòng thiết kế mới.

---

## 1. Quyết định PM đã chốt trước khi chạy

### 1.1. Phần đã nhận

**Retrieval / lexical Proof A:** PM ACCEPT / DONE trong phạm vi đã đo trước đó.  
Không tune lại search, không mở vector, không chuẩn hóa toàn kho.

**Scoped write-gate Proof:** PM ACCEPT trong **phạm vi Gate 0 authority/write/audit** dựa trên bằng chứng mới:

- 66/66 ca chính PASS;
- 20/20 assertion read-back/audit PASS;
- hai writer cùng revision → một 200, một 409;
- exact retry không tạo effect mới; cùng key khác payload → 409;
- forced rollback không để partial business mutation;
- fake contract/stale revision và các bypass trong phạm vi đã thử bị chặn;
- Agent phiên độc lập đọc state thật rồi ghi tiếp record revision 2→3;
- required extension lỗi load → app lab dừng, restore đúng bytes.

**Không cần chạy lại toàn bộ 66 ca nếu guard không thay đổi.** Giữ hash/source và chạy regression subset đúng phần bị chạm ở lượt này.

### 1.2. Cách hiểu đúng về custom code hiện có

Một Directus bundle guard hiện có:

- 163 dòng JS lõi;
- 2 dòng app export;
- metadata;
- 50 dòng PG relational DDL;
- 0 production deploy.

PM nhận nó là:

> **FEASIBILITY IMPLEMENTATION CANDIDATE đã chứng minh được trên exact lab hiện tại.**

Không gọi nó là production architecture cuối cùng.

Lý do chấp nhận candidate này: exact đường native/config đã thử không cưỡng chế được contract + expected revision theo requirement, còn candidate dùng lại ItemsService/accountability/Joi/transaction/FK của PG và không chứa business logic riêng cho từng Field/MOW.

**Trước production/target stack sau này vẫn phải kiểm lại built-in của target version.** Nếu target có đường native tương đương với ít bảo trì hơn, ưu tiên thay guard; không giữ custom chỉ vì đã viết.

### 1.3. Trạng thái còn lại

- Factory architecture = DONE.
- Proof B authority/write/audit = đủ Gate0 scope theo acceptance trên.
- Authoring kernel đã có retrieval + draft/write + fresh-Agent resume evidence.
- **UI declarative integration = NOT RUN.**
- **Immutable business release/pin = chưa có; `main` chỉ Draft.**
- **Proof C autonomous runtime = NOT RUN.**
- Gate0 = DOING cho tới PM exit review.
- O1–O3 vẫn NOT VERIFIED.
- R1 full UI review chưa mở.

---

# 2. MỤC TIÊU DUY NHẤT LƯỢT NÀY

Chứng minh bằng actual evidence một lát cắt nhỏ:

```text
AI/Agent thay đổi khai báo
→ UI hiện đúng thay đổi mà không viết code riêng cho form đó
→ người nhập qua đúng guarded write action
→ save/read-back/reopen đúng
→ một immutable TEST release fixture được pin
→ event thật trong lab
→ runtime tự nhận việc khi KHÔNG có Agent điều phối
→ một AUTO MOT thực hiện safe internal action
→ result + attempt + ACK/FAIL + audit/correlation
```

Nếu lát cắt này PASS, nộp:

> `READY FOR PM GATE0 EXIT REVIEW`

**Codex không tự đóng Gate0.**

Không dùng một proof PASS để tuyên bố O1/O2/O3 VERIFIED.

---

# 3. GIỮ LÁT CẮT RẤT NHỎ

Dùng lại family hiện có:

- 1 MOW test;
- 1 MOT test;
- 1 MOIT/form test;
- 3 Field hiện có: duration, system-created date, note;
- write gate đã chứng minh;
- một safe internal AUTO action.

Không thêm business domain mới.

Không chuẩn hóa catalog toàn hệ.

Không full HMITL/NTGV.

Không long-wait/backpressure/load/DR.

Không external email/webhook/payment/file side effect.

Không full R1 UI review.

---

# 4. PHẦN U — AI KHAI BÁO → UI TỰ PHẢN ÁNH

## U0. Chọn đúng renderer hiện hữu, không rà cả hệ thống

Bắt đầu từ exact source/build đã biết:

`Form block → UForm → FormCustom`

Current evidence cho thấy UForm đã đọc `form.schema` để dựng input nhưng submit đang hard-code vào inbox.

Chỉ kiểm bounded source cần thiết để trả lời:

1. renderer hiện hữu có thể nhận submit action/config hay chưa;
2. có composable/transport/helper hiện hữu nào ghép được không;
3. có đường read-back/edit record hiện hữu reuse được không.

Không mở W003/R1 và không rà tất cả UI.

Nếu tìm thấy existing path phù hợp → dùng lại.

## U1. Code-last rule cho UI

Ưu tiên:

1. existing config/prop/action;
2. existing composable/helper;
3. compose các khối đang có;
4. **chỉ nếu 1–3 không đủ:** được sửa/thêm **một generic submit transport/adapter dùng chung** cho renderer hiện hữu.

Không tạo renderer/page riêng cho form test.

Không branch code theo:

- `field.so_phut`;
- `field.ghi_chu`;
- ID MOW/MOT/form test;
- tên collection nghiệp vụ cụ thể.

Business target/profile phải do server route/policy quyết như write-gate hiện tại; UI không được chọn tên bảng tùy ý.

Nếu phải sửa `.vue`/composable, đây là product code và phải kê đúng LOC/purpose/maintenance. Không gọi là config.

## U2. Ca chứng minh quan trọng nhất

Dùng **hai revision khai báo**, nhưng **không đổi UI code giữa hai revision**.

### U2-A · Declaration V1

AI/Agent dùng guarded write path tạo/cập nhật form chỉ có:

- duration_minutes;
- date_created system field.

Boot một Nuxt lab/rehearsal cô lập hoặc một đường browser thực tương đương dùng exact current renderer.

UI phải tự hiện đúng trường người nhập được và không cho người nhập system-created date.

### U2-B · Declaration V2

Sau khi UI V1 đã chạy:

AI/Agent chỉ thay **declaration/data** qua write gate để thêm Field `note` đã tồn tại.

Từ thời điểm update declaration V1→V2:

**không sửa code, không rebuild UI chỉ để biết Field note.**

Reload/refetch cùng form.

PASS khi UI tự xuất hiện thêm ô note từ declaration mới.

Đây là phép thử trực tiếp requirement:

> AI khai báo → UI phản ánh.

Nếu phải thêm code riêng sau khi thêm note → FAIL mục tiêu declarative UI.

## U3. Submit và read-back

Từ UI thật:

1. nhập duration + note;
2. submit qua guarded action;
3. request có `request_id` ổn định và `expected_revision`;
4. server quyết profile/target;
5. nhận record ID + revision;
6. read-back từ canonical source;
7. mở lại UI và thấy đúng dữ liệu đã lưu.

Test thêm:

- input sai datatype → UI nhận lỗi server, không giả success;
- UI stale revision → server 409;
- UI không được tự lấy revision mới rồi replay payload cũ âm thầm;
- sau conflict phải refetch và yêu cầu resolve/merge phù hợp;
- retry exact logical request không tạo record/effect thứ hai.

Không coi HTTP/API test cũ là UI PASS; phải có actual browser/UI evidence.

## U4. Evidence UI

Nộp tối thiểu:

- source/hash renderer trước và sau;
- config/adapter thay đổi nếu có;
- browser request/response;
- ảnh hoặc browser evidence V1;
- declaration-only update;
- ảnh/browser evidence V2 tự xuất hiện note;
- submit/read-back/reopen;
- stale 409 behavior;
- số product code/config mới.

Không cần làm UI đẹp trong proof.

---

# 5. PHẦN R — EXACT VERSION PIN CHO PROOF C, KHÔNG XÂY FULL RELEASE ENGINE

Current `main` là editable Draft và **không được dùng làm bằng chứng immutable runtime version**.

Gate0 không yêu cầu dựng full T4/release system.

Dùng đường ít nhất theo thứ tự:

1. reuse một immutable/versioned mechanism hiện hữu **nếu exact semantics được chứng minh**;
2. nếu không có, tạo **TEST-ONLY immutable release fixture/snapshot** tối thiểu trong lab chỉ để Proof C pin được exact set.

Fixture phải chứa/ref đủ để runtime biết chính xác:

- MOW test version;
- MOT test version;
- form/contract version cần dùng;
- AUTO capability/action version;
- hash/revision identity nếu cần.

Business test identities không được sửa release fixture sau khi tạo.

Tạo V1 trước khi runtime.

Sau đó có thể tạo V2, nhưng instance đã sinh từ V1 vẫn phải đọc V1.

**Không gọi test fixture này là production release model.**

Không dùng Directus content-version `main`/delta làm immutable business release nếu semantics đó chưa được chứng minh.

---

# 6. PHẦN C — AUTONOMOUS RUNTIME KERNEL

## C0. Không Agent orchestration

Proof C chỉ PASS khi:

> sau khi event được tạo, không có Agent/human nào phải chọn tool, claim job, gọi capability hoặc ACK thủ công.

Agent được phép chuẩn bị fixture và phát event test.

Sau event:

**runtime process tự chạy.**

## C1. Trước khi build: quyết candidate bằng actual evidence, không bằng chủ thuyết

Không dựng hai runtime đầy đủ.

Xét rất ngắn các candidate thực tế đã biết:

### Candidate 1 · Existing PG `job_queue` + `fn_job_enqueue/claim/ack`

Ưu điểm: đã có PG primitives.

Phải kiểm exact source/gap đã biết:

- lease expiry semantics;
- ACK/summary persistence;
- authority/service boundary;
- mapping event/job/instance/attempt;
- lượng generic worker code vẫn cần.

Không chọn chỉ vì “đã có bảng”.

### Candidate 2 · pg-boss

Đã được triage là ecosystem candidate phù hợp version PG/Node Directus đã đo.

Nếu xét:

- pin exact package version;
- lab only;
- một worker process riêng, không nhét worker vào CMS process;
- tính cả dependency/schema/process/upgrade burden;
- vẫn cần generic capability handler và mapping business state.

Không chọn chỉ vì thư viện nổi tiếng.

### Candidate 3 · Directus-native/current composition

Prior evidence đã không tìm thấy bridge đáp ứng contract hiện tại.

Không rà lại toàn bộ Directus 11.5.1 từ đầu.

Chỉ hồi sinh candidate nếu có **actual new evidence** về một path native chưa được kiểm trước đó.

### Quy tắc chọn

Chọn đúng **một** candidate có:

- correctness đủ contract;
- ít custom logic nhất;
- ít moving parts nhất;
- không duplicate business truth;
- maintenance/upgrade/exit rõ nhất.

Không đặt LOC threshold giả.

Không viết lại queue/retry/locking nếu ecosystem/native đã làm tốt hơn.

Nếu existing queue cần vá nhiều queue semantics riêng, ưu tiên library mature thay vì tự xây queue.

Nếu existing queue chỉ cần generic executor rất mỏng và giữ nguyên primitives an toàn, reuse nó có thể rẻ hơn thêm queue schema mới.

Ghi decision bằng evidence rồi **triển khai chỉ candidate được chọn**.

Không cần hỏi Owner cho lựa chọn kỹ thuật đảo ngược này.

## C2. Runtime contract nhỏ nhất

Dùng event test nội bộ.

```text
event occurrence
→ dedup/correlation
→ create/load Instance + exact TEST release V1
→ enqueue/claim
→ create Attempt
→ invoke one registered safe AUTO capability
→ capability gọi guarded write action bằng service identity
→ persist result/evidence
→ ACK hoặc FAIL
```

Safe AUTO capability có thể là một `WRITE_RECORD`/internal status-result action trên fixture.

Không external effect.

Business semantics phải ở declaration/release fixture/PG, không hard-code trong worker.

Worker chỉ:

- claim;
- load exact contract/version;
- dispatch registered capability;
- persist result;
- ACK/FAIL.

Không branch riêng theo MOW test.

## C3. Bắt buộc test

### C3-A · Happy path

Một event → đúng một Instance → đúng một Attempt → đúng một safe effect → ACK success.

### C3-B · Duplicate event

Gửi lại cùng occurrence/correlation theo contract.

Không tạo effect thứ hai.

Không nuốt một occurrence mới hợp lệ chỉ vì cùng business case.

### C3-C · Exact version pin

Instance 1 sinh từ TEST release V1.

Sau đó tạo V2.

Retry/inspect Instance 1 vẫn dùng V1.

Event mới theo binding test có thể dùng V2.

Không resolve `latest/main` khi xử lý Instance cũ.

### C3-D · Không Agent

Log/process evidence cho thấy runtime process tự đi từ queued/event tới result/ACK.

Không có command thủ công ở giữa để claim/action/ack.

### C3-E · Restart tối thiểu

Ít nhất một smoke:

- restart riêng runtime worker/process;
- durable event/work vẫn được xử lý hoặc reconcile từ PG/queue;
- không double effect.

Không cần production-grade crash matrix.

### C3-F · Authority/audit

Trace được:

`event/correlation → job/work → Instance → Attempt → capability version → guarded write receipt → result/ACK`

Service identity không biến thành human approver.

---

# 7. CODE / HẠ TẦNG — HARD BOUNDARY

Mục tiêu không phải “0 code”.

Mục tiêu:

> **Dùng xã hội/platform đã làm trước; chỉ tự code phần nối generic thật sự thiếu.**

Lượt này:

- không fork Directus;
- không viết workflow engine;
- không viết queue algorithm riêng nếu candidate có sẵn;
- không per-MOW/per-form code;
- không thêm search/vector;
- không thêm Kafka/Redis/graph DB;
- không sửa production;
- không nâng Directus/Nuxt chỉ để làm proof;
- không đụng 5 container demo;
- không public lab ports/credentials;
- không dùng dữ liệu học viên thật.

Kê riêng:

1. product code mới;
2. existing product code sửa;
3. SQL/DDL mới;
4. dependency mới;
5. process/container mới;
6. test harness;
7. code candidate hiện có vẫn phải bảo trì.

Không dùng “LOC thấp” để che thêm một service lớn.

---

# 8. REGRESSION WRITE-GATE

Nếu write-gate source/hash **không đổi**:

không cần chạy lại 66/66.

Chạy regression subset tối thiểu qua UI/runtime:

- valid human write;
- valid service write;
- fake contract;
- wrong scope;
- stale revision;
- exact replay;
- different-payload same key;
- native bypass;
- audit correlation.

Nếu guard thay đổi:

phải chạy lại full frozen suite 66/66.

---

# 9. ĐIỀU KIỆN ĐỂ BÁO “READY FOR PM GATE0 EXIT REVIEW”

Chỉ báo READY khi tất cả dưới đây có actual evidence:

### A · Bounded authoring feasibility

- retrieval path đã ACCEPT;
- AI thay declaration;
- cổng ghi bảo vệ declaration;
- Agent mới resume được;
- UI đọc declaration và tự phản ánh thay đổi mà không per-form code.

### B · Authority/write/audit

- scoped write-gate acceptance giữ nguyên sau regression;
- UI và runtime đều đi qua authority/audit hợp lệ.

### C · Autonomous runtime

- no-Agent event→AUTO→result→ACK chạy được;
- duplicate không double effect;
- exact TEST release pin giữ được;
- worker restart smoke không mất/double work.

### Feasibility implementation shape

Phải chỉ ra được:

- phần nào dùng PG;
- phần nào dùng Directus;
- phần nào dùng Nuxt;
- dependency/ecosystem nào dùng;
- custom code tối thiểu còn lại;
- maintenance owner cần có ở production;
- đường thay custom bằng target built-in sau này.

Không cần:

- full HMITL/NTGV;
- full release governance;
- full UI selection;
- full catalog;
- scale/load;
- production deploy.

---

# 10. NẾU FAIL

Không mở architecture revision để “giải thích”.

Nếu UI FAIL:

- nộp exact source/gap;
- chỉ rõ generic capability thiếu;
- lượng thay đổi tối thiểu;
- không dựng renderer mới hàng loạt.

Nếu runtime FAIL:

- nộp candidate, exact failure và maintenance cost;
- nếu candidate đầu không fit thì được thử candidate thứ hai **chỉ sau khi first candidate đã có evidence NOT FIT**;
- không viết engine vô hạn.

Nếu immutable fixture/pin FAIL:

- không dùng `main/latest` để làm đẹp demo;
- báo đúng gap.

---

# 11. SSOT

Chỉ cập nhật SSOT **một lần sau actual evidence**.

Version tiếp theo theo sequence hiện hành.

Ghi PM acceptance:

- retrieval = ACCEPT/DONE;
- scoped write-gate = PM ACCEPT cho Gate0 authority/write/audit;
- custom guard = feasibility candidate, 0 production deploy.

Sau lượt này Codex chỉ được đề xuất:

- `READY FOR PM GATE0 EXIT REVIEW`, hoặc
- `PARTIAL/FAIL` với đúng blocker còn lại.

**Không tự đổi Gate0 DONE.**
**Không tự đổi O1–O3 VERIFIED.**
**Không tự mở R1.**

PM/GPT sẽ review evidence và quyết định đóng Gate0.

---

# 12. BÁO CÁO CHO OWNER — TỐI ĐA MỘT MÀN

Báo đúng 8 ý:

1. UI dùng renderer nào, reuse gì.
2. AI đổi declaration thì UI có tự đổi không.
3. Submit/read-back/conflict có PASS không.
4. Runtime candidate nào được chọn và vì sao.
5. Event→AUTO→ACK có tự chạy không.
6. Duplicate/version pin/restart kết quả gì.
7. Tổng custom product code/dependency/process mới.
8. Kết luận: READY FOR PM GATE0 EXIT REVIEW hay còn đúng blocker nào.

Không kể toàn bộ harness/debug trừ khi FAIL ảnh hưởng kết luận.

---

## Kết luận điều hành

**Không thiết kế thêm. Không làm đẹp demo. Không cố giữ “zero-code”.**

Mục tiêu của lượt này là trả lời bằng chạy thật:

> Với PG + Directus + Nuxt đang có, cộng đúng phần nối generic tối thiểu nếu thật sự cần, liệu chuỗi **AI khai báo → UI tự hiện → người nhập → hệ thống tự chạy AUTO không cần Agent** có khả thi và bảo trì được hay không?

Đó là bằng chứng cuối cần để PM quyết định Gate0.
