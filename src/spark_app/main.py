from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

def process_stream(rdd):
    if not rdd.isEmpty():
        alerts = rdd.collect()
        for alert in alerts:
            print(f"Alert: {alert}")

if __name__ == "__main__":
    conf = SparkConf().setAppName("SnortAlertProcessor")
    sc = SparkContext(conf=conf)
    ssc = StreamingContext(sc, 5)  # 5秒批处理

    lines = ssc.socketTextStream("snort", 5555)
    lines.foreachRDD(process_stream)

    ssc.start()
    ssc.awaitTermination()
