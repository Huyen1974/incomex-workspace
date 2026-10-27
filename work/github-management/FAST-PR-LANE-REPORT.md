# FAST-PR-LANE — F0 XONG, bàn giao KST

RUN_ID: `GHM-FAST-PR-LANE-20261027-04` · Codex · 27/10/2026.
Owner RUN; GPT Host P74 READY last-touch `5f9bb019c6a2fba146d5b86d5debcdb3a34f9e93`; PROMPT SHA256 `d15fceeca2169522192f986c208ab346400d6affb3c9baf3d76a4548c841c832`. P75 clarification đã đọc. STARTED P76, KQ P77. Không sửa PROMPT hay phần đã nghiệm thu P66/P71.

## 1. Kết quả và hai PR để KST xem

**F0=PASS theo phạm vi pilot tin cậy. S4-B=PASS sửa xác thực và kiểm candidate; audit nghiệp vụ vẫn RED. Chưa merge/deploy, chưa F1/C2/F2/C4.**

| Việc thật / DoD | PR / unit / policy | Bằng chứng và bàn giao |
|---|---|---|
| AD: test hợp đồng limit/offset/next_offset của `/kb/list`, không đổi runtime | [PR350](https://github.com/Huyen1974/agent-data-test/pull/350), **33 tests PASS**, policy GREEN, gate GREEN | [Run40459074294](https://github.com/Huyen1974/agent-data-test/actions/runs/40459074294), runner `ghm-ci-agent-data-test`; 1 file/151 dòng thêm. KST có thể xét; PR còn draft/open, chưa merge |
| Web: sửa audit Web Health P71, giữ 13 CHECK/ngưỡng cũ | [PR676](https://github.com/Huyen1974/web-test/pull/676), **16 unit PASS**, policy **RED KST_REVIEW_REQUIRED**, gate RED đúng yêu cầu | [Run40459085757](https://github.com/Huyen1974/web-test/actions/runs/40459085757), runner `ghm-ci-web-test`; 3 files,527+/520−. Đổi workflow/script CI và tham chiếu secret ⇒ KST phải duyệt; không ép xanh |

Hai PR đều secret scan PASS, preflight PASS, mergeable=true tại lúc đọc cuối; GitHub đánh AD clean/Web unstable do policy RED. Bảng tóm tắt KST nằm ngay trong job summary và body PR: DoD, tác giả, files/diff size, test, SHA, tác động, readiness. Không tạo PR giả hoặc thay mã production để có việc thử.

| Repo | Head tác giả | Merge-test thực chạy | Main bootstrap hiện hành |
|---|---|---|---|
| Agent Data | `ce36577ff19026f7259e7092608b713498143afb` | `6c26a92dfac0082105d0359d8a373ad92edc8265` | `76db54ff8904164955e8977d2a8184fba9c51fbf` |
| Web | `4556635ca22ada5bacba26b681ef638ec6f566ff` | `a069ba6499eecfa490095da71ad8e563c6260413` | `f8c51fe7a8d833cdee8156595d7d76e50621c66a` |

Một phiên Codex worker thứ hai làm AD test; phiên chính làm Web/gate ở worktree riêng. Worker AD commit test-only `40eb6d1…`,19 case mới +14 kế thừa; nạp đúng hàm production bằng AST theo mẫu repo, không sao chép thuật toán hoặc khởi động dịch vụ. Hai nhánh giữ cho dev tiếp tục: `dev/codex-ad/pagination-contract`, `dev/codex-web/health-audit`. Không giữ VPS-GHI khi viết mã.

## 2. Gate tối thiểu và giới hạn thực tế

Ngoại lệ bootstrap F0 đã dùng **đúng một commit/mỗi main**, non-force, kiểm old SHA trước và readback sau; mỗi commit chỉ thêm `.github/workflows/ghm-pr-gate.yml`. Không ghi mã ứng dụng lên main, không merge PR. Rollback workflow: KST/Owner có thể revert đúng commit bootstrap, không đụng runtime/PR; RUN này không thực hiện revert.

- Native GitHub Actions: `pull_request` tới main với opened/synchronize/reopened/ready_for_review; dispatch chỉ kiểm main tin cậy. Không push-dev trigger, không pull_request_target, concurrency theo PR/cancel bản cũ, job tên duy nhất `gate`.
- `contents: read`, không tham chiếu repository secrets trong PR gate; job chỉ nhận same-repo/Owner account/nhánh `dev/codex*` hoặc `dev/claude-code`. Preflight kiểm author, actor/triggering_actor, base còn là live main, head SHA, cha của merge-test và hash workflow đang thực thi bằng bản main. PR đổi chính gate ⇒ dừng trước checkout/chạy mã PR.
- **Đối chiếu độc lập trên Mac** trước khi mở PR: blob gate tại head bằng main ghim; hash AD `3b9e04f66af56080a660f24fb8a516c6aa8ffb25eed320b9fe9211bf450b2e5e`, Web `8e7aea0edb7e1cb0658c738a2a223eb108c038634ad47ef697e53f487e531428`. Self-check của workflow không tự chống được PR thay cả workflow/loại bỏ self-check; pilot dựa thêm nguồn tác giả tin cậy/kiểm Mac, không claim hard-lock.
- Checkout dùng lại exact-fetch với token ngắn hạn qua môi trường Git tạm, không lưu credential (`persist_credentials=false` được kiểm trong log/config); tránh lỗi gitlink Web lịch sử, không init submodule. Token job không chuyển vào unit step. Không dùng tài khoản/key production Mac trong runner.
- Gitleaks8.30.1/hash binary kế thừa từ CI Web, không dựng công cụ mới. Config quét/ignore ở trusted workflow, không đọc cấu hình allowlist từ PR; không cho comment `gitleaks:allow` trong PR tắt phát hiện. Scope guard ghi files/diff size và policy RED khi đổi workflow/scripts CI, thêm tham chiếu secret, hoặc diff lớn. Metadata summary cũ được xóa trước preflight để không báo nhầm SHA.
- Web không build Nuxt; chỉ Node24.21.0 + frozen deps/ignore-scripts +16 unit đã có. AD baseline14 và19 test mới chạy thật. Flock chung giữ một đoạn cài/test nặng mỗi lần; không tăng RAM/swap.
- Hai runner vẫn user10001, không privileged/socket/bind host; named volumes `/runner` và `/ci-lock`, mỗi runner 1 CPU/1,5 GiB, MemorySwap=Memory. Cleanup hook kế thừa chạy sau job; không thay runner/config/watchdog.

GitHub trả403 yêu cầu Pro khi đọc branch protection private. Hai agent dùng chung tài khoản Owner `Huyen1974`; không có bằng chứng máy phân biệt được từng agent. Persistent runner không là môi trường sạch tuyệt đối; chưa mở fork, Dependabot hay actor ngoài pilot lên lane này. Trước F2 phải kiểm lại trust boundary/C2 đúng P74. [GitHub secure-use](https://docs.github.com/en/actions/reference/security/secure-use), [PR event/merge SHA](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request).

Bậc giải pháp: **2 cấu hình/ghép native GitHub và runner hiện có**, chỉ inline preflight mỏng trong workflow; không gateway/token/server/registry mới. PG/Directus không phải SSOT của Git PR/check nên không chuyển state Git vào DB.

## 3. S4-B: HTTP401 đã xử lý, lỗi dữ liệu giữ RED

Nguồn hiện hữu chỉ rõ GSM `AGENT_DATA_API_KEY`, project được repo sử dụng; đã ghim **version2 ENABLED** và chứng minh giá trị khớp cả `API_KEY` production lẫn map nginx bằng phép so khớp không xuất giá trị. Một GET `/kb/list?limit=1` trên Mac tới đúng HTTPS endpoint trả **200/application-json/items array/1 item**. Lần dùng Python trước đó dừng TLS handshake vì trust store Mac chưa đủ, **chưa gửi HTTP**; chuyển sang curl hệ thống, vẫn xác minh TLS/không redirect, không dùng insecure.

Chỉ sau các bằng chứng trên, cập nhật đúng **một GitHub secret đang có** ở Web qua stdin lúc06:08:26Z; không tạo credential hoặc sửa secret production. Đường khôi phục đã biết: ghi lại cùng phiên bản GSM chuẩn đã ghim và kiểm200; theo P75 không coi giá trị cũ401 không đọc lại được là bản lùi hợp lệ. Không in/lưu key vào log, file hay repo. Metadata/source chi tiết ở bằng chứng private.

[Audit candidate40459402138](https://github.com/Huyen1974/web-test/actions/runs/40459402138), branch `c1b-audit-finalize-health`, SHA `d3b1ec811eb79733a4b63fe30c2adaf3b4f935b1`, runner VPS Web: **dùng1/2 lượt dispatch được cấp**, không cần lượt2. Ba file audit trong PR676 byte-for-byte bằng candidate đã kiểm.

| CHECK | Kết quả thực | Chứng cứ |
|---|---|---|
| 1 Services | PASS | HTTP/service liveness |
| 2 Integrity | **FAIL dữ liệu/tiêu chí hiện hành** | 10.043 docs,20.297 vectors,ratio2,02,sync warning; HTTP/JSON hợp lệ; SQL read-only độc lập xác nhận10.043 alive docs |
| 3 Content | PASS | 3 bản ghi/trang theo luật cũ |
| 4 Cache | PASS có WARN kế thừa | Không đổi luật WARN/FAIL |
| 5 Search | PASS | HTTP200, context array5; không phải zero-context |
| 6 Directus | PASS | Ping/collection và401/403 bảo vệ flows đúng; lỗi curl --fail P71 đã sửa |
| 7 Structure | **FAIL dữ liệu/cấu trúc thật** | 20 trang/9.604 items tớiEOF; 5 thư mục ngoài allowed: assets,draft,reports,temp,test. SQL read-only độc lập khớp danh sách/hash |
| 8 Gap | PASS/WARN | AD9.604 ↔ Directus9.613, gap9 ≤10; không fallback0 hoặc kết luận mất9.613docs |
| 9 Registry | PASS | Ngưỡng cũ giữ nguyên |
| 10 Quality | PASS/WARN | CAT-ALL=SUM2.144.349; Qdrant ok;2 orphan vectors. Không auto-cleanup. Ghost không in lại ở nhánh WARN này, không giả số đo mới |
| 11 Rules | PASS | Blocking rules theo luật cũ |
| 12 Registry page | PASS | HTTP200,191CAT occurrences,11,452063s <15s; không đổi timeout, không chạy lại hosted đối chứng P71 |
| 13 Reconciliation | PASS INFO | Giữ ý nghĩa INFO |

**13/13 kết quả đáng tin ở lượt kiểm này;11 PASS / 2 FAIL nghiệp vụ, job vẫn RED và thông báo failure vẫn giữ.** Hash ID phân trang và SELECT độc lập cùng `e8215d52af884bc998554367c25789fe690dcdaa7031d77a48b2bd33e85b4f49`. Không sửa dữ liệu/schema/threshold. Giao nợ ratio-warning, thư mục trái allowed,2 orphan cho Host/chủ Agent Data quyết; không mở task mới.

`AUDIT_EXECUTION_VERIFIED=PASS_CANDIDATE`, `BUSINESS_HEALTH=FAIL`. Audit main cũ vẫn ACTIVE, lịch không đổi; chưa promote nên chuyển audit vận hành vẫn2/3. Chờ KST xem PR676, không claim C1B PASS. Agent Data Compose/rollback DDL còn nguyên nợ S4-A, không đụng trong RUN này.

## 4. Thời gian, bảo vệ và bàn giao

- PR350 mở 06:05:51Z; gate06:05:57–06:06:33Z =36 s, từ mở PR đến kết quả42s.
- PR676 mở 06:05:57Z; gate06:06:04–06:06:59Z =55 s, từ mở PR đến kết quả62s. Hai lane nhận việc song song; đoạn nặng tuần tự qua flock.
- Audit S4-B06:09:18–06:10:41Z =83 s. **GitHub-hosted dùng trong RUN:0 phút**, không đổi budget $0/Stop usage, không mua Pro. Không tuyên số tiền hóa đơn từ job elapsed.
- KST dự kiến cần 5–10 phút AD và 10–15 phút Web để đọc summary/diff (ước lượng, chưa đo). Không có baseline hàng đợi VPS so sánh ⇒ không bịa %speedup. F0 chứng minh viết/PR không chờ cờ, chưa chứng minh toàn đường release đã nhanh.
- Guard PRE22/22 và POST**25/25 PASS**, footprint host0,32/32 đèn UP, không đỏ mới, receipt**310**. GLOBAL_GUARD vẫn có3 vùng UNKNOWN kế thừa, không nâng thành chứng nhận toàn hệ tuyệt đối.
- Ứng dụng giữ image/start time P71: AD `46e0ba15…` từ26/10 08:19:50Z; Web `5cfe1dda…` từ26/10 17:20:25Z, cả hai healthy. **0 app restart/0 DDL/0 deploy/0 merge PR/0 runner reinstall**. Không host mutation cần lease; VPS-GHI không nhận trong RUN, trạng thái root vẫn trống khi đóng.
- GitHub footprint thực:2 workflow bootstrap main +2 PR +1 secret Web được phép. Đ30: CI33/16 và audit13; Đ31: SHA/blob/readback+Guard/INV25/cleanup+schedule hiện hữu. Giới hạn hard enforcement ghi rõ ở§2, C2 không tự làm.
- Giữ hai worktree/nhánhPR và bằng chứng để KST tiếp tục; không coi chúng là rác build. Không có canary/build container tạm. Manifest bằng chứng private: 15 tệp, SHA256 `57d48ef12baa8b393be282ba5e8f05feeffaa9f693a9cc53f935a5bd6a6589a8`.

**NEXT_TRIGGER=OWNER_KST_REVIEW_FIRST_WEB_PR_AND_MANUAL_RELEASE.** Host nghiệm thu F0 rồi giao Claude Code CLI F1 riêng; Web Health PR chỉ sửa audit, Host cần chọn thêm một PR ứng dụng nhỏ cho diễn tập release. Codex không tự bắt đầu F1/C2/F2/C4. Báo cáo này là KQ executor, không thay chữ ký ACCEPT của Host/KST.
