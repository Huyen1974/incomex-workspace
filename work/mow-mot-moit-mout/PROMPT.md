# PROMPT — MMIM.2 · Thu thập và tổ chức information · DRAFT CHỜ CLAUDE REVIEW

## 0. Lệnh và phạm vi
Owner đã giao việc này ngày 2026-09-20. Đây là lượt THU THẬP / TỔ CHỨC TÀI LIỆU, không phải lượt sửa sản phẩm.

Trước khi làm:
1. **Executor_Surface = Codex.**
2. Chọn **Write_Path theo capability đã audit, không theo hãng**: ưu tiên `workspace_*`; nếu chính phiên Codex không bind `workspace_*` nhưng bind `fs_*` đã audit thì dùng `fs_*`. Cấm dùng Git/CLI/native/API để ghi repo.
3. Gọi đúng **MỘT read-gate** của Write_Path đã chọn để đọc `work/mow-mot-moit-mout/COLLAB.md` (`workspace_read` hoặc `fs_read` tương ứng). Ghi `WRITE_PATH=<workspace_*|fs_*>` vào báo cáo. Gate fail → DỪNG ngay trước khảo sát/mutation và nêu tool đã thử.
4. Đọc `AGENTS.md` → README §0/D12 → `work/mow-mot-moit-mout/COLLAB.md` (đặc biệt §0) → toàn bộ prompt này.
5. Kiểm tra `READY@<SHA>` trong COLLAB bằng **commit cuối chạm `PROMPT.md`**, KHÔNG so với HEAD repo. Nếu không khớp: DỪNG.

Nguồn trên Mac, ưu tiên đúng path Owner giao:
`/Users/nmhuyen/Desktop/quy trình`

Nếu lookup fail do Unicode/path: resolve thư mục cùng tên dưới `/Users/nmhuyen/Desktop` trước; sau đó mới thử Documents/Google Drive cục bộ. Nếu có >1 candidate, đối chiếu sổ chỉ đường/marker/SHA đã biết; không chọn chỉ vì trùng tên. Ghi path thực dùng vào README.

Đích duy nhất của lượt MMIM.2:
`work/mow-mot-moit-mout/information/`

File gốc/HTML chính — CẤM SỬA trong lượt này:
`work/mow-mot-moit-mout/mow-mot-moit-mout.html`

Bản HTML trên repo là bản làm việc chuẩn của việc này. Các bản cùng/ gần tên trên Mac chỉ đọc để đối chiếu, không được chép đè lên repo.

## 1. Mục tiêu
Khảo sát toàn bộ `/Users/nmhuyen/Desktop/quy trình` để tìm các file thực sự liên quan tới hồ sơ MOW · MOT · MOIT · MOUT và file HTML chính hiện hành. Các tài liệu FIELD/UI liên quan trực tiếp được đưa vào cùng phạm vi nguồn của lượt thu thập, nhưng MMIM.2 không tự thay đổi mục tiêu nghiệp vụ đã xác nhận ở COLLAB §0.

Tự đề xuất cấu trúc dễ hiểu trong `information/`, rồi COPY các **tài liệu text/lightweight thực sự cần thiết** vào đó. Binary/ảnh KHÔNG đưa vào Git trong MMIM.2; chỉ kiểm kê đủ để bước shared-assets sau có thể publish một lần và mọi AI đọc bằng URL HTTPS. Mục tiêu của `information/` là: AI hoặc người mới vào việc có thể biết đâu là phụ thuộc trực tiếp, nguồn nghiệp vụ/thiết kế, tham khảo và legacy — mà không phải mò lại toàn bộ Desktop.

## 2. Trình tự khảo sát và nguyên tắc chọn file
Trước khi tự phân loại, nếu còn tồn tại thì đọc các sổ chỉ đường:
- `00-DOC-TRUOC.md`
- `KHO/00-CANH-BAO-DOC-TRUOC.txt`
- `KHO/00-NHAT-KY-DON-DEP.txt`

Kế thừa các nhãn “cũ/hết hiệu lực/không dùng” đã có căn cứ; không phân loại lại từ đầu chỉ dựa vào tên file.

Rà theo bốn lớp:

**A · Phụ thuộc trực tiếp của HTML chính**
- Quét các tham chiếu file tương đối từ `src`, `href`, manifest/fetch/import và metadata. Bỏ qua URL `http(s)`, fragment `#...`, `javascript:`, `mailto:` và `data:`.
- Bộ ảnh hiện hành đang dùng tiền tố thư mục Unicode dạng NFD. Trong MMIM.2: **KHÔNG copy ảnh/binary vào Git, KHÔNG base64, KHÔNG cố tái tạo tên thư mục NFD và KHÔNG sửa HTML**.
- Với từng ảnh/binary liên quan, chỉ đọc metadata từ Mac và tính: `image_id/path nguồn · extension/MIME · bytes · SHA-256 · old_src`. Nếu `image-manifest.json` là text nhỏ thì copy nó vào `information/` như tài liệu nguồn; không coi việc không đưa ảnh vào Git là thiếu phụ thuộc.
- Tạo file text `information/assets-manifest.json`. Mỗi asset tối thiểu có: `asset_id`, `source_mac`, `old_src`, `bytes`, `sha256`, `ext`, `publish_name_ascii`, `shared_url`, `state`. `publish_name_ascii` dùng ASCII ổn định, ưu tiên `<asset_id>-<sha12>.<ext>`; `shared_url=null`, `state="PENDING_SHARED_PUBLISH"` trong MMIM.2.
- README bắt buộc có `LINK-MAP`: địa chỉ tương đối cũ trong HTML → nguồn Mac → SHA/bytes → `publish_name_ascii` → `SHARED_ASSET_PENDING` hoặc `MISSING`. Đây là đầu vào cho bước shared-assets/MMIM.3 sau; Codex không vá HTML và không tự publish binary trong MMIM.2.

**B · Nguồn được HTML chính nêu đích danh**
- HTML/MD/JSON/JS/CSS/ảnh/tài liệu mà nội dung/comment/metadata file chính dẫn tới.
- Đặc biệt rà các nguồn thiết kế/quy trình như `00-NGUON-THIET-KE.html`, `cấu trúc hệ thống.html`, `BAN-DO-BUOC-UI-AGENT.html`, `TAO-MOT-QUY-TRINH.html` và các file tương tự thực sự được dẫn.
- Nếu HTML ghi sẵn SHA cho một nguồn thì tính SHA file Mac và ghi MATCH/MISMATCH; không tự thay nguồn để “khớp”.

**C · Tài liệu làm việc hiện hành có liên quan trực tiếp**
- file mô tả/triển khai MOW, MOT, MOIT, MOUT, FIELD, UI cha/UI con, quy trình tạo, config, ma trận, test;
- chỉ copy khi có lý do sử dụng rõ.

**D · Lịch sử / legacy / bản chép runtime**
- backup, phiên bản cũ, script cập nhật cũ, tài liệu hết hiệu lực chỉ giữ nếu cần đối chiếu;
- HTML/JS/CSS trên Mac là bản chép của các UI đang chạy tại VPS `/ui-preview/mcp-writes/` KHÔNG được xếp CURRENT. Nếu cần giữ, xếp D và ghi rõ: `MAC_COPY_ONLY · current_runtime_source = VPS root ui`.
- MMIM.2 không fetch/copy runtime VPS.

Không copy mù toàn bộ thư mục. Không lấy `.git`, `node_modules`, cache/temp, file hệ thống, file không liên quan hoặc bản sao trùng hash.

**Text lớn:** file text >100 KB KHÔNG relay toàn nội dung qua model và KHÔNG copy vào Git trong MMIM.2. Chỉ ghi metadata `kind=large_text · source_mac · bytes · sha256 · state=PENDING_LARGE_TEXT` vào `assets-manifest.json`/README để xử lý cùng external/shared-assets sau.

## 3. Cách tổ chức — Codex tự đề xuất
Codex được quyền quyết định cây bên trong `information/` sau khi khảo sát thật, với các chốt:
- ít tầng, tên dễ hiểu;
- phân biệt rõ `DIRECT-DEPENDENCY` / `CURRENT` / `REFERENCE` / `LEGACY`;
- binary/ảnh tuyệt đối không nằm trong cây Git của `information/`; chỉ manifest/link-map là text;
- file text/tài liệu nhẹ vẫn giữ tên nguồn nếu không gây lỗi; nếu cần đổi tên bản copy để tránh Unicode/path collision thì README phải có mapping nguồn → đích;
- cùng nội dung trùng hash chỉ giữ một bản và ghi mọi đường nguồn trùng.

Không tạo file tiến độ. Hai file điều khiển bắt buộc trong `information/` là:
- `README.md` — inventory/link-map/quyết định phân loại;
- `assets-manifest.json` — metadata/hash/địa chỉ của binary **và text >100 KB**, không chứa binary/base64 hay nội dung text lớn.

## 4. README bắt buộc
README tối thiểu có:
1. Cây `information/` và lý do.
2. Inventory **tài liệu text/lightweight**: nguồn Mac → đích repo → A/B/C/D → lý do → bytes → SHA-256.
3. `LINK-MAP` cho mọi tham chiếu file tương đối của HTML chính. Với binary: địa chỉ cũ → nguồn Mac → SHA/bytes → `publish_name_ascii` → `SHARED_ASSET_PENDING`/`MISSING`; với text: thêm đích repo nếu đã copy.
4. Tóm tắt `assets-manifest.json`: tổng số binary, tổng bytes, duplicate theo SHA, thiếu file nào; **không yêu cầu ảnh nằm trong Git**.
5. File đã xem nhưng không copy + lý do, dùng nhãn `OMITTED_PUBLIC_SENSITIVE`, `OUT_OF_SCOPE`, `DUPLICATE`, `MAC_RUNTIME_COPY`, `BINARY_EXTERNAL` khi phù hợp.
6. Trùng hash và bản giữ lại/asset_id chuẩn.
7. SHA đối chiếu bản HTML trên Mac nếu tìm thấy; SHA nguồn nào đã được HTML ghi sẵn.
8. Cảnh báo Unicode/đường dẫn tương đối.
9. UNKNOWN còn lại; không tự suy thành “đủ”.
10. Tổng số file text đã copy + tổng dung lượng; binary báo riêng số file/tổng bytes nhưng không commit.

README là mục lục ngắn, không phải bài thuyết minh.

## 5. Công khai và an toàn
Repo được Owner chấp nhận công khai để ưu tiên tốc độ/chất lượng, nhưng KHÔNG đưa thông tin quá nhạy cảm hoặc không cần thiết lên public repo.

Không copy:
- credential, secret, token, private key, session/cookie;
- CCCD/hộ chiếu/tài khoản ngân hàng, hồ sơ tài chính/cá nhân, địa chỉ/SĐT cá nhân khi không cần cho công việc;
- hợp đồng/tài liệu có điều khoản, giá hoặc thông tin đối tác mang tính không công khai nếu không cần thiết cho việc này;
- dữ liệu người thật có thể gây rủi ro riêng tư khi ghép nhiều trường định danh.

Tên người/tên công ty hoặc thông tin nghiệp vụ đã công khai không tự động bị loại nếu thực sự cần cho tài liệu công việc. Với xlsx/docx/pdf nghi có dữ liệu nhạy cảm, mở kiểm nội dung trước khi copy; không quyết định chỉ từ tên file.

Ngưỡng relay/copy của MMIM.2: text >100 KB/file đi `PENDING_LARGE_TEXT`; binary luôn external inventory. Không dùng ngưỡng 50/250 MB để chờ đến lúc quá muộn.

Các chốt khác:
- CẤM sửa nội dung/format/metadata/tên/vị trí `mow-mot-moit-mout.html`.
- CẤM xoá/di chuyển/đổi tên nguồn dưới `/Users/nmhuyen/Desktop/quy trình`.
- Chỉ COPY **text/tài liệu nhẹ** từ Mac sang `information/`; binary/ảnh chỉ inventory/hash, không commit Git.
- Không đụng VPS/runtime/production và không tự publish shared-assets trong MMIM.2.
- Không ghi đè file đích khác nội dung.
- Với text nhỏ đã copy: ưu tiên hash nguồn = hash đích. Nếu connector chuẩn hoá newline/BOM nhưng nội dung text tương đương, ghi `NORMALIZED_BY_TRANSPORT` + SHA nguồn/đích + loại chuẩn hoá; không retry vòng lặp. Với binary/text >100 KB: PASS của MMIM.2 = định vị + bytes/SHA + manifest/link-map, không phải đã upload.

## 6. Đúng bản và kiểm trước khi kết thúc
Bắt buộc:
- HTML chính trên repo vẫn đúng SHA-256:
  `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c`.
- Nếu thấy bản gốc Mac `quy trình/từ thực tế đã làm.html`, tính SHA và ghi vào README. Nếu khác SHA repo: KHÔNG copy đè hoặc “hòa giải”; repo vẫn là bản làm việc chuẩn, ghi divergence để Host xử lý.
- Bản cùng tên nằm trong thư mục con mà tài liệu đã đánh dấu cũ không được dùng làm current.
- Mutation **do chính Codex tạo** không được nằm ngoài:
  - `work/mow-mot-moit-mout/information/**`
  - và cập nhật trạng thái `work/mow-mot-moit-mout/COLLAB.md`.
  Thay đổi chen ngang của việc khác/HEAD repo không tự làm MMIM.2 fail; xử lý bằng version/head guard của Write_Path đã chọn.
- mỗi file text đã copy có hash nguồn = hash đích;
- `assets-manifest.json` phủ toàn bộ binary được HTML/file manifest tham chiếu; mỗi entry có source tồn tại hoặc trạng thái `MISSING` rõ ràng;
- README phản ánh file thật, không ghi “đã copy/upload” từ suy đoán.

## 7. Ghi Git, retry và báo cáo
- **Write_Path của MMIM.2 phải là một trong hai capability đã audit:** `workspace_*` (primary) hoặc `fs_*` (fallback nếu bind). Dùng transaction/write/edit của **cùng family đã qua read-gate** để tạo `information/**` và cập nhật COLLAB. Không chuyển family giữa chừng trừ khi Host phát RUN mới.
- **CẤM** `git add/commit/push`, tạo branch để lách luật, GitHub native/App/API/CLI để ghi repo. Git/CLI chỉ đọc nếu cần.
- Việc không nhập được binary/text >100 KB **không phải blocker**, vì MMIM.2 chỉ inventory chúng.
- Nếu text nhỏ cần copy nhưng Write_Path không có thao tác tạo file phù hợp: ghi `OMITTED_TOOL_LIMITATION` và tiếp tục phần độc lập; chỉ DỪNG nếu thiếu file đó làm inventory/link-map sai bản chất.
- Khi tool trả timeout/`OUTCOME_UNKNOWN`/`RECOVERY_REQUIRED`: **read-back/journal/commit trước**, dùng cùng idempotency key nếu retry được; không ghi lại mù.

Khi hoàn tất:
- ghi `information/` + cập nhật COLLAB đúng workflow repo bằng đường ghi được phép;
- MMIM.2 → `MACHINE_DONE`, ghi số file text/dung lượng + số binary/tổng bytes inventoried và `information/README.md`;
- không tự nghiệm thu nghiệp vụ, không sửa HTML chính, không sửa Owner View, không upload binary.

Thông báo cuối:
`XONG · MMIM.2 · executor=Codex · write_path=<workspace_*|fs_*> · text=<số file>/<dung lượng> · external_inventory=<số file>/<dung lượng> · main_html_sha=PASS · xem information/README.md`

Nếu không truy cập được Mac, conflict/secret không xử lý an toàn, hoặc hash HTML repo thay đổi:
`DỪNG · MMIM.2 · <lý do cụ thể>`
