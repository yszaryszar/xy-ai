# 使用 Node.js 构建前端
FROM node:23.5 as builder
WORKDIR /app

# 安装 pnpm
RUN corepack enable && corepack prepare pnpm@latest --activate

# 复制前端代码并安装依赖
COPY . .
RUN pnpm install && pnpm run build

# 输出构建产物到指定目录
CMD ["cp", "-r", "dist", "/frontend-dist"]
