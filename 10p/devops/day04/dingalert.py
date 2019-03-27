#!/usr/bin/env python
import json
import requests
import sys

def send_msg(url,reminders,msg):
  headers = {"Content-Type":"application/json;charset=utf-8"}
  data={
    "msgtype":"text",
    "at":{
      "atMobiles":reminders,
      "isAtAll":False,
    },
    "text":{
      "content":msg,
    }
  }

  r = requests.post(url,data=json.dumps(data),headers=headers)
  return r.text

if __name__=="__main__":
  msg = sys.argv[1]
  reminders=['18262629610','18061696520']
  url = 'https://oapi.dingtalk.com/robot/send?access_token=02776d4ea387378b79f3b9a47c6ef40e99b426e1e2539d1de36f99cd119c8441'
  print(send_msg(url,reminders,msg))
