# Điều tra Hermes: định danh, sudo/root và Google Secret Manager

**Ngày:** 23/10/2026; thu bằng chứng khoảng12:00–12:14 +07. **Người điều tra:** Codex. **Phạm vi:** chỉ điều tra, không triển khai; theo chỉ đạo trực tiếp mới của Owner. **Dự án repo:** `work/hermes-joint-workspace/`, tương ứng luồng điều phối `work/MCP+HERMES/7(N1-N6)`. Báo cáo gửi GPT Host xem xét trước khi Owner quyết triển khai.

## 1. Kết luận ngắn

**Có thể dùng phân quyền sẵn có để chặn Hermes tự nâng lên root và tự truy cập GSM. Chưa thấy cần thêm gateway, Guard, registry định danh hay hệ thống trung gian.** Phần lớn nền tảng đã có; cần dùng đúng danh tính và đóng đúng đường vòng của hai cửa.

Hermes đã có user Linux riêng và thẻ MCP riêng. Hai dịch vụ đang chạy có `NoNewPrivileges`; Hermes không có credential Google được đăng nhập trong profile gcloud của mình. Tuy nhiên sudoers còn **một grant cho sáu lệnh quản lý dịch vụ Hermes**. Nếu yêu cầu là không có sudo hoàn toàn, đây là thay đổi rõ ràng nhỏ nhất cần làm.

**Không thể dùng hai cửa này để chứng nhận “Hermes không bao giờ thấy bất kỳ giá trị nào từng lấy từ GSM”.** Một số khóa cần cho Hermes chạy đã được loader root lấy rồi cấp cho chính UID Hermes. IAM chặn việc gọi GSM, không thu lại bản sao khóa đã đưa cho ứng dụng. Cần phân biệt yêu cầu này với việc cấm Hermes dùng credential Google hoặc quyền dịch vụ khác để đọc secret ngoài chức năng của nó.

Không gỡ các rào hiện hành trong lượt điều tra. Không coi việc phải tách model/dispatcher, bảo vệ Host/READY hoặc triển khai B/C/E là điều kiện thứ ba bắt buộc của phương án hai cửa.

## 2. Bảng gửi GPT Host

| Vị trí | Quyền hiện tại | Nguy cơ thực tế | Cách chặn tối thiểu |
|---|---|---|---|
| **Sudo/root** | Hermes UID/GID10301, chỉ group `hermes`; gateway/serve là service host, không phải container; `NoNewPrivs=1`, `CapEff=0`. Sudoers còn sáu lệnh systemctl cố định cho hai service Hermes, không shell tùy ý. | Không phải root toàn quyền. Chính sách sáu lệnh vẫn áp nếu có tiến trình cùng UID không mang NNP; chưa chứng minh Hermes hiện tạo được tiến trình như vậy. Không thể báo “sudoers=0”. Các đường tương đương root phải tính cùng cửa này. | Giữ user hiện có và NNP. Nếu chốt zero-sudo, thu hồi đúng grant `hermes ALL=(root) NOPASSWD: HERMES_UPDATE_UNITS` trong `/etc/sudoers.d/90-hermes-update`; không xóa chương trình sudo toàn VPS, không khóa terminal. |
| **GSM** | Hermes không có Google principal riêng thấy trong project policy; profile gcloud Hermes không có credential/token đã đăng nhập. Root loader dùng Google principal riêng có quyền đọc GSM. | Google IAM nhìn credential, không nhìn nhãn agent hay UID Linux. Nếu Hermes lấy được credential Google của root/backend thì IAM xem lời gọi là backend. Không được chỉ kiểm `gcloud auth list` của Hermes rồi chốt an toàn. | Không cấp `secretmanager.versions.access`, quyền sửa IAM/impersonation cho principal Hermes nếu sau này có. Giữ credential Google/backend ngoài quyền đọc/ghi của UID Hermes bằng owner/group/ACL hiện có. Không thu hồi hàng loạt quyền các dịch vụ đang cần GSM. |
| **Đường gián tiếp liên quan** | MCP đã map credential riêng → `agent_id=hermes` ở server. Helper đang có là menu cố định; B/C/E mới dựng vẫn dormant. File root/service và queue đặc quyền đã kiểm không cho Hermes ghi. | Cho sửa code/config hoặc mượn credential của một principal đặc quyền sẽ đi vòng hai cửa. Ngược lại, một backend tự lấy secret để trả dữ liệu chức năng không đồng nghĩa Hermes được đọc secret. | Dùng lại identity/profile và quyền file/service sẵn có. Không biến helper thành generic root exec hoặc generic secret-read proxy. Không triển khai B/C/E hay tách dispatcher chỉ để làm bảng kiểm xanh. |

## 3. “Thẻ định danh” đã có — không cần dựng lại

Ba loại danh tính có chức năng khác nhau:

| Nơi thực thi | Định danh thực tế | Cơ chế đang có |
|---|---|---|
| Terminal/tiến trình Hermes trên VPS | Linux `hermes`, UID/GID10301 | Linux user/group, systemd `User=hermes`, NNP, quyền file |
| Hermes gọi MCP | `agent_id=hermes`, label `agent-gw/hermes` | Credential riêng tham chiếu `AGENT_GW_KEY_HERMES`, map phía server tại `/mcp-agent` |
| Dịch vụ truy cập Google | Google service account của chính dịch vụ | Google IAM, gcloud/ADC hoặc credential được loader giữ |

`workspace-tools.json` đã có profile riêng cho Hermes và các bề mặt `gpt-web`, `codex`, `claude-code`, `claude-chat-web`, `google-main`. Mã xác thực server từ chối profile tắt, credential thiếu/trùng hoặc match nhiều profile; không tin `agent_id` tự khai trong nội dung yêu cầu. Thêm một agent khi thật sự cần chỉ dùng mẫu profile/credential hiện có, không mở registry hoặc route mới.

**Không cần tạo Google service account cho agent không dùng Google API.** Không cấp quyền GSM là cách đơn giản hơn cấp rồi dựng thêm lớp chặn. Hai agent dùng cùng UID hoặc cùng Google credential vẫn là cùng principal tại cửa tương ứng, dù có tên/model khác nhau. Đây là điều cần ghi đúng trong map hiện có, không phải lý do xây một “hệ điều hành định danh” mới.

Model và dispatcher Hermes hiện dùng chung UID/key. Điều này còn giới hạn về xác thực ai tạo quyết định workflow, nhưng tự nó không cấp root hoặc GSM. Không kéo vấn đề đó thành điều kiện bắt buộc ngoài hai cửa Owner giao lần này.

## 4. Bằng chứng cửa sudo/root

### 4.1. Danh tính đang chạy

- Hai service `hermes-gateway.service` và `hermes-serve.service`: `User=Group=hermes`, không supplementary group; PID quan sát2896 và2687324. Metadata UID/GID đều10301. Có quan sát child cùng UID; thông thường fork/exec kế thừa UID và NNP, remote MCP backend là principal khác.
- Cả hai có `NoNewPrivileges=yes`, `ProtectSystem=strict`, `ProtectHome=yes`, `RestrictSUIDSGID=yes`; runtime `NoNewPrivs=1`, effective/ambient capabilities=0. Không có Exec prefix `+`/`!` nâng quyền trong unit đã kiểm. Capability bounding set là trần, không đồng nghĩa process đang có mọi quyền trong trần.
- Shell tài khoản là `nologin`; điều đó không ngăn terminal tool chạy dưới UID Hermes và không thay thế phân quyền sudo.

Linux xác nhận NNP kế thừa qua fork/exec và chặn exec nhận thêm quyền setuid/file capabilities; nó không tự cô lập credential hay chặn mọi khả năng dùng dịch vụ đặc quyền bên ngoài. [Tài liệu Linux Kernel](https://www.kernel.org/doc/html/latest/userspace-api/no_new_privs.html).

### 4.2. Sáu ngoại lệ sudo còn thật

`sudo -l -U hermes` cho đúng ba action `start`, `restart`, `reset-failed` với `--no-ask-password` cho mỗi service `hermes-gateway.service` và `hermes-serve.service`, tổng sáu command. Không thấy shell, wildcard argv hoặc sudo/admin group trong kết quả. File sudoers root:root0440; Hermes không sửa được.

NNP đang chặn sudo nâng quyền trong cây service hiện hành. Nhưng sudoers là chính sách theo user, nên không nên dựa chỉ vào NNP của hai service để gọi cả danh tính “không có sudo”. Nếu Owner muốn zero-sudo, chỉ cần thu hồi một grant nói trên. Không sửa helper/Guard toàn hệ vì việc này.

### 4.3. Các đường root tương đương đã xem

- Docker socket root:docker0660; Hermes đọc=false, ghi=false; không trong group docker. Không thấy LXD/Podman socket ở các đường mặc định được kiểm. Quyền điều khiển Docker có thể tác động filesystem host, nên phải xem nó là đường root tương đương, không phải một cửa thiết kế mới. [Docker Engine security](https://docs.docker.com/engine/security/).
- Root SSH directory/key metadata: Hermes không đọc được; không đọc byte key.
- Các unit/drop-in, loader, preflight, relay, updater và parent directory được kiểm thuộc root và Hermes không ghi được. Code Hermes có thể ghi bởi Hermes nhưng chạy dưới Hermes, không tự trở thành code root.
- System bus socket có mode thông thường0666; không tự cấp quyền root. Các rule polkit admin/default đã kiểm không grant quản trị cho Hermes; nhóm admin/sudo không chứa Hermes. Chỉ kiểm inventory/metadata/điều kiện chọn lọc, không tuyên bố audit đầy đủ mọi policy. Không gọi thử action đặc quyền.
- Không phát hiện custom setuid ở bốn thư mục executable đã kiểm; file capabilities thấy ping/mtr-packet chỉ CAP_NET_RAW. Đây không phải audit toàn filesystem, kernel exploit hoặc mọi nhánh shell của updater.

## 5. Bằng chứng cửa GSM và giới hạn quan trọng

### 5.1. Google IAM hiện hành

- Root gcloud đang dùng service account `cursor-ci-builder@…` tại lúc kiểm, không phải Hermes. `hermes-key.service` chạy root, loader dùng gcloud và tham chiếu root HOME; chưa đối chiếu principal của lần fetch lịch sử bằng token/log. Root account không đọc được project IAM; metadata policy được đọc bằng tài khoản Owner đã đăng nhập sẵn trên Mac, không login mới hoặc cấp thêm quyền.
- Project policy có bốn service account được cấp `roles/secretmanager.secretAccessor`; chưa thấy principal Google dành riêng cho Hermes.
- Service account root-active còn có custom role `MCPSecretManagerOperator` chứa `secretmanager.versions.access`. **Chỉ gỡ role Secret Accessor khỏi account này sẽ không làm nó mất quyền đọc**, do còn grant khác. Đây là bằng chứng phải xét effective permissions, không chữa bằng tên role.
- Một số service account khác có quyền impersonation/token creation; không thấy grant đó cho principal Hermes trong project policy đã xem. Đã đọc một số policy service account/secret liên quan; không tuyên bố đã phủ toàn bộ53secret và mọi cấp tổ chức/folder/đường federation.

Google nêu rõ Secret Accessor ở cấp project áp cho mọi secret trong project; IAM dùng principal đã xác thực và quyền có thể kế thừa từ cấp cha. [Secret Manager access control](https://docs.cloud.google.com/secret-manager/docs/access-control). Credential service account bị người khác sử dụng sẽ mang quyền của account đó; vì vậy quyền giữ credential là một phần của khóa GSM. [Service account credentials](https://docs.cloud.google.com/iam/docs/service-account-creds).

### 5.2. Không đọc giá trị secret để kiểm

Chỉ kiểm owner/group/ACL, khả năng đọc/ghi boolean và metadata tài khoản/role. Không gọi `gcloud secrets versions access`, AccessSecretVersion, token-print/impersonation để thử; không mở giá trị secret, private key hoặc raw process environment.

Profile gcloud Hermes có0credential và0token đã đăng nhập (chỉ count hàng DB, không lấy giá trị); ADC mặc định không thấy. Quyền kiểm độc lập bằng `runuser -u hermes -- test -r/-w`:

| Đường thực tế được kiểm | Owner/mode | Hermes đọc/ghi |
|---|---|---|
| Root gcloud credential DB/token DB/legacy ADC | root,0600; `/root`0700 | false/false |
| `/etc/incomex/agent-data.env` | root,0600; parent0700 | false/false |
| `/opt/incomex/docker/credentials/google-credentials.json`, mount vào Agent Data | root:root0600 | false/false |
| `/opt/incomex/docker/nginx/secrets`, mount vào nginx | root:root0700 | false/false |
| `/usr/local/sbin/hermes-key-fetch` | root:root0700 | false/false |
| `/run/hermes/or.env` và `tg.env` | root:hermes0640 | true/false — khóa runtime của ứng dụng |

Container mount check chỉ lấy metadata đường có tên credential/secret/key/gcloud/env, không mở file. Không coi việc không có ADC mặc định hoặc các đường trên bị chặn là bằng chứng không tồn tại mọi credential ở nơi khác.

### 5.3. Phân biệt khóa của chính ứng dụng với quyền đọc GSM

Loader root đang nạp file `/run/hermes/or.env`, root:hermes và UID Hermes đọc được. Các tên biến được xác minh theo metadata/mã loader chọn lọc gồm khóa OpenRouter, thẻ agent-gateway, webhook và Qdrant local API key; **không đọc giá trị**. Đây là credential runtime đã cấp cho ứng dụng, không phải Google service account private key hoặc token cấp quyền gọi GSM.

Hệ quả:

1. Về cơ chế, có thể chặn Hermes gọi GSM và mượn credential Google/backend bằng IAM + quyền file/process hiện có; chưa xác nhận phủ mọi đường mượn credential trên toàn VPS.
2. Không được tuyên bố khóa runtime đã cấp cho UID Hermes là “Hermes không đọc được”. Với terminal cùng UID, việc đọc file đó đang được quyền Linux cho phép.
3. Nếu Owner chỉ muốn hai cửa root/GSM, giữ cơ chế bootstrap hiện tại và ghi rõ loại khóa runtime được ứng dụng dùng; không dựng bridge để giấu mọi thứ rồi làm hỏng công cụ.
4. Nếu yêu cầu tuyệt đối là cả giá trị khóa runtime của chính Hermes cũng không được tới code/model có terminal cùng UID, hai khóa sudo/IAM **không đủ cho yêu cầu khác này**. Đó là giới hạn mô hình thực thi, không phải lý do tự mở rộng triển khai trong lượt khảo sát.

## 6. Đường gián tiếp và những gì không cần làm lại

| Đường | Principal giữ quyền | Kết quả kiểm và giới hạn |
|---|---|---|
| Hermes → MCP Workspace | Server xác thực `agent_id=hermes`; backend thực hiện quyền của chính backend | Live profile có7tool đọc/ghi Workspace; không generic exec/GSM-read. Không giả danh Hermes để gọi mutation thử. |
| Host helper → sudo helper | `incomex-mcp-helper` → root script được chỉ danh | Bốn menu `docker-ps`, `docker-logs`, `ui-commit`, `ui-move`; source/allowlist root-owned. Không có menu generic shell hoặc secret-read trong mã đã xem; không gọi thực để thử. |
| B/C/E mới dựng → HJW helper | Root oneshot, queue root0700 | Đang dormant, chưa cấp model. `ops_plan` chỉ trả kế hoạch, không chạy lệnh. Không expose/deploy trong điều tra này. |
| Graph wrapper → GSM | Google principal của UID/HOME thực sự chạy wrapper | Wrapper tự gọi GSM. Chạy dưới Hermes không tự có IAM; chạy ở backend giữ credential thì backend chịu trách nhiệm. Không gọi wrapper/doctor vì có thể đọc secret. |

Một service đọc secret để cung cấp chức năng không đồng nghĩa caller được đọc secret. Nhưng generic exec, khả năng đọc credential hoặc sửa code/config của service đó sẽ phá cửa GSM/root. Các quyền owner/group/ACL ngăn đường vòng này vẫn thuộc **hai cửa đã giao**, không phải thêm gateway hay một hệ thống kiểm soát hành vi.

Đã đọc roadmap0.9/0.17 và P347/P353/P359/P362/P363:

- N1 PASS, N2 PASS_WITH_RESIDUAL; không làm lại connector hoặc phần giới hạn hãng.
- N3 CLOSED_WITH_LIMITS; giữ updater/A1, ACL5/postimage Guard và cron/V1 read-only đã đạt. Owner-chat giữ bộ công cụ thường theo cấu hình hiện tại.
- B/C/E dựng phía server nhưng chưa deploy image ngày23/10, giữ dormant; D10 PG chưa được duyệt; N4–N6 chưa mở.
- Điều30/31 và lỗi POST rollback#21 giữ nguyên hồ sơ, không sửa proof/baseline để làm xanh. Không hồi sinh RUN04/RUN05 hoặc triển khai B/C/E để phục vụ phép kiểm hai cửa.

Phạm vi đề xuất mới theo chỉ đạo Owner là **hai cửa**. P363 từng gom thêm yêu cầu workflow/dữ liệu thành bốn cửa; báo cáo này tách chúng ra để không lặp lại cách tiếp cận rộng. Không tự gỡ các rào đang sống khi chỉ được giao điều tra.

## 7. Chính xác sửa gì nếu Owner duyệt triển khai sau báo cáo

1. **Không cấp lại identity Hermes:** dùng user `hermes` và profile MCP đã có. Agent mới dùng cùng mẫu cấu hình/credential riêng khi có nhu cầu, không làm mới registry/gateway.
2. **Sudo:** nếu zero-sudo là tiêu chí, sửa đúng một grant trong `/etc/sudoers.d/90-hermes-update`. Giữ nguyên file chương trình, root-owned updater và các tài khoản/dịch vụ khác. Xóa alias/file dư chỉ sau khi đối chiếu không còn caller; không cần dọn để đạt mục tiêu.
3. **GSM:** chưa có binding Google của Hermes được xác nhận cần thu hồi. Không có căn cứ bắt buộc sửa project IAM hàng loạt chỉ để chặn UID này. Giữ credential Google và credential của backend có đặc quyền ngoài UID Hermes; nếu kiểm tra bổ sung phát hiện một đường đọc/impersonation thật thì thu đúng grant/ACL ở đường đó. Không chỉ gỡ `roles/secretmanager.secretAccessor` mà bỏ qua custom/inherited grants.
4. **Để thực sự giản lược các hạn chế ngoài hai cửa:** profile `agent_profiles.hermes` trong `/opt/incomex/config/workspace-tools.json` đang có `allowed_tools`, `allowed_roots`, `read_scope`, `write_scope`, `post_guard`; Hermes `config.yaml` còn chia toolset cron/Telegram/CLI. Giới hạn7tool/5file/cron read-only là chính sách nghiệp vụ riêng, **không phải hệ quả bắt buộc của cấm sudo/GSM**. Khi Owner quyết áp dụng phương án mới, dùng chính cấu hình này để mở phạm vi công cụ thường cần dùng, không xây gateway khác và không bắt chờ tách dispatcher/N4–N6. Không đề xuất cấp master credential hoặc quyền sửa code/config của principal root/GSM vì sẽ mở lại hai cửa. Lượt hiện tại chỉ báo vị trí cần đổi, không tự gỡ ACL5, cron policy hoặc Điều30/31; chưa đo hồi quy của một cấu hình mở mới để ghim giá trị triển khai.

**Chức năng có nguy cơ ảnh hưởng:** sáu thao tác Hermes tự `systemctl start/restart/reset-failed` sẽ mất quyền nếu thu grant. In-place `/update` đã bị chặn từ trước; đường nâng cấp được hỗ trợ là `hermes-safe-update apply` do root/Owner kiểm soát. Chat, MCP, terminal thường, cron thường và updater do root điều hành dự kiến giữ được; đây là dự kiến theo cấu hình, chưa là regression PASS sau sửa. Graph/log/PG mới chưa được cấp từ trước; khóa hai cửa hoặc thu grant sudo không tự làm các năng lực chưa triển khai này xuất hiện. Tước quyền đọc `or.env/tg.env` hay thu project IAM của loader một cách mù có thể làm hỏng bootstrap/provider/Telegram và các dịch vụ khác, không phải phương án tối thiểu đề xuất.

**Nghiệm thu ngắn khi có lượt triển khai riêng:** kiểm sudo policy không còn grant Hermes; UID/NNP/capabilities không đổi; các credential path đặc quyền vẫn không đọc/ghi được; không có IAM accessor/impersonation cho principal agent; chat/MCP/terminal và updater đúng đường vẫn chạy. Dùng kiểm metadata/quyền hoặc secret giả để thử âm; không đọc secret production để chứng minh bị chặn. Điều30/31 theo footprint thật của delta đó.

## 8. Ranh giới khi Hermes bị chiếm quyền và khi VPS đã mất root

- **Chiếm UID Hermes:** các ranh giới Linux/IAM nêu trên có ích nếu không có credential/privileged API bị lộ. Kẻ tấn công vẫn có quyền dữ liệu và khóa runtime hợp lệ của chính Hermes; không hứa không có thiệt hại ngoài hai cửa.
- **Chiếm root toàn VPS:** root có thể đổi sudoers/systemd, giả UID, đọc hoặc sử dụng credential của loader/backend. Root-active service account hiện còn quyền đọc GSM ở cấp project và custom role. Hai khóa cùng cấu hình máy này **không bảo vệ GSM trước root đã bị chiếm**. IAM vẫn giới hạn quyền của principal, nhưng root có thể mượn principal đang cần được phép đọc.

Không tự mở thiết kế chống full-root compromise: yêu cầu đó cần ranh giới tin cậy nằm ngoài quyền kiểm soát root hiện tại và ảnh hưởng vận hành; Owner chỉ yêu cầu báo đúng giới hạn.

## 9. Bằng chứng, cách đo và phần chưa đo

Các nhánh Codex cùng một ghế, không thay review khác hãng. Các phép đo dùng SSH chỉ đọc, `id`, metadata process/status, `systemctl show` trường chọn lọc, `sudo -l -U hermes`, owner/group/ACL và `test -r/-w`; đọc policy IAM/role metadata bằng tài khoản có sẵn; parse profile chỉ lấy các field không bí mật. Không tạo service/user/key, không thay IAM, không restart, không thực thi helper privileged action, không gọi GSM payload API.

Nguồn kỹ thuật chính:

- `/etc/sudoers.d/90-hermes-update`; unit/drop-in gateway/serve/key/safe-update; metadata `/proc/<PID>/status`.
- `/opt/incomex/config/workspace-tools.json` và `agent_data/workspace_tools.py` phần credential→profile, `agent_check`.
- `/usr/local/sbin/incomex-mcp-helper-priv`, `/etc/incomex-mcp-helper/priv.conf`, permission các queue/file liên quan.
- Project IAM, selected service-account/secret policies và custom role metadata; không lưu bản dump unredacted vào repo công khai.
- Repo `work/hermes-joint-workspace/COLLAB.md`, roadmap0.9/0.17, P347/P353/P359/P362/P363 và PROMPT đang đánh dấu historical/closed.

Cloud Logging API hiện chưa được bật trong project; không có bằng chứng log GSM truy cập lịch sử trong lượt này. Không bật API để khảo sát, không suy từ thiếu log rằng chưa từng có truy cập sai. IAMCredentials API đang enabled, nhưng không gọi tạo token.

**Giới hạn:** không kiểm toàn bộ53secret IAM/organization/folder/federation; không đọc raw environment, Google credential values hoặc full script có nguy cơ chứa credential; không kiểm exploit kernel, mọi executable/filesystem hoặc mọi nhánh root updater; không thử chiếm dịch vụ hoặc làm E2E có secret. Các lần đọc quá rộng bị bộ duyệt tự động từ chối đã không chạy; tiếp tục bằng metadata/permission boolean an toàn. Không biến giới hạn này thành chứng nhận không có bất kỳ đường vòng nào.

JEV là ý kiến phụ cho lựa chọn kiến trúc, không đo VPS: receipt `gen-dec-1792732237-koNLQamxC7iqMItcEeZS`. Kết quả ủng hộ dùng native controls, không biến identity workflow thành cửa thứ ba, không hứa bảo vệ khóa đã cấp hoặc full-root compromise. Số đo trong báo cáo dựa trên kiểm tra trực tiếp; JEV không thay Owner/GPT Host quyết triển khai.

**Trạng thái:** điều tra và báo cáo; đề xuất chưa triển khai. Không sửa roadmap, PROMPT, view, Guard, secret hoặc quyền vận hành đã chốt.
