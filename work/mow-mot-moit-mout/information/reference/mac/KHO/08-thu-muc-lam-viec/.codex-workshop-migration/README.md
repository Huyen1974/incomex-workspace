# XƯỞNG VẼ INCOMEX

`/opt/incomex/docs/mcp-writes` là nguồn gốc duy nhất để Owner, Claude Cowork,
Codex và Claude Code cùng thiết kế:

- giao diện;
- luồng nghiệp vụ;
- hợp đồng thông tin;
- dữ liệu mẫu và tài liệu nghiệm thu.

## Quy tắc ngắn

1. Đọc `AGENTS.md` trước khi sửa.
2. Không tự sửa phần Owner đã chốt.
3. Không tạo một bản UI “mới hơn” ở thư mục khác.
4. Cấu trúc dùng nhiều nơi phải có một renderer/source; nhân bản bằng dữ liệu.
5. Trước và sau thay đổi lớn, ghi mỏ neo:

   ```bash
   mcp-writes-git snapshot "ly do"
   ```

6. Timer Git tự chạy mỗi 5 phút là lưới an toàn, không thay thế nghiệm thu.
7. Không push repo này. Đây là sổ quay lui cục bộ trên VPS.

## Xưởng vẽ và hệ thống chạy thật

- Xưởng vẽ trả lời: UI trông thế nào, người thao tác ra sao, nghiệp vụ và hợp
  đồng thông tin là gì.
- Repo ứng dụng/PG trả lời: code chạy thật, quyền, API, bảng và triển khai.
- Khi chuyển một thiết kế sang hệ thống chạy thật, ghi lại commit nguồn của
  xưởng. Không sửa ngược thiết kế gốc chỉ để chiều theo chi tiết triển khai.

## Đường dẫn

- Xưởng trên đĩa: `/opt/incomex/docs/mcp-writes`
- Preview: `https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/`
- New MODT: `https://vps.incomexsaigoncorp.vn/admin-new-modt`
- Git local: `/usr/local/bin/mcp-writes-git`

`ui-preview` trong xưởng chỉ là symlink tương thích cho yêu cầu cũ; nó trỏ về
chính thư mục này và không phải bản sao.
