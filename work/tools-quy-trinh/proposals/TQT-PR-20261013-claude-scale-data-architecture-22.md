# TQT-PR-20261013-claude-scale-data-architecture-22
## Cấu trúc dữ liệu cho 1.000 việc · tận dụng MacBook · luật 1 trang có máy chặn · 13/10/2026

TQT-PROPOSAL: TQT-PR-20261013-claude-scale-data-architecture-22
TARGET: cách lưu/ghi/đọc dữ liệu thử ngoài PG của tools-quy-trinh + mow-mot-moit-mout (view.html, UI-REVIEW-MOW001.json, catalog) · vai GitHub/MacBook/VPS · luật cho AI.
TESTED: chỉ đọc @4da3dbd. Đo kích thước file qua lịch sử Git; tách cấu trúc view.html và hồ sơ MOW001 bằng script; mô phỏng tách theo việc + bỏ trùng trên chính hồ sơ MOW001 (cục bộ, không ghi đâu); số đo cổng ghi (vps_status metrics); RAM/CPU/đĩa VPS; đọc PROOT04 (đo VPS 13/10). JEV: gen-dec-1791883595.
BLOCKER_TYPE: LOI_CAU_TRUC_DU_LIEU (một khối lớn, chép trùng, ghi lại cả khối) · LUAT_DAI_KHONG_CHAN (luật dài, không có máy chặn)
OBSERVED: mục 1.
PROPOSED_CHANGE: REQUEST_CHANGES đề xuất GPT — đồng ý hướng, sửa 5 điểm (mục 2). Mô hình mục 3, luật 1 trang mục 4, phép thử PT-01 mục 5.

---

## 0. Nhìn 30 giây
- 🔴 **Chậm vì hình dạng dữ liệu, không phải vì VPS yếu.** CPU VPS mới bận 20–31%. Cái nặng là: một việc = một khối 13 MB, bị chép thêm 1 bản vào view.html, sửa 1 ô cũng phải đọc và ghi lại cả khối.
- ✅ **Hướng của Owner đúng:** hiệu chỉnh ngoài PG, ổn mới vào PG một lần (D27). Không đưa từng phần vào PG.
- 🟢 **Cách sửa:** một định nghĩa dùng chung · mỗi việc một chỗ nhỏ · ghi nhỏ · view chỉ là khuôn. AI trên MacBook đọc tại máy, chỉ ghi qua cổng.
- 🟢 **Luật cho AI: 8 dòng, 6 dòng máy tự chặn** (mục 4). Phải đọc trước khi làm ≤ 1 trang, thay cho ~30.000 chữ hiện nay.

Ví dụ đời thường: thư viện. Sách gốc để một chỗ (định nghĩa quy trình). Người mượn chỉ cầm một phiếu nhỏ ghi mã sách (việc). Hiện nay ta photo nguyên cuốn sách kẹp vào mỗi phiếu, rồi dán tất cả phiếu lên bảng tin (view). Có 1 người mượn đã nặng; 1.000 người thì sập.

---

## 1. Số đo — đã xác minh / giả thuyết
| # | Điều | Số | Loại |
|---|---|---|---|
| S1 | view.html phình | 0,6 MB (10/10) → 101,7 MB (12/10 13:04) → 16,3 MB (nay) | ✅ Git |
| S2 | view.html chứa nguyên hồ sơ MOW001 | 8,65 MB, giống từng byte với UI-REVIEW-MOW001.json (12,9 MB) → **2 bản của cùng dữ liệu** | ✅ script |
| S3 | Chép trùng trong 1 hồ sơ | khối 128 KB chép vào 16 bản ghi; 1 chuỗi 112 KB lặp 27 lần; ~34% là trùng | ✅ script |
| S4 | Tách theo việc + bỏ trùng (mô phỏng trên MOW001) | 253 bản ghi trạng thái: trung vị 0,55 KB, lớn nhất 5,1 KB, tổng 195 KB · nội dung dùng chung 3,2 MB lưu 1 lần · lịch sử 1,9 MB | ✅ mô phỏng |
| S5 | Cổng ghi đọc thừa (cộng dồn từ khi cổng đo) | đọc 3,06 GB để trả 80 MB · tìm 2,77 GB · stat 1,74 GB (băm cả tệp) | ✅ metrics |
| S6 | Ghi lớn, đụng nhau (cộng dồn) | 1.459 giao dịch, TB 6,7 s, ~455 KB/lần, lỗi 14%, 116 xung đột phiên | ✅ metrics |
| S7 | VPS | CPU bận 20–31% · swap đầy 99% · container chạm trần RAM · workspace-exec ghi ~51 GiB/ngày · bản chụp giao dịch +1,4 GiB/ngày | ✅ PROOT04 |
| S8 | Luật phải đọc | AGENTS 10.773 chữ + README TQT 12.923 + §0 6.388 ≈ 30.000 chữ | ✅ đếm |
| S9 | Luật bị vi phạm | Bảng 13 dòng thay vì 8, sai thứ tự; nhật ký STARTED/KQ ghi vào ô 3; chữ dính liền không dấu cách; mục P lộn thứ tự | ✅ đọc COLLAB |
| H1 | MacBook chạy bộ kiểm/dựng view nhanh hơn VPS vài lần | MacBook đã chạy bộ kiểm 006 hết 92 s trên hồ sơ 13 MB (P46); VPS chưa có số so | ❓ đo ở PT-01 |
| H2 | Sau khi tách, việc thứ 1.000 không làm chậm việc thứ 1 | — | ❓ đo ở PT-01 |

Đã đúng hướng, giữ lại: P38 lưu lịch sử theo hash; P42 sự kiện 87 bước ghi theo definition_sha256. Chỉ cần tách khỏi view và thôi chép.

---

## 2. Phản biện đề xuất GPT — REQUEST_CHANGES
Đồng ý: nguyên nhân chính là cách lưu/ghi · tách view khỏi dữ liệu · định nghĩa lưu 1 lần · bằng chứng theo hash · AI chỉ lấy dữ liệu cần · thử có số đo · **không đưa từng phần vào PG** (phiên GPT thứ hai đúng, phiên thứ nhất sai với D27).

Sửa 5 điểm:
1. **Bỏ phương án B (SQLite trên VPS).** Trái điều kiện 1 của Owner: AI chat không đọc/ghi trực tiếp được, tệp nhị phân không xem khác biệt được, thêm một dịch vụ. Chọn A, cụ thể là **mỗi việc một thư mục nhỏ trong repo** (JEV 0,97). Đo chỉ để chốt ngưỡng, không để chọn A/B.
2. **Không dựng "kho dữ liệu thử trên VPS" riêng.** Kho thử chính là repo GitHub; VPS chỉ là cổng ghi + nơi Owner xem. Thêm kho thứ hai = hai nguồn chuẩn.
3. **MacBook: quan trọng nhất là "đọc tại chỗ", rồi mới đến "tính nặng".** Codex/Claude Code trên Mac đọc bản clone (miễn phí cho VPS) thay cho đọc/tìm/stat qua cổng (S5). Chỉ ghi qua cổng như hiện nay (JEV 1,0).
4. **Luật phải có máy chặn ở cổng ghi**, không chỉ viết ngắn (JEV 0,77). Cổng đã có sẵn cơ chế chặn (TRIAL_CONTRACT_REJECTED…), chỉ thêm ngưỡng.
5. **Danh sách việc cho Owner do máy sinh** (dùng lại hvu-sync ~4 phút đang chạy), AI không ghi tay — tránh một tệp "nóng" mà mọi AI cùng ghi.

Ghi thêm: ngoài PG chỉ cần chứa **định nghĩa + vài chục đến vài trăm ca thử**. 1.000 việc thật là việc của PG ở bước ③. Mô phỏng 1.000 việc trên MacBook là để chứng minh cấu trúc vào PG không phải sửa.

---

## 3. Mô hình đề xuất
| Nơi | Giữ / làm | Không làm |
|---|---|---|
| GitHub repo | Nguồn chuẩn duy nhất: định nghĩa (mã@phiên) · thư mục từng việc · luật · mã | Không chứa bản chép |
| MacBook | Codex/Claude Code đọc bản clone; chạy bộ kiểm, dựng/xem trước UI, chụp màn hình, mô phỏng 100–1.000 việc | Không giữ gì duy nhất: chưa commit = chưa có |
| VPS | Cổng ghi (kiểm phiên + máy chặn) · Owner view mỏng · MCP cho AI chat · Hermes | Không dựng kho riêng; không chạy dựng/kiểm nặng khi Mac làm được |
| PG | Bước ③: nạp một lần (D27) | Không ghi thử |

Hình dạng (Host nội dung chốt tên):
```
definitions/<mã>@<phiên>.json      ← quy trình, MOT, hợp đồng: lưu 1 lần, không sửa sau khi phát hành
jobs/<mã-việc>/state.json          ← trạng thái hiện tại của 1 việc (~200 KB)
jobs/<mã-việc>/events-<tháng>.jsonl ← mỗi lần ghi = thêm 1 dòng: master_code · record_id · schema_version · …
blobs/<sha256>                     ← nội dung lớn/bằng chứng, lưu 1 lần (quá lớn thì lên Drive, giữ hash)
view.html                          ← chỉ là khuôn ≤ 300 KB; mở việc nào tải việc đó
jobs/index.json                    ← máy sinh, 1 dòng/việc cho Owner: tên · 7 ô màu · ai làm tiếp · tắc vì gì
```
Mỗi dòng sự kiện có master_code + record_id + schema_version ⇒ bước ③ nạp thẳng vào bảng PG tương ứng, cùng bộ kiểm (PR-12 v2 C1).

Một điểm Owner cần gật: **tài liệu cho người vẫn là 1 trang (view); dữ liệu cho máy chia theo việc, giống từng dòng trong một bảng** — không phải đẻ thêm tài liệu.

---

## 4. Luật dữ liệu 1 trang (🤖 = cổng ghi tự chặn · 📖 = tự giác, kiểm sau)
1. 🤖 **Một định nghĩa, nhiều tham chiếu.** Việc chỉ ghi mã@phiên. Chặn khối ≥ 2 KB lặp lại trong hồ sơ.
2. 🤖 **Ghi nhỏ.** Mỗi lần ghi chạm đúng 1 việc, thêm dòng sự kiện; không ghi lại cả hồ sơ. Chặn 1 lần ghi > 100 KB, tệp dữ liệu > 2 MB.
3. 🤖 **View là khuôn.** Không nhúng dữ liệu việc. Chặn view > 300 KB.
4. 🤖 **Bằng chứng lớn theo hash.** Hồ sơ chỉ giữ hash. Chặn khối > 50 KB trong hồ sơ.
5. 📖 **Đọc đúng phần cần** theo mã việc/mã bước. AI trên MacBook đọc bản clone.
6. 📖 **Tính ở đâu cũng được, chưa commit = chưa có.** MacBook không giữ gì duy nhất.
7. 🤖 **Ghi có kiểm phiên.** Đụng nhau thì đọc lại, không ghi đè. Khoá theo việc, không khoá cả hệ.
8. 🤖 **Bảng đúng 8 dòng; ô 3 không chứa nhật ký chạy** (nhật ký → mục P).

Phải đọc trước khi làm: Bảng + ô 1–2 + 8 dòng này + thẻ việc mình (≤ 1 trang). Phần dài còn lại là để tra, không phải để nhớ.

---

## 5. Phép thử PT-01 (một lượt, không mở dự án hạ tầng)
- **Ca:** MOW001 (TQT-VIEC-001) + QTTH006.
- **Làm:** script chuyển hồ sơ hiện tại sang hình dạng mục 3 (bản cũ giữ nguyên, chỉ đọc, tới khi đạt) · view đọc theo việc · mô phỏng 100 và 1.000 việc **trên MacBook, không đẩy lên repo**.
- **Đo trước/sau 6 thao tác:** mở 1 việc · sửa 1 bước · đọc lại · chạy bộ kiểm 1 việc · xuất view · 2 AI ghi 2 việc cùng lúc.
- **Đạt khi (ngưỡng đề xuất, PT-01 chốt):**

| Phép | Ngưỡng |
|---|---|
| Sửa 1 bước | ghi ≤ 10 KB, ≤ 3 s |
| Mở 1 việc | tải ≤ 300 KB |
| Danh sách 1.000 việc cho Owner | mở ≤ 2 s |
| Việc thứ 1.000 so với việc thứ 1 | thời gian sửa 1 bước chênh ≤ 20% |
| 2 AI ghi 2 việc khác nhau | 0 xung đột; cùng 1 việc thì phát hiện xung đột phiên |
| MacBook tắt | Owner view vẫn mở bản đã commit |
| G1 đã nhận | 7/7 giữ nguyên, không mất lịch sử |
| Chuẩn bị vào PG | 100% dòng có master_code · record_id · schema_version |

- **Ai:** Codex (Host nội dung, chạy trên MacBook) làm · Claude Code đo lại độc lập trên MacBook · Claude Kiểm soát đối chiếu ngưỡng.
- **Khi:** phần chạy cục bộ làm được ngay; phần ghi repo sau khi VPSC-HEAL nhả VPS-GHI.

---

## 6. Việc bổ sung (thứ tự)
- **V0 — làm ngay, không cần dựng gì:** từ nay không nhúng thêm dữ liệu việc vào view.html, không chép định nghĩa (luật 1, 3).
- **V1 — PT-01** (mục 5).
- **V2 — đạt PT-01:** chuyển MOW001 sang hình dạng mới; view.html còn khuôn; bản cũ chuyển lưu trữ, không xoá.
- **V3 — máy chặn ở cổng** cho 6 luật 🤖, ngưỡng theo PT-01.
- **V4 — luật 1 trang:** đặt mục 4 ở đầu README; phần dài thành "tra cứu".
- **V5 — danh sách việc cho Owner do máy sinh** (hvu-sync).

## 7. Ranh giới với việc khác
RAM, swap, healthcheck, PG trên VPS là việc của VPSC-HEAL/PROOT04 (đang chạy). TQT chỉ lo cách lưu và ghi của mình — đúng các mục PROOT04 giao TQT: G9 (workspace-exec ~51 GiB/ngày), D06 (bản chụp giao dịch), D07 + D12 (image/staging tqt-*). Khoá chung VPS-GHI chỉ nên áp cho thay đổi hệ thống, không áp cho ghi dữ liệu việc (đề xuất cho Host root, ngoài phạm vi PR này).

## 8. Rà 2 vòng
- Vòng 1: số đo S1–S9 từ Git/metrics/PROOT04/script; tách đã xác minh khỏi giả thuyết (H1, H2 để PT-01 đo).
- Vòng 2: gốc rễ — dữ liệu từng việc bị nhúng vào khuôn dùng chung nên chi phí tăng theo tổng số việc. Kiểm mô hình theo 2 điều Owner giữ (GitHub chung · Owner xem view), D27 (PG một lần) và luật 1 tài liệu. JEV: gốc rễ là hình dạng dữ liệu 1,0 · thư mục theo việc 0,97 · Mac đọc tại chỗ 1,0 · máy chặn 0,77 · REQUEST_CHANGES 0,97.
