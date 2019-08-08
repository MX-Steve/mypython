import requests

#r=requests.get('http://www.sogou.com')
#print(r.text) # 文本内容
r=requests.get('https://fanyi.bdstatic.com/static/translation/img/header/logo_40c4f13.svg')
with open('/tmp/steve.svg','wb') as fobj:
    fobj.write(r.content) # 非文本文件内容

