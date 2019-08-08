from urllib import request
import json

url='http://www.weather.com.cn/data/sk/101010100.html'
r=request.urlopen(url)
data=r.read()
obj=json.loads(data)
print(json.loads(data))

