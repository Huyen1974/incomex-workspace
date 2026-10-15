# PROMPT — TQT-B12-DRAFT-ZONE-20261015-01
RUN_ID: TQT-B12-DRAFT-ZONE-20261015-01
Status: DRAFT · Claude Host Kiểm soát soạn 15/10 theo COLLAB §0 R40–R47 · chờ Owner gật Q1+Q2 (ghi ở 3.4) · GPT rà rồi READY đúng SHA · chưa RUN.
Task: work/tools-quy-trinh · Host nội dung Codex · Host Kiểm soát Claude Chat · Executor: Claude Code CLI trên Mac · Ghi repo: gateway `workspace_*` có expected_version · Ghi VPS: chỉ 1 tệp DOT mới + vùng `tqt_*` trên Directus + 1 khai báo Guard + ghim Config Guard, giữ `VPS-GHI` suốt lượt.
Owner 15/10 14:34: «1. Vẽ cái UI cho đủ 2. Liệt kê các trường cho đủ (làm hợp đồng thông tin) 3. rà config cho khả thi (đúng trường, đúng chỗ) … Đừng phức tạp hóa vấn đề lên.» · 14/10 21:39: «… xoá phần tạm => DOT vẫn dùng được».

## Đích lượt này (nôm na)
Dựng «bàn làm việc» trên Directus nháp: 5 bảng nối nhau bằng mã, đổ dữ liệu đã có vào, Owner mở ra xem được; chứng minh 1 lệnh xoá sạch và dựng lại y nguyên từ GitHub. **Chưa làm QT001** (đó là B3).

## Luật cứng (chạm ⇒ DỪNG)
1. **0 dòng sửa DOT cũ, không gọi DOT cũ khi chạy.** Chụp hash `/opt/incomex/dot/bin/*` trước/sau; chỉ được thêm `dot-master-apply` và cập nhật sổ bằng `dot-dot-catalog --write`.
2. Ghi Directus **chỉ qua `dot-master-apply`**, bằng Directus API chính thức + khoá máy GSM (chép cách nạp khoá của `dot-web-incomex`, không import nó). Không SQL ghi, không psql, không ghi tay Studio, không dùng tool MCP `directus_create/update/delete`.
3. Mọi đối tượng tạo ra mang tiền tố `tqt_draft_` (vùng nháp) hoặc `tqt_selftest_` (bài thử), nhóm «TQT — NHÁP», ghi chú bắt đầu `[TQT_NHAP]`, vào sổ sở hữu `/var/lib/incomex-master-apply/<vung>/owned.json`. Danh sách tiền tố được xoá viết cứng trong mã, không lấy từ JSON.
4. Không dùng `dot-collection-create`/`dot-collection-register`/`dot-registry-*`; không đăng ký vào sổ hệ thống; không Flow/trigger/hook trên bảng nháp; không quyền public; không khoá ngoại ra ngoài vùng.
5. Chụp schema Directus đầy đủ trước/sau (API `/schema/snapshot`): diff chỉ được chứa đối tượng `tqt_*` + quyền/tài khoản xem của vùng. Lệch ⇒ `xoa-vung` phần lượt này tạo + DỪNG.
6. Không đụng SSH/khoá/vai PG (R47 chỉ ghi nhận). Không in bí mật ra màn hình, chat, repo.

## Các bước
| Bước | Làm gì | Xong khi |
|---|---|---|
| S0 cổng | Đọc AGENTS → COLLAB gốc → COLLAB TQT §0 (R40–R47) → PROMPT này. Cần: READY đúng SHA; dòng Owner gật Q1+Q2 ở 3.4 (chưa có Q1 thì bỏ S5, phần khác vẫn chạy); `VPS-GHI: trống` → lấy khoá. | STARTED ghi vào COLLAB TQT |
| S1 B1 · chỉ đọc | ① Đọc `dot-web-incomex` + Directus API thật: xác nhận làm được 4 luật R41 mà không sửa/gọi DOT cũ. ② Chỉ ra nguồn: danh sách quy trình theo Công thức (dự kiến Nhóm cha/Nhóm con ML-DEF-001/002 từ `chuoi-data-v1.js`) · QT001 = MOW001, 3 màn MOT (`work/mow-mot-moit-mout/UI-REVIEW-MOW001.json`) · Master of Master 86 (gốc `ui` `master-of-master-v1.html` #catalog-data) · 28 ML-DEF (`evidence/ui-inputs/definition-master-registry-v1.js`) · 250 Field (`view.html` → `catalog.field_registry`). ③ Chọn mã có sẵn cho 5 bảng lõi (Quy trình · Màn hình · Field · Master · Hợp đồng); không tự đặt mã trùng. ④ Đo: PG Census có báo bảng chưa nhãn không · Owner mở Directus ở URL nào · xoá collection có để sót gì. | 1 bảng ngắn trong P mới: nguồn · số dòng · mã · vướng. Vướng chặn ⇒ DỪNG báo. |
| S2 dữ liệu GitHub | Tạo `work/tools-quy-trinh/master/`: `vung.json` (chỉ vùng `nhap`) · `master.json` (mọi Master: mã, tên, loại ①②③, lý do, `dung_bang`; 5 bảng lõi `dung_bang: true` kèm danh sách mã Field làm cột) · `field.json` (250 Field + Field của 5 bảng lõi theo R36: tên cột, tên hiển thị có «?», kiểu, mô tả, vòng đời) · `<mã>.json` dữ liệu có sẵn của từng bảng lõi. Chỉ JSON, một commit. Nguồn nào bẩn/trùng thì để lại cho B3, ghi lý do. | SHA commit |
| S3 DOT | Viết `/opt/incomex/dot/bin/dot-master-apply` (python3; nhãn đầu tệp như DOT khác; `--help`; chạy thử mặc định, `--execute` mới ghi). Lệnh: `ap <SHA40> --vung nhap` · `kiem` · `co-lap <vung>` · `xoa-vung <vung>` · `thu` (tự tạo vùng `tqt_selftest_`, kiểm, xoá). Đọc tệp bằng `git show <SHA>:…` trên bản sao repo ở VPS; SHA phải nằm trên main; không chạy mã từ repo. Kiểm hết rồi mới ghi; lỗi kiểm thì không ghi gì. Phần G2 để sẵn chỗ nhưng tắt cứng. Bảo vệ Điều 30/31: ghim Config Guard bằng `apply-v0`, sổ DOT, checker `kiem` gắn Guard theo đường `web_incomex` đã dùng (B-CWEB01), rollback = phiên trước của tệp + `xoa-vung`. | `thu` PASS; ghim xong |
| S4 áp vùng nháp | `ap <SHA S2> --vung nhap --execute`: 5 bảng, `ma` là khoá chính dạng chuỗi, quan hệ theo mã (Màn hình→Quy trình; Hợp đồng→Màn hình, Field, Master nơi ghi), nạp dữ liệu. Tạo 3 bộ lọc «thiếu»: Màn hình chưa có Field · Field chưa ai dùng · Hợp đồng có nơi ghi là Master loại ③. | Biên nhận ĐẠT; đọc lại khớp tệp |
| S5 tài khoản xem (chỉ khi Q1 gật) | 1 policy «TQT NHÁP · chỉ xem» (app access, admin=false, chỉ đọc `tqt_draft_*` + bộ lọc của vùng), 1 tài khoản `xem-nhap@incomexsaigoncorp.vn`, không gắn policy khác, giao diện sáng, vi-VN. Mật khẩu sinh ngẫu nhiên cất vào GSM, đưa Owner bằng `pbcopy`, không in. | Tự đăng nhập thử: thấy đúng nhóm nháp, không sửa được, không thấy bảng khác; ảnh chụp |
| S6 thử xoá | `xoa-vung nhap --execute` → đếm còn sót (bảng, cột, quan hệ, nhóm, quyền, tài khoản, bộ lọc, khai báo Guard của vùng) = 0; nhật ký audit hệ thống báo riêng → `ap` lại cùng SHA → so khớp 100% với lần đầu (làm lại S5 nếu đã có). | 2 biên nhận + so khớp |
| S7 đóng | `kiem` xanh; hash DOT cũ không đổi; trả `VPS-GHI`; dọn đồ tạm; ghi 1 P/KQ vào COLLAB TQT (biên nhận, SHA, số bảng/dòng, còn sót, ảnh). Cập nhật Bảng điều khiển ô ✅/■/➡. Đưa Owner link + 4 bước xem bằng tiếng Việt (mở URL → dán mật khẩu → vào «TQT — NHÁP» → mở bộ lọc «thiếu»); Owner xem khi tiện, không chặn KQ. | KQ |

## KQ
- `XONG`: S1–S7 đạt, có biên nhận, còn sót = 0, hash DOT cũ không đổi.
- `DỪNG · <lý do>`: luật cứng bị chạm, B1 thấy vướng chặn, diff ngoài `tqt_*`, xoá còn sót. Trước khi dừng: `xoa-vung` phần lượt này tạo trên Directus (giữ DOT và tệp GitHub), trả cờ, ghi KQ.
- Không làm trong lượt này: QT001 (B3) · dựng bảng cho Master ngoài 5 bảng lõi · G2 · SSH/vai PG · view.html/CHECK005/006.

---
# LỊCH SỬ — KHÔNG CÒN HIỆU LỰC từ 15/10/2026 (thay bằng TQT-B12-DRAFT-ZONE-20261015-01 ở trên)

## (cũ) Hiện hành · Owner giao Host rà QTTH 05 và DOT · 11/10/2026

**P33 hiện hành:** trước khi viết script hoặc gọi công cụ, đọc README mục P33, tra Master DOT/Tool và bảng dùng lại. Dùng CHECK-006 để kiểm kê nguồn + sự kiện có bằng chứng; không cộng hook/gateway thành lượt duy nhất, không lấy có tệp làm đã kiểm. Giữ ⑤, 7 mốc, MOW001 0/7 và không PG. VPS là SSOT; không đẩy gateway sang GitHub cũ.

P31/PR14 hiện hành: đọc README mục P31. CAT-206 schema 1.2, IC phiên 2; kiểm dữ liệu đã ghi/đọc từ P01, tập trường từ schema nguồn, lịch sử toàn bằng chứng. Gọi runner với registry mới đọc và --before-product bản trước. Chỉ trust do adapter thực thi cấp ngoài hồ sơ mới được dùng; PASS tự khai không đủ. Tệp TEST hai tiến trình không phải ca MOW001; reviewer thật UNASSIGNED, endpoint quyền thật/hook máy chủ còn mở. MOW001 0/7, không qua CP03.

P30: trước khi thêm Master/DOT, đối chiếu danh sách sau ghép bằng runner hiện hữu với registry UI vừa đọc; thiếu đầu vào không được báo PASS. Dùng lại Master DOT ML-DEF-024, CAT-006 chỉ là alias có căn cứ. Không tạo Master/script thứ hai cho cùng nguồn/chức năng. Xem README mục DOT và bằng chứng host_review_P30. UI chặn danh sách có xung đột; rào ghi máy chủ còn mở.

Owner giao trực tiếp phiên Codex này tiếp tục tools-quy-trinh, đi bộ từng bước theo phản biện GPT Pro, sửa điểm hở và quản lý tái sử dụng DOT/script/bộ kiểm. Giữ ⑤ và 7 mốc. Nguồn: COLLAB §0, README và catalog trong view.html. Phạm vi: nguồn thiết kế, bộ kiểm, danh mục và UI Master liên quan; không triển khai PG/production nghiệp vụ.

Bộ tính mốc duy nhất: view.html#tqt-record-control. Chạy lại từ Master DOT ML-DEF-024 (CAT-006 là alias) bằng run-tqt-checks.py; CAT-012 định nghĩa bộ ca, CAT-015 kết quả. Kết quả/giới hạn mới ở UI-REVIEW-AGGREGATE.json#host_review_P26. MOW001 chưa đạt CP03; không tự sửa trạng thái thành sẵn sàng/xong từ các cờ khai báo.

**P28 / PR-12 v2:** chạy thử ngoài PG theo D27. Dùng kho thử khai báo trong phiếu sản phẩm hiện hữu theo `catalog.trial_storage_contract`; không tạo bản sao, không chạm PG. 13 câu khai được lưu có mã/phiên cấu trúc/phiên bản ghi; nội dung chưa kiểm vẫn NOT_TESTED, không tự qua CP03. Mapping toàn phiếu, nguồn các Master khác và kiểm độc lập còn mở. Đọc README mục Kho thử ngoài PG và `catalog.host_review_PR12` trước bước tiếp.

**P29 / PR-13 — đọc trước bước kế:** hợp đồng thông tin áp dụng là đầu bài bắt buộc trước rà Config. Đọc README mục P29, `catalog.host_review_PR13` và bản áp dụng CAT-206* trong phiếu MOW001. Không dùng cờ đã rà thay bản hợp đồng; không tự nghiệm thu 51 dòng nháp hoặc 34 địa chỉ chưa thử. Mọi sửa kho thử phải chạy TQT-CHECK-006 `--before-product` trên nguồn vừa đọc, rồi transaction có expected_version và readback; server hook còn mở. Người kiểm độc lập và nơi ghi đúng schema phải đủ trước CP03.

## Lịch sử các đề bài trước — không dùng làm chỉ đạo hiện hành

# PROMPT hiện hành · D24/P23 · Từ mục tiêu tới kết quả

Host/roster chỉ đọc tại COLLAB §0. Mục tiêu Owner giữ nguyên; bổ sung D24: bất cứ việc lớn/nhỏ đều bắt đầu bằng ⑤ khai đủ việc, hai đầu nối, điều kiện, kế hoạch, nơi ghi, người làm/kiểm/duyệt/nhận và vòng đời.

1. Đọc AGENTS → COLLAB §0 → README → MOW-TH-005@1.1-design. Không sinh luồng quản lý ngoài MOW/MOT.
2. Dùng `catalog.work_form` và `trial_contract`; ghi vào phiếu hiện hữu. Đọc phiếu thật `work/mow-mot-moit-mout/UI-REVIEW-MOW001.json#/application_D24`, không tự tạo phiếu/sổ thứ hai. Overview là bản xem được sinh lại từ phiếu nguồn.
3. MOW001 chỉ **G1 thiết kế 3 MOT**; không G2/G3. Phiếu đang CHUAN_BI, chưa cho S3. QT-CTCM-012 rà bộ câu/đáp án đúng đối tượng và phiên; xác minh nguồn vào, đích ra/nơi ghi, quyền và kế hoạch; người có quyền ghi start_confirmation đúng phiên mới bắt đầu.
4. ⑤ gọi ①/G1; ① gọi ④ kiểm UI. Kế hoạch phải có ca kết nối nhận đầu vào và trả đầu ra, không chỉ kiểm từng màn riêng. Người làm/kiểm ghi kết quả, căn cứ, hiệu lực và việc tiếp trong phiếu. Tự kiểm không nhận thành kiểm độc lập.
5. Thiếu quy trình/đầu vào/nơi ghi/quyền → ② giữ hồ sơ, ③ sửa quy trình khi cần. Không có lỗi thì issue_ref=null; luôn có issue_register_ref chỉ nơi ghi. Không tự tạo lỗi giả, tự nghĩ bước thay quy trình hay coi hướng dẫn thiếu là quyền làm tiếp.
6. ③ sửa xong phải thử → duyệt → công bố phiên → kiểm nơi dùng → ngừng hướng dẫn cũ. Mỗi nơi bị ảnh hưởng có kiểm lại. Giữ lịch sử kết quả cũ, chỉ phần mất hiệu lực cần kiểm lại.
7. G1 xong khi thiết kế/phiếu/ca/bằng chứng đạt, Owner duyệt đúng phạm vi và xác nhận nhận. Chưa PG không chặn thiết kế, nhưng không báo production đã chạy. Kết thúc báo DOER_CONFIRM cùng phiếu thật.

Lượt D24 hoàn thiện khuôn/phiếu/kiểm khai báo; chưa sửa UI sản phẩm hoặc thực hiện ca người/AI mới. Chưa MOW002, chưa T2.5, chưa thay công thức, chưa PG. Năm chốt máy TQT-ISS-007 vẫn mở.

<details><summary>Lịch sử giao việc trước D23 · không dùng để cấp/chặn quyền hiện hành</summary>

**D22/P21 — HIỆN HÀNH:** Owner giao lại Astra Codex làm Host; rà và sửa tính nhất quán Overview, 005 và MOW/MOT. Chỉ đạo Host GPT Chat/D19 phía dưới đã hết hiệu lực. 005 vẫn là đề xuất, không READY/RUN; mọi bước chọn/thực hiện/kiểm/bàn giao phải thuộc MOW/MOT, dùng cùng phiếu/hồ sơ đúng phạm vi và phiên. Đọc `catalog.consistency_review` và README; chưa áp thử quy trình trước khi chỉ rõ MOT/hợp đồng/nơi nhận còn thiếu. TQT-ISS-004/007 tiếp tục mở.

# PROMPT — Tools quy trình · Làm theo quy trình ra đúng sản phẩm

**D21/P19 — HIỆN HÀNH:** chú giải duy nhất `catalog.records[].guide` / `catalog.normal_processes[].guide`, 4 trường ngắn. `MOW-TH-005` mới là **ĐỀ XUẤT 0.1-draft** để sở hữu 6 bước; **CẤM coi READY/RUN, chưa quyết Chuỗi/PG**. Không sửa lại công thức/Master ngoài scope từ bản nháp, không tự nhảy sang MOW002. `CHUNG.APQUYTRINH` vẫn chỉ cổng trước khi chạy; `QT-CTCM-012` chỉ xử lý câu hỏi.

**Host hiện hành (D19, 09/10/2026): GPT Chat; Astra Codex chỉ còn là Host lịch sử D17.** Lượt này chỉ trình bày Over view, không READY/RUN sửa kỹ thuật; các phần prompt cũ bên dưới là hồ sơ việc có sẵn, không tự động được phép chạy.

## Đọc đích trước khi làm
Mục tiêu chuẩn và tiêu chí hoàn thành ở [COLLAB.md §0, ô 1–2](COLLAB.md); trạng thái hiện tại ở Bảng điều khiển cùng file. Giữ nguyên 15 ý Owner, đọc cả phần “Làm rõ mục tiêu” ngày 09/10: phải có quy trình khép kín, đủ câu hỏi/đáp án và bằng chứng làm theo ra đúng sản phẩm. Ma trận, UI và mô hình dữ liệu là các phần phục vụ mục tiêu này. Chi tiết dưới đây là cách thực hiện và lịch sử; không thay tiêu chí nghiệm thu.

## Hiện hành · Master tổng hợp · 09/10/2026
Đọc danh mục `tqt-composite-processes.catalog`: 4 Quy trình tổng hợp đang thiết kế (`MOW-TH-001…004`) + 1 đề xuất chưa duyệt (`MOW-TH-005`) trong Master `ML-MOW-TH-001`; 9 Tool + 3 quy trình bổ sung (12 thành phần). Bản đề xuất chưa được Owner duyệt không được READY/RUN. Đọc review_07 và checkpoint_policy. Tham chiếu quy trình bằng code/version, nguồn đọc tách resource; không quay lại danh mục kiểm kê vòng6 để kết luận chưa có mã. Giữ nguyên mục tiêu đang chờ Owner/Claude chốt. Phần tiếp tục về 5 chốt thực thi bên dưới vẫn còn hiệu lực.

## Tiếp tục rà 5 chốt vòng 6 · 09/10/2026
Đi theo đường vào đầu README. Đọc danh mục quy trình, `host_review_06` và TQT-ISS-007. 87 ca đạt vẫn còn 5 chốt sai được tái hiện; gói NOT_FROZEN.
Thứ tự tiếp tục: đúng đối tượng/tập câu bắt buộc → hợp đồng kết quả con–cha → kết thúc đúng đường đi và ACK cuối → quyền theo thời điểm → kiểm PG qua DOT đúng quyền. Mỗi chốt phải có ca đúng và ca sai; không sửa bằng số câu cố định hoặc buộc mọi nhánh đi cả sáu bước.
Kiểm kê mã hiện có không tự cấp mã Master. Ý ghép câu hỏi vào quy trình là đề xuất của Owner đang rà, chưa đổi công thức, tầng hay tạo MOW cho từng nhóm. Mọi sửa nguồn do Host, AI khác chỉ proposal. Chưa MOW002, chưa RUN PG. Các mục dưới là lịch sử và phạm vi nguồn.

## Mô hình có mã · lượt trước · Owner bổ sung hướng PG 09/10/2026
Đọc README mục Mô hình và JSON view.html#tqt-process-model; dùng check-process-model.py để kiểm/xuất gói SQL nháp. Dữ liệu MOW/MOT có phiên, lần/vòng/việc chạy, call và event riêng. Phiếu bắt buộc có cả MOW/MOT đang làm lẫn đối tượng/ nghiệp vụ; không đổi Field thành MOW. Chưa tăng số câu. Bản DRAFT/SIM không là đăng ký Master, không có quyền gọi/ghi PG. Tiếp theo chốt mapping Master và nơi nhận thật, rồi thử staging/concurrency/ca thật đúng quyền; đóng TQT-ISS-007 khi có bằng chứng, không đóng vì mô hình chạy qua kiểm.

## Rà khép kín · Owner tiếp tục 09/10/2026
Đọc README mục Khép kín và view.html#tqt-khep-kin. TQT-TH-001 chưa đăng ký Master MOW; không coi mã tài liệu là mã đối tượng. Kế tiếp: chốt quan hệ MOW gọi con, ánh xạ Nhóm cha/con rồi đăng ký đúng Master; áp thử đường thiếu Field tới khi xử lý và kiểm lại nơi gọi. Câu hỏi tại ma trận, hồ sơ mở TQT-ISS-007 tại cùng nguồn, không tạo nguồn song song. T2.5/Master riêng/vòng đời ứng viên mới chỉ đề xuất. Không tự chạy PG, thay công thức hoặc phát RUN từ bản thiết kế này.

## Quy trình tổng hợp · Owner giao trực tiếp 09/10/2026
Bắt đầu từ `view.html#list-quy-trinh-tong-hop`, TQT-TH-001. Nguồn điều phối: JSON `tqt-composite-processes`, gồm giai đoạn, bước, quy trình con, đầu ra, checkpoint và đường quay lại. Chọn phần đang làm, đọc nguồn con và bộ câu hỏi/ghi chú; lưu kết quả ở phiếu sản phẩm/sổ đã có. Không tự coi khung mới đã qua áp thử, không phát PG hoặc vận hành chỉ vì đã có hướng dẫn. Trình Owner bản tóm tắt nguyên nhân và quyết định cần chốt, không chuyển toàn bộ log.

## Phạm vi bộ câu hỏi · Owner giao trực tiếp 08/10/2026
Host: **Astra Codex**, phiên Owner chỉ định. Làm UI Câu hỏi cơ bản theo Công thức, ma trận câu hỏi là SSOT và bộ ghép nghiệp vụ UI/Test/Config. Giữ nội dung cũ; không thay định nghĩa Công thức hay dựng UI thứ 2. Mục tiêu nguyên văn: COLLAB.md §0 ô 1 bổ sung 08/10. Cách sửa nguồn và nộp góp ý: README.md.
Nguồn mới: `view.html#tqt-question-matrix`; bảng cho người và AI: `view.html#ma-tran-cau-hoi`. Bộ câu hỏi đang hiệu chỉnh, chưa nghiệm thu. Chỉ Host nhập ý kiến đã xem xét; thành viên khác chỉ đề xuất riêng.
Kiểm giao diện và liên kết thật sau đồng bộ; không lấy UI chạy được để tuyên bố bộ câu hỏi đã đủ.
Tiếp theo: thử MOW-NHC-001 với bộ câu hỏi áp dụng và quy tắc `rules` trong cùng JSON. Bàn giao câu trả lời theo mã/phạm vi, nguồn/phiên bản, bằng chứng hoặc chỗ thiếu; đối chiếu Nhóm cha/con, MOW/MOT và chỗ bàn giao. Chỉ ra căn cứ suy ra trường/nút/trạng thái UI, nguồn cần sửa, đề xuất tách bước nếu thật sự cần. Kết quả thử phải có DOER_CONFIRM đúng phạm vi; chưa có kết quả thì không nhận đã đủ. Không làm MOW 002.

## Kết quả áp dụng 09/10/2026
Đã rà lại MOW001: đọc `UI-REVIEW-MOW001.json` của task sản phẩm, mục `process_trial_20261009` trước khi vẽ/sửa tiếp. Hợp đồng A/B/C và đáp án tại đó là căn cứ thiết kế; phụ thuộc runtime giữ mở. Khi ghép phải đọc cả `notes`/`note_policy` và tham chiếu Config trong cùng JSON câu hỏi. Không tự tăng câu hỏi chung hoặc thêm Bước con để lấp lỗi triển khai.

## Hồ sơ yêu cầu trước — đã được chỉ đạo trên thay thế, giữ để truy nguồn
Các giới hạn READ-ONLY/Host GPT Chat trong phần lưu vết dưới đây không phải lệnh hiện hành cho Host mới.

STATUS: **DRAFT · READ-ONLY REVIEW REQUEST · CHƯA READY/RUN SỬA NGUỒN**
Host: GPT Chat (OpenAI-main) · Codex: người rà và đề xuất theo Owner 08/10.
PROCESS: CHUNG.APQUYTRINH — chỉ đối chiếu, chưa là lệnh RUN.
MOW001→002 UI PROMPT cũ: **SUPERSEDED TRƯỚC READY**, giữ bản cũ trong Git history; **KHÔNG vẽ MOW 001 hoặc 002 ở lượt này**.
Write zone: file đề xuất riêng `work/tools-quy-trinh/proposals/TQT-PR-20261008-codex-root-questions-01.md` nếu được phép ghi đề xuất; nếu không, trả toàn bộ nội dung dưới chat cho Host, không bypass/quét credential.
**CẤM sửa** `work/tools-quy-trinh/{COLLAB.md,README.md,view.html,PROMPT.md}`, mọi `ui/*`, file chuẩn `work/mow-mot-moit-mout/*`, bảng PG/Directus và công thức/Master chính. Không tạo task/Master/dữ liệu mới.

## 1 · Mục đích của lượt này
Owner chỉ ra: thiếu câu hỏi bắt buộc ngay trong công thức gốc, khiến lúng túng khi vẽ UI. Phải **đặt câu hỏi riêng ở gốc**, kiểm từng thành phần, rồi ghép và bổ sung bộ câu hỏi nghiệp vụ UI/Config. Nếu thêm một Bước con, nó tự có câu hỏi cần trả lời và kế thừa đúng câu hỏi gốc, không đắp vá hàng nghìn bản MOW/MOT.

**Ba nguyên liệu gốc:**
- `CT-001` **Bước** gồm **Bước lớn và Bước con** (không biến Bước con thành nguyên liệu độc lập thứ tư).
- `CT-002` **Tầng/đối tượng**: Field T0; MOIT/MOUT cùng T0.5 nhưng khác loại; MOT T1; MOW T2.
- `CT-002.1` **Chuỗi**: CTCM, VHCM, CMSXQT (SSOT mã/tên tại `ui/chuoi-data-v1.js`).

**Quy tắc ghép đang có, giữ nguyên:** CT-003 Chuỗi+Bước+Tầng⇒Nhóm cha; CT-004 Chuỗi+Bước con+Tầng⇒Nhóm con; CT-005 Chuỗi+Bước+Tầng+Nhóm cha⇒MOW; CT-005.1 Chuỗi+Nhóm con⇒MOT. Bộ câu hỏi chuyên môn (UI, Config…) chỉ thêm **SAU khi ghép**, không lẫn vào câu hỏi của nguyên liệu gốc.

## 2 · Đọc đúng nguồn, bản mới nhất
1. `AGENTS.md` → `work/tools-quy-trinh/COLLAB.md` §0/Host → `README.md` và `view.html#quy-trinh-hieu-chinh`, `#ra-ui` và 9 Tools; đọc `work/mow-mot-moit-mout/{README.md,FORMULA-AI-README.md,CHANGE-PROPAGATION.md,CHANGE-IMPACT-MAP.json}`.
2. Root `ui` READ ONLY: `definition-master-data-v1.js` CT001/002/002.1/003/004/005/005.1 và ML-DEF-001/002/004/005/021; `chuoi-data-v1.js`. Nguồn người: `work/mow-mot-moit-mout/ban-duyet.html#formula-root-1` (dùng nguồn formula nếu portal đăng nhập chặn). Ghi path/phiên bản thực tế; không đoán source từ chat.
3. Baseline cần kiểm: **9 Bước lớn; 23 Bước con B1–B7, B8/B9 chưa bóc; 5 loại Tầng; 3 Chuỗi**. Dataset CH-001 đã có 35 Nhóm cha, 115 Nhóm con, 35 MOW và MOT dẫn xuất. Đây là **số kiểm kê**, KHÔNG yêu cầu sinh tích 9×5×3 hay thêm B8/B9.
4. Một ca mẫu duy nhất: `MOW-NHC-001`, CH-001/CTCM+B1 Tìm+T0 Field+NHC-001 với Bước con 1.1 Tìm thường, 1.2 Tìm nâng cao, 1.3 Xác nhận phù hợp; 3 MOT từ 3 Nhóm con. **MOW 002 chưa làm**.

## 3 · Sản phẩm Codex phải đề xuất
**A. Rà gốc đã có/chưa có:** liệt kê nguồn định nghĩa và câu hỏi hiện hữu cho Chuỗi, Tầng, 9 Bước lớn và 23 Bước con; đánh `CÓ CÂU HỎI / CHỈ CÓ MÔ TẢ / THIẾU / KHÔNG ÁP DỤNG` kèm bằng chứng. B8/B9 thiếu Bước con không có nghĩa phải tự bổ sung. Chỉ ra câu chuyên môn UI/Config đang đặt nhầm tầng nếu có.

**B. Xây bộ câu hỏi tối thiểu và giao diện câu trả lời:** Mỗi câu có `Q_ID | LEVEL_OWNER (CHUOI/TANG/BUOC/BUOC_CON/CHUYEN_MON) | CÂU HỎI | ĐẦU VÀO/NGUỒN TRẢ LỜI | BẮT BUỘC hay N-A có lý do | CÁCH KIỂM | XONG KHI | ISSUE_REF`. Không hỏi trùng: câu ở cấp cha được con kế thừa bằng ID, không chép lại.

Nhóm câu khởi đầu để Codex rà, **chưa được Owner chốt**:
- Chuỗi: mục đích, đầu ra của tiến trình, giới hạn trách nhiệm.
- Tầng: đối tượng nào, Master/bằng chứng tồn tại, quan hệ và các ràng buộc chung theo loại.
- Bước lớn: một nhiệm vụ gì, vào/ra, nhánh kết quả, khi nào thực sự kết thúc, việc gì thuộc Bước khác.
- Bước con: hành động nguyên tử, ai/máy làm, đầu vào, kết quả ra, lỗi/quay lại, bằng chứng, khi nào xem là xong. Vẽ một UI hay tái sử dụng UI là câu hỏi bổ sung **sau khi ghép**, không ép 1 Bước con = 1 mã UI mới.
- Nghiệp vụ **thiết kế UI**: nêu bộ câu hỏi design trước khi vẽ, dùng lại UI cha; phân biệt với **8 câu rà/kiểm UI** hiện có. Nghiệp vụ **Config**: tái sử dụng **7 câu Config** hiện có, đề xuất delta, không ép mọi câu vào mọi bước.

**C. Định nghĩa phép ghép:** với một tổ hợp hợp lệ, dẫn chiếu đúng câu hỏi của Chuỗi, Tầng, Bước lớn, Bước con, sau đó ghép bộ câu hỏi UI hoặc Config. `MISSING` câu bắt buộc → `BLOCKED` có mã; `CONFLICT` hai lớp → chỉ đúng nguồn để quyết; `N-A` có lý do. Cấm sao chép full bộ câu hỏi trên từng dòng MOW/MOT. Định nghĩa rõ khi nào thiếu **Bước con thực sự** (nhiệm vụ mới, có vào/ra và điều kiện xong riêng), khi nào chỉ cần **thêm câu hỏi/nhánh**.

**D. Thử ghép MOW001 trên giấy, không tạo UI:** lập `Q_ID gốc → câu kế thừa → trả lời hiện hành → câu UI/Config thêm → bằng chứng/thiếu ở đâu` cho ba MOT. Không đổi CT-001.
- B1 **Tìm chỉ tìm ra/chưa tìm ra/chưa đủ căn cứ**, không thực thi B2 Dùng, không tạo Field, không biến điểm JEV thành giấy phép dùng.
- Với 1.1/1.2/1.3, xử lý mẫu hai vòng: vector tìm + JEV dựa dữ liệu được cấp; Xanh/Vàng/Đỏ và điều kiện dừng; Vàng có thể sửa yêu cầu/tìm lại; chưa có JEV thật thì ghi GAP OPEN-04, không bịa số liệu.
- Chứng minh câu hỏi nào đủ để xác định trạng thái/hiển thị UI, câu nào còn thiếu Config; điều kiện nào buộc bổ sung hỏi gốc thay vì vá UI ngọn.

**E. Đề xuất vị trí canonical + lan truyền:** mỗi delta `SOURCE_GỐC (CT001/002/002.1) → downstream CT003/004/005/005.1 → Master Nhóm/MOW/MOT → UI/Tools/test → phép kiểm/rollback`. Nếu cần bộ câu hỏi thành Master List, ưu tiên dùng lại Master đã có trước, không tự tạo mới. Việc sửa CT/ML canonical thuộc quyền Host của task MOW/Owner theo quy định, **không mặc nhiên do Codex được ghi**.

## 4 · Nghiệm thu bài ĐỀ XUẤT này
- Một khuôn Q_ID dùng được ở **3 nguyên liệu gốc / 4 cấp đọc**.
- Có kiểm kê 9 Bước lớn, 23 Bước con thực, 5 loại Tầng, 3 Chuỗi theo nguồn; kết quả ngắn gọn, không đòi tự điền tích chéo hàng nghìn tổ hợp.
- Thử ghép riêng MOW001 chứng minh phát hiện thừa/thiếu/xung đột; hai bộ câu hỏi chuyên môn UI và Config **không trùng gốc**.
- Mỗi điều cần sửa ghi đúng SOURCE, câu/bước, bằng chứng và impact; trường hợp chỉ là nhánh thì **không tạo Bước con**.
- Chính Codex ghi `DOER_CONFIRM=YES/NO/PARTIAL`: đọc nguồn có tổ chức được bộ câu hỏi và thử ghép không? Thiếu đầu vào nào vẫn BLOCKED?
- KQ đưa Host: `A. TÓM TẮT | B. BỘ CÂU HỎI GỐC | C. QUY TẮC GHÉP | D. THỬ MOW001 | E. DELTA + DOER_CONFIRM + FILE PROPOSAL`.
- Khi đủ, Host rà bằng chứng, trao đổi Reviewer khác hãng và Owner quyết các thay đổi nghĩa gốc; **chỉ sau đó** cập nhật root/propagation rồi mới phát RUN vẽ MOW001. Không tự xem đề xuất này đã có hiệu lực.

</details>


### Tiếp tục sau P32 · 12/10
Đọc README P32 + catalog.host_review_PR15. Owner chốt VPS đang dùng là SSOT, GitHub cũ không dùng để triển khai gateway. Cửa ghi đã ENFORCED cho một tệp kho thử, 10 ca quyền thật/gate đã đạt; chi tiết và hash ở Master DOT CHECK004.runtime_binding. Dùng CHECK006 --verify --vps-ui để chạy lại đủ bộ, không mở DOT/Master mới. Không suy quyền tệp thành 34 endpoint đã đạt. Còn: phân quyền phiên Host, người kiểm độc lập, hoàn thiện các bản ghi đến hạn và đi đường MOW001 thật. Giữ 0/7, không PG. Khi sửa schema/engine phải nâng bộ ghim triển khai có kiểm, không cho worker tự thay validator.
