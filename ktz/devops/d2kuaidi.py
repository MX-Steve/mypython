import json
from urllib import request

url='http://www.kuaidi100.com/query?type=%s&postid=%s'
r=request.urlopen(url%('youzhengguonei','9893442769997'))
data=r.read()
obj=json.loads(data)
print(obj)
