# Reproducible Mac test fixtures

These files are evidence, not runtime changes and not additional PR files. Extract into a temporary tests directory; set HJW_TEST_SOURCE to the candidate source tree. Python 3.11 + pytest/jsonschema and existing application dependencies. All state/data are temporary and fake. The import-download test stubs network I/O. No production endpoint called.

Run `python -m pytest <tests> -q`; for the main-based source exclude `test_runtime_queue.py` because main deliberately does not contain PR357. Runtime suite includes it. Supervisor and nice calls are stubbed; queue claims, actual file handlers and receipts run in-process. Thus 4 running/6 queued is a controlled SQLite scheduler proof, not four OS-worker performance measurement.

## conftest.py

```python
import os,sys
sys.path.insert(0,os.environ['HJW_TEST_SOURCE'])
```

## test_acl.py

```python
from test_ad import env,write
from agent_data import workspace_tools as w,hvu_signals as hvu,workspace_declaration as d

def test_declaration_does_not_grant_hermes_tools_or_paths(env,monkeypatch):
    hvu.agent.set('hermes')
    monkeypatch.setattr(w,'agent_profiles',lambda:{'hermes':{'tools':frozenset({'workspace_read','workspace_edit'}),'roots':frozenset({'fixture'}),'read':{'fixture':['']},'write':{'fixture':['work/allowed']}}})
    a=write(declared_actor='Owner Root',declaration_context={'origin_environment':'vps','task_id':'fixture','command_ref':'RUN-OWNER'})
    assert w.call('workspace_write_new',a)['error']=='TOOL_NOT_ALLOWED'
    assert w.call('workspace_edit',dict(a,path='work/other/a.md',edits=[]))['error']=='SCOPE_DENIED'
    assert w.call('workspace_task_start',{'tool':'workspace_write_new','arguments':a})['error']=='TOOL_NOT_ALLOWED'
    assert not list(env[0].iterdir())

def test_existing_infra_classification_is_non_source():
    for name in ('infra_graph','infra_logs','infra_ops_plan'):assert d.target(name,{}) is False
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
    root,state=env;a=write(declared_actor='Codex Worker',declaration_context={'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN-FIXTURE'})
    result=w.call('workspace_write_new',a);assert 'error' not in result,result
    assert (root/'a.md').read_text()=='hello'
    assert result['declaration_receipt']['facts']['declared_actor']['raw']=='Codex Worker'
    assert w.call('workspace_write_new',a)['replayed'] is True
    swapped=w.call('workspace_write_new',dict(a,declared_actor='Other'))
    assert swapped['error']=='OPERATION_ID_REUSED',swapped
    hvu.bind('credential:other')
    swapped=w.call('workspace_write_new',a);assert swapped['error']=='OPERATION_ID_REUSED'

def test_missing_then_same_id_allowed(env):
    denied=w.call('workspace_write_new',write());assert denied['error']=='DECLARATION_REQUIRED'
    accepted=w.call('workspace_write_new',write(declared_actor='Worker',declaration_context={'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN-FIXTURE'}));assert 'error' not in accepted,accepted

def test_legacy_journal_not_relabelled(env,monkeypatch):
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','advertise')
    old=w.call('workspace_write_new',write());assert 'error' not in old,old
    assert 'declaration_receipt' not in old
    monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
    result=w.call('workspace_write_new',write(declared_actor='Worker',declaration_context={'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN-FIXTURE'}))
    assert result['error']=='OPERATION_ID_REUSED'

def test_upload_carried_once_and_swaps(env):
    root,state=env;data=b'upload';sha=hashlib.sha256(data).hexdigest()
    first=w.call('workspace_upload_begin',{'root':'fixture','path':'upload.md','message':'fixture','total_bytes':len(data),'sha256':sha,'declared_actor':'Worker','declaration_context':{'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN-FIXTURE'}})
    assert 'error' not in first,first
    uid=first['upload_id'];args={'upload_id':uid,'offset':0,'data_base64':base64.b64encode(data).decode(),'sha256':sha}
    assert w.call('workspace_upload_append',dict(args,declared_actor='Other'))['error']=='DECLARATION_ACTOR_MISMATCH'
    assert 'error' not in w.call('workspace_upload_append',args)
    result=w.call('workspace_upload_commit',{'upload_id':uid});assert 'error' not in result,result
    assert result['declaration_receipt']['declared_actor']=='worker'
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
    args={'tool':'workspace_write_new','arguments':write(),'operation_id':'queue-01','declared_actor':'Worker','declaration_context':{'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN-FIXTURE'}}
    result=w.call('workspace_task_start',args);assert 'error' not in result,result
    q=tasks.queue(w);key=result['task_id'];row=q.get(key,'tasks');request=json.loads(row['request'])
    assert request['_declaration']['declared_actor']=='worker'
    assert w.call('workspace_task_start',args)['task_id']==key
    assert w.call('workspace_task_start',dict(args,declared_actor='Other'))['error']=='OPERATION_ID_REUSED'
    assert q.claim('tasks','fixture',1)
    tasks.run(key)
    finished=q.status(key,'tasks');assert finished['status']=='completed',finished
    assert finished['result']['declaration_receipt']['declared_actor']=='worker'
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
    result=w.call('workspace_import_file',{'root':'fixture','path':'import.md','message':'fixture','file':{'file_id':'fixture-file','download_url':'https://files.oaiusercontent.com/fixture'},'declared_actor':'Worker','declaration_context':{'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN-FIXTURE'}})
    assert 'error' not in result,result
    assert result['declaration_receipt']['declared_actor']=='worker'
    assert (env[0]/'import.md').read_text()=='imported'

def test_edit_copy_move_transaction(env):
    root,state=env
    made=w.call('workspace_write_new',write(declared_actor='Worker',declaration_context={'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN-FIXTURE'}));assert 'error' not in made,made
    edit=w.call('workspace_edit',{'root':'fixture','path':'a.md','edits':[{'old_str':'hello','new_str':'changed'}],'expected_version':made['version'],'message':'fixture','declared_actor':'Worker','declaration_context':{'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN-FIXTURE'}})
    assert 'error' not in edit,edit
    for name,source,dest in [('workspace_copy','a.md','b.md'),('workspace_move','b.md','c.md')]:
        result=w.call(name,{'root':'fixture','from':source,'to':dest,'expected_version':w.call('workspace_stat',{'root':'fixture','path':source})['version'],'message':'fixture','declared_actor':'Worker','declaration_context':{'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN-FIXTURE'}})
        assert 'error' not in result,result
    txn=w.call('workspace_transaction',{'root':'fixture','message':'fixture','operations':[{'op':'create','path':'d.md','content':'txn'}],'declared_actor':'Worker','declaration_context':{'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN-FIXTURE'}})
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
    pair=d.resolve({'declared_actor':' Worker ','declaration_context':{'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN-FIXTURE'}},WHO)
    assert d.resolve({},WHO,pair)==pair
    for args,who in [({'declared_actor':'Other'},WHO),({},dict(WHO,label='other'))]:
        with pytest.raises(d.Denied):d.resolve(args,who,pair)
    with d.scope(pair):assert d.receipt({'changed':True})['declaration_receipt']==pair
    assert d.current.get() is None
    with d.scope(pair):assert 'declaration_receipt' not in d.receipt({'replayed':True})
```

## test_four_facts.py

```python
import asyncio, json
import pytest
from agent_data import declaration_contract as d
WHO={'authenticated':True,'label':'shared-gpt'}
CTX={'origin_environment':'Macbok','task_id':'fixture','command_ref':'HJW-DECLARATION-GATE-FOUR-FACTS-20261029-14'}
def args(**extra):return dict(declared_actor='GPT Live', declaration_context=dict(CTX), **extra)
@pytest.fixture(autouse=True)
def mode(monkeypatch):monkeypatch.setenv('WORKSPACE_DECLARATION_MODE','enforce')
@pytest.mark.parametrize('name',['GPT Live','gpt_live','gptlive','ＧＰＴ　Ｌｉｖｅ'])
def test_alias(name):
    a=args();a['declared_actor']=name;v=d.resolve(a,WHO)
    assert v['declared_actor']=='gpt-live' and v['facts']['declared_actor']['raw']==name
    assert v['facts']['origin_environment']['canonical']=='macbook'
    assert v['command_kind']=='RUN'
@pytest.mark.parametrize('bad',[None,'',33,{},[],True,'x\nname','x\x00name','x'*129,'../Owner','\u200b'])
def test_bad_product(bad):
    a=args();a['declared_actor']=bad
    with pytest.raises(d.Denied) as e:d.resolve(a,WHO)
    assert e.value.result()['mutation']=='none'
def test_unknown_valid_name():
    a=args();a['declared_actor']='New AI 2030';v=d.resolve(a,WHO)
    assert v['declared_actor']=='new-ai-2030' and v['flags']==['UNREGISTERED_ALIAS']
@pytest.mark.parametrize('field',['declared_actor','origin_environment','task_id','command_ref'])
def test_missing_field(field):
    a=args()
    if field=='declared_actor':a.pop(field)
    else:a['declaration_context'].pop(field)
    with pytest.raises(d.Denied) as e:d.resolve(a,WHO)
    assert e.value.result()['missing_fields']==[field]
@pytest.mark.parametrize('env',['Mac Book','macos','mac','macbook','macbok','CLOUD','vps'])
def test_environment(env):
    a=args();a['declaration_context']['origin_environment']=env
    assert d.resolve(a,WHO)['facts']['origin_environment']['canonical'] in ('macbook','cloud','vps')
def test_shared_credential_not_environment():
    a=args();a['declaration_context'].pop('origin_environment')
    with pytest.raises(d.Denied) as e:d.resolve(a,dict(WHO,gateway='vps'))
    assert 'origin_environment' in e.value.fields
def test_task_derive_and_conflict():
    a=args(path='work/fixture/COLLAB.md');a['declaration_context'].pop('task_id')
    v=d.resolve(a,WHO);assert v['facts']['task_id']['canonical']=='fixture' and v['facts']['task_id']['provenance']=='derived'
    a['declaration_context']['task_id']='fixtur'
    with pytest.raises(d.Denied):d.resolve(a,WHO)
def test_multitask_and_traversal():
    with pytest.raises(d.Denied):d.resolve(args(operations=[{'path':'work/a/file'},{'path':'work/b/file'}]),WHO)
    a=args();a['declaration_context']['task_id']='../other'
    with pytest.raises(d.Denied):d.resolve(a,WHO)
def test_verified_context_conflict():
    with pytest.raises(d.Denied):d.resolve(args(),WHO,verified={'command_ref':'OTHER-RUN'})
def test_ad_hoc_not_run():
    a=args(operation_id='real-operation');a['declaration_context'].pop('command_ref')
    v=d.resolve(a,WHO);assert v['command_kind']=='ad-hoc' and v['facts']['command_ref']['canonical']=='real-operation'
def test_alias_upgrade_replay_hash(monkeypatch):
    a=args();a['declared_actor']='gptlive';old=d.resolve(a,WHO)
    with d.scope(old):h=d.bind_hash(a)
    monkeypatch.setitem(d.ALIASES,'gptlive','new-canonical')
    with d.scope(d.resolve(a,WHO)):assert d.bind_hash(a)==h
    assert d.resolve({},WHO,old)==old
@pytest.mark.parametrize('field',['origin_environment','task_id','command_ref'])
def test_carried_cannot_swap(field):
    old=d.resolve(args(),WHO)
    with pytest.raises(d.Denied):d.resolve({'declaration_context':{field:'other'}},WHO,old)
def test_forged_metadata_dispatch(tmp_path,monkeypatch):
    from agent_data import workspace_tools as w,hvu_signals as hvu
    hvu.bind('credential:fixture');hvu._agent=None
    r=w.call('workspace_write_new',dict(args(),_hvu={'label':'Owner'}))
    assert r['error']=='CLIENT_METADATA_FORBIDDEN'
    hvu.identity.set(None)
```

## test_runtime_queue.py

```python
import json
from test_ad import env,write
from agent_data import workspace_tools as w,workspace_tasks as tasks,hvu_signals as hvu

def test_ten_requests_four_active_six_queued_finish_and_replay(env,monkeypatch):
    monkeypatch.setattr(tasks,'ensure_supervisor',lambda:None)
    monkeypatch.setattr(tasks.os,'nice',lambda n:0)
    q=tasks.queue(w)
    assert hasattr(q,'enqueue_once'), 'This integration suite targets PR357/runtime, not pre-queue GH main'
    args=[];keys=[]
    for i in range(10):
        a={'tool':'workspace_write_new','arguments':dict(write(),path=f'{i}.md',operation_id=f'inner-{i}'),'operation_id':f'queue-{i}','declared_actor':'New AI Worker','declaration_context':{'origin_environment':'macbook','task_id':'fixture','command_ref':'RUN17-LAB'}}
        r=w.call('workspace_task_start',a);assert 'error' not in r,r
        args.append(a);keys.append(r['task_id'])
    claimed=[q.claim('tasks','mac-fixture',4) for _ in range(4)]
    assert all(claimed) and q.claim('tasks','mac-fixture',4) is None
    with q.db() as db:counts=dict(db.execute('select status,count(*) from jobs group by status').fetchall())
    assert counts=={'queued':6,'running':4},counts
    for r in claimed:tasks.run(r['id'])
    while (r:=q.claim('tasks','mac-fixture',4)) is not None:tasks.run(r['id'])
    for i,key in enumerate(keys):
        r=q.status(key,'tasks');assert r['status']=='completed',r
        assert r['result']['declaration_receipt']['facts']['command_ref']['canonical']=='RUN17-LAB'
        hvu.bind('credential:fixture');hvu._agent=None
        replay=w.call('workspace_task_start',args[i]);assert replay['task_id']==key and replay['replayed']
    with q.db() as db:assert db.execute('select count(*) from jobs').fetchone()[0]==10
    assert len(list(env[0].glob('*.md')))==10
    changed=dict(args[0],declared_actor='Other');assert w.call('workspace_task_start',changed)['error']=='OPERATION_ID_REUSED'
    print('QUEUE10: accepted=10 active=4 queued=6 completed=10 replay=10 duplicate_jobs=0')
```
