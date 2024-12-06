import unittest
import subprocess

class SnortTest(unittest.TestCase):
    def test_snort_conf(self):
        # 检查 Snort 配置文件是否存在
        result = subprocess.run(['docker', 'exec', 'snort', 'test', '-f', '/etc/snort/snort.conf'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.returncode, 0, "Snort 配置文件有误或不存在。")

    def test_snort_running(self):
        # 检查 Snort 容器是否在运行
        result = subprocess.run(['docker', 'ps', '--filter', 'name=snort', '--format', '{{.Status}}'], stdout=subprocess.PIPE)
        status = result.stdout.decode().strip()
        self.assertIn("Up", status, "Snort 容器未运行。")

if __name__ == '__main__':
    unittest.main()
