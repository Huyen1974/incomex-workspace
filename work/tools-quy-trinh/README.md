# tools-quy-trinh · Cửa vào

## Ma trận câu hỏi · hiệu lực 08/10/2026
- Owner đã giao **Astra Codex trong phiên này làm Host**, thay GPT Chat. Các thành viên khác, kể cả Codex ở phiên khác, chỉ gửi đề xuất riêng. Đây là đổi vai theo chỉ đạo trực tiếp, không phải tuyên bố cổng máy đã khóa được.
- Mở trực tiếp [Câu hỏi cơ bản trên hệ thống](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=cau-hoi-co-ban). URL ghi nhớ tab/mục; bước 1.2 dùng section=q-B1-2, mã câu vẫn Q-B1.2-01. Renderer chỉ nhận từ đúng iframe; xem bằng chứng ở COLLAB §0 ô 3.
- Đọc [Câu hỏi cơ bản](view.html#cau-hoi-co-ban) → [Câu hỏi nghiệp vụ](view.html#cau-hoi-nghiep-vu); đọc hàng loạt tại [Ma trận câu hỏi](view.html#ma-tran-cau-hoi).
- **SSOT của bộ câu hỏi mới:** JSON trong `view.html`, script `id="tqt-question-matrix"`. `groups` chứa mã/loại/cha/nguồn; `questions` chứa mã câu, nhóm sở hữu, câu hỏi, trạng thái; `inheritance` quy định câu chung. AI đọc trực tiếp JSON này; bảng, sơ đồ, bộ ghép và vùng JSON để sao chép đều đọc cùng dữ liệu.
- Host sửa câu hỏi trong JSON, giữ nguyên mã; không sửa chữ tại bản render, không nhân câu hỏi vào từng MOW/MOT. Bước con kế thừa bước lớn và câu chung; thêm câu riêng khi có khác biệt cần kiểm. Thêm nhóm/câu phải kiểm mã duy nhất, cha tồn tại, có câu hỏi, mọi cách xem cùng kết quả.
- Thuật ngữ theo chỉ đạo mới: **chuyên môn = Bước/Tầng/Chuỗi**; **nghiệp vụ = UI/Test/Config…**. Các cách gọi khác ở hồ sơ cũ được giữ để truy nguồn.
- Các nhóm nghiệp vụ khởi đầu: UI, Test/rà UI, Config, Nguyên tắc giao việc (đã được nêu trong mục tiêu Owner); thêm nhóm trong ma trận thì thẻ và bộ ghép tự nhận. Câu hỏi của các nhóm này vẫn là bản khởi tạo.
- Bộ câu hỏi mới là **bản đầu đang hiệu chỉnh**, không phải kết luận đã đủ hoặc đã qua hội đồng. Thành phần Công thức được đối chiếu nguồn; không đồng nghĩa các câu hỏi mới đã được Owner duyệt. Tầng bối cảnh T3–T7 thu gọn; B8/B9 chưa có bước con.
- Nội dung cũ giữ nguyên trong [Quy trình hiện có](view.html#tqt-legacy), liên kết cũ vẫn mở đúng mục. Bộ 8/7 câu và Master Tool legacy chưa cắt chuyển; không lấy việc thêm ma trận mới làm bằng chứng hoàn thành TQT-ISS-004.
- Góp ý: file riêng theo mẫu bên dưới, trỏ mã Q/nhóm, nêu chỗ vướng khi làm và câu đề nghị sửa. Chỉ Host quyết định tiếp nhận rồi cập nhật nguồn; không sửa thẳng bốn file chính. Chưa gọi hội đồng trong lượt dựng bản đầu này.


## 0. ĐỌC NGAY — DÀNH CHO MỌI AI (kể cả khi vừa bị từ chối ghi)

**Host duy nhất của task:** `Astra Codex · phiên Owner chỉ định 08/10/2026` (`Host_ID=OpenAI-main`). Mục tiêu và tiêu chí xong chỉ ở [COLLAB.md §0](COLLAB.md); phải đọc `../../AGENTS.md` và §0 trước khi thực thi.

**Chọn đúng tình huống:**

1. **Muốn dùng quy trình để làm thật:** đọc [Quy trình hiệu chỉnh hướng dẫn và quy trình](view.html#quy-trinh-hieu-chinh) nếu đang xây/sửa quy trình; nếu đang rà UI, đọc [Rà một UI · 6 bước](view.html#ra-ui). Thực hiện theo bước, lưu **sản phẩm/bằng chứng thực tế** tại task sản phẩm được phép ghi. Không đạt → ghi đúng chỗ thiếu, không tự tô PASS.
2. **Thành viên ngoài Host muốn sửa quy trình hoặc sổ TQT:** **KHÔNG** sửa trực tiếp `view.html`, `COLLAB.md`, `README.md` hay hồ sơ trên trang. Tạo **một file đề xuất riêng** `work/tools-quy-trinh/proposals/TQT-PR-YYYYMMDD-<seat>-<so>.md`, tên không trùng; Host đọc → duyệt → chỉ Host nhập vào nguồn chính rồi kiểm lại.
3. **Bị từ chối ghi, VERSION_CONFLICT hoặc không rõ quyền:** **DỪNG sửa nguồn đích**; đọc lại file README **`work/tools-quy-trinh/README.md`**, đối chiếu quyền và mẫu bên dưới; chuyển sang nộp đề xuất riêng, không retry cùng lệnh/bypass/ép push. Nếu ngay cả đường tạo đề xuất bị chặn, báo Host mã lỗi + đường dẫn + thời điểm; không tự mở đường khác.

### Xác nhận của người thực hiện — bắt buộc trước khi Host công nhận quy trình đạt

Bộ 8 câu/MOT và 7 câu Config **đã nằm ở** [“Rà một UI”](view.html#ra-ui); không viết lại bộ câu ở đây. Mỗi lần rà một UI, Codex/agent phải có câu trả lời + bằng chứng hoặc ghi rõ BLOCKED/NOT_TESTED/N-A kèm lý do cho **mọi câu áp dụng**, mọi nhánh bắt buộc và việc bàn giao.

Cuối lượt, **chính AI đã làm** gửi nguyên khối xác nhận này (trong file đề xuất riêng theo cổng trên, tuyệt đối không sửa ba file chuẩn):

```text
DOER_CONFIRM: YES | NO | PARTIAL     # Tôi đọc từ đầu, không được giải thích thêm, có hoàn tất quy trình RÀ SOÁT trong phạm vi giao không?
READ_VERSION: <commit/phiên bản README + #ra-ui + URL/phiên bản UI>
SCOPE: <MOT/màn nào, phần nào N-A hoặc chưa được phép thử>
QUESTION_COVERAGE: <Q1-Q8/MOT và 7 Config: đủ câu trả lời + chứng cứ hoặc lý do còn thiếu>
BRANCH_COVERAGE: <nhánh và ca: PASS/FAIL/BLOCKED/NOT_TESTED/N-A + lý do>
DELIVERED_OUTPUT: <đường dẫn phiếu kiểm, số ca, mã sổ, bằng chứng đọc lại; thiếu thì ghi CHƯA CÓ>
MISSING_FROM_PROCEDURE: <đúng câu/bước/đường dẫn/định nghĩa xong cần thêm, hoặc KHÔNG>
UI_PRODUCT_STATUS: <PASS|FAIL|BLOCKED|PARTIAL>  # Kết quả sản phẩm UI, TÁCH với việc làm được quy trình rà
```

**Quy tắc đọc kết luận:** `DOER_CONFIRM=YES` chỉ khi agent tự đi hết hướng dẫn và **bàn giao được phiếu rà soát đầy đủ phạm vi** mà không phải hỏi cách làm; UI đang lỗi vẫn có thể được kết luận `BLOCKED/FAIL` **nếu đã phát hiện, đối chiếu nguồn, ghi bằng chứng và hồ sơ đúng**. Nếu mới thử vài ca, chưa phủ hết câu hỏi/nhánh hoặc không tìm được nơi lưu thì `PARTIAL/NO`, **không** dùng 5 ca đạt để kết luận cả quy trình. Host chỉ công nhận bản hướng dẫn sau xác nhận của người làm **và** kiểm được kết quả thật; khi thiếu câu/bước, ghi vào hồ sơ TQT-ISS-003, sửa theo vòng TQT-QT-001 và cho phiên mới thử lại.

**Khuôn đề xuất 6 dòng (không cần viết báo cáo dài):**

```text
TQT-PROPOSAL: <mã duy nhất / tên file>
TARGET: <TQT-QT-001 hoặc TOOL-CTCM-xxx / mã sổ + bước>
TESTED: <ai đã đọc và làm / phiên nguồn / đầu ra thật / link evidence>
BLOCKER_TYPE: <THIEU_HUONG_DAN | THIEU_SAN_PHAM | THIEU_QUYET_DINH | THIEU_QUYEN | LOI_QUY_TRINH>
OBSERVED: <đọc hướng dẫn nào, làm đến bước nào, kết quả thực tế và đúng ra phải là gì>
PROPOSED_CHANGE: <thêm/sửa đúng câu, bước, nhánh, kiểm chứng lại thế nào>
```

Nếu **thiếu chức năng sản phẩm** (ví dụ chưa có nguồn Field thật/JEV) thì nêu `THIEU_SAN_PHAM` và mã issue sản phẩm, **không** viết hướng dẫn giả rằng đã có. Host phân loại trước khi sửa.

### Quyền ghi & phản hồi khi bị chặn (TQT_GATE_V1)

| Vai trò | Được ghi | Không được ghi |
|---|---|---|
| Astra Codex — Host, phiên Owner chỉ định | Nội dung chuẩn/sổ/README trong task sau khi duyệt và kiểm bằng version | Không tự sửa runtime MOW/VPS ngoài phạm vi |
| Mọi AI ngoài phiên Host (GPT Chat/Claude/Codex/Claude Code…) | File đề xuất **riêng** trong `proposals/`; bằng chứng sản phẩm ở task được giao | 3 file chuẩn và sổ TQT trên trang |
| Owner | Góp ý/đề xuất trực tiếp bằng chat; Host ghi lên repo | Không bị yêu cầu thao tác Git/Markdown |

**Hiệu lực:** quy định vai trò và đường nộp đề xuất **đã áp dụng**; cổng từ chối ghi theo danh tính kỹ thuật **CHƯA ĐƯỢC XÁC MINH** (TQT-ISS-006). Github đang khóa push thường theo ruleset `gateway-only-writes`, nhưng gateway có DeployKey chung: **không có nghĩa** mọi AI khác đã bị chặn path.

**Yêu cầu kỹ thuật để hoàn thiện TQT-ISS-006, chưa giả là máy đã làm:** gateway phải xác thực **đúng phiên/bề mặt được Owner giao làm Host** bằng identity server-side, không tin chuỗi tự khai trong commit và không chỉ so `Host_ID=OpenAI-main` (có thể dùng chung nhiều bề mặt). Khi AI khác cố ghi các file chuẩn, trả `HOST_APPROVAL_REQUIRED`, kèm `readme_path=work/tools-quy-trinh/README.md` và `allowed_proposal_path=work/tools-quy-trinh/proposals/TQT-PR-...`; thử được ca từ chối main, cho phép proposal và Host duyệt nhập/kiểm. Nếu lỗi do nguồn bận/xung đột thì trả lỗi thật, không ngụy thành đã bị chặn quyền.

**Không thay luật toàn repo.** Quy ước này chỉ dành cho `work/tools-quy-trinh`. Sổ `OPEN-01…10` ở MOW vẫn sửa tại nguồn MOW tới khi hoàn tất chuyển nguồn TQT-ISS-004.

---
Đọc `../../AGENTS.md` → [§0/Bảng điều khiển](COLLAB.md) trước; lấy mục tiêu, tiêu chí, Host/roster và việc kế tiếp từ đó.

## Mở đúng nội dung

| Cần làm gì | Nguồn phải đọc |
|---|---|
| Owner xem task | [Tools quy trình](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh) |
| Nhìn nhanh có gì, thiếu gì, tắc ở đâu | [Bảng 30 giây](view.html#bang) |
| Nhận diện phạm vi, lớp và nhóm chuyên môn | [Cách phân loại](view.html#phan-loai) |
| Tổ chức câu hỏi từ gốc, ghép với nghiệp vụ | [Ma trận câu hỏi](view.html#ma-tran-cau-hoi) · [Phạm vi Host hiện hành](PROMPT.md); ý kiến ngoài Host gửi riêng |
| Owner cùng xây dựng quy trình hiệu chỉnh | [Quy trình hiệu chỉnh hướng dẫn và quy trình · TQT-QT-001](view.html#quy-trinh-hieu-chinh) — bản thử v0.1 chưa đạt |
| Rà UI đang có, viết ca và lưu kết quả | [Hướng dẫn thực hành](view.html#ra-ui) → 8 câu/MOT, 7 câu Config, khuôn ca, nơi ghi và kiểm lại |
| Đọc đủ 9 Tools, từng bước/câu hỏi | [9 Tool · một khuôn](view.html#tool-9) — bản chép, chưa cắt chuyển nơi sửa |
| Luật dùng chung: công thức, xong khi, đi tới đích, sửa hay ghi sổ, Tool→DOT | [Dùng chung](view.html#dung-chung) |
| Xem áp thử MOW-NHC-001 và các lượt chạy | [Áp thử](view.html#ap-thu) · [Sổ lượt chạy](view.html#so-luot-chay) |
| Nguồn cũ đã chép, nơi đang gọi, cách cắt chuyển | [Chuyển nguồn](view.html#chuyen-nguon) → mở bản cũ tại VPS |
| Ghi/kiểm vấn đề của tools-quy-trinh | [Sổ vấn đề](view.html#so-van-de) — TQT sửa ở đây; OPEN là bản chép, trạng thái hiện hành ở sổ MOW tới khi cắt chuyển |
| Đọc vấn đề và kết quả MOW đã có | [Sổ MOW / Tools](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html#issue-register) · [Kết quả từng lượt](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html#tools-run-register) |
| AI ngoài Host gửi đề xuất sửa quy trình/sổ | Tạo file **riêng** `proposals/TQT-PR-YYYYMMDD-<seat>-<so>.md` gồm mã Tool/vấn đề, ca làm thật, câu/bước cần sửa, đề xuất và bằng chứng; **không sửa** `view.html`/`COLLAB.md`/`README.md` |
| Host duyệt và nhập chuẩn | [TQT-HOST-GATE](COLLAB.md) · Host đối chiếu, chấp thuận/từ chối và cập nhật một nguồn, kiểm kết quả; chưa có chốt chặn quyền máy riêng, theo TQT-ISS-006 |
| Đọc cách góp ý / việc bị tắc | [Cách góp ý](view.html#gop-y) · gửi theo file đề xuất nêu trên, không viết trực tiếp vào sổ chuẩn |
| Tiếp nhận thêm nguồn | Đọc TQT-SOURCES và TQT-REQ trong COLLAB; giữ mã/nguồn/hợp đồng hiện hành |

`view.html` là HTML chính duy nhất. Mục tiêu/tiêu chí/trạng thái điều hành nằm trong COLLAB; sổ vấn đề của task nằm trong `view.html#so-van-de`. Mỗi nội dung có đúng một nơi cập nhật.

Artifact/quy trình được bổ sung về sau phải đăng ký tại đây hoặc danh mục chuẩn được công bố trong task, để phiên tiếp theo biết lúc nào đọc và dùng.
