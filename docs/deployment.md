# 部署指南

## 环境要求

- Docker >= 20.10
- Docker Compose >= 1.29
- 服务器至少 8 核 CPU，16GB 内存

## 安装步骤

1. 克隆仓库

```bash
git clone https://github.com/yourusername/DistributedSnort-Framework.git
cd DistributedSnort-Framework
```

2. 构建Docker镜像

```bash
docker-compose build
```

3. 启动所有服务

```bash
docker-compose up -d
```

4. 检查服务状态

```bash
docker-compose ps
```

## 安装步骤

**Snort 配置**: 编辑 `docker/snort/snort.conf` 以配置 Snort 规则和参数。

**Spark 配置**: 编辑 `docker/spark/spark.conf` 以调整 Spark 集群设置。

**Nginx 配置**: 编辑 `docker/nginx/nginx.conf` 以设置负载均衡策略。

**Web 服务器配置**: 编辑 `src/web_server/app.py` 以配置后端服务参数。

## 常见问题

无法启动 Snort 容器

- 请检查 `snort.conf` 配置文件是否正确，确保规则文件路径正确。

Spark 集群未响应

- 检查 Spark 容器日志，确保所有节点正常启动并互相通信。