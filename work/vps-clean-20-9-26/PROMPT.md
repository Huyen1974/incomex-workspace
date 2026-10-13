# PROMPT — VPSC-HEAL-DISK-MEM-20261013-01 · Chặn nguồn phình đĩa + dọn đủ để #11 xanh thật + nâng trần RAM đã chứng minh

RUN_ID: VPSC-HEAL-DISK-MEM-20261013-01
Task: `work/vps-clean-20-9-26` (VPSC) — **thay N2a cũ** (READY cũ `dc13606`, chưa bao giờ STARTED). Graph P143/P144, PROOT04 và Codex DIAG-20261013 đã chứng minh N2a chỉ gỡ 3/9 lý do #11. Không phải việc mới.
Soạn: Claude Chat theo lệnh Owner trực tiếp 13/10 14:25 +07 (nguyên văn ở P81). Rà soát: GPT Chat (Host VPSC, khác hãng) **một lượt**: được sửa lỗi nhỏ DRAFT (A6) rồi ghi ACCEPT + READY đúng SHA trong cùng commit; vấn đề lớn thì PARTIAL đúng 1 blocker. Owner: «GPT chỉ có ý kiến nếu ok thì chạy luôn cho nhanh.»
Executor: Claude Code CLI, phiên MỚI trên Mac, qua `ssh contabo`. Ghi repo: Incomex MCP `workspace_*` root `workspace`. Sửa cấu hình được bảo vệ: chỉ `incomex-config-apply-v0`.
Status: **DRAFT — chờ GPT ACCEPT+READY**.
Bằng chứng: `/opt/incomex/work/vps-clean-20-9-26/VPSC-HEAL-DISK-MEM-20261013-01/` (chỉ receipt đã làm sạch, không bí mật, không dữ liệu khách). Báo cáo: một mục `HEAL-20261013` trong `BAO-CAO.md` hiện có. Tiến độ + KQ: dưới P81 trong `COLLAB.md` của việc này. Không tạo tệp repo mới. **Chỉ thực hiện phần trên dòng `LỊCH SỬ — N2a cũ`; phần thu gọn bên dưới là bản lưu, KHÔNG thực hiện.**

## 0. Mục tiêu và thế nào là XONG
Owner (D22/D23 + gật Q1–Q5 ngày 13/10): VPS1 sạch, không tái phình, nhanh lại; xoá theo Drive-first trừ ngoại lệ Q1/Q3; không giả xanh.
Ba việc, theo thứ tự ảnh hưởng: (1) **chặn nguồn**: bản chụp trước-sửa (transactions +1,46 GiB/24h, `.before` +0,27), helper queue (+0,25), Git loose objects; (2) **dọn một lần** đủ để SLOPE7D tự hết; (3) **nâng trần RAM đã chứng minh**: claude-mcp chạm 1 GiB 67.256 lần + swap riêng đầy; Postgres chạm 2 GiB 45.123 lần.
**XONG khi đủ cả 8 (đo thật, ghi số):**
1. Kuma #11 xanh, lý do do storage-watch tính lại sau RUN (không đổi ngưỡng/hạn/kind để né).
2. Đĩa trống ≥ max(41 GiB; mốc `df-bytes.tsv` 7 ngày trước − 2 GiB).
3. Van A1–A4 nằm trong `vps-retention.sh`, mỗi van có receipt một lượt chạy thật + bytes trước/sau; 3 dòng CONTROL_DEBT sang ROTATING đúng luật §3.
4. Protection Guard POST `--coverage`: không đích nào mới đỏ so với PRE_RED_SET; mọi tệp đã sửa đều MATCH qua apply-v0.
5. 22 đèn: không đèn nào mới đỏ so với PRE.
6. claude-mcp: memory.current <80% trần mới, swap riêng không đầy; Postgres: bộ đếm `max` trong `memory.events` tăng 0 trong 10 phút sau khi đổi.
7. Độ trễ công cụ thật p50 (10 lần) ≤150 ms, hoặc nhanh hơn PRE ≥50% — ghi cả hai số.
8. PG, Qdrant, Directus, Nuxt, agent-data, Neo4j Graph khoẻ (health 200/healthy); thư mục dữ liệu PG/Qdrant/Neo4j không mất byte nào.
Thiếu một điều ⇒ KQ DỪNG với đúng một blocker nhỏ nhất; phần đã làm giữ nguyên nếu an toàn; không nới ngưỡng. Sau RUN, watcher hiện có tự đo 24h; không ai ngồi chờ. Mốc 24h (tăng ≤0,5 GiB/ngày, transactions ≤ ~3 GiB, claude-mcp phẳng) do Host đọc ở phiên sau.

## 0A. Quyền Owner — khối Owner dán PHẢI có nguyên dòng này
Owner gật Q1–Q5 (Graph P144, 13/10/2026): Q1 bản chụp trước-sửa đã có trong Git giữ 48 giờ rồi xoá, không qua Drive; Q2 dọn D03 D04 D07 D12 D14 D15; Q3 image cũ agent-data và claude-mcp giữ bản đang chạy + 2 bản trước + bản rollback còn trỏ, xoá phần còn lại, không qua Drive; Q4 dừng tmux «agents»/htop 22/05 và 2 Nuxt mồ côi 20/08; Q5 nâng trần RAM claude-mcp 1→1,5 GiB, Postgres 2→3 GiB; mọi xoá khác theo D23 Drive-first.

Quyền này cấp một lần cho đúng phạm vi trên và cho các lượt định kỳ của van A1–A4. Thiếu dòng này, hoặc thiếu GPT ACCEPT+READY đúng SHA PROMPT hiện tại ⇒ DỪNG trước STARTED. (D13 build cache không dọn vì D10 cấm `docker builder`.)

## 1. Luật cứng (phạm ⇒ dừng bước đó, giữ nguyên, ghi blocker)
- **Một lượt ghi VPS (DROOT54 d):** giữ dòng `VPS-GHI` của COLLAB gốc từ trước thay đổi đầu tiên tới KQ; dòng không trống ⇒ `KQ DỪNG · VPS_BẬN`, không chờ. Cờ STARTED chỉ chạy trên Mac (HJW P313) không chặn.
- **Báo từng bước (DROOT54 a):** hết mỗi bước một dòng `<RUN_ID> · bước k/7 · <xong gì, số> · <UTC> · dự kiến xong <UTC>` dưới P81.
- **KHÔNG ĐƯỢC:** Git gc/prune/reflog expire hay sửa ref; Docker prune hàng loạt (system/image/volume/container) và lệnh builder/buildx (D10); gỡ image cưỡng bức; xoá theo wildcard không có danh sách chính xác; VACUUM/truncate/xoá DB, queue, audit; chạm thư mục dữ liệu PG/Qdrant/Neo4j, transaction log Neo4j, `/var/lib/hermes`, tệp Graph (`/opt/incomex/work/graph-server/**`), mã agent-data (#22 đang chờ TQT P41); sửa `storage-watch.py`; đổi ngưỡng/hạn/kind để lấy xanh; tạo lịch/timer/cron mới; tắt healthcheck/monitor; khởi động lại dịch vụ ngoài bước D.
- **Bí mật:** không in env/.env/token/khoá; tìm chuỗi chỉ in tên tệp; log chỉ đếm; không đưa dữ liệu khách/queue thô vào Git.
- **Cấu hình được bảo vệ** chỉ qua `incomex-config-apply-v0 --target-id <id> --expected-baseline <baseline hiện tại>` + rollback `.pre`; tệp không thuộc registry thì giữ bản `.pre` cạnh tệp + receipt sha256 trước/sau. Đích đang DRIFT ⇒ không đụng, ghi blocker.
- **Nghi ngờ thì giữ:** mọi mục không chứng minh được thì giữ, ghi lý do, làm tiếp phần độc lập.
- Ngân sách ≤2 giờ; quá ⇒ dừng ở ranh giới bước, KQ DỪNG kèm phần đã xong.

## 2. S0 — đọc + chụp PRE (chỉ đọc)
1. Đọc `AGENTS.md` → COLLAB gốc (DROOT54, `VPS-GHI`) → VPSC COLLAB §0 + P81 → PROMPT này → Graph COLLAB P144 → VPSC `BAO-CAO.md` DIAG-20261013 §2–§4 → COLLAB gốc PROOT04 ①–⑨. Xác minh GPT ACCEPT+READY đúng SHA PROMPT hiện tại và khối Owner có dòng §0A.
2. Sàn tài nguyên: MemAvailable ≥3 GiB, đĩa trống ≥20 GiB, không có build/apply/backup/restore đang chạy.
3. PRE (ghi vào thư mục bằng chứng): `df -B1 /`; faults trong `/var/lib/incomex/disk-watch/state.json` + dòng DISKWATCH mới nhất; mốc 7 ngày từ `df-bytes.tsv`; `/opt/incomex/logs/bang-den.json`; Guard PRE `--coverage` + drift-check (PRE_RED_SET dự kiến 4 đích: `agent_data/lifecycle.py`, `workspace_tools.py`, `hvu_signals.py`, Hermes `config.yaml`); cgroup claude-mcp và postgres: memory.current/max, memory.swap.current/max, memory.events; bằng chứng phiên MCP (đếm log tạo/đóng phiên 24h trong container claude-mcp, số kết nối ESTABLISHED tới cổng dịch vụ); độ trễ p50 10 lần một công cụ đọc nhẹ qua MCP mà phiên có (ưu tiên `fs_list` Incomex VPS, không thì `workspace_stat` Agent Data).
4. Giữ khoá: đổi `VPS-GHI: trống` → `VPS-GHI: VPSC-HEAL-DISK-MEM-20261013-01 · VPSC · từ <UTC> · dự kiến <UTC+2h>` và ghi dòng STARTED của RUN_ID này dưới P81, có expected_version, trước thay đổi đầu tiên.

## 3. Bước A — van chặn nguồn (lâu dài, trong `vps-retention.sh`)
Trước hết đọc mã đang chạy trong container (không chỉ nguồn host): `workspace_operations.py` (ghi bản chụp dòng 353–356, thao tác `restore`, tra `operation_id`), GC trong `workspace_runtime.py`, mã khôi phục lúc khởi động, chỗ ghi `.before`. Nếu đường nào đọc tệp số của giao dịch đã committed/applied ⇒ KHÔNG làm A1, ghi blocker. Ghi kết luận vào bằng chứng.
- **A1 transactions** (`/opt/incomex/data/workspace-tools/transactions/<tid>/`): chỉ xét `manifest.json` có status committed, applied hoặc rolled_back, cũ hơn 48 giờ, không có khoá/lease/job đang chạy. Với từng tệp bản chụp số `0`, `1`, …: tính blob id bằng `git hash-object` rồi kiểm blob đó có trong repo của root tương ứng bằng `git cat-file -e` (root workspace = bản clone Git mà agent-data dùng; root ui = Git cục bộ của xưởng UI). **Mọi** tệp bản chụp của giao dịch đều có trong Git ⇒ bỏ các tệp số đó (Q1), **giữ `manifest.json`**. Có tệp không có trong Git (vd `operator-preserved-after.json`) ⇒ giữ cả giao dịch; cũ hơn 14 ngày thì đi đường Drive-first §5. Không bao giờ đụng prepared, push_unknown, rollback_conflict hoặc trạng thái không rõ.
- **A2 `.before`** (tệp chụp đơn ở gốc `/opt/incomex/data/workspace-tools/` và nơi mã chỉ ra): cũ hơn 48 giờ và blob có trong một repo Git đã biết ⇒ bỏ (Q1); không chứng minh được ⇒ giữ.
- **A3 helper** (`/var/lib/incomex-mcp-helper`): `queue/out/*.json`, `queue/done` đã xong, snapshot P02 đã bị thay (không phải current/previous/pin), cũ hơn 7 ngày, không pending/running/error, hết tham chiếu ⇒ Drive-first §5 rồi bỏ. Giữ `queue/in` và trạng thái hiện hành.
- **A4 Git loose objects:** `/opt/incomex/mcp-roots/gh`, bản clone Git của workspace-tools (`github-workspace`), 2 mirror P02 (agent-data và helper; đường dẫn lấy từ `p02_snapshot.py`/cấu hình). Mỗi repo: không có tiến trình git đang chạy trên repo đó; `git fsck` trước; đếm refs; `git repack -d -q` (không `-a`, không gc/prune); sau đó `git fsck` sạch và refs y nguyên. Lỗi ⇒ dừng repo đó.
- **Cài van:** thêm A1–A4 thành luật mới trong `/opt/incomex/scripts/vps-retention.sh` (chạy theo cron sẵn có, luật hằng ngày như (k)), qua apply-v0 + rollback; chạy chế độ chỉ in danh sách + sha256 trước, rồi một lượt thật ngay. Không sửa `/etc/cron.d/vps-retention`. Chạy lại chế độ thử của các luật cũ để chứng minh không hồi quy.
- **Registry** (`/opt/incomex/scripts/storage-registry.tsv`, qua apply-v0): chỉ sau receipt lượt thật, đổi 3 dòng CONTROL_DEBT (transactions, helper, mcp-roots) sang ROTATING kèm trường van cron trỏ `vps-retention.sh`, trường tệp trỏ mã luật, và trần bằng (thời hạn giữ × dòng vào 24h đo được) × 1,3 — ghi công thức và số (cú pháp theo đúng các dòng ROTATING đang có và `storage-watch.py` dòng 412–417). Nguồn đang tăng chưa có tên thuộc việc khác (PROOT04: `/var/lib` → hjw-control +178 MiB/24h, chủ HJW): thêm một dòng riêng kind CONTROL_DEBT, owner HJW, hạn ngày 16/10/2026 01:00 UTC, lý do một câu — không lập van hộ HJW. Nguồn lạ khác >128 MiB/24h: ghi blocker, không tự phân loại.

## 4. Bước B — dọn một lần (Q2, Q3)
- **B1 image (Q2: D03 D04 D07; Q3: D01 D11):** kê mọi image (ID, tag, RepoDigests, ngày tạo, cỡ riêng). Tập GIỮ = image của mọi container (kể cả đang dừng) + chuỗi cha + 2 bản trước của mỗi repository (luật R03) + image agent-data-hvu tag mcpw-r2-20261001 (đường lùi PROOT03) + mọi tag/ID được nhắc trong compose/rollback/script dưới `/opt/incomex/{docker,claude-mcp,scripts,dot}` và `/opt/incomex/work/graph-server/prod-v1` (tìm bằng grep chỉ in tên tệp) + mọi image Graph/Neo4j/gs-*. Gỡ phần còn lại thuộc D01, D03, D04, D07, D11 bằng lệnh gỡ image thường theo ID (Docker từ chối thì giữ). Ghi RepoDigests của D03/D04 trước để kéo lại được. Đo `df` trước/sau (không tin số reclaimable của docker).
- **B2 staging TQT (D12):** `/opt/incomex/staging/tqt-p32`, `tqt-p33`, `tqt-p36` ⇒ Drive-first §5 ⇒ bỏ đúng 3 thư mục.
- **B3 tạm cũ (D14):** phần thử cũ trong `/var/tmp/jev-gate` và mục trong `/tmp` cũ hơn 7 ngày, không tiến trình nào giữ (`fuser`), không phải socket, không phải `tmux-*`, `systemd-private-*`, hay `lark-gpg-home-*` còn gpg-agent sống ⇒ gom một gói Drive-first §5 ⇒ bỏ đúng danh sách.
- **B4 (D15):** gỡ container Created `workspace-job-0ae7…` (không cưỡng bức). 5 volume treo: volume thuộc project compose của dịch vụ đang chạy ⇒ giữ; còn lại ⇒ tar Drive-first §5 ⇒ gỡ đúng tên volume.
- **Giữ nguyên:** D02 Hermes, D05 Graph, D08 backup-staging, D09 `/root` (chưa rõ chủ), D13 build cache (D10), dữ liệu PG/Qdrant/Neo4j.

<!-- PHẦN-2B: §5–§10 -->

---

<details><summary>LỊCH SỬ — N2a cũ VPSC-N2A-DISK11-CONTROLS-20261011-01 (READY dc13606, chưa chạy, đã thay ngày 13/10) — KHÔNG THỰC HIỆN</summary>

# (Lịch sử) PROMPT — VPSC-N2A-DISK11-CONTROLS-20261011-01 · THREE CONTROL_DEBT #11 HOTFIX (SCOPE N2a)

RUN_ID: VPSC-N2A-DISK11-CONTROLS-20261011-01
Task: `work/vps-clean-20-9-26` (VPSC) · D22/roadmap N2a, **not a new task**.
Executor: Claude Code CLI (new session), Owner manually pastes after **Claude Reviewer exact ACCEPT + GPT Host READY same SHA**.
Repo_Write_Path: existing Incomex MCP `workspace_*`, root=`workspace`; VPS config/runtime via already accepted native paths and `incomex-config-apply-v0` only.
Status: **DRAFT · D23 OWNER DRIVE-FIRST supersedes P76/P77 old PROMPT @d4eeb15 · P79 Claude Reviewer sửa nhỏ §0B (đường thử khôi phục + đích Drive) + ACCEPT đúng SHA bản này · NO READY/RUN**.
Evidence: reuse `/opt/incomex/work/vps-clean-20-9-26/` under a run-scoped subdir; report one section under existing `BAO-CAO.md` and KQ in task `COLLAB.md`. Never create duplicate repo files as progress notes.

## 0. GOAL — CLEAR THE *ACTUAL* BLOCKER, NO SCOPE CREEP
Owner has directed priority to complete Graph R10 promptly; the sole known hard execution gate is **Kuma #11 Disk Usage RED** caused by three VPSC `CONTROL_DEBT` deadlines 2026-10-11T01:00:00Z (not disk fullness: 11/10 physical free ≈42 GB):
1. `/opt/incomex/data/workspace-tools/transactions`: operation backups, baseline historical +62 MB/day.
2. `/var/lib/incomex-mcp-helper`: queue/out, done and P02 backlog, historical +105 MB/day.
3. `/opt/incomex/mcp-roots/gh` (under `/opt/incomex/mcp-roots`): loose Git objects/ref growth.

**Mục tiêu RUN N2a:** sửa đúng ba nguồn CONTROL_DEBT bằng van giới hạn thật, kiểm chứng Kuma #11 GREEN và Guard POST same-or-better. Không lách bằng nới ngưỡng, đổi hạn debt/kind, đặt cap-only hoặc di chuyển dữ liệu sang thư mục khác cùng ổ.

**Ngoài RUN:** C2 312 UNKNOWN+2 excluded, 3 EVIDENCE_DEBT, D22/N2b để VPSC sau; R7 A/B/C1/C3/D/POST giữ nguyên. Không sửa Graph R10, HJW, ứng dụng agent-data/helper hoặc task đã đóng. Cấm Git prune/reflog expiry, queue truncate, xoá wildcard không có danh sách kiểm chứng, broad wipe hay đổi services/PG/Directus.

## 0A. OWNER DIRECTIVE D23 · CHÍNH SÁCH GIỮ HẠN ĐÃ ĐỒNG Ý CÓ ĐIỀU KIỆN, CHƯA READY
Theo chỉ đạo trực tiếp D23, Owner đã đồng ý dọn an toàn và yêu cầu **Drive-before-delete**. Dòng dưới định danh phạm vi được chấp thuận; PROMPT tự nó không phát RUN. Claude Executor vẫn phải thấy đúng câu trong **khối Owner thực sự dán** (một dòng):
Owner cho VPSC N2a trên VPS1 tái dùng vps-retention.sh và kho Google Drive mã hóa hiện hữu để lưu trước-xóa các bản transactions đã hoàn tất, hết tham chiếu, trên 14 ngày và helper queue/out/*.json, queue/done, p02 snapshot đã hết vai trò, hết tham chiếu, trên 7 ngày; chỉ được xoá sau khi tải bản cứu hộ lên Drive, kiểm hash/readback và thử khôi phục PASS, kiểm lại job/idempotency/rollback/consumer cùng danh sách hash ngay trước xoá; giữ nguyên mọi bản chưa rõ, còn dùng hoặc là bản khôi phục duy nhất chưa chứng minh bản Drive dùng được, không xoá khác và không prune/làm mất lịch sử Git.

Thiếu câu này, thiếu một Claude ACCEPT SHA mới, thiếu Host READY exact SHA, thiếu Guard/no concurrent hoặc archive Drive verify/restore PASS thì DỪNG trước STARTED hoặc trước DELETE. Owner cấp quyền một lần cho đúng policy định kỳ trong phạm vi trên; từng lần tự kiểm refs/hash/fresh receipt, lỗi/UNKNOWN thì KEEP và cảnh báo. Không phải xin Owner mỗi ngày. Không đụng dữ liệu độc nhất cần khôi phục khi chưa có proof offsite/restore.

## 0B. OWNER D23 · DRIVE-FIRST VERIFIABLE CLEANUP
- Người dùng đã duyệt nguyên tắc: **archive lên Google Drive rồi mới DELETE local**, tái dùng đúng backup/retention đang có. VPSC các đợt trước từng thực hiện `tar|gzip|gpg→rclone rescue/vpsc-r3`, MD5 readback rồi xoá và backup mã hóa mỗi đêm; **không giả định backup PG/config hiện đã chứa transactions/helper**. Đây là cổng bổ sung an toàn, không xây hệ backup thứ hai. §0A hiện là policy Owner đã cho phép có điều kiện, nhưng Host chưa READY bản sửa và chỉ Owner dán RUN có nguyên văn câu chính sách mới.
- S0 READ-ONLY chứng minh remote rclone/GPG hiện hữu và restore route, bản backup gần nhất, quota/quyền/hạn giữ rescue; không in token/secret, không mở rộng remote hay cloud project. Đích rescue phải có vòng đời đã kiểm, không bị backup-keeper xoá sớm hơn khi cần khôi phục.
- **Đích Drive (P79, theo mã):** thư mục con mới `rescue/vpsc-n2a/` của đích mã hoá hiện hữu, mã hoá bằng đúng khoá công khai người nhận của `backup-to-gdrive.sh` (kiểm vân tay trước). `backup-to-gdrive.sh` chỉ tỉa `rescue/vpsc-r2|r3|r6` ⇒ thư mục mới không bị xoá sớm. N2a **không xoá gì trên Drive và không sửa `backup-to-gdrive.sh`**; meta mỗi gói ghi `retain_until` = +12 tháng (như r3/r6); KQ báo GB/tháng đổ ra Drive + trần dự kiến; luật tỉa `rescue/vpsc-n2a/` theo khuôn r3/r6 = nợ VPSC lượt sau, phải xong trước `retain_until` sớm nhất. Đây là cách đáp ứng gạch «Drive archive cũng phải có retention» dưới đây, không phải cổng XONG của N2a.
- **Đường thử khôi phục (P79, theo mã):** keyring bền của VPS chỉ có khoá công khai (`backup-to-gdrive.sh`: «can never decrypt») ⇒ không giải mã bằng keyring đó, không đưa khoá riêng vào đĩa bền. Tái dùng đúng chuỗi đã chứng minh của DOT `dot-pg-restore-verify-db` (VPSC R6 C4): khoá riêng phục hồi đi thẳng Secret Manager → `gpg --import` vào GNUPGHOME tmpfs riêng của lượt (0700), không vào biến/argv/log/đĩa bền/Git, agent không xem/chép → đọc ngược đối tượng từ Drive → `gpg -d | tar` đủ số mục/byte theo manifest + extract ít nhất một mẫu mỗi gói vào tmpfs, sha256 = manifest → đối chứng âm (gói cắt cụt phải fail) → xoá sạch tmpfs, keyring gốc còn 0 khoá riêng, residue 0. Áp cho **mọi gói trước DELETE, cả lượt RUN lẫn các lượt cron sau**; thiếu gcloud/Secret Manager/chỗ tmpfs hoặc bước nào lỗi ⇒ chỉ upload, KEEP local, cảnh báo, không xanh giả.
- Với từng tập A/B đủ điều kiện: dry-run danh sách exact path+hash+references→gói nhỏ mã hóa bằng khoá đã xác minh→stream lên Drive bằng cổng cũ→xác minh object/count/size/checksum readback và **thử extract/restore một mẫu không ảnh hưởng production**, hash khớp→recheck trạng thái job/refs, symlink, canonical delete-set ngay trước DELETE. Lỗi upload/hash/restore/remote/retention/refs ⇒ **KEEP local; báo blocker, không xanh giả**. Không tải raw customer/queue ra Git, chỉ receipt sanitized và pointer phục hồi private.
- C Git chỉ repack -d nếu fsck, refs/recovery và bản code-backup/offsite hiện hữu đã chứng minh; không cần copy từng loose object lên Drive khi cùng nội dung reachable đã có trong pack và recovery đã đủ, nhưng thiếu recovery proof thì không repack.
- Không đưa bất kỳ archive/log/queue đã dọn trên Drive vào Graph như một node/cạnh hay bằng chứng nguồn nghiệp vụ; **dọn ổ ≠ xoá/thay thế chân lý Graph**. Drive archive cũng phải có retention, không trở thành nguồn rác vô hạn.
- Thời gian giữ N2a khởi động: transactions >14d, helper >7d. Owner muốn xem xét nhanh hơn; executor **đo ứng viên >7d/>3d** và báo Host sau đợt đầu, nhưng không tự áp giảm hạn trong RUN này khi chưa được chứng minh và ký delta.

## 1. S0 HARD AUTH + LIVE RESOURCE / GUARD
1. Đọc `AGENTS.md` → root `COLLAB.md` → VPSC Bảng, §0, P68–P78/BAO-CAO R7, D23 Drive-first §0A/§0B và một Claude reviewer ACCEPT exact SHA mới, last-touch PROMPT và reviewer/Host exact SHA. Kiểm **không có STARTED active/STOP/COUNCIL_ALERT, no HJW/Graph concurrent mutation**. #11 RED là **đối tượng đang chữa**, không giả vờ PRE 22/22: freeze `PRE_RED_SET` và raw reason, yêu cầu các đèn khác cùng Guard Config CLEAN hoặc có reason và owner minh bạch. Active resource floor: MemAvailable ≥3GiB + disk free ≥20GiB, no active PSI/OOM hazard. Nếu khác mà không giải thích được ⇒ KQ DỪNG sạch. **Do not wait/poll/hold terminal.**
2. Preflight full SHA and root gate before writing. If passed, record `STARTED@VPSC-N2A-DISK11-CONTROLS-20261011-01` + root shared busy atomically in one repo commit before first mutation. Preserve all actual scripts/registry/queue state/baseline hashes, support existing coverage Guard C3 and revocable rollback to PRE. No secret or raw customer data in Git/evidence.
3. Read-only inspect each `CONTROL_DEBT` row in `scripts/storage-registry.tsv`: canonical owner, due, path, cap, source classifier, current bytes/rate and what evidence the detector requires before clearing. Inspect existing `storage-watch.py`, retention scripts/timers, `incomex-config-apply-v0 --help`, and Config Guard protected paths. Freeze **allowed exact footprint matrix**, candidate patches and inverse before mutation. If status RED is a real fault (not just deadline) fix it under the same three source boundaries, not by changing the monitor definition.

## 2. N2a — THREE SOURCE CONTROLS (FOUR FIXES P73)
A · Transactions: chỉ backup completed, quá 14 ngày, chứng minh không còn prepared/push_unknown/rollback_conflict/unknown, queued/running, operation_id/idempotency, audit/rollback/recovery refs. Tuổi không đủ để xóa; UNKNOWN/sole recovery => KEEP. Sau OWNER permission §0A, dry-run exact sorted candidate paths + SHA256/state/ref proof; DRIVE-FIRST upload, readback và restore mẫu PASS theo §0B rồi mới kiểm lại references ngay trước xóa. Không có chứng cứ đủ => nợ vẫn OPEN, KQ DỪNG.

B · Helper: chỉ queue/out/*.json, completed queue/done và p02 snapshot superseded/noncurrent, quá 7 ngày, chứng minh không có pending/running/error, consumer/alert/current pin/P02/audit/recovery refs; queue/in và current state phải giữ. Dry-run exact candidates/hashes, Drive encrypted archive+readback+sample restore PASS §0B rồi mới recheck references, UNKNOWN => KEEP. Không sửa helper/HJW code; no concurrent HJW trước mọi mutation.

C · mcp-roots/gh: git fsck trước/sau; kiểm HEAD, refs/recovery/reflogs/bundles và P02 writer lock, chỉ native git repack -d (không dùng git gc, kể cả --prune=never, vì gc tự chạy reflog expire theo gc.reflogExpire 90d/unreachable 30d) nếu chứng minh tất cả refs/objects phục hồi còn nguyên. Cấm prune/reflog expire/ref rewrite; không đủ bằng chứng => nợ OPEN.

ONE VALVE: dùng lại công cụ hiện có trước. agent-data/helper không có retention cho A/B (P73), nhưng VPSC đã có người gác kho /opt/incomex/scripts/vps-retention.sh (R2–R5b: cron mỗi giờ /etc/cron.d/vps-retention, flock, log /var/log/incomex/vps-retention.log, luật (a)–(l), chế độ chỉ in danh sách + sha256 như --chi-l-thu, LOCKED trong code-ledger, đã là van cron=vps-retention\.sh của 4 dòng sổ). Mặc định: thêm luật A/B/C vào script đó, mỗi ngày một lượt theo giờ UTC như (k), qua incomex-config-apply-v0 + rollback, chạy lại chế độ thử của luật cũ để chứng minh không hồi quy; không sửa /etc/cron.d/vps-retention. Chỉ khi không làm được (ghi lý do đo được) mới tạo đúng một script retention dưới /opt/incomex/scripts/ + một systemd timer (service unit tối thiểu của nó) chạy hằng ngày, gọi A/B/C theo điều kiện an toàn, cài qua incomex-config-apply-v0 và đăng ký Code Ledger/Config Guard/coverage/rollback. Lượt đầu dry-run, test fail-closed với active/unknown/symlink/ref mismatch **và upload/readback/restore Drive lỗi**; rồi mới được thực thi cleanup sau §0B PASS trong quyền §0A. Mỗi lượt timer chạy trong shared lock, có receipt và quan sát actual bytes; có job khác thì SKIP, không sleep/WAIT.

Mọi source phải có PRE/POST bytes/slope, proof reference safety/restore; A/B bổ sung encrypted Drive archive/count/hash/readback/sample restore receipts theo §0B. status INSTALLED_AND_PROVEN|DRY_RUN_ONLY|BLOCKED; move cùng ổ, cap-only hay upload-only không chứng minh dọn đúng.

## 3. #11 REAL GREEN / POST GATE
- Any protected mutation must apply by `incomex-config-apply-v0` with exact target and validated rollback. Do not change registry debt due/status directly to hide `DEBT_OVERDUE`. Registry chỉ được đổi ba CONTROL_DEBT sang ROTATING khi van đã chạy thật có receipt, có proof cleanup/Guard/rollback; valve bắt buộc gồm cap= + phần sống: cron=vps-retention\.sh (kèm file=vps-retention.sh~<mã luật>) nếu dùng cron hiện có, hoặc fresh=<tệp dấu chỉ ghi khi lượt dọn chạy xong>@26 nếu là systemd timer — valve_ok cron= chỉ đọc crontab root + /etc/cron.d (storage-watch.py:412–417), không thấy systemd timer. cap=/file= đứng một mình là xanh giả, cấm. Không sửa storage-watch.py trong N2a; khe valve_ok cho qua cap-only (P73) ghi nợ VPSC lượt sau. Không đổi hạn debt/kind/threshold để né đỏ. If missing control, keep explicit RED/DEBT and explain.
- After each bounded candidate apply, validate source consumers/queue recovery/refs, Config Guard, existing retention paths. POST should be **same-or-better relative to legitimate PRE**: #11 GREEN, other 21 lamps no newly RED, Guard protected footprint exactly approved modifications with coverage, no secret leak. **Cổng XONG gồm ba điều đo thật + GDrive-FIRST bắt buộc:** (i) A/B đã upload Drive mã hóa, hash/readback và restore PASS trước DELETE; mỗi nguồn A/B/C có receipt lượt chạy thật của van + bytes PRE/POST đo được (cap=, file= hay sửa hạn nợ không tính); (ii) Kuma #11 GREEN với lý do mới do storage-watch tính lại; (iii) Protection Guard POST --coverage PASS, không đèn nào mới đỏ so với PRE_RED_SET. If #11 remains RED from these debts, KQ DỪNG, do NOT override it.
- If RED arises from another independent VPSC defect, give one bounded root cause/owner, no scope widening without separate authorization. No nightly/24h terminal wait, no background experiment; existing watcher/Guard monitors steady state after run.

## 4. KQ / SHARE SLOT WITH GRAPH
Report `KQ@VPSC-N2A-DISK11-CONTROLS-20261011-01 XONG|DỪNG` with Drive-first archive/readback/sample restore receipts (A/B) and evidence for each of the 3 debt sources, Config Guard PRE/POST, Kuma #11 final reason, no regressions, actual vs forecast disk and slope, tests, rollback, any unresolved debt and NEXT_TRIGGER. Write VPSC COLLAB (same commit release root busy) and existing BAO-CAO; leave Graph PROMPT/SHA untouched.
- If **XONG and #11 GREEN with Guard proof**, note `NEXT_TRIGGER=GRAPH_R10_HOST_FRESH_PRE_READY_EBF52956...`; host Graph independently does fresh Guard PRE and issues READY at its already signed SHA, then Owner manually pastes R10.
- If **DỪNG**, return exact smallest fix/Owner-only decision, do not ask Owner to run Graph against RED and do not relabel as green.

## 5. STEP WALK
| Phase | Who | Trigger | Proof | Fault |
|---|---|---|---|---|
| S0 | Claude Code | exact REVIEW+HOST READY+Owner pasted RUN | no concurrent + PRE snapshot/resource/protected footprint | KQ DỪNG before mutation |
| A transactions | Claude Code | S0 pass | operation/recovery reference proofs, native control candidate/dry-run | preserve evidence, continue independent sources |
| B helper | Claude Code | A measured | queue/P02 reference/TTL control tests | preserve evidence, continue |
| C gh | Claude Code | B measured | fsck/refs/GC non-destructive validation | preserve refs, no prune |
| POST | Claude Code | A-C accounted | actual control receipts, true #11 GREEN, all other lamps same-or-better | KQ DỪNG or rollback scoped delta |
| KQ | Claude Code | terminal | exact KQ, release root busy, no unapproved writes | next trigger VPSC or Graph R10 |

**DO NOT do C2, Graph, HJW mutation.** Claude P73 đã ký 4 sửa có điều kiện, Host P75 áp 4 sửa, Claude P76 ACCEPT bản cũ d4eeb15; vì Owner D23 thêm gate Drive-first materially nên Reviewer phải ký đúng PROMPT mới một lượt hẹp (được sửa DRAFT theo bằng chứng), rồi Host mới READY sau fresh Guard/shared VPS; không rà lại toàn bộ R7. P79 Claude đã sửa §0B và ACCEPT bản này; Host READY đúng SHA last-touch, không mở thêm vòng review.

</details>
