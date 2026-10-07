#!/usr/bin/env python3
"""Receipt completeness gate; does not substitute for browser/visual tests."""
import json, sys
from pathlib import Path
CONTRACT = json.loads(Path(__file__).with_name("UI-REVIEW-CONTRACT.json").read_text())
CHECKS = CONTRACT["required_checks"]
def validate(d):
    errors=[]
    if not d.get("source_version"): errors.append("missing source_version")
    scope=d.get("scope",[])
    if not scope or len(scope)!=len(set(scope)): errors.append("scope empty or duplicate")
    rows=d.get("results",[])
    ids=[r.get("id") for r in rows]
    if len(ids)!=len(set(ids)) or set(ids)!=set(scope): errors.append("results must cover scope exactly once")
    for r in rows:
        if not r.get("url"): errors.append(str(r.get("id"))+": missing URL")
        parity=r.get("parity",{})
        for key in CONTRACT["parity_required"]:
            if key not in parity: errors.append(str(r.get("id"))+": missing parity."+key)
        for key in ("baseline_url","baseline_version","observed_version"):
            if not parity.get(key): errors.append(str(r.get("id"))+": empty parity."+key)
        measurements=parity.get("measurements",[])
        if not measurements: errors.append(str(r.get("id"))+": no measured comparison")
        for m in measurements:
            if not all(k in m for k in ("part","property","expected","actual")):
                errors.append(str(r.get("id"))+": malformed measurement"); continue
            if m["expected"] != m["actual"]:
                errors.append(str(r.get("id"))+": style mismatch "+m["part"]+"."+m["property"])
            if r.get("parent")=="UI.MASTER" and not r.get("specialized_parent"):
                token=CONTRACT["master_parent_baseline"]["tokens"].get(m["part"],{}).get(m["property"])
                if token is not None and (m["expected"]!=token or m["actual"]!=token):
                    errors.append(str(r.get("id"))+": violates approved Master token")
        if parity.get("differences"): errors.append(str(r.get("id"))+": unresolved differences")
        for k in CHECKS:
            c=r.get("checks",{}).get(k,{})
            if c.get("status") not in ("PASS","N-A") or not str(c.get("evidence","")).strip():
                errors.append(str(r.get("id"))+":"+k+" incomplete/failed or no evidence")
    return errors
if __name__=="__main__":
    if len(sys.argv)!=2: sys.exit("usage: check-ui-review.py receipt.json")
    try: errors=validate(json.loads(Path(sys.argv[1]).read_text()))
    except (OSError,ValueError,TypeError,KeyError) as e: sys.exit("BLOCKED: "+str(e))
    print("BLOCKED\n"+"\n".join(errors) if errors else "RECEIPT_COMPLETE (verify evidence separately)")
    sys.exit(bool(errors))
