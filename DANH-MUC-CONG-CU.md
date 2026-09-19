# Danh mục công cụ kết nối GitHub qua MCP — đối chiếu với hai đầu nối

Lập: Claude Chat · 2026-09-19 · theo yêu cầu Owner. Nguồn chuẩn (đọc ngày 2026-09-19):
- GitHub MCP Server chính thức: https://github.com/github/github-mcp-server (README, mục Tools)
- Filesystem MCP chuẩn: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- Git MCP chuẩn: https://github.com/modelcontextprotocol/servers/tree/main/src/git

## 1. Tóm tắt cho Owner

| | Số lượng |
|---|---|
| Công cụ chuẩn cho GitHub qua MCP (3 bộ chính thức) | **115** = GitHub MCP 90 + Filesystem 13 + Git 12 |
| Liên quan việc của mình (tài liệu trong 1 repo, chỉ nhánh main, không PR/Issue) | **31** |
| Không liên quan (PR, Issue, Actions, Gist, thông báo, Project, sao, Copilot, nhánh, phát hành…) | **84** — lý do ở mục 4 |
| 31 công cụ chuẩn liên quan quy về | **26 năng lực chuẩn-derived**; audit người dùng bổ sung LARGE/RESUMABLE, HISTORICAL RESTORE và OWNER-VIEW PUBLISH BOUNDARY → **29 năng lực** |
| GPT hôm nay | 🟢 15 · 🟡 8 (đã làm, chưa triển khai) · 🔴 1 · x 2 |
| Claude hôm nay | 🟢 16 · 🔴 7 · x 3 |
| Sau R03 (đã READY, chưa chạy) | GPT 🟢 24 · x 2 — Claude 🟢 23 · x 3 — không còn ô thiếu |

x = cố ý không làm theo quyết định (xoá là quyền Owner; D10 không mở cửa HTTP mới).
Công cụ đang có: GPT 37 (26 workspace/ui/vps + 11 KB) · Claude 23 (11 fs_* + read_file/write_file + 2 PG + 4 Directus + vps_status + 3 ui).

## 2. Bảng năng lực — 26 dòng từ chuẩn + 3 dòng đặc thù Incomex

> Lưu ý: con số 115 là snapshot tham chiếu của ba server/repo chính thức tại ngày đọc, **không phải “mọi công cụ MCP trên đời”**. GitHub MCP cấu hình được theo toolset/tool và remote có tool bổ sung; các server tham chiếu cũng thay đổi theo thời gian. Cổng quyết định của Incomex là 29 năng lực người dùng bên dưới, không phải số tool bên ngoài.

| # | Năng lực | Công cụ chuẩn tương ứng | GPT | Claude | Hôm nay GPT/Claude | Sau R03 |
|---|---|---|---|---|---|---|
| 1 | Liệt kê thư mục | list_directory, list_directory_with_sizes, directory_tree, get_repository_tree | workspace_list | fs_list | 🟢/🟢 | 🟢/🟢 |
| 2 | Đọc tệp | read_text_file, read_multiple_files, get_file_contents | workspace_read, workspace_result_read | fs_read, read_file | 🟢/🟢 | 🟢/🟢 |
| 3 | Tìm | search_files, search_code | workspace_search | fs_search | 🟢/🟢 | 🟢/🟢 |
| 4 | Thông tin tệp | get_file_info | workspace_stat | fs_stat | 🟢/🟢 | 🟢/🟢 |
| 5 | Thông tin thư mục + mã phiên bản cây | (chuẩn không có) | workspace_stat | fs_stat | 🟡/🔴 | 🟢/🟢 |
| 6 | Lịch sử | list_commits, search_commits, git_log | workspace_log | fs_log | 🟢/🟢 | 🟢/🟢 |
| 7 | So bản | get_commit, git_show, git_diff | workspace_diff | fs_diff | 🟢/🟢 | 🟢/🟢 |
| 8 | Tạo tệp (cha chưa có) | write_file + create_directory, create_or_update_file | workspace_write_new | fs_write | 🟡/🟢 | 🟢/🟢 |
| 9 | Sửa từng khúc | edit_file | workspace_edit | fs_edit | 🟢/🟢 | 🟢/🟢 |
| 10 | Thay cả tệp có khoá (không ghi đè mù) | create_or_update_file (sha) | workspace_edit, workspace_transaction | fs_write, fs_transaction | 🟢/🔴 | 🟢/🟢 |
| 11 | Chép tệp | (chuẩn không có) | workspace_copy | fs_copy | 🟢/🟢 | 🟢/🟢 |
| 12 | Chép thư mục | (chuẩn không có) | workspace_copy | fs_copy | 🟡/🔴 | 🟢/🟢 |
| 13 | Dời/đổi tên tệp | move_file | workspace_move | fs_move | 🟢/🟢 | 🟢/🟢 |
| 14 | Dời thư mục (lưu trữ việc) | move_file | workspace_move | fs_move | 🟡/🟢 | 🟢/🟢 |
| 15 | Nhiều thao tác = 1 commit (cả cây) | push_files | workspace_transaction | fs_transaction | 🟡/🔴 (tệp 🟢) | 🟢/🟢 |
| 16 | Xoá | delete_file | — | — | x/x | x/x (quyền Owner; thay bằng dời vào lưu trữ) |
| 17 | Nhập tệp từ chat (đính kèm, tệp lớn) | (chuẩn không có) | workspace_import_file, workspace_upload_* | — | 🟢/x | 🟢/x (D10: giao GPT) |
| 18 | Xuất tệp ra để xử lý | read_media_file | — | — | x/x | x/x (D10) |
| 19 | Khoá đồng thời (tệp/cây/head) | create_or_update_file (sha) | expected_version, expected_head | expected_version, expected_head | 🟡/🔴 (phần cây) | 🟢/🟢 |
| 20 | Gọi lại không ghi đôi | (chuẩn không có) | operation_id | operation_id | 🟡/🟢 | 🟢/🟢 |
| 21 | Hỏng giữa chừng không để rác, không thư mục ma | (chuẩn không có) | (trong mọi lệnh ghi) | (trong mọi lệnh ghi) | 🟡/🔴 | 🟢/🟢 |
| 22 | Chặn đường nguy hiểm (.., tuyệt đối, symlink, chồng lấn) | list_allowed_directories | (trong mọi lệnh) | (trong mọi lệnh) | 🟢/🟢 | 🟢/🟢 |
| 23 | Tên tiếng Việt không sinh đôi (NFC/NFD) | (chuẩn không có) | (trong mọi lệnh) | (trong mọi lệnh) | 🔴/🔴 | 🟢/🟢 (D09) |
| 24 | Chính sách cỡ/nhị phân/bí mật | (chuẩn không có) | quét bí mật, trần cỡ | quét bí mật, trần cỡ | 🟢/🟢 | 🟢/🟢 (D11: gh chỉ tệp chữ) |
| 25 | Độ tươi (luôn đọc bản mới nhất) | git_status | (tự kéo) | (tự kéo) | 🟢/🟢 | 🟢/🟢 |
| 26 | Chat nhận đúng bộ công cụ | (chuẩn không có) | 37 tool | 23 tool | 🟢/🟢 | kiểm lại theo tool count + input schema + description/annotations + build/fingerprint |
| 27 | Upload lớn/resumable | (chuẩn không có) | workspace_upload_* | — | 🟢/x | 🟢/x (D10) |
| 28 | Đọc lịch sử + khôi phục an toàn một tệp hiện hữu | git_show/get_file_contents(ref) + write guarded | **chưa có đường server-side restore** | **chưa có đường server-side restore** | 🔴/🔴 | phải PASS trong R03; forward commit, không reset/force, không relay file lớn qua model |
| 29 | Publish tài liệu GitHub SSOT → VPS Owner View | (không thuộc FS/Git chuẩn) | copy/move hiện chỉ 1 root | fs_* hiện tách root | N/A/N/A | **N/A(R04/D08)** — lớp Owner View kế tiếp phải làm server-side, không coi là thiếu R03 |

## 3. Công cụ mình có mà chuẩn không có
- Vì hai AI cùng ghi một repo: mã phiên bản cây, gọi lại không ghi đôi, nhiều thao tác = 1 commit, tự kéo bản mới, chặn tên sinh đôi.
- Ngoài GitHub: GPT có chạy mã trong bản sao cô lập (workspace_exec, workspace_task_*), chụp/soi trang (ui_*), sức khoẻ VPS; Claude có soi/bấm trang (ui_*), sức khoẻ VPS, đọc PG chỉ đọc, ghi Directus có duyệt.

## 4. Phụ lục — 115 công cụ chuẩn, từng cái CẦN hay KHÔNG

A. GitHub MCP chính thức (90)
- repos (20): CẦN get_file_contents (2) · create_or_update_file (8, 10) · push_files (15) · list_commits (6) · get_commit (7) · search_code (3) · search_commits (6) · delete_file (16, x quyền Owner). KHÔNG create_branch, list_branches (chỉ dùng main) · list_tags, get_tag, list_releases, get_latest_release, get_release_by_tag (không phát hành) · create_repository, fork_repository, delete_repository, list_repository_collaborators, search_repositories (không quản trị repo khác).
- git (1): CẦN get_repository_tree (1).
- issues (9), labels (2 ngoài get_label), pull_requests (10), discussions (5): KHÔNG — thảo luận và duyệt đi qua COLLAB.md, không qua PR/Issue (đã chốt từ R10).
- actions (4), code_quality (1), code_security (2), dependabot (2), security_advisories (4): KHÔNG — repo tài liệu, không CI, không mã.
- secret_protection (2: get_secret_scanning_alert, list_secret_scanning_alerts): KHÔNG bắt buộc; ĐỀ XUẤT xem xét sau như lưới an toàn cho repo công khai.
- context (3), users (1), orgs (1), stargazers (3), notifications (6), gists (4), projects (3), copilot (2), copilot_issue_intents (1), chỉ bản remote (4: create_pull_request_with_copilot, get_copilot_space, list_copilot_spaces, github_support_docs_search): KHÔNG.

B. Filesystem MCP chuẩn (13) — tất cả CẦN, đã quy về 26 năng lực:
read_text_file (2) · read_multiple_files (2) · read_media_file (18) · write_file (8, 10) · edit_file (9) · create_directory (8 — thay bằng tự tạo cha, không cần lệnh riêng vì Git không lưu thư mục rỗng) · list_directory, list_directory_with_sizes, directory_tree (1) · move_file (13, 14) · search_files (3) · get_file_info (4, 5) · list_allowed_directories (22).

C. Git MCP chuẩn (12):
CẦN git_log (6) · git_show, git_diff (7) · git_status (25) · git_add, git_commit, git_reset, git_diff_staged, git_diff_unstaged (gộp bên trong mọi lệnh ghi, không cần lệnh riêng). KHÔNG git_create_branch, git_checkout, git_branch (chỉ main).

Cách dùng bảng này: mọi lần đổi đầu nối phải chạy lại đủ 26 dòng ở mục 2 với cả hai phía; dòng nào không 🟢 thì phải có số quyết định (Dxx) giải thích vì sao là x.
