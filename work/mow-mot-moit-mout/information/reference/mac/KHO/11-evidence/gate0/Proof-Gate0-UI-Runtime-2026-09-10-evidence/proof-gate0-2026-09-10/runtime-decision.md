# Quyết candidate trước khi viết worker — 10/09/2026

**Chọn duy nhất pg-boss12.30.0** cho lab; package được chuẩn bị với lockfile/ignore-scripts, worker riêng dùng Node22.14.0 có sẵn trong pinned Directus image. Không đưa worker vào CMS process, không nâng stack. Chưa coi install là runtime PASS.

| Candidate | Exact evidence và gap | Disposition |
|---|---|---|
| Existing PG job_queue/functions | source-database.json và c1-endpoint-trace.json trong proof trước: claim atomic có sẵn, ACK không thấy kiểm lease_until/persist summary; authority caller text; chưa có executable bridge/capability handler. Để đáp ứng scope phải chứng minh/vá queue semantics ngoài generic dispatch. | NOT FIT cho lượt này từ exact source, không chạy/modify queue production. Không build candidate1. |
| pg-boss12.30.0 | Package/version/Node requirement đã kiểm nguồn chính thức. Library cung cấp durable job, polling/claim/retry/completion và transaction adapter; chỉ bổ sung event/instance/release/attempt mapping + registered safe action qua guard. | SELECTED để thực đo. Không viết lại queue/retry/locking. |
| Directus-native/current composition | Proof trước không tìm thấy approved native bridge; không có new evidence để hồi sinh. | Không mở lại survey. |

Nguồn: exact PG/bridge trong gói đã nhận; [package tag12.30.0](https://raw.githubusercontent.com/timgit/pg-boss/12.30.0/package.json), [pg-boss job states/work behavior](https://pgboss.io/introduction). Lockfile và installed source là căn cứ thực thi cuối, không theo floating latest.

Một nguồn execution: pg-boss schema riêng trong lab PG; không enqueue song song vào job_queue cũ. Canonical TEST event/instance/attempt/results và immutable release ở PG; queue chỉ làm chủ delivery/retry/ACK. Worker service gọi guard, không dùng admin cho effect. Không external action.

Chi phí: dependency mới cùng transitive lock; một process/container worker mới; schema library tạo; generic mapping/handler vẫn là code, phải kê LOC. Cần owner sản phẩm cho package/schema upgrades, service credential, telemetry và replay/regression. Exit: dừng intake, drain/reconcile event→job→receipt trước thay executor; giữ IDs/evidence. Target native sau này phải chứng minh cùng contract trước thay candidate.
