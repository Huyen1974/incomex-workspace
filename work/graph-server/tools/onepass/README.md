# tools/onepass — GS-ALL-SOURCE-ONEPASS-DISCOVERY-AUDIT-20261030-01

Khảo sát chỉ đọc toàn bộ nguồn × lớp × cạnh ↔ Graph (P-UC1-HOST-B2). Dùng lại làm **bộ hồi quy** cho các gói sửa A–H.

| Tệp | Là gì | Chạy |
|---|---|---|
| `matrix.tsv` | Ma trận 83 dòng nguồn × lớp/cạnh: số native + bằng chứng, số Graph, trạng thái, nguyên nhân, gói sửa | đọc |
| `census_runtime.py` | Đường điểm danh thứ hai (độc lập graph_cert): cron mọi user kể cả dòng tắt bằng comment, systemd system/user/transient/linger, tiến trình theo cgroup (tìm mồ côi), cổng TCP/UDP, Docker container/image/volume/network/compose, kho git `/opt` sâu 5, tệp chạy ngoài code-ledger, nginx đếm/băm, kho hàng đợi cục bộ, remote rclone | `ssh contabo 'python3 -I -B -' < census_runtime.py > out.json` (chỉ đọc metadata; không in argv/env/nội dung; `git --no-optional-locks`) |
| `onepass_fixtures.py` | 11 ca thử âm trên bản sao `graph_cert.py` production: DISABLED≠ABSENT, user khác root, NO_ACCESS, include nginx, .socket/.path/drop-in, lệnh lỗi ⇒ không được ĐỦ, bảng/flow mới ⇒ ADD, Qdrant thiếu trang, kho git ngoài `/opt/incomex`, LIMIT cứng | `python3 -I onepass_fixtures.py <graph_cert.py>` (Mac, không mạng) |
| `fixtures-result.json` | Kết quả 30/10 trên `graph_cert.py` engine c1d2-1: 5 PASS / 6 GAP | — |

Nghiệm thu gói B: 11/11 PASS (ca GAP đổi thành PASS), không ca PASS nào hỏng.
Không PG/Directus trực tiếp trong các script này: số PG/Directus lấy từ giấy `cert/current.json` (bộ đọc graph-refresh) và kiểm kê C0 22/10.
