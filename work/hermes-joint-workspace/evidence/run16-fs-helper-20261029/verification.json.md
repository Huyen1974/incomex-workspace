# Verification receipts

```json
{
  "source": {
    "manifest_file_count": 16,
    "helper_functions_unchanged_except": [
      "handle"
    ],
    "rollback_files_verified": 14,
    "rollback_contracts_removed": true,
    "live_source_hashes_unchanged": true,
    "secret_pattern_scan": "PASS",
    "source_scope": "Claude/fs + helper only"
  },
  "image": {
    "release_commit": "7e3c04967d054e7a40877d00c264aaee623546d1",
    "base": "sha256:bacd21605a06825d0a725bcaefecdf55abbe85e075ab7be8fe93da3e04b5f961",
    "candidate": "sha256:5fb82e3a1296c06b19d04610c06081ff750a2da803eab65183548a664250b351",
    "run14_candidate": "sha256:ae6f4f7204298a365afa3a73c91a69b01bd872910024d5c275ca088824119cde",
    "base_layers_preserved": true,
    "additional_filesystem_layers": 1,
    "app_hashes": {
      "audit.py": "243a4cf5b1b40519210674c8f27acf4eb5055547a89b6daf39b507d223fe0044",
      "sqlguard.py": "c43754c70195c9e18e5339e9834b0e4d060ef1788971cce22c0dc87916b3001e",
      "tools.py": "363f9131c140fa148d62456ac1539c6889f9c53e1eaf2dd0d97ea063b8df6484",
      "server.py": "ea6756dcf97dceeb350ecaff6fb94ea8df865c73c501200b7ca5b70d1a16407c",
      "sanitize.py": "403421a94bb3f6260b38cff71ffb11b4a417ac727c30d9c859392cfa5dae66ff",
      "__init__.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "limits.py": "7b37290046b96eeb19e81fc3342c9f38f1319e5dbec35f07739c3df0d46c9e29",
      "hvu_signals.py": "912b655446fd5487d441525041ca4b0e12ffa6699dd36eafa89e9153d895382e",
      "declaration_contract.py": "bdcf9131c6681e82e8d8bfe4b1497fab52815ecec0e29989f4429d79aacb4e47",
      "hostq.py": "4eab7af3436dde7277a762728b554c7dd067f26387f6276b5c9f1d49a9b5ffcd",
      "hosttools.py": "24621bf0553057983fd6a8214f9e9390df7079e17f2300fe7a81f5c26fa2c8d7",
      "fsroots.py": "392cee632d28174166a8d798f2a4ddc8f181d3610d83ecb561b79bb3a85d9197"
    },
    "run14_app_byte_parity": true,
    "run14_nonexecutable_appledouble_removed": {
      "._sanitize.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b",
      "._tools.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b",
      "._server.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b",
      "._audit.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b",
      "._hostq.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b",
      "._limits.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b",
      "._sqlguard.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b",
      "._fsroots.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b",
      ".___init__.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b",
      "._declaration_contract.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b",
      "._hvu_signals.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b",
      "._hosttools.py": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
    },
    "entrypoint_cmd_user_workdir_ports_unchanged": true,
    "image_ids_equal": false,
    "config_diff_from_run14": {
      "Labels": {
        "run14": {
          "com.docker.compose.project": "claude-mcp",
          "com.docker.compose.service": "claude-mcp",
          "com.docker.compose.version": "5.0.2",
          "incomex.candidate.run": "HJW-DECLARATION-GATE-FOUR-FACTS-20261029-14"
        },
        "run16": {
          "com.docker.compose.project": "claude-mcp",
          "com.docker.compose.service": "claude-mcp",
          "com.docker.compose.version": "5.0.2",
          "incomex.candidate.run": "HJW-G8-FS-HELPER-LOCAL-GIT-20261029-16"
        }
      }
    },
    "run14_last_layer": "sha256:36562dab96a6bc78dad827793f23d2191cf8f1a623f1ec7c0e7059ea3fa5ef41",
    "run16_last_layer": "sha256:153afd3fd4cfad8a6964f7385a9fd6af866ee893d958bb3b81dc6e78379a5b7e",
    "live_images_unchanged": true,
    "live_surface_labels": {
      "/incomex-claude-mcp": null,
      "/incomex-gemini-mcp": "gemini-agy [auth:google-main]"
    }
  },
  "http": {
    "kind": "fs",
    "platform": "linux",
    "http_schema": true,
    "missing_isError": true,
    "zero_mutation": true,
    "write_receipt": {
      "content": [
        {
          "type": "text",
          "text": "OK fs_write root=fixture path=canary.md tạo mới 23B · operation_id=linux-http-01\nversion: - -> 5f05ed16a6e75325 · commit=- · gốc này không có sổ git\nDECLARATION_RECEIPT {\"alias_version\": \"1\", \"authenticated_actor\": \"Anthropic/ClaudeAI [auth:claude-chat]\", \"command_kind\": \"RUN\", \"contract_version\": \"four-facts-1\", \"declared_actor\": \"gpt-live\", \"facts\": {\"command_ref\": {\"canonical\": \"RUN-HTTP-FIXTURE\", \"provenance\": \"self_declared\", \"raw\": \"RUN-HTTP-FIXTURE\"}, \"declared_actor\": {\"canonical\": \"gpt-live\", \"provenance\": \"self_declared\", \"raw\": \"GPT Live\"}, \"origin_environment\": {\"canonical\": \"macbook\", \"provenance\": \"self_declared\", \"raw\": \"macbok\"}, \"task_id\": {\"canonical\": \"fixture\", \"provenance\": \"self_declared\", \"raw\": \"fixture\"}}, \"flags\": [], \"normalizer_version\": \"four-facts-1\"}"
        }
      ],
      "structuredContent": {
        "result": "OK fs_write root=fixture path=canary.md tạo mới 23B · operation_id=linux-http-01\nversion: - -> 5f05ed16a6e75325 · commit=- · gốc này không có sổ git\nDECLARATION_RECEIPT {\"alias_version\": \"1\", \"authenticated_actor\": \"Anthropic/ClaudeAI [auth:claude-chat]\", \"command_kind\": \"RUN\", \"contract_version\": \"four-facts-1\", \"declared_actor\": \"gpt-live\", \"facts\": {\"command_ref\": {\"canonical\": \"RUN-HTTP-FIXTURE\", \"provenance\": \"self_declared\", \"raw\": \"RUN-HTTP-FIXTURE\"}, \"declared_actor\": {\"canonical\": \"gpt-live\", \"provenance\": \"self_declared\", \"raw\": \"GPT Live\"}, \"origin_environment\": {\"canonical\": \"macbook\", \"provenance\": \"self_declared\", \"raw\": \"macbok\"}, \"task_id\": {\"canonical\": \"fixture\", \"provenance\": \"self_declared\", \"raw\": \"fixture\"}}, \"flags\": [], \"normalizer_version\": \"four-facts-1\"}"
      },
      "isError": false
    },
    "replay": {
      "content": [
        {
          "type": "text",
          "text": "[REPLAY operation_id=linux-http-01 — thao tác này ĐÃ thực hiện lúc 2026-10-29T10:44:25Z; không làm lại, trả kết quả đã ghi]\nOK fs_write root=fixture path=canary.md tạo mới 23B · operation_id=linux-http-01\nversion: - -> 5f05ed16a6e75325 · commit=- · gốc này không có sổ git\nDECLARATION_RECEIPT {\"alias_version\": \"1\", \"authenticated_actor\": \"Anthropic/ClaudeAI [auth:claude-chat]\", \"command_kind\": \"RUN\", \"contract_version\": \"four-facts-1\", \"declared_actor\": \"gpt-live\", \"facts\": {\"command_ref\": {\"canonical\": \"RUN-HTTP-FIXTURE\", \"provenance\": \"self_declared\", \"raw\": \"RUN-HTTP-FIXTURE\"}, \"declared_actor\": {\"canonical\": \"gpt-live\", \"provenance\": \"self_declared\", \"raw\": \"GPT Live\"}, \"origin_environment\": {\"canonical\": \"macbook\", \"provenance\": \"self_declared\", \"raw\": \"macbok\"}, \"task_id\": {\"canonical\": \"fixture\", \"provenance\": \"self_declared\", \"raw\": \"fixture\"}}, \"flags\": [], \"normalizer_version\": \"four-facts-1\"}"
        }
      ],
      "structuredContent": {
        "result": "[REPLAY operation_id=linux-http-01 — thao tác này ĐÃ thực hiện lúc 2026-10-29T10:44:25Z; không làm lại, trả kết quả đã ghi]\nOK fs_write root=fixture path=canary.md tạo mới 23B · operation_id=linux-http-01\nversion: - -> 5f05ed16a6e75325 · commit=- · gốc này không có sổ git\nDECLARATION_RECEIPT {\"alias_version\": \"1\", \"authenticated_actor\": \"Anthropic/ClaudeAI [auth:claude-chat]\", \"command_kind\": \"RUN\", \"contract_version\": \"four-facts-1\", \"declared_actor\": \"gpt-live\", \"facts\": {\"command_ref\": {\"canonical\": \"RUN-HTTP-FIXTURE\", \"provenance\": \"self_declared\", \"raw\": \"RUN-HTTP-FIXTURE\"}, \"declared_actor\": {\"canonical\": \"gpt-live\", \"provenance\": \"self_declared\", \"raw\": \"GPT Live\"}, \"origin_environment\": {\"canonical\": \"macbook\", \"provenance\": \"self_declared\", \"raw\": \"macbok\"}, \"task_id\": {\"canonical\": \"fixture\", \"provenance\": \"self_declared\", \"raw\": \"fixture\"}}, \"flags\": [], \"normalizer_version\": \"four-facts-1\"}"
      },
      "isError": false
    },
    "changed_facts_conflict": true,
    "lifespan": "on"
  },
  "helper_linux": {
    "linux_helper": "PASS",
    "requests": 15,
    "six_writers_missing_denied": true,
    "six_writers_carried_receipt": true,
    "upload_bytes_and_cleanup": true,
    "legacy_advertise": true,
    "readonly_nonwriter": true,
    "off_menu_denied": true,
    "privileged_actions": "mocked; no external execution"
  },
  "catalog": [
    {
      "surface": "Anthropic/ClaudeAI [auth:claude-chat]",
      "tools": [
        "directus_create",
        "directus_delete",
        "directus_read",
        "directus_update",
        "fs_copy",
        "fs_diff",
        "fs_edit",
        "fs_list",
        "fs_log",
        "fs_move",
        "fs_read",
        "fs_search",
        "fs_stat",
        "fs_transaction",
        "fs_write",
        "pg_schema",
        "query_pg",
        "read_file",
        "ui_act",
        "ui_inspect",
        "ui_screenshot",
        "vps_status",
        "write_file"
      ],
      "catalog_names_sha256": "b6a1d817824c6c734d70c1c29287b1787c9d6612b9458ef0c98b19a458eee35c"
    },
    {
      "surface": "Anthropic/ClaudeAI [auth:claude-chat]",
      "tools": [
        "directus_create",
        "directus_delete",
        "directus_read",
        "directus_update",
        "fs_copy",
        "fs_diff",
        "fs_edit",
        "fs_list",
        "fs_log",
        "fs_move",
        "fs_read",
        "fs_search",
        "fs_stat",
        "fs_transaction",
        "fs_write",
        "pg_schema",
        "query_pg",
        "read_file",
        "ui_act",
        "ui_inspect",
        "ui_screenshot",
        "vps_status",
        "write_file"
      ],
      "catalog_names_sha256": "b6a1d817824c6c734d70c1c29287b1787c9d6612b9458ef0c98b19a458eee35c"
    },
    {
      "surface": "gemini-agy [auth:google-main]",
      "tools": [
        "directus_create",
        "directus_delete",
        "directus_read",
        "directus_update",
        "fs_copy",
        "fs_diff",
        "fs_edit",
        "fs_list",
        "fs_log",
        "fs_move",
        "fs_read",
        "fs_search",
        "fs_stat",
        "fs_transaction",
        "fs_write",
        "pg_schema",
        "query_pg",
        "read_file",
        "ui_act",
        "ui_inspect",
        "ui_screenshot",
        "vps_status",
        "write_file"
      ],
      "catalog_names_sha256": "b6a1d817824c6c734d70c1c29287b1787c9d6612b9458ef0c98b19a458eee35c"
    }
  ],
  "metadata_diff": {
    "removed": {
      "/app/app/._tools.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258868000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      },
      "/app/app/._hosttools.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258868000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      },
      "/app/app/._sqlguard.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258868000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      },
      "/app/app/._hostq.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258868000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      },
      "/app/app/._sanitize.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258868000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      },
      "/app/app/._hvu_signals.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258868000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      },
      "/app/app/.___init__.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258868000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      },
      "/app/app/._fsroots.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258868000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      },
      "/app/app/._limits.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258868000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      },
      "/app/app/._audit.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258868000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      },
      "/app/app/._server.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258988000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      },
      "/app/app/._declaration_contract.py": {
        "mode": "0o644",
        "uid": 0,
        "gid": 0,
        "mtime_ns": 1793258951000000000,
        "sha256": "c2d04a808d54bf331dea49d52021018fb65596860939a60afd3e31747ed3f61b"
      }
    },
    "added": {},
    "changed": {
      "/app/app/hvu_signals.py": {
        "mtime_ns": {
          "run14": 1793258868000000000,
          "run16": 1793270424000000000
        }
      },
      "/app/app/__init__.py": {
        "mtime_ns": {
          "run14": 1793258868000000000,
          "run16": 1793270424000000000
        }
      },
      "/app/app/sqlguard.py": {
        "mtime_ns": {
          "run14": 1793258868000000000,
          "run16": 1793270424000000000
        }
      },
      "/app/app/audit.py": {
        "mtime_ns": {
          "run14": 1793258868000000000,
          "run16": 1793270424000000000
        }
      },
      "/app/app/server.py": {
        "mtime_ns": {
          "run14": 1793258988000000000,
          "run16": 1793270424000000000
        }
      },
      "/app/app/limits.py": {
        "mtime_ns": {
          "run14": 1793258868000000000,
          "run16": 1793270424000000000
        }
      },
      "/app/app/hostq.py": {
        "mtime_ns": {
          "run14": 1793258868000000000,
          "run16": 1793270424000000000
        }
      },
      "/app/app/fsroots.py": {
        "mtime_ns": {
          "run14": 1793258868000000000,
          "run16": 1793270424000000000
        }
      },
      "/app/app/tools.py": {
        "mtime_ns": {
          "run14": 1793258868000000000,
          "run16": 1793270424000000000
        }
      },
      "/app/app/hosttools.py": {
        "mtime_ns": {
          "run14": 1793258868000000000,
          "run16": 1793270424000000000
        }
      },
      "/app/app/sanitize.py": {
        "mtime_ns": {
          "run14": 1793258868000000000,
          "run16": 1793270424000000000
        }
      },
      "/app/app/declaration_contract.py": {
        "mtime_ns": {
          "run14": 1793258951000000000,
          "run16": 1793270424000000000
        }
      }
    }
  }
}
```
