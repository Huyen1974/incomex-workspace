# Source manifest

```json
{
  "run": "HJW-G8-FS-HELPER-LOCAL-GIT-20261029-16",
  "git_base": "00452246b1ac499d2e62cba8ea12be2aee919f2b",
  "base_image": "sha256:bacd21605a06825d0a725bcaefecdf55abbe85e075ab7be8fe93da3e04b5f961",
  "scoped_patch_sha256": "d266db6c18237f9875529bfbce3d43f4357eca696e9cccff8a34e84501ef2bd7",
  "files": [
    {
      "path": "claude-mcp/app/__init__.py",
      "canonical": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "runtime_baseline": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "candidate": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "provenance": "SOURCE-PINNED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/app/audit.py",
      "canonical": "243a4cf5b1b40519210674c8f27acf4eb5055547a89b6daf39b507d223fe0044",
      "runtime_baseline": "243a4cf5b1b40519210674c8f27acf4eb5055547a89b6daf39b507d223fe0044",
      "candidate": "243a4cf5b1b40519210674c8f27acf4eb5055547a89b6daf39b507d223fe0044",
      "provenance": "SOURCE-PINNED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/app/declaration_contract.py",
      "canonical": null,
      "runtime_baseline": null,
      "candidate": "bdcf9131c6681e82e8d8bfe4b1497fab52815ecec0e29989f4429d79aacb4e47",
      "provenance": "RECONSTRUCTED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/app/fsroots.py",
      "canonical": "46975a735b3d54206aaef2172fd2bd9ee5add090cf1cc969ab14c4a8754b5612",
      "runtime_baseline": "46975a735b3d54206aaef2172fd2bd9ee5add090cf1cc969ab14c4a8754b5612",
      "candidate": "392cee632d28174166a8d798f2a4ddc8f181d3610d83ecb561b79bb3a85d9197",
      "provenance": "RECONSTRUCTED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/app/hostq.py",
      "canonical": "4c34e0ffe2d39310b00a6f9f8d3e2d214f5ea25309d8c848e68a3799e11484d1",
      "runtime_baseline": "4c34e0ffe2d39310b00a6f9f8d3e2d214f5ea25309d8c848e68a3799e11484d1",
      "candidate": "4eab7af3436dde7277a762728b554c7dd067f26387f6276b5c9f1d49a9b5ffcd",
      "provenance": "RECONSTRUCTED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/app/hosttools.py",
      "canonical": "24621bf0553057983fd6a8214f9e9390df7079e17f2300fe7a81f5c26fa2c8d7",
      "runtime_baseline": "24621bf0553057983fd6a8214f9e9390df7079e17f2300fe7a81f5c26fa2c8d7",
      "candidate": "24621bf0553057983fd6a8214f9e9390df7079e17f2300fe7a81f5c26fa2c8d7",
      "provenance": "SOURCE-PINNED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/app/hvu_signals.py",
      "canonical": "912b655446fd5487d441525041ca4b0e12ffa6699dd36eafa89e9153d895382e",
      "runtime_baseline": "912b655446fd5487d441525041ca4b0e12ffa6699dd36eafa89e9153d895382e",
      "candidate": "912b655446fd5487d441525041ca4b0e12ffa6699dd36eafa89e9153d895382e",
      "provenance": "SOURCE-PINNED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/app/limits.py",
      "canonical": "7b37290046b96eeb19e81fc3342c9f38f1319e5dbec35f07739c3df0d46c9e29",
      "runtime_baseline": "7b37290046b96eeb19e81fc3342c9f38f1319e5dbec35f07739c3df0d46c9e29",
      "candidate": "7b37290046b96eeb19e81fc3342c9f38f1319e5dbec35f07739c3df0d46c9e29",
      "provenance": "SOURCE-PINNED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/app/sanitize.py",
      "canonical": "403421a94bb3f6260b38cff71ffb11b4a417ac727c30d9c859392cfa5dae66ff",
      "runtime_baseline": "403421a94bb3f6260b38cff71ffb11b4a417ac727c30d9c859392cfa5dae66ff",
      "candidate": "403421a94bb3f6260b38cff71ffb11b4a417ac727c30d9c859392cfa5dae66ff",
      "provenance": "SOURCE-PINNED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/app/server.py",
      "canonical": "d14c6a1278f6a587f62359577acb75dbdebbf09317a4b3204c05f7c959381992",
      "runtime_baseline": "422dd29578daac04d626509c556a6f981d90665d0ae598d4499eb5703faa28d9",
      "candidate": "ea6756dcf97dceeb350ecaff6fb94ea8df865c73c501200b7ca5b70d1a16407c",
      "provenance": "RECONSTRUCTED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/app/sqlguard.py",
      "canonical": "c43754c70195c9e18e5339e9834b0e4d060ef1788971cce22c0dc87916b3001e",
      "runtime_baseline": "c43754c70195c9e18e5339e9834b0e4d060ef1788971cce22c0dc87916b3001e",
      "candidate": "c43754c70195c9e18e5339e9834b0e4d060ef1788971cce22c0dc87916b3001e",
      "provenance": "SOURCE-PINNED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/app/tools.py",
      "canonical": "363f9131c140fa148d62456ac1539c6889f9c53e1eaf2dd0d97ea063b8df6484",
      "runtime_baseline": "363f9131c140fa148d62456ac1539c6889f9c53e1eaf2dd0d97ea063b8df6484",
      "candidate": "363f9131c140fa148d62456ac1539c6889f9c53e1eaf2dd0d97ea063b8df6484",
      "provenance": "SOURCE-PINNED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/helper/declaration_contract.py",
      "canonical": null,
      "runtime_baseline": null,
      "candidate": "bdcf9131c6681e82e8d8bfe4b1497fab52815ecec0e29989f4429d79aacb4e47",
      "provenance": "RECONSTRUCTED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/helper/hvu_signals.py",
      "canonical": "912b655446fd5487d441525041ca4b0e12ffa6699dd36eafa89e9153d895382e",
      "runtime_baseline": "912b655446fd5487d441525041ca4b0e12ffa6699dd36eafa89e9153d895382e",
      "candidate": "912b655446fd5487d441525041ca4b0e12ffa6699dd36eafa89e9153d895382e",
      "provenance": "SOURCE-PINNED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/helper/mcp_host_helper.py",
      "canonical": "e5790c74edbb24575c5015982953d98aa8165657574b4782df18a49382710f11",
      "runtime_baseline": "e5790c74edbb24575c5015982953d98aa8165657574b4782df18a49382710f11",
      "candidate": "7ab59d5a843c0625b1500da54e212849b16d816e70984f86718a446edbc8f643",
      "provenance": "RECONSTRUCTED",
      "source": "pinned runtime + RUN14 scoped patch"
    },
    {
      "path": "claude-mcp/helper/p02_snapshot.py",
      "canonical": "e68e5e9271d53fa97cb04bd048d51ea448957427a313f28c2f37cfc90856ca01",
      "runtime_baseline": "e68e5e9271d53fa97cb04bd048d51ea448957427a313f28c2f37cfc90856ca01",
      "candidate": "e68e5e9271d53fa97cb04bd048d51ea448957427a313f28c2f37cfc90856ca01",
      "provenance": "SOURCE-PINNED",
      "source": "pinned runtime + RUN14 scoped patch"
    }
  ],
  "consumer_mapping": {
    "claude": "candidate only",
    "gemini": "shared canonical source; live original unchanged; do not rebuild",
    "helper": "shared; candidate only",
    "agent_data_hermes": "excluded"
  },
  "release_ref": "refs/heads/hjw/g8-fs-helper-20261029-16",
  "release_commit": "7e3c04967d054e7a40877d00c264aaee623546d1",
  "candidate_image": "sha256:5fb82e3a1296c06b19d04610c06081ff750a2da803eab65183548a664250b351"
}
```
