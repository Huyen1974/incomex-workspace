# PROMPT — VPSUP VPS2-FREEZE-MINLAB · đóng băng e-learning + chuẩn bị lab

RUN_ID: VPSUP-VPS2-FREEZE-MINLAB-20260928-01
STATUS: Chỉ thực thi sau khi COLLAB có READY đúng SHA commit cuối chạm file này và Owner/GPT Host phát RUN.
Host: GPT Chat · GPT-VPSUP-20260926-A
Host_Revision: VPSUP-P29-FREEZE-MINLAB
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: **fs_* / Incomex VPS MCP · root gh → incomex-workspace/main**.
Runtime_Write_Path: SSH/operator hiện hữu tới VPS2; VPS1 chỉ read-check các invariant cần thiết.
Runtime VPS là SSOT. Không có fallback Directus/PG mutation.

## 0. Mục tiêu duy nhất

Sau BK1, biến VPS2 thành **lab tạm an toàn**, không còn nuôi e-learning online:

1. Freeze toàn bộ stack ứng dụng e-learning trên VPS2: stopped + no-autostart, giữ compose/volume/image + dữ liệu/backup để phục hồi. **Ngoại lệ duy nhất:** địa chỉ `elearning.incomexsaigoncorp.vn` vẫn được phép trả một trang tĩnh “Chương trình đang nâng cấp” để iframe “Chương trình tiếng Nhật” trên GDDH không vỡ; trang này không PHP/DB/queue.
2. Khi stack dừng, 3307/8080 phải hết listener; `cms_queue` hết sinh log.
3. Dọn đúng phần tái tạo được đã kiểm ở G0 để lấy lại capacity cho lab; không đụng volume/dữ liệu e-learning.
4. Thêm 4 GiB swap nếu chưa có để VPS2 đủ đệm cho lab.
5. Gỡ **persistent outbound trust/credential** từ VPS2 tới VPS1, Drive, Secret Manager, GitHub nếu có và nếu đã có source-of-truth khác; không tạo trust mới.
6. Không nâng/sửa MySQL, không sửa IPv6, không sửa queue, không dựng backup/monitor dài hạn cho VPS2.
7. Không triển khai cờ/lease mới trong VPSUP; scoped lease thuộc `mcp-workspace`, tái dùng khi sẵn sàng.

Đích sau RUN: VPS2 = SSH vào được + đủ disk/swap + không e-learning chạy + không credential bền dẫn sang hệ chính + sẵn làm nơi clone/nâng VPS1.

## 1. Read gate / collision gate

1. `fs_stat work/vps1-up-grade/COLLAB.md`.
2. Đọc: `AGENTS.md` → task COLLAB (§0, D22–D23, BK1 KQ, P28) → PROMPT này → view.html §8–§10.
3. READY phải khớp commit cuối chạm PROMPT.
4. Xác minh BK1 rescue e-learning 09/08 đã có offsite Drive + restore proof; source/volume VPS2 còn nguyên.
5. Xác minh không có người học/user thật hoặc dependency hiện tại cần e-learning online. Nếu có bằng chứng ngược chỉ đạo Owner ⇒ DỪNG và báo.
6. Xác minh không có executor/RUN khác đang mutation VPS2 hoặc cùng compose/docker storage. Có ⇒ DỪNG.
7. Repo/version conflict tạm thời do task khác: re-read/diff; task path không đổi thì retry. Runtime/executor conflict tuyệt đối không được “chờ vài phút rồi tự làm”.
8. `MCPW-AD1-FIX` gen2 watcher đang chạy nền trên VPS1:
   - không gọi Guard/ruleset PRE/POST trong RUN này;
   - không restart/mutate `agent-data` hoặc `claude-mcp`;
   - không sửa Kuma/AD1 watcher.
9. Nếu lượt cron BK1 thật đầu tiên đã sinh artifact thì chỉ read-check nhanh trạng thái; nếu chưa tới giờ thì ghi `PENDING_TIME`, **không chờ** và không tạo watcher mới.

## 2. Cấm

- Không reboot VPS1/VPS2.
- Không nâng MySQL/PHP/Laravel/nginx/Caddy/Docker hay package e-learning.
- Không rotate MySQL credential trong RUN này nếu stack được freeze thành công.
- Không sửa IPv6/default route.
- Không sửa `cms_queue`; mục tiêu là stop cùng stack.
- Không tạo recurring e-learning backup/monitor.
- Không xóa named volume/bind data/DB e-learning.
- Không xóa backup 09/08 trên VPS2 hoặc BK1 trên Drive.
- Không xóa compose/source/config cần để phục hồi.
- Không prune toàn bộ image/volume mù quáng.
- Không đụng image/digest VPS1 cần cho CURRENT clone.
- Không xóa `incomex-web-buildstage`.
- Không tạo credential/key/service/DB/port mới.
- Không import secret từ VPS1/Drive/Secret Manager vào VPS2 để “chuẩn bị lab”.
- Không in token/password/private key/rclone config/service-account value.

## 3. PRE — inventory ngắn, đủ rollback

Chụp:
- disk/free/inode/RAM/swap;
- `docker ps -a`, compose project labels, container StartedAt/restart policy;
- exact compose/config path + sha256;
- named volumes/binds + size;
- image IDs/digests;
- listeners 22/80/443/3307/8080 v4/v6;
- e-learning BK1 artifact/source checksum reference;
- candidate cleanup theo sổ G0;
- outbound credential/trust inventory **chỉ tên/path/type**, không value;
- current `/etc/fstab` + swap state.

Lưu before-state/rollback dưới hồ sơ runtime:
`/opt/incomex/work/vps1-up-grade/VPS2-FREEZE-MINLAB-20260928/`
Chỉ metadata/hash/checkpoint/log sanitized; không secret.

Phân loại đúng compose project e-learning trước khi stop. Nếu không phân biệt được container/volume thuộc e-learning với lab/system ⇒ DỪNG.

## 4. A · Freeze e-learning

### A1 · No-autostart
- Xác định tất cả container thuộc đúng e-learning compose/project.
- Giữ nguyên compose/source, volume/bind, image.
- Đặt restart policy của **đúng e-learning containers** về no-autostart theo cách bền và rollback được; nếu source compose có `restart: always/unless-stopped`, sửa source tối thiểu để lần reboot/compose sau không tự bật ngoài ý muốn.
- Không đụng container ngoài project.

### A2 · Stop
- Stop toàn bộ e-learning project theo dependency-order an toàn.
- Không `down -v`, không remove volume.
- Có thể remove riêng container `cms_queue` sau khi đã stop nếu việc đó là cách an toàn nhất để giải phóng writable-layer log và compose/image/volume vẫn đủ tái tạo; nếu không chắc ⇒ chỉ stop, không remove.

### A2b · Giữ URL công khai bằng trang tĩnh
- Cấu hình web server hiện hữu đang phục vụ `elearning.incomexsaigoncorp.vn` để mọi path trả đúng **một trang HTML tĩnh** với thông báo `Chương trình đang nâng cấp`.
- Không script ngoài, không form, không API/PHP/MySQL/queue; không tạo service/port mới; giữ TLS/domain hiện hữu.
- Không gửi header làm iframe GDDH bị chặn. Không nới CSP ngoài mức hiện tại nếu không cần.
- Nếu web server hiện hữu nằm trong compose e-learning thì chỉ được giữ **riêng lớp web tĩnh tối thiểu** chạy; application/PHP/MySQL/queue vẫn stopped/no-autostart.
- Nếu không làm được A2b bằng web server/service hiện hữu mà phải tạo service/port mới ⇒ **bỏ A2b, ghi gap, vẫn freeze**; không mở rộng scope.

### A3 · Verify freeze
- 0 application/PHP/MySQL/queue container RUNNING; chỉ được phép còn đúng lớp web tĩnh A2b nếu cần.
- restart policy/no-autostart đúng.
- 3307/8080 = không listener v4/v6.
- 80/443 chỉ còn lớp trang tĩnh A2b (hoặc offline nếu A2b phải bỏ). Từ ngoài: GET `elearning.incomexsaigoncorp.vn` = 200 với nội dung tĩnh; iframe “Chương trình tiếng Nhật” trên GDDH hiển thị thông báo, không ô lỗi.
- SSH 22 vẫn reachable.
- volume/bind/data count/size vẫn hiện hữu, không mất.
- BK1 source backup + Drive backup vẫn tồn tại.

### A4 · Credential rule
- Không rotate MySQL lúc stack đã stopped.
- Ghi cờ vận hành `ROTATE_BEFORE_NEXT_START`: nếu bất kỳ lý do nào phải bật lại e-learning trên VPS2, trước start phải phát RUN riêng để rotate/root-localhost + kiểm security.
- Không tự bật lại trong RUN này.

## 5. B · Cleanup để lấy chỗ làm lab

Chỉ sau A PASS.

KEEP tuyệt đối:
- named volume/bind/data e-learning;
- compose/source/config e-learning;
- bản backup 09/08 local + BK1 offsite reference;
- image/ID cần để phục hồi e-learning nếu không chứng minh pull/rebuild được;
- exact image/digest khớp VPS1 cần cho CURRENT parity clone;
- `incomex-web-buildstage`.

DỌN được khi live evidence khớp G0:
1. writable-layer/log rác của `cms_queue` sau freeze;
2. Docker build cache reclaimable không được container/image KEEP tham chiếu;
3. image build/test cũ không container dùng và không nằm KEEP_SET;
4. systemd journal về khoảng 200 MiB;
5. duplicate/test artifact tháng 8 đã được G0 phân loại tái tạo được và không phải backup/source duy nhất.

Luật:
- `docker system prune -a --volumes` = CẤM.
- Xóa image theo exact ID/list sau khi kiểm reference; không pattern mù.
- Không xóa volume.
- Mỗi nhóm dọn: đo before→delete→measure after.
- Mục tiêu mềm: thu hồi khoảng 20–26 GiB; nếu ít hơn nhưng KEEP đúng thì PASS, không cố xóa thêm để đạt số.

## 6. C · Swap/capacity

- Nếu swap <4 GiB: tạo 1 swapfile 4 GiB bằng cơ chế chuẩn host, mode 600, `mkswap/swapon`, thêm đúng một entry bền trong `/etc/fstab`.
- Nếu swap đã ≥4 GiB: giữ, không tạo thêm.
- Không tune sâu kernel trong RUN này.
- Không cần resource-cap container e-learning vì stack stopped; resource cap cho CURRENT/TARGET sẽ nằm trong RUN clone.
- Verify `free`, `swapon`, `/etc/fstab`, reboot-persistence bằng config inspection; **không reboot**.

## 7. D · Gỡ persistent outbound trust khỏi VPS2

Mục tiêu: VPS2 bị chiếm không lan sang VPS1/Drive/Secret Manager/GitHub.

Audit root + service homes + `/etc` + compose env references cho:
- SSH private key dùng outbound;
- rclone config/token;
- Google service-account/GSM credential;
- GitHub deploy key/PAT;
- VPS1 private key/credential;
- cloud/API credential không cần cho e-learning stopped/lab.

Không tính inbound `authorized_keys` Owner/Mac là outbound trust; phải giữ đường SSH quản trị.

Với mỗi credential:
- xác minh source-of-truth/copy quản trị nằm ngoài VPS2;
- nếu là persistent outbound trust và không cần cho host basic operation ⇒ remove khỏi VPS2 + verify không còn reference;
- nếu không chứng minh được source-of-truth hoặc có dependency hợp lệ ⇒ DỪNG mục D cho credential đó và báo, **không xóa mù**.

Future lab:
- dữ liệu/config từ VPS1 được push vào hoặc dùng credential tạm theo từng RUN;
- không cất key bền trên VPS2.

Không triển khai busy-lock/lease mới; ghi `DEFER_TO_MCPW_SCOPED_LEASE`.

## 8. POST / acceptance

PASS khi:
- BK1 e-learning offsite/source vẫn nguyên;
- 0 application/PHP/MySQL/queue e-learning running + no-autostart; chỉ static-only web A2b được phép chạy;
- 3307/8080 không listener; 80/443 nếu còn thì chỉ phục vụ HTML tĩnh A2b;
- SSH vẫn tốt;
- volume/bind/data e-learning nguyên;
- `cms_queue` không còn sinh log;
- disk free tăng rõ và KEEP_SET nguyên; ghi exact GiB before→after;
- swap ≥4 GiB và config bền;
- không còn persistent outbound trust đã xác minh không cần; exceptions liệt kê theo path/type, không secret;
- 0 agent-data/claude-mcp mutation/restart;
- không gọi Guard/ruleset, không làm nhiễu AD1 gen2;
- không MySQL upgrade/rotate, không IPv6 fix;
- source/health VPS1 không đổi.

DỪNG nếu:
- có active executor conflict;
- e-learning thực tế có user/dependency cần online;
- volume/data ownership không rõ;
- cleanup chạm KEEP_SET;
- outbound credential unique/source-of-truth mơ hồ mà cần xóa;
- SSH management bị ảnh hưởng;
- phát hiện compromise active.

## 9. Rollback

Lưu exact compose/restart-policy/fstab before-state.
Rollback chỉ cho:
- no-autostart/source compose delta;
- swap/fstab nếu swap gây lỗi;
- credential removal chỉ khi có backup/source-of-truth đã chứng minh.

**Không rollback bằng cách tự bật lại e-learning sau khi RUN XONG.**
Nếu Owner cần bật lại, dùng RUN riêng `ROTATE_BEFORE_NEXT_START`.

## 10. Report

Không tạo repo file mới.

### `view.html` §9
Khối ngắn `VPS2 FREEZE/MINLAB`:
- e-learning app/PHP/MySQL/queue RUNNING→STOPPED/no-autostart; static URL A2b PASS|GAP;
- port/listener before→after;
- disk/free before→after + cleanup groups;
- swap;
- outbound trust removed/exceptions;
- BK1/volume preservation;
- residual `ROTATE_BEFORE_NEXT_START`;
- NEXT = Clone CURRENT.

### `COLLAB.md`
- Dòng hiện hành;
- `KQ@VPSUP-VPS2-FREEZE-MINLAB-20260928-01 XONG|DỪNG`;
- không mở Owner blocker nếu không thật sự cần quyết định mới.

Commit qua `fs_transaction`:
`[Claude Code] VPSUP-VPS2-FREEZE-MINLAB · freeze e-learning và chuẩn bị lab`

Kết thúc Owner đúng một dòng: `XONG` hoặc `DỪNG — <lý do>`.

## 11. Sau RUN — không làm

Host mới phát:
1. CURRENT clone/rehearsal trên VPS2;
2. nâng từng lớp + TARGET;
3. rollback/cutover rehearsal;
4. production cutover VPS1;
5. canh 7 ngày;
6. chuyển e-learning về VPS1 (stopped mặc định nếu chưa dùng) + backup cuối + huỷ VPS2 đúng kỳ.

Không tự nhảy bước.
