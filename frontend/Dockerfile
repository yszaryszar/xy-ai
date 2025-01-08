# 使用 Node.js 构建前端代码
FROM node:23.5 as builder
WORKDIR /app

# 安装 pnpm
RUN corepack enable && corepack prepare pnpm@latest --activate

# 复制代码并安装依赖
COPY . .
RUN pnpm install && pnpm run build

# 第二阶段：仅包含构建产物
FROM alpine
WORKDIR /frontend-dist
COPY --from=builder /app/dist .
