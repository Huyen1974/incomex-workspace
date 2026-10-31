# tools/onepass — GS-ALL-SOURCE-ONEPASS-DISCOVERY-AUDIT-20261030-01

Khảo sát chỉ đọc toàn bộ nguồn × lớp × cạnh ↔ Graph (P-UC1-HOST-B2). Dùng lại làm **bộ hồi quy** cho các gói sửa A–H.

| Tệp | Là gì | Chạy |
|---|---|---|
| `matrix.tsv` | Ma trận 83 dòng nguồn × lớp/cạnh: số native + bằng chứng, số Graph, trạng thái, nguyên nhân, gói sửa | đọc |
| `census_runtime.py` | Đường điểm danh thứ hai (độc lập graph_cert): cron mọi user kể cả dòng tắt bằng comment, systemd system/user/transient/linger, tiến trình theo cgroup (tìm mồ côi), cổng TCP/UDP, Docker container/image/volume/network/compose, kho git `/opt` sâu 5, tệp chạy ngoài code-ledger, nginx đếm/băm, kho hàng đợi cục bộ, remote rclone | `ssh contabo 'python3 -I -B -' < census_runtime.py > out.json` (chỉ đọc metadata; không in argv/env/nội dung; `git --no-optional-locks`) |
| `onepass_fixtures.py` | 11 ca thử âm trên bản sao `graph_cert.py` production: DISABLED≠ABSENT, user khác root, NO_ACCESS, include nginx, .socket/.path/drop-in, lệnh lỗi ⇒ không được ĐỦ, bảng/flow mới ⇒ ADD, Qdrant thiếu trang, kho git ngoài `/opt/incomex`, LIMIT cứng | `python3 -I onepass_fixtures.py <graph_cert.py>` (Mac, không mạng) |
| `fixtures-result.json` | Kết quả 30/10 trên `graph_cert.py` engine c1d2-1: 5 PASS / 6 GAP | — |

Nghiệm thu gói B: 11/11 PASS (ca GAP đổi thành PASS), không ca PASS nào hỏng.
## K0 + P2 (lưu 31/10, GS-COV2-SYNC-CORE-20261031-02, theo OWNER_SCOPE@GS-20261031-K0P2-ARCHIVE)

| Tệp | Là gì | Chạy |
|---|---|---|
| `k0_tools.shar.sh` (sha256 `ddb8a38f`) | Bộ đọc nguồn + oracle K0: nguyên byte 11 tệp (`k0_reconcile.py` `f6afbb50`, `k0_run.sh`, `k0_catalog.sql`, `k0_directus_table.sql`, `k0_runtime.py`, `k0_derived.py`, `k0_stat.sql`, `k0_usage*.py`, `k0_graph_export.py`, `k0_fixtures.py`) | `sh k0_tools.shar.sh <thư mục mới>` tự kiểm sha256. Đọc nguồn chạy trên VPS, chỉ đọc; `k0_reconcile.py` chạy ở Mac |
| `p2_track_functions_pl.sh` (`0b2954bf`) | Script một lần đã áp 30/10: `track_functions=pl`, có diễn tập lùi đúng byte | Lưu để tra cứu. **Có ghi cấu hình PG, không chạy lại nếu chưa có lệnh riêng** |

Quét 31/10: trufflehog 3.90.8 0 phát hiện. Tệp chỉ có mã, không dữ liệu nguồn.
Giới hạn đã biết: `k0_graph_export.py` chưa lấy trạng thái cạnh, `k0_reconcile.py` so `RETIRED` chữ hoa trong khi Graph ghi `retired` ⇒ phải sửa trước khi dùng so Graph production có gỡ mềm.

Fixture SYNC-CORE (Mac, không cần engine):
`python3 -I ../c1d/c1d_fixtures.py --sync-core ../c1d/graph_autocover.py <k0_reconcile.py> <ảnh T1> <ảnh T2> <graph.json> <gh.json> <gh-oracle.json> --out kq.json`
Kết quả tối đa FIXTURE_PASS. Ảnh K0 ở Mac: `~/Incomex-Graph-View/evidence-private/`, không lên repo.

Không PG/Directus trực tiếp trong các script này: số PG/Directus lấy từ giấy `cert/current.json` (bộ đọc graph-refresh) và kiểm kê C0 22/10.
