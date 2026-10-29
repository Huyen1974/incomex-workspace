# RUN12 fixture source and results

These are isolated tests, NOT real-client C1. Preserve filenames under `run12/tests/`; sources are under `run12/upstream/`.

## conftest.py

```python
import os,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'upstream'))
os.environ.update(PG_USER_RO='fixture',PG_PASSWORD_RO='fixture')
```

## test_ad.py

```python
import base64,hashlib,json
from pathlib import Path
import pytest
from agent_data import workspace_tools as w, hvu_signals as hvu, declaration_contract as d, workspace_declaration as adapter

@pytest.fixture
def env(tmp_path,monkeypatch):
    root=tmp_path/'root';root.mkdir();state=tmp_path/'state'
    config=tmp_path/'config.json';config.write_text(json.dumps({'state_dir':str(state),'roots':{'fixture':{'path':str(root),'mode':'filesystem','writable':True}},'resources':{}}))
    monkeypatch.setenv('WORKSPACE_CONFIG',str(config));monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
    hvu.bind('credential:fixture');hvu._agent=None
    yield root,state
    hvu.identity.set(None);hvu.agent.set(None);hvu._agent=None

def write(**extra):return dict(root='fixture',path='a.md',content='hello',message='fixture',operation_id='fixture-01',**extra)

@pytest.mark.parametrize('name',sorted(adapter.WRITES|{'workspace_task_start'}))
@pytest.mark.parametrize('value',[None,'',15])
def test_all_source_routes_deny_before_state(env,name,value):
    root,state=env
    args=write(declared_actor=value)
    if name=='workspace_task_start':args={'tool':'workspace_write_new','arguments':write(),'declared_actor':value}
    if name in ('workspace_upload_append','workspace_upload_commit'):
        uid='a'*32;state.mkdir();(state/'uploads').mkdir();(state/'uploads'/f'{uid}.json').write_text('{}');args={'upload_id':uid,'declared_actor':value}
    before={str(p):p.read_bytes() for p in root.parent.rglob('*') if p.is_file()}
    result=w.call(name,args)
    assert result.get('mutation')=='none',result
    after={str(p):p.read_bytes() for p in root.parent.rglob('*') if p.is_file()}
    assert before==after

def test_real_write_retry_actor_swap(env):
    root,state=env;a=write(declared_actor='Codex Worker')
    result=w.call('workspace_write_new',a);assert 'error' not in result,result
    assert (root/'a.md').read_text()=='hello'
    assert result['declaration_receipt']=={'declared_actor':'Codex Worker','authenticated_actor':'credential:fixture'}
    assert w.call('workspace_write_new',a)['replayed'] is True
    swapped=w.call('workspace_write_new',dict(a,declared_actor='Other'))
    assert swapped['error']=='OPERATION_ID_REUSED',swapped
    hvu.bind('credential:other')
    swapped=w.call('workspace_write_new',a);assert swapped['error']=='OPERATION_ID_REUSED'

def test_missing_then_same_id_allowed(env):
    denied=w.call('workspace_write_new',write());assert denied['error']=='DECLARATION_REQUIRED'
    accepted=w.call('workspace_write_new',write(declared_actor='Worker'));assert 'error' not in accepted,accepted

def test_legacy_journal_not_relabelled(env,monkeypatch):
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','advertise')
    old=w.call('workspace_write_new',write());assert 'error' not in old,old
    assert 'declaration_receipt' not in old
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
    result=w.call('workspace_write_new',write(declared_actor='Worker'))
    assert result['error']=='OPERATION_ID_REUSED'

def test_upload_carried_once_and_swaps(env):
    root,state=env;data=b'upload';sha=hashlib.sha256(data).hexdigest()
    first=w.call('workspace_upload_begin',{'root':'fixture','path':'upload.md','message':'fixture','total_bytes':len(data),'sha256':sha,'declared_actor':'Worker'})
    assert 'error' not in first,first
    uid=first['upload_id'];args={'upload_id':uid,'offset':0,'data_base64':base64.b64encode(data).decode(),'sha256':sha}
    assert w.call('workspace_upload_append',dict(args,declared_actor='Other'))['error']=='DECLARATION_ACTOR_MISMATCH'
    assert 'error' not in w.call('workspace_upload_append',args)
    result=w.call('workspace_upload_commit',{'upload_id':uid});assert 'error' not in result,result
    assert result['declaration_receipt']['declared_actor']=='Worker'
    assert (root/'upload.md').read_bytes()==data
    assert w.call('workspace_upload_commit',{'upload_id':uid})['declaration_receipt']==result['declaration_receipt']

def test_schema_and_unknown_writer(env):
    for definition in w.TOOL_SCHEMAS:
        name=definition['name']
        if name in adapter.WRITES|{'workspace_task_start'}:
            assert 'declared_actor' in definition['inputSchema']['properties']
            assert 'DECLARATION_REQUIRED' in definition['description']
            assert 'declared_actor' not in definition['inputSchema'].get('required',[])
        else:assert name in adapter.NON_SOURCE
    assert w.call('workspace_future_write',{})['error']=='UNCLASSIFIED_TOOL'

def test_read_no_declaration(env):
    root,_=env;(root/'read.md').write_text('read works')
    result=w.call('workspace_read',{'root':'fixture','path':'read.md'})
    assert result.get('content')=='read works',result
    assert 'declaration_receipt' not in result

def test_queue_worker_and_legacy(env,monkeypatch):
    from agent_data import workspace_tasks as tasks
    monkeypatch.setattr(tasks,'ensure_supervisor',lambda:None)
    monkeypatch.setattr(tasks.os,'nice',lambda n:0)
    args={'tool':'workspace_write_new','arguments':write(),'operation_id':'queue-01','declared_actor':'Worker'}
    result=w.call('workspace_task_start',args);assert 'error' not in result,result
    q=tasks.queue(w);key=result['task_id'];row=q.get(key,'tasks');request=json.loads(row['request'])
    assert request['_declaration']['declared_actor']=='Worker'
    assert w.call('workspace_task_start',args)['task_id']==key
    assert w.call('workspace_task_start',dict(args,declared_actor='Other'))['error']=='OPERATION_ID_REUSED'
    assert q.claim('tasks','fixture',1)
    tasks.run(key)
    finished=q.status(key,'tasks');assert finished['status']=='completed',finished
    assert finished['result']['declaration_receipt']['declared_actor']=='Worker'
    old=q.enqueue('tasks',{'_hvu':hvu.hidden(),'tool':'workspace_write_new','arguments':dict(write(),path='legacy.md',operation_id='old-01')})
    assert q.claim('tasks','fixture',1)
    tasks.run(old)
    assert q.status(old,'tasks')['result']['error']=='LEGACY_JOB_UNATTRIBUTED'
    assert not (env[0]/'legacy.md').exists()
    assert d.current.get() is None

def test_import_carries_declaration(env,monkeypatch):
    import io,socket,urllib.request
    from types import SimpleNamespace
    monkeypatch.setattr(socket,'getaddrinfo',lambda *a,**k:[(2,1,6,'',('8.8.8.8',443))])
    monkeypatch.setattr(urllib.request,'build_opener',lambda *a:SimpleNamespace(open=lambda *a,**k:io.BytesIO(b'imported')))
    result=w.call('workspace_import_file',{'root':'fixture','path':'import.md','message':'fixture','file':{'file_id':'fixture-file','download_url':'https://files.oaiusercontent.com/fixture'},'declared_actor':'Worker'})
    assert 'error' not in result,result
    assert result['declaration_receipt']['declared_actor']=='Worker'
    assert (env[0]/'import.md').read_text()=='imported'

def test_edit_copy_move_transaction(env):
    root,state=env
    made=w.call('workspace_write_new',write(declared_actor='Worker'));assert 'error' not in made,made
    edit=w.call('workspace_edit',{'root':'fixture','path':'a.md','edits':[{'old_str':'hello','new_str':'changed'}],'expected_version':made['version'],'message':'fixture','declared_actor':'Worker'})
    assert 'error' not in edit,edit
    for name,source,dest in [('workspace_copy','a.md','b.md'),('workspace_move','b.md','c.md')]:
        result=w.call(name,{'root':'fixture','from':source,'to':dest,'expected_version':w.call('workspace_stat',{'root':'fixture','path':source})['version'],'message':'fixture','declared_actor':'Worker'})
        assert 'error' not in result,result
    txn=w.call('workspace_transaction',{'root':'fixture','message':'fixture','operations':[{'op':'create','path':'d.md','content':'txn'}],'declared_actor':'Worker'})
    assert 'error' not in txn,txn
    assert (root/'d.md').read_text()=='txn'
```

## test_contract.py

```python
import pytest
from agent_data import declaration_contract as d
WHO={'label':'credential:test','authenticated':True}
@pytest.mark.parametrize('value',[None,'','  ',42,False,[],{},'bad\nname'])
def test_invalid_actionable(value,monkeypatch):
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
    with pytest.raises(d.Denied) as error:d.resolve({'declared_actor':value},WHO)
    result=error.value.result()
    assert result['error']=='DECLARATION_REQUIRED' and result['mutation']=='none'
    assert result['example']['declared_actor'] and 'repeat' in result['detail']
def test_unknown_credential_never_promoted(monkeypatch):
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
    with pytest.raises(d.Denied,match='trusted'):d.resolve({'declared_actor':'Codex'}, {'label':'clientInfo'})
def test_advertise_preserves_old_payload(monkeypatch):
    monkeypatch.delenv('WORKSPACE_DECLARATION_MODE',raising=False)
    assert d.resolve({},None) is None
    with d.scope(None):assert d.bind_hash({'content':'x'})=={'content':'x'}
def test_swap_and_context_cleanup(monkeypatch):
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
    pair=d.resolve({'declared_actor':' Worker '},WHO)
    assert d.resolve({},WHO,pair)==pair
    for args,who in [({'declared_actor':'Other'},WHO),({},dict(WHO,label='other'))]:
        with pytest.raises(d.Denied):d.resolve(args,who,pair)
    with d.scope(pair):assert d.receipt({'changed':True})['declaration_receipt']==pair
    assert d.current.get() is None
    with d.scope(pair):assert 'declaration_receipt' not in d.receipt({'replayed':True})
def test_single_contract_bytes():
    from pathlib import Path
    root=Path(__file__).parents[1]/'upstream'
    assert len({(root/p).read_bytes() for p in ['shared/declaration_contract.py','agent_data/declaration_contract.py','claude/app/declaration_contract.py','claude/helper/declaration_contract.py']})==1
```

## test_fs.py

```python
import asyncio,json
from types import SimpleNamespace
import pytest
from claude.app import server as s,fsroots as fs,tools,audit,hvu_signals as hvu,declaration_contract as d

@pytest.fixture
def env(tmp_path,monkeypatch):
    root=tmp_path/'files';root.mkdir()
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
    monkeypatch.setenv('FS_ROOTS_JSON',json.dumps({'fixture':{'paths':[str(root)],'mode':'rw','vcs':'none'}}))
    monkeypatch.setattr(fs,'_ROOTS',fs._load_roots())
    monkeypatch.setattr(fs,'_OPS_JOURNAL',str(tmp_path/'ops.jsonl'));monkeypatch.setattr(fs,'_WRITE_LOG',str(tmp_path/'writes.jsonl'));monkeypatch.setattr(fs,'_LOCK_DIR',str(tmp_path))
    monkeypatch.setattr(audit,'_AUDIT_PATH',str(tmp_path/'audit.jsonl'))
    monkeypatch.setattr(tools,'_WRITE_ALLOWLIST',[str(root)])
    monkeypatch.setattr(hvu.Store,'touch',lambda *a,**k:None)
    return root

def call(name,args):return asyncio.run(s._finalize(name,SimpleNamespace(request_id='fixture'),args))
def payload(env,**extra):return dict(root='fixture',path='a.md',content='hello',message='fixture',operation_id='fixture-01',**extra)

@pytest.mark.parametrize('name',sorted(s._DECLARED_WRITES))
@pytest.mark.parametrize('bad',[None,'',42,{},'bad\nname'])
def test_deny_zero_files(env,name,bad):
    before={str(p):p.read_bytes() for p in env.parent.rglob('*') if p.is_file()}
    result=json.loads(call(name,payload(env,declared_actor=bad)))
    assert result['error']=='DECLARATION_REQUIRED'
    assert before=={str(p):p.read_bytes() for p in env.parent.rglob('*') if p.is_file()}

def test_write_retry_and_swap(env):
    args=payload(env,declared_actor='Worker')
    first=call('fs_write',args);assert '[ERROR]' not in first and '[DENIED' not in first,first
    assert (env/'a.md').read_text()=='hello'
    assert 'DECLARATION_RECEIPT' in first and 'Worker' in first
    replay=call('fs_write',args);assert 'DECLARATION_RECEIPT' in replay,replay
    assert 'operation_id_reused' in call('fs_write',dict(args,declared_actor='Other'))
    assert d.current.get() is None

def test_legacy_receipt_not_stamped(env,monkeypatch):
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','advertise')
    old=call('fs_write',payload(env));assert '[DENIED' not in old,old
    assert 'DECLARATION_RECEIPT' not in old
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
    assert 'operation_id_reused' in call('fs_write',payload(env,declared_actor='Worker'))

def test_write_file_real(env):
    result=call('write_file',{'path':str(env/'direct.md'),'content':'direct','declared_actor':'Worker'})
    assert '[DENIED' not in result,result
    assert (env/'direct.md').read_text()=='direct'
    assert 'DECLARATION_RECEIPT' in result

def test_schema(env):
    definitions=asyncio.run(s.mcp.list_tools())
    for definition in definitions:
        if definition.name in s._DECLARED_WRITES:
            assert 'declared_actor' in definition.inputSchema['properties']
            assert 'DECLARATION_REQUIRED' in definition.description
            assert 'declared_actor' not in definition.inputSchema.get('required',[])

def test_read_unchanged(env):
    (env/'read.md').write_text('read works')
    result=call('fs_read',{'root':'fixture','path':'read.md'})
    assert 'read works' in result and 'DECLARATION_RECEIPT' not in result,result

def test_unknown_writer_fail_closed(env):
    result=json.loads(call('fs_future_write',{}));assert result['error']=='UNCLASSIFIED_TOOL'

def test_edit_copy_move_and_atomic_transaction(env,monkeypatch):
    args=payload(env,declared_actor='Worker');assert '[DENIED' not in call('fs_write',args)
    # The existing version is the first 16 SHA256 digits, as returned by fs_stat.
    import hashlib
    version=hashlib.sha256(b'hello').hexdigest()[:16]
    result=call('fs_edit',{'root':'fixture','path':'a.md','edits':[{'old_str':'hello','new_str':'changed'}],'expected_version':version,'message':'fixture','declared_actor':'Worker'})
    assert '[DENIED' not in result and '[ERROR]' not in result,result
    fs._ROOTS['fixture']['vcs']='git-local'
    monkeypatch.setattr(fs.hostq,'configured',lambda:True)
    monkeypatch.setattr(fs.hostq,'request',lambda *a,**k:{'commit':'fixture-local-only'})
    for name,source,dest in [('fs_copy','a.md','b.md'),('fs_move','b.md','c.md')]:
        result=call(name,{'root':'fixture','from':source,'to':dest,'message':'fixture','declared_actor':'Worker'})
        assert '[DENIED' not in result and '[ERROR]' not in result,result
    result=call('fs_transaction',{'root':'fixture','ops':[{'op':'write','path':'txn.md','content':'txn'}],'message':'fixture','declared_actor':'Worker'})
    assert '[DENIED' not in result and '[ERROR]' not in result,result
    assert (env/'txn.md').read_text()=='txn'
    denied=call('fs_transaction',{'root':'fixture','ops':[{'op':'write','path':'partial.md','content':'partial'},{'op':'edit','path':'missing.md','edits':[]}],'message':'fixture','declared_actor':'Worker'})
    assert '[DENIED' in denied and not (env/'partial.md').exists(),denied

def test_restore_uses_same_gate_before_helper(env,monkeypatch):
    invoked=[]
    monkeypatch.setattr(fs,'_transaction_restore',lambda *a:invoked.append(a) or {'text':'fixture restore'})
    args={'root':'fixture','ops':[{'op':'restore','version':'a'*40}],'message':'fixture'}
    assert json.loads(call('fs_transaction',args))['error']=='DECLARATION_REQUIRED' and not invoked
    result=call('fs_transaction',dict(args,declared_actor='Worker'))
    assert 'DECLARATION_RECEIPT' in result and len(invoked)==1,result
```

## test_helper.py

```python
import importlib,sys,json,time
from pathlib import Path
import pytest

@pytest.fixture
def helper(tmp_path,monkeypatch):
    for name in ('in','out','done'):(tmp_path/name).mkdir()
    monkeypatch.setenv('MCP_HELPER_QUEUE',str(tmp_path));monkeypatch.setenv('MCP_HELPER_ROOTS_JSON','{}');monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
    monkeypatch.syspath_prepend(str(Path(__file__).parents[1]/'upstream/claude/helper'))
    import mcp_host_helper as h
    monkeypatch.setattr(h,'Q_IN',str(tmp_path/'in'));monkeypatch.setattr(h,'Q_OUT',str(tmp_path/'out'));monkeypatch.setattr(h,'Q_DONE',str(tmp_path/'done'))
    called=[]
    def action(*args):called.append(args);return {'changed':True}
    for name in ('gh_put_commit_push','gh_apply_commit_push','gh_move','gh_revert_commit_push','ui_commit','ui_move'):
        monkeypatch.setattr(h,'act_'+name,action)
    return h,tmp_path,called

def send(h,base,action,args):
    uid='a'*32
    (base/'in'/f'{uid}.json').write_text(json.dumps({'v':1,'id':uid,'action':action,'args':args,'deadline':time.time()+20}))
    h.handle(uid+'.json')
    return json.loads((base/'out'/f'{uid}.json').read_text())

@pytest.mark.parametrize('action',['gh_put_commit_push','gh_apply_commit_push','gh_move','gh_revert_commit_push','ui_commit','ui_move'])
def test_helper_gate_and_carry(helper,action):
    h,base,called=helper
    who={'label':'credential:fixture','gateway':'claude','surface_key':'fixture'}
    result=send(h,base,action,{'_hvu':who})
    assert result['reason']=='LEGACY_JOB_UNATTRIBUTED' and not called
    pair={'declared_actor':'Worker','authenticated_actor':'credential:fixture'}
    result=send(h,base,action,{'_hvu':who,'_declaration':pair})
    assert result['ok'] and result['declaration_receipt']==pair and len(called)==1
    assert h.declaration.current.get() is None
    result=send(h,base,action,{'_hvu':dict(who,label='Other'),'_declaration':pair})
    assert result['reason']=='DECLARATION_ACTOR_MISMATCH' and len(called)==1
    result=send(h,base,action,{'_declaration':pair})
    assert result['reason']=='AUTHENTICATED_ACTOR_REQUIRED' and len(called)==1

def test_hostq_carries_ui_before_enqueue(tmp_path,monkeypatch):
    from claude.app import hostq as q, declaration_contract as d,hvu_signals as hvu
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
    inside=tmp_path/'in';outside=tmp_path/'out';inside.mkdir();outside.mkdir()
    monkeypatch.setattr(q,'_QUEUE_IN',str(inside));monkeypatch.setattr(q,'_QUEUE_OUT',str(outside));monkeypatch.setattr(q,'alive',lambda:{'state':'idle'})
    who={'label':'credential:fixture','gateway':'claude','surface_key':'fixture'}
    hvu.identity.set(who)
    with pytest.raises(q.HelperError):q.request('ui_commit',{},wait_s=1)
    assert not list(inside.iterdir())
    uid='b'*32;(outside/(uid+'.json')).write_text('{"ok":true}')
    pair={'declared_actor':'Worker','authenticated_actor':who['label']}
    with d.scope(pair):assert q.request('ui_commit',{'path':'fixture.md'},wait_s=1,rid=uid)['ok']
    envelope=json.loads((inside/(uid+'.json')).read_text())
    assert envelope['args']['_declaration']==pair and envelope['args']['_hvu']==who
    hvu.identity.set(None)
```

## test_packaging.py

```python
from pathlib import Path
import hashlib,subprocess,tempfile,shutil

def test_baseline_pins():
    root=Path(__file__).parents[1]/'baseline'
    pins={'agent_data/workspace_tools.py':'d3f22b9285f5e7a2b14cb737c7cb1cb6d3f16640a3c412bfcc53c7016c6ec55b',
          'claude/app/server.py':'422dd29578daac04d626509c556a6f981d90665d0ae598d4499eb5703faa28d9',
          'claude/helper/mcp_host_helper.py':'e5790c74edbb24575c5015982953d98aa8165657574b4782df18a49382710f11'}
    for p,sha in pins.items():assert hashlib.sha256((root/p).read_bytes()).hexdigest()==sha

def test_reverse_patch_restores_every_baseline_byte(tmp_path):
    root=Path(__file__).parents[1]/'upstream'
    baseline='9e1935f'
    diff=subprocess.check_output(['git','-C',str(root),'diff','--binary',baseline])
    # Tracked runtime files only; added contract modules are removed by rollback packaging.
    paths=subprocess.check_output(['git','-C',str(root),'ls-tree','-r','--name-only',baseline],text=True).splitlines()
    candidate_paths=subprocess.check_output(['git','-C',str(root),'ls-files'],text=True).splitlines()
    for p in candidate_paths:
        target=tmp_path/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((root/p).read_bytes())
    subprocess.run(['git','apply','--reverse','--unsafe-paths','-'],input=diff,cwd=tmp_path,check=True)
    for p in paths:
        before=subprocess.check_output(['git','-C',str(root),'show',baseline+':'+p])
        assert (tmp_path/p).read_bytes()==before
    assert not any((tmp_path/p).exists() for p in set(candidate_paths)-set(paths))
```

## Observed run

```text
........................................................................ [ 73%]
..........................                                               [100%]
=============================== warnings summary ===============================
run12/venv/lib/python3.11/site-packages/pydantic_settings/sources/utils.py:51
  /Users/nmhuyen/Documents/Codex/2026-10-25/x-l-cho-t-i/run12/venv/lib/python3.11/site-packages/pydantic_settings/sources/utils.py:51: IncompleteFieldDefinitionWarning: Field 'lifespan' has an incomplete definition: its annotation contains an unresolved forward reference, so settings sources may fail to correctly resolve its value. Call `model_rebuild()` on the model where the field is defined, once all the referenced types are defined.
    warnings.warn(  # noqa: B028  (called from many sources at differing depths, so no stacklevel is correct)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
98 passed, 1 warning in 1.05s
```
