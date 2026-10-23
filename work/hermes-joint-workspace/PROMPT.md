# HJW N3 · P368 · Một thẻ, hai cổng
RUN_ID: HJW-HERMES-TWO-GATES-20261023-01
STATUS: DRAFT_NOT_READY · chưa STARTED · chưa được sửa production.
Host: GPT Chat · Executor_Surface: Codex · Write_Path: Incomex MCP workspace_* cho hồ sơ; approved VPS apply-v0/DOT hiện có cho runtime. Không ghi Git/repo bằng SSH.

Owner chuyển quyết định GPT Host P368 sau phản biện Claude P367. Chỉ chạy khi Host ghi READY đúng full Git SHA cuối chạm file này và Owner giao RUN cho Codex. Một RUN, hai pha, một KQ cuối có kết quả riêng từng pha; không tự phát RUN tiếp. Mục tiêu: dùng danh tính Linux/MCP/Google hiện có, khóa sudo/root và đường đọc GSM, trả quyền COLLAB hợp lệ; không thêm gateway, Guard, helper hay hệ quản lý.

## S0 · Đọc, đo và chốt delta trước mutation
Đọc AGENTS.md → root COLLAB (VPS-GHI) → HJW Bảng/§1–3/roadmap 0.9, 0.17/P363–P368 → PROMPT này; đọc mã updater và bộ canh hiện hành. Xác minh READY/Owner RUN đúng SHA, 0 RUN HJW active; read-gate Write_Path PASS mới ghi STARTED theo DROOT31 rồi PRE. Không nhận READY RUN04. N2 OpenAI Dot tách riêng, không sửa profile/roster/route của N2.
Đo journal sudo tối đa 30 ngày cho đúng 6 lệnh systemctl start/restart/reset-failed của hermes-gateway.service và hermes-serve.service; đối chiếu caller, số lượt, cửa sổ log thực có và mã /usr/local/sbin/hermes-safe-update. Không suy “0 dùng” từ log bị xoay/mất. Chứng minh updater root hiện có độc lập với HERMES_UPDATE_UNITS; chỉ khi chứng minh được mới thu grant. Cần quyền root/helper mới hoặc chưa đủ bằng chứng an toàn ⇒ DỪNG, trả Owner quyết, không tự tạo.
PRE ghi trạng thái dịch vụ/đường chat-terminal-MCP-Workspace-cron-updater, UID/group/quyền, IAM metadata, footprint/diff/hash và backup thật từng pha. Recheck DROOT30 trước từng nhóm mutation, chỉ giữ VPS-GHI trong thao tác đã được cấp, không giữ để chờ người. Điều 30/31, Config/Code Guard và đường apply hiện có phải cho phép đúng delta; bị từ chối thì DỪNG, không lách Guard hoặc sửa bằng chứng cũ. #21 rollback FAIL lịch sử giữ nguyên, không dùng reconstructed backup làm original hoặc lấy periodic xanh thay POST.

## S1 · Pha 1: hai cổng
1. Khi S0 chứng minh đủ: thu hồi đúng grant HERMES_UPDATE_UNITS của hermes trong /etc/sudoers.d/90-hermes-update, giữ quyền khác của VPS. Kiểm sudoers hợp lệ và Hermes không còn sudo grant hay đường root tương đương qua group/socket đã kiểm; không thử khai thác nâng quyền. Hermes mất quyền tự yêu cầu start/restart/reset-failed hai unit; updater root và systemd phục hồi sẵn có phải còn hoạt động. Không nâng phiên bản Hermes trong RUN này.
2. Xác minh Google IAM, quyền mượn/impersonate service account và đường gián tiếp qua MCP/dịch vụ hiện có bằng metadata/mã. Không có grant Hermes cần thu hồi ⇒ không sửa IAM. Nếu phát hiện grant/đường đọc mới chưa có delta rõ trong P368 ⇒ DỪNG trước thay quyền đó, báo Owner; không tự mở phạm vi.
3. Gắn đúng 4 nhóm kiểm boolean vào bộ canh hiện có, giữ nhịp và kênh báo hiện có: (a) UID Hermes không đọc credential đặc quyền: root gcloud, agent-data.env, Google credential mount, nginx secrets, hermes-key-fetch; (b) profile Google/ADC của Hermes không có credential/token/default ADC; (c) unit/env/config Hermes không tham chiếu Google/ADC credential; (d) Hermes không thuộc nhóm có quyền Docker, không truy cập Docker socket. Đo bằng quyền thực của Hermes, chỉ xuất đúng/sai và đường đã che; không dump env, token, giá trị secret hoặc gọi GSM access payload. Thiếu quyền đo ≠ PASS.
Mỗi nhóm có ca hợp lệ và ca sai trong fixture/bản sao của bộ test, không đặt credential thật hoặc mở quyền production để thử. Có bằng chứng bốn nhóm PASS trong nhịp canh thật trước Pha 2. Ghi checkpoint P1 và backup P2 riêng; lỗi P1 thì lùi đúng delta P1 qua đường hợp lệ, báo lỗi/cửa chưa khóa.

## S2 · Pha 2: bỏ hạn chế thừa
Thay write_scope Hermes bằng đúng một mẫu work/*/COLLAB.md; INV19 phải kiểm đúng một wildcard và post-image Guard còn sống. Giữ loại trừ done-tasks và kiểm đường chuẩn hiện có. Không mở ghi file khác. Giữ post-image Guard, kiểm task/role, chống giả Host/READY/KQ/ASSIGN/RESULT; cron không người trực vẫn chỉ đọc. Không sửa Guard để vượt phép kiểm.
Chạy lại đủ 33 negative tests hiện có (tests/continuation/test_hjw_post_guard.py tại nguồn Agent Data VPS), giữ nguyên ý nghĩa các ca cấm. Thêm cross-task: ghi chú dữ liệu đúng vai được phép tại COLLAB việc khác; giả Host/READY/KQ hoặc sửa vùng bảo vệ tại việc khác vẫn bị chặn; đường lồng/ngoài work/*/COLLAB.md bị chặn. Dùng fixture cho ca âm, không phá hồ sơ thật.
Hermes thật, đúng danh tính của mình, ghi một ghi chú dữ liệu hợp lệ vào work/vps-clean-20-10-26/COLLAB.md, marker HJW-TWO-GATES-WRITE-20261023-01; PRE phải chứng minh đích ngoài 5 file cũ. Không chốt/đổi Bảng/READY/KQ của việc đó. Nếu đích đã đóng hoặc quyền nhiệm vụ không còn hợp lệ thì DỪNG tại gate, không tự chọn đích khác. Đọc lại commit/author/receipt qua workspace; executor mượn key hoặc tự ghi thay không tính PASS. Nếu P2 lỗi, chỉ lùi P2 về backup đầu P2; giữ P1 đã đạt, kiểm lại hai cổng.

## S3 · POST và KQ
Đạt khi: không sudo grant; không mở đường đọc GSM trực tiếp/gián tiếp; 4 nhóm canh PASS; chat, terminal, MCP, Workspace, cron RO và updater hiện có bình thường; ghi COLLAB thật thành công, sửa sai bị Guard chặn; Điều 30/31/footprint/PRE-POST/rollback thật và fleet same-or-better có receipt. Dùng phép smoke updater hiện có không nâng cấp; chưa thử sống thì ghi CHƯA THỬ, không giả PASS. Hai cổng không bảo vệ khi kẻ tấn công đã có toàn quyền root, không hứa giấu mọi runtime key Hermes được cấp dùng.
Ghi kết quả và tham chiếu evidence đã che vào chính HJW COLLAB.md, cập nhật Bảng/roadmap N3 đúng phần đã đạt, một KQ XONG hoặc DỪNG với P1/P2 riêng, nhả VPS-GHI và dọn fixture/tác vụ tạm. Không sửa audit cũ, tài liệu PG, B/C/E, D10, N4–N6; không sửa Guard/proof để che FAIL, không thêm RUN. Có blocker thì ghi đúng chủ và NEXT_TRIGGER, kết thúc lượt.

STEP_WALK_V1 (SLA tính từ khi từng bước bắt đầu; quá hạn ghi checkpoint/DỪNG, không giữ phiên chờ):
| Bước | Ai · trigger | SLA | Evidence | Hỏng: ai biết/khi nào · bước kế |
|---|---|---|---|---|
| S0 | Codex · READY đúng SHA + Owner RUN | 30 phút | read-gate, log ≤30 ngày, updater độc lập, PRE | Host/Owner ngay trong KQ DỪNG; đạt → S1 |
| S1 | Codex · S0 PASS + VPS-GHI | 30 phút | sudo/IAM, 4 nhóm canh, rollback P1 | Host/Owner ngay qua kênh hiện có; đạt → S2 |
| S2 | Codex + Hermes thật · P1 PASS | 30 phút | 33 ca âm + cross-task, ghi thật/receipt | Host/Owner ngay; lỗi lùi P2, giữ P1 → S3 |
| S3 | Codex · xong hoặc lỗi pha | 15 phút | POST/đường lùi, KQ P1/P2, trả khóa | Host/Owner nhận KQ ngay; Host nghiệm thu |
