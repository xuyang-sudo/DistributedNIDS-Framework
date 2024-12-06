#!/bin/bash

# 构建 Docker 镜像
docker-compose build

# 启动所有服务
docker-compose up -d

echo "部署完成。访问 http://localhost:8080 查看。"
