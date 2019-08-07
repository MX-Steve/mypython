import wget
import os
from urllib import request
import re

def get_html(url,html):
    headers={'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
    r=request.Request(url,headers=headers)
    js=request.urlopen(r)
    with open(html,'wb') as fobj:
        while True:
            data=js.read(4096)
            if not data:
                break
            fobj.write(data)

def get_url(fname,patt):
    patt_list=[]
    cpatt=re.compile(patt)
    with open(fname) as fobj:
        for line in fobj:
            m=cpatt.search(line)
            if m:
                patt_list.append(m.group())
    return patt_list

def get_pics(img_list,dst):
    for img in img_list:
       img='http:'+img
       wget.download(img,dst)

if __name__=="__main__":
    url="https://www.jianshu.com/"
    html='/tmp/jianshu.html'
    dst='/tmp/jianshu'
    if not os.path.exists(dst):
        os.mkdir(dst)
    get_html(url,html)
    img_patt='//[\w/.-]+\.(png|jpg|jpeg|gif)'
    img_list=get_url(html,img_patt)
    get_pics(img_list,dst)
