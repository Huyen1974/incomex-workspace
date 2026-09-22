# Đầu vào kiểm độc lập · Bản đồ Pha B v1.6.20

**Chưa có kết luận independent PASS.** Codex tự rà tài liệu và logical walk; không thay reviewer. Mở HTML ở gốc gói, mục Chuyển báo cáo/Đi bộ logic/Rà ngược. Không cần chạy lab hoặc production action.

## Năm câu cần kết luận

1. **Mẫu số và nguồn:** 87bước/987lượt có giữ phạm vi Checkpoint0,68hàng cũ cótext và248crosswalk không? Owner “bạn tiếp tục việc đang dở và thực hiện nốt nhé” là chỉ đạo đi tiếp, không acceptance của mọi proposal. Blocker9hàng lịch sử có thật sự ngăn kết luận đủ23/23 không? `historical-source-check.json` cho hash current trùng14. Xin đừng thay source thiếu bằng suy đoán.
2. **Vòng đời và ngoại lệ:** cả12nhóm×4luồng, People/Org tại nguồn chính thức, binding khác Definition, HMITL khác AUTO, Field không task độc lập;8walk và các nhánh chờ/return có thiếu nhu cầu nào? `source-operation` là backup/restore/capacity/RPO/RTO, không HR operation. Nếu thiếu material, ghi source/step/amendment cần quyết.
3. **Control/Agent có đủ cụ thể để giao việc kế tiếp:** từng bước có thôngtin tối thiểu, auto-fill, quyền/error/context, ảnh/source, expected test?84asset không phải automation. Kiểm 3bước chưa dẫn primitive:batch/purge/source-operation.10tool/source có bị nâng lab/source thành deployedtool không? T0dispatcher/tựresume còn thiếu.
4. **Chọn/ghép/loại UI đúng logic và ownership:**30vùng đề nghị là22sửa-ghép/7bù/1xácminh;48candidate có trùngURL/mode. Chỉ4nhãn CHỐT/NHÁP/CÔNG CỤ/BỎ, đều có authority phạm vi.6đề nghịBỎ phải bảo toàn capability/redirect/consumer và không delete sớm. D03 giữ vai đã nhận, không nguyênứngdụng. MOUT không completion; NTGV5vai không grant.
5. **Counts/source/state:**63UI=0đủ+51thiếu+10chưacó+2chưarõ;24khôngformriêng;87total. 30surfaces và11contractgaps và6bảng snapshot khác đơn vị. Heatmap108 ô phải đúng tênhàng→familykey (lỗi cũ đã sửa), cột Ban hành không0giả; xám còn xám vì chưa kiểm chức năng. D04ACCEPT, Gates không bị tựđóng. Kiểm CG06feedbackUUID→integer, CG02literalinput, CG05thiếuTable/People/Org profile, nativeIUdomain/quyền.

## Cách tái kiểm không chạy nghiệp vụ

`document-harness.zip` giữ generator + kiểm tĩnh + kiểm hàm render/filter trong Node VM với DOM giả. Chỉ phần kiểm tài liệu được dùng; không chạy code proof/Flow/harness lab trong source được dẫn. Kết quả gốc ở `check-results.json` và `document-function-check.json`. Manifest/hash không thay kiểm semantic completeness.

Các ca nên lấy mẫu: MOW/Tạo/graph→ready; MOT/Sử dụng/HMITLvsAUTO; MOIT/Sửa/dirtyrevision; MOUT/context; Field/Sửa/unit; People/Org/Ngừng/sourceACK; backup/restore ở luồng ngoài12; feedback→V2→measure.

Bản đồ không có product/API action. Các ảnh là snapshot cũ, source có thể chứa handler thực nhưng chỉ được trích đọc, không nhúng thực thi. Browser file URL bị công cụ chặn ở lượt trước; Codex không lách qua server/browser khác. Chưa kiểm bố cục/điều hướng bằng browser thật của bản đồ.

## Điều PM cần xử lý sau review

Tìm snapshot đúng02/09 cho9hàng hoặc đưa disposition có thẩm quyền; quyết nhận/trả sửa completeness. Sau đó giao theo nhóm dùng lại/bổ sung và rà baseline trước Contract/Data. Không giao “chỉ vá6gap rồi Pilot”. Không đề nghị thêm bảng khi chưa xét nativeIU/registry/source và quyền.
