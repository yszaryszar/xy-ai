# 使用官方 Nginx 镜像
FROM nginx:alpine

# 复制 Nginx 配置文件
COPY ./nginx.conf /etc/nginx/nginx.conf

# 复制前端构建的静态文件到 Nginx
#COPY ../frontend/dist /usr/share/nginx/html

# 暴露端口
EXPOSE 80 443
