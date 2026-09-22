# Platform — quyết định có giới hạn, 11/09/2026

**CURRENT MODULE BRIDGE WITH KNOWN RISK. Directus12 full target: PENDING LICENSE PRECONDITION. Không production upgrade.**

| Thành phần | Nguồn/phiên bản đã kiểm | Kết luận |
|---|---|---|
| PostgreSQL | CURRENT 16.13 đọc thật; TARGET 16.15, official 13/08/2026 | Giữ major 16. Lab 16.15 constraint và dump/restore đạt; kế hoạch production ở dưới. |
| Directus | CURRENT 11.5.1; latest 12.3.1 npm official; image exact theo lab.json | Bridge 11.5.1/Joi17.13.3 chạy các proof. Gate2 đã thấy 12.3.1 trả 403 custom_permission_rules_enabled. Không đổi tên proof bridge thành target pass. |
| Nuxt/Node | Nuxt4.5.2 / Node24.21.0; worker Node22.23.2 / pg-boss12.30.0 / pg8.23.0 | Giữ exact target đã nhận; không đuổi major mới. Build/SSR/session/Form/Table lặp lại trên bridge; worker actual17cases. |
| UI/Image | installed UI2.22.3 / Image1.11.0; latest UI4.11.1 / Image2.1.0 | Audit hiện tại 4 mục: 1 moderate, 3 high. Không force major. |

## Module decision

Đã build lại đúng module hiện dùng trên Nuxt4.5.2, giữ FormCustom, Form/UForm, DirectusTable và transport nguyên hash Gate2. Native Vite cssMinify=esbuild vẫn cần cho CSS UI2. Browser đăng nhập session native, render form+3contract rows, gửi 150 phút thành công và read-back. `nuxt-session-ssr.json` ghi 200, httpOnly/Lax, Secure=false chỉ loopback.

UI4.11.1 không drop-in: source chính thức Table dùng prop `data` và TanStack ColumnDef; DirectusTable hiện truyền `rows` + `key/label`; Form API4 dùng FormField thay FormGroup, Tailwind4 khác nền UI2. Đã đối chiếu exact source/peerDependencies; chưa migrate/build toàn module4. Không gọi đây là TARGET MODULE SET READY. Audit hiện tại đề nghị hai major trên; không áp dụng tự động. Image vẫn cảnh báo sharp binary darwin-arm64; upload/signature/image transformation, SSO/session expiry/CSRF và localStorage identity/scope key chưa production verified. Chủ trì next: Codex bounded module migration proposal+PM xét chi phí thay đổi; không buộc Owner học UI mới chỉ để giảm audit.

## License facts cần giữ đúng

Nguồn: [Directus OIG](https://directus.com/oig), [FAQ](https://directus.com/oig/faq), [license](https://directus.com/license), raw receipts+SHA ở evidence/official-sources.json và official-followup.json. Hai threshold là doanh thu dưới 5M USD/năm và dưới 50 nhân viên. Studio end-user/entity scope xác định tổ chức nào phải đủ điều kiện; không phải threshold ghế thứ ba. Revenue Owner đã cung cấp, không hỏi lại. Chưa đủ: headcount/entity scope/Studio external users/software key. OIG cần registration/key, telemetry và kết nối license; air-gapped/offline không được bao hàm. Lab no-egress này không chứng minh activation/full licensed permissions. Không đăng ký, không nhận terms, không cấp key, không bypass. Nếu chọn OIG, PM cần kế hoạch staging có license/egress đúng phạm vi trước target permission proof. License chưa đủ không chặn đọc metadata/hợp đồng hay proof bridge.

## PostgreSQL16.13→16.15: kế hoạch minor production, CHƯA THỰC HIỆN

Đã đọc metadata 5 database: postgres,workflow,directus,incomex_metadata,directus_gov_test_20260602. `pg-minor-metadata.jsonl` ghi exact extension/opclass/expression. Hai DB directus và gov_test có mỗi 3 GiST: `normative_registry.excl_nrm_temporal` dùng gist_text_ops(article_number)+range_ops(valid_period); `idx_nrm_valid_period` và `universal_edges.idx_ue_valid_time` dùng range_ops. Không có GiST float4/float8 opclass hay extension ltree trong 5 DB. Vì vậy lỗi btree_gist NaN/ltree của release16.15 **không áp dụng theo metadata đã quan sát**, không cần đọc business values để đếm NaN trên index không chứa float. Không suy rằng mọi index/hệ khác đều an toàn; recheck trước window.

Nguồn: [PG16.15 release notes](https://www.postgresql.org/docs/release/16.15/). Minor16.X không bắt buộc dump/restore, nhưng phải có backup khôi phục đã diễn tập. Không reindex hàng loạt theo tên GiST. Replication slots đã kiểm theo 5 DB; pgcrypto extension có ở directus/gov_test, tìm function callers chỉ là source evidence, không loại trừ ứng dụng ngoài DB dùng PGP.

Kế hoạch có cổng dừng: (1) chốt maintenance window/backup owner/RPO-RTO và danh sách client+replication+PGP callers; (2) backup physical/snapshot hoặc logical phù hợp và test restore sang host riêng; (3) kiểm extension/shared_preload/output-plugin/config compatibility và đủ disk; (4) tạm dừng writer bằng kế hoạch được duyệt, đổi exact minor image, startup/version/schema/read/write smoke có đối chiếu; (5) rollback bằng backup/quy trình đã test nếu smoke sai — không hứa đổi image ngược sau khi có writes là đủ. Chưa có window/RPO-RTO/production backup-restore bằng chứng nên production adoption còn chờ. Proof hiện tại chỉ dump/restore DB synthetic trong container riêng của lab; so forms/contracts/versions/ranges/GiST khớp. Không production backup/reindex/DDL/restart.
