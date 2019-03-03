import requests

payload={'wd':"hello world"}
r = requests.get('http://www.baidu.com/s',params=payload)
data = r.content

with open('/tmp/bbb.html', 'wb') as fobj:
    fobj.write(data)