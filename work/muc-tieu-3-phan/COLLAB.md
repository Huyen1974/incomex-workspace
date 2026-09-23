# COLLAB — muc-tieu-3-phan

Tên việc: Mục tiêu 3 phần
Host: Claude Chat · Host_ID: CLAUDE-MT3-260923-A
HTML chính: (chưa có)

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN (nguyên văn lời User, 2026-09-23)

### 1. Mục tiêu
> Ở phần mục tiêu giờ hơi lộn xộn. Có thể các bạn hiểu ban đầu và cập nhật trong quá trình làm. Nhưng kết quả cuối cùng là nội dung vừa dài, vừa lộn xộn và đôi khi lại không thống nhất (không diễn đạt được hết các mong muốn của user.
>
> Tôi muốn việc này (mục tiêu) chia ra thành 3 phần:
>
> 1. Mục tiêu (ngắn gọn, chỉ đạo từ user viết thật ngắn) Cái này User sẽ rà soát thường xuyên.
> 2. Thế nào là hoàn thành? Cái này cũng rất ngắn. User chỉ đạo gõ vào cho khúc triết.
> 3. Các chi tiết cần đạt. Các bạn muốn ghi gì cũng được. AI hay ghi dài, các bạn tư đọc với nhau. Nhưng tôi muốn làm rõ mục 1 và 2 để làm kim chỉ nam. (Tất nhiên là những việc này có thể thay đổi. Tức là nếu 1 việc dài những gì đã xong rồi, thì có thể xóa đi cho ngắn. Chị để lại các mục tiêu sắp tới. Còn chi tiết AI tự ghi, tự đọc với nhau (nhưng Host kiểm soát)
>
> Cái này phải rõ ràng cấu trúc từ Gh chứ không chỉ UI ở phía VPS.

### 2. Thế nào là hoàn thành
- Mọi việc trong repo có §0 đúng ba phần; phần 1 và 2 ngắn và là lời Owner. *(đề xuất — chờ Owner gật)*
- Mở một việc trên web là thấy ngay phần 1 và 2; chi tiết và vòng cũ gập lại. *(đề xuất — chờ Owner gật)*
- AI mở việc mới là tự viết đúng khuôn này, không ai phải nhắc. *(đề xuất — chờ Owner gật)*

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Khuôn §0 chuẩn, tên mục con cố định để máy đọc được: `### 1. Mục tiêu` · `### 2. Thế nào là hoàn thành` · `### 3. Chi tiết cần đạt` · `### Vòng trước`. Dòng `Xác nhận User:` giữ nguyên ở đầu §0 (A9 không đổi).
- Sở hữu: phần 1–2 là lời Owner — AI không tự sửa chữ, chỉ được đề xuất và đánh dấu *(đề xuất — chờ Owner gật)*; phần 3 Host quản, được cắt gọn khi hạng mục đã XONG (giữ một dòng tóm tắt + mã commit); `### Vòng trước` giữ các khối A0 cũ, không xoá.
- Parser + view đọc đúng bốn mục; việc chưa chuẩn thì cảnh báo chứ không vỡ; tìm kiếm vẫn quét toàn bộ §0.
- Di trú toàn bộ việc hiện có (cả `done-tasks`) sang khuôn mới, không sửa chữ Owner, không xoá lịch sử.

### Vòng trước
- Chưa có vòng trước.

## Trạng thái
- 2026-09-23 · Mở việc theo chỉ đạo Owner; Host Claude Chat; Executor dự kiến Codex/GPT Work. PROMPT `MT3-20260923-01` đã soạn.
- READY@7192b994fd69c5a94707f8c0ad42d59e464e7873 · Host Claude Chat · đã đối chiếu Git log: commit cuối chạm `work/muc-tieu-3-phan/PROMPT.md`; sẵn sàng RUN `MT3-20260923-01` cho Codex/GPT Work.
- Owner 23/09/2026: **CHỐT GIAO**. Executor_Surface=`Codex/GPT Work`. Write_Path bắt buộc: runtime VPS=`SSH/deploy path hiện hữu theo README §11`; tài liệu `incomex-workspace`=`workspace_*` với expected version/head. Trước mutation phải read-gate đúng cả hai đường; thiếu/bind fail thì DỪNG, không tự đổi sang Git/native hay GitHub→VPS. Scope chỉ MT3; không triển khai deep-link/MMIM/HVU khác ngoài việc di trú riêng §0 của các task theo PROMPT.

## Kết quả RUN MT3-20260923-01
KQ@MT3-20260923-01 XONG

- Gate: commit cuối chạm PROMPT = `7192b994fd69c5a94707f8c0ad42d59e464e7873`, khớp READY; hai Write_Path đọc/ghi được trước mutation.
- Runtime VPS (SSOT): parser/view tại `/opt/incomex/docker/nuxt-repo/scripts/hvu-b2/sync.py` và `scripts/hvu-b2/ui/app.vue`; commits `75ffea3`, `50acede`. Chỉ tách bốn trường §0, fallback cảnh báo cho §0 cũ, và hiển thị hai phần đầu mở sẵn. `(chưa có)` ở HTML chính được nhận đúng là không có tài liệu.
- Luật A0 trong `AGENTS.md`: commit `938f87cdd2f85081154eaf24691b008ecf7c009c`.
- Di trú §0 (commit `1e32fa47b76163c530e432477f72285e8dd9e48e`; giữ nguyên câu chữ vòng hiện hành ở `3918254ce30659a8fc3e1f9239f762391988a1f7`): `gsm-access-audit`, `hermes-joint-workspace`, `hpml-view-for-user`, `mcp-token-argv`, `mow-mot-moit-mout`, `muc-tieu-3-phan`, `vps-clean-20-9-26`, `done-tasks/jev-integration`, `done-tasks/mcp-workspace`. Chỉ §0 đổi; A0 cũ giữ nguyên ở `Vòng trước`. Phần 1/2 chưa có lời Owner chốt được ghi rõ là đề xuất.
- Kiểm thử: `Ran 21 tests in 9.262s — OK` (fixture cũ/mới, B2/B3 regression); Nuxt build PASS; HTTP 200 cho `/knowledge/modules` và view tĩnh; webhook tự nhận revision `3918254ce30659a8fc3e1f9239f762391988a1f7`, 9/9 task structured, 0 lỗi. Mở trực tiếp MT3 và việc đã xong JEV trên web: hai mục đầu hiện sẵn, Chi tiết/Vòng trước gập; tiến độ và tình trạng vẫn hiển thị.
- Bằng chứng/rollback VPS: `/opt/incomex/work/muc-tieu-3-phan/` có `regression.log`, `build.log`, các bản `sync.py.before`, `app.vue.before`, `view.html.before`. Có thể khôi phục ba bản này rồi build lại; tài liệu Git khôi phục bằng commit đảo hai commit di trú nếu cần. Không đổi gateway, MCP, presence, retention hoặc cơ chế webhook/backstop.

## Owner cần quyết
- —
