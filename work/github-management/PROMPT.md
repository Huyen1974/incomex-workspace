# PROMPT — G1 CỔNG KIỂM MÃ GITHUB XANH THẬT (CANONICAL)

RUN_ID: GHM-GH-GREEN-GATE-20261027-06
STATUS: CANONICAL_G1 · GPT Host P85 ACCEPT Claude P84, làm rõ pilot CI khi workflow PR tự đổi và hai pha A/B tuyệt đối không giữ RUN chờ. **Hiệu lực chỉ khi Host ký READY đúng last-touch SHA tại COLLAB P85 và Owner phát OWNER RUN rõ cho từng pha**. Chưa có Owner RUN thì NO_START; chữ ký P80/F1 không áp dụng.
Hai phần dùng cùng RUN_ID, **là hai lượt thực thi tuần tự**: **Phần A — Codex** (developer, 1 PR/repo) kết thúc bằng KQ_A và giải phóng mọi cờ/phiên; **Phần B — Claude Code CLI (KST)** chỉ STARTED sau KQ_A có chứng cứ và **Owner chuyển lệnh Phần B riêng**. Không giữ terminal/RUN/VPS-GHI để chờ người khác. Host không phải ký lại nếu KQ_A đúng DoD_A và PROMPT last-touch không đổi; nếu A thiếu, STOP nhánh cụ thể, báo Host. Không C2/Pro/F2/C4/deploy/task mới.
Repo private: `Huyen1974/agent-data-test`, `Huyen1974/web-test`. Sổ chung: `work/github-management` (repo public — không ghi tên/giá trị secret).

## Mục tiêu (đo trên GitHub bằng gh API — không dựa báo cáo)
1. Check `gate` (job sẵn có của workflow «PR gate») là cổng mã duy nhất. Với PR trong làn pilot chỉ có 2 kết cục: **GREEN** khi preflight + quét secret + unit + luật CI kiểm bằng máy đều đạt; **RED** kèm lý do khi có lỗi thật — RED thì không merge.
2. Hết đỏ giả sau merge; HEAD `main` mỗi repo có `gate` GREEN trên đúng SHA.
3. KST chỉ merge khi `gate` = success (không phải skipped) được GitHub gắn đúng PR head SHA, đồng thời xác minh **merge-test SHA** (`github.sha` ở `pull_request` thường là SHA merge thử chứ không phải head SHA), base = main hiện tại, không còn lượt gate nào của PR đang chờ/chạy. Không lặp lại #676 (merge khi gate đỏ). GREEN của workflow do chính PR thay đổi là bằng chứng CI pilot, **không chứng minh gate không thể bị sửa để tự báo xanh**.
4. Web Health đỏ vì dữ liệu thật: giữ đỏ, tách khỏi cổng mã. Quyết định dữ liệu thuộc Owner (COLLAB P84 §4); G1 không sửa dữ liệu, ngưỡng, danh sách thư mục, không tắt audit.

## Sự thật Claude đã đo (gh API 27/10 21:30 +07) — S0 đo lại, lệch nhỏ thì ghi, không dừng
- Web 100 run gần nhất: 48 đỏ (Health Check 41, PR gate 3, probe c1b cũ 4) · 16 xanh · 36 huỷ (ops-smoke trước 26/10 16:19, từ đó 5/5 xanh). **Health Check đỏ liên tục từ 05/04/2026 (>700 lượt)**; lượt mới chỉ CHECK2 + CHECK7 đỏ, 11 CHECK xanh.
- AD 100 run: 80 xanh · 20 đỏ (Lint Only 15 + Data Lifecycle 4 — cũ, workflow đã tắt/đã xanh lại; PR gate 1 đỏ giả).
- Đỏ giả BASE_MOVED (AD run 40478406281, Web run 40478954350): KST chạy `gh pr ready` rồi merge sau 3–4 giây; sự kiện `ready_for_review` mở lượt gate mới trên **cùng SHA**, lượt này chạy sau merge ⇒ main đã đổi ⇒ đỏ. Lỗi quy trình + trigger thừa, không phải lỗi mã.
- Bảo vệ nhánh: cả hai repo `protected:false`; API bảo vệ/ruleset trả «Upgrade to GitHub Pro» ⇒ Free private **không cưỡng chế gì**. Web còn cấu hình cũ không hiệu lực đòi 4 check của workflow đã tắt (Pass Gate, Quality Gate, check-critical-files, Contract Schema Validation).
- Luật «dòng thêm có `secrets.` ⇒ đỏ» bắt nhầm mã Python dùng thư viện chuẩn `secrets` (AD đã có trong test).
- PR mở cũ: Web #117/#327/#669, AD 11 PR Dependabot (#325–#334, #349) — G1 không đụng, chỉ liệt kê.

## Phần A — Codex (nhánh `dev/codex-ad/g1-gate`, `dev/codex-web/g1-gate`; PR mở thường, không draft)
**S0** Đọc AGENTS.md → COLLAB P82–P84 → ROADMAP §0.4a → PROMPT. Đo lại bằng gh API: main SHA, 2 runner online, workflow active, 100 run. Chỉ STOP nếu main có commit lạ không rõ nguồn. Không giữ VPS-GHI (không đổi host).
**S1** Sửa `.github/workflows/ghm-pr-gate.yml` (+ script nhỏ nếu cần) ở mỗi repo; giữ tên job `gate`, runner pilot, flock, không secrets/docker.sock/root, quyền token chỉ đọc:
- a. Bỏ trigger `ready_for_review` (cùng SHA đã test ở opened/synchronize). Thêm `closed` để concurrency theo PR (đang cancel-in-progress) huỷ lượt còn chờ/chạy khi PR merge/đóng; job bỏ qua ở action closed ⇒ xám, không đỏ, không ghi «test pass».
- b. Thêm `push` lên main: test đúng commit vừa vào main, không so với main live, không xét luật PR. Lượt cũ bị huỷ khi main đổi tiếp là chấp nhận.
- c. PR mở mà base đã đổi lúc chạy: vẫn RED `BASE_MOVED_REBASE_REQUIRED`; cách xử lý một đường: `gh pr update-branch <số>` rồi chờ lượt mới.
- d. Thay «đổi tệp CI là đỏ» bằng luật máy **và kiểm độc lập KST**: PR đổi `.github/workflows/**` hoặc script CI ⇒ chạy actionlint ghim phiên bản + sha256 (như gitleaks), kiểm không `pull_request_target`, không dùng `secrets.` trong PR workflows, `permissions: contents:read`, chỉ runner pilot, không docker.sock/privileged; workflows dùng secret chỉ schedule/dispatch main theo chính sách hiện hữu. Vi phạm ⇒ RED, đạt ⇒ máy GREEN + annotation `CI_CHANGE_KST_REVIEW`. **Vì workflow `pull_request` được lấy từ merge commit do PR đóng góp, chính PR có thể đổi/bỏ bước kiểm:** trước merge, KST phải đọc và đối chiếu SHA/diff của workflow/CI scripts với baseline `main` **ngoài chính job PR** (Mac/GitHub API), xác nhận actionlint/secret scan/logic kiểm thật không bị bỏ hoặc làm rỗng; nếu bị vô hiệu hóa ⇒ KST BLOCK, cho dù UI GREEN. Đây chỉ là pilot trusted-author, không là hard enforcement C2. Chỉ xét tham chiếu `secrets.` trong workflow cho policy này, gitleaks tiếp tục quét mọi thay đổi khác. Diff >200 tệp/5000 dòng giữ RED, tách PR.
- e. Bỏ điều kiện gate blob head phải byte-đúng `main` để không kẹt mọi PR sửa gate; GitHub `pull_request` thực thi workflow từ merge-test PR nên mọi bước mới vẫn phải KST xác minh độc lập ngoài workflow như (d). **Owner RUN lệnh này cho phép pilot đúng một PR G1 sửa gate mỗi repo theo quy trình KST**, không phải cho phép bỏ scan/cơ chế bảo vệ, không cấp quyền Codex tự merge/main. PR phải GREEN theo gate mới và đủ KST review tại SHA mới; chưa có Pro vẫn không được tuyên hardlock.
- f. PR ngoài làn (tác giả/nhánh khác, Dependabot): giữ bỏ qua như hiện tại, không chạy mã PR. Ghi rõ trong summary: GitHub tính job bị bỏ qua do điều kiện = Success với required check ⇒ KST không merge khi gate = skipped; C2 xử lý bằng ruleset.
- g. Cấm tô xanh: không continue-on-error/exit 0 giả, không bỏ quét secret, không xoá/chạy lại run cũ để đổi màu.
**S2** Thử thật trên GitHub, mỗi repo:
- Dương: PR G1 GREEN trên đúng head SHA; job summary đủ head/base/merge-test/luật CI/unit/scan.
- Âm: 1 PR tiêu đề bắt đầu `G1-NEG` (không merge): commit 1 làm hỏng 1 unit ⇒ RED; commit 2 sửa unit nhưng thêm 1 tệp workflow nhỏ dùng trigger `pull_request_target` (không tham chiếu secret nào, không nạp secret thật) ⇒ RED; đóng PR ⇒ không sinh đỏ mới. Tối đa 2 run đỏ/repo, ghi run ID.
- Base đổi: xảy ra tự nhiên thì ghi; không tạo commit main để thử.
**DoD A:** 2 PR G1 GREEN đúng SHA + 2 PR âm đỏ đúng lý do và đã đóng; bảng run ID/kết luận lấy từ gh API; 0 merge/deploy. Ghi P85 + bảng. NEXT_TRIGGER=OWNER_GIAO_KST_PHAN_B_GHM-GH-GREEN-GATE-20261027-06.

## Phần B — Claude Code CLI (KST), cùng RUN_ID, sau DoD A
**B1** Mỗi PR G1, gh API phải chứng minh latest `gate=success` cho PR head SHA, test merge SHA với đúng base/head, không bị `skipped`/`cancelled`, không có run cùng PR đang chờ/chạy và base summary trùng current main (`gh pr update-branch` nếu lệch rồi đợi GREEN mới). **KST kiểm độc lập toàn diff workflow/CI scripts và các bước kiểm từ GitHub `main` và PR tại SHA ghim, nhất là các thay đổi của gate tự kiểm, không chấp nhận script bị xóa/vô hiệu hóa dù GH xanh.** COMMENT `KST_ACCEPT@<head SHA>` kèm bằng chứng và giới hạn pilot, rồi `gh pr merge <số> --merge --match-head-commit <SHA>`. Không đổi trạng thái draft/ready ngay trước merge. Đây chưa phải enforced review vì hai vai dùng chung GitHub Owner identity.
**B2** Sau merge: lượt `gate` push main GREEN trên SHA main mới; 0 run đỏ mới do merge; lượt Health Check kế tiếp vẫn chỉ CHECK2/CHECK7 đỏ (không đổi).
**B3** KQ: `GH_CODE_GATE=PASS|FAIL` (từng repo, kèm run ID) · `GH_HARDLOCK_ENFORCED=NO` (Free private; C2 phải thay 4 check cũ của Web bằng `gate`, chặn merge khi skipped, bật «base phải mới nhất») · `BUSINESS_HEALTH=FAIL` giữ · Bảng/ROADMAP/README. Không deploy (chỉ đổi workflow, không đụng runtime), không VPS-GHI.
NEXT_TRIGGER=HOST_ACCEPT_G1 — Host và Claude tự đối chiếu mọi run ID bằng gh API trước khi ACCEPT.
