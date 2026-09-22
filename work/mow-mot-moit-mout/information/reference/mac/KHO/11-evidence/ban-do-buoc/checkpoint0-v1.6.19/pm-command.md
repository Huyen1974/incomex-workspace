# Lệnh giao Codex — bản đồ từng bước/UI/Agent: chốt phạm vi trước, rà đủ sau

**GPT Chat / PM · 11/09/2026 · Bản hợp nhất góp ý Fible**  
**Đầu vào hiện tại:** `cấu trúc hệ thống.html` v1.6.18 và evidence trong dự án.  
**Gói bằng chứng mới nhất:** `KHO/11-evidence/gate3-4/Gate3-4-v1.6.18-bang-chung.zip`.

**LỆNH HIỆN HÀNH DUY NHẤT.** Bản này thay toàn bộ `Lenh_Codex_Lap_Ban_Do_Buoc_UI_Agent_Ra_Lai_Buoc1.md`, đã gộp các góp ý giám sát được PM nhận. Không thi hành lệnh cũ và phụ lục như hai chỉ đạo song song. Nếu đã làm một phần, giữ lại nguồn/evidence/kết quả phù hợp; không xóa hoặc làm lại chỉ vì đổi lệnh.

**Một gói việc, đúng một điểm dừng bắt buộc:** nộp danh sách bước để Owner xác nhận phạm vi trước khi kiểm kê UI chi tiết. Sau xác nhận, làm trọn phần còn lại; không hỏi duyệt từng màn.

## 1. Quyết định điều hành — thay hướng đi của lượt kế tiếp

Owner yêu cầu làm lại đúng phương pháp:

> **Từ yêu cầu/thiết kế → liệt kê bước cần có → thông tin và hành động từng bước → UI và đường Agent/tool → đối chiếu cái đang có → chốt giữ/sửa/bổ sung/loại bỏ → kiểm ngược thiết kế → mới khóa Contract/Data.**

Không tiếp tục giao “vá sáu UNKNOWN rồi mở Pilot”. Sáu gap của v1.6.18 là bằng chứng đưa vào bản đồ, không phải toàn bộ phần hệ thống còn thiếu.

PM điều chỉnh nghiệm thu:
- Giữ giá trị các bằng chứng kỹ thuật/lab Rev2 đã có: intent→Draft, reuse/resume, machine test, lifecycle, pin và feedback trace trong đúng giới hạn đã báo. Không chạy lại toàn bộ, không xóa lịch sử. Lab đã dọn không được mô tả thành deployment còn đang hoạt động; giữ gói replay/evidence. Bản đồ chỉ gắn sáu gap vào bước tương ứng, không đặt lại mọi proof thành chưa làm.
- **Gate1 mở lại phần completeness:** kiểm kê 41 candidate, phân vai và chọn 5 pattern không đủ để kết luận mọi bước đã có UI/thông tin/đường Agent phù hợp.
- Gate2 giữ những thiết kế/workshop đã kiểm, nhưng kết luận “đã khép toàn bộ UI” phải được xét lại sau bản đồ này.
- Gate3/4 giữ PARTIAL và các kết quả đã nộp; tạm dừng mở rộng triển khai/khóa cuối. Gate5–7 chưa mở.
- Gate0 giữ evidence khả thi đã nhận, nhưng baseline phải được kiểm ngược từ bản đồ; phát hiện mâu thuẫn thật thì ghi proposal sửa đúng nguồn. Không dùng câu “đã khóa” để từ chối rà logic.
- D03 và các lựa chọn UI trước đây là đầu vào có phạm vi; được đề nghị điều chỉnh khi đối chiếu nhu cầu từng bước cho thấy không phù hợp. Không tự viết lại lịch sử D03.

**D04 đã được OWNER ACCEPT.** Owner đã phát biểu trực tiếp trong cuộc trao đổi:

> “Đồng ý: executor ≠ delegate ≠ người nhận task tiếp ≠ người nhận báo cáo ≠ đầu mối bàn giao.”

Ghi D04 `DECIDED / OWNER ACCEPT · 11/09/2026`, giữ đủ năm nghĩa đã trình. Đây là quyết định về nghĩa vai, không phải cấp quyền cho tài khoản hay duyệt chính sách production. Không hỏi Owner lại. Nhãn WAITING OWNER của D04 trong v1.6.18 đã cũ so với chỉ đạo này.

Các quyết định trên thay phần “không reopen Gate0–2 / chuẩn bị mở Pilot” trong lệnh Rev2 cũ. Không thay các giới hạn an toàn.

## 2. Sản phẩm trọn gói phải giao

Owner cho phép **một tài liệu HTML mới** tại thư mục dự án:

`BAN-DO-BUOC-UI-AGENT.html`

Tên hiển thị: **Bản đồ từng bước — cần gì, đã có gì, còn thiếu gì**.

Đây phải là **bản đồ được điền từ nguồn và UI thực**, không phải template trống, bài tổng luận, hoặc một workshop dựng riêng quanh quy trình thời lượng.

Phạm vi của hai tài liệu:
- `cấu trúc hệ thống.html`: kiến trúc, mục tiêu, quyết định có thẩm quyền, trạng thái và lịch sử dự án.
- `BAN-DO-BUOC-UI-AGENT.html`: nơi duy nhất giữ ma trận chi tiết từng bước, yêu cầu thông tin, đối chiếu UI/tool, gap và đề xuất xử lý. Là tài liệu con được SSOT dẫn chiếu; không là nguồn ra quyết định kiến trúc thứ hai.

Không copy toàn bộ ma trận vào SSOT. SSOT chỉ giữ kết luận, mẫu số/tổng hợp được sinh từ bản đồ, quyết định, gap quan trọng và link. Các bảng/checklist trong HTML mới phải được sinh từ cùng một dataset để không có nhiều bản số liệu phải sửa tay.

**Owner chỉ cần mở HTML mới để xem công việc.** Ảnh/source/evidence dùng đường tương đối dưới `KHO/11-evidence/`; không buộc Owner mở JSON hoặc đi tìm ZIP. Được tạo dữ liệu/harness kiểm tài liệu và tài sản ảnh đi kèm; chúng không phải tài liệu kiến trúc mới.

## 3. Một gói lớn, hai pha và đúng một điểm duyệt giữa chừng

### Pha A — phục hồi nguồn, lập danh sách bước và trình phạm vi

1. Đọc các nguồn bắt buộc ở §4; lập đối chiếu từng bước cũ với yêu cầu hiện hành.
2. Liệt kê toàn bộ bước cần có, gồm luồng chính/phụ thuộc và nhánh chờ/lỗi; không dùng số UI hiện hữu để giới hạn danh sách.
3. Ghi mục tiêu, điều kiện bắt đầu, kết quả, chủ thể người/máy và nơi đi tiếp đủ để nhận diện từng bước. Chưa điền trước mức đủ UI hoặc chọn bản UI chính.
4. Tự rà độ phủ nguồn/family/vòng đời và kiểm bằng góc người mới học. Chuẩn bị cho PM/Fible kiểm độc lập, không tự ghi independent PASS.
5. Trình **Checkpoint 0 — danh sách bước đề nghị chốt**, rồi DỪNG để Owner phản hồi. Không tự coi sự im lặng hoặc D04 đã đồng ý là duyệt danh sách bước.

Được đọc ba trang quy trình cũ/Help/source như tài liệu yêu cầu ngay ở Pha A. Chưa thực hiện rà control/field từng candidate hoặc tính tỷ lệ đủ UI trước checkpoint. Kết quả UI từng có vẫn giữ; không làm lại inventory cũ trong pha này.

**Bản Owner cần đọc:** tối đa hai trang nội dung tiếng Việt dễ đọc ngay trong `BAN-DO-BUOC-UI-AGENT.html` ở chế độ “Duyệt danh sách bước”. Có các chuỗi tạo/sửa/ngừng/sử dụng theo nhóm, tổng bước và những chỗ đề xuất gộp/tách/bổ sung; một mục minh họa cách đếm. Danh sách đầy đủ + nguồn gập bên dưới, không ép cả trăm dòng vào hai trang bằng font nhỏ.

Chỉ hỏi: **“Các luồng/bước này đã đúng ý nghiệp vụ chưa, còn thiếu hoặc sai chỗ nào?”** Không yêu cầu Owner kiểm từng URL, schema, tool hoặc xác nhận rằng hệ thống đã đủ. PM/Fible chịu trách nhiệm kiểm kỹ độ phủ; Owner không gánh việc phát hiện mọi sai sót thay AI.

Khi Owner bổ sung, cập nhật đúng phạm vi và lưu chênh lệch. Đóng băng bản có nguồn + hash sau khi được xác nhận. Đây là checkpoint duy nhất có kế hoạch xin Owner duyệt; không mở checkpoint riêng cho từng family.

### Pha B — sau khi phạm vi được xác nhận, thực hiện trọn bản đồ

1. Lập bảng tool thực có ở §6 trước khi điền cột Agent.
2. Hoàn thiện nhu cầu thông tin/hành động/đường Agent theo từng bước đã chốt.
3. Gắn UI/Help/source hiện hữu vào từng bước, so field/control/state và các biến thể.
4. Ghi khoảng thiếu UI/tool, đề nghị giữ/ghép/sửa/thiết kế thêm/ngừng dùng.
5. Truy vết contract/data sơ bộ; rà ngược Gate0 thành danh sách phát hiện/đề xuất, không tự sửa Factory/INV.
6. Đi bộ tạo/sửa/loại bỏ/sử dụng, tự QA toàn bộ và chuẩn bị supervisor review.
7. Sinh thống kê + heatmap 12×9 từ cùng dataset; hoàn thiện HTML và cập nhật SSOT ở đợt bàn giao cuối.

Được chia agent/phiên nội bộ; chỉ một writer hợp nhất. Mỗi pha có checkpoint/evidence bền để tiếp tục, không phụ thuộc trí nhớ chat. Sau Checkpoint 0 không gửi báo cáo hoàn thành sau từng object. Lỗi nguồn/quyền/an toàn: lưu giới hạn, làm các nhánh độc lập, không bịa để PASS. Nếu đã rà UI theo lệnh cũ, giữ làm evidence chưa nghiệm thu và dừng ở Checkpoint 0 thay vì xóa kết quả.

## 4. Nguồn và phạm vi cần phủ

Đọc SSOT current **toàn phần có ảnh hưởng yêu cầu**, đặc biệt mục tiêu Owner, G/J/L, ownership, toolchain, lifecycle, runtime, cải tiến, retire và các quyết định. Dùng lại nguồn cũ/Help/registry để phục hồi những yêu cầu đã thảo luận nhưng bị rơi.

Nguồn tối thiểu:
- SSOT v1.6.18, các quyết định Owner/PM mới trong lệnh này.
- `00-NGUON-THIET-KE.html`, phần liên quan của `SO-HOP-DONG-THONG-TIN.xlsx`, Help/ghi chú các UI.
- Ba nguồn quy trình có từ trước: **`mot-process-v1.html`**, **`bat-dau-o-day.html`**, **`quy-trinh-he-thong.html`**. Ưu tiên snapshot đúng ngày/version đã archive; nếu cần, đọc bản current ở `ui-preview/mcp-writes/` và ghi rõ khác biệt. Không chỉ đọc menu hoặc tên file.
- Nguồn đối chiếu đi kèm: `00-NGUON-THIET-KE.html` §4.0/§4.9 và lịch sử v2.6–v2.9; L00–L09 và các bảng đối tượng §05–§11 trong SSOT. Các nguồn cũ là căn cứ phục hồi tư duy, không thay chỉ đạo Owner/PM hiện hành.
- Gói R1, Gate1/R2–R8, Gate2/R9, các snapshot UI/source/ảnh và 8 nhóm gap đã lưu.
- Evidence Gate3–4 v1.6.18: limits, sáu gap, contracts/data matrix, chuỗi Agent và UI thực đã thử.
- Candidate UI còn truy cập được và repo/component tương ứng, ở chế độ đọc.

Ưu tiên nguồn trong `KHO/11-evidence`; không discovery lại một thứ đã có bằng chứng còn phù hợp. Khi source/version thay đổi phải ghi rõ.

**Phục hồi mẫu số, không sinh bộ bước mới từ trí nhớ:** nguồn cũ đã ghi 16 bước tạo quy trình và 4 chỗ đứt; nguồn khác ghi 23 bước/4 nhánh với trạng thái 6/8/9 ngày 02/09. Đây là **hai phạm vi/góc nhìn lịch sử**, không cộng thành 39 bước, không bắt ngày nay giữ nguyên tổng, không mang tỷ lệ cũ thành hiện trạng.

Đọc và lập bảng: `nguồn + bước gốc → bước trên bản đồ → giữ/gộp/tách/thay thế/không áp dụng → lý do`. Không bỏ một bước cũ mà không ghi disposition. Bước mới phát hiện phải ghi căn cứ suy ra/yêu cầu, nhãn “phát hiện/đề xuất mới”, không giả rằng từng được duyệt. Chỗ nguồn cũ trái baseline hiện hành giữ cả hai ý và đưa vào rà ngược.

Nhận định “sáu gap kỹ thuật trùng sáu màn thiếu cũ” là giả thuyết đối chiếu, không tự coi là quan hệ 1:1. Kiểm từng yêu cầu trước khi ghép.

Phạm vi chính: **MOW, MOT, MOIT, MOUT, Field**, mỗi loại có **tạo/dùng lại; sửa/cải tiến; ngừng/loại bỏ** và cách được sử dụng khi quy trình chạy. Không gộp MOIT nhập liệu với MOUT tham khảo hoặc với output hoàn thành Task.

**Phủ đủ 12 đối tượng của heatmap hiện có, không chỉ năm đối tượng chính.** Bảy nhóm còn lại là **Table, Trigger, Condition, NTGV, Người/vai/ủy quyền, Hướng dẫn và Cây tổ chức**. Mỗi nhóm phải có dòng tạo/dùng lại, sửa và ngừng riêng, cùng Test/Duyệt/Ban hành/Sử dụng khi áp dụng. Được dẫn “bước chung + khác biệt”, nhưng view mở rộng phải cho thấy đầy đủ yêu cầu của nhóm đó; không chỉ nói “xuất hiện ở một bước MOW”. N/A cần căn cứ, không phát minh một cơ chế mới để lấp ô.

People/Role/Delegation và Cây tổ chức có thể được quản tại nguồn ngoài; vẫn phải mô tả đường lookup/đồng bộ/đổi/ngừng ở đúng authority, không tự xây HR master thứ hai.

Các phụ thuộc khác như Capability/AUTO, Test, Review/Approval, Publish/Activate, audit, phản hồi/thu hồi cũng phải có bước hoặc ánh xạ rõ khi cần. 12 hàng heatmap không phải cớ bỏ tài nguyên ngoài 12 hàng; chỉ không tự tạo thêm Mother/taxonomy. Bước liên quan Trigger phải phân biệt workflow-start với điều kiện bắt đầu các bước sau.

Bước chung dùng lại định nghĩa chung; khác biệt theo family phải hiện rõ khi chọn family đó. **Không thu phạm vi bản đồ về Pilot thời lượng**. Pilot là một ví dụ kiểm xuyên chuỗi, không đại diện mọi bước của sản phẩm.

Mỗi yêu cầu lấy từ đâu phải có link/anchor. Điều suy ra hoặc đề xuất mới phải được gắn nhãn, chưa coi là quyết định đã duyệt. Không biến phát biểu trong Help cũ thành authority nếu trái chỉ đạo current.

## 5. Cách đếm bước — phải trả lời được “có bao nhiêu bước?”

Không dùng số Gate, G1–G10, J01–J16, số URL hay số click thay cho tổng bước.

Một bước đủ nhỏ để rà là một đơn vị có **điều kiện vào, mục tiêu, chủ thể thực hiện, thông tin cần dùng, hành động/kết quả và nơi đi tiếp**. Tách khi các phần đó thay đổi đáng kể; không tách từng nút/field thành một bước chỉ để tăng số lượng.

Lập danh sách yêu cầu/bước có crosswalk nguồn trước; trình Checkpoint 0 theo §3; bản Owner đã xác nhận mới là phạm vi freeze có hash. Sau đó mới đối chiếu inventory chi tiết.

Freeze không có nghĩa cố giữ sai: phát hiện thiếu sau đó phải ghi nguồn, lý do và chênh lệch mẫu số. Không tự bỏ requirement/N/A để làm đẹp tỷ lệ. Bổ sung cách biểu diễn không đổi nghĩa thì PM rà ở cuối; thay đổi material về luồng/nghĩa/phạm vi phải để proposal chờ đúng authority, không tự thêm rồi claim Owner đã duyệt. Phần bị ảnh hưởng chưa được tính đủ.

Phải báo riêng:
- Số chặng lớn để Owner dễ đọc.
- Số bước chi tiết theo từng family và từng luồng tạo/sửa/loại bỏ/sử dụng.
- Số bước chung được tái sử dụng và số bước đặc thù; không cộng hai lần để báo “tổng duy nhất”.
- Nhánh lỗi/chờ/trả sửa/tiếp tục nào là trạng thái của cùng bước, nhánh nào là bước khác có lý do.

Có thể dùng anchor/local key phục vụ truy vết và đếm; không đẻ một hệ taxonomy cấp sản phẩm mới. Dùng lại G/J/L/U khi phù hợp và giải thích bằng tiếng Việt.

## 6. Mỗi bước phải có hai đường song song, dùng chung sự thật

Trong HTML, khi mở một bước phải nhìn được **Người/UI** cạnh **Agent/công cụ**, cùng input/output/context, không phải hai quy trình độc lập giữ hai bộ dữ liệu.

### Bảng tool thực có — phải có trước khi điền cột Agent

Lập một bảng ngắn, bản tóm tắt không quá một màn/trang; chi tiết gập. Dùng evidence đã có, không chạy lab mới để lập bảng.

Mỗi mục: `tool/action cụ thể · nguồn/phiên bản · làm được gì · đầu vào/đầu ra/quyền · caller · mức bằng chứng · giới hạn · link`.

Kiểm các ứng viên thực đã biết: cổng ghi/guard, Directus API, MCP/query client nếu có executable/source đã kiểm, pg-boss worker, validator/compiler, runbook T0 của Rev2. **Đây là danh sách cần xác minh, không danh sách đã mặc nhiên sẵn sàng.**

Tách rõ: đang triển khai và truy cập được / đã chạy trong lab có gói tái tạo / mới có source hoặc runbook / chưa có / chưa xác minh. Lab đã dọn không thành service đang sống; shell transcript/runbook không thành dispatcher; thư viện đã cài không thành tool đáp ứng bước.

Cột **Agent hiện có** chỉ được dẫn tool/action trong bảng này với đúng phạm vi đã chứng minh. Không có mục phù hợp thì ghi CHƯA CÓ hoặc CHƯA XÁC MINH. Cột **phương án cần có** được mô tả proposal rõ ràng nhưng không tính là tool hiện có; ưu tiên API/config/native và khối dùng lại đã biết trước phần code mới. Tool có thể phục vụ nhiều bước; không tạo một tool/microservice cho mỗi bước.

Mỗi step card có đủ:

| Phần | Phải trả lời |
|---|---|
| Nguồn và mục tiêu | Yêu cầu nào sinh ra bước; áp dụng family/luồng nào; điều gì chứng minh bước xong? |
| Điểm vào/điểm ra | Đến từ đâu; điều kiện bắt đầu; kết quả gì; bước/nhánh kế; chờ ai và quay lại đâu? |
| Người/UI | Vai nào xem/làm; cần thấy gì để quyết; nhập gì tối thiểu; hành động nào, điều kiện được phép, thông báo/lỗi/khôi phục nào? |
| Agent/tool | Agent suy luận phần gì; công cụ tất định làm gì; gọi đường/tool nào; input/output; kiểm quyền/contract; ghi/đọc lại/checkpoint ở đâu? |
| Tự động hóa | Đã có tool và evidence, mới có thiết kế, thiếu tool hay chưa xác minh; còn ai khởi chạy/resume; không gọi shell transcript là dispatcher đã triển khai. |
| Ngữ cảnh | Object/package/version/revision/Task/Instance/actor/scope cần giữ; chuyển màn/caller không mất hay lấy nhầm context. |
| Ngoại lệ | Thiếu nguyên liệu, mơ hồ, sai quyền, stale, lỗi test, gián đoạn, replay… đường xử lý liên quan và điều kiện quay lại. |
| UI ứng viên | Màn/vùng/control/state nào; snapshot, source/Help, version; tình trạng đã có/thiếu/chưa rõ. |
| Hợp đồng sơ bộ | Nguồn của từng thông tin, ai sở hữu, ý nghĩa/kiểu/đơn vị, quyền, kết quả đọc/ghi; map tới C01–C10 nếu có. |
| Kiểm tra | Một cách kiểm cụ thể, expected, evidence hiện có và phần CHƯA CHẠY; không dùng “đã map pattern” làm bằng chứng đủ thông tin. |

Bước máy làm hoàn toàn không buộc có màn riêng. Ghi rõ **không cần UI nhập riêng**, nhưng phải chỉ ra nơi quan sát kết quả hoặc xử lý ngoại lệ khi cần. Không đếm việc thiếu một màn không cần thiết thành UI gap.

Đừng chỉ điền `T1`, `T2`, `P02`, `có API` hoặc `AI xử lý`. Phải nêu tool/action/cổng cụ thể đã biết hoặc đánh **CHƯA CÓ PHƯƠNG ÁN / CHƯA CHỨNG MINH**, cùng phần cần thiết kế.

Đường Agent/bulk phải xét tình huống lặp/dở dang: tìm trước tạo, gần đúng cần quyết, gửi batch có phần lỗi, gián đoạn/tiếp tục, nhận kết quả muộn, khác revision, quyền khác scope. Mục tiêu 98% khai báo AI không có nghĩa AI tự cấp quyền hoặc tự duyệt mọi việc.

## 7. Bản nháp hợp đồng UI — đối chiếu từng thông tin, không chỉ tổng field

Mỗi **surface/trạng thái có nhu cầu thông tin khác biệt** cần một bảng nhu cầu thông tin. Surface có thể là page, tab, drawer, panel, modal hay vùng dùng chung, không mặc định là trang mới.

Với từng thông tin/control bắt buộc phải nêu:
- Tên nôm na và semantic key/ref khi có; nghĩa, kiểu/đơn vị, điều kiện bắt buộc.
- Hiển thị, người nhập, máy suy ra/tự điền, chỉ đọc hay chỉ server giữ; không đẩy ID kỹ thuật cho người gõ nếu máy có thể lấy.
- Nguồn đọc/context/provenance, owner và quyền xem/sửa.
- Default/validation, empty/unknown/error; giá trị có đổi khi đổi version/scope không.
- Hành động dùng thông tin đó, kết quả ghi/đọc lại; thông tin chuyển bước sau.
- Màn/vùng/control thực tế đã có nó chưa; khác tên nhưng cùng nghĩa hay cùng tên khác nghĩa.
- Trạng thái: **đủ; thiếu; thừa/sai vai; xung đột nghĩa; chưa xác minh; N/A có căn cứ**.

Common fields được định nghĩa một lần, mỗi view kế thừa có override/delta rõ và xem được bản expanded. Không copy hàng trăm dòng context rồi báo thành hàng trăm field mới.

Không đồng nhất Field Definition, một ô nhập, cột PG và thuộc tính JSON. Không coi bảng 7 mục readiness hoặc 177 fact Pilot là toàn bộ yêu cầu UI.

Các trạng thái cần rà theo áp dụng: nháp/loading/empty, thiếu nguyên liệu, ambiguity, chờ/được/trả duyệt, stale test/approval, 403, 409 giữ dữ liệu đang nhập, version khác, lỗi nguồn, gián đoạn/resume, retire còn nơi dùng. Không bắt tất cả states thành màn riêng.

## 8. Nội dung đặc thù không được bỏ sót

Dùng danh sách này làm câu hỏi đối chiếu nguồn, không tự biến mọi ví dụ thành feature mới đã duyệt.

- **MOW:** intent, reuse, bước/nối tiếp/song song/nhánh/join, gắn MOT version, đủ/thiếu, start/binding/time, activation, version rollout, quan sát/ngoại lệ, sửa và ngừng nhận mới.
- **MOT:** nghĩa việc, HMITL/AUTO, đầu vào cần có, MOIT/MOUT/Guidance, người/service thực hiện, deadline, output/completion, bàn giao/lỗi; phân biệt Definition dùng chung với từng Task Instance. Dùng lại MOT không tự có nghĩa mọi runtime Task của hai quy trình là cùng một việc.
- **MOIT:** dùng lại form/Field, layout, required theo form, prefill/context, target/action, validation, lưu/mở lại/conflict, version đang dùng; sửa form không sửa nghĩa Field.
- **MOUT:** nguồn/tham số/filter/độ mới/quyền/consumer context, thiếu nguồn hoặc thiếu quyền, mở ngay trong việc được giao; không thay output hoàn thành của MOT bằng một báo cáo.
- **Field:** nghĩa/alias/kiểu/đơn vị, nguồn mapping, reuse/gần đúng, where-used, đổi nghĩa/kiểu/constraint, version/migration và retire an toàn.
- **Loại bỏ:** phân biệt bỏ bản nháp, gỡ binding ở một chỗ, ngừng dùng/activate mới, retire Definition, lưu trữ, hard-delete, và ngừng dùng UI cũ. Không gộp thành một nút Xóa.
- **Thời điểm kích hoạt bước:** bước đầu có thể dùng workflow-start Trigger; bước sau có thể do output trước + dependency/Condition/join/timer. Không sinh Trigger Definition giả cho mọi bước.
- **Runtime:** nhận việc/nhìn thông tin/nhập/kết thúc/chuyển bước, giám sát AUTO, thiếu người/ủy quyền hết hạn, retry/exception; việc nào tự động thì không tạo card bắt người bấm Done giả.
- **Cải tiến:** góp ý tại đúng context, xử lý/giữ dấu vết, tạo V2, test lại/impact/phát hành, đo trước-sau và phản hồi đóng góp. Chỉ có nút Góp ý chưa khép luồng.

Sáu gap v1.6.18 phải gắn vào đúng bước/thông tin/UI/tool: Task Instance, executor HMITL, dynamic input, handoff/output-receipt, MOUT context, MOUT consumer. Đây là các gap đã biết, **không phải toàn bộ checklist**. Đặc biệt phân biệt semantic release pin với giá trị nghiệp vụ người nhập lúc chạy; chỉ mô tả yêu cầu/đường xử lý, không vá guard trong lượt này.

## 9. Gắn thiết kế đã có vào bản đồ; xử lý 3–4 biến thể một tính năng

Rà theo **nhu cầu của bước**, không chọn bản mới nhất/đẹp nhất/nhiều nút nhất trước rồi uốn quy trình theo nó.

Cho mỗi UI cần thiết:
1. Thu tất cả candidate liên quan trong phạm vi đã xác định, gồm biến thể cũ có Help/nội dung riêng.
2. Gắn ảnh/current snapshot hoặc preview đọc an toàn **ngay trong step card**, đúng vùng liên quan; link source/Help ngay cạnh.
3. So cạnh nhau: cùng chức năng nhưng khác gì, thiếu/thừa thông tin nào, hành trình/context/owner có đúng không.
4. Đề nghị một vai trò chính, phần dùng lại từ bản khác, các sửa đổi cụ thể và phần cần thiết kế mới.

Ảnh/UI có sẵn phải ghi rõ **MOCK / CHỈ THIẾT KẾ / SOURCE-ONLY / ĐÃ NỐI MỘT PHẦN / ĐÃ KIỂM TRONG PHẠM VI** theo evidence. Thiết kế đủ không đồng nghĩa đã nối dữ liệu.

Không nhúng script/action có thể ghi vào hệ thật. Dùng ảnh hoặc snapshot chỉ đọc/sandbox; link live có nhãn rõ. Không sao chép nguyên production HTML rồi để nút Save chạy thật trong tài liệu.

Với surface chưa có, hiển thị ô **CHƯA CÓ THIẾT KẾ** và khung thông tin cần bổ sung. Có thể dùng wireframe nội dung tĩnh tối thiểu trong tài liệu để dễ đọc, nhưng phải gắn **ĐỀ XUẤT**, không được tính nó vào tồn kho UI đã có. Không đi xây cả UI production hay một prototype thay hệ thống.

Dùng đúng **bốn nhãn xử lý UI trong nguồn cũ**: **CHỐT / NHÁP / CÔNG CỤ / BỎ**. Không thay bằng sáu nhãn disposition mới.

- CHỐT: bản/pattern được chọn để đưa vào đường sản phẩm; không tự mang nghĩa đã deploy/kết nối/chạy đúng.
- NHÁP: ở xưởng thiết kế, chưa chọn dùng chính thức.
- CÔNG CỤ: phục vụ Agent/xưởng như nghĩa nguồn cũ, không mặc nhiên là màn người dùng nghiệp vụ.
- BỎ: đề nghị gỡ khỏi đường dùng/menu sau khi có replacement và quyết định hợp lệ, không tự hard-delete.

**Vai trò** library/review/expert/runtime là thông tin riêng; **hành động** ghép/sửa/lấy phần nào là mô tả riêng; **mức đủ thiết kế/triển khai/kiểm chứng** là trục khác. Không gán CÔNG CỤ cho mọi expert UI chỉ để đủ bốn nhãn.

Codex đề nghị nhãn, có nguồn/lý do/authority; không tự ra quyết định CHỐT/BỎ thay PM. Nhãn trước đây có quyết định giữ provenance, nhưng được đề nghị rà lại theo completeness. Chưa đủ căn cứ thì để nhãn đề nghị trống kèm lý do, không ép chọn và không tạo nhãn disposition thứ năm.

Bản đề nghị BỎ có replacement, nội dung cần bảo toàn, consumer/deep-link đã biết hoặc chưa biết và điều kiện loại bỏ. **Lượt này không xóa UI/code/route/menu thật.**

## 10. Thống kê phải trả lời đúng câu hỏi Owner

Dashboard HTML phải sinh số liệu từ ma trận, không điền tay. Tách ba đơn vị:

1. **Bước/yêu cầu:** tổng bước, bước cần UI, không cần UI riêng, bước có UI đủ/thiếu/chưa có/chưa xác minh; bước có/thiếu phương án Agent/tool.
2. **Surface thiết kế duy nhất:** page/panel/drawer/view-state có khác biệt cần thiết; cái dùng lại ở nhiều bước chỉ đếm một lần. Danh sách cần sửa, cần thiết kế thêm, bản cũ cần hợp nhất/ngừng dùng.
3. **Năng lực/hợp đồng/dữ liệu:** yêu cầu thông tin/control thiếu, tool thiếu, contract gap, source/table mapping chưa chứng minh. Không cộng chúng vào số UI.

Phải có các tổng theo cả 12 đối tượng đã nêu ở §4 và theo tạo/sửa/loại bỏ/sử dụng. Năm đối tượng chính đặt ở view đầu; bảy nhóm phụ thuộc mở được và không mất trong tổng.

Công bố mẫu số và quy tắc N/A. Tỷ lệ “đã đủ UI” lấy **bước cần UI và đã đủ thiết kế thông tin** làm cơ sở, kèm số chưa xác minh; không lấy `số URL đã mở / số URL tìm được`. Tỷ lệ triển khai kết nối là một chỉ số khác.

Owner ước tính 25% hoặc dưới 50% đã có chỉ là giả thuyết cần đo; không dùng nó làm target hoặc kết luận.

**Số UI cần thiết kế mới phải xuất phát từ các surface còn thiếu sau khi đã gộp nhu cầu dùng chung**, không phải cứ một bước thiếu tạo một màn. Đồng thời không được lấy tên 5 pattern để che việc phần lớn trạng thái/field cụ thể chưa được thiết kế.

### Dùng lại heatmap 12×9 trong SSOT

Không dựng dashboard tổng hợp thứ ba. Giữ đúng 12 hàng đã có và chín cột **Tìm / Tạo / Lắp / Test / Duyệt / Ban hành / Run / Sửa / Ngừng**.

- Mỗi bước gắn đúng đối tượng/chức năng, có thể nhiều liên hệ; đếm duy nhất trong từng phạm vi, không cộng các tổng chồng nhau thành tổng toàn hệ.
- Bảng mới và heatmap SSOT được **sinh từ cùng dataset bản đồ**. Khi ghi tài liệu, tạo snapshot tổng hợp kèm hash dataset; không cần đọc JSON động từ file:// để làm Owner phải chạy server.
- Mỗi ô chỉ rõ số bước/nhu cầu có đủ thiết kế, số còn thiếu/chưa xác minh; bấm mở đúng tập bước trong bản đồ.
- **Không đổi nghĩa màu cũ để làm đẹp tiến độ:** một ô chưa được kiểm chức năng không tự xanh chỉ vì đã map UI. Hiển thị riêng mức đủ thiết kế và mức đã kiểm hành vi/phạm vi bằng nhãn/số trong chính ô hoặc phần mở chi tiết. Không gọi simulated walkthrough hoặc mock đủ field là runtime PASS.
- Dùng legend/mức hiện có; nếu đang có trạng thái xám thì thay chỉ khi dataset/evidence đáp ứng chính tiêu chí ô đó. Có thể biết đầy đủ thiếu gì nhưng chức năng vẫn chưa được kiểm.
- N/A phải có reason, không dùng để xóa thiếu sót khỏi mẫu số. Tool có thiếu vẫn hiện riêng, không biến thành UI mới để đếm.

## 11. Contract/table: kiểm độ đủ sơ bộ và tính hợp lý, chưa khóa schema

Sau bản đồ thông tin mới đối chiếu C01–C10, registry hợp đồng cũ, matrix 385/177 và metadata thật đã có.

Mỗi thông tin/hành động cần map:
`Bước → UI/tool → contract hiện có hoặc khoảng thiếu → logical fact/owner → source/read/write đã biết hoặc chưa biết`.

Chỉ ra:
- Hợp đồng thiếu thông tin nào từ UI/tool; hợp đồng có mà không biết dùng ở bước nào.
- Cùng fact đang bị khai lặp ở đâu; cùng tên nhưng khác nghĩa.
- Candidate source/table phù hợp/chưa phù hợp và bằng chứng; quan hệ thực/FK so với metadata/discovered relation.
- Nơi chỉ cần dùng lại query/view/relationship/config so với gap thật sự cần thay data model.

Trả lời câu hỏi số table bằng **bảng lập luận có nguồn**: bảng hiện hữu liên quan, dùng lại, trùng/có thể hợp nhất, candidate bổ sung nếu có, chưa đủ dữ kiện. Không suy 119 khai báo =119 bảng, một UI =một bảng, hoặc “đếm đủ tables” là data lock.

Nếu chưa đủ căn cứ kết luận số table tối ưu, ghi rõ thiếu căn cứ nào. Không thêm DDL, permission engine, runtime adapter hoặc table production chỉ để điền hết UNKNOWN. Đề xuất data mới vẫn chưa được duyệt.

## 12. Hình thức HTML để Owner thực sự dùng được

Mở bằng browser từ thư mục dự án, không cần cài dependency. Không tạo một ứng dụng tài liệu cần server riêng.

- Màn đầu ngắn: đang rà bước gì, số bước/tình trạng UI/Agent, việc thiếu chính. Có nút **Xem từng bước** và **Chỉ xem phần thiếu**.
- Chọn family: MOW / MOT / MOIT / MOUT / Field; bảy nhóm phụ thuộc có lựa chọn mở riêng. Chọn luồng Tạo / Sửa / Loại bỏ / Sử dụng. Mặc định không bắt Owner đọc 12 đối tượng cùng lúc, nhưng tất cả đều tìm được và có bước riêng.
- Danh sách bước bằng tiếng Việt dễ đọc; bấm một bước mới bung chi tiết hai cột Người/UI và Agent/tool. Xem được điểm trước/sau, chờ/nhánh mà không mất context.
- Trong bước có ảnh/thiết kế thực, bảng field/control thiếu và phương án xử lý; không bắt Owner tìm ảnh ở file khác.
- Có chế độ xem ngược: chọn một UI → thấy tất cả bước nó phục vụ; chọn gap → thấy bước/mục tiêu bị ảnh hưởng.
- Có tổng hợp trùng/thừa và danh mục thiết kế bù dùng chung.
- Không giăng bảng ngang 20 cột trên màn chính. Detail technical gập; common detail dẫn link, không chép lại.
- Nhãn “đã thiết kế / đã triển khai / đã kiểm” phải tách rõ. Các nút của tài liệu chỉ điều hướng/lọc, không giả thao tác nghiệp vụ chạy thật.

Dữ liệu ma trận có thể nhúng trong HTML và sinh các view/checklist từ đó. Ảnh/source đi kèm dùng relative assets trong kho dự án. Owner mở HTML ở thư mục dự án đọc được, không phải truy lại thư mục phiên Codex.

## 13. Tự kiểm hai chiều và điều kiện hoàn thành gói

**Đi bộ logic từ yêu cầu → UI/tool**, rồi **đi ngược từ từng UI/contract/table candidate → yêu cầu**. Không chỉ static-check HTML.

Checklist tự QA bắt buộc:

| Kiểm | Đạt khi |
|---|---|
| Phủ nguồn | Mỗi yêu cầu trong phạm vi có bước thực hiện, phụ thuộc hoặc N/A có lý do. Đề xuất/UNKNOWN được nêu rõ; không bỏ vì chưa có UI. |
| Phủ family/luồng | Cả 12 đối tượng có tạo/sửa/ngừng và sử dụng phù hợp; shared steps có mapping/delta/expanded view. Phụ thuộc không bị ẩn ngoài mẫu số. |
| Đầu-cuối | Từ intent tới vận hành và từ sửa/feedback tới version mới có điểm vào/ra, trạng thái chờ, lỗi, quay lại. Không có đoạn “rồi AI xử lý” chưa mô tả. |
| Thông tin từng bước | Có nhu cầu xem/nhập/tự điền/quyền/action/output/error; đối chiếu xuống field/control hoặc gap cụ thể, không chỉ tên pattern. |
| Agent song song | Mỗi mục hiện có dẫn bảng tool/evidence; proposal tách riêng. Lab/runbook không nhận nhầm là deployed automation; batch/resume không bắt người nhớ tool. |
| UI hiện hữu | Mỗi bước cần UI có candidate+ảnh/source hoặc bằng chứng chưa tìm thấy trong phạm vi. Candidate đủ/thiếu dựa trên thông tin/state, không dựa nhãn/tuổi bản. |
| Duplicate/retire | Các variant được so cùng yêu cầu, có đề nghị bảo toàn/hợp nhất/loại bỏ; không delete trước approval. |
| Mẫu số | Crosswalk từ ba nguồn bước cũ + G/J/L; Checkpoint0 có Owner phản hồi; freeze/amendments minh bạch; số bước/surface/thông tin tách biệt và chưa xác minh không bị giấu. |
| Contract/data | Có trace hai chiều; thiếu/trùng/source unknown được nêu; không chốt schema từ UI. |
| Gate0 reverse review | Có bảng bước→nguồn/mâu thuẫn→tác động→đề xuất→người quyết. Không sửa Factory/INV/ownership; kiểm hash/nội dung các vùng được bảo vệ. |
| Chỉ đạo current | D04 Owner accepted; Gate1 completeness mở lại; không gọi Gate2 UI complete/full Contract/Data locked; không mở Pilot. |
| Tài liệu chạy | Filters/step links/preview/backlinks/ảnh hoạt động; heatmap12×9 và số tổng sinh cùng dataset/hash, không đổi màu chức năng từ đủ design; không runtime write/secret. |

Đi bộ tối thiểu các loại đường: tạo mới đủ nguyên liệu; thiếu/gần đúng và tự quay lại; sửa một nguyên liệu dùng chung; thay version khi còn lượt cũ; gỡ một binding mà không xóa Definition; ngừng dùng khi còn where-used; HMITL→AUTO với input người nhập và MOUT; góp ý→V2. Áp các biến thể material theo family, không chỉ một happy path Pilot.

**Hoàn thành gói = bản đồ đã kiểm đủ và chỉ chính xác mọi khoảng trống trong phạm vi, không phải hệ thống đã hết gap.** UI chưa có hoặc tool chưa xây là kết quả hợp lệ nếu nhu cầu/tiêu chí/cách xử lý rõ. Thiếu nguồn khiến không xác định nổi nhu cầu phải ghi blocker của bản đồ, không dùng dấu “?” để báo toàn gói hoàn tất.

### Hàng rào rà ngược Gate0

Kết quả là **một bảng phát hiện**: `bước → nguồn/điều khoản mâu thuẫn hoặc thiếu → ảnh hưởng → đề xuất → PM/Owner quyết → trạng thái`.

Trong lượt này không sửa nội dung Factory, INV hoặc semantic ownership đã chốt, không đổi tool/runtime contract để khớp UI. Phát hiện của supervisor cũng là evidence/proposal, không tự thành quyền sửa kiến trúc. Chỉ được nhập các quyết định có thẩm quyền ghi sẵn trong lệnh này (D04, phạm vi Gate1/2, quan hệ hai tài liệu).

Nếu một mâu thuẫn làm chưa định nghĩa được bước, giữ rõ các phương án + blocker tại bước, không chọn ngầm để báo đủ. PM xử lý sau cùng với rà bản đồ; không dùng “đã khóa” để loại bỏ phát hiện.

Fible nhận một mục hướng dẫn trong gói evidence để kiểm độc lập:
1. Mẫu số có đối chiếu từng bước trong ba nguồn cũ với thiết kế current, đủ 12 đối tượng và có Owner xác nhận phạm vi hay đang đếm UI tìm được?
2. Có bỏ sót tạo/sửa/loại bỏ và nhánh chờ/lỗi nào không?
3. Field/control và đường Agent có đủ cụ thể để biết phải thiết kế thêm gì không?
4. Chọn/loại UI có giữ đúng logic nghiệp vụ và ownership không?
5. Counts, source/evidence và trạng thái PM/Owner có đúng không?

Supervisor kiểm logic thực hiện lẫn kỹ thuật; hash/link PASS không thay completeness. Agent tự-review không gọi independent review. Không ép supervisor PASS trước khi nộp nếu chưa có công cụ/phiên supervisor thực sự.

## 14. Cập nhật và bàn giao — không để chỉ đạo nằm lại trong chat

Giữ single writer. Dùng staged copy, backup/hash và self-QA trước mỗi lần bàn giao hợp lệ; kiểm current hash trước ghi, nếu phiên khác đã sửa thì reconcile, không overwrite mù.

- **Checkpoint 0:** lưu HTML có bản duyệt phạm vi, crosswalk và nguồn đầy đủ. Ghi SSOT một lần để nhận D04 đã Owner ACCEPT, Gate1 completeness đang mở lại, link tài liệu con và “chờ Owner xác nhận danh sách bước”. Chưa tô coverage UI và chưa gọi bản đồ hoàn chỉnh.
- **Bàn giao cuối sau Owner xác nhận và Pha B:** cập nhật HTML/dataset/ảnh, sinh lại heatmap và kết luận SSOT một lần. Dùng version kế tiếp còn trống, ngày thực. Không sinh revision SSOT sau mỗi đối tượng hoặc mỗi nhận xét nhỏ.

Hai lần bàn giao này có mục đích riêng; không giữ dữ kiện D04 sai trong lúc chờ checkpoint, cũng không phát hành trước kết luận inventory chưa làm. Chỉ cho Owner một link đọc tại mỗi lần.

SSOT phải cập nhật đồng bộ Owner/Work/Gates/Decisions/Next/History/footer:
- D04 = OWNER ACCEPT, không còn current WAITING OWNER; lịch sử giữ nguyên có nhãn.
- Cho phép tài liệu HTML con và ranh giới hai file như §2.
- Gate1 completeness = DOING sau PM reopen; acceptance inventory/role trước đây giữ scope lịch sử.
- Gate2 composition cũ giữ evidence, nhưng current completeness chờ rà Gate1; dùng trạng thái hợp lệ hiện có, không thêm enum.
- Gate3/4 PARTIAL và tạm dừng khóa cuối theo dependency; Gate5–7 chưa mở.
- Gate0 bounded feasibility giữ nguyên; có kết quả/proposal rà ngược, không tự phủ nhận hoặc miễn kiểm baseline.
- Rev2 mới là bằng chứng có giới hạn; giữ sáu gap nhưng không mô tả “chỉ còn sáu gap là tới Pilot”.
- Nhập nguồn chỉ đạo Owner yêu cầu requirements-first và phê duyệt D04; nhập review correction PM có ngày, không sửa lịch sử như thể trước đây chưa từng nghiệm thu.
- Chỉ dẫn tới bản đồ từng bước, thống kê có phạm vi và danh sách vấn đề cần PM/Owner xem. Không paste toàn ma trận trở lại SSOT.
- Cập nhật heatmap 12×9 từ cùng dataset, giữ nghĩa design/implementation/verification rõ như §10; kiểm hash và tổng khớp.
- Dẫn bảng tool thực có và các giới hạn triển khai; không thăng bằng chứng lab thành service hoạt động.
- Bảo toàn các proof Rev2 và các dòng Kịch bản nghiệm thu số 0 theo đúng evidence hiện có; không reset kết quả chỉ vì quay lại phương pháp requirements-first.

**Quy tắc giữ bản đồ sống:** mọi WORK-ID sau này có thay đổi UI, tool nối UI, yêu cầu field/control, điều kiện/hành vi hoặc contract liên quan phải cập nhật những dòng bản đồ bị ảnh hưởng, evidence và số tổng/heatmap trong cùng lần bàn giao. Ghi rõ Step/UI refs bị tác động; nếu không tác động thì N/A có lý do. Chưa cập nhật hoặc đang mâu thuẫn với source current thì work chưa đủ điều kiện PM ACCEPT. Không biến bản đồ thành bản chụp một lần rồi bỏ quên như nguồn lịch sử.

Không product code/DDL/DML/migration/deploy/restart/Flow execution hoặc sửa UI hiện hành trong gói này. Chỉ đọc nguồn, tạo tài liệu/bảng đối chiếu/evidence và sửa tài liệu được cho phép. Code HTML/QA vẫn kê là code tài liệu, không gọi zero-code. Không chase version/license/runtime hay chạy thêm lab để né việc lập bản đồ.

**Báo cáo Checkpoint 0:** chỉ gửi link mở bản duyệt tiếng Việt ≤2 trang trong HTML, tổng theo luồng/nhóm, số bước cũ được giữ/gộp/tách/bổ sung và các chỗ cần Owner xem. Trạng thái “CHỜ XÁC NHẬN PHẠM VI”. DỪNG trước Pha B; không gửi Owner cả bộ JSON/log.

**Báo cáo cuối sau Pha B** chỉ cần:
1. Link mở **BAN-DO-BUOC-UI-AGENT.html** tại dự án.
2. Số bước theo family/luồng; mẫu số cần UI.
3. Số bước đủ UI, UI thiếu thông tin, chưa có UI, chưa xác minh.
4. Số surface duy nhất giữ/sửa/thiết kế thêm/hợp nhất-ngừng dùng.
5. Số bước chưa có tool/đường tự động đã chứng minh, tách rõ “có phương án nhưng chưa xây” và “chưa có phương án”; bảng tool source/evidence.
6. Gap hợp đồng/dữ liệu và kết luận về table ở đúng mức căn cứ.
7. Các điều Gate0 cần xem lại; chưa tự chốt thay Owner/PM.
8. D04, Gate1–4, heatmap12×9 và SSOT đã được sửa trạng thái gì; Checkpoint0 acceptance, self-QA và giới hạn.

Nộp snapshot HTML mới/SSOT, dataset/check-results và evidence ảnh/source cần thiết trong một ZIP có manifest cho PM/supervisor. Link đọc trỏ thư mục giải nén; ZIP là bản niêm phong. Không yêu cầu Owner chuyển từng file phụ.

**Không tự đóng Gate1/2 hoặc Gate3/4.** Chỉ nộp bản đồ đã kiểm để Owner/PM rà và thống nhất. Sau khi bản đồ được nhận, PM mới giao thiết kế bù/ghép/loại UI theo các nhóm đủ lớn, rồi kiểm lại Gate0 trước khi chốt Contract/Data.
