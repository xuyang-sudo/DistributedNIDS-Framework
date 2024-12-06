# DistributedNIDS-Framework

DistributedNIDS-Framework 是一个开源的分布式入侵检测系统，利用 Apache Spark 进行分布式处理，Snort 作为入侵检测引擎，通过容器化部署，使用 Nginx 进行负载均衡。

## 功能

- 分布式流量分析与入侵检测
- 容器化部署，易于扩展与维护
- 实时监控与报警
- 可视化管理界面

## 技术栈

- **Snort**: 入侵检测系统
- **Apache Spark**: 分布式数据处理
- **Docker**: 容器化部署
- **Nginx**: 负载均衡
- **Flask**: 后端 Web 服务
- **React**: 前端管理界面

## 安装

请参阅 [部署文档](docs/deployment.md) 了解详细的安装步骤。

## 使用

启动所有服务：

```bash
docker-compose up -d
```

访问 Web 界面：

```
http://localhost:8080
```

## 贡献

欢迎贡献！请参阅 [贡献指南](CONTRIBUTING.md) 了解更多信息。