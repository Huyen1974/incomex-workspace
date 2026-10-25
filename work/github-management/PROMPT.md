# PROMPT — GHM C1 · KHÔI PHỤC CI/CD 2 REPO, MÁY CHẠY ĐẶT TRÊN VPS
RUN_ID: GHM-C1-CICD-VPS-20261025-01
STATUS: DRAFT — Claude soạn theo Owner 25/10 15:18 (COLLAB P22), ký ACCEPT@last-touch; GPT Host đọc TOÀN BỘ rồi READY@cùng SHA; Owner giao Claude Code CLI. Thay `GHM-G0-CICD-VERIFY-20261025-01` và pilot P20 `GHM-R2P-FREE-20261025-01` (cả hai SUPERSEDED_UNRUN, giữ trong lịch sử Git).

Executor: Claude Code CLI chạy root trên VPS, vai KST (kỹ sư trưởng). Lấy cờ VPS-GHI trước mọi ghi; Điều 30/31: mọi thứ làm xong phải kiểm lại và đưa ngay vào bảo vệ trong cùng lượt.
Giấy phép: Owner 25/10 15:18 (COLLAB §0.3) = GO DROOT56 cho đúng việc này — khôi phục CI/CD GitHub↔VPS của `Huyen1974/agent-data-test` và `Huyen1974/web-test` qua các cổng dưới. Không mở rộng sang việc khác.
ENTRY: AGENTS.md root → root COLLAB (cờ VPS-GHI, DROOT56, PROOT08/09) → work/github-management/COLLAB §0 + Bảng + P12/P17/P22 → PROMPT này. Thiếu ACCEPT/READY cùng SHA hoặc Owner RUN ⇒ DỪNG.

**Mục tiêu:** mỗi repo chạy được đường nhánh → PR → test trên VPS → main → deploy trên VPS (kiểm sức khoẻ + tự lùi). GitHub không còn giữ chìa vào VPS: máy chạy (runner chính hãng GitHub, giấy phép MIT) nằm ngay trên VPS, dùng biến/mật khẩu sẵn có tại chỗ.
**Vì sao không bật lại workflow cũ (Claude đọc 25/10):** Web build trên GitHub rồi SSH/rsync ~15 bước, chép đè `docker-compose.yml` + nginx từ repo (bản 03/2026) lên bản đang chạy (22/10), tự chạy SQL; Agent Data rsync `--delete` main 04/2026 đè thư mục mã VPS mới hơn. Bật lại = mất mã/cấu hình.

## A — MÃ NỀN: main = mã trên VPS (≤45′)
- A1 STARTED + cờ VPS-GHI. Đo lại từng thư mục mã `/opt/incomex/docker/agent-data-repo`, `/opt/incomex/docker/nuxt-repo`: nhánh, HEAD, tệp sửa chưa commit, submodule, bản `vps-daily-*` mới nhất; mã đang chạy (image agent-data, `/opt/incomex/deploys/nuxt-output`) dựng từ SHA nào — không rõ ghi UNKNOWN.
- A2 Bản clone KST riêng `/opt/incomex/kst/<repo>` (root, 0700, ngoài tầm Hermes): clone cục bộ từ thư mục mã; phần sửa chưa commit → 1 commit «baseline VPS 2026-10-25» trong bản clone KST (KHÔNG commit/checkout/reset trong thư mục mã đang chạy). Quét bí mật trước khi đẩy; có dấu hiệu ⇒ DỪNG.
- A3 Lấy main cũ qua đường riêng như job sao lưu `git-push-gh-daily-v2.sh` (KHÔNG đổi `origin` sentinel DROOT56, không đụng Config Guard của thư mục mã). Tag `archive/main-20261025` = main cũ; `git merge -s ours` ⇒ main tiến thẳng; đẩy main + tag, KHÔNG force-push.
- A4 Trước khi đẩy: xác nhận mọi workflow deploy cũ đang disabled (P17); cùng commit chuyển 15 workflow BỎ sang `.github/workflows-archive/` (không xoá, không chạy được nữa). Sau khi đẩy: `git diff <baseline> origin/main` chỉ khác thư mục archive; main cũ là tổ tiên; tag có. Ghi SHA đồng bộ vào `/opt/incomex/kst/<repo>.synced`.

## B — MÁY CHẠY TRÊN VPS (≤60′)
- B1 Tải `actions/runner` bản mới nhất từ GitHub releases, kiểm SHA256 chính hãng. Token đăng ký lấy bằng thẻ sẵn có trên VPS (thẻ của job sao lưu nếu đủ quyền) — không in, không lưu. Không thẻ nào đủ quyền ⇒ DỪNG, NEXT_TRIGGER=OWNER_RUNNER_TOKEN (Host soạn sẵn các bước bấm cho Owner).
- B2 Mỗi repo 2 máy chạy:
  - `vps-deploy`: dịch vụ systemd, user `ghrunner` (nhóm docker), thư mục `/opt/incomex/runners/<repo>-deploy`. Cổng: hook trước việc `ACTIONS_RUNNER_HOOK_JOB_STARTED=/opt/incomex/runners/hooks/only-main.sh` (root:root 0755, `ghrunner` không sửa được) — exit 1 trừ khi `GITHUB_REF=refs/heads/main` VÀ `GITHUB_EVENT_NAME` ∈ {push, workflow_dispatch} VÀ `GITHUB_WORKFLOW_REF` = `<owner>/<repo>/.github/workflows/deploy-vps-local.yml@refs/heads/main`. Hook thoát ≠ 0 ⇒ việc không chạy (GitHub Docs).
  - `vps-ci`: chạy trong container (ảnh runner chính hãng), `--ephemeral`, không gắn docker.sock, không gắn thư mục máy chủ, mạng riêng (không vào mạng compose), `--cpus 2 --memory 3g`, mỗi lúc 1 việc.
- B3 Điều 30/31 + giám sát: đăng ký hook, cấu hình runner, `.git/config` bản clone KST vào `code-ledger.tsv` (LOCKED) / Config Guard; Kuma theo dõi các dịch vụ runner; đăng ký các script mới vào bảng công cụ.

## C — WORKFLOW MỚI (≤45′, KST đẩy lên main)
- C1 `ci.yml`: on pull_request + push mọi nhánh, `runs-on: [self-hosted, vps-ci]`. Agent Data: pytest phần không cần DB thật. Web: `pnpm install --frozen-lockfile` + lint/test có sẵn + build.
- C2 `deploy-vps-local.yml`: `runs-on: [self-hosted, vps-deploy]`, CHỈ `workflow_dispatch` với input `sha` (mặc định HEAD main; phải là tổ tiên của main). Trigger `push: main` thêm ở C2 khoá main, không phải lượt này.
  - Trước: thư mục mã VPS không có commit/sửa mới so với `<repo>.synced`; có ⇒ DỪNG (KST đưa lên main trước) — không mất mã VPS.
  - Agent Data: `docker build` từ bản checkout của runner → tag `agent-data-local:<sha>`; `latest` hiện tại → `prev`; mới → `latest`; `docker compose up -d --no-build agent-data`; kiểm `/info`, `/api/health`, số tài liệu ≥100; hỏng ⇒ `prev` → `latest`, tạo lại, exit 1.
  - Web: build `.output` trong thư mục runner (giới hạn bộ nhớ), sao `nuxt-output` → `nuxt-output.prev`, chép bản mới (cục bộ), restart nuxt, reload nginx, kiểm `/knowledge`; hỏng ⇒ trả `.prev`.
  - Xong: nếu SHA vừa deploy mới hơn thì thư mục mã VPS tiến thẳng (`--ff-only`) tới SHA đó từ bản checkout cục bộ, cập nhật `.synced`; `origin` giữ sentinel.
  - KHÔNG: chép compose/nginx từ repo · SQL migration tự động · rsync DOT (ghi nợ riêng).
- C3 3 workflow kiểm giữ lại: đổi `runs-on` → `[self-hosted, vps-ci]` ⇒ phút GitHub = 0.

## D — THỬ THẬT (≤45′)
- D1 CI: mỗi repo 1 PR nhỏ (1 dòng README) → `ci.yml` xanh trên `vps-ci`; ghi thời gian.
- D2 Chặn: nhánh thử thêm 1 workflow `runs-on vps-deploy` → bị hook từ chối ở «Set up runner»; ghi bằng chứng rồi đóng PR/nhánh thử.
- D3 Deploy: dispatch `deploy-vps-local` mỗi repo với `sha` = SHA đang chạy (A1) ⇒ không đổi hành vi; SHA đang chạy UNKNOWN ⇒ dùng mã nền A2 và ghi rõ. Health xanh; ghi thời gian so với cách cũ. Mỗi lần khởi động lại ~1 phút; Owner RUN lệnh này = đồng ý.
- D4 Diễn tập lùi: chạy bước lùi (`prev`) rồi deploy lại → health xanh.
- D5 Tải VPS trong lúc build/test: production vẫn trả lời bình thường; quá tải ⇒ dừng việc CI, báo Host. Phút GitHub-hosted tăng thêm = 0.
- Nâng production lên mã nền mới hơn SHA đang chạy KHÔNG thuộc lượt này (Host/Owner quyết sau).

## KQ
- XONG khi A–D đạt cả 2 repo. NEXT_TRIGGER=GHM_C2_LOCK_MAIN (😊 Owner mua Pro → Codex khoá main + chìa KST → bật `push: main` cho deploy).
- KQ@GHM-C1-CICD-VPS-20261025-01 XONG|DỪNG + Bảng cùng commit trong COLLAB: bảng 2 repo × A/B/C/D, thời gian deploy, URL PR thử. Repo public chỉ tóm tắt; chi tiết thẻ/đường ở `/opt/incomex/work/github-management/GHM-C1-CICD-VPS-20261025-01/` (root-only).
- Lùi toàn bộ: dừng + gỡ runner (`config.sh remove`); main giữ nguyên (đã có tag `archive/`); workflow cũ vẫn nằm trong archive.

CẤM: khôi phục chìa SSH/secret cũ hoặc bật workflow cũ; chép compose/nginx từ repo; SQL tự động; force-push; xoá tệp (chỉ chuyển archive); đổi `origin` sentinel; tạo deploy key; mua Pro; >1 việc CI cùng lúc; đụng dịch vụ ngoài agent-data/nuxt/nginx reload. Gặp lỗi ⇒ dừng sạch đúng bước, KQ DỪNG + NEXT_TRIGGER, không giữ phiên chờ.
