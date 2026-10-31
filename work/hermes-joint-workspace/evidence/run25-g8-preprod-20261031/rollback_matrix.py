#!/usr/bin/env python3
"""RUN25: candidate -> rollback tree -> candidate on ONE queue.sqlite and one workspace, in separate processes.
Usage: rollback_matrix.py <candidate_tree> <rollback_tree> <label>. Runs only on this machine, in a temp dir.
The identity is set directly, as the gateway would after authentication.
Trees: `git archive <sha> agent_data | tar -x -C <dir>`; D1 = cc3df977 (running), main = 6160f9ad."""
import json, os, subprocess, sys, tempfile
from pathlib import Path

DRIVER = r"""
import json, sys, time
from agent_data import hvu_signals as hvu, workspace_tasks, workspace_tools as w
from agent_data.workspace_runtime import Queue
hvu.identity.set({'label': 'claude-code [auth:claude-code]', 'surface_key': 'k' * 24, 'gateway': 'agent-data', 'authenticated': True})
step = json.loads(sys.argv[1]); out = {}
try:
    kind = step['do']
    if kind == 'task':
        a = dict(tool='workspace_write_new', arguments={'root': 'ui', 'path': step['path'], 'content': 'x', 'message': 'm'}, operation_id=step['op'], **step.get('facts', {}))
        r = w.call('workspace_task_start', a)
        out['start'] = {k: r.get(k) for k in ('task_id', 'status', 'replayed', 'error')}
        if r.get('task_id'):
            for _ in range(200):
                s = w.call('workspace_task_status', {'task_id': r['task_id']})
                if s['status'] not in ('queued', 'running'): break
                time.sleep(0.1)
            out['final'] = s['status']
            out['receipt'] = bool((s.get('result') or {}).get('declaration_receipt'))
    elif kind == 'enqueue_declared':
        q = Queue(w.state_dir())
        out['id'] = q.enqueue('tasks', {'_hvu': hvu.hidden(), '_declaration': step['carried'], 'tool': 'workspace_write_new',
                                         'arguments': {'root': 'ui', 'path': step['path'], 'content': 'x', 'message': 'm'}, 'operation_id': None, 'args_hash': None})
    elif kind == 'drain':
        workspace_tasks.ensure_supervisor()
        for _ in range(200):
            s = w.call('workspace_task_status', {'task_id': step['id']})
            if s['status'] not in ('queued', 'running'): break
            time.sleep(0.1)
        out['final'] = s['status']; out['error'] = (s.get('result') or {}).get('error')
    elif kind == 'edit':
        st = w.call('workspace_stat', {'root': 'ui', 'path': step['path']})
        version = step.get('version') or st.get('version')
        a = dict(root='ui', path=step['path'], expected_version=version, message='m', edits=[{'old_str': 'x', 'new_str': 'y'}], operation_id=step['op'], **step.get('facts', {}))
        r = w.call('workspace_edit', a)
        out = {k: r.get(k) for k in ('changed', 'replayed', 'error', 'version')}; out['version_used'] = version
    elif kind == 'upload_begin':
        import base64, hashlib
        data = b'hello'
        r = w.call('workspace_upload_begin', dict(root='ui', path=step['path'], total_bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), message='m', **step.get('facts', {})))
        out = {k: r.get(k) for k in ('upload_id', 'error')}
    elif kind == 'upload_finish':
        import base64, hashlib
        r = w.call('workspace_upload_append', dict(upload_id=step['id'], offset=0, data_base64=base64.b64encode(b'hello').decode(), sha256=hashlib.sha256(b'hello').hexdigest()))
        out['append'] = r.get('error') or 'ok'
        r = w.call('workspace_upload_commit', dict(upload_id=step['id']))
        out['commit'] = r.get('error') or 'ok'
    elif kind == 'count':
        with Queue(w.state_dir()).db() as db:
            out['tasks'] = db.execute("SELECT count(*) c FROM jobs WHERE kind='tasks'").fetchone()['c']
            out['columns'] = sorted(x['name'] for x in db.execute('PRAGMA table_info(jobs)') if x['name'] in ('operation_id', 'args_hash'))
finally:
    workspace_tasks.stop_supervisor()
print(json.dumps(out, default=str))
"""

FACTS = {'declared_actor': 'Claude Code', 'declaration_context': {'origin_environment': 'macbook', 'task_id': 'hermes-joint-workspace', 'command_ref': 'RUN-rollback-matrix'}}
candidate, rollback, label = sys.argv[1:4]
tmp = Path(tempfile.mkdtemp(prefix='g8-rollback-'))
(tmp / 'ui').mkdir()
conf = tmp / 'config.json'
conf.write_text(json.dumps({'roots': {'ui': {'path': str(tmp / 'ui'), 'writable': True}}, 'state_dir': str(tmp / 'state'), 'resources': {'shutdown_grace_seconds': 1}}))

def run(tree, **step):
    env = {k: v for k, v in os.environ.items() if k not in ('PYTHONPATH', 'WORKSPACE_DECLARATION_MODE')}
    env.update(PYTHONPATH=tree, WORKSPACE_CONFIG=str(conf), PYTHONDONTWRITEBYTECODE='1')
    p = subprocess.run([sys.executable, '-c', DRIVER, json.dumps(step)], cwd=tree, env=env, capture_output=True, text=True, timeout=120)
    if p.returncode:
        return {'crash': p.stderr[-400:]}
    return json.loads(p.stdout.strip().splitlines()[-1])

rows = {}
rows['A1 candidate declared task op-a'] = run(candidate, do='task', path='a.txt', op='op-a', facts=FACTS)
rows['A2 rollback retry op-a without facts'] = run(rollback, do='task', path='a.txt', op='op-a')
rows['B1 candidate undeclared task op-b'] = run(candidate, do='task', path='b.txt', op='op-b')
rows['B2 rollback retry op-b'] = run(rollback, do='task', path='b.txt', op='op-b')
rows['count after B2'] = run(rollback, do='count')
rows['B3 file b.txt exists once'] = {'text': (tmp / 'ui' / 'b.txt').read_text() if (tmp / 'ui' / 'b.txt').exists() else None}
carried = {'contract_version': 'four-facts-1', 'normalizer_version': 'four-facts-1', 'alias_version': '1', 'declared_actor': 'claude-code', 'authenticated_actor': 'claude-code [auth:claude-code]',
           'facts': {k: {'raw': v, 'canonical': v, 'provenance': 'self_declared'} for k, v in {'declared_actor': 'Claude Code', 'origin_environment': 'macbook', 'task_id': 'hermes-joint-workspace', 'command_ref': 'RUN-x'}.items()},
           'command_kind': 'RUN', 'flags': []}
queued = run(candidate, do='enqueue_declared', path='c.txt', carried=carried)
rows['C1 candidate left a declared job queued'] = queued
rows['C2 rollback supervisor drains it'] = run(rollback, do='drain', id=queued.get('id'))
up = run(candidate, do='upload_begin', path='u.txt', facts=FACTS)
rows['D1 candidate declared upload begin'] = up
rows['D2 rollback append+commit'] = run(rollback, do='upload_finish', id=up.get('upload_id'))
(tmp / 'ui' / 'e.txt').write_text('x')
e1 = run(candidate, do='edit', path='e.txt', op='op-e')
rows['E1 candidate undeclared edit op-e'] = e1
rows['E2 rollback retry op-e same version'] = run(rollback, do='edit', path='e.txt', op='op-e', version=e1.get('version_used'))
rows['F1 candidate retry op-a with original facts'] = run(candidate, do='task', path='a.txt', op='op-a', facts=FACTS)
rows['count at end'] = run(candidate, do='count')
print(json.dumps({'label': label, 'rows': rows}, indent=1))
