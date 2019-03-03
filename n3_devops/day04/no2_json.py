import json
from urllib import request
html = request.urlopen('http://www.weather.com.cn/data/sk/101010100.html')
result = html.read()
w = json.loads(result)
print(w)
print(w['weatherinfo']['SD'])