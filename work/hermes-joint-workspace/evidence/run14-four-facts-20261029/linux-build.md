# RUN14 Linux HTTP and build evidence

Both actual candidate images passed real loopback HTTP tools/list, tools/call, isError on missing declaration with zero target mutation, four-fact write/receipt, replay, and changed-facts conflict. Containers had network=none, no production data mounts, no published ports, read-only root filesystem and bounded tmpfs/RAM/CPU.

AD HTTP lifespan was OFF to exclude external services/supervisor; FS lifespan ON. No production commit, full production startup, active-client refresh, cold AI or production rollback is claimed. Initial lab failures (tokenizer cache absent, wrong import working directory, legacy fake credential) were corrected in the fixture without changing production. Public tokenizer cache was reused; no real credentials copied.

## Actual image HTTP results
```json
{"kind": "ad", "platform": "linux", "http_schema": true, "missing_isError": true, "zero_mutation": true, "write_receipt": {"content": [{"type": "text", "text": "{\"changed\": true, \"version\": \"5f05ed16a6e753257459547ff4c3f5e83b6abf20c82fbe283000ff2bd0587ee2\", \"commit\": null, \"pushed\": false, \"diff\": [{\"created\": true, \"bytes\": 23}], \"backup_id\": \"3fd729cb9de64f04a47808275476449a\", \"warnings\": [], \"declaration_receipt\": {\"contract_version\": \"four-facts-1\", \"normalizer_version\": \"four-facts-1\", \"alias_version\": \"1\", \"declared_actor\": \"gpt-live\", \"authenticated_actor\": \"OpenAI/Codex fixture\", \"facts\": {\"declared_actor\": {\"raw\": \"GPT Live\", \"canonical\": \"gpt-live\", \"provenance\": \"self_declared\"}, \"origin_environment\": {\"raw\": \"macbok\", \"canonical\": \"macbook\", \"provenance\": \"self_declared\"}, \"task_id\": {\"raw\": \"fixture\", \"canonical\": \"fixture\", \"provenance\": \"self_declared\"}, \"command_ref\": {\"raw\": \"RUN-HTTP-FIXTURE\", \"canonical\": \"RUN-HTTP-FIXTURE\", \"provenance\": \"self_declared\"}}, \"command_kind\": \"RUN\", \"flags\": []}, \"operation_id\": \"linux-http-01\"}"}], "isError": false}, "replay": {"content": [{"type": "text", "text": "{\"changed\": true, \"version\": \"5f05ed16a6e753257459547ff4c3f5e83b6abf20c82fbe283000ff2bd0587ee2\", \"commit\": null, \"pushed\": false, \"diff\": [{\"created\": true, \"bytes\": 23}], \"backup_id\": \"3fd729cb9de64f04a47808275476449a\", \"warnings\": [], \"declaration_receipt\": {\"contract_version\": \"four-facts-1\", \"normalizer_version\": \"four-facts-1\", \"alias_version\": \"1\", \"declared_actor\": \"gpt-live\", \"authenticated_actor\": \"OpenAI/Codex fixture\", \"facts\": {\"declared_actor\": {\"raw\": \"GPT Live\", \"canonical\": \"gpt-live\", \"provenance\": \"self_declared\"}, \"origin_environment\": {\"raw\": \"macbok\", \"canonical\": \"macbook\", \"provenance\": \"self_declared\"}, \"task_id\": {\"raw\": \"fixture\", \"canonical\": \"fixture\", \"provenance\": \"self_declared\"}, \"command_ref\": {\"raw\": \"RUN-HTTP-FIXTURE\", \"canonical\": \"RUN-HTTP-FIXTURE\", \"provenance\": \"self_declared\"}}, \"command_kind\": \"RUN\", \"flags\": []}, \"replayed\": true, \"operation_id\": \"linux-http-01\", \"first_performed_at\": \"2026-10-29T07:41:21Z\"}"}], "isError": false}, "changed_facts_conflict": true, "lifespan": "off (external services excluded)"}
{"kind": "fs", "platform": "linux", "http_schema": true, "missing_isError": true, "zero_mutation": true, "write_receipt": {"content": [{"type": "text", "text": "OK fs_write root=fixture path=canary.md tạo mới 23B · operation_id=linux-http-01\nversion: - -> 5f05ed16a6e75325 · commit=- · gốc này không có sổ git\nDECLARATION_RECEIPT {\"alias_version\": \"1\", \"authenticated_actor\": \"Anthropic/ClaudeAI [auth:claude-chat]\", \"command_kind\": \"RUN\", \"contract_version\": \"four-facts-1\", \"declared_actor\": \"gpt-live\", \"facts\": {\"command_ref\": {\"canonical\": \"RUN-HTTP-FIXTURE\", \"provenance\": \"self_declared\", \"raw\": \"RUN-HTTP-FIXTURE\"}, \"declared_actor\": {\"canonical\": \"gpt-live\", \"provenance\": \"self_declared\", \"raw\": \"GPT Live\"}, \"origin_environment\": {\"canonical\": \"macbook\", \"provenance\": \"self_declared\", \"raw\": \"macbok\"}, \"task_id\": {\"canonical\": \"fixture\", \"provenance\": \"self_declared\", \"raw\": \"fixture\"}}, \"flags\": [], \"normalizer_version\": \"four-facts-1\"}"}], "structuredContent": {"result": "OK fs_write root=fixture path=canary.md tạo mới 23B · operation_id=linux-http-01\nversion: - -> 5f05ed16a6e75325 · commit=- · gốc này không có sổ git\nDECLARATION_RECEIPT {\"alias_version\": \"1\", \"authenticated_actor\": \"Anthropic/ClaudeAI [auth:claude-chat]\", \"command_kind\": \"RUN\", \"contract_version\": \"four-facts-1\", \"declared_actor\": \"gpt-live\", \"facts\": {\"command_ref\": {\"canonical\": \"RUN-HTTP-FIXTURE\", \"provenance\": \"self_declared\", \"raw\": \"RUN-HTTP-FIXTURE\"}, \"declared_actor\": {\"canonical\": \"gpt-live\", \"provenance\": \"self_declared\", \"raw\": \"GPT Live\"}, \"origin_environment\": {\"canonical\": \"macbook\", \"provenance\": \"self_declared\", \"raw\": \"macbok\"}, \"task_id\": {\"canonical\": \"fixture\", \"provenance\": \"self_declared\", \"raw\": \"fixture\"}}, \"flags\": [], \"normalizer_version\": \"four-facts-1\"}"}, "isError": false}, "replay": {"content": [{"type": "text", "text": "[REPLAY operation_id=linux-http-01 — thao tác này ĐÃ thực hiện lúc 2026-10-29T07:41:27Z; không làm lại, trả kết quả đã ghi]\nOK fs_write root=fixture path=canary.md tạo mới 23B · operation_id=linux-http-01\nversion: - -> 5f05ed16a6e75325 · commit=- · gốc này không có sổ git\nDECLARATION_RECEIPT {\"alias_version\": \"1\", \"authenticated_actor\": \"Anthropic/ClaudeAI [auth:claude-chat]\", \"command_kind\": \"RUN\", \"contract_version\": \"four-facts-1\", \"declared_actor\": \"gpt-live\", \"facts\": {\"command_ref\": {\"canonical\": \"RUN-HTTP-FIXTURE\", \"provenance\": \"self_declared\", \"raw\": \"RUN-HTTP-FIXTURE\"}, \"declared_actor\": {\"canonical\": \"gpt-live\", \"provenance\": \"self_declared\", \"raw\": \"GPT Live\"}, \"origin_environment\": {\"canonical\": \"macbook\", \"provenance\": \"self_declared\", \"raw\": \"macbok\"}, \"task_id\": {\"canonical\": \"fixture\", \"provenance\": \"self_declared\", \"raw\": \"fixture\"}}, \"flags\": [], \"normalizer_version\": \"four-facts-1\"}"}], "structuredContent": {"result": "[REPLAY operation_id=linux-http-01 — thao tác này ĐÃ thực hiện lúc 2026-10-29T07:41:27Z; không làm lại, trả kết quả đã ghi]\nOK fs_write root=fixture path=canary.md tạo mới 23B · operation_id=linux-http-01\nversion: - -> 5f05ed16a6e75325 · commit=- · gốc này không có sổ git\nDECLARATION_RECEIPT {\"alias_version\": \"1\", \"authenticated_actor\": \"Anthropic/ClaudeAI [auth:claude-chat]\", \"command_kind\": \"RUN\", \"contract_version\": \"four-facts-1\", \"declared_actor\": \"gpt-live\", \"facts\": {\"command_ref\": {\"canonical\": \"RUN-HTTP-FIXTURE\", \"provenance\": \"self_declared\", \"raw\": \"RUN-HTTP-FIXTURE\"}, \"declared_actor\": {\"canonical\": \"gpt-live\", \"provenance\": \"self_declared\", \"raw\": \"GPT Live\"}, \"origin_environment\": {\"canonical\": \"macbook\", \"provenance\": \"self_declared\", \"raw\": \"macbok\"}, \"task_id\": {\"canonical\": \"fixture\", \"provenance\": \"self_declared\", \"raw\": \"fixture\"}}, \"flags\": [], \"normalizer_version\": \"four-facts-1\"}"}, "isError": false}, "changed_facts_conflict": true, "lifespan": "on"}
```

## Build
```text
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            BuildKit is currently disabled; enable it by removing the DOCKER_BUILDKIT=0
            environment-variable.

Sending build context to Docker daemon  1.175MB

Step 1/5 : ARG BASE=sha256:46e0ba15f18f2c4241a6a704eaa7c3f209432453a78e04dff626187ec1f50c8c
Step 2/5 : FROM ${BASE}
 ---> 46e0ba15f18f
Step 3/5 : COPY upstream/agent_data/ /app/agent_data/
 ---> 892d8e422864
Step 4/5 : ENV WORKSPACE_DECLARATION_MODE=advertise
 ---> Running in f87037e704ae
 ---> Removed intermediate container f87037e704ae
 ---> 171fac1795a4
Step 5/5 : LABEL incomex.candidate.run=HJW-DECLARATION-GATE-FOUR-FACTS-20261029-14
 ---> Running in 35f4f396b1ad
 ---> Removed intermediate container 35f4f396b1ad
 ---> cda9d67a5a51
Successfully built cda9d67a5a51
Successfully tagged hjw-run14-ad:candidate
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            BuildKit is currently disabled; enable it by removing the DOCKER_BUILDKIT=0
            environment-variable.

Sending build context to Docker daemon  1.175MB

Step 1/5 : ARG BASE=sha256:bacd21605a06825d0a725bcaefecdf55abbe85e075ab7be8fe93da3e04b5f961
Step 2/5 : FROM ${BASE}
 ---> bacd21605a06
Step 3/5 : COPY upstream/claude/app/ /app/app/
 ---> 98a5602edcd8
Step 4/5 : ENV WORKSPACE_DECLARATION_MODE=advertise
 ---> Running in 2a42d0c60913
 ---> Removed intermediate container 2a42d0c60913
 ---> d4231182eddc
Step 5/5 : LABEL incomex.candidate.run=HJW-DECLARATION-GATE-FOUR-FACTS-20261029-14
 ---> Running in 7afc19f42985
 ---> Removed intermediate container 7afc19f42985
 ---> ae6f4f720429
Successfully built ae6f4f720429
Successfully tagged hjw-run14-fs:candidate
```

## Dockerfile.ad
```text
ARG BASE=sha256:46e0ba15f18f2c4241a6a704eaa7c3f209432453a78e04dff626187ec1f50c8c
FROM ${BASE}
COPY upstream/agent_data/ /app/agent_data/
ENV WORKSPACE_DECLARATION_MODE=advertise
LABEL incomex.candidate.run=HJW-DECLARATION-GATE-FOUR-FACTS-20261029-14
```

## Dockerfile.fs
```text
ARG BASE=sha256:bacd21605a06825d0a725bcaefecdf55abbe85e075ab7be8fe93da3e04b5f961
FROM ${BASE}
COPY upstream/claude/app/ /app/app/
ENV WORKSPACE_DECLARATION_MODE=advertise
LABEL incomex.candidate.run=HJW-DECLARATION-GATE-FOUR-FACTS-20261029-14
```

## .dockerignore
```text
**
!Dockerfile.ad
!Dockerfile.fs
!upstream/
!upstream/agent_data/
!upstream/agent_data/*.py
!upstream/claude/
!upstream/claude/app/
!upstream/claude/app/*.py
```

## http_probe.py
```text
"""Bounded offline real HTTP probe; launched inside no-network container."""
import json, os, pathlib, socket, subprocess, sys, tempfile, time
import httpx
kind=sys.argv[1]
base=pathlib.Path(tempfile.mkdtemp(prefix='fourfacts-'))
files=base/'files';files.mkdir()
# Lab credential environment setup omitted: only synthetic fixture values were used; no production credentials.
if kind=='fs':
    os.environ['FS_ROOTS_JSON']=json.dumps({'fixture':{'paths':[str(files)],'mode':'rw','vcs':'none'}})
    module=os.environ.get('PROBE_FS_MODULE','claude.app.server:app')
else:
    config=base/'workspace.json'
    config.write_text(json.dumps({'state_dir':str(base/'state'),'roots':{'fixture':{'path':str(files),'mode':'filesystem','writable':True}},'resources':{},'master_profiles':{'fixture':{'enabled':True,'credential_env':'LAB_PROFILE_KEY','label':'OpenAI/Codex fixture'}}}))
    os.environ['WORKSPACE_CONFIG']=str(config);module='agent_data.server:app'
# No externally reachable listener: isolated container loopback only.
with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
log=open(base/'server.log','w+')
p=subprocess.Popen([sys.executable,'-m','uvicorn',module,'--host','127.0.0.1','--port',str(port),'--lifespan','on' if kind=='fs' else 'off'],stdout=log,stderr=log)
try:
    url=f'http://127.0.0.1:{port}/mcp'
    c=httpx.Client(timeout=10,headers={'Accept':'application/json, text/event-stream','X-API-Key':'fixture-only-not-a-real-secret-000000000000','Authorization':'Bearer fixture-only-not-a-real-secret-000000000000'})
    for _ in range(80):
        if p.poll() is not None:raise RuntimeError('server exited')
        try:
            c.get(f'http://127.0.0.1:{port}/healthz');break
        except httpx.ConnectError:time.sleep(.25)
    counter=0
    def rpc(method,params):
        global counter
        counter+=1;r=c.post(url,json={'jsonrpc':'2.0','id':counter,'method':method,'params':params});r.raise_for_status()
        if r.headers.get('mcp-session-id'):c.headers['mcp-session-id']=r.headers['mcp-session-id']
        text=r.text
        if 'text/event-stream' in r.headers.get('content-type',''):
            text=next(line[6:] for line in text.splitlines() if line.startswith('data: '))
        obj=json.loads(text)
        if 'error' in obj:raise RuntimeError(obj)
        return obj['result']
    rpc('initialize',{'protocolVersion':'2024-11-05','capabilities':{},'clientInfo':{'name':'http-fixture','version':'1'}})
    c.post(url,json={'jsonrpc':'2.0','method':'notifications/initialized'})
    name='fs_write' if kind=='fs' else 'workspace_write_new'
    schema=next(t for t in rpc('tools/list',{})['tools'] if t['name']==name)
    assert 'declaration_context' in schema['inputSchema']['properties']
    a={'root':'fixture','path':'canary.md','content':'RUN14 Linux HTTP canary','message':'fixture','operation_id':'linux-http-01'}
    bad=rpc('tools/call',{'name':name,'arguments':a})
    assert bad['isError'] is True,bad
    assert 'DECLARATION_REQUIRED' in bad['content'][0]['text'] and 'missing_fields' in bad['content'][0]['text'],bad
    assert not (files/'canary.md').exists()
    a.update(declared_actor='GPT Live',declaration_context={'origin_environment':'macbok','task_id':'fixture','command_ref':'RUN-HTTP-FIXTURE'})
    good=rpc('tools/call',{'name':name,'arguments':a})
    assert not good.get('isError'),good
    assert (files/'canary.md').read_text()==a['content'],good
    assert 'declaration_receipt' in good['content'][0]['text'].lower(),good
    again=rpc('tools/call',{'name':name,'arguments':a});assert not again.get('isError'),again
    a['declaration_context']['origin_environment']='cloud'
    conflict=rpc('tools/call',{'name':name,'arguments':a})
    assert 'operation_id_reused' in conflict['content'][0]['text'].lower(),conflict
    print(json.dumps({'kind':kind,'platform':sys.platform,'http_schema':True,'missing_isError':bad['isError'],'zero_mutation':True,'write_receipt':good,'replay':again,'changed_facts_conflict':True,'lifespan':'on' if kind=='fs' else 'off (external services excluded)'},ensure_ascii=False))
finally:
    p.terminate()
    try:p.wait(timeout=5)
    except subprocess.TimeoutExpired:p.kill();p.wait()
    log.seek(0)
    if sys.exc_info()[0]:print(log.read()[-8000:],file=sys.stderr)
```

Build uses DOCKER_BUILDKIT=0 to resolve pinned local image IDs; BuildKit interpreted sha256 as a registry name and failed before build. No base image was changed. Retained tags: hjw-run14-ad:candidate and hjw-run14-fs:candidate.
