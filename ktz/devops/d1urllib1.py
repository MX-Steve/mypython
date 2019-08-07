from urllib import request
html=request.urlopen('http://www.daneiyunzhijia.com')
data=html.read()
with open('/tmp/dnyzj.html','wb') as fobj:
    fobj.write(data)

