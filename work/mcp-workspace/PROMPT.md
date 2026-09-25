# PROMPT — MCPW-P02 · VPS last-good read cache + freshness debt + giảm xung đột giả

RUN_ID: MCPW-P02-20260925-01
Trạng thái: **DRAFT REV2 — K8 + PROTECTION GUARD — CHƯA READY / CHƯA RUN**
**READY@94de3978dcf648670a82a4290ae65b0dd4e6c608 và RUN@MCPW-P02-20260925-01 cũ HẾT HIỆU LỰC** vì execution pack đã thay đổi sau incident `MCPW-RECOVERY-20260925-01`. Phải review/READY mới trước mọi mutation P02.
Host: GPT Chat · Host_ID `GPT-MCPW-250925-A`
Owner đã duyệt kiến trúc P02 và freshness debt ngày 25/09/2026; MCPW-LOCK đã XONG, ruleset `gateway-only-writes` id `23976991` đang active.
Executor_Surface dự kiến: **Claude Code CLI trên Mac của Owner, chế độ hỏi quyền mặc định** (không auto-mode). Mỗi lệnh mutation hiện nút quyền để Owner bấm Yes.
Write_Path báo cáo repo: chỉ `fs_*` / `workspace_*`. GitHub native/App/API/CLI và `git push` trực tiếp vào incomex-workspace là READ-ONLY/bị ruleset chặn.

## 0. Mục tiêu
Xử lý dứt điểm rủi ro vận hành đã tái hiện: GitHub/SSH deploy-key có lúc chậm ~15 s làm read đồng thời BUSY dù VPS còn bản local tốt.

Đích:
1. Read/search/list/stat/log/diff phục vụ từ **snapshot last-good bất biến trên VPS**, không phụ thuộc network GitHub trong critical path.
2. GitHub vẫn là **durable SSOT + write authority**; write luôn revalidate GitHub trước mutation.
3. Nếu snapshot chưa được xác nhận mới nhất, AI/Agent biết rõ `fresh / refreshing / stale`, mang `recheck_required` và trả freshness debt trước kết luận cần HEAD hiện thời.
4. Hai gateway giữ cache riêng; không tạo SSOT thứ hai, không Forgejo/Gitea, không thêm deploy key.
5. Sửa luôn xung đột giả của `workspace_*`: commit ở file/task khác không được làm version của file đang sửa mất hiệu lực.
6. Sửa lỗi gốc đã gây `RECOVERY_REQUIRED`: push timeout không được tự biến thành khóa root chỉ vì local circuit chặn chính bước remote-proof.
7. Bảo vệ mọi capability/runtime đã PASS bằng một Protection Guard theo Điều 30 + Điều 31, dùng cùng contract ở PRE/POST và định kỳ.

## 1. Gate G0 — đọc và khớp
Trước mutation:
- đọc `AGENTS.md → root COLLAB.md → work/mcp-workspace/COLLAB.md → PROMPT.md`;
- xác nhận RUN_ID đúng và chỉ chạy khi COLLAB có `READY@<SHA>` khớp commit cuối chạm PROMPT.md;
- xác nhận GitHub ruleset `23976991` vẫn active, bypass chỉ DeployKey;
- xác nhận worktree/source của hai gateway sạch hoặc phân biệt rõ thay đổi ngoài scope; có mutation chen ngang thì DỪNG/hòa giải;
- đo baseline 12-way read + metrics BUSY/OVERLOADED + số GitHub refresh hiện tại.

Không đạt gate nào → KQ DỪNG, không deploy.

## 2. Phạm vi được phép
**K1–K8 chỉ áp cho hai root Git đẩy GitHub:** `gh` của `fs_*` và `workspace` của `workspace_*`. Không đổi hành vi, khoá, version hay snapshot của root `ui`; không đổi `docs`/`code` read-only.

Được:
- sửa **mã/runtime hiện hữu** của hai gateway `workspace_*` và `fs_*`;
- sửa test hiện hữu, config/compose/systemd hiện hữu khi thật sự cần;
- tạo **derived runtime cache/state directories trên VPS** dưới vùng state hiện hữu; đây là cache dẫn xuất, không phải SSOT;
- build image/deploy/restart hai gateway **từng cổng một**, có rollback và health gate.

Không được:
- tạo task/project/file nghiệp vụ mới trong incomex-workspace;
- đổi tool name/count/input schema/auth/hash contract;
- thêm deploy key/token/PAT hoặc đổi ruleset;
- sửa receiver HVU nếu chỉ cần đọc trạng thái hiện hữu;
- làm GitHub thành cache phụ khác hoặc dựng Forgejo/Gitea;
- force-push/reset/xóa dữ liệu;
- tăng timeout để che lỗi.

## 3. K1 — Snapshot read-serving tách khỏi worktree ghi
Mỗi gateway giữ **cache riêng**:
- snapshot bất biến theo commit SHA, dựng từ Git object đã fetch;
- con trỏ `current` đổi nguyên tử;
- request đang đọc snapshot cũ không bị phá khi snapshot mới được advance;
- read/search/list/stat đọc snapshot;
- log/diff/ref đọc object DB tại snapshot/ref;
- không read nào lấy root/write lock hoặc đọc worktree writer;
- snapshot phải nằm trong **vùng đã mount/nhìn thấy sẵn của đúng gateway**. Với `fs_*`, snapshot phục vụ container là file/thư mục thường, không dựa vào `.git`/worktree path chỉ có trên host; nếu buộc đổi compose/bind-mount thì phải khai trước + rollback riêng.

GC chỉ dọn **derived snapshot do chính P02 tạo** khi không còn request dùng, có audit theo tiền lệ revision-gc; không đụng Git history/business data/audit.

## 4. K2 — Trạng thái freshness máy đọc được
Mỗi gateway có trạng thái nhỏ, ghi nguyên tử:
- `snapshot_sha`
- `confirmed_at`
- `last_attempt`
- `last_error`

Mỗi phản hồi HEAD-dependent phải biểu đạt:
- `freshness = fresh | refreshing | stale`
- `recheck_required = true|false`
- `source_head`
- `refreshed_at`
- `remote_head` khi biết.

`workspace_*`: response-only metadata, không đổi input schema/tools/list/hash.
`fs_*`: đưa cùng thông tin máy đọc vào format phản hồi hiện hữu, không đổi surface tool.

Quy tắc:
- `fresh` → `recheck_required=false`;
- `refreshing|stale` → `recheck_required=true`;
- `ref=<sha>` đã có local là bất biến → không freshness debt cho chính nội dung commit đó.

Sau reboot/start, có snapshot thì phục vụ ngay nhưng **không được fresh** trước lần xác nhận remote thành công đầu tiên.

## 5. K3 — Freshness debt / nợ kiểm lại
AI không phải dừng công việc khi nhận non-fresh:
- được phân tích/draft trên last-good;
- kết luận hiện trạng là provisional.

Trước READY/SHA, “đã có/chưa có”, nghiệm thu HEAD hiện tại hoặc kết luận cuối phụ thuộc current state:
1. recheck bằng safety read đúng root/path;
2. nếu `fresh` và `source_head` không đổi → clear debt;
3. nếu `fresh` nhưng head đổi → diff head cũ→mới trên phần liên quan, cập nhật kết luận rồi mới clear;
4. nếu vẫn non-fresh → không loop vô hạn; hoàn tất với câu rõ `chưa xác nhận bản mới nhất` + source_head/refreshed_at, không gọi đó là evidence fresh.

Gateway tự kích/join refresh nền; request có thể trả trước khi refresh nền xong.

## 6. K4 — Refresher single-flight, bounded, không làm read BUSY
- refresh/fetch chạy **ngoài root lock của writer**;
- một refresh active mỗi gateway xuyên process/worker;
- read quá cửa sổ freshness kích/join refresh, chỉ chờ bounded:
  - khởi điểm `W=60s`
  - `D_plain≈3s`
  - `D_safe≈5s`
  - stale threshold≈5 phút
- hết D → trả last-good + freshness; **không WORKSPACE_BUSY/OVERLOADED chỉ vì GitHub refresh chậm**.
- SHA mới chỉ advance nếu là hậu duệ snapshot hiện hành; không lùi.
- fetch/fsck lỗi → giữ last-good, stale + last_error;
- **B1:** nếu hint HVU đã biết `publishedRevision` mới hơn snapshot (khác và không phải tổ tiên của snapshot) thì snapshot hiện tại **mất fresh ngay**, `recheck_required=true`, kích refresh ngay không chờ hết W. Nếu hint `publishedRevision == snapshot_sha` và `status=fresh` thì được tính là một lần remote confirmation tại `lastCheckedAt`.

Các số W/D phải benchmark rồi chốt; không tăng mù.

## 7. K5 — Gợi ý từ HVU: dùng bảng tin hiện hữu, correctness không phụ thuộc nó
- Owner View đã có `sync-status.json` với `publishedRevision / lastCheckedAt / status`.
- Hai gateway chỉ **đọc** nó như hint nếu ghép mỏng được; không sửa receiver, không tạo daemon/pipeline mới.
- file thiếu/hỏng/quyền không cho đọc → bỏ hint, lazy refresh theo W vẫn đúng.
- `fs_*` có thể đọc host file hiện hữu.
- `workspace_*`: dùng cách mỏng sẵn có (HTTP nội bộ hoặc bind-mount read-only) chỉ khi chứng minh được; nếu không, lazy-only.

Hint không bao giờ là write authority.

## 8. K6 — Kênh read GitHub: benchmark HTTPS public vs SSH deploy key
Repo hiện PUBLIC.
Đo cùng điều kiện:
- read fetch/ls-remote qua HTTPS anonymous;
- read fetch/ls-remote qua SSH deploy key.

Nếu HTTPS có p95 ổn định hơn và không cần auth, **read refresher được phép dùng HTTPS anonymous** để tránh bước deploy-key lookup đã từng treo ~15s.
Write vẫn dùng SSH deploy key gateway.
Nếu repo trở lại private → fallback SSH read mà không đổi kiến trúc.

Không dùng PAT/token cho read. Nếu HTTPS anonymous lỗi/bị giới hạn/không dùng được thì **tự fallback sang SSH read cho đúng lượt đó**; kênh lỗi không được làm response mang `fresh`. Đo cả tần suất/ảnh hưởng vì HVU cũng dùng HTTPS anonymous từ cùng VPS/IP.

## 9. K7 — Version theo nội dung, loại xung đột giả ở workspace_*
Hiện file version của `workspace_*` gắn `HEAD:hash`, làm commit ở task/file khác gây VERSION_CONFLICT giả.

Chuyển về đúng technical contract:
- file `expected_version` dựa trên **nội dung file** (content hash/stable content token), không phụ thuộc repo HEAD;
- directory/tree version dựa trên nội dung/cấu trúc tree, không phụ thuộc commit ngoài tree;
- `expected_head` / `expected_HEAD` vẫn là guard riêng khi caller muốn pin cả repo;
- target file/tree thật sự đổi → vẫn VERSION_CONFLICT;
- commit ở file khác → version file không mất hiệu lực;
- tương thích caller đang giữ legacy `HEAD:hash`: parser nhận và kiểm phần content hash khi có thể; nếu không thể thì trả lỗi chuyển tiếp rõ ràng, không hiểu sai token;
- không đổi tool count/input schema/hash.

## 9B. K8 — Push timeout, remote-proof và tự hòa giải fail-closed
Incident recovery đã chứng minh chuỗi lỗi: push timeout → local git circuit mở → `ls-remote` kiểm ngay sau bị chính circuit chặn → `push_unknown` → khóa root.

K8 bắt buộc:
1. Sau push timeout/mất phản hồi, remote-proof không được thất bại chỉ vì local circuit vừa mở: chờ circuit hết hạn hoặc dùng đường proof hẹp không chịu circuit local, nhưng luôn bounded timeout; **không push lại mù**.
2. Proof phải kiểm commit transaction có nằm trong **remote history** hay chưa, không chỉ so với remote HEAD:
   - remote chứa commit → chốt `committed`, không duplicate push;
   - remote chắc chắn không chứa commit → chỉ rollback khi local state đủ điều kiện an toàn;
   - chưa chứng minh được → giữ `push_unknown`, chặn ghi, không đoán.
3. `push_unknown` chỉ được chặn write/current-HEAD mutation; last-good read vẫn phục vụ với `stale` + `recheck_required=true`.
4. Tự hòa giải khi network trở lại chỉ khi máy chứng minh đủ điều kiện như recovery hôm nay: cùng root lock + đúng uid gateway; pending record xác định; worktree sạch; không git process; không later local commit/unrelated delta; base/parent quan hệ với remote rõ; orphan được giữ bằng `refs/recovery/*` + bundle verify trước mutation. Sau đó mới được `reset --keep` về exact remote SHA + record `rolled_back/reconciled` nếu commit thật sự không ở remote. Bất kỳ ambiguity/multi-pending/dirty/proof unavailable → **không tự reset**, giữ chặn ghi + read last-good + alert.
5. Fault injection bắt buộc: timeout nhưng commit không tới remote; timeout nhưng commit đã tới remote; mất mạng hẳn rồi mạng về; mutant remote-proof bị circuit local chặn. Mỗi ca phải chứng minh không duplicate và không khóa đọc.

## 10. Write path — giữ strict GitHub
Không nới write:
1. chuẩn bị từ snapshot local;
2. writer lock;
3. fetch/revalidate GitHub HEAD thật;
4. kiểm expected_version/content + expected_head nếu có;
5. commit đúng scope;
6. push fast-forward qua deploy key;
7. push OK → dựng/advance snapshot gateway đó lên SHA vừa push **trước khi trả success**;
8. push rejected → phục hồi scope hiện hành;
9. outcome unknown → journal/recovery hiện hành; không advance mù.

Hai gateway cùng ghi vẫn do GitHub fast-forward phân xử.
P02 không thêm deploy key.

## 10B. MCPW PROTECTION GUARD — Điều 30 + Điều 31
Một bộ kiểm **read-only**, tái dùng checker hiện hữu; không dựng framework/service/DB/port mới.

### Ba chế độ cùng một contract
- **PRE:** trước mutation/restart từng gateway. PRE fail → không mutation.
- **POST:** sau mutation/restart từng gateway. POST fail → DỪNG và rollback đúng delta vừa đổi; không tự chữa service ngoài scope.
- **PERIODIC:** chỉ đọc, mục tiêu phát hiện ≤10 phút. Reuse timer/monitoring/Kuma + Telegram hiện hữu; không tạo service mới. Periodic phải chạy từ lớp không phụ thuộc hoàn toàn vào chính root `workspace` để khi root bị khóa vẫn báo được. Watchdog theo tinh thần Điều 31 phải chứng minh checker còn sống, không coi im lặng là PASS.

### Reuse bắt buộc — B5
Ngoài `run_acceptance.py`, config-guard và health/smoke hiện hữu, tái dùng bộ snapshot PRE/POST của `MCPW-RECOVERY-20260925-01`: 12 container/image/StartedAt/health, service, timer, crontab, source/config hash, HTTP routes, listening ports, disk và git dirty/head. Không viết lại một bộ đo song song nếu dữ liệu đã có.

### Invariants tối thiểu
1. ruleset `gateway-only-writes` id `23976991` active; bypass chỉ DeployKey; không thêm key;
2. GPT Full All 2 giữ 37 tools + input schema/fingerprint/auth/operation_id/transaction/restore, trừ đúng semantics K1–K8 đã duyệt;
3. Claude gateway/surface inventory + fingerprint/auth hiện hành không giảm;
4. `workspace_*` + `fs_*`: read/search/list/stat/log/diff + write/version/idempotency/recovery cũ còn PASS;
5. Agent Data healthy; config-guard CLEAN;
6. Owner View/Nuxt/Directus/public MCP routes hiện hành còn PASS;
7. Hermes không hồi quy do Agent Data: đúng 7 tool, trusted scope/attribution giữ nguyên, `AGENT_DATA_*` không quay lại env Hermes, health PASS;
8. service ngoài scope không recreate/restart; image/StartedAt/config/hash ngoài scope giữ nguyên;
9. nginx/HJW webhook không đổi trong P02;
10. không có pending recovery record chặn root quá ngưỡng; clone/head/remote không drift im lặng.

### B2 — kiểm như client thật
Không chỉ gọi hàm nội bộ. Guard/acceptance phải gọi MCP thật qua đúng public path hiện hành mà GPT, Claude và Hermes dùng; nội bộ chỉ là bằng chứng phụ. HTTP 200 một mình không đủ: phải assert tool inventory/fingerprint/auth/capability cụ thể.

### B3 — negative control không phá production
Dùng fixture/input giả cho checker: tool count sai, fingerprint lệch, pending-record giả trong state temp, HEAD lệch, watchdog stale… mỗi mutant phải FAIL. Không tamper production chỉ để chứng minh guard biết fail.

## 11. Triển khai / quyền
**Chạy Claude Code ở chế độ hỏi quyền mặc định, KHÔNG auto-mode.**
Owner/RUN mới sau READY mới ủy quyền toàn bộ đúng scope P02; **không bắt Owner gõ lại câu xác nhận tự do cho từng bước**. Nếu nền tảng yêu cầu confirmation thì chỉ dùng nút permission/Yes bình thường. Trước mutation, Agent liệt kê ngắn các nhóm lệnh có thể hiện nút Yes:
- sửa source/test/config hai gateway;
- build image/package;
- restart/deploy từng gateway;
- tạo derived cache/state directories nếu cần;
- smoke/acceptance write qua hai gateway.

Không yêu cầu Owner tự chạy shell command thay Agent nếu chế độ hỏi quyền có thể cấp quyền bình thường.

Deploy từng gateway:
- test/build trước;
- rollback riêng từng cổng;
- deploy cổng 1 → theo DROOT10 cho trạng thái STARTING tối đa 5 phút; **không smoke, không rollback chỉ vì chưa ready trong cửa sổ STARTING**; sau khi healthy mới acceptance cơ bản → cổng 2;
- áp cùng STARTING gate cho cổng 2;
- không restart đồng thời;
- nếu cổng 1 fail thật sau STARTING/health gate thì rollback trước khi đụng cổng 2.

## 12. Acceptance bắt buộc — 17 mục
1. **GitHub giả chậm 20–30s** trong test environment: 12 read song song mỗi gateway = 0 BUSY/OVERLOADED do refresh, response ≤ D+1s; mutant bỏ bounded wait phải FAIL.
2. Mọi `refreshing|stale` có `recheck_required=true`; `fresh` và local `ref=<sha>` có false. **Hint HVU báo revision mới hơn snapshot phải lập tức làm non-fresh + `recheck_required=true`, không được giữ fresh tới hết W.**
3. Bỏ độ chậm → safety recheck thành fresh; nếu HEAD đổi phải cung cấp đủ old/new để diff trước khi clear debt.
4. Restart gateway khi GitHub bị chặn: last-good vẫn đọc được nhưng không response nào fresh trước remote confirmation. **Ở mục này, `remote confirmation` gồm cả hint HVU hợp lệ còn trong W; vì vậy bài thử phải chặn GitHub và đồng thời làm hint cũ hơn W hoặc vắng để chứng minh không tự gắn `fresh`.**
5. Push thành công rồi read ngay cùng gateway phải thấy commit mới, kể cả GitHub chậm sau push.
6. **Concurrency/version:** (a) gateway Y sửa file F → gateway X dùng version cũ F phải conflict; (b) commit ở file/task khác không đổi F → version F cũ vẫn hợp lệ; (c) expected_head cũ nếu được truyền vẫn conflict; (d) legacy HEAD:hash được xử lý đúng/chuyển tiếp rõ.
7. Hint HVU cũ/out-of-order không được làm snapshot lùi.
8. Hint HVU thiếu/hỏng/không mount được → 1–7 vẫn PASS bằng lazy refresh.
9. Write + refresh đồng thời không deadlock, không rò ref-lock/BUSY ra read caller.
10. Không hồi quy: GPT 37 tools + input schema/hash `dbbfc590a969` + auth 401 + operation_id replay + transaction/restore; Claude surface/tool fingerprint hiện hành không giảm; ruleset vẫn active, không thêm deploy key. Root `ui` giữ nguyên cơ chế/lock/version cũ và phải có một lượt read-write smoke qua cả hai cổng như baseline.
11. Repo đã khóa: write thật qua `fs_*` và `workspace_*` PASS; GitHub native human write vẫn bị ruleset chặn (dùng bằng chứng T1 hiện có nếu không cần tạo probe mới).
12. Đo before→after: p50/p95 read thường/safety, 12-way, số GitHub refresh/hour, HTTPS-vs-SSH read latency, BUSY/OVERLOADED delta, RAM/load/disk của cache.
13. **K8/no-remote:** push timeout, commit không tới remote → xác nhận từ remote rồi rollback sạch; không để RECOVERY_REQUIRED kéo dài.
14. **K8/already-remote:** push đã tới remote nhưng response timeout → nhận ra commit trong remote history, mark committed, không commit/push lần hai.
15. **K8/outage + self-heal:** remote-proof unavailable → write block + last-good read; mạng về và chỉ khi toàn bộ precondition xác định mới tự hòa giải; orphan/bundle còn nguyên. Mutant circuit chặn remote-proof phải FAIL.
16. **Protection PRE/POST + periodic:** cùng một invariant contract; PRE=PASS và POST=PASS, diff ngoài scope=0; periodic phát hiện pending/drift/liveness trong ≤10 phút và gửi qua monitoring/Telegram hiện hữu.
17. **Protection negative control + client E2E:** mutant fixture phải FAIL; gọi MCP thật qua các public path GPT/Claude/Hermes và assert capability cụ thể, không thay bằng HTTP 200.

## 13. Rollback
Trước deploy phải có rollback riêng từng gateway về image/source/config trước P02.
Rollback một cổng không kéo cổng kia.
Derived cache có thể bỏ và quay về behavior cũ; không xóa Git history/audit/business data.
Rollback không được disable ruleset `gateway-only-writes`.

## 14. Cấm
- không tạo SSOT thứ hai;
- không tạo app/plugin/MCP route/tool mới;
- không thêm deploy key/PAT/token;
- không đổi GitHub ruleset;
- không force/reset/delete business/Git/audit data; **ngoại lệ duy nhất:** được GC/xoá các thư mục snapshot dẫn xuất do chính P02 tạo trong vùng cache P02, có audit và không còn request sử dụng;
- không tạo file/task/project mới trong incomex-workspace;
- không sửa Owner View receiver nếu chỉ cần đọc status;
- không coi stale là fresh;
- không retry write mù;
- không đổi behavior khác ngoài K1–K8 và Protection Guard read-only đã nêu.

## 15. Báo cáo KQ
Ghi vào **chính** `work/mcp-workspace/COLLAB.md`, không tạo report/file mới trong repo. Hồ sơ runtime/bench/rollback trên VPS đặt tại `/opt/incomex/work/mcp-workspace/MCPW-P02-20260925/` theo DROOT12/mẫu MCPW-STAB.
- implementation K1–K8 + Protection Guard;
- exact runtime commits/images/config;
- 17 acceptance PASS/FAIL;
- before→after metrics;
- rollback;
- điểm còn lại.

Dòng cuối:
`KQ@MCPW-P02-20260925-01 XONG`
hoặc
`KQ@MCPW-P02-20260925-01 DỪNG · <lý do>`.

Sau P02 XONG **không đóng mcp-workspace**: Host/Founders cập nhật README Technical Contract bằng luật freshness debt K2–K3; sau đó tiếp tục vòng §0.2(3)–(4) về vai trò + tín hiệu giao/đẩy việc + **scoped lease cưỡng chế xung đột đa-Agent**. Presence chỉ là quan sát, không được dùng thay lease.
