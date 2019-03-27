import requests
# r = requests.get('http://www.baidu.com')
# print(r.text)
# r = requests.get('https://www.baidu.com/img/bd_logo1.png')
# with open('/tmp/logo.png','wb') as fobj:
#     fobj.write(r.content)

# r = requests.get("http://www.weather.com.cn/data/cityinfo/101010100.html")
# # r.json()
# # print(r.encoding)
# r.encoding = 'utf8'
# print(r.json())

kd_url="http://www.kuaidi100.com/query"
kd_params = {'type':"youzhengguonei","postid":"9893442769997"}
r = requests.get(kd_url,kd_params)
print(r.json())