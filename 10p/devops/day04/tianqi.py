# http://www.weather.com.cn/data/sk/city_code.html
# http://www.weather.com.cn/data/cityinfo/city_code.html
# http://www.weather.com.cn/data/zs/city_code.html
# lianyungang => 101191001
# http://www.weather.com.cn/data/sk/101191001.html
# http://www.weather.com.cn/data/cityinfo/101191001.html

from urllib import request
import json

skurl="http://www.weather.com.cn/data/sk/101191001.html"
r = request.urlopen(skurl)
data = r.read()
print(data)
r.close()
lygsk=json.loads(data)
print(lygsk)
print("wendu:" , lygsk['weatherinfo']['temp'])
print("SHIDU:" , lygsk['weatherinfo']['SD'])











