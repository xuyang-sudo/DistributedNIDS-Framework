# 使用官方 Spark 镜像
FROM bitnami/spark:latest

# 复制 Spark 配置文件
COPY spark.conf /opt/bitnami/spark/conf/

# 设置工作目录
WORKDIR /opt/bitnami/spark

# 启动 Spark
CMD ["spark-class", "org.apache.spark.deploy.master.Master"]
