# Dockerfile (React)
FROM node:16-alpine
WORKDIR /app
COPY ./vite-project/package*.json ./
# Docker frontend 起動時のエラーを解消するためのパッケージ
RUN npm i @rollup/rollup-linux-arm64-musl
# yarn が必要な場合は、都度インストール。
RUN npm i
COPY ./vite-project .
CMD npm run dev
