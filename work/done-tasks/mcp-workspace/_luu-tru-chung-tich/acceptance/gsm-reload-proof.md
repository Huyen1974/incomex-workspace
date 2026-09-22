# Bằng chứng GSM là nguồn khoá

2026-09-17: bản nạp tạm của deploy key trên VPS (tmpfs) đã bị xoá, không còn bản sao nào trên đĩa;
trợ lý host khởi động lại → script nạp khoá lấy lại từ GSM (`MCP_WORKSPACE_GH_DEPLOY_KEY`) → file này được push thành công.

2026-09-17, Claude Chat (claude.ai) tự nghiệm thu: đọc file này qua fs_read rồi sửa đúng dòng này qua fs_edit — commit do chính Claude Chat đẩy lên.
