# CT-000 audit — công cụ dùng chung

**Master:** ML-DEF-023 · mã ổn định `python:ct000-audit`. Không cấp mã công cụ mới theo từng phiên hoặc từng script con.

**Bậc 3: code kiểm thử mỏng**, dùng lại bộ mô phỏng Claude làm đối tượng cần kiểm; không xây bộ vận hành/điều phối mới. Các điều kiện mong đợi của ca phản ví dụ được kiểm riêng với B1–B11. Bộ này không phải một máy chứng minh độc lập hoàn chỉnh.

## Chạy v6 trên nguồn hiện tại trong repo

Từ thư mục gốc repo, Python 3, không cần gói ngoài:

```bash
python3 work/mow-mot-moit-mout/audit-ct000/run.py --out /tmp/ct000-audit-v6-results
```

## Tái hiện đúng bản đã rà dù nguồn hiện tại đã đổi

```bash
python3 work/mow-mot-moit-mout/audit-ct000/run.py --snapshot --out /tmp/ct000-audit-v6-results
```

Hai lệnh đọc HTML + mã kiểm; ghi JSON và stdout/stderr vào `--out`. Không gọi PG, Directus, mạng hoặc duyệt đồ thị lớn. Không sửa đầu vào. Kết quả bản đang chốt phải là **exit 1, FINDINGS_REMAIN**.

- **0:** các probe đã chạy đạt trong phạm vi ghi ở báo cáo; không thay nghiệm thu PG/Flow hoặc duyệt hết 17 kịch bản.
- **1:** tái hiện được điểm cần sửa/kiểm; có JSON/vết chạy.
- **2:** nguồn đổi ngoài phiên hỗ trợ, thiếu đầu vào hoặc máy kiểm lỗi; chưa kết luận, không tính là phát hiện đột biến thành công.

Đọc `REPORT.md` và `evidence/summary.json`. `flow_results.json` chứa đường đi + dữ kiện trước/sau; `checker_results.json` chứa phép thử khả năng phát hiện và phân loại kết quả của máy kiểm; `data_results.json` chứa đầu vào thiếu/sai.

## Phiên được hỗ trợ

V6 rà bản 107 dòng tại head `250792dce8380e94aa5fe85ce22477925150e6b8`:

- `ban-duyet.html` đầy đủ: SHA256 `b94a70383f2e44ffadd9fa6c3e60868152eb0027c53cbb82e9ea8e1184625999`.
- Trích đoạn trong `snapshots/ban-duyet.html` (có đủ CT-000.4): SHA256 `4d2a73a183c2ded90de6164a0e33eaf2ce47efef740edeb5157e67648fd69e83`.
- `kiem-ct000-4.py`: SHA256 `9e9436cdc058cb480e08ed6dc7062e0d74b18aae43ccbd1e632342939e4ecbd2`.

Nguồn đổi: rà ý nghĩa thay đổi, cập nhật các ca và guard rồi kiểm lại. **Không chỉ đổi hash để tắt cảnh báo.** Bản chụp trong snapshots là bằng chứng lịch sử, không phải nguồn vận hành thứ hai.

## Dùng lại v5

V5 giữ nguyên tại `work/mow-mot-moit-mout/ct000-audit-v5/`, gồm mã, bản nguồn, 11 đột biến và bằng chứng 92 dòng. Chạy:

```bash
python3 work/mow-mot-moit-mout/ct000-audit-v5/audit_ct000.py --out /tmp/ct000-audit-v5-results
```

V5 chỉ tái hiện bản 92 dòng; không dùng nó để ký bản 107 dòng. Cùng một mã Master giữ đường đọc các phiên, phạm vi và hash để tránh viết lại công cụ khi cần tra lỗi cũ.

## Vòng đời

Chủ quản nội dung quy trình: Claude Host, việc `mbm-qtth-07-ve-ui-mow`. Ghế phản biện: GPT. Công cụ là tài sản dùng chung, mọi AI có quyền đọc repo đều có thể chạy theo phạm vi này. Không có lịch chạy nền, không cấp quyền triển khai. Kết quả thiếu bằng chứng phải được giữ là chưa kiểm.
