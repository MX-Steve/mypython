from urllib.request import urlopen
import json

# url="http://www.kuaidi100.com/query?type=%s&postid=%s"
# type: kuaidigongsi ; postid: kuaididanhao
url="http://www.kuaidi100.com/query?type=youzhengguonei&postid=9893442769997"
r = urlopen(url)
data = r.read()
data = json.loads(data)
info = data['data']
# print(info)
# print(info[-1])
# time = info[-1]['time']
# context = info[-1]['context']
# print("time: %s;context: %s"%(time,context))
info.reverse()
# print(info)
for info_dict in info:
    print("time: %s ; context: %s"%(info_dict['time'],info_dict['context']))