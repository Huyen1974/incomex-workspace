# PROMPT — HJW · N1 CLOUD CONNECTOR TWIN + SYNC FOUNDATION

RUN_ID: HJW-N1-CLOUD-TWIN-SYNC-20261005-01
STATUS: DRAFT · chờ Claude Chat Reviewer rà một lượt; CHƯA READY, CHƯA RUN
Reviewer: Claude Chat · pending
Host: GPT Chat · GPT-HJW-260922-A
Executor_Surface: Claude Code CLI
Write_Path: repo qua workspace_*; mutation runtime/config chỉ qua DOT/wrapper/apply path hiện hữu đã được bảo vệ; không ad-hoc.
Node: N1 / 6 · Roadmap SSOT HJW 0.17
Owner_intent: **KHÔNG MOVE khỏi MacBook. Giữ nguyên môi trường Mac để Owner tiếp tục làm việc; tạo cloud twin tương đương phục vụ automation và thiết lập cơ chế đồng bộ thay đổi nhanh về sau.**

## 0. Mục tiêu duy nhất

Hoàn thành **N1 = Cloud Connector Twin + Sync Foundation** trong **một PROMPT / một RUN**:

1. Kiểm kê toàn bộ custom Incomex MCP/connector liên quan GPT, Claude, Hermes và người thi hành.
2. **Giữ nguyên bản Mac đang dùng**; không uninstall, disable, thay local bằng cloud hoặc làm giảm chức năng Mac.
3. Với mọi connector **cloudable**, cloud phải có một **functional twin** đủ tool/schema/chức năng cần thiết. Cloud/web automation dùng twin cloud; Mac vẫn dùng local khi cần.
4. Không clone bí mật mù quáng: identity/credential có thể tách riêng theo runtime; chỉ yêu cầu parity chức năng và đúng scope.
5. Thiết lập cơ chế **đồng bộ dài hạn đơn giản**: một thay đổi được duyệt chỉ phải thực hiện tại **một nguồn chuẩn**, sau đó một thao tác sync/apply tất định cập nhật Mac + cloud; không sửa tay hai target.
6. Chứng minh bằng live acceptance: Mac ngủ thì GPT Chat + Claude Chat vẫn làm việc hội đồng trên cloud; Mac thức lại thì local vẫn hoạt động; một sync canary vô hại đi từ nguồn chuẩn → cả hai runtime rồi rollback qua cùng đường.
7. Mọi phần mới/sửa phải vào Điều 30/31 + Config/Protection Guard + rollback/receipt ngay trong N1.

**Không thuộc N1:** OpenAI Dots (N2) · Hermes-Mac courier/session control (N3) · Council Core/Level-State runtime (N4) · dual mode/multi-level (N5) · AUTO mới · UI/DB/workflow engine mới.

## 1. Luật khóa của RUN

- Đọc và tuân thủ: AGENTS A2/A5/A6/A9/A9-GLB → root DROOT22/30/31/32/34/37/38/40/41/42 → HJW §0.7/0.9/0.17 + P132 + P136/P137 → prompt này.
- **R1:** PASS N1 chỉ Owner được nới/bỏ. Host/Reviewer chỉ làm rõ/làm chặt.
- **R3:** code/config tạo trong N1 phải được bảo vệ ngay trong RUN này.
- **R4:** PRE + xếp loại nằm trong cùng RUN. Nếu có mutation thật, dừng đúng một checkpoint trước mutation; Host + Reviewer rà danh sách; đụng config server hoặc secret mới trên server ⇒ Owner gật một lần; sau đó cùng RUN tiếp tục.
- Không mở node/task/file tiến độ mới. Báo cáo/checkpoint/KQ ghi vào HJW COLLAB theo A6.
- Repo công khai: cấm ghi endpoint đầy đủ có secret path, token, secret value, chat id, IP riêng, username/path người dùng trên Mac hoặc nội dung file bí mật.
- Không dùng tool đang xuất hiện trong chat làm bằng chứng runtime ở đâu.
- Không force migration chỉ để đạt bảng. **Mac là runtime được giữ lại có chủ ý.**
- Không dựng service/gateway/daemon sync mới nếu existing source/apply/Guard có thể giải quyết.
- Không two-way filesystem sync mù. Đồng bộ phải theo **nguồn chuẩn + release/config template + secret injection riêng** để tránh conflict và lộ secret.

## 2. Read gate trước RUN / trước mỗi mutation

1. Xác minh Write_Path thật sự dùng được bằng **một read-gate**, không ghi thử.
2. Re-read COLLAB + PROMPT; READY phải trỏ đúng last-touch PROMPT; không HOLD/STOP.
3. Đọc fresh bảng đèn + registry. Không dùng số đèn cố định; mọi đèn phải xanh trước first mutation, trừ đỏ nằm chính trong scope N1 và có đường sửa/rollback.
4. Kiểm cờ bận / executor khác đang mutation shared VPS/Mac. Có conflict ⇒ chỉ đọc, chờ; không chen mutation.
5. Sau PRE dài, sau checkpoint R4 và trước first mutation: lặp DROOT30 freshness gate.
6. Không in secret/config raw ra terminal/log/repo; chỉ đọc tối thiểu để phân loại.

## 3. PHA A — PRE INVENTORY · READ-ONLY, 0 MUTATION

### 3.1 Hai định nghĩa

- **Cần cho hội đồng:** thiếu connector đó thì GPT Chat, Claude Chat hoặc Hermes-VPS không làm được ít nhất một việc: đọc repo · ghi repo bằng identity riêng · đọc bằng chứng server · hỏi JEV.
- **Cloudable:** chức năng connector không bắt buộc màn hình/phiên đăng nhập/file/hardware chỉ tồn tại trên Mac. Có thể cần credential riêng trên cloud nhưng không vì vậy mà gọi là Mac-only.

### 3.2 Bảng inventory duy nhất

Mỗi connector một dòng, đúng 9 ô:

1. **Tên** — chỉ tên route/app/profile, không URL đầy đủ.
2. **Ai dùng + cần cho hội đồng?** — surfaces + có/không.
3. **Runtime thật + chuỗi gọi** — `Mac cầu nối / Mac chạy thật / VPS / provider-cloud`; phía sau chỉ ghi tên route/service, không secret path.
4. **Identity + secret source** — identity/author; chỉ tên secret/profile/store, không value.
5. **Phụ thuộc Mac** — GUI/session/file/hardware/local binary nào, nếu có.
6. **Cloud twin hiện có** — đủ / thiếu tool nào / chưa có.
7. **Parity hiện tại** — tool/schema/chức năng chính: khớp / lệch gì.
8. **Xếp loại N1 + sync candidate** — `ALREADY_TWIN / SYNC_EXISTING / CREATE_CLOUD_TWIN / MAC_ONLY_EXCEPTION` + một câu lý do + nguồn chuẩn/sync path đề nghị.
9. **Protection** — Guard/đèn hiện có: có/chưa + tên, không secret.

### 3.3 Bắt buộc có trong bảng

- `agent-data` bản Mac.
- `directus` bản Mac.
- `lark-crud-gateway`.
- `Incomex_VPS` / route tên `claude-mcp`.
- `Incomex_KB` / `claude-kb`.
- `JEV` / `jev-mcp`.
- cổng GPT / `gpt-mcp`.
- cổng agent chung / `api/mcp-agent` — chỉ tên route.
- bản Lark trên server / `lark-mcp-remote`.
- `cowork-mcp` / `cowork-runner`.
- mọi custom MCP/plugin Incomex khác phía GPT/Claude.
- connector của Claude Code/Codex trên Mac: chỉ liệt kê tên + vai người thi hành; không khảo sát sâu nếu không liên quan cloud automation.

Không đưa connector hãng phổ thông như Drive/Gmail chỉ vì chúng tồn tại; N1 tập trung custom Incomex connector/runtime.

### 3.4 Bằng chứng được phép

File cấu hình đọc tối thiểu · tiến trình/service/container · file/runtime server · tool names/schema summary · author/identity commit · Guard/registry.

**CẤM trong Pha A:** tool ghi để thử · login lại · click reconnect · restart · cài tool · tạo token/profile/service · sửa config · sync · rebaseline.

### 3.5 Output checkpoint A

Ghi một mục P trong HJW COLLAB:
- bảng 9 ô;
- tổng số mỗi class;
- connector nào cần cho hội đồng;
- connector nào cloudable;
- connector nào thực sự `MAC_ONLY_EXCEPTION`;
- danh sách thiếu bằng chứng → `UNKNOWN`, không đoán.

Nếu còn UNKNOWN ảnh hưởng quyết định mutation ⇒ tiếp tục read-only trong cùng RUN cho tới khi đủ hoặc ghi BLOCKER; không mutation mù.

## 4. PHA B — THIẾT KẾ TWIN + SYNC PLAN TỪ BẰNG CHỨNG THẬT

Với từng connector không phải `MAC_ONLY_EXCEPTION`, lập plan ngắn:

1. **Mac giữ gì:** binary/config/profile/local workflow hiện hành nào phải giữ nguyên.
2. **Cloud twin ở đâu:** reuse server/container/profile/route hiện có; chỉ tạo mới phần thiếu.
3. **Functional parity:** tool/schema/capability nào phải khớp; cái nào được khác vì runtime.
4. **Identity:** Mac và cloud dùng identity/credential nào; cloud phải có scope hẹp, không tái dùng credential rộng chỉ để nhanh.
5. **Nguồn chuẩn cho thay đổi tương lai:** code/package/release/config template/schema lấy từ đâu. Không chọn hai nguồn cùng quyền sửa.
6. **Secret handling:** secret không đi qua repo/sync file; inject riêng từ secret store/profile hiện hữu.
7. **Sync path:** ưu tiên existing reviewed update/apply path. Một thay đổi được duyệt ⇒ **một action/command** cập nhật cả Mac + cloud hoặc khiến cả hai lấy cùng release. Không sửa tay target thứ hai.
8. **Drift proof:** version/hash/tool-schema marker nào Guard so được; lệch phải báo.
9. **Rollback:** quay cả hai runtime về bản trước bằng cùng cơ chế, không xóa bản Mac.

### R4 CHECKPOINT — chỉ một lần

Nếu có bất kỳ mutation:
- ghi **exact change list** theo connector;
- source → Mac target → cloud target;
- secret/profile mới — chỉ tên;
- service/config nào chạm;
- sync mechanism;
- rollback từng dòng;
- rủi ro shared runtime.

Sau đó **dừng trong cùng RUN**:
- Host + Claude Reviewer rà một lượt.
- Nếu chạm server config hoặc thêm secret/profile trên server ⇒ Owner gật **một lần cho toàn nhóm đã liệt kê**.
- Không được thêm mutation ngoài danh sách sau checkpoint; phát sinh mới ⇒ quay lại checkpoint cùng node/generation.

Không có mutation cần thiết ⇒ ghi `N1_R4_NO_MUTATION` và đi thẳng Pha D/E.

## 5. PHA C — TẠO / HOÀN THIỆN CLOUD TWIN, GIỮ MAC NGUYÊN TRẠNG

1. **Không uninstall/disable/repoint-away bản Mac.** Mac phải tiếp tục phục vụ Owner như trước.
2. `ALREADY_TWIN`: không rebuild; chỉ chuẩn hóa parity/sync evidence nếu thiếu.
3. `SYNC_EXISTING`: đưa Mac + cloud về cùng approved release/template/schema bằng path hiện hữu; không viết lại hệ.
4. `CREATE_CLOUD_TWIN`: tạo bản cloud tối thiểu bằng reuse container/profile/gateway pattern đang có; không dựng gateway/service mới nếu có chỗ cắm hiện hữu.
5. Cloud/web surfaces cần automation dùng cloud identity/profile; Mac local surfaces vẫn có thể dùng local identity/profile.
6. Secret/profile cloud tách riêng nếu an toàn hơn; không copy secret byte-for-byte chỉ vì gọi là copy nguyên trạng.
7. Mỗi nhóm mutation: D30 PRE → apply → health → functional smoke → POST; lỗi ⇒ rollback nhóm đó trước khi đi tiếp.
8. Không rebaseline Guard để che drift/lỗi.

## 6. PHA D — LIVE ACCEPTANCE: CLOUD ĐỘC LẬP + MAC VẪN NGUYÊN

### D1 · Parity

Lập bảng Mac↔cloud cho mọi connector cloudable: release/version · tool/schema/capability · identity · health · lệch có chủ ý.

Không bắt byte-equal config khi runtime khác nhau; bắt **functional parity + cùng approved release/template**.

### D2 · Mac-off proof — độc lập executor

1. executor ghi checkpoint `N1_MAC_OFF_READY`;
2. Owner chỉ làm **một thao tác**: cho Mac ngủ/gập theo hướng dẫn Host;
3. trong lúc Mac không phục vụ, **GPT Chat và Claude Chat tự thực hiện bằng cloud path**, mỗi bên: đọc một dòng repo · ghi một dòng/bằng chứng scoped bằng identity riêng · đọc một bằng chứng server cần cho hội đồng;
4. bằng chứng phải có timestamp/commit/identity; executor trên Mac **không tự chứng nhận** D2;
5. Owner bật Mac lại; cùng RUN tiếp tục từ repo evidence.

PASS D2 = cả GPT + Claude hoạt động hội đồng không phụ thuộc Mac.

### D3 · Mac-on regression

- local connector Owner/Claude Code/Codex cần vẫn khởi động/đọc được theo baseline;
- không mất local config/profile/tool;
- cloud twin vẫn healthy.

Mac có thêm cloud twin **không được đổi nghĩa thành Mac phải gọi cloud** cho công việc local.

## 7. PHA E — SYNC CANARY + DRIFT + PROTECTION

### E1 · Sync mechanism

- Với mỗi nhóm connector dùng cùng source, tạo/reuse một sync/apply action tất định.
- Ưu tiên **source-based release sync**, không rsync filesystem mù.
- Idempotent: chạy lại cùng version không tạo khác biệt mới.
- Mac offline: cloud tiếp tục chạy bản đã duyệt; khi Mac online lại, sync đưa Mac về approved version, không hạ cloud theo bản cũ trên Mac.
- Conflict rule: **approved source/version thắng**, không dùng newest-file-wins.

### E2 · Canary thật nhưng an toàn

Chọn **một connector đại diện** và một canary non-secret · không đổi business behavior · reversible.

1. thay canary **chỉ tại approved source**;
2. chạy đúng **một sync/apply action**;
3. chứng minh Mac + cloud cùng nhận canary **không sửa tay target thứ hai**;
4. ghi thời gian convergence; **target ≤10 phút / một chu kỳ apply+Guard bình thường**;
5. rollback canary tại source và chạy cùng action; cả hai quay lại;
6. nếu target >10 phút hoặc cần sửa tay target thứ hai ⇒ N1 chưa PASS; tối ưu trong N1, không đẩy node sau.

### E3 · Drift negative

Không phá live service. Dùng candidate/fixture/manifest an toàn để chứng minh:
- Mac/cloud version/schema drift ⇒ Guard đỏ/cảnh báo;
- missing/corrupt sync metadata ⇒ fail-closed;
- sync failure không làm mất bản đang chạy;
- không auto rebaseline.

### E4 · Protection

Mọi script/config/profile/manifest/sync target mới:
- vào Config/Protection Guard/INV tương ứng;
- D30/31 pre/post;
- mutant/negative proof;
- rollback một lệnh/đường rõ;
- receipt/registry;
- không nguồn alert ngoài sổ.

## 8. PASS N1 — KHÔNG ĐƯỢC NỚI

N1 chỉ `XONG` khi **đủ tất cả**:

1. Inventory bao phủ mọi custom Incomex connector trong scope, 0 UNKNOWN ảnh hưởng quyết định.
2. **Mac vẫn nguyên chức năng**; không connector local bị tháo chỉ vì có cloud.
3. Mọi connector cloudable có **cloud twin dùng được**; `MAC_ONLY_EXCEPTION` chỉ khi có bằng chứng kỹ thuật thật.
4. GPT Chat + Claude Chat PASS Mac-off proof bằng cloud path, identity riêng, ngoài scope bị chặn.
5. Mac-on regression PASS.
6. Functional parity/tool-schema cần thiết PASS.
7. Có **một nguồn approved** cho từng nhóm sync; không dual-edit.
8. Sync canary thật PASS: source → Mac+cloud → rollback, không sửa tay target thứ hai; convergence target ≤10 phút.
9. Drift negative/Guard PASS; sync failure không phá runtime.
10. Mọi mutation nằm trong D30/31 + protection; rollback/receipt sạch.
11. Không mở N2/N3/N4 trong N1; không code courier/Dot/Council Core.
12. Fresh lights/registry cuối: mọi đèn xanh, không nguồn ngoài sổ, AUTO_ALLOWLIST vẫn rỗng.

**Không được MOVE_TO node sau cho connector cloudable chưa có twin/sync.** Việc chưa xong của N1 ở lại N1. Chỉ `MAC_ONLY_EXCEPTION` kỹ thuật thật mới được disposition trong N1; nới dòng PASS cần Owner theo R1.

## 9. KQ / checkpoint canon

Trong HJW COLLAB, dùng các mốc:
- `BƯỚC N1-A INVENTORY PASS|BLOCKED`
- `BƯỚC N1-R4 WAITING_REVIEW|NO_MUTATION|APPROVED`
- `BƯỚC N1-C TWIN APPLY PASS|BLOCKED`
- `BƯỚC N1-D MAC_OFF PASS|BLOCKED`
- `BƯỚC N1-E SYNC+PROTECT PASS|BLOCKED`

KQ cuối PASS:
`KQ@HJW-N1-CLOUD-TWIN-SYNC-20261005-01 XONG · N1_PASS · MAC_PRESERVED · CLOUD_TWINS_READY · MAC_OFF_PASS · SYNC_CANARY_PASS · PROTECTION_CLEAN`

KQ chưa đạt:
`KQ@HJW-N1-CLOUD-TWIN-SYNC-20261005-01 DỪNG · <BLOCKER_CỤ_THỂ> · CONTINUE_SAME_NODE`

Không ghi KQ XONG nếu còn một điều PASS §8 chưa đạt.

## 10. Reviewer cần rà ở DRAFT này

Claude Chat chỉ rà một lượt:

1. Prompt đã phản ánh đúng Owner: **copy/sync, không move khỏi Mac** chưa?
2. R1/R3/R4 và S1–S3 P132 có đủ, có chỗ lộ secret/endpoint không?
3. N1 có đủ lớn kiểu G7 nhưng vẫn đúng boundary, không lấn N2–N4 không?
4. Sync source/canary/drift có quá phức tạp không; có thể bỏ thành phần nào mà vẫn chứng minh được thay đổi về sau đồng bộ nhanh không?
5. PASS §8 có điểm nào mơ hồ khiến phiên sau tự nới được không?

Nếu 0 blocker: Reviewer ghi ACCEPT + chỉnh chữ nhỏ nếu có. Host sau đó mới sửa prompt nếu cần, phát READY@full SHA và RUN.
