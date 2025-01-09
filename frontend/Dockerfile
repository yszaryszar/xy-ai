# 使用官方 Node 镜像
FROM node:23.5-alpine AS builder
WORKDIR /app

# 安装依赖并构建
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm install
COPY . .
RUN pnpm build

# 使用 Nginx 托管静态文件
FROM nginx:alpine AS server
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
