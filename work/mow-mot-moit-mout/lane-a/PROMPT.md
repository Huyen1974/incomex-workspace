# PROMPT — LANE A09R1 · Tiếp tục sửa Owner View sau dirty-gate

RUN_ID: MMIM-LANE-A09R1-20261001-01
PROCESS: CHUNG.APQUYTRINH
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex

## 0. Mục tiêu
Tiếp tục đúng A09 để sửa:
- tab con thỉnh thoảng tự nhảy về UI Master;
- document/iframe remount khi revision chung đổi nhưng tài liệu hiện tại không đổi.

Không sửa `ban-duyet.html`.

## 1. Ngoại lệ dirty-gate hẹp do Host chốt
A09 đã chứng minh:
- repo VPS `/opt/incomex/docker/nuxt-repo` HEAD `79d4dcb57c1cd94213076a042570fd373a75f358`;
- dirty duy nhất nhìn thấy ở parent là submodule `web-rp-current`;
- `scripts/hvu-b2` sạch;
- A09 không sửa/reset/commit `web-rp-current`.

A09R1 **được phép bỏ qua dirty ngoài RUN tại `web-rp-current` CHỈ KHI** trước write chứng minh đồng thời:
1. `git status --porcelain -- scripts/hvu-b2` vẫn sạch;
2. `web-rp-current` không được import/read/copy/use bởi build/deploy dependency closure của HPML;
3. `package.json`, `nuxt.config.ts`, `pack.mjs`, README build/deploy và script copy runtime không trỏ vào `web-rp-current`;
4. build output HPML chỉ phụ thuộc source/dependency đã xác định và không đọc submodule dirty đó;
5. không có file dirty khác xuất hiện trong target/dependency closure.

Nếu bất kỳ điều nào không chứng minh được → DỪNG `DIRTY_DEPENDENCY_UNPROVEN`.

**Cấm** reset/checkout/clean/stash/commit `web-rp-current`.

## 2. Source baseline phải re-read
Tại VPS:
- `scripts/hvu-b2/README.md`
- `scripts/hvu-b2/ui/app.vue`
- `scripts/hvu-b2/ui/nuxt.config.ts`
- `scripts/hvu-b2/ui/pack.mjs`
- `scripts/hvu-b2/sync.py`
- package/dependency files thật sự dùng khi build;
- deploy/copy mapping tới `/ui-preview/hpml-view-for-user/view.html`.

Ghi lại SHA/hash trước sửa và xác nhận vẫn khớp hoặc nêu diff so A09.

## 3. Patch contract
Tách **global snapshot revision** khỏi **document identity**.

### Bắt buộc
- `publishedRevision` đổi vì việc khác không làm iframe của task hiện tại remount.
- Identity của iframe phải dựa trên tài liệu task hiện tại:
  ưu tiên `documentRevision` hoặc content fingerprint/hash.
- Nếu `documentRevision` hiện chỉ là global revision và đổi theo HEAD dù bytes không đổi, phải sửa data contract/publisher để có identity ổn định theo document content.
- `:key` và `:src` không được đổi khi bytes document task hiện tại không đổi.
- Khi document task đổi thật: reload đúng một lần.
- Giữ task selected.
- Giữ section/tab con hiện tại (`matrix-view-formula`, v.v.).
- Không tự default về `matrix-view-master` khi section hiện tại vẫn hợp lệ.
- Giữ Back/Forward/deep-link.
- Không tắt poll/sync/stale logic để né lỗi.

## 4. Test bắt buộc
### T1 unrelated-change
Mở:
`mow-mot-moit-mout + section=matrix-view-formula`.
Gây/quan sát một revision mới không đổi document này.
PASS:
- iframe node không remount;
- section vẫn formula;
- details/scroll/filter state không mất.

### T2 real document change
Đổi document identity thật trong ca test an toàn.
PASS:
- reload 1 lần;
- nội dung mới xuất hiện;
- section formula được giữ.

### T3 navigation
- click Formula ↔ Master ↔ tab khác;
- Back/Forward;
- deep-link;
- manual reload.
Không tự nhảy Master ngoài URL/section yêu cầu Master.

### T4 sync/load
- poll vẫn chạy cadence cũ;
- stale/error vẫn last-good;
- không loop request/remount;
- không tăng bất thường request count.

## 5. Build/deploy
Theo README hiện hành thật.
Trước deploy:
- backup/hash artifact live;
- ghi rollback path/command.

Sau deploy:
- hash source sửa;
- hash output;
- hash live;
- buildId nếu có;
- HTTP/functional console;
- T1–T4.

Không sửa/push bất kỳ source ngoài target closure.

## 6. KQ
Ghi qua workspace vào lane-a/COLLAB:
`KQ@MMIM-LANE-A09R1-20261001-01 XONG|DỪNG`
`KQ@LANE-A A09R1 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS|BLOCK · dirty_exception=PASS|BLOCK · dependency_isolated=PASS|BLOCK · unrelated_remount=PASS|BLOCK · real_change=PASS|BLOCK · section_preserved=PASS|BLOCK · NEXT=<one thing>`

Kèm:
- dependency-closure evidence;
- dirty status before/after;
- files changed;
- before/after hashes;
- build/deploy/rollback;
- T1–T4 evidence.

Dừng.
