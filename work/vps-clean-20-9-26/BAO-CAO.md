# BÁO CÁO — vps-clean-20-9-26

Tài liệu báo cáo duy nhất của việc này (D04). Lượt mới chèn lên đầu, giữ nguyên mục cũ. Chỉ chứa bản đã làm sạch; bằng chứng thô nằm trên VPS ngoài Git.

---

## V1 — Codex thẩm tra · 21/09/2026 · executor=Codex Desktop qua SSH (shell VPS) · write_path=workspace_*

RUN_ID `VPSC-V1-20260921-01` · PROMPT@3131bdee21a080a6fdfb5138ca72c2b7b3d30a38 (đã kiểm commit cuối chạm PROMPT, khớp OWNER_APPROVED + READY). Based_on repo `76c5490fe8088a9cb18af7722da8235fb0840220`. **Kết quả: DỪNG / V1_LIMITED — chưa hoàn tất thẩm tra để duyệt dọn.** Đo nhẹ trực tiếp 21/09/2026 khoảng 07:48–07:53Z, không lấy số R1 làm số V1. Đơn vị GB dưới đây = GiB.

### 1. CHO OWNER

- **Chưa nên duyệt triển khai toàn bộ phương án R1.** Đĩa hiện 91%, dùng 86,39GiB, trống **9,41GiB**; vượt ngưỡng chỉ đo nhẹ của PROMPT.
- Xác nhận độc lập Qdrant giữ **160 snapshot, 27,58GiB** và script hằng ngày không xoá snapshot server-side.
- Xác nhận script deploy sao Nuxt không tỉa; builder context-pack chép sang staging nhưng không dọn nguồn tạm. Log Directus hiện **1,316GiB**; chưa đo được tốc độ tăng độc lập.
- **N1 chưa qua cổng cứu hộ:** bản host mới nhất ngày 21/09; gói Drive được phản ánh trong meta/log ngày 20/09. Meta không có danh mục/checksum từng snapshot.
- Phát hiện script Drive vẫn xoá snapshot tạm sau khi tải thất bại; trạng thái PASS/COMPLETE không chứng minh đầy đủ thành phần Qdrant. Cần sửa điều kiện thành công trước khi dùng làm bằng chứng xoá.
- Ngay cả giả sử thu hồi đủ 34,4GiB của R1, hiện chỉ đạt **43,81GiB trống**, chưa đạt mục tiêu 45GiB.
- Đã kiểm RootFS của từng image N7/N8: không là tiền tố image đang chạy, không container nào dùng trực tiếp; vẫn phải giữ cổng R03/cứu hộ.
- **PASS 1 / REVISE 6 / BLOCK 8. PASS duy nhất là giữ N14, không phải cho xoá. Thu hồi được xác nhận đủ điều kiện xoá: 0GiB.**
- Không xoá/sửa dữ liệu, không restart, không chạy dọn, không tải/giải mã backup. Chỉ ghi báo cáo này và dòng VPSC.3.

### 2. Kết quả N1–N15

PASS = khuyến nghị của nhóm đã được xác minh trong phạm vi nêu; PASS cho HOLD không được cộng vào thu hồi. REVISE = cần sửa phương án/bổ sung bằng chứng; BLOCK = chưa được mở cổng xoá. Dấu “—” là **chưa đo**, không phải 0 và không sao chép số R1.

| Nhóm | GB R1 | GB V1 | Kết luận | Lý do |
|---|---:|---:|---|---|
| N1 Qdrant | 27,6 | 27,581 (allocated) | BLOCK | 160 snapshot được đếm trực tiếp; host có 8 bản 14–21/09, bản 21/09 là 236.036.608 byte. Chưa chứng minh snapshot mới nhất có trong gói Drive; meta chỉ cấp gói, script có nhánh bỏ qua lỗi tải. Không duyệt xoá toàn bộ theo bằng chứng hiện có. |
| N2 Log Directus | 1,3 | 1,316 | REVISE | stat file xác nhận kích thước; container tạo 23/07. Chưa kiểm độc lập cấu hình xoay log/file descriptor và chưa có tốc độ đo độc lập. “Hằng ngày, nếu >100MB thì truncate” không tạo trần 100MB giữa hai lượt; cần quy tắc xoay/cắt có trần và kiểm sau thao tác. |
| N3 Bản sao Nuxt | 2,7 | — | BLOCK | Đếm 66 thư mục khớp `nuxt-output.*`; còn tên dạng `nuxt-output-*`. R1 dùng tổng nhiều dạng tên nên không được so số lượng như cùng một tập. Chưa grep từng target qua mã, /etc, crontab mọi user và systemd; chưa chốt danh sách 3 bản gần nhất + bản mốc. Không quét sâu ở 91%. |
| N4 context-pack.tmp | 1,45 | — | REVISE | 1.001 thư mục, 979 có mtime thư mục >3 ngày; **không đồng nghĩa 979 thư mục an toàn để xoá**. R1 ghi ~990 ứng viên. Phải kiểm nội dung mới nhất/trạng thái job và loại lượt đang chạy; builder xác nhận thiếu dọn nguồn tạm. Chưa đo GB độc lập. |
| N5 Cache | ~1,4 | — | REVISE | Chưa đo lại block có thể thu hồi/working set. Dọn theo tháng chưa chứng minh trần 1GB; cần chỉ rõ công cụ/chủ cache, giữ browser runtime và loại hardlink trước khi tính dung lượng. |
| N6 Build cache | 0,4 | — | BLOCK | R03 hiện CLIENT-ONLY FINAL ACCEPTANCE, chưa CLOSED. Chưa xác minh lại GC/thu hồi thực tế của backend build. |
| N7 7 image trung gian | ≤0,5 | — | BLOCK | Kiểm riêng đủ 7 ID: không container dùng, RootFS không là tiền tố của image đang chạy. R03 chưa CLOSED; quan hệ lớp đúng không thay thế quyền bỏ rollback hoặc chứng minh số GB thu hồi. |
| N8 9 image local-only | ~2–3 | — | BLOCK | Kiểm riêng đủ 9 ID: không container dùng, RootFS không là tiền tố của image đang chạy. Chưa có bằng chứng rescue off-VPS và load/khôi phục cho đúng tập image, không cộng GB ước lượng vào số an toàn. |
| N9 Dump cũ postgres | 4,1 | — | BLOCK | Chưa grep từng tên qua đầy đủ các nguồn tham chiếu bắt buộc; chưa có cứu hộ kiểm được. Cần manifest chính xác và tách khỏi N10 để không trùng file .sql. |
| N10 SQL tạm | 0,14 | — | REVISE | Chưa kiểm từng file/job đang dùng và ranh giới N9; tuổi >7 ngày không tự chứng minh file dùng một lần. Quy tắc phải loại job đang chạy và giữ/quarantine đúng manifest. |
| N11 Tồn dư mission | ~5,5 | — | BLOCK | Chưa grep từng tên/đường dẫn; danh sách hiện còn wildcard và “…” nên chưa phải manifest xoá. Cần loại chính xác N12 và mọi file/dữ liệu còn phụ thuộc, rồi cứu hộ. |
| N12 Giữ theo nhãn | ~1,0 | — | BLOCK | Giữ nguyên UNKNOWN_HOLD; chưa kiểm độc lập từng nhãn/checkpoint. Không đưa các mục này vào purge chung theo tuổi hay toàn thư mục cha. |
| N13 DB thử | 1,2 | 1,174 | REVISE | DB còn tồn tại: 1.260.534.807 byte. Giữ UNKNOWN_HOLD, không đo chuỗi theo thời gian. Kiểm chuỗi chính xác “CẤM XOÁ” trong comment trả false; chưa chứng minh nhãn bị gỡ (có thể khác cách viết). Cần đối chiếu nhãn DEL-1; chưa có bằng chứng đủ gate backup/dependency để xoá. |
| N14 Hermes cũ | 3,0 | — | PASS (giữ) | Đọc launcher thực tế: lệnh hermes vẫn exec venv dưới `/usr/local/lib/hermes-agent`. Xác nhận phải giữ; chưa duyệt chuyển launcher/hợp nhất/xoá. Không tính dung lượng thu hồi. |
| N15 Alpine/kernel | ~0,3 | — | REVISE | Chưa kiểm tham chiếu Alpine, kernel dự phòng và cơ chế tự dọn; tiếp tục HOLD, chưa được tính vào thu hồi. |

**Phạm vi chưa hoàn tất:** không chạy du tầng 1, quét lớp ghi containerd, tổng file mở đã xoá, grep toàn bộ tham chiếu N3/N9/N11 hoặc rà toàn đĩa tìm nguồn ≥0,5GiB, vì cổng 91% chỉ cho đo nhẹ. Không xác nhận lại đối soát du–df hoặc tổng BUSINESS/operational của R1. Phiên thực tế là Codex Desktop điều khiển shell VPS qua SSH, **không phải Codex CLI chạy trực tiếp trên VPS như nhãn yêu cầu**; ghi rõ sai khác, không giả lập executor. Trước lượt tiếp cần Host phản ánh đúng bề mặt thực thi vào đề bài.

### 3. Các hiệu chỉnh bắt buộc trước đề bài dọn

**V1-01 · Backup Qdrant phải chứng minh đủ thành phần và thất bại thì dừng.** Mã VPS `scripts/backup-to-gdrive.sh:258–274` cho phép list/create lỗi qua `|| true`; tải snapshot lỗi chỉ ghi WARN rồi vẫn gọi DELETE. Lượt mới nhất đọc được có thông báo snapshot + upload hoàn tất, không thấy WARN tải lỗi; điều đó **không phải bằng chứng đã kiểm payload**. Meta config không có inventory từng snapshot, payload đã che. Không suy “backup hằng ngày PASS” thành “snapshot cần giữ đã có ngoài VPS”. Cần manifest gồm collection, tên/thời điểm/size/checksum snapshot, liên kết với gói off-VPS và xác minh khôi phục phù hợp trên máy ngoài VPS; không tải về ổ đang đầy. Bản host ngày 21/09 và gói ngày 20/09 là hai mốc khác nhau, không diễn đạt là cùng bản mới nhất.

Chỉnh đề xuất vá `qdrant-backup.sh`: chỉ DELETE đúng snapshot sau khi sao chép thành công và kiểm tính toàn vẹn; nếu một bước lỗi thì giữ bản nguồn + báo lỗi. Không thêm xoá mọi snapshot >1 ngày vô điều kiện, vì có thể xoá bản duy nhất của lượt backup thất bại. Chốt retention theo tập đã được chứng minh có bản cứu, loại snapshot đang tạo/tải. Qdrant có API riêng [xoá snapshot collection](https://api.qdrant.tech/v-1-18-x/api-reference/snapshots/delete-snapshot?explorer=true); đó là thao tác API, không phải lệnh restart. V1 không gọi DELETE và chưa kiểm thời gian thu hồi block thực tế.

**V1-02 · Tính lại dung lượng mục tiêu từ số hiện tại và tránh cộng trùng.** df chính xác: tổng 102.888.095.744 byte, dùng 92.765.503.488, available 10.105.815.040. Dùng tăng **2,94GiB** so với số cuối R1 04:10Z; nguyên nhân chưa được đối soát, không quy thành tốc độ tăng ổn định. Muốn đạt 45GiB từ mốc này cần thu hồi ròng ít nhất **35,59GiB**, chưa tính phát sinh/tạm trong khi thao tác. Theo giả thiết R1 34,4GiB cũng chỉ đạt 43,81GiB. Phải dùng available thực tế, không lấy tổng trừ used bỏ qua reserved space. N9/N10 phải tách tập .sql; N11/N12 phải tách vùng có nhãn; image chia sẻ layer chỉ tính phần vật lý thực sự có thể giải phóng.

**V1-03 · Chốt manifest và bảo vệ rollback/job đang chạy.** N3 phải liệt kê chính xác cả dạng tên chấm và gạch ngang, chỉ rõ bản mốc; R1 vừa nói “1 bản mốc” vừa cho tối đa 2 nên trần 4×45MB chưa nhất quán. N3/N9/N11 bắt buộc kiểm từng tên qua đủ nguồn tham chiếu của PROMPT; grep thư mục cha không thay thế được. N4/N10 kiểm job/lock và thời điểm ghi nội dung, không chỉ tuổi thư mục. Đặt kiểm tra lại target ngay trước mutation để tránh deploy/backup chen ngang. R03 chưa CLOSED nên giữ nguyên cổng rollback/build cache.

**V1-04 · Phân biệt lịch dọn với trần bảo đảm.** Cron cắt log khi >100MB một lần/ngày cho phép tăng thêm cả ngày; dọn cache hằng tháng không chứng minh ≤1GB. Snapshot còn giữ ≤1 ngày không có steady-state 0 tuyệt đối và còn peak lúc tạo/sao chép. TTL 30 ngày cho mission không đồng nghĩa local 0 khi vẫn có mission mới. Bổ sung budget, kiểm tần suất/overshoot, xử lý khi job dọn hoặc offload lỗi và đỉnh dung lượng tạm; tính lại tổng mức ổn định thay vì giữ nguyên con số 34,5GiB của R1.

**V1-05 · Không xoá mù dữ liệu phục hồi công cụ hoặc lịch sử.** TTL `transactions/jobs/results` cần chủ workspace xác nhận riêng từng loại, giữ job đang chạy và journal/idempotency còn cần khôi phục. Không áp purge chung cho toàn cây workspace-tools. `git gc` không tự hạn chế dung lượng lịch sử còn được tham chiếu; `--prune=now` cũng không nên trở thành quy tắc mặc định khi còn tiến trình ghi. Các đề xuất này cần được cụ thể hoá trong đề bài sau, chưa triển khai.

**V1-06 · Cứu hộ ngoài VPS theo bộ có thể khôi phục.** N8/N9/N11 cần kiểm thành công mọi chặng nén/mã hoá/upload, checksum và đối tượng hoàn chỉnh trước xoá nguồn; có kế hoạch khôi phục kiểm được, không tạo gói cứu lớn trên VPS. Retention Drive giữ theo bộ artifact + meta và tính riêng lưu lượng nạp hằng tháng với tổng dung lượng lưu ổn định; “tăng ròng ~0” không có nghĩa “không tải thêm dữ liệu”. Tôn trọng nhãn giữ/mission còn mở trước mọi TTL chung.

**Bốn nguyên nhân R1:** (1) xác nhận cơ chế rò Qdrant và GB; (2) xác nhận mã deploy thiếu tỉa, chưa xác nhận GB; (3) xác nhận file pm2 lớn, chưa xác nhận độc lập tốc độ hay toàn bộ cấu hình rotation; (4) xác nhận builder không dọn nguồn và số thư mục, chưa xác nhận GB/tốc độ. Chưa đủ căn cứ nói R1 không bỏ sót nguồn ≥0,5GiB; chênh df 2,94GiB là phần còn mở.

### 4. Bằng chứng và giới hạn

Bằng chứng mới lấy trực tiếp qua shell VPS, giữ trong output công cụ của phiên; **không tạo kho raw hoặc file tạm mới trên VPS**, không đọc lại số raw R1 để thay phép đo. Repo chỉ có tóm tắt đã làm sạch:

- E01: df, thời gian UTC, danh sách container/trạng thái; phép đo đầu đã báo 91%. Có thêm một df byte trong bước định danh để tính chính xác; đây là lặp ngoài yêu cầu “mỗi phép đo một lần”, không dùng làm chuỗi đo tốc độ và không có sleep.
- E02: liệt kê metadata một tầng snapshot Qdrant: 160 file snapshot; tổng snapshot/checksum 29.613.664.768 byte logic, **29.615.128.576 byte cấp phát**; danh sách 8 bản host.
- E03: stat duy nhất log pm2: 1.413.027.126 byte logic, 2.759.832 block ×512; ngày tạo container 23/07. Không đọc nội dung log truy cập.
- E04: liệt kê một tầng deploy/context-pack và đọc mã trực tiếp `qdrant-backup.sh`, `backup-to-gdrive.sh`, `dung-va-trien-khai.sh`, `dot-context-pack-build.sh`; chỉ xuất nhánh liên quan đã che thông tin nhạy cảm.
- E05: Docker inspect container + image metadata, đối chiếu đủ từng ID N7/N8 với RootFS image đang chạy và tham chiếu của cả container dừng.
- E06: meta staging config ngày 20/09, status PASS/COMPLETE, chỉ báo điều kiện từ đoạn log lượt mới nhất; **không truy cập/list Drive trực tiếp, không checksum payload hoặc giải mã**.
- E07: đọc launcher Hermes; truy vấn metadata DB thử bằng phiên read-only. Lần kết nối đầu bằng role mặc định không thành công; lần dùng role cấu hình của container thành công, không đo activity theo thời gian.
- E08: trạng thái R03 đọc từ `work/mcp-workspace/COLLAB.md` ở cùng Based_on; vẫn chưa CLOSED.

**NEXT cho Host:** xử lý V1-01–V1-06 và điều kiện nguồn đĩa tăng, chốt đúng executor/phạm vi phép đo nhẹ để hoàn tất những mục còn thiếu; chưa dùng báo cáo giới hạn này làm giấy duyệt dọn. Không ghi MACHINE_DONE vì phép thẩm tra tổng và grep bắt buộc chưa hoàn tất.

---

## R1 — 09/2026 · UNVERIFIED_R1 · executor=Claude Code CLI · write_path=workspace_*

RUN_ID `VPSC-R1-20260920-01` · PROMPT@`7ce1cbd389a9ca54e12d74cf2f8aeb6306334c65` (khớp READY) · đo 2026-09-21 03:26Z → 04:11Z · chế độ AUDIT / NO PRODUCTION MUTATION.
Đơn vị: **GB = GiB** như `df -h`/`du`. "Từ 24/07" = từ lúc dọn xong 24/07 ~07:30Z tới lúc bắt đầu đo (57,8 ngày). "GB/tháng" = quy về 30 ngày.
Mọi số dưới đây là **UNVERIFIED_R1** cho tới khi Host đo lại và Codex thẩm tra (VPSC.3).

### 1. CHO OWNER

**Kết luận một câu:** đĩa đầy lại không phải vì dữ liệu nghiệp vụ (chỉ 2,5GB, gần như đứng yên) mà vì **một script backup Qdrant quên xoá bản chụp bên trong Qdrant** — riêng nó chiếm 27,6GB và ăn **~6,6GB mỗi tháng**, tức một nửa mức đầy lại từ 24/07. Cộng thêm bản sao web trước mỗi deploy, log truy cập của Directus và bản dựng tạm context-pack không ai xoá.

**Anh cần quyết (3 câu):**

1. **Xoá 27,6GB bản chụp Qdrant cũ + sửa script để không kẹt nữa?** Bản mới nhất luôn có bản sao ở ổ ngoài container (7 ngày) và trên Drive (hằng ngày từ 20/07); các bản cũ hơn chỉ là trạng thái quá khứ của chỉ mục vector, tái tạo được. → **PM đề xuất: ĐỒNG Ý** sau khi Codex PASS. Xoá qua API của Qdrant, không restart, không phụ thuộc R03. Chỉ riêng việc này đã đưa đĩa từ 12GB lên ~40GB trống.
2. **~9,6GB dump và bản chụp cũ từ các mission tháng 5–7** (trong container postgres 4,1GB, `/opt/incomex/backups` + `/root` + MySQL cũ 5,5GB) — đưa lên Drive rồi xoá khỏi VPS? → **PM đề xuất: ĐỒNG Ý đưa lên Drive** (mã hoá, giữ 12 tháng) rồi xoá tại VPS; riêng các mục DEL-1 dán nhãn "giữ lâu/cấm xoá" để nguyên.
3. **DB thử `directus_gov_test_20260602` (1,2GB, nhãn DEL-1 "CẤM XOÁ", chưa có bản ngoài VPS) và bản cài Hermes cũ (3,0GB, lệnh `hermes` vẫn trỏ vào)** — giữ trên VPS hay chuyển đi? → **PM đề xuất:** DB thử: dump ra Drive trước, **giữ nguyên trên VPS** tới khi DEL-1 kết luận. Hermes: gom về một bản cài (dịch vụ đang chạy bản trong `/var/lib/hermes`), bỏ bản cũ sau khi chuyển lệnh `hermes`.

**Ma trận nguồn sinh** (đối soát với df ở dòng cuối)

| # | Nguồn sinh | LOẠI | Hiện tại GB | Tăng từ 24/07 | GB/tháng | Bounded? | Ổn định dự kiến GB | Thu hồi an toàn GB | Màu |
|---|---|---|---:|---:|---:|---|---:|---:|---|
| 1 | Bản chụp Qdrant kẹt trong container (`qdrant-backup.sh`) | DISPOSABLE | 27,6 | +12,7 | 6,6 | `FAIL_UNBOUNDED` | 0 | 27,6 | 🔴 |
| 2 | Bản sao web Nuxt trước mỗi deploy (`deploys/nuxt-output.*`, 70 bản sao) | DISPOSABLE | 2,9 | +2,0 | 1,1 (14 ngày gần: 1,5) | `FAIL_UNBOUNDED` | 0,2 | 2,7 | 🔴 |
| 3 | Log truy cập pm2 bên trong container Directus | DISPOSABLE | 1,3 | +1,3 | 0,7 | `FAIL_UNBOUNDED` | 0,1 | 1,3 | 🔴 |
| 4 | Bản dựng tạm `context-pack.tmp` (999 bản, 3 giờ/lần) | DISPOSABLE | 1,5 | +0,75 | 0,4 | `FAIL_UNBOUNDED` | 0,05 | 1,45 | 🔴 |
| 5 | Hermes: 2 bản cài + cache | RUNTIME (+cache DISPOSABLE) | 6,6 | +4,3 | 0,4 (+3,7 cài một lần) | `FAIL_UNBOUNDED` | 3,2 (+3,0 nếu giữ bản cũ) | 0,5 | 🔴 |
| 6 | Image Docker: đang chạy + cha + rollback + trung gian | RUNTIME / rollback | 9,7 | +1,0 | 0,5 | `FAIL_UNBOUNDED` (không luật giữ N tag) | ~8 | 0 lúc này (chờ R03; cứu trước ~2–3) | 🔴 |
| 7 | Build cache | DISPOSABLE | 0,2 (+phần trong kho image) | +0,2 | ~0,1 | trần GC mặc định, chưa khai | ≤1 | 0,4 sau R03 | 🟡 |
| 8 | Cache công cụ ở `/root` (npm, pip, uv, electron, node-gyp, playwright) | DISPOSABLE | 1,9 | +0,4 | 0,2 | `FAIL_UNBOUNDED` | 1,0 | 0,9 | 🔴 |
| 9 | `/tmp` bên trong container postgres (dump tháng 5 + file SQL tạm của agent) | NONBUSINESS_KEEP | 4,2 | +0,14 | 0,07 | `FAIL_UNBOUNDED` | 0 | 0 lúc này (câu 2) | 🔴 |
| 10 | Tồn dư mission: dump / bản chụp / checkpoint / thư mục stage không hạn xoá | NONBUSINESS_KEEP | 6,5 | +0,3 | 0,15 | `FAIL_UNBOUNDED` | 0 | 0 lúc này (câu 2) | 🔴 |
| 11 | DB thử `directus_gov_test_20260602` | NONBUSINESS_KEEP | 1,2 | 0 | 0 | tĩnh | 1,2 (0 nếu chuyển đi) | 0 (HOLD) | 🟡 |
| 12 | Backup vòng quay tại chỗ (PG 7 ngày, Qdrant 7 ngày, gói Drive 1 bộ) | NONBUSINESS_KEEP | 3,0 | ~0 | ~0 | trần local 7 ngày | 3,0 | 0 | 🟢 |
| 13 | Backup Lark tại chỗ (JSONL giải nén + tar.gz) | NONBUSINESS_KEEP | 1,2 (cuối phiên 1,1: lượt 21/09 đã thay lượt 14/09) | +1,2 | 0 | có trần: `prune-local` xoá lượt cũ sau offsite-ok | 1,1 (nay) / 0,1 (sau vá) | 0 | 🟡 |
| 14 | Log: journald, Docker json, `/var/log`, `/opt/incomex/logs` | DISPOSABLE | 1,8 | +0,2 | ~0,05 phần không trần | phần lớn có trần | 2,5 | 0 | 🟡 |
| 15 | Trạng thái công cụ workspace + cowork runner | RUNTIME | 0,45 | +0,45 | chưa rõ | chưa thấy TTL | 0,5 | 0 | 🟡 |
| 16 | Thư mục làm việc mission (`evidence/ staging/ tmp/ work/ artifacts/ exports/`) | DISPOSABLE (có phần bằng chứng) | 0,16 | ~+0,1 | ~0,05 | `FAIL_UNBOUNDED` (không TTL) | 0,05 | 0 | 🔴 |
| 17 | Công cụ AI + git (Claude Code, Codex, `.git`, clone, mcp-roots) | RUNTIME | 1,1 | +0,1 | ~0 | tự giữ 3 bản / gc tuần | 1,1 | 0 | 🟢 |
| 18 | PostgreSQL sống (`directus`, `incomex_metadata`, WAL) | BUSINESS_LIVE | 2,2 | +0,05 | 0,03 | nghiệp vụ | 2,2 + tăng tự nhiên | — | 🟢 |
| 19 | Qdrant storage (vector thật) | BUSINESS_LIVE | 0,2 | ~0 | ~0 | nghiệp vụ | 0,2 | — | 🟢 |
| 20 | Hệ điều hành, mã, swap 2GB, node_modules/venv, lặt vặt | RUNTIME | 9,6 | +0,5 | ~0,1 | ổn | 9,6 | 0 | 🟢 |
| | **Cộng BUSINESS_LIVE** | | **2,5** | +0,05 | | | 2,5 | | |
| | **Cộng RUNTIME_WORKING_SET** | | **26,7** | +5,6 | | | ~22,3 (+3,0 nếu giữ Hermes cũ) | | |
| | **Cộng NONBUSINESS_KEEP** | | **16,1** | +1,7 | | | ~4,4 | | |
| | **Cộng DISPOSABLE_REBUILDABLE** | | **38,0** | +18,4 | | | ~5,2 | | |
| | **TỔNG (du)** | | **83,3** | **+25,7** | **~11,5 đang chạy** | | **~34,5** | **34,4 ngay + 0,4 sau R03** | |
| | **df lúc bắt đầu đo** | | **83,4** | **+25,7** (58G→84G) | 13,3 TB (gồm cài Hermes) | | | | |

Đối soát: tổng `du` 83,3GB so với `df` 83,4GB (lệch 0,07GB = metadata + file đã xoá còn mở 0,02GB + ghi trong lúc đo). Tổng mức tăng theo dòng 25,7GB so với `df` tăng 25,7GB; khoảng ~1GB trong đó là ước lượng (dòng 14, 17, 20). Không có khoản lệch >3GB chưa giải thích.

**Hai con số tách bạch**
- **Nghiệp vụ:** hôm nay **2,5GB** (3% phần đã dùng). Tăng ~0,05GB từ 24/07.
- **Vận hành:** hôm nay **80,9GB** (97%). Sau khi áp đủ trần/TTL/đưa-ra-ngoài ở §7: **~32GB** (~35GB nếu giữ bản cài Hermes cũ). Toàn đĩa khi đó ~34,5GB dùng / 95,8GB → **trống ~61GB**.
- Mức tăng ngoài nghiệp vụ đang chạy **~11,5GB/tháng** = gần **4 lần ngưỡng đỏ 3GB/tháng**. 14 ngày gần nhất riêng nguồn 1–4 đã ~4GB.
- Dọn ngay lớp `DELETE_PROVEN_SAFE` (nhóm 1–5 ở §6): trống **12,4 → ~46,8GB** (đạt T1 ≥45GB). Cộng lớp cứu-rồi-xoá: ~57GB.

---

### 2. CHO PM

#### §3 Đo tổng + đối soát (tóm tắt)

- `df /` lúc bắt đầu (03:26Z): 89.549.037.568 B dùng · 13.322.280.960 B trống · 88%. Inode 9%. `df` lúc cuối: 04:10:37Z 89.607.528.448 B dùng · 13.263.790.080 B trống · 88% — chênh ròng +0,06GB, khớp với 2 bản sao do 2 lần deploy Nuxt trong lúc đo (+~0,08GB) và lượt backup Lark thay lượt cũ (−~0,05GB); R1 chỉ ghi 0,2MB bằng chứng.
- `du -x` tầng 1: `/var` 49,5GB (trong đó `/var/lib/containerd` **42,9GB**, `/var/lib/hermes` 3,4GB, `/var/log` ~1,3GB) · `/opt` 17,4GB (`/opt/incomex` 14,0GB, `/opt/workflow/postgres` 3,4GB) · `/usr` 8,7GB (có `/usr/local/lib/hermes-agent` 3,0GB) · `/root` 5,6GB · `/swapfile` 2,0GB · `/tmp` 0,14GB.
- Docker 29.2.1 dùng **kho image containerd** (snapshotter overlayfs) nên `/var/lib/docker` chỉ 0,7GB; image + lớp ghi container nằm hết trong `/var/lib/containerd`. Trong 42,9GB đó: lớp ghi `incomex-qdrant` **27,6GB**, lớp ghi `postgres` 4,2GB, lớp ghi `incomex-directus` 1,3GB, snapshot image 7,6GB, kho blob nén 2,2GB.
- `docker system df` báo Images 46GB / "reclaimable 37GB" — **con số này sai lệch** với kho containerd: đo thật, toàn bộ snapshot image chỉ 7,6GB và image tạo từ 24/07 chỉ chiếm 0,9GB. Không dùng số "reclaimable" của Docker để ước lượng thu hồi.
- Log: `daemon.json` đã có `max-size 50m × 3` (nghi vấn f ở PROMPT **không đúng** với log Docker); journald `SystemMaxUse=1G` (đang 1,0GB); `/var/log` ~0,24GB ngoài journal.
- File đã xoá còn bị giữ (`lsof +L1`): 70 file, 0,02GB — không đáng kể.
- Hardlink: `deploys/` 0 file nlink>1 (mỗi bản sao Nuxt chiếm chỗ thật); cache uv/pnpm có hardlink vào venv/node_modules nên xoá cache uv/pnpm thu hồi thấp (đã loại khỏi lớp an toàn).
- Swap: `/swapfile` 2GB, đang dùng 0,35GB. Không có snap. Kernel: 6.8.0-139 (đang dùng) + 6.8.0-90 (cũ, ~0,3GB).

#### §4 Sổ nguồn sinh (Generator Registry)

| Nguồn sinh | Path | LOẠI | Trigger | Tần suất | GB | Tăng từ 24/07 | GB/tháng | Cần ở VPS? | Trần local đề xuất | Ổn định tính ra | Giữ dài: đích · ngân sách · hạn | Tái tạo được: quy tắc xoá | Quy tắc giữ hiện có | Tự dọn? | Nguyên nhân rò | Chủ |
|---|---|---|---|---|---:|---:|---:|---|---|---|---|---|---|---|---|---|
| Bản chụp Qdrant server-side | `/qdrant/snapshots/production_documents/` trong lớp ghi container `incomex-qdrant` (không có bind) | DISPOSABLE | cron root `qdrant-backup.sh` | 1 lần/ngày 03:00 giờ máy | 27,6 (160 bản, 67→225MB/bản) | +12,7 (60 bản) | 6,6 và tăng theo cỡ collection | Không — bản ở host 7 ngày + gói Drive hằng ngày đã đủ | 0 bản trong container | 0 × 1 ngày = 0 | Đã có trên Drive trong gói cấu hình hằng ngày | Xoá bằng API Qdrant ngay sau `docker cp` | Script xoá bản ở host >7 ngày; **không xoá bản trong Qdrant** | Không | Script POST tạo snapshot → `docker cp` ra host → không gọi DELETE (script Drive `backup-to-gdrive.sh` thì có DELETE) | hạ tầng backup (cron root) |
| Bản sao web trước deploy | `/opt/incomex/deploys/nuxt-output.truoc-*`, `.bak*`, `-pre-*`, `.backup-*` | DISPOSABLE (rollback ngắn hạn) | `scripts/phai-cu/dung-va-trien-khai.sh` (`cp -a` trước rsync) + sao lưu tay | mỗi deploy; 16 bản/14 ngày | 2,9 (70 bản sao × ~43MB) | +2,0 (47 bản) | 1,1 TB / 1,5 gần | Có, nhưng chỉ vài bản gần nhất để hoàn tác | 3 bản mới nhất + 1 bản mốc | 4 × 0,045 = 0,2 | — | Giữ 3 mới nhất + mốc, xoá phần còn lại sau mỗi deploy | Không có | Không | Script chỉ sao, không tỉa | quy trình deploy Nuxt |
| Log pm2 Directus | `/home/node/.pm2/logs/directus-out-0.log` trong lớp ghi `incomex-directus` | DISPOSABLE | tiến trình Directus (pm2-runtime), ghi mỗi request | liên tục ~23MB/ngày | 1,3 (1 file) | +1,3 (container tạo 23/07) | 0,7 | Không cần giữ lịch sử | 100MB | 23MB/ngày × ≤4 ngày ≈ 0,1 | — | Cắt về 0 khi >100MB (truncate, file đang mở) hoặc hạ mức log | `max-size` của Docker **không áp** cho file pm2 trong container | Không | Log nằm trong container, không có xoay vòng | Directus (image chính hãng) |
| Bản dựng tạm context-pack | `/opt/incomex/context-pack.tmp/<BUILD_ID>` | DISPOSABLE | cron user incomex `dot-context-pack-build.sh` | 3 giờ/lần | 1,5 (999 thư mục) | +0,75 (399) | 0,4 | Không, sau khi đã chép sang staging | 3 ngày | ~8 bản/ngày × 3 ngày × 1,5MB ≈ 0,04 | — | Xoá `.tmp/<BUILD_ID>` ngay khi chép xong + dọn >3 ngày | `dot-context-pack-retention-cleanup` chỉ dọn `context-pack-staging` (7 ngày, tối thiểu 3) | Không (staging thì có) | Builder ghi `.tmp/<BUILD_ID>` rồi chép, không xoá nguồn | DOT context-pack |
| Hermes — bản đang chạy | `/var/lib/hermes/hermes-agent` (+ `.agent-browser`, `.hermes`, `work` 8G thưa) | RUNTIME | systemd `hermes-serve`, `hermes-gateway`, relay | chạy thường trực; cập nhật tay (28/07, 11/09) | 2,7 + ảnh `work` 0,2 (trần cứng 8G) | +2,9 (cài 28/07) | ~0,2/lần cập nhật (pack git mới) | Có — dịch vụ đang chạy | 1 bản cài + `git gc` sau cập nhật | ~2,9 | — | — | Không | Không | Mỗi lần cập nhật để lại pack git + dependency cũ | Hermes (systemd hermes-*) |
| Hermes — bản cài cũ | `/usr/local/lib/hermes-agent` | RUNTIME? → `UNKNOWN_HOLD` | lệnh `/usr/local/bin/hermes` vẫn trỏ vào; phiên tmux demo từ 05/2026 | cập nhật 28/07, 11/09 | 3,0 | +0,7 (2 pack git 0,34 + 0,35) | ~0,3 | Chưa rõ — trùng chức năng bản đang chạy | 0 sau khi hợp nhất | 0 | — | — | Không | Không | Hai bản cài song song | Hermes |
| Hermes — cache | `/var/lib/hermes/.npm`, `.cache` (uv, electron) | DISPOSABLE | cài/cập nhật | theo cập nhật | 0,75 | +0,75 | ~0,1 | Không | 0,3 | 0,3 | — | `npm cache clean`, `uv cache prune` sau cập nhật | Không | Không | Cache không trần | Hermes |
| Image Docker cục bộ | kho containerd | RUNTIME (đang chạy + cha) / rollback | build tay theo mission (R03, hardening, continuation, workspace…) | 20 image mới 17–20/09 | 7,6 snapshot + 2,2 blob | +1,0 | 0,5 (dồn theo đợt build) | Có cho image đang chạy + cha; rollback chỉ vài bản | chạy + cha + 2 rollback/dịch vụ | ~8 | Rollback cũ: bản cứu trên Drive (`docker save`) ~2–3GB, giữ 12 tháng | Image dựng lại được từ Dockerfile trên VPS thì xoá sau R03 | Không có luật giữ N tag | Không | Mỗi lần build thêm tag mới, không tỉa | các mission build image |
| Build cache BuildKit | `/var/lib/docker/buildkit` + snapshot trong containerd | DISPOSABLE | `docker build` | theo đợt build | Docker báo 0,86 (0,41 riêng) | +0,86 (24/07 là 0) | ~0,45 | Không | `keepStorage` 1–2GB | ≤1–2 | — | `builder prune --keep-storage` sau R03 | GC mặc định của BuildKit, chưa khai trần | Có (mặc định) | — | build |
| Lớp ghi container postgres `/tmp` | `/tmp` trong `postgres` (2.866 mục) | NONBUSINESS_KEEP (dump cũ) + DISPOSABLE (SQL tạm) | agent `docker cp` file .sql/.dump vào để chạy | theo mission | 4,2 (4,1 là dump 05/2026) | +0,14 | 0,07 | Không — dump cũ là bản chụp DB tháng 5, SQL tạm là rác | 0 (TTL 7 ngày cho SQL tạm) | ~0 | Dump cũ: Drive mã hoá, ≤5GB một lần, giữ 12 tháng | SQL tạm: xoá >7 ngày | Không | Không | Agent chép file vào container, không dọn; nằm trong lớp ghi nên còn mãi tới khi recreate | agent/mission |
| Tồn dư mission | `/opt/incomex/backups/*` ngoài vòng quay (19 dump iucore, `dieu44_*` giữ, `vps-backup-20260718`, mysql, `iu-core-70000x`, `dieu45-phase1`, `pg-ngoai-vong-luan-chuyen`…), `/root/backups`, `/root/*checkpoint*`, `/root/p0-2-*`, `wsq5_*`, `phase7-*`, `agent-runs`, `mcp-nolimit-stage`, `/opt/incomex/docker/mysql`, `docker/dieu44_*` | NONBUSINESS_KEEP | mission thủ công | theo mission | 6,5 | +0,3 | 0,15 | Không cần nằm trên VPS | 0 (mọi dump mission TTL 30 ngày tại chỗ) | 0 | Drive mã hoá, ~6GB một lần + ≤1GB/tháng, giữ 12 tháng | — | Không | Không | Không có quy ước hạn xoá cho bản chụp mission | agent/mission |
| DB thử governance | `directus_gov_test_20260602` trong PG (1,2GB) | NONBUSINESS_KEEP | — (tĩnh từ 01/08) | — | 1,2 | 0 | 0 | Không cần chạy; nhãn DEL-1 "CẤM XOÁ" vì giữ 202 dòng duy nhất | giữ tới DEL-1 kết luận | 1,2 | Dump ra Drive (≤0,2GB nén), giữ vô hạn tới DEL-1 | — | nhãn COMMENT ON DATABASE: CẤM XOÁ | — | — | DEL-1 |
| Backup PG vòng quay | `/opt/incomex/backups/pg/directus_*.sql.gz` | NONBUSINESS_KEEP | cron root `pg-backup.sh` 02:27 | ngày | 1,0 (9 bản × 115MB) | ~0 | ~0 | Có — khôi phục nhanh tại chỗ | 7 ngày | 0,12 × 8 ≈ 1,0 | Drive (gói mã hoá hằng ngày) | — | `RETENTION_DAYS=7` | Có | — | hạ tầng backup |
| Backup Qdrant vòng quay | `/opt/incomex/backups/qdrant/*.snapshot` | NONBUSINESS_KEEP | `qdrant-backup.sh` | ngày | 1,7 (8 bản) | ~0 | ~0 | Có | 7 ngày | 0,22 × 8 ≈ 1,8 | Drive | — | `RETENTION_DAYS=7` | Có | — | hạ tầng backup |
| Gói Drive tại chỗ | `/var/lib/incomex/backup-staging` | NONBUSINESS_KEEP | cron `backup-to-gdrive.sh` 20:37 | ngày | 0,3 | ~0 | 0 | Có (bộ mới nhất) | 1 bộ | 0,3 | Drive: xem dòng "Drive" dưới | — | `LOCAL_KEEP=1` | Có | — | hạ tầng backup |
| Backup Lark | `/opt/incomex/lark-backups/daily/<ngày>`, `archives/` | NONBUSINESS_KEEP | systemd `s177-lark-backup.timer` T2+T5 03:15Z | 2 lần/tuần | 1,2 (cuối phiên 1,1) | +1,2 | 0 (vòng) | Chỉ cần bản nén mới nhất | giữ tar.gz 1–2 bản; JSONL xoá ngay khi offsite-ok | 0,07 × 2 ≈ 0,1 | Drive (đã có offsite-ok) | — | `prune-local` sau offsite-ok (script ghi 14 ngày; đo thật 21/09: lượt mới thay lượt 14/09, còn 1 thư mục JSONL + 1 tar.gz) | Có | Giữ JSONL giải nén 1,1GB trong khi bản nén 70MB đã lên Drive | Lark ops |
| Drive (đích ngoài VPS) | thư mục backup mã hoá trên Drive | NONBUSINESS_KEEP | `backup-to-gdrive.sh` | ngày | 18,4 trên Drive (280 đối tượng từ 20/07) | +18,4 trên Drive | ~8,6 trên Drive | — | — | — | **Chưa có hạn giữ ở đích** — đề xuất 30 bản ngày + 12 bản tháng ≈ 12GB | — | `MAX_REMOTE_BACKUPS=14` chỉ áp cho file cũ ở gốc, không áp thư mục mã hoá | Không | Thiếu bước tỉa ở đích | hạ tầng backup |
| Log Docker json | `/var/lib/docker/containers/*/*-json.log` | DISPOSABLE | Docker | liên tục | 0,5 | ~+0,2 | 0 (có trần) | Không | 50MB × 3 / container (đang có) | ≤1,8 | — | — | `max-size 50m, max-file 3` | Có | — | Docker |
| journald | `/var/log/journal` | DISPOSABLE | systemd | liên tục | 1,0 | ~0 | 0 | Không | 1G (đang có) | 1,0 | — | — | `SystemMaxUse=1G` | Có | — | OS |
| Log ứng dụng theo ngày | `/var/log/incomex/hc-executor*-<ngày>.log` (306 file), `/opt/incomex/logs/disk-snapshots/` | DISPOSABLE | cron `dot-hc-executor*` (3 giờ), `disk-monitor.sh` (giờ, khi >85%) | 3 giờ / giờ | ~0,1 | +0,01 | ~0,01 | Không | 30 ngày | nhỏ | — | xoá >30 ngày | logrotate không bắt tên file theo ngày; `disk-snapshots` đang giữ 30 file (~1MB) | Một phần | Tên file theo ngày | DOT / hạ tầng |
| Cache `/root` | `.npm` 0,67 · `.cache` 1,2 (playwright 0,63, uv 0,26, electron 0,11, pip 0,07, node-gyp 0,06) | DISPOSABLE (playwright headless = RUNTIME, agent-data gắn vào) | npm/pip/uv/playwright | theo cài đặt | 1,9 | +0,4 | 0,2 | Không (trừ playwright headless) | 1GB | ≤1 | — | dọn cache hằng tháng bằng lệnh của chính công cụ | Không | Không | Cache không trần | agent/tooling |
| Trạng thái công cụ workspace | `/opt/incomex/data/workspace-tools` (transactions, jobs, results, `.before/.json`) | RUNTIME | agent-data `workspace_*` | liên tục từ 17/09 | 0,11 | +0,11 (4,6 ngày) | ~0,7 nếu giữ nhịp | Có (idempotency, khôi phục) | TTL 14 ngày (cần chủ công cụ xác nhận) | ~0,3 | — | — | Chưa thấy TTL | Chưa rõ | — | agent-data workspace |
| Cowork runner | `/var/lib/incomex-cowork` (jobs 53, ảnh 1G thưa) | RUNTIME | cowork runner | theo job | 0,3 | +0,3 (từ 26/07) | ~0,1 | Có | theo `incomex-cowork-audit-retention` | ~0,3 | — | — | timer retention có sẵn (chưa kiểm phạm vi) | Có? | — | Cowork |
| Thư mục làm việc mission | `/opt/incomex/{evidence,staging,tmp,work,artifacts,exports}` | NONBUSINESS / DISPOSABLE | agent/mission | theo mission | 0,16 | ~+0,1 | ~0,05 | Chỉ khi mission đang mở | TTL 30 ngày rồi đưa ra ngoài hoặc xoá | ~0,05 | Drive nếu là bằng chứng | xoá >30 ngày | Không | Không | Không có quy ước | agent/mission |
| Công cụ AI | `~/.claude` + 3 bản Claude Code 0,67 · `~/.codex` 0,05 · `~/.hermes` 0,02 · `~/.gemini`: không có | RUNTIME | tự cập nhật | — | 0,75 | ~0 | ~0 | Có | tự giữ 3 bản | 0,75 | — | — | Claude Code tự giữ 3 bản | Có | — | tooling |
| Git | `/opt/incomex/.git` 0,27 (74 commit từ 24/07, không remote) · sổ git 5 phút `docs/mcp-writes/.git` 1MB · clone `data/workspace-tools/github-workspace` 0,03 · `mcp-roots` 0,03 · `nuxt-repo/.git` 0,02 | RUNTIME | commit tay / timer 5 phút / connector | — | 0,35 | ~+0,1 | ~0,05 | Có (lịch sử mã SSOT) | — | chậm | — | — | `mcp-writes-git-gc.timer` hằng tuần | Có | — | hạ tầng |
| node_modules / venv | `nuxt-repo/web` 0,7 · `venv-xlsx` 0,07 · `lark-client/.venv` 0,08 · `agent-data-repo` 0,05 | RUNTIME | build/cài | — | 0,9 | +0,07 | ~0 | Có | — | 0,9 | — | — | — | — | — | các dịch vụ |
| PostgreSQL sống | `/opt/workflow/postgres/data` (`directus` 1,72 · `incomex_metadata` 0,41 · WAL ~0,08) | BUSINESS_LIVE | Directus/DOT | liên tục | 2,2 | +0,05 | 0,03 | Có | `max_wal_size 1GB`, không slot, archive off | — | Drive hằng ngày | — | — | — | — | Directus |
| Qdrant storage | `/opt/incomex/docker/qdrant/data` (bind) | BUSINESS_LIVE | agent-data/KB | liên tục | 0,22 | ~0 | ~0 | Có | — | — | Drive hằng ngày | — | — | — | — | KB |
| Volume Docker có tên | — | — | — | — | 0 | 0 | 0 | — | — | — | — | — | — | — | Không có volume nào (mọi dữ liệu là bind) | ✖ |
| Hệ thống | swapfile 2,0 · `/tmp` 0,14 · `/var/tmp` 0 · snap: không · apt cache 0,11 + lists 0,2 · kernel cũ 6.8.0-90 ~0,3 | RUNTIME / DISPOSABLE | OS | — | ~2,8 | ~+0,3 | ~0,1 | Có | 2 kernel | ~2,8 | — | `apt clean` định kỳ | unattended-upgrades | Có | — | OS |

**File >64MB trong `/opt/incomex` ngoài vòng quay:** `backups/dieu44_v0_3_readobs_dryrun_rerun_…/prod-directus-….sql` 0,62GB (giữ lại từ 24/07 vì REF=1) · `.git/objects/pack/pack-69d1….pack` 0,26GB (git, bình thường) · `backups/vps-backup-20260718_203701.tar.gz` 0,25GB · `docker/mysql/data/directus/directus_revisions.ibd` 0,13GB (MySQL cũ trước khi chuyển PG) · `backups/mysql-pre-pg-migration.sql` 0,11GB · `backups/pg-ngoai-vong-luan-chuyen/…` 0,11GB (DEL-1 "giữ lâu"). Các file >64MB còn lại là backup vòng quay (PG, Qdrant) và JSONL của backup Lark.

**Các chỗ cách ly do mission 24/07 tạo — vẫn còn đủ:** 5 image agent-data (`5a7eb4e4e2a2`, `b6154accb6d8`, `bfe092449032`, `d53a11072c00`, `9421cd9c4303`) · 2 image claude-mcp rollback (`73f953f71632`, `37098dc6ef6e`) · 7 thư mục `/root/*-checkpoint-*` (thêm 2 thư mục cùng loại tạo sau: `integrity-sm-fallback-r0-checkpoint-20260724T144500Z`, `c2b-f1-safety`) · thư mục `dieu44_…_rerun_20260516T230306Z` · 19 dump `directus-pre-iucore-*` · `/root/vps-clean-minimum-delete-manifest.tsv`.

**Vì sao `incomex-nuxt` chạy image "không tag":** compose khai image Nuxt **theo digest** (qua một biến môi trường; đã đối chiếu biến đó trỏ cùng image `72715a92885c`, không chép giá trị cấu hình vào đây). Container được tạo theo digest nên `docker ps` hiện ID. Image vẫn mang tag `…/web-test/nuxt-ssr:latest` của registry đã chết. Mã web không nằm trong image mà ở bind `/opt/incomex/deploys/nuxt-output → /app/.output`. Nếu compose recreate thì vẫn lên đúng image `72715a92885c` (miễn là image còn tại chỗ). Có bản cứu image trên Drive từ 21/07. ⇒ Hard-KEEP. Đề xuất ở lượt dọn: gắn thêm một tag cục bộ ghim digest để không ai dọn nhầm.

**Chuỗi cha–con image** (kiểm bằng tiền tố RootFS, khớp với các dòng `FROM` trong Dockerfile trên VPS):
- claude-mcp đang chạy `r03-finalclose` (`6b48248fa29f`) ← `r03-nametwin` (`7e25b17974bd`) ← `r03-20260920` (`e33bf3c0efe3`) ← `harden-20260919` (`70f04144fb42`) ← `phase0.9` (`d34e31acc759`) ← `phase0.5a` (`7034f4425d93`) ← `phase1a` (`7c0096602a1c`). Không phải cha: `phase0.6-fs` (`1176031f7b72`), `phase0.7-nolimit` (`11cbf7d2dbd2`), `phase0.8-1e` (`1fa4430a2d0c`), `rollback` (`37098dc6ef6e`), `rollback-pre-p2b` (`73f953f71632`).
- agent-data đang chạy `agent-data-r03:20260920-finalclose` (`cb20894c3bf8`) ← `r03 nametwin` (`519b2965db4a`) ← `r03 lifecycle` (`d3f5a6f54744`) ← `hardening:20260919-harden` (`bf38e829f501`) ← `hardening:20260918-opid` (`0ba7fd24528e`) ← `hardening:20260918-final` (`e1befd50f96f`) ← `workspace:20260917-git` (`c59c891af08c`) ← `agent-data-local:latest` = `workspace-base:20260917` (`9acd60503290`). Không phải cha: `continuation:20260918` (`2bd8638edac0`), `continuation:20260918-final` (`6b391ca38bef`), `hardening:20260918` (`eefb7bbe6c98`), `workspace:20260917` (`18a85d9ad4b3`), 4 bản `agent-data-local:*` cũ, `agent-data-test` (`9421cd9c4303`).
- claude-kb đang chạy `c5-20260918` (`87787b08bf3a`) ← `v1` (`0de33745213e`) ← `v1-pre-p05a-t3` (`3cf3065bf66e`). cowork chạy `phase1b`/`phase1a`; `pre-r2a` (`9095606afe72`, `ecf31f124168`) không phải cha.

#### §5 Backup

1. **Cơ chế đang chạy:** `pg-backup.sh` (cron 02:27, DB `directus`, giữ 7 ngày) · `qdrant-backup.sh` (cron 03:00, collection `production_documents`, giữ 7 ngày ở host) · `backup-to-gdrive.sh` (cron 20:37: `pg_dump | gzip | gpg` + gói cấu hình có snapshot Qdrant mọi collection, compose, nginx/TLS, scripts; staging giữ 1 bộ) · `code-backup-to-gdrive.sh` (cron 4 lần/ngày, giữ 1 tại chỗ, 56 trên Drive) · `s177-lark-backup` (timer T2+T5) · `mcp-writes-git-snapshot` (5 phút, git cục bộ) · context-pack (3 giờ).
2. **Các lượt gần nhất:** gói Drive **25/25 lượt "Upload complete" 27/08–20/09**; status file lượt 20/09: `PASS · COMPLETE`. `pg-backup` 21/09 OK (kept=9). `qdrant-backup` 17–21/09 OK mỗi ngày. Lark: `Finished` 03/09, 07/09, 10/09, 14/09, 17/09 (lượt 17/09 không để lại thư mục ngày — cần xem). `code-backup`: ⚪ log có (cập nhật 20/09 20:02) nhưng R1 chưa bóc được kết quả từng lượt.
3. **Bản mới nhất trên Drive (liệt kê chỉ đọc):** 20/09 — dump DB 119MB + gói cấu hình 169MB + 2 `meta.json`. Thư mục mã hoá có 280 đối tượng / 18,4GB, cũ nhất 20/07.
4. **Hạn giữ thực tế so với cấu hình:** PG tại chỗ 9 bản (7 ngày ✓) · Qdrant tại chỗ 8 bản (✓) · staging 1 bộ (✓) · **Drive thư mục mã hoá: không tỉa** — 63 ngày liên tục, ~8,6GB/tháng; `MAX_REMOTE_BACKUPS=14` chỉ áp cho file cũ ở gốc. Drive còn trống ~4,96TiB nên chưa nguy, nhưng theo D02 đích phải có hạn giữ. **Bản chụp Qdrant trong container: không có hạn giữ** (nguồn số 1).
5. **Tồn dư `.tmp/.partial`:** staging sạch (trap dọn `.partial`); `lark-backups/tmp` ~0.
6. **Lồng nhau:** gói cấu hình chứa snapshot Qdrant (có chủ ý), không chứa deploy/node_modules. `code-backup` loại `.git`, `node_modules`, `.nuxt`, `.output`, cache, `dist`, `.venv` ✓. Backup Lark giữ cả JSONL giải nén lẫn tar.gz (lặp ×16 dung lượng).
7. **Khôi phục (không diễn tập, không tốn đĩa):** sha256 của 2 gói staging **khớp** `meta.json`. `gpg --list-packets` đọc được gói khoá công khai; VPS không có khoá bí mật (đúng thiết kế), không giải mã ra đĩa. Bằng chứng khôi phục gần nhất: `OFF_VPS_DECRYPTION_RECOVERY = PASS` (vps-recovery-prep 24/07) và pg-restore-test 20/05 → **đã 58 ngày, quá 30 ngày ⇒ rủi ro**. Đề xuất diễn tập khôi phục sau khi dọn xong (khi đĩa có chỗ).
⇒ Mọi file liên quan backup ngoài vòng quay đang để `UNKNOWN_HOLD` hoặc `RESCUE_BEFORE_DELETE`; không mục backup nào được xếp `DELETE_PROVEN_SAFE`.

#### §6 Manifest ứng viên dọn

Hard-KEEP (không vào lớp xoá): 12 container đang chạy + image của chúng + mọi image cha ở §4 · `72715a92885c` (Nuxt) · tag rollback R03 (`claude-mcp-local:r03-*`, `*:rollback-pre-*-20260920`, `agent-data-r03:*`) tới khi R03 CLOSED · `postgres:16` · mọi bind mount dữ liệu · `deploys/nuxt-output` (bản đang chạy) · `deploys/web-test` (cron integrity chạy script ở đây) · `context-pack/`, `context-pack-staging/` · `/root/.cache/ms-playwright/chromium_headless_shell-1223` (agent-data gắn vào).

| Nhóm | Đường dẫn / ID | GB | Lớp | Bằng chứng | Tham chiếu / phụ thuộc | Cách lùi |
|---|---|---:|---|---|---|---|
| N1 Qdrant | 160 bản chụp `production_documents-…snapshot` (+`.checksum`) trong container `incomex-qdrant` | 27,6 | `DELETE_PROVEN_SAFE` | 05, 06, 08, s19 | Không script nào đọc lại theo tên (script chỉ `docker cp` bản vừa tạo); không container khác gắn; không phải cha/rollback | Bản host 8 ngày gần nhất + gói Drive hằng ngày (có snapshot mọi collection). Xoá bằng `DELETE /collections/production_documents/snapshots/<tên>`, không `rm`, không restart |
| N2 Log Directus | `/home/node/.pm2/logs/directus-out-0.log` trong `incomex-directus` | 1,3 | `DELETE_PROVEN_SAFE` (cắt về 0) | 04, 05, 14 | File đang mở bởi pm2 ⇒ chỉ `truncate`, không `rm` | Log truy cập, không cần lùi |
| N3 Bản sao Nuxt | 66 thư mục `deploys/nuxt-output.*` cũ (70 bản sao lúc 04:11Z), giữ 3 bản mới nhất + 1 bản mốc | 2,7 | `DELETE_PROVEN_SAFE`* | 09, s19 | Script deploy chỉ dùng bản vừa tạo để hoàn tác; không cron/systemd trỏ vào; nlink=1. *Codex cần grep từng tên trước khi PASS | 3 bản mới nhất còn tại chỗ; mã nguồn web thật ở máy Mac |
| N4 context-pack | `context-pack.tmp/<BUILD_ID>` cũ hơn 3 ngày (~990 thư mục) | 1,45 | `DELETE_PROVEN_SAFE` | 09, s19 | Builder chỉ ghi `.tmp/<BUILD_ID>` của lượt mình rồi chép sang staging; `dot-dieu43-fs-verify` chỉ kiểm thư mục `.tmp` tồn tại ⇒ giữ thư mục gốc | Tái tạo bằng lượt build kế tiếp |
| N5 Cache | `/root/.npm`, `/var/lib/hermes/.npm`, `/root/.cache/{pip,node-gyp,electron}`, `/var/lib/hermes/.cache/electron` | ~1,4 | `DELETE_PROVEN_SAFE` (bằng lệnh dọn của chính công cụ) | 13, 07 | Không gồm uv/pnpm (hardlink vào venv/node_modules) và playwright headless (agent-data gắn) | Tự tải lại khi cần |
| N6 Build cache | BuildKit (0,41 riêng) | 0,4 | `DELETE_PROVEN_SAFE` — **chờ R03 CLOSED** | 02 | build lại image rollback R03 có thể cần cache | `docker builder prune --keep-storage` |
| N7 Image trung gian R03-era | `2bd8638edac0`, `6b391ca38bef`, `eefb7bbe6c98`, `18a85d9ad4b3`, `1176031f7b72`, `11cbf7d2dbd2`, `1fa4430a2d0c` | ≤0,5 (đo thật) | `KEEP_ROLLBACK_UNTIL_R03_CLOSED` → sau đó `QUARANTINE_FIRST` | 02, 16, 15 | Không container dùng; không là cha của image đang chạy; mang tag `rollback-pre-*` của chuỗi 17–19/09 | Dockerfile còn trên VPS (không bit-exact) ⇒ muốn chắc thì `docker save` trước |
| N8 Image cũ local-only | `5a7eb4e4e2a2`, `b6154accb6d8`, `bfe092449032`, `d53a11072c00`, `9421cd9c4303`, `37098dc6ef6e`, `73f953f71632`, `9095606afe72`, `ecf31f124168` | ~2–3 (Docker báo cao hơn; đo df trước/sau) | `RESCUE_BEFORE_DELETE` | 02, 16, KB 24/07 | Không container dùng, không là cha; registry đã chết ⇒ không kéo lại được | `docker save \| gzip` → Drive, ~2–3GB, kiểm sha256, khôi phục `docker load` |
| N9 Dump cũ trong container postgres | `/tmp/*.dump`, `*.sql`, thư mục `dieu45_phase3`, `nuxt-output-*`, `d28-*`… (05–06/2026) | 4,1 | `RESCUE_BEFORE_DELETE` | 05, 14 | Không cron/script trỏ vào (cần Codex grep); là bản chụp DB thật ⇒ dữ liệu nhạy cảm | Nén + gpg → Drive (~2–3GB), sha256, khôi phục `pg_restore --table` chọn lọc |
| N10 SQL tạm của agent trong container postgres | `/tmp/*.sql` sau 24/07 (~140 file) | 0,14 | `QUARANTINE_FIRST` | 14 | Agent có thể còn đang dùng file gần đây | Giữ 7 ngày gần nhất |
| N11 Tồn dư mission | 19 dump `directus-pre-iucore-*`, `vps-backup-20260718…tar.gz`, `mysql/` + `mysql-pre-pg-migration.sql`, `iu-core-70000x/`, `dieu45-phase1/`, `/root/backups/`, `/root/{p0-2-*,wsq5_*,phase7-rerun-backups,agent-runs,mcp-nolimit-stage}`, `/opt/incomex/docker/{mysql,dieu44_*}`, `directus-dump.sql` | ~5,5 | `RESCUE_BEFORE_DELETE` | 01, 10, 13, 15 | Không cron/systemd trỏ vào theo grep tên thư mục cha (cần Codex grep từng tên) | Nén + gpg → Drive, sha256, giữ 12 tháng |
| N12 Giữ theo nhãn | `pg-ngoai-vong-luan-chuyen/` (DEL-1 "giữ lâu"), `dieu44_…_rerun_20260516T230306Z` (REF=1), 9 thư mục `/root/*checkpoint*` (có thể chứa bí mật) | ~1,0 | `UNKNOWN_HOLD` | 10, 13, KB 24/07 | nhãn DEL-1 / mission bảo mật | Chờ DEL-1 và chủ mission |
| N13 DB thử | `directus_gov_test_20260602` | 1,2 | `UNKNOWN_HOLD` | 13, 17 | `DB_DELETE_GATE`: (a) ✓ đúng target, owner là role quản trị của cụm PG, tạo 02/06 · (b) ✗ 0 kết nối đang mở ở cả 3 lần đọc, nhưng trong 30 phút `xact_commit` +68, `tup_returned` +159.566 — R1 chỉ tự mở 1 phiên (~3 truy vấn) ⇒ có tiến trình khác kết nối ngắn định kỳ, chưa xác định (xem dưới) · (c) ⚠ không cron/script chạy trỏ vào, nhưng ~3.277 file tài liệu/context-pack nhắc tên · (d) ⚠ DB có `postgres_fdw` trỏ ra `incomex_metadata` (chiều ra; không DB nào trỏ vào nó), không pub/sub · (e) ✗ **không có bản ngoài VPS** · nhãn DB: DEL-1 "CẤM XOÁ" | Dump ra Drive trước; DROP chỉ sau DEL-1 + Owner |
| N14 Hermes bản cũ | `/usr/local/lib/hermes-agent` | 3,0 | `UNKNOWN_HOLD` | 13 | `/usr/local/bin/hermes` còn gọi venv của bản này; dịch vụ systemd dùng bản `/var/lib/hermes` | Hợp nhất lệnh CLI trước |
| N15 Nhỏ | `alpine:latest` (`28bd5fe8b56d`); kernel cũ 6.8.0-90 | ~0,3 | `UNKNOWN_HOLD` (chưa grep script dùng `alpine`) / để apt tự lo | 02, 07 | — | kéo lại từ Docker Hub |

`DB_DELETE_GATE` (b) — chỉ số `pg_stat_database` của DB thử: 03:40:20Z `xact_commit=146.462 · tup_returned=389.726.111` → 03:44:34Z `146.470 · 389.747.351` → 04:10:37Z `146.530 · 389.885.677`, `sessions`=87 (DEL-1 ghi 49 phiên hôm 01/08). Lưu ý: lúc 03:44:35Z R1 tự mở **1 phiên** vào DB này để đọc `pg_foreign_server` (mục d), nên số lần 3 có phần do R1. Phần tăng giữa lần 1 và 2 (trước khi R1 kết nối) và phần lớn mức tăng tới lần 3 không phải của R1; số phiên tăng 49 → 87 từ 01/08 ⇒ có thứ vẫn chạm vào DB này. Chưa xác định nguồn ⇒ gate (b) FAIL. (D05 cho phép không chờ lần đọc 3; lần 3 đã chạy xong trước khi thấy D05, giữ lại để tham khảo — kết luận `UNKNOWN_HOLD` không đổi vì (e) đã FAIL.)

**Cộng:**
- Duyệt toàn bộ `DELETE_PROVEN_SAFE` (N1–N5): **~34,4GB** (N1 27,6 · N2 1,3 · N3 2,7 · N4 1,45 · N5 1,4). Thêm N6 sau R03 CLOSED: +0,4.
- Duyệt thêm `QUARANTINE_FIRST` (N7 sau R03, N10): +≤0,6.
- Cứu rồi xoá `RESCUE_BEFORE_DELETE` (N8, N9, N11): +~12GB tại VPS; cần **~10–12GB chỗ trên Drive**, không cất lên chính ổ VPS (dump nén trực tiếp thành luồng `gzip | gpg | rclone`, như script Drive đang làm).
- `UNKNOWN_HOLD` (N12–N15): ~5,5GB, không tính vào thu hồi.

#### §7 Khoá vòi (chỉ đề xuất, chưa làm)

| Nguồn | Sửa ở đâu | Quy tắc bằng số | Lý do |
|---|---|---|---|
| Bản chụp Qdrant | `scripts/qdrant-backup.sh` | Sau `docker cp` gọi `DELETE` đúng snapshot vừa tạo (như `backup-to-gdrive.sh` đã làm); thêm bước dọn mọi snapshot server-side cũ hơn 1 ngày. Host giữ 7 ngày như cũ | Ổn định: 0 trong container thay vì +6,6GB/tháng |
| Bản sao Nuxt | `scripts/phai-cu/dung-va-trien-khai.sh` | Sau khi deploy xong: giữ 3 bản `nuxt-output.truoc-*` mới nhất + 1 bản mốc (đặt tên `*.moc-*`, tối đa 2), xoá phần còn lại | 4 × 45MB = 0,2GB; đủ hoàn tác 3 lần gần nhất |
| Log pm2 Directus | cron root hằng ngày | `truncate -s 0` log pm2 trong container khi >100MB; hoặc hạ mức log request (đổi config → cần Owner) | Trần 100MB |
| context-pack.tmp | `dot/bin/dot-context-pack-build.sh` + `dot-context-pack-retention-cleanup` | Builder xoá `.tmp/<BUILD_ID>` ngay khi chép xong; retention dọn thêm `.tmp/*` >3 ngày | ~0,04GB |
| Image Docker | quy trình build/deploy (luật cho agent) | Mỗi dịch vụ: image đang chạy + mọi cha + tối đa 2 tag rollback; bản thứ 3 trở đi: `docker save` → Drive rồi xoá. Khai `builder gc keepStorage=2GB` trong `daemon.json` (đổi config → Owner) | ~8GB image, ≤2GB build cache |
| Hermes | quy trình cập nhật Hermes | Sau mỗi lần cập nhật: `git gc --prune=now`, `npm cache clean --force`, `uv cache prune`; chỉ một bản cài | Cài ~2,9GB + cache ≤0,3GB |
| `/tmp` container postgres | luật cho agent + cron tuần | Chạy SQL qua stdin (`docker exec -i … psql < file`) thay vì chép vào container; cron tuần xoá `/tmp/*.sql` >7 ngày trong container | ~0 |
| Tồn dư mission | luật cho agent | Bằng chứng/dump mission để ở `/var/lib/incomex-audit/<mission>/`, TTL 30 ngày, hết hạn thì đưa ra Drive hoặc xoá; `/root` không phải chỗ để dump | 0 tại chỗ |
| Backup Lark | `lark-backups/bin/s177-lark-backup-prune-local` | Có `.offsite-ok` là xoá ngay thư mục JSONL giải nén; giữ 1–2 tar.gz gần nhất | ~0,1GB thay vì ~1,1GB |
| Drive | `backup-to-gdrive.sh` | Tỉa thư mục mã hoá: giữ 30 bản ngày + 12 bản cuối tháng | Đích ~12GB, ngân sách tăng ~0 |
| Cache `/root` | cron tháng | `npm cache clean --force`, `pip cache purge`; trần 1GB | ≤1GB |
| Trạng thái workspace-tools | chủ agent-data | Xác nhận/khai TTL cho `transactions/jobs/results` (đề xuất 14 ngày) | ~0,3GB |
| Log theo ngày | `/etc/logrotate.d/incomex` | Bắt `hc-executor*-*.log` với `maxage 30` | nhỏ |
| Chuông | `scripts/disk-monitor.sh` (cron giờ) + monitor push "Disk Usage" có sẵn trong uptime-kuma | Ngưỡng 80% vàng / 90% đỏ (hiện 85%, chỉ ghi log). Đẩy trạng thái lên monitor Kuma đang có (cần xác minh ai đang đẩy). Thêm đo tuần tổng các nguồn §4, cửa sổ trượt 14 ngày, báo đỏ khi ngoài nghiệp vụ >3GB/tháng | T4 |

**Cộng lại sau khi áp đủ:**
- Mức ổn định tại chỗ: nghiệp vụ ~2,5GB + vận hành ~32GB = **~34,5GB / 95,8GB (36%)** (~37,5GB nếu giữ Hermes cũ; +1GB nếu chưa vá Lark).
- Biên: trống ~61GB. Graph (AGE) cần ≤1GB (§8). 12 tháng nghiệp vụ: PG `directus` tăng ~0,03GB/tháng, dự phòng 2GB. Còn lại **~58GB**.
- Đổ thêm ra ngoài VPS: một lần ~10–12GB (cứu N8, N9, N11) + dump DB thử ≤0,2GB. Định kỳ: ~0 thêm so với hiện tại. Gói Drive hiện ~8,6GB/tháng sẽ về trạng thái ổn định ~12GB tổng nếu áp tỉa đích. Drive còn trống ~4,96TiB. Mỗi lượt đẩy hằng ngày ~1–2 phút (có một lượt 17/09 mất 36 phút).

#### §8 Chỗ cho Graph (ước lượng)

- Apache AGE là extension trong PG16 hiện có. Image postgres có AGE: +0,3–0,7GB (build thêm extension hoặc dùng image AGE cho PG16). Đổi image = restart postgres ⇒ việc riêng, sau khi dọn.
- Dữ liệu: `universal_edges` hiện **2,5MB** (bảng 0,8MB + index 1,7MB, ~2.269 dòng). Dù graph gấp 10–50 lần vẫn <0,2GB. Nạp graph cần WAL/temp tạm ≤1GB (`max_wal_size` 1GB).
- Kết luận: **sau dọn thừa chỗ** (cần ~1–2GB, sẽ có ≥45GB trống). Ngay cả bây giờ 12GB trống vẫn chứa được về dung lượng. Rủi ro thật là vòi rò ~11,5GB/tháng: không khoá vòi thì chỗ trống sẽ lại hết sau vài tháng, Graph hay không cũng vậy.

#### Ghi chú phụ (ngoài phạm vi, không xử lý)

- Crontab root có các dòng `CRON_TZ=…`, nhưng cron của Ubuntu **bỏ qua `CRON_TZ`**: log cho thấy `qdrant-backup.sh` chạy 03:00 giờ máy (CEST), không phải 03:00 UTC như nhãn trong script ghi.
- Trong lúc đo có việc khác ghi đĩa, **không phải R1**: backup Lark lượt 21/09 chạy 03:27:55Z → 03:55:37Z (thêm lượt 21/09 ~1,1GB rồi `prune-local` bỏ lượt 14/09) và **2 lần deploy Nuxt** lúc 03:30Z và 03:38Z (tạo `nuxt-output.truoc-20260921-053026` và `-053858`, mỗi bản ~43MB).
- `disk-monitor.sh` hiện chỉ ghi log (ngưỡng 85%) và mỗi giờ ghi một bản chụp vào `/opt/incomex/logs/disk-snapshots/` khi vượt ngưỡng (hiện 30 file ~1MB, có vẻ đã có giới hạn).

---

### 3. KHO BẰNG CHỨNG

- Đường dẫn: `/var/lib/incomex-audit/VPSC-R1-20260920/` trên VPS (quyền 700, ngoài mọi cây Git — `git rev-parse` báo không nằm trong work tree trước khi ghi). Chỉ mục: `INDEX.md`. Tổng: 204KB, 22 file (≤200MB). Không commit/push ở đâu.
- Nội dung: bảng tổng hợp, không có danh sách file thô toàn cây; secret đã che (`***MASKED***`), không in nội dung `.env`/dump/backup mã hoá.
- Lệnh đã chạy (tất cả chỉ đọc; `du`/`find` dưới `nice -n 19 ionice -c3 timeout`, luôn `-x`, không quét `/proc` `/sys`): `df -B1 / -h / -i` · `du --max-depth` theo tầng · `docker version/info/system df -v/buildx du/ps -a -s/images/inspect/image inspect/volume ls` · `find -newerct 2026-07-24` (chỉ khoanh vùng) + `stat %W` (btime) · `lsof +L1` · `journalctl --disk-usage` · `crontab -l` mọi user, `/etc/cron.d`, `systemctl list-timers/list-units/cat` · `grep` script (che secret) · `psql` chỉ đọc (`pg_database_size`, `pg_stat_database`, `pg_stat_activity`, `pg_foreign_server`, `pg_extension`, `pg_publication/subscription`, `pg_total_relation_size`) · `rclone lsl/lsf/size/about/lsd` (chỉ đọc) · `sha256sum` · `gpg --list-packets` (không giải mã) · `sqlite3` đọc tên monitor Kuma · `git count-objects/log`.
- Ghi duy nhất của R1 trên VPS: thư mục bằng chứng trên. Không xoá, không restart, không sửa cron/systemd/config, không docker save/tag/prune, không VACUUM/DROP.
