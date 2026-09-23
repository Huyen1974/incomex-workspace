# PROMPT — HVU-DEEPLINK01 · DRAFT FOR CLAUDE REVIEW · NO RUN

## 0. Trạng thái / gate
Đây là **yêu cầu bổ sung trong task hiện có** `work/hpml-view-for-user/`. Không tạo task mới.

Bản này **chưa giao Claude Code CLI**. Thứ tự bắt buộc:
1. GPT Host tập hợp yêu cầu.
2. Claude Chat review/phản biện trực tiếp bản này.
3. Host xử lý các P của Claude.
4. Chỉ khi GPT Host + Claude Chat **đồng thuận, không còn P OPEN/OWNER liên quan**, Host mới đổi prompt sang READY và phát RUN cho Claude Code CLI.

Trước bước 4: **NO RUN / NO AGENT MUTATION**.

## 1. Mục tiêu
Làm URL của `https://vps.incomexsaigoncorp.vn/knowledge/modules` phản ánh đúng vị trí User đang xem, để chỉ cần gửi URL là người/AI mở được **đúng task → đúng tab/khu vực → đúng bảng/mục con**, không phải giải thích lại vị trí.

Giữ tương thích deep-link hiện có:
`?task=<task-id>`

Mở rộng tối thiểu bằng các mã/ID ổn định, ví dụ:
`?task=mow-mot-moit-mout&view=step&section=mot&detail=MOT01`

Tên tham số cụ thể có thể Claude đề nghị điều chỉnh nếu code hiện tại đã có convention tốt hơn, nhưng phải giữ nguyên mục tiêu: URL đủ để định vị chính xác và có thể copy/share.

## 2. Nguyên tắc xử lý
- Ưu tiên **thay đổi frontend nhỏ nhất**, tận dụng `URLSearchParams` + History API/cơ chế route hiện hữu.
- Không redesign Task html view.
- Không đổi database, MCP/connector, sync/presence/B2/B3 nếu không có bằng chứng bắt buộc.
- Không suy vị trí bằng text hiển thị/STT; dùng **ID/code ổn định**.
- Khi User đổi tab/khu vực/mục con, URL cập nhật tương ứng mà không reload toàn trang nếu không cần.
- Khi mở URL trực tiếp, UI phải khôi phục đúng vị trí được mã hóa.
- URL sai hoặc ID đã mất phải fallback an toàn, không làm hỏng trang.
- Back/Forward phải phục hồi hợp lý nếu cơ chế hiện tại cho phép bằng thay đổi nhỏ.
- Giữ `task=<id>` là khóa task hiện hành.

## 3. Ranh giới hệ thống
- Runtime viewer trên VPS là SSOT theo AGENTS/README §11; read-gate code production trước khi sửa.
- GitHub task này chỉ giữ yêu cầu/evidence; không dùng repo copy để ghi đè runtime.
- Không sửa nghiệp vụ/Step của `mow-mot-moit-mout` từ prompt HVU.
- Nếu cần child/iframe relay để truyền vị trí xuống HTML công việc, chỉ bổ sung phần tối thiểu tương thích sandbox hiện tại; không nới security như `allow-same-origin`.
- Không mở task phụ cho deep-link.

## 4. Acceptance tối thiểu
A1. `?task=<id>` cũ vẫn mở đúng task.
A2. URL có task + tab/view mở đúng tab.
A3. URL có thêm section/detail mở đúng khu vực/mục con.
A4. Thao tác trên UI làm URL thay đổi đúng.
A5. Copy URL sang cửa sổ mới vẫn định vị đúng.
A6. Back/Forward không làm state lệch hoặc vỡ.
A7. Query/ID không hợp lệ fallback an toàn.
A8. Không regression Master list, search, Now/Done, task detail, B2/B3/presence.
A9. Không thay đổi public MCP contract/auth và không làm yếu sandbox/security.

## 5. Yêu cầu Claude Chat review trước RUN
Claude Chat chỉ review, **không thực thi**. Cần trả lời ngắn:
- Contract URL trên có đủ để đạt mục tiêu “gửi link là định vị được ngay” chưa?
- Có phần nào đang phức tạp quá so với code production thực tế không?
- Có regression/security edge case nào phải thêm vào acceptance không?
- Đề nghị ACCEPT hoặc CHANGE cụ thể; ghi P vào `COLLAB.md`.

Chỉ sau khi Host xử lý review và đạt đồng thuận mới xác định Executor_Surface/Write_Path/read-gate và chuyển READY cho Claude Code CLI.

Kết thúc DRAFT: **NO RUN**.
