# RUN25 — G8 tiền triển khai: kiểm toán nguồn, Linux, gói release GitHub→VPS1

**Kết quả: SOURCE_RELEASE_REVIEWED (tác giả tự kiểm) · PARTIAL_PREPROD · IMAGE_BUILD_NOT_TESTED · ROLLBACK_IMAGE_NOT_TESTED · LINUX_CONTINUATION_NOT_TESTED · NO_GO_RELEASE.** Không phải G8_SYSTEM, KST_ACCEPT, C1/C2 hay enforce. 0 merge, 0 deploy, 0 lệnh của em tới VPS1/VPS2/PG/KB/Directus. Trạng thái production dưới đây lấy từ biên nhận VPSC2 P30 (29/10) và nhánh backup `vps-daily-20261031`, không đo lại.

RUN `HJW-G8-PREPROD-QUALIFICATION-20261031-25` · READY@d8e3e2a9ef874298bfe6628e3149e44a2e8454a8 · PROMPT SHA256 23d0d2a93cf60d4d3f10a59cdf0f23a9582fb01e0318dcaa7da75bb2722c57fc. Em vừa viết RUN24 nên đây không phải review độc lập.

## Manifest
| Mốc | SHA |
|---|---|
| main (base) | 6160f9ad6e5d16012dfe20bb59949abf5ffadad2 |
| PR357 (OPEN/DRAFT, không đổi) | 36c682914c9f412078113b6d85319f11356d1130 |
| PR358 trước RUN | 5ef7d97e7a08ba7d904d5a0b63e5f64243c65b16 |
| **PR358 HEAD sau RUN (OPEN/DRAFT, push không force)** | **235dc88087257f5163f44201beb9e69c5f738025** |
| Bản đang chạy (P30): release D1 | cc3df9778f784e124f9d206569fac52cb890f8dc |
| Nguồn VPS (P30, khớp `vps-daily-20261031`): D2 | 1cc706dc0f1ba7ef05f4631c04f604d2cacd9982 |
| Image đang chạy (P30) | agent-data-hvu:w4q-20261029-06 · sha256:4635e417e5400a9f85d1ed569f1c2f977845405bf7b8d834ab7002006f7d1045 |

[CI 41179743952](https://github.com/Huyen1974/agent-data-test/actions/runs/41179743952), job 124474521165: SUCCESS đúng head/base, merge-test 9f01a67a, mọi bước success, **Unit 357 passed** ([ci-run.json](ci-run.json)). Workflow không đổi. CI chạy trên runner tự host đặt trong container trên VPS1, đúng đường PROMPT quy định.

## A — Phát hiện mới
1. **Đã sửa: `mcp_server/stdio_server.py` + `server.py` không khởi động khi chạy dạng tệp.** RUN23 thêm `from agent_data import kb_declaration`; Claude Desktop chạy `python .../mcp_server/stdio_server.py`, lúc đó sys.path[0] là `mcp_server/`. Đo: PR358 cũ `ModuleNotFoundError`, main chạy được. Máy Owner hiện không dính vì venv cài editable, nhưng venv khác sẽ hỏng. Sửa: nối gốc repo vào sys.path. Test mới trong gate, đỏ trước khi sửa (2 failed).
2. **31 ca đỏ không hẳn do Mac: 2 ca là của chính PR358.** `test_hvu_signals::*contract_unchanged` xanh trên main, đỏ trên PR358 vì schema đổi. RUN24 chỉ so với PR358 cũ nên không thấy. Đo: 37/37 tool schema trùng main sau khi bỏ 2 field khai danh và đoạn mô tả nối thêm. Sửa: giữ baseline 24/09 làm phép so trên danh sách đã bỏ phần khai danh, ghi hash mới có chủ đích; thêm field lạ vào schema thì đỏ lại (đã thử).
3. **Schema đổi khi deploy:** `connectorSchemaHash` `dbbfc590a969`→`9dd3c23717f1`, `/mcp-gpt` `1c1c7ea1315d`→`31606fc87cba`. Guard INV2 in hash này; ghim hay chỉ in thì chưa đọc được từ đây ⇒ phải đo ở PRE. `CONNECTOR_SCHEMA_VERSION` giữ nguyên, Host/KST quyết có cần đổi.
4. **Delta thật lớn hơn diff PR358.** So với bản đang chạy D1, ứng viên còn lần đầu đưa lên: `pg_store.py` bỏ DDL lúc khởi động và mã HJW S3 (`hjw_infra.py`, phần trong `server.py`, `workspace_tools.py`). S3 chỉ mở khi hồ sơ agent ghi tên `infra_*`; P363 từng ghi KEEP_DORMANT. Chi tiết 17 tệp: [release-manifest.json](release-manifest.json).
5. **Rollback đúng đích là D1, không phải main.** Production đã có PR357 nên lùi về D1 không chạy lại việc đã xong; lùi về main thì có (đo ở mục C).
6. **`deploy-vps.yml` có `push: main` với `agent_data/**`, hiện `disabled_manually`** (đọc API 31/10), lần chạy cuối 03/04. Nếu ai bật lại thì merge sẽ rsync `--delete` và build image khác dòng. `release.yml`, `terraform-apply.yml` cũng tắt. `vector-audit.yml` cũng `disabled_manually`, lần chạy cuối 11/03, và COLLAB GHM ghi chìa SSH đã thu hồi 16/10 ⇒ consumer này đang ngủ, không chặn advertise.
7. **Thông tin Docker của P490 đã cũ** (mục B).

Rà đối kháng không ra lỗi thêm: 26 handler đều phân loại, 0 ngoại lệ; `workspace_tools.call` được gọi qua thuộc tính module nên wrapper không bị lách; hồ sơ thật có đủ `credential_env`+`label` như `profile_facts` cần; cây `Dockerfile.mcp` import được trong venv sạch chỉ cài `mcp_server/requirements.txt`. Chi phí đã biết: stdio trong venv có langroid khởi động thêm ~2 s (đo 2,0 s so với 0,27 s) vì `agent_data/__init__.py` thử nạp langroid; `_kb_input` phân tích JSON thân lần nữa; thân REST có khoá bắt đầu `_` bị 403 cả ở advertise (chủ ý từ RUN23, chưa thấy consumer nào gửi).

### Bảng writer logic
Nhãn theo PROMPT; bảng chỉ nói về nguồn và phép thử, chưa chạy production.
| Writer | Nhãn | Bằng chứng / thiếu |
|---|---|---|
| `workspace_*` ghi (10 tool) qua mọi route MCP | COVERED | `workspace_declaration.WRITES`, 0 chưa phân loại, gate 357 |
| `workspace_task_start` → supervisor | COVERED | test tiến trình thật, `test_hjw_g8_package` |
| `workspace_exec` + worker host | COVERED ở nguồn | `_declaration` chép vào kết quả; service host chưa thử trên VPS |
| Upload begin/append/commit, import_file | COVERED | gate; carry qua meta |
| KB MCP 5 tool, REST 5 route | COVERED | RUN23, gate |
| KB admin 4 route | COVERED | `test_hjw_g8_package`: 28 ca HTTP từ cây COPY |
| Client stdio/hybrid chuyển tiếp | COVERED | gate; sau sửa mục A1 |
| `pg_vector_listener` | DERIVED_INTERNAL | theo NOTIFY, không có người gọi |
| `directus_sync` ghi `knowledge_documents` | DERIVED_INTERNAL | theo sự kiện của lượt ghi đã guard |
| `/documents/{id}/move` | OUTSIDE_SCOPE | raise 501 |
| `/documents/batch`, đọc KB | OUTSIDE_SCOPE | chỉ đọc |
| `/chat`, webhook, presence, `main.py` metadata | OUTSIDE_SCOPE | không ghi KB chính |
| Gateway `fs_*`/Gemini | OUTSIDE_SCOPE của PR358, **bắt buộc trước G8_SYSTEM** | candidate RUN16 chỉ ở ref local `7e3c0496` |
| SQL thẳng vào `kb_documents` | **UNKNOWN** | chưa kiểm kê role/đường ghi |
| Directus Flow `POST/DELETE /documents` | **UNKNOWN** | mã ở web-test `dot-flow-setup-sync`, không gửi header; chưa đọc Flow sống |
| Cron `reconcile-tasks.py` upsert | **UNKNOWN** | nhãn trong tệp ghi cron 6 giờ, đo 30/07; không gửi header |
| `dot-knowledge-ingest(-batch)`, `upload_content.py`, `test-*-connections.sh`, `test_mcp_e2e.sh` | **UNKNOWN** | không gửi header khi ghi; chưa biết còn ai chạy |
| `vector-audit.yml` auto_heal | **UNKNOWN**, đang tắt | patch đề xuất dưới |

Các dòng REST UNKNOWN **không ảnh hưởng advertise**, nhưng sẽ nhận 403 nếu bật enforce. Phải đo sống và sửa hết trước enforce. **Vì vậy chưa thể nói FULL.**

### Vector-audit: chỉ đề xuất
[vector-audit-compat.patch](vector-audit-compat.patch) thêm `X-Write-Declaration`, không áp vào PR358. Đo: `git apply --check` OK; `gate_policy.workflow_errors` trước và sau cùng `RUNNER_OUTSIDE_PILOT`, `SECRET_JOB_MAIN_GUARD_REQUIRED`, nên sửa trong PR358 sẽ làm gate đỏ như Host nhận định; header được `resolve` nhận ở enforce (cờ `UNREGISTERED_ALIAS`, không chặn). Chạy lại workflow này cần runner khác và secret đã thu hồi ⇒ khi cần auto_heal, dùng cùng header trong một DOT trên VPS là đường gọn hơn.

## B — Linux và Docker
**IMAGE_BUILD_NOT_TESTED, ROLLBACK_IMAGE_NOT_TESTED, LINUX_CONTINUATION_NOT_TESTED.**

**Docker Desktop (chỉ đọc, không mở):** 4.57.0, macOS 27.2, daemon không chạy, không có socket. `Docker.raw` 44 GB, mtime 17/02/2026, đọc lại cuối RUN không đổi. Log: 01:05Z lỗi `md5: command not found`; **01:08–01:09Z lần thứ hai cùng lượt RUN24 chạy bước đặc quyền thành công (`installRootPasswordOK`, exit 0)**, `com.docker.vmnetd` chạy bằng root từ 01:09:09Z và `/var/run/docker.sock` trỏ về socket người dùng. P489 không ghi việc này; em ghi đính chính ở đây. Lỗi md5: `/usr/bin/md5` không tồn tại, chỉ có `/sbin/md5`; `do shell script` chạy từ shell của em không thấy md5 vì PATH thiếu `/sbin`. Vì sao lần thứ hai qua được và ai nhập mật khẩu: chưa rõ. Lần mở kế tiếp có thể không vướng vmnetd nữa: **chưa thử**.

**Em quyết không mở** (JEV `gen-dec-1793429269-jsB7DbVE8OkKlSlDyGLk`, không mở 0,97): khởi động sẽ ghi vào VM 44 GB; và dù lên được cũng không test được bản thật vì base `agent-data-hvu:w4q-20261029-06` chỉ có trên VPS1, x86-64, còn Mac là arm64. Không có Lima/Colima/Podman/QEMU/OrbStack.

**Đường Linux:** runner gate là container trên VPS1, không có Docker socket, đã chạy Unit 357 trên Linux. Chạy `tests/continuation` ở đó cần sửa workflow và tốn RAM VPS1 (từng OOM ở 1–1,5 GiB) ⇒ không làm. Không có máy Linux thử nào khác.

**`tests/continuation` (Python 3.11, requirements pin):**
| Môi trường | Kết quả |
|---|---|
| main 6160f9ad, APFS mặc định | 30 failed, 256 passed |
| PR358 5ef7d97e, APFS mặc định | 32 failed, 261 passed |
| PR358 5ef7d97e, APFS phân biệt hoa/thường + venv đầu PATH | 9 failed, 284 passed |
| **PR358 235dc880, cùng môi trường trên** | **7 failed, 290 passed, 5 skipped** |

Phân loại 32 ca: 2 do PR358 (đã sửa) · 21 do APFS không phân biệt hoa/thường (mất đỏ trên ổ ảnh phân biệt hoa/thường) · 1 `test_g6` vì `python3` ngoài venv thiếu jsonschema · 1 `test_g1` do thư mục tạm của em thuộc nhóm `wheel`, không có trong 31 của RUN24 · **7 còn đỏ, đều đỏ cả trên main:**
- 5 ca NFC/NFD: `test_d09_an_nfc_twin_is_refused_and_names_the_file_already_there`, `test_d09_existing_bytes_are_never_renamed`, `test_d09_a_transaction_destination_is_guarded_too` (lifecycle_r03) · `test_d1_move_renames_nfd_to_nfc_on_purpose`, `test_d3_write_new_into_an_nfd_twin_folder_is_refused` (name_twin_r03). Giả thuyết: APFS đồng nhất Unicode dạng chuẩn; chưa chứng minh được nếu không có ext4.
- 2 ca `test_p02_snapshot_k8::test_acc15_outage_then_self_heal[False|True]`: trả `OPERATION_FAILED` thay vì `RECOVERY_REQUIRED`. **Chưa rõ nguyên nhân**; ghi chú CONN-REPAIR 03C từng gọi là chập chờn.

Chạy trên Linux cần: `git checkout 235dc880`, Python 3.11, `pip install -r requirements.txt`, rồi `PATH=<venv>/bin:$PATH PYTHONPATH=. python -m pytest -o addopts='' -q tests/continuation`, đặt basetemp trên ext4. Đạt khi 7 tên trên hết đỏ và không có tên mới; bộ này cần máy thử có ≥ 2 GiB RAM riêng (ước tính), không dùng production.

**Test mới thay 2 script lab:** `tests/continuation/test_hjw_g8_package.py`, 4 passed: cây chỉ gồm tệp COPY của `Dockerfile.continuation` phục vụ đủ route admin qua HTTP · task khai danh qua supervisor thật ở enforce · cây `Dockerfile.mcp` import và quảng bá 4 facts · stdio chạy dạng tệp. Khoá API sinh ngẫu nhiên mỗi lần chạy. Không build image nên không chứng minh base image. Gate 357 passed 3/3 lần trên Mac.

## C — Gói release và rollback
### Đóng gói theo runtime
| Runtime | Cách đóng gói đúng | Trạng thái |
|---|---|---|
| Container `incomex-agent-data` | Overlay `FROM agent-data-hvu:w4q-20261029-06`, COPY đúng 12 tệp `agent_data/` + 2 tệp `mcp_server/` trong manifest (29→33 tệp .py) | DESIGN_READY |
| `Dockerfile.continuation` | Chỉ dùng làm danh sách COPY đã kiểm. **Không build nguyên trạng:** FROM `20260917-git` không phải dòng đang chạy; quan hệ với image hiện tại chưa đo | DESIGN_READY |
| `Dockerfile.mcp` | Ứng viên độc lập, import đã thử; **chưa rà có dịch vụ nào đang dùng** | UNKNOWN |
| `Dockerfile` gốc + `deploy-vps.yml` | Không dùng: dòng image khác, đang tắt | Loại |
| `incomex-workspace-exec.service` | Script chèn `/opt/incomex/docker/agent-data-repo` vào sys.path, nhập `workspace_runtime` từ cây nguồn host; phải restart khi hàng exec = 0 | DESIGN_READY |
| `queue.sqlite` | Cột đã có từ PR357 (P28/P30), ứng viên **không đổi schema**, chỉ thêm thử lại lúc chuyển WAL; không cần di trú hay lùi schema | Đo ở mức nguồn |

### ONE-GO GH→VPS1 (kế hoạch, chưa thực thi)
Đường: compose qua apply-v0 như P30, không dùng `ghm-manual-deploy.py` cho lượt này vì nhánh Agent Data của nó chưa chạy thật (JEV `gen-dec-1793431245-w9xXIavEM6ucdamSqoHs`, 0,97). Thời lượng là ước tính.
1. **Trước GO:** KST độc lập review đúng HEAD, ghi `KST_ACCEPT@SHA`; Host trình Owner GO đúng đích ghi trên repo (DROOT56).
2. **Merge:** KST merge PR358 (commit M), không merge PR357 rồi đóng PR357. Ngay trước merge đọc lại `deploy-vps`, `release`, `terraform-apply` còn `disabled_manually`; còn bật ⇒ DỪNG. Gate main xanh đúng M.
3. **Chép nguồn:** `git archive M` từ Mac sang `/opt/incomex/work/hermes-joint-workspace/<RUN>/`, so SHA256 tar hai đầu. Không fetch vào `agent-data-repo`.
4. **PRE chỉ đọc:** image, compose hash, release, nguồn D2 sạch, queue và exec = 0, RAM ≥ 3 GiB, Guard PRE; Guard INV2 ghim hash hay không; `allowed_tools` của Hermes có `infra_*` không; compose không đặt `WORKSPACE_DECLARATION_MODE=enforce`; target Guard cho từng tệp nguồn; đường script của service exec. Bản đo mới nào lệch manifest ⇒ DỪNG.
5. **Build overlay:** tag `agent-data-hvu:g8-<sha12>`, kiểm tag base = 4635e417 (BuildKit không nhận FROM theo ID), tiền tố RootFS trùng, config trùng, blob image = M, 0 tệp `._*`.
6. **Canary, chưa đổi production:** container riêng, 1 worker, cổng loopback khác, trần RAM 1 GiB, `state_dir` riêng (**không dùng chung `queue.sqlite` production**). Kiểm health, 37 tool, hash mới, khoá sai 401, khởi động không DDL. Test chạy trên Mac với mã rút từ image, không chạy trong VPS. Lỗi ⇒ DỪNG, production chưa đổi.
7. **Chuyển đổi, giữ VPS-GHI vài phút:** Guard PRE; apply-v0 `vpsup-docker-compose` chỉ đổi `image:`, recreate riêng agent-data (P30: ngắt 28,1 s); healthy thì đưa ngay commit release R vào nguồn VPS và apply-v0 `connector-sync-registry` + commit DOT để thu hẹp khe INV20 (P30: 32 s).
8. **Nguồn VPS:** D2 **không phải tổ tiên main** (merge-base bfe86c8) nên ghi chú «chỉ-ff» ở T1-AD đã cũ. Dùng commit tiến có cây = M, tệp thuộc Guard qua apply-v0 từng target; thêm dòng `code-ledger.tsv` cho 4 tệp mới để giữ INV23.
9. **Sau chuyển:** worker M1=M2=4 bằng `wcount.sh` (UNKNOWN ≠ 0), Guard, một lượt ghi có khai báo trả receipt; restart service exec khi hàng = 0 rồi thử một job.
10. **Diễn tập lùi thật:** lùi về 4635e417 rồi tiến lại, thêm 2 lần ngắt ~28 s (ước tính). Không có bước này thì rollback image vẫn NOT_TESTED. Host/Owner chốt trong GO.
11. **Guard POST + Điều 30/31:** footprint PRE→POST, Telegram receipt theo R4, INV2/INV20/INV23, không đổi DNS/PG/Directus. Trả VPS-GHI.
12. **Sau đó, lượt riêng:** giữ advertise; client Refresh; C2 + C1 AI thật; đo và sửa consumer UNKNOWN; Gateway `fs_*`; mapping; rồi mới enforce.

### Rollback
**Đích: 4635e417 + release D1 + compose/connectors `.pre`, chỉ khi hàng chờ đã đối soát.** Đo bằng [rollback_matrix.py](rollback_matrix.py) trên một `queue.sqlite`, tiến trình riêng, mã thật; **mức nguồn, không phải image:**
| Tình huống | Lùi về D1 ([kết quả](rollback-to-d1.json)) | Lùi về main ([kết quả](rollback-to-main.json)) |
|---|---|---|
| Retry việc đã xong, không khai báo | Replay đúng task, 0 chạy lại | **Xếp hàng chạy lại** (ca này chỉ thất bại vì tệp đã tồn tại) |
| Retry việc đã xong, từng khai báo, không còn field | `OPERATION_ID_REUSED`, 0 chạy lại | **Xếp hàng chạy lại** |
| Việc khai báo còn chờ trong hàng | Chạy xong, mất receipt | Chạy xong, mất receipt |
| Upload khai báo dở | Append + commit OK | Append + commit OK |
| `workspace_edit` có op id | Replay | Replay |
| Tiến lại ứng viên, retry đúng facts | Replay, có receipt | Replay, có receipt |

**Giới hạn, không gọi là rollback an toàn tuyệt đối:** client đã khai báo phải đổi op id sau khi lùi; job chờ mất receipt khai danh; kết quả đã có `declaration_receipt` vẫn nằm trong DB, mã cũ bỏ qua; worker host chưa được thử chéo phiên bản. **Lùi tiếp về 46e0ba15 hoặc main bị cấm nếu không có Owner**, vì chạy lại việc đã xong.
**Kích hoạt lùi:** health không lên trong 120 s; số tool ≠ 37; khoá sai không 401; 5xx mới; worker đếm được ≠ 4; Guard POST đỏ mới do lượt này. Đếm lỗi hoặc UNKNOWN không được tự kích hoạt lùi (bài học P28).

### Mapping danh tính
Không cần Owner nhập từng field. Khi có GO, ghi `master_profiles.<id>.declaration_facts` qua apply-v0 config workspace. Chỉ map điều một khoá chứng minh được; `task_id`/`command_ref` luôn theo lượt.
| Hồ sơ (theo test B1; đo lại lúc PRE) | `declared_actor` | `origin_environment` | Ghi chú |
|---|---|---|---|
| `claude-code` | map `claude-code` | **chưa map** đến khi chứng minh khoá chỉ ở Mac | |
| `codex` | **chưa map** | **chưa map** | khoá dùng cho nhiều bề mặt Codex: chưa đo |
| `gpt-web` | **chưa map** | **chưa map** | GPT Chat/Work/Dot chung khoá (AGENTS A2) |
| agent `hermes` | ngoài `master_profiles`, tự khai | tự khai | mã hiện chỉ map master; nhu cầu riêng nếu cần |

### GO / NO-GO hiện tại: **NO_GO_RELEASE**
JEV `gen-dec-1793429269-jsB7DbVE8OkKlSlDyGLk`: NO_GO kèm điều kiện 0,98. Host nghiệm thu độc lập.
| # | Điều kiện | Hiện tại | Chặn |
|---|---|---|---|
| 1 | KST độc lập đúng HEAD | chưa | merge |
| 2 | Owner GO ghi repo đúng đích GH→VPS1 | chưa | mọi bước tới VPS |
| 3 | Build + canary overlay | NOT_TESTED; base chỉ trên VPS1 | chuyển production |
| 4 | Diễn tập rollback image | NOT_TESTED | gọi rollback đã kiểm |
| 5 | 7 ca continuation trên Linux | NOT_TESTED | Host quyết chặn hay chấp nhận rủi ro; đều đỏ cả trên main, không do PR358 |
| 6 | INV2, `allowed_tools`, target Guard | chưa đọc | bước 7 |
| 7 | RAM ≥ 3 GiB, Guard PRE sạch | chưa đo hôm nay | bước 6–7 |
| 8 | Consumer UNKNOWN, `fs_*`, mapping, vector-audit | chưa | enforce, không chặn advertise |

**Điểm vướng vòng:** điều kiện 3 chỉ thực hiện được trên VPS1, mà chép mã lên VPS1 đã là GH→VPS cần Owner GO, và PROMPT cho Host chỉ trình GO khi image đã test. Đề xuất Host: một Owner GO chia hai chặng, chặng 1 gồm bước 3–6 không đổi production, dừng lại nghiệm thu; chặng 2 gồm bước 7–11. Nếu không muốn, cần một máy Linux x86-64 thử riêng có bản `docker save` của base, mà lấy bản đó cũng là một lần đọc VPS1.

## Dọn dẹp
Worktree, venv, ổ ảnh tạm và tiến trình test đã gỡ trước khi ghi KQ. Không sudo, không đổi cấu hình Docker hay hệ thống, không mở Docker Desktop. Mọi thứ em tạo trên Mac nằm trong thư mục scratch: worktree, 2 venv, một ổ ảnh APFS tạm để so sánh.
