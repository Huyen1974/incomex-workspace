# RUN14 — Candidate bốn thông tin, chưa triển khai

Đọc P460/KQ tại COLLAB. Candidate tiếp tục từ P452; RUN13 không chạy lại.

- [candidate.patch.md](candidate.patch.md): cumulative diff đúng baseline runtime P452; không áp thẳng lên checkout canonical khác byte.
- [manifest.json](manifest.json): source/patch/image/file hashes, phạm vi và giới hạn.
- [tests.md](tests.md): 136 kiểm thử local đạt (98 ca hồi quy cập nhật đầu vào + 38 ca mới), 0 fail/skip; một warning cũ.
- [linux-build.md](linux-build.md): build recipe, real HTTP probe và receipt của hai image candidate; không phải AI C1.
- [release-gate.md](release-gate.md): blocker source/rebuild, ma trận G1–G9 và Guard.

Một contract chung đóng gói byte-identical vào AD/FS/helper. Thêm envelope optional, chuẩn hóa NFKC/casefold/bí danh minh bạch, phân biệt source environment với Gateway, command RUN với operation id, raw/canonical/provenance, error missing_fields và isError qua HTTP. Giữ auth và carry context, hash idempotency dựa vào raw facts/auth để alias update không đổi receipt cũ.

Production không advertise/enforce, không Refresh client. Chưa promote lên đường build canonical; bản Git hồ sơ này là bằng chứng/candidate, không thay nguồn release. Không tuyên bố XONG.

NEXT_TRIGGER: GPT Host chốt cách phát hành theo baseline runtime mà không xóa hoặc đưa thêm phần Hermes/Gemini ngoài phạm vi; giữ candidate và image đã pin, hoàn tất source canonical/rebuild/rollback rồi mới advertise → client Refresh/C2 → C1 cold/final → enforce. Không cần Owner duyệt lại quyền hoặc bấm Refresh lúc chưa có schema mới trên server.
