# API 文档

## 获取检测结果

**Endpoint:** `/api/results`

**Method:** GET

**Response:**

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "timestamp": "2024-12-06T12:00:00Z",
            "source_ip": "192.168.1.10",
            "destination_ip": "10.0.0.5",
            "alert": "Possible SQL Injection"
        },
        ...
    ]
}
```

## 添加新规则

**Endpoint:** `/api/rules`

**Method:** POST

**Request Body:**

```json
{
    "rule": "alert tcp any any -> any 80 (msg:\"SQL Injection Attempt\"; content:\"SELECT\"; nocase; sid:1000001;)"
}
```

**Response:**

```json
{
    "status": "success",
    "message": "Rule added successfully."
}
```

## 删除规则

**Endpoint:** `/api/rules/{id}`

**Method:** DELETE

**Response:**

```json
{
    "status": "success",
    "message": "Rule deleted successfully."
}
```

