FROM node:22-bookworm-slim
ARG RUNNER_VERSION=2.338.1
ARG RUNNER_SHA256=08e9ccb3604d2462c24b5e33604dc30810296ca15cc65f23cffd4317eb144c37
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl git python3 python3-venv libicu72 libssl3 libkrb5-3 zlib1g liblttng-ust1 util-linux procps && rm -rf /var/lib/apt/lists/*
RUN npm install --global pnpm@9.6.0
RUN groupadd --gid 10001 ci && useradd --uid 10001 --gid ci --create-home runner && mkdir -p /runner-template /runner /ci-lock && chown runner:ci /runner /ci-lock
RUN curl --fail --location --retry 3 --output /tmp/runner.tar.gz https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz && echo "${RUNNER_SHA256}  /tmp/runner.tar.gz" | sha256sum --check --status && tar xzf /tmp/runner.tar.gz -C /runner-template && rm /tmp/runner.tar.gz && chown -R runner:ci /runner-template
COPY ci-cleanup.sh /usr/local/bin/ci-cleanup.sh
RUN chmod 755 /usr/local/bin/ci-cleanup.sh
ENV ACTIONS_RUNNER_HOOK_JOB_COMPLETED=/usr/local/bin/ci-cleanup.sh
ENV HOME=/runner/home
USER 10001:10001
WORKDIR /runner
CMD ["./run.sh"]
