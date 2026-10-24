# KẾ HOẠCH THỰC HIỆN — github-management · V0.2 · 24/10/2026 · đã áp Claude P5 C1–C10

**TRẠNG THÁI: DRAFT · Claude P5 ACCEPT_WITH_CORRECTIONS · chờ GPT Host đồng thuận · KHÔNG ĐƯỢC RUN.**

Tài liệu này là *bảng đầu việc cụ thể* cho Codex và Claude Code CLI. [ROADMAP.md](ROADMAP.md) giữ các mốc và điều kiện chốt, [COLLAB.md](COLLAB.md) giữ duy nhất mục tiêu Owner, trạng thái và quyết định. Không tạo thêm hệ điều hành công việc; dùng lại hội đồng, luật AGENTS, Issue/PR và DOT/Codex hiện có.

## 1. Mục tiêu, vai trò và giới hạn

**Đích ưu tiên:** mở không gian để 3–5 agent viết mã song song trên hai kho đang có, không tranh cờ VPS-GHI khi viết mã. Claude Code CLI tập trung kiểm tra, yêu cầu sửa và merge từng PR. **Đích cuối:** Owner giao một batch nhiệm vụ buổi tối, các agent nhận và làm khi Owner vắng mặt; sáng có báo cáo từng việc, không tự deploy vô điều kiện.

| Vai | Chịu trách nhiệm chính | Ranh giới |
|---|---|---|
| Owner | Phê duyệt roadmap, quyền và các bước thay đổi production; quyết mục tiêu nghiệp vụ | Không phải duyệt từng commit hoặc canh ca đêm |
| GPT Host | Phân mốc, chốt PROMPT, nhận KQ, xử lý ý kiến Claude, báo Owner | Không giả quyết định Owner hay tự ghi READY trước đủ cổng |
| Codex (executor R0–R2, điều phối R4/R6) | Khảo sát, tắt Actions, cài ruleset/thẻ, soạn luật repo, giao việc pilot và ghi evidence | Không cầm chìa KST, không ghi `main`, không tự duyệt mã do chính Codex viết |
| Claude Code CLI (Chief = KST) | Người duy nhất ghi `main` (R3 trở đi): mã nền, merge PR trên nền mới nhất, NHẬN/SỬA/TRẢ LẠI/BỎ, triển khai R5 | Phiên KST không nhận việc phát triển; không tự bỏ Guard; không coi merge sạch là chức năng đúng |
| Các worker (Codex, Hermes, Claude, ghế khác đã cấp quyền) | Mỗi việc một workspace/branch/PR, có biên nhận/test | Không ghi trực tiếp nhánh chính, không giữ VPS-GHI để phát triển |
| DOT (mốc sau) | Nhắc/điều phối Codex và lấy receipt theo cơ chế hội đồng đã có | Không mặc nhiên được gọi agent nếu chưa có đường thực thi được kiểm chứng |

**Giới hạn cứng trong giai đoạn lập kế hoạch:** không tắt Actions, không thay quyền/secret, không pull/reset/force-push hay sửa main GitHub, không đổi Git remote, container hoặc deploy VPS, không mở public hai repo, không chi tiền. Mọi thay đổi thực tế chỉ bắt đầu sau Claude phản biện, GPT chốt, Owner duyệt và RUN hợp lệ.

## 2. Danh mục đầu việc giao Codex theo đúng thứ tự

| ID | Bước | Công việc chi tiết | Chứng cứ hoàn thành |
|---|---|---|---|
| R0.1 | Nguồn mã VPS | 2 thư mục mã đang chạy `docker/agent-data-repo`, `docker/nuxt-repo`: nhánh, HEAD, sạch/bẩn, remote (ẩn credential); HEAD đã có trên nhánh `vps-daily-*` chưa | Bảng thư mục → nhánh → HEAD → có trên GitHub; điểm UNKNOWN |
| R0.2 | Mã đang chạy | Mỗi dịch vụ (agent-data, nuxt): image/bản build đang chạy dựng từ commit nào; có gì đang kéo `main` 2 kho không | Bảng dịch vụ → commit đang chạy; lệch HEAD ghi rõ |
| R0.3 | Actions, thẻ, đường gọi | Workflow 2 kho (lịch, lần chạy cuối, việc làm) + Dependabot; mọi thẻ/app/khoá ghi được 2 kho (tên + quyền, không in giá trị); chỉ đọc đường gọi cho R6: Dot→Codex, Codex cloud / Claude Code web nối được 2 kho | Mỗi workflow: MIGRATE (chức năng cần giữ → Guard/Kuma, ghi nợ) hoặc BỎ — không có GIỮ; ma trận thẻ; R6 khả thi có/không + bằng chứng |
| R1.1 | Tắt Actions | Cùng RUN R0: tắt Actions cấp repo 2 kho, tắt Dependabot tự mở PR, huỷ run dở; không xoá YAML, không phục hồi khoá SSH. Workflow đang làm việc sản xuất chưa có đường thay ⇒ DỪNG trước bước này | Settings Disabled; push thử không sinh run; usage mới 0 |
| R1.2 | 😊 Owner mua Pro | Chỉ sau R1.1. Bấm: github.com/settings/billing → nâng GitHub Pro; rồi Budgets and alerts → New budget → Product-level budget · Actions · cả tài khoản · số tiền 0 → tích «Stop usage when budget limit is reached» → Create budget | Trang billing: Pro + budget $0 có dừng |
| R2.1 | Khoá main | Codex: ruleset chỉ `main` 2 kho (update · deletion · non_fast_forward; bypass duy nhất DeployKey). Claude Code CLI trên VPS (cờ VPS-GHI, Đ30/31): tạo bản clone riêng của KST, sinh 1 chìa/kho trong đó (remote riêng, không phải khoá mặc định của máy); Codex gắn chìa công khai làm deploy key ghi | Ruleset active; đúng 1 deploy key ghi/kho |
| R2.2 | Thẻ dev + hạ quyền | Mỗi ghế dev 1 thẻ fine-grained chỉ 2 kho (Contents + Pull requests, không Administration). Hạ quyền mọi thẻ admin trong ma trận R0.3: `gh` trên Mac chuyển sang thẻ dev khi cài xong; PAT backup VPS nếu có Administration ⇒ thay thẻ chỉ Contents (Claude Code CLI, Đ30/31) | 0 thẻ admin ngoài Owner trên web (passkey) |
| R2.3 | Phép thử âm | T-a dev đẩy main → chặn · T-b dev sửa ruleset → chặn · T-d đẩy workflow → không chạy · T-e dev force-push/xoá main → chặn · T-c KST đẩy main → qua (chạy ở R3.2) | Kết quả từng phép thử bằng danh tính thật; UNKNOWN không tính PASS |
| R2.4 | Luật repo | Codex soạn AGENTS.md ≤ 1 trang + mẫu PR 6 ô cho từng kho (nháp trong task; R3.3 mới commit) | Người mới đọc biết nhận / làm / nộp mà không hỏi lại |
| R3.1 | Lưu main cũ | KST: tag `archive/main-<ngày>` trỏ main cũ | Tag đúng SHA |
| R3.2 | Mã nền = VPS | KST trong bản clone: lấy HEAD thẳng từ thư mục mã VPS (cùng máy), merge main cũ với chiến lược giữ nguyên cây VPS, đẩy `main` bằng chìa KST (fast-forward, không force) | `git diff <HEAD VPS> main` rỗng; main cũ là tổ tiên; T-c PASS |
| R3.3 | Luật vào repo | KST commit bản R2.4 lên main | Commit trên main |
| R3.4 | Cầu nối | Tới khi R5 xong: mỗi sáng KST merge commit VPS mới vào main như một PR (chống hai nguồn lệch) | Không commit VPS nào vắng trên main quá 1 ngày |
| R3.5 | Ngoài 2 kho | Ghi DOT/Graph/nginx/systemd/Guard/scripts chưa có kho vào nợ «kho ops»; không tự nhét | Danh sách trong task |
| R4.1 | 3 ghế song song | 3 việc thật, khác khu tệp, có unit test, ≤ 2 giờ; Codex (cloud) · Claude Code (cloud) · Hermes (VPS), sandbox riêng, nhánh `dev/<ghế>/<mã việc>`, phiếu 6 ô | 3 PR của 3 ghế; giờ nhận/xong từng việc |
| R4.2 | KST duyệt | Trên main mới nhất: test → NHẬN / SỬA / TRẢ LẠI / BỎ; kiểm lại SHA main + PR trước khi đẩy | ≥ 2 NHẬN; 0 lần dev ghi được main; Actions 0 |
| R5.1 | Triển khai từ main | Owner GO (nối lại chiều GitHub→VPS — luật DROOT56). Theo cờ từng khu: VPS lấy đúng SHA main bằng thẻ chỉ đọc → build/khởi động lại theo cách đang dùng → health; lùi = SHA trước | SHA đang chạy = SHA main; diễn tập lùi PASS |
| R5.2 | Khoá nguồn VPS | Guard: thư mục mã VPS phải sạch và HEAD là một SHA của main; dừng backup ngược khi đã khớp; giữ nguyên backup PG/Qdrant/Directus/Drive | Guard xanh; thử sửa tay ⇒ đỏ |
| R6.1 | Giao việc đêm | Theo đường đã chứng minh ở R0.3; mỗi việc biên nhận / hạn / dừng sạch; lỗi một việc không chặn việc khác | Batch chạy khi Owner vắng |
| R6.2 | Nghiệm thu đêm | 3–5 việc, KST duyệt từng PR, bảng sáng §4 | ≥ 2/3 NHẬN; không ai canh |

**Thứ tự phụ thuộc:** R0+R1 (một RUN) → R2 → R3 → R4 → (R5 ∥ R6). Các mục đọc/chuẩn bị độc lập trong cùng một mốc có thể làm song song nếu không đụng cờ VPS-GHI; không tự chuyển mốc khi gate chưa PASS.

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

Claude ghi trực tiếp ý kiến trong COLLAB một mục P-Review: **ACCEPT / ACCEPT_WITH_CORRECTIONS / BLOCKED**, kèm diff cụ thể, evidence và SHA file đang đọc. Có thể sửa bản nháp đúng phần chưa đạt nhưng không mở thêm mục tiêu, không dùng phản biện làm lệnh RUN. GPT Host chốt sau khi đọc diff; Owner xác nhận roadmap; **chỉ sau đó mới soạn RUN Codex đầu tiên (R0 read-only)**. Nếu Claude còn bất đồng thực chất về mất mã, quyền hoặc production, Host ghi đúng một câu Owner cần quyết, không tiếp tục bằng giả đồng thuận.

## 7. Dữ kiện đã đo và chưa đo
Ngày 24/10: Git VPS agent-data, UI và workspace báo clean; GitHub main hai repo còn cũ/không protected, chứa 17 và 11 workflow; có Actions được kích hoạt theo lịch. **Chưa đo** remotes/upstreams, `docker/nuxt-repo`, commit đang chạy từng dịch vụ và các thẻ đang có quyền; bắt buộc làm tại R0. Claude P5 bổ sung: `vps-daily-20261023` = HEAD VPS agent-data (75ed0e80); agent-data đang chạy b6ebaf94 (đo 23/10). VPS có swap gần cạn, vì vậy không mặc định dùng VPS1 để chạy toàn bộ build/test.
