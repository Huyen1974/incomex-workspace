#!/bin/bash
set -euo pipefail
# Only the per-job checkout is removed; this is hygiene, not a security boundary.
case "${GITHUB_WORKSPACE:-}" in
  /runner/_work/*/*) find "$GITHUB_WORKSPACE" -mindepth 1 -maxdepth 1 -exec rm -rf -- {} + ;;
  *) echo 'No matching CI checkout to clean.' ;;
esac
