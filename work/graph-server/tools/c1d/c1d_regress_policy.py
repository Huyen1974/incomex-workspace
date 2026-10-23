#!/usr/bin/env python3
# GS-C1D · F18c / F22c: SUPERSEDED_BY_POLICY có bằng chứng + ca THAY THẾ chạy trên luật hiện hành (không xoá ca cũ, không tô 51/51).
# F18c (C1-A) khẳng định: Guard CŨ (trước dòng A24) coi nguồn gửi graph-refresh là «ngoài sổ» ⇒ INV16 đỏ. C1-A đã CÓ CHỦ ĐÍCH thêm A24 ⇒ trên
#   Guard hiện hành graph-refresh nằm trong sổ. Bất biến thật cần giữ = «nguồn gửi KHÔNG đăng ký ⇒ INV16 'ngoài sổ'»: ca F18c' tiêm một đường
#   gửi giả chưa đăng ký vào Guard SỐNG (bản chép, chỉ đọc kuma) ⇒ phải đỏ; và graph-refresh (đã đăng ký A24) ⇒ không đỏ.
# F22c (C1-A) khẳng định: ô MỘT PHẦN chưa nhận mốc ⇒ KHÔNG gọi trang. C1-C (JEV gen-dec-1792730088 chọn B) đổi: VÀNG MỚI gọi trang ĐÚNG MỘT lượt
#   rồi UP kèm danh sách vàng. Ca F22c': lượt 1 ⇒ DOWN (NEW) · lượt 2 cùng sự cố ⇒ UP + «VÀNG mở» (ALREADY_NOTIFIED).
# K1.6f (C1-C) khẳng định: bộ nhãn cũ trong bộ nhớ, tệp đổi ⇒ nạp bản trên đĩa VÀ vẫn ĐỦ với giấy do bản cũ cấp. K3 (PROMPT C1-D §2: engine
#   version drift ⇒ MỘT PHẦN) đổi: bộ máy trên đĩa ≠ bộ máy đã cấp giấy ⇒ MỘT PHẦN ENGINE_CHANGED_SINCE_CERT tới khi bộ máy mới cấp lại. Ca K1.6f':
#   tệp đổi ⇒ nhãn do BẢN TRÊN ĐĨA tính (băm mới trong lý do) + MỘT PHẦN; giấy cấp lại bởi bản mới ⇒ ĐỦ.
# Dùng: c1d_regress_policy.py <guard sống> <guard.orig C1-A> <graph_cert C1-A v1> <graph_cert ứng viên v5> <out.json> <cert-cells c1d> <giấy v5 dời giờ>
import hashlib, importlib.machinery, importlib.util, json, os, sys, tempfile, time
guard, guard_orig, gc_v1, gc_v5, out, cells_p, doc_p = sys.argv[1:8]
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()


def load(path, name):
    ldr = importlib.machinery.SourceFileLoader(name, path)
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader(name, ldr))
    ldr.exec_module(m)
    return m
res = []
gd = load(guard, "guard_live_fx")
kf = gd.kuma_coverage_facts()
now = kf["now"]
tbf = gd.tin_bao_facts(["INV15.kuma_telegram_coverage"], kf, now)
tbf["found"]["path:/opt/incomex/graph-server/prod-v1/bin/graph-refresh"] = "incomex-graph-refresh.service"
tbf["found"]["path:/opt/incomex/graph-server/prod-v1/bin/c1d-fixture-unregistered-sender"] = "incomex-c1d-fixture.service"
gd.c_tin_bao(tbf)
loi = gd.TB_LAST["loi"]
fake = any("c1d-fixture-unregistered-sender" in x and "ngoài sổ" in x for x in loi)
gref = not any("graph-refresh" in x and "ngoài sổ" in x for x in loi)
res.append({"id": "F18c'", "replaces": "F18c", "status": "SUPERSEDED_BY_POLICY", "pass": fake and gref,
            "prior_rule": {"file": guard_orig, "sha256": sha(guard_orig), "assertion": "graph-refresh KHÔNG có dòng sổ ⇒ INV16 'ngoài sổ' ĐỎ"},
            "current_rule": {"file": guard, "sha256": sha(guard), "assertion": "A24 đăng ký graph-refresh; nguồn gửi chưa đăng ký ⇒ 'ngoài sổ' ĐỎ"},
            "detail": {"fake_flagged": fake, "graph_refresh_not_flagged": gref, "loi_sample": loi[:3]}})
tmp = tempfile.mkdtemp(prefix="gs-c1d-pol-", dir="/dev/shm")
os.environ.update(GS_CERT_DIR=tmp + "/cert")
os.makedirs(tmp + "/cert")
G = load(gc_v5, "gc_v5_pol")
doc = {"format": G.FORMAT, "generated_at": G.now_iso(), "cells": {"x:cell": {"key": "x:cell", "status": G.MP, "reasons": ["GRAPH_CLASS_NOT_LOADED"], "reader_pass": True}},
       "directory": None, "summary": {"du": 0, "cells": 1}}
doc["self_sha256"] = G.self_sha(doc)
st1, msg1, inc1 = G.alarm(doc, baseline={"accepted_partial": {}}, prev_open={})
G.record_incidents(inc1)
st2, msg2, inc2 = G.alarm(doc, baseline={"accepted_partial": {}})
res.append({"id": "F22c'", "replaces": "F22c", "status": "SUPERSEDED_BY_POLICY", "pass": st1 == "down" and "VÀNG MỚI" in msg1 and st2 == "up" and "VÀNG mở" in msg2,
            "prior_rule": {"file": gc_v1, "sha256": sha(gc_v1), "assertion": "ô MỘT PHẦN chưa nhận mốc ⇒ đèn UP, không gọi trang"},
            "current_rule": {"file": gc_v5, "sha256": sha(gc_v5), "assertion": "VÀNG MỚI gọi trang MỘT lượt (DOWN) rồi UP + danh sách vàng; nhắc 168h (C1-C, JEV gen-dec-1792730088 B)"},
            "detail": {"tick1": [st1, msg1[:100]], "tick2": [st2, msg2[:100]]}})
import shutil, copy
os.environ["GS_CERT_CELLS"] = cells_p
eng = tmp + "/engine/graph_cert.py"
os.makedirs(os.path.dirname(eng))
shutil.copyfile(gc_v5, eng)
E = load(eng, "gc_engine_copy_pol")
d0 = json.load(open(doc_p))
EP = dict(d0["graph_epoch"])
IUQ = "MATCH (g:PgTrigger)-[:ON_TABLE]->(:PgTable {id: 'public.information_unit'}) RETURN g.id AS x"
NOW = E.parse_iso("2026-10-23T05:00:00Z")
CAT = json.load(open(cells_p))
L0 = E.label_for("read-cypher", {"query": IUQ}, 7, NOW, d0, CAT, lambda: dict(EP), False)
with open(eng, "a") as f:
    f.write("\n# bản mới cài (đổi băm)\n")
new = sha(eng)
L1 = E.label_for("read-cypher", {"query": IUQ}, 7, NOW, d0, CAT, lambda: dict(EP), False)
d1 = copy.deepcopy(d0)
d1["engine_sha256"] = new
d1.pop("self_sha256", None)
d1["self_sha256"] = E.self_sha(d1)
L2 = E.label_for("read-cypher", {"query": IUQ}, 7, NOW, d1, CAT, lambda: dict(EP), False)
res.append({"id": "K1.6f'", "replaces": "K1.6f", "status": "SUPERSEDED_BY_POLICY",
            "pass": L0["completeness_label"] == E.DU and L1["completeness_label"] == E.MP and "ENGINE_CHANGED_SINCE_CERT" in L1["reason"] and new[:12] in L1["reason"]
                    and L2["completeness_label"] == E.DU,
            "prior_rule": {"file": "GS-C1C c1c_fixtures.py K1.6f", "assertion": "tệp bộ nhãn đổi ⇒ nạp bản đĩa, vẫn ĐỦ với giấy bản cũ"},
            "current_rule": {"file": gc_v5, "sha256": sha(gc_v5), "assertion": "K3: bộ máy đĩa ≠ bộ máy cấp giấy ⇒ MỘT PHẦN ENGINE_CHANGED_SINCE_CERT; cấp lại bởi bản mới ⇒ ĐỦ"},
            "detail": {"before_change": L0["completeness_label"], "after_change": [L1["completeness_label"], L1["reason"][:90]], "after_reissue": L2["completeness_label"]}})
shutil.rmtree(tmp, ignore_errors=True)
json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
for r in res:
    print(r["id"], "replaces", r["replaces"], r["status"], "PASS" if r["pass"] else "FAIL", json.dumps(r["detail"], ensure_ascii=False)[:200])
sys.exit(0 if all(r["pass"] for r in res) else 1)
