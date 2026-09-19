# Danh mục công cụ kết nối GitHub qua MCP — đối chiếu với hai đầu nối

Lập: Claude Chat · 2026-09-19 · theo yêu cầu Owner; GPT bổ sung bản 29 dòng; Claude rà độc lập và thống nhất số. Nguồn tham chiếu (đọc ngày 2026-09-19):
- GitHub MCP Server chính thức: https://github.com/github/github-mcp-server (README, mục Tools)
- Filesystem MCP chuẩn: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- Git MCP chuẩn: https://github.com/modelcontextprotocol/servers/tree/main/src/git

## 1. Tóm tắt cho Owner

| | Số lượng |
|---|---|
| Công cụ tham chiếu (snapshot 3 bộ chính thức, không phải "mọi công cụ trên đời") | **115** = GitHub MCP 90 + Filesystem 13 + Git 12 |
| Liên quan việc của mình (tài liệu trong 1 repo, chỉ nhánh main, không PR/Issue) | **31** |
| Không liên quan | **84** — lý do ở mục 4 |
| Cổng quyết định của Incomex | **29 năng lực người dùng** (mục 2) |
| GPT hôm nay | 🟢 11 · 🟡 11 (đã làm, chưa triển khai) · 🔴 4 · x 3 |
| Claude hôm nay | 🟢 14 · 🔴 10 · x 5 |
| Mục tiêu sau R03 | GPT 🟢 26 · x 3 — Claude 🟢 24 · x 5 — không còn ô thiếu |

x = cố ý không làm, có số quyết định: xoá (quyền Owner) · xuất tệp và nhập trực tiếp từ sandbox Claude (D10) · Owner View (R04/D08).
Công cụ đang có: GPT 37 (26 workspace/ui/vps + 11 KB) · Claude 23 (11 fs_* + read_file/write_file + 2 PG + 4 Directus + vps_status + 3 ui).

## 2. 29 năng lực — SỐ CHUẨN (trùng PROMPT R03 §2; nơi lưu lâu dài là tệp này)

**Cách chấm:** một ô GPT/Claude chỉ 🟢 khi mọi root áp dụng đều PASS. Git SSOT: GPT=`workspace`, Claude=`gh`; `ui` là mirror nên mutation=N/A(D08/R04) trừ regression read/lock; `docs` read-only; code/runtime roots ngoài catalog tài liệu. Client binding chấm riêng GPT Chat, GPT Work, Claude Chat; client khác N/A nếu chưa bind.

| # | Năng lực | Công cụ tham chiếu | GPT | Claude | Hôm nay GPT/Claude | Mục tiêu sau R03 |
|---|---|---|---|---|---|---|
| 1 | Liệt kê + phát hiện gốc và quyền | list_directory, directory_tree, get_repository_tree, list_allowed_directories | workspace_list | fs_list | 🟢/🟢 | 🟢/🟢 |
| 2 | Đọc giữ nguyên byte (BOM, CRLF, dòng rất dài, tệp vài MB) | read_text_file, read_multiple_files, get_file_contents | workspace_read, workspace_result_read | fs_read, read_file | 🟢/🟢 (BOM/CRLF chưa thử) | 🟢/🟢 |
| 3 | Tìm | search_files, search_code | workspace_search | fs_search | 🟢/🟢 | 🟢/🟢 |
| 4 | Thông tin tệp | get_file_info | workspace_stat | fs_stat | 🟢/🟢 | 🟢/🟢 |
| 5 | Thông tin thư mục + mã cây | (tham chiếu không có) | workspace_stat | fs_stat | 🟡/🔴 | 🟢/🟢 |
| 6 | Lịch sử theo path, đi theo tệp khi dời | list_commits, search_commits, git_log | workspace_log | fs_log | 🟢/🟢 | 🟢/🟢 |
| 7 | So file hoặc directory subtree giữa hai phiên bản bất kỳ | get_commit, git_show, git_diff | workspace_diff | fs_diff | 🔴/🔴 (mới so từng commit / từ bản sao lưu) | 🟢/🟢 |
| 8 | Tạo tệp, cha chưa có | write_file + create_directory, create_or_update_file | workspace_write_new | fs_write | 🟡/🟢 | 🟢/🟢 |
| 9 | Sửa từng khúc + literal replace_all có đếm/expected_count | edit_file | workspace_edit | fs_edit | 🔴/🔴 (chưa có replace_all) | 🟢/🟢 |
| 10 | Thay cả tệp có khoá | create_or_update_file (sha) | workspace_edit, workspace_transaction | fs_write, fs_transaction | 🟢/🔴 | 🟢/🟢 |
| 11 | Chép tệp | (tham chiếu không có) | workspace_copy | fs_copy | 🟢/🟢 | 🟢/🟢 |
| 12 | Chép thư mục | (tham chiếu không có) | workspace_copy | fs_copy | 🟡/🔴 | 🟢/🟢 |
| 13 | Dời/đổi tên tệp | move_file | workspace_move | fs_move | 🟢/🟢 | 🟢/🟢 |
| 14 | Dời thư mục (lưu trữ việc) | move_file | workspace_move | fs_move | 🟡/🟢 | 🟢/🟢 |
| 15 | Nhiều thao tác = 1 commit (cả cây) | push_files | workspace_transaction | fs_transaction | 🟡/🔴 | 🟢/🟢 |
| 16 | Xoá | delete_file | — | — | x/x | x/x (quyền Owner; dời vào lưu trữ) |
| 17 | Nhập tệp đính kèm | (tham chiếu không có) | workspace_import_file | — | 🟡/x | 🟢/x (D10) |
| 18 | Tải lện tệp lớn, nối tiếp được | (tham chiếu không có) | workspace_upload_* | — | 🟡/x | 🟢/x (D10) |
| 19 | Xuất/tải/đóng gói backup ra máy hoặc GDrive | read_media_file | — | — | x/x | x/x (D10) |
| 20 | Khoá/concurrency trên Git SSOT; BUSY/OVERLOADED không mutation | create_or_update_file (sha) | expected_version/head | expected_version/head | 🟡/🔴 | 🟢/🟢 |
| 21 | Gọi lại không ghi đôi | (tham chiếu không có) | operation_id | operation_id | 🟡/🟢 | 🟢/🟢 |
| 22 | Hỏng không để rác, không thư mục ma | (tham chiếu không có) | trong mọi lệnh ghi | trong mọi lệnh ghi | 🟡/🔴 | 🟢/🟢 |
| 23 | Chặn đường nguy hiểm | list_allowed_directories | trong mọi lệnh | trong mọi lệnh | 🟢/🟢 | 🟢/🟢 |
| 24 | Tên tiếng Việt không sinh đôi; hoa/thường trên Mac | (tham chiếu không có) | trong mọi lệnh | trong mọi lệnh | 🔴/🔴 | 🟢/🟢 (D09) |
| 25 | Chính sách Git/cỡ/bí mật; AI direct-GitHub ngoài 2 MCP chỉ đọc; dirty-worktree; UTF-8 | git_add, git_commit (nội bộ) | quét bí mật, trần cỡ | quét bí mật, trần cỡ | 🟡/🟢 (GitHub native còn ghi được) | 🟢/🟢 (D11, D12) |
| 26 | Độ tươi, chéo GPT↔Claude | git_status | tự kéo | tự kéo | 🟢/🟢 | 🟢/🟢 |
| 27 | Client thật nhận đúng tool/schema/metadata | (tham chiếu không có) | GPT Chat + Work | Claude Chat | cần nghiệm thu sau deploy | mỗi surface PASS hoặc N/A rõ; refresh/reconnect đúng 1 lần nếu đổi |
| 28 | Đọc bản cũ + restore forward-commit; multi-file compensation không vi phạm no-delete | git_show, get_file_contents(ref) + ghi có khoá | chưa có | chưa có | 🔴/🔴 | 🟢/🟢 |
| 29 | Đưa tài liệu GitHub sang VPS Owner View | (không thuộc FS/Git) | — | — | x/x | x/x (R04/D08) |

## 3. Công cụ mình có mà tham chiếu không có
- Vì hai AI cùng ghi một repo: mã cây, gọi lại không ghi đôi, nhiều thao tác = 1 commit, tự kéo bản mới, chặn tên sinh đôi.
- Ngoài GitHub: GPT có chạy mã trong bản sao cô lập (workspace_exec, workspace_task_*), chụp/soi trang (ui_*), sức khoẻ VPS; Claude có soi/bấm trang (ui_*), sức khoẻ VPS, đọc PG chỉ đọc, ghi Directus có duyệt.
- Đã cân nhắc và KHÔNG cần: blame từng dòng, tìm trong lịch sử theo nội dung, đọc nhiều tệp một lần, thẻ phiên bản (READY@SHA đã thay), tạo thư mục rỗng (Git không lưu).

## 4. Phụ lục — 115 công cụ tham chiếu, từng cái CẦN hay KHÔNG (số trong ngoặc = dòng ở mục 2)

A. GitHub MCP chính thức (90)
- repos (20): CẦN get_file_contents (2, 28) · create_or_update_file (8, 10) · push_files (15) · list_commits (6) · get_commit (7) · search_code (3) · search_commits (6) · delete_file (16, x quyền Owner). KHÔNG create_branch, list_branches (chỉ main) · list_tags, get_tag, list_releases, get_latest_release, get_release_by_tag (không phát hành) · create_repository, fork_repository, delete_repository, list_repository_collaborators, search_repositories (không quản trị repo khác).
- git (1): CẦN get_repository_tree (1).
- issues (9), labels (2 ngoài get_label), pull_requests (10), discussions (5): KHÔNG — thảo luận và duyệt qua COLLAB.md (đã chốt từ R10).
- actions (4), code_quality (1), code_security (2), dependabot (2), security_advisories (4): KHÔNG — repo tài liệu, không CI, không mã.
- secret_protection (2): KHÔNG bắt buộc; ĐỀ XUẤT xem xét sau như lưới an toàn cho repo công khai.
- context (3), users (1), orgs (1), stargazers (3), notifications (6), gists (4), projects (3), copilot (2), copilot_issue_intents (1), chỉ bản remote (4): KHÔNG.

B. Filesystem MCP chuẩn (13) — tất cả CẦN:
read_text_file, read_multiple_files (2) · read_media_file (19) · write_file (8, 10) · edit_file (9) · create_directory (8 — thay bằng tự tạo cha) · list_directory, list_directory_with_sizes, directory_tree (1) · move_file (13, 14) · search_files (3) · get_file_info (4, 5) · list_allowed_directories (1, 23).

C. Git MCP chuẩn (12):
CẦN git_log (6) · git_show, git_diff (7, 28) · git_status (26) · git_add, git_commit, git_reset, git_diff_staged, git_diff_unstaged (15, 25 — gộp trong mọi lệnh ghi). KHÔNG git_create_branch, git_checkout, git_branch (chỉ main).

Cách dùng: mọi lần đổi đầu nối phải chạy lại đủ 29 dòng mục 2 với cả hai phía; dòng nào không 🟢 phải có số quyết định (Dxx/Rxx).
