# RUN17 scoped diff

SHA256 `94517824b03280fff5a7d1c0815dd20c38c1f0e97469e3d08163439a3ae1d7ac`

```diff
--- /dev/null
+++ b/agent_data/declaration_contract.py
@@ -0,0 +1,169 @@
+"""Four-fact attribution. Never authentication or authorization; no network calls."""
+import contextvars
+import json
+import os
+import re
+import unicodedata
+from contextlib import contextmanager
+
+VERSION = 'four-facts-1'
+ALIASES = {'gptlive': 'gpt-live', 'codexdesktop': 'codex-desktop', 'claudecode': 'claude-code'}
+ENV_ALIASES = {'macbok': 'macbook', 'mac-book': 'macbook', 'mac': 'macbook', 'macos': 'macbook'}
+DESCRIPTION = ('Before writing, provide four facts: AI product declared_actor and declaration_context '
+               '{origin_environment:"cloud|macbook|vps",task_id:"hermes-joint-workspace",command_ref:"RUN-..."}. '
+               'Only supply facts not available from verified server context. Example declared_actor:"GPT Live". '
+               'DECLARATION_REQUIRED missing facts return missing_fields and field_example; repeat the same call with those facts. '
+               'No ticket or Owner action is needed. One declaration is carried through chunks and queued work. '
+               'Self declaration never grants permissions. operation_id is idempotency, not RUN authorization.')
+FIELD = {'description': DESCRIPTION}
+CONTEXT_FIELD = {'description': DESCRIPTION}
+current = contextvars.ContextVar('write_declaration', default=None)
+EXAMPLES = {'declared_actor': 'GPT Live', 'origin_environment': 'cloud',
+            'task_id': 'hermes-joint-workspace', 'command_ref': 'RUN-...'}
+
+class Denied(Exception):
+    def __init__(self, code='DECLARATION_REQUIRED', detail=DESCRIPTION, fields=None):
+        self.code, self.detail = code, detail
+        self.fields = fields or ['declared_actor']
+        super().__init__(detail)
+    def result(self):
+        return {'error': self.code, 'detail': self.detail, 'instruction': self.detail,
+                'missing_fields': self.fields,
+                'field_example': {k: EXAMPLES.get(k, 'use the original verified context') for k in self.fields},
+                'field': self.fields[0], 'example': {'declared_actor': EXAMPLES['declared_actor'],
+                'declaration_context': {k:v for k,v in EXAMPLES.items() if k != 'declared_actor'}}, 'mutation': 'none'}
+
+def enforced():
+    mode = os.environ.get('WORKSPACE_DECLARATION_MODE', 'advertise')
+    if mode not in ('advertise', 'enforce'):
+        raise Denied('DECLARATION_MODE_INVALID', 'Operator must select advertise or enforce.')
+    return mode == 'enforce'
+
+def clean(value, field, limit=128):
+    if (not isinstance(value, str) or not value.strip() or len(value) > limit
+            or any(unicodedata.category(c).startswith('C') for c in value)):
+        raise Denied(fields=[field])
+    value = unicodedata.normalize('NFKC', value).strip()
+    if len(value) > limit:
+        raise Denied(fields=[field])
+    return value
+
+def actor(value):
+    value = re.sub(r'[\s_-]+', '-', clean(value, 'declared_actor').casefold())
+    if not all(c.isalnum() or c in '-.' for c in value) or not any(c.isalnum() for c in value):
+        raise Denied(fields=['declared_actor'])
+    return ALIASES.get(value, value)
+
+def canonical(value, field):
+    if field == 'declared_actor':
+        return actor(value)
+    value = clean(value, field, 200)
+    if field == 'origin_environment':
+        value = re.sub(r'[\s_-]+', '-', value.casefold())
+        value = ENV_ALIASES.get(value, value)
+        if value not in ('cloud', 'macbook', 'vps'):
+            raise Denied('CONTEXT_CLARIFICATION_REQUIRED', 'Set origin_environment to the AI source: cloud, macbook or vps; not the Gateway host.', [field])
+    if field == 'task_id':
+        value = value.removeprefix('work/').rstrip('/')
+        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*(?:/[A-Za-z0-9][A-Za-z0-9._-]*)*', value) or any(x in ('.','..') for x in value.split('/')):
+            raise Denied('CONTEXT_CLARIFICATION_REQUIRED', 'Use the exact task path; task names are never fuzzy-corrected.', [field])
+    return value
+
+def authenticate(who):
+    if not isinstance(who, dict) or who.get('authenticated') is not True or not who.get('label'):
+        raise Denied('AUTHENTICATED_ACTOR_REQUIRED', 'A trusted Gateway credential is required; self declaration cannot grant access.')
+    return who['label']
+
+def target_task(args):
+    """Derive only a unique explicit work/<task> target; never from free text."""
+    paths = []
+    def collect(a):
+        for k in ('path', 'from', 'to'):
+            if isinstance(a.get(k), str): paths.append(a[k])
+        for k in ('operations', 'ops'):
+            for op in a.get(k, []) if isinstance(a.get(k, []), list) else []:
+                if isinstance(op, dict): collect(op)
+        if isinstance(a.get('arguments'), dict): collect(a['arguments'])
+    collect(args)
+    tasks = set()
+    for path in paths:
+        parts = path.split('/')
+        if '..' in parts or path.startswith('/'):
+            continue
+        if len(parts) > 2 and parts[0] == 'work': tasks.add(parts[1])
+    if len(tasks) > 1:
+        raise Denied('CONTEXT_CLARIFICATION_REQUIRED', 'Targets span multiple tasks; split the logical write by task.', ['task_id'])
+    return next(iter(tasks), None)
+
+def resolve(args, who, carried=None, verified=None):
+    """carried and verified must originate only from trusted server adapters."""
+    value = args.get('declared_actor')
+    context = args.get('declaration_context')
+    if carried is None and not enforced() and value is None and context is None:
+        return None
+    auth = authenticate(who)
+    if context is None: context = {}
+    if not isinstance(context, dict) or set(context) - {'origin_environment','task_id','command_ref'}:
+        raise Denied('CONTEXT_CLARIFICATION_REQUIRED', DESCRIPTION, ['origin_environment','task_id','command_ref'])
+    supplied = dict(context)
+    if value is not None: supplied['declared_actor'] = value
+    if carried is not None:
+        if isinstance(carried, dict) and carried.get('authenticated_actor') != auth:
+            raise Denied('DECLARATION_ACTOR_MISMATCH', 'Retry with the original credential.')
+        if not isinstance(carried, dict) or carried.get('contract_version') != VERSION or carried.get('authenticated_actor') != auth or not all(k in carried.get('facts', {}) for k in EXAMPLES):
+            raise Denied('DECLARATION_CONTEXT_INVALID', 'Use the original credential and four-fact logical write; reconcile legacy metadata before enforce.')
+        # Carry the original receipt byte values; do not re-normalize using a newer alias table.
+        for field, raw in supplied.items():
+            if raw != carried['facts'][field]['raw']:
+                raise Denied('DECLARATION_ACTOR_MISMATCH', 'Retry with the original four facts and credential.', [field])
+        return json.loads(json.dumps(carried))
+    verified = verified or {}
+    derived_task = target_task(args)
+    if derived_task:
+        if verified.get('task_id') and canonical(verified['task_id'],'task_id') != derived_task:
+            raise Denied('CONTEXT_CLARIFICATION_REQUIRED', 'Target task conflicts with verified task.', ['task_id'])
+        verified = dict(verified, task_id=derived_task)
+    facts, missing = {}, []
+    for field in EXAMPLES:
+        raw = verified.get(field, supplied.get(field))
+        provenance = 'verified' if field in verified else 'self_declared'
+        if field == 'task_id' and derived_task: provenance = 'derived'
+        if raw is None and field == 'command_ref' and args.get('operation_id'):
+            raw, provenance = args['operation_id'], 'derived'
+        if raw is None:
+            missing.append(field); continue
+        normalized = canonical(raw, field)
+        if field in verified and field in supplied and canonical(supplied[field],field) != normalized:
+            raise Denied('CONTEXT_CLARIFICATION_REQUIRED', 'Declared context conflicts with verified context; retry with the exact task/assignment.', [field])
+        facts[field] = {'raw': supplied.get(field, raw), 'canonical': normalized, 'provenance': provenance}
+    if missing:
+        raise Denied(fields=missing)
+    kind = 'ad-hoc' if facts['command_ref']['provenance'] == 'derived' else ('RUN' if re.search(r'(?:^RUN-|-[0-9]{8}-[0-9]+$)', facts['command_ref']['canonical']) else 'assignment')
+    return {'contract_version': VERSION, 'normalizer_version': VERSION, 'alias_version': '1',
+            'declared_actor': facts['declared_actor']['canonical'], 'authenticated_actor': auth,
+            'facts': facts, 'command_kind': kind,
+            'flags': [] if facts['declared_actor']['canonical'] in set(ALIASES.values()) | {'gpt-chat','gpt-work','claude-chat','claude-code-cli','codex-worker'} else ['UNREGISTERED_ALIAS']}
+
+@contextmanager
+def scope(value):
+    token = current.set(value)
+    try: yield
+    finally: current.reset(token)
+
+def bind_hash(args):
+    result = {k:v for k,v in args.items() if k not in ('declared_actor','declaration_context')}
+    if current.get() is not None:
+        v = current.get()
+        # Bind original facts/auth, not versioned canonical aliases. Historical receipts remain immutable.
+        result['_declaration'] = {'authenticated_actor':v['authenticated_actor'], 'raw_facts':{k:x['raw'] for k,x in v['facts'].items()}}
+    return result
+
+def receipt(result):
+    if current.get() is None or not isinstance(result, dict) or result.get('error') or result.get('replayed'):
+        return result
+    return dict(result, declaration_receipt=dict(current.get()))
+
+def text_receipt(text):
+    if current.get() is None or '\nDECLARATION_RECEIPT ' in text:
+        return text
+    return text + '\nDECLARATION_RECEIPT ' + json.dumps(current.get(), ensure_ascii=False, sort_keys=True)
--- /dev/null
+++ b/agent_data/workspace_declaration.py
@@ -0,0 +1,67 @@
+"""Thin adapter; classifications explicit so newly introduced writers fail closed."""
+import json
+import re
+from pathlib import Path
+from agent_data import declaration_contract as d, hvu_signals
+
+WRITES = frozenset('workspace_edit workspace_write_new workspace_copy workspace_move workspace_transaction workspace_upload_begin workspace_upload_append workspace_upload_commit workspace_import_file'.split())
+NON_SOURCE = frozenset('infra_graph infra_logs infra_ops_plan workspace_list workspace_read workspace_search workspace_diff workspace_log vps_status ui_screenshot ui_inspect workspace_upload_status workspace_result_read workspace_exec workspace_exec_status workspace_exec_cancel workspace_task_status workspace_task_cancel workspace_stat'.split())
+
+def target(name, args):
+    if name == 'workspace_task_start':
+        if args.get('tool') == name:
+            raise d.Denied('TOOL_NOT_ALLOWED')
+        return target(args.get('tool'), args.get('arguments', {}))
+    if name in WRITES:
+        return True
+    if name in NON_SOURCE:
+        return False
+    raise d.Denied('UNCLASSIFIED_TOOL', 'Gateway must classify this tool before it can run.')
+
+def install(w):
+    for definition in w.TOOL_SCHEMAS:
+        if definition['name'] in WRITES | {'workspace_task_start'}:
+            definition['inputSchema']['properties']['declared_actor'] = dict(d.FIELD)
+            definition['inputSchema']['properties']['declaration_context'] = dict(d.CONTEXT_FIELD)
+            definition['description'] += ' ' + d.DESCRIPTION
+    original = w.call
+    def call(name, args):
+        # Scope authorization precedes declaration; declaration precedes ALL state writes.
+        agent_id = hvu_signals.agent_id()
+        if agent_id is not None:
+            try:
+                w.agent_check(agent_id, name, args)
+            except w.WorkspaceError as error:
+                return {'error': error.code, 'detail': error.detail}
+        try:
+            if any(k.startswith('_') for k in args):
+                raise d.Denied('CLIENT_METADATA_FORBIDDEN', 'Server-carried metadata cannot be supplied by clients.')
+            if not target(name, args):
+                with d.scope(None):
+                    return original(name, args)
+            carried = d.current.get()
+            if name in ('workspace_upload_append', 'workspace_upload_commit'):
+                uid = args.get('upload_id', '')
+                if not isinstance(uid, str) or not re.fullmatch('[a-f0-9]{32}', uid):
+                    raise d.Denied('INVALID_ID')
+                # config() is read-only; state_dir() would mkdir before admission.
+                p = Path(w.config()['state_dir']) / 'uploads' / (uid + '.json')
+                try:
+                    meta = json.loads(p.read_text())
+                except (OSError, ValueError):
+                    raise d.Denied('UPLOAD_NOT_FOUND')
+                carried = meta.get('_declaration')
+                if carried is None and (d.enforced() or args.get('declared_actor') is not None):
+                    raise d.Denied('LEGACY_UPLOAD_UNATTRIBUTED', 'Begin a new declared upload; old metadata is not attributed retroactively.')
+            declaration = d.resolve(args, hvu_signals.hidden(), carried)
+            clean = {k: v for k, v in args.items() if k not in ('declared_actor', 'declaration_context')}
+            if name == 'workspace_task_start':
+                nested = clean.get('arguments', {})
+                if 'declared_actor' in nested or 'declaration_context' in nested:
+                    d.resolve(nested, hvu_signals.hidden(), declaration)
+                    clean['arguments'] = {k: v for k, v in nested.items() if k not in ('declared_actor', 'declaration_context')}
+            with d.scope(declaration):
+                return d.receipt(original(name, clean))
+        except d.Denied as error:
+            return error.result()
+    w.call = call
--- a/agent_data/workspace_idempotency.py
+++ b/agent_data/workspace_idempotency.py
@@ -10,6 +10,7 @@
 operation_id is removed before hashing so the same payload hashes alike with or without it.
 Omitting operation_id keeps the pre-existing behaviour exactly, so older clients are unaffected.
 """
+from agent_data import declaration_contract as declaration
 import json
 import os
 import re
@@ -122,7 +123,7 @@
         return entries[-1]
 
     def args_hash(args):
-        keep = {k: v for k, v in args.items() if k != 'operation_id'}
+        keep = declaration.bind_hash({k: v for k, v in args.items() if k != 'operation_id'})
         # The attachment reference carries a fresh download_url per attempt; the file_id
         # is what identifies the attachment, so the URL must not decide identity.
         if isinstance(keep.get('file'), dict):
@@ -180,7 +181,7 @@
         def wrapped(args):
             given = args.get('operation_id')
             if given is None:
-                return handler(args)  # unchanged legacy behaviour
+                return declaration.receipt(handler(args))
             if not isinstance(given, str) or not OP_ID_RX.fullmatch(given):
                 w.fail('INVALID_ARGUMENT',
                        'operation_id: 2-80 characters, letters/digits/._:- starting alphanumeric.')
@@ -194,7 +195,7 @@
             # this 'preparing' line or is blocked on the root lock.
             record(given, tool, root, digest_value, 'preparing')
             try:
-                result = handler({k: v for k, v in args.items() if k != 'operation_id'})
+                result = declaration.receipt(handler({k: v for k, v in args.items() if k != 'operation_id'}))
             except w.WorkspaceError as error:
                 if error.code in UNCLEAN:
                     # H08: an unclean outcome is quarantined, not offered for a retry.
--- a/agent_data/workspace_tasks.py
+++ b/agent_data/workspace_tasks.py
@@ -1,6 +1,7 @@
 """Durable SQLite task queue; one exclusive supervisor, bounded active subprocesses.
 Restart requeues pre-commit work; critical interrupted writes require reconciliation.
 """
+from agent_data import declaration_contract as declaration
 import fcntl
 import json
 import os
@@ -49,12 +50,12 @@
         if disk_state(w.state_dir(),policy,len(json.dumps(args).encode()))['pressure']:w.fail('DISK_PRESSURE','Retry after temporary storage is reclaimed.')
         q=queue(w);args_hash=None
         from agent_data import hvu_signals
-        request={'_hvu':hvu_signals.hidden(),'tool':tool,'arguments':args,'operation_id':a.get('operation_id'),'args_hash':args_hash}
+        request={'_hvu':hvu_signals.hidden(),'_declaration':declaration.current.get(),'tool':tool,'arguments':args,'operation_id':a.get('operation_id'),'args_hash':args_hash}
         # H14 (2026-09-19): a retry after a lost response must find the work it
         # already queued, not queue it again. VPSC2-W4Q-05: also after it finished, and
         # atomically when two workers receive the same retry at once.
         if a.get('operation_id') is not None:
-            op_id=w.check_operation_id(a['operation_id']);args_hash=request['args_hash']=w.payload_hash(a)
+            op_id=w.check_operation_id(a['operation_id']);args_hash=request['args_hash']=w.payload_hash(declaration.bind_hash(a))
             key,prior_hash,replayed=q.enqueue_once('tasks',request,op_id,args_hash)
             if replayed:
                 if prior_hash!=args_hash:
@@ -217,9 +218,22 @@
     os.nice(int(policy.get('worker_nice',5)))
     request=json.loads(row['request'])
     from agent_data import hvu_signals
+    hvu_signals.identity.set(None)
+    hvu_signals.agent.set(None)
     hvu_signals.restore_hidden(request.get('_hvu'))
     os.environ['WORKSPACE_TASK_ATTEMPT']=str(row['attempts'])
-    try:result=w.call(request['tool'],request['arguments'])
+    try:
+        with declaration.scope(None):
+            from agent_data.workspace_declaration import target
+            carried=request.get('_declaration')
+            if target(request['tool'],request['arguments']):
+                if carried is None and declaration.enforced():
+                    raise declaration.Denied('LEGACY_JOB_UNATTRIBUTED','Legacy job requires operator reconciliation; no new attribution is inferred.')
+                value=declaration.resolve({},hvu_signals.hidden(),carried)
+            else:value=None
+            with declaration.scope(value):
+                result=w.call(request['tool'],request['arguments'])
+    except declaration.Denied as error:result=error.result()
     except MemoryError:result={'error':'RESOURCE_PRESSURE','detail':'Operator may increase worker memory or use smaller transport windows.'}
     error=result.get('error')
     if error in ('WORKSPACE_BUSY','OVERLOADED','DISK_PRESSURE','UPSTREAM_UNAVAILABLE'):
--- a/agent_data/workspace_tools.py
+++ b/agent_data/workspace_tools.py
@@ -2105,3 +2105,6 @@
 # Last: wraps the final write handlers, so copy/move/transaction are covered too.
 from agent_data import workspace_idempotency
 workspace_idempotency.install(sys.modules[__name__])
+
+from agent_data import workspace_declaration
+workspace_declaration.install(sys.modules[__name__])
--- a/agent_data/workspace_transfer.py
+++ b/agent_data/workspace_transfer.py
@@ -2,6 +2,7 @@
 No logical byte/count ceiling. Private state is never a workspace root.
 Checksums, expected HEAD/content, atomic finalize and metadata-only audit retained.
 """
+from agent_data import declaration_contract as declaration
 import base64
 import fcntl
 import hashlib
@@ -60,6 +61,7 @@
                 except (OSError,ValueError):continue
                 if prior.get('status') not in ('uploading','committed'):continue
                 if (prior.get('root'),prior.get('path'),prior.get('sha256'),prior.get('total_bytes'))!=(a['root'],a['path'],a['sha256'],a['total_bytes']):continue
+                if prior.get('_declaration') != declaration.current.get():continue
                 data=state('uploads',prior['id'])
                 if prior['status']=='committed':
                     w.journal({'event':'upload_begin_already_committed','id':prior['id'],'root':a['root'],'path':a['path']})
@@ -74,7 +76,7 @@
                 if not w.version_ok(a['expected_version'],raw): w.fail('VERSION_CONFLICT')
             elif os.path.lexists(str(Path(spec['path'])/a['path'])): w.fail('FILE_EXISTS')
             uid=uuid.uuid4().hex;p=state('uploads',uid)
-            meta=dict(a,id=uid,expected_head=head,status='uploading',created_at=time.time())
+            meta=dict(a,id=uid,expected_head=head,status='uploading',created_at=time.time(),_declaration=declaration.current.get())
             save(p.with_suffix('.json'),meta)
             with open(p,'xb') as f: os.chmod(p,0o600)
             w.journal({'event':'upload_begin','id':uid,'root':a['root'],'path':a['path'],'total_bytes':a['total_bytes'],'sha256':a['sha256']})
@@ -130,6 +132,7 @@
                 result=w.write(args)
             else:
                 result=w.write(dict(args,content=content),True)
+            result=declaration.receipt(result)
             result['sha256']=m['sha256']
             if result.get('push_status')=='UNKNOWN_DO_NOT_RETRY': return result
             m.update(status='committed',result=result);save(p.with_suffix('.json'),m)
```
