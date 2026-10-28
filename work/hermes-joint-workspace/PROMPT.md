# HJW — Codex rà mã Gateway: "xưng danh mới được ghi" (CHỈ ĐỌC)

RUN_ID: HJW-DECLARATION-GATE-AUDIT-20261028-10
STATUS: READ_ONLY_AUDIT_ONLY · KHÔNG THI CÔNG · chỉ chạy sau khi Host có READY đúng SHA và Owner giao trực tiếp
Executor_Surface: Codex trong ChatGPT/Codex Desktop/Work (KHÔNG bắt buộc Codex CLI)
Read_Path: GitHub Huyen1974/incomex-workspace + repo mã Huyen1974/agent-data-test và các nguồn Gateway hiện hữu được phép đọc
Write_Path: chỉ `workspace_*`/capability D12 đã bind để ghi báo cáo P/KQ vào `work/hermes-joint-workspace/COLLAB.md`; cấm GitHub native write
Scope: duy nhất HJW · xem AGENTS A2/A5/A6, README D12, HJW COLLAB §0, Bảng, P439–P443. Không mở task mới.

## Mục tiêu — đúng hai câu hỏi
1. **AI đến cửa ghi có tự biết phải khai tên không?** Nếu không khai, có thể trả `DECLARATION_REQUIRED` rõ từng trường, ví dụ và cách gọi lại ngay trong **một** lượt trả lỗi, tuyệt đối không sửa dữ liệu?
2. **Có thể làm điều đó một lần về chính sách** cho mọi đường ghi repo hiện có (Workspace/FS/upload/import/async) mà không dựng server/DB/đường quyền mới? Cần sửa những file/choke point nào, mất công sức ở mức nào?

## S0 · Đọc mã hiện hành, không giả một gateway vật lý
- Kiểm tra nguồn đang thật sự phục vụ và phiên bản được pin; chỉ đọc: `agent_data/workspace_tools.py` (master_profiles, auth, tools/call, tool schemas), `agent_data/hvu_signals.py`, `agent_data/workspace_idempotency.py`, schema/adapter của `workspace_upload_*`, `workspace_import_file`, `workspace_task_*`, phần `fs_*` thuộc Claude/Incomex VPS. Nguồn nào chưa có quyền đọc ghi **UNKNOWN + cách tìm đúng chủ**, không bịa.
- Đối chiếu GitHub native direct write với Gateway D12 (ruleset bảo vệ main), không sửa ruleset.
- Lập bảng NGẮN: `đường ghi | server/entrypoint | schema tools/list | chung pre-write hook? | có operation_id? | actor đã xác thực? | lỗi khi thiếu khai báo | GAP`.
- Kiểm mọi biến thể source mutation: create/edit/copy/move/transaction, upload/import/commit, async/background, và mọi đường có thể gọi ghi dù tên không bắt đầu `write`. Chỉ rà tính phủ, không chạy phép thử live.

## S1 · Đề xuất hợp đồng tối thiểu
- Ưu tiên **xưng danh NGAY TRONG lệnh ghi**, không có bước gọi xin token trước. Mỗi lệnh chỉ thêm **một tên AI tự khai** `declared_actor` (task/path và idempotency giữ theo tham số đã có nếu phù hợp).
- Không coi `operation_id` là authentication token. Kiểm xem có dùng mã hiện hữu làm vé giao dịch/receipt một lần được không, những tool nào còn thiếu.
- Bắt buộc làm cho AI tự hiểu từ cả **mô tả tool** và **lỗi**. Ví dụ contract:
  `error=DECLARATION_REQUIRED; required_field=declared_actor; example=gpt-live; instruction="Gọi lại đúng công cụ ghi này, thêm declared_actor, giữ nguyên nội dung và operation_id phù hợp"; mutation=none`.
- Nếu schema validation chặn trước khi vào handler, chỉ ra chỗ phải thay schema/dispatcher để lỗi vẫn hữu dụng; đừng để một AI phải tự đọc AGENTS hoặc hỏi Owner mới biết cách sửa.
- Với khai báo hợp lệ: trả `declared_actor` + `authenticated_actor` (theo credential thực) + transaction/commit receipt; actor Git đã xác thực phải được giữ, không thay bằng tên tự khai.
- Phân biệt rõ **ghế làm việc** và **phiếu/quorum A2**. Tất cả AI đã qua cửa xác thực có thể xưng tên làm việc; không cộng phiếu cứng vì khai tên.

## S2 · Chọn một cách ngắn nhất, chỉ trên giấy
- So sánh tối đa 2 cách tận dụng code hiện hành: (A) thêm/chuẩn hóa một field khai báo cho mọi tool ghi qua schema+dispatcher; (B) dùng một envelope/metadata chung đã có nếu chứng minh đủ an toàn và phổ quát.
- Chọn cách ít nơi chứa logic nhất, không đặt biệt lệ mỗi AI, không tạo "Master thẻ" lớn, DB, listener, cron hoặc API mới. Nếu `fs_*` và `workspace_*` là hai server, nói rõ có cần 2 điểm móc mỏng theo một hợp đồng chung không.
- Nêu danh sách **file dự kiến chạm, số điểm sửa, các suite/test sẵn có, một kế hoạch lùi, độ khó nhỏ/vừa/lớn**, không hứa số ngày chưa có cơ sở. Thử mô phỏng lỗi bằng test plan, **chưa chạy test mutation**.
- Bộ nghiệm thu phải gồm: tool mô tả trước; thiếu tên → lỗi tự hướng dẫn, 0 ghi; tên đúng → 1 write/receipt; retry không ghi đôi; `fs_*` và `workspace_*` giống nhau; tool mới về sau không đi vòng; giữ nguyên key/profile, D12, A2; code/commit không leak secrets.
- Riêng GPT Live 409: xác minh đủ bằng chứng trực tiếp hay chỉ suy luận từ ruleset; nêu **đường đúng qua Workspace** cho Live khi tool thật có bind, không tự gọi Live từ Codex hay mở khoá main.

## Kết quả và điểm dừng
- Ghi đúng một mục `P444 · Codex · Audit xưng danh Gateway` trong HJW COLLAB qua D12 và `KQ@HJW-DECLARATION-GATE-AUDIT-20261028-10 XONG|DỪNG` theo bằng chứng; nêu rõ `SOURCE_HEAD`, commit, 1 phương án ưu tiên, chỗ sửa, còn UNKNOWN và ONE NEXT_TRIGGER cho Owner/Host quyết thi công.
- **CẤM trong RUN này:** sửa mã, cấu hình, tool schema thực, MCP, env, keys, Cloud plugin permission, production, nginx, VPS, Gemini, GitHub ruleset, AGENTS/A2, cấp phiếu/vote, RUN nền, thí nghiệm ghi thử ngoài một P/KQ report SSOT. Không giữ terminal/job chờ.
- Báo Owner 3 câu ngắn: phương án đơn giản nhất là gì, có mấy nơi thực sự phải sửa, điều gì còn cần chốt trước thi công.

STEP_WALK_V1: S0 Codex đọc source đúng HEAD → S1 đối chiếu entrypoint/error/schema → S2 chọn minimal delta + test plan → S3 ghi P444/KQ vào repo & trả cờ; lỗi bất kỳ điểm nào thì ghi UNKNOWN/DỪNG, không tự sửa.
