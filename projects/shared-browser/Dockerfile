# Official images pinned by digest; rebuild periodically for browser security fixes.
FROM node:24-bookworm-slim@sha256:d6aa754f16b3197301076f047b5def2f02ea1dbbc2ca920407d46d7ec7f87b20
RUN --mount=type=secret,id=proxy,required=false \
    if [ -f /run/secrets/proxy ]; then export http_proxy="$(cat /run/secrets/proxy)" https_proxy="$(cat /run/secrets/proxy)"; fi; \
    apt-get update && apt-get install -y --no-install-recommends chromium xvfb x11vnc ca-certificates fonts-liberation fonts-dejavu-core libnss3-tools && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=secret,id=proxy,required=false --mount=type=secret,id=ca,required=false \
    if [ -f /run/secrets/ca ]; then export NODE_EXTRA_CA_CERTS=/run/secrets/ca; fi; \
    if [ -f /run/secrets/proxy ]; then export https_proxy="$(cat /run/secrets/proxy)" HTTPS_PROXY="$(cat /run/secrets/proxy)"; fi; \
    npm ci --ignore-scripts --no-audit --no-fund
COPY . .
RUN npm run build && mkdir -p /data /tmp/.X11-unix && chown -R node:node /app /data /tmp/.X11-unix
USER node
ENV BROWSER_DATA_DIR=/data/gateway BROWSER_PROFILE_DIR=/data/profile GATEWAY_BIND=0.0.0.0
EXPOSE 8787
ENTRYPOINT ["node","supervisor.mjs"]
