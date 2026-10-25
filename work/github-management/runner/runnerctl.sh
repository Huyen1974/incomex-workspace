#!/bin/bash
set -euo pipefail
umask 077
if [[ "${1:-}" == --help ]]; then
  echo 'dot-github-ci-runner — install/start/stop/remove/recreate/verify one bounded GitHub CI runner'
  echo 'Usage: dot-github-ci-runner ACTION agent-data-test|web-test'
  echo 'Install consumes only a short-lived registration token on stdin; root operator with approved RUN and VPS-GHI required.'
  echo 'No deploy. Remove is per-repo and retains the private data volume.'
  exit 0
fi
action=${1:?install|start|stop|remove|verify}
repo=${2:?agent-data-test|web-test}
case "$repo" in agent-data-test|web-test) ;; *) exit 64 ;; esac
name="ghm-ci-$repo"
volume="${name}-data"
image='incomex-ci-runner:2.338.1-c1a'
create_runner() {
  docker create --name "$name" --restart unless-stopped --stop-signal SIGINT --stop-timeout 30 --init --network ghm-ci --user 10001:10001 --cap-drop ALL --security-opt no-new-privileges --pids-limit 256 --cpus 1 --memory 1536m --memory-swap 1536m --log-opt max-size=10m --log-opt max-file=2 --mount "type=volume,src=$volume,dst=/runner" --mount type=volume,src=ghm-ci-build-lock,dst=/ci-lock "$image" >/dev/null
  docker start "$name" >/dev/null
}
case "$action" in
 install)
  if docker container inspect "$name" >/dev/null 2>&1; then echo 'Container exists; use verify/start'; exit 1; fi
  docker network inspect ghm-ci >/dev/null 2>&1 || docker network create ghm-ci >/dev/null
  docker volume create "$volume" >/dev/null
  docker volume create ghm-ci-build-lock >/dev/null
  docker run --rm --network none --user 0:0 --cpus 1 --memory 256m --memory-swap 256m --mount "type=volume,src=$volume,dst=/runner" --mount type=volume,src=ghm-ci-build-lock,dst=/ci-lock "$image" bash -c 'cp -a /runner-template/. /runner/; mkdir -p /runner/home; chown -R 10001:10001 /runner; chmod 700 /runner; touch /ci-lock/build.lock; chown 10001:10001 /ci-lock/build.lock; chmod 600 /ci-lock/build.lock' >/dev/null
  # Short-lived registration token comes ONLY over encrypted stdin, never argv or Docker Env.
  docker run --rm -i --network ghm-ci --user 10001:10001 --cap-drop ALL --security-opt no-new-privileges --cpus 1 --memory 512m --memory-swap 512m --mount "type=volume,src=$volume,dst=/runner" "$image" bash -c 'set -e; IFS= read -r ACTIONS_RUNNER_INPUT_TOKEN; export ACTIONS_RUNNER_INPUT_TOKEN; umask 077; ./config.sh --unattended --url "$1" --name "$2" --labels "$3" --work _work --disableupdate >/runner/configure.log 2>&1; unset ACTIONS_RUNNER_INPUT_TOKEN; chmod 600 /runner/.credentials*; echo REGISTRATION_OK' _ "https://github.com/Huyen1974/$repo" "$name" "ghm-c1a-$repo"
  create_runner
  echo "STARTED $name" ;;
 recreate)
  # Operator must first verify the GitHub runner is idle; preserves registration and private data.
  docker volume inspect "$volume" >/dev/null
  docker stop --time 30 "$name" >/dev/null
  docker rm "$name" >/dev/null
  create_runner
  echo "RECREATED $name" ;;
 start|stop) docker "$action" "$name" >/dev/null; echo "$action $name" ;;
 remove)
  # Remove only this CI container. Volumes retain credentials until GitHub registration is revoked.
  docker rm -f "$name" >/dev/null
  echo "REMOVED $name; GitHub runner registration must also be removed by Mac admin; private volume retained." ;;
 verify)
  docker inspect --format '{{.Name}} user={{.Config.User}} cpu={{.HostConfig.NanoCpus}} memory={{.HostConfig.Memory}} swap={{.HostConfig.MemorySwap}} restart={{.HostConfig.RestartPolicy.Name}} network={{.HostConfig.NetworkMode}} privileged={{.HostConfig.Privileged}} state={{.State.Status}}' "$name" ;;
 *) exit 64 ;;
esac
