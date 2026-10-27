# F1 KST — review/merge hai PR + Web production chạy bản build từ GitHub main

RUN_ID: `GHM-F1-KST-REVIEW-MERGE-WEB-20261027-05` · Executor: Claude Code CLI (Kỹ sư trưởng) trên Mac, gh `Huyen1974` + SSH Owner.
P80 READY@`77c23c7911d5b87c1b2494080e1f06d7e7cff5b1` = last-touch PROMPT; Owner RUN trực tiếp. STARTED P81 commit `e0f425a0` lúc **09:06:56Z** (dòng STARTED ghi nhầm «09:14Z», đính chính tại đây). Mọi giờ là UTC 27/10/2026.

**KQ: XONG.** `F1_A=PASS` · `AUDIT_EXECUTION_VERIFIED=PASS_MAIN` · `BUSINESS_HEALTH=FAIL` (giữ RED) · `F1_B: WEB_RUNTIME=MAIN@e9f5801f422f2ae452023386cb1ce66d96c1cbc4` (đang phục vụ, giữ chạy). C1B Agent Data rollback **vẫn chưa đạt**, AD không deploy. Đây là mốc đổi nguồn build của production, **không phải** PR đổi mã ứng dụng (thuộc F2).

## 1. F1_A — review và merge

| PR | Head đã duyệt | Chữ ký KST | Merge (`--merge --match-head-commit`) |
|---|---|---|---|
| [AD #350](https://github.com/Huyen1974/agent-data-test/pull/350) test-only `/kb/list` | `ce36577ff19026f7259e7092608b713498143afb` | [KST_ACCEPT](https://github.com/Huyen1974/agent-data-test/pull/350#issuecomment-6437884635) | 09:07:33Z → main AD `a03a3b8f37ead0d73181ed96baf85e05c9c05544` |
| [Web #676](https://github.com/Huyen1974/web-test/pull/676) audit Web Health | `4556635c…` → KST_FIX `5aee9a2bca884d4e85915edc11a49d9c0dbf200c` | [KST_ACCEPT_WORKFLOW](https://github.com/Huyen1974/web-test/pull/676#issuecomment-6437965239) | 09:11:54Z → main Web `e9f5801f422f2ae452023386cb1ce66d96c1cbc4` |

- **#350:** đọc toàn diff (1 tệp +151). Test nạp bằng AST đúng thân `_error`/`_ensure_pg`/`_normalize_list_pagination`/`_list_kb_documents_page` + `LIST_DOCUMENTS_DEFAULT_LIMIT` của `agent_data/server.py` tại head, chỉ thay DB/HTTP adapter ⇒ unit contract, không phải integration. Chạy lại độc lập trên Mac **19/19 PASS**; gate run 40459074294 SUCCESS (33 tests). Base không đổi trước merge.
- **#676:** đọc toàn diff 3 tệp; blob trước KST_FIX = candidate `d3b1ec8`. Đối chiếu từng bước CHECK với main: 4/9/13 không đổi; 1/6 chuyển `/server/health`→`/server/ping` (Directus 12); 2/5/7/8/12 chuyển vào `scripts/ghm/web-health-audit.py` với ngưỡng nghiệp vụ cũ giữ nguyên (sync=ok & docs>50, ratio chỉ WARN, gap ≤10, ≥15/≥15/>0/>0, rules=10 WARN, registries 15 s); khoá API qua stdin của curl; lỗi HTTP/schema là technical, không coi 0. Unit audit 11/11 OK trên Mac.
- **KST_FIX** (luật merge Owner #5): một commit chỉ xoá dòng điều kiện `workflow_dispatch` của nhánh `c1b-audit-finalize-health` (−1 dòng); lịch `0 */6 * * *` + dispatch chỉ `refs/heads/main`. Gate run 40478663324 trên head mới: preflight/gitleaks («no leaks found»)/unit **16 passed** đều success; policy RED đúng 2 lý do được phép (`workflow/CI execution script`, `secret reference`) ⇒ ngoại lệ thủ công có lý do. Không self-APPROVE (cùng GitHub identity), không cấp secret cho PR, không force/bypass.

## 2. Audit Web Health trên main

[Run 40478982147](https://github.com/Huyen1974/web-test/actions/runs/40478982147) — dispatch **1/2** từ main, `ref=refs/heads/main sha=e9f5801f`, runner VPS `ghm-ci-web-test`, 09:12–09:13Z. Đủ 13 CHECK, **11 PASS / 2 FAIL nghiệp vụ**, job RED và bước báo lỗi giữ nguyên:
- CHECK2 FAIL: 10.043 docs · 20.297 vectors · ratio 2,02 · `sync_status=warning` (HTTP/JSON hợp lệ).
- CHECK7 FAIL: phân trang đủ 20 trang/9.604 mục; 5 thư mục ngoài allowed: assets, draft, reports, temp, test. `ids_sha256 e8215d52…` = P77.
- CHECK8 PASS/WARN gap 9 (AD 9.604 ↔ Directus 9.613); CHECK12 PASS (169/169/2.461/851/10, registries 200 trong 10 s); CHECK5 context 5.
- 3/3 audit nay chạy trên runner VPS (Data Lifecycle, ops-smoke, Health). Nợ ratio/sync, 5 thư mục, 2 orphan vectors giao chủ Agent Data/Host; không sửa dữ liệu/ngưỡng, không auto-heal.

## 3. F1_B — Web production lên bản build từ main và GIỮ

- **Nguồn:** main `e9f5801f…`: cây `web/` = `83cb7fbdf5953f9cc0ce32ff7c7ed97c332169d3` (= P66 `728fa1d`, F0 `f8c51fe`, PR676); `build-web-runtime.py` blob `a55a457`, addon sha256 `c2b4dcce…` (= COMPILER_SHA), `package.json` blob `0fbe090`, lockfile sha256 `7b6e11c0…` (= P66). Tar `web/`+`scripts/ghm/` bằng `git archive` trên Mac, sha256 `f665aa3d…` khớp hai đầu (VPS không giữ credential GitHub). Không có nguồn/đầu vào build mới.
- **Build:** `scripts/ghm/build-web-runtime.py` của chính main, Node 24.21.0 (digest `9ec4a2e2…`), Nuxt 4.5.2, pnpm 9.6.0, container 2 CPU/3 GiB, 0 swap thêm; 09:20–09:26Z; RAM khả dụng thấp nhất 925 MB. Output 1.831 tệp + 6 symlink, `cweb-owned-build.json` đúng lock/compiler.
- **Parity canary** (script P66 `canary-web-parity.py`, chỉ đổi RUN/đường dẫn/tên container): nuxt + nginx dùng một lần trên loopback, cùng image/mount chỉ đọc. Lượt đầu 164/166: 2 trang registries của **bản live cũ** timeout 15 s (candidate 200) ⇒ kiểm lại tuần tự 60 s như P66: 3/3 PASS ⇒ **166/166** (132 VPSUP + 32 CWEB + 2 tài nguyên), 34 nội dung tĩnh trùng checksum. 0 container canary còn lại.
- **PRE:** Guard PRE 09:19:46Z PASS (đỏ có sẵn ∅). Nuxt old image `5cfe1dda…`, StartedAt `2026-10-26T17:20:25.078798399Z`, healthy; live = known-good P61 = `old_manifest` (1.831 tệp + 6 symlink); profile bảo vệ `057cda45…`; script deploy `7b1d917c…` và config `b3563a16…` đúng bản P66 (bản chép giữ trong hồ sơ).
- **Config deploy qua apply-v0** (script deploy KHÔNG đổi): `b3563a16` → `1e113957` (approved_main_sha, canary 166, candidate materialize 1.876 đường dẫn cùng cách P66, 32 http_contract, lease 40′) → `c13cfa11` (đóng lease 09:30:49Z).
- **Deploy 09:28:43–09:29:30Z** bằng `ghm-manual-deploy.py` P61/P66: dry-run PASS, SHA sai bị từ chối, deploy exit 0; **1 restart Nuxt** (StartedAt `2026-10-27T09:28:46.61491405Z`, image giữ `5cfe1dda…`, healthy), nginx chỉ reload qua script (container không restart), Agent Data không đổi. Hậu kiểm: **34/34 contract tĩnh + 166/166 route live PASS**; output phục vụ = candidate (`server/index.mjs` `99315cd2…`); profile bảo vệ `057cda45` → `d8d34c69` (runtime = manifest mới). **Giữ chạy, không rollback.**
- **Đường lùi:** bản old nằm ở thư mục trao đổi `deploy/ghm-f1/nuxt4-main-e9f5801f` (đã kiểm = `old_manifest`) + known-good P61 nguyên vẹn; `ghm-manual-deploy.py nuxt --rollback` cần lease mới qua apply-v0 (lease đã đóng, thử lùi sau khi đóng bị chặn `LEASE_EXPIRED`); restart_count 1/4.

## 4. Bảo vệ và đóng

- Guard periodic 09:30:32Z «OK all invariants» (gồm bảo vệ Web); Kuma 32/32 UP, 0 nhịp lỗi #1/#6/#22 từ 09:28Z. Config Guard CLEAN.
- Guard POST1 09:32Z FAIL coverage (proof Đ30 thiếu nguyên chuỗi `--run`) — giữ nguyên làm bằng chứng; bổ sung dòng RUN vào proof ⇒ **POST2 09:33:22Z PASS**: footprint 2/2 (config deploy, profile bảo vệ Web) đủ 4 ô, không đỏ mới, change_event PASS; **biên nhận 312**.
- VPS-GHI 09:18Z → trả trong commit KQ. 0 container/tiến trình thử, thư mục tạm build rỗng. Giữ output build, thư mục trao đổi (62 MB) và bằng chứng (hồ sơ VPS `work/github-management/<RUN>/`, 140 MB) — không phải rác.
- Không deploy Agent Data, không sửa PG/Directus/nginx config, không auto-CD, không Pro, không F2/C4, không task mới.
- Sự cố ghi repo: commit `da2e9bf8` tạo nhầm tệp báo cáo này với nội dung giữ chỗ «PLACEHOLDER» (message đã mang chữ KQ) trước khi đủ các phần; commit kế tiếp thay nội dung thật cùng KQ/bảng/trả cờ. Không ảnh hưởng VPS.

## 5. Giới hạn và nợ

- Bản build không giống byte với old (tên chunk khác); parity theo HTTP/content-type + checksum tĩnh đúng tiêu chí P66.
- `workflow_dispatch` của một nhánh chạy bản workflow của chính nhánh đó ⇒ khoá cứng cần environment/ruleset (C2 Pro); pilot vẫn dựa tác giả tin cậy.
- Script deploy ghi nhãn agent `openai-codex` cố định cho lần apply-v0 profile; executor thật là Claude Code (không sửa script để đổi nhãn).
- Business RED (CHECK2/CHECK7, 2 orphan) và C1B AD rollback là nợ riêng, không chặn F2.

**NEXT_TRIGGER=HOST_ACCEPT_F1_P82** → GPT Host nghiệm thu; Owner quyết C2 Pro trước F2; PR đổi mã ứng dụng Web đầu tiên ở F2.
