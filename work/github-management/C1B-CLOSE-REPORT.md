# C1B CLOSE — kết quả và bằng chứng

RUN_ID: `GHM-C1B-CLOSE-20261026-02` · Executor: Codex Desktop/openai-codex.
**KQ: XONG CÓ GIỚI HẠN. Web đã deploy–rollback thật; 2/3 audit đã chuyển và GREEN. Agent Data chưa qua canary, Web Health Check chưa đạt. Chưa đủ nghiệm thu toàn bộ C1B; không mở C3/C2/C4.**

P64 READY last-touch `7ccf89e276b4848704dd8ad1b4a8a75bd3f846cb`; PROMPT SHA256 `3af5f83d0eae4b2f44e6ebeb507eba0ef4ffe8a77b64d326fbc1bdb1a8989725`, kiểm lại không đổi. Owner RUN trực tiếp. STARTED P65 commit `90560368a35a0ac3e05338a443f6365453d239f6`. Cờ nhận thực tế 16:17:39Z tại `5816be7`; lỗi nhập giờ ban đầu đã sửa công khai bằng `86db356`. Tất cả giờ dưới đây là UTC ngày 26/10/2026; 17:00Z trở đi tương ứng ngày 27/10 tại Việt Nam.

## Kết quả theo cổng

| Hạng mục | Kết quả | Giới hạn / bằng chứng chính |
|---|---|---|
| S0 / kế thừa P61 | PASS | PRE 22/22, manifest P61 `a9a84b4b…` nguyên vẹn; READY/main/cờ kiểm trước mutation. Không làm lại runner, archive hoặc token cũ. |
| R1 Web source/PARITY/CI/main | PASS | Đúng Nuxt 4.5.2, Node 24.21.0; 166/166 parity; CI 16/16 unit test; main `728fa1d…`. |
| R2 AD effective config / source | PASS phần đối chiếu | **17 trường**, không phải 18 như checkpoint nhập nhầm; 40 tệp image đều có trên main, 2 tệp khác do main mới hơn. Image candidate giữ nguyên toàn bộ Config. |
| R2/R4 AD canary / deploy–rollback | CHƯA ĐẠT | Canary PG chỉ đọc: `/info` và `/health` 200 nhưng `/kb/list?limit=1` 500; bootstrap không khởi tạo được store. 0 restart AD. |
| R4 Web deploy–rollback | PASS thật | Deploy 17:19:49Z; contract 34/34; rollback 17:20:25Z; old healthy xác nhận 17:20:36Z. Hai restart, old output/profile phục hồi đúng. |
| R3 Data Lifecycle | PASS | Candidate và main GREEN trên runner AD; giữ lịch `0 1 * * *` và chế độ báo cáo hiện hữu. |
| R3 ops-smoke | PASS | Candidate và main GREEN trên runner Web; ping/pages/asset 200; lịch `0 */6 * * *`; HTTP 4xx fail ngay, timeout 5 phút. |
| R3 Web Health Check | FAIL, không promote | Chạy đủ 13 CHECK: 8 PASS, 5 FAIL. Workflow hosted cũ vẫn ACTIVE, không bỏ kiểm để ép xanh. |
| Guard phạm vi thay đổi | PASS, POST 25/25 | Footprint cuối RUN: đúng một file cấu hình của công cụ deploy; script deploy không đổi. |
| GLOBAL_GUARD | PARTIAL | #11 vẫn là nợ có trước; ledger còn vùng UNKNOWN. Không nhận toàn hệ sạch. |
| VPS-GHI | Đã trả trong commit KQ P66; deploy lease đã đóng | 0 tiến trình/container thử còn chạy; hai runner online/idle, giới hạn không đổi. |

## Web: nguồn đúng bản đang chạy và diễn tập thật

Nguồn khôi phục đủ từ nền `nuxt-repo/web @41621e4`, patch Nuxt4 SHA256 `47c5c4eb8922fe064d27013b903bf510a7e99e80452c186ee0a5d6044a85b374`, hai commit lab `c649bda544811ba9d31f598be09f815f06d3c48d` và `3934015d02ad4c2a6b27f9de0513e27b1779aacd`. Đối chiếu 570 tệp lab trước khi ghép CWEB từ nguồn đã chấp nhận `132ff49`/`ed76ba06` cùng tài nguyên tĩnh.

Đã giữ đúng cách build hiện hữu: Nuxt4 nền, sau đó compiler CWEB nguyên bản. Gom tất cả vào một lần Nuxt build làm sai đường tài nguyên; đã tái tạo đúng quy trình, không vá ứng dụng để che lỗi. Compiler SHA256 `c2b4dcce32fb7796248dc9a0e6212ffc10d41f4575c686f42d7b707f47b86c4e`. Lockfile SHA256 `7b6e11c06254901609f73313b65fbb5446e281546e8a2edd0bfcff94eff91773`; pnpm 9.6.0; build image Node ghim digest `9ec4a2e289874ed0d722e1772ec2de45d2801541db8612f3638b26f128c69ac2`. Công cụ build tái lập tại `scripts/ghm/` đã chạy đầu-cuối thành công, giới hạn 2 CPU/3 GiB và không thêm swap; không tạo cơ chế deploy mới.

Parity gồm 132 route VPSUP, 32 route CWEB và hai asset. HTTP/content-type trùng live; 34 nội dung tĩnh trùng checksum. Ba route registries phải kiểm lại tuần tự với timeout 60 giây do live chậm; cả ba đạt, không loại route hay đổi tiêu chí. Build sinh tên chunk khác nên **không tuyên bố toàn bộ output rebuild giống byte với old**.

CI [40366408664](https://github.com/Huyen1974/web-test/actions/runs/40366408664) GREEN tại **`728fa1deaee45b36c07714ede1da4c0633683e89`**, runner `ghm-ci-web-test`: checkout exact SHA, gitleaks delta sạch, Node 24.21.0, kiểm input build và 16/16 row-link tests. Hai lần CI trước dừng ở checkout do gitlink lịch sử không có `.gitmodules`; giữ gitlink, dùng fetch exact SHA với xác thực tạm trong bộ nhớ, không lưu credential. Main fast-forward non-force từ `f1fe708…` lên SHA xanh; cây `web/` bằng cây đã canary. Không thêm trigger `dev/*` hoặc PR, không bật auto-deploy.

Cổng dry-run tiếp tục bắt được manifest P61 thiếu sáu symlink thư viện. Đã chứng minh old live và backup khớp cả 1.831 tệp thường + 6 symlink, bổ sung metadata release; không hạ kiểm, không sửa Guard. Candidate materialize các đường symlink thành tệp khi sao chép: toàn bộ 1.876 đường dẫn khớp hash nội dung nguồn đã canary. SHA sai bị từ chối trước mutation.

Diễn tập dùng **nguyên script P61**, SHA256 `7b1d917c18090d26b8700c2b0d0f37655228f89ade2668fe92605d0b2ef10ea6`:
- Candidate healthy, 34/34 trang/asset tĩnh trùng HTTP, content-type và checksum; các route health của công cụ deploy cũng đạt.
- Rollback về old: 1.831 tệp + 6 symlink và profile bảo vệ khớp nguyên bản; image vẫn `5cfe1dda767a4529aef2dfc99a3289ca62be225edd457c6408341806f2834569`.
- Web StartedAt sau rollback `2026-10-26T17:20:25.078798399Z`, healthy, không OOM. **2/4 restart đã dùng**, không dùng recovery khẩn cấp. Chỉ reload nginx qua công cụ P61; không restart nginx/DB/VPS.

## Agent Data: đã phân biệt rõ đối chiếu đạt và canary chưa đạt

17 trường hiệu lực đã chuẩn hóa gồm image, env, mounts, networks, ports, user, entrypoint, cmd, working_dir, restart, healthcheck, labels ngoài compose, memory, swap, CPU, init và stop_timeout. Tất cả bằng nhau; env chỉ so hash, không xuất giá trị. Nhãn Compose lịch sử khác hash render hiện tại nhưng **không có khác biệt cấu hình hiệu lực**. Chưa truy nguyên đầy đủ phiên bản renderer tạo nhãn cũ; không đổi Compose để ép nhãn khớp.

40 tệp image có đủ trên main; `server.py` và `workspace_tools.py` khác do release `2b14c2a` cũ hơn `bfe86c8` trên main. Main hiện `251739422a997c9741e487fb4252f3c3d92e1be1`, thêm audit, không đổi mã ứng dụng so baseline P61. Candidate mới `0419152b…` được dựng trên image old `46e0ba15…`, giữ toàn bộ image Config giống nhau, hash Config hai bên `41c29d399f800659f02e4a0f5d5ad3de5cccdb0c0a335a1229e0fa005513096d`. Candidate P61 khác CMD không được dùng.

Canary cô lập, không host port, mounts chỉ đọc, listener vector bị chặn và không bật workspace supervisor. Với PG read-only, bootstrap `CREATE IF NOT EXISTS` không chạy được: `/health` vẫn trả 200 nhưng kiểm dữ liệu chưa đạt, `/kb/list` 500. Không coi health 200 là đủ.

Đã kiểm catalog bằng truy vấn chỉ đọc: cả 6 bảng/index mà bootstrap dùng đều tồn tại. **Bộ xét duyệt tự động vẫn từ chối chạy canary bootstrap thông thường vì lệnh CREATE có khả năng ghi schema bằng credential production.** Hai lần bị từ chối không thực thi. Đã hỏi Owner quyền rõ cho đúng canary giới hạn này; chưa nhận được câu trả lời ở thời điểm đóng RUN. Không thử đường vòng, không sửa bootstrap/schema/quyền để vượt chặn.

AD vẫn old image `46e0ba15f18f2c4241a6a704eaa7c3f209432453a78e04dff626187ec1f50c8c`, healthy; StartedAt **`2026-10-26T08:19:50.062914772Z` không đổi**. Không sửa config/script deploy AD; image mới chỉ giữ làm candidate chưa phát hành.

## Ba audit: bằng chứng và lỗi còn mở

| Audit | Candidate | Main đã chạy thật | Trạng thái cuối |
|---|---|---|---|
| Data Lifecycle | [40357980536](https://github.com/Huyen1974/agent-data-test/actions/runs/40357980536), `6ea92ef…`, GREEN | [40359232468](https://github.com/Huyen1974/agent-data-test/actions/runs/40359232468), `2517394…`, GREEN, 39 giây | ACTIVE trên runner AD; cùng script/chế độ advisory và lịch. |
| ops-smoke | [40357987004](https://github.com/Huyen1974/web-test/actions/runs/40357987004), `1333f33…`, GREEN | [40359238669](https://github.com/Huyen1974/web-test/actions/runs/40359238669), `f1fe708…`, GREEN, 20 giây | ACTIVE trên runner Web; source main mới giữ nguyên workflow này. |
| Web Health | [40358212304](https://github.com/Huyen1974/web-test/actions/runs/40358212304), `9bfc84f…`, FAIL, 121 giây | Không promote, không dispatch bản lỗi trên main | Giữ hosted ACTIVE. |

Data Lifecycle báo 10.040 documents, 20.294 vectors, **2 vector mồ côi và 1 tài liệu thiếu vector**, `needs_cleanup`. Job GREEN là chạy thành công chế độ báo cáo đã có, **không chứng minh dữ liệu hoàn toàn sạch**. Không auto-heal/xóa dữ liệu.

Web Health giữ đủ 13 CHECK; jq được tải bản ghim/checksum trong job temp, không cấp root. Năm lỗi:
- CHECK2: `sync_status=warning`.
- CHECK5: search không có context; log thiếu dữ kiện HTTP/auth để kết luận RAG hỏng.
- CHECK7: phản hồi list/null không parse được; cần làm rõ contract và quyền key của đúng repo.
- CHECK8: số AD bị tính thành 0 so Directus 9.613; **gap 9.613 chưa phải bằng chứng mất dữ liệu** vì đầu vào chưa được xác thực.
- CHECK12: các số PG 169/169/2455/851/10 đạt; trang registries timeout 15 giây. Kiểm parity riêng sau đó timeout 60 giây đạt, nhưng không tự sửa chuẩn audit để ép PASS.

Hai workflow đã promote chỉ nhận schedule/dispatch từ `refs/heads/main`; ngoại lệ thử nhánh đã bỏ. Không disable workflow vừa chuyển. Lịch sử runner từ khi tạo được đối chiếu: không job PR chưa tin cậy; cleanup có sẵn chạy trước audit dùng key. Không secret mới, không GSM/SSH/root/socket trong runner. Hai runner giữ 1 CPU, 1,5 GiB RAM, MemorySwap=Memory (không thêm swap), online/idle. C3.0 vẫn phải tách audit có secret khỏi lane nhận PR trước khi mở worker; RUN này chưa triển khai C3.0.

Mọi CI/audit mới do RUN này gọi chạy trên self-hosted, không tạo job GitHub-hosted mới. So sánh đo được: ops hosted cũ bị hủy sau 605 giây so main VPS mới 20 giây; lifecycle hosted cũ 24 giây so VPS 39 giây. Đây là số từng job, không phải dự báo tiết kiệm cả tháng. Web Health chưa chuyển nên còn dùng hạn mức hosted. Ngân sách $0/Stop không thay; mức 1.348 phút và net $0 là **snapshot P61 12:32Z**, không giả thành phép đo billing mới.

## Bảo vệ, rollback, dọn dẹp và bàn giao

- Footprint bảo vệ cuối RUN: cấu hình công cụ deploy. Bản trước thay đổi SHA256 `9c22eb89adc90a16259017a4c80d56c6f1cbf560788ab8fd708723ebfd4a944f`; bản cuối `b3563a16cfbbb90a2229fe6aae2bc5e2eb8708e9328ecad20c4bedcf4ce69167`. Script P61 nguyên vẹn. Runtime/profile Web đã hoàn nguyên; nguồn ứng dụng tại VPS không sửa.
- Config Guard thật CLEAN; fixture của chính detector bắt thay nội dung và thiếu file, phục hồi CLEAN. Helper rollback riêng RUN chỉ khôi phục config qua apply-v0, mặc định dry-run; đã kiểm backup/hash và điều kiện ứng dụng đang old. Đây là lùi metadata, không tạo đường deploy thứ hai. Thời hạn deploy của RUN đã đóng lúc 17:29:53Z; phép thử LEASE_EXPIRED bị chặn trước mutation, bộ đếm restart vẫn 2.
- POST cuối 17:31:54Z **25/25 PASS**, footprint/coverage 1/1; #11 = PREEXISTING_SAME. Hai POST trước được giữ nguyên: lần đầu thiếu run_id của proof (đã bổ sung), sau đó coverage đạt nhưng #11 heartbeat khác PRE; không sửa Guard hoặc đèn #11. POST cuối chạy trên cấu hình đã đóng lease và #11 trở lại trạng thái nợ trước RUN. SHA256 POST cuối `914826ec7642ce6cca238d00fc4a5c1919448ed9498796e0d822aaba565afa44`.
- Đã dọn đúng hai thư mục build tạm của RUN; 0 container thử còn lại. Giữ candidate, known-good, log và manifest riêng. Đĩa sau dọn 65%, còn khoảng 36,5 GB; RAM khả dụng khoảng 4,7 GB. Swap toàn máy gần đầy là trạng thái kế thừa; runner không được thêm swap.
- Không tạo key, đổi quyền/IAM, sửa DB/PG/Qdrant/Directus/nginx config, archive thêm repo, mua Pro hay mở C3/C2/C4. Không đụng N2 Dot.
- Bằng chứng riêng trên VPS theo thư mục RUN gồm `web-parity-final.json`, `web-rehearsal.json`, `manifest-completion.json`, `ad-image-config-parity.json`, `ad-canary.json`, `control-proof.json`, `final-host-state.json`, POST và log CI/audit. Chỉ báo cáo đã lược thông tin được ghi lên workspace public. Manifest riêng gồm **96 tệp**, SHA256 **`76292db27f083dc94a24a2eaf65afd121f218bf476d04e653c1c5387903292d3`**, chốt 17:33:15Z.

**NEXT_TRIGGER:** GPT Host/Claude nghiệm thu riêng phần Web và hai audit; quyết định quyền canary bootstrap AD cùng xử lý lỗi Web Health trong phạm vi tiếp theo. Muốn tiếp tục áp VPS phải có lệnh hợp lệ và kiểm lại READY/cờ/runtime. Không chờ giữ máy, không tự tạo RUN mới. **C1B_SCOPED=FAIL (thiếu AD R4 và audit thứ ba); phần Web/coverage đã đạt được giữ nguyên.**
