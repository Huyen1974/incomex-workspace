# RUN17 source manifest

```json
{
  "gh_main": "b4c9ea19cf2e57594a231c2819e098fe0002c99a",
  "pr357_head": "36c682914c9f412078113b6d85319f11356d1130",
  "runtime_source": "1cc706dc0f1ba7ef05f4631c04f604d2cacd9982",
  "runtime_image": "sha256:4635e417e5400a9f85d1ed569f1c2f977845405bf7b8d834ab7002006f7d1045",
  "files": [
    {
      "path": "agent_data/declaration_contract.py",
      "gh_base": null,
      "gh_candidate": "bdcf9131c6681e82e8d8bfe4b1497fab52815ecec0e29989f4429d79aacb4e47",
      "runtime_base": null,
      "runtime_candidate": "bdcf9131c6681e82e8d8bfe4b1497fab52815ecec0e29989f4429d79aacb4e47",
      "source_d2": null
    },
    {
      "path": "agent_data/workspace_declaration.py",
      "gh_base": null,
      "gh_candidate": "51d3b948a8f3c9f27fe2f075c5f8207c55fc74da0d4577463f0c59f6747a2dd6",
      "runtime_base": null,
      "runtime_candidate": "51d3b948a8f3c9f27fe2f075c5f8207c55fc74da0d4577463f0c59f6747a2dd6",
      "source_d2": null
    },
    {
      "path": "agent_data/workspace_idempotency.py",
      "gh_base": "90d5e3f936fa027dff4f40c080bd63f9eb41ab2a3d671177391527d9964d1a66",
      "gh_candidate": "643e515e21d0baa2b5a3b902b5924b6cd13fbc6a5d65f51298227a7ad1003652",
      "runtime_base": "90d5e3f936fa027dff4f40c080bd63f9eb41ab2a3d671177391527d9964d1a66",
      "runtime_candidate": "643e515e21d0baa2b5a3b902b5924b6cd13fbc6a5d65f51298227a7ad1003652",
      "source_d2": "90d5e3f936fa027dff4f40c080bd63f9eb41ab2a3d671177391527d9964d1a66"
    },
    {
      "path": "agent_data/workspace_tasks.py",
      "gh_base": "292142cacd2f832569a66c288b668971667b13b76c8ae11f40b604052692e930",
      "gh_candidate": "e15e2d8cb4a67436aee114a768563cf63181c3ef19534d9e5f52b10e22fd7f05",
      "runtime_base": "ca84034e0ed6eba0124fff6f63a54cb8f92563f3cbc3805c0ed69653f0b6f796",
      "runtime_candidate": "c17768e71f909bf1f162ed85b010ac979d108436ebb7d48fd8eb12527bc7bc77",
      "source_d2": "ca84034e0ed6eba0124fff6f63a54cb8f92563f3cbc3805c0ed69653f0b6f796"
    },
    {
      "path": "agent_data/workspace_tools.py",
      "gh_base": "84ed31d64c7d517205de0de641633bbf6252a727b54084b7eccdb032ac5a907b",
      "gh_candidate": "af2b47da0b38661a120d975d9e5a0b25f338c74c930798fbbcc2dce7312a66a5",
      "runtime_base": "d3f22b9285f5e7a2b14cb737c7cb1cb6d3f16640a3c412bfcc53c7016c6ec55b",
      "runtime_candidate": "6eebfe26123a3f341e43b3257b52963511b3302420bf933ada71ff9d5bfd75c9",
      "source_d2": "84ed31d64c7d517205de0de641633bbf6252a727b54084b7eccdb032ac5a907b"
    },
    {
      "path": "agent_data/workspace_transfer.py",
      "gh_base": "d2863b7d381a8b71b1e600baa118e94e589ece7c8107b0c25cca8479d164e97b",
      "gh_candidate": "ef79fed44727ff68f478476b776fc7088d2e482a905bc407042257ba034cf781",
      "runtime_base": "d2863b7d381a8b71b1e600baa118e94e589ece7c8107b0c25cca8479d164e97b",
      "runtime_candidate": "ef79fed44727ff68f478476b776fc7088d2e482a905bc407042257ba034cf781",
      "source_d2": "d2863b7d381a8b71b1e600baa118e94e589ece7c8107b0c25cca8479d164e97b"
    }
  ],
  "pr357_queue_files_runtime_byte_equal": true,
  "queue_logic_preserved": true,
  "hermes_source_prefix_unchanged": true,
  "pr_url": "https://github.com/Huyen1974/agent-data-test/pull/358",
  "pr_head": "4851f6cde86bade6ce70433958cddc76a307f9f1",
  "branch": "dev/codex-ad/hjw-g8-four-facts-20261030",
  "runtime_worker_count": 4,
  "gh_diff_sha256": "b0b99cca2b4bccc71abbf3ce173574205dc6c26b38d9d9d6e2c1a9ee295f00b0",
  "runtime_diff_sha256": "94517824b03280fff5a7d1c0815dd20c38c1f0e97469e3d08163439a3ae1d7ac",
  "tests": {
    "conftest.py": "a969c8a4b00efb4889f93efdb4aa3e9fd4c468b3191f1c2039d7f162d3126fe6",
    "test_contract.py": "0586b7df7b1bf8b55196f12e864e1df0be352511fa685f43d7262b3d5c488ec2",
    "test_runtime_queue.py": "e532f6649b6d51ab887827e2d22bdad7ae2b2f2eeec09774cba42b8f95725a46",
    "test_ad.py": "a14a32619ba68ba7b8bd25b07460e58c7b6aa21162a0ca55f3ca965781087268",
    "test_acl.py": "1796fa35c447fe09c88eab03194f72b1d1eb2b19da76ceea124115b537abc07c",
    "test_four_facts.py": "20367f5249ff383a10ee56a06da0fe47973f8d8b26fc1daabdadd394e54a59aa"
  }
}
```
