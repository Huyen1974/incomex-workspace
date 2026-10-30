# HJW · RUN19 — Codex sửa F1/F2 trên PR #358; KHÔNG MERGE/DEPLOY
RUN_ID: HJW-G8-AD-F1F2-FIX-GATE-20261030-19
STATUS: FINAL_PROMPT · chỉ có hiệu lực với Host READY@full last-touch PROMPT SHA trên HJW COLLAB + Owner dispatch tay, NO_AUTO_RUN.
Executor_Surface: Codex Desktop MacBook, dev. GPT Chat Host điều hành trực tiếp đến 13h; Claude Chat tạm offline, không cần chờ. KST Claude Code CLI P476 đã phản biện kỹ thuật; chỉ có Host ký READY.
Write_Path: Git/gh ở Mac vào đúng dev branch của PR #358 (Huyen1974/agent-data-test); STARTED/KQ+Bảng và evidence tại Huyen1974/incomex-workspace/work/hermes-joint-workspace qua workspace_* Gateway D12. Không sửa VPS.
Read_First: AGENTS A0/A2/A5/A6/DROOT30/31/56/58/60+GHM_CODE_CHANNEL → README §11/D12 → root COLLAB → HJW COLLAB §0/§1–3/Bảng/P458/P474–P477 → PROMPT này → RUN18 KST P476/README evidence → GitHub PR #358/#357/main, CI GH.

## 1. Đích và luật khóa đầu vào DROOT60
**Chỉ hai lỗi F1/F2 có KST chứng minh ở P476:**
- F1: `agent_data/declaration_contract.py::target_task` suy sai `done-tasks` thay vì mã việc từ `work/done-tasks/<id>/...`, gây lỗi đóng/mở lại. Sửa nhỏ, không fuzzy task ID, giữ `work/<id>/...`; cặp from/to cho cùng id hợp lệ, cặp khác id bị từ chối và không ghi. Không suy ra mã việc khi path rỗng, thiếu id hoặc nguy hiểm. KST đã thử bản sửa cục bộ 4 dòng, 7/7 PASS + 90 RUN17 PASS nhưng đã hoàn tác — tham khảo, không copy nếu chưa test.
- F2: mã bốn thông tin chưa có test check-in/gate. Tạo đúng test file `tests/unit/test_hjw_four_facts.py` và nối bắt buộc vào TESTS của step `Unit tests` ở chính workflow `.github/workflows/ghm-pr-gate.yml` hiện hữu, **không tạo workflow/runner mới**, không sửa policy/preflight/secret scan/permissions/trigger. GH gate phải FAIL nếu test mới FAIL hoặc file không tồn tại. Việc thay workflow phải được KST review độc lập sau, không coi gate tự duyệt workflow của chính mình.

**INPUT READY HOST_VERIFIED**: PR358 OPEN/DRAFT head `4851f6cde86bade6ce70433958cddc76a307f9f1`, base/main `b4c9ea19cf2e57594a231c2819e098fe0002c99a`, hiện 6 paths code; PR357 OPEN/DRAFT head `36c682914c9f412078113b6d85319f11356d1130`, 4 paths queue, trùng `workspace_tasks.py`. Codex đã push PR358 thật ở RUN17, có đường GH dev; PR351 từng thay workflow qua lane dev/codex. P476 KST chứng minh F1 và ghép hai PR (2 dòng, queue giữ `enqueue_once`). CI gate hiện cài pytest 8.4.2/PyYAML/jsonschema/psycopg2-binary, unit step chỉ chạy danh sách 4 tests cố định + KB pagination tùy chọn: F2 còn thiếu thật. Repo main vẫn có `AGENT_INFRA_TOOLS` Hermes. VPS 4worker source `1cc706dc0f1ba7ef05f4631c04f604d2cacd9982`, image `4635e417…`, PR357 đã có trên live nhưng chưa merge; không lấy GH main/PR358 làm deploy image. Gh auth/CI/branch freshness và kết quả test khi thực thi = EXECUTOR_FRESHNESS, không tự biến thành S0 blocker do Host chưa tìm nguồn.
**Đúng 3 path thay đổi dự kiến trong RUN19:** contract.py F1, test/unit file mới, ghm-pr-gate.yml một dòng ở Unit tests; tổng PR358 sau lượt dự kiến 8 files. Nếu phát hiện phát sinh hợp lý, dừng mở rộng, nêu bằng chứng cho Host, không bẻ scope.

## 2. STEP_WALK — một lượt Codex
**S0: one read gate.** Kiểm HJW READY/STOP/STARTED, PR branch và HEAD đúng repository, PR357 không thay; nếu SHA tiến thì đọc diff scope mới. Ghi STARTED DROOT31. Không PRECHECK RUN riêng, không yêu cầu Claude Chat, không dò repo/remote mới. Nếu GH write permission session đổi, vẫn có thể làm local source/test và KQ PARTIAL, không bỏ kết quả.
**S1: F1 RED→GREEN.** Viết test mới trước và chạy trên PR358 HEAD hiện tại để chứng minh F1 đỏ: active path, done-tasks path, move active→done, done→active, nhiều operation cùng task, move cross-task phải reject, path `work/done-tasks` không có id phải không suy sai; declared correct id succeeds, wrong id fails/zero mutation. Sửa target_task vài dòng rồi chạy GREEN, không nới quyền/ACL, task names exact, không đổi protocol.
**S2: F2 và CI thực sự chạy.** Test file chuyên biệt phải bao phủ F1 cộng four-facts logic: đủ bốn trường, missing_fields/field_example, alias + unknown valid AI product, origin cloud/macbook/vps, raw/canonical/provenance, auth không nâng quyền, scope mismatch/0 mutation, operation_id retry changed facts và upload/queue carry qua fixtures tối thiểu. Trên runner hiện tại KHÔNG có FastAPI/PG/Docker; chỉ dùng deps sẵn, các stubs nhỏ không giả E2E. Điều kiện `WORKSPACE_DECLARATION_MODE` advertise/enforce phải test đúng; không cần Docker Mac.
Thêm tên test mới vào TESTS cố định trong unit step của `ghm-pr-gate.yml`, không bọc bằng điều kiện `if test -f`, không dùng ignore errors. Giữ nguyên GHM preflight/policy/secret scan/runner, mọi test cũ và gate summary. Diff với main phải chỉ bổ sung tên test trong YAML; workflow self-edit phải được KST rà sau, không sửa policy để làm xanh. Chạy local Mac tests cần thiết + regression RUN17 89/90 nếu phù hợp; PR357 queue overlay chỉ Mac/read-only, không sửa PR357, không kéo Hermes vào runtime.
Commit rồi push **không force** lên chính branch PR358; đọc GH gate theo HEAD mới. Chứng minh test mới thật sự chạy (log Unit tests có tên/count), gate SUCCESS đúng SHA; nếu gate chỉ xanh nhưng không chạy test mới = F2 FAIL. Lỗi test mình gây ra sửa cùng RUN phạm vi; CI pending/gh auth mất quyền thì ghi P478 PARTIAL với code/test/commit đã giữ, không chờ vô hạn.
**S3: KQ/cleanup.** Ghi P478/KQ và Bảng qua workspace_*, evidence `evidence/run19-ad-f1f2-20261030/` gồm PR URL, HEAD trước/sau, 3 file diff, test RED→GREEN, workflow unit test evidence+CI run/sha, ghi PR357 unchanged, 0 VPS mutation. Dọn Mac scratch. KQ chỉ `G8_AD_F1F2_SOURCE_CI_PASS` khi F1 và test gate mới thật PASS; còn lại PARTIAL chính xác. PR luôn DRAFT, không KST_ACCEPT, không MERGE/DEPLOY.

## 3. Các khoảng trống còn lại — bắt buộc trước G8_SYSTEM, KHÔNG code trong RUN19
- `workspace_exec` hiện NON_SOURCE nhưng có thể ghi state/queue: khảo sát logical write/carry 4 facts, không bỏ vì tool tên là exec.
- KB write tools upload_document/update_document/patch_document/ingest_document/delete_document hiện không đi qua adapter workspace declaration: phải đo/gate trước khi tuyên mọi lượt ghi hai Gateway được khai danh.
- Auto-fill: chỉ derive AI product + origin_environment từ verified metadata thực sự đáng tin (nếu có); nếu không đủ thì yêu cầu AI khai, không suy từ VPS host; operation_id là mã transaction, KHÔNG giả mã RUN. Lưu raw+canonical+provenance.
- PR357 fresh queue.sqlite bootstrap race ở DB trống là nợ VPSC2 độc lập; không sửa thuật toán queue lần này, nhưng kiểm rõ trước khả năng phục hồi/rollout.
- Sau F1/F2 + KST CI review, khép coverage và thử Linux AD image rebuild/rollback cùng source queue4 mới, rồi G8_SYSTEM → advertise-only → C2+C1 AI thật/Owner Connect một lần → guarded enforce/C1_FINAL. Không merge PR357/358 hay GH→VPS khi chưa GO an toàn.

## STEP_WALK_V1
| Bước | Actor/trigger | Evidence | Fail |
|---|---|---|---|
| S0 | Codex sau Owner dispatch | READY, GH HEAD, STARTED | scoped diff hoặc PARTIAL có bằng chứng |
| S1 | Codex | F1 red/green tests & code diff | sửa hẹp, không đổi live |
| S2 | Codex | test checked-in + workflow Unit tests thật + GH gate SHA | CI pending/RED: PARTIAL, không merge |
| S3 | Codex | P478/KQ+Bảng/evidence, cleanup | Host nghiệm thu, KST CI diff review sau |

**Cấm**: merge/push main, deploy, thêm workflow/runner/secret, sửa PR357 hoặc Hermes/Gemini/live VPS/PG/Directus, mở task mới, chờ Claude Chat đến 13h.
