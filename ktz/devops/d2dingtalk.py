#!/usr/bin/env python3

import json
import requests
import sys


def send_msg(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,   # 不@所有人
        },
        "text": {
            "content": msg,   # 消息正文
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()  # 服务器返回消息，用于调试

if __name__ == '__main__':
    msg = sys.argv[1]
    reminders = ['18262629610']  # 特殊提醒要查看的人,就是@某人一下
    url = 'https://oapi.dingtalk.com/robot/send?access_token=61c487db5d5c72583dbd02d2eb2ca169aa5eaec1c9a6bf0e1264b148b0fc9bad'
    print(send_msg(url, reminders, msg))
