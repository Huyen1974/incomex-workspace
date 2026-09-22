# Disposition các đường ghi — sau candidate r3

Đối chiếu bảng trước sửa trong write-paths-before.md; quyền thực trong configured.json, raw requests.jsonl/gate-results.json. Bảng này áp dụng identities human-editor/service-author của fixture; outsider được đo deny. Admin cấu hình và DB superuser là trust boundary, không phải business identities được bảo vệ khỏi chính người quản trị.

| Đường | Quyền/kiểm hợp đồng/revision/mutation | Actual |
|---|---|---|
| POST proof-write/form/:id | Native ItemsService accountability; governed Joi profile + FK/exact catalog; khóa form và CAS trong cùng transaction; sync links + native audit + receipt | Valid V1/note/partial200; sai contract422; stale409 |
| POST proof-write/record/:id | Native ItemsService quyền thật; governed record profile + form exact current Draft revision; CAS + audit + receipt cùng transaction | Human create/service update200, reject spoof/scope/input; cùng request replay200 |
| Native item create/update/delete + bulk | Giữ permissions để ItemsService của gate kiểm thật; core hook chỉ nhận transaction do endpoint sở hữu, mọi native bypass không có capability bị deny | REST403; query emitEvents=false và version cũng403 |
| Native /versions create/read/save/promote/update | Đóng business version permissions gồm READ vì save dùng quyền read; ID version thật còn tồn tại phục vụ deny |403, delta/main không đổi |
| GraphQL mutation | Native mutation gặp cùng core hook/permissions | HTTP200 với error WRITE_GATE_REQUIRED/FORBIDDEN; PG/audit không đổi |
| MOW/MOT/checkpoint/catalog/profile/route writes | Native business permissions đóng sau seed; không cần sửa qua pilot | MOW/catalog403; exact permission snapshot lưu trong configured.json |
| Material links/receipts | PG nội bộ, không có business API write; cùng transaction endpoint quản lý; FK không cho sai quan hệ | link-write403; constraints/readback + rollback có evidence |
| Arbitrary action/table | Không có enabled route quản trị trong PG → deny, không nhận collection từ body |403 |

Không kiểm mọi HTTP verb/capability toàn Directus. Không chứng minh admin/deployment misconfiguration chống được mọi cách; required-bundle load failure đã thử dừng app. Receipt replay đọc lại native authority hiện hành trước trả kết quả gốc. Không mở native content version editor trong scope để tránh một cửa save không cưỡng chế được revision Draft.
