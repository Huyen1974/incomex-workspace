# PROMPT — LANE A03 · Align dot-walk with Process Contract HTML

RUN_ID: MMIM-LANE-A03-20260928-01
PROCESS: CHUNG.APQUYTRINH
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor: Codex

Write scope:
- `work/mow-mot-moit-mout/cong-cu/dot-walk-check.py`
- `work/mow-mot-moit-mout/lane-a/COLLAB.md`

READ-ONLY:
- `ban-duyet.html`
- `cong-cu/dot-process-gate.py`
- lane-b/COLLAB B02 KQ.

## 0. Gate
Đọc AGENTS → parent COLLAB D56–D63 → Lane A A02 KQ → Lane B B02 KQ → file này.
Chạy E1 gate trên prompt/catalog trước mutation. FAIL → DỪNG.

## 1. Lỗi cần sửa
A02 contract schema đặt process attrs trên chính thẻ `<p ...>`.
B02 đã chứng minh:
- attrs trên wrapper div → dot-walk PASS nhưng A02 audit 0/0;
- attrs trên p → A02 audit 12/15 nhưng dot-walk chỉ thấy 27 process.

Root cause: `dot-walk-check.py::parse_procs` regex chỉ nhận đúng `<p><b>MÃ</b>...`.

## 2. Sửa tối thiểu
Giữ contract A02: attrs nằm trên `p`.
Nâng `dot-walk-check.py` để nhận:
- `<p><b>CODE</b>...`
- `<p data-...><b>CODE</b>...`
- whitespace hợp lệ giữa p và b nếu có.

Vẫn chỉ parse trong `id="ml5-cho-ai"`.
Không đọc/diễn giải contract attrs; walk-check chỉ cần không làm mất process vì attrs.
Không refactor rộng nếu không cần.

Khuôn đề xuất tối thiểu:
`<p\\b[^>]*>\\s*<b>([A-Z0-9_]+\\.[A-Z0-9_]+)</b>(.*?)</p>`
hoặc parser tương đương an toàn hơn, nhưng phải giữ toàn bộ acceptance cũ.

## 3. Test bắt buộc
1. Catalog hiện hành 39 process: walk exit 0, số/actor/labels giữ baseline.
2. Fixture clone catalog, thêm attrs A02 trên đúng 12 `p` nhưng không span: walk vẫn thấy 39.
3. Fixture contract đầy đủ tối thiểu có proc-contract spans: walk vẫn thấy 39.
4. Thẻ p unrelated ngoài ml5-cho-ai không được tính process.
5. Process code malformed không được tính.
6. dot-process-gate E1 trên catalog hiện hành vẫn PASS.
7. A02 `--audit-contracts` trên catalog hiện hành vẫn 0/39 opt-in, errors=0.
8. py_compile PASS.

Không sửa ban-duyet để test; fixture temp/scratch only.

## 4. Không làm
- không sửa process canonical;
- không sửa A02 gate;
- không Step/UI;
- không E3 gateway;
- không tạo file mới.

## 5. KQ
`KQ@MMIM-LANE-A03-20260928-01 XONG|DỪNG`
`KQ@LANE-A A03 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS|BLOCK · walk_attrs=PASS|BLOCK · NEXT=B02R1|<...>`

Báo ngắn:
`XONG · A03 · walk39=PASS · attrs_p=PASS · A02_compat=PASS · NEXT=B02R1`

Dừng.
