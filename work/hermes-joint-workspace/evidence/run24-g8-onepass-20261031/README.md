# RUN24 — G8 ONEPASS: khép KB admin, ghép queue4, sửa race SQLite, đóng gói

**Kết quả: SOURCE_INTEGRATED_CI_PASS · IMAGE_BUILD_NOT_TESTED.** Chỉ là mức nguồn + CI + phép thử trên Mac. Không phải G8_SYSTEM, C1/C2, KST_ACCEPT hay production enforcement. 0 ghi VPS, 0 ghi main, PR357 không đổi.

RUN `HJW-G8-ONEPASS-CLAUDE-20261031-24` · READY@7fff307201121e1f14c09c4a5cb7ad8da872205e · PROMPT SHA256 c5b66452af7dc73c27630fca93eef7c13a5281f7a3838dccf8afbbb166c98cc3 · executor Claude Code CLI/MacBook, cũng là người viết mã nên không tự nghiệm thu.

## Manifest
| Mốc | SHA |
|---|---|
| main (base) | 6160f9ad6e5d16012dfe20bb59949abf5ffadad2 |
| PR357 (giữ nguyên, OPEN/DRAFT) | 36c682914c9f412078113b6d85319f11356d1130 |
| PR358 trước RUN | 2d966640a0ccdf22fec50ee45a725fdfb41bfe48 |
| S1 admin KB | 0a72ed820a4a971fc4bfe7c2239d1f5cd4b068f7 |
| Merge PR357 | fe9480165dbcd0ccb6924abc68c8609e2f4dc136 (cha 0a72ed82 + 36c68291) |
| S2 race SQLite + test | cc7d274169359380decff42f9bc1bb38b917df03 |
| **Combined HEAD (S3 đóng gói)** | **5ef7d97e7a08ba7d904d5a0b63e5f64243c65b16** |

Push không force lên nhánh có sẵn `dev/codex-ad/hjw-g8-four-facts-20261030`. PR358 vẫn DRAFT; thân PR ghi rõ đã chứa nguồn PR357. **Về sau không merge cả hai:** merge PR358 đã mang theo commit của PR357, nên PR357 phải đóng hoặc đổi đích lúc release.

## S1 — KB admin
| Route · chế độ | Loại | Thiếu/sai khai báo | Khai đúng | advertise, không khai |
|---|---|---|---|---|
| `/kb/reindex` | ghi | 403 trước mọi chạm store | 200 + receipt | kết quả cũ |
| `/kb/reindex-missing` | ghi | 403 trước mọi chạm store | 200 + receipt | kết quả cũ |
| `/kb/cleanup-orphans` dry_run=false | ghi | 403 trước mọi chạm store | 200 + receipt | kết quả cũ |
| `/kb/audit-sync` auto_heal=true | ghi | 403 trước mọi chạm store | 200 + receipt | kết quả cũ |
| `/kb/cleanup-orphans` mặc định, dry_run=true | đọc | không đòi, header hỏng bị bỏ qua | như cũ, không receipt | như cũ |
| `/kb/audit-sync` mặc định, auto_heal=false | đọc | không đòi, header hỏng bị bỏ qua | như cũ, không receipt | như cũ |

- Guard nằm ở chính handler (`kb_declaration.writer`), gọi trực tiếp handler cũng không lách được; dùng lại `declaration_contract`, không thêm gateway/DB/token. Sai khoá API vẫn 403 như hiện hành.
- Khoá dùng chung chỉ chứng minh `credential:shared-rest`; tên AI/nguồn ghi `self_declared`. Tự điền `verified` chỉ từ profile mapping đã xác thực (fixture); mapping sống chưa có và REST hiện không có profile nào. Khai trái mapping ⇒ 403.
- Lỗi một phần: `write_outcome` = partial kèm store lỗi; handler sập giữa chừng ⇒ 500 `KB_WRITE_FAILED`, giữ receipt, không lộ chi tiết lỗi.
- Bổ sung ngoài danh sách PROMPT, cùng phạm vi: `writer` nay bắt mọi exception sau khi đã nhận khai báo (trước chỉ bắt HTTP error); chỉ đổi hành vi khi có receipt.

**Rà sơ đồ ghi KB:** test `test_kb_every_write_route_is_guarded_inventory` dựng đồ thị gọi hàm trên `server.py`: mọi route chạm `set_doc/update_doc/upsert_document/delete_document` đều có guard, trừ `move_document` (câu lệnh đầu là raise 501, test kiểm đúng điều đó). Đường MCP đi qua handler đã guard.

**Residual có tên (không claim FULL):**
- `pg_vector_listener.py`: tự xoá/upsert Qdrant theo PG NOTIFY. Là đồng bộ dẫn xuất, không có người gọi nên không có 4 facts; ghi PG thẳng bằng SQL ngoài API thì không ai khai.
- `main.py` tool metadata của agent: ghi `metadata_store` (không phải `kb_documents`) qua tool của langroid.
- `/chat`, webhook, presence: ngoài phạm vi KB chính, như RUN23.
- Consumer phải sửa TRƯỚC enforce: `.github/workflows/vector-audit.yml` (input `auto_heal`) gọi audit-sync không có header. `scripts/check_orphan_vectors.py` và `scripts/test_mcp_e2e.sh` dùng chế độ đọc, không ảnh hưởng.

## S2 — ghép queue4 và race SQLite
Xung đột đúng 2 tệp `workspace_tasks.py`, `workspace_execution.py`. Giữ `enqueue_once`/`BEGIN IMMEDIATE` của PR357, giữ `_declaration` và `bind_hash` của PR358. [merge-proof.txt](merge-proof.txt) có diff hai chiều: test PR357 cùng blob; `workspace_runtime.py` chỉ thêm `_enable_wal`; `tasks/execution` so với PR357 chỉ thêm phần khai danh. Các tệp còn lại của PR358 cùng blob, trừ `kb_declaration.py`, `server.py`, test (do S1).

**Nguyên nhân race:** chuyển DB mới sang WAL cần khoá độc quyền và SQLite không gọi busy handler cho khoá đó, nên `connect(timeout=5)` vô tác dụng. **Sửa:** `_enable_wal` thử lại có trần 5 giây, chỉ với lỗi `locked`; không thêm queue/service/DB. Production đã WAL nên lệnh pragma không phải chờ.

Số đo: [race-before-2p.json](race-before-2p.json), [race-before-8p.json](race-before-8p.json), [race-after-2p.json](race-after-2p.json), [race-after-8p.json](race-after-8p.json); chạy lại bằng [fresh_db_stress.py](fresh_db_stress.py).

| Đo | Trước sửa | Sau sửa |
|---|---|---|
| DB mới, 2 tiến trình | 13/40 vòng hỏng | 0/100 |
| DB mới, 8 tiến trình | 12/40 vòng hỏng, 38 lỗi | 0/60 |
| `test_vpsc2_w4q05_queue.py` | đỏ ngay vòng 0 | 7 passed, 5/5 lần chạy |

Test mới trong tệp gate, bằng tiến trình thật: 10 job xếp hàng ⇒ peak đúng 4, 0 mất, mỗi tệp ghi đúng 1 lần · replay sau finish khi request đã NULL · khác declared_actor/command_ref ⇒ `OPERATION_ID_REUSED` · 2 tiến trình DB mới cùng operation_id ⇒ 1 job, 1 bên replayed · SIGKILL supervisor, poll hồi sinh pid mới, giữ receipt · alias `done-tasks` qua hàng đợi · `workspace_exec` đi nhánh nguyên tử. ACL Hermes: test `test_declaration_does_not_grant_hermes_tools_or_paths` có sẵn vẫn PASS.

## S3 — đóng gói và CI
- **Sửa một lỗi ngoài phần Host đã thấy:** `Dockerfile.continuation` thiếu module khai danh như Host ghi; thêm vào đó `Dockerfile.mcp` chỉ COPY `mcp_server/` trong khi `mcp_server/server.py` từ RUN23 đã `import agent_data.kb_declaration`, nên image MCP dựng từ tệp đó sẽ thiếu module khi import. Cả hai đã sửa. `Dockerfile` gốc copy cả thư mục nên đủ. Chưa rà tệp nào đang được dùng thật cho image MCP.
- Test `test_image_manifest_ships_every_local_module_it_imports` trong gate giữ COPY khớp đồ thị import (RED trên Dockerfile cũ: [s3-manifest-red.txt](s3-manifest-red.txt)).
- **IMAGE_BUILD_NOT_TESTED.** Docker Desktop 4.57 có cài, daemon không chạy; em mở thử một lần và nó dừng ở hộp lỗi: `initializing backend: initializing cli binaries configuration: repairing vmnetd configuration: configuring privileged port mapping: applescript error: … /bin/sh: md5: command not found`. Lỗi này lần đầu xuất hiện trong log ở lượt mở của em (log cũ từ 02/2026 không có); `/sbin/md5` vẫn có trên máy; **nguyên nhân chưa chẩn đoán xong** (macOS 27.2 hoặc môi trường PATH). Không thử sửa vì bước đó đụng cấu hình đặc quyền trên máy Owner; không bấm «Reset to factory defaults» vì sẽ xoá dữ liệu VM 44 GB. Đã tắt các tiến trình Docker em mở. Không có Lima/Colima/Podman. Không dùng VPS để bù.
- **Thay thế có giới hạn, không phải image** ([package-smoke.json](package-smoke.json)): dựng cây chỉ gồm đúng tệp COPY, requirements pin thật (FastAPI 0.116.1), app thật: 16/16 ca HTTP admin qua route thật, OpenAPI không lộ tham số nội bộ; `mcp_server.server` import được từ cây Dockerfile.mcp; task khai danh chạy qua supervisor/worker thật từ cây đó. Base image `agent-data-workspace:20260917-git` không có trên Mac nên việc FROM còn hợp lệ là chưa kiểm.
- **Rollback mức nguồn trên cùng một queue.sqlite:** candidate → PR357 → main → candidate đều chạy được task mới; job đang chờ không mất. Giới hạn: lùi về main thì retry job đã xong bị chạy lại (đúng lỗi PR357 sửa). **Rollback image: NOT_TESTED.**
- Runbook rollback image (`DESIGN_READY`, chưa chạy): build overlay FROM đúng tag đang chạy, ghi tag cũ; lùi = compose về tag cũ + release ghim cũ qua apply-v0; `queue.sqlite` chỉ thêm cột nên không cần lùi schema; `incomex-workspace-exec.service` trên host import `workspace_runtime` từ cây nguồn VPS nên phải đổi cùng lượt. Chạy thật cần Owner GO theo DROOT56.

## GitHub CI
[Run 41155116908](https://github.com/Huyen1974/agent-data-test/actions/runs/41155116908), job 124400090105, **SUCCESS**, `gate=GREEN` đúng head `5ef7d97e`, base `6160f9ad`, merge-test `b541bd12`. Preflight, secret scan, actionlint/policy, policy regressions, Unit đều success, không bước nào skipped; **Unit thật 355 passed in 44.99s**, TESTS gồm `test_hjw_four_facts.py` ([ci-summary.json](ci-summary.json), [ci-run.json](ci-run.json)). Workflow không đổi trong RUN này. `ci_change_kst_review=true` còn nguyên từ diff PR cũ: CI xanh không cấp quyền merge.

## Test đã chạy
| Bộ | Kết quả | Tệp |
|---|---|---|
| Danh sách TESTS của gate, Mac | 355 passed, 5/5 lần | [head-unit-5x.txt](head-unit-5x.txt) |
| RED S1: test mới trên mã trước S1 | 64 failed, 4 passed | [s1-red.txt](s1-red.txt), mốc S1 [s1-unit.txt](s1-unit.txt) |
| RED S2: test race trên mã chưa sửa WAL | 4 failed | [s2-red.txt](s2-red.txt) |
| HTTP fixture admin | 37 PASS | [admin-rest-lab.json](admin-rest-lab.json) |
| `tests/continuation` | HEAD 31 failed/262 passed; PR358 trước RUN cùng đúng 31 ca | [cont-head.txt](cont-head.txt) |

**Hai script lab không nằm trong repo:** `admin_rest_lab.py` và `package_smoke.py` bị Gateway từ chối `SENSITIVE_CONTENT` (chúng chứa khoá giả kiểu `fixture-key-only`, không phải khoá thật). Không sửa chữ để né bộ quét. Chỉ có kết quả JSON; KST muốn kiểm thì tự dựng phép thử HTTP, và test trong gate vẫn tái lập được phần guard qua handler thật.

**31 ca đỏ `tests/continuation` có sẵn trên Mac, không do RUN này** (so khớp từng tên: 0 mới, 0 hết): chủ yếu nhóm `name_twin`/`restore_twin`/`lifecycle`. Nguyên nhân chưa đo, em đoán liên quan hệ tệp Mac; bộ này không nằm trong gate nên chưa có bằng chứng trên Linux.

## Còn thiếu để tới G8_SYSTEM
1. Linux image thật + rollback image (máy có Docker chạy được; không dùng production).
2. KST rà độc lập khác người viết trên combined HEAD; CI đổi workflow vẫn cần KST.
3. Chạy `tests/continuation` trên Linux để xác nhận 31 ca đỏ chỉ do Mac.
4. Cấu hình mapping profile sống; sửa `vector-audit.yml` trước enforce.
5. Source alignment GitHub↔VPS, release có Owner GO (DROOT56), advertise-only → C1/C2 AI thật → guarded enforce/C1_FINAL.
