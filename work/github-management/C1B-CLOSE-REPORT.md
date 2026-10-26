# C1B CLOSE — bằng chứng thực thi
RUN_ID: GHM-C1B-CLOSE-20261026-02
Trạng thái: ĐANG THỰC HIỆN · Codex · 2026-10-26 16:31Z
READY: P64 @ 7ccf89e276b4848704dd8ad1b4a8a75bd3f846cb. PROMPT SHA256 3af5f83d0eae4b2f44e6ebeb507eba0ef4ffe8a77b64d326fbc1bdb1a8989725.
STARTED P65: 90560368a35a0ac3e05338a443f6365453d239f6. Cờ VPS nhận tại commit 5816be7; mốc giờ nhập nhầm được sửa theo timestamp thật 16:17:39Z tại 86db356, hết hạn 18:00Z.

| Hạng mục | Kết quả đã đo | Phần còn lại |
|---|---|---|
| S0/P61 | Guard PRE 22/22 PASS; manifest P61 a9a84b4b… nguyên vẹn; main ban đầu đúng P64; cờ trống trước nhận | POST cuối RUN |
| Nguồn Web | Tìm được lab trên VPS2; patch SHA256 47c5c4eb8922fe064d27013b903bf510a7e99e80452c186ee0a5d6044a85b374; commit c649bda544811ba9d31f598be09f815f06d3c48d + 3934015d02ad4c2a6b27f9de0513e27b1779aacd; khôi phục đúng 570 tệp lab rồi giữ CWEB đã chạy (132ff49, kế tiếp ed76ba06); build Nuxt4.5.2/Node24.21.0 PASS, 2 CPU/3 GiB/no extra swap | Parity 132+32+2 đang chạy; chưa promote nguồn/chưa restart |
| AD cấu hình | 18 trường hiệu lực bằng nhau sau chuẩn hóa kiểu số/đơn vị/kế thừa image; hash Compose cũ khác nhãn nhưng không phát hiện khác hiệu lực; 40 tệp image không thiếu trong main, 2 tệp khác đúng release 2b14c2a → bfe86c8 | Candidate P61 có CMD khác; tạo lớp mã main trên đúng image cũ để giữ CMD/env/dependencies; canary/rollback chưa hoàn tất |
| Data Lifecycle | Candidate [40357980536](https://github.com/Huyen1974/agent-data-test/actions/runs/40357980536) GREEN; main [40359232468](https://github.com/Huyen1974/agent-data-test/actions/runs/40359232468) GREEN @251739422a997c9741e487fb4252f3c3d92e1be1; runner ghm-ci-agent-data-test | Giữ cảnh báo sẵn có: 2 vector mồ côi, 1 tài liệu thiếu vector; không auto-heal |
| ops-smoke | Candidate [40357987004](https://github.com/Huyen1974/web-test/actions/runs/40357987004) GREEN; main [40359238669](https://github.com/Huyen1974/web-test/actions/runs/40359238669) GREEN @f1fe708e685eab61a2bd7a9e22e68f4f7df11914; runner ghm-ci-web-test; ping/pages/asset đều 200 | Lịch 6 giờ giữ nguyên; 4xx dừng ngay, timeout 5 phút |
| Health Check | Candidate [40358212304](https://github.com/Huyen1974/web-test/actions/runs/40358212304) @9bfc84f40e4cd3f6512ddae33aef3ec40648ace1 chạy đủ 13 CHECK: 8 PASS, 5 FAIL (2/5/7/8/12) | Không promote; hosted còn ACTIVE. Cần phân biệt lỗi dữ liệu với lỗi auth/schema trong CHECK, không coi gap 9613 là mất dữ liệu đã xác nhận |
| Deploy/rollback | 0 restart production tới checkpoint này | Chỉ chạy app đạt gate riêng |

## Audit và quyền
- Từ ngày tạo runner 25/10, lịch sử job chỉ có C1A/P61 do Owner kiểm soát; không có pull_request/pull_request_target. Cleanup hook có sẵn chạy lại trước key audit, hai checkout còn 0 tệp.
- Runner giữ UID10001, không sudo/socket/credential mount mới. Key lấy từ GitHub Actions secret của đúng repo. Không key mới, không GSM/SSH trong job.
- Hai workflow chính thức chỉ nhận schedule/workflow_dispatch trên refs/heads/main, ngoại lệ nhánh thử đã bỏ. Không disable workflow vừa chuyển. C3.0 vẫn cần tách lane trước khi nhận mã PR.
- Health Check cần jq: bản 1.8.1 tải từ release chính thức, kiểm SHA256 020468de7539ce70ef1bceaf7cde2e8c4f2ca6c3afb84642aabc5c97d9fc2a0d, nằm trong job temp; không cấp root.
- CHECK2 sync_status=warning; CHECK5 0 context; CHECK7 parse/list không đạt; CHECK8 gap tính từ câu trả lời chưa đủ xác thực; CHECK12 trang registries timeout. Không sửa dữ liệu/quyền để ép PASS.

## Hồ sơ riêng và giới hạn
Bằng chứng private VPS: /opt/incomex/work/github-management/GHM-C1B-CLOSE-20261026-02/.
Mac: work/ghm-c1b-close/ (manifest, log Actions, source hashes; không có giá trị secret trong báo cáo).
Gitleaks nguồn Nuxt tìm 2 cảnh báo ở template .directus/docker-compose.yaml; tệp không đổi so main P61, không có secret mới trong delta. Không dùng token Directus lịch sử 401.
GLOBAL_GUARD vẫn PARTIAL theo nợ #11/khu vực chưa phủ từ P61; không sửa hộ. C3/C2/C4 chưa được chạy.
