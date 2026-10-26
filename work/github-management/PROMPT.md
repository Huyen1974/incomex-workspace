# PROMPT — GHM C1A · KHÉP 1 LỖI S3: KHAI BÁO DUNG LƯỢNG 2 VOLUME RUNNER
RUN_ID: GHM-C1A-S3-VOLUMES-20261026-01
STATUS: DRAFT_NOT_READY — DROOT58: CODEX làm C1A hai volumes, Claude P42 đã góp ý kỹ thuật và Host P44/P45 chốt; **chỉ một chữ ký READY@full last-touch SHA của Host hoặc Co-host hợp lệ**, không cần chữ ký Council/Reviewer. Chưa READY vì VPS-GHI có RUN khác gia hạn ở mẫu gần nhất; Host chỉ ký khi cờ thật trống và có thể START. AUTO0 Owner chuyển RUN là dispatch, không ký kỹ thuật lần hai. Chưa STARTED; P39–P40 đã KQ DỪNG.

EXECUTOR_SURFACE: **Codex CLI/Desktop**, quyền GitHub/VPS đã có. WRITE_PATH: chỉ khai báo tài nguyên hai volume runner C1A vào cơ chế storage-registry/storage-watch hiện hành và bằng chứng Guard liên quan trên VPS, qua cờ VPS-GHI/Đ30–31; trong repo chỉ ghi STARTED/KQ/Bảng/roadmap của `work/github-management`. Không giao Claude Code chạy thay. **Không xây thêm monitor/script cron mới.**

ĐÍCH DUY NHẤT: khép C1A S3 thiếu khai báo dung lượng **hai volume dữ liệu runner tổng ~1,93 GiB** theo P40. Đây là thiếu nhãn/canh, KHÔNG phải yêu cầu giải phóng đĩa. Hai self-hosted runner và CI đã đạt được GIỮ NGUYÊN:
- Agent Data: https://github.com/Huyen1974/agent-data-test/actions/runs/40199854696 · 6/6 PASS · SHA eeb357de688e161c1fe575fdff626351a7b891a6.
- Web: https://github.com/Huyen1974/web-test/actions/runs/40200962649 · 16/16 PASS · SHA b6f1ab84505867f95aba8131beb235516c31e422.
- P40: cgroup live zero-swap/CPU/RAM đúng, INV25 PASS (76/76 fixtures, 5/5, 3/3, 6/6), runner ONLINE, C1A coverage 7 mục riêng + 3 delta dùng chung đã kiểm; GLOBAL_GUARD=PARTIAL do nợ khác. Không chạy lại các phép thử đó nếu nguồn không đổi.

## S0 — XÁC ĐỊNH CHÍNH XÁC HAI VOLUME & CỔNG GHI
1. Đọc AGENTS.md → root COLLAB (DROOT30/31/48, VPS-GHI) → work/github-management COLLAB P35–P44 → báo cáo private P40 **đúng SHA + manifest** → `runner/README.md`/`runnerctl.sh` để xác định **đúng 2 data volumes được P40 nêu**; không đo/đụng toàn Docker. Kiểm volume khóa dùng chung có đang được khai báo riêng hay không, chỉ báo nếu thuộc nợ khác.
2. Đọc **chỉ** contract và các dòng có liên quan của `/opt/incomex/scripts/storage-registry.tsv`, cơ chế `storage-watch`/#11, Config Guard/code-ledger và đường apply-v0 hiện hữu. Đối chiếu path Docker volume thực tế, owner, vòng đời persistent, phân loại được hệ thống hỗ trợ. Dùng kích thước live từng volume và tổng; không dump nội dung volume (chứa credential runner). Lấy số tăng theo lịch sử sẵn có nếu có, không bịa trend/cap. Không suy từ 1,93 GiB là lỗi đầy đĩa.
3. PRE: chụp đúng bản registry + baseline/guard hash, trạng thái #11, health app/runner, giới hạn swap/cgroup đã đạt. Kiểm VPS-GHI trống, không actor khác ghi cùng storage-registry/Config Guard; lấy cờ CAS và kiểm freshness trước first mutation. Nếu bận, DỪNG không ghi chồng. Không dùng PRE mới thay PRE gốc P35/P40 để tô xanh sai.

## S1 — KHAI BÁO 2 VOLUME BẰNG CƠ CHẾ HIỆN CÓ
1. Thêm/sửa **chính xác 2 dòng có định danh volume thực đo** vào storage-registry (hoặc đúng entrypoint tương đương nếu file đó đã quy định cho named Docker volumes), không khai khái quát cả `/var/lib/docker`. Bắt buộc có owner C1A/GHM, loại RUNTIME_STATE/persistent phù hợp schema, nguồn đo dung lượng, đơn vị, ngưỡng/cap theo **công thức có sẵn**; nếu chưa có số tăng 24h thì dùng fallback **đã được policy hiện hữu cho phép** và ghi bằng chứng, không tự đặt trần vô căn cứ. Dòng sâu nhất thắng nếu contract hỗ trợ; không đổi dòng cha/đích khác.
2. Hai volume chứa dữ liệu runner cần giữ. **KHÔNG xóa, prune, truncate, di chuyển, tự gia hạn credential, tạo luật tự dọn/xoay volume.** Chỉ sử dụng tính năng canh/cảnh báo hoặc ràng buộc tăng trưởng sẵn có. Nếu policy đòi valve mà không có cơ chế dọn được duyệt, chọn đúng mode `MONITORED/STATIC` tương thích (nếu có) thay vì dựng van giả; không tự chế class hoặc script.
3. Sửa qua Config Guard/apply-v0/luồng đăng ký sẵn có, snapshot .truoc và bốn ô trước/sau/kiểm/lùi cho phần C1A. Không sửa Guard nguồn chung của RUN khác nếu không cần; không reset baseline, đổi ngưỡng #11, restart runner/app, hay thay chương trình storage-watch.

## S2 — KIỂM CHỨNG THẬT, KHÔNG TÔ XANH GIẢ
1. Kiểm schema registry/Guard, chạy chế độ check **hiện có** của storage-watch và Guard. Phải chứng minh cả hai volume khớp đúng entry, dung lượng live được đọc và có cảnh báo khi vượt cap hoặc biến mất. Phép thử âm chỉ trên **fixture/bản sao registry** đã cô lập, không làm đầy volume thật; đối chiếu không có false PASS, trạng thái thật không bị thay.
2. Đối chiếu P40: hai runner vẫn ONLINE/idle; kernel `memory.swap.max=0`, CPU/RAM như trước; 2 GitHub jobs vẫn `success`, SHA không đổi; các ứng dụng VPS/HEAD/main không thay; INV25/Config Guard hợp lệ. Đo/ghi chiều tăng dung lượng bằng số liệu thật, không bắt buộc phát sinh 24h tăng giả.
3. Phân biệt `C1A_STORAGE=PASS|FAIL`, `C1A_S3_SCOPED=PASS|FAIL` và `GLOBAL_GUARD=PASS|PARTIAL`. RED/nợ ngoài C1A ở P40 đã bàn giao thì giữ đúng chủ, không đưa vào blocker C1A; **nếu lỗi từ chính khai báo volume/C1A** còn thì DỪNG đúng 1 blocker và giữ thành quả.

## S3 — ĐÓNG C1A VÀ BÀN GIAO C1B
- KQ@GHM-C1A-S3-VOLUMES-20261026-01 XONG|DỪNG, bảng + roadmap/README cùng commit, bằng chứng private (hash, registry before/after, cap/size, canary, Guard POST), trả VPS-GHI và dọn sampler. Chỉ ghi C1A **XONG theo scope** khi 2 volume được canh thật, Guard scoped đạt, runner/CI không xấu, 0 lỗi mới của C1A. Có thể GLOBAL_GUARD=PARTIAL vì việc khác, nhưng tuyệt đối không báo toàn hệ xanh giả.
- Nếu scoped XONG: NEXT_TRIGGER=HOST_ACCEPT_C1A_AND_PREPARE_C1B_CLAUDE_CODE; **không tự chạy C1B**, không bật deploy cũ, không mua Pro. Nếu DỪNG: nêu đúng 1 blocker, đường Owner/Host giải quyết, không mở khảo sát lại R0/R1/swap/test.
- CẤM: xóa/chạm nội dung volume/credential runner, tăng trần toàn VPS, chạy lại CI xanh, sửa `main`/source GitHub, restart app/runner, cài thêm cron/agent/monitor mới, sửa nội dung ngoài 2 volume + registry bảo vệ liên quan, dọn các nợ Guard của RUN khác.

STEP_WALK_V1:
| Bước | Agent/Trigger | Hạn tham chiếu | Evidence | Hỏng/next |
| S0 | Codex/Owner RUN | ≤15 phút | P40 private + 2 volumes, PRE/cờ | Bận/sai nguồn→DỪNG Host |
| S1 | Codex/S0 PASS | ≤20 phút | 2 entries/size/cap + apply receipt, rollback | Không đúng policy→DỪNG nguyên trạng |
| S2 | Codex/S1 | ≤20 phút | live storage-watch + fixture negative + Guard | FAIL đúng C1A thì sửa trong scope |
| S3 | Codex/S2 | ≤10 phút | POST scoped/global + KQ/cờ trả | Host nghiệm thu và chuyển C1B |
