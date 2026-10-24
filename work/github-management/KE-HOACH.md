# KẾ HOẠCH THỰC HIỆN — github-management · V0.1 · 24/10/2026

**TRẠNG THÁI: DRAFT / YÊU CẦU CLAUDE PHẢN BIỆN / KHÔNG ĐƯỢC RUN.**

Tài liệu này là *bảng đầu việc cụ thể* cho Codex và Claude Code CLI. [ROADMAP.md](ROADMAP.md) giữ các mốc và điều kiện chốt, [COLLAB.md](COLLAB.md) giữ duy nhất mục tiêu Owner, trạng thái và quyết định. Không tạo thêm hệ điều hành công việc; dùng lại hội đồng, luật AGENTS, Issue/PR và DOT/Codex hiện có.

## 1. Mục tiêu, vai trò và giới hạn

**Đích ưu tiên:** mở không gian để 3–5 agent viết mã song song trên hai kho đang có, không tranh cờ VPS-GHI khi viết mã. Claude Code CLI tập trung kiểm tra, yêu cầu sửa và merge từng PR. **Đích cuối:** Owner giao một batch nhiệm vụ buổi tối, các agent nhận và làm khi Owner vắng mặt; sáng có báo cáo từng việc, không tự deploy vô điều kiện.

| Vai | Chịu trách nhiệm chính | Ranh giới |
|---|---|---|
| Owner | Phê duyệt roadmap, quyền và các bước thay đổi production; quyết mục tiêu nghiệp vụ | Không phải duyệt từng commit hoặc canh ca đêm |
| GPT Host | Phân mốc, chốt PROMPT, nhận KQ, xử lý ý kiến Claude, báo Owner | Không giả quyết định Owner hay tự ghi READY trước đủ cổng |
| Codex (executor) | Khảo sát, chuẩn bị luật ở 2 repo, đối soát mã VPS, dựng đường CI/CD và ghi evidence | Không tự review hoặc nhập mã do chính Codex viết khi cần reviewer độc lập |
| Claude Code CLI (Chief/Reviewer) | Phản biện kế hoạch; duyệt PR, test ứng viên merge trên nền mới nhất, NHẬN/SỬA/TRẢ/BỎ | Không tự bỏ Guard, không coi merge sạch là chức năng đúng |
| Các worker (Codex, Hermes, Claude, ghế khác đã cấp quyền) | Mỗi việc một workspace/branch/PR, có biên nhận/test | Không ghi trực tiếp nhánh chính, không giữ VPS-GHI để phát triển |
| DOT (mốc sau) | Nhắc/điều phối Codex và lấy receipt theo cơ chế hội đồng đã có | Không mặc nhiên được gọi agent nếu chưa có đường thực thi được kiểm chứng |

**Giới hạn cứng trong giai đoạn lập kế hoạch:** không tắt Actions, không thay quyền/secret, không pull/reset/force-push hay sửa main GitHub, không đổi Git remote, container hoặc deploy VPS, không mở public hai repo, không chi tiền. Mọi thay đổi thực tế chỉ bắt đầu sau Claude phản biện, GPT chốt, Owner duyệt và RUN hợp lệ.

## 2. Danh mục đầu việc giao Codex theo đúng thứ tự

| ID | Bước | Công việc chi tiết | Chứng cứ hoàn thành |
|---|---|---|---|
| R0.1 | Kiểm Git read-only | Kiểm từng vùng mã VPS: branch, HEAD, git status, upstream/remote (ẩn URL chứa credential), các tệp được theo dõi/chưa theo dõi, hook/luồng đồng bộ | Manifest đường nguồn → SHA → repo đích, trạng thái sạch/bẩn, điểm UNKNOWN |
| R0.2 | Xác định mã đang phục vụ | So sánh Git worktree với container/image, build artifact, scripts đang chạy, không suy chỉ từ HEAD | Bảng mã nguồn thực chạy, file hash và các phần nằm ngoài Git |
| R0.3 | Đường backup và Actions | Kiểm cron/timer/hooks VPS→GitHub, 17+11 workflow trên 2 repo, run theo lịch, đường deploy cũ và quan hệ monitor/backup | Phân loại KEEP / MIGRATE / DISABLE cho mỗi job, không phá canh thiết yếu |
| R1.1 | Chuẩn bị tắt | Xử lý những workflow có chức năng thiết yếu và các required checks đang phụ thuộc Actions | Báo cáo tác động và đường thay thế, không sinh job trùng |
| R1.2 | Disable Actions | Tắt cấp repo ở agent-data-test và web-test; chỉ xử lý run đang chạy theo RUN được duyệt, không xóa YAML, không phục hồi SSH root secret | Cài đặt Disabled, push/PR/schedule không có job mới; usage mới 0 |
| R2.1 | Khung luật AI | Codex tạo trên nhánh chuẩn bị: AGENTS/README/CONTRIBUTING, Issue/PR templates, chuẩn worker/chief, scope và quy tắc đọc trước | Người mới đọc đầu vào biết cách nhận, code, test, nộp PR mà không hỏi lại |
| R2.2 | Cấp thẻ và quyền | Kiểm danh tính riêng thật; thử worker tạo branch/PR, bị chặn ghi/xóa/force push main, bị chặn gỡ ruleset; Chief được nhập hợp lệ | Ma trận quyền và phép thử âm với các danh tính thực |
| R2.3 | Quyết plan GitHub | Nếu private Free không hỗ trợ hard-lock cần thiết: trình Owner phương án Pro và chi phí chính xác trước khi cấp quyền viết main | GO/NO-GO quyền; không dùng luật trên giấy hoặc CODEOWNERS thay khóa GitHub |
| R3.1 | Ranh giới 2 repo | Liệt kê module/path của Agent Data/RAG/MCP và Web/Nuxt/Directus UI; chỉ định chủ, đánh dấu DOT/Graph/Guard/OS config ngoài phạm vi | Ma trận path/module → owner repo hoặc OUT-OF-SCOPE |
| R3.2 | Chuẩn mã từ VPS | Xác minh mã *thực đang chạy*, loại secret/.env/data/dump/build sinh/backup, lưu ref main cũ, tạo baseline-candidate riêng và hash manifest | Ứng viên mã mới đúng nguồn, nhánh/tag cũ phục hồi được |
| R3.3 | Đối soát hai chiều | So khớp cây tệp candidate với mã đang chạy và delta phát sinh trong lúc chuẩn bị; kiểm tác động route/tool/config | File diff rõ và danh sách DRIFT=0 hoặc chưa đạt; không kéo GitHub xuống VPS |
| R4.1 | 3 agent song song | Giao 3 nhiệm vụ độc lập từ candidate, mỗi agent một clone/worktree/branch và PR; ghi thời điểm nhận/hoàn tất để đo tắc nghẽn | 3 receipt, 3 workspace, 3 PR của 3 worker thực |
| R4.2 | Test merge | Chief so diff/scope trên HEAD đích mới nhất; tạo merge candidate, unit/regression/integration test, xử lý conflict và stale base | Ít nhất 2 PR đạt DoD, không làm mất mã cũ; có PR bị lỗi phải trả đúng lý do |
| R4.3 | Thử CD ngoài Actions | Build/test trong môi trường tách biệt cùng kiến trúc đích khi cần; dry-run và staging, rollback, xác minh nguồn SHA | CI PASS, CD staging/dry-run PASS, Actions 0; không giả nhận đã deploy production |
| R5.1 | Chuyển vào main | Chỉ khi Owner GO: đưa baseline/PR được duyệt thành *forward commit* trên main, giữ lịch sử/tag cũ, kiểm ruleset thực | Main mới đúng hash, old main vẫn phục hồi, dev không thể ghi main |
| R5.2 | Đường deploy xuống VPS | Chỉ lấy release SHA đã phê duyệt qua cổng deploy; PRE backup, POST health/Guard, rollback thực | Source SHA = deployed SHA; không còn lối kéo nhánh tùy ý |
| R5.3 | Đổi chiều sync an toàn | Chỉ ngắt VPS→GitHub mirror cũ sau khi xác minh mã GitHub và runtime khớp, bảo toàn backup PG/Qdrant/Directus/Drive | Không có hai job đồng bộ ghi đè; phục hồi mã và dữ liệu được phân định |
| R6.1 | Tự động giao ca đêm | Nối DOT→Codex→worker bằng hội đồng hiện có, kiểm claim/receipt/timeout/cancel và độc lập từng job | Batch được giao khi Owner không online, lỗi một việc không chặn việc khác |
| R6.2 | Nghiệm thu ca đêm | Chạy thử batch 3–5 nhiệm vụ, chief review từng PR và báo cáo lúc sáng | Số việc XONG/SỬA/TRẢ/BỎ; từng PR/SHA/test; không cần người thức canh |

**Thứ tự phụ thuộc:** R0 → R1 → R2 → R3 → R4 → R5 → R6. Các mục đọc/chuẩn bị độc lập trong cùng một mốc có thể làm song song nếu không đụng cờ VPS-GHI; không tự chuyển mốc khi gate chưa PASS.

## 3. Phân loại mã dự kiến tại R3 — phải đo rồi mới chốt
- **agent-data-test:** backend Agent Data, RAG/ingest/search, công cụ MCP thuộc Agent Data và các test liên quan. Không đưa dữ liệu PG/Qdrant, secret, backup hay OS runtime.
- **web-test:** Nuxt/UI, giao diện Directus và tích hợp ứng dụng web, test frontend. Không đưa cơ sở dữ liệu, core RAG hay mã vận hành chưa phân chủ.
- **Ngoài phạm vi trước khi khảo sát:** DOT runtime, Graph Server, nginx/systemd/Guard/compose hoặc scripts dùng chung không được tự nhét vào repo bất kỳ. Ghi danh mục nợ riêng, không tự mở repo thứ ba.

**Không xóa main cũ:** sao lưu ref/tag và manifest trước; chuyển cây mã bằng commit mới tiến lên, không reset/force push. Không công khai lịch sử repo đang private khi chưa kiểm toán. Mã runtime không đồng nghĩa với git HEAD; phải đo image/config đang phục vụ.

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
| G2 trước merge candidate | Baseline và nguồn runtime được xác minh, test/DoD sẵn, Chief độc lập | Snapshot lệch mã chạy hoặc thiếu test quan trọng |
| G3 trước main/deploy | Owner GO, test merge/staging/rollback PASS, archive còn phục hồi | Không ghim được SHA, branch cũ có thể được kéo nhầm |
| G4 trước ca đêm | Cơ chế DOT/Codex/agents gọi được thật, có biên nhận và giới hạn, trạng thái DỪNG sạch | Chỉ là kế hoạch hoặc phải có Owner canh |

Khi fail, Codex báo KQ DỪNG + NEXT_TRIGGER, trả mọi lock; không tự phát sinh dịch vụ, cron, key hay bước mới. Công việc đang phục vụ trên VPS vẫn hoạt động theo đường cũ cho tới R5 GO và POST/rollback xác nhận.

## 6. Đề nghị Claude phản biện — một vòng, đi thẳng vào điểm quyết định
Claude Reviewer đọc AGENTS.md → COLLAB §0/Bảng/P3/P4 → ROADMAP.md → tài liệu này. Kiểm sáu câu hỏi: (1) R0→R1 không làm mất backup/monitor? (2) Khóa main private/Pro đúng quyền thực? (3) R3 mã nguồn từ runtime và cách giữ lịch sử có chuẩn? (4) R4 ba agent/merge stale/các test thật? (5) R5 deploy một SHA, kiểm rollback, chặn luồng ngược? (6) R6 reuse hội đồng/DOT, có receipt, không giả tự động?

Claude ghi trực tiếp ý kiến trong COLLAB một mục P-Review: **ACCEPT / ACCEPT_WITH_CORRECTIONS / BLOCKED**, kèm diff cụ thể, evidence và SHA file đang đọc. Có thể sửa bản nháp đúng phần chưa đạt nhưng không mở thêm mục tiêu, không dùng phản biện làm lệnh RUN. GPT Host chốt sau khi đọc diff; Owner xác nhận roadmap; **chỉ sau đó mới soạn RUN Codex đầu tiên (R0 read-only)**. Nếu Claude còn bất đồng thực chất về mất mã, quyền hoặc production, Host ghi đúng một câu Owner cần quyết, không tiếp tục bằng giả đồng thuận.

## 7. Dữ kiện đã đo và chưa đo
Ngày 24/10: Git VPS agent-data, UI và workspace báo clean; GitHub main hai repo còn cũ/không protected, chứa 17 và 11 workflow; có Actions được kích hoạt theo lịch. **Chưa đo** remotes/upstreams, code container thực tế và tập hợp backup ngược; điều đó bắt buộc làm tại R0. VPS có swap gần cạn, vì vậy không mặc định dùng VPS1 để chạy toàn bộ build/test.
