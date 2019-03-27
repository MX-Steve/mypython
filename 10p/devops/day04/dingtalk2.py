import requests
import sys
import json
import getpass


def send_msg(url, msg, reminders=None):
    headers = {"Content-Type": "application/json;charset=utf-8"}
    data = {
        "msgtype": "text",
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,
        },
        "text": {
            "content": msg,
        }
    }
    # data1 = {
    #     "msgtype": "link",
    #     "link":{
    #         "text":"nsd1810 step 5",
    #         "title":"my title",
    #         "picUrl": "",
    #         "msgUrl":""
    #     }
    # }
    data1 = {
        "msgtype": "markdown",
        "markdown": {"title":"杭州天气",
            "text":"#### 杭州天气  \n > 9度，@18262629610 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](https://www.seniverse.com) "
        },
        "at": {
            "atMobiles": [
            "1825718XXXX"
        ],
        "isAtAll": False
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text


if __name__ == '__main__':
    # msg = sys.argv[1]
    msg = "Today is a good day"
    # reminders = ['18262629610', '18061696520']
    reminders = ['18061696520']
    # url=getpass.getpass()  # jiqiren de token dizhi
    # https://im.dingtalk.com
    url = 'https://oapi.dingtalk.com/robot/send?access_token=02776d4ea387378b79f3b9a47c6ef40e99b426e1e2539d1de36f99cd119c8441'
    print(send_msg(url, msg, reminders))




