import requests

#r=requests.get('http://www.sogou.com')
#print(r.text) # 文本内容

#r=requests.get('https://fanyi.bdstatic.com/static/translation/img/header/logo_40c4f13.svg')
#with open('/tmp/steve.svg','wb') as fobj:
#    fobj.write(r.content) # 非文本文件内容

#url='http://www.weather.com.cn/data/sk/101010100.html'
#r=requests.get(url)
#r.encoding='utf8'
#obj=r.json()
#print(obj)
#print(type(obj))

r=requests.get('https://fanyi.bdstatic.com/static/translation/img/header/logo_40c4f13.svg')
with open('/tmp/newimg.jpg','wb') as fobj:
    for data in r.iter_content(4096):
        fobj.write(data)
# r.iter_content()用于迭代内容
