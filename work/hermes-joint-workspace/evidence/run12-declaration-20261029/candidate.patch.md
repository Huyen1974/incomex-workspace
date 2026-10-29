# RUN12 offline candidate patch

Local snapshot candidate commit: `0ca9577fe7cf115f4501ffbcdb199fa211cb6c6d`. Runtime baseline commit: `9e1935fd62631b4bc5344f67c5c120ecb1618228`. NOT DEPLOYED. Remove this Markdown envelope to obtain the exact unified diff.

```diff
diff --git a/agent_data/declaration_contract.py b/agent_data/declaration_contract.py
new file mode 100644
index 0000000..260b783
--- /dev/null
+++ b/agent_data/declaration_contract.py
@@ -0,0 +1,77 @@
+"""RUN12 single declaration contract. Packaged byte-identically in both gateways/helper.
+Self declaration is attribution, never authentication or an authorization grant.
+Advertise is the compatibility default; operator enforcement is a separate rollout.
+"""
+import contextvars
+import json
+import os
+from contextlib import contextmanager
+
+DESCRIPTION = ('Before writing, pass declared_actor: your AI name (example: "Codex Worker"). '
+               'This is self declaration, not a new credential. If DECLARATION_REQUIRED, '
+               'repeat the same call with your name; no ticket or Owner action is needed. '
+               'One declaration is carried through upload chunks and queued work.')
+FIELD = {'description': DESCRIPTION}  # Validate here, not in transport, to return actionable errors.
+current = contextvars.ContextVar('write_declaration', default=None)
+
+class Denied(Exception):
+    def __init__(self, code='DECLARATION_REQUIRED', detail=DESCRIPTION):
+        self.code, self.detail = code, detail
+        super().__init__(detail)
+    def result(self):
+        return {'error': self.code, 'detail': self.detail, 'field': 'declared_actor',
+                'example': {'declared_actor': 'Codex Worker'}, 'mutation': 'none'}
+
+def enforced():
+    mode = os.environ.get('WORKSPACE_DECLARATION_MODE', 'advertise')
+    if mode not in ('advertise', 'enforce'):
+        raise Denied('DECLARATION_MODE_INVALID', 'Operator must select advertise or enforce.')
+    return mode == 'enforce'
+
+def actor(value):
+    if not isinstance(value, str) or not value.strip() or any(not c.isprintable() for c in value):
+        raise Denied()
+    return value.strip()
+
+def authenticate(who):
+    if not isinstance(who, dict) or who.get('authenticated') is not True or not who.get('label'):
+        raise Denied('AUTHENTICATED_ACTOR_REQUIRED', 'A trusted Gateway credential is required; self declaration cannot grant access.')
+    return who['label']
+
+def resolve(args, who, carried=None):
+    """Only trusted adapters may supply carried (persisted server-owned metadata)."""
+    value = args.get('declared_actor')
+    if carried is not None:
+        if not isinstance(carried, dict) or set(carried) != {'declared_actor', 'authenticated_actor'}:
+            raise Denied('DECLARATION_CONTEXT_INVALID')
+        expected = {'declared_actor': actor(carried['declared_actor']), 'authenticated_actor': authenticate(who)}
+        if expected != carried or (value is not None and actor(value) != carried['declared_actor']):
+            raise Denied('DECLARATION_ACTOR_MISMATCH', 'Retry with the original actor and credential, or begin a new logical write.')
+        return dict(carried)
+    if value is None and not enforced():
+        return None
+    return {'declared_actor': actor(value), 'authenticated_actor': authenticate(who)}
+
+@contextmanager
+def scope(value):
+    token = current.set(value)
+    try:
+        yield
+    finally:
+        current.reset(token)
+
+def bind_hash(args):
+    result = {k: v for k, v in args.items() if k != 'declared_actor'}
+    if current.get() is not None:
+        result['_declaration'] = dict(current.get())
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
diff --git a/agent_data/workspace_declaration.py b/agent_data/workspace_declaration.py
new file mode 100644
index 0000000..b4111a8
--- /dev/null
+++ b/agent_data/workspace_declaration.py
@@ -0,0 +1,64 @@
+"""Thin adapter; classifications explicit so newly introduced writers fail closed."""
+import json
+import re
+from pathlib import Path
+from agent_data import declaration_contract as d, hvu_signals
+
+WRITES = frozenset('workspace_edit workspace_write_new workspace_copy workspace_move workspace_transaction workspace_upload_begin workspace_upload_append workspace_upload_commit workspace_import_file'.split())
+NON_SOURCE = frozenset('workspace_list workspace_read workspace_search workspace_diff workspace_log vps_status ui_screenshot ui_inspect workspace_upload_status workspace_result_read workspace_exec workspace_exec_status workspace_exec_cancel workspace_task_status workspace_task_cancel workspace_stat'.split())
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
+            clean = {k: v for k, v in args.items() if k != 'declared_actor'}
+            if name == 'workspace_task_start':
+                nested = clean.get('arguments', {})
+                if 'declared_actor' in nested:
+                    d.resolve(nested, hvu_signals.hidden(), declaration)
+                    clean['arguments'] = {k: v for k, v in nested.items() if k != 'declared_actor'}
+            with d.scope(declaration):
+                return d.receipt(original(name, clean))
+        except d.Denied as error:
+            return error.result()
+    w.call = call
diff --git a/agent_data/workspace_idempotency.py b/agent_data/workspace_idempotency.py
index d337367..ce18bcf 100644
--- a/agent_data/workspace_idempotency.py
+++ b/agent_data/workspace_idempotency.py
@@ -10,6 +10,7 @@ so it survives a container restart. The request is kept only as a normalised has
 operation_id is removed before hashing so the same payload hashes alike with or without it.
 Omitting operation_id keeps the pre-existing behaviour exactly, so older clients are unaffected.
 """
+from agent_data import declaration_contract as declaration
 import json
 import os
 import re
@@ -122,7 +123,7 @@ def install(w):
         return entries[-1]
 
     def args_hash(args):
-        keep = {k: v for k, v in args.items() if k != 'operation_id'}
+        keep = declaration.bind_hash({k: v for k, v in args.items() if k != 'operation_id'})
         # The attachment reference carries a fresh download_url per attempt; the file_id
         # is what identifies the attachment, so the URL must not decide identity.
         if isinstance(keep.get('file'), dict):
@@ -180,7 +181,7 @@ def install(w):
         def wrapped(args):
             given = args.get('operation_id')
             if given is None:
-                return handler(args)  # unchanged legacy behaviour
+                return declaration.receipt(handler(args))
             if not isinstance(given, str) or not OP_ID_RX.fullmatch(given):
                 w.fail('INVALID_ARGUMENT',
                        'operation_id: 2-80 characters, letters/digits/._:- starting alphanumeric.')
@@ -194,7 +195,7 @@ def install(w):
             # this 'preparing' line or is blocked on the root lock.
             record(given, tool, root, digest_value, 'preparing')
             try:
-                result = handler({k: v for k, v in args.items() if k != 'operation_id'})
+                result = declaration.receipt(handler({k: v for k, v in args.items() if k != 'operation_id'}))
             except w.WorkspaceError as error:
                 if error.code in UNCLEAN:
                     # H08: an unclean outcome is quarantined, not offered for a retry.
diff --git a/agent_data/workspace_tasks.py b/agent_data/workspace_tasks.py
index c44372b..d614142 100644
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
@@ -50,7 +51,7 @@ def install(w):
         # H14 (2026-09-19): a retry after a lost response must find the work it
         # already queued, not queue it again.
         if a.get('operation_id') is not None:
-            op_id=w.check_operation_id(a['operation_id']);args_hash=w.payload_hash(a)
+            op_id=w.check_operation_id(a['operation_id']);args_hash=w.payload_hash(declaration.bind_hash(a))
             key,prior=q.find_by_operation('tasks',op_id)
             if key:
                 if prior.get('args_hash')!=args_hash:
@@ -59,7 +60,7 @@ def install(w):
                 ensure_supervisor()
                 return dict(q.status(key,'tasks'),poll_tool='workspace_task_status',replayed=True)
         from agent_data import hvu_signals
-        key=q.enqueue('tasks',{'_hvu':hvu_signals.hidden(),'tool':tool,'arguments':args,'operation_id':a.get('operation_id'),'args_hash':args_hash})
+        key=q.enqueue('tasks',{'_hvu':hvu_signals.hidden(),'_declaration':declaration.current.get(),'tool':tool,'arguments':args,'operation_id':a.get('operation_id'),'args_hash':args_hash})
         w.journal({'event':'task_queued','id':key,'tool':tool})
         ensure_supervisor()
         return dict(q.status(key,'tasks'),poll_tool='workspace_task_status')
@@ -204,9 +205,22 @@ def run(key):
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
diff --git a/agent_data/workspace_tools.py b/agent_data/workspace_tools.py
index c43a109..82073f0 100644
--- a/agent_data/workspace_tools.py
+++ b/agent_data/workspace_tools.py
@@ -2105,3 +2105,6 @@ workspace_snapshot.install(sys.modules[__name__])
 # Last: wraps the final write handlers, so copy/move/transaction are covered too.
 from agent_data import workspace_idempotency
 workspace_idempotency.install(sys.modules[__name__])
+
+from agent_data import workspace_declaration
+workspace_declaration.install(sys.modules[__name__])
diff --git a/agent_data/workspace_transfer.py b/agent_data/workspace_transfer.py
index f99f8d1..c6b3584 100644
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
@@ -60,6 +61,7 @@ def install(w):
                 except (OSError,ValueError):continue
                 if prior.get('status') not in ('uploading','committed'):continue
                 if (prior.get('root'),prior.get('path'),prior.get('sha256'),prior.get('total_bytes'))!=(a['root'],a['path'],a['sha256'],a['total_bytes']):continue
+                if prior.get('_declaration') != declaration.current.get():continue
                 data=state('uploads',prior['id'])
                 if prior['status']=='committed':
                     w.journal({'event':'upload_begin_already_committed','id':prior['id'],'root':a['root'],'path':a['path']})
@@ -74,7 +76,7 @@ def install(w):
                 if not w.version_ok(a['expected_version'],raw): w.fail('VERSION_CONFLICT')
             elif os.path.lexists(str(Path(spec['path'])/a['path'])): w.fail('FILE_EXISTS')
             uid=uuid.uuid4().hex;p=state('uploads',uid)
-            meta=dict(a,id=uid,expected_head=head,status='uploading',created_at=time.time())
+            meta=dict(a,id=uid,expected_head=head,status='uploading',created_at=time.time(),_declaration=declaration.current.get())
             save(p.with_suffix('.json'),meta)
             with open(p,'xb') as f: os.chmod(p,0o600)
             w.journal({'event':'upload_begin','id':uid,'root':a['root'],'path':a['path'],'total_bytes':a['total_bytes'],'sha256':a['sha256']})
@@ -130,6 +132,7 @@ def install(w):
                 result=w.write(args)
             else:
                 result=w.write(dict(args,content=content),True)
+            result=declaration.receipt(result)
             result['sha256']=m['sha256']
             if result.get('push_status')=='UNKNOWN_DO_NOT_RETRY': return result
             m.update(status='committed',result=result);save(p.with_suffix('.json'),m)
diff --git a/claude/app/declaration_contract.py b/claude/app/declaration_contract.py
new file mode 100644
index 0000000..260b783
--- /dev/null
+++ b/claude/app/declaration_contract.py
@@ -0,0 +1,77 @@
+"""RUN12 single declaration contract. Packaged byte-identically in both gateways/helper.
+Self declaration is attribution, never authentication or an authorization grant.
+Advertise is the compatibility default; operator enforcement is a separate rollout.
+"""
+import contextvars
+import json
+import os
+from contextlib import contextmanager
+
+DESCRIPTION = ('Before writing, pass declared_actor: your AI name (example: "Codex Worker"). '
+               'This is self declaration, not a new credential. If DECLARATION_REQUIRED, '
+               'repeat the same call with your name; no ticket or Owner action is needed. '
+               'One declaration is carried through upload chunks and queued work.')
+FIELD = {'description': DESCRIPTION}  # Validate here, not in transport, to return actionable errors.
+current = contextvars.ContextVar('write_declaration', default=None)
+
+class Denied(Exception):
+    def __init__(self, code='DECLARATION_REQUIRED', detail=DESCRIPTION):
+        self.code, self.detail = code, detail
+        super().__init__(detail)
+    def result(self):
+        return {'error': self.code, 'detail': self.detail, 'field': 'declared_actor',
+                'example': {'declared_actor': 'Codex Worker'}, 'mutation': 'none'}
+
+def enforced():
+    mode = os.environ.get('WORKSPACE_DECLARATION_MODE', 'advertise')
+    if mode not in ('advertise', 'enforce'):
+        raise Denied('DECLARATION_MODE_INVALID', 'Operator must select advertise or enforce.')
+    return mode == 'enforce'
+
+def actor(value):
+    if not isinstance(value, str) or not value.strip() or any(not c.isprintable() for c in value):
+        raise Denied()
+    return value.strip()
+
+def authenticate(who):
+    if not isinstance(who, dict) or who.get('authenticated') is not True or not who.get('label'):
+        raise Denied('AUTHENTICATED_ACTOR_REQUIRED', 'A trusted Gateway credential is required; self declaration cannot grant access.')
+    return who['label']
+
+def resolve(args, who, carried=None):
+    """Only trusted adapters may supply carried (persisted server-owned metadata)."""
+    value = args.get('declared_actor')
+    if carried is not None:
+        if not isinstance(carried, dict) or set(carried) != {'declared_actor', 'authenticated_actor'}:
+            raise Denied('DECLARATION_CONTEXT_INVALID')
+        expected = {'declared_actor': actor(carried['declared_actor']), 'authenticated_actor': authenticate(who)}
+        if expected != carried or (value is not None and actor(value) != carried['declared_actor']):
+            raise Denied('DECLARATION_ACTOR_MISMATCH', 'Retry with the original actor and credential, or begin a new logical write.')
+        return dict(carried)
+    if value is None and not enforced():
+        return None
+    return {'declared_actor': actor(value), 'authenticated_actor': authenticate(who)}
+
+@contextmanager
+def scope(value):
+    token = current.set(value)
+    try:
+        yield
+    finally:
+        current.reset(token)
+
+def bind_hash(args):
+    result = {k: v for k, v in args.items() if k != 'declared_actor'}
+    if current.get() is not None:
+        result['_declaration'] = dict(current.get())
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
diff --git a/claude/app/fsroots.py b/claude/app/fsroots.py
index 02b9144..7024285 100644
--- a/claude/app/fsroots.py
+++ b/claude/app/fsroots.py
@@ -46,6 +46,7 @@ DOT 0.9 (2026-09-18) — shared workspace contract (S1–S3) + C1/C2:
     source (it is read through the strict filter only).
 """
 from __future__ import annotations
+from . import declaration_contract as declaration
 
 import base64
 import contextlib
@@ -647,7 +648,7 @@ def _journal_find(op_id: str) -> dict | None:
 
 
 def _args_hash(args: dict) -> str:
-    keep = {k: v for k, v in args.items() if k != "operation_id"}
+    keep = declaration.bind_hash({k: v for k, v in args.items() if k != "operation_id"})
     return hashlib.sha256(json.dumps(keep, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")).hexdigest()[:16]
 
 
@@ -763,7 +764,7 @@ def _run_write(op: _Op, fn):
     if replay is not None:
         return replay
     try:
-        text = fn()
+        text = declaration.text_receipt(fn())
     except ToolError as e:
         # H08: an unclean outcome has already filed its own, stronger record;
         # overwriting it with 'failed' would reopen the id for a blind retry.
@@ -1666,7 +1667,7 @@ def _helper_write(op: _Op | None, action: str, args: dict, payload: bytes | None
     UNKNOWN outcome (journaled), never silently retried."""
     try:
         from . import hvu_signals
-        internal_args = dict(args, _hvu=hvu_signals.hidden())
+        internal_args = dict(args, _hvu=hvu_signals.hidden(), _declaration=declaration.current.get())
         result = hostq.request(action, internal_args, wait_s=wait_s, payload=payload)
         ids = result.pop('_hvu_work_ids',[])
         try:
diff --git a/claude/app/hostq.py b/claude/app/hostq.py
index b870208..87cbb9d 100644
--- a/claude/app/hostq.py
+++ b/claude/app/hostq.py
@@ -107,6 +107,15 @@ def request(action: str, args: dict, *, wait_s: float, payload: bytes | None = N
             rid: str | None = None) -> dict:
     """Send one request, wait up to `wait_s` for the answer. Returns the
     answer dict (ok=true) or raises HelperError (with .rid)."""
+    # Every repository helper write (including UI commits) carries the same context.
+    if action in ('gh_put_commit_push','gh_apply_commit_push','gh_move','gh_revert_commit_push','ui_commit','ui_move'):
+        from . import declaration_contract as declaration, hvu_signals
+        try:
+            who = hvu_signals.hidden()
+            value = declaration.resolve({}, dict(who or {}, authenticated=bool(who)), declaration.current.get())
+        except declaration.Denied as error:
+            raise HelperError(error.code, error.detail)
+        args = dict(args, _hvu=who, _declaration=value)
     if not configured():
         raise HelperError(
             "helper_unavailable",
diff --git a/claude/app/server.py b/claude/app/server.py
index 643b54b..4ecd3f2 100644
--- a/claude/app/server.py
+++ b/claude/app/server.py
@@ -11,6 +11,8 @@ depth re-checked here for the /mcp path only, SSE-safe pure-ASGI).
 """
 from __future__ import annotations
 
+from typing import Any
+from . import declaration_contract as declaration
 import asyncio
 import os
 
@@ -64,13 +66,16 @@ def _client_ip(ctx: Context) -> str:
     return "unknown"
 
 
+_DECLARED_WRITES = frozenset('write_file fs_write fs_edit fs_copy fs_move fs_transaction'.split())
+_DECLARED_READS = frozenset('fs_list fs_read fs_search fs_stat fs_log fs_diff'.split())
+_NON_SOURCE = frozenset('pg_schema query_pg read_file directus_read directus_create directus_update directus_delete vps_status ui_screenshot'.split())
+
 async def _finalize(name: str, ctx: Context, args: dict) -> str:
     """Run a sync tool with timeout, then redact + truncate + audit.
 
     Identical wrapper semantics to the previous server (§3G/§3I/§3J);
     only the transport around it changed.
     """
-    fn = getattr(tools, name, None) or getattr(fsroots, name, None) or getattr(hosttools, name)
     timeout_s = TOOL_TIMEOUTS.get(name, TOOL_TIMEOUT_S)
     status = "success"
     denied_reason = None
@@ -85,6 +90,15 @@ async def _finalize(name: str, ctx: Context, args: dict) -> str:
     # call is the claude.ai connector surface (Claude Chat/Cowork). clientInfo stays display-only.
     value = hvu_signals.label(SURFACE_LABEL)
     who = {'label':value,'surface_key':hvu_signals.key(value),'gateway':'claude'}
+    try:
+        value = declaration.resolve(args, dict(who, authenticated=True)) if name in _DECLARED_WRITES else None
+        if name not in _DECLARED_WRITES | _DECLARED_READS | _NON_SOURCE:
+            raise declaration.Denied('UNCLASSIFIED_TOOL')
+    except declaration.Denied as error:
+        return __import__('json').dumps(error.result(), ensure_ascii=False)
+    fn = getattr(tools, name, None) or getattr(fsroots, name, None) or getattr(hosttools, name)
+    args = {k:v for k,v in args.items() if k != 'declared_actor'}
+    declaration_token = declaration.current.set(value)
     token = hvu_signals.identity.set(who)
     try:
         hvu_signals.Store('/var/log/mcp-audit/hvu-presence.json','claude').touch(who,hvu_signals.work_ids(name,args))
@@ -95,10 +109,12 @@ async def _finalize(name: str, ctx: Context, args: dict) -> str:
             result = await asyncio.wait_for(
                 asyncio.to_thread(fn, args), timeout=timeout_s
             )
-            text = result["text"]
+            text = declaration.text_receipt(result["text"])
             rows = result.get("rows")
             row_trunc = result.get("row_truncated", False)
             audit_extra = result.get("audit_extra") or {}
+            if value is not None:
+                audit_extra.update(value)
             byte_budget = result.get("byte_budget")
         except asyncio.TimeoutError:
             status, denied_reason = "timeout", "tool_timeout"
@@ -116,6 +132,7 @@ async def _finalize(name: str, ctx: Context, args: dict) -> str:
             status = "error"
             text = f"[ERROR] {type(e).__name__}: {e}"
         finally:
+            declaration.current.reset(declaration_token)
             hvu_signals.identity.reset(token)
 
     # Write-tool audit metadata even on denial/error (§3I / Phase 2B).
@@ -278,19 +295,20 @@ async def directus_delete(
 
 @mcp.tool(
     annotations=_WRITE,
-    description="Write a UTF-8 text file into the narrow write allowlist "
+    description=declaration.DESCRIPTION + ("Write a UTF-8 text file into the narrow write allowlist "
     "(/opt/incomex/docs/mcp-writes). Atomic (tmp+rename), symlink-resolved, "
     f"secret-denylisted, text-only, <= {L.WRITE_MAX_BYTES} bytes. mode='overwrite' (default) or "
-    "'append'. Content is NOT redacted (deliberate authoring)."
+    "'append'. Content is NOT redacted (deliberate authoring).")
 )
 async def write_file(
-    path: str, content: str, ctx: Context, mode: str = "overwrite"
-) -> str:
+    path: str, content: str, ctx: Context, mode: str = "overwrite",
+    declared_actor: Any = None) -> str:
     return await _finalize(
-        "write_file", ctx, {"path": path, "content": content, "mode": mode}
+        "write_file", ctx, {"declared_actor": declared_actor, "path": path, "content": content, "mode": mode}
     )
 
 
+
 # --- fs_* : one tool set over several named roots (FS_ROOTS_JSON) ------------
 # Usage rules live IN the descriptions on purpose: models pick tools by
 # description, and there is no separate manual to drift out of date.
@@ -386,7 +404,7 @@ async def fs_search(root: str, pattern: str, ctx: Context, path: str = "", regex
 
 @mcp.tool(
     annotations=_WRITE_IDEMP,
-    description="Surgically edit an existing file: edits=[{old_str,new_str},...]. "
+    description=declaration.DESCRIPTION + ("Surgically edit an existing file: edits=[{old_str,new_str},...]. "
     "PREFERRED way to change any existing file (never resend a whole big file). "
     "Each old_str must match EXACTLY ONE place (copy it verbatim from fs_read/"
     "fs_search, whitespace included); 0 or >1 matches -> the whole call is refused "
@@ -406,19 +424,20 @@ async def fs_search(root: str, pattern: str, ctx: Context, path: str = "", regex
     "operation_id (optional): pass your own id to make the call SAFE TO RETRY - the same id with the same "
     "arguments replays the recorded answer instead of committing twice; a lost answer is reported "
     "OUTCOME_UNKNOWN and resolved on retry. expected_head (root gh): refuse when main moved since you read. "
-    "Example: fs_edit(root='ui', path='x.html', edits=[{'old_str':'gap:8px','new_str':'gap:12px'}], message='widen card gap')"
+    "Example: fs_edit(root='ui', path='x.html', edits=[{'old_str':'gap:8px','new_str':'gap:12px'}], message='widen card gap')")
 )
 async def fs_edit(root: str, path: str, edits: list[dict], message: str, ctx: Context,
                   expected_version: str | None = None, expected_head: str | None = None,
-                  operation_id: str | None = None) -> str:
-    return await _finalize("fs_edit", ctx, {"root": root, "path": path, "edits": edits,
+                  operation_id: str | None = None, declared_actor: Any = None) -> str:
+    return await _finalize("fs_edit", ctx, {"declared_actor": declared_actor, "root": root, "path": path, "edits": edits,
                                             "message": message, "expected_version": expected_version,
                                             "expected_head": expected_head, "operation_id": operation_id})
 
 
+
 @mcp.tool(
     annotations=_WRITE_IDEMP,
-    description=f"Create a text file or replace one (content <= {L.WRITE_MAX_BYTES} bytes). Missing parent "
+    description=declaration.DESCRIPTION + (f"Create a text file or replace one (content <= {L.WRITE_MAX_BYTES} bytes). Missing parent "
     "folders are created in every writable root. Replacing an EXISTING file ALWAYS needs "
     "expected_version (the 'version' fs_read/fs_stat gave you - proof you read the file that is there "
     "now), at every size; creating a new file needs nothing. Above "
@@ -429,20 +448,21 @@ async def fs_edit(root: str, path: str, edits: list[dict], message: str, ctx: Co
     "operation_id (optional): pass your own id to make the call SAFE TO RETRY - the same id with the same "
     "arguments replays the recorded answer instead of committing twice; a lost answer is reported "
     "OUTCOME_UNKNOWN and resolved on retry. expected_head (root gh): refuse when main moved since you read. "
-    "Example: fs_write(root='gh', path='notes/plan.md', content='# Plan\\n', message='add plan')"
+    "Example: fs_write(root='gh', path='notes/plan.md', content='# Plan\\n', message='add plan')")
 )
 async def fs_write(root: str, path: str, content: str, message: str, ctx: Context,
                    expected_version: str | None = None, overwrite_large: bool = False,
-                   expected_head: str | None = None, operation_id: str | None = None) -> str:
-    return await _finalize("fs_write", ctx, {"root": root, "path": path, "content": content,
+                   expected_head: str | None = None, operation_id: str | None = None, declared_actor: Any = None) -> str:
+    return await _finalize("fs_write", ctx, {"declared_actor": declared_actor, "root": root, "path": path, "content": content,
                                              "message": message, "expected_version": expected_version,
                                              "overwrite_large": overwrite_large,
                                              "expected_head": expected_head, "operation_id": operation_id})
 
 
+
 @mcp.tool(
     annotations=_WRITE_IDEMP,
-    description="Rename or move a file/folder INSIDE root 'gh' or 'ui' with `git mv`, so the "
+    description=declaration.DESCRIPTION + ("Rename or move a file/folder INSIDE root 'gh' or 'ui' with `git mv`, so the "
     "history follows it (this is a move, never a delete). Refused when the destination "
     "already exists - nothing is ever overwritten. Missing destination folders are created. "
     "'message' (required) becomes the commit message. Root 'gh': pull -> git mv -> commit -> "
@@ -458,20 +478,21 @@ async def fs_write(root: str, path: str, content: str, message: str, ctx: Contex
     "tree token fs_stat gives a folder; if anyone changed any file below it since you read, the move "
     "is refused instead of carrying a tree you never saw. Moving a directory into itself or onto its "
     "own parent is refused before anything is touched. "
-    "Example: fs_move(root='ui', from_path='draft.html', to_path='archive/2026/draft.html', message='archive old draft')"
+    "Example: fs_move(root='ui', from_path='draft.html', to_path='archive/2026/draft.html', message='archive old draft')")
 )
 async def fs_move(root: str, from_path: str, to_path: str, message: str, ctx: Context,
                   expected_version: str | None = None,
-                  expected_head: str | None = None, operation_id: str | None = None) -> str:
-    return await _finalize("fs_move", ctx, {"root": root, "from": from_path, "to": to_path,
+                  expected_head: str | None = None, operation_id: str | None = None, declared_actor: Any = None) -> str:
+    return await _finalize("fs_move", ctx, {"declared_actor": declared_actor, "root": root, "from": from_path, "to": to_path,
                                             "message": message, "expected_version": expected_version,
                                             "expected_head": expected_head,
                                             "operation_id": operation_id})
 
 
+
 @mcp.tool(
     annotations=_WRITE_IDEMP,
-    description="Copy one file OR a whole directory tree server-side (bytes never pass through the model; "
+    description=declaration.DESCRIPTION + ("Copy one file OR a whole directory tree server-side (bytes never pass through the model; "
     "SHA256 checked). A directory is copied recursively as ONE commit, all-or-nothing: symlinks, "
     "gitlinks and submodules at any depth refuse the whole call (nothing is written), every file is "
     f"secret-scanned on its own, and there are ceilings of {L.TREE_MAX_FILES} files / {L.TREE_MAX_BYTES} "
@@ -485,17 +506,18 @@ async def fs_move(root: str, from_path: str, to_path: str, message: str, ctx: Co
     "operation_id (optional): pass your own id to make the call SAFE TO RETRY - the same id with the same "
     "arguments replays the recorded answer instead of committing twice; a lost answer is reported "
     "OUTCOME_UNKNOWN and resolved on retry. expected_head (root gh): refuse when main moved since you read. "
-    "Example: fs_copy(root='gh', from_root='docs', from_path='docs/BAN-DO-HE-THONG-20260729.md', to_path='reports/ban-do.md', message='import map')"
+    "Example: fs_copy(root='gh', from_root='docs', from_path='docs/BAN-DO-HE-THONG-20260729.md', to_path='reports/ban-do.md', message='import map')")
 )
 async def fs_copy(root: str, from_path: str, to_path: str, message: str, ctx: Context,
                   from_root: str | None = None, expected_version: str | None = None,
-                  expected_head: str | None = None, operation_id: str | None = None) -> str:
-    return await _finalize("fs_copy", ctx, {"root": root, "from": from_path, "to": to_path,
+                  expected_head: str | None = None, operation_id: str | None = None, declared_actor: Any = None) -> str:
+    return await _finalize("fs_copy", ctx, {"declared_actor": declared_actor, "root": root, "from": from_path, "to": to_path,
                                             "from_root": from_root, "message": message,
                                             "expected_version": expected_version,
                                             "expected_head": expected_head, "operation_id": operation_id})
 
 
+
 @mcp.tool(
     annotations=_RO,
     description="Metadata of one path WITHOUT its content: type, bytes, mtime, version (the same id fs_read "
@@ -512,7 +534,7 @@ async def fs_stat(root: str, path: str, ctx: Context, lines: bool = False, histo
 
 @mcp.tool(
     annotations=_WRITE_IDEMP,
-    description="Several changes in ONE root as ONE all-or-nothing operation and (root gh) ONE commit + "
+    description=declaration.DESCRIPTION + ("Several changes in ONE root as ONE all-or-nothing operation and (root gh) ONE commit + "
     "push. ops = list of {op:'write', path, content, expected_version?} | {op:'edit', path, edits:[{old_str,"
     "new_str}], expected_version?} | {op:'move', from, to, expected_version?} | {op:'copy', from, to, "
     "from_root?, expected_version?} | {op:'restore', version, path?, archive_dir?}. 'copy' and 'move' "
@@ -530,14 +552,15 @@ async def fs_stat(root: str, path: str, ctx: Context, lines: bool = False, histo
     "arguments replays the recorded answer instead of committing twice; a lost answer is reported "
     "OUTCOME_UNKNOWN and resolved on retry. expected_head (root gh): refuse when main moved since you read. "
     "Example: fs_transaction(root='gh', message='page + script', ops=[{'op':'write','path':'p.html','content':'...'},"
-    "{'op':'edit','path':'app.js','edits':[{'old_str':'v1','new_str':'v2'}],'expected_version':'ab12...'}])"
+    "{'op':'edit','path':'app.js','edits':[{'old_str':'v1','new_str':'v2'}],'expected_version':'ab12...'}])")
 )
 async def fs_transaction(root: str, ops: list[dict], message: str, ctx: Context,
-                         expected_head: str | None = None, operation_id: str | None = None) -> str:
-    return await _finalize("fs_transaction", ctx, {"root": root, "ops": ops, "message": message,
+                         expected_head: str | None = None, operation_id: str | None = None, declared_actor: Any = None) -> str:
+    return await _finalize("fs_transaction", ctx, {"declared_actor": declared_actor, "root": root, "ops": ops, "message": message,
                                                    "expected_head": expected_head, "operation_id": operation_id})
 
 
+
 @mcp.tool(
     annotations=_RO,
     description="Who changed what: commits (hash, time, author, subject) of a "
diff --git a/claude/helper/declaration_contract.py b/claude/helper/declaration_contract.py
new file mode 100644
index 0000000..260b783
--- /dev/null
+++ b/claude/helper/declaration_contract.py
@@ -0,0 +1,77 @@
+"""RUN12 single declaration contract. Packaged byte-identically in both gateways/helper.
+Self declaration is attribution, never authentication or an authorization grant.
+Advertise is the compatibility default; operator enforcement is a separate rollout.
+"""
+import contextvars
+import json
+import os
+from contextlib import contextmanager
+
+DESCRIPTION = ('Before writing, pass declared_actor: your AI name (example: "Codex Worker"). '
+               'This is self declaration, not a new credential. If DECLARATION_REQUIRED, '
+               'repeat the same call with your name; no ticket or Owner action is needed. '
+               'One declaration is carried through upload chunks and queued work.')
+FIELD = {'description': DESCRIPTION}  # Validate here, not in transport, to return actionable errors.
+current = contextvars.ContextVar('write_declaration', default=None)
+
+class Denied(Exception):
+    def __init__(self, code='DECLARATION_REQUIRED', detail=DESCRIPTION):
+        self.code, self.detail = code, detail
+        super().__init__(detail)
+    def result(self):
+        return {'error': self.code, 'detail': self.detail, 'field': 'declared_actor',
+                'example': {'declared_actor': 'Codex Worker'}, 'mutation': 'none'}
+
+def enforced():
+    mode = os.environ.get('WORKSPACE_DECLARATION_MODE', 'advertise')
+    if mode not in ('advertise', 'enforce'):
+        raise Denied('DECLARATION_MODE_INVALID', 'Operator must select advertise or enforce.')
+    return mode == 'enforce'
+
+def actor(value):
+    if not isinstance(value, str) or not value.strip() or any(not c.isprintable() for c in value):
+        raise Denied()
+    return value.strip()
+
+def authenticate(who):
+    if not isinstance(who, dict) or who.get('authenticated') is not True or not who.get('label'):
+        raise Denied('AUTHENTICATED_ACTOR_REQUIRED', 'A trusted Gateway credential is required; self declaration cannot grant access.')
+    return who['label']
+
+def resolve(args, who, carried=None):
+    """Only trusted adapters may supply carried (persisted server-owned metadata)."""
+    value = args.get('declared_actor')
+    if carried is not None:
+        if not isinstance(carried, dict) or set(carried) != {'declared_actor', 'authenticated_actor'}:
+            raise Denied('DECLARATION_CONTEXT_INVALID')
+        expected = {'declared_actor': actor(carried['declared_actor']), 'authenticated_actor': authenticate(who)}
+        if expected != carried or (value is not None and actor(value) != carried['declared_actor']):
+            raise Denied('DECLARATION_ACTOR_MISMATCH', 'Retry with the original actor and credential, or begin a new logical write.')
+        return dict(carried)
+    if value is None and not enforced():
+        return None
+    return {'declared_actor': actor(value), 'authenticated_actor': authenticate(who)}
+
+@contextmanager
+def scope(value):
+    token = current.set(value)
+    try:
+        yield
+    finally:
+        current.reset(token)
+
+def bind_hash(args):
+    result = {k: v for k, v in args.items() if k != 'declared_actor'}
+    if current.get() is not None:
+        result['_declaration'] = dict(current.get())
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
diff --git a/claude/helper/mcp_host_helper.py b/claude/helper/mcp_host_helper.py
index 151df0d..5875b5e 100644
--- a/claude/helper/mcp_host_helper.py
+++ b/claude/helper/mcp_host_helper.py
@@ -31,6 +31,7 @@ import tempfile
 import time
 import uuid
 import hvu_signals
+import declaration_contract as declaration
 import p02_snapshot as P02
 import unicodedata
 import urllib.parse
@@ -2106,6 +2107,15 @@ def handle(fname: str) -> None:
             raise Refuse("off_menu", f"hành động ngoài thực đơn: {str(action)[:60]!r}")
         if isinstance(req.get("deadline"), (int, float)) and time.time() > req["deadline"]:
             raise Refuse("expired", "yêu cầu đã quá hạn chờ — không thực hiện")
+        carried = a.pop('_declaration', None)
+        declaration.current.set(None)
+        if action in ('gh_put_commit_push','gh_apply_commit_push','gh_move','gh_revert_commit_push','ui_commit','ui_move'):
+            try:
+                if carried is None and declaration.enforced():
+                    raise declaration.Denied('LEGACY_JOB_UNATTRIBUTED')
+                declaration.current.set(declaration.resolve({}, dict(hvu_signals.hidden() or {}, authenticated=bool(hvu_signals.hidden())), carried))
+            except declaration.Denied as error:
+                raise Refuse(error.code, error.detail)
         payload = None
         if req.get("payload") is not None:
             payload_name = req["payload"]
@@ -2137,7 +2147,7 @@ def handle(fname: str) -> None:
                     res['_hvu_work_ids'] = hvu_signals.work_ids('',{'root':a.get('root'),'ops':[{'path':v} for v in out_text(changed).splitlines()]})
             except Exception:
                 pass
-        answer(rid, {"ok": True, **res})
+        answer(rid, declaration.receipt({"ok": True, **res}))
         log(f"OK id={rid[:8]} action={action} {summary} ms={int((time.time() - t0) * 1000)}")
     except Refuse as e:
         answer(rid if re.fullmatch(r"[0-9a-f]{32}", rid) else "0" * 32, {"ok": False, "reason": e.reason, "error": e.msg})
@@ -2149,6 +2159,7 @@ def handle(fname: str) -> None:
         answer(rid, {"ok": False, "reason": "helper_error", "error": f"{type(e).__name__}: {mask(str(e))[:300]}"})
         log(f"ERROR id={rid[:8]} action={action} {summary} {type(e).__name__}: {mask(str(e))[:300]}")
     finally:
+        declaration.current.set(None)
         hvu_signals.identity.set(None)
         try:
             os.replace(src, os.path.join(Q_DONE, fname))  # requests are kept (tiny)
diff --git a/shared/declaration_contract.py b/shared/declaration_contract.py
new file mode 100644
index 0000000..260b783
--- /dev/null
+++ b/shared/declaration_contract.py
@@ -0,0 +1,77 @@
+"""RUN12 single declaration contract. Packaged byte-identically in both gateways/helper.
+Self declaration is attribution, never authentication or an authorization grant.
+Advertise is the compatibility default; operator enforcement is a separate rollout.
+"""
+import contextvars
+import json
+import os
+from contextlib import contextmanager
+
+DESCRIPTION = ('Before writing, pass declared_actor: your AI name (example: "Codex Worker"). '
+               'This is self declaration, not a new credential. If DECLARATION_REQUIRED, '
+               'repeat the same call with your name; no ticket or Owner action is needed. '
+               'One declaration is carried through upload chunks and queued work.')
+FIELD = {'description': DESCRIPTION}  # Validate here, not in transport, to return actionable errors.
+current = contextvars.ContextVar('write_declaration', default=None)
+
+class Denied(Exception):
+    def __init__(self, code='DECLARATION_REQUIRED', detail=DESCRIPTION):
+        self.code, self.detail = code, detail
+        super().__init__(detail)
+    def result(self):
+        return {'error': self.code, 'detail': self.detail, 'field': 'declared_actor',
+                'example': {'declared_actor': 'Codex Worker'}, 'mutation': 'none'}
+
+def enforced():
+    mode = os.environ.get('WORKSPACE_DECLARATION_MODE', 'advertise')
+    if mode not in ('advertise', 'enforce'):
+        raise Denied('DECLARATION_MODE_INVALID', 'Operator must select advertise or enforce.')
+    return mode == 'enforce'
+
+def actor(value):
+    if not isinstance(value, str) or not value.strip() or any(not c.isprintable() for c in value):
+        raise Denied()
+    return value.strip()
+
+def authenticate(who):
+    if not isinstance(who, dict) or who.get('authenticated') is not True or not who.get('label'):
+        raise Denied('AUTHENTICATED_ACTOR_REQUIRED', 'A trusted Gateway credential is required; self declaration cannot grant access.')
+    return who['label']
+
+def resolve(args, who, carried=None):
+    """Only trusted adapters may supply carried (persisted server-owned metadata)."""
+    value = args.get('declared_actor')
+    if carried is not None:
+        if not isinstance(carried, dict) or set(carried) != {'declared_actor', 'authenticated_actor'}:
+            raise Denied('DECLARATION_CONTEXT_INVALID')
+        expected = {'declared_actor': actor(carried['declared_actor']), 'authenticated_actor': authenticate(who)}
+        if expected != carried or (value is not None and actor(value) != carried['declared_actor']):
+            raise Denied('DECLARATION_ACTOR_MISMATCH', 'Retry with the original actor and credential, or begin a new logical write.')
+        return dict(carried)
+    if value is None and not enforced():
+        return None
+    return {'declared_actor': actor(value), 'authenticated_actor': authenticate(who)}
+
+@contextmanager
+def scope(value):
+    token = current.set(value)
+    try:
+        yield
+    finally:
+        current.reset(token)
+
+def bind_hash(args):
+    result = {k: v for k, v in args.items() if k != 'declared_actor'}
+    if current.get() is not None:
+        result['_declaration'] = dict(current.get())
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
```
