# CI runner pilot

RUN: GHM-C1A-RESUME-20261025-02. Binary actions/runner 2.338.1 được kiểm SHA256 chính thức; image được đóng gói tại VPS, không phải official runner image.

- Dockerfile: Node 22, pnpm 9.6.0, Python 3 và runner chính thức.
- runnerctl.sh: install/start/stop/remove/verify, tham số repo chỉ agent-data-test hoặc web-test. Install nhận registration token ngắn hạn qua stdin SSH; không truyền PAT.
- runner-watch.py: đầu kiểm runner, được gọi qua cơ chế giám sát hiện có.
- ci-cleanup.sh: xóa checkout CI sau job. Persistent runner, không phải ephemeral hay cách ly tuyệt đối.

Mỗi container user 10001, không Docker socket/host mounts/privileged; 1 CPU/1536 MiB, không swap thêm; network CI riêng. Hai workflow dùng flock chung trong volume CI để chỉ một bước cài/test nặng cùng lúc. Docker restart unless-stopped giúp tự chạy sau boot; chưa được coi là đã thử reboot VPS.

Rollback từng repo: stop/remove đúng container qua runnerctl, xóa registration tương ứng bằng phiên GitHub admin trên Mac. Volume riêng giữ lại để khôi phục, không xóa dữ liệu tùy tiện. Không thao tác application containers hoặc source tree đang phục vụ.

Trạng thái: CI 2/2 GREEN; KQ DỪNG S3, chưa nghiệm thu toàn bộ Đ30–31. Xem [báo cáo công khai đã lược thông tin](../C1A-RESUME-REPORT.md) và [COLLAB P35](../COLLAB.md). Chi tiết vận hành và các điểm chưa đạt chỉ lưu vùng bằng chứng riêng, không đưa lên repo public. Không tự chạy C1B/C2.
