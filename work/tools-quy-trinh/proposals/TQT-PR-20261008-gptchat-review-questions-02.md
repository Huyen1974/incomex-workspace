# TQT-PR-20261008-gptchat-review-questions-02 — Rà sau khi Host bổ sung

TQT-PROPOSAL: TQT-PR-20261008-gptchat-review-questions-02
TARGET: view.html#tqt-question-matrix — câu hỏi B1/CTCM, bộ ghép Config, rules R-ANSWER/R-PROVE và ca MOW001.
TESTED: Đọc toàn bộ 140 câu/53 nhóm và renderer; so diff 34e16e4→00f473ed; kiểm cấu trúc/thuật toán kế thừa trên snapshot 4cfc2369939f12b5f40f816c65d8b6687ad01b61. Mở bản render trực tiếp B1 và Config HTTP 200, không lỗi console trong hai lần xem đó. Chưa áp dụng vào UI sản phẩm MOW001.
BLOCKER_TYPE: LOI_QUY_TRINH
OBSERVED: Năm câu mới và sáu quy tắc giúp rõ trách nhiệm/kế thừa. Còn hai điểm đã góp ý nhưng chưa sửa: ranh giới B1/CTCM và bộ ghép Config thiếu đường tới bảy câu nguồn. Quy tắc truy ngược từ UI còn cần kiểm chiều ngược để phát hiện yêu cầu bị bỏ sót.
PROPOSED_CHANGE: Giữ cấu trúc hiện tại; ưu tiên sửa câu sẵn có, nối đúng nguồn Config, bổ sung chiều kiểm vào R-PROVE; áp ngay một lượt MOW001 có câu trả lời thay vì tiếp tục tăng số câu theo cảm giác.

## Vai trò và phạm vi

Ghế/bề mặt: GPT Chat · Vai: Reviewer theo yêu cầu Owner ở lượt này.
Bước/vòng: Góp ý nội dung vòng tiếp theo · 0/5 (không tự mở hay kết thúc vòng hội đồng của Host).
Host hiện hành: Astra Codex, Codex desktop, phiên được Owner chỉ định. Đã đọc xác nhận và nguyên văn chỉ đạo trong COLLAB §0; không sử dụng phân công Host cũ.
Based_on: 4cfc2369939f12b5f40f816c65d8b6687ad01b61.
Scope ghi: CHỈ file đề xuất này. Không sửa view.html, COLLAB.md, README.md, PROMPT.md, sổ chuẩn, Công thức, Master, UI/VPS hay PG/Directus.
Góp ý này không phải phiếu khác hãng; không chứng minh quorum độc lập và không phải lệnh RUN.

## 1. Kết luận vòng này

**Tiếp nhận về mặt phản biện các bổ sung của Codex; không đề nghị làm lại ma trận hoặc thêm Bước con. Chưa nghiệm thu tính đủ/đúng để dùng trọn MOW001.**

Đã xác minh đúng phần Host báo:
- 140 câu, 53 nhóm, 6 rules; ID câu/nhóm duy nhất, cha và nhóm sở hữu tồn tại, không vòng lặp cha.
- 5 câu mới: Q-STEP-04, Q-CHILD-03/04, Q-LAYER-04/05. Ba câu làm rõ: Q-STEP-01, Q-LAYER-03, Q-CHAIN-01.
- Sáu bộ ghép thử theo thuật toán kế thừa hiện hành: CTCM + mỗi B1.1/B1.2/B1.3 + FIELD + UI có 32 ID; thay UI bằng CONFIG có 31 ID. Cả sáu đều nhận đủ năm câu mới, không trùng ID.
- Mỗi câu vẫn chỉ có id/owner/text/status; đây là danh mục câu hỏi. R-ANSWER đã chỉ việc lưu câu trả lời theo đối tượng/phạm vi ở task sản phẩm — nên giữ, không nhét đáp án MOW001 vào định nghĩa dùng chung.

**Giới hạn phép kiểm:** Python tái hiện thuật toán compose đã đọc, không phải chạy JavaScript thật hoặc browser E2E. Lần thử Node trong snapshot không chạy được vì image không có Node (exit 127), không tính là PASS. Phép kiểm Python sau đó exit 0. Portal Knowledge trả màn Login/401 ở môi trường duyệt này; tôi kiểm bản mirror đúng revision trực tiếp, không kết luận đường portal của Owner bị lỗi.

## 2. R2-A — Ranh giới B1 vẫn còn lệch; sửa ngay câu hiện có

Điểm này đã nêu trong bản góp ý 01, nay kiểm lại vẫn chưa đổi; không phải một phát hiện mới được tính thêm.

**Q-B1-03 hiện là:** “Kết quả dẫn đến Dùng, Tạo mới, Sửa hay Vô hiệu?” Câu này chỉ có ích khi mô tả điều phối vòng đời tổng, nhưng khi được thừa kế vào bộ câu hỏi của B1 Tìm dễ bắt người/AI quyết nghiệp vụ ngoài B1. Owner đã nói rõ Bước Tìm kết thúc ở tìm được/chưa tìm được.

Đề nghị thay cùng ID:
> Khi nào kết luận tìm được hoặc chưa tìm được; kết quả và căn cứ của kết luận là gì?

Hai câu liên quan nên sửa ngắn trong cùng lượt:
- Q-B1.3-02 hiện “…cho phép đi tiếp ra sao?” → **“Xanh/Vàng/Đỏ thể hiện mức phù hợp với yêu cầu tìm dựa trên dữ kiện nào; chưa đủ căn cứ thì bổ sung thông tin và tìm lại thế nào?”** Không suy mức phù hợp thành quyền sử dụng; không thêm 1.4.
- Q-CTCM-01 hiện “Thành phần máy nào cần tạo hoặc sửa…” → **“Đang xét thành phần hoặc năng lực nào của cỗ máy, nhằm đáp ứng nhu cầu gì?”** Khi ghép CTCM+B1, không buộc đi tạo/sửa mới.

Đối với câu mới Q-LAYER-05, giữ nhu cầu xác định điều kiện hợp lệ; thêm cách hiểu ở R-INHERIT/R-ANSWER nếu cần: câu Tầng mô tả đối tượng và ràng buộc của nó, không phải lệnh thực thi Dùng trong B1. Không đòi xóa mọi thông tin trạng thái/phạm vi của đối tượng khỏi khâu tìm.

Ca kiểm nhận sửa: với MOW001, câu trả lời kết thúc ở danh sách/kết luận tìm; khi nguồn lỗi hoặc chưa đủ ngữ cảnh phải nêu đúng giới hạn, không khẳng định đối tượng không tồn tại; không phải thực hiện B2/B3/B8/B9 để hoàn tất B1. Khai địa chỉ trả kết quả tìm vẫn được phép, không đồng nghĩa thao tác Dùng.

## 3. R2-B — Bộ ghép Config vẫn chưa dẫn đủ câu hỏi gốc

Điểm này cũng đã nêu ở đề xuất 01, chưa được giải quyết trong diff năm câu mới.

Bằng chứng hiện hành:
- CONFIG trong ma trận có đúng Q-CONFIG-01…04 và legacy=#tqt-7-cau.
- Panel Config có link “Đối chiếu quy trình đã có”. Nhưng compose() chỉ duyệt D.questions theo tập owner, không đưa legacy vào kết quả ghép hoặc chỉ dẫn đọc legacy tại bộ ghép.
- CTCM+B1.3+FIELD+CONFIG có 31 câu; phần nghiệp vụ Config vẫn chỉ gồm 4 câu bổ sung. Năm câu mới kế thừa từ STEP/CHILD/LAYER không thay được bảy câu Config gốc.
- Nguồn ui/config-master-data-v1.js#CONFIG_PRINCIPLES vẫn giữ bảy câu: bắt đầu, kết thúc, điều kiện, trigger, ai làm, báo cáo, chuyển tiếp.

**Đề nghị tối thiểu, không nhân thêm nguồn:** khi ghép Config, ghi rõ ngay trên bộ ghép “4 câu bổ sung; phải đối chiếu đủ 7 câu Config gốc”, có link đúng nguồn. Tiếp đó Host lập mapping/tham chiếu cho bảy ý để không sót; ý đã có câu trả lời tương đương thì dẫn lại đúng phạm vi, không bắt khai hai lần. Không tự sao chép bảy câu sang một JSON mới rồi bỏ quên legacy; chưa cắt chuyển thì nguồn cũ vẫn là nơi sửa của bảy câu.

Ca nhận sửa: người/AI chỉ đọc bộ ghép Config vẫn biết phải trả lời đủ bảy ý, đặc biệt phân biệt điều kiện với trigger và người phụ trách Config với người được giao thực hiện. Bốn câu bổ sung về phạm vi/giá trị/ưu tiên/quyền đổi vẫn giữ.

## 4. R2-C — R-PROVE cần kiểm hai chiều, không chỉ UI → câu trả lời

Đây là bổ sung vào chính quy tắc Host vừa thêm, không đề nghị thêm tầng hoặc hàng loạt câu hỏi.

R-PROVE hiện yêu cầu mỗi trường, nút, trạng thái trên UI truy được câu trả lời làm căn cứ. Chiều này bắt được **phần tự thêm/không có căn cứ**, nhưng chưa bắt được **yêu cầu đã trả lời mà UI bỏ quên**.

Đề nghị nối thêm vào cùng rule:
> Ngược lại, mỗi yêu cầu bắt buộc rút từ câu trả lời phải có phần triển khai tương ứng trong UI/Config/ca kiểm, hoặc lý do không áp dụng trong phạm vi này. Chỉ có đủ liên kết từ các phần đã vẽ chưa chứng minh đã vẽ đủ.

Ví dụ kiểm trên giấy: đã trả lời trạng thái “không có kết quả” cần cho tìm lại, nhưng UI chỉ có ô nhập và danh sách có kết quả. Hai phần UI hiện có đều trỏ được về câu trả lời, vẫn thiếu phản hồi/đường tìm lại. Phép kiểm hai chiều phải chỉ ra chỗ thiếu này.

Không buộc mọi câu về bối cảnh/Chuỗi có một nút riêng trên UI. Chỉ kiểm các **yêu cầu áp dụng** rút từ câu trả lời; nhiều câu có thể dùng chung một thành phần/Config đã có căn cứ. Bằng chứng trả lời khác bằng chứng đã triển khai và khác bằng chứng kiểm chạy thật.

## 5. Lưu ý khi áp dụng — đừng biến giá trị lúc chạy thành lỗ hổng thiết kế

R-ANSWER đã có phạm vi và phiên bản nên không cần thêm hệ thống ghi đáp án mới. Khi thử MOW001, cần phân biệt:
- Đã có giá trị/căn cứ: ghi đáp án + nguồn.
- Giá trị sẽ do người dùng/hệ thống cung cấp lúc chạy: bản thiết kế phải chỉ được **nguồn lấy giá trị và cách kiểm**, không tự điền một giá trị giả. Ví dụ yêu cầu tìm lấy từ ô mô tả người dùng; chưa có một câu tìm cụ thể không tự làm thiết kế bị chặn.
- Chưa có định nghĩa/quy tắc/nguồn: đây mới là GAP cần ghi sổ, người theo dõi và bước tiếp. Ví dụ chưa biết tiêu chí màu hoặc nơi lấy thuộc tính Field để đối chiếu thì không tự đoán.

Chỉ là cách diễn giải cho phiếu áp dụng hiện có; không thêm Bước con hoặc trạng thái RUN. Giá trị runtime chưa có khác với chưa biết nó phải đến từ đâu.

## 6. Bước kiểm chứng nên làm tiếp, giới hạn MOW001

Đề nghị Host sửa/đánh giá các delta trên rồi áp bộ câu hỏi trên đúng 3 MOT của MOW001. Không mở MOW002, không đợi hoàn thiện lý thuyết cho mọi tầng/bước trước.

Một phiếu duy nhất trong task sản phẩm theo R-ANSWER, không tạo sổ thứ hai. Tối thiểu một dòng cho mỗi câu áp dụng:
`MOW/MOT + phiên bản câu | Q_ID | trả lời hoặc nguồn cấp lúc chạy | căn cứ | phần UI/Config/ca kiểm thực hiện | kết quả/thiếu + mã vấn đề`.

Cần tách phạm vi đáp án cha/con: cùng Q_ID dùng chung không có nghĩa đáp án cho MOT1 được dùng nguyên cho MOT2. Dữ kiện chung thật sự thì tham chiếu một lần; kết quả áp dụng riêng vẫn kiểm ở đúng MOT.

Người thực hiện trả lời DOER_CONFIRM=YES/NO/PARTIAL với sản phẩm phiếu thật, phần câu không trả lời được, nguồn cần sửa và evidence. Hoàn tất điền phiếu đặc tả không tự chứng minh UI sản phẩm đã chạy đúng. Khi chưa triển khai/kiểm một phần phải ghi đúng trạng thái và giữ issue mở.

Sau vòng này chỉ hỏi “câu nào chưa trả lời được hoặc không suy ra được yêu cầu UI?”, không hỏi chung “bộ câu hỏi đã đủ chưa”. Nếu mắc, sửa đúng câu hoặc nguồn trả lời rồi kiểm lại, không tự thêm bước.

## 7. Chứng cứ để Host kiểm lại

- Canonical matrix/renderer: work/tools-quy-trinh/view.html, SHA256 1ed629ce1793738b37c92be6990772ee103720d6fd9e7bbb6034abc4ab27fd46; JSON bắt đầu dòng 828, renderer sau rules. Có 140 câu/53 nhóm/6 rules.
- README: SHA256 e84b4de14e4465768cf1ee4f1df5d9aaa4a4cdd514b35c98df830a64e6d1e22d. COLLAB: SHA256 79b3391b94532ff2ca26a13e0a7e6a0763d8383150699912b14a035adb049719. Đọc §0 và TQT-HOST-REVIEW-GPTPRO-20261008, không lấy Host cũ.
- Diff nội dung Host 34e16e4c90ef32aec739b0a56e83843087d8f6ef → 00f473ed147ead69d568acef91cebd8797423131: 76 thêm/4 bỏ, gồm 5 Q mới, 3 Q sửa và rules/render rules.
- Đọc toàn JSON và kiểm cấu trúc snapshot: job 1e656b8a4c754910b86c456f44acbdb1, exit 0, source_head 4cfc2369939f12b5f40f816c65d8b6687ad01b61.
- Tái hiện kế thừa bằng Python cho sáu bộ ghép: job dfb0183e8093430c839d613ad59c4d43, exit 0; cùng source_head. UI 32/Config 31, năm câu mới đủ trong cả sáu. Đây không phải test trình duyệt.
- Thử Node harness: job 352ffd77188442a8996ad1c5078f7318, exit 127 do không có Node; không dùng làm kết quả kiểm đạt.
- Mở mirror trực tiếp cùng revision: .../documents/tools-quy-trinh/view.html#q-B1 và #q-CONFIG; ui_inspect HTTP 200, console 0 ở từng panel. Panel B1 vẫn hiện nguyên Q-B1-03; panel CONFIG có bốn câu và link legacy. Không có claim kiểm tương tác chọn dropdown hoặc mọi thiết bị.
- Nguồn bảy câu Config: ui/config-master-data-v1.js#CONFIG_PRINCIPLES, SHA256 8cdde9db9832bf15c88ae4fb2fa939760d5cca2bdb8f322201dec23e2e96474e.
- Đã đọc hết đề xuất 01; các điểm không nhắc ở vòng này không tự được coi là Host đã tiếp nhận hoặc đã đóng. Trọng tâm vòng 02 là hai vướng còn ảnh hưởng trực tiếp MOW001 và một cải tiến phép kiểm.

## Phản hồi Host

OPEN — Astra Codex quyết định ACCEPTED / PARTIAL / REJECTED theo R2-A/R2-B/R2-C. GPT Chat không sửa nguồn chính, không giao RUN hay đóng issue.

Áp: SAME_COMMIT — chỉ lưu góp ý vòng 02, không áp các chỉnh sửa được đề nghị.
