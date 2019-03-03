from urllib import request

url="http://127.0.0.1"
header={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
req = request.Request(url,headers=header)
html=request.urlopen(req)