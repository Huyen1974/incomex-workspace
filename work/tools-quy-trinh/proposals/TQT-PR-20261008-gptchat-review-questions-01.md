# TQT-PR-20261008-gptchat-review-questions-01 — Rà bộ câu hỏi bản đầu

TQT-PROPOSAL: TQT-PR-20261008-gptchat-review-questions-01
TARGET: work/tools-quy-trinh/view.html#tqt-question-matrix — 135 câu / 53 nhóm; các bộ ghép và câu hỏi kế thừa.
TESTED: GPT Chat đọc toàn bộ JSON câu hỏi và phần renderer liên quan; kiểm tĩnh trên snapshot e50ba7e503e92d23f9fbeaf111e1c56db6dbfb92, exit 0. Không chạy nghiệp vụ thực tế.
BLOCKER_TYPE: LOI_QUY_TRINH
OBSERVED: Cấu trúc một nguồn và kế thừa đúng hướng; một số câu còn kéo sai phạm vi B1, lẫn chiều lắp ráp với luồng dữ liệu, lẫn câu thiết kế với câu kiểm, và Config ghép chưa mang theo 7 câu gốc.
PROPOSED_CHANGE: Sửa đúng các mã dưới đây; ưu tiên thay chữ và dùng lại câu trả lời, chỉ thêm câu chung còn thiếu. Không thêm Bước con hay sửa công thức trong đề xuất này.

## P-REVIEW · OPEN — chờ Astra Codex xem xét
Ghế/bề mặt: GPT Chat · Vai: Reviewer do Owner giao trực tiếp ở lượt này.
Bước/vòng: Rà nội dung câu hỏi bản đầu · 0/5 (góp ý theo yêu cầu Owner; không tự mở hoặc chốt vòng hội đồng).
Host hiện hành: Astra Codex — Codex desktop, phiên Owner chỉ định. Người quyết định tiếp nhận/chỉnh/bỏ là Host, không phải người viết bản góp ý.
Based_on: e50ba7e503e92d23f9fbeaf111e1c56db6dbfb92.
Scope đọc: AGENTS A0/A2/A3/A4; COLLAB §0 và chỉ đạo Owner mới; README; toàn bộ script tqt-question-matrix và phần renderer common/detail/compose; các nguồn đối chiếu được liệt kê bên dưới.
Scope ghi: CHỈ file đề xuất này trong proposals/. Không sửa COLLAB.md, README.md, PROMPT.md, view.html, sổ chuẩn, công thức, Master hay runtime.
Lưu ý vai trò: Owner nói rõ GPT Chat không còn Host và chỉ Codex sửa file chính. Góp ý này không đại diện phiếu khác hãng, không chứng minh quorum độc lập theo AGENTS.

## 1. Kết luận và bằng chứng

**Đề nghị giữ cấu trúc hiện tại, hiệu chỉnh một số câu trước khi dùng để nghiệm thu. Không làm lại từ đầu.** Chuyên môn = Bước/Tầng/Chuỗi; nghiệp vụ = UI/Test/Config/NTGV. Bước con thuộc Bước, không là nguyên liệu gốc thứ tư.

Kiểm tĩnh thật trên snapshot, job `09df38b08fb14e9ca71ee344cc6da9bf`, exit 0:
- 53 nhóm, 135 câu; ID nhóm/câu không trùng; mọi owner và parent đều tồn tại.
- Phân bố câu: chung 11; Bước lớn 27; Bước con 46; Tầng 25 (15 câu T0–T2 + 10 câu bối cảnh T3–T7); Chuỗi 9; nghiệp vụ 17.
- Ghép CTCM + B1.2 + FIELD + UI: 27 câu, đúng 27 ID khác nhau; kế thừa B1 và STEP có mặt.
- Ghép CTCM + B1.3 + FIELD + CONFIG: 26 câu; phần CONFIG chỉ có Q-CONFIG-01…04. Hàm compose không đọc 7 câu legacy.
- Mỗi câu mới hiện có đúng `id, owner, text, status`. Chưa có dữ liệu trả lời/áp dụng trong ma trận — phù hợp một danh mục câu hỏi; không được suy danh mục đã đủ thành một lần áp dụng thành công.

Điểm nên GIỮ: một JSON sinh nhiều cách xem; mã câu ổn định; Bước con kế thừa câu cha; không tự sinh con B8/B9; T3–T7 để riêng bối cảnh; dữ liệu cũ không bị xóa; toàn bộ câu mới còn draft.

Giới hạn: kiểm trên không phải browser E2E, không xác nhận hình thức UI và không phải một lượt người mới thực hiện ra sản phẩm. Chưa rà toàn bộ nội dung legacy/9 Tools; chỉ đối chiếu bộ 8/7 câu và nguồn công thức cần thiết. Mọi sửa chữ bên dưới đều là ĐỀ XUẤT, chưa áp dụng.

### Nguồn đã đối chiếu
- Ma trận: `work/tools-quy-trinh/view.html`, SHA256 `a3af3045dc98c009bf340f984d87edecc83bd7a975bdca3403e2db45bb5cf062`, từ dòng 827; renderer bắt đầu sau JSON. Nội dung này là SSOT câu hỏi mới theo README, không phải bản sao cần loại bỏ.
- `work/tools-quy-trinh/README.md`, SHA256 `02f5ed46c2ae192b84493c9dc0fdd3668b03ffa96ab889b995ff879470bcd2d6`.
- `work/tools-quy-trinh/COLLAB.md`, SHA256 `deeb68856f2f6a097a5d6577c33cf7cc6183ae59e845b26ecff017312d178837`; §0 xác nhận Astra Codex làm Host và chỉ đạo Owner về ma trận.
- Root ui `definition-master-data-v1.js`, SHA256 `93eae888106544e7905751a15cc72b360971f3d8bda437887bfbf3f5c07b044c`: CT-001-N1-3, CT-001-N6-3, CT-002. CT-002 nói rõ chiều lắp ráp, không phải chiều luồng dữ liệu. CT-001-N6-3 đang quy định FAIL → 5.3; nếu cần → 5.1/5.2 → Test lại.
- Root ui `config-master-data-v1.js`, SHA256 `8cdde9db9832bf15c88ae4fb2fa939760d5cca2bdb8f322201dec23e2e96474e`, CONFIG_PRINCIPLES: 7 câu về bắt đầu, kết thúc, điều kiện, trigger, ai làm, báo cáo, chuyển tiếp.
- Owner đã làm rõ ngay trong trao đổi: B1 chỉ tìm được/chưa tìm được rồi kết thúc; không thực thi Dùng. Vòng bổ sung ngữ cảnh là tìm lại, chưa có quyết định thêm 1.4.

## 2. Quy tắc đọc bản góp ý

`GIỮ` = chưa thấy cần đổi ở vòng này, không đồng nghĩa đã nghiệm thu đủ. `SỬA` = thay chữ ở đúng ID hiện có. `BỔ SUNG` = Host cân nhắc cấp mã, người góp ý không tự cấp mã canonical. Những câu trong cùng nhóm không được nhắc sửa mặc định đề nghị giữ.

Không xóa mã/lịch sử để giảm số câu. Hai câu có ý gần nhau chưa chắc trùng: câu cha có thể hỏi quy tắc, câu con hỏi kết quả áp dụng. Chỉ nên bỏ việc trả lời lặp nếu thực sự cùng một dữ kiện; tham chiếu câu trả lời gốc thay vì chép lại.

## 3. Câu chung — sửa ít, dùng được cho nhiều nhóm

| Mã/nhóm | Nhận xét | Câu đề nghị / xử lý |
|---|---|---|
| Q-STEP-01 | Chỉ hỏi kết quả, chưa buộc làm rõ phần ngoài phạm vi; đây là nguồn dễ lẫn Tìm với Dùng. | SỬA: **“Bước này chỉ cần đạt kết quả gì; việc gì không thuộc bước này?”** |
| Q-STEP-02/03 | Đã hỏi đầu vào/trách nhiệm và bằng chứng kết thúc. | GIỮ. Đánh giá ở cấp Bước lớn; không tự dùng câu trả lời đó để chứng nhận mọi Bước con đã xong. |
| Q-CHILD-01 | “Giao gì cho bước tiếp theo” mặc định luôn có bước tiếp, chưa bao quát trả kết quả hoặc kết thúc. | SỬA: **“Bước con nhận gì từ đâu; trả kết quả gì, cho đâu hoặc kết thúc tại đâu?”** |
| Q-CHILD-02 | Có câu xử lý thiếu/sai. | GIỮ; câu trả lời cần chỉ đúng nguồn xử lý, không mặc định hỏi Owner. |
| CHILD · thiếu câu chung | Hiện hai câu chung chỉ nói nhận/giao và lỗi; chưa hỏi trực tiếp hành động và điều kiện xong riêng của Bước con. | BỔ SUNG hai câu ngắn, đặt một lần ở CHILD: **“Người hay máy thực hiện hành động gì ở bước con này?”** và **“Bước con này xong khi nào, kiểm bằng gì?”** Không chép thành 46 câu riêng. |
| Q-LAYER-01/02 | Phạm vi đối tượng và nguồn/mã/dùng lại phù hợp. | GIỮ. |
| Q-LAYER-03 | “Nhận gì từ tầng dưới/cung cấp gì cho tầng trên” dễ biến chiều lắp ráp thành chiều dữ liệu; Field không có tầng dưới trong lát này, T3–T7 lại là bối cảnh. | SỬA: **“Đối tượng gồm những thành phần nào và được ghép vào đâu; phần nào không áp dụng?”** Luồng nhận/giao cụ thể giữ ở MOIT/MOUT/MOT. |
| Q-CHAIN-01/03 | Mục đích/đối tượng phục vụ, trách nhiệm và kiểm kết quả phù hợp. | GIỮ như thông tin cấp Chuỗi; không bắt mỗi MOT khai lại cả Chuỗi. |
| Q-CHAIN-02 | “Chuyển sang chuỗi khác” dễ làm người làm hiểu Chuỗi là các trạng thái nối tiếp bắt buộc. | SỬA: **“Phạm vi và dấu mốc bắt đầu/kết thúc của Chuỗi này là gì?”** Chỉ khai giao tiếp Chuỗi khác nếu thực tế có, không ép thành bước tiếp. |

## 4. Bước lớn — rà đủ B1 đến B9

| Nhóm | Đề nghị |
|---|---|
| **B1 · Tìm** | Q-B1-01/02 giữ. **Thay Q-B1-03** “Kết quả dẫn đến Dùng, Tạo mới, Sửa hay Vô hiệu?” bằng **“Khi nào kết luận tìm được hoặc chưa tìm được; kết luận kèm kết quả và căn cứ gì?”** Bỏ yêu cầu chọn/thực hiện nghiệp vụ khác khỏi câu này. BỔ SUNG một câu chung B1: **“Không có kết quả do chưa tìm thấy, chưa đủ dữ kiện hay lỗi/giới hạn nguồn; phân biệt bằng gì?”** Không tìm ra không tự chứng minh đối tượng không tồn tại. |
| **B2 · Dùng** | Giữ 3 câu: đúng đối tượng/phiên bản/phạm vi; người xác nhận/nơi dùng; bằng chứng áp dụng. Đây là nơi hỏi quyền và tác động sử dụng, không dồn ngược về B1. |
| **B3 · Đề xuất tạo mới** | Q-B3-01 đang mặc định “thứ đã có”. SỬA: **“Chưa có đối tượng phù hợp hay đối tượng hiện có chưa đáp ứng; bằng chứng tra cứu nào dẫn tới đề xuất tạo mới?”** Giữ Q-B3-02/03. Không cần tạo thêm nhóm nghiệp vụ cho trường hợp chưa tồn tại. |
| **B4 · Duyệt đề xuất tạo** | Giữ 3 câu. Không gộp với B7: B4 duyệt đề xuất trước tạo; B7 duyệt cho dùng sau kiểm. Giảm khai lại cùng tiêu chí/người duyệt ở B4.1, xem mục Bước con. |
| **B5 · Khai báo** | Q-B5-01/02 giữ. Q-B5-03 nên bao quát sai/mâu thuẫn chứ không chỉ trống: **“Thông tin đã đủ, hợp lệ và nhất quán để chuyển Test chưa; còn thiếu/sai gì?”** |
| **B6 · Test** | Q-B6-01/02 giữ. Q-B6-03 SỬA: **“Ca nào PASS, FAIL, chưa kiểm hoặc bị chặn; bằng chứng và đầu mối xử lý ở đâu?”** Không ép chưa chạy/bị chặn thành FAIL hoặc PASS. Đây là trạng thái phép kiểm, không thêm trạng thái RUN. |
| **B7 · Duyệt cho dùng** | Giữ 3 câu; cần đọc cùng B7.1 để kiểm bằng chứng đúng phiên bản, không dùng PASS cũ cho bản đã thay đổi. Không coi có người phê duyệt là tự có bằng chứng triển khai tới mọi nơi dùng. |
| **B8 · Sửa** | Q-B8-01 SỬA nhẹ: **“Sửa nguồn gốc nào, vì sao, ảnh hưởng những nơi kế thừa nào?”** Giữ 02/03. Không tự bóc thêm Bước con khi Owner chưa yêu cầu. |
| **B9 · Vô hiệu/Nghỉ hưu** | Giữ 01/03. Q-B9-02 nên nói rõ giữ lịch sử: **“Việc đang chạy, dữ liệu/lịch sử cũ và đường thay thế được xử lý thế nào?”** Không mặc định vô hiệu là xóa. Không tự thêm bước con. |

## 5. Bước con — đủ 23 nhóm, không bổ sung 1.4

Các câu chung CHILD đề nghị bổ sung ở mục 3 áp dụng một lần cho toàn bộ bảng này. Dưới đây chỉ là phần khác biệt thực sự của từng nhóm.

| Nhóm (2 câu riêng/nhóm) | Giữ / sửa / giảm lặp |
|---|---|
| **1.1 Tìm thường** | Giữ Q-B1.1-01. Q-B1.1-02 làm rõ **“Kết quả được xếp và giải thích mức phù hợp theo yêu cầu tìm và dữ kiện nào?”** Không đồng nhất độ tương tự từ khóa với đủ điều kiện sử dụng. |
| **1.2 Tìm nâng cao** | Q-B1.2-01 SỬA: **“Còn thiếu ngữ cảnh hay điều kiện tìm nào; bổ sung rồi tìm lại thế nào?”** Giữ 02 về thu hẹp/bỏ lọc. Vòng tìm lại không đòi sinh Bước con mới. |
| **1.3 Xác nhận phù hợp** | Q-B1.3-01 giữ. Q-B1.3-02 SỬA: **“Mức phù hợp Xanh/Vàng/Đỏ dựa vào dữ kiện nào; chưa đủ căn cứ thì làm rõ hoặc tìm lại thế nào?”** Bỏ “cho phép đi tiếp” nếu bị hiểu thành cấp phép Dùng. Q-B1-03 đã lo kết thúc B1. |
| **2.1 Người chọn Dùng** | Giữ 01; 02 cần tham chiếu phiên bản/phạm vi đã xác định ở Q-B2-01, chỉ hỏi xác nhận có đúng dữ kiện đó không. Không buộc người làm khai cùng giá trị hai lần. |
| **2.2 Máy áp dụng & xác nhận** | Giữ cả hai, đặc biệt thất bại/bấm lại. Không chuyển chức năng này sang 1.3. |
| **3.1 Ghi nhận ý tưởng** | Giữ cả hai. Câu lưu bản và tránh trùng có ích, không bỏ để rút ngắn hình thức. |
| **3.2 Chuẩn hóa đề xuất** | Giữ ý 01 nhưng làm thành kiểm áp dụng: **“Đề xuất này còn chỗ nào chưa đáp ứng mục tiêu, phạm vi, kết quả đã nêu?”** Dùng lại đáp án Q-B3-02. Giữ 02 về điểm cần làm rõ. |
| **3.3 Cập nhật Master** | Giữ cả hai: bản ghi đúng và căn cứ đổi trạng thái. Không tự coi điền đủ là đã chuẩn hóa. |
| **3.4 Giao phụ trách** | Giữ cả hai: người nhận + đủ thông tin + bằng chứng đã nhận. |
| **4.1 Ra quyết định** | Q-B4.1-01 đề nghị hỏi kết quả áp dụng **“Hồ sơ này đáp ứng/chưa đáp ứng tiêu chí nào; ai có thẩm quyền quyết định?”** Tiêu chí/nhóm người duyệt được tham chiếu từ Q-B4-01/02. Giữ 02 quyết định + lý do. |
| **4.2 Cập nhật Master** | Giữ cả hai; truy vết quyết định không trùng với thao tác quyết định. |
| **4.3 Báo người đề xuất** | Giữ cả hai: nơi nhận đúng công việc và người nhận hiểu việc tiếp theo. |
| **4.4 Chuyển bước** | Giữ cả hai: nhánh theo quyết định và tránh chuyển sai/lặp. |
| **5.1 Khai báo chung** | Giữ cả hai, có phiên bản chuẩn và dùng lại dữ liệu. |
| **5.2 Khai báo riêng** | Giữ cả hai: phần bổ sung và kiểm mâu thuẫn/trùng với phần chung. |
| **5.3 Rà phần còn thiếu** | Q-B5.3-01 SỬA: **“So với yêu cầu và ràng buộc, còn thiếu, sai hoặc mâu thuẫn gì?”** Đối chiếu chứ không chép lại câu Q-B5-03. Giữ 02 về nơi sửa chung/riêng. |
| **6.1 Test theo khai báo** | Q-B6.1-01 SỬA: **“Mỗi điều khai báo liên hệ yêu cầu nào và được kiểm bằng ca nào?”** Giữ 02. Tránh chỉ lấy chính điều vừa khai để tự kết luận điều đó đúng. |
| **6.2 PASS** | Giữ cả hai; ghi PASS chỉ khi mọi ca bắt buộc đạt, không suy từ một vài ca mẫu. |
| **6.3 FAIL** | Giữ cả hai. Đã đối chiếu công thức gốc thực sự quy định FAIL → 5.3 → 5.1/5.2 khi cần; KHÔNG tự sửa câu này thành đường khác chỉ vì mong tổng quát hơn. Ca chưa kiểm/bị chặn xử lý ở câu B6, không giả làm lỗi khai báo. |
| **7.1 Đóng gói báo cáo** | Q-B7.1-01 SỬA: **“Báo cáo đúng phiên bản đang xét và bằng chứng Test còn hiệu lực không?”** Giữ 02 về phần đạt/hạn chế. |
| **7.2 Giao người duyệt** | Giữ cả hai; kiểm đúng người và mở được hồ sơ là hai việc khác nhau. |
| **7.3 Người phê duyệt** | Giữ 01. Q-B7.3-02 SỬA nhẹ: **“Lý do, điều kiện kèm theo và cách xử lý khi chưa được duyệt được ghi ở đâu?”** Chưa thêm Bước con mới. |
| **7.4 Cập nhật Master & hiệu lực** | Giữ cả hai: bản ghi hiệu lực và nơi dùng đã nhận đúng bản không phải cùng một phép kiểm. |

## 6. Tầng — giữ sự khác nhau giữa đối tượng đang xét và công việc đang thực hiện

Cần một lời dẫn chung: **câu thuộc Tầng mô tả đối tượng được xét, không phải lệnh thực thi đối tượng đó.** Ví dụ đang Tìm một MOW vẫn được hỏi nó gồm MOT gì để đánh giá sự phù hợp, nhưng không được chạy MOW ấy chỉ để trả lời câu hỏi.

| Nhóm | Đề nghị |
|---|---|
| **FIELD · T0** | Giữ 01/02. Q-FIELD-03 bổ sung phần hay bị bỏ sót: **“Khi nào bắt buộc; rỗng, chưa có giá trị và giới hạn hợp lệ được hiểu/kiểm thế nào?”** Không ép mọi Field có đơn vị hay miền số; N-A có lý do. |
| **MOIT · T0.5** | Q-MOIT-01 SỬA nhẹ: **“Bộ đầu vào gồm những Field nào, ánh xạ từ nguồn nào?”** Giữ 02/03. Cần mapping nguồn thực, không chỉ danh sách tên Field. |
| **MOUT · T0.5** | Giữ cả ba. Đầu ra khác đầu vào, không nhập chung thành một nhóm vì cùng T0.5. |
| **MOT · T1** | Giữ cả ba: kết quả/người thực hiện, MOIT/MOUT, điều kiện đầu–cuối/thực hiện lại. Không xóa vì có chữ giống STEP: một bên hỏi đối tượng MOT, một bên hỏi hành động đang làm. |
| **MOW · T2** | Giữ 01/03. Q-MOW-02 SỬA: **“Thứ tự, nhánh và điều kiện nối MOT là gì; MOUT bước trước khớp MOIT bước sau ra sao?”** Từng MOT đúng riêng vẫn chưa chứng minh ghép đúng. |
| **T3 Chuyên môn** | Giữ 2 câu về phạm vi và chuẩn chung/riêng. Dùng nhãn đầy đủ T3, tránh lẫn từ “chuyên môn” mới của Owner dùng cho bộ câu hỏi Bước/Tầng/Chuỗi. |
| **T4 Phòng ban** | Giữ 2 câu về trách nhiệm và giao nhận giữa chuyên môn. |
| **T5 Khối** | Giữ 2 câu về phối hợp và quy tắc/giao thoa. |
| **T6 Công ty** | Giữ 2 câu về chuẩn chung và phân quyền. |
| **T7 Lĩnh vực** | Giữ 2 câu về trong/ngoài phạm vi và chuẩn dùng chung. |

T3–T7 tiếp tục là bối cảnh thu gọn. Trong lượt MOW001 không bắt điền mọi câu T3–T7 hoặc coi chúng là vật liệu bắt buộc ghép CT-003/004. Bộ chọn hiện cho chọn từng T3–T7; nên hiển thị rõ “bối cảnh”, không đổi công thức.

## 7. Chuỗi — bỏ giả định mọi bước trong Chuỗi đều đang tạo/sửa

| Nhóm | Đề nghị |
|---|---|
| **CTCM** | Q-CTCM-01 đang hỏi “Thành phần máy nào cần tạo hoặc sửa…”, nhưng khi ghép với B1 việc hiện tại chỉ Tìm. SỬA: **“Đang xét thành phần hoặc năng lực nào của cỗ máy, nhằm đáp ứng nhu cầu gì?”** Q-CTCM-02 giữ ở cấp định hướng tái sử dụng, không biến thành lệnh tạo bổ sung. Q-CTCM-03 nên là **“Đầu ra chế tạo cần bàn giao cho nơi sử dụng nào, kèm giới hạn gì?”**, không mặc định mọi kết quả chỉ giao sang Chuỗi VHCM. |
| **VHCM** | Giữ 01/02. Q-VHCM-03 thêm điều kiện: **“Nếu có sự cố, xử lý trong vận hành hay chuyển về chế tạo theo tiêu chí nào?”** Không bắt một lượt vận hành bình thường phải có sự cố mới được kết thúc. |
| **CMSXQT** | Giữ 3 câu. Q-CMSXQT-03 đã hỏi ai thử và bằng chứng đúng sản phẩm; không thêm bản chép câu đó vào mọi nghiệp vụ. Không mở quy trình phái cử/tuyển dụng ngoài phạm vi Owner hiện giao. |

## 8. Nghiệp vụ — UI, Test, Config, nguyên tắc giao việc

### 8.1. Thiết kế UI
- **Q-UI-02/03: GIỮ** — chọn nguồn cha, phần chung/riêng; phần máy điền và phần người thực sự nhập.
- **Q-UI-01: SỬA** thành “Màn hình cần giúp người dùng hiểu việc gì và nhận biết kết quả gì?” để dùng được trước khi có UI, không chỉ hỏi đã nhìn thấy UI tốt chưa.
- **Q-UI-04: SỬA** thành “Cần thể hiện những trạng thái nào: chưa nhập, đang xử lý, có/không có kết quả, chưa đủ căn cứ, lỗi?” Hiện câu chưa tách không kết quả với lỗi và chưa đủ căn cứ. Dùng nhánh gốc làm nguồn, không tự invent thêm Bước con.
- **Q-UI-05: SỬA** thành “Mỗi thao tác dự kiến nhận gì, trả/gửi gì, đến đâu; khi chưa có nơi nhận thì thể hiện thế nào?” Đây là đặc tả trước vẽ. Việc bấm thật đối chiếu kết quả chuyển cho TEST, không khai lại thành hai bộ nghĩa khác nhau.
- **BỔ SUNG một câu UI dùng chung:** “Trên màn hẹp và khi dùng bàn phím, thông tin/hành động chính được bố trí để dùng được thế nào?” Không cần một chuỗi câu mới về từng pixel; vẫn tham chiếu UI cha hiện hành.

### 8.2. Test / rà UI
- **Q-TEST-01/04: GIỮ** — Given/When/Then và bằng chứng/phiên bản/tái hiện.
- **Q-TEST-02: GIỮ lõi**, khi áp cho UI đối chiếu thêm các trạng thái và yêu cầu màn hẹp/bàn phím/mẫu cha đã đặc tả ở nhóm UI. Không viết bộ yêu cầu thứ hai trong Test rồi hợp thức hóa UI sai.
- **Q-TEST-03: SỬA** “không cần giải thích ngoài UI” thành **“Người hoặc AI mới chỉ dùng những nguồn đã được chỉ định cho vai đó có làm ra đúng sản phẩm, không cần hỏi thêm không?”** Người dùng cuối chỉ có UI/Help khác agent được yêu cầu đọc README/quy trình. Câu cũ dễ coi việc đọc README bắt buộc là phép thử thất bại.
- Chưa chạy hoặc bị chặn phải báo riêng; không coi số câu đủ, số màu xanh hay exit của kiểm schema là bằng chứng chức năng đã đúng.

### 8.3. Config — ưu tiên sửa cách ghép hơn viết thêm tùy hứng
**Bốn câu Q-CONFIG-01…04 hiện hợp lý như câu bổ sung**, nhưng chưa thay được bảy câu Config đã chốt: bắt đầu / kết thúc / điều kiện / trigger / ai làm / báo cáo / chuyển tiếp.

Chứng cứ cụ thể: nhóm CONFIG có legacy `#tqt-7-cau`; detail có link mở legacy, nhưng `compose()` chỉ lấy D.questions của các owner. Do đó chọn CTCM+B1.3+FIELD+CONFIG cho 26 câu, trong đó đúng 4 câu Config, không mang theo 7 câu gốc. Đây là thiếu phạm vi nội dung bộ ghép, không phải lỗi trùng ID.

Đề nghị Host:
1. **Giữ bốn câu bổ sung**, nối tham chiếu tới 7 câu gốc khi chọn Config, vẫn giữ một nguồn sửa hiện hành cho 7 câu. Không chép sang một bộ mới rồi bỏ quên legacy.
2. Trong lúc chưa nối được, ghi ngay tại kết quả ghép: **“4 câu bổ sung; còn phải trả lời 7 câu Config gốc ở …”**. Link trong panel nhóm riêng không thay cho chỉ dẫn ở bộ ghép.
3. Q-CONFIG-02 hỏi mặc định nhưng không được bịa mặc định khi chưa chốt; cho phép ghi “chưa có quyết định” + mã sổ. Q-CONFIG-03 giữ xử lý ưu tiên; trường hợp không rule khớp/nhiều rule mâu thuẫn cần câu trả lời, không lặng lẽ chọn rule đầu.

### 8.4. Nguyên tắc giao việc
- Giữ Q-NTGV-02/03/04: trigger/gói bàn giao, quyền/thời hạn/nhận việc, không nhận/quá hạn/không làm được.
- Q-NTGV-01 SỬA nhẹ: **“Dựa tiêu chí nào để chọn người/vai trò/AI; nếu nhiều bên cùng khớp thì ưu tiên ra sao?”** Câu 04 xử lý trường hợp không nhận; không cần tạo thêm bước giao việc mới.
- Đừng trộn người có quyền sửa Config với người được giao thực hiện; Q-CONFIG-04 và Q-NTGV-03 không phải hai câu trùng để bỏ.

## 9. Ghép và rút gọn — bốn điểm cần thống nhất

### G1. Kế thừa câu không đồng nghĩa dùng cùng câu trả lời
27 mã khác nhau không chứng minh 27 nội dung không trùng. Cần ghi rõ **câu cha = quy tắc/phạm vi; câu con = cách áp dụng/bằng chứng của công việc con**. Khi dữ kiện thật sự giống nhau thì dẫn lại đáp án gốc, không yêu cầu người/AI khai lần hai.

Các cặp nên rà để giảm lặp: Q-B4-02 ↔ Q-B4.1-01; Q-B2-01 ↔ Q-B2.1-02; Q-B3-02 ↔ Q-B3.2-01; Q-B5-03 ↔ Q-B5.3-01. Ngược lại không gộp kiểm danh mục đã cập nhật với nơi sử dụng đã nhận bản mới, không gộp MOIT với MOUT, không gộp B4 với B7.

### G2. Một mẫu ghi câu trả lời theo lần áp dụng, không làm nặng màn gốc
Giữ danh mục câu hỏi ngắn. Chỉ cần chỉ dẫn một dòng cho phiếu áp dụng:
`Q_ID | đối tượng/bước đang xét | trả lời hoặc CHƯA CÓ/N-A+lý do | nguồn/bằng chứng | mã vấn đề nếu còn thiếu`.

Câu trả lời của MOW001 nằm ở phiếu của lượt áp dụng, KHÔNG nhét vào câu gốc để mọi MOW khác kế thừa nhầm. Chưa cần dựng một UI trả lời hoặc PG table mới trong vòng này. Thiếu chưa sửa ngay thì Host ghi/ghép vào sổ hiện có; Reviewer chỉ nộp đề xuất này.

### G3. Nhìn thấy bộ ghép chưa đồng nghĩa được phép thực hiện
Renderer hiện nói rõ đây là preview và bao nhiêu thành phần đã chọn — nên giữ. Khi áp dụng thật cần đủ thành phần theo ngữ cảnh, nguồn đúng, câu bắt buộc đã trả lời hoặc có lý do N-A, mọi mâu thuẫn có đầu mối; phần chưa đủ không được nhận ĐẠT. Không cần biến preview thành một máy tự phê duyệt mới.

### G4. Rà tính khớp của đầu ra/đầu vào sau khi từng phần đúng
Q-MOW-02 đề nghị sửa ở mục 6 đảm nhiệm việc này. Thử tối thiểu một trường hợp từng MOT có câu trả lời nhưng MOUT/MOIT giữa hai MOT không khớp: hệ thống/người rà phải chỉ được điểm ghép sai. Không giải bằng thêm hàng loạt câu hỏi giống nhau ở từng cấp.

## 10. Đề nghị thứ tự Host xem xét

**Ưu tiên trước lượt áp dụng MOW001:** ranh giới B1/Q-B1.3, giả định tạo/sửa ở Q-CTCM-01, chiều ghép ở Q-LAYER-03, hai câu chung CHILD, và cách bộ ghép Config dẫn đủ 7 câu cũ. Các điểm này có thể làm AI hiểu sai việc dù UI hiển thị đúng.

**Tiếp theo, sửa chữ trong cùng vòng nếu thuận tiện:** tách design/test, giảm trả lời lặp cha/con, kiểm mapping MOUT→MOIT và trạng thái chưa kiểm/bị chặn. T3–T7, CMSXQT, B8/B9 giữ bộ đầu để hiệu chỉnh theo ca thật, không mở rộng ngay.

Đề nghị ít nhất bốn phép thử sau khi Host nhận sửa:
- CTCM+B1.3+FIELD+UI: người thực hiện xác nhận chỉ thực hiện Tìm; không bị câu hỏi bắt Dùng/Tạo/Sửa; phân biệt chưa tìm thấy với lỗi nguồn, có vòng bổ sung ngữ cảnh; không thêm 1.4.
- CTCM+B1.3+FIELD+CONFIG: nhìn bộ ghép biết 4 câu bổ sung và đủ đường tới 7 câu gốc; điều kiện khác trigger; không tự nhập default thiếu căn cứ.
- B4.1: hỏi quy tắc cha một lần, câu con dùng lại rồi kiểm hồ sơ cụ thể; không trả lời trùng vì khác ID.
- B6/TEST: chưa kiểm/bị chặn không mang PASS/FAIL giả; một phiên AI mới đọc đúng tài liệu và bàn giao được phiếu áp dụng cùng DOER_CONFIRM.

## Phản hồi Host

Chưa có. Astra Codex quyết ACCEPTED / PARTIAL / REJECTED theo từng mục. Reviewer không tự cập nhật nguồn chuẩn, không tự mở thêm task/sổ và không phát READY/RUN.

Áp: SAME_COMMIT (chỉ áp việc lưu đề xuất; không phải áp các sửa đổi được đề nghị).
