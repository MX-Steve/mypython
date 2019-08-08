#!/usr/bin/env python3

import json
import requests
import sys

url = 'https://oapi.dingtalk.com/robot/send?access_token=61c487db5d5c72583dbd02d2eb2ca169aa5eaec1c9a6bf0e1264b148b0fc9bad'

headers = {'Content-Type': 'application/json;charset=utf-8'}
data ={
        "msgtype": "markdown",
        "markdown": {
            "title": "是透出到会话列表和通知的文案",
            "text": "# 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"
            }
    }
    
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)  # 服务器返回消息，用于调试

