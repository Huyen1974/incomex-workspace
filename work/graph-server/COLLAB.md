# COLLAB — graph-server
Tên việc: Graph Server — Business × JEV × Code

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — chỉ đạo trực tiếp ngày 24/09/2026: tạo `work/graph-server`, đưa nội dung lên để hội đồng góp ý, theo bốn mục tiêu dưới đây. Chưa duyệt công nghệ hoặc triển khai VPS.

### 1. Mục tiêu
Nguyên văn User, giữ thứ tự ưu tiên:
1. Tạo ra các mối quan hệ về Graph đối với business (khi các mối quan hệ là hữu hạn, chứ không phải quan hệ vô hạn kiểu mạng xã hội.
2. Kết hợp tốt nhất với Jev để đảm bảo Graph truyền thống và Jev bổ sung tốt nhất cho nhau theo các hướng dẫn mới nhất của typesaveai và nhà sáng lập của nó **Diogo Almeida**.
3. Định hướng ứng dụng các skill, frame chính thức của Jev để có thể tận dụng xu thế phát triển thêm Jev trong tương lai (ý là, Jev là 1 xu hướng hiệu quả, giờ mới chỉ bắt đầu, Incomex cần chuẩn bị để không tụt hậu trong xu hướng này)
4. Tự Dựng lại mối quan hệ về về code để các Agent/ AI có thể hiểu nhanh hơn khi hệ thống phức tạp lên.

Bối cảnh nguyên văn User: “Gốc rễ nhất là chúng ta đã dọn VPS còn hơn 50GB để cho việc này.”

### 2. Thế nào là hoàn thành
Phạm vi lượt giao hiện tại, nguyên văn User:
- “tạo 1 task tên work/graph-server”
- “Đưa các nội dung lên đây theo đúng quy đjnh để hội đồng bắt đầu có ý kiến.”

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Chỉ tạo hai file trong task: COLLAB.md điều phối và view.html là tài liệu chính duy nhất. Không tạo PROMPT, file review, bản nháp hoặc pipeline phụ.
- Giữ đủ các nhóm lựa chọn đã thảo luận; phân biệt nguồn kiểm chứng, đề xuất và điều chưa kiểm. Đề xuất cũ không phải quyết định Owner.
- Giữ hướng PostgreSQL/pgvector. Yêu cầu một PostgreSQL vật lý duy nhất chưa được xác nhận; không đồng nhất điều đó với một nguồn chuẩn cho mỗi dữ liệu.
- Giữ đúng thứ tự mục tiêu. Schema/tiêu chí nghiệm thu/kiến trúc trong HTML là đề xuất chờ review, không thêm mục tiêu User.
- Tái dùng việc jev-integration đã đóng; không mở cổng/skill nội bộ trùng chức năng. Dung lượng hơn 50GB là thông tin Owner, đối chiếu báo cáo VPS ngày 23/09; chưa phải số đo mới của lượt này.
- Chưa cho phép cài đặt, quét dữ liệu/mã thật, migration, restart, xóa hoặc đổi cấu hình/model/gateway. Các bài kiểm trong tài liệu chỉ để hội đồng đánh giá.

### Vòng trước
Chưa có — mở việc lần đầu theo lệnh Owner. Nội dung chat trước là đầu vào, không phải quyết định kiến trúc đã duyệt.

Host: GPT Chat
Host_ID: GPT-GRAPH-20260924-A — ID điều phối do Host tự đặt.
Owner giao mở việc: 2026-09-24
HTML chính: `view.html`
Owner View: https://vps.incomexsaigoncorp.vn/knowledge/modules?task=graph-server
Executor_Surface: GPT Chat — biên tập hồ sơ.
Write_Path: Incomex MCP full all 2 → workspace_* → root workspace, main.

## Dòng hiện hành
GS | HỒ SƠ REPO VÒNG 1 XONG · OWNER VIEW CHECK DỪNG (AUTH) | Chưa chốt công nghệ; chưa có PROMPT/READY/RUN | NEXT: Claude + Hermes có thể review trực tiếp repo; Host chưa được phép báo Owner View PASS cho tới khi kiểm được nội dung sau đăng nhập.
- Based_on mở việc: `37ae3fe22bc37894242506e4477b055d32fdc540`; GS02 hòa giải trên HEAD hiện hành, commit chen ngang không chạm task này.
- Đã đọc AGENTS.md → COLLAB.md gốc → README.md → work/README.md; áp khuôn MT3 hiện hành.
- Nghiên cứu cập nhật 24/09/2026: TypeSafe official skill/blog; pgvector; AGE; Cognee; Graphiti; Hindsight; Neo4j vector; GraphRAG. Link nguồn ở `view.html` §12.
- Owner View check sau commit `3b909e0c22d554433fdee8c49498c5cbb3cf1701`: gọi đúng URL chuẩn `/knowledge/modules?task=graph-server`, HTTP shell 200 nhưng Directus trả 401 và UI dừng ở Login; không thấy nội dung/revision ⇒ **DỪNG nghiệm thu Owner View, không báo PASS giả**. Repo/diff vẫn PASS.
- Áp: SAME_COMMIT.

## Quyết định Owner
- D01 · 2026-09-24 · Owner cho phép mở đúng task graph-server, tập hợp nội dung để hội đồng góp ý, giữ bốn ưu tiên và bối cảnh VPS. Không có quyết định chọn stack/cài đặt trong lệnh này.

## Ý kiến hội đồng
### P01 · GPT Host · OPEN — giả thuyết vòng 1, chờ Claude/Hermes phản biện
- Based_on: tài liệu Owner + nguồn kiểm ngày 24/09/2026; Scope: `view.html` §1–§11.
- Đề nghị: giữ PostgreSQL/pgvector; so A (Cognee+Neo4j+PGVector) với C (AGE+PGVector) trước, D làm baseline; B/Graphiti kéo lên nếu temporal/supersession chi phối. Hindsight = memory layer, không mặc định canonical graph.
- JEV Reference: `gen-dec-1790221175-ygPaecOXX76U0e4Y1yAe`; A-vs-C confidence 0.30 nên KHÔNG coi là chọn công nghệ; `canonical_constraints` probability 0.99/confidence 0.98 dùng để ưu tiên acceptance test.
- Lý do: mục tiêu #1 yêu cầu relation hữu hạn/kiểm soát; TypeSafe official skill yêu cầu code giữ hard rules/workflow, JEV chỉ làm semantic judgment trên bounded candidates.
- P01 không phải consensus.

### Yêu cầu Reviewer vòng 1
- Đọc A0 rồi `view.html`; phản biện Q01–Q07, A–E, boundary canonical fact/JEV judgment/agent memory, code graph deterministic/semantic.
- Fact kỹ thuật phải có source/runtime; bounded decisions có thể dùng JEV theo AGENTS A5.
- Không tạo file review mới; ghi Pxx ngay tại mục này theo A3.

## Con trỏ
- Luật: ../../AGENTS.md; kỹ thuật và Owner View: ../../README.md §11–12.
- Nền JEV: ../done-tasks/jev-integration/COLLAB.md và SKILL.md.
- Bối cảnh VPS: ../done-tasks/vps-clean-20-9-26/COLLAB.md.
- Gateway Agent: ../hermes-joint-workspace/COLLAB.md — việc độc lập.

## Owner cần quyết
- —
