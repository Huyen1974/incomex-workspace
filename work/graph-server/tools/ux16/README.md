# ux16 — bảng hướng dẫn tiếng Việt cho Gephi Lite (Graph riêng trên Mac)

- **Lượt tạo:** `GS-MAC-UX-CLEAR-20261027-16` (P279–P280, Claude Code CLI) · nghiệm thu: TECH_ACCEPT_WITH_LIMITS (P288) · lưu lên repo: DOC-SYNC 28/10.
- **Làm gì:** thêm 1 dòng hook vào bundle Gephi Lite v1.0.2 (`window.__incomexGL`) và nối khối «INCOMEX GUIDE» vào cuối bundle: bảng «Hướng dẫn & Quan hệ» (quan hệ trực tiếp · ứng viên tách riêng · 2 bước ghi là suy luận; báo số quan hệ bị ẩn khi lọc; nghĩa nhãn; tên nút bấm). Chỉ đọc dữ liệu đã nạp, 0 mã mạng, chỉ dùng `textContent`.
- **Tệp:** `build.py` (dựng lại bundle từ bản sao lưu byte-exact) · `incomex-guide.js` (nguồn bảng).
- **Khác bản trên Mac đúng 1 chỗ:** chữ gợi ý ô tìm. Mac: «Gõ mã, ví dụ <mã đơn thật>» (sha256 `560fb9fe3d9dcb9ae3a744205a190b0037d409773cc5fcc52d488f3175e55bbc`); repo: «Gõ mã nút» (sha256 `3656c71abeab14e1acece11523c70f3e38f118a96eccdac9b79a8eefcf406279`) vì repo công khai. Dựng từ bản repo cho bundle khác bản đang chạy đúng chuỗi gợi ý đó.
- **Mã băm:** bundle gốc `index-CWSVxO7S.js` `801f1ac1d1281b987e88d0afa14c3900ee4aa94301490d9814918639bbb69a77` → bản đang chạy `8390895199529e405f8d105bafb5474437c6177e4fa2338dfd9e444f9ecb5f8e` · `build.py` `cd7da212526cd977e70d4f06254aac4e07f5f5085b2959a08d64a8b3034f14a3` · GEXF không đổi `2cdd641220e6991ec689aaa5c5fbefa5df66e4a4e974d06ea2b22c9375013826`.
- **Đã kiểm dựng lại (28/10, DOC-SYNC, ngoài Mac):** `build.py` (chỉ đổi 2 đường dẫn sang thư mục tạm) + bản sao lưu `801f1ac1…` + guide bản Mac ⇒ đúng `8390895199529e405f8d105bafb5474437c6177e4fa2338dfd9e444f9ecb5f8e` (bundle đang chạy); guide bản repo ⇒ `4e3aac24310fccebfb0dafec798811272f226ed58496903ceacf34416fae5d12`, khác đúng 1 dòng `inp.placeholder`.
- **Công cụ mở/dựng màn hình đi kèm:** `../view-mac/` (`serve.py`, `OPEN-GRAPH.command`, `build/`).
- **Dựng lại (trên Mac):** `python3 build.py ~/Incomex-Graph-View/ux16/incomex-guide.js` (đường dẫn trong `build.py` là của Mac Owner).
- **Lùi:** chép `~/Incomex-Graph-View/ux16/backup/index-CWSVxO7S.js.truoc` về `app/gephi-lite/v1.0.2/assets/index-CWSVxO7S.js` (byte-exact); README cũ ở `ux16/backup/README.txt.truoc`.
- **Bộ thử:** `~/Incomex-Graph-View/ux16/tests/` (`cdp-run.mjs` + `tests-*.mjs`, node 20 `--experimental-websocket`, Chrome headless hồ sơ tạm, tắt extension) — KHÔNG đưa lên repo vì chứa mã đơn/record id thật.
- **Nợ:** chưa đăng ký vào sổ công cụ Master Tool/DOT (cần lượt ghi có quyền). Bản Mac là bản chạy: sửa trên Mac thì cùng lượt chép lại đây và cập nhật mã băm.
