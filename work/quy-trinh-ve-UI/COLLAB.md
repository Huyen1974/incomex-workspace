# COLLAB — quy-trinh-ve-UI
Tên việc: quy-trinh-ve-UI
Host: Claude Chat · Host_ID: CLAUDE-UIPROC-260924-A (phiên A tiếp tục từ chiều 24/09 theo lệnh Owner; phiên B `CLAUDE-UIPROC-260924-B` xử lý P04 xong, đã bàn giao — một Host sống tại một thời điểm) · Owner giao 24/09/2026 (GPT Chat mở việc; đổi Host theo lệnh Owner do phiên GPT không có đường ghi)

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner giao trực tiếp và bổ sung ngày 24/09/2026 trong ChatGPT.

### 1. Mục tiêu
1. Chốt được quy trình vẽ UI chuẩn, đảm bảo không bị thiếu. Liệt kê các câu hỏi chuẩn phải trả lời từng bước và phải có câu trả lời chính xác mới là hoàn thành.
2. Chốt được quy trình liệt kê hợp đồng thông tin => để tạo được danh mục hợp đồng thông tin, danh mục khai báo.
3. Chốt được tool làm việc này. Tool có thể cài thêm nếu cần (ưu tiên nguồn mở, nhẹ). Nhớ dùng Jev để tham khảo các khâu.
4. Toàn bộ quá trình này do AI và Agent thực hiện; User chỉ ra lệnh, duyệt các quyết định cần quyền Owner và xem kết quả.
5. (bổ sung 24/09) Workflow ngắn gọn, vẽ từng bước cần làm gì, con người nhìn là hiểu ngay — text quá dài không đọc được. Tôi sẽ cùng Codex vẽ thử trước xem còn yếu chỗ nào. Có dùng công cụ gì không?

### 2. Thế nào là hoàn thành
- Chốt được đủ 3 nội dung chuyên môn trên thành một quy trình có thể dùng lặp lại cho mọi UI.
- Mỗi bước UI có checklist/câu hỏi bắt buộc và điều kiện PASS rõ ràng; thiếu hoặc trả lời chưa chính xác thì chưa được coi là xong.
- Có quy trình sinh và kiểm danh mục hợp đồng thông tin/danh mục khai báo.
- Có tool/workflow được chọn sau khi so sánh; nếu cần cài thêm thì phải Owner duyệt trước.
- Quy trình đủ tự động để AI/Agent tự khảo sát → lập danh mục → thiết kế → kiểm tra → sửa; không yêu cầu User thao tác chi tiết.
- Hội đồng đã có ý kiến (24/09: GPT · Claude; Hermes khi nối xong — D07); bất đồng còn lại được đưa Owner quyết.
- Đầu `view.html` có bức tranh một màn hình; Owner + Codex vẽ thử trên FIELD qua được và chỗ yếu lộ ra đã được vá.
- Nội dung chính Owner/hội đồng đọc được trên Owner View chuẩn của VPS.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Giai đoạn hiện tại: **VẼ THỬ TRÊN FIELD** (đồng thuận phương pháp GPT+Claude xong 24/09, P05 ACCEPTED; Hermes chưa nối — D07). Owner đã chốt nơi ghi bài thử: tab Step quy trình của `work/mow-mot-moit-mout/ban-duyet.html` (24/09); không tạo file mới. Áp R1 (AGENTS A10): không cài/dựng tool mới trước bài thi FIELD. Codex được khảo sát/bấm thử UI hiện có ở K0; bảng G chỉ chặn vẽ hoặc đổi UI mới. Chưa có RUN riêng để sửa UI/runtime.
- HTML chính: `view.html` — bản đồng thuận 24/09 (Host Claude viết lại theo D06: quyết định trước → sơ đồ K0–K7 → nội dung). Bản đầu của GPT ở commit `fe1b4c054bae59e4d5e1861efcca3a09d80d4ca6`.
- Nguyên tắc Owner 24/09 (qua GPT): ba nguyên tắc D03–D05 là điều kiện bắt buộc kế thừa ở mọi nơi áp dụng quy trình; chi tiết ghi thẳng repo, Owner chỉ nắm mục tiêu ngắn gọn.
- Phải tách rõ ba lớp: (A) coverage quy trình UI; (B) hợp đồng thông tin/danh mục khai báo; (C) tool hỗ trợ. Mọi lựa chọn hữu hạn quan trọng tham khảo JEV theo A5/DROOT13/D05.
- Kế thừa MMIM (`work/mow-mot-moit-mout/`): xương S01–S08 + bản ghi phụ thuộc R3.4, 5 trạng thái UI R3.6, quản lý sau tạo R3.7, FIELD03 (15 chiều, data dictionary, master mã). FIELD là lượt áp dụng đầu = bài thi 4 lỗ đã biết + 1 kiểm hồi quy nút ✎.
- Còn mở: nơi đặt danh mục khai báo/hợp đồng khi chạy thật (hỏi Owner khi vào bài thi FIELD, DROOT16). Máy kiểm là file mới → Owner duyệt trước khi tạo.

### Vòng trước
- — Việc mới.

## Quyết định Owner
- D01 · 2026-09-24 · Toàn bộ quá trình do AI/Agent làm; User chỉ ra lệnh, duyệt quyết định cần quyền Owner và xem kết quả.
- D02 · 2026-09-24 · Nội dung đề xuất phải được đưa lên Owner View VPS để hội đồng đọc và có ý kiến; dùng đúng HTML chính `view.html`, không tạo đường xem phụ.
- D03 · 2026-09-24 · **Mã + Master List áp dụng đệ quy** (Owner nêu, GPT soạn văn bản, Owner đồng ý 24/09): mọi loại đối tượng ≥2 cá thể phải có mã và Master List; tìm master trước khi tạo; mã ≠ tên ≠ phiên bản; liên kết theo định danh; master đăng ký vào danh mục master chung. Văn bản đầy đủ + điều kiện trượt: `view.html` mục 7.1.
- D04 · 2026-09-24 · **"Người mới có làm được không?"** — mỗi quy trình qua lượt đi thử như người mới do AI khác thực hiện; chuỗi Tìm → chọn/tạo → xử lý thiếu → quay lại → lưu → tìm lại → sửa/ngừng/xoá. `view.html` mục 7.2.
- D05 · 2026-09-24 · **JEV có điểm tham khảo bắt buộc** theo một bảng chung 5 điểm; không hỏi JEV thay máy kiểm; ghi lại đầu vào/lựa chọn/result id/kết luận Host. `view.html` mục 7.3.
- D07 · 2026-09-24 · Hermes chưa kết nối nên chưa tham gia; hội đồng việc này hiện = GPT + Claude. Owner muốn thấy workflow vẽ ngắn gọn nhìn là hiểu (đã thành mục 0 `view.html`, chi tiết gập lại) và sẽ cùng Codex vẽ thử trước.
- D06 · 2026-09-24 · Owner đồng ý toàn bộ đề xuất Claude: quy trình chuẩn kế thừa MMIM, FIELD làm lượt áp dụng đầu; **Claude Chat làm Host**; Claude làm thư ký chép phản hồi Host GPT vào COLLAB; Host được sửa `view.html` kể cả bố cục (quyết định trước → sơ đồ → nội dung).

- D08 · 2026-09-24 · Owner chốt sửa tối thiểu hướng dẫn: trần 40 dòng chỉ cho kịch bản chi tiết, ma trận vẫn đủ tổ hợp; được kiểm/bấm UI hiện có từ K0 trước bảng G, bảng G chỉ chặn vẽ/đổi UI mới; nút ✎ chuyển thành kiểm hồi quy. Bài thử FIELD ghi trong tab Step quy trình của `work/mow-mot-moit-mout/ban-duyet.html`, không tạo file mới. · Áp: SAME_COMMIT.

- D09 · 2026-09-24 · Owner yêu cầu tab đầu **Workflow for User** là hình luồng có ô, mũi tên và màu, giữ đúng K0–K7 cùng ba lần Owner chạm; tab thứ hai chứa hướng dẫn chữ cho AI. Bản vẽ đầu để Owner cùng sửa, chưa là quy trình đã chốt. Không tạo file mới. · Áp: SAME_COMMIT.
- JEV tham khảo bố cục · input = brief Owner (8 khâu, 3 điểm chạm, đọc hình nhanh hơn chữ, desktop/mobile) + overview cũ nhiều chữ; options = luồng dọc / lưới 4×2 / cuộn ngang / swimlane / chưa chọn; model `typesafe/jev-1.13-20260917`; result luồng dọc 0,93, confidence 0,92; id `gen-dec-1790244619-nAXQ91ffffD0zgV2HIWO`; Host chọn luồng dọc vì mũi tên theo một hướng.

## Nội dung chính
- SSOT Owner/hội đồng: `work/quy-trinh-ve-UI/view.html` (mục 1 Owner cần quyết · 2 tiến độ · 3 D · 4 khâu K0–K7 · 5 hợp đồng 3 tầng · 6 nguồn+trạng thái kiểm · 7 ba nguyên tắc Owner · 8 nghiệm thu 4 cửa · 9 kho 34 câu · 10 ma trận · 11 18 thuộc tính theo tầng · 12 tool · 13 hội đồng).
- Link Owner View chuẩn: `https://vps.incomexsaigoncorp.vn/knowledge/modules?task=quy-trinh-ve-UI`.

## JEV
- JEV01 · GPT · `gen-dec-1790217288-56iSttNoJua2z4V7xBo7` · method/contract/tool 1.00 · REFERENCE ONLY · thiếu state/options kèm theo (D05 yêu cầu từ nay ghi kèm).
- JEV02 · Claude · `gen-dec-1790218524-d6cpWPLgEsnqORcMJkiS` · state = sự kiện thô (MMIM R3/FIELD03, Owner 23/09, registry PG, đề xuất view.html, luật repo); câu hỏi: base · contract_shape · field_identity_source · tool_ssot · acceptance · machine_check · question_scope; kết quả: kế thừa MMIM 1.00 · 3 tầng 0.99 · registry trước 0.99 · chữ+Git 1.00 · nghiệm thu 4 cửa 0.85 (conf 0.80) · máy kiểm 0.51/0.37 · mặc định-vs-từng-bước 0.52/0.38 (conf 0.27) → Host chốt hai câu chưa chắc theo ONE SSOT.
- JEV03 · GPT Reviewer · `gen-dec-1790225616-LmDobZAOO2pUeXehVOly` · model `typesafe/jev-1.13-20260917` · state = D03/D05 + 4 đề xuất P03 + ONE SSOT; lựa chọn hữu hạn: chính sách mã · trạng thái registry hiện có · kiểm người mới · mức ghi JEV. Kết quả: ID nội bộ do hệ thống kiểm soát, mã nghiệp vụ/ngoại bộ là thuộc tính riêng B=1.00 (conf 0.99); registry hiện có chỉ chốt sau kiểm cấu trúc/phạm vi B=0.99 (conf 0.98); kiểm người mới hai vòng C=1.00; lượt JEV thường chỉ result-id+kết luận B=0.75 (conf 0.67). Reviewer không nhận điểm cuối nguyên xi vì D05/Owner đã yêu cầu truy vết đầu vào+lựa chọn+nguồn+model+confidence; JEV chỉ là bằng chứng phụ.
- JEV04 · Claude Host · `gen-dec-1790226954-4DftRoFSJXIhwQJc01tA` · jev-1.13-20260917 · nguồn D03/D05 + P04@`e682cf6` + sự thật cổng JEV không lưu state · câu hỏi→lựa chọn: `id_policy`{máy sinh mọi mã · ID nội bộ hệ thống + mã nghiệp vụ là thuộc tính · thiếu} · `jev_log_line`{chỉ id+kết luận · một dòng đủ trường · khối mọi lượt · thiếu} · `question_identity`(noul: lấy số thứ tự hiển thị làm định danh có vi phạm D03) · kết quả: ID nội bộ + mã thuộc tính 1,00 (conf 1,00) · một dòng đủ trường 1,00 (0,99) · vi phạm 0,88 · Host: nhận P04 mục 1, 5, 6. Dòng này là mẫu khuôn một-dòng mới (view.html 7.3).

## Ý kiến hội đồng
- P01 · GPT Chat · ACCEPTED · Based_on `fe1b4c054bae59e4d5e1861efcca3a09d80d4ca6` · Scope `view.html` 2–8 · xương sống matrix → contract → flow → UI → kiểm; không xong vì màn hình; text/Git trước; soi nhánh thiếu → đã vào view.html mục 4, 8, 12. Áp: SAME_COMMIT.
- P02 · Claude Chat · ACCEPTED có chỉnh · Based_on `e58235cc0f985fed622ff861b4dbf8fe7b092f8d` · Áp: `02a652b` (bản đầy đủ) · C1–C3 nhận; C4 nhận có chỉnh (tách nguồn / trạng thái kiểm); C5 nhận theo nhóm điểm chạm; Q1–Q3 nhận; Q4/Q6 nhận có chỉnh ("theo nghĩa" là tiêu chí phát hiện, khoá là mã; trùng tên xét theo phạm vi; máy kiểm bắt mã trùng + tham chiếu treo + câu bắt buộc chưa trả lời); Q5 nhận hướng chữ/Git, view.html vẫn là tài liệu chính; Q7–Q8 nhận (5 lỗi FIELD là điều kiện cần); sửa ví dụ: "bắt buộc nhập" thuộc tầng gắn, thay đổi mất tương thích đi qua phiên bản + nơi dùng.
- HR01 · Host GPT trả lời P02 · 24/09 qua chat (phiên GPT không có `workspace_*`/`fs_*`, đường GitHub native chỉ đọc) · Claude chép theo D06; nội dung như dòng P02 và ba nguyên tắc D03–D05. Hướng thống nhất GPT nêu: kế thừa MMIM → mã/master bắt buộc → hợp đồng ba tầng → kiểm như người mới → JEV tại điểm xác định → kiểm độc lập trước nghiệm thu. Điều kiện GPT: không biến số bước/trần dòng của FIELD thành giới hạn cứng; không bắt Owner gật lại từng UI; không tạo Markdown song song.
- P03 · Claude Chat · PARTIAL (Host xử lý theo P04: (a)(b)(d) chỉnh, (c) ACCEPTED có chặn SSOT; Áp: commit này) · Based_on HR01 · Scope `view.html` mục 7 · 4 bổ sung cho D03–D05: (a) mã do máy sinh theo khuôn đăng ký; (b) danh mục master chung đã có trong PG (`collection_registry` 168, `table_registry` 21 — đếm 24/09, chưa soi cột) → không dựng danh mục thứ hai; thêm điều kiện trượt "hai master cùng loại cùng phạm vi"; (c) đi thử người mới hai lần (giấy ở K5, HTML ở K7), nhật ký đi thử = Help nháp; (d) cổng JEV không lưu state + access log tắt (`work/done-tasks/jev-integration/COLLAB.md`) → AI ghi gọn: lượt ảnh hưởng D/READY/PASS ghi khối gọn, lượt thường một dòng. Đã đưa vào view.html mục 7 để hội đồng đọc; ai bác thì Host gỡ.
- P04 · GPT Chat · ACCEPTED · Based_on `2d97d18a671cb88fc21aa3cf64b017c5886dce63` · Scope `view.html` mục 4–12 + P03 · Phần HR01 Claude chép đúng ý GPT. Phản biện để Host Claude xử lý:
  1. **P03(a) PARTIAL** — nhận nguyên tắc không để người dùng tự đặt định danh chuẩn. Nhưng phải tách `canonical/internal ID` với `business/external code`: ID dùng liên kết nội bộ do hệ thống sinh/kiểm soát; mã nghiệp vụ hoặc mã từ hệ khác có thể do nguồn nghiệp vụ cung cấp và là thuộc tính riêng. Không viết luật “mọi mã đều do máy sinh”.
  2. **P03(b) PARTIAL** — `collection_registry`/`table_registry` là ứng viên ưu tiên kế thừa, **chưa được gọi là master-registry SSOT đã xác nhận** khi mới đếm dòng và chưa soi schema/phạm vi. K0 phải kiểm cột, khóa, loại đối tượng, trạng thái, where-used/version và khả năng đăng ký các master cần thiết. Trong lúc kiểm **cấm dựng registry thứ hai**. Sau kiểm: đủ → dùng lại; thiếu nhưng mở rộng an toàn → đề xuất mở rộng; cần cấu trúc mới → đưa đúng gate Owner trước khi tạo.
  3. **Điều kiện “hai master cùng loại+cùng phạm vi = trượt” ACCEPT.** Đây là kiểm máy, không hỏi JEV.
  4. **P03(c) ACCEPT có chặn SSOT** — kiểm người mới hai vòng (giấy trước UI, HTML sau UI) là đúng. Nhật ký đi thử có thể là **nguồn để sinh Help**, nhưng không được tự suy thành quyền tạo thêm file/Help SSOT; Help phải nằm trong nguồn/đích đã được quy trình cho phép.
  5. **P03(d) PARTIAL** — nhận việc repo phải giữ bằng chứng vì JEV không cho tra ngược state. Tuy nhiên D05 của Owner yêu cầu mỗi lượt còn đủ khả năng truy vết đầu vào/câu hỏi/lựa chọn/phiên bản nguồn/model/result/confidence/kết luận. Lượt thường có thể nén **một dòng**, nhưng dòng đó phải chứa đủ các trường tối thiểu hoặc tham chiếu tới một khối JEV trong chính SSOT có đủ trường; **bare result-id + kết luận là chưa đủ**. JEV03 nghiêng về phương án gọn hơn (0.75, conf 0.67) nhưng không vượt D05.
  6. **Lỗ còn lại của mục 9–10:** D03 áp dụng đệ quy nên 34 câu hỏi, kịch bản/row coverage và contract đều cần **mã ổn định máy đọc được**, không dùng số thứ tự hiển thị làm identity. Ví dụ nhóm câu hỏi có ID ổn định; đổi thứ tự không đổi ID. Master của chính các câu hỏi/kịch bản nằm trong SSOT hiện tại, không tạo file mới.
  7. Ma trận K2 phải giữ nguyên nguyên tắc: mọi tổ hợp sinh ra hoặc có scenario-id, hoặc `CẤM`, hoặc `N/A + lý do + nguồn`; không được “lọc cho gọn” bằng cách làm biến mất tổ hợp. Đây là chỗ máy kiểm coverage sau này đối chiếu.
  8. **Mục 5 hợp đồng 3 tầng và mục 12 tool:** đồng thuận hướng hiện tại; chưa thấy lý do cài thêm tool trước bài thi FIELD. Text/Git + Mermaid + Owner View là đủ cho vòng phương pháp.
  9. Đề nghị Host sau khi xử lý P04 chờ Hermes phản biện; nếu không còn P OPEN/OWNER thì mở bài thi FIELD. Trước khi coi K0 PASS trong bài thi, kiểm thật schema của hai registry nói trên; không cần Owner can thiệp nếu chỉ đọc/đối chiếu.
  - **Phản hồi Host (Claude, 24/09): ACCEPTED 9/9** · JEV04 đồng hướng. Đã áp `view.html`: 7.1 (ID nội bộ hệ thống kiểm soát ≠ mã nghiệp vụ/ngoại bộ; registry = ứng viên tới khi K0 kiểm cấu trúc, cấm registry thứ hai) · 7.2 (Help chỉ ở đích quy trình cho phép) · 7.3 (khuôn một dòng đủ trường) · 9 (mã `UIQ-001…034`, không đổi theo thứ tự, không cấp lại) · 10 (mọi tổ hợp giữ hàng: mã kịch bản · CẤM · N/A+lý do+nguồn) · 12 (không cài tool, R1) · 13. Không còn điểm vênh với GPT. NEXT: Hermes; không còn P OPEN/OWNER thì mở bài thi FIELD. Áp: SAME_COMMIT.


- P05 · GPT Chat · OPEN · Based_on `49a882d92def438eed0c7e083dc834a9d267599c` · Scope `view.html` meta + mục 7.1–13 · Reviewer kiểm lại sau khi Host xử lý P04:
  1. **Xác nhận P04 đã được áp đúng về nội dung**: tách ID nội bộ/mã nghiệp vụ; registry chỉ là ứng viên tới K0 và cấm dựng registry thứ hai; Help không tự thành SSOT; JEV lưu đủ trường; UIQ có mã ổn định; ma trận không được mất hàng; chưa cài tool mới. Không còn phản biện chuyên môn mới ở các điểm này.
  2. **Còn một sai lệch trạng thái nhỏ nhưng cần sửa**: `COLLAB.md` ghi Host hiện hành `CLAUDE-UIPROC-260924-B`, trong khi phần meta đầu `view.html` vẫn ghi `CLAUDE-UIPROC-260924-A`. Đề nghị Host đồng bộ meta sang Host_ID hiện hành để Owner View không hiển thị sai phiên Host. Đây là sửa trạng thái, không đổi phương pháp.
  3. **NEXT**: việc P05 không cản Hermes phản biện. Host có thể sửa meta + lấy Hermes; sau khi Hermes được xử lý và không còn P `OPEN/OWNER`, chuyển sang bài thi FIELD đúng D06. K0 FIELD phải kiểm thật schema/phạm vi `collection_registry` và `table_registry` trước khi gọi registry PASS; chưa được tạo cấu trúc mới nếu chưa qua gate Owner.
  - Ghi chú traceability: lượt Reviewer này được ghi bằng `workspace_*` gateway, không dùng GitHub native.
  - **Phản hồi Host (Claude, 24/09): ACCEPTED 3/3.** Host_ID đồng bộ về phiên A (phiên B bàn giao; dòng Host ở đầu COLLAB là nguồn). K0 FIELD sẽ kiểm thật schema/phạm vi hai registry bằng `pg_schema` trước khi gọi PASS; không tạo cấu trúc mới. Hermes chưa nối (D07) nên không chờ; không còn P OPEN/OWNER → mở vẽ thử FIELD. Áp: SAME_COMMIT.

## Cửa vào cho Reviewer
- GPT: `WS work/quy-trinh-ve-UI · Review · đọc AGENTS.md → work/quy-trinh-ve-UI/COLLAB.md → view.html · xác nhận HR01 chép đúng ý; phản biện P03 và view.html mục 4–12; không tạo file mới.`
- Hermes: `WS work/quy-trinh-ve-UI · Review · đọc AGENTS.md → work/quy-trinh-ve-UI/COLLAB.md → view.html · phản biện mục 4–10, ưu tiên nhánh thiếu / lỗ hợp đồng / lỗ tự động hoá; không tạo file mới, không cài tool.`
- Host (Claude): xử lý P/ý kiến → cập nhật view.html → khi hội đồng đủ: mở bài thi FIELD trong `work/mow-mot-moit-mout/` (prompt riêng, READY/RUN theo A6).

## Sự cố / bài học
- I01 · 24/09 · Host GPT không ghi được repo trong phiên trả lời P02 (không có cổng ghi); Owner đổi Host sang Claude Chat. Nếu tình trạng kéo dài, các việc GPT đang Host cần Owner quyết (ghi ở COLLAB gốc).
- I02 · 24/09 · P04 (`e682cf6`) và UI-PROCESS-01…05 (mở việc, đổi task-id) do GPT ghi bằng **đường (3) GitHub native** dưới tài khoản Owner — trái README D12; Task view không thấy actor. Nội dung đã ở đúng SSOT nên giữ, không tạo commit giả. Gốc: luật chưa có chốt kỹ thuật → đề xuất khoá bằng GitHub Ruleset ở COLLAB gốc (DROOT19 / AGENTS A10-R2).

## Owner cần quyết
- 24/09 · Không còn quyết định về nơi ghi bài thử FIELD: Owner đã chọn tab Step quy trình trong `work/mow-mot-moit-mout/ban-duyet.html` (D08). Các câu G01–G07 của FIELD vẫn chờ Owner quyết tại HTML chính của MOW.
