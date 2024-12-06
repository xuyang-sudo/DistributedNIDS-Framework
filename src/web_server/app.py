from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/results', methods=['GET'])
def get_results():
    # 示例数据，实际应从数据库或 Spark 获取
    results = [
        {
            "id": 1,
            "timestamp": "2024-12-06T12:00:00Z",
            "source_ip": "192.168.1.10",
            "destination_ip": "10.0.0.5",
            "alert": "Possible SQL Injection"
        },
        # 更多结果
    ]
    return jsonify({"status": "success", "data": results})

@app.route('/api/rules', methods=['POST'])
def add_rule():
    rule = request.json.get('rule')
    # 将规则添加到 Snort 配置
    with open('/etc/snort/rules/local.rules', 'a') as f:
        f.write(f"{rule}\n")
    return jsonify({"status": "success", "message": "Rule added successfully."}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
