# Gate3–4: bằng chứng và phần chưa đạt · 11/09/2026

**BLOCKED BY DATA-AUTHORITY + LIFECYCLE-AUTHORITY.** Hồ sơ này giải thích bằng chứng của lượt v1.6.17; trạng thái dự án mới hơn luôn đọc ở file cấu trúc hệ thống. Gate0–2 giữ phạm vi PM đã nhận; Gate3/4 chưa exit, Gate5–7 chưa bắt đầu, O1–O3 chưa xác minh.

## Phần đã chứng minh

- Có C01–C10 và 11 family, tổng cộng 28 profile. Kiểm cấu trúc cuối **112/112** bằng Joi17.13.3. C01 phân biệt tám loại identity; immutable Version không mang edit revision hay activation. Fixtures là dữ liệu tổng hợp, không phải quyết định nguồn nghiệp vụ.
- C06–C08: sửa hai adapter có sẵn để lấy form/profile từ release của Instance, kiểm quyền hiện thời qua native Directus và dùng retry/ACK của pg-boss. Fresh lab **17/17**; closure V1 16 nguyên liệu, V2 17, mọi node đều reachable, ref phân giải được, digest đúng, không có giá trị main/latest. Phạm vi chỉ một MOT/AUTO ghi nội bộ.
- P5/P6: **29/29** ca. Route/profile tách nội dung binding khỏi global Definition; có cả API write được phép và API write bị chặn. Parent FK, expected revision và slot giúp chặn kết quả muộn; provenance được giữ để đọc lại context rồi resume. Chưa phải toàn bộ cơ chế tự admission/duyệt của Factory.
- Reference/type/unit/FK/UNIQUE **30/30**; action/evidence stale **10/10**. Khi mất phản hồi sau commit, worker ngừng retry, phép đối soát đọc receipt và record xác nhận một effect. Phép đọc này chưa tự hoàn tất trạng thái nghiệp vụ của queue.
- Nuxt bridge build, SSR, session, Form submit/readback và Table đã chạy. PG có metadata của năm DB và synthetic dump/restore. Chi tiết và giới hạn tại PLATFORM.md.

## Vì sao chưa thể khóa nguồn dữ liệu

Matrix kiểm kê **385 vị trí khai báo**, không phải 385 cột cần tạo: 4 native authority, 26 reuse mapping, 44 đề xuất NEW_REQUIRED chưa đủ bằng chứng loại reuse và 311 UNKNOWN. Các trường context lặp lại cần cùng một authority. Mọi đề xuất tạo mới đều chưa là quyền tạo bảng/cột production.

Metadata thật cho thấy `unit_version` có FK tới `information_unit` và unique theo version sequence, nhưng chưa có căn cứ nhận nó làm semantic Version của các family quy trình. `workflow_steps` có ID và workflow ID nhưng chưa có FK vật lý/quan hệ version tương ứng. `binding_registry` quản lý nguồn đọc, không tự trở thành active-release binding. Candidate concept/usage có FK thật nhưng chưa được nhận làm Field authority. Tên gần giống không đủ để chọn nguồn.

Các dòng UNKNOWN ghi rõ candidate khác nguồn đã xác minh; đường dẫn lab minh họa không được coi là bằng chứng từng contract field đã được lưu. C06 generic envelope và representation graph trong lab cũng chưa có mapping đầy đủ được nhận. Không nên mở một catalog khác hoặc tạo schema theo số leaf để che phần thiếu này.

## Các điểm chặn và đầu ra cần tiếp tục

| Điểm | Bằng chứng / điều kiện gỡ | Đầu mối |
|---|---|---|
| DATA-AUTHORITY | Chứng minh đúng domain, constraints và consumer cho nguồn Definition/Version/owner của representative pilot; giải quyết các UNKNOWN ảnh hưởng pilot; mỗi NEW_REQUIRED phải có căn cứ loại I0–I5. Xem production-mapping.jsonl và ba data map. | Codex truy nguồn, kiểm và đề xuất; PM nhận mapping. Owner không phải chọn bảng/cột. |
| LIFECYCLE-AUTHORITY | C09 đã tách năm action và chặn evidence cũ, nhưng chưa nối policy thật, expiry/revocation, separation of duties và authority cho publish/activate. Không thay approval thật bằng fixture. | Codex kiểm nguồn/quyền và đề xuất; PM chốt policy trong thẩm quyền; chỉ đưa Owner phần đổi trách nhiệm con người. |
| D04 | A là khuyến nghị: executor, delegate, next-task executor, report recipient và handoff contact khác nghĩa. Service tổng hợp không quyết thay nghĩa nhân sự. | WAITING OWNER; không hỏi lại giữa package. |
| Adoption | Directus12 license, Nuxt major/session gaps, người bảo trì và kế hoạch triển khai/khôi phục còn điều kiện. Không dùng điểm này để phủ nhận proof bridge. | PM điều hành bước kế tiếp; chưa triển khai production. |

Không tuyên bố tất cả 16 nhóm ca PM yêu cầu đã đạt ở mức hành vi: output incomplete và retire với Instance đang chạy chưa có proof riêng đầy đủ; expiry/delegation/SoD cũng chưa được kiểm trọn. QA.json phân biệt từng phạm vi. Đây là hồ sơ có kết quả một phần và blocker có nguồn, không phải hồ sơ đề nghị exit.

## Quy trình, bảo trì và tiếp nhận

Đã đọc fresh năm nguồn KB và luật repo; receipt ở evidence/rule-sources.json. Phản biện trước code tại proof/PLAN.md do cùng Agent thực hiện, không gọi là review độc lập. Giữ native PG/Directus/Joi/pg-boss; I6 chỉ sửa adapter đã có. Nếu native target sau này đáp ứng cùng contract và đủ bằng chứng, ưu tiên thay adapter. PM phải chỉ định người bảo trì trước adoption; Agent tác giả không thay trách nhiệm này.

Không sửa OR/TD backend hay tạo PR/deploy vì runtime production không đổi; các phát hiện/việc mở đã hợp nhất vào SSOT/W005. Production chỉ đọc, không COMMENT ON. Hai lab riêng đã dọn; process state của năm demo và hai safe GET không đổi, không gọi đây là full regression. Nhật ký lỗi thử và cách sửa có ở evidence/development-notes.md; Agent sau chỉ đọc mục liên quan, không điều tra lại từ đầu.
