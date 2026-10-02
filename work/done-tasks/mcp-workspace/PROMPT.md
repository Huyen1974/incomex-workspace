# PROMPT — MCPW R6 · PROTECT THÀNH QUẢ + N9 FINAL + READY TO CLOSE

RUN_ID: MCPW-R6-PROTECT-CLOSE-20261002-01
Host: GPT Chat · GPT-MCPW-250925-A
Executor_Surface: Claude Code CLI trên Mac Owner
Report_Write_Path: `work/mcp-workspace/COLLAB.md` qua `workspace_*` profile `claude-code`
Runtime: VPS1 production + repo/source hiện hành
STATUS: CHƯA RUN. Reviewer đã rà (P86 · ACCEPT-with-delta) — chờ Host READY đúng commit cuối chạm file này.

## 0. Mục tiêu duy nhất

KHÔNG thêm capability mới.

**Ngân sách cứng:** 0 restart/recreate dịch vụ (agent-data · claude-mcp · nginx · Directus · Hermes gateway/serve) · không build/đổi image · không sửa `lifecycle.py` / `server.py` / `app.vue` / `view.html` · không service/timer/cron/DB/monitor Kuma mới · tối đa 4 invariant mới · Owner thao tác dự kiến = 0. Buộc vượt bất kỳ mục nào ⇒ DỪNG trước khi làm, báo Host.

Lấy toàn bộ thành quả MCPW đã đạt làm **baseline được bảo vệ**, áp ngay:
- **Điều 30 v1.2 — Luật Bảo vệ Hồi quy:** thay đổi sau này chạm chức năng/UI phải có test chứng minh cái cũ không hỏng; UI phải có browser evidence thật.
- **Điều 31 v1.2 — Luật Toàn Vẹn Hệ Thống:** hệ thống tự kiểm liên tục, tự phơi bày drift/lỗi; guard/watchdog cũng phải được kiểm.

Sau đó chuẩn bị bằng chứng theo khung E1–E6 để Host + Reviewer nghiệm thu N9 (executor không tự nghiệm thu). Đủ bằng chứng ⇒
`KQ@MCPW-R6-PROTECT-CLOSE-20261002-01 XONG · PROTECTED_READY_FOR_OWNER_CLOSE`.

Owner là người gật đóng MCPW. Executor không tự mở roadmap tiếp theo.

## 1. Baseline phải bảo vệ — cấm làm lại

Đọc:
1. `AGENTS.md` (DROOT29–33, đặc biệt DROOT30/31);
2. `work/mcp-workspace/COLLAB.md` §0.1–§0.3 + P80–P85 + KQ R2;
3. PROMPT này;
4. KB luật sống:
   - `knowledge/dev/laws/dieu30-regression-protection-law.md`
   - `knowledge/dev/laws/dieu31-system-integrity-law.md`

Baseline hiện hành:
- gateway-only-writes;
- P02/read-serving;
- contract GPT 37 / claude-mcp 23;
- B1 server-side identity;
- B2A legacy shared key WRITE deny trên MCP;
- lifecycle ledger `queue.sqlite`, mode=audit, 0 DENY;
- Claude Code hook/lifecycle;
- Codex Desktop hook/lifecycle trên bề mặt Owner dùng thật — PASS `9fe894c`;
- SSH correlation + SSH_UNKNOWN/NGOÀI VIỆC;
- Owner View “Sổ phiên” + “Ngoài việc” + đỏ/vàng;
- Hermes manual Telegram gate + task/chat vào sổ + ghi đúng task + config Guard;
- R2 source/image/config hiện hành;
- test R2 23/23 PASS + negative/mutant hiện hữu.

**Không được redesign hay thay cơ chế nếu test/guard hiện có đã đủ.**

## 2. Ngoài scope cứng

Không làm:
- Bảng giao việc/NEXT;
- scoped lease/fencing;
- REST legacy enforcement;
- Directus/private writer;
- VPSUP/DNS;
- Hermes AUTO;
- sửa `sync.py` của MMIM; rebaseline `hvu-sync-py` **trừ đúng ngoại lệ §6.3** (chỉ khi Owner đã ĐỒNG Ý `O-HVU-SYNC`);
- cleanup lịch sử/test sessions ngoài cái cần cho verification;
- framework/monitor/service mới nếu guard/test hiện hữu ghép được.

`Disk Usage/Cron Heartbeat` thuộc VPSUP/hạ tầng, không xử lý trong RUN này.

## 3. START gate — không chờ theo giờ

PASS khi:
1. R2 đã KQ XONG; Codex Desktop hậu kiểm PASS;
2. PROMPT last-touch = READY Host;
3. không có RUN khác đang mutation cùng file/service cần chạm trong RUN này;
4. agent-data/claude-mcp/nginx healthy; workspace fresh;
5. rollback exact cho mọi file/config sẽ sửa.

Repo HEAD đổi do task độc lập ⇒ re-read/diff; chỉ collision thật mới dừng.

Sau PASS ghi:
`STARTED@MCPW-R6-PROTECT-CLOSE-20261002-01 <UTC> · executor=Claude Code CLI`.

DROOT30 ngay trước mutation đầu và sau mọi checkpoint chờ Owner.

## 4. Điều 30 — Regression Protection Pack

### 4.1 Backend/lifecycle contract

Tái dùng test R2 hiện có. Chứng minh chúng **thực sự nằm trong đường test tự động hiện hành** của repo agent-data.

Bắt buộc bảo vệ tối thiểu:
- actor lấy từ credential, payload spoof không đổi actor;
- event idempotent, retry không double-count;
- bad event reject;
- ACTIVE / waiting / LOST / AWAITING_REPORT / REPORTED;
- “chờ người” không LOST;
- nhắc KQ đúng 1 lần;
- KQ khác actor không report;
- HOOK_MISSING;
- SSH causal match; ambiguous ⇒ SSH_UNKNOWN;
- NGOÀI VIỆC;
- 2 executor cùng work/RUN ⇒ đỏ; reviewer song song không đỏ;
- mode=audit ⇒ không DENY;
- Hermes task/chat import;
- contract 37/23 không đổi.

Nếu CI/test command hiện tại đã tự chạy `tests/continuation/test_r2_*.py` ⇒ chỉ ghi bằng chứng, **không thêm pipeline**.
Nếu chưa chạy ⇒ thêm tối thiểu vào test workflow hiện hữu; không tạo hệ CI thứ hai.
“Đường test tự động hiện hành” = bộ acceptance/release gate đang dùng trước khi đổi image agent-data (vd `run_acceptance.py` + `tests/continuation`), không phải GitHub Actions mới.

**Biển báo tại chỗ (2–4 dòng):** ghi lệnh test phải chạy trước khi sửa/deploy vào README/biển thư mục **hiện hữu** của `tests/continuation` và của `scripts/hvu-b2` (`README.md` / `00-NHAN-THU-MUC.md`). Không tạo file mới nếu đã có chỗ ghi.

### 4.2 Owner View — browser regression theo Điều 30

Owner View là bề mặt người dùng đã thay đổi ⇒ phải có browser evidence thật.

Reuse Playwright/browser harness hiện hữu trong nuxt/UI repo; không dựng framework mới nếu đã có.

Contract tối thiểu cho task có fixture/snapshot kiểm soát:
- có khu vực/nhãn “Sổ phiên”;
- có “Ngoài việc” khi có outside session;
- hiển thị actor/surface + thời điểm + trạng thái;
- warning HOOK_MISSING/SSH_UNKNOWN/NGOÀI VIỆC hiển thị khi fixture có;
- AWAITING_REPORT/LOST hiển thị rõ;
- 2 executor cùng work/RUN ⇒ cảnh báo đỏ;
- reviewer/chat song song không tạo đỏ;
- route/page không 404, không chỉ chấm HTTP 200.

**Điều 30: browser content assertions là bằng chứng; API/SSR 200 không đủ.**

Nếu có harness Playwright hiện hữu ⇒ thêm test vào harness đó.
Nếu không có harness nào phù hợp ⇒ dùng công cụ browser hiện hữu để tạo test nhỏ nhất có thể tái chạy và ghi rõ residual; không kéo npm/framework lớn chỉ để đẹp hồ sơ.

Giới hạn: test chạy trên **fixture**, assert theo **chữ hiển thị** — không sửa `app.vue`/build lại `view.html` chỉ để thêm `data-testid`. Thư mục `scripts/hvu-b2` dùng chung với lane MMIM: chỉ thêm file test/fixture + dòng biển báo; không sửa `sync.py`.

### 4.3 Post-change smoke

Sau mọi mutation của RUN này:
- chạy backend regression;
- browser smoke Owner View;
- contract 37/23;
- gateway/P02/B1/B2A/Hermes manual gate smoke.

Không có artifact/bằng chứng ⇒ không PASS.

## 5. Điều 31 — Integrity + self-detection

### 5.1 Config Guard — bảo vệ byte/config đã sinh

Đối chiếu registry live.

MCPW-owned targets tối thiểu phải được bảo vệ:
- `agent_data/lifecycle.py`;
- lifecycle receiver/server delta liên quan;
- `scripts/presence-import.py`;
- importer service/timer;
- `presence.py` / Owner View adapter đã đổi;
- Hermes config hash target;
- workspace-tools lifecycle config;
- `hjw_gate.py` (R2 đã đổi `8ced89b40382` → `6993c82a4755`).

`app.vue`/`view.html` dùng chung với lane MMIM và được build lại hợp lệ ⇒ **không** đăng ký hash (sẽ đỏ mỗi lần MMIM build); bảo vệ bằng test trình duyệt §4.2 + cảm biến nhãn §5.2.

Nếu đã có trong 61 targets và hash đúng ⇒ KEEP.
Thiếu target của chính R2 ⇒ đăng ký qua apply path hiện hữu trong cùng RUN.
Không rebaseline target của task khác.

Drift `hvu-sync-py` (MMIM A09R1): xử lý theo §6.3.

### 5.2 Protection Guard — thêm/kiểm invariant R2 bằng cơ chế hiện hữu

Reuse Protection Guard/periodic/watchdog hiện hữu; không service mới.

MCPW R2 phải tự phát hiện tối thiểu (cái nào guard hiện hữu đã canh ⇒ KEEP + ghi evidence, không thêm bản thứ hai):
1. lifecycle mode không còn `audit`;
2. importer chết / snapshot lifecycle quá cũ (`presence.json` khối `lifecycle.generatedAt` > 10 phút) hoặc parse lỗi/thiếu field cốt lõi;
3. Owner View đang phục vụ mất nhãn cốt lõi (“Sổ phiên”, “Ngoài việc”) hoặc mất khối `lifecycle` — kiểm bằng đọc file/HTTP + tìm chuỗi, **không chạy trình duyệt trong guard định kỳ**;
4. contract 37/23 hoặc legacy B2A regression (INV hiện có đã phủ ⇒ KEEP).
Lệch byte của file/config R2 (lifecycle, importer, presence, gate, Hermes config) đã do Config Guard báo qua INV5_6 ⇒ không thêm invariant trùng.

**Luật cho invariant mới:** chạy tại chỗ (không gọi GitHub — ngân sách `rest_anon` 2/h; không LLM); **2-pass** — 2 lượt liên tiếp fail mới đỏ (Điều 31 §4.4); gộp vào monitor Kuma hiện có. `INV5_6.health_routes http /=HTTPError` đã chớp DOWN→UP 3 lần/3 ngày ⇒ áp cùng luật 2-pass nếu sửa gọn trong cùng file; không điều tra lịch sử.

**Mac hooks không cần monitor mới:** khi Claude Code/Codex hoạt động qua gateway/SSH mà hook không có, `HOOK_MISSING` chính là sensor Điều 31. Giữ cơ chế này.

Không dựng cơ chế “ngoại lệ drift đã biết” trong guard; drift ngoài MCPW xử lý tại nguồn theo §6.3.

Không sửa lịch sử DOWN→UP cũ. Chỉ sửa lỗi live còn tồn tại hoặc invariant mới chưa được canh.

### 5.3 Watchdog/self-protection

Kiểm guard/watchdog hiện hữu còn tự canh:
- Protection Guard bị chết/im lặng ⇒ có dead-man/alert;
- Config Guard bị lỗi ⇒ không giả PASS;
- receiver/importer test failure ⇒ không bị nuốt.

Nếu đã có coverage tương đương ⇒ KEEP, ghi evidence.
Chỉ vá lỗ thực tế chứng minh được.

## 6. Cảnh báo Telegram hiện hành — chỉ xử lý owner MCPW

Trong cùng RUN, trước KQ. Live PASS ⇒ không đào alert lịch sử.

**6.1 Hermes gateway `drift=GATE` — MCPW-owned, do R2 gây ra:** R2 đổi `hjw_gate.py` (`8ced89b40382` → `6993c82a4755`) và đã đăng ký Config Guard, nhưng baseline riêng của `hjw-control-root.py tick` chưa cập nhật ⇒ `kuma-push.sh hermes` đẩy DOWN. Hash live = `6993c82a4755` ⇒ cập nhật baseline bằng đường chính thức của HJW control (không sửa tay nếu có lệnh), ghi old/new; đạt khi `tick` trả `drift=none` và monitor “Hermes gateway” UP. Hash live khác ⇒ DỪNG, báo Host (gate bị đổi ngoài R2). Công tắc Owner (`stop`, AUTO rỗng) giữ nguyên.

**6.2 MCPW Protection Guard:** còn đỏ do nguyên nhân MCPW ⇒ sửa đúng gốc + regression.

**6.3 `hvu-sync-py` — drift của MMIM A09R1, đang giữ INV5_6 đỏ liên tục (Kuma chỉ báo khi đổi trạng thái ⇒ lỗi mới của MCPW không còn báo được):**
- Mặc định: không đụng; KQ ghi “Protection Guard còn đỏ do drift MMIM” (không chặn KQ).
- **Chỉ khi `## Quyết định Owner` của COLLAB có `O-HVU-SYNC · ĐỒNG Ý`:** sha256 live của `scripts/hvu-b2/sync.py` = `a64a59eb0468890f7463fa2699eee55bd5f84f6875b45f545a50ab12dfe46722` (bản A09R1, Host MMIM nghiệm thu D102) ⇒ rebaseline **đúng một mục** `hvu-sync-py` qua apply path, ghi old/new + lý do (DROOT29); sau đó Config Guard 61/61 và Protection Guard UP. Hash khác ⇒ không rebaseline, ghi hash thật, báo Host MMIM.

`Disk Usage No heartbeat` không thuộc MCPW (Config Guard cho thấy `kuma-push-sh`/`cron-kuma-push` không đổi); không chạm.

## 7. Bằng chứng theo khung E1–E6 (executor chuẩn bị · nghiệm thu N9 là của Host + Reviewer)

### E1 — Scope diff
Ngoài scope = 0. Mọi file mới/sửa phải map vào Điều30/31 protection hoặc test/guard của baseline MCPW.

### E2 — Runtime identity
Ghi before→after:
- image/hash/StartedAt;
- config hash;
- service/timer status;
- guard target/hash;
- UI source hash nếu sửa.

### E3 — Independent source/live
Executor chạy:
- backend tests;
- browser Owner View;
- live guard status;
- contract 37/23;
- lifecycle snapshot;
- Hermes gate.

### E4 — Negative control
Ít nhất một negative/mutant cho từng lớp mới thêm:
- regression test phải đỏ nếu invariant UI/backend bị bỏ;
- integrity sensor phải đỏ nếu snapshot stale/config/hash sai trên fixture/bản sao;
- không phá production để tạo lỗi.

### E5 — Reconciliation
- 0 duplicate event từ retry trong fixture;
- snapshot/import cursor không bỏ/nhân đôi;
- guard không báo PASS khi source unavailable;
- browser contract đọc đúng fixture/state.

### E6 — Rollback
Mỗi mutation có exact rollback; rehearsal trên bản sao khi phù hợp.
Không rollback production nếu PASS.

## 8. Acceptance cuối

PASS khi đồng thời:
- Điều 30 backend regression durable;
- Điều 30 Owner View browser regression durable hoặc residual nhỏ có bằng chứng rõ nhưng không làm mù regression;
- Điều 31 Config Guard phủ toàn MCPW R2-owned files/config;
- Protection Guard tự canh các invariant R2 quan trọng;
- watchdog/self-protection PASS;
- Hermes gateway monitor UP (`drift=none`);
- Protection Guard không còn đỏ do MCPW; UP hẳn nếu §6.3 được Owner cho phép;
- ngân sách cứng §0 không vượt;
- backend R2 23/23 (hoặc suite kế thừa) PASS;
- contract 37/23 PASS;
- P02/B1/B2A/Hermes manual gate không regression;
- Codex Desktop + Claude Code detection baseline vẫn PASS;
- ngoài scope = 0.

Không đặt soak mới nếu test/sensor trực tiếp đủ bằng chứng.

## 9. KQ

PASS:
`KQ@MCPW-R6-PROTECT-CLOSE-20261002-01 XONG · PROTECTED_READY_FOR_OWNER_CLOSE`

KQ mở đầu bằng bảng:
| Khối | Trạng thái |
|---|---|
| Mục tiêu 5 AI được bắt | 🟢/blocker |
| Điều 30 backend | |
| Điều 30 Owner View/browser | |
| Điều 31 Config Guard | |
| Điều 31 Protection Guard/watchdog | |
| Bằng chứng E1–E6 | |
| MCPW-owned alert live | |

Sau đó mới ghi evidence ngắn:
- commits/diff;
- test/browser artifacts;
- guard/watchdog;
- runtime before→after;
- rollback;
- residual thật.

FAIL:
`KQ@MCPW-R6-PROTECT-CLOSE-20261002-01 DỪNG · <blocker>`

## 10. Sau KQ

Executor KHÔNG tự mở Bảng giao việc/NEXT/lease/REST/Directus/VPSUP.

Nếu KQ XONG:
- Claude Chat Reviewer nghiệm thu 1 vòng cuối trên KQ + artifacts;
- Host đối chiếu;
- Owner nhìn Owner View và gật O-MCPW-CLOSE;
- sau đó mới mở roadmap “Bảng giao việc / Quy trình công việc”.
