# PROMPT — K10 persistence regression cho hai đầu nối

RUN_ID: K10-PERSIST-20260919-02

Chỉ chạy khi `COLLAB.md` ghi `READY@<full-sha>` khớp đúng commit cuối chạm `PROMPT.md` và có lệnh RUN hợp lệ từ Owner/GPT Editor.

## Mục tiêu
Chốt K10 của P08 mà **không restart production chỉ để thử**: chứng minh journal `operation_id` của cả GPT và Claude sống qua một process/handler mới và replay đúng, không tạo commit/job/write mới.

## Việc phải làm
1. Đọc `AGENTS.md`, `COLLAB.md` P07–P08 và KB §13 hiện hữu.
2. Xác minh persistence:
   - GPT: `state_dir()/operations.jsonl` nằm ngoài workspace, trên bind-mount host `/opt/incomex/data/workspace-tools`.
   - Claude: `FS_OPS_JOURNAL` nằm trên bind-mount host.
3. Với **mỗi đầu nối**, thêm regression test độc lập:
   - process/handler A ghi một operation có `operation_id` vào journal persistent;
   - kết thúc A, tạo **process/handler B mới** dùng cùng journal;
   - B gọi lại cùng tool + cùng id + cùng payload;
   - PASS khi nhận REPLAY/kết quả cũ và không sinh commit/job/write lần hai;
   - cùng id + payload khác vẫn bị từ chối.
4. Test dùng temp state/bản sao cô lập; không restart service production, không đụng dữ liệu business.
5. Nếu test đỏ: sửa tối thiểu đúng lỗi K10, thêm test đỏ-trước → xanh-sau. Chỉ deploy/restart nếu runtime code thật sự thay đổi; nếu chỉ thêm test thì không deploy.
6. Chạy regression liên quan của cả hai connector. Không tuyên bố client PASS; K1–K9 vẫn do Claude Chat/GPT Chat thực hiện.
7. Cập nhật **chính KB §13 hiện hữu**, thêm mục K10: test nào, kết quả, commit mã/test, có/không sửa runtime. Không tạo report/progress/handoff mới.
8. Không sửa `AGENTS.md`, `README.md`, `COLLAB.md`, `PROMPT.md`.

## Điều kiện PASS
K10 chỉ PASS khi cả GPT và Claude có:
- persistent host journal/bind-mount được xác minh;
- process/handler mới replay đúng từ journal cũ;
- không commit/job/write lần hai;
- khác payload bị từ chối;
- regression liên quan xanh.

## Trả lời Owner
Chỉ một dòng:
`K10-PERSIST-20260919-02: XONG — báo cáo KB §13`
hoặc
`K10-PERSIST-20260919-02: DỪNG — lý do ở KB §13`
