# 使用官方 Nginx 镜像
FROM nginx:latest

# 复制 Nginx 配置文件
COPY nginx.conf /etc/nginx/nginx.conf

# 设置工作目录
WORKDIR /etc/nginx

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]
