# work

Mọi công việc dài hạn nằm dưới thư mục này. Mỗi thư mục con trực tiếp là một việc/project độc lập và có `COLLAB.md` riêng; `PROMPT.md` chỉ có khi cần giao Agent. Test, evidence, assets và archive phải nằm trong đúng thư mục công việc, không đặt ở root repo.

Quy ước: `work/<work-id>/...`. Root repo chỉ giữ `AGENTS.md`, `README.md`, `COLLAB.md` và `work/`.

## Mẫu bắt buộc ở đầu mỗi `work/<work-id>/COLLAB.md`
Ngay sau dòng tiêu đề `# COLLAB — <work-id>`, phải là:

```md
## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Mục tiêu: ...
- Nhiệm vụ/phạm vi: ...
- Tiêu chí xong: ...
- Xác nhận User: CHƯA XÁC NHẬN | ĐÃ XÁC NHẬN — <ngày/nguồn chỉ đạo>
```

Theo `AGENTS.md#A0_OBJECTIVE`, AI mở việc/soạn thảo phải nhắc lại khối này và được User xác nhận trước khi lập/thảo luận kế hoạch, tạo PROMPT/RUN hay thực thi. Mọi AI vào việc phải đọc khối này trước phần trạng thái/kế hoạch.
