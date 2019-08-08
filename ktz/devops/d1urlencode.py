from urllib import request,error

#url="https://www.sogou.com/web?query=" + request.quote('中国')
#print(url)
#html=request.urlopen(url)

#html=request.urlopen('http://127.0.0.1/abc')
try:
    html=request.urlopen('http://127.0.0.1/ban')
except error.HTTPError as e:
    print('错误:',e)

try:
    html=request.urlopen('http://127.0.0.1/abc')
except error.HTTPError as e:
    print('错误:',e)
