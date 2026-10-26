# CI runner pilot

RUN: GHM-C1A-RESUME-20261025-02. Binary actions/runner 2.338.1 được kiểm SHA256 chính thức; image được đóng gói tại VPS, không phải official runner image.

- Dockerfile: Node 22, pnpm 9.6.0, Python 3 và runner chính thức.
- runnerctl.sh: install/start/stop/remove/verify, tham số repo chỉ agent-data-test hoặc web-test. Install nhận registration token ngắn hạn qua stdin SSH; không truyền PAT.
- runner-watch.py: đầu kiểm runner, được gọi qua cơ chế giám sát hiện có.
- ci-cleanup.sh: xóa checkout CI sau job. Persistent runner, không phải ephemeral hay cách ly tuyệt đối.

Mỗi container user 10001, không Docker socket/host mounts/privileged; 1 CPU/1536 MiB, không swap thêm; network CI riêng. Hai workflow dùng flock chung trong volume CI để chỉ một bước cài/test nặng cùng lúc. Docker restart unless-stopped giúp tự chạy sau boot; chưa được coi là đã thử reboot VPS.

Rollback từng repo: stop/remove đúng container qua runnerctl, xóa registration tương ứng bằng phiên GitHub admin trên Mac. Volume riêng giữ lại để khôi phục, không xóa dữ liệu tùy tiện. Không thao tác application containers hoặc source tree đang phục vụ.

Trạng thái mới nhất: CI 2/2 GREEN giữ nguyên; [S3-CLOSE P40](../C1A-S3-CLOSE-REPORT.md) KQ DỪNG do 1 thiếu sót thuộc C1A, chưa nghiệm thu toàn bộ Đ30–31. Checker vận hành đã được cập nhật trong RUN S3-CLOSE; nguồn hiện hành, hash và bản lùi lưu trong hồ sơ riêng theo giới hạn PROMPT. Các tệp code ở thư mục này là snapshot P35, không dùng snapshot checker cũ để ghi đè bản vận hành mới. Điều phối tại [COLLAB](../COLLAB.md). Không tự chạy C1B/C2.
