# KẾ HOẠCH THỰC HIỆN — github-management · V0.5 · 28/10/2026 · C2 PRIVATE MAIN GH GATE P98

**Trạng thái GPT Host P99: ACCEPT Claude P98, C2-A PASS theo GitHub (4 PR GREEN +2 PR RED OUT_OF_PILOT, 6 PR OPEN). P92 READY last-touch `664f06e0d2c8d7839d35241f0d93a0995cda70f0` còn hiệu lực, PROMPT không đổi, không mở vòng 2. C2-B CHƯA RUN vì API `/rulesets` cả hai private repo vẫn 403 Upgrade GitHub Pro, main protected:false, Web legacy 4 contexts cần KST B1 sau Pro. Owner nâng Pro → Host xác minh API/SHA → Owner giao Claude Code CLI B (same RUN GHM-C2-PRIVATE-MAIN-PROTECT-20261028-07), rồi C2-B hardlock thử âm; chỉ F2 khi C3.0 runner trust boundary/actor rights đạt. Health business FAIL/AD rollback nợ riêng.**

Tài liệu này là *bảng đầu việc cụ thể* cho Codex và Claude Code CLI. [ROADMAP.md](ROADMAP.md) giữ các mốc và điều kiện chốt, [COLLAB.md](COLLAB.md) giữ duy nhất mục tiêu Owner, trạng thái và quyết định. Không tạo thêm hệ điều hành công việc; dùng lại hội đồng, luật AGENTS, Issue/PR và DOT/Codex hiện có.

## 0. FAST-PR-LANE 27/10/2026 (F0/F1/G1 đã qua pilot; bước hiện hành C2, xem ROADMAP §0.4b)
- **C2 theo P90:** trước khi mở F2, Owner Pro GH private cho branch/ruleset, required `gate` đúng SHA trên main hai repo, thử RED/skipped/direct push/behind/admin, Web bỏ 4 contexts legacy. KST-only quyền merge không thể cưỡng chế khi Codex/Claude cùng account Huyen1974; trình Owner chọn danh tính/merge path nếu muốn cứng vai. Không bật auto-CD hay thêm hạ tầng.
- **Health riêng:** 28/10 11:00 +07 Web Health trên SHA 4f8405a9: CHECK2/7 business FAIL, CHECK12 PASS; 2 orphan. Chưa Owner GO sửa 30 docs test / 8 docs thật, không tự mutation. C1B AD rollback cũng riêng.
- Đường găng: F0 Code branch/PR CI an toàn hai repo (không VPS-GHI khi viết mã) → F1 KST xét/merge, Web deploy theo script/VPS-GHI → F2 nhân 3 ghế. C1B AD Compose old rollback DDL/Web Health 401 xử lý độc lập, không gộp cổng vào dev.
- F0 P74 chỉ pilot PR từ Codex/Claude Code CLI trusted trên runner C1A persistent hiện có; KHÔNG coi là cách ly tuyệt đối khỏi audit secrets. Preflight policy từ nguồn tin cậy trước mã PR, không fork/actor ngoài scope; F2 thêm worker cần C2 kiểm thực quyền/secret/trust boundary. Chỉ mở trigger PR, không bật push dev trùng lần CI.
- Sau F0/F1 Owner có thể mua GitHub Pro để bảo vệ main private/required checks sớm, không tự thanh toán. KST Claude Code CLI review/merge GitHub, release script thực thi trên VPS; người phát triển không tự merge/deploy.
- Bằng chứng F0: PR350/676 + CI head/merge SHA đã PASS P77. F1: Claude Code CLI KST review/merge đúng SHA + Web Health main 13 CHECK đáng tin (business RED vẫn RED); Web production lần đầu phục vụ build từ GitHub main và GIỮ sau parity 166/166+Guard, old pinned rollback. PR Web đổi mã ứng dụng đầu tiên là F2, không bịa trong F1. F2: 3 PR, ít nhất 2 KST nhận; C2 Pro do Owner quyết trước thêm worker.

## 1. Mục tiêu, vai trò và giới hạn

**Đích ưu tiên:** mở không gian để 3–5 agent viết mã song song trên hai kho đang có, không tranh cờ VPS-GHI khi viết mã. Claude Code CLI tập trung kiểm tra, yêu cầu sửa và merge từng PR. **Đích cuối:** Owner giao một batch nhiệm vụ buổi tối, các agent nhận và làm khi Owner vắng mặt; sáng có báo cáo từng việc, không tự deploy vô điều kiện.

| Vai | Chịu trách nhiệm chính | Ranh giới |
|---|---|---|
| Owner | Phê duyệt roadmap, quyền và các bước thay đổi production; quyết mục tiêu nghiệp vụ | Không phải duyệt từng commit hoặc canh ca đêm |
| GPT Host | Phân mốc, chốt PROMPT, nhận KQ, xử lý ý kiến Claude, báo Owner | Không giả quyết định Owner hay tự ghi READY trước đủ cổng |
| Codex (executor R0–R2 và C1B theo Owner, điều phối R4/R6) | Khảo sát, tắt Actions, cài ruleset/thẻ, soạn luật repo, giao việc pilot và ghi evidence | Không cầm chìa KST, không tự duyệt mã do chính Codex viết; riêng C1B Owner RUN cho phép scoped main/deploy CHỈ qua cổng có quyền hợp lệ của Codex, không vượt guard/secret/role |
| Claude Code CLI (Chief = KST) | KST review/merge `main` từ C3 trở đi (C1B Codex có phép thực thi scoped riêng theo Owner): mã nền, merge PR trên nền mới nhất, NHẬN/SỬA/TRẢ LẠI/BỎ, triển khai thường lệ sau C1B | Phiên KST không nhận việc phát triển; không tự bỏ Guard; không coi merge sạch là chức năng đúng |
| Các worker (Codex, Hermes, Claude, ghế khác đã cấp quyền) | Mỗi việc một workspace/branch/PR, có biên nhận/test | Không ghi trực tiếp nhánh chính, không giữ VPS-GHI để phát triển |
| DOT (mốc sau) | Nhắc/điều phối Codex và lấy receipt theo cơ chế hội đồng đã có | Không mặc nhiên được gọi agent nếu chưa có đường thực thi được kiểm chứng |

**Giới hạn cứng trong giai đoạn lập kế hoạch:** không tắt Actions, không thay quyền/secret, không pull/reset/force-push hay sửa main GitHub, không đổi Git remote, container hoặc deploy VPS, không mở public hai repo, không chi tiền. Mọi thay đổi thực tế chỉ bắt đầu sau Claude phản biện, GPT chốt, Owner duyệt và RUN hợp lệ.

## 2. Danh mục đầu việc giao Codex theo đúng thứ tự

| ID | Bước | Công việc chi tiết | Chứng cứ hoàn thành |
|---|---|---|---|
| R0.1 | Nguồn mã VPS | 2 thư mục mã đang chạy `docker/agent-data-repo`, `docker/nuxt-repo`: nhánh, HEAD, sạch/bẩn, remote (ẩn credential); HEAD đã có trên nhánh `vps-daily-*` chưa | Bảng thư mục → nhánh → HEAD → có trên GitHub; điểm UNKNOWN |
| R0.2 | Mã đang chạy | Mỗi dịch vụ (agent-data, nuxt): image/bản build đang chạy dựng từ commit nào; có gì đang kéo `main` 2 kho không | Bảng dịch vụ → commit đang chạy; lệch HEAD ghi rõ |
| R0.3 | Actions, thẻ, đường gọi | Workflow 2 kho (lịch, lần chạy cuối, việc làm) + Dependabot; mọi thẻ/app/khoá ghi được 2 kho (tên + quyền, không in giá trị); chỉ đọc đường gọi cho R6: Dot→Codex, Codex cloud / Claude Code web nối được 2 kho | Mỗi workflow: MIGRATE (chức năng cần giữ → Guard/Kuma, ghi nợ) hoặc BỎ — không có GIỮ; ma trận thẻ; R6 khả thi có/không + bằng chứng |
| R1.1 | Khoá chi phí (P14) | Owner 25/10: Actions vẫn bật. PROMPT GHM-R1-COST: đo billing; ngân sách Actions $0 + «Stop usage» + cảnh báo 75/90/100%; tắt riêng từng workflow thừa bằng `gh workflow disable` (bật lại được), giữ 3 nhóm kiểm cần; không runner, không tắt Actions cấp repo | Ngân sách $0 + Stop có; 3 nhóm nghiệp vụ + Dependabot dynamic managed (runner tiêu chuẩn miễn phí), 15 BỎ đã disable; budget $0 + Stop verified |
| R1.2 | 😊 Owner mua Pro | Chỉ tại C2 SAU C3, Owner mới nâng Pro để khóa main private: github.com/settings/billing → nâng GitHub Pro. Ngân sách $0 + Stop của R1.1 giữ nguyên nên gắn thẻ thanh toán không mở đường mất tiền | Owner xác nhận Pro và budget Actions $0 + Stop sau nâng cấp |
| C1A | Codex cài runner và chạy CI thật trên VPS | Hai GitHub repo private, mỗi repo runner CI cách ly non-root; không docker.sock/secret, tổng 2CPU/3GiB; một workflow `push` test mã thật trên nhánh dev/repo | CI 2/2 PASS P35; Swap/kernel và INV25 đã đạt P40; Codex P48 đã khai/canh đúng 2 data volumes 8/8, Host P49 ACCEPT C1A scoped. GLOBAL_GUARD PARTIAL và dữ liệu 24h chưa đủ, không giả global PASS. Không gộp nhiệm vụ sang C1B. Không chạy lại hai CI đã PASS. |
| C1B | **Codex (Owner RUN C1B)** chuẩn nguồn và thử deploy VPS thủ công qua cổng được phép | Host P49 đã nghiệm thu C1A scoped; C1B chỉ chạy khi Host READY mới/Owner giao Codex RUN: xác minh Web runtime output và Agent Data image đang chạy theo SHA (khác HEAD thì STOP và đối chiếu); bảo toàn main cũ bằng tag/backup, chuẩn baseline theo nguồn VPS đã kiểm, không force-push; script deploy local cổng host hẹp mà Codex được phép gọi trong RUN; không mượn quyền KST, PRE/POST health + rollback thật; chuyển 3 workflow audit còn hosted sang runner VPS nếu test đạt. Đ30/31, cờ VPS-GHI, kiểm writer xung đột. Không runner nhận PR có Docker/root, không bật tự động CD trước C2, không cấp Codex quyền admin/KST mới | 2 repo main SOURCE đúng tree/giữ old main, candidate build+manual deploy+rollback runtime cũ healthy; 3 audit runner VPS tương đương, không ghi đè config/DB hay làm hỏng dịch vụ cũ |
| G0 · BỎ (P22) | Kiểm ba tuyến CI/CD cũ theo DROOT56 (READ-ONLY) | Codex sử dụng PROOT08/09, P12/P17 và mẫu mới để chỉ rõ GitHub PR/CI, backup VPS→GitHub và CD GitHub→VPS đã bị khóa; không nối lại, không tạo secret | Một bảng VERIFIED/UNKNOWN, tiêu chí phục hồi an toàn và lệnh bước kế độc lập |
| R2-P(A) · BỎ (P22) | Bootstrap Free | Codex dựng 1 repo public thử sạch/lịch sử mới; Actions repo thử OFF; ruleset main-only và 3 Issue, test worker thật dev branch/PR (+ main reject) | Repo/3 Issue/nhánh/permission evidence, không đụng 2 repo private |
| R2-P(B) · BỎ (P22 → C3 trên 2 repo thật) | 3 agent song song | Codex, Hermes, Claude/ghế khác nhận 3 việc tách scope, tự code/commit/PR ở 3 workspace; Chief review/test/merge lần lượt | 3 PR, ≥2 Chief NHẬN, 0 push main từ dev, giờ thực đo và bảng sáng |
| R2.1 | Khoá main hai repo PRIVATE tại C2 sau C3 | **R2-A** Codex: ruleset `chief-only-main` chỉ `main` 2 kho (update · deletion · non_fast_forward; bypass duy nhất DeployKey; trước đó đếm deploy key ghi = 0). **R2-B** Claude Code CLI trên VPS (cờ VPS-GHI, Đ30/31): tạo bản clone riêng của KST, sinh 1 chìa/kho trong đó (remote riêng, không phải khoá mặc định của máy); Codex gắn chìa công khai làm deploy key ghi | R2-A: ruleset active, 0 deploy key ghi · R2-B: đúng 1 deploy key ghi/kho |
| R2.2 | Thẻ worker và quyền C2 | **R2-B.** Worker tự động cần danh tính/quyền giới hạn chỉ cho nhánh/PR ở 2 repo; ưu tiên tận dụng quyền đang có, chỉ tạo key/token phụ khi thử cưỡng chế cho thấy cần. **Không tự hạ quyền phiên `gh` Owner trên Mac của Codex/Claude Code CLI** (Owner đã chốt P57/P58/P63); khóa thao tác ghi `main` bằng ruleset/ký KST riêng. PAT/khóa sao lưu VPS nếu có quyền thừa thì kiểm riêng, không tác động trong C1B. | Worker không thể đưa mã vào main trái quy trình; Owner Mac vẫn dùng quyền được cấp; phép thử âm C2 PASS |
| R2.3 | Phép thử âm | T-a đẩy main → chặn (R2-A, thử bằng Owner admin: mạnh nhất bị chặn ⇒ dev bị chặn) · T-b dev sửa ruleset → chặn (R2-B) · T-d sau khi gắn thẻ Pro, ngân sách $0 + Stop vẫn hiệu lực (trang billing) · T-e force-push/xoá main → chặn (đọc lại luật, không thử thật) · T-c KST đẩy main → qua (chạy ở R3.2) | Kết quả từng phép thử bằng danh tính thật; UNKNOWN không tính PASS |
| R2.4 | Luật repo | **R2-A** Codex soạn AGENTS.md ≤ 1 trang + mẫu PR 6 ô, đẩy nhánh `dev/codex/GHM-R2A-rules` + 1 PR nháp mỗi kho SAU khi khoá main (= thử nhánh dev vẫn mở); R3.3 KST merge | Người mới đọc biết nhận / làm / nộp mà không hỏi lại |
| R3.1 | Lưu main cũ | KST: tag `archive/main-<ngày>` trỏ main cũ | Tag đúng SHA |
| R3.2 | Mã nền = VPS | KST trong bản clone: lấy HEAD thẳng từ thư mục mã VPS (cùng máy), merge main cũ với chiến lược giữ nguyên cây VPS, đẩy `main` bằng chìa KST (fast-forward, không force) | `git diff <HEAD VPS> main` rỗng; main cũ là tổ tiên; T-c PASS |
| R3.3 | Luật vào repo | KST merge PR nháp R2.4 (rebase lên main mới) | Commit trên main |
| R3.4 | Cầu nối | Tới khi R5 xong: mỗi sáng KST merge commit VPS mới vào main như một PR (chống hai nguồn lệch) | Không commit VPS nào vắng trên main quá 1 ngày |
| R3.5 | Ngoài 2 kho | Ghi DOT/Graph/nginx/systemd/Guard/scripts chưa có kho vào nợ «kho ops»; không tự nhét | Danh sách trong task |
| R4.1 | 3 ghế song song | 3 việc thật, khác khu tệp, có unit test, ≤ 2 giờ; Codex · Hermes · ghế dev AI thứ ba độc lập (KST không tự duyệt PR mình), sandbox riêng, nhánh `dev/<ghế>/<mã việc>`, phiếu 6 ô | 3 PR của 3 ghế; giờ nhận/xong từng việc |
| R4.2 | KST duyệt | Trên main mới nhất: test → NHẬN / SỬA / TRẢ LẠI / BỎ; kiểm lại SHA main + PR trước khi đẩy | ≥2 PR KST NHẬN; trước C2 chỉ chứng minh 0 direct push main thực tế và 0 auto deploy, chưa khóa main cưỡng chế ở private Free; CI chạy VPS |
| R5.1 | Triển khai từ main | Owner GO (nối lại chiều GitHub→VPS — luật DROOT56). Theo cờ từng khu: VPS lấy đúng SHA main bằng thẻ chỉ đọc → build/khởi động lại theo cách đang dùng → health; lùi = SHA trước | SHA đang chạy = SHA main; diễn tập lùi PASS |
| R5.2 | Khoá nguồn VPS (P7) | (a) cấu hình cổng workspace: root `agent-data` `writable=false` (như root `docs`) · (b) 2 thư mục mã gắn chỉ đọc; bước deploy KST mở → cập nhật SHA/build → khoá lại · (c) `origin` giữ URL chết DROOT56, deploy dùng URL riêng + thẻ chỉ đọc · (d) Guard có sẵn thêm 1 điều kiện: sạch + HEAD = SHA đã deploy + đang chỉ đọc · (e) biển `00-NHAN-THU-MUC.md` mỗi thư mục · dừng backup ngược khi đã khớp; giữ backup PG/Qdrant/Directus/Drive; mọi thay đổi qua apply-v0 + Đ30/31 | 4 phép thử âm: sửa tay ⇒ Read-only · MCP ⇒ READ_ONLY_ROOT · `git push origin` ⇒ lỗi DROOT56 · mở khoá ngoài deploy ⇒ Guard đỏ Telegram |
| R6.1 | Giao việc đêm | Theo đường đã chứng minh ở R0.3; mỗi việc biên nhận / hạn / dừng sạch; lỗi một việc không chặn việc khác | Batch chạy khi Owner vắng |
| R6.2 | Nghiệm thu đêm | 3–5 việc, KST duyệt từng PR, bảng sáng §4 | ≥ 2/3 NHẬN; không ai canh |

**Thứ tự phụ thuộc:** R0+R1 (một RUN) → R2 → R3 → R4 → (R5 ∥ R6). R5/R6 chỉ song song ở phần **giao việc, code, mở PR, test riêng**; Chief phải ngừng merge mới vào main khi R5 đang pin release/build/restart/rollback. Các mục đọc độc lập không cần VPS-GHI; thao tác ghi thuộc khu đang chạy phải tuân thủ cờ. Không tự chuyển mốc khi gate chưa PASS.

## 3. Phân loại mã dự kiến tại R3 — phải đo rồi mới chốt
- **agent-data-test:** backend Agent Data, RAG/ingest/search, công cụ MCP thuộc Agent Data và các test liên quan. Không đưa dữ liệu PG/Qdrant, secret, backup hay OS runtime.
- **web-test:** Nuxt/UI, giao diện Directus và tích hợp ứng dụng web, test frontend. Không đưa cơ sở dữ liệu, core RAG hay mã vận hành chưa phân chủ.
- **Ngoài phạm vi trước khi khảo sát:** DOT runtime, Graph Server, nginx/systemd/Guard/compose hoặc scripts dùng chung không được tự nhét vào repo bất kỳ. Ghi danh mục nợ riêng, không tự mở repo thứ ba.

**Không xóa main cũ:** tag trước (R3.1); chuyển cây mã bằng commit merge tiến lên (R3.2), không reset/force push. Không công khai lịch sử repo đang private khi chưa kiểm toán. Mã runtime không đồng nghĩa với git HEAD; phải đo image/config đang phục vụ.

## 4. Luật vận hành tối thiểu khi chính thức áp dụng
### Phiếu giao việc 6 ô
1. TASK_ID + Issue; 2. Mục tiêu và *thế nào là hoàn thành* (lệnh test/DoD); 3. Scope tệp được phép/cấm; 4. Phụ thuộc và base SHA; 5. Worker + Chief; 6. Thời hạn/quota và điều kiện dừng.

Mỗi worker bắt buộc đọc root luật và hướng dẫn repo, Issue trước STARTED; code trong clone/worktree riêng, branch dev/<seat>/<task-id>. Một việc độc lập không đợi Chief merge trước mới nhận. Việc phụ thuộc giao diện/API chưa merge phải ghi dependency hoặc nhánh xếp chồng; chủ API làm đầu tiên.

### Chief review/merge
1. Nhận PR + evidence đúng scope/DoD; thiếu → TRẢ LẠI.
2. Lấy HEAD mới nhất của nhánh đích; tạo merge candidate độc lập, không chép nguyên tệp cũ đè lên main.
3. Chạy test trên ứng viên đã ghép; lỗi xung đột/logic/khác scope → TRẢ LẠI kèm file/test/mong đợi.
4. Chọn **NHẬN / SỬA NHỎ / TRẢ LẠI / BỎ**; Chief tự sửa phải có reviewer khác hãng.
5. Trước merge recheck cả SHA main và PR. HEAD thay đổi sau khi test → phải test lại. Chỉ actor Chief được nhập; merge không tự deploy.

### Bảng kết quả sáng
Mỗi TASK_ID một dòng: Worker | Repo/Branch | PR + SHA | Test | Chief decision | Merge status | Blocker/NEXT_TRIGGER | Deployed? (mặc định **KHÔNG**). Chỉ cần Owner xem ngoại lệ, không phải đọc log dài.

## 5. Cổng NO-GO & rollback
| Gate | Phải chứng minh trước bước kế | Dừng nếu |
|---|---|---|
| G0 trước tắt Actions | Biết rõ workflow còn hữu ích và đường thay thế không ảnh hưởng dịch vụ | Không biết job nào đang backup/canh/triển khai |
| G1 trước cấp quyền dev | Worker có quyền branch/PR nhưng không có quyền ghi main/ruleset; thử âm bằng danh tính thật | Chưa có hard-lock, actor dùng chung admin |
| G2 trước R3 | HEAD VPS + commit đang chạy đã ghi (R0); khoá, thẻ, chìa KST PASS (R2) | HEAD VPS bẩn/chưa rõ hoặc khoá chưa PASS |
| G3 trước deploy R5 | Owner GO, test merge/staging/rollback PASS, archive còn phục hồi | Không ghim được SHA, branch cũ có thể được kéo nhầm |
| G4 trước ca đêm | Cơ chế DOT/Codex/agents gọi được thật, có biên nhận và giới hạn, trạng thái DỪNG sạch | Chỉ là kế hoạch hoặc phải có Owner canh |

Khi fail, Codex báo KQ DỪNG + NEXT_TRIGGER, trả mọi lock; không tự phát sinh dịch vụ, cron, key hay bước mới. Công việc đang phục vụ trên VPS vẫn hoạt động theo đường cũ cho tới R5 GO và POST/rollback xác nhận.

## 6. Đề nghị Claude phản biện — một vòng, đi thẳng vào điểm quyết định
Claude Reviewer đọc AGENTS.md → COLLAB §0/Bảng/P3/P4 → ROADMAP.md → tài liệu này. Kiểm sáu câu hỏi: (1) R0→R1 không làm mất backup/monitor? (2) Khóa main private/Pro đúng quyền thực? (3) R3 mã nguồn từ runtime và cách giữ lịch sử có chuẩn? (4) R4 ba agent/merge stale/các test thật? (5) R5 deploy một SHA, kiểm rollback, chặn luồng ngược? (6) R6 reuse hội đồng/DOT, có receipt, không giả tự động?

Reviewer khác hãng ghi P-Review có evidence (`ACCEPTED|PARTIAL|REJECTED` là ý kiến, KHÔNG là chữ ký). Host xem và quyết định cuối; **chỉ một `READY@<full last-touch PROMPT SHA>` của Host hoặc Co-host hợp lệ là đủ**, không cần `ACCEPT@SHA` từ hội đồng (DROOT58). Host tự quyết có mở vòng 2/3 khi còn vấn đề kỹ thuật thật, **TỐI ĐA 3** theo DROOT57; không mở vòng do chỉnh STATUS/SHA. AUTO0 Owner chuyển prompt chỉ để kích hoạt executor, các cổng Guard/VPS-GHI/Owner-only còn hiệu lực.

## 7. Dữ kiện đã đo và chưa đo
Ngày 24/10: Git VPS agent-data, UI và workspace báo clean; GitHub main hai repo còn cũ/không protected, chứa 17 và 11 workflow; có Actions được kích hoạt theo lịch. **Chưa đo** remotes/upstreams, `docker/nuxt-repo`, commit đang chạy từng dịch vụ và các thẻ đang có quyền; bắt buộc làm tại R0. Claude P5 bổ sung: `vps-daily-20261023` = HEAD VPS agent-data (75ed0e80); agent-data đang chạy b6ebaf94 (đo 23/10). VPS có swap gần cạn, vì vậy không mặc định dùng VPS1 để chạy toàn bộ build/test.
