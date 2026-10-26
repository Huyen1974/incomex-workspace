# CODEX — HJW-N2-DOT-S1-CLOSE-20261026-02

RUN_ID: HJW-N2-DOT-S1-CLOSE-20261026-02
STATUS: DRAFT_NOT_READY. Chỉ chạy sau Host READY đúng last-touch SHA + Owner RUN mới.
Executor_Surface: Codex trên Mac · Task: work/hermes-joint-workspace.
Write_Path: hồ sơ qua workspace_*/fs_* theo D12; phần mã ứng viên VPS trong worktree thử độc lập theo Đ30/31 và cờ VPS-GHI nếu có ghi lên VPS. KHÔNG ghi Agent Data/container production.

## MỤC TIÊU & CỬA VÀO

Chỉ hoàn tất S1 bị DỪNG tại P410, để có một candidate N2 hoàn chỉnh, kiểm chứng được, sau đó mới sử dụng +1 forward recreate Agent Data đã được Owner cho phép nhưng CHƯA DÙNG. KHÔNG triển khai Agent Data, không thay nginx/route, không mở Plugin Dot, không cấp SSH/sudo/GSM, không đổi Gmail. Git giữ PROMPT R2 trước tại commit 7e220733f812599a4236be968f66dc91602be568.

Giữ đúng mục tiêu Owner N2 trong HJW §1–§3: Dot có actor openai-dot riêng, đủ kết nối nghiệp vụ, ghế phản biện có receipt, báo cáo cho Owner bằng thoại. Cơ chế SSH/root-equivalent trong P407/P408 vẫn thuộc hợp đồng N2 sau này, với rủi ro ROOT_SSH_OWNER_APPROVAL_NOT_ENFORCED; không triển khai ở RUN S1-only. Dot làm Host, gọi Codex/Work tự động, N4–N6 để sau. N1 Cloud đã đạt; N3 Hermes CLOSED_WITH_LIMITS.

**Không coi báo cáo B1/ý kiến Reviewer là RUN.** P410 KQ DỪNG đã đóng RUN cũ. Owner GO +1 recreate có từ R2, không phải quyền cho RUN_ID mới tự chạy khi chưa Host READY/Owner dispatch.

## S0 — READ-GATE VÀ CÔ LẬP

Đọc AGENTS, HJW COLLAB mục tiêu/Bảng/roadmap/P404–P411, PROMPT hiện hành, nguồn TQT P38 và P410. Kiểm HEAD, STOP/ALERT, Executor_Surface/Write_Path và Guard. Khi chỉ đọc không giữ VPS-GHI; nếu cần sửa candidate/build/thử trên VPS thì lấy cờ CAS trước, có giới hạn tài nguyên và nhả ngay sau checkpoint. Nếu task khác giữ cờ => KQ DỪNG/nhả phiên, không tranh máy, không chờ terminal. Không gọi thêm API AI thuê bao, không chạm database/live services để thử.

## S1 — CHỐT CA TQT HỢP ĐỒNG THẬT, KHÔNG TEST CHẠY VÒNG TRÒN

Nguồn chính: work/tools-quy-trinh/COLLAB.md P38 và các CHECK004/005/006, codec packed-history/HISTORY_REFERENCE của view đã ghim, guard hiện hữu FIELD-identity, RESULT-P01 và checkpoint. P410 báo 3 phép thử KQ lịch sử đã PASS; ca thứ tư bị TRIAL_CONTRACT_REJECTED do fixture chưa hợp hợp đồng, KHÔNG phải bằng chứng production hỏng.

1. Lấy observed/signed fixture hợp lệ theo nguồn/đường đọc đã được duyệt, chỉ READ-ONLY; không tạo giả Owner approval, RESULT-P01, FIELD-identity, checkpoint hay sửa validator/policy/Guard để ép PASS. Xác minh history/codec/checkpoint đúng phiên.
2. Kiểm TQT với CÙNG điều kiện/tệp đầu vào đối với baseline conn03a đang dùng và candidate (không phải production). Nếu cả hai từ chối do fixture không hợp đồng, ghi INCONCLUSIVE_FIXTURE với chứng cứ và phân loại TQT thành nợ fixture có chủ; không gọi đó là TQT PASS. Chỉ được coi là **không hồi quy so với baseline** nếu diff chứng minh không đổi cổng TQT/trial/ACL và các negative tests liên quan vẫn PASS.
3. Nếu baseline hợp lệ/PASS mà candidate FAIL, hoặc thay đổi candidate chạm đường dùng chung trial/ownership làm mất bảo vệ, phải BLOCK S1; sửa đúng mã/fixture theo nguồn đã duyệt rồi thử lại có giới hạn. Nếu không tạo được fixture hợp lệ và đường TQT có thể bị ảnh hưởng bởi candidate => BLOCK, không đoán an toàn.
4. Giới hạn bộ thử như evidence P38: ưu tiên chạy trực tiếp CHECK004/codec ở vùng thử; đừng lặp container 1–2 GiB vô hạn. Từ chối hợp đồng là lỗi dữ liệu đầu vào, không giải bằng tăng RAM tùy tiện.

## S2 — KHÉP MA TRẬN ĐỦ CONNECTOR TRƯỚC RECREATE

Không coi “37 tools Agent Data” đồng nghĩa đầy đủ mọi connector. Từ P399/P404/P410, mỗi họ phải có một dòng: current source/route, cloud-usable?, Dot credential/actor từ server, read/write/execute, phép âm, cấu hình nằm ở image hay ngoài image, tình trạng PASS/CHƯA THỬ/CHƯA THỂ, bằng chứng.

Các họ bắt buộc: Workspace/KB/RAG/upload/transaction/exec/UI, Directus + PG/schema, Graph/Neo4j read, Lark, VPS status/operational, JEV, Gmail/Drive/Calendar/GitHub/Canva và đường chính thức Codex Cloud/Work/Mac/voice.

- Với Directus/PG và Lark đang dùng nhãn/credential cố định, không coi thêm URL là định danh Dot. Xác minh cách dùng các twin/gateway và server-side actor/scope đang có; không chia khóa Claude để giả identity.
- Với Graph stdio/SSH loopback, chứng minh có cloud route tương thích hiện hữu hoặc ghi blocker chính xác; KHÔNG dựng bridge, reverse proxy hoặc server MCP mới ngoài scope.
- Với vendor Plugin/voice/SSH cloud chỉ Owner/Dot thật mới xác minh được: phân loại CLIENT_ONLY_PENDING; không bắt phải có client khi chưa cấp Dot route. Gmail đã được đặt Allow read actions / ask before writes, không đổi thêm và không gửi thử.
- Đưa TẤT CẢ delta server-side phải ở trong image vào cùng candidate trước khi dùng +1 recreate. Delta độc lập (Plugin native/user-only) phải ghi rõ để không giả thiếu restart. Nếu connector bắt buộc vẫn cần image lần thứ hai/chưa biết giải pháp => S1_BLOCKED, không consume recreate.

## S3 — CANDIDATE CỐ ĐỊNH, THỬ TRÊN MÃ VÀ IMAGE TẠM

Baseline live theo P410: agent-data conn03a release 2b14c2a, image rollback digest ở P410; giữ KB/CONN03A hiện hành, không lấy checkout Hermes chưa phát hành. Candidate đầu vào R2 là local commit 8bd6d6c21e2336e610e2ace80c0219f7bcebd255, ref candidate/hjw-n2-recover-20261026, parent 2b14c2a. Rà mọi diff trong candidate (Queue.finish/terminal/cancel/recovery/ownership/worker import workspace_runtime.py) và 8 cấu hình đã sao lưu.

Nếu sửa candidate, commit mới **chỉ trong nhánh thử**, ghi SHA và danh sách diff đúng scope; không sửa production hoặc tự đổi source release đã ghim trong PROMPT này. Đo lại 63 regression trọng tâm, test rộng hiện có (không lấy 63 thay full suite), trial/TQT baseline differential, cross-profile denial, không rò argv/secret, lifecycle completed/failed/cancelled, replay/idempotency và hồi quy KB 5 profile cũ. Có thể build image tạm trong vùng thử khi tài nguyên cho phép, ghi image digest. Chỉ cấp nhãn S1_CANDIDATE_READY khi source SHA và image digest được pin, các suite bắt buộc đủ, ma trận S2 đã xác nhận delta không cần forward recreate ngoài 1 lần đã được Owner cho.

Không đổi health/Guard baseline để che lỗi. Nếu test fail, nguồn thiếu hoặc phải đổi thiết kế lớn, dừng với đúng một blocker và đề nghị patch nhỏ, không tự mở task mới.

## S4 — KẾT QUẢ VÀ TRẢ MÁY

Ghi P/KQ cùng Bảng/roadmap tại HJW bằng gateway, không ghi mật khẩu/secret lên repo. Báo:
- TQT: VALID_PASS hoặc BASELINE_SAME_FIXTURE_INVALID (không được tính PASS) hoặc REGRESSION_BLOCKED, evidence có thể kiểm.
- Các họ connector: SERVER_READY / CLIENT_ONLY_PENDING / BLOCKED (lý do cụ thể và owner kỹ thuật).
- Candidate source SHA/image digest và full regression vs baseline; nếu chưa đủ ghi NOT_DEPLOYABLE.
- Lượt +1 forward recreate: **UNUSED**, image/config production không đổi, Guard/health/footprint thật; trả VPS-GHI, không job thử nền.
- Một NEXT_TRIGGER cho Host chốt bước triển khai cuối khi S1 đủ; nếu còn BLOCKED, nêu đúng chỗ cần sửa, không đề nghị Owner duyệt lại GO.

Nếu tất cả S1 đạt, KQ XONG của RUN S1-only, **không phải N2 FULL_PASS**; Host sẽ soạn READY cho một RUN triển khai/đo Dot thật, chỉ dùng +1 forward recreate và thao tác Owner gom một lần.

## STEP_WALK_V1

| Bước | Ai/trigger | Evidence phải đo | Nếu không đạt |
|---|---|---|---|
| S0 | Codex · Owner RUN + Host READY | HEAD, role, cờ/Guard, scope | DỪNG sạch |
| S1 | Codex · S0 PASS | observed TQT + so baseline/candidate | phân biệt invalid fixture / regression |
| S2 | Codex · S1 rõ | full connector matrix + 1-recreate dependency | BLOCKED đúng họ |
| S3 | Codex · S2 rõ | candidate SHA/digest, suites, rollback | NOT_DEPLOYABLE |
| S4 | Codex · kết thúc | POST, KQ, trả cờ, NEXT_TRIGGER | DỪNG + 1 blocker |

CẤM: tự recreate/restart Agent Data, nginx hay service production; tạo key/route/plugin/live Gmail, root/GSM/SSH cho Dot trong lượt này; sửa/giảm trial validator/Guard; dùng task Codex hoặc server fixture để ghi PASS T1–T6 Dot thật; thay scope sang Hermes/GitHub/Graph/Directus production; đặt lịch hoặc giữ máy chờ Owner.
