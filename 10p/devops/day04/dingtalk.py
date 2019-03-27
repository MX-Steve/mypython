import requests
import sys
import json
import getpass

def send_msg(url, msg, reminders=None):
    headers = {"Content-Type": "application/json;charset=utf-8"}
    data = {
        "msgtype": "text",
        "at":{
            "atMobiles": reminders,
            "isAtAll": False,
        },
        "text": {
            "content": msg,
        }
    }
    r = requests.post(url,data=json.dumps(data),headers=headers)
    return r.text

if __name__ == '__main__':
    msg = sys.argv[1]
    reminders = ['18262629610','18061696520']
    # url=getpass.getpass()  # jiqiren de token dizhi
    url='https://www.dingtalk.com/'
    print(send_msg(url,msg,reminders))




