# PROMPT — VPSUP VPS2-TRUST-CLOSE · đóng đường tin cậy bền trước Clone CURRENT

RUN_ID: VPSUP-VPS2-TRUST-CLOSE-20260928-01
STATUS: Chỉ thực thi sau khi COLLAB có READY đúng SHA commit cuối chạm file này và Owner/GPT Host phát RUN.
Host: GPT Chat · GPT-VPSUP-20260926-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: **fs_* / Incomex VPS MCP · root gh → incomex-workspace/main**.
Runtime_Write_Path: SSH/operator hiện hữu tới VPS2; VPS1 chỉ read-check nếu cần.
Runtime VPS là SSOT. Không có fallback Directus/PG mutation.

## 0. Mục tiêu duy nhất

Đóng **mục D** còn lại của FREEZE/MINLAB trước Clone CURRENT:

1. Kiểm đúng các **đường/reference outbound trust đã giới hạn** trên VPS2, chỉ metadata/path/type, tuyệt đối không đọc/in giá trị secret.
2. Gỡ khỏi VPS2 những credential/trust bền đã chứng minh:
   - không còn cần cho host/lab cơ bản;
   - có source-of-truth/copy quản trị ở ngoài VPS2;
   - nếu VPS2 bị chiếm, credential đó có thể dùng để chạm VPS1/Drive/Secret Manager/GitHub/cloud.
3. Giữ inbound SSH quản trị của Owner/Mac.
4. Không quét credential toàn filesystem; không mở rộng sang hardening khác.
5. Nhóm dọn 5 ≈0,62 GiB = **SKIP BY HOST**, không làm trong RUN này.

Đích: trước khi đặt clone production lên VPS2, host lab không còn persistent outbound credential/trust có thể quay ngược sang hệ chính.

## 1. Read gate / collision gate

1. `fs_stat work/vps1-up-grade/COLLAB.md`.
2. Đọc: `AGENTS.md` → task COLLAB (§0, D22–D23, FREEZE KQ, P30–P34) → PROMPT này → view.html §9.
3. READY phải khớp commit cuối chạm PROMPT.
4. Xác minh FREEZE phần A/A2b/B/C vẫn giữ:
   - app/PHP/MySQL/queue stopped/no-autostart;
   - static page GDDH 200;
   - 3307/8080 không listener;
   - volume/data/backup nguyên;
   - swap 4 GiB;
   - disk free vẫn đủ lab.
5. Xác minh không có executor/RUN khác đang mutation VPS2. Có ⇒ DỪNG.
6. AD1-FIX gen2 đang chạy nền trên VPS1:
   - không gọi Guard/ruleset;
   - không restart/mutate `agent-data`/`claude-mcp`;
   - không sửa Kuma/AD1 watcher.
7. Repo/version conflict tạm thời: re-read/diff; task path không đổi thì retry. Runtime conflict tuyệt đối không tự vượt.

## 2. Permission rule của client — KHÔNG mở rộng

Claude Code auto-mode có thể chặn bước audit với nhãn `Credential Exploration`.

- **Không** thêm permission rule Bash rộng/toàn cục.
- **Không** tắt cơ chế an toàn của client.
- Nếu client chặn một lệnh metadata-only đã đúng allowlist dưới đây, hoặc đúng phép T1 chỉ **suy public fingerprint từ private key đã biết path mà không in key material**, chuyển sang chế độ approval bình thường và yêu cầu Owner **Allow once** cho đúng lệnh đó.
- Không yêu cầu Owner tự chạy shell bằng `!`.
- Không gộp thêm lệnh đọc secret/value vào cùng approval.
- Không `cat`/in private key; T1 chỉ được để công cụ đọc nội bộ và xuất fingerprint.
- Nếu không thể có approval một lần cho metadata-only/T1 inspection đúng allowlist ⇒ DỪNG, không lách.

## 3. Audit allowlist — chỉ metadata/reference, không value

Không `find /` hay grep toàn filesystem cho từ khóa secret/token/password.

Chỉ được kiểm các bề mặt chuẩn sau:

### A. SSH outbound
- `/root/.ssh/` và home của service user thực có trên VPS2.
- Chỉ liệt kê: tên file, loại file, owner/mode, public-key fingerprint nếu suy được từ private key **mà không in private material**.
- `authorized_keys` = inbound management, **KEEP**.
- Private key outbound chỉ là candidate nếu config/known_hosts/ssh config/service reference chứng minh được dùng ra ngoài **hoặc T1 chứng minh VPS1 đang trust public key tương ứng**.

### T1. Đối chiếu trust trực tiếp VPS2 → VPS1 — READ-ONLY
- Chỉ áp với **private key đã phát hiện trong các SSH path allowlist ở mục A**; không mở rộng thành tìm private key trên toàn VPS2.
- Với từng key đó, suy public fingerprint nội bộ mà **không in private/public key material**.
- Trên VPS1 chỉ đọc fingerprint của các dòng `authorized_keys` thuộc `root` và service user có SSH login thực tế; không sửa file, không in raw key.
- So sánh và ghi đúng một kết luận tổng: `VPS1_TRUSTS_VPS2_KEY=YES|NO` + candidate ID tương ứng nếu YES.
- Nếu `YES` và private key tương ứng **vẫn còn trên VPS2** ⇒ candidate đó không được `KEEP_JUSTIFIED`; phải `REMOVE` an toàn hoặc `STOP_UNKNOWN`. G1 **không PASS** khi key có thể pivot vẫn còn trên VPS2.
- Nếu `YES` nhưng private key tương ứng đã `REMOVE` khỏi VPS2 trong RUN này ⇒ G1 có thể PASS; ghi follow-up VPS1 để xoá dòng `authorized_keys` cũ ở lượt VPS1 sau. **Không sửa VPS1 trong RUN này.**
- Nếu key cần passphrase/agent state để suy fingerprint mà không thể làm an toàn ⇒ `STOP_UNKNOWN`, không xin/đọc passphrase.

### B. rclone / Drive
- Chỉ kiểm **sự tồn tại + path + owner/mode + tên remote**, không in token/config value:
  - `/root/.config/rclone/rclone.conf`
  - path rclone config được service/cron hiện hữu tham chiếu nếu khác.
- Không gọi remote API chỉ để audit credential.

### C. Google/GSM
- Chỉ kiểm existence/path/type của:
  - Google ADC/service-account file path được env/systemd/compose hiện hữu tham chiếu;
  - `/root/.config/gcloud/` hoặc `/root/.config/google-cloud-sdk/` nếu có.
- Không in JSON/key/client_secret/access_token/refresh_token.

### D. GitHub
- Chỉ kiểm private key/PAT/file path được git remote, ssh config, cron/systemd/compose hiện hữu trên VPS2 tham chiếu.
- Không đọc PAT/token value; không gọi GitHub để “test” credential.

### E. VPS1 / cloud / app outbound
- Chỉ đọc **env var names + referenced file paths** từ compose/systemd/cron/config đang chạy hoặc giữ cho lab.
- Các tên cần nhận diện: VPS1 SSH/key path, Secret Manager credential path, cloud service-account path, GitHub/rclone path.
- Không `cat` file secret, không dump environment values, không `set`, không `/proc/*/environ`.

## 4. Phân loại

Mỗi candidate chỉ ghi:

`ID | type | path | owner/mode | referenced_by | destination_class | source_of_truth_outside_VPS2=YES|NO|UNKNOWN | needed_now=YES|NO | decision`

Decision:
- `KEEP_INBOUND`: inbound SSH Owner/Mac.
- `REMOVE`: outbound credential bền, không cần, và **hoặc** SoT ngoài VPS2 = YES **hoặc** thuộc ngoại lệ T1b `RETIRE_LOCAL_ONLY_KEY` dưới đây.
- `KEEP_JUSTIFIED`: thật sự cần cho host basic operation; phải ghi lý do cụ thể.
- `STOP_UNKNOWN`: SoT hoặc dependency mơ hồ ⇒ không xóa, KQ DỪNG cho mục D.

Không ghi fingerprint đầy đủ nếu không cần; rút gọn đủ đối chiếu.

## 5. Gỡ trust — chỉ exact candidate

Chỉ với `REMOVE`:

1. Mặc định phải chứng minh source-of-truth/copy quản trị ngoài VPS2 trước khi xóa.
   - **Ngoại lệ T1b · `RETIRE_LOCAL_ONLY_KEY`:** chỉ áp cho private key trong SSH allowlist khi T1=YES, key đó được xác định là cặp khoá riêng của VPS2, `needed_now=NO`, không phải inbound management, không có service/config/job còn phụ thuộc, và mục tiêu là chấm dứt hẳn khả năng VPS2 SSH vào VPS1. Trường hợp này **không cần** SoT ngoài VPS2 và **không được tạo bản sao mới** chỉ để rollback; xóa là retire có chủ đích, phải Owner `Allow once`, ghi rõ `RETIRE_LOCAL_ONLY_KEY` trong bảng.
   - Nếu chưa chứng minh được đủ tất cả điều kiện T1b ⇒ không dùng ngoại lệ; quay về SoT=YES hoặc `STOP_UNKNOWN`.
2. Chụp metadata + sha256 **nếu việc hash không đọc/in secret ra output**; không tạo thêm bản sao secret. Với `RETIRE_LOCAL_ONLY_KEY`, chỉ giữ metadata/fingerprint rút gọn, không backup private key.
3. Xóa đúng file/config credential hoặc bỏ đúng reference.
4. Verify:
   - path/reference không còn;
   - inbound SSH Owner/Mac vẫn hoạt động;
   - static GDDH vẫn 200;
   - e-learning app vẫn stopped;
   - 3307/8080 vẫn không listener.
5. Không revoke credential ở provider trong RUN này trừ khi PROMPT nói rõ — mục tiêu là VPS2 không giữ copy. Provider-side revoke thuộc task nguồn nếu credential đó còn được dùng nơi khác.

Nếu removal ảnh hưởng host/lab basic operation ⇒ rollback reference từ source-of-truth chỉ khi cần, rồi DỪNG. Riêng `RETIRE_LOCAL_ONLY_KEY` không có rollback key theo thiết kế; vì vậy phải chứng minh `needed_now=NO` + không dependency **trước** khi xin Owner Allow once.

## 6. Những thứ KHÔNG làm

- Không xoá nhóm dọn 5.
- Không dọn thêm disk/cache/image.
- Không rotate/nâng MySQL.
- Không sửa IPv6.
- Không sửa static page/Caddy trừ rollback nếu regression.
- Không reboot.
- Không clone CURRENT.
- Không copy secret mới vào VPS2.
- Không tạo service/port/user/key mới.
- Không sửa backup BK1.
- Không xử lý `queue.sqlite` trong RUN này.
- Không triển khai busy lease mới.

## 7. Acceptance G1

G1 PASS khi:
- FREEZE invariants vẫn PASS;
- VPS2 đủ disk/swap cho lab;
- audit allowlist hoàn tất mà không đọc/in secret value;
- tất cả persistent outbound credential/trust candidate đã:
  - REMOVE an toàn theo SoT=YES, hoặc
  - REMOVE theo T1b `RETIRE_LOCAL_ONLY_KEY` đủ gate + Owner Allow once, hoặc
  - KEEP_JUSTIFIED với lý do không cho phép pivot sang VPS1/Drive/Secret Manager/GitHub;
- không còn `STOP_UNKNOWN`;
- inbound SSH Owner/Mac còn hoạt động;
- T1 đã ghi `VPS1_TRUSTS_VPS2_KEY=YES|NO`; nếu YES thì không còn matching private key trên VPS2 trước khi PASS;
- 0 VPS1 mutation;
- 0 agent-data/claude-mcp restart/mutation;
- không gọi Guard/ruleset;
- nhóm dọn 5 SKIP không ảnh hưởng PASS.

Nếu có `STOP_UNKNOWN` ⇒ KQ DỪNG, không Clone CURRENT.

## 8. Đầu vào khóa cho Clone CURRENT

Nếu G1 PASS, ghi rõ vào COLLAB:

Clone CURRENT **bắt buộc**:
- chỉ bind `127.0.0.1`/internal; truy cập bằng SSH tunnel;
- chặn outbound của clone trước boot;
- không chép Telegram/GitHub/OpenAI/Agent-data/rclone/GSM credential production;
- Directus `KEY/SECRET` khác production;
- static token trong `directus_users.token` của clone phải vô hiệu/đổi trước boot;
- singleton/cron/Flow webhook/request/backup-retention/Hermes/Kuma/git-push = disabled trước boot;
- dữ liệu production có thể clone, nhưng **credential production không được clone**.

## 9. Report

Không tạo repo file mới.

### `COLLAB.md`
- Dòng hiện hành;
- `KQ@VPSUP-VPS2-TRUST-CLOSE-20260928-01 XONG|DỪNG`;
- bảng candidate chỉ path/type/reference/decision, không secret; candidate T1b phải ghi `RETIRE_LOCAL_ONLY_KEY` + `needed_now=NO`;
- T1: `VPS1_TRUSTS_VPS2_KEY=YES|NO`; nếu YES ghi candidate đã REMOVE và follow-up VPS1, không in raw key;
- nếu XONG: `G1 PASS · NEXT Clone CURRENT`.

### `view.html`
Cập nhật khối FREEZE/MINLAB:
- A/B/C ACCEPTED;
- group 5 = SKIP BY HOST;
- D TRUST-CLOSE PASS|STOP;
- số candidate remove/keep/unknown;
- NEXT Clone CURRENT nếu G1 PASS.

Commit:
`[Claude Code] VPSUP-VPS2-TRUST-CLOSE · đóng outbound trust trước clone`

Kết thúc Owner đúng một dòng:
`XONG` hoặc `DỪNG — <lý do>`.

## 10. Sau RUN — không làm

Nếu XONG/G1 PASS: Host mới phát Clone CURRENT.
Nếu DỪNG: Host xử lý đúng candidate UNKNOWN; không quay lại cleanup VPS2.

Không tự nhảy bước.
