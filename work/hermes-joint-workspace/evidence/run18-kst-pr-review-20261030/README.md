# RUN18 — KST review PR #358 × PR #357 (Claude Code CLI, MacBook)

RUN_ID `HJW-G8-KST-PR358-PR357-REVIEW-20261030-18` · READY@f8468817fe1b671c0f6b3fb5c4c714f22b071480 · STARTED `b7508eb5` · kết luận ở HJW COLLAB P476.

## Ref đã ghim (đọc lại 03:11Z và 03:25Z, không đổi)
- main `b4c9ea19cf2e57594a231c2819e098fe0002c99a`
- PR #357 OPEN/DRAFT head `36c682914c9f412078113b6d85319f11356d1130` (4 tệp)
- PR #358 OPEN/DRAFT head `4851f6cde86bade6ce70433958cddc76a307f9f1` (6 tệp), check `gate` completed/success trên đúng head
- `deploy-vps.yml` state qua API Actions: `disabled_manually` (đo 03:2xZ; vẫn có trigger `push main` trong tệp, bật lại được bằng tay)

## Bản tích hợp tạm (chỉ Mac, branch local `kst/run18-int`, KHÔNG push, đã xoá sau lượt)
`git merge --no-ff refs/kst/pr358` trên PR357 ⇒ 1 xung đột duy nhất `agent_data/workspace_tasks.py`. Giải: giữ nguyên cấu trúc PR357 (`request` + `enqueue_once`), thêm hai chỗ của PR358:

```diff
-        request={'_hvu':hvu_signals.hidden(),'tool':tool,'arguments':args,'operation_id':a.get('operation_id'),'args_hash':args_hash}
+        request={'_hvu':hvu_signals.hidden(),'_declaration':declaration.current.get(),'tool':tool,'arguments':args,'operation_id':a.get('operation_id'),'args_hash':args_hash}
@@
-            op_id=w.check_operation_id(a['operation_id']);args_hash=request['args_hash']=w.payload_hash(a)
+            op_id=w.check_operation_id(a['operation_id']);args_hash=request['args_hash']=w.payload_hash(declaration.bind_hash(a))
```
(+ import `declaration_contract` và khối `run()` của PR358 áp sạch.)

Kiểm tương đương: `diff PR357..int` = đúng 6 tệp PR358, +264/−7 (bằng `diff main..PR358`); `diff PR358..int` = đúng 4 tệp PR357, +220/−48 (bằng `diff main..PR357`). Commit local `48cdd9dc22d4373121dc4ce3eebdaecbc416d04b`; sha256 `workspace_tasks.py` tích hợp `c17768e71f909bf1f162ed85b010ac979d108436ebb7d48fd8eb12527bc7bc77`.

## Kết quả test thật (venv Python 3.11.6, pytest 9.2.0, Mac)
| Bộ | Cây | Kết quả |
|---|---|---|
| RUN17 fixtures (evidence run17 tests-source) | tích hợp | 90 passed |
| KST real-process (tệp dưới) | tích hợp | 4 passed + 3 FAIL đúng chủ đích (2 lỗi done-tasks + 1 kỳ vọng mã lỗi nested, đã chỉnh: bị chặn ở cửa INVALID_ARGUMENT, 0 hàng/0 tệp) |
| `tests/continuation` (298) | PR357 | 39 failed, 221 passed, 5 skipped, 33 errors |
| `tests/continuation` (298) | tích hợp | 38 failed, 222 passed, 5 skipped, 33 errors — tập FAIL/ERROR trùng PR357, khác duy nhất race test bên dưới |
| PR357 `test_two_processes_same_id_at_once_queue_one_job` | PR357 và tích hợp | chập chờn, FAIL ở vòng 0 cả hai cây |
| Bản sửa F1 thử local (rồi hoàn tác) | tích hợp+F1 | KST 7 passed · RUN17 90 passed |

Lỗi có sẵn từ main (không do ghép): hai tiến trình cùng mở `queue.sqlite` CHƯA tồn tại ⇒ `PRAGMA journal_mode=WAL` → `sqlite3.OperationalError: database is locked` (tái hiện 4/9 tiến trình trên thư mục mới). `_BOOTSTRAP_LOCK` chỉ trong một tiến trình. Production đã có DB ở WAL nên không dính; chỉ làm race test PR357 chập chờn trên DB mới. Không có job nhân đôi (một bên nhận OPERATION_FAILED).

Các FAIL/ERROR có sẵn ở cả hai cây: thiếu `fastapi` trong venv, FS Mac không phân biệt hoa/thường (`name_twin`), hvu/lifecycle/restore fixtures — không liên quan diff.

Quan sát đường thật nhiều tiến trình (RUN17 chỉ in-process): `KST-QUEUE10-REAL: accepted=10 peak_running=4 completed=10 replay=10 rows=10 changed_fact=REUSED`; race 2 tiến trình cùng `operation_id` có khai báo 6/6 vòng = 1 job, 1 bên `replayed`; supervisor không chạy, chỉ poll `workspace_task_status` ⇒ hồi sinh, hoàn tất, receipt giữ đủ 4 facts.

Lỗi chứng minh: `DONE_TASKS {'path': 'work/done-tasks/kst-fixture/COLLAB.md'} derived= done-tasks declared-correct= CONTEXT_CLARIFICATION_REQUIRED` và `{'from': 'work/kst-fixture', 'to': 'work/done-tasks/kst-fixture'}` cùng kết quả. `CASE_VARIANT CONTEXT_CLARIFICATION_REQUIRED ['task_id'] {'task_id': 'hermes-joint-workspace'}` (ví dụ tĩnh, không phải task suy ra).

## Bản sửa F1 đã thử (đề xuất, không áp lên PR)
```diff
-        if len(parts) > 2 and parts[0] == 'work': tasks.add(parts[1])
+        # work/<id>/... and work/done-tasks/<id>/...; done-tasks is reserved, never a task id.
+        if parts[0] == 'work' and len(parts) >= 2 and parts[1]:
+            if parts[1] != 'done-tasks': tasks.add(parts[1])
+            elif len(parts) >= 3 and parts[2]: tasks.add(parts[2])
```
(Bản chạy thử thiếu hai kiểm `and parts[1]`/`and parts[2]` cho đường `work/`; thêm vào khi sửa thật.)

## Tệp test KST (chạy: `SRC=<cây> python -m pytest -c /dev/null --rootdir . -q -s <tệp>` trong cây; dọn `pkill -f agent_data.workspace_tasks` sau)
```python
"""KST RUN18 extra checks on local integration main+PR357+PR358 (real supervisor + OS worker subprocesses)."""
import json,os,signal,subprocess,sys,time
sys.path.insert(0,os.path.join(os.environ['SRC'],'tests','continuation'))
import pytest
from test_workspace import workspace, call, await_task
from agent_data import workspace_tools as w, hvu_signals as hvu, declaration_contract as d
from agent_data.workspace_runtime import Queue
REPO=os.environ['SRC']
CTX={'origin_environment':'MacBook','task_id':'kst-fixture','command_ref':'HJW-G8-KST-PR358-PR357-REVIEW-20261030-18'}

@pytest.fixture
def enforced(workspace,monkeypatch):
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
    ui,_,conf,f=workspace
    conf['resources']={'task_concurrency':4};f.write_text(json.dumps(conf))
    hvu.bind('credential:kst-fixture')
    Queue(w.state_dir())  # pre-bootstrap: the fresh-DB WAL race is pre-existing on main, tested separately
    yield workspace
    hvu.identity.set(None);hvu.agent.set(None)
    try:os.kill(int((w.state_dir()/'task-supervisor.pid').read_text()),signal.SIGTERM)
    except Exception:pass

def task(i,op=None,**over):
    a={'tool':'workspace_write_new','arguments':{'root':'ui','path':f'w{i}.md','content':f'x{i}\n','message':'kst','operation_id':f'inner-{i}'},
       'operation_id':op or f'kst-q-{i}','declared_actor':'Claude Code CLI','declaration_context':dict(CTX)}
    a.update(over);return a

def counts():
    with Queue(w.state_dir()).db() as db:return dict(db.execute("select status,count(*) from jobs where kind='tasks' group by status").fetchall())

def test_ten_declared_tasks_real_supervisor_four_workers(enforced):
    ui=enforced[0];keys=[]
    for i in range(10):
        r=call('workspace_task_start',**task(i));assert 'error' not in r,r;keys.append(r['task_id'])
    peak=0;deadline=time.monotonic()+120
    while time.monotonic()<deadline:
        c=counts();peak=max(peak,c.get('running',0))
        if c.get('completed',0)+c.get('failed',0)==10:break
        time.sleep(.05)
    assert counts()=={'completed':10},counts()
    assert 1<=peak<=4,peak
    for i,k in enumerate(keys):
        s=call('workspace_task_status',task_id=k);rc=s['result']['declaration_receipt']
        assert rc['authenticated_actor']=='credential:kst-fixture'
        assert {f:v['provenance'] for f,v in rc['facts'].items()}=={'declared_actor':'self_declared','origin_environment':'self_declared','task_id':'self_declared','command_ref':'self_declared'}
        assert rc['facts']['origin_environment']['canonical']=='macbook' and rc['command_kind']=='RUN'
        rp=call('workspace_task_start',**task(i));assert rp['task_id']==k and rp.get('replayed') is True,rp
    with Queue(w.state_dir()).db() as db:assert db.execute('select count(*) from jobs').fetchone()[0]==10
    assert sorted(p.name for p in ui.glob('w*.md'))==sorted(f'w{i}.md' for i in range(10))
    bad=call('workspace_task_start',**task(0,declaration_context=dict(CTX,task_id='other-task')))
    assert bad['error']=='OPERATION_ID_REUSED',bad

RACER='''
import json,os,sys,time
from agent_data import workspace_tools as w,hvu_signals as hvu
hvu.bind('credential:kst-fixture')
at=float(sys.argv[1])
while time.time()<at:pass
print(json.dumps(w.call('workspace_task_start',json.loads(sys.argv[2]))))
'''
def test_two_processes_same_declared_operation_one_job(enforced):
    env=dict(os.environ,PYTHONPATH=REPO)
    for r in range(6):
        at=time.time()+1.2;a=task(100+r,op=f'kst-race-{r}')
        ps=[subprocess.Popen([sys.executable,'-c',RACER,str(at),json.dumps(a)],stdout=subprocess.PIPE,text=True,env=env,cwd=REPO) for _ in range(2)]
        outs=[json.loads(p.communicate()[0].strip().splitlines()[-1]) for p in ps]
        assert all('error' not in o for o in outs),outs
        assert len({o['task_id'] for o in outs})==1,outs
        assert sum(bool(o.get('replayed')) for o in outs)==1,outs
    with Queue(w.state_dir()).db() as db:assert db.execute("select count(*) from jobs where kind='tasks'").fetchone()[0]==6

def test_dead_supervisor_poll_revives_and_keeps_declaration(enforced,monkeypatch):
    from agent_data import workspace_tasks as tasks
    real=tasks.ensure_supervisor
    monkeypatch.setattr(tasks,'ensure_supervisor',lambda:None)
    r=call('workspace_task_start',**task(7,op='kst-revive'));assert r['status']=='queued',r
    monkeypatch.setattr(tasks,'ensure_supervisor',real)
    s=await_task(r['task_id'],timeout=60)
    assert s['status']=='completed',s
    assert s['result']['declaration_receipt']['facts']['command_ref']['canonical']==CTX['command_ref']
    assert (enforced[0]/'w7.md').exists()

def test_nested_client_metadata_rejected_without_write(enforced):
    a=task(8,op='kst-nested');a['arguments']['_declaration']={'authenticated_actor':'credential:kst-fixture','facts':{}}
    r=call('workspace_task_start',**a)
    s=await_task(r['task_id'],timeout=60) if 'task_id' in r else r
    res=s.get('result',s)
    assert res.get('error') in ('CLIENT_METADATA_FORBIDDEN','INVALID_ARGUMENT'),s
    assert not (enforced[0]/'w8.md').exists()

@pytest.mark.parametrize('args,expect',[
    ({'path':'work/done-tasks/kst-fixture/COLLAB.md'},'kst-fixture'),
    ({'from':'work/kst-fixture','to':'work/done-tasks/kst-fixture'},'kst-fixture'),
])
def test_task_path_done_tasks(enforced,args,expect):
    a=dict(args,declared_actor='Claude Code CLI',declaration_context={k:v for k,v in CTX.items() if k!='task_id'})
    got=d.resolve(a,hvu.hidden())['facts']['task_id']['canonical']
    a['declaration_context']['task_id']=expect
    try:d.resolve(a,hvu.hidden());ok=True
    except d.Denied as e:ok=e.code
    assert got==expect and ok is True

def test_task_case_variant_error_payload(enforced):
    a={'path':'work/kst-fixture/COLLAB.md','declared_actor':'Claude Code CLI','declaration_context':dict(CTX,task_id='KST-Fixture')}
    with pytest.raises(d.Denied) as e:d.resolve(a,hvu.hidden())
    r=e.value.result();print('CASE_VARIANT',r['error'],r['missing_fields'],r['field_example'])
```

Dọn: worktree `kst.gzLh/int` + `kst.gzLh/b357`, branch local `kst/run18-int`, refs `refs/kst/pr357|pr358` trong clone Mac `~/agent-data-test` xoá sau lượt; 0 tiến trình supervisor còn sống; không đụng remote/PR.
