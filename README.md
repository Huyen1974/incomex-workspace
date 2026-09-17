# incomex-workspace

Kho làm việc CÔNG KHAI (PUBLIC từ 17/09/2026 — không commit secret; secret scanning + push protection đang bật) để Claude/ChatGPT đọc–sửa file qua đầu nối MCP "Incomex VPS" (gốc `gh`).
Commit từ GPT workspace dùng tác giả "AI via Incomex Workspace"; connector Claude hiện hữu giữ tác giả riêng. Không force-push lên `main`.

GPT dùng app "Incomex AgentData MCP — GPT Full b1gdc", root `workspace`: đọc cửa sổ nhỏ → exact edit với expected_version → commit/push → kiểm diff. File lớn hoặc HTML một dòng dùng workspace_read/search/edit; GitHub native dùng browse, PR/review và file nhỏ.

Các file `acceptance/gpt-*` là bản sao kiểm thử ngày 17/09/2026, không phải nguồn ứng dụng business. Đã kiểm file 314 KB và một dòng 2,21 MB, stale HEAD/SHA và commit chen ngang. App GPT cần Refresh để nhận đủ 20 tool; giữ nguyên URL/secret.
