from urllib import request
html=request.urlopen('http://5b0988e595225.cdn.sohucs.com/images/20170829/fb988f78086f4f2e9e38bfef727a9319.jpeg')
data=html.read()
with open('/tmp/a.jpeg','wb') as fobj:
    fobj.write(data)

