# 使用官方 Snort 镜像作为基础
FROM ubuntu:20.04

# 安装必要的软件包
RUN apt-get update && \
    apt-get install -y snort && \
    apt-get clean

# 复制 Snort 配置文件
COPY snort.conf /etc/snort/snort.conf

# 设置工作目录
WORKDIR /etc/snort

# 启动 Snort
CMD ["snort", "-c", "/etc/snort/snort.conf", "-i", "eth0"]