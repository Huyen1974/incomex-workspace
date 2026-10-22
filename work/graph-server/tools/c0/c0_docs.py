#!/usr/bin/env python3
# GS-C0-COVERAGE-INVENTORY-20261022-05 · F8 · TÀI LIỆU / QUYẾT ĐỊNH / LUẬT TRONG REPO incomex-workspace (chỉ-đọc) — dùng lại được
# Chạy trên clone đọc (Mac): python3 -I c0_docs.py ~/projects/incomex-workspace > docs.json
# Đếm: DROOT, mục A AGENTS, việc Now/Done, PROMPT, mục P, trích dẫn DROOT/P/Điều, commit git và commit có trích dẫn.
import glob, json, os, re, subprocess, sys

top = sys.argv[1] if len(sys.argv) > 1 else "."
os.chdir(top)
S, D = {}, {}
agents = open("AGENTS.md", encoding="utf-8").read()
root = open("COLLAB.md", encoding="utf-8").read()
S["droot_ids_defined_root_collab"] = len(set(re.findall(r"\bDROOT(\d+)\b", root)))
S["droot_ids_cited_agents"] = len(set(re.findall(r"\bDROOT(\d+)\b", agents)))
S["agents_sections_A"] = len(re.findall(r"^## A\d+", agents, re.M))
work, done = sorted(glob.glob("work/*/COLLAB.md")), sorted(glob.glob("work/done-tasks/*/COLLAB.md"))
S["tasks_now"], S["tasks_done"] = len(work), len(done)
S["prompt_files"] = len(glob.glob("work/*/PROMPT.md")) + len(glob.glob("work/done-tasks/*/PROMPT.md"))
pent, dieu, droot_c, p_c = {}, set(), 0, 0
for f in work + done:
    t = open(f, encoding="utf-8", errors="replace").read()
    pent[f.split("/")[-2]] = len(re.findall(r"^### P\d+[a-z]?\b", t, re.M))
    dieu |= set(re.findall(r"Điều\s+(\d+)", t))
    droot_c += len(re.findall(r"\bDROOT\d+\b", t))
    p_c += len(re.findall(r"\bP\d{2,3}\b", t))
S["p_entries_total"] = sum(pent.values())
D["p_entries_by_task"] = pent
S["citations_in_task_collabs"] = {"DROOT": droot_c, "P_nn": p_c, "Dieu_distinct": len(dieu)}
S["dieu_distinct_ids"] = sorted(dieu, key=int)
log = subprocess.run(["git", "log", "--format=%H\t%s"], capture_output=True, text=True).stdout.splitlines()
S["git_commits"] = len(log)
S["commits_citing_P"] = sum(bool(re.search(r"\bP\d{2,3}\b", l)) for l in log)
S["commits_citing_DROOT"] = sum(bool(re.search(r"\bDROOT\d+\b", l)) for l in log)
S["commits_citing_task_or_RUN"] = sum(bool(re.search(r"work/|RUN|GS |HJW|VPSC|HVU", l)) for l in log)
S["files_tracked"] = len(subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.splitlines())
S["head"] = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
print(json.dumps({"summary": S, "detail": D}, ensure_ascii=False))
