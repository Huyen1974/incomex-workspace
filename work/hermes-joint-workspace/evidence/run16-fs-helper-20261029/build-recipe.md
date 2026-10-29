# Committed build recipe

`claude-mcp/release/run16/build.sh` at final ref.

```sh
#!/bin/sh
# Run from this candidate Git worktree, never the live checkout.
set -eu
repo=$(git rev-parse --show-toplevel)
ref=$(git rev-parse HEAD)
context=$(mktemp -d /tmp/hjw-run16-build.XXXXXX)
trap 'rm -rf "$context"' EXIT HUP INT TERM
git -C "$repo" archive "$ref" claude-mcp/app claude-mcp/release/run16 | tar -x -C "$context"
# Git archive uses tar.umask; normalize immutable app source to original image modes.
find "$context/claude-mcp/app" -type d -exec chmod 755 {} +
find "$context/claude-mcp/app" -type f -exec chmod 644 {} +
DOCKER_BUILDKIT=0 docker build --network none --pull=false -t hjw-run16-fs:candidate -f "$context/claude-mcp/release/run16/Dockerfile" "$context"
```
