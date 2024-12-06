import unittest
from pyspark import SparkContext, SparkConf
from src.spark_app.main import process_stream

class SparkAppTest(unittest.TestCase):
    def setUp(self):
        conf = SparkConf().setAppName("TestApp")
        self.sc = SparkContext(conf=conf)
        self.rdd = self.sc.parallelize(["alert1", "alert2"])

    def test_process_stream(self):
        # 捕获打印输出
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        process_stream(self.rdd)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Alert: alert1", output)
        self.assertIn("Alert: alert2", output)

    def tearDown(self):
        self.sc.stop()

if __name__ == '__main__':
    unittest.main()
