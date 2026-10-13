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
