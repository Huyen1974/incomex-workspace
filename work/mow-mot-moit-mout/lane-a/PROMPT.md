# PROMPT — LANE A08 · Tìm SSOT loader HPML gây reload

RUN_ID: MMIM-LANE-A08-20260930-01
PROCESS: CHUNG.TIM
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex

Write_Path: chỉ append KQ vào `work/mow-mot-moit-mout/lane-a/COLLAB.md`.
Mọi source/runtime/canonical khác: **READ-ONLY**.

## 0. Registry / concurrency
Đọc `../council/REGISTRY.md` READ-ONLY.
B06 là writer duy nhất của `ban-duyet.html`.
A08 không patch `ban-duyet.html`, không patch runtime.

## 1. Bằng chứng A07 đã PROVEN
Owner View có reload thừa khi `publishedRevision` đổi vì commit không liên quan dù bytes của tài liệu không đổi.
Runtime đang phục vụ:
`/ui-preview/hpml-view-for-user/view.html`
A07 thấy logic kiểu `sync-status → publishedRevision → Y/H → iframe key/src`, nhưng chưa xác định SSOT source có quyền ghi.

## 2. Câu hỏi duy nhất
**Source-of-truth nào sinh runtime loader HPML này, nằm ở đâu và đường deploy nào cập nhật nó?**

## 3. Tìm bằng chứng
Read-only search:
- workspace repo hiện tại;
- các path/config/deploy manifest/script tham chiếu `hpml-view-for-user`, `sync-status`, `publishedRevision`, iframe key/src;
- root ui nếu có source;
- tài liệu deploy/README liên quan;
- history chỉ đọc khi cần.

Không suy từ minified runtime nếu không truy được source authority.

## 4. Kết quả chỉ được một trong hai
### FOUND_SOURCE
Ghi:
- repo/root/path SSOT;
- current hash/version;
- write authority / deploy route;
- runtime URL tương ứng;
- bằng chứng source này thật sự sinh runtime đang phục vụ;
- patch point tối thiểu cho A09.

### BLOCKED_SOURCE_UNAVAILABLE
Ghi:
- đã tìm những root/path nào;
- runtime nào đọc được;
- source authority nào còn thiếu;
- cần expose/kết nối gì để Host có thể giao patch an toàn.

## 5. Không làm
- Không sửa runtime bundle trực tiếp.
- Không sửa portal bằng cách tìm/replace mù.
- Không sửa `ban-duyet.html`.
- Không “fix” chỉ bằng bỏ iframe key nếu src vẫn đổi.

## 6. KQ
`KQ@MMIM-LANE-A08-20260930-01 XONG|DỪNG`
`KQ@LANE-A A08 · PROCESS=CHUNG.TIM · PROCESS_GATE=PASS|BLOCK · source=FOUND|BLOCKED · runtime=/ui-preview/hpml-view-for-user/view.html · NEXT=A09_PATCH_HPML|HOST_EXPOSE_SOURCE`
`COORD · NOW=XONG|DỪNG · NEXT=<...> · BLOCKED_BY=<...> · RESERVED_TARGETS=lane-a/COLLAB.md · LAST_SYNC=PRESERVE-01/A08`

Dừng.
