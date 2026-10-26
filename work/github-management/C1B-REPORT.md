# C1B — KQ XONG CÓ GIỚI HẠN · 26/10/2026

RUN_ID: `GHM-C1B-CODEX-BASELINE-MANUAL-CD-20261026-01`  
Executor: Codex · Host READY P58: `39dde3fbb411a4c626ab979cb6296ba139798fba`  
PROMPT SHA256: `75e636ad9fc3edb7c4658701ccc15fedea02fc4f060ae5cb393c9b927ef7a1cc`  
KQ: P61 · **C1B_SCOPED=FAIL; CONTROL_PROTECTION=PASS; GUARD_POST=PASS; GLOBAL_GUARD=PARTIAL.**

**Đã giữ được 2 main mới, 2 CI xanh, 2 bản build và 4 repo archive. Chưa đạt mục tiêu deploy/rollback hai ứng dụng và chuyển ba audit.** Không tuyên bố production đang chạy main mới. Hai ứng dụng cũ healthy, không restart; source VPS giữ nguyên. Không tự mở C3/C2/C4.

## 1. Kết quả S0–S7

| Bước | Kết quả | Bằng chứng / phần còn thiếu |
|---|---|---|
| S0 | PASS | READY/PROMPT/Owner RUN, gh Owner có workflow, SSH hợp lệ; PRE PASS; ngân sách Actions $0 + Usage blocked. VPS-GHI CAS trước ghi host. |
| S1 | PASS trong phạm vi baseline | Clone riêng; cây VPS, phần Web chưa commit, lịch sử main cũ và archive giữ đủ; quét credential/license/migration. Không chạy SQL. Không chứng nhận license toàn bộ dependency. |
| S2 | PASS 2/2 | CI ứng viên thực chạy trên runner từng repo; main fast-forward đúng SHA đã GREEN, không force và không trộn mã main cũ. |
| S3 | PARTIAL | Build 2/2 thành công; một script deploy và cấu hình đã được Config Guard/code-ledger bảo vệ. Kiểm âm/đổi thư mục nguyên tử rồi khôi phục trong fixture PASS. Canary chưa đủ để cho phép deploy. |
| S4 | DỪNG riêng từng app | AD lệch Compose config hash. Web candidate mất CSS/JS do đường dẫn sau đóng gói. **0/2 diễn tập deploy–rollback; 0 restart.** |
| S5 | Chưa chuyển, 0/3 | Hai nhóm cần secret production; ops-smoke thực nhận runner nhưng HTTP 403 rồi timeout. Giữ kiểm cũ an toàn. |
| S6 | POST/bàn giao hoàn thành có giới hạn | POST 25/25 phép kiểm PASS, coverage 4/4, không đỏ mới; receipt 307; hồ sơ có hash; trả VPS-GHI. |
| S7 | XONG độc lập | Archive 4, giữ 5 ứng viên; giữ chatgpt-githubnew; không đổi visibility. |

## 2. Source, GitHub và runtime là ba trạng thái khác nhau

| Repo | Source VPS HEAD | Main cũ → main mới đã CI GREEN |
|---|---|---|
| agent-data-test | `bfe86c8ce1c0c1d16ca860fedf6aa324b1ec196f` | `0a26280b009d1893188b3c6b4a3c7db728082fcb` → `e6274592b9b8a291e4b9aeafcdf55370a10e09f4` |
| web-test | `0979ffa34d1718f8d052c629715b3aaeb981b9af` | `07caed3b8cacd958066e578a68bc4d60cfa136b8` → `747c3b12c893a4186c197f17d312e38da7ed654f` |

- [Agent Data CI 40324553292](https://github.com/Huyen1974/agent-data-test/actions/runs/40324553292): **6 passed**, runner ghm-ci-agent-data-test, đúng SHA main mới.
- [Web CI 40325187106](https://github.com/Huyen1974/web-test/actions/runs/40325187106): **16 passed**, runner ghm-ci-web-test, đúng SHA main mới.
- Mỗi repo có tag `archive/c1b-main-before-20261026` trỏ main cũ, đã readback. Main cũ vẫn là tổ tiên của main mới.
- Web gitlink vẫn chỉ commit cũ trên VPS nhưng working tree bên trong bẩn: 1 file sửa và 9 file chưa track. Snapshot riêng `37ae9e570714e21f39d4752332907797171145fa`, tag `archive/c1b-web-rp-source-20261026`; parent baseline `db7838dd9fce39b1e8f6021948cde649a0eb320b`. Không checkout/reset cây VPS.
- Diff ngoài baseline chỉ có workflow probe đã kê. Có **112 commit AD và 29 commit Web** chỉ ở main cũ: danh sách lưu riêng cho KST xét ở C3, không tự trộn.
- Runtime AD vẫn image `46e0ba15f18f2c4241a6a704eaa7c3f209432453a78e04dff626187ec1f50c8c`; Nuxt vẫn image `5cfe1dda767a4529aef2dfc99a3289ca62be225edd457c6408341806f2834569` và output cũ 1.831 file. Binding source HEAD → runtime release **UNKNOWN**, không suy đoán.
- License metadata hai cây là MIT; Web có 32 đường SQL/migration được nhận diện, không thực thi. JWT lịch sử đã hết hạn; token Directus lịch sử được Owner cho phép kiểm một GET, trả **401**, không xuất token/body. Literal default cũ không khớp env credential đang chạy; đây là nợ lịch sử cần xử lý riêng, không đồng nghĩa chứng minh mọi credential từng tồn tại đều đã bị thu hồi.

## 3. Build, canary và hai blocker deploy

**Agent Data:** build theo Dockerfile/requirements đã ghim trong source; lần đầu hết 600 giây tại tải NLTK, lần thử lại bằng cache thành công. Candidate image:
`sha256:b2526adbac2f300325a7e75bd54e88b9b027d6b0cbc3dddcf3fecb84632eb2b4`.
Canary không mạng/credential không chứng minh được HTTP contract; log có ConnectionError. Không coi đây là lỗi production. Blocker quyết định vẫn là Compose config hash **khác** hash của container thật: restart bằng Compose không bảo đảm phục hồi đúng cấu hình cũ. Đã pin image old và lưu snapshot riêng; không sửa Compose để ép qua cổng.

**Web:** lần build đầu Node hết heap 1,5 GiB; lần hai thành công với heap 2,5 GiB, container giới hạn 2 CPU/3 GiB, MemorySwap=Memory. Lockfile frozen, không nâng dependency. Artifact là **Nuxt 3.20.2 / Nitro 2.12.8**, runtime cũ là Nuxt 4.5.2 / Nitro 2.13.4.

Canary thủ công không credential, chỉ URL công khai: hai trang Knowledge và sáu trang công ty trả 200; sáu trang công ty trùng checksum nội dung với bản live. Tuy nhiên **continuity.css và interaction.js trả 404 ở candidate, 200 ở live**. Hai file tồn tại và đọc được; bundler chuyển import.meta.url sang globalThis._importMeta_.url của entrypoint, làm đường dẫn tương đối trỏ sai. Không hạ test, chép vá output hoặc thay source/main ngoài baseline được duyệt.

**Control deploy:** đã tạo đúng một script dùng lại cho hai app, có help/dry-run/health/deploy exact SHA/rollback và giới hạn restart. Cấu hình hiện từ chối hai app theo đúng blocker trên; chưa được nghiệm thu đường deploy production. Kiểm âm, atomic exchange/restore trong thư mục thử, mutant/missing/restore qua logic detector hiện có PASS; Config Guard production CLEAN. Đây **không phải** bằng chứng diễn tập rollback ứng dụng thật.

## 4. Ba audit và chi phí

| Nhóm | Kết quả | Đường tiếp |
|---|---|---|
| AD Data Lifecycle | Chưa chuyển: cần AGENT_DATA_API_KEY | Host quyết định cách giữ cùng kiểm mà không cấp production secret cho runner. |
| Web Health Check | Chưa chuyển: workflow dùng API key và tham chiếu SSH key | Tách đúng phụ thuộc/quyền trong phạm vi được duyệt tiếp theo; không bỏ test để xanh. |
| Web ops-smoke | [Run 40326499440](https://github.com/Huyen1974/web-test/actions/runs/40326499440), SHA `0a8be8152f5ba687fd8e7e01ef32708a8d2263a5`, runner ghm-ci-web-test; health 403, job vượt 10 phút, conclusion cancelled | Xác định contract health/public access rồi thử lại; nhánh thử giữ làm bằng chứng, không promote. |

Bản thử ops-smoke giữ test/scripts/triggers; contents:read, dùng repo variable URL đã có và bỏ fallback secret không dùng. Không cấp secret/DB/root cho runner. Ba nhóm chính vẫn active; các workflow deploy cũ vẫn disabled, không auto-deploy khi main đổi.

Ngân sách Actions UI xác minh **$0/$0, Usage blocked**. Usage tháng 10: Linux gross **1.348 phút**, discount 1.348, net **$0**; không suy billable rỗng của vài run là tổng tài khoản. **Phút hosted giảm thực tế từ S5 = 0**, vì chưa chuyển nhóm nào. Các audit hosted và repo khác vẫn tiêu thụ hạn mức, có nguy cơ bị chặn khi hết miễn phí. Không mua Pro, đổi ngân sách hay tạo runner mới.

## 5. S7 — archive có điều kiện

| Repo | Kết quả / lý do |
|---|---|
| platform-infra | ARCHIVED; đủ tiêu chí, không Pages |
| mpc_back_end_for_agent | ARCHIVED; đủ tiêu chí, không Pages |
| LarkBase_OAuth_Policy | ARCHIVED; đủ tiêu chí, không Pages |
| tool-kiem-thu-ci | ARCHIVED; đủ tiêu chí, không Pages |
| agent-data-test-backup | GIỮ: workflow chạy 26/10 |
| web-test-backup | GIỮ: workflow chạy 26/10 |
| agent-data | GIỮ: tên còn tham chiếu trong mã đang dùng |
| agent_data | GIỮ: tên còn tham chiếu trong mã đang dùng |
| agent-data-production | GIỮ: còn tham chiếu trong bootstrap code |

Đã kiểm mã/config/script và code-ledger, không chỉ tài liệu cũ; tên trùng tên module được giữ thận trọng. Readback archive/visibility PASS. Hoàn tác từng repo bằng `gh repo unarchive Huyen1974/<repo>`.

**chatgpt-githubnew giữ nguyên:** github-actions[bot] push main 26/10 07:54:19Z, SHA `3807a416560d49d98930951c29fd6406467b42fe`; có lịch đồng bộ secret hằng ngày và báo cáo/housekeeping hằng tuần, 18 workflow active. Tháng 10 **46 phút Actions Linux, net $0**; không can thiệp.

## 6. Bảo vệ, bằng chứng và bàn giao

- Guard POST **13:41:12Z PASS**, 25/25 kiểm; footprint đúng **4 tệp**, coverage đủ; Config Guard, INV23, INV25 PASS. **Receipt 307**. PREEXISTING_SAME #11, không đỏ mới do C1B.
- **GLOBAL_GUARD=PARTIAL** giữ riêng: đèn #11 có trước, vùng không quét/nợ quan trắc toàn hệ chưa được C1B giải quyết. POST PASS không xóa nợ toàn hệ.
- Cả hai app giữ nguyên container ID, image/output và StartedAt; **0 restart**, không đổi DB/nginx/source live. Hai runner vẫn giới hạn cũ, không thêm swap.
- Đã dọn thư mục source/dependency build tạm và cache riêng có thể gỡ; 0 container thử. Đĩa từ 62% lên 64%, còn khoảng 37,2 GB; giữ image candidate, output candidate và known-good để tái sử dụng. Swap host vẫn đầy từ trước; không swapoff.
- Hồ sơ private cùng RUN, nhánh `p58`: **1.911 file**; manifest SHA256 **`a9a84b4b059673fbd56de3fce47d33b31115cb5c663c94d2e4f9854b57927cd4`**. Gồm PRE/POST, build/canary/log, Git/CI, quét credential, archive readback, script/config hashes, kiểm bảo vệ và đường gỡ riêng control. Không đưa snapshot cấu hình/secret lên repo public.
- VPS-GHI đã trả cùng KQ P61; không RUN/kiểm thử nền của Codex còn giữ máy.

**NEXT_TRIGGER=HOST_REVIEW_C1B_P61_LIMITS.** Host/Claude nghiệm thu phần đã đạt; xác định phạm vi xử lý lệch cấu hình AD, lỗi đóng gói Web và quyền/contract ba audit. Giữ hai main an toàn, không đảo main để che blocker. KST vẫn là Claude Code CLI từ C3; chưa tự chạy C3/C2/C4.
