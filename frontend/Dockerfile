# 使用 Node.js 构建前端代码
FROM node:23.5 as builder
WORKDIR /app

# 安装 pnpm
RUN corepack enable && corepack prepare pnpm@latest --activate

# 复制代码并安装依赖
COPY . .
RUN pnpm install && pnpm run build

# 第二阶段：使用 nginx 提供静态文件服务
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
#EXPOSE 80 443  # 暴露端口
#CMD ["nginx", "-g", "daemon off;"]
