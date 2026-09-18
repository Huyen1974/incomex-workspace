# AGENTS.md — Incomex Workspace

**Hợp đồng chuẩn của repo này nằm trong [`README.md`](README.md), mục "Shared Workspace Contract — v1.1". File AGENTS.md chỉ là CỬA VÀO.**

Ở đây không có luật riêng. Cần thêm hoặc sửa luật thì sửa chính hợp đồng trong `README.md` — đừng viết luật vào file này, đừng tạo file luật thứ ba.

Vào đúng cửa:

1. **Đọc hợp đồng trước khi ghi.** §0 nói rõ có BA đường ghi — GPT qua VPS, Claude qua VPS, và GitHub native ghi thẳng — và đường nào thiếu chốt chặn nào.
2. **Nguồn hiện hành là GitHub trên đúng branch/ref đang làm**, không phải bản chat hay bản local cũ.
3. **Trước khi sửa: lấy version/SHA hiện tại. Đã đổi → KHÔNG ghi đè; đọc lại và hoà giải.** (§3)
4. **Qua VPS không có công cụ xoá.** `delete_file` của GitHub native chỉ dùng khi chủ duyệt từng lần; dọn dẹp = rename vào `_luu-tru-chung-tich-*/`. (§7)
5. **File lớn thì đọc theo cửa sổ, không nạp cả file; giữ nguyên tên Unicode.** (§8)
6. **Chỉ báo PASS khi đã gọi thật**, và nói rõ bằng chứng đến từ backend hay từ client thật. (§10)
