# DỰ THẢO TIÊU CHUẨN — NHIỀU AI VIẾT MÃ SONG SONG
Phiên 0.1 · 23/10/2026 · CHƯA DUYỆT · không được coi là quy định có hiệu lực.

## A. Nguyên tắc thiết kế để hội đồng xét
1. **Mỗi agent có workspace độc lập** (clone hoặc git worktree/isolated sandbox), nhánh và phạm vi tệp của chính mình; có thể đồng thời làm trên cùng một repo. GitHub lưu/chuyển mã và PR, KHÔNG cung cấp máy thực thi phát triển miễn phí.
2. **Không chờ merge để bắt đầu việc độc lập.** Việc phụ thuộc mã chưa merge phải khai báo dependency, hoặc thiết kế stacked branch; không giả định cả ba nhánh tự động tương thích.
3. **Quyền thực tế hơn văn bản luật.** Agent phát triển không có admin hoặc chung token Owner; chỉ được tạo/push nhánh công việc và mở PR. Trước khi làm thật phải có bằng chứng phép thử quyền âm. Người sửa chính sách bảo vệ main độc lập với agent phát triển.
4. **Kỹ sư trưởng không auto-merge dựa vào báo 'no conflict'.** Luôn lấy main mới nhất tạo post-merge candidate, đọc diff, chạy test, chặn ngoài phạm vi, đối chiếu head SHA tại giờ nhập. Kiểm logic/test không thể bảo đảm 100% đúng chức năng.
5. **Không tự deploy sau merge.** Quyền deploy ở VPS là cổng riêng với kiểm tra, rollback; không tự động ghi ngược từ GitHub lên VPS cho tới khi source baseline đã đối soát.
6. **Dùng tiêu chuẩn Git/PR/CI/ruleset có sẵn**, tránh tự phát minh thêm nền tảng/hệ thống. Không tự dựng GitHub runner hoặc lịch mới khi chưa có yêu cầu.
7. **Actions=OFF** ở repo mã khi được quyết định; không đặt required checks phụ thuộc Actions đã tắt. Nếu cần status checks, kiểm chứng bộ kiểm bên ngoài có thể báo kết quả tới GitHub bằng actor đủ quyền, không có secrets ở repo.
8. **Đêm làm việc không có người trực** chỉ khi chứng minh được cơ chế dispatch, identity, receipt, restart/resume, quota và lỗi dừng sạch; không dựa vào một agent 'hứa' sẽ chạy nền.

## B. Mẫu chuẩn cho một nhiệm vụ mã (đề xuất, chưa chốt)
Owner chỉ cần giao: (i) mục tiêu; (ii) xong khi nào; (iii) mức ưu tiên/điều không được đụng. Host/kỹ sư trưởng phải điền phần máy trước khi đưa agent:
| Ô | Bắt buộc? | Nội dung |
|---|---|---|
| TASK_ID / Issue | Có | mã ổn định + một nguồn sự thật; ID PR liên kết |
| Goal / Acceptance | Có | kết quả cần đạt + phép thử minh chứng DoD, không chỉ 'đã code' |
| Repo + base SHA | Có | kho mã private, phiên bản bắt đầu; kiểm lại latest main lúc merge |
| Owner / Host / Chief / Worker | Có | tên vai và identity thực; tác giả không tự duyệt PR của mình |
| Allowed / Forbidden scope | Có | danh sách khu tệp/đích được sửa và thứ cấm thay đổi |
| Dependencies | Có | độc lập / phụ thuộc TASK_ID nào; ưu tiên tránh sửa cùng tệp nóng |
| Test contract | Có | lệnh unit/integration, dữ liệu giả, môi trường test, mức PASS |
| Branch / PR | Có | 1 việc=1 nhánh riêng/1 PR (hoặc lý do chia PR) |
| SLA / budget / stop rule | Có | thời hạn tối đa, giới hạn tài nguyên và điều kiện DỪNG |
| Evidence / handoff | Có | commit SHA, PR, diff, kết quả test, rủi ro, rollback, người nhận sáng |
Quy tắc chia việc: có thể chạy nhiều việc chung repo khi scope và dependency cho phép; công việc chồng API/schema/infra phải lập thứ tự hoặc người sở hữu interface trước. Hạn mức 400 dòng PR nếu dùng chỉ là tín hiệu cần xem xét, KHÔNG là chuẩn cứng.

## C. Hợp đồng ca đêm — bản nháp
- Ban ngày: Owner/Host chốt một batch N việc; mỗi việc có TASK_ID, DoD, nhánh, worker, dependency, mức quyền, giới hạn chi phí; chưa đủ thì không đưa vào batch.
- Đêm: dispatcher được phê duyệt gọi/nhắc đúng các agent có kết nối đã test; mỗi agent tự claim, lấy base, viết mã trong sandbox, test theo DoD, push nhánh, mở PR, nộp receipt. Không dùng tài khoản GitHub Owner hoặc token admin.
- Với mỗi agent: READY → STARTED → XONG (có PR và evidence) hoặc DỪNG (lý do + NEXT_TRIGGER). Không treo terminal/VPS-GHI để chờ; không tự nhận thêm việc ngoài danh sách.
- Kỹ sư trưởng: review từng PR theo hàng đợi, có thể giao lại đúng worker. Đề xuất dùng Codex làm điều phối công việc và Dot nhắc Codex; **phải chứng minh được Dot gọi/nhắc Codex thật, không giả định từ tên sản phẩm.** GPT Chat/Work/Dot cùng ghế nếu dùng chung OpenAI-main, không tăng quorum.
- Buổi sáng: một bảng tổng N việc (XONG được review/merge, XONG chờ review, DỪNG kèm blocker, phép thử PASS/FAIL, thay đổi ở main, không tự deploy). Chủ trì chỉ báo nội dung và ngoại lệ cần Owner quyết.

## D. Quy trình review/merge chuẩn — xét mọi trường hợp
0. ĐẦU VÀO: PR có task ID, worker/identity, đúng scope, DoD, test/evidence. Thiếu ⇒ trả bổ sung; không động main.
1. Kiểm actor/token quyền, commit và đường tệp: không secret, đổi luật, file cấm, mã sinh ngoài scope, dependency chưa giải quyết. Có ⇒ DỪNG hoặc xin duyệt riêng.
2. Đọc diff giữa nhánh việc và base, so với main hiện tại. Không lấy nguyên tệp cũ chép lên; nếu thay vùng mã khác nhiệm vụ phải giải thích, không im lặng chấp nhận.
3. Tạo **ứng viên merge trong môi trường tách biệt** từ main HEAD mới nhất + PR; conflict ⇒ trả worker/điều phối, không chọn ours/theirs tự động; không có conflict vẫn phải kiểm logic, API, cấu hình, data migration.
4. Chạy linter/unit/integration/security/migration checks theo rủi ro trên chính ứng viên merge; không trên nhánh cũ đơn lẻ. Kết quả kèm mã commit và log.
5. Chief kết luận:
   - NHẬN: đủ mục tiêu + test xanh + scope đúng + review khác hãng khi cần; ghi ACCEPT đúng SHA.
   - SỬA NHỎ: sai sót nhỏ không đổi mục tiêu, sửa trên nhánh PR; sửa bởi Chief phải có ghế khác review lại.
   - TRẢ SỬA: thiếu DoD/test/có lỗi sửa được; ghi lỗi ở file/dòng, kết quả mong đợi, worker sửa và nộp lại.
   - VIẾT LẠI: sai kiến trúc/sai mục tiêu/không an toàn; chỉ rõ tiêu chí không đạt và phạm vi xây lại.
   - BỎ: việc hết giá trị/hủy có thẩm quyền; đóng PR, lưu evidence, không xóa nhánh tùy tiện.
6. Trước MERGE kiểm lại SHA của main và SHA của nhánh PR. Bất kỳ thay đổi nào sau test/duyệt ⇒ quay lại bước 2–4, không nhập bản đã xét trên nền cũ. PR do Chief tự làm cần reviewer độc lập trước nhập.
7. Merge bằng cổng được GitHub cưỡng chế; xác minh main mới chứa đúng nội dung đã test, cập nhật task/biên nhận. **Không deploy cùng thao tác merge**, triển khai theo cửa production và rollback riêng.

## E. Danh sách câu hỏi PHẢI TRẢ LỜI trước khi mua Pro/GO
### E1 Quyền GitHub
- Pro cho private repository loại nào (personal hay tổ chức)? Có cho actor cụ thể ghi main bằng cách nào? Restrict who can push ở branch protection có giới hạn cho org hay không?
- Ai được tạo/sửa ruleset, disable protections, push/merge? Chủ repo và token app có bypass không? Khi tất cả agent đang đăng nhập cùng tài khoản Owner có tách được quyền thật không?
- Thử trên kho test cả push main, delete/force push, sửa rule, merge không review, merge khi status fail; phải chặn khi actor là worker.
- Required review với nhiều bot có vận hành thật không? Tắt Actions thì required checks/merge queue dùng nguồn kiểm nào? Có buộc dùng Actions không?
### E2 Workspace và phân việc
- Mỗi ghế thật sự có môi trường viết/test biệt lập ở Mac/VPS2/cloud riêng không? Dung lượng RAM/disk/concurrency tối đa là bao nhiêu?
- Một nhiệm vụ ở một repo nhưng 3 agent chung sửa tệp nóng: chia việc theo module/contract thế nào? Khi sửa cùng dòng hoặc API phụ thuộc nhau ai phân xử?
- Lúc không có Owner, actor nào có quyền khởi chạy, nhận việc, nhắc/cancel và nộp receipt? Dot→Codex thực sự có đầu ra máy nào?
### E3 Tính nguyên vẹn, nguồn mã và test
- Hai main code repo so với vps-daily và code runtime khác nhau thế nào? Có thể lấy baseline đúng không cần ghi đè? Mã vận hành chưa ở kho nào?
- Test nào bắt lỗi 'merge sạch nhưng phá API'? Ai cấp dữ liệu giả và bảo vệ production? Có đủ bản build/thử riêng hay không?
- Ai có quyền mở/merge/deploy mã cần chỉnh schema, infrastructure, quyền, bí mật? Ai xác nhận rollback?
### E4 Sản xuất và chi phí
- Tắt Actions 100% ở từng repo và lịch khởi chạy trên tất cả nhánh thế nào? Budget Actions 0 có đúng scope và hành vi không? Bằng chứng kỳ hóa đơn/giới hạn?
- Thiết kế sử dụng test ngoài GitHub mà không đổ toàn bộ tải lên VPS1, không làm gián đoạn dịch vụ hiện tại?
- Cần GitHub Pro hay mô hình org/Team để phân quyền như yêu cầu? So chi phí và số ghế thực tế; không dựa vào giá quảng cáo một người.
- Sáng hôm sau trả báo cáo gì, tỷ lệ hoàn thành tối thiểu nào qua 3 đêm thử, điều kiện dừng/pivot là gì?

## F. Bộ thử bắt buộc trước vận hành thật (đề xuất)
T1: 3 agent cùng làm ba nhánh cùng repo, sửa khác khu, lần lượt merge; tất cả tính năng ban đầu và mã mới còn đủ.
T2: Hai nhánh sửa cùng dòng → conflict được chặn; trả đúng worker với diff dễ hiểu.
T3: Hai nhánh tự merge được nhưng thay đổi logic API khiến test tích hợp lỗi → cổng từ chối.
T4: main thay đổi giữa test và merge → cổng bắt buộc kiểm lại trên HEAD mới.
T5: worker push main, force push, xóa branch bảo vệ, sửa ruleset/billing → đều bị từ chối theo ma trận quyền đã chốt.
T6: Actions OFF, push/PR không chạy workflows mới; không có required check bị treo vô hạn.
T7: mất một worker giữa đêm → receipt DỪNG, nhả tài nguyên, batch còn lại tiếp tục.
T8: PR đã nhận nhưng deploy lỗi → rollback và audit đạt; giữ main chuẩn, không tùy tiện force reset.
T9: Dot/Codex nhận/giao việc thật qua kết nối được cấp và xuất biên nhận; không có đường gọi ⇒ đánh dấu CHƯA ĐẠT.
T10: sáng Owner nhìn thấy đủ bảng batch và bằng chứng mỗi việc; không cần đọc các log dài.

## G. Thứ tự tối thiểu để hội đồng đề nghị Owner quyết
1. Xác minh luật hiện hành và bằng chứng nguồn GitHub + VPS READ-ONLY.
2. Chốt mô hình phân quyền, format giao việc, review/merge và tiêu chí pilot; hội đồng phản biện khác hãng.
3. Thử 3 agent độc lập và các ca âm trong môi trường tách biệt; có evidence, không ảnh hưởng main/production.
4. Khi GO mới tắt Actions / đổi quyền / nâng gói theo trình tự Owner duyệt. Việc mua không thay thế bước 1–3.
5. Khi pilot xanh mới đề xuất vận hành ca đêm; deploy được phê duyệt riêng.

## H. Tài liệu tiêu chuẩn để đối chiếu (GitHub Docs)
- Branch protection: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- Ruleset và điều kiện plan: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
- Quản lý GitHub Actions settings: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository
- Required checks và PR: https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks
- Giá chính thức: https://github.com/pricing
- Các con số throughput/PR và giả định VPS2 trong đề xuất Claude là giả thuyết cần đo, KHÔNG là cam kết sản xuất.
