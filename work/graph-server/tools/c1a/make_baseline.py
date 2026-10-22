#!/usr/bin/env python3
# GS-C1A-CERT-QUALITYGATE-20261022-07 · sinh manifest/cert-baseline.json = MỐC của đèn #24 (CT5), chỉ để dập tin trùng — KHÔNG làm ô xanh.
#   certified_floor        = ô ĐỦ ở lượt cấp giấy thật lúc cài (tụt khỏi ĐỦ ⇒ DOWN). Host thêm/bớt bằng apply-v0.
#   accepted_partial       = ô MỘT PHẦN đã có trong danh sách GAP C0 Host nhận P193 (TECH_ACCEPT_WITH_LIMITS) ⇒ không gọi trang.
#   pending_host_ack       = ô MỘT PHẦN KHÔNG có trong danh sách đó (đo lần đầu ở C1-A) ⇒ không tự nhận; tin đèn nêu tên, Host B1 quyết.
#   accepted_directory_parents = nguồn cha ở 9 cửa lúc cài (thêm/mất về sau ⇒ NEW_SOURCE_UNHANDLED / SOURCE_VANISHED ⇒ DOWN).
# Dùng: make_baseline.py <real_run.json> <cert-cells.json> <out.json>
import json, sys, time

run, cells, out = sys.argv[1:4]
d = json.load(open(run))
cat = {c["key"]: c for c in json.load(open(cells))["cells"]}
PENDING = {"lark:88-phai-cu:b88": "nguồn Lark 88-phai-cu mới hơn Graph (đo C1-A 22/10: +4 bản ghi/+10 cạnh so với bộ nạp R7); lane b88 graph-refresh "
                                  "nạp ở lượt timer kế — chưa có ACK Host",
           "kb:production_documents": "M-b đo lần đầu C1-A 22/10 (không vector/văn bản): PG ready thiếu ở Qdrant · Qdrant còn tài liệu đã xoá mềm · "
                                      "point thiếu document_id — Host B1 quyết nhận mốc hay giao sửa (không xoá/chuyển vector trong C1-A)"}
floor, acc, pend = [], {}, {}
for k, c in sorted(d["cells"].items()):
    if c["status"] == "ĐỦ tại T":
        floor.append(k)
    elif k in PENDING:
        pend[k] = {"why": PENDING[k], "reasons_at_install": c.get("reasons")}
    elif "GAP-C0" in str(cat[k].get("gap")) or str(cat[k].get("gap", "")).startswith("C0 "):
        acc[k] = {"gap": cat[k]["gap"], "ack": "Host P193 TECH_ACCEPT_WITH_LIMITS danh sách GAP C0 (P192) — chỉ dập tin trùng",
                  "reader_pass": bool(c.get("reader_pass")), "reasons_at_install": (c.get("reasons") or [])[:3]}
    else:
        pend[k] = {"why": "không thuộc danh sách GAP C0", "reasons_at_install": c.get("reasons")}
doc = {"format": "graph-cert-baseline-v1", "written_by": "GS-C1A-CERT-QUALITYGATE-20261022-07", "written_at": time.strftime("%FT%TZ", time.gmtime()),
       "from_run": {"generated_at": d["generated_at"], "self_sha256": d["self_sha256"]},
       "policy": "Mốc chỉ dập tin trùng của đèn #24; không bao giờ làm ô MỘT PHẦN thành ĐỦ (nhãn N4 luôn tính từ giấy). Đổi mốc = Host ghi lý do + apply-v0.",
       "certified_floor": floor, "accepted_partial": acc, "pending_host_ack": pend,
       "accepted_directory_parents": sorted(x for xs in (d.get("directory") or {}).get("parents", {}).values() for x in xs),
       "record_only_gates": ["G9"], "ephemeral_parent_patterns": ["^docker:workspace-job-[0-9a-f]+$"],
       "notes": {"G9": "thư mục việc work/* đổi thường xuyên theo việc mới ⇒ chỉ ghi băm/biên nhận, không gọi trang (Graph chưa có lớp việc — GAP-C0-13)",
                 "ephemeral": "container workspace_exec (workspace-job-<hex>) sống vài phút, do cổng agent-data quản lý"}}
json.dump(doc, open(out, "w"), ensure_ascii=False, indent=1, sort_keys=True)
print("floor=%d accepted=%d pending=%s parents=%d" % (len(floor), len(acc), sorted(pend), len(doc["accepted_directory_parents"])))
