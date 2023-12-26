# Dockerfile (React)
FROM node:16-slim
WORKDIR /usr/src/app
COPY ./vite-project/package*.json .
# Docker frontend 起動時のエラーを解消するためのパッケージ
RUN npm i @rollup/rollup-linux-arm64-musl && npm i @rollup/rollup-linux-arm64-gnu
# yarn が必要な場合は、都度インストール。
RUN npm i
COPY ./vite-project .
CMD npm run dev
