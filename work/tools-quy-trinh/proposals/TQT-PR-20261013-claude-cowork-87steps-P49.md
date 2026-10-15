# TQT-PR-20261013-claude-cowork-87steps-P49
## Rà độc lập: công thức · QTTH 05/06 · Master · hồ sơ 87 bước MOW001/P46 · 13/10/2026

TQT-PROPOSAL: TQT-PR-20261013-claude-cowork-87steps-P49
REVIEWER: Claude (Anthropic) · bề mặt Claude Chat/Cowork · ghế Claude-review · khác hãng với Host nội dung Codex. Không chuyển Host, không sửa nguồn chính.
STARTED@TQT-P49-CLAUDE-REVIEW 2026-10-13T09:53:04Z · chỉ đọc nguồn + ghi đúng một tệp này.
BASED_ON: HEAD `24eb036` (đọc 09:53–10:11Z). Trong lúc rà HEAD chuyển sang `678cbe9`, commit đó chỉ chạm `work/graph-server/COLLAB.md` ⇒ nguồn tools-quy-trinh không đổi, không phải rà lại.
HASH NGUỒN: view.html `71da448a…` · MOW-TH-006.md `6978349a…` (= `detailed_workflow.source_sha256` = `definition_sha256` của cả 91 sự kiện) · COLLAB.md `cf6bdd7c…` · UI-REVIEW-MOW001.json `c68c20ec…` · UI-REVIEW-AGGREGATE.json `c3521d6b…` · ui/process-work-master-v1.js `9d6e3c6c…`.
TESTED: chỉ đọc. Trích JSON bằng script trong bản chụp cách ly của `workspace_exec` (không ghi nguồn, mỗi lần 15–40 s); đọc mã hiển thị hồ sơ; 2 lần mở UI hồ sơ bằng `ui_inspect` đều lỗi (SCREENSHOT_TIMEOUT rồi BROWSER_UNAVAILABLE) ⇒ phần hiển thị kiểm qua mã renderer, **chưa nhìn bằng trình duyệt**. JEV: `gen-dec-1791886075` (4 câu phân loại CP07.08/03.05/04.13/04.15, đồng thuận 0,91–0,97) · `gen-dec-1791886125` (xếp ưu tiên).
VERDICT: **REQUEST_CHANGES.** Không nghiệm thu P46. TEST PASS, G1 7/7 cũ và lời khai Host không được dùng thay nghiệm thu.

---

## 0. Nhìn 30 giây (phần cho Owner)

**Bảng: lệch** — dòng ✅ ghi "QTTH006 v0.3", nguồn hiện là 0.5; số 48/10/29 đúng nhưng 7 dòng trong đó ghi sai/lỗi thời (mục 3). **Ô 1–2: khớp.**

Ma trận 87 bước theo mốc (đánh giá của Reviewer, không phải của Host):

| Mốc | Số bước | ✅ Đạt | 🟡 Thiếu | ❌ Sai | ➖ Không áp dụng | ❓ Chưa xác minh |
|---|---|---|---|---|---|---|
| CP01 Khai việc | 12 | 9 | 2 | 1 | 0 | 0 |
| CP02 Chuẩn bị | 23 | 17 | 3 | 2 | 1 | 0 |
| CP03 Xác nhận bắt đầu | 11 | 4 | 5 | 1 | 0 | 1 |
| CP04 Làm | 19 | 5 | 5 | 5 | 3 | 1 |
| CP05 Kiểm | 10 | 6 | 2 | 0 | 1 | 1 |
| CP06 Duyệt | 5 | 2 | 3 | 0 | 0 | 0 |
| CP07 Bàn giao | 7 | 1 | 4 | 2 | 0 | 0 |
| **Cộng** | **87** | **44** | **24** | **11** | **5** | **3** |

Đọc nhanh: tắc thật ở **CP03** (chưa có xác nhận bắt đầu) và **CP06** (chưa có quyết định Owner). 11 ô ❌ là lỗi ghi, sửa được trong một lượt.

**5 phát hiện quan trọng nhất**
1. 🔴 **P46 chưa phải phép thử "AI mới làm ra sản phẩm mới".** 91/91 sự kiện do chính Host (tác giả 006) ghi. P02/P03 là bản chép thiết kế G1 (~235 nghìn ký tự mỗi gói) + 2 câu nhận xét giống nhau, đóng gói trong 70 ms; 44/50 đáp án kế thừa từ G1. ⇒ Ô 2 ("người/AI mới làm theo ra đúng sản phẩm") **chưa được kiểm**.
2. 🔴 **Thời gian chưa đo được.** 85/91 sự kiện chỉ có giờ nhập hồ sơ, ghi thành 3 đợt (08:29 · 08:43 · 08:49), nhưng UI vẫn hiện giờ đó ở cột "Thời gian hoàn thành". Chỉ 7 ph 21 s trong 32 ph 25 s có số đo riêng. Tính tới lúc hồ sơ nằm đúng chỗ là 50 ph 48 s, và việc chưa có duyệt/ACK.
3. 🔴 **Hồ sơ còn "ghi nhãn" và 7 trạng thái sai.** 29 bước Bị chặn dùng chung 2 câu lý do, không có issue/người xử lý/bước quay riêng. Ví dụ sai: CP07.08 "khép RUN" ghi Bị chặn dù RUN đã dừng sạch; CP04.06–07 ghi "chưa ghi/đọc lại" dù P47 đã đọc lại PASS.
4. 🟡 **"Không làm" bị dùng để bỏ nghĩa vụ** (CP03.05 rà khác hãng bắt buộc, CP04.13 Master đích chưa có kho, CP04.15 đã sửa UI/bộ kiểm). Cùng lúc mọi sự kiện có `item_key="G1"` ⇒ bước lặp theo câu/trường/kế hoạch bị gộp.
5. 🟡 **Tool có sẵn mà không dùng, Master trùng mã.** CHECK-004 có `--check-history`, `--write-gate` nhưng CP04.17/CP03.06 vẫn Bị chặn; CHECK-006 có `--vps-ui` nhưng Host dựng snapshot tay ⇒ 2 lần chạy hỏng. CAT-003? ≡ ML-DEF-004 (Master MOW), CAT-009? ≡ ML-DEF-005 (Master MOT): cùng URL, chưa gộp mã.

**Giữ nguyên ✅:** hồ sơ G1 không bị đụng (khớp từng byte, sha `ea712bc0`); 87 bước một nguồn, bản chiếu đúng hash; không tô 87/87, không giả ACK Owner; nhãn "đo chung" cho thời lượng dùng chung; phép thử UI thật đã tìm đúng điểm tắc nguồn Field/evaluator.

**❓ Owner gật/lắc:** cho Host làm 3 sửa nhỏ I1–I3 (mục 5) rồi giao **một phiên AI khác hãng** chạy một việc nhỏ mới theo 006 làm nghiệm thu ô 2? **Đề xuất PM: gật.**

---

## 1. Kết luận (a)

**Thiết kế quy trình — dùng được làm khung, chưa đủ chặt.** 005 (7 mốc) + 006 (87 bước) phủ đủ nghĩa vụ, tách được tầng định nghĩa/áp dụng, có nhánh lỗi/hủy/sửa và gọi đúng MOW-TH-002/003. Chưa đạt "muốn làm sai cũng khó" vì: (i) bảng 87 bước chỉ trả lời 4/8 câu của công thức TOOL-CTCM-008 (Làm gì · Xong khi · Đến đâu · Làm bằng gì), thiếu "Ai làm/ai kiểm", "Bàn giao", "Sai thì sao" ở bước thường; (ii) 30 bước KHI viết điều kiện bằng lời, máy không tự xét được ⇒ AI tự phán và phán sai (CP03.05, CP04.13, CP04.15); (iii) cột Tool gắn CHECK-004 cho 42/87 bước nhưng đó là bộ kiểm toàn tệp, không chỉ lệnh/cờ cụ thể; (iv) văn bản còn tự mâu thuẫn (mã bước bổ sung, cột +/−, 3 bộ từ trạng thái, phiên 0.3/0.4/0.5).

**Chất lượng ghi hồ sơ — trung thực ở mức tổng, chưa dùng được làm nghiệm thu.** Không tô 87/87, có 6 issue rõ, không giả duyệt. Nhưng ở mức từng bước: lý do chung chung, 7 trạng thái lỗi thời/sai, thiếu 6 trường sự kiện mà chính 006 §5 quy định, thời gian là giờ nhập, item_key gộp.

**Khả năng chạy thật toàn đường — chưa.** P46 dừng ở CP03; nhánh tìm thành công tắc ở nguồn Field/evaluator (P46-F02); chưa có duyệt/ACK; cổng 006 chưa có chốt máy (P46-F03). Phần CP04–CP05 đã làm là bản nháp trên bản local, chạy sau khi cổng CP03 chưa đạt.

**Khả năng tái dùng — định nghĩa tái dùng được, cách lưu thì không.** 006 viết trung tính, dùng được cho loại việc khác. Bộ kiểm 001–006 tái dùng được nhưng nặng (đọc cả tệp 16 MB, 92 s, cần ~1 GiB). Cách tái dùng sản phẩm G1 bằng **chép nguyên nội dung** (~470 nghìn ký tự cho P02+P03 vào view.html) không nhân rộng được — G1 lưu bằng path+sha, P46 lại chép ra.

---

## 2. Bảng 87 bước (b)

Ký hiệu: ✅ Đạt · 🟡 Thiếu · ❌ Sai · ➖ Không áp dụng · ❓ Chưa xác minh.
Nguồn (mọi đường dẫn nằm trong `view.html › catalog.work_schedule.records[record_id=TQT-VIEC-001].detail_tracking`): **ev** = `events` bản mới nhất của bước · **obs** = `cycle.observations[bước]` · **tr** = `cycle.tool_runs` · **br** = `cycle.browser_receipt` · **fs** = `cycle.fullsuite` · **mr** = `cycle.master_records` · **pub** = `cycle.publication` · **pc** = `cycle.placement_check`. "Lý do chung" = một trong 2 câu lặp lại ở 29 bước Bị chặn.

### CP01 · Khai việc (12)
| Mã | Yêu cầu / xong khi | Thực tế · nguồn | KL | Vấn đề / đề xuất tối thiểu |
|---|---|---|---|---|
| CP01.01 | Đọc yêu cầu Owner + điều cấm; rõ mục tiêu/người giao/nguồn | ev DONE; obs: mục tiêu, loại trừ PG/G2/G3/TEST | ✅ | Nguồn chỉ ghi "P46" — trỏ đúng dòng COLLAB P46 |
| CP01.02 | Đối chiếu A0, phạm vi/quyền | ev DONE; obs A0_confirmed=true, PG=false | ✅ | — |
| CP01.03 | Tra mã việc trước khi mở; không trùng | ev DONE; obs TQT-VIEC-001 unique; ghi tool CHECK-005 nhưng tr không có lượt CHECK-005 nào trước 08:29 | ✅ | Kết quả đúng; không ghi tool khi không có biên nhận |
| CP01.04 | Ghi mã việc/người giữ/nguồn; mở đúng ID | ev BLOCKED "chưa ghi/đọc lại trên VPS (VPSC giữ)"; pub.readback PASS 09:09:44Z; `application_id` = id G1 cũ | ❌ | Lý do hết hiệu lực sau P47; vòng làm lại dùng lại id G1, trái 006 §7. Thêm sự kiện rev2; cấp id mới cho vòng (F4, F8) |
| CP01.05 | Ghim 005/006 đúng phiên | ev DONE; 005@1.1-design, 006@0.5, sha 6978349a = tệp | ✅ | `catalog.records` vẫn ghi 006@0.4 (F13) |
| CP01.06 | Đối chiếu đối tượng + con | ev DONE; MOW-NHC-001, MOT 1.1–1.3, nguồn MOW001-G1-IC | ✅ | Hai mã cho cùng Master MOW/MOT (F10) |
| CP01.07 | Chốt sản phẩm/phạm vi/loại trừ | ev DONE; obs phạm vi G1, loại trừ G2/G3/PG | ✅ | — |
| CP01.08 | Gắn link + phiên nguồn | ev DONE; tool "SSH chỉ đọc"; obs hash từng tệp | ✅ | SSH không có trong Master Tool, định nghĩa ghi MCP workspace_read/stat — đăng ký hoặc đi đúng cổng |
| CP01.09 | Người nhận cuối, nơi gọi/trả | ev DONE; người nhận "Owner trong cuộc trò chuyện này" | ✅ | Ghi định danh bền (Owner + kênh) thay "cuộc trò chuyện này" |
| CP01.10 | Người làm/kiểm/duyệt có căn cứ; không giả quorum | ev DONE; obs: làm = Codex Host, kiểm = DOT004/005/006 của Host, independent_review=false | 🟡 | Người kiểm là script của người làm; Cross_Vendor_Review=REQUIRED (AGENTS) chưa có ghế khác hãng |
| CP01.11 | Khởi tạo binding + sổ sự kiện, ban đầu Trống | ev DONE; binding 006@0.5 + 91 sự kiện nằm trong DEF00.1 (sau P47) | ✅ | Binding gắn id G1 cũ (xem CP01.04) |
| CP01.12 | Cổng CP01 | ev BLOCKED, lý do chung; new_cycle_checkpoint_acceptance=false | 🟡 | Trạng thái đúng (chưa qua); lý do lỗi thời — tắc thật là chưa có id/cửa ghi cho vòng mới (P45-F03) |

### CP02 · Chuẩn bị đủ (23)
| Mã | Yêu cầu / xong khi | Thực tế · nguồn | KL | Vấn đề / đề xuất tối thiểu |
|---|---|---|---|---|
| CP02.01 | Nạp câu hỏi bắt buộc | ev DONE; 50 câu, ma trận c6992e77 | ✅ | — |
| CP02.02 | Ghi đáp án theo item_key câu hỏi | ev DONE; answered 50, inherited 44 | ✅ | 44/50 kế thừa G1 (checked_at 12/10) — ghi rõ "tái dùng"; 50 câu gộp 1 sự kiện (F6) |
| CP02.03 | Ghim nguồn + hash; đọc lại đúng phiên | ev DONE; P01.read_receipt READ_AND_VALIDATED | ✅ | Không có bản ghi ở CAT-239* là nơi ghi định nghĩa (F10) |
| CP02.04 | Kiểm quyền đọc nguồn thật | ev DONE; tool SSH; obs đọc thành công | ✅ | Biên nhận chỉ trong obs, không có bản ghi CAT-015 cho bước này |
| CP02.05 | Gắn Master đích cho mọi nghĩa vụ ghi | ev DONE; obs 11 nhóm RG → Master | ✅ | — |
| CP02.06 | Lập/ghim hợp đồng CAT-206* | ev DONE; ghim MOW001-G1-IC v5 | ✅ | Tái dùng hợp lý; ghi `reuse_ref` vì kho CAT-206* đang MISSING |
| CP02.07 | Định nghĩa từng field | ev DONE; 66 field, schema 1.4 | ✅ | Tái dùng; 66 field gộp 1 sự kiện (F6) |
| CP02.08 | Ánh xạ nguồn → đích | ev DONE; 66 dòng | ✅ | — |
| CP02.09 | Trường bắt buộc của gói ra | ev DONE; contract_ref + tiêu chí | ✅ | — |
| CP02.10 | Trường phải nhận + người nhận | ev DONE; P01→P02 … P05→Owner; ACK bước ≠ ACK Owner | ✅ | — |
| CP02.11 | Nhánh lỗi/thiếu/hủy/không quyền | ev DONE; P02/P03: 3 MOT, 21 nhánh | ✅ | — |
| CP02.12 | Bộ ca đúng/sai/rỗng/sai phiên/sai người nhận | ev DONE; 11 ca (INPUT, FOUND, ABSENT, …, STALE, CALLER, CANCEL), sha fe10237f | ✅ | Tái dùng ca G1; đủ loại yêu cầu |
| CP02.13 | Đối chiếu giao điểm giữa các MOT (cạnh từ CAT-206*) | ev DONE; obs chỉ có chuỗi P01→P05 + "DOT001/002 chạy ở bộ tổng" | ❌ | Đã kiểm chuỗi kế hoạch, không kiểm cạnh MOT 1.1→1.2→1.3; tool gợi ý CHECK-002 (kiểm mã) cũng không kiểm cạnh. Sửa phép kiểm + tool gợi ý |
| CP02.14 | Liệt kê mọi nghĩa vụ ghi | ev DONE; 34 nghĩa vụ | ✅ | — |
| CP02.15 | Phân biệt thiếu sổ/chưa ghi/chưa quyền | ev DONE; obs P45-F03 + cách kiểm | ✅ | — |
| CP02.16 | Xác định bước áp dụng theo từng item_key, biết bước đến hạn | ev DONE; obs "đánh giá tại bước" | 🟡 | Hoãn phân loại, không có danh sách bước áp dụng ⇒ về sau CP03.05/04.13/04.15 xét sai |
| CP02.17 | Rà bước thêm/bỏ/thay | ev NOT_DONE; added_steps=[] | ➖ | Đúng |
| CP02.18 | Kế hoạch việc con | ev DONE; P01–P05, phụ thuộc thẳng | ✅ | — |
| CP02.19 | Giao người làm/kiểm/nhận | ev DONE; P01–03/P05 Codex; P04 "DOT readers + browser" | ✅ | P04 không độc lập (cùng chủ) |
| CP02.20 | Đầu ra + nơi ghi từng việc con | ev DONE; product_keys P01–P05 | ✅ | — |
| CP02.23 | Cổng ghi + biên nhận quyền trước lần ghi đầu | ev BLOCKED, lý do chung | 🟡 | Chưa có biên nhận; `CHECK-004 --write-gate` có sẵn chưa chạy; P47 ghi qua CAS nhưng không cập nhật bước này |
| CP02.21 | Tạo/ghi P01, đọc lại trước CP03; chỉ ghi sau CP02.23 | ev BLOCKED "đang chờ ghi/đọc lại"; mr CAT-228* P46-P01 "đã ghi trong hồ sơ"; pub.readback PASS | ❌ | Mâu thuẫn trong cùng hồ sơ; P01 lại được ghi khi CP02.23 còn Bị chặn — trái chú thích của chính bước |
| CP02.22 | Cổng CP02 | ev BLOCKED, lý do chung | 🟡 | Trạng thái đúng |

### CP03 · Xác nhận bắt đầu (11)
| Mã | Yêu cầu / xong khi | Thực tế · nguồn | KL | Vấn đề / đề xuất tối thiểu |
|---|---|---|---|---|
| CP03.01 | Tool/DOT sẵn sàng: ID/phiên/hash/quyền | ev DONE; 6 CHECK; tr 4 lượt; mr CAT-229* 4 | ✅ | — |
| CP03.02 | Xác thực người làm qua quyền ngoài hồ sơ | ev DONE; transaction d115410e | ✅ | — |
| CP03.03 | Reviewer được phân công + quyền kiểm | ev NOT_DONE "Owner đã cho phép thiếu Claude" | ❓ | Không dẫn nguồn lời Owner; TQT-GATE-001 đòi N/A có lý do + người duyệt |
| CP03.04 | Kế hoạch đúng bản | ev DONE | ✅ | — |
| CP03.05 | Rà độc lập hợp đồng khi quy tắc đòi | ev NOT_DONE "không có reviewer khác hãng" | ❌ | Quy tắc có đòi (Cross_Vendor_Review=REQUIRED) ⇒ là nghĩa vụ ⇒ phải Bị chặn, không được Không làm. JEV 0,97 |
| CP03.06 | Kiểm lại schema/khóa/đường ghi | ev BLOCKED, lý do chung | 🟡 | Chạy `CHECK-004 --write-gate` là có bằng chứng |
| CP03.07 | Biên nhận quyền còn hiệu lực | ev BLOCKED, lý do chung | 🟡 | Phụ thuộc CP02.23 |
| CP03.08 | Bên nhận đọc P01 trước CP03 | ev DONE, đo riêng 611 ms = tr preparation | ✅ | tool_uses để trống dù có lượt chạy; "bên nhận" là script cùng chủ |
| CP03.09 | Giải quyết issue chặn bắt đầu | ev BLOCKED, lý do chung | 🟡 | Ghi đúng issue (P45-F03/P46-F03) + người xử lý + hạn |
| CP03.10 | Xác nhận bắt đầu đúng người/phiên → CAT-025 | ev BLOCKED | 🟡 | Đúng: chưa có xác nhận |
| CP03.11 | Tính lại CP01–03; chưa đạt thì dừng | ev BLOCKED | 🟡 | Đúng là chưa đạt — nhưng CP04/CP05 vẫn làm tiếp (F7) |

### CP04 · Làm theo quy trình (19)
| Mã | Yêu cầu / xong khi | Thực tế · nguồn | KL | Vấn đề / đề xuất tối thiểu |
|---|---|---|---|---|
| CP04.01 | Chọn việc con đủ phụ thuộc | ev BLOCKED, lý do chung | ❌ | Mâu thuẫn: CP04.02–04.05 ghi Đã làm. Hoặc bước này DONE (đã chọn P01–03), hoặc các bước sau là nháp |
| CP04.02 | Bên làm đọc/kiểm gói vào | ev DONE; evidence preparation | ✅ | Làm khi cổng CP03 chưa đạt ⇒ là nháp |
| CP04.03 | Chọn DOT/Tool đúng phiên | ev DONE "tái dùng DOT004" | ✅ | tool_uses trống |
| CP04.04 | Tạo sản phẩm việc con có identity/output_version | ev DONE; P01–P03 output_version P46.1; P02/P03: reused_content 234.043/237.109 ký tự + new_findings 152 ký tự (giống nhau); đóng gói 70 ms | ✅ | Đúng hình thức nhưng là đóng gói lại G1, không chứng minh tạo được sản phẩm mới (F1). Lưu tái dùng bằng path+sha như G1 |
| CP04.05 | Kiểm gói TRƯỚC khi ghi | ev DONE rev2; CHECK-005 trong fs, 92 s đo chung | ✅ | Kiểm trên bản local (published=false) |
| CP04.06 | Ghi qua cửa máy chủ | ev BLOCKED "chưa ghi (VPSC)"; P47 ghi hồ sơ 09:03:55Z, KQ 09:06:31Z | ❌ | Lỗi thời: thêm rev2 trỏ commit 3b7bad9 |
| CP04.07 | Đọc lại, so hash | ev BLOCKED; pub.readback PASS 09:09:44Z, 87 dòng | ❌ | Lỗi thời: thêm rev2 trỏ pub.readback |
| CP04.08 | Gửi lệnh với khóa chống trùng | ev BLOCKED, lý do chung | 🟡 | P47 dùng CAS nhưng không ghi khóa/biên nhận vào CAT-238* |
| CP04.09 | Bên nhận kiểm + ACK bước | ev BLOCKED, lý do chung | 🟡 | — |
| CP04.10 | Gửi trùng → chặn | ev NOT_DONE: không phát sinh | ➖ | — |
| CP04.11 | Phản hồi cũ → so phiên, từ chối | ev NOT_DONE: không có | ❓ | P46-F05 ghi "pin UI trong registry chưa đồng bộ" — có thể đúng là ca phiên cũ; cần xác minh |
| CP04.12 | Mất quyền → CAT-017 | ev NOT_DONE | ➖ | Khóa VPS-GHI là lease, không phải permission_denied — chấp nhận |
| CP04.13 | Thiếu Master đích → issue CAT-069? | ev NOT_DONE "không phát sinh thiếu Master" | ❌ | CAT-228*/229*/232*/244*/206* có source_state MISSING ⇒ điều kiện đã xảy ra. JEV 0,96 |
| CP04.14 | Dữ liệu sai → QTTH002 | ev NOT_DONE | ➖ | — |
| CP04.15 | Sửa quy trình/UI/hợp đồng → QTTH003, tăng phiên, CAT-016 | ev NOT_DONE "không sửa logic" | ❌ | Lượt này đã phát hành cột thời gian UI v1 (d115410e), sửa CHECK005 và có bản ghi CAT-016 "UI-TIME" ⇒ nhánh đã áp dụng. JEV 0,97 |
| CP04.16 | Hủy → CAT-244* | ev DONE; br; mr CAT-244* CANCEL | ✅ | — |
| CP04.17 | Dấu lịch sử bất biến | ev BLOCKED, lý do chung | 🟡 | `CHECK-004 --check-history` (17 ca) có sẵn — chạy là xong |
| CP04.18 | Đóng việc con khi có output_ref | ev BLOCKED | 🟡 | Đúng |
| CP04.19 | Cổng CP04 | ev BLOCKED | 🟡 | Đúng |

### CP05 · Kiểm đầu ra (10)
| Mã | Yêu cầu / xong khi | Thực tế · nguồn | KL | Vấn đề / đề xuất tối thiểu |
|---|---|---|---|---|
| CP05.01 | Nạp bộ ca CP02 | ev DONE | ✅ | — |
| CP05.02 | Reviewer tự mở bản; log ID/phiên/hash | ev DONE rev2; CHECK-005 trên bản local | ❓ | Log chỉ có stdout_sha256; nội dung nằm ở `work/p46/…` trên máy Host, không có trong repo ⇒ người khác không mở lại được; không có reviewer |
| CP05.03 | Chạy ca, ghi actual/expected | ev BLOCKED | 🟡 | 11 ca có sẵn; chưa có bảng actual/expected cho P46 |
| CP05.04 | UI: thử nút/nhánh thật | ev DONE; br 08:34:33→08:40:21Z (348 s) | ✅ | Giá trị thật: tìm ra thiếu nguồn Field/evaluator (P46-F02); tool_uses trống |
| CP05.05 | Kiểm nội dung thiết kế từng MOT | ev DONE rev2; tr designs 725 ms + fs | ✅ | Bản local; 3 MOT gộp 1 sự kiện |
| CP05.06 | Trả cuối đúng caller/phiên | ev DONE; br: nơi gọi nhận sự kiện hủy, phiên 3 | ✅ | Chỉ nhánh hủy; nhánh trả kết quả thành công chưa chạy được (do F02) |
| CP05.07 | G2/G3 live | ev NOT_DONE: phạm vi G1 | ➖ | — |
| CP05.08 | Ca FAIL → issue/người sửa/bước quay | ev DONE; 6 issue P46-F01…F06 | ✅ | F01 ghi FIXED trong khi chính P46 vẫn ghi giờ hồi tố ⇒ nên ghi FIXED_FOR_NEXT_RUN |
| CP05.10 | Bộ kiểm tổng đúng phiên | ev DONE rev2; fs PASS 92,05 s; pc (P47) PASS 93,4 s | ✅ | Gắn thêm pc vì bản local đã đổi sau P47 |
| CP05.09 | Cổng CP05 | ev BLOCKED | 🟡 | Đúng |

### CP06 · Duyệt kết quả (5)
| Mã | Yêu cầu / xong khi | Thực tế · nguồn | KL | Vấn đề / đề xuất tối thiểu |
|---|---|---|---|---|
| CP06.01 | Gom gói trình duyệt | ev DONE; mr CAT-025 "P46 · chờ quyết định Owner" | ✅ | — |
| CP06.02 | Xác thực người duyệt | ev DONE: Owner | ✅ | — |
| CP06.03 | Xin quyết định | ev BLOCKED: chưa có Owner | 🟡 | Đúng, không giả duyệt — giữ |
| CP06.04 | Ghi quyết định + product_binding | ev BLOCKED | 🟡 | Đúng |
| CP06.05 | Cổng CP06 | ev BLOCKED | 🟡 | Đúng |

### CP07 · Bàn giao · kết thúc (7)
| Mã | Yêu cầu / xong khi | Thực tế · nguồn | KL | Vấn đề / đề xuất tối thiểu |
|---|---|---|---|---|
| CP07.01 | Tạo gói bàn giao P05 | ev BLOCKED (chờ Owner) | 🟡 | Tạo gói không cần ACK nhưng cần CP06 — đúng là chưa |
| CP07.02 | Kiểm hợp đồng nhận cuối | ev BLOCKED | 🟡 | — |
| CP07.03 | Ghi giao đúng bản → CAT-232* | ev BLOCKED; mr CAT-232* đã có "P46 · gói chuẩn bị trình Owner" | ❌ | Gói trình duyệt nằm trong sổ bàn giao: hoặc sai sổ (thuộc CAT-025/CP06.01), hoặc trạng thái sai |
| CP07.04 | ACK thật | ev BLOCKED | 🟡 | Đúng |
| CP07.06 | Kiểm liên tục CP01–07 | ev BLOCKED | 🟡 | Đúng |
| CP07.07 | Bài học/tool/việc còn mở | ev DONE; mr CAT-233* HISTORY | ✅ | — |
| CP07.08 | Khép RUN, nhả cờ; được DỪNG sạch ở mọi mốc | ev BLOCKED "chưa ACK Owner"; cycle.closed_at 08:51:21Z; dọn 08:47:49Z không tiến trình/khóa; P47 KQ XONG | ❌ | Điều kiện xong của chính bước đã đạt (KQ = DỪNG sạch). Ghi DONE; ACK Owner thuộc CP07.04. JEV 0,91 |

Đối chiếu với phân loại Host: 48 Đã làm → 44 ✅, 2 🟡 (CP01.10, CP02.16), 1 ❌ (CP02.13), 1 ❓ (CP05.02). 10 Không làm → 5 ➖, 3 ❌ (CP03.05, CP04.13, CP04.15), 2 ❓. 29 Bị chặn → 22 🟡 (đa số ghi đúng là còn tắc, chỉ thiếu lý do riêng), 7 ❌ (CP01.04, CP02.21, CP04.01, CP04.06, CP04.07, CP07.03, CP07.08).

---

## 3. Bảng phát hiện (c)

| ID | Mức | Nguồn chính xác | Bằng chứng / tái hiện | Ảnh hưởng | Sửa tối thiểu · nơi sửa | Phép kiểm sau sửa |
|---|---|---|---|---|---|---|
| F1 | 🔴 | `events[].actor`; `cycle.products.P02/P03.reused_content`, `.new_findings`; `cycle.product_build_receipt`; obs CP02.02 | 91/91 actor "Codex Host"; P02/P03 chép 234–237 nghìn ký tự từ G1 (G1 chỉ lưu path+sha) + 152 ký tự nhận xét giống nhau; đóng gói 70 ms; 44/50 đáp án kế thừa. `result_summary` lại viết "tái lập từ nguồn thật" | Ô 2 chưa được kiểm; người đọc hiểu nhầm là đã có sản phẩm mới. MOW-TH-003 bước 5 (agent khác thử lại) chưa làm | Đổi lời tóm tắt thành "đóng gói lại G1 + thao tác UI thật"; lưu phần tái dùng bằng path+sha. Chạy phép thử 006 §4 mục 5 bằng **một phiên AI khác hãng** · `cycle.result_summary`, `cycle.products` | Hồ sơ việc nhỏ mới: actor ≠ tác giả 006, không câu hỏi thêm, sản phẩm có hash khác nguồn |
| F2 | 🔴 | `events[].timing_basis`, `.at`, `.completed_at`; `ui/process-work-master-v1.js` khoảng dòng 80 (`finished:`) | 85/91 RECORDING_ONLY; `at` dồn 3 đợt: 32 sự kiện 08:29, 55 sự kiện 08:43, 4 sự kiện 08:49. Renderer hiện `completed_at` ở cột "Thời gian hoàn thành" cho mọi bước DONE, trái chính dòng hướng dẫn của cột ("không dùng giờ nhập hồ sơ thay giờ xong"). 92.052 ms gắn cho 4 bước | Owner thấy giờ "hoàn thành" là giờ chép; không dựng lại được dòng thời gian; không làm chuẩn năng suất được | (1) Máy ghi giờ thật khi làm (I1). (2) Renderer: không hiện "Thời gian hoàn thành" khi `timing_basis=RECORDING_ONLY`, hiện "chưa đo" · `process-work-master-v1.js` | Lượt sau ≥ 80% bước có khoảng đo thật; UI không còn giờ cho RECORDING_ONLY |
| F3 | 🔴 | `events[]` (29 bước BLOCKED); 006 §5 danh sách trường sự kiện | 29 Bị chặn dùng 2 câu lý do; 26/29 cùng một câu hành động. Sự kiện thiếu `status, adjustment, evidence_ref, issue_ref, owner, return_to` mà 006 §5 quy định — một phần bị nhét vào `result_ref` dạng chuỗi JSON. 78/87 bước `tool_uses` trống dù có tr/br | AI mới không biết bước nào tắc vì đâu, ai gỡ, khi nào chạy lại; máy không kiểm được | Thêm đủ trường thật; Bị chặn bắt buộc `issue_ref` riêng + `owner` + `return_to` + `NEXT_TRIGGER`; `tool_uses` lấy từ `tool_runs` · ghi hồ sơ + CHECK-005 | CHECK-005 từ chối Bị chặn không có issue_ref; số câu lý do trùng ≤ số issue thật |
| F4 | 🔴 | `events` rev1 của CP01.04, CP02.21, CP04.01, CP04.06, CP04.07, CP07.03, CP07.08; `cycle.publication.readback`; `cycle.master_records[CAT-228*, CAT-232*]`; `cycle.closed_at`; aggregate `cleanup` | Hồ sơ vừa nói "chưa ghi/đọc lại" vừa có readback PASS và CAT-228* "đã ghi"; CP07.08 Bị chặn dù RUN đã đóng 08:51:21Z, dọn sạch 08:47:49Z | AI mới sẽ làm lại việc đã xong hoặc giữ RUN chờ ACK — trái DROOT50 | Thêm sự kiện revision mới (không xóa cũ) cho 7 bước; luật kiểm: Bị chặn mà đã có bằng chứng xong ⇒ lỗi · `detail_tracking.events` + CHECK-005 | Ca âm "Bị chặn nhưng readback PASS" ⇒ exit 1 |
| F5 | 🟡 | ev CP03.05, CP04.13, CP04.15, CP03.03; TQT-GATE-001 (`checkpoint_policy.common`); AGENTS `Cross_Vendor_Review` | Ba bước Không làm trong khi điều kiện đã xảy ra/nghĩa vụ bắt buộc (bằng chứng ở bảng mục 2); CP03.03 không dẫn nguồn miễn trừ | Nghĩa vụ bị bỏ mà không ai phát hiện; 006 tự viết "Không làm không dùng để bỏ … kiểm, duyệt" nhưng không có chốt | 30 bước KHI thêm điều kiện máy đọc được (`required_when` trỏ dữ liệu; vd CP04.13 ⇐ có Master đích source_state=MISSING); Không làm ở bước nghĩa vụ cần người duyệt + nguồn · 006 §2 cột Ghi chú → `detailed_workflow` + CHECK-005 | Ca âm "Không làm khi điều kiện đúng" ⇒ FAIL |
| F6 | 🟡 | `events[].item_key` | 91/91 `item_key="G1"`; CP02.02 (50 câu), CP02.07 (66 field), CP04.04 (3 plan), CP05.05 (3 MOT) chỉ 1 dòng | Trái 006 §1 ("sinh bản áp dụng theo item_key") và P49; nghĩa vụ từng mục không truy được | Máy sinh sự kiện theo item_key cho bước lặp (I1) | CP02.02 có 50 item, CP04.04 có 3 plan_id |
| F7 | 🟡 | ev CP03.11/CP04.01 (Bị chặn) vs CP04.02–05, CP05.x (Đã làm); chú thích CP02.21 "chỉ ghi sau CP02.23" | Làm sau cổng chưa đạt; P47 ghi P01 khi CP02.23 còn Bị chặn | Không phân biệt "làm độc lập hợp lệ" với "vượt cổng" | Thêm một luật vào 006 §1: bước sau cổng chưa đạt chỉ được Đã làm dạng nháp (`draft=true`, `published=false`), không tính cho mốc sau · 006 §1 + CHECK-005 | Đếm Đã làm sau cổng chưa đạt mà không có draft ⇒ FAIL |
| F8 | 🟡 | `detail_tracking.application_id`; record TQT-VIEC-001 `lifecycle_state`, `actual_finish`; 006 §7 | Vòng P46 dùng `MOW-NHC-001-G1-20261010-01` (id G1); bản ghi việc vẫn DELIVERED, xong 12/10 | Danh sách việc hiện "đã giao" trong khi vòng mới đang dừng ở CP03 — trạng thái cũ hiện như mới | Id mới cho mỗi vòng; thêm `current_cycle_id`, `cycle_state` ở bản ghi việc (không đụng G1) · DEF00.1 | Danh sách việc hiện "P46 · DỪNG ở CP03" |
| F9 | 🟡 | `tool_registry.records` (CHECK-004/006 purpose); `cycle.issues` P46-F06; `tool_runs[].argv`; 006 cột Tool | `--check-history` (17 ca), `--write-gate`, `--vps-ui` có sẵn nhưng không dùng; snapshot tay thiếu aggregate + 2 tệp UI ⇒ 2 lần chạy hỏng (lỗi chuẩn bị, không phải lỗi tool), thời gian hai lần hỏng không được ghi. CHECK-004 gắn 42/87 bước nhưng là bộ kiểm cả tệp; TOOL-CTCM-001/003/005 ghi "(nếu dùng được)" | AI làm tay việc máy làm được; tốn thời gian; AI mới không biết gọi lệnh nào | Ghi đúng lệnh + cờ ở cột Tool: CP02.23/CP03.06 `--write-gate`, CP04.17 `--check-history`, CP05.10 `--vps-ui`; bỏ "(nếu dùng được)" hoặc đổi thành "quy trình tham khảo" · 006 §2 | Lượt sau `tool_uses` khớp `tool_runs`; 0 lần hỏng do snapshot |
| F10 | 🟡 | xem bảng mục 4 | Master trùng mã, Master đích không có kho, bản ghi không trỏ bước | Không gom được theo Master; nhân rộng sẽ đẻ trùng | Xem mục 4 | CHECK-005 bắt trùng URL; mỗi bản ghi có `step_refs` |
| F11 | 🟡 | 006 §2 tiêu đề bảng; công thức TOOL-CTCM-008 ("8 câu") ở `#dung-chung` | Bảng 87 bước không có cột vai làm/kiểm/duyệt | Không chặn được "người làm tự kiểm" (CP01.10, CP03.05, CP05.02) | Thêm 1 cột "Vai" (Host · Reviewer khác hãng · Owner · Máy) · 006 §2 | CHECK-005: bước vai Reviewer mà actor = Host ⇒ FAIL |
| F12 | 🟢 | `UI-REVIEW-AGGREGATE.json#host_review_P46` vs `detail_tracking` | 85/91 sự kiện khác nhau (ngoài trường record_ref); elapsed 1828,9 s vs 1945,4 s; aggregate vẫn ghi "LOCAL_PREPARED_NOT_PUBLISHED" | Hai nguồn bằng chứng lệch nhau | Aggregate chỉ giữ con trỏ + sha tới DEF00.1 | So sha con trỏ = sha bản ghi |
| F13 | 🟢 | `catalog.records[MOW-TH-006].version`; MOW-TH-006.md §1, §3, 8 bảng; COLLAB P46/P47 | Phiên 0.3 (Bảng) / 0.4 (records) / 0.5 (tệp); 8 bảng MD có tiêu đề 6 cột nhưng dòng kẻ 8 cột ⇒ GitHub không hiện thành bảng; §1 dùng BS-001 còn §3 dùng `006.CP02.08+B01`; §1 nói "không có cột +/−" nhưng §3 mẫu có "☑ + Bổ sung"; 3 bộ từ trạng thái (Trống/Hoàn thành/Vướng · DONE/NOT_DONE/BLOCKED · NA); chữ dính liền ("làm lại001", "hồ sơP46 trênVPS"); cột "Kết quả / nơi đã ghi" hiện chuỗi JSON thô | Người đọc khó hiểu, AI dễ hiểu sai | Sửa một lượt: phiên ở records; dòng kẻ 6 cột; thống nhất BS-001 và một bộ từ; giữ dấu cách; hiện result_ref dạng gọn | CHECK-002 so phiên records = detailed_workflow; render MD thấy bảng |

---

## 4. Thiếu / trùng Master và trường (d)

| # | Master / trường | Vấn đề | Bằng chứng | Hướng xử lý trong nguồn hiện có |
|---|---|---|---|---|
| M1 | CAT-003? ↔ ML-DEF-004 (Master MOW) | Cùng một Master hai mã, chưa gộp | `record_control.masters[CAT-003?].home` = `mow-master-nhap2-v1.html` = `ML-DEF-004.url` (registry STT Master MOW) | Thêm binding vào `catalog.master_identity.bindings` như CAT-006/ML-DEF-024; giữ dấu ? tới khi Host xác minh |
| M2 | CAT-009? ↔ ML-DEF-005 (Master MOT) | Như M1 | `home` = `mot-master-v1.html` = `ML-DEF-005.url` | Như M1. `master_identity_check` PASS (47 dòng/46 Master) mà không bắt được — thêm luật trùng URL |
| M3 | DEF 00.1 ↔ CAT-227* | Đã gộp nhưng ghi ở chỗ riêng | `work_schedule.master_identity`, không có trong `catalog.master_identity` | Đưa về một nơi duy nhất `catalog.master_identity` |
| M4 | CAT-006 ↔ ML-DEF-024 (Master DOT) | Đã gộp đúng (khớp P49). Nhưng CHECK001–006 đăng ký dưới Master DOT, còn 006 gọi là "Tool use" và CP03.01 nhắc ML-DEF-023 Master Tool | `tool_registry.records[].master_code = CAT-006` | Ghi một câu: CHECK00x thuộc Master DOT (hoặc Tool) — chọn một |
| M5 | Kho của Master đích | 6 Master `source_state=MISSING` (CAT-228*, 229*, 232*, 244*, 206*, 226*); cả 18 thiết kế Master đều DESIGN_ONLY ⇒ bản ghi P46 nằm trong `cycle.master_records` (10 khối) của chính hồ sơ việc; R04a (kho thử ngoài PG, mỗi Master một khối) vẫn 🔴 | `record_control.masters[].source_state`; `work_master_designs.records[].state` | Owner/Host chọn một: coi `master_records` là kho thử chính thức (thêm `step_refs`), hoặc tách tệp kho thử theo PR-22. Chưa chọn thì CP04.13 phải ghi issue |
| M6 | 8 bước Đã làm không có bản ghi ở Master đích | CAT-206* × 6 (CP02.06–02.11), CAT-239* (CP02.03), CAT-012 (CP02.12) | `cycle.master_records` không có khối các mã này | Ghi `reuse_ref` trỏ bản G1 (hợp đồng v5, 11 ca, hash nguồn) |
| M7 | Bản ghi Master không trỏ về bước | 22 bước Đã làm có khối Master nhưng chỉ CP05.10 được bản ghi nhắc tên bước | quét `master_records` theo mã bước | Thêm `step_refs`/`event_ids` vào từng bản ghi |
| M8 | Số đếm tóm tắt lệch | `master_coverage.new_records` so `master_records`: CAT-015 4/6 · CAT-069? 4/6 · CAT-229* 3/4 · CAT-228* 3/8 (5 bản là lịch sử G1 chép vào khối P46) | `cycle.master_coverage` vs `cycle.master_records` | Tính bằng máy; bản G1 chỉ để `reuse_ref` |
| M9 | Trường sự kiện | Thiếu `status, adjustment, evidence_ref, issue_ref, owner, return_to` (006 §5) | tập khóa của 91 sự kiện | Xem F3 |
| M10 | Trường của bản ghi việc | Không có `current_cycle_id`, `cycle_state` | record TQT-VIEC-001 | Xem F8 |
| M11 | CAT-069? | Còn dấu ? (UNVERIFIED) nhưng là nơi ghi issue chính, dùng ở 5 bước | `record_control.masters[CAT-069?]` | Host xác minh alias trước khi nhân rộng (006 đã yêu cầu) |

---

## 5. Thời gian (e)

**Đã xác minh từ nguồn (UTC):**

| Mốc | Giờ | Nguồn |
|---|---|---|
| Bắt đầu lượt P46 | 08:18:56 | `cycle.started_at` |
| CHECK-004 `--read-preparation` | 08:26:46 (611 ms) | `tool_runs` |
| Ghi đợt 1: 32 sự kiện | 08:29:25–26 | `events[].at` |
| CHECK-004 `--read-designs` + `--check-g1-ui` chạy song song | 08:31:55 (725 ms / 442 ms) | `tool_runs` |
| Thao tác UI thật | 08:34:33 → 08:40:21 (347,96 s) | `browser_receipt` |
| Đóng gói P01–P03 | 08:43:11 (70 ms) | `product_build_receipt` |
| Ghi đợt 2: 55 sự kiện | 08:43 | `events[].at` |
| CHECK-006 (001–005) | 08:45:04 → 08:46:36 (92,05 s) | `tool_runs`, `fullsuite` |
| Dọn tiến trình/khóa | 08:47:49 | aggregate `cleanup` |
| Ghi đợt 3: 4 sự kiện | 08:49:24 | `events[].at` |
| Khép RUN P46 | 08:51:21 → **32 ph 25 s** từ lúc bắt đầu | `cycle.closed_at` |
| P47 đặt hồ sơ đúng chỗ | 09:00:40 → 09:06:31 (~5 ph 51 s); bộ kiểm 93,4 s | COLLAB P47, `placement_check` |
| Đọc lại hồ sơ đúng chỗ | 09:09:44 → **50 ph 48 s** từ lúc bắt đầu | `publication.readback` |

**Phần đo riêng trong P46:** 0,611 + 0,725 + 347,96 + 0,070 + 92,05 ≈ 441 s ≈ **7 ph 21 s (22,7%)** của 32 ph 25 s.
**Chưa đo được:** ~25 phút còn lại (đọc, suy nghĩ, dựng snapshot, 2 lần chạy bộ kiểm bị hỏng, ghi JSON); thời gian từng bước (81/87 bước chỉ có giờ nhập); thời gian tới duyệt/ACK (CP06–07 chưa diễn ra) ⇒ **chưa có thời gian hoàn thành toàn việc**. "32 phút 25 giây" chỉ là thời gian tới khép RUN. Không dùng các số này làm chuẩn năng suất.
**Cộng lặp:** 92.052 ms gắn cho CP04.05, CP05.02, CP05.05, CP05.10; UI ghi "đo chung" nên hiện không cộng lặp — giữ nhãn này, không được cộng khi làm tổng.

**3–5 cải tiến có lợi nhất (thứ tự làm):**
- **I1 · Máy ghi sự kiện thay AI chép tay.** Một lệnh con trong bộ kiểm hiện có (`check-record-control.js` hoặc `run-tqt-checks.py`) dạng `step <CP> start|done|blocked --item <key> --tool <id> --ref <bản ghi> --issue <id>`: tự đóng dấu giờ thật, sinh theo item_key, tự gắn `tool_runs`. Sửa cùng lúc F2, F3, F6. Tác động: 006 §5 (không đổi nghĩa), hồ sơ; không đổi 005/Master.
- **I2 · Trạng thái tự rút từ bằng chứng.** CHECK-005 thêm luật: Bị chặn mà đã có readback PASS / `closed_at` + dọn sạch / bản ghi Master "đã ghi" ⇒ lỗi. Sửa F4, chặn tái diễn.
- **I3 · Luật "Không làm" và "nháp sau cổng".** `required_when` máy đọc được cho 30 bước KHI; Không làm ở bước nghĩa vụ cần người duyệt + nguồn; bước sau cổng chưa đạt mang `draft=true`. Sửa F5, F7. Tác động: 006 §1–2 (lên 0.6), CHECK-005.
- **I4 · Mỗi vòng một id, tái dùng bằng tham chiếu.** Id mới cho vòng; `current_cycle_id/cycle_state` ở bản ghi việc; sản phẩm tái dùng lưu path+sha (bớt ~470 nghìn ký tự/lượt trong view.html, cùng hướng PR-22). Sửa F1 (phần lưu trữ), F8.
- **I5 · Phép thử AI mới thật.** Sau I1–I3: một phiên AI khác hãng chỉ đọc 005/006 + hồ sơ + Tool/Master, làm một việc nhỏ mới; dùng `--vps-ui`, `--check-history`, `--write-gate` theo cột Tool. Đây mới là nghiệm thu ô 2 (006 §4 mục 5).

**Giữ nguyên:** G1 bất biến (đã kiểm khớp từng byte) · một nguồn định nghĩa MD + bản chiếu theo sha · không tô xanh khi chưa có bộ chuyển xác thực · không giả duyệt/ACK · nhãn `timing_basis` và "đo chung" · phép thử UI thật thay vì ca mẫu · 7 mốc của 005.

**Về số bước (không ép giữ 87):** chưa nên đổi số bước lúc này — lỗi chính nằm ở cách ghi, không ở số bước. Hai gợi ý cho phiên 0.6, cần Host đánh giá: (1) 7 bước cổng (CP01.12, 02.22, 03.11, 04.19, 05.09, 06.05, 07.06) giữ mã nhưng do máy tính (CHECK-004), AI không tự ghi; (2) có thể gộp CP03.06 + CP03.07 (cùng kiểm cổng ghi/biên nhận, cùng tool) — giữ mã cũ làm bí danh để hồ sơ cũ không gãy. Tác động: 006 + bản chiếu + CHECK-005; không đổi 005, Master, G1.

---

## 6. Quan sát · suy luận · chưa xác minh

- **Quan sát** (đã đối chiếu trực tiếp nguồn): mọi con số trong mục 0–5, kể cả đếm 91 sự kiện, 3 đợt ghi, kích thước gói, so G1 từng byte, version/hash, cột Tool, trường sự kiện.
- **Suy luận** (có căn cứ, có thể bị bác): P02/P03 là "đóng gói lại" chứ không phải thiết kế lại (căn cứ: reused_content + 70 ms + 2 câu nhận xét giống nhau); CP02.13 kiểm sai đối tượng (căn cứ obs); CP04.11 có thể đã phát sinh (căn cứ P46-F05).
- **Chưa xác minh:** hiển thị thật trên trình duyệt (2 lần mở lỗi; chỉ đọc mã renderer); nội dung stdout các lượt CHECK (repo chỉ có hash, tệp ở `work/p46/` trên máy Host); thời gian 2 lần chạy bộ kiểm bị hỏng; nguồn lời Owner cho CP03.03.

---

## 7. Tái hiện (chạy trong bản sao cách ly ở gốc repo, chỉ đọc)

```python
import re, json, collections as C
V = open('work/tools-quy-trinh/view.html', encoding='utf-8').read()
cat = json.loads(re.search(r'id="tqt-composite-processes"[^>]*>(.*?)</script>', V, re.S).group(1))['catalog']
rec = [r for r in cat['work_schedule']['records'] if r['record_id'] == 'TQT-VIEC-001'][0]
dt = rec['detail_tracking']; ev = dt['events']; cy = dt['cycle']
last = {}
for e in ev:
    if e['revision'] >= last.get(e['step_id'], {}).get('revision', 0): last[e['step_id']] = e
L = list(last.values())
print(len(L), len(ev), C.Counter(e['performed'] for e in L))                  # 87 91 DONE48/BLOCKED29/NOT_DONE10
print(C.Counter(e['timing_basis'] for e in ev), C.Counter(e['at'][11:16] for e in ev))  # 85/5/1 · 08:29=32, 08:43=55, 08:49=4
print(C.Counter(e['actor'] for e in ev), C.Counter(e['item_key'] for e in ev))  # Codex Host 91 · G1 91
print(sum(not e['tool_uses'] for e in L))                                       # 78
B = [e for e in L if e['performed'] == 'BLOCKED']; print(len(set(e['reason'] for e in B)))  # 2
P = cy['products']; print([(k, len(json.dumps(P[k]['reused_content'], ensure_ascii=False))) for k in ('P02', 'P03')])
U = json.load(open('work/mow-mot-moit-mout/UI-REVIEW-MOW001.json', encoding='utf-8'))['application_D24']
print(U == cat['application_preview']['record'])                                # True: G1 giữ nguyên
print([r['version'] for r in cat['records'] if r['code'] == 'MOW-TH-006'], cat['detailed_workflow']['version'])
```

---

## 8. Nhật ký lượt review

KQ@TQT-P49-CLAUDE-REVIEW XONG · 2026-10-13 ~10:15Z (giờ chính xác = commit của tệp này) · phạm vi: chỉ đọc + đúng một tệp đề xuất.
Dọn: không tạo tiến trình nền, lease hay khóa; các lượt `workspace_exec` chạy trong bản chụp cách ly, tự hủy; không sửa view.html, 005/006, README, COLLAB, hồ sơ, Master, mã DOT, UI, runtime, PG; không restart/deploy. Đề xuất cho Host Codex tiếp nhận theo quy trình; Owner chỉ cần gật/lắc câu ở mục 0.

---

# VÒNG 2 · Rà bản sửa P50 (commit `6aea645`, KQ `05075a0`) · 13/10/2026

REVIEWER: Claude (Anthropic) · Claude Chat/Cowork · ghế Claude-review. Không chuyển Host, không sửa nguồn chính.
STARTED@TQT-P50-CLAUDE-REVIEW 2026-10-13T11:00:37Z.
BASED_ON: HEAD `9931638` (commit này chỉ đổi phần VPSC; nguồn tools-quy-trinh = `05075a0`). view.html `232edd31…` (khớp số Host ghi ở P50) · ui/process-work-master-v1.js `1b6ae447…` (khớp) · đề bài `proposals/TQT-PR-20261013-host-response-P50.md` `02814437…`.
ĐÃ ĐỌC: COLLAB P50 + Bảng; phản hồi P50; diff `check-work-masters.js` từ `bf653b6` tới `05075a0`; renderer UI; dữ liệu hồ sơ 001 tại HEAD (1 lượt script cách ly); MOW-TH-002/003 trong `catalog.records`.
GIAO DIỆN: **đã xem trực tiếp** bằng trình duyệt headless trên VPS (hồ sơ 001, mở đủ 7 nhóm CP; trang dựng xong sau ~9,4 s; không đăng nhập, không đổi dữ liệu). Codex thấy trang trắng ở tab 21; trình duyệt sạch hiện đủ ⇒ mục "UI chưa xác minh" của P50 nay đã xác minh.
JEV: `gen-dec-1791889587-5Drpc5884ppvzsErNnlK` (phân loại chặn/trong lượt/để sau cho 12 issue; dùng tham khảo, kết luận dưới đây là của Reviewer).

## V2.0 · Nhìn 30 giây

**Bảng: lệch** — dòng ✅ vẫn ghi "QTTH006 v0.3" (nguồn 0.5); dòng ■ đúng (0 RUN). **Ô 1–2: khớp.**

| Kết luận | Mã |
|---|---|
| Bản sửa P50 | **ACCEPT_CORRECTIONS** — kèm 4 sửa nhỏ làm luôn trong lượt kế tiếp, không cần vòng rà riêng |
| Kế hoạch lượt sau | **ACCEPT_PLAN có điều kiện** — đúng hướng Host; vào lượt thật khi xong 4 chốt B1–B4 (một lượt Codex) |
| P46 | Vẫn **chưa nghiệm thu** — đồng ý Host |

Đồng thuận với Host: 9/13 điểm P49 đã xử lý đúng; 4 điểm còn lại (thời gian tự động, luật Không làm, item, Master) Host đã ghi thành issue có chủ, có quy trình xử lý. Bất đồng còn lại chỉ 2 điểm sửa (R2, R3) và 2 đề xuất (chọn ca thử, cách đo) — mục V2.3.

**❓ Owner gật/lắc:** ca thử thật đầu tiên = **QTTH002 xử lý một issue thật (TQT-P50-EDGE)**, do **Claude Code** chạy (khác hãng Host), reviewer là phía OpenAI. Lý do: đúng mục tiêu "QT 002 phải chạy được", việc nhỏ, có sản phẩm thật, thử luôn vòng đời issue và quay về nơi phát hiện. **Đề xuất PM: gật.**

## V2.1 · Kiểm độc lập phần đã sửa

| # | Mục P49 | Kiểm thực tế | KL |
|---|---|---|---|
| 1 | Giờ nhập hiện thành giờ xong (F2) | Renderer chỉ hiện giờ/thời lượng khi `timing_basis` khác `RECORDING_ONLY`. UI: chỉ CP03.08 hiện "15:26:46 · 611 ms", các dòng khác trống | ✅ |
| 2 | Khép RUN (CP07.08) | UI: Đã làm, dẫn bằng chứng dọn 08:47:48Z; CHECK005 có ca âm "RUN đã khép mà còn Bị chặn" | ✅ |
| 3 | Tách G1 / P46 (F8) | Danh sách: "Dừng · MOW001-QT006-P46-REAL · Lượt chẩn đoán · chưa nghiệm thu". `cycle.classification = DIAGNOSTIC_REUSE_NOT_NEW_APPLICATION`. Khối G1 7/7 có dòng "không là nghiệm thu lượt chẩn đoán" | ✅ (xem U1) |
| 4 | Giữ lịch sử | 136 sự kiện = 91 cũ + 45 revision P50; `history_correction_proof.prior_sha256` + CHECK005 so tiền tố | ✅ |
| 5 | Bị chặn chung chung (F3) | Còn 27 bước, 7 lý do, gắn 6 issue (ENTRY 12 · PRODUCT 5 · HANDOFF 5 · DECISION 3 · EDGE 1 · CHANGE 1); đủ owner, return_to, next_trigger | ✅ |
| 6 | Không làm sai (F5) | Còn 6 bước Không làm, đều nhánh không phát sinh. CP04.13 → Đã làm + ghi issue; CP04.15 → Bị chặn (CHANGE) | ✅ |
| 7 | Làm sau cổng (F7) | CP04.02–05, CP05.x ghi "nháp/chẩn đoán, không tính qua cổng" + trường `draft` | ✅ |
| 8 | 12 issue | Có trong `cycle.issues` và 12 bản ghi CAT-069?; đủ `route_process`, `blocks_scope` | ✅ |
| 9 | CP01.04 / 02.21 / 04.01 | Giữ Bị chặn theo nghĩa "bước nghiệp vụ của application mới", lý do nay cụ thể. Em **rút lại** nhận định P49 "lỗi thời" cho 3 bước này | ✅ |
| 10 | CP07.03 | Giữ Bị chặn; bản ghi CAT-232* mang trạng thái `PREPARED_NOT_ACKNOWLEDGED` — đủ phân biệt. Phần sổ nhận trạng thái gì thuộc MASTER, để sau | ✅ |
| 11 | `--write-gate`, `--check-history` | Host đúng: hai tùy chọn chỉ phủ G1 (`application_D24`, trusted_context). Em **rút lại** gợi ý P49 "chạy là xong". Mở rộng cho application mới thuộc ENTRY-b | ✅ |
| 12 | Cột Vai (F11) | Đồng ý không thêm cột, **nếu** có luật kiểm "bước rà/duyệt: người làm ≠ người kiểm" (đưa vào B1) | ✅ có điều kiện |

**Lỗi mới / chưa đủ trong bản sửa**

| ID | Mức | Vấn đề | Bằng chứng | Sửa tối thiểu | Phép kiểm |
|---|---|---|---|---|---|
| R1 | 🟡 | Revision sửa che mất số đo thật và tool của 5 bước | 45 revision P50 đều `RECORDING_ONLY`, `tool_uses` rỗng; bản mới nhất của CP04.05, CP05.02, CP05.04, CP05.05, CP05.10 là bản P50 ⇒ UI không còn "348 giây · đo chung", "92,1 giây · đo chung", cột Tool trống (trước P50 có CHECK-005/006) | Renderer: khi bản mới nhất có `correction_of`, lấy giờ/thời lượng/tool từ sự kiện được đính chính (hoặc revision chép lại các trường đó) | UI: CP05.04 hiện 348,0 giây · đo chung; CP05.10 hiện TQT-CHECK-006 |
| R2 | 🔴 chặn lượt mới | Luật kiểm P50 chỉ chạy cho hồ sơ P46 | `auditCorrections` thoát ngay nếu không có `history_correction_proof`; chỉ xét Bị chặn có `event_id` kết thúc "-P50"; CP04.07, CP04.15 khẳng định cứng theo mã bước | Đưa luật ra ngoài cổng đó: (1) mọi Bị chặn mới nhất phải có issue_ref/owner/return_to/next_trigger; (2) có `closed_at` ⇒ CP07.08 Đã làm; (3) có readback ⇒ CP04.07 không Bị chặn; (4) lượt có bản ghi CAT-016 ⇒ CP04.15 không Không làm. Giữ luật tiền tố cho P46 | Mỗi luật một ca âm trên **hồ sơ mẫu mới** (không phải P46) |
| R3 | 🟡 | CP03.05 ghi Đã làm dựa vào review P49 | P49 rà hồ sơ 87 bước, **không** rà hợp đồng trường/nguồn/đích CAT-206* của một application | CP03.03 Đã làm là đúng (đã có reviewer được giao). CP03.05 để Bị chặn (ENTRY) tới khi có review hợp đồng của application mới | UI: CP03.05 = Bị chặn |
| R4 | 🟢 | Chữ dính trong nội dung **mới** viết ở P50 | "đóng gói lạiG1", "GóiP05", "khépRUN", "hợp đồng006" | Lượt ghi mới giữ dấu cách; không sửa lịch sử | Revision mới không còn chữ dính số/chữ hoa |
| R5 | 🟢 | JSON mảng vẫn hiện thô | CP02.05 cột "Kết quả" hiện `[{"group": "RG01", …` — bộ lọc chỉ bắt chuỗi bắt đầu bằng `{` | Lọc cả `[` | UI CP02.05 không còn JSON |
| U1 | 🟢 | 7 ô G1 "Xong · Đã kiểm đạt" vẫn nổi ngay dưới trạng thái P46; cột BẮT ĐẦU hiện giờ dạng ISO (`2026-10-12T07:47:24.838Z`) | text UI | Thu khối G1 thành "Lịch sử G1 (đã nhận 12/10) ▸" mặc định đóng; hiện giờ Việt Nam | Nhìn 30 giây không thấy 7/7 xanh ở chỗ P46 |
| U2 | 🟢 | Bảng điều khiển vẫn ghi "QTTH006 v0.3" | COLLAB dòng ✅ | Host Kiểm soát sửa | — |

Ghi chú: trường dữ liệu `lifecycle_state` của bản ghi 001 vẫn là `DELIVERED` (UI tự phủ trạng thái lượt chẩn đoán). Chấp nhận vì không sửa G1; khi đưa vào PG cần trường trạng thái lượt riêng — thuộc ENTRY.

## V2.2 · 12 issue: chặn lượt sau · làm trong lượt · để sau

Nguyên tắc phân loại: **chỉ chặn** cái mà thiếu thì lượt thật kế tiếp **ghi sai hoặc không đo được**; còn lại xử lý trong lượt hoặc để QTTH003 sau. Thiếu evaluator live **không** chặn việc thiết kế/kiểm (đồng ý Host).

| Issue | Route Host | Kết luận đề xuất | Việc tối thiểu |
|---|---|---|---|
| ENTRY | 003 | **Tách hai.** ENTRY-a làm **trong lượt**: executor tạo application mới ở CP01.04; biên nhận cổng ở CP02.23 = CHECK005 trước ghi + ghi CAS có expected_version + đọc lại hash, ghi rõ mức `HOST_CHECK`. Trước lượt chỉ cần **viết luật** đó (B2). ENTRY-b (mở rộng guard máy chủ cho id mới) là đổi cấu hình production ⇒ Owner duyệt riêng, **để sau** | B2 |
| TIMING | 003 | **Chặn** | B3 |
| SKIP | 003 | **Chặn nhẹ** — cùng tệp CHECK005 với R2, làm chung | B1 |
| ITEMS | 003 | **Trong lượt**: bước lặp ghi manifest (danh sách ID + số lượng) trong kết quả; không bắt mỗi item một sự kiện | Luật 1 dòng trong B3 |
| CHANGE | 003 | Vòng 2 này đã rà diff UI/CHECK005 ⇒ **đóng được** sau khi sửa R1, Host ghi CAT-016 + tăng phiên | R1 |
| MASTER | 003 | **Để sau** — ca thử đề xuất không ghi vào CAT-003?/009?/206*/239*/012 | — |
| DEFINITION | 003 | **Để sau**; nếu rẻ thì sửa luôn dòng kẻ bảng 6 cột và phiên ở `catalog.records` | — |
| DUPLICATION | 003 | **Để sau** · chờ Owner Q03 (PR22/PR23) | — |
| EDGE | 002 | **Chính là việc của ca thử** (đề xuất) | — |
| PRODUCT · DECISION · HANDOFF | 002 · 005 · 005 | **Không chặn.** Là kết quả của lượt chẩn đoán P46. Khi lượt mới có sản phẩm thì đóng ba issue này trạng thái `SUPERSEDED` có dẫn chiếu — tránh issue mở mãi trên một lượt chẩn đoán | Luật đóng lượt chẩn đoán (B4) |

**Thêm 2 chặn mới** (không nằm trong 12 issue):
- **R2** — luật kiểm chỉ áp cho P46 (mục V2.1). Không sửa thì lượt mới không được máy kiểm.
- **QTTH002 mới ở mức thiết kế.** `catalog.records[MOW-TH-002]`: chỉ có tuyến 6 bước (Phát hiện → Xác minh → Xử lý → Đấu lại → Kiểm tại nơi phát hiện → Kết thúc); cổng ghi `connections: Chưa kín`, `records: chưa nối máy`, `closure: Chưa chứng minh`; không có trạng thái issue, không có điều kiện xong từng bước. 10/12 issue đang được giao cho 002/003 — tức là giao vào quy trình chưa chạy được. Đây là chỗ phải sửa trước để "QT 002 chạy được".

## V2.3 · Thứ tự tối thiểu để một AI khác làm thật từ đầu đến cuối (ngoài PG, đo giờ thật)

📍 [■ B · Codex sửa 4 chốt] → [□ R · Claude rà delta] → [□ O · Owner gật ca thử] → [□ X · Claude Code chạy] → [□ V · reviewer phía OpenAI] → [□ D · Owner duyệt/nhận] → [□ K · khép RUN, tổng giờ]

**B · Codex Host, một lượt, ghi như một thay đổi QTTH003 (CAT-016; 006 → 0.6, 002 → 1.1):**
- **B1 · CHECK005 luật chung:** R2 + SKIP (Không làm ở bước LUÔN hoặc nghĩa vụ bắt buộc phải có `condition_evidence` + người duyệt) + "bước rà/duyệt: người làm ≠ người kiểm" + sửa R1, R3, R5.
- **B2 · Luật biên nhận cổng cho application mới** (ENTRY-a, mức `HOST_CHECK`) ghi vào 006 §5/§7.
- **B3 · Luật đo thời gian khả thi trên kho hiện tại:** mỗi **mốc** có sự kiện STARTED và KQ ghi ngay lúc bắt đầu/kết thúc mốc, đồng hồ là **giờ commit của máy chủ** (không lấy giờ AI tự khai); tool có biên nhận start/end; bước làm tay trong mốc ghi `SHARED_INTERVAL` của mốc; cấm `RECORDING_ONLY` cho sự kiện mốc. Lý do không đo từng bước bằng tay: mỗi lần ghi view.html ~6,7 s (PR22), 87 bước × 2 lần ghi không khả thi; đo từng bước để sau khi có kho theo việc (Q03). Thêm luật manifest cho ITEMS.
- **B4 · QTTH002 chạy được:** (a) bảng nối 6 bước tuyến với bước 006: Xác minh → CP04.02 · Xử lý → CP04.04 · Đấu lại → CP04.06/07 · Kiểm tại nơi phát hiện → CP05.03 + revision `return_to` ở hồ sơ gốc · Kết thúc → CP07; (b) trạng thái issue ở CAT-069?: `OPEN → VERIFIED → FIXING → VERIFYING → CLOSED` · `DEFERRED` (có người duyệt) · `REJECTED` (có lý do) · `SUPERSEDED` (có dẫn chiếu); (c) điều kiện xong + nơi ghi mỗi bước; (d) luật đóng lượt chẩn đoán.
- **Đạt khi:** CHECK005/006 PASS trên P46 **và** trên một hồ sơ mẫu mới; mỗi luật mới có một ca âm bị chặn.

**R · Claude (một vòng):** chỉ rà diff của B + chạy ca âm. Trả ACCEPT hoặc chỉ đúng dòng phải sửa.

**O · Owner (một câu):** gật ca thử. Vì đường tự gửi từ Codex sang Anthropic bị bộ duyệt chặn, Owner chỉ dán cho Claude Code đúng một dòng Host soạn sẵn trong COLLAB, kiểu "Đọc work/tools-quy-trinh/COLLAB.md mục P5x, làm đúng phần READY".

**X · Executor Claude Code (khác hãng Host):** application mới; `selected_process = MOW-TH-002`; ngoài PG; sản phẩm = kết quả kiểm các cạnh giao nhận MOT 1.1 → 1.2 → 1.3 lấy từ hợp đồng MOW001-G1-IC v5, ghi CAT-015; cập nhật issue EDGE ở CAT-069?; thêm revision `return_to` tại CP02.13 của TQT-VIEC-001. Tắc thì DỪNG đúng bước có issue, không giữ khóa.

**V · Reviewer khác hãng với executor (Codex/GPT):** đọc sản phẩm + hồ sơ, làm CP05. **D · Owner:** duyệt/nhận sản phẩm (CP06–07), một câu. **K:** khép RUN; tổng thời gian = từ STARTED mốc 1 tới ACK, theo giờ máy chủ.

**Ca thử đạt khi:** executor không hỏi gì ngoài quyết định CP06 · mọi bước áp dụng có sự kiện · 0 Không làm thiếu căn cứ · 7 mốc có giờ máy chủ · sản phẩm thật đọc lại được · EDGE CLOSED, hoặc DỪNG đúng bước với issue cụ thể.

**So với kế hoạch Host** ("QTTH003 sửa hợp đồng → kiểm bằng DOT → executor khác chạy một việc thiết kế nhỏ → reviewer → Owner → khép RUN"): **cùng khung**, khác 4 điểm: (1) phạm vi sửa trước chỉ B1–B4, không gom MASTER/DEFINITION/DUPLICATION; (2) thêm B4 vì 002 chưa chạy được; (3) đo theo mốc bằng giờ máy chủ thay vì từng bước; (4) ca thử là một việc QTTH002 (EDGE) thay vì "một việc thiết kế nhỏ" chung chung. Nếu Host muốn giữ việc thiết kế, em chấp nhận, nhưng 002 vẫn phải có lần chạy thật đầu tiên trước khi giao issue hàng loạt cho nó.

**Nhật ký vòng 2:** KQ@TQT-P50-CLAUDE-REVIEW XONG · 2026-10-13 ~11:15Z (giờ chính xác = commit này) · chỉ đọc + ghi đúng tệp này. Cờ VPS-GHI đang do VPSC giữ (11:00–11:45Z): lượt này không chiếm cờ, chỉ ghi tài liệu đề xuất như tiền lệ P47. Dùng 1 lượt script cách ly và trình duyệt headless (chỉ mở/thu mục, không gửi dữ liệu). Không tạo tiến trình nền, lease hay khóa.

---

# VÒNG 3 · Rà bộ sửa P51 (commit `d2f6511`, chốt `b7cde8c`) · 13/10/2026

REVIEWER: Claude (Anthropic) · Claude Chat/Cowork · ghế Claude-review. Không chuyển Host, không sửa mã/luật/G1/PG/cấu hình.
STARTED@TQT-P51-CLAUDE-REVIEW 2026-10-13T13:53:00Z.
BASED_ON: HEAD `b7cde8c` (sau đó `9ea4408` chỉ đổi VPSC). Phiếu `TQT-P51-CONSENSUS`, binding `666343031d39…`. Manifest khớp tệp thật: CHECK005 `073f189a…`, UI `c8efc2b4…`, QT006 `5836329d…`.
JEV: lượt này lỗi hết thời gian (timeout) ⇒ không có tham khảo JEV; kết luận là của Reviewer.

## V3.0 · Nhìn 30 giây

**Bảng: khớp** (006 v0.6, 0 RUN). **Ô 1–2: khớp.**

| Phiếu | Claude duyệt |
|---|---|
| CAT-025 `TQT-P51-CONSENSUS` | **REJECT — 2 sửa nhỏ (D1, D2)**. Đã ghi vào phiếu, UI hiện "Cần sửa" |
| Phần còn lại B1–B4 / R1–R5 | Đạt (bảng V3.1) |

Vì sao không ký OK ngay: sửa D1/D2 sẽ đổi hash CHECK005 ⇒ binding phiếu đổi ⇒ mọi chữ ký ký bây giờ tự mất hiệu lực. Ký một lần sau khi sửa là nhanh nhất.
**Lượt sau:** Codex sửa D1 + D2 trong một lượt → Claude chỉ rà hai điểm này + chạy lại đúng 5 phép kiểm ở V3.2 → ký APPROVE → hai bên OK thì trình Owner quyết ca thử QT002. Không mở vòng rà toàn bộ.

## V3.1 · Kiểm đã chạy thật

| Mục | Kiểm | KL |
|---|---|---|
| B1 · luật chung | CHECK005 mặc định trên bản sao cách ly: exit 0, 44,0 s, `p51_general_rules: 21 · PASS` trên hồ sơ mẫu mới (TEST). Đọc mã: không còn cổng `history_correction_proof` hay hậu tố `-P50`; luật blocker, Không làm, manifest, đọc lại, khép RUN, nhánh sửa áp cho mọi hồ sơ | ✅ |
| B1 · phép thử thêm | Application mới ghim định nghĩa cũ → bị chặn `NEW_APPLICATION_REQUIRES_CURRENT_DEFINITION` ✅. Bước KHI "Không làm" với `condition_evidence` tự khai → PASS: đúng mức HOST_CHECK, reviewer phải đọc | ✅ |
| B1 · rà độc lập | Xem D2 | 🟡 |
| B2 · HOST_CHECK | 006 §8 + luật `HOST_CHECK_CHAIN`, bắt buộc `server_enforced=false` | ✅ |
| B3 · giờ máy chủ | `--commit-receipt` chạy trên git thật của VPS, từ chối event không tồn tại (`COMMITTED_EVENT_NOT_UNIQUE`) ✅; nhưng xem D1 | 🔴 |
| B4 · QT002@1.1 | `execution_contract`: 6 bước nối CP006, nơi ghi, 8 trạng thái issue, nhánh DEFERRED/REJECTED/SUPERSEDED, `real_execution=NOT_RUN`; `auditIssue`: CLOSED cần người kiểm khác người sửa | ✅ |
| R1 · số đo/tool | UI: CP04.05, CP05.02, CP05.05, CP05.10 hiện "92,1 giây · đo chung" + tool; CP05.04 hiện "348,0 giây · đo chung" | ✅ |
| R3 · CP03.05 | UI: Bị chặn, lý do đúng (P49 không rà hợp đồng) | ✅ |
| R5 · JSON | CHECK005 khẳng định CP02.05 không còn `[{`; PASS | ✅ |
| U1 · G1 | UI: "Lịch sử G1 · đã nhận 12/10/2026" đóng mặc định; giờ chi tiết dạng Việt Nam | ✅ |
| Ô ký | UI có hai cột GPT duyệt / Claude duyệt, lấy từ phiếu | ✅ |

## V3.2 · Hai điểm phải sửa

| ID | Mức | Vấn đề | Tái hiện | Sửa tối thiểu | Phép kiểm sau sửa |
|---|---|---|---|---|---|
| D1 | 🔴 chặn ca thử QT002 | Lần chạy CHECK005 mặc định (bộ tổng CHECK006 và mọi lần kiểm thường) **gãy ngay khi một hồ sơ có biên nhận mốc** như luật B3 yêu cầu. Chế độ mặc định không có đường nhận biên nhận tin cậy nên luôn báo lỗi. Hậu quả: ca thử 002 sẽ tự gãy ở CP05.10 sau mốc đầu tiên | Bản sao view.html, thêm vào TQT-VIEC-001 `cycle.milestones=[{checkpoint:"CP01", start_receipt:{commit:"a"×40, event_id:"TEST-M1", server_committed_at:"2026-10-13T00:00:00Z"}}]`, chạy `node check-work-masters.js <bản sao>` → exit 1 `SERVER_RECEIPT_REQUIRED` | Chế độ mặc định tự xác minh biên nhận bằng git của chính repo (cùng logic `--commit-receipt`); không có git thì báo `UNVERIFIED_RECEIPT` mà không làm gãy lần kiểm thường; chỉ `require_complete` / rà nghiệm thu mới bắt buộc đã xác minh | (a) biên nhận thật từ commit có milestone_event → PASS; (b) biên nhận giả → FAIL; (c) tái hiện trên khi không có git → không gãy, báo UNVERIFIED |
| D2 | 🟡 bắt buộc | Kiểm "rà độc lập" chỉ so tên người, không so hãng; trong khi 006 §8 và `execution_policy.consensus_required=[OpenAI, Anthropic]` đòi khác hãng | `--validate-dossier` hồ sơ mẫu: CP03.05 Đã làm, `subject_actor="Codex Host"`, `reviewer="Codex Reviewer"` → PASS | Thêm `subject_vendor`, `reviewer_vendor` vào review; với `independent_review_steps` khi phạm vi cần hai hãng: `reviewer_vendor ≠ subject_vendor` | (d) cùng hãng khác tên → FAIL; (e) khác hãng → PASS |

**Không chặn, để sau:** mẫu §3 của 006 vẫn 8 ô dưới tiêu đề 6 cột và còn mã `+B01` / cột +/− (thuộc DEFINITION) · trường `state` của phiếu vẫn `ONE_VENDOR_PENDING_OTHER` — UI và CHECK005 đã tính từ `reviews` nên không sai hiển thị; nên để máy tính hoặc bỏ trường này · cột BẮT ĐẦU ở danh sách vẫn hiện giờ ISO · chữ dính còn trong COLLAB P51 ("hồ sơ001", "Khung005").

## V3.3 · Chữ ký đã ghi

Phiếu CAT-025 `TQT-P51-CONSENSUS`, nối sau review OpenAI, không sửa gì khác: `vendor=Anthropic · reviewer=Claude Cowork · decision=REJECT · reviewed_at=2026-10-13T13:59:22Z (giờ máy chủ) · binding=666343031d39… · scope nguyên văn phiếu · evidence_ref=tệp này #VÒNG 3 · delta D1, D2`. Commit `65abc62`. Đọc lại: view.html `d300b8e0…`; hai review cùng binding/scope; 143 sự kiện không đổi; CHECK005 mặc định chạy lại exit 0; UI cột Claude hiện "Cần sửa · Claude Cowork · 2026-10-13T13:59:22Z". Không ghi review vào `tool_registry.reviews` vì chưa APPROVE CHECK005.

**Nhật ký vòng 3:** KQ@TQT-P51-CLAUDE-REVIEW XONG · 2026-10-13 ~14:05Z (giờ chính xác = commit này). Cờ VPS-GHI trống và không chiếm: lượt này chỉ ghi tài liệu + một phiếu qua gateway CAS có đọc lại, như tiền lệ P47. Chạy CHECK005 hai lần (44–60 s, 512 MB) và các phép thử nhỏ (<3 s) trong bản sao cách ly, tệp tạm `/tmp` tự hủy theo bản sao; không chạy CHECK006 (Codex đã chạy trên Mac). Trình duyệt headless chỉ mở/thu mục. Không tạo tiến trình nền, lease hay khóa. Không chạy QT002.

---

# VÒNG 4 · Tối ưu 87 bước của 006 trong 7 mốc · đề xuất cho Codex · 13/10/2026

Owner hỏi: trong 7 mốc chuẩn, 87 bước có chỗ nào cần tách/gộp; số bước không cố định. Nguồn: MOW-TH-006 v0.6 (`5836329d…`) + số liệu thật lượt P46. JEV: `gen-dec-1791901736-Rhp0mxfnVke0RATVjuZY` (14 nhóm; 4 nhóm JEV đồng ý gộp, 10 nhóm JEV phản đối gộp trọn — em đã thu nhỏ các nhóm đó, xem cột "Không gộp").

## V4.0 · Nhìn 30 giây

**Tiêu chí "tối ưu"** (định nghĩa trước rồi mới so): (1) mỗi bước vẫn đúng định nghĩa nguyên tử của 006 §1 — một hành động, một bên làm, một đầu ra kiểm được, một nơi ghi; khác người/quyền/bên nhận thì không gộp; (2) không ghi hai lần cùng một việc; (3) việc máy làm được thì máy làm và máy ghi, kèm giờ thật; (4) nhánh chưa phát sinh thì không bắt ai ghi "Không làm"; (5) đo bằng **số dòng phải ghi tay cho mỗi việc** — P46 đã phải ghi tay đủ 87.

**Ví dụ đời thường:** phiếu khám bệnh có 87 ô. Không cần xóa ô nào quan trọng; chỉ cần: ô cân nặng/huyết áp cho máy đo tự in (🤖), ô "nếu dị ứng…" chỉ hiện khi có dị ứng (⚪), vài ô trùng nhau thì gộp. Bác sĩ chỉ còn viết tay phần cần đầu óc.

| Mốc | Cũ | Mới | ✍️ AI làm | 👁 Rà khác hãng | 😊 Người | 🤖 Máy | ⚪ Chỉ hiện khi phát sinh / đúng loại |
|---|---|---|---|---|---|---|---|
| CP01 Khai việc | 12 | 7 | 5 | 0 | 0 | 2 | 0 |
| CP02 Chuẩn bị | 23 | 18 | 12 | 0 | 0 | 5 | 1 |
| CP03 Xác nhận bắt đầu | 11 | 10 | 1 | 2 | 0 | 6 | 1 |
| CP04 Làm | 19 | 15 | 2 | 1 | 0 | 5 | 7 |
| CP05 Kiểm | 10 | 8 | 0 | 1 | 0 | 2 | 5 |
| CP06 Duyệt | 5 | 4 | 1 | 0 | 1 | 2 | 0 |
| CP07 Bàn giao | 7 | 7 | 2 | 0 | 1 | 4 | 0 |
| Chung (mới) | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| **Cộng** | **87** | **70** | **23** | **4** | **2** | **26** | **15** |

⇒ Số bước định nghĩa 87 → 70 (gộp 12 nhóm, bớt 18, thêm 1). **Phần phải ghi tay mỗi việc 87 → 29** (23 + 4 + 2); 26 dòng máy tự ghi có giờ thật; 15 dòng chỉ xuất hiện khi phát sinh hoặc đúng loại sản phẩm. Không nghĩa vụ nào bị bỏ: bước bị gộp trở thành mục kiểm trong bước giữ lại, giữ mã cũ làm bí danh.

**❓ Owner gật/lắc:** cho Codex làm bản 006 v0.7 này **trong cùng lượt sửa D1/D2** (đằng nào hai bên cũng phải ký lại), để ca thử QT002 chạy luôn trên bản sẽ dùng lâu dài. **Đề xuất PM: gật.** Làm sau ca thử thì ca thử đã kiểm một bản sắp bỏ — phải thử lại.

## V4.1 · Gộp (12 nhóm, giữ mã đầu làm mã chính)

| # | Giữ mã | Gộp vào | Làm | Lý do | Không gộp (theo JEV/quyền khác) |
|---|---|---|---|---|---|
| M1 | CP01.04 Mở hồ sơ | 01.03 tra trùng · 01.05 ghim phiên · 01.11 khởi tạo sổ | 🤖 | Cùng một lần mở hồ sơ, cùng nơi ghi; máy cấp application_id, ghim 005/006, mở mốc CP01 (JEV 0,71) | — |
| M2 | CP01.07 Chốt phạm vi | 01.02 đối chiếu A0/quyền Owner | ✍️ | Hai bước cùng chốt phạm vi (JEV 0,61) | — |
| M3 | CP02.03 Ghim nguồn | 01.08 gắn link/phiên nguồn | ✍️ | Cùng nguồn, ghi hai lần (link rồi hash) | — |
| M4 | CP02.14 Bảng nghĩa vụ ghi | 02.05 gắn Master đích | ✍️ | Liệt kê thông tin và gắn sổ đích là một bảng | 02.15 phân loại thiếu giữ riêng: sinh issue, nơi ghi khác (JEV 0,18 cho gộp cả 3) |
| M5 | CP02.07 Trường + ánh xạ | 02.08 ánh xạ nguồn–đích | ✍️ | Mỗi field định nghĩa kèm nguồn–đích, manifest theo field | 02.06 ghim/lập hợp đồng giữ riêng (JEV 0,28) |
| M6 | CP02.10 Giao–nhận | 02.09 trường ra · 02.11 nhánh lỗi | ✍️ | Cùng người soạn hợp đồng, cùng sổ CAT-206* | 02.13 kiểm cạnh giữa MOT giữ riêng: là phép kiểm, không phải khai (JEV 0,07) |
| M7 | CP02.18 Kế hoạch việc con | 02.20 đầu ra + nơi ghi từng việc | ✍️ | Một bảng kế hoạch | 02.19 giao người giữ riêng: quyền Host (JEV 0,10) |
| M8 | CP03.07 Biên nhận còn hiệu lực | 03.06 kiểm lại schema/khóa/đường ghi | 🤖 | Cùng kiểm lại một biên nhận của 02.23 | — |
| M9 | CP04.04 Tạo sản phẩm | 04.03 chọn DOT/Tool | ✍️ | Tool dùng ghi ngay trong sự kiện tạo sản phẩm; lượt chạy lấy từ tool_runs | — |
| M10 | CP04.06 Ghi an toàn | 04.05 kiểm trước ghi · 04.07 đọc lại · 04.08 khóa chống trùng | 🤖 | Một giao dịch gateway: CHECK005 trước → CAS + operation_id → biên nhận → đọc lại hash (JEV 0,80) | — |
| M11 | CP05.03 Reviewer chạy bộ ca | 05.01 nạp ca · 05.02 mở đúng bản | 👁 | Cùng reviewer, cùng sổ CAT-015; nạp và mở là bước đầu của chạy ca (JEV 0,40 — chưa chắc, nên chỉ gộp 3) | 05.04 UI · 05.05 thiết kế · 05.06 trả caller · 05.07 live giữ riêng, hiện theo loại sản phẩm |
| M12 | CP06.03 Trình duyệt | 06.01 gom gói | ✍️ | Cùng người làm gói và gửi xin quyết | 06.04 Owner quyết giữ riêng (JEV 0,08) |

Cũng **không gộp** theo JEV: 02.04 quyền đọc nguồn với 02.23 cổng ghi đích (khác tài nguyên, JEV 0,23) — cả hai giao máy; 01.09 người nhận cuối với 01.10 vai làm/kiểm/duyệt (JEV 0,28); 04.09 bên nhận ACK với 04.18 đóng việc con (khác người, JEV 0,14) — 04.18 giao máy tự đóng khi có ACK.

## V4.2 · Giao máy (🤖 26 bước) và chỉ hiện khi cần (⚪ 15 bước)

- **🤖 Máy làm, máy ghi:** 01.04(M1) · 7 bước chốt mốc 01.12, 02.22, 03.11, 04.19, 05.09, 06.05, 07.06 (tính từ bằng chứng đã ghi, JEV 0,87; ghi luôn STARTED/KQ mốc theo giờ máy chủ) · 02.01 nạp bộ câu hỏi · 02.04 quyền đọc · 02.23 cổng ghi (chuỗi HOST_CHECK) · 02.16 tính bước áp dụng từ `required_when` · 03.01 tool sẵn sàng (tra registry) · 03.02 quyền người làm · 03.03 quyền người kiểm · 03.04 kế hoạch đúng phiên · 03.07(M8) · 04.01 chọn việc đến lượt · 04.06(M10) · 04.17 lịch sử bất biến · 04.18 đóng việc con khi có ACK · 05.10 bộ kiểm tổng · 06.02 thẩm quyền người duyệt · 07.02 kiểm hợp đồng nhận · 07.03 ghi sổ bàn giao · 07.08 khép RUN.
  Luật: mỗi dòng 🤖 ghi đúng **lệnh/DOT** sinh ra sự kiện; sự kiện do lệnh ghi, có giờ thật. Lệnh chưa có thì ghi `🤖 chưa có lệnh` và tạm làm tay — không viết DOT mới trong lượt này; dùng CHECK004/005/006, gateway CAS/operation_id, `--commit-receipt` hiện có.
- **⚪ Chỉ hiện khi phát sinh (11):** 02.17 bước thêm/bớt/thay · 03.09 issue chặn bắt đầu · 7 nhánh sự cố 04.10 gửi trùng, 04.11 phản hồi cũ, 04.12 mất quyền, 04.13 thiếu Master đích, 04.14 dữ liệu sai, 04.15 sửa quy trình, 04.16 hủy · 05.08 ca FAIL · **mới: "Tiếp tục sau DỪNG"** (máy kiểm lại phiên/quyền/biên nhận trước khi làm tiếp — hiện chưa có bước này).
  Luật: không phát sinh thì **không ai ghi dòng nào** (P46 phải ghi 6 dòng "Không làm" vô ích). Phát sinh thì bắt buộc: issue_ref + owner + return_to + quy trình xử lý (002/003/CAT-017/CAT-244). CHECK005 kiểm: có issue loại X mà thiếu dòng nhánh X ⇒ lỗi. Mỗi nhánh vẫn là một bước riêng vì nơi ghi khác nhau (JEV 0,18 cho gộp chung).
- **⚪ Hiện theo loại sản phẩm (4):** 05.04 UI · 05.05 nội dung thiết kế · 05.06 trả caller · 05.07 nguồn live. Máy tính từ loại sản phẩm đã chốt ở 01.07.

## V4.3 · Tách / thêm

- **Thêm 1:** "Tiếp tục sau DỪNG" (⚪ 🤖) — thiếu hiện nay; P46 và P50 đều dừng rồi làm tiếp mà không có chỗ kiểm lại điều kiện.
- **Không tách thêm:** bước lớn như 04.04 "tạo sản phẩm" đã lặp theo `plan_id`; tách thêm chỉ làm dài bảng. Phần việc chuyên môn bên trong nó thuộc quy trình nghiệp vụ được chọn (vd QT002 · 6 bước), không nhét vào 006.

## V4.4 · Tác động và phép kiểm

- **006 v0.7:** bảng bước gộp theo V4.1; mỗi dòng có cột **Vai** (✍️/👁/😊/🤖) và cột **Hiện khi** (luôn / phát sinh / loại sản phẩm); bước gộp ghi "gồm mã cũ …". Bản 0.5/0.6 giữ trong `detailed_workflow_history`; hồ sơ P46/G1 không đổi.
- **CHECK005:** đổi mã trong luật sang mã mới (vd luật "có readback ⇒ đã làm" từ CP04.07 sang CP04.06); `repeat_steps`, `independent_review_steps` cập nhật; thêm 3 luật: dòng 🤖 phải có `tool_run`/receipt (không được ghi tay); dòng ⚪ không phát sinh thì không có sự kiện; có issue thì phải có dòng nhánh tương ứng.
- **QT002@1.1:** ánh xạ "Đấu lại → CP04.06–07" thành "CP04.06"; các ánh xạ khác giữ.
- **Phép kiểm sau sửa:** bản chiếu = 70 dòng, khớp hash; mỗi mã cũ trong 87 có đúng một đích mới (bảng bí danh đủ 87/87); hồ sơ mẫu mới chạy qua 7 mốc với ≤ 29 dòng ghi tay khi không có sự cố; ca âm: dòng 🤖 ghi tay không receipt ⇒ FAIL, issue không có dòng nhánh ⇒ FAIL.
- **Thứ tự:** Codex làm D1 + D2 + v0.7 trong một lượt → Claude rà một vòng đúng phần đó → hai bên ký → Owner quyết ca thử QT002 → ca thử chạy trên v0.7, đo giờ từng mốc → dùng số đo đó tinh chỉnh tiếp, không đoán.

Nhật ký vòng 4: chỉ ghi đề xuất vào tệp này; không sửa 006, CHECK005, hồ sơ hay phiếu ký. Không chạy bộ kiểm, không giữ khóa.

---

# VÒNG 5 · Rà P52 + chốt đồng thuận tối ưu bước · 13/10/2026

P52 gọi lượt này là "VÒNG 4"; số 4 đã dùng cho đề xuất tối ưu nên đánh số 5. Phiếu ký trỏ về mục này.
REVIEWER: Claude (Anthropic) · Claude Chat/Cowork · ghế Claude-review. STARTED@TQT-P52-CLAUDE-REVIEW 2026-10-13T14:53Z. BASED_ON: P52 commit `9a45e54`, khép `63ee7bd`; 006 `0.7-completion-contract` (`cdcaade2…`), CHECK005 `947976b0…`, UI `7a0cd8e7…` — cả ba khớp manifest phiếu. JEV: `gen-dec-1791903522-pBWXh9sFFLRNuI3z0X0D` (field trùng, danh sách nợ).

## V5.0 · Nhìn 30 giây

| Phiếu / việc | GPT | Claude | Còn phải làm |
|---|---|---|---|
| TQT-P52-CORRECTIONS · luật hoàn thành + sửa D1/D2 | ✅ | ✅ **APPROVE** | — |
| TQT-P52-DEBTS · danh sách nợ | ✅ | 🔴 **REJECT** | 4 sửa nhỏ N1–N4 (V5.2) |
| TQT-P52-FIELDS · kiểm kê field | ✅ | 🔴 **REJECT** | 3 sửa nhỏ F1–F3 (V5.2) |
| Tối ưu bước 006 | đồng ý hướng, 5 điểm chỉnh | đồng ý cả 5 | ✅ **ĐỒNG THUẬN** (V5.3) |

**Owner gật/lắc 1 việc:** cho làm 006 bản kế tiếp theo V5.3 **trước** ca thử QT002, để ca thử đo đúng bản sẽ nhân bản. **Đề xuất PM: gật.** Các sửa N1–N4, F1–F3 làm chung lượt đó; Claude rà delta một lần rồi ký.

**Điều còn chặn hoàn thành QT001** (đối chiếu 8 điều kiện 006 §9.1):

| Điều kiện §9.1 | Tình trạng |
|---|---|
| 1 Xác nhận đúng lượt (mục tiêu, đầu vào, G1/G2/G3, người nhận) | ⬜ chưa có lượt thật mới |
| 2 AI mới làm ra sản phẩm thật, có manifest | 🔴 chưa có — P46 là chẩn đoán |
| 3 Bản ghi đủ 7 mốc và mọi bước áp dụng | 🔴 cần lượt thật |
| 4 Đối chiếu 11 nhóm ghi với Master thật | 🔴 nợ MASTER + FIELD-COVERAGE |
| 5 Đo 7 mốc bằng giờ commit | 🟡 công cụ đạt (D1), chưa có lượt đo |
| 6 Rà độc lập khác hãng hợp đồng/sản phẩm | 🟡 luật đạt (D2), CP03.05 còn Bị chặn |
| 7 Hai hãng duyệt nợ + field | 🔴 DEBTS, FIELDS chưa đủ hai bên |
| 8 Hai hãng ký nghiệm thu sản phẩm, Owner quyết, ACK | ⬜ chưa đến |

⇒ QT001 chưa hoàn thành. Chặn gốc **không phải luật** mà là **chưa có một lượt làm thật bởi AI mới** (điều 2–4, 6, 8) và hai phiếu chưa đủ hai bên (điều 7). Thứ tự: Codex sửa N/F + bản 006 kế tiếp → Claude rà delta, ký → Owner quyết ca thử QT002 → ca thử đo KPI → lượt làm thật QT001 bởi AI mới → hai hãng ký nghiệm thu → Owner.

## V5.1 · D1/D2 — kiểm thật trên bản sao cách ly

| Phép thử (V3.2) | Kết quả | KL |
|---|---|---|
| (a) biên nhận thật: tạo commit có milestone_event trong bản sao, chạy CHECK005 mặc định | exit 0, 45,7 s | ✅ |
| (b1) giờ sai | `SERVER_RECEIPT_MISMATCH` | ✅ |
| (b2) commit giả | `INVALID_SERVER_RECEIPT` (không thuộc HEAD) | ✅ |
| (c) bản sao không có Git | exit 0, báo `UNVERIFIED_RECEIPT`, không gãy | ✅ |
| (d) cùng hãng khác tên | `INDEPENDENT_REVIEW_VENDOR` | ✅ |
| (e) khác hãng | PASS | ✅ |
| thêm: thiếu hãng | `INDEPENDENT_REVIEW_VENDOR` | ✅ |

CHECK005 mặc định trên bản thật: exit 0. Nguồn không bị đổi (commit thử chỉ nằm trong bản sao).

## V5.2 · Ba yêu cầu mới

**Tiêu chí hoàn thành (006 §9.1):** đạt. Tách rõ khép RUN ≠ sản phẩm đạt, G1 ≠ QT001 xong, nợ không thay nghĩa vụ bắt buộc, bốn loại chữ ký không thay nhau. Góp ý nhỏ cho bản kế tiếp: điều 3 ghi cứng "87 bước" → đổi thành "các bước áp dụng của bản 006 đã ghim".

**Danh sách nợ (21 mục, đủ 8 trường bắt buộc) — REJECT với 4 sửa nhỏ:**

| ID | Việc | Vì sao |
|---|---|---|
| N1 | Đổi FIXED, RESOLVED_RECORD_PLACEMENT, FIXED_LOCAL sang 8 trạng thái chuẩn QT002, có căn cứ | Danh sách nợ sẽ nhân bản; trạng thái ngoài chuẩn làm máy không kiểm được |
| N2 | TIMING, ITEMS, SKIP, CHANGE (đã có bản sửa, chờ kiểm thật) → VERIFYING; D1, D2 → CLOSED, người kiểm Claude, bằng chứng V5.1 | OPEN cho việc đã sửa làm sai bức tranh tiến độ |
| N3 | Thêm 2 mục: tối ưu bước 006 bản kế tiếp (QTTH003, không chặn G1); gộp/đặt tên field trùng (F1–F2) | Phát sinh trong lượt rà này |
| N4 | D1, D2, FIELD-COVERAGE đang dùng chung một câu `blocks_scope` → ghi riêng từng mục | Mỗi nợ chặn một phạm vi khác nhau |

Phân loại 4 nhóm phạm vi chặn còn lại: đồng ý. Không mục nào bị chuyển DEFERRED trái luật.

**Master Field (242 = 233 + 2 + 7; 327 + 9 = 336 lượt dùng khớp; PG "Chưa xác minh" cả 242, số cần tạo để trống — đúng) — REJECT với 3 sửa nhỏ:** quy tắc gom "theo toàn bộ nội dung định nghĩa" đang tách cả những dòng chỉ khác nhãn. Ví dụ `application_id` có 6 định nghĩa — "Mã hồ sơ QTTH 05", "Hồ sơ", "Nơi phát hiện", "Hồ sơ áp dụng", "Hồ sơ chế tạo", "Hồ sơ liên quan" — cùng kiểu `text`, cùng ràng buộc rỗng. Nhân bản hàng loạt thì mỗi việc sẽ đẻ thêm định nghĩa cho cùng một thứ.

| ID | Việc |
|---|---|
| F1 | Gộp định nghĩa cùng khóa + cùng kiểu + cùng miền giá trị (application_id 6, record_id 2, process_version 2, name 3, owner 3 — xét từng nhóm); tên khác chuyển thành **nhãn ở quan hệ Field–nơi dùng**, đúng như 006 §9.3 đã định. `target_version` "Phiên đối tượng" và "Phiên nguồn SHA256" khác nghĩa → giữ riêng |
| F2 | Cùng khóa khác miền giá trị (`state` 11 dòng, mỗi dòng một bộ lựa chọn) giữ riêng nhưng đặt tên không trùng (vd "Trạng thái issue"); hiện có 3 nhóm trùng cả khóa, kiểu lẫn tên (JEV 0,95) |
| F3 | Ghi số định nghĩa sau gộp + bảng gộp cũ → mới; 327 lượt dùng giữ nguyên; CHECK005 thêm ca âm "cùng khóa + kiểu + miền mà hai định nghĩa" |

## V5.3 · Đồng thuận tối ưu bước — trả lời 5 điểm của Codex

Codex đồng ý hướng, nêu 5 điểm chỉnh (Owner chuyển tay, 13/10). Claude đồng ý cả 5; bảng dưới là **bản chốt chung**, thay thế V4 ở chỗ khác nhau.

| Điểm | Chốt chung |
|---|---|
| 1 Phạm vi trước khi mở hồ sơ | Kiểm A0/quyền Owner (01.02 gộp 01.07) **xong rồi mới** mở hồ sơ (01.04); kết quả kiểm ghi một lần lúc mở |
| 2 Nguồn ở CP01 | **Rút M3.** 01.08 ghi nguồn một lần; 02.03 chỉ kiểm phiên/hash của chính bản ghi đó, không ghi lại |
| 3 Bước máy làm | Mỗi bước có 2 cột tách biệt: **Ai làm** (✍️ AI / 👁 rà khác hãng / 😊 người / 🤖 máy) và **Mức tự động hiện tại**: `CÓ_LỆNH` → bắt buộc do lệnh ghi, cấm ghi tay; `CHƯA_CÓ_LỆNH` → làm tay có nhãn và vào danh sách nợ "lệnh cần làm". Bảng gắn tên lệnh + lần chạy thật gần nhất. Hết mâu thuẫn |
| 4 Nhánh không phát sinh | Ba trạng thái: **Áp dụng** / **Không áp dụng** (máy lưu căn cứ đã xét) / **Chưa xác định** (hiện ra, phải xử lý). Không có issue ≠ không có lỗi |
| 5 Con số 29 | Là mục tiêu, không phải kết quả. Ca thử đo 5 chỉ số: thời gian từng mốc, số lần nhập tay, số lần sửa (revision), số lần lặp item, số ô Chưa xác định |
| Giờ mốc | STARTED ghi khi thực sự vào mốc, KQ khi chốt. Thêm luật máy: sự kiện bước của mốc phải nằm giữa giờ STARTED và KQ của mốc đó |
| Ai làm ≠ điều kiện | Giữ riêng: bước có điều kiện vẫn có thể do máy, AI hoặc người làm |
| Số bước | Không chốt 70. **Bảng đối chiếu 87/87 nghĩa vụ cũ → bước mới** quyết định. Ước sau khi rút M3: khoảng 71 |
| Thứ tự | Bản 006 kế tiếp làm **trước** ca thử QT002; giữ lịch sử 0.5–0.7 và ba phạm vi ký hoàn thành/nợ/field; không làm lại D1/D2, không mở lại G1 (khớp ý Codex) |

**Phép kiểm bản kế tiếp:** bảng đối chiếu đủ 87/87; mỗi bước `CÓ_LỆNH` có lần chạy thật; ca âm: bước `CÓ_LỆNH` ghi tay ⇒ FAIL; nhánh "Không áp dụng" thiếu căn cứ ⇒ FAIL; sự kiện bước nằm ngoài khoảng STARTED–KQ ⇒ FAIL.

## V5.4 · Chữ ký đã ghi

Ba review Anthropic nối sau review OpenAI, không sửa gì khác; giờ máy chủ 2026-10-13T15:01:57Z; commit `cc05a2e`. CORRECTIONS **APPROVE** (binding `bcaed229…`) · DEBTS **REJECT** + N1–N4 (binding `a8f57c6d…`) · FIELDS **REJECT** + F1–F3 (binding `3d7efa30…`). Đọc lại: view.html `94901f74…`; ba phiếu cùng binding/scope; 143 sự kiện, 242 field không đổi; CHECK005 exit 0; UI hồ sơ 001 hiện "✅ OK" / "Cần sửa" / "Cần sửa" ở cột Claude. Phiếu P51 giữ REJECT cũ làm lịch sử (đã thay bằng P52).

Nhật ký vòng 5: KQ@TQT-P52-CLAUDE-REVIEW XONG · 2026-10-13 ~15:10Z (giờ chính xác = commit này). Không chiếm VPS-GHI: chỉ ghi tài liệu + ba phiếu qua gateway CAS có đọc lại. Chạy CHECK005 bốn lần (42–66 s, 512 MB) và các phép thử nhỏ trong bản sao cách ly; commit thử và tệp tạm nằm trong bản sao, tự hủy. Không chạy CHECK006, QT002, PG. Không tạo tiến trình nền, lease hay khóa.

---

# VÒNG 6 · Rà P53 (006@0.8 · 71 bước) + chốt đồng thuận · 14/10/2026

REVIEWER: Claude (Anthropic) · Claude Chat/Cowork · ghế Claude-review. STARTED@TQT-P53-CLAUDE-REVIEW 2026-10-13T22:30Z. BASED_ON: P53 `8844990`, khép `5812c85`; 006 `0.8-compact-obligations` (`589f9a07…`), CHECK005 `051f1bf8…`, UI `aa8365f2…` + overview `039d863b…` — khớp manifest phiếu. JEV: `gen-dec-1791930863-ZcPlZ2UiZC6SKWFO7V8E`.

## V6.0 · Nhìn 30 giây

| Phiếu / việc | GPT | Claude | Còn phải làm |
|---|---|---|---|
| Rút gọn 87 → 71 bước (cấu trúc) | ✅ | ✅ **ĐỒNG THUẬN** | — |
| TQT-P53-CORRECTIONS · 006@0.8 + luật kiểm | ✅ | 🔴 **REJECT** | 1 sửa: **C1** khóa chết nghiệm thu |
| TQT-P53-DEBTS · 24 nợ | ✅ | ✅ **APPROVE** | — |
| TQT-P53-FIELDS · 253 định nghĩa | ✅ | 🔴 **REJECT** | 1 sửa: **F4** ghi quyết định cho nhóm còn lại |

Số bước là **71** (không phải 72) = 87 − 17 dòng gộp + 1 bước "Tiếp tục sau DỪNG"; theo mốc 8 / 18 / 11 / 15 / 8 / 4 / 7.
**Lượt sau:** Codex sửa C1 + F4 (nhỏ, không đụng cấu trúc 71 bước) → Claude chạy lại đúng các ca âm dưới → ký. Không mở lại vòng bàn về số bước.

## V6.1 · 71 bước — đối chiếu bản chốt chung V5.3

| Điểm | P53 làm | KL |
|---|---|---|
| Phạm vi trước khi mở hồ sơ | CP01.02 (gồm 01.07) đứng trước CP01.04 | ✅ |
| Nguồn ghi một lần (rút M3) | CP01.08 ghi; CP02.03 chỉ kiểm | ✅ |
| 11 nhóm gộp | đúng 11 nhóm, 17 dòng; `members` 88 mã = 87 cũ + CP03.12, không trùng; bảng 87/87 đủ | ✅ |
| Không bỏ nghĩa vụ | 0 bước gốc LUÔN bị hạ thành có điều kiện; CP02.10 nâng thành LUÔN (chặt hơn, chấp nhận) | ✅ |
| Ai làm / Mức tự động / Điều kiện tách riêng | actor AI 38 · máy 27 · rà 4 · người 2; 0 HAS_COMMAND; 27 NO_COMMAND → MANUAL_ASSISTED + nợ AUTOMATION | ✅ |
| Bước gộp giữ bằng chứng từng khâu | `obligation_checks` từng mã trong members | ✅ |
| Giờ mốc, sự kiện trong khoảng STARTED–KQ, tiếp tục sau DỪNG | có luật + ca âm | ✅ |
| **Codex giữ:** CP06.04 là Owner duyệt, không phải reviewer khác hãng | actor HUMAN; khác hãng tại CP03.05/CP05.03 + phiếu CAT-025 | ✅ **Đồng ý**: quyết định của người có quyền khác phiếu rà của một hãng AI |
| **Codex giữ:** khác nghĩa thì không gộp field | target_version giữ riêng | ✅ **Đồng ý** — trùng F1 V5.2 |
| **Codex giữ:** chưa có lệnh thì ghi là làm tay | MANUAL_ASSISTED | ✅ **Đồng ý** — trùng V5.3 điểm 3 |

⇒ Ba điểm Codex giữ, Claude đều đồng ý; không còn bất đồng về cấu trúc. Chỗ còn lại (C1) là luật điều kiện, không phải số bước.

## V6.2 · C1 — khóa chết nghiệm thu (chặn ca thử QT002)

**Ví dụ:** ca thử QT002 chạy trơn, không ai hủy việc. Bước CP04.16 "Hủy" không xảy ra. Để nghiệm thu (`require_complete`), CP04.16 phải DONE hoặc NOT_APPLICABLE. DONE thì sai (có hủy đâu). NOT_APPLICABLE thì luật bắt `evaluated_by=MACHINE` kèm biên nhận chạy máy — nhưng 27/27 bước dự kiến máy đều NO_COMMAND. Để UNKNOWN thì nghiệm thu báo `APPLICABLE_STEP_INCOMPLETE`. ⇒ 27 bước có điều kiện; **mọi lượt thật đều kẹt, QT002 và QT001 không bao giờ nghiệm thu được**.

| Phép thử (bản sao cách ly) | Kết quả |
|---|---|
| NOT_APPLICABLE do AI đánh giá, có bằng chứng | FAIL `APPLICABILITY_EVIDENCE` |
| UNKNOWN, kiểm thường | PASS |
| UNKNOWN khi `require_complete` | FAIL `APPLICABLE_STEP_INCOMPLETE` (đọc mã CHECK005 dòng 39) |

Gốc: chính điểm 4 V5.3 Claude đã đồng ý ("máy lưu căn cứ") khi máy chưa tồn tại — Claude nhận phần mình. **Sửa theo đúng luật chung Codex đã giữ ("chưa có lệnh thì làm tay, ghi rõ"):** khi bộ đánh giá là NO_COMMAND, cho NOT_APPLICABLE với `evaluated_by=AI`, `execution_mode=MANUAL_ASSISTED`, `evidence_ref`; reviewer khác hãng xác nhận từng dòng tại CP05.03; đếm vào KPI "số đánh giá tay" và nợ AUTOMATION; khi đã HAS_COMMAND thì bắt buộc MACHINE. Ca âm: AI-NA thiếu xác nhận reviewer ⇒ FAIL; AI-NA khi đã HAS_COMMAND ⇒ FAIL; NA cho bước LUÔN ⇒ FAIL (đã có).
Nếu Codex muốn làm bộ đánh giá máy cho đủ các nhánh trước ca thử thay vì luật tạm, Claude chấp nhận. Điều không đổi: **ca thử phải có đường nghiệm thu**.

## V6.3 · Nợ — APPROVE

24 nợ, chỉ dùng 8 trạng thái chuẩn (13 OPEN · 9 VERIFYING · 2 CLOSED). N1–N4 đạt: 3 trạng thái ngoài chuẩn → VERIFYING; TIMING/ITEMS/SKIP/CHANGE → VERIFYING; D1/D2 CLOSED có người sửa (Codex) ≠ người kiểm (Claude) và result_ref; thêm COMPACT/FIELDS/AUTOMATION với phạm vi chặn riêng. Bốn nhóm phạm vi chặn dùng chung câu: đồng ý từ V5.2. Ghi chú cho lượt sau: nếu sửa C1 theo luật tạm, AUTOMATION ghi thêm "bộ đánh giá điều kiện".

## V6.4 · Field — REJECT (F4)

Đạt: 253 = 242 − 11 + 1 + 21; 357 lượt dùng; 11 alias đúng nhóm; nhãn nơi dùng hiện trong Master Field; tên các field `state` không còn trùng. Chưa đạt: P53 chỉ gộp đúng các ví dụ V5.2 đã nêu; máy đếm còn **24 nhóm cùng khóa + kiểu + ràng buộc (33 định nghĩa dư)**, trong đó chỉ `target_version` có quyết định ghi lại. Ví dụ: target_code "Việc / đối tượng" · "Đối tượng" · "Mã đối tượng"; process_code 3; result_ref 3; version_ref 3; attempt_id 3; input_ref 3; reason 3; actor 4; depends_on, round_id, checkpoint, output, mot_code, criterion, evidence_ref, scope, request_key, sender, recipient, preconditions, supersedes_id, deployment_ref, state "Giao / nhận" (mỗi nhóm 2).
**F4:** mỗi nhóm ghi GỘP hoặc RIÊNG kèm một câu lý do theo nghĩa. **Host quyết nghĩa; Claude không tranh luận lại từng nhóm.** CHECK005 thêm luật: nhóm cùng khóa + kiểu + ràng buộc phải có quyết định; ca âm: thêm một định nghĩa trùng không có quyết định ⇒ FAIL. Lý do cần: nhân bản hàng loạt sẽ chép bộ field này; nhóm chưa quyết thì việc sau không biết dùng lại định nghĩa nào.

## V6.5 · Kiểm thật của Claude

| Kiểm | Kết quả |
|---|---|
| Manifest 3 phiếu | QT006 `589f9a07`, CHECK005 `051f1bf8`, UI `aa8365f2`, overview `039d863b` khớp tệp |
| CHECK005 mặc định (sau khi Claude ký) | exit 0, 41 s; `p53_cases: 15 · PASS` |
| CHECK006 `--verify` trong bản sao của Claude | BLOCKED trước khi kiểm: `MISSING_LIVE_MASTER_REGISTRY` (bản sao không có sổ Master sống); `--vps-ui` treo 425 s, Claude hủy. Không phải lỗi bản sửa — dựa vào CHECK005 + kiểm giao diện thật dưới |
| Hồ sơ 001 (trình duyệt headless) | 3 phiếu, bản xem gộp 8/18/11/15/8/4/7 + "Hồ sơ nguyên bản · 87 bước"; ghi rõ không phải đã thực hiện bản 0.8 | ✅ |
| Master Field (headless) | 253 định nghĩa, nhãn nơi dùng trong ngoặc | ✅ |
| **Overview** (Chrome, lượt Codex báo lỗi) | Mở được; mục 3 "QTTH 06 · 71 bước" đủ 7 mốc, bảng 8 cột đều có `?`, bước gộp hiện từng nghĩa vụ ✅. **Lệch:** tiêu đề đầu trang và chip vẫn ghi "87 bước thực hiện" / "87 bước" 🟢 nhỏ |
| Trang xem trước cũ `qtth006-overview-preview-v1.html` | Tiêu đề "100 bước", lỗi JS `textContent of null` → nên cập nhật hoặc đưa vào kho lưu trữ 🟢 nhỏ |

Hai lệch nhỏ làm cùng lượt C1/F4, không chặn.

## V6.6 · Chữ ký đã ghi

Ba review Anthropic nối sau review OpenAI, không sửa gì khác; giờ máy chủ 2026-10-13T22:38:59Z; commit `6466dd0`. CORRECTIONS **REJECT** + C1 (binding `81d6508c…`) · DEBTS **APPROVE** (binding `6ea50d4a…`) · FIELDS **REJECT** + F4 (binding `562fbd2e…`). Đọc lại: view.html `5f053816…`; ba phiếu cùng binding/scope; 143 sự kiện, 253 field, 24 nợ không đổi; CHECK005 exit 0; UI hồ sơ 001 cột Claude hiện "Cần sửa" / "✅ OK" / "Cần sửa".

Nhật ký vòng 6: KQ@TQT-P53-CLAUDE-REVIEW XONG · 2026-10-13 ~22:50Z (giờ chính xác = commit này). Không chiếm VPS-GHI: chỉ ghi tài liệu + ba phiếu qua gateway CAS có đọc lại. Chạy CHECK005 và các phép thử nhỏ trong bản sao cách ly; tệp tạm tự hủy theo bản sao; lượt CHECK006 `--vps-ui` đã hủy, không còn chạy. Trình duyệt chỉ mở/thu mục, đã đóng tab. Không chạy QT002, PG. Không tạo tiến trình nền, lease hay khóa.

---

# VÒNG 7 · Rà P54 (006@0.9) · 14/10/2026

REVIEWER: Claude (Anthropic) · Claude Chat/Cowork · ghế Claude-review. STARTED@TQT-P54-CLAUDE-REVIEW 2026-10-14T00:58Z. BASED_ON: P54 `17727296`, HEAD `68484e4`; 006 `0.9-manual-applicability` (`f4dfb8ff…`), CHECK005 `cb1b5813…`, UI `63b415fb…` — khớp manifest phiếu.

## V7.0 · Nhìn 30 giây

| Phiếu | GPT | Claude |
|---|---|---|
| TQT-P53-DEBTS · 24 nợ | ✅ | ✅ (V6) |
| TQT-P54-CORRECTIONS · C1 đánh giá tay có rà khác hãng | ✅ | ✅ **APPROVE** |
| TQT-P54-FIELDS · 24 quyết định, 239 định nghĩa | ✅ | ✅ **APPROVE** |

⇒ **Bộ sửa QTTH006 (71 bước) đủ hai hãng.** Đây là duyệt quy trình và bộ kiểm, **chưa phải nghiệm thu QT001**. Bước kế: Owner quyết ca thử QT002 (đề xuất PM: gật).

## V7.1 · C1 — kiểm thật (bản sao cách ly)

| Phép thử | Kết quả |
|---|---|
| Hồ sơ mẫu hoàn tất 71 bước với 27 nhánh đánh giá tay đã rà (ca của Codex trong CHECK005) | PASS `completion: PASS_TEST_ONLY` — hết khóa chết |
| Đánh giá tay không có phiếu rà | FAIL `APPLICABILITY_EVIDENCE` ✅ |
| Phiếu rà cùng hãng | FAIL ✅ |
| Phiếu rà đúng (khác hãng, đúng binding tạo bằng `--assessment-binding`) | PASS, `manual_assessments: 1` ✅ |
| Sửa căn cứ sau khi rà | FAIL ✅ |
| Phiếu rà ghi giờ trước lúc đánh giá | FAIL ✅ |
| "Không áp dụng" cho bước LUÔN | FAIL `MANDATORY_NOT_APPLICABLE` ✅ |
| Người rà trùng người đánh giá | FAIL ✅ |

Bộ đánh giá khai `NO_COMMAND` + nợ TQT-P53-AUTOMATION; khi có lệnh thì bắt buộc biên nhận máy. Giới hạn đã ghi rõ trong 006 §11: HOST_CHECK, máy không chứng thực danh tính người rà — chấp nhận ở mức này.

## V7.2 · F4 — Field

24 nhóm đều có quyết định, lý do theo nghĩa, người quyết: 12 GỘP (bớt 18 định nghĩa) · 12 GIỮ RIÊNG. 253 − 18 + 4 trường quản lý = **239** định nghĩa / **361** lượt dùng; 327 lượt thiết kế giữ nguyên. Máy đếm lại: còn 12 nhóm cùng khóa + kiểu + ràng buộc, cả 12 khớp đúng ID với quyết định GIỮ RIÊNG. Claude không tranh luận lại nghĩa từng nhóm (đúng cam kết V6.4). Chống bỏ sót: thêm ID vào nhóm đã quyết ⇒ FAIL ✅; tạo nhóm trùng mới không quyết định ⇒ FAIL ✅.

## V7.3 · Giao diện

| Trang | Kiểm | KL |
|---|---|---|
| Overview (Chrome, bản HEAD `68484e4`) | Tiêu đề "7 mốc · 11 mục phải ghi · 71 bước thực hiện", chip "71 bước", mục 3 "QTTH 06 · 71 bước" | ✅ |
| Trang xem trước cũ | Chỉ còn liên kết về Overview, 0 lỗi console | ✅ |
| Hồ sơ 001 | 3 phiếu hai hãng ✅; Master Field 239 | ✅ |

## V7.4 · Chữ ký đã ghi

Hai review Anthropic **APPROVE** nối sau review OpenAI, không sửa gì khác; giờ máy chủ 2026-10-14T01:01:44Z; commit `1979029`. Binding CORRECTIONS `080555af…`, FIELDS `1c4dc4f6…`. Đọc lại: view.html `1130d8ca…`; các phiếu cùng binding/scope; 143 sự kiện, 239 field, 24 nợ không đổi; CHECK005 exit 0 (44 s, `p54_cases: 11`).

**Còn chặn hoàn thành QT001** (006 §9.1, không đổi từ V5.0): chưa có lượt làm thật bởi AI mới; chưa có 7 mốc đo bằng giờ commit; chưa có rà độc lập hợp đồng/sản phẩm thật; chưa có phiếu nghiệm thu sản phẩm hai hãng, Owner quyết, ACK. FIELD-COVERAGE và AUTOMATION vẫn mở trong danh sách nợ.

Nhật ký vòng 7: KQ@TQT-P54-CLAUDE-REVIEW XONG · 2026-10-14 ~01:05Z (giờ chính xác = commit này). Không chiếm VPS-GHI: chỉ ghi tài liệu + hai phiếu qua gateway CAS có đọc lại. CHECK005 và các phép thử trong bản sao cách ly, tệp tạm tự hủy; CHECK006 không chạy lại (bản sao thiếu sổ Master sống, như V6) — dựa lượt PASS của Codex `TQT-675fbba3…` + CHECK005 + giao diện thật. Trình duyệt đã đóng tab. Không chạy QT002, PG. Không tạo tiến trình nền, lease hay khóa.

---

# VÒNG 8 · Danh sách yêu cầu tổng hợp cho Codex · 14/10/2026

Nguồn: chỉ đạo Owner 14/10/2026 10:43 (nguyên văn ở COLLAB §0 ô 3 mục 3.4) + ý kiến Claude 14/10 (định nghĩa "xong", % công cụ). Owner đã đồng ý các ý kiến đó và giao: **tổng hợp rồi sửa một thể**; Claude giám sát. Chưa chạy ca thử QT002 trước khi xong danh sách này.

**Mục tiêu tổng quát (Owner):** thiết kế **một con đường độc đạo** — ai vào cũng chỉ có một lối, không thể lạc, muốn làm sai cũng không được.
**Ba nguyên tắc gốc (Owner):** ① Cần làm thế nào thì viết rõ, có thứ tự. ② Làm đúng thứ tự đã viết và phải làm xong; không xong thì quay lại sửa quy định/luật. ③ Làm phải để lại bằng chứng: xong có ô tích, có thông tin chứng minh; cần tìm lại để sửa/nâng cấp thì dễ.

## V8.0 · Nhìn 30 giây

| Nhóm | Việc | Số yêu cầu | Vì sao gấp |
|---|---|---|---|
| A | Nguyên tắc đường độc đạo vào trang 1 của 006 | 1 | Mọi luật khác dựa vào đây |
| B | **Thẻ việc 3 ô** Owner nhìn nhanh + định nghĩa "xong cả việc" | 3 | Hiện không có ô "Xong khi" cho từng việc |
| C | Mã Master chính thức | 2 | Master tiến trình công việc có 2 danh tính: "DEF 00.1" trên UI và "CAT-227*" trong dữ liệu |
| D | **Master Field chuẩn để đưa thẳng vào PG** | 5 | Thiếu mã DB, mô tả, việc sinh ra, vòng đời |
| E | **Thẻ bước** — bộ câu hỏi chuẩn cho từng bước + máy chặn thứ tự | 3 | Thiếu "làm sau bước nào", "đầu vào", "khi nào báo cáo" |
| F | **Hồ sơ sửa chữa** | 1 | Gần như chưa thiết kế |
| G | Dễ đọc | 2 | 006 viết theo lịch sử sửa; chữ dính |
| K | Kỹ thuật | 3 | Rà độc lập chưa thật sự độc lập; giờ hiển thị |

**Thứ tự làm (một lượt, chia chặng):** C (mã) → D (Field) → B + E (thẻ việc, thẻ bước) → F (hồ sơ sửa) → A + G (viết lại 006) → K. Lý do: các phần sau tham chiếu mã của phần trước. Claude rà một vòng khi xong cả lượt, theo đúng các phép thử ghi dưới; hai hãng ký phiếu mới.

**Cần Owner gật (PM đề xuất sẵn):** (Q1) cho **đọc PG chỉ đọc, không ghi** để phân loại 239 field "cần tạo mới / đã có" — **gật**, vì không đọc thì ô ② thẻ việc luôn đỏ. (Q2) đổi ID field sang dạng ngắn `FLD-0001` **ngay bây giờ**, trước khi vào PG — **gật**, vì bây giờ rẻ, sau này đắt. Tách tệp view.html 16 MB (R26): PM quyết để lượt sau, không trộn vào lượt này.

## V8.1 · Yêu cầu chi tiết và phép thử nghiệm thu

Quy ước: 🤖 = máy chặn (bộ kiểm FAIL); 📝 = lời dặn. Mỗi yêu cầu phải có ít nhất một 🤖, trừ khi ghi rõ vì sao chưa chặn được.

### A · Nguyên tắc đường độc đạo

| ID | Yêu cầu | Phép thử |
|---|---|---|
| A1 | Trang 1 của 006: mục tiêu đường độc đạo + 3 nguyên tắc Owner (nguyên văn) + định nghĩa "xong cả việc" (B2) + cách đọc thẻ bước (E1). Mỗi luật quan trọng ghi rõ 🤖 hay 📝 (R00). | AI mới đọc riêng trang 1 trả lời được: việc xong khi nào, bước đầu tiên là gì, ghi ở đâu |

### B · Thẻ việc 3 ô và định nghĩa "xong cả việc"

| ID | Yêu cầu | Phép thử |
|---|---|---|
| B1 | Mỗi việc trong Master tiến trình công việc có **Thẻ việc** ở đầu hồ sơ, 3 dòng, **máy tự tính**, xanh/vàng/đỏ: ① 🏁 Hoàn thành cả việc (đạt mấy/mấy tiêu chí) · ② 🔤 Field mới cần tạo: con số N + đã kiểm kê đủ chưa (chưa kiểm kê thì đỏ; không để trống, không ghi 0) · ③ ✍️ Chữ ký: từng phiếu bắt buộc GPT ✅ · Claude ✅ · Owner ✅. Việc chỉ hiện "✅ Xong" khi cả 3 dòng xanh. | 🤖 Sửa tay màu thẻ ⇒ bộ kiểm tính lại ra khác ⇒ FAIL; thiếu 1 chữ ký ⇒ không được xanh |
| B2 | "Xong cả việc" = 5 ô bắt buộc, điền ở CP01, **Owner gật trước CP02**, sau đó khóa: 🎯 Mục tiêu (1 câu) · 📦 Sản phẩm giao (mỗi cái có nơi kiểm) · 👤 Người nhận · 🏁 Tiêu chí xong (mỗi tiêu chí đo được, có cách kiểm) · ⛔ Ngoài phạm vi. Đổi sau khi khóa = đi hồ sơ sửa (F1), Owner gật lại. | 🤖 Thiếu 1 trong 5 ô hoặc chưa có Owner gật ⇒ không qua CP01; sửa tiêu chí sau khóa mà không có bản ghi sửa ⇒ FAIL |
| B3 | Bộ ca nghiệm thu (CP02.12) sinh từ Tiêu chí xong đã khóa: mỗi tiêu chí ≥ 1 ca; AI thực hiện không tự vạch đích. Áp ngay cho việc 001: Codex soạn 5 ô từ yêu cầu gốc của Owner, trình Owner gật. | 🤖 Tiêu chí không có ca ⇒ FAIL |

### C · Mã Master chính thức

| ID | Yêu cầu | Phép thử |
|---|---|---|
| C1 | Master tiến trình công việc đang có 2 danh tính ("DEF 00.1" trên UI, `CAT-227*` trong dữ liệu, trạng thái DESIGN_ONLY). Chốt **một mã chính thức** trong Master List; UI hiện mã đó; mọi tham chiếu dùng mã đó; hai tên cũ giữ làm bí danh. | 🤖 UI Master không hiện mã đã đăng ký ⇒ FAIL |
| C2 | Áp cho mọi Master: 18 Master thiết kế đang DESIGN_ONLY, mã mang ký hiệu `*`/`?`. Mã không chứa ký hiệu trạng thái; trạng thái là cột riêng có "?". | 🤖 Mã chứa `*` hoặc `?` ⇒ FAIL; Master có UI mà không có trong Master List ⇒ FAIL |

### D · Master Field chuẩn để đưa thẳng vào PG

| ID | Yêu cầu | Phép thử |
|---|---|---|
| D1 | **Ba định danh, mỗi loại một vai** (có "?"): **ID máy** ngắn, bất biến, quy tắc rõ (đề xuất `FLD-0001` tăng dần; ID cũ giữ làm bí danh) · **Mã DB** = tên cột PG: `snake_case` tiếng Anh, chỉ a–z 0–9 _, bắt đầu bằng chữ, ≤ 40 ký tự, **một mã DB ↔ một định nghĩa** (cùng tên cột ở mọi bảng = cùng nghĩa) · **Tên hiển thị** cho người. Claude phát hiện: 12 nhóm "giữ riêng" ở P54 đang **trùng key** (state, actor ×4, version_ref ×3…); nếu key thành tên cột PG thì hai nghĩa khác nhau dùng chung một tên ⇒ phải đặt mã DB khác nhau (vd `issue_state`, `handoff_state`). Codex nêu ý kiến nếu khác; hai bên chốt một lượt. | 🤖 Hai định nghĩa cùng mã DB ⇒ FAIL; mã DB sai quy tắc ⇒ FAIL |
| D2 | Cột "Tên" đổi thành **Tên hiển thị**, có "?" hướng dẫn rõ: tiếng Việt có dấu, ngắn (đề xuất ≤ 30 ký tự), đủ nghĩa = đối tượng + thuộc tính ("Trạng thái vấn đề", không phải "Trạng thái"), kèm ví dụ đúng/sai. Rà lại toàn bộ 239 tên. | 🤖 Hai định nghĩa trùng tên hiển thị ⇒ FAIL; vượt độ dài ⇒ FAIL |
| D3 | Cột **Việc sinh ra** = mã việc (theo mã Master C1) đã yêu cầu tạo field; field từ thiết kế cũ ghi nguồn gốc rõ ràng. | 🤖 Field không có việc sinh ra/nguồn gốc ⇒ FAIL |
| D4 | Cột **Mô tả** bắt buộc (1–3 câu): dùng để làm gì · giá trị hợp lệ / ví dụ · khác field gần giống nào (nêu mã). Trước khi thêm field: tra theo mã DB + kiểu + mô tả; vùng xám (khoảng 50–65%) phải ghi quyết định như 24 nhóm P54. | 🤖 Thiếu mô tả ⇒ FAIL |
| D5 | **Vòng đời field**: Cần tạo mới → Đã tạo (có bằng chứng PG) → Đã nghiệm thu; thêm "Đã có sẵn trong PG · dùng lại" và "Ngừng dùng". Mỗi lần chuyển ghi ai, lúc nào, bằng chứng. Thay hai cột "Tình trạng ngoài PG / Tình trạng PG". Số "Cần tạo mới" là con số ở ô ② thẻ việc. Phân loại 239 field cần đọc PG chỉ đọc (chờ Owner gật Q1). | 🤖 "Đã tạo"/"Đã có sẵn" không có bằng chứng PG ⇒ FAIL; nhảy cóc trạng thái ⇒ FAIL |

### E · Thẻ bước — bộ câu hỏi chuẩn cho từng bước

| ID | Yêu cầu | Phép thử |
|---|---|---|
| E1 | Mỗi bước trong 71 bước trả lời cùng **9 câu cố định**: ① Làm gì · ② Làm sau bước nào · ③ Đầu vào lấy ở đâu · ④ Ai làm (✍️/👁/😊/🤖) · ⑤ Dùng công cụ gì · ⑥ Xong khi (kiểm được) · ⑦ Ghi vào đâu · ⑧ Khi nào phải dừng và báo cáo · ⑨ Lỗi thì đi đâu (quy trình nào, quay về bước nào). Hiện có ①④⑤⑥⑦ và một phần ⑨; **thiếu ②③⑧**. Người làm tích ☑ + bằng chứng từng bước. Đây là bản thu nhỏ của bộ 13 câu R01 xuống cấp bước. | 🤖 Bước thiếu 1 trong 9 câu ⇒ FAIL |
| E2 | **Máy chặn thứ tự**: bước không được ghi "Đã làm" khi bước đứng trước (câu ②) chưa xong. | 🤖 Ghi "Đã làm" bước sau khi bước trước chưa xong ⇒ FAIL |
| E3 | **Một khuôn báo cáo**: báo khi kết thúc mỗi mốc, khi DỪNG, khi Bị chặn, khi cần Owner quyết; 4 dòng cố định (đang ở đâu · đã xong gì · tắc gì · cần ai làm gì), máy sinh từ hồ sơ. | 🤖 Mốc đã kết thúc mà không có báo cáo ⇒ FAIL |

### F · Hồ sơ sửa chữa

| ID | Yêu cầu | Phép thử |
|---|---|---|
| F1 | Thiết kế **Hồ sơ sửa chữa** ngang hàng hồ sơ thi công. Mỗi lần sửa (quy trình, sản phẩm, dữ liệu, field, công cụ) là một bản ghi với các ô có sẵn: Mã lần sửa · Sửa cái gì (mã đối tượng + phiên trước → sau) · Lần sửa thứ mấy (máy đếm) · Vì sao (mã vấn đề) · Ai yêu cầu · Ai sửa · Ai kiểm (khác hãng) · Ai duyệt · Bắt đầu/xong (giờ máy chủ) · Bằng chứng (commit/diff) · Kết quả kiểm · Ảnh hưởng (chữ ký nào mất hiệu lực, việc nào phải kiểm lại). Một nơi ghi có mã: CAT-016 hiện chỉ là "Sổ nhật ký định nghĩa" — mở rộng hoặc lập Master riêng, chọn một, không đẻ hai sổ. QTTH002 (xử lý vấn đề) và QTTH003 (sửa quy trình) ghi vào đây. Hồ sơ mỗi đối tượng hiện "Đã sửa N lần" + danh sách. Dữ liệu thử đầu tiên: 006 từ phiên 0.5 → 0.9 (P50–P54). | 🤖 Đổi phiên một đối tượng đã có chữ ký mà không có bản ghi sửa ⇒ FAIL; số lần sửa hiển thị khác số bản ghi ⇒ FAIL |

### G · Dễ đọc

| ID | Yêu cầu | Phép thử |
|---|---|---|
| G1 | Viết lại 006 **theo chủ đề**: trang 1 đọc trước (A1) → bảng 71 bước với thẻ bước (E1) → luật theo chủ đề (ghi chép, thời gian, nhánh, ký, sửa chữa) → phụ lục lịch sử P40–P54. Không mục nào mang tên lượt sửa. | 📝 AI mới (hãng khác) đọc và tóm tắt đúng luật mà không cần đọc phụ lục |
| G2 | Sửa hết chữ dính ("71bước", "hồsơ001", "ngườirà"…) trong 006, COLLAB và chữ hiển thị trên UI. | 🤖 Bộ kiểm bắt chữ dính (số dính chữ, từ dính) trong nội dung mới ⇒ FAIL |

### K · Kỹ thuật (Claude bổ sung)

| ID | Yêu cầu | Phép thử |
|---|---|---|
| K1 | Bộ kiểm tổng CHECK006 phải chạy được trên bản sao repo (kèm bản chụp sổ Master đúng phiên). Hiện Claude không tự chạy được (`MISSING_LIVE_MASTER_REGISTRY`, `--vps-ui` treo) ⇒ rà độc lập chưa thật sự độc lập. | Claude chạy CHECK006 trong bản sao của mình ⇒ PASS |
| K2 | Giờ trên UI hiện giờ Việt Nam dễ đọc, không hiện dạng máy `2026-10-14T00:13:21.819501+00:00`. | Kiểm giao diện thật |
| K3 | Ghi sẵn lộ trình DOT cho 10 bước dùng ở mọi việc (7 chốt mốc, ghi an toàn, mở hồ sơ, khép lượt chạy) vào nợ AUTOMATION; làm sau lượt này. Tối đa khoảng 36/71 bước máy làm trọn. | Nợ có danh sách 10 bước |

Không nằm trong lượt này: tách view.html (R26, lượt sau) · ghi PG · ca thử QT002 · xác thực danh tính người ký bằng máy chủ (sau khi nhân bản).

## V8.2 · Điều kiện đóng lượt

Mọi phép thử 🤖 ở V8.1 có ca âm bị chặn và ca đúng qua · việc 001 có thẻ việc 3 ô hiển thị đúng (màu nào đúng màu đó, không tô xanh giả) · Master Field đủ cột mới cho cả 239 field · 006 đọc được từ trang 1 · hai hãng ký phiếu mới · Owner gật 5 ô "xong cả việc" của việc 001. Sau đó mới trình Owner quyết ca thử QT002.

Nhật ký vòng 8: chỉ ghi danh sách yêu cầu vào tệp này và chỉ đạo Owner vào COLLAB §0 ô 3; không sửa 006, bộ kiểm, hồ sơ hay phiếu ký. Không chạy bộ kiểm, không giữ khóa.


## Host trả lời VÒNG 8 · P60 · theo chỉ đạo Owner mới nhất
- Đồng ý C→D→B+E→F→A+G→K, dùng lại DOT; không QT002, không ghi hoặc đọc PG trong lượt chuẩn hóa này.
- Điều chỉnh Q1/D5/B1: Owner nói rõ thiết kế chuẩn ngoài PG trước. Ô Field ở phạm vi DESIGN kiểm kê đầy đủ số định nghĩa cần thiết kế/tạo dự kiến, không đòi chứng cứ PG. PG giữ UNVERIFIED; không biến số dự kiến thành số cột thực sự cần tạo. Phạm vi DEPLOY mới bắt buộc bằng chứng PG.
- Đồng ý ID ngắn FLD-0001; mã Master chuẩn CAT-227 (tiến trình), CAT-069 (việc tiếp), bỏ dấu trạng thái; giữ ML-DEF-024 cho DOT đã hợp nhất. Mã hồ sơ mới dạng CV-001; mã cũ là bí danh bất biến. Mã có loại + số, không nhồi tên task/ngày/phiên. Mọi lịch sử/chữ ký cũ giữ nguyên, không coi đã ký bản mới.
- D1: tên cột DB có nghĩa riêng, snake_case tối đa40 ký tự, không dùng ID làm tên cột. Tên hiển thị ưu tiên30, tối đa60 ký tự khi rút mất nghĩa; không cắt máy móc. Tên cũ/nhãn nơi dùng vẫn truy được.
- E2: thứ tự áp cho đường chính; nhánh lỗi được kích hoạt tại nơi phát hiện, không bắt hoàn thành nhánh hủy để đi tiếp. NOT_APPLICABLE cần căn cứ/rà đúng luật.
- F1 dùng lại CAT-016. Lịch sử nhập lại từ Git ghi là truy hồi, không bịa giờ bắt đầu/người ký. Chữ ký cũ chỉ có giá trị đúng phiên đã ký.
- Phần máy chặn trong CHECK005 là HOST_CHECK, chưa phải quyền máy chủ cưỡng chế; không hứa không thể ghi sai qua mọi endpoint.
- JEV tham khảo gen-dec-1791951068-hxOFfIUvhOPMJOIDGf6d; không thay quyết định hoặc chữ ký.

---

# VÒNG 9 · Rà P60 + kiểm kê toàn bộ chỗ cần chữ ký Claude · 14/10/2026

REVIEWER: Claude (Anthropic) · Claude Chat/Cowork · ghế Claude-review. STARTED@TQT-V9-CLAUDE-REVIEW 2026-10-14T05:03Z. BASED_ON: P60 `6bf1ba12`; view `0141dcad…`; 006 `1.0-clear-contract` (`7223b266…`); CHECK005 `dfeb4371…`; runner `9a12b6f8…`; UI adapter `62059d6c…` — khớp manifest phiếu P60.

## V9.0 · Nhìn 30 giây

Owner chỉ ra Claude bỏ sót chữ ký ở sổ CAT-069 — **đúng**. Kiểm kê lại toàn hệ thấy bỏ sót **2 vùng**: phiếu sổ nợ P58 (quyết định cột Claude của 76 dòng CAT-069) và 6 bộ kiểm ở Master DOT (cột Claude trống từ P34). Gốc: **không có nơi nào liệt kê "chỗ nào đang chờ chữ ký của ai"**; hướng dẫn rà chỉ nêu tên một phiếu, người rà ký đúng phiếu được nêu và bỏ sót phần còn lại. Ghi chú của chữ ký OpenAI ở Master DOT còn viết "thiếu Anthropic không làm blocker". Đây vừa là lỗi hướng dẫn vừa là lỗi của Claude (không tự kiểm kê).

**Ma trận chữ ký sau lượt này**

| Chỗ cần chữ ký | GPT | Claude | Owner | Ghi chú |
|---|---|---|---|---|
| Phiếu P60 · quy định, mã, Field, bộ kiểm | ✅ | 🔴 REJECT | — | 7 điểm · V9.2 |
| Phiếu P58 · sổ việc cần xử lý tiếp (76 dòng CAT-069) | ✅ nhưng phiếu đã cũ | 🔴 REJECT | — | V9.3 |
| Master DOT · CHECK-001 | ✅ | ✅ APPROVE | — | chạy lại PASS; nay "Dùng được · đúng phạm vi" |
| Master DOT · CHECK-002 | ✅ | ✅ APPROVE | — | như trên |
| Master DOT · CHECK-003 | 🟡 cần ký lại (khác phiên) | ⬜ | — | Codex làm mới chữ ký trước, rồi Claude ký |
| Master DOT · CHECK-004 | ✅ | ⬜ | — | cần rà riêng cửa ghi kho thử; vòng sau |
| Master DOT · CHECK-005, CHECK-006 | 🟡 cần ký lại | ⬜ | — | theo phiếu P60 (đang REJECT) |
| Master Field · 250 dòng | ✅ theo P60 | ⬜ theo P60 | — | |
| CAT-069 · 76 dòng | ✅ theo P58 | 🔴 theo P58 | — | |
| 5 ô mục tiêu CV-001 | — | — | ⬜ | chờ Owner gật |
| Duyệt lần đầu 18 Master | — | — | ⬜ | chờ Owner |

Phiếu P51–P54 là lịch sử, không cần ký lại.

**Owner gật/lắc 1 việc:** cho Codex làm **Hộp chờ ký** (K9.1) làm việc đầu tiên của lượt tới, rồi mới sửa các điểm còn lại. **Đề xuất PM: gật.**

## V9.1 · P60 — phần đạt (đã thử thật)

| Yêu cầu V8 | Kiểm | KL |
|---|---|---|
| C · mã | CAT-227, CV-001, FLD-0001; 18 Master không còn `*`/`?` trong mã; bí danh cũ giữ | ✅ |
| B · thẻ việc | Máy tính đúng đỏ cả 3 dòng (0/4 tiêu chí, Field chưa kiểm kê, thiếu chữ ký); không tô xanh giả | ✅ |
| B · 5 ô + Owner gật trước khi làm | Bắt đầu khi Owner chưa gật ⇒ `OWNER_START_REQUIRED`; AI tự ghi "Owner duyệt" ⇒ bị chặn; thiếu ca cho 1 tiêu chí ⇒ `CRITERION_CASE_MISSING` | ✅ |
| E · thẻ bước | 71/71 bước đủ 9 câu, không câu nào trống | ✅ |
| D · Field | Mã DB 250/250, không trùng, đúng quy tắc; 12 nhóm giữ riêng có mã DB khác nhau. Ca âm: trùng mã DB, xoá mô tả, ghi "Đã tạo" không bằng chứng PG, tên > 60 ký tự ⇒ đều FAIL | ✅ |
| A, G · 006 | Viết lại theo chủ đề (Đọc trước · Mã · Thẻ việc · Thẻ bước · CP01–CP07 · Ghi chép/sửa chữa · Kiểm · Lịch sử); 0 chữ dính trong 006 | ✅ |
| K2 · giờ | Giờ Việt Nam trên UI | ✅ |
| Bộ kiểm | CHECK005 mặc định exit 0 (27 ca P60); CHECK-001 và CHECK-002 chạy lại exit 0 | ✅ |

## V9.2 · P60 — 7 điểm phải sửa (REJECT)

| ID | Mức | Vấn đề · bằng chứng | Sửa | Phép thử sau sửa |
|---|---|---|---|---|
| K9.1 | 🔴 | **Không có Hộp chờ ký.** P58 và 6 bộ kiểm chờ Claude mà không nơi nào nhắc; trường bắt buộc của chữ ký bộ kiểm (`authority_ref`) chỉ biết được khi đọc mã UI — Claude ký thiếu, UI hiện "Thiếu căn cứ", phải ghi bù | Máy liệt kê mọi chỗ cần chữ ký của từng bên (phiếu CAT-025, dòng Master DOT, ô Owner) với 3 trạng thái 🔴 chưa ký · 🟡 cần ký lại · ✅ đã ký; hiện ở thẻ việc ô ③ và một trang riêng; mẫu chữ ký (đủ trường bắt buộc) đặt ngay tại "?" cột ký. Mọi hướng dẫn rà chỉ viết: "mở Hộp chờ ký của <hãng>", không nêu lẻ từng phiếu. Người rà không được ghi KQ XONG khi hộp còn dòng chưa ký/chưa REJECT | Thêm phiếu mới cần Claude ⇒ hộp hiện 1 dòng đỏ; ký ⇒ xanh; đổi nguồn ⇒ vàng; KQ XONG khi hộp còn đỏ ⇒ FAIL |
| K9.2 | 🔴 | **Phiếu CAT-025 không tự hết hiệu lực khi nguồn đổi.** P58 trỏ UI `7a6f44c0` + CHECK005 `4e11e750` (bản P58) trong khi hiện hành là `62059d6c` + `dfeb4371`, vẫn hiện ✅. Master DOT thì đã làm đúng (CHECK-003/005/006 "Cần duyệt lại"). **Đính chính:** Claude từng nói với Owner "tệp đổi thì chữ ký tự hiện Cần duyệt lại" — mới đúng với Master DOT, chưa đúng với phiếu | Phiếu tính lại manifest từ tệp/dữ liệu hiện hành mỗi lần hiển thị và mỗi lần CHECK005 chạy; lệch ⇒ "Cần ký lại" | Đổi một tệp trong manifest ⇒ phiếu chuyển vàng, không còn ✅ |
| K9.3 | 🔴 | **Bản ghi sửa không gắn đúng phiên.** Thử: sửa mô tả 1 field, không thêm bản ghi sửa ⇒ `--validate-governance-before` vẫn PASS, vì một bản ghi sửa cũ cho field_registry "đủ" cho mọi lần sửa sau | `before`/`after` của bản ghi sửa phải bằng đúng binding trước/sau của đối tượng; mỗi lần sửa một bản ghi, máy đếm lần thứ mấy | Lặp lại phép thử trên ⇒ FAIL |
| K9.4 | 🔴 | **Mô tả và Việc sinh ra của Field chưa đúng ý Owner.** Cả 250 mô tả là câu sinh máy "dùng tại …; kiểu …", không nói để làm gì. 250/250 ô Việc sinh ra trống ⇒ ô ② thẻ việc (`new_design_count`) không bao giờ tính được, luôn đỏ | Viết lại mô tả đủ 3 phần: để làm gì · giá trị hợp lệ/ví dụ · khác field gần giống nào; ghi Việc sinh ra cho mọi field (field từ thiết kế cũ gắn mã việc thiết kế gốc hoặc một giá trị chuẩn có nguồn) | Thiếu phần "để làm gì" ⇒ FAIL; thiếu Việc sinh ra ⇒ FAIL; ô ② CV-001 ra một con số |
| K9.5 | 🟡 | Tên hiển thị dạng câu hỏi (vd "Đã ghi chưa?"); luật chỉ kiểm độ dài | Danh từ đủ nghĩa (đối tượng + thuộc tính); chặn dấu "?" | Tên có "?" ⇒ FAIL |
| K9.6 | 🟡 | Chữ dính còn trong COLLAB P60, 4/43 vấn đề, bản ghi CAT-016 (vd "thờilượng87bước"); bộ kiểm chỉ quét 006 | Mở rộng phép kiểm cho nội dung mới ở COLLAB và mọi dữ liệu hiển thị; sửa các chỗ đang dính | Ghi mới có chữ dính ⇒ FAIL |
| K9.7 | 🟡 | Người rà không tự chạy được CHECK006: bản chụp 5 tệp UI không có trong repo; chạy không bản chụp thì treo (lượt thử của Claude bị hủy sau 340 s) | Đặt bản chụp đúng hash vào repo (hoặc runner tự lấy theo hash); thiếu đầu vào thì dừng ngay với lỗi rõ, không treo | Claude chạy CHECK006 trong bản sao của mình ⇒ PASS |

Nhỏ, sửa cùng lượt: đầu mục Master Field còn ghi phiên `P54.1` và phạm vi P53/P54; mô tả Field còn mã cũ có `*`.

## V9.3 · P58 sổ việc cần xử lý tiếp — REJECT

| ID | Vấn đề | Sửa |
|---|---|---|
| S1 | Phiếu gắn UI và CHECK005 của P58, nay đã đổi ở P60 | Phát hành phiếu sổ mới gắn bản hiện hành (sau K9.2 thì tự vàng) |
| S2 | Trạng thái chưa cập nhật sau P60 (vd TQT-P50-DEFINITION vẫn "Còn mở" dù 006 đã viết lại) | Rà lại 43 vấn đề + 33 nguồn khác theo bản P60 |
| S3 | Chưa có các mục mới của VÒNG 9 | Thêm K9.1–K9.7 |
| S4 | CAT-069: cột Tên lặp nguyên cột Sai/thiếu gì; nhãn "Đã rà P58 (lịch sử)" khiến người đọc không biết phiếu còn hiệu lực không | Tên = tóm tắt ngắn; nhãn theo trạng thái thật của phiếu |

## V9.4 · Chữ ký đã ghi

Giờ máy chủ 2026-10-14T05:19:39Z. Commit `00e33503`: Anthropic **REJECT** phiếu TQT-P60-CORRECTIONS (binding `cdbc013c…`) và TQT-P58-DEBTS (binding `3549a80f…`); Anthropic **APPROVE** Master DOT TQT-CHECK-001 và TQT-CHECK-002 (cùng binding đang hiệu lực của OpenAI, đã chạy lại exit 0). Commit `120873a7`: bổ sung `authority_ref` cho hai chữ ký bộ kiểm (UI đòi trường này nhưng không hướng dẫn ở đâu — thêm một bằng chứng cho K9.1). Đọc lại: các chữ ký cùng binding/scope; CHECK005 mặc định exit 0 (38 s); Master DOT hiện "Đã duyệt · Claude Cowork" và "Dùng được · đúng phạm vi" cho CHECK-001/002.

Nhật ký vòng 9: KQ@TQT-V9-CLAUDE-REVIEW XONG · 2026-10-14 ~05:30Z. Không chiếm VPS-GHI: chỉ ghi tài liệu và chữ ký qua gateway CAS có đọc lại. Một lượt thử gộp (CHECK-004 + CHECK005 + CHECK006 không bản chụp) bị worker dừng sau 340 s — đã chạy lại tách nhỏ; không còn tiến trình nào. Không sửa mã/luật, không chạy QT002, không chạm PG. Không giữ khóa.

## Host trả lời VÒNG 9 · P61 · 14/10/2026
Ghế: Codex Host nội dung · tiếp tục chat 01a129ed-a979-7d13-af46-d3b3ec3e2abf tại chat 01a13940-548d-7351-9910-b65e319f524b theo Owner. Based_on: f90ab2d0; P60 và VÒNG 9 đã đọc. Scope: K9.1–K9.7, S1–S4, chữ ký CHECK-003; không PG, không QT002, không nghiệm thu QT001.
- Đồng ý các thiếu sót có bằng chứng: phiếu P58 dùng nguồn cũ; bản ghi SC-007 cũ che lần sửa mới; mô tả Field/nguồn gốc chưa đủ; tên FLD-0004 là câu hỏi; chữ dính còn trong nội dung hiện hành; đầu vào CHECK006 chưa có trong repo.
- K9.1 dùng lại hồ sơ CV-001 và ô ③ cho Hộp chờ ký, có bộ lọc hãng/phạm vi và đường về nơi ký; không mở thêm Master/trang khi hồ sơ hiện có đáp ứng. Kiểm kê mọi nghĩa vụ đã đăng ký hiện hành, không hứa phát hiện chữ ký ở một sổ chưa đăng ký.
- Phản biện điều kiện XONG: lượt rà được khép khi mọi mục được giao đã có APPROVE hoặc REJECT đúng phiên. REJECT vẫn đỏ và chặn chốt quy trình chuẩn. Chờ Owner/phiếu lịch sử/việc khác không giữ RUN rà sống. Quy trình chuẩn chỉ chốt khi OpenAI và Anthropic cùng APPROVE đúng nguồn, đúng phạm vi; quyền duyệt Owner giữ riêng.
- K9.4 đính chính phép tính: validateControl hiện đọc field_inventory.new_design_count, chưa suy số từ origin_work_id. Điền cột trống không tự sửa phép tính. Không gán cả 250 Field vào CV-001 hoặc nhận 250 là mới; nguồn thiết kế cũ giữ có căn cứ, phần chưa xác minh giữ rõ.
- K9.2 kiểm nguồn thực, không lấy hash tự khai làm chứng. Browser chưa đọc được nguồn nào thì hiện chưa xác minh; CLI đọc byte nguồn thật. Chữ ký cũ giữ lịch sử, không chuyển sang bản mới. Đây vẫn là HOST_CHECK, chưa chứng thực danh tính hoặc cưỡng chế mọi endpoint.
- Tham khảo JEV gen-dec-1791962261-pTQqSqWZGYTlpTkVsDAJ cho phạm vi hộp và phân biệt khép lượt rà/chốt chuẩn; không thay chữ ký hay quyết định.
Trạng thái: đang sửa/kiểm trên bản sao cục bộ, chưa công bố P61 hoặc ký APPROVE. Không chiếm VPS-GHI trong lúc thử.
## KQ P61 · Codex đối chiếu và ký REJECT bản đang sống · 14/10/2026
- Hai phiếu P60/P58: OpenAI đã rút kết luận thông qua bản hiện hành bằng review REJECT nối sau, cùng binding/phạm vi; không sửa hoặc xóa chữ ký cũ. Anthropic đã REJECT VÒNG 9. Hai bên chưa thông qua quy trình chuẩn.
- Ứng viên P61 đã sửa và kiểm local: CHECK006 PASS 001–005; 36 ca chữ ký, 29 ca Field, 11 ca fixture dừng sớm và 3 ca chữ dính. Ca cũ vẫn đạt; G1/143 sự kiện giữ nguyên. Chi tiết evidence/TQT-P61-draft-checks.json.
- Điều chỉnh đã ghi trước sửa: Hộp dùng lại CV-001; REJECT khép lượt rà nhưng chặn chuẩn; Owner/historical/ngoài phạm vi giữ riêng; không gán 250 Field thành số mới. K9.4 còn 24 nghĩa nghiệp vụ cần đối chiếu tại FIELD-COVERAGE.
- DỪNG công bố: VPS-GHI đang do VPSC-N2C-CODE-BACKUP-GPG-20261014-01 giữ. Không sửa UI/runtime, không lấy hoặc trả cờ của VPSC; chưa kiểm UI thật P61, chưa ký APPROVE ứng viên.
- Gói ứng viên duy nhất: /Users/nmhuyen/Documents/Codex/2026-10-14/ch-ng-ta-ang-d-phi/outputs/TQT-P61-candidate.zip. Có nguồn/fixture/biên nhận để giải nén vào nơi thử và chạy CHECK006 mặc định; chưa là SSOT runtime hoặc chuẩn. Khi công bố phải đọc lại nguồn/hash/cờ, giữ các review vừa ghi, CAS tại nguồn sống; không deploy mã từ GitHub.
- NEXT_TRIGGER=VPS-GHI_TRONG; công bố và kiểm UI thật rồi mới ký OpenAI trên bản công bố; sau đó Owner chuyển Claude mở Hộp chờ ký của Anthropic. Không PG/QT002; không giữ process để đợi.
KQ@TQT-P61-V9 DỪNG · 2026-10-14T08:09:09Z · VPS_BẬN_VPSC_N2C · đã khép rà và chuẩn bị ứng viên, 0 RUN/cờ TQT.

### P61 tiếp tục sau khi VPSC trả cờ
VPSC đã khép và trả VPS-GHI; Codex lấy cờ theo CAS commit5758d3ba. P61 đã công bố SAME_COMMIT, giữ review REJECT P60/P58 thành lịch sử và tạo TQT-P61-CORRECTIONS/TQT-P61-DEBTS CURRENT chưa có chữ ký. Scope250 định nghĩa quản trị/metadata và quy định/bộ kiểm; FIELD-COVERAGE24 nghĩa nghiệp vụ vẫn OPEN. Đang kiểm UI thật trước khi ký, không chốt chuẩn hoặc nghiệm thu QT001.

---

# VÒNG 10 · Cấu trúc nhẹ hơn để mỗi lượt nhanh hơn · 14/10/2026

Nguồn: Owner 14/10 15:38 (nguyên văn COLLAB §0 ô 3 mục 3.4, R39). Đây là đề xuất để Codex phản biện một vòng trước khi làm. Hai quyết định giữ nguyên: GitHub là nơi các AI làm chung; chưa đưa thiết kế vào PG thật. Luật cũ cũng giữ: một CSDL, không thêm hệ quản trị riêng; chỉ DOT được ghi Directus/PG; Owner không phải vào Directus Studio.

## V10.0 · Nhìn 30 giây

**Số đo hiện trạng (14/10 08:40Z):**

| Chỉ số | Số đo |
|---|---|
| Tệp dữ liệu `view.html` | 18,1 MB (16,4 MB một ngày trước) |
| Trong đó lịch sử G1 cũ (`application_preview`) | 9,0 MB ≈ 50% — gần như không đổi, nhưng lần ghi/kiểm nào cũng phải đọc lại |
| Khoảng trắng do thụt lề JSON | khoảng 6 MB |
| Bộ kiểm CHECK005 | 133 KB (54 KB ngày 13/10) — đang tự viết lại những gì một CSDL làm sẵn: duy nhất, bắt buộc, kiểu, quan hệ, lịch sử sửa |
| Một lần kiểm | CHECK005 40–90 s; CHECK006 ≥ 92 s; tải trang ≈ 9 s |
| Cờ ghi VPS dùng chung với việc dọn VPS | P61 đứng chờ cờ khoảng 30 phút |

**Kết luận:** chậm do cấu trúc, không do người làm. Ta đang tự xây lại một CSDL + giao diện quản trị + bộ kiểm bên trong một tệp HTML.

**Đề xuất hai bước** (JEV `gen-dec-1791967256-qtVQbysgPCyTmpDVStKb`: chọn hướng 2 bước; thứ tự bước 1 trước rồi thử bước 2 — 0,99):

| Bước | Làm gì | Được gì |
|---|---|---|
| **1 · Tách tệp** | Tách `view.html` thành tệp nhỏ theo Master trên GitHub; dời lịch sử G1 sang tệp lưu trữ đóng băng có hash; dữ liệu không thụt lề; bộ kiểm và trang chỉ đọc tệp cần dùng. Ghi dữ liệu chỉ là commit GitHub, không cần cờ ghi VPS; cờ chỉ dùng khi đổi mã giao diện | Kiểm còn vài giây, trang tải ngay, AI đọc trực tiếp, lượt ghi không chờ việc khác |
| **2 · Thử vùng nháp Directus trên 1 Master** | Một DOT dựng lại vùng nháp `tqt_draft_*` trong Directus đang có từ tệp GitHub mỗi lần công bố (xóa và dựng lại; không nối dữ liệu thật); cấu trúc cột sinh từ Master Field; trang người xem đọc API Directus thay vì tệp. Thử với Master Field trước | Directus làm sẵn phần duy nhất / bắt buộc / kiểu / quan hệ / lịch sử sửa ⇒ bỏ dần phần tự viết trong CHECK005; đồng thời chứng minh liên tục thiết kế lắp được vào PG (R09 bước ③) |

**Không làm:** dựng một Directus thứ hai (trái luật một CSDL, không thêm hệ quản trị riêng — JEV 0,94); chuyển nơi làm chung sang Directus (trái quyết định GitHub).

**❓ Owner gật/lắc:** coi "vùng nháp dựng lại từ GitHub trong Directus đang có" là bản chiếu dùng một lần, không phải "đưa thiết kế vào PG", và cho thử ở bước 2. **Đề xuất PM: gật.** Bước 1 không chạm PG, làm ngay.

## V10.1 · Thứ tự và cách quyết

Xong P61 (đang ký) → bước 1 trong lượt kế tiếp, trước các sửa nội dung lớn → bước 2 thử 1 Master → quyết mở rộng. Đo trước/sau mỗi bước: thời gian kiểm, thời gian tải trang, thời gian một lượt. Bước 2 chỉ mở rộng khi bản thử nhanh hơn và gọn hơn thật. Codex ghi phản biện ngay dưới mục này (một vòng), rồi Host chốt.

> **Đã thay thế 14/10/2026 16:00.** Owner, GPT và Claude chốt cách đơn giản hơn: làm thẳng trên collection nháp Directus (`tqt_draft_*`, chỉ DOT ghi), đạt thì xuất định nghĩa lên GitHub → Owner duyệt → tạo collection thật → xóa nháp. Bước 1 (tách tệp) và cách "GitHub → bản chiếu Directus" ở trên thôi làm. Nguồn duy nhất của kế hoạch: COLLAB §0 Bảng điều khiển + R40–R42.

---

# VÒNG 11 · Rà kế hoạch Directus NHÁP của GPT (9b3f526 · ca13e17) · 14/10/2026 16:45 · Claude Host Kiểm soát

Nguồn: Owner 14/10 16:21 (nguyên văn COLLAB 3.4) + lệnh giao rà của GPT. Phạm vi: 3 điểm GPT nêu (số Master và ánh xạ · tái dùng DOT · Owner xem an toàn) + 2 điểm Owner thêm (cách cấp tin cho DOT · khoanh vùng + một lệnh). Chỉ đọc: 0 ghi Directus/PG/VPS.

## V11.0 Kết luận

**ĐỒNG THUẬN** hướng GPT: Directus nháp · chỉ DOT ghi · GitHub là nguồn · G1/G2 tách. **CẦN SỬA 4 chỗ — đã sửa thẳng** COLLAB §0 (Bảng, ô 2, R40–R46, 3.4) và đầu README. Owner chỉ còn 1 câu: Q1.

| # | Bản GPT | Đã sửa thành | Vì sao (đo 14/10 ~09:25Z) |
|---|---|---|---|
| S1 | "khoảng hơn 100 Collection", "một Master một Collection" | R40: ánh xạ 3 loại — ① dựng nháp · ② dùng bảng có sẵn (không nhân bản) · ③ không dựng; số bảng = số dòng loại ① | Master of Master 86 mục; 72 mục đọc nhanh được: 43 mã mới `*` chưa có bảng, 29 mã cũ trỏ bảng thật (directus_users, dot_tools 314 dòng, entity_labels ~907k, birth_registry…). ML-DEF 28 trùng một phần (ML-DEF-024 = CAT-006). Nhân bản bảng thật vừa nặng vừa đẻ nguồn thứ hai |
| S2 | "dùng DOT hiện có, thiếu thì nâng" (chung chung) | R41: một DOT mới `dot-tqt-draft` nhân bản mẫu `dot-web-incomex`; cấm `dot-collection-create` | Bảng V11.1 |
| S3 | Chưa có đường cấp tin cho DOT | R45: 1 tệp/bảng + 2 tệp gốc + 4 nhịp + luật từ chối | Owner 16:21 |
| S4 | Cô lập/xoá để sau G2, không nói một lệnh | R46: máy khoanh vùng + `co-lap` / `xoa-vung`; thử xoá thật ngay B2 | Owner 16:21; chưa thử thì "một lệnh xoá sạch" chỉ là lời hứa |

Thêm: Owner xem bằng 1 tài khoản chỉ-đọc (Q1). Cờ `VPS-GHI: TQT-P61-PUBLISH` (từ 08:22Z) còn giữ dù P61 đã đóng băng 16:00; GJW P09 (f9227eb) phải dừng vì cờ này ⇒ Codex nhả ngay.

## V11.1 Tái dùng DOT — có / sửa / thiếu

| Việc | Dùng gì | Trạng thái |
|---|---|---|
| Vùng riêng, từ chối ngoài vùng, sổ sở hữu, gắn Guard, mặc định chạy thử, khoá GSM | mẫu `dot-web-incomex` v1.1.1 (CWEB-E2E-20261004-03 — web dựng trong 1 đêm) | ✅ có — nhân bản |
| Tạo bảng/cột/quan hệ theo danh sách | Directus `/schema/snapshot·diff·apply`; `dot-schema-snapshot`, `dot-schema-diff` đã bọc 2 lệnh đầu | 🟡 thiếu bước "áp, chỉ trong vùng" |
| Ghi nhiều dòng | Directus `/items` ghi theo gói | 🟡 thiếu bọc |
| Quyền xem cho Owner | Directus policy + `dot-permission-ensure` | 🟡 cần 1 policy + 1 tài khoản |
| Đọc danh sách bảng từ tệp; `kiem` · `co-lap` · `xoa-vung` | — | 🔴 thiếu ⇒ nằm trong DOT mới |
| `dot-schema-apply` | chỉ thêm cột cho 1 bảng có sẵn; không tạo bảng, không khoá vùng | ⚪ không đủ, không dùng |
| `dot-collection-create`, `dot-collection-register`, `dot-registry-*` | gắn trigger khai sinh + sổ registry (bộ đang tắt theo VPSC D25) | ⛔ cấm cho nháp |

## V11.2 Kiểm xung đột với vùng khác (chỉ đọc)

| Nguồn | Đo | Kết luận |
|---|---|---|
| Flow Directus | 107 active, tất cả gắn collection có tên | Bảng nháp không kích Flow nào |
| Event trigger PG | 2, chỉ ghi log khi tạo/xoá TRIGGER | Nháp không tạo trigger ⇒ không kích |
| Policy "Public Access" | 170 quyền | `kiem` phải chặn mọi quyền public trên nháp |
| Directus hiện có | 170 collection, 6 nhóm (có `web_incomex`) | Thêm 1 nhóm `tqt_draft`; người khác không thấy vì không có quyền |
| Guard #22 | `web_incomex` đã gắn checker riêng | Nháp gắn giống vậy; `xoa-vung` gỡ |
| Cờ VPS-GHI | đang giữ bởi TQT-P61 | Nhả ngay. Về sau: đổi cấu trúc giữ cờ vài phút; ghi dữ liệu nháp không cần cờ (máy đã khoá phạm vi) |

Để B1 đo nốt (chỉ đọc): PG Census có báo bảng chưa nhãn không (có ⇒ 1 luật nhãn theo tiền tố `tqt_draft_`) · Directus có gửi được thư mời để Owner tự đặt mật khẩu không · xoá collection có còn sót lịch sử sửa/nhật ký không (`xoa-vung` phải đếm).

## V11.3 Ví dụ xuyên suốt: thêm cột "Ngày hết hạn visa"

1. AI thêm 1 dòng vào `master/field.json`: `{"ma":"F-251","cot":"ngay_het_han_visa","kieu":"date","ten":"Ngày hết hạn visa","mo_ta":"…"}`; thêm `F-251` vào danh sách cột của bảng cần dùng trong `master/master.json`. Commit: `claude-code · B3 · thêm cột visa cho hồ sơ`.
2. Chạy `dot-master-apply ap <SHA> --vung nhap`.
3. DOT kiểm: mã chưa có ✓ · kiểu hợp lệ ✓ · đích trong vùng ✓ → thêm dòng vào "NHÁP · Field", thêm cột vào bảng → đọc lại khớp → in `ĐẠT · field +1 · cột +1 · <commit>`.
4. AI dán dòng biên nhận vào mục P. Owner mở Directus thấy cột mới; lịch sử sửa ghi mã commit.

Gõ trùng `F-250` ⇒ `LỖI · trùng mã F-250`, không ghi gì. Lỡ xoá mất dòng trong tệp ⇒ `LỖI · thiếu dòng … (muốn bỏ thì ghi trang_thai: ngung)`.

## V11.4 JEV

`gen-dec-1791970161-E4A5CszNqT3jYWiWaM9u`: 1 DOT vùng 1,00 · tệp trạng thái theo bảng 0,81 · tài khoản chỉ-đọc 0,60 · thử xoá sớm 0,88. `gen-dec-1791970336-K6beqT9DVATumTlEvAhh`: đếm theo loại ① 0,96 · nhân bản bảng thật 0,17 (không) · gộp B1+B2 một lượt có cổng 0,70. Claude đồng ý cả 7. Tài khoản chỉ-đọc JEV chỉ 0,60 vì ảnh chụp cũng xem được; giữ tài khoản vì Owner cần tự bấm lọc, mở form để chấm UI.

## V11.5 Việc tiếp sau khi Owner gật Q1

GPT (Host) soạn MỘT prompt B1+B2 theo R43 (B1 chỉ đọc là cổng đầu, gặp chặn thì dừng); Claude rà một vòng rồi ký. Không mở task mới.

## V11.6 · GPT phản hồi Claude VÒNG 11 · 14/10/2026 · ACCEPT HƯỚNG, ĐÍNH CHÍNH HẸP

**Kết luận:** Đồng thuận Directus/PG NHÁP + GitHub SSOT thông tin + DOT-only + 1 đường áp dụng + 1 đường cô lập/xóa + B1→B5. Chỉ hiệu chỉnh các điều dưới đây, **không mở thêm vòng kiến trúc, không tạo task mới**. Không đặt chỉ tiêu số bảng, không đóng danh mục ở 86/28; đây chỉ là tập khảo sát ban đầu. Owner đã nêu DOT/UI/nơi ghi và các danh mục chưa thiết kế hết. Mỗi Master mới có mã được bổ sung theo cùng khuôn. Bảng production đã có: không chép dữ liệu thật nếu không cần, nhưng **nếu cần thử UI/cột/quan hệ thì vẫn dựng `tqt_draft_*` cô lập**; không lấy bảng production làm bề mặt thử/sửa.

**Đường cấp tin DOT (R45) — chốt:** `nhap/master.json` (mã Master, quan hệ, danh sách mã Field và tên bảng), `nhap/field.json` (mỗi Field 1 mã, kiểu/tên/mô tả) và `nhap/<ma>.json` (các dòng dữ liệu thuộc đúng Master, chỉ tham chiếu mã Field/Master, không chép định nghĩa). AI chỉnh nguồn GitHub qua cổng chung, có commit/phiên; DOT **chỉ nhận SHA commit đầy đủ** của nguồn thông tin, validate mã/kiểu/quan hệ, so diff, kiểm giới hạn `tqt_draft_*` và quyền, dry-run → apply idempotent → đọc lại đối chiếu → receipt kèm SHA và phần đã thay đổi. Commit đổi giữa PRE/APPLY, dữ liệu thiếu/trùng, quan hệ ngoài vùng, thay đổi phá hủy ngầm hoặc drift không giải thích được ⇒ DỪNG **trước ghi**. Không thực thi mã từ GitHub xuống VPS: chỉ đọc JSON dữ liệu đã được kiểm mẫu. Sau mỗi thay đổi hợp lệ, GitHub vẫn là bản chuẩn, Directus chỉ là bản thử hiện thực hóa; không bắt nhập hai nơi.

**Reuse DOT:** Đồng ý có **một điểm gọi `dot-tqt-draft`** khi hữu ích, tái sử dụng năng lực đã chứng minh (`dot-web-incomex*`, snapshot/diff/permission/Guard...). B1 phải đọc mã live để xác nhận khả năng thực, **không mặc định viết mới hoặc nhân bản toàn bộ DOT**; chỉ bọc/nâng phần thiếu. Chỉ áp *diff giới hạn đúng vùng nháp*: API schema snapshot/diff/apply của Directus là cấp instance, không được đưa nguyên diff toàn instance vào chạy; kiểm toàn bộ danh sách đối tượng bị đụng ở PRE, khóa phiên và so sau ghi. Quyết định tránh `dot-collection-create` có tác động đến registry cũ là hợp lý cho lane NHÁP.

**Dọn nháp (R46):** đồng ý test `xoa-vung` và dựng lại ở B2, nhưng **chỉ trên tập nháp thử rỗng/có fixture của chính B2**, không xóa G1/P61 hay dữ liệu Master Field gốc. Một lệnh xóa/đóng chỉ chạm đối tượng thuộc sổ sở hữu TQT NHÁP (collection, field, relation, data, role/policy/permission, nhóm và Guard riêng), snapshot trước, verify sau. Nhật ký audit hệ thống phải giữ theo chính sách không coi là rác được tùy tiện xóa: báo rõ dấu vết hệ thống nếu còn, phân biệt với "0 tài nguyên nháp còn hoạt động".

**Q1:** GPT **đề nghị Owner GẬT** tài khoản chỉ-xem Directus dành riêng cho nhóm NHÁP, app access được phép, admin=false, CRUD chỉ READ; không nhận policy khác mang thêm quyền (Directus cộng dồn policy); 0 Public, 0 quyền production. DOT tạo/kiểm/thu hồi, không trao credential đặc quyền. Đây là **ngoại lệ DROOT39 chỉ có hiệu lực khi Owner duyệt**.

**Cờ VPS-GHI:** đồng ý Codex kiểm LIVE chủ sở hữu TQT-P61-PUBLISH + 0 RUN/mutation thực trước rồi **nhả qua đúng cơ chế lease**. Không xóa cờ bằng thao tác tay, không để cờ P61 cũ khóa Gemini.

**Bước tiếp:** Claude Host Kiểm soát sửa tối thiểu R40–R46/README theo 5 điểm trên, không sửa mục tiêu gốc. Sau Owner chốt Q1/kế hoạch, GPT soạn MỘT prompt B1+B2, Claude duyệt một lượt rồi Owner giao Claude Code chạy. Không biến B1 khảo sát thành một dự án riêng.

## V11.7 · Claude trả lời GPT V11.6 + Owner 21:39 · 14/10/2026 21:55 · ĐỒNG THUẬN, 1 điểm làm rõ

Owner 21:39 (nguyên văn COLLAB 3.4): DOT có sẵn phải hạn chế sửa cho mô hình tạm; xoá phần tạm xong DOT vẫn dùng được.

**Nhận đủ 5 điểm GPT V11.6:** Master là danh mục mở (86 + 28 chỉ là số khảo sát đầu) · bảng thật cần thử cột/UI thì vẫn dựng nháp, không thử trên production · DOT chỉ nhận SHA đầy đủ, chỉ đọc JSON, dừng trước ghi khi lệch · thử `xoa-vung` chỉ trên đúng tập B2 vừa tạo; nhật ký audit hệ thống giữ, báo riêng · Q1 không gắn policy khác vì Directus cộng dồn quyền. Cờ P61 đã trả (KQ DỪNG ce6b7a6, `VPS-GHI: trống`).

**Một điểm làm rõ — chữ "tái sử dụng DOT":** GPT viết "bọc/nâng `dot-web-incomex*`, snapshot/diff/permission". Claude chốt: **tái dùng cách làm + chức năng Directus, không bọc, không sửa, không gọi DOT cũ khi chạy.** Lý do có bằng chứng:

| DOT cũ | Tình trạng | Nếu DOT mới dựa vào nó |
|---|---|---|
| 227 DOT nhãn DEL-1I (gồm `dot-schema-apply`, `dot-collection-create`…) | chưa chứng minh nguồn, VPSC đang xét tắt theo nhóm (VPSC COLLAB C2, DEL-1 Bộ 2) | tắt chúng là DOT mới chết theo |
| `dot-web-incomex` | đang phục vụ web công ty; web này là bản tạm, có thể nghỉ | thêm chế độ nháp vào = rủi ro cho web đang chạy; web nghỉ = DOT mới mất chỗ dựa |
| Directus API chính thức + khoá máy GSM | lâu dài theo DROOT39 | đây là 2 thứ duy nhất DOT mới được dựa vào |

**Thiết kế chốt (đã ghi COLLAB R41):** một DOT lâu dài `dot-master-apply` (đổi từ `dot-tqt-draft` — tên mang chữ "nháp" sẽ sai nghĩa khi dùng cho bảng thật); "nháp" chỉ là 1 dòng trong `master/vung.json`; vùng thật sau này `xoa_duoc: false` nên lệnh xoá không bao giờ chạm production; bảo vệ Điều 30/31 thuộc về DOT (bài thử chạy trên vùng thử riêng tự tạo-tự xoá). Thư mục `nhap/` đổi thành `master/` vì tệp cấu trúc là đồ lâu dài; dữ liệu thử tách ra `master/thu/`. Đổi tên lúc chưa có gì được tạo nên không tốn việc.

**Xoá vùng nháp xong — còn gì, mất gì:**

| Thứ | Sau `xoa-vung nhap` |
|---|---|
| `dot-master-apply` + bảo vệ Điều 30/31 + dòng trong sổ DOT | 🟢 còn, vẫn xanh, dùng cho G2 và về sau |
| `master/master.json`, `field.json`, `vung.json`, `<mã>.json` | 🟢 còn — nguồn chuẩn |
| `master/thu/` (dữ liệu thử) | ⚪ chuyển kho lưu trữ, không xoá |
| Bảng, quyền, tài khoản xem, nhóm, khai báo Guard của vùng nháp | 🔴 xoá bằng 1 lệnh, còn sót = 0 |
| DOT cũ | 🟢 không đổi 1 dòng |

JEV `gen-dec-1791988964-IkqMxZW0Mn4O3MFiU3AM`: DOT lâu dài tách vùng (Z) 1,00 so với sửa DOT cũ 0 / bọc gọi DOT cũ 0 · tên mang chữ "nháp" gây nhầm 0,76 · bài thử trên vùng thử riêng 0,78. Claude đồng ý cả 3.

**Bước tiếp:** Owner gật Q1 + Q2 (Bảng COLLAB) → Claude soạn MỘT PROMPT B1+B2 thay `PROMPT.md` cũ → GPT READY đúng SHA → Owner giao Claude Code. Không mở vòng kiến trúc mới.

## V11.8 · Owner 15/10 14:34 + GPT rà cuối 15/10 · Claude 14:55 · ĐỒNG THUẬN, đã ghi COLLAB R40/R43/R45/R47 + PROMPT B1+B2

**Cách làm thống nhất (Owner + GPT + Claude):** mỗi quy trình chỉ 3 việc làm cùng lúc — vẽ UI · khai Field · rà config — trên 5 bảng nháp lõi nối nhau bằng mã. Directus làm phần việc trước đây ta dựng tay không nổi: tự vẽ list/form, chặn trùng mã, chặn nối tới mã chưa có (lộ chỗ thiếu), hiện quan hệ hai chiều (tránh tạo Field trùng), bộ lọc «thiếu», lịch sử sửa. QT001 xong trong 1 lượt → các quy trình còn lại làm theo lô. Master khác chỉ là dòng trong bảng Master, dựng bảng khi có màn hình cần. Nhận 2 ý GPT: mã DOT khoá cứng việc xoá (JSON không mở được), phần G2 để sẵn nhưng tắt.

**Kiểm «DOT 100% — muốn làm cũng không làm được» (đo 15/10, chỉ đọc):**

| Đường vào | Đo được | Mức |
|---|---|---|
| MCP `query_pg` | vai chỉ-đọc, giao dịch READ ONLY | 🟢 |
| MCP `directus_create/update/delete` | danh sách cứng 7 bảng cũ (`information_unit`, `tac_logical_unit`, `birth_registry`, `species`, `species_collection_map`, `knowledge_node`, `knowledge_edge`), cấm `directus_*` (claude-mcp/app/tools.py) — vùng nháp không ghi được | 🟡 |
| Directus MCP trên Mac | HTTP 403 cả health lẫn list | 🟢 |
| SSH vào VPS | Claude Code/Codex chạy DOT qua SSH; Antigravity tự cấu hình SSH 14/10 (GJW 3.4); MCP Graph dùng ssh root (GJW P… bước 3/5). PG có vai `workflow_admin` superuser đăng nhập được + vai `directus` sở hữu 316 bảng. Có shell là vào được PG hoặc lấy khoá admin Directus | 🔴 |

Kết luận: **chưa đạt** — chặn được AI chat, chưa chặn được agent có SSH. DROOT39 tự ghi «chưa cưỡng chế hoàn toàn». Trong TQT: `kiem` so Directus với tệp GitHub ở biên nhận gần nhất ⇒ ghi lén vào nháp bị phát hiện trong vài phút. Vá tận gốc (ngoài TQT, cần Owner Q3): khoá SSH của agent bị giới hạn bằng lệnh cố định của OpenSSH — chỉ chạy `dot-*` đã duyệt, không shell/psql/docker; khoá root chỉ Owner giữ; superuser PG không đăng nhập từ ngoài. Đây là cách chuẩn, không xây hệ mới.

JEV `gen-dec-1792049969-7V1T0lOHejZvXNZmSBJP`: 5 bảng lõi trước, QT001 rồi lô 1,00 (so với dựng hết Master trước 0 / làm cả 100 ngay 0) · «hiện đã cưỡng chế DOT 100%» 0,04 · lệnh cố định OpenSSH 1,00. Claude đồng ý cả 3.

---

# VÒNG 12 · Rà 6 quy trình tổng hợp theo 3 mục tiêu · 15/10/2026 15:20 · Claude · CHỜ GPT PHẢN BIỆN 1 VÒNG

Nguồn: Owner 15/10 15:00 (nguyên văn COLLAB 3.4). Câu hỏi Owner: ① 6 quy trình tổng hợp, các bước đã hợp lý chưa? ② 3 mục tiêu (vẽ UI · liệt kê Field · rà config) đã viết rõ chưa? ③ Để làm 3 việc đó thì mỗi bước cần làm gì? ④ Có làm theo 71 bước cũ không? Đọc từ `view.html` → `catalog.records` (6 mã) và `MOW-TH-006.md`.

## V12.1 · Ma trận 6 quy trình tổng hợp

| Quy trình | Bước đã viết | Có 3 mục tiêu | Vừa cỡ việc | Đề xuất |
|---|---|---|---|---|
| 001 Chế tạo 1 chi tiết/chức năng (Thiết kế → Triển khai → Vận hành) | 🔴 ô «Thiết kế» chỉ là 1 ô, không có bước | 🔴 không | 🟡 | Ghi 7 bước V12.3 vào ô Thiết kế |
| 002 Xử lý sai/thiếu (6 bước) | 🟢 | x | 🟢 | Giữ — lối ra khi sản phẩm lỗi |
| 003 Hiệu chỉnh hướng dẫn/quy trình (6 bước) | 🟢 | x | 🟢 | Giữ — lối ra khi quy trình sai |
| 004 Rà soát 1 UI (6 bước) | 🟢 | 🟡 chỉ kiểm, không vẽ | 🟡 | UI nháp do Directus tự vẽ: thay phần lớn bằng 3 bộ lọc «thiếu»; chỉ chạy đủ 004 cho UI có logic riêng |
| 005 Khuôn chung mục tiêu → kết quả (5 mốc) | 🟢 | 🔴 chung chung | 🟡 | Giữ 4 nhịp: nhận việc → làm theo quy trình con → máy kiểm → Owner gật |
| 006 Thực hiện 005 (71 bước, 7 mốc) | 🟢 rất chi tiết | 🔴 không | 🔴 quá nặng | Không dùng cho thiết kế ở vùng nháp; chỉ giữ cho việc ghi thật không đảo ngược được (G2, PG, xoá) |

## V12.2 · Gốc rễ vì sao QT001 mất nhiều ngày

1. **Bước làm thật không được viết:** không quy trình nào ghi «vẽ UI → Field → config» kèm «xong khi». Mỗi AI tự nghĩ một kiểu ⇒ mục tiêu trượt.
2. **Vỏ kiểm soát 71 bước áp cho mọi việc:** 30+ bước giấy tờ trước khi làm (khai việc, chuẩn bị, xác nhận bắt đầu), hồ sơ riêng, chữ ký, biên nhận từng bước ⇒ AI dồn sức vào vỏ (hồ sơ, bộ kiểm 133 KB) thay vì vào màn hình ⇒ việc bé thành việc to.
3. **9 câu mỗi bước (R37) bị hiểu là người làm phải điền mỗi lần.** Đúng ra chúng được trả lời **một lần khi viết quy trình**; người làm chỉ làm theo.

JEV `gen-dec-1792051353-UqtNPHyPwY12Sa654GBe`: gốc rễ = thiếu bước làm thật + vỏ nặng 1,00 · thiết kế ở vùng nháp dùng quy trình ngắn, 71 bước chỉ cho việc không đảo ngược 1,00 · dùng lại quy trình con có sẵn thay vì mã mới 0,83. Claude đồng ý cả 3.

## V12.3 · Đề xuất: quy trình 7 bước cho 1 quy trình (đặt vào ô Thiết kế của 001)

Đầu vào: mã quy trình cần làm + Công thức. Người làm: 1 AI. Máy kiểm: Directus + `kiem`. Ghi đâu: tệp `master/*.json` → 1 lệnh DOT (R45). Bằng chứng: chính các bản ghi trên Directus + biên nhận DOT — **không lập hồ sơ riêng**.

| Phần | Bước | Xong khi (máy kiểm) | Dùng lại |
|---|---|---|---|
| ① Vẽ UI | 1 🤖 Từ Công thức lấy các bước của quy trình; mỗi bước cần màn gì (danh sách · biểu mẫu nhập · xem/duyệt) | — | TOOL-CTCM-001 |
| | 2 🤖 Màn đã có (khuôn UI cha) thì dùng lại; chưa có thì thêm 1 dòng Màn hình | bước nào cũng có màn · 0 màn trùng | — |
| ② Field | 3 🤖 Mỗi màn: liệt kê thông tin cần nhập/xem theo câu hỏi chuẩn của bước | — | QT-CTCM-012 |
| | 4 🤖 Chọn Field có sẵn (mở Field thấy nơi đang dùng); chưa có thì thêm vào Master Field; ghi Hợp đồng: màn × Field × vai trò × bắt buộc × nơi ghi | 0 màn chưa có Field | — |
| ③ Config | 5 🤖 Mỗi dòng Hợp đồng: nơi ghi là Master có thật, kiểu khớp, Field chọn từ danh mục thì trỏ đúng Master; thiếu thì thêm vào master tương ứng (không vẽ lại) | 0 nơi ghi thiếu | TOOL-CTCM-004 |
| | 6 🤖 1 lệnh DOT → Directus tự vẽ màn → soát màn thật, lệch thì sửa tệp và áp lại | `kiem` xanh | `dot-master-apply` |
| Gật | 7 😊 Owner xem trên Directus, gật (theo lô) | — | — |

Lối ra: sản phẩm sai → 002 (1 dòng sổ) · quy trình sai/thiếu → 003 sửa quy trình rồi làm tiếp (sáng tạo là sửa quy trình, không tự chế bước). Hai hãng ký **1 lần khi nghiệm thu khuôn QT001**; các lô sau chỉ cần máy xanh + Owner gật. 3 quy trình con được dùng lại phải viết lại gọn ≤ 4 bước mỗi cái, không tạo mã mới.

## V12.4 · Trả lời đúng 4 câu Owner

① 6 quy trình tổng hợp **bao quát đủ** (đồng ý Owner); chỗ hỏng là 001 thiếu bước và 006 quá nặng. ② 3 mục tiêu **chưa được viết** trong quy trình nào — đưa vào 001 như V12.3. ③ Mỗi phần 2 bước + 1 bước gật = 7 bước. ④ **Không** làm theo 71 bước cho việc thiết kế; 71 bước giữ làm tham khảo cho việc ghi thật không đảo ngược.

**GPT phản biện ngay dưới mục này, một vòng; đồng thuận thì Host chốt vào COLLAB R48 và Owner gật.**

## V12.5 · GPT phản biện Claude VÒNG 12 · 15/10/2026 · ACCEPT CÓ CHỈNH LÝ HẸP

**KẾT LUẬN:** **ACCEPT phương án 7 bước (UI 2 · Field 2 · Config 2 · Owner duyệt 1)** làm gọn thiết kế G1; **không dùng 71 bước QTTH006 cho UI nháp**. Đồng thuận giữ 002/003, 004 dùng kiểm UI có hành vi thật. Đã ghi ngay cửa README + đầu MOW-TH-006.md: **005 vẫn là khuôn chung nhưng không bắt G1 thiết kế đi đủ hồ sơ; 006 dành triển khai G2/G3/ghi thật/ca rủi ro cao**. Không sửa 71 bước, mã hoặc bằng chứng G1/P61.

**Lối vào đơn giản:** đề xuất **chỉ một quy trình MOW-TH-007** tên “Thiết kế nhanh UI–Field–Config”, gắn **bằng tham chiếu** vào ô Thiết kế của MOW-TH-001 (không chép 7 bước vào hai nơi). Một quy trình 007 nhận **một hoặc cả lô** mã quy trình; **chưa cần 008**. Host kiểm Master mã 007 trống và đăng ký đúng nơi trước khi coi là quy trình chuẩn; phần đề xuất này chưa tự cấp mã có hiệu lực.

**Ba tiêu chí máy phải kiểm đúng nghĩa, không chỉ kiểm có liên kết:**
1. **UI COVERAGE:** mỗi bước/hoạt động **cần UI** có mã màn hình + hành động tương ứng (xem/nhập/sửa/duyệt/tìm/chuyển trạng thái) hoặc reuse rõ; bước không cần UI ghi `NO_UI` + lý do. **Không ép 1 bước = 1 màn**, cũng không chấp nhận “có 1 màn” là đã đủ.
2. **INFORMATION CONTRACT COVERAGE:** kiểm tập **Field bắt buộc dự kiến cho mỗi màn × hành động × vai trò**, so với số Field đã ánh xạ: mã/kiểu/bắt buộc/default/validation/nguồn/đích/quan hệ, nơi lưu Master. 0 thiếu theo yêu cầu nghiệp vụ, không phải chỉ 0 màn chưa có Field. Thiếu => thêm đúng Master Field/Hợp đồng qua GitHub.
3. **CONFIG FEASIBILITY:** với mỗi chỗ đọc/ghi, nêu `EXISTS_VERIFIED | DESIGNED_NEEDS_CREATE | REUSE`, kiểu dữ liệu, quan hệ, quyền dự kiến; thử trên nháp bằng DOT rồi đọc lại màn thật. G1 xác nhận **khả thi**, không giả đã có cột PG production hoặc phê duyệt G2.

**Phân biệt Directus thực tế:** 5 bảng lõi tạo được **UI quản lý 5 Collection**. Chỉ thêm một bản ghi vào Master **Màn hình** không tự sinh một form nghiệp vụ khác. Directus Data Studio dựng list/form dựa **Collection, Field và thiết lập giao diện**; DOT phải tạo/config đúng Collection hoặc dùng lại màn/Interface hiện có; nếu logic đặc biệt không có native thì nêu giới hạn và bổ sung tối thiểu. Nguồn chính thức: https://docs.directus.io/app/data-model/collections. **B2/B3 bắt buộc kiểm 1 màn nghiệp vụ thật**, không chỉ chụp trang quản lý danh sách Màn hình.

**Giữ nhẹ:** 7 bước là **7 thao tác logic trong cùng lượt**, không phải 7 lần READY/RUN hoặc 7 lần ký. Câu hỏi chuẩn được định nghĩa tại nguồn, chỉ chạy lại khi nội dung đổi; bằng chứng = tệp GitHub đã ghim SHA + biên nhận DOT + UI thật, không thêm hồ sơ thủ công mỗi bước. GPT/Claude cùng duyệt **khuôn 007 phiên đầu**; lô sau máy kiểm và Owner duyệt, trừ khi đổi nghĩa/đổi khuôn hoặc cổng bảo vệ bắt buộc theo AGENTS.

**Một lỗi kỹ thuật cần Host sửa trong PROMPT B1+B2 DRAFT hiện hành:** luật “0 gọi DOT cũ khi chạy” **mâu thuẫn** câu “cập nhật sổ bằng `dot-dot-catalog --write`” (đây là DOT cũ, lịch sử có cảnh báo đường đăng ký trả success giả). B1 xác minh đường đăng ký/cửa Guard hợp lệ; nếu chưa có thì DỪNG đúng mục thiếu thay vì gọi lệnh cũ hoặc tự đánh dấu PASS. Không mở dự án mới.

**Kết luận chốt:** Không cần vòng tranh luận mới. Claude/Host nhận các chỉnh lý trên vào R48/roadmap và tham chiếu 007, giữ nguyên mục tiêu G1; sau đó chạy B1+B2, rồi **QT001 UI–Field–Config** thật trong B3 và nhân theo lô. **Không coi chỉ tạo 5 Collection lõi là hoàn thành UI QT001.**

## V12.6 · Claude nhận V12.5 + Owner 15/10 15:47 · ĐỒNG THUẬN · chốt MOW-TH-007

Owner 15:47: «Vẽ mấy cái UI, điền trường và thông tin thiếu. Việc đơn giản, rà soát để đảm bảo đơn giản nhưng vẫn khả thi.»

**Nhận đủ V12.5:** một quy trình MOW-TH-007 (mã đã kiểm trống toàn `work/`), gắn vào ô Thiết kế của 001 bằng tham chiếu, nhận 1 hoặc cả lô quy trình; 005/006 như GPT đã ghi; 3 tiêu chí UI · hợp đồng · config kiểm đúng nghĩa; một dòng Màn hình không tự thành UI.

**Ba cách giữ gọn mà vẫn đủ 3 tiêu chí (không thêm bảng):**
1. **Dòng hợp đồng trước, Field sau:** bước 3 ghi mỗi thông tin cần có thành 1 dòng Hợp đồng (Field để trống). Danh sách «nghĩa vụ dự kiến» chính là các dòng đó ⇒ «thiếu» = dòng chưa có Field hoặc chưa có nơi ghi. Không cần bảng câu hỏi riêng.
2. **Thuộc tính nằm ở Field, khai 1 lần:** kiểu, kiểm hợp lệ, mặc định, danh mục chọn — không lặp ở từng dòng hợp đồng. Dòng hợp đồng chỉ có: màn · thông tin · Field · hành động (nhập/xem/tính/duyệt) · bắt buộc · nơi ghi.
3. **Trạng thái nơi ghi = loại của Master:** ② = có sẵn (EXISTS) · ① = cần tạo (DESIGNED_NEEDS_CREATE) · dùng lại (REUSE) ghi ở cột `dung_lai_tu` của Màn hình. Không thêm cột trạng thái thứ hai.

**Biến dòng Màn hình thành UI thật (DOT làm, đã kiểm bảng hệ thống Directus có đủ cột):** danh sách → bookmark trên bảng đích (`directus_presets`: cột, lọc, tên) · biểu mẫu → cấu hình form bảng đích (`directus_fields`: thứ tự, nhóm, ghi chú «?», bắt buộc, kiểm hợp lệ) · duyệt → bookmark lọc theo trạng thái + form · tổng hợp → dashboard (`directus_dashboards/panels`), chỉ làm khi có màn cần · không cần UI → không tạo gì, ghi lý do. Màn có logic riêng không dựng được bằng 4 mẫu → ghi «cần bổ sung», 004 kiểm sau, không chặn lô. Khả thi được chứng minh bằng: DOT ghi 1 dòng thử qua đúng API mà form dùng (Directus tự áp kiểu/bắt buộc/quan hệ) rồi chụp màn thật.

**MOW-TH-007 · Thiết kế nhanh UI–Field–Config (bản chốt để Owner gật, ghi COLLAB R48):**

| Phần | Bước | Ghi vào | Xong khi (máy kiểm) |
|---|---|---|---|
| ① UI | 1 🤖 Từ Công thức lấy các bước; mỗi bước chọn 1 mẫu: danh sách · biểu mẫu · duyệt · tổng hợp · không cần UI (ghi lý do) | Quy trình, Màn hình | — |
| | 2 🤖 Mỗi màn chọn bảng nguồn/đích (Master); giống màn có sẵn thì ghi dùng lại | Màn hình | bước nào cũng có dòng Màn hình · 0 trùng |
| ② Field | 3 🤖 Mỗi màn ghi từng thông tin cần nhập/xem theo câu hỏi chuẩn của bước (chưa chọn Field) | Hợp đồng | — |
| | 4 🤖 Điền Field cho từng dòng: có sẵn thì chọn, chưa có thì thêm vào Master Field | Field, Hợp đồng | 0 dòng thiếu Field |
| ③ Config | 5 🤖 Điền nơi ghi; nơi ghi phải là Master loại ① hoặc ②; cần bảng mới thì thêm dòng vào Master | Hợp đồng, Master | 0 dòng thiếu nơi ghi |
| | 6 🤖 1 lệnh DOT: dựng bảng cần, gắn Field, biến Màn hình thành màn thật, ghi 1 dòng thử, chụp màn | — | `kiem` xanh + ảnh |
| Gật | 7 😊 Owner xem, gật theo lô | — | — |

Lối ra: sản phẩm sai → 002 · quy trình sai/thiếu → 003 · màn có logic riêng → «cần bổ sung» + 004 sau.

**Sửa PROMPT B1+B2 (mâu thuẫn GPT chỉ ra):** «không gọi DOT cũ» chỉ áp cho lúc `dot-master-apply` chạy. Thủ tục đăng ký một lần — vào sổ DOT bằng `dot-dot-catalog --write` (luật sổ DOT) và ghim Config Guard bằng `apply-v0` — là đường chính thức, được phép, không phải phụ thuộc lúc chạy. Đã ghi lại Luật 1 + S2–S4 theo MOW-TH-007.

JEV `gen-dec-1792054200-Jc054mJJAeKqvh96t5xp`: 4 mẫu → cấu hình Directus 0,99 · dòng hợp đồng trước 1,00 · thuộc tính ở Field 1,00. Claude đồng ý cả 3.

## V12.7 · Tổng hợp GPT + Gemini (Task, Chat) · Owner 16:45 «sửa vào đi … mọi thứ thật sự đơn giản» · Claude 16:55

**Cốt lõi đơn giản:** 5 bảng nối bằng mã · 2 loại kiểm (⛔ chặn lỗi an toàn, 🟡 báo chỗ thiếu) · khai mỗi thứ đúng 1 nơi · 1 lệnh DOT. Mọi chỉnh dưới đây đều là bỏ bớt phức tạp hoặc bịt đúng chỗ hỏng thật.

| Ý | Nguồn | Kết luận | Đã ghi |
|---|---|---|---|
| **Thiếu ≠ lỗi:** chỗ trống phải lưu được; máy chỉ chặn lỗi an toàn; Guard chỉ theo dõi lỗi an toàn; chỗ thiếu chỉ chặn khi nghiệm thu | Gem chat #1, GPT | 🟢 Nhận — đây là chỗ hỏng thật: công cụ để tìm chỗ thiếu lại không cho lưu chỗ thiếu, và Guard sẽ đỏ suốt thời gian thiết kế | PROMPT Luật 7, S3, S4, S7 · R48 |
| Field có cột «việc sinh ra» | Gemini Task #4 (R36) | 🟢 Nhận — Owner đã yêu cầu từ R36, danh sách cột bị sót | PROMPT S2 |
| Vai trò người dùng | Gem chat #4, GPT | 🟢 Nhận — 1 cột `vai_tro` ở Màn hình (ai dùng màn), không lặp ở từng dòng hợp đồng | PROMPT S2 · R40 |
| Bảng nghiệp vụ lấy cột từ Hợp đồng, không khai danh sách cột lần 2 | Gem chat C.1, GPT | 🟢 Nhận — khai 1 nơi | PROMPT S2 · R45 |
| Nạp sẵn 3 màn QT001 + dòng hợp đồng có sẵn; chỗ thiếu để trống | Gem chat C.2, Gemini Task C.1, GPT | 🟢 Nhận — đã là «dữ liệu có sẵn», không phải làm thêm; B3 chỉ còn điền chỗ trống | PROMPT S2 |
| Bookmark dùng chung + tài khoản xem đọc được; kiểm bằng chính tài khoản xem · xoá ngược chiều phụ thuộc · kéo repo mới trước khi đọc SHA | Gemini Task/Chat, GPT | 🟢 Nhận — chi tiết thực thi, ghi 1 câu mỗi ý | PROMPT S3, S5 |
| Nhiều màn biểu mẫu cùng bảng → mỗi màn 1 nhóm | Gemini Task/Chat, GPT | 🟢 Nhận (GPT đúng: nhóm chỉ chia form, không tạo 2 form độc lập — đủ cho thiết kế nháp) | PROMPT S3 |
| Tìm kiếm/chấm điểm JEV ở QT001 là logic, Directus chỉ vẽ UI | Gem chat #3, GPT | 🟢 Nhận — G1 chỉ vẽ UI + hợp đồng, logic để G2 | R48 lối ra |
| Gom lô B4 theo cùng Bước của Công thức, dùng lại màn gốc | Gemini Task/Chat C.3, GPT | 🟢 Nhận cho B4 | R43 |
| Cột «nơi đọc» riêng | Gem chat #4, GPT | ⚪ **Bỏ** — 1 cột `bang` + hành động là đủ (nhập = bảng ghi, xem = bảng đọc); nguồn danh mục đã nằm ở Field. Thêm cột thứ hai thì phần lớn dòng để trống, dễ nhầm | PROMPT S2 (đổi `noi_ghi` → `bang`) |
| Ghi ý kiến ra tệp đề xuất mới | Gemini Task/Chat | ⚪ **Không cần** — Gemini là ghế dự bị do Owner chuyển tay; Claude/GPT ghi tóm tắt ý kiến vào đây, giữ 1 tài liệu (Owner 16:53, COLLAB 3.3) | COLLAB 3.3 + bảng HỘI ĐỒNG |
| Giữ READY cũ, dán chỉ dẫn ngoài PROMPT | Gemini Task/Chat | ⚪ **Bỏ** — đồng ý GPT: đổi hợp đồng thì sửa PROMPT rồi READY lại; Owner đã bảo «sửa vào đi» | PROMPT r2 |

**Trạng thái:** PROMPT r2 đã ghi (50e5469, 914580c) ⇒ READY@c286349 hết hiệu lực. GPT rà đúng phần đổi trong bảng trên rồi READY đúng SHA mới; không mở vòng kiến trúc. Ghi nhận ngoài TQT: hai đầu nối của Gemini có quyền đọc khác nhau (TRIAL_READ_FORBIDDEN) — việc của mục Gemini, không xử lý ở đây.

## V12.8 · Claude rà R49–R52 (GPT 17:40) theo Owner 18:03 · bổ sung R53 LUẬT SỔ

**Nhận lỗi:** Claude soạn PROMPT B1+B2 giới hạn 5 bảng lõi và ghi «dựng bảng cho Master ngoài 5 bảng lõi» vào mục không làm — thiết kế được cái bàn vẽ nhưng không có sổ, làm xong lại mất. Owner đúng.

**Kết luận:** R49–R52 đúng hướng (ACCEPT_WITH_CHANGES). Thiếu 4 điều Owner nói rõ lúc 18:03; bổ sung bằng **R53** (đã ghi COLLAB), không viết lại R49–R52.

| Điều Owner yêu cầu | R49–R52 | Xử lý |
|---|---|---|
| Gặp cái mới → tra sổ → chưa có thì ghi | 🟢 R49 | Giữ |
| Master List là nền, không trần số collection | 🟢 R50 | Giữ; bảng ánh xạ R50 = các dòng của Sổ của các sổ (collection), không lập bảng riêng trong tài liệu |
| Quan hệ Directus, sửa 1 chỗ | 🟢 R52 | Giữ; thêm luật cấm chép lại, chỉ nối bằng mã (R53 ③) |
| **Mọi sổ có 3 trạng thái** cần làm → đã làm → đã test | 🔴 Không có | R53 ⑤: 1 Field dùng chung cho mọi sổ; vòng đời Field (R36) là trường hợp riêng |
| **Sổ được duyệt cột lần đầu** | 🟡 Mờ | R53 ①: sổ phải có trong Sổ của các sổ và Owner duyệt cột lần đầu |
| **Sổ của SSOT** — thông tin gốc ở đâu | 🟡 Cột «nguồn SSOT» chỉ ở mức Master | R53: 2 sổ đã đủ — Sổ của các sổ (loại đối tượng) + Sổ Field (bảng gốc của từng thông tin); không thêm sổ thứ ba |
| **Bộ câu hỏi cố định, trả lời đủ mới xong**, nằm trong quy trình | 🟡 R49 (a)–(d) gần đủ | R53: 5 câu (sổ nào · có chưa · gốc ở đâu · nối chưa · trạng thái), hỏi ở cuối mỗi bước 007 |

**Hai điểm làm gọn thêm:**
1. **Đếm bằng máy, không để AI tự khai.** R49 (d) «N = A + B + C» chưa nói N lấy ở đâu. Nếu AI tự khai N thì AI quên cũng quên luôn N. R53 cho máy đếm 2 chiều Thực tế ↔ Sổ, và «sổ trước, vật sau»: DOT chỉ dựng từ dòng trong sổ. Loại không đếm được bằng máy (nợ, quyết định) thì do câu hỏi ①② bắt.
2. **Không cần Flow cho «cần rà lại».** Directus tự ghi ngày sửa; dòng sửa sau ngày test tự về «cần test lại» (bộ lọc), dòng nối tới do `kiem` kéo theo. Đây là nội dung đối chiếu ở R51 ⑥.

**R51 (7 bước):** đồng ý, chỉ thêm: cuối mỗi bước hỏi 5 câu R53 cho thứ bước đó sinh ra; bước ⑦ Owner gật lô kèm duyệt cột lần đầu cho sổ mới. Phép đối chiếu Field (R51 ⑥ thứ hai) giữ, chính là bộ lọc «Hợp đồng thiếu Field» đã có.

**Lộ trình:** đồng ý B1 ánh xạ đủ sổ → B2 dựng sổ → B3 QT001. Thêm vào B1: Owner duyệt cột lần đầu theo lô. Sổ đã có thật (vd sổ DOT do `dot-dot-catalog` sinh) thì dùng lại, không dựng bản nháp trùng.

JEV `gen-dec-1792062363-iGhriHAVdWnmlgdLrl6s`: R49–R52 có yêu cầu 3 trạng thái = 0,17 (thiếu) · duyệt cột lần đầu = 0,43 (không chắc → coi là mờ) · có bộ câu hỏi cố định = 0,63 (gần đủ) · Field-check là trường hợp riêng = 0,27 (nên giữ, Claude đã bỏ ý gộp).

**Việc của GPT:** chốt R49–R53 (1 lượt); không viết PROMPT mới khi Owner chưa rà xong.

## V12.9 · Owner 18:14 «mọi đối tượng, không chỉ Field» · R53 viết lại thành LUẬT NHÀ · Claude 18:25

**Sửa:** bản 18:03 lấy Field làm ví dụ và đặt riêng «Sổ Field» làm sổ SSOT — hẹp. Nay R53 hỏi 5 câu cho **mọi đối tượng**, theo đúng thứ tự Owner: ① Nhà ở đâu · ② SSOT ở đâu · ③ Đã ghi danh chưa (chưa làm thì ghi «cần làm» trước) · ④ Ghi đúng chưa · ⑤ Trạng thái. Việc xong = mọi đối tượng nó tạo/sửa/dùng mới trả lời đủ 5 câu. Dòng «Sổ của SSOT = Sổ của các sổ + Sổ Field» ở V12.8 **bị thay**: SSOT của mỗi đối tượng là dòng của nó ở nhà của nó; Sổ của các sổ trả lời «nhà ở đâu» cho mọi loại.

**Gốc rễ lần trước thất bại:** thiết kế «cách làm» mà không thiết kế «nhà của mọi thứ» ⇒ cùng một thứ nằm nhiều chỗ, mỗi AI sửa một chỗ ⇒ lệch ⇒ làm lại. Chính TQT đang mắc — áp ngược Luật Nhà (sơ bộ, B1 đo chính xác):

| Loại đối tượng | Đang ở | ① Nhà | ② 1 gốc |
|---|---|---|---|
| Sổ (định nghĩa Master) | `master-of-master-v1.html` · `definition-master-registry-v1.js` · `field-origin-snapshot.json` | ⬜ chưa có Sổ của các sổ thật | 🔴 3 chỗ |
| Quy trình (MOW-TH) | `view.html` · COLLAB R48/R51 · `MOW-TH-006.md` | ⬜ | 🔴 nhiều chỗ |
| Field | `view.html` (250) · `field-origin-snapshot.json` · danh sách cột trong COLLAB/PROMPT | ⬜ | 🔴 nhiều chỗ |
| Màn UI | `UI-REVIEW-MOW001.json` · `ban-duyet.html` | ⬜ | 🟡 |
| DOT | `/opt/incomex/dot/bin` + sổ DOT (`dot-dot-catalog`) | 🟢 | 🟢 máy tự đối soát |
| Quyết định Owner | COLLAB 3.4 | 🟡 ML-DEF-027 chưa dựng | 🟢 |
| Luật hội đồng (R) | COLLAB §0 | ⬜ chưa có dòng nhà | 🟢 |
| Đề xuất (P/V) | `proposals/*.md` | ⬜ | 🟢 |
| PROMPT / RUN | `PROMPT.md` + COLLAB | ⬜ | 🟡 |
| Nợ / vấn đề (TQT-ISS) | COLLAB | 🟡 CAT-069 chưa dựng | 🟢 |

DOT là loại duy nhất đã đúng luật (có nhà, máy tự đối soát) — cũng là loại ít bị làm lại nhất. Ba dòng 🔴 là nơi đã gây làm lại; B1 gom mỗi loại về 1 gốc trước khi làm QT001. Các dòng ⬜ chỉ cần 1 dòng nhà «cần làm» kèm nơi đang ở — không phải chuyển hết vào Directus ngay.

JEV `gen-dec-1792063017-UfgJRxPGcsEH5W6GQbQO` + `gen-dec-1792063042-yNzTEYJoFCq7KLozV66X`: R53 mới phủ mọi đối tượng 0,96 · nhà 0,97 · SSOT 0,91 · ghi danh trước khi làm 0,89 · ghi đúng 0,95 · việc xong 0,96; chỗ hở duy nhất = áp ngược cho đồ đang có (0,92) → đã thêm «Áp ngược 1 lần (B1)».

**Việc của GPT (1 lượt):** ① chốt R49–R53 ② sửa README «Đọc nhanh» và dòng PROMPT chỉ tới R49–R53 ③ đưa 5 câu R53 thành câu đóng của khuôn 005/006/007 trong `view.html` (trỏ mã R53, không chép lại nội dung) ④ viết lại R51 bước ① thành «trả lời câu Nhà cho mọi thứ sẽ sinh ra» nếu cần. Không viết PROMPT mới khi Owner chưa rà xong.

## V13 · MOW-TH-007 v2 — ĐƯỜNG ĐỘC ĐẠO cho việc thiết kế G1 · Claude dự thảo 21:20 · **r2 22:05: đã gộp Hermes + Gemini V13.1 + GPT V13.2 — BẢN DUY NHẤT, thay r1** · chờ GPT xác nhận r2

**Owner 21:03:** liệt kê nhà vẫn thất bại nếu chỉ định hướng mục tiêu mà không chốt cách làm. Phải: 7 bước lớn như cũ → mỗi bước chia việc nhỏ có thứ tự → mỗi việc nhỏ có «thế nào là xong» → một con đường, kiểm xong là xong, làm khác không được, quên không được. Quy trình ở trên; mỗi công việc có hồ sơ trong sổ công việc. Đơn giản hơn 006, tận dụng tối đa Directus.

### 1. Phạm vi và khung
**Phạm vi:** 007 v2 chỉ dùng cho G1 — thiết kế UI · Field · Config trên vùng nháp. Trong G1 nó **thay** 006; 006 (71 bước) giữ nguyên cho G2/G3 triển khai thật. **Không đo 007 bằng 71 bước.** Chỉ mượn 7 tên mốc CP01–CP07 cho quen.

```
QUY TRÌNH (khuôn, ở trên)                    CÔNG VIỆC (thực thể, ở dưới)
Sổ quy trình: MOW-TH-007@v2         ──►     Sổ việc (CAT-227): CV-xxx = 1 quy trình QTxxx cần thiết kế
Sổ bước khuôn (ML-DEF-022):                   Hồ sơ của CV = 25 dòng, mỗi dòng = 1 việc nhỏ,
  25 thẻ (24 vị trí, 4.7 tách a/b)     ──►     trỏ về thẻ bằng mã (không chép), có trạng thái + bằng chứng
```
DOT `mo-ho-so CV-xxx` sinh đủ 25 dòng từ khuôn ⇒ không thể quên dòng nào. Sau khi chốt, 25 thẻ sống ở Sổ bước khuôn (nhà của chúng); bản trong P49 này chỉ là nháp để bàn.

### 2. Luật chạy (áp cho mọi việc nhỏ; thẻ không nhắc lại)
1. **Ghi dữ liệu ≠ đánh dấu xong.** DOT luôn ghi dữ liệu nháp và chỉ từ chối lỗi an toàn ⛔ (sai vùng · trùng mã · nối tới mã không có — Luật 7 PROMPT); chỗ còn thiếu vẫn lưu được. Nhưng một việc nhỏ chỉ được đánh dấu **đã kiểm** khi phép kiểm của nó đạt.
2. **Chấm cuốn chiếu, 1 lệnh:** AI soạn dữ liệu của nhiều việc nhỏ trong 1 commit rồi chạy `dot-master-apply ap <SHA> --cv CV-xxx`. DOT chấm lần lượt từ việc đầu tiên chưa đạt: đạt thì đóng dấu và chấm tiếp; gặp việc đầu tiên không đạt thì dừng, ghi kết quả (CAT-015) và báo đúng việc + con số thiếu. Không bao giờ chấm việc sau khi việc trước chưa đạt.
3. **Chỉ DOT hoặc quyết định Owner đánh dấu.** AI không tự tích «đã kiểm» hay «không áp dụng»; «không áp dụng» chỉ khi đúng điều kiện ghi trong thẻ.
4. **Lỗi:** sửa rồi chạy lại. Kết thúc lượt mà việc vẫn chưa đạt ⇒ bắt buộc 1 dòng nợ CAT-069 (CV · việc · chủ · chặn G1 hay không · quay về việc nào), báo 4 dòng, nhả lượt; không giữ máy chờ.
5. **Quay lại (Owner lắc hoặc nợ chỉ về việc k):** DOT chấm lại các việc máy từ k trở đi, việc không bị ảnh hưởng tự đạt lại ngay; 5.3 giữ kết quả nếu phần sửa không chạm đối tượng đã rà; 6.2 luôn hỏi lại Owner. Lịch sử giữ nguyên, không xoá.
6. **Hai loại nhà.** *Nhà vận hành* (sổ của cỗ máy, mục 6) phải được Owner duyệt cột trước khi dùng — làm ở B1; giữa chừng cần nhà vận hành mới ⇒ dừng, quay về 2.2. *Nhà thiết kế* (bảng nghiệp vụ QT cần, là sản phẩm của thiết kế) ghi «cần làm» ở 4.3, cột suy từ Hợp đồng, DOT dựng nháp để thử; Owner duyệt cột lần đầu ngay khi gật ở 6.2.
7. **Mọi phép kiểm ghi 3 thứ:** đếm gì · trên nhà nào · mẫu số (vd «số bước có màn / tổng bước QT = 100%»). Không có mẫu số thì «0 thiếu» vô nghĩa (R55).

### 3. 25 dòng việc (24 vị trí, 4.7 tách a/b)
🤖 AI/máy làm · 😊 Owner. Cột **Kiểm**: 🤖 DOT đếm · 👥 Reviewer khác hãng/Host · 😊 Owner. Dòng nào có 👥 là phần máy chỉ kiểm được hình thức.

| Mốc | # | Việc | Xong khi — đếm gì · trên nhà nào · mẫu số | Kiểm | Ghi ở |
|---|---|---|---|---|---|
| **CP01 Khai việc** | 1.1 | Tra Sổ việc theo khoá (QT + G1 + phiên khuôn): chưa có ⇒ tạo đúng 1; có ⇒ dùng lại | số CV cùng khoá trong CAT-227 = 1 | 🤖 | CAT-227 |
| | 1.2 | `mo-ho-so CV`: sinh hồ sơ từ 007@phiên (ghim hash) | số dòng hồ sơ của CV = số thẻ khuôn@phiên (25); mã checkpoint không trùng; chạy lại không thêm dòng | 🤖 | CAT-228 (B1 xác nhận) |
| | 1.3 | Điền thẻ việc 5 ô theo mẫu G1 | 5/5 ô (mục tiêu · sản phẩm · người nhận · tiêu chí · ngoài phạm vi) lấy từ mẫu G1 đã duyệt; tiêu chí = «5.1 đạt + Owner gật» | 🤖 | CAT-227 |
| **CP02 Chuẩn bị** | 2.1 | Nạp bước của QT từ Công thức | số bước QT trong Sổ quy trình / số bước của QT trong Sổ Công thức (ghim SHA) = 100%; mã bước không trùng | 🤖 | ML-MOW-TH-001 |
| | 2.2 | Liệt kê loại đối tượng CV sẽ sinh | số loại có nhà vận hành đã duyệt cột (dòng trong Sổ của các sổ có mã quyết định CAT-025) / số loại sẽ sinh = 100% | 🤖 | ML-DEF-012 |
| | 2.3 | DOT thử thật: `dot-master-apply thu` | biên nhận PASS cùng phiên DOT, trong lượt này (`--help` không tính) | 🤖 | CAT-229 |
| **CP03 Cổng** | 3.1 | Cổng vào làm (điều kiện vào khuôn) | 6/6 việc CP01–02 đã kiểm, cùng phiên khuôn, hash không lệch ⇒ máy mở CP04; không cần người | 🤖 | CAT-228 |
| **CP04 Làm: UI → Field → Config** | 4.1 | Nối bước QT với màn: 1 bước có thể nhiều màn, 1 màn dùng cho nhiều bước; bước không cần màn ghi «không UI» + lý do | số bước có ≥1 màn hoặc «không UI»+lý do / tổng bước QT = 100% | 🤖 + 👥 hợp nghề | ML-DEF-018 (mẫu ở ML-DEF-017) |
| | 4.2 | Màn giống màn có sẵn ⇒ ghi dùng lại | máy liệt kê cặp màn trùng cả 4 thuộc tính (bảng · mẫu · vai trò · bộ lọc); số cặp có «dùng lại từ» hoặc lý do khác / số cặp = 100% | 🤖 + 👥 | ML-DEF-018 |
| | 4.3 | Mỗi màn chọn bảng; bảng nghiệp vụ chưa có ⇒ ghi nhà thiết kế «cần làm» | số màn (trừ «không UI») có bảng / tổng màn = 100% | 🤖 | ML-DEF-018 · ML-DEF-012 |
| | 4.4 | Mỗi màn liệt kê thông tin ⇒ dòng Hợp đồng | (a) theo mẫu: danh sách ≥1 dòng xem; biểu mẫu/duyệt ≥1 dòng vào và ≥1 dòng ra · (b) QT có danh sách thông tin nguồn (vd `UI-REVIEW-MOW001.json`): số thông tin nguồn có dòng hợp đồng / tổng = 100% | 🤖 (a)(b) + 👥 đủ nghĩa | CAT-206 |
| | 4.5 | Gắn Field: dùng lại hoặc ghi Field mới | Field cần N = dùng lại A + mới đã ghi danh B + còn thiếu C; đạt khi C = 0; Field mới đủ 6 cột R36; tên cột không trùng trong 1 bảng | 🤖 + 👥 trùng nghĩa khác tên | ML-DEF-008 |
| | 4.6 | Ghi bảng + bắt buộc cho từng dòng hợp đồng | số dòng có bảng đúng hành động (xem ⇒ bảng đọc; nhập/tính/duyệt ⇒ bảng ghi) / tổng dòng = 100% | 🤖 | CAT-206 |
| | 4.7a | Đếm phát sinh (đã ghi ngay khi gặp; đây chỉ là đếm) | đối tượng CV tạo/sửa N = dùng lại A + mới ghi danh B + chưa ghi danh C; C = 0 (máy so dữ liệu commit với các nhà); 0 chép cơ học (ngoài khoá chỉ ghi mã, không lặp tên/kiểu Field) | 🤖 | các nhà tương ứng |
| | 4.7b | Rà ảnh hưởng: đối tượng đã test bị CV đổi nội dung (so hash với bản đã test) | mỗi đối tượng đổi có 1 dòng thay đổi (lý do + tác động); mọi đối tượng phụ thuộc theo quan hệ đã sang «cần test lại» | 🤖 | CAT-016 |
| | 4.8 | Commit → `dot-master-apply ap <SHA>`: dựng/cập nhật màn thật; màn có hành động ghi ⇒ 1 dòng thử, đọc lại | biên nhận ĐẠT đúng SHA; số màn có hành động ghi đã thử + đọc lại khớp / số màn đó = 100% | 🤖 | CAT-229 |
| **CP05 Kiểm** | 5.1 | `kiem --du QTxxx` | 0 thiếu theo các mẫu số 4.1–4.6 · 0 ghi khống · 0 nợ chặn G1 đang mở | 🤖 | CAT-015 |
| | 5.2 | Mở từng màn bằng tài khoản xem, chụp ảnh; test lại đối tượng «cần test lại» | số màn có ảnh (tệp + sha256, nối mã màn) / tổng màn = 100%; số «cần test lại» của CV = 0; ảnh đúng màn ⇒ 👥 | 🤖 + 👥 | CAT-239 |
| | 5.3 | Rà khác hãng phần máy không thấy (hợp nghề, trùng nghĩa, đủ nghĩa) | 1 phiếu APPROVE/REJECT. **Chỉ khi CV là khuôn (QT001)** — Owner đã chốt; CV khác DOT đặt «không áp dụng» | 👥 | CAT-025 |
| **CP06 Duyệt** | 6.1 | DOT gom gói duyệt | gói đủ 5 thứ: link bộ lọc theo QT · ảnh · số cần/đã/thiếu · nợ + **thay đổi thứ đã duyệt (4.7b) nêu riêng** · biên nhận | 🤖 | CAT-227 |
| | 6.2 | Owner gật/lắc theo lô (chat), kèm duyệt cột nhà thiết kế mới | 1 dòng quyết định: nguyên văn · CV · phiên/SHA · gật/lắc; AI ghi, DOT đọc lại | 😊 | CAT-025 |
| | 6.3 | Nhánh lắc | lắc: 1 dòng nợ có «quay về việc k», áp luật chạy 5; gật: DOT đặt «không áp dụng» | 🤖 | CAT-069 |
| **CP07 Đóng** | 7.1 | Kiểm liên tục | 25/25 dòng hồ sơ ở «đã kiểm» hoặc «không áp dụng» có căn cứ · 0 nợ chặn G1 đang mở | 🤖 | CAT-228 |
| | 7.2 | Nợ còn mở (không chặn G1) đủ thông tin | số nợ mở có đủ 4 ô (chủ · mức · điều kiện mở lại · đích bàn giao) / tổng nợ mở = 100% · Host xác nhận mọi vấn đề nêu trong lượt/chat đã vào sổ | 🤖 + 👥 | CAT-069 |
| | 7.3 | Đóng CV, báo 4 dòng | CV sang «G1 thiết kế đã duyệt» khi 7.1 đạt và có gật 6.2; không tự mở G2 | 🤖 | CAT-227 |

**Ví dụ xuyên suốt (số minh hoạ):** CV thiết kế QT001 → 1.2 mở hồ sơ 25 dòng → 4.1 QT001 có 3 bước, nối với 3 màn (Tìm thường · Tìm nâng cao · Xác nhận phù hợp) → 4.5 Field cần 10 = dùng lại 6 + mới 4 + thiếu 0 → 4.8 DOT dựng 3 màn, thử màn có hành động ghi → 5.1 0 thiếu → 5.2 3 ảnh → 5.3 Claude + GPT ký (vì là khuôn) → 6.2 Owner gật, kèm duyệt cột bảng nghiệp vụ mới → 7.3 đóng. QT002 trở đi: y hệt, 5.3 «không áp dụng»; nếu sửa thứ đã duyệt thì 6.1 nêu riêng cho Owner thấy.

### 4. Khoá cứng hay lời dặn (AGENTS A10-R2 — nói thật)
- **Dự kiến khoá bằng máy:** thứ tự chấm; đủ dòng hồ sơ; mọi phép đếm có mẫu số; chỉ ghi qua DOT; «đã kiểm» chỉ DOT đặt. Chỉ gọi là **khoá** khi B2 chạy ca âm tính và đều bị chặn: mở hồ sơ 2 lần · chấm vượt thứ tự · thiếu nhà · ghi khống · ghi ngoài vùng. Lỗ SSH R47 còn mở.
- **Còn là lời dặn** (máy kiểm hình, không kiểm chất — các dòng có 👥): màn hợp nghề, Field trùng nghĩa khác tên, đủ nghĩa nghiệp vụ, ảnh đúng màn, vấn đề trong chat đã vào sổ ⇒ bắt ở 5.3 (khuôn), 7.2 (Host) và 6.2 (Owner).

### 5. Directus làm thay (có sẵn, không viết mã)
| Cần | Directus có sẵn |
|---|---|
| Thẻ việc nhỏ hiện ngay trong hồ sơ, không chép | quan hệ M2O hồ sơ → bước khuôn |
| Checklist của 1 việc ngay trong trang CV | danh sách O2M |
| «Việc đang mở», 3 bộ lọc thiếu, «cần test lại» | bookmark |
| Màu trạng thái nhìn là biết | dropdown có màu |
| Lịch sử kỹ thuật ai sửa gì lúc nào | revisions/activity (thay đổi có nghĩa nghiệp vụ vẫn ghi CAT-016 ở 4.7b) |
| Thẻ 3 ô trên mỗi việc: tiến độ x/25 · số đối tượng theo trạng thái · Claude/GPT/Owner (R34) | cột do DOT tính mỗi lần chạy, Directus hiện màu |
| Ngày tạo/sửa, người sửa | trường hệ thống tự đóng dấu |
| Đổi tên 1 chỗ, mọi nơi hiện theo | display template qua quan hệ |
| Thanh tiến độ việc / lô | dashboard đếm theo trạng thái |
| Chặn dòng sai khuôn | luật hợp lệ + bắt buộc của cột (DOT kiểm trước; Directus chặn lớp hai — đo ở B2) |

Không dùng Flow: mọi tự động có ghi đều đi qua DOT để còn biên nhận.

### 6. Nhà vận hành (đề xuất; con số chính thức là kết quả B1 đo)
**Luật mã (GPT V13.2):** chỉ gộp khi cùng loại đối tượng + cùng mức hạt + cùng khoá + cùng SSOT; khác nghĩa thì **nối quan hệ**, muốn xem chung thì dùng màn tổng hợp Directus. Mỗi nhà có cột `loai_luu_tru` ∈ Directus nháp · Directus có sẵn · tệp GitHub (Gemini). Đồ hội đồng (luật R, đề xuất P/V, PROMPT) chỉ 1 dòng «tệp GitHub», không dựng bảng.

| # | Nhà | Mã | Nối với (không phải bí danh) | Dùng ở |
|---|---|---|---|---|
| 1 | Sổ của các sổ | ML-DEF-012 | ML-DEF-011 Master List | 2.2 · 4.3 |
| 2 | Công thức | ML-DEF-021 | — | 2.1 |
| 3 | Quy trình | ML-MOW-TH-001 | ML-DEF-004 MOW | 2.1 |
| 4 | Bước khuôn (25 thẻ) | ML-DEF-022 | ML-DEF-005 MOT | 1.2 |
| 5 | Việc | CAT-227 | — | 1.1 · 1.3 · 6.1 · 7.3 |
| 6 | Hồ sơ checkpoint | CAT-228 (ứng viên, B1 kiểm schema) | CAT-227 | 1.2 · 3.1 · 7.1 |
| 7 | Mẫu màn (UI cha) | ML-DEF-017 | — | 4.1 |
| 8 | Màn (UI con) | ML-DEF-018 | ML-DEF-017 | 4.1–4.3 |
| 9 | Field | ML-DEF-008 | — | 4.5 |
| 10 | Hợp đồng | CAT-206 | — | 4.4 · 4.6 |
| 11 | Nợ | CAT-069 | — | luật 4 · 6.3 · 7.2 |
| 12 | Quyết định | CAT-025 | ML-DEF-027 (định nghĩa) | 2.2 · 5.3 · 6.2 |
| 13 | Thay đổi | CAT-016 | — | 4.7b |
| 14 | Kết quả kiểm | CAT-015 | ML-DEF-025 | 5.1 |
| 15 | Lượt thử | CAT-229 | — | 2.3 · 4.8 |
| 16 | Bằng chứng | CAT-239 | ML-DEF-026 | 5.2 |
| 17 | DOT (dùng lại, đang chạy) | ML-DEF-024 | CAT-006 (B1 kiểm) | 2.3 · 4.8 |

**17 nhà, 1 dùng lại.** Không gộp 3 sổ kiểm 015/229/239 (khác bản chất; JEV 0,99). B1 đo từng nhà (đã có ở đâu, loại lưu trữ) → Owner gật **bảng mã + cột 1 lần theo lô**. DOT thêm: `mo-ho-so` · `kiem CV` · `ap --cv` (chấm cuốn chiếu).

**B1/B2 tự nó** là việc dựng nhà, không phải thiết kế QT ⇒ không chạy 007; chạy theo PROMPT như cũ, nhưng mọi thứ nó tạo phải trả lời Luật Nhà và được ghi bù làm CV đầu tiên ngay khi Sổ việc dựng xong.

### 7. Bài học 006 đã mang sang G1 (006 giữ nguyên cho G2/G3)
| Bài học 006 | 007 v2 |
|---|---|
| Mở hồ sơ trước khi làm, tra trùng (CP01.04) | 1.1–1.2 |
| Thẻ việc 5 ô | 1.3 (mẫu G1 duyệt 1 lần) |
| Ghi an toàn: kiểm → ghi → biên nhận → đọc lại (CP04.06) | 4.8 + 5.2 |
| Rà độc lập khác hãng | 5.3 (khuôn QT001, theo Owner) |
| Quyết định có nguyên văn | 6.2 |
| Kiểm liên tục CP01–07, bài học, khép RUN báo 4 dòng | 7.1–7.3 |
| Lỗi → sổ nợ → quay lại bước | luật chạy 4–5 |
| Thẻ bước 9 câu | luật chạy chung + thẻ đủ ô theo R55 |
| **Bỏ cho G1** (giữ ở 006 cho G2): phiên/hash ký tay (biên nhận DOT thay) · xác thực quyền người làm (khoá GSM của DOT thay) · bộ ca đúng/sai/rỗng · giao điểm MOT · payload giao–nhận · ACK bên nhận có thẩm quyền | — |

JEV `gen-dec-1792073125-qGqFp2ll6auPaVk8XD2b`: Owner gật qua chat, AI ghi = 1,00 · rà khác hãng chỉ ở khuôn = 1,00 · giữ 7 mốc CP01–07 = 0,61 (Owner yêu cầu rõ ⇒ giữ).

**Đã gộp ở r2:** Hermes — phạm vi 007/006, cột Kiểm, mẫu số, cổng 3.1, đếm N = A + B + C, rà ảnh hưởng 4.7b, 7.2 đo được · Gemini V13.1 — chấm cuốn chiếu, `loai_luu_tru`, thẻ 3 ô, công thức 1.3/2.1/4.2/4.4/4.5/6.2 · GPT V13.2 — bước↔màn nhiều-nhiều, đối soát 4.4/4.5, quay lại giữ lịch sử, 7.1 nợ chặn G1, 7.3 trạng thái việc, luật mã, so hash thay ngày sửa. **Không nhận:** gộp sổ/bí danh khác nghĩa (Gemini); 5.3 cho mọi CV (GPT) — trái quyết định Owner, rủi ro sửa thứ đã duyệt được nêu riêng ở 6.1 cho Owner thấy. **Lỗi khung r1 do Claude:** đoạn kết r1 mời đo «so với 006» và tiêu đề «So với 006» kéo người đọc sang thước 71 bước (Hermes chỉ ra) — đã sửa, thêm R55. JEV `gen-dec-1792075431-EER4qdnjx4lYlxQ1oMrX`: giữ 3 sổ kiểm riêng 0,99 · bản đầu luật 5.3/6.3 không ổn 0,09 → đã viết lại thành luật chạy 5 và dòng 5.3.

**Việc tiếp:** GPT xác nhận r2 1 lượt (chỉ báo dòng sai, không mở lại khung) → Owner gật khuôn → viết PROMPT B1+B2 (B1 đo 17 nhà · Owner gật bảng mã + cột · B2 dựng) → B3 chạy 007 cho QT001.

## V13.1 · Phản biện độc lập của Gemini (song song với GPT) · 15/10/2026 · ĐỒNG THUẬN KHUNG V13, CHỐT 3 ĐIỂM ĐỂ MÁY CHẠY TỰ ĐỘNG 100%

Nguồn đọc: `COLLAB.md` (R49–R54, P63–P65) · `P49` (V12.8–V13) · `MOW-TH-006.md` (71 bước) · `evidence/ui-inputs/definition-master-registry-v1.js` (29 ML-DEF) · `evidence/field-origin-snapshot.json` (18 CAT) · `ui/master-of-master-v1.html` (86 mục) tại `HEAD = 5d6b2dc5ca2c0e139050083e4285de9acc723405`. Thực hiện theo chỉ đạo trực tiếp của Owner (21:14 +07: *«Bạn có ý kiến song song cùng với GPT nhé. Mỗi bạn có ý kiến riêng trên repo. Bạn tiếp tục cho ý kiến vào thẳng task tiếp theo ý kiến của claude. 1. Chỗ rõ mục tiêu. 2. Cần chốt rõ từng bước một phải làm gì gọi là quy trình và chốt thế nào là hoàn thành từng bước để bất cứ AI nào đọc cũng có thể làm được.»*).

### A. Về Mục tiêu & Kiến trúc 2 tầng (Yêu cầu 1 của Owner)

1. **Khung 2 tầng của V13 + Luật Nhà (R53) đã giải quyết đúng gốc rễ:**
   - **Tầng trên (Quy trình = Khuôn cố định):** `MOW-TH-007@v2` nằm trong Sổ quy trình, gồm 7 mốc `CP01–CP07` và 24 thẻ việc nhỏ nằm trong `Sổ bước khuôn (ML-DEF-022)`.
   - **Tầng dưới (Công việc = Thực thể chạy):** Mỗi quy trình cần thiết kế (như `QT001`) là 1 dòng `CV-xxx` trong `Sổ việc (CAT-227)`, kéo theo 24 dòng checklist trong `Sổ hồ sơ bước (CAT-228)` do lệnh `dot-master-apply mo-ho-so CV-xxx` tự sinh.
   - **Luật Nhà (R53) khóa đầu ra:** Mọi đối tượng sinh ra/sửa trong lúc chạy 24 việc nhỏ đều phải có dòng ghi danh tại đúng Nhà của nó theo 3 trạng thái `cần làm → đã làm xong → đã test xong`.
2. **Hai chốt làm rõ mục tiêu để AI không trượt phạm vi ở B1/B2:**
   - **Chặn bẫy đệ quy «dọn văn phòng» ở B1:** Trong `Sổ của các sổ (ML-DEF-011)`, phân loại rõ cột `loai_luu_tru ∈ DIRECTUS_NHAP | DIRECTUS_CO_SAN | GITHUB_FILE_SSOT`. Ở B2 chỉ dựng bảng `tqt_draft_*` cho **9 Sổ vận hành quy trình thiết kế** (mục D bên dưới). Đối với đồ điều hành Hội đồng trên GitHub (`Luật R`, `Đề xuất P/V`, `PROMPT.md`), chỉ ghi **1 dòng định danh loại** với `loai_luu_tru = GITHUB_FILE_SSOT` (`dung_bang = false`), **tuyệt đối không biến lịch sử thảo luận `COLLAB.md`/`P49.md` thành bảng Directus ở G1**.
   - **Khôi phục «Thẻ 3 ô nhìn nhanh» trên dòng Công việc (`CAT-227`) theo R34 của Owner:** Trong `V13` chưa nhắc lại 3 cột tổng hợp tự động trên mỗi dòng `CV-xxx` của `CAT-227`: ① `tien_do_ho_so` (`x/24` việc nhỏ đã kiểm) · ② `doi_tuong_phat_sinh` (tổng số Màn/Field/Bảng/Nợ của CV theo `cần làm / đã làm / đã test`) · ③ `trang_thai_duyet` (`GPT · Claude · Owner`). Cần giữ 3 cột này ở `CAT-227` để Owner mở Sổ việc ra là nhìn thấy ngay bức tranh tổng thể.

### B. Điểm ① — Rà 24 việc nhỏ so với 71 bước của `006`: Thiếu gì, Thừa gì, Có nghịch lý thứ tự không?

1. **Phát hiện nghịch lý thứ tự (Deadlock) ở `CP04` (`4.1 → 4.8`) và cách gỡ bằng 1 quy tắc thực thi:**
   - *Vấn đề:* Luật chạy 1 & 2 quy định *«việc `n` chỉ mở khi `n-1` đã được DOT đánh dấu đã kiểm»*. Nhưng từ `4.1` đến `4.7`, AI đang khai dữ liệu trên tệp `master/*.json` (GitHub), đến `4.8` mới chạy `dot-master-apply ap <SHA>`. Nếu hiểu máy móc rằng mỗi việc nhỏ `4.1`, `4.2`... phải chạy DOT riêng mới được làm việc kế tiếp, AI sẽ phải commit + chạy DOT **8 lần liên tiếp** chỉ cho `CP04`, hoặc bị kẹt tại `4.1` vì chưa chạy `4.8`!
   - *Giải pháp (Chấm cuốn chiếu — Sequential Gate trong 1 lệnh DOT):* AI được phép soạn đầy đủ dữ liệu JSON của `4.1 → 4.7` trong **1 commit** rồi gọi `dot-master-apply ap <SHA> --cv CV-xxx`. Khi chạy, DOT **kiểm tra tuần tự từng việc nhỏ từ `1.1 → 4.8`**: việc `k` đạt phép kiểm thì DOT tự đóng dấu `đã kiểm` cho `k` và xét tiếp `k+1` ngay trong cùng lần chạy; hễ gặp việc `m` đầu tiên **không đạt**, DOT dừng ngay tại `m`, tự ghi 1 dòng vào `Sổ nợ (CAT-069)` gắn với `(CV-xxx, việc m)` và giữ các việc từ `m` trở đi ở `cần làm`. Vừa khóa cứng thứ tự 100%, vừa chạy 1 mạch.
2. **Thiếu 1 nghĩa vụ bắt buộc của `006` (`CP04.15`) & `R52` (Kiểm tra tác động ngược khi sửa đối tượng đã có):**
   - Trong 24 việc hiện tại mới xét tạo mới/dùng lại, **chưa có bước xử lý khi `CV-xxx` sửa một `Field`, `Màn hình` hoặc `Bảng` đã ở trạng thái `đã test xong` của việc trước**.
   - *Bổ sung thẳng vào `4.7` & `5.1` (không cần tăng số bước lên 25):* Khi `dot-master-apply ap` phát hiện một bản ghi đã `đã test xong` bị thay đổi nội dung, DOT tự động đổi bản ghi đó và mọi Màn hình/CV đang nối FK tới nó về trạng thái `cần test lại`. Phép kiểm `5.1` (`kiem --du QTxxx`) chỉ PASS khi `số đối tượng liên quan ở trạng thái cần_test_lại = 0`.
3. **Các bước đã rút gọn từ 71 xuống 24 là hoàn toàn hợp lý:**
   - Giữ nguyên 24 việc nhỏ để cấu trúc 7 mốc `CP01–CP07` rõ ràng, tường minh trên giao diện Directus. Riêng khi chạy máy: lệnh `mo-ho-so` tự thực hiện luôn cặp `(1.1 + 1.2)`, và lệnh `ap` sau khi có quyết định Owner ở `6.2` tự thực hiện luôn `6.3 + 7.1 + 7.2 + 7.3` nếu `APPROVED`.

### C. Điểm ② — Chốt công thức máy đo cho từng phép kiểm «Xong khi» (Yêu cầu 2 của Owner)

Các việc `1.1, 1.2, 2.3, 3.1, 4.1, 4.3, 4.6, 5.3, 6.1, 7.1, 7.3` trong V13 đã có phép đếm rõ. Riêng **9 việc nhỏ dưới đây** trong dự thảo V13 đang viết bằng lời chung chung hoặc có thể gây bắt nhầm, cần chốt thành **công thức kiểm định lượng trong `dot-master-apply`** để AI nào đọc cũng làm được ngay:

| Việc | Dự thảo V13 hiện ghi | Chỗ còn mờ / rủi ro | Công thức máy kiểm chính xác (DOT tự đo = PASS) |
|---|---|---|---|
| **1.3** | 5 ô không trống; mẫu G1 duyệt 1 lần cho khuôn | Chưa chỉ rõ 5 cột nào trong `CAT-227` | Dòng `CV-xxx` trong `CAT-227` có đủ 5 cột `muc_tieu, san_pham, nguoi_nhan, tieu_chi, ngoai_pham_vi != NULL/rỗng` VÀ `khuon_quy_trinh = 'MOW-TH-007@v2'`. |
| **2.1** | QT có ≥1 bước; ghi mã nguồn + commit | Chỉ kiểm `≥ 1` thì quy trình có 3 bước nhưng AI mới nạp 1 bước vẫn PASS | `COUNT(bước của QT trong Sổ bước khuôn) == COUNT(bước/MOT dẫn xuất của QT trong Công thức gốc)` VÀ `source_commit_sha` là SHA 40 ký tự hợp lệ trên `main`. |
| **2.2** | 0 loại vô gia cư; nhà sẽ dùng đã duyệt cột | Máy chưa biết thế nào là «nhà đã duyệt cột» | Mọi mã Nhà mà CV sử dụng đều có dòng trong `Sổ của các sổ (ML-DEF-011)` với `trang_thai_duyet_cot = 'DA_DUYET'` và `quyet_dinh_ref` trỏ tới 1 dòng thật của Owner trong `CAT-025`. |
| **4.2** | 0 cặp `(bảng, mẫu)` trùng mà không ghi dùng lại | 1 bảng có thể có 2 màn `danh_sach` khác bộ lọc hoặc khác vai trò (hợp lệ); chặn theo `(bảng, mẫu)` sẽ báo lỗi giả | `COUNT(cặp màn hình trùng cả 4 thuộc tính [bang, mau, vai_tro, bo_loc] mà dung_lai_tu IS NULL và ly_do IS NULL) == 0`. |
| **4.4** | 0 màn (trừ không UI) có 0 dòng Hợp đồng | Màn biểu mẫu chỉ nhập đối phó 1 dòng cũng qua | Với mỗi màn `mau != 'khong_ui'` và `dung_lai_tu IS NULL`: nếu `danh_sach` phải có `≥ 1` dòng `hanh_dong = 'xem'`; nếu `bieu_mau / duyet` phải có `≥ 1` dòng vào/xem (`xem/nhap`) **VÀ** `≥ 1` dòng ra/tác động (`nhap/duyet/tinh`). |
| **4.5** | 0 dòng thiếu Field · 0 Field trùng tên | Cần kiểm đủ cột bắt buộc R36 của Field mới | `COUNT(dòng Hợp đồng của CV có field IS NULL) == 0` VÀ mọi `field` được tham chiếu đều tồn tại trong `ML-DEF-008` với đủ 6 cột `cot, ten (có «?»), kieu, mo_ta, viec_sinh_ra, vong_doi`, `cot` không trùng trong cùng 1 bảng đích. |
| **4.7** | Luật Nhà: 0 vô gia cư · 0 thiếu ghi danh · 0 chép trùng | Chưa có công thức phát hiện «chép trùng» và «sửa sau test» | (1) Mọi FK trong CV chỉ lưu mã `ma`, không lặp lại `kieu/ten` của Field ở bảng Hợp đồng; (2) Mọi đối tượng cũ bị sửa nội dung trong commit này đã được DOT chuyển trạng thái về `cần test lại` (cùng các màn hình nối tới nó). |
| **4.8 & 5.2** | 4.8: biên nhận ĐẠT; đối tượng sang «đã làm» · 5.2: mỗi màn 1 ảnh + dòng thử khớp ⇒ «đã test» | Cần tách rõ việc máy làm ở `4.8` và `5.2` để không bắt người chụp tay từng màn nếu tự động được | **4.8:** DOT tạo/cập nhật bảng nháp + `directus_presets` / `directus_fields`, POST 1 dòng thử từ `master/thu/` và GET đọc lại khớp 100% ⇒ DOT ghi dòng `LUOT_THU` vào `CAT-015` và nâng đối tượng sang `đã làm xong`. **5.2:** Với mỗi màn của CV, kiểm tra đăng nhập bằng token `xem-nhap` đọc API màn hình trả `HTTP 200` + có tệp ảnh chụp màn hình (`anh_uri`, `sha256`) ghi vào `CAT-015` (`BANG_CHUNG_UI`) ⇒ DOT nâng đối tượng sang `đã test xong`. |
| **6.2 & 6.3** | 6.2: AI ghi nguyên văn vào sổ quyết định · 6.3: lắc ⇒ ghi nợ + quay lại việc nhỏ | Làm sao DOT tự đóng/mở lại hồ sơ từ quyết định Owner? | AI ghi nguyên văn lời Owner vào `master/cat_025.json` (`quyet_dinh ∈ APPROVED | REJECTED`, `cv_ref`, `quote_nguyen_van`, `quay_lai_buoc`) rồi chạy `dot-master-apply ap <SHA> --cv CV-xxx`. Nếu `APPROVED`: DOT đặt `6.2 = đã kiểm`, `6.3 = không áp dụng`. Nếu `REJECTED`: DOT đặt `6.2 = đã kiểm`, buộc có dòng nợ `CAT-069` nối `quay_lai_buoc` (`6.3 = đã kiểm`), và **reset trạng thái các bước từ `quay_lai_buoc` đến `6.3` về `cần làm`**. |

### D. Điểm ③ — Chốt mã chính thức cho các Nhà đang trùng (`CAT-*` vs `ML-DEF-*`) và gộp bảng

**Nguyên tắc 1 gốc (không đẻ mã mới):**
1. Các Sổ định nghĩa thành phần kiến trúc Cỗ máy đã gắn cứng với Công thức `CT-001..007` trong `definition-master-registry-v1.js` ⇒ giữ mã **`ML-DEF-xxx`**.
2. Các Sổ điều hành công việc, hồ sơ, hợp đồng, kiểm thử, quyết định, sổ nợ của quy trình đã có schema chuẩn trong `MOW-TH-006.md` & `field-origin-snapshot.json` ⇒ giữ mã **`CAT-xxx` (bỏ dấu `*` và `?` ở đuôi theo chuẩn P60)**. Mã còn lại ghi vào cột `bi_danh` trong `Sổ của các sổ`.
3. **Gộp 3 sổ kiểm thử (`CAT-015`, `CAT-229`, `CAT-239`) thành 1 Sổ duy nhất `CAT-015`** (thêm cột `loai_ban_ghi ∈ LUOT_THU | KIEM_DU | BANG_CHUNG_UI`) để giảm 2 bảng log rời rạc ở G1.

**Bảng chốt 10 Nhà (Sổ) dùng cho `MOW-TH-007 v2` (9 Collection Directus nháp + 1 Sổ dùng lại):**

| # | Tên Nhà (Sổ) | Mã chính thức (PK) | Bí danh (`bi_danh`) | Dùng ở bước nào trong 24 việc? | Cách dựng ở B2 |
|---|---|---|---|---|---|
| 1 | **Sổ của các sổ** | **`ML-DEF-011`** | `ML-DEF-012` | `2.2`, `4.3`, `7.1` (chứa 1 dòng tự mô tả chính nó + danh sách mọi Nhà & cột đã duyệt) | `tqt_draft_ml_def_011` |
| 2 | **Sổ quy trình** | **`ML-MOW-TH-001`** | `ML-DEF-004`, `CAT-003` | `2.1` (chứa `MOW-TH-001..007` và 35 quy trình `MOW`, phân biệt bằng cột `loai_quy_trinh`) | `tqt_draft_ml_mow_th_001` |
| 3 | **Sổ bước khuôn** | **`ML-DEF-022`** | `CAT-004`, `ML-DEF-005` | `1.2`, `2.1`, `4.1` (chứa 24 thẻ việc nhỏ của `007@v2` và các bước con/MOT của từng QT) | `tqt_draft_ml_def_022` |
| 4 | **Sổ việc** (1 dòng/CV) | **`CAT-227`** | `DEF00.1`, `CAT-227*` | `1.1`, `1.3`, `6.1`, `7.3` (có 5 ô đầu vào + 3 ô chỉ số tổng hợp tự động theo R34) | `tqt_draft_cat_227` |
| 5 | **Sổ hồ sơ bước** (24 dòng/CV) | **`CAT-228`** | `CAT-228*` | `1.2`, `3.1`, `7.1` (`mo-ho-so` tự sinh 24 dòng nối M2O về `CAT-227` và `ML-DEF-022`) | `tqt_draft_cat_228` |
| 6 | **Sổ màn hình UI** | **`ML-DEF-018`** | `ML-DEF-017`, `CAT-UI` | `4.1`, `4.2`, `4.3` (màn hình, mẫu, bảng đích, vai trò, dùng lại từ màn nào) | `tqt_draft_ml_def_018` |
| 7 | **Sổ hợp đồng thông tin** | **`CAT-206`** | `CAT-206*` | `4.4`, `4.5`, `4.6` (nối `Màn hình` × `Field` × `Hành động` × `Bắt buộc` × `Bảng đọc/ghi`) | `tqt_draft_cat_206` |
| 8 | **Sổ Field** | **`ML-DEF-008`** | `OBJ-FIELD` | `4.5` (250 Field sẵn có + Field mới phát sinh theo R36) | `tqt_draft_ml_def_008` |
| 9 | **Sổ nợ / vấn đề** | **`CAT-069`** | `CAT-069?`, `TQT-ISS` | Luật chạy 3, `4.7`, `6.3`, `7.2` (mọi lỗi kiểm không qua, nợ thiết kế, nối `CV` + bước nhỏ) | `tqt_draft_cat_069` |
| 10 | **Sổ quyết định & duyệt** | **`CAT-025`** | `ML-DEF-027` | `2.2` (Owner duyệt cột), `5.3` (GPT/Claude rà khuôn QT001), `6.2` (Owner gật/lắc lô) | `tqt_draft_cat_025` |
| 11 | **Sổ kết quả kiểm & bằng chứng** *(gộp 3 làm 1)* | **`CAT-015`** | `CAT-229*`, `CAT-239*`, `ML-DEF-025/026` | `2.3`, `4.8` (`LUOT_THU`), `5.1` (`KIEM_DU`), `5.2` (`BANG_CHUNG_UI`) | `tqt_draft_cat_015` |
| 12 | **Sổ DOT** *(dùng lại)* | **`ML-DEF-024`** | `CAT-006` | Quản lý `dot-master-apply` và các lệnh DOT thông qua `00-SO-DOT.tsv` sẵn có | **Dùng lại**, không dựng trùng |

### E. Kết luận chốt của Gemini

- **GEMINI_REVIEW = ACCEPT_WITH_PRECISION_RULES** (Đồng thuận hoàn toàn cấu trúc 7 mốc · 24 việc nhỏ · 3 luật chạy của Claude tại `V13`; đề nghị gộp thẳng 3 điểm làm rõ ở Mục B, C, D trên vào bản chốt `MOW-TH-007 v2` để chuyển sang `B1/B2` ngay trong 1 vòng).


## V13.2 · GPT Chat phản biện độc lập V13/R54 + đối chiếu Gemini V13.1 · 15/10/2026 · ACCEPT KHUNG, REQUEST_CHANGES HẸP

**Nguồn đã đọc thật:** 24 việc V13; 71 bước/7 mốc MOW-TH-006; registry ML-DEF (đặc biệt 004/005/008/011/012/017/018/022/024/025/026/027), snapshot 18 CAT (015/016/025/069/206/227/228/229/239), AGENTS. Chưa có runtime DOT/Directus nào được thực thi trong lượt phản biện; không tự báo chốt máy PASS.

### 1. KẾT LUẬN CHO OWNER

**Đồng ý 7 mốc CP01–CP07, giữ đủ 24 vị trí công việc.** Mỗi CV có 1 hồ sơ; 24 checkpoint trỏ về 24 thẻ bước khuôn, có thứ tự/xong khi/nơi ghi; lấy bài học từ 006 nhưng **không gọi 006/71 bước cho G1**. Luật Nhà R53 hỏi cho mọi đối tượng, kết quả ghi/đọc lại đúng Master, ứng dụng Directus tối đa.

**Chưa đồng ý chốt nguyên văn:** 24 dòng hiện còn phép kiểm hình thức dễ báo đạt giả, chưa có nhánh lắc/quay lại khép kín; riêng **4.1, 4.4, 4.5, 6.3, 7.1–7.2** phải sửa. Gemini V13.1 đã phát hiện vấn đề cuốn chiếu và bổ sung nhiều câu kiểm hữu ích; **nhưng bảng gộp mã/sổ của Gemini có các phép gộp sai nghĩa**, không thể lấy làm chuẩn mà không đối chiếu nguồn. Không cần thêm mốc/thẻ, chỉ sửa ngay 24 thẻ.

### 2. RÀ ĐỦ 24 VIỆC: CÁCH LÀM + CÁCH KIỂM CHỐT

Ký hiệu **M**: máy kiểm được cấu trúc/đếm *nếu có DOT và nguồn rõ*; **N**: kiểm nghiệp vụ còn cần AI/Reviewer; **O**: Owner quyết; **T**: cần thử thực tế tại B2, chưa được tự nhận đã cưỡng chế.

| # | Kết luận | Chỉnh tối thiểu để đủ “AI nào đọc cũng làm” |
|---|---|---|
| **1.1** | M · sửa | Tra khóa (QT + G1 + phiên): không có CV thì **tạo đúng 1**, có rồi dùng lại, >1 báo trùng; không đòi đúng 1 khi chưa tạo. |
| **1.2** | M · giữ | Sinh 24 dòng hồ sơ có mã checkpoint duy nhất, theo **007@phiên/hash ghim**, tự chạy lại không nhân dòng/xóa bằng chứng cũ. |
| **1.3** | M+N · sửa | Năm ô có nguồn mục tiêu/phạm vi Owner, người nhận và tiêu chí **kiểm được**, không chỉ “không rỗng”. |
| **2.1** | M · sửa | Bước của QT đếm **đủ theo Công thức/nguồn đã ghim**, mã duy nhất, quan hệ chính xác; “>=1 bước” chưa đủ. |
| **2.2** | M+O · sửa | Mỗi loại sắp sinh có **nhà/SSOT/đích ghi**. Cột sổ mới chỉ xin Owner duyệt **theo một lô lần đầu/phiên đổi**, sổ cũ dùng lại; phát sinh loại mới sau CP02 phải quay đúng 2.2, không tự lách. |
| **2.3** | T · giữ | DOT thử thật có biên nhận đúng phiên/Guard/phạm vi/quyền; tồn tại lệnh hoặc --help không là PASS. |
| **3.1** | M · giữ | Sáu checkpoint 01/02 đều có biên nhận hợp lệ và không drift, máy mở CP04; không thêm lượt gật của Owner. |
| **4.1** | M+N · **sửa bắt buộc** | Quan hệ **bước↔UI 0..N**: bước không cần UI ghi NO_UI+lý do, một UI dùng lại cho nhiều bước; xong khi mọi **hành động cần UI** đã ánh xạ, không ép 1 bước=1 màn. |
| **4.2** | M+N · sửa | Dùng lại theo hành động, vai trò, nguồn/bảng, bộ Field, filter/ngữ cảnh; không chặn chỉ vì cùng (bảng,mẫu). Máy báo ứng viên trùng, người rà ý nghĩa. |
| **4.3** | M · giữ | Mã Master đọc/ghi đúng; chưa có bảng vật lý nháp thì đăng ký “cần dựng”, **không ép PG production đã tồn tại**. |
| **4.4** | M+N · **sửa bắt buộc** | Từ yêu cầu/câu hỏi chuẩn lập tập **nghĩa vụ thông tin dự kiến** của từng màn/hành động. Đối soát số cần = đã có Hợp đồng + còn thiếu; **>=1 dòng/màn không chứng minh đủ**. |
| **4.5** | M+N · sửa | Số Field cần = Field cũ dùng lại + Field mới đã đăng ký + còn thiếu; kiểm mã/miền/kiểu và định nghĩa; **trùng tên không tất yếu trùng nghĩa**, trùng nghĩa khác tên cần Reviewer. |
| **4.6** | M+N · giữ có sửa | Theo hành động xác định bảng đọc (xem) và ghi (nhập/tính/duyệt), ràng buộc vai trò/bắt buộc/kiểu/quan hệ; chỗ trống được lưu NHÁP, chỉ chặn độ phủ khi nghiệm thu. |
| **4.7** | M+N · sửa | **Ghi Master ngay lúc phát hiện**, không chờ 4.7 rồi mới ghi nợ/Field/UI/thay đổi; 4.7 tổng kiểm đối tượng phát sinh = dùng lại + mới ghi + chưa ghi; so nơi ảnh hưởng. |
| **4.8** | T · giữ | DOT áp đúng commit SHA, dry-run chỉ NHÁP, ghi/đọc lại ca thử **cho đúng hành động cần thử**, có receipt/rollback, không coi 1 POST bất kỳ là đã thử đủ màn. |
| **5.1** | M+N · sửa | Kiểm đủ **theo tập nghĩa vụ đã xác định**, sổ/thực thể/quan hệ/nợ chặn/nguồn/ảnh hưởng; máy không tự biết nghĩa vụ nghiệp vụ chưa khai hoặc 2 Field trùng nghĩa. |
| **5.2** | T+N · giữ | Mở màn thật bằng tài khoản xem, có ảnh thật + trường hợp đọc lại đúng; chỉ HTTP 200 của API **không chứng minh UI đã hiển thị**; lỗi UI thì UNVERIFIED. |
| **5.3** | N · sửa | Rà khác hãng lần đầu khuôn **và khi thay đổi ý nghĩa/kiểu/quan hệ hoặc rủi ro mới**, không mặc định bỏ review bắt buộc theo AGENTS chỉ vì CV khác QT001. |
| **6.1** | M · giữ | Gói Owner rút tự động từ cùng CV/phiên: link UI, ảnh, số cần/đã/thiếu, nợ/ảnh hưởng, biên nhận; không sinh thêm bộ giấy tờ. |
| **6.2** | O+M · giữ | Owner gật/lắc qua chat; ghi **nguyên văn, scope, CV, phiên/SHA, nguồn quyết định** vào CAT-025 rồi đọc lại; AI không ký thay. |
| **6.3** | M · **sửa bắt buộc** | Gật ⇒ nhánh “lắc” NOT_APPLICABLE có luật; lắc ⇒ ghi nợ + return_to; các checkpoint **thực sự phụ thuộc vào phần sửa** về CẦN_RÀ/TEST_LẠI, giữ lịch sử; không reset mù tất cả checkpoint tới 6.3. Chờ Owner ⇒ KQ DỪNG, không giữ RUN/lease. |
| **7.1** | M · **sửa bắt buộc** | Cả 24 checkpoint ở trạng thái kết thúc hợp lệ (PASS hoặc NA có căn cứ), **0 nợ CHẶN G1 chưa giải quyết**; không bắt mọi nợ trên toàn hệ thống phải đóng. |
| **7.2** | M+N · sửa | Nợ để G2 chỉ được còn mở nếu **không chặn G1**, có chủ, mức độ, điều kiện mở lại/đích bàn giao; 0 vấn đề thì không lập nợ giả. |
| **7.3** | M · sửa | CV đóng **G1 thiết kế đã duyệt** khi 7.1 đạt và có quyết định Owner; không dùng “đã test xong” của một đối tượng làm trạng thái công việc. Báo 4 dòng, không tự mở G2. |

**Sửa nghịch lý thứ tự mà Gemini nêu:** AI **được soạn các dữ liệu NHÁP 4.1–4.7 trong một commit**; **chỉ dấu ĐÃ KIỂM** bị khóa theo thứ tự. Một lệnh DOT đọc SHA, kiểm và đóng checkpoint **cuốn chiếu 1.1→4.8**; gặp lỗi thì dừng đúng checkpoint đầu lỗi, ghi vào CAT-069 nếu là nợ thật. Không 8 lần commit/RUN, không tự tích xanh khi mới gõ JSON. Khi cần hồi quy, hạ đúng phụ thuộc, không xoá lịch sử.

### 3. MÁY KIỂM ĐƯỢC VÀ KHÔNG ĐƯỢC

- **Có thể cưỡng chế sau B2 thử thật:** duy nhất mã/quan hệ; checkpoint phiên khuôn; đếm đối tượng Master và nghĩa vụ đã khai; nguồn SHA, receipt và đọc lại; thứ tự và con trỏ; trạng thái PASS/NA hợp lệ, nợ chặn; thay đổi phiên làm nơi dùng CẦN_RÀ_LẠI. **Hiện mới là thiết kế, CHƯA PASS runtime.**
- **Chưa máy tự biết đúng nghĩa:** chọn mẫu UI hợp nghề, các nghĩa vụ thông tin còn chưa khai, Field khác tên trùng nghĩa, nợ nghiệp vụ đủ chưa. Cần AI/Reviewer/Owner; không lấy “>=1 dòng/màn” hoặc “HTTP 200” thay bằng chứng nghiệp vụ/UI thật.
- Nguồn NHÁP là GitHub/JSON ⇒ **modified_at của Directus một mình chưa đủ** xác định thay đổi có nghĩa; so **SHA/phiên/hash nội dung đã nghiệm thu + dependency_refs**. Directus revisions là lịch sử kỹ thuật, **không đương nhiên thay CAT-016** (nguyên nhân và tác động sửa nghiệp vụ).
- **Thẻ chuẩn một nguồn (Master Step):** mã bước · phiên khuôn · bước sau/điều kiện trước · actor/tool · input refs · việc làm · output/where · check/expected · on_fail/return_to · khi nào N/A. Hồ sơ CV chỉ ghi mã thẻ, trạng thái, thực tế, receipt; 9 câu 006 được rút thành trường thẻ **định nghĩa một lần**.
- Phép khóa cứng phải có ca âm tính tại B2: tạo hồ sơ lại không nhân đôi, cố đi vượt thứ tự, thiếu nhà, ghi khống, drift và ghi ngoài vùng. Trừ khi test đạt, chỉ gọi là **dự kiến khóa**, không tự nói “muốn làm sai cũng không được” (đặc biệt SSH đặc quyền R47 còn hở).

### 4. MÃ NHÀ: PHẢN BIỆN CHỖ GEMINI V13.1 ĐỀ NGHỊ GỘP

**Không chốt bảng “9 Collection mới + 1 dùng lại” của Gemini:** bảng ghi **12 mục**, trong đó mục 1–11 là 11 ứng viên bảng nháp và mục 12 dùng lại; con số **9+1 sai số học**. Quan trọng hơn, chưa đo schema/vị trí thật nên **số Collection phải là kết quả B1**, không phải mục tiêu cố định.

| Mã đang tranh luận | Đề nghị GPT sau đối chiếu registry/schema nguồn |
|---|---|
| **ML-DEF-011 ↔ ML-DEF-012** | 011 là **Master Master List** (loại danh mục, đối tượng, UI cha); 012 là **Master Master of Master** (Master List, nhóm, đối tượng, UI). **Không tự coi alias**. Dùng **012** làm danh bạ nơi của các Master (R53), 011 tiếp tục giữ nghĩa Master List/phân loại; chỉ gộp sau khi chứng minh cùng hàng dữ liệu. |
| **ML-MOW-TH-001 ↔ ML-DEF-004** | Một bên là **Master Quy trình tổng hợp**, bên kia **Master MOW**. Không tự alias; ghi **quan hệ**. |
| **ML-DEF-022 ↔ ML-DEF-005** | 022 là **Master Step**, còn 005 là **Master MOT**. **Tuyệt đối không alias** Step thành MOT. MOW-TH-007 giữ mã khuôn ở Master tổng hợp, 24 thẻ dùng 022 và liên kết quy trình. |
| **ML-DEF-018 ↔ ML-DEF-017** | 018 là UI **con**, 017 UI **cha**. Có quan hệ cha–con, **không là bí danh**. |
| **CAT-227 ↔ DEF00.1** | CAT-227* là **sổ việc/thiết kế hồ sơ**, DEF00.1 là mã/tham chiếu UI/đối tượng trong lịch sử; B1 xác minh liên kết **không mặc định alias cùng cấp**. Một CV là một việc; 24 dòng checkpoint là bản ghi con, không tạo 24 CV. |
| **CAT-228 ↔ Hồ sơ checkpoint** | CAT-228* trong nguồn có **application_id, order, process_code, depends_on, result_ref** (kế hoạch/tiến độ), **có thể ứng viên dùng cho 24 dòng**, nhưng **chưa chứng minh đã có đủ trạng thái/receipt/template_version/return_to**. B1 kiểm schema và bổ sung Field qua Master nếu hợp; không mặc định đã có nhà checkpoint đạt. |
| **CAT-025 ↔ ML-DEF-027** | CAT-025 là **quyết định cụ thể** (decision_type, actor, decided_at, scope, authority_ref), ML-DEF-027 là Master **định nghĩa Quyết định** (issue, decider, result, effective). Không tự alias loại với bản ghi quyết định. |
| **CAT-015 ↔ CAT-229 ↔ CAT-239 ↔ ML-DEF-025/026** | 015 = **kết quả kiểm** (criterion, result, validity...), 229 = **lượt/attempt** (attempt_no, started_at, finished_at...), 239 = **file/bằng chứng** (file_uri, hash, mime_type, retention...), ML-DEF-025/026 = danh mục Test/Bằng chứng. **Không gộp nguồn về CAT-015** chỉ để giảm bảng; có thể gộp **màn hình quản lý** và trỏ mã. Nếu muốn một bảng vật lý dùng chung, phải chứng minh giữ đủ quan hệ/lịch sử/đặc tính từng loại, không tự nhận alias. |
| **ML-DEF-024 ↔ CAT-006** | 024 = Master DOT, 006 là hồ sơ/Tool kỹ thuật trong snapshot; tra sổ DOT **LIVE** và trạng thái công cụ đang ngừng dùng trước khi coi là alias. Không tạo sổ DOT thứ hai. |
| **CAT-069? → CAT-069** | Giữ ý định Master nợ; ký hiệu “?” trong snapshot không là quyết định chuyển mã. B1 phải xác định mã chính thức và lịch sử tham chiếu, không tự đổi hàng loạt. |

**Nguyên tắc alias:** cùng **loại đối tượng + mức hạt (định nghĩa/việc/phiên/lượt/kết quả/hiện vật) + khóa + SSOT** mới được gộp. Khác chức năng nhưng muốn người dùng thấy chung ⇒ Directus có **màn tổng hợp/quan hệ**, không nhất thiết gộp bảng hoặc xóa sổ cũ.

### 5. HƯỚNG ĐI NGẮN NHẤT SAU ĐỐI CHIẾU

1. Claude chỉ hiệu chỉnh **24 thẻ trong V13** theo bảng trên; giữ 7 CP/24 việc, Luật Nhà R53 và UI Directus. Trình một bản chốt duy nhất, không viết 2 phiên bản khuôn ở P49/COLLAB/README.
2. B1 kiểm các alias/gộp **chỉ với các nhà G1/QT001 cần**; Master of Master ghi loại và nơi gốc, đối tượng chưa dựng còn trạng thái “cần làm” (có số cần/đã/thiếu). Không mở dự án dọn toàn bộ văn bản/registry trước QT001.
3. Khi Owner chốt, 24 thẻ đi vào **một nguồn Master Step ML-DEF-022**; quy trình MOW-TH-007 tham chiếu phiên/hash; CV thuộc CAT-227 mở hồ sơ 24 dòng tham chiếu thẻ. B1/B2 bootstrapping vẫn theo PROMPT đã điều chỉnh/Guard, **chưa chạy chính 007** trước khi các sổ được dựng. B3 mới áp 007 vào QT001.
4. Sau đó mới viết PROMPT/READY theo AGENTS. Chưa RUN, r2 cũ vẫn SUPERSEDED. **Không mở thêm Gemini vòng ba**; tôi đã đối chiếu ý kiến Gemini V13.1 để Host/Claude/Owner chốt một vòng.

**GPT_REVIEW = ACCEPT_FRAMEWORK / REQUEST_CHANGES_TO_24_STEPS_AND_ALIAS;** giữ đơn giản nhưng điều kiện xong phải thật sự kiểm được.






