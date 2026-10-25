# PROMPT — GHM C1A · ĐÓNG S3 TRÊN BẰNG CHỨNG ĐÃ CÓ (KHÔNG CHẠY LẠI CI)
RUN_ID: GHM-C1A-S3-CLOSE-20261025-01
STATUS: DRAFT_NOT_READY — KHÔNG RUN. Claude Reviewer đọc P35/P36 + PROMPT này, chỉ rà 2 điểm swap/Guard và ký ACCEPT đúng last-touch SHA; GPT Host READY cùng SHA; Owner giao **CODEX** chạy. Giữ lịch sử P35 KQ DỪNG. Không dùng lại RUN_ID đã kết thúc.

**EXECUTOR: Codex CLI/Desktop trên Mac** · GitHub read-only đối chiếu 2 CI cũ, VPS qua quyền đã cấp + cờ VPS-GHI cho thay đổi đúng runner/INV25; `workspace_*` root=workspace chỉ ghi STARTED/KQ/Bảng. Claude Reviewer độc lập; không giao Claude thực thi thay Codex.

**Mục tiêu DUY NHẤT:** Hoàn tất nghiệm thu bảo vệ C1A sau khi **đã có 2/2 GitHub CI GREEN** trên runner VPS. Không cài lại runner, không clone/push mã, không chạy lại 6/6 và 16/16 test vì riêng vấn đề POST. Chỉ sửa nếu có bằng chứng drift thực trong runner/cgroup/Guard do chính C1A sở hữu.

**Biên nhận CI đã khóa:** Agent Data https://github.com/Huyen1974/agent-data-test/actions/runs/40199854696 attempt 3, SHA eeb357de688e161c1fe575fdff626351a7b891a6 (6/6); Web https://github.com/Huyen1974/web-test/actions/runs/40200962649, SHA b6f1ab84505867f95aba8131beb235516c31e422 (16/16). GitHub đã xác nhận hai run completed/success. Hai runner đang giữ, repo PRIVATE, `main` và app runtime không đổi theo P35.

**ENTRY:** AGENTS.md root (A5/A6, DROOT30/31/48/56) → root COLLAB cờ VPS-GHI / các RUN khác → work/github-management/COLLAB P32–P36 → C1A-RESUME-REPORT.md + báo cáo PRIVATE P35 đúng SHA/hash → PROMPT này. Đừng lặp R0/R1, quay lại P27 token, triển khai C1B hoặc kéo lại test cũ.

## S0 — KHÓA ĐÚNG ĐẦU VÀO, READ-ONLY TRƯỚC GHI
- Đối chiếu đúng P35: POST 23/25; C3.footprint_coverage và C3.same_or_better FAIL; footprint 87 mục (7 runner/CI có chứng cứ, 80 mục chưa đủ coverage gồm tệp dùng chung và tín hiệu giám sát từ RUN xen kẽ); sai lệch **live cgroup** `memory.swap.max=max` đã từng có ở cả hai runner, hiện báo về `0`. PRE gốc và mốc giờ từ P32/P35 là baseline cố định; **không làm PRE mới thay baseline cũ để tô xanh**.
- Đọc bằng chứng private P35 chỉ đúng các tệp Guard POST, coverage, audit RUN khác `CONN-REPAIR-20261025-02` và dữ liệu cgroup. Với 80 mục không đủ coverage, phân loại `C1A_OWNED | OTHER_RUN_PROVEN | UNKNOWN` bằng commit/mtime/hash/owner/bằng chứng, KHÔNG mặc định mọi mục đều ngoài C1A. Không in credential, đường dẫn hay cấu hình nhạy cảm lên repo public.
- Kiểm tra cờ VPS-GHI/HEAD/PROMPT/STOP hiện hành, không có writer khác đang sửa cùng Docker/Config Guard, trạng thái hai runner và các app, Config Guard và các đèn. Nếu đang có xung đột chủ quyền ghi thì **dừng mutation**, ghi đúng bằng chứng xung đột, không chờ giữ cờ hoặc lén ghi chồng. Khác SHA/runtime mới với hai job CI đã duyệt thì nói rõ; không nhận thử cũ cho runtime bị thay đổi.

## S1 — ĐÓNG ĐÚNG LỖ GIỚI HẠN SWAP CỦA RUNNER
- Trên **cả hai runner đang chạy**, lấy Docker inspect (Memory/MemorySwap/NanoCpus/cpu quota), container PID/ID và cgroup v2 **live**: `memory.max`, `memory.swap.max`, `memory.swap.current`, `cpu.max`; không dùng giá trị khai báo trong Docker thay cho kernel. Mỗi runner phải giới hạn RAM ≤1536 MiB, CPU ≤1, `memory.swap.max=0`, tổng hai runner ≤3GiB/2CPU và chỉ một job nặng tại một thời điểm.
- Docker Docs: đặt `--memory-swap` = `--memory` mới tương ứng **không có swap**; `memory.swap.max=max` là sai rào chắn, dù Docker inspect đã khai đúng. Phải kiểm việc giới hạn đang hiệu lực khi runner idle, trong một phép thử tài nguyên **nhẹ** và sau khi runner được tạo lại đúng script nếu thật sự cần. Không dùng OOM stress test/full build để ép swap; không reboot VPS và không rerun hai CI xanh.
- Nếu live limit lệch hoặc chưa có canh: **ngừng nhận job ở runner liên quan trước**, sửa ĐÚNG script runner/nguồn cấu hình C1A và mở rộng checker **INV25 đang có** để đọc cgroup live (không tạo poller/monitor mới). Checker phải báo FAIL khi `memory.swap.max` không bằng `0`, hoặc CPU/RAM vượt chính sách; ca âm/dương trên fixture hoặc container clone an toàn, không phá live. Sau sửa cần đối chiếu lại Config Guard/code-ledger và kiểm runner ONLINE, app cũ không đổi. Nếu không xác định được vì sao giá trị `max` đã xuất hiện, ghi **ROOT_CAUSE_UNKNOWN** (không dựng kết luận giả), nhưng bắt buộc chứng minh rào chắn live hiện đúng và sẽ bị Guard bắt đỏ khi tái diễn.

## S2 — TÁCH COVERAGE C1A KHỎI DELTA CỦA RUN KHÁC
- Kiểm mỗi mục runner/CI C1A đã thay trong P32–P35 được ghi đủ footprint 4 ô (trước/sau/kiểm/rollback), Config Guard/code-ledger/INV25/Kuma; đủ `C1A_SCOPE_COVERAGE=PASS` khi có bằng chứng thật. Nếu thiếu mục C1A, bổ sung đúng mục đó theo Điều 30/31 qua đường apply hiện có; không đổi baseline chung để cho qua.
- Các tệp dùng chung/đèn của `CONN-REPAIR-20261025-02` hoặc RUN khác: **không tự thêm vào phạm vi C1A**, không rollback cả registry/Guard, không tạo coverage thay chủ sở hữu. Phải chỉ ra bằng chứng actor/commit/hash và người chịu trách nhiệm từng nhóm, trả họ `80 mục chưa đủ coverage` hoặc phần UNKNOWN với receipt cụ thể. Nếu dấu vết cho thấy RUN khác ghi trong lúc Codex giữ VPS-GHI, ghi **CONCURRENT_WRITE_CONFLICT** với khoảng thời gian và chủ, thông báo Owner/Host; không âm thầm hợp thức hóa.
- Với #11 (Disk Usage), #22 (Guard cache), #26 (Claude↔KB) báo RED trong POST P35: kiểm nguồn/nhịp ở mức đủ kết luận `C1A_CAUSED | OTHER_RUN_PROVEN | UNKNOWN`. Không tự xử lý dịch vụ khác, không đổi câu thông báo để làm sạch. Lấy một POST mới theo snapshot hiện tại và so với PRE P32/P35 đã đóng băng; báo riêng `GLOBAL_GUARD` thay vì gọi 23/25 là PASS.

## S3 — POST KHÉP C1A, GIỮ HAI RUNNER
- Chỉ `C1A_S3_SCOPED=PASS` khi đồng thời có (a) hai GitHub CI cũ success cùng SHA/source/runner image chưa bị thay vật chất, (b) kernel cgroup live **no-swap/CPU/RAM đúng** ở hai runner, checker hiện có bắt sai lệch, (c) các thay đổi C1A có footprint đủ và Guard chức năng C1A PASS, (d) không có RED mới quy nguyên nhân cho C1A, (e) runner online/restart policy phục hồi như P35, ứng dụng VPS và `main` không đổi.
- Nếu các hạng mục chung khác vẫn đỏ nhưng được **chứng minh độc lập là không thuộc C1A**, ghi `C1A_S3_SCOPED=PASS · GLOBAL_GUARD=PARTIAL`, bảng nợ bằng chứng/Owner đúng việc; không ghi GLOBAL PASS, không tự đóng cảnh báo còn mở. Nếu còn dấu hiệu C1A gây lỗi hoặc 80 mục chưa phân định được thì **KQ DỪNG** với một blocker và NEXT_TRIGGER chính xác, giữ CI/runner đã đạt.
- KQ@GHM-C1A-S3-CLOSE-20261025-01 XONG|DỪNG + Bảng/README/ROADMAP cùng commit, bản private lưu PRE/POST, cgroup live/probe và danh sách attribution; trong repo public chỉ số đếm và kết luận. **KQ XONG (scoped) không tự cấp GO C1B**: Host/Reviewer đọc KQ rồi quyết có thể đi tiếp hay phải xử lý nợ liên quan. Trả VPS-GHI, dọn sampler, không chạy nền chờ.
- Cấm: sửa main/PR/source của hai repo, full CI rerun nếu nguồn/môi trường không đổi; tự bật deploy/workflow cũ, sửa Docker daemon/PG/Qdrant/Directus/Nuxt/Agent Data/nginx, reboot VPS, xóa secret, đổi Guard baseline hàng loạt, tự nhận quyền của CONN-REPAIR, mở C1B/C2.

STEP_WALK_V1:
| Bước | Executor / trigger | Hạn tham chiếu | Evidence | Lỗi / next |
| S0 | Codex / Owner RUN | ≤15 phút | P35 private, owner map, cờ/Git state | scope/writer conflict⇒DỪNG Host |
| S1 | Codex / S0 PASS | ≤30 phút | live cgroup both + INV25 negative fixture | live drift⇒quarantine đúng runner |
| S2 | Codex / S1 PASS | ≤30 phút | C1A coverage 4 ô + external attribution | C1A thiếu proof⇒sửa đúng mục; UNKNOWN⇒DỪNG |
| S3 | Codex / S2 PASS | ≤15 phút | POST scoped/global, receipt + KQ | Host/Reviewer nghiệm thu |
