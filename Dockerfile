FROM python:3.11-slim AS build

WORKDIR /app

RUN <<EOF
apt-get update
apt-get install -y default-libmysqlclient-dev build-essential pkg-config
EOF

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY . .

FROM build as development

RUN <<EOF
apt-get install -y --no-install-recommends git
EOF

RUN <<EOF
useradd -s /bin/bash -m vscode
groupadd docker
usermod -aG docker vscode
EOF

RUN <<EOF
chmod +x prestart.dev.sh
chmod +x run.dev.sh
EOF

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /

CMD ["./run.dev.sh"]
# CMD [python3]

