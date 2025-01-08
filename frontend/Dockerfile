# 使用 Node.js 23.5 基础镜像
FROM node:23.5

# 安装 pnpm
RUN npm install -g pnpm

# 设置工作目录
WORKDIR /frontend

# 安装依赖
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

# 复制项目源码
COPY . .

# 构建静态文件
RUN pnpm run build

# 默认运行静态文件服务器（在生产环境中将静态文件交给 Nginx）
CMD ["pnpm", "run", "serve"]
