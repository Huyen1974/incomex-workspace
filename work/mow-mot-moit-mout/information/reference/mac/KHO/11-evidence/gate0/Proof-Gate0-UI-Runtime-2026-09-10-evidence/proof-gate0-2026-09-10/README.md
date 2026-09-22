# Proof UI + Runtime Gate0 — 10/09/2026

**Verdict: READY FOR PM GATE0 EXIT REVIEW.** Đề nghị PM xét evidence trong phạm vi lệnh `pm-command.md`; không tự nghiệm thu Gate0. Retrieval đã PM ACCEPT/DONE; scoped write-gate trước đã PM ACCEPT. Bộ 66 ca không chạy lại vì hash guard giữ nguyên. O1–O3 vẫn NOT VERIFIED; R1, full release governance và production deployment chưa mở.

Đọc nhanh: [8 ý gửi PM](bao-cao-owner.md) · [đối chiếu 19 điều kiện](verification.json) · [12 điều kiện UI](ui-verification.json) · [trace 3 lượt tự chạy](runtime-trace.json) · [9 receipt/actor/audit](audit-correlation.json) · [code và bảo trì](code-inventory.md) · [cleanup](cleanup.json).

## Kết quả thực đo

| Yêu cầu PM | Kết quả và nguồn |
|---|---|
| U0/U1 existing renderer, code-last | Current compiled UForm source được đọc lại có cùng SHA; bounded local Form/UForm/FormCustom reuse, không survey cả hệ. `current-renderer-source.json`, `ui-source-before/provenance.json`, `ui-product.diff`. UForm cũ hard-code inbox; helper có sẵn cung cấp HTTP/CRUD, chưa giải quyết expected revision/request replay/conflict/read-back. Một composable dùng lại `$fetch`; không Field/MOW-specific branches. |
| U2 declaration-only V1→V2 | `remote/declaration-v1-result.json`, `remote/declaration-v2-result.json`: service qua guarded write; form revision2→3, schema một input→hai input; cùng 3 Field. `ui-v1.png`, `ui-v2.png`, AX tương ứng. Ngày tạo chỉ ở system_fields, không input người nhập. `ui-final-hash-verification.json`:36/36 source/build không đổi. |
| U3 actual browser | `browser-http.jsonl`, `ui-submit*`, `ui-reopen*`, `ui-wrong-datatype*`, `ui-conflict*`, `ui-resolved*`, `ui-exact-retry*`, `ui-final-reopen*`. Tạo record revision1, mở lại; 422 không mutation; service đẩy revision2→3 trong lúc UI giữ2; UI409, giữ bản nháp và chặn submit tiếp. Người chủ động đọc3/nhập lại rồi ghi4. Exact retry cùng body/key trả replayed=true và vẫn4. |
| R immutable TEST fixture | `remote/release-v1.json`, `release-v2.json`: mỗi snapshot gồm MOW/MOT test version, form revision3, 3 Field/3 exact contracts, profiles và capability code SHA. Runtime so content hash/code hash trước dispatch. Business API identities và worker/producer SQL không sửa release được; current binding chuyển V2, instance cũ giữ V1. |
| C candidate | Chỉ triển khai pg-boss12.30.0 +pg8.23.0. `runtime-decision.md`, lock, installed source/package hashes; native worker complete/fail excerpt. Không fork thư viện, không viết queue algorithm, không nhét worker vào CMS. |
| C3-A/D autonomous | Event001 commit07:09:08.211 UTC; worker tự nhận07:09:08.537, guarded effect07:09:09.744, lưu result và native ACK. Không Agent claim/action/ACK. `remote/worker.jsonl`, `runtime-trace.json`, native `proof_boss.job` completed/output. PID1 là PID trong container; Docker host PID/process lưu riêng. |
| C3-B duplicate/new occurrence | Cùng event001 trả cùng event/instance/job; ảnh PG happy/duplicate không đổi effects/audit. Event002/003 cùng case vẫn tạo lượt mới hợp lệ. Cùng occurrence đổi payload bị OCCURRENCE_CONFLICT trước commit. |
| C3-C/E pin/restart | Dừng riêng worker; event002 đã queued, instance pinV1, chưa attempt. Tạo V2/chuyển binding, restart worker: event002 tự chạy V1, event003 mới chạyV2. 3 jobs completed, 3 attempts, 3 AUTO records revision1; không effect thừa. Không kill giữa effect/ACK. |
| C3-F / regression | 10 negative cases đều từ chối và không mutation; valid human/service/stale/replay đo qua UI/runtime. 9/9 receipts map đúng native Revision→Activity actor. `remote/regression-subset-results.json`, `audit-correlation.json`, `verification.json`. Service không thành human approver. |

## Exact environment và giới hạn

PG16.13 pinned image +Directus11.5.1 image cùng digest proof trước; runtime Node22.14.0 tách process. Nuxt3.20.2, Vue3.5.25, NuxtUI2.22.3 lấy từ dependencies hiện có; không nâng nền. Browser harness chạy Node20.19.6 local, trong khi current deployment đã đo Node20.20.0. Vì vậy bằng chứng là **component browser rehearsal dùng current renderer**, không khẳng định toàn production bundle/deployment giống hệt. FormCustom và Form block không đổi, UForm chỉ đổi tích hợp trước V1. Build hoàn tất trước freeze; không HMR/rebuild giữa V1/V2.

Proxy lab native-login bằng một synthetic human-editor, token chỉ ở server/request, không đưa credential vào browser evidence. Đây là cách tạo identity có quyền thật cho proof; chưa chứng minh production login/session/delegation. Runtime dùng synthetic service-author, không admin; worker PG role không UPDATE business record/release. Bootstrap owner có thể dựng/dọn fixture và không phải business identity.

**Pin có giới hạn cần PM thấy rõ:** TEST release có immutable snapshot và code/hash/ref chính xác; lần thử V2 đổi MOW/MOT test version và input của AUTO, cùng form Draft revision3/contract versions. Guard hiện tại vẫn chỉ chấp nhận exact current editable-main revision và governed profile hiện hành; chưa là release-aware execution API. Nếu Draft/catalog thay đổi sau này, không được tự resolve latest/replay input cũ; đường xử lý/thiết kế release-aware còn phải thực chứng ở scope sau. Không dùng `main` làm bằng chứng immutable; immutable identity là release UUID/hash trong bảng TEST riêng.

Full health503 vì SMTP cố ý đóng ở loopback:9; PG/storage checks đều OK, API ping200. Không gọi đó là full health PASS. Lab internal network, không public ports/egress/external side effect; không dữ liệu học viên. Cleanup đối chiếu 5 demo IDs/images/start/restart/state và hai safe GET status/body/location không đổi; đây không full demo regression.

## Bản thử và sửa lỗi

`corrections.md` giữ tất cả lỗi đã gặp: thiếu cấu hình build harness, thao tác clear UI đầu tiên không xóa được35 (đã tạo thêm valid revision2), thiếu bootstrap/producer ACL, bỏ khóa đọc thừa, collector đọc thiếu nhất quán, metadata driver dependency. Các lần emit lỗi đều rollback trước tạo event/instance/job. V1 fixture generation đầu bị hủy ở bootstrap khi chưa runtime event/effect, có snapshot/source/log giữ lại. Bộ runtime thực đo đầy đủ bắt đầu sau sửa; không relabel các lần lỗi thành PASS. `observe-restarted-v1.json` là timeline sample bị overlap event003, không dùng cho cross-table counts; final verifier dùng atomic MVCC snapshot.

## Chạy lại

1. Dùng **lab mới do người chạy sở hữu**, chỉnh thống nhất tên/ownership/path trong các harness; kiểm occupancy và demo smoke trước. Không chạy trực tiếp script này lên production: fixture không phải migration triển khai.
2. Pinned PG/Directus từ `provision-lab.py`; seed cùng family/contracts/identities, seed-draft metadata; configure guard/relations rồi mount đúng extension bytes. Credential được sinh riêng, giữ private, không có trong archive.
3. Chuẩn bị isolated Nuxt harness từ `ui-source-after`, dùng đúng versions của repo hiện có. Đây không là bản repo ứng dụng đầy đủ. Build trước test, freeze sources và build; boot loopback qua protected lab identity proxy. Thực hiện declaration V1, browser V1, declaration V2, reload V2 và chuỗi thao tác UI trong evidence. Không sửa UI giữa hai declaration.
4. `runtime/package-lock.json` + `npm ci --ignore-scripts` trên môi trường phù hợp; runtime dùng Node≥22.12 (proof dùng22.14). `runtime-prepare.py init` tạo TEST mapping/roles, native setup pg-boss tạo queue/schema, grant producer INSERT cả job và job_common. Bootstrap CREATE được revoke sau setup.
5. Sau UI record tạo TESTreleaseV1; start worker; emit event1; chỉ đọc evidence cho tới jobcompleted. Emit lại event1; dừng worker; emit2; chụp queued/pin; tạo V2; restart worker; chờ tự complete; emit3. Event fixtures và control ghi ở `runtime-events.json`, `runtime-control.py`, `emit-event.py`. Không manual claim/action/ACK.
6. Chạy scoped negatives, thu consistent PG snapshot/worker/HTTP/audit. Offline chạy `python3 verify-evidence.py` với cấu trúc artifact `remote/`; assertion hiện tại19/19. Dùng hash guard để quyết có cần full66 hay không.
7. Export allowlist, kiểm file hashes/secret scan, dọn chỉ resources có ownership label, đối chiếu demos. Không giữ credential để tiện chạy lại. Final ZIP manifest kiểm SHA/bytes; HTML snapshot chỉ read-only evidence, không SSOT current thứ hai.

Không đo effort/tokens toàn vòng, tỉ lệ98%, throughput/load, production SLO hoặc full HMITL. Không mở candidate runtime thứ hai. Phải có maintenance owner/target built-in review trước đưa candidate vào sản phẩm.
