import re
from urllib.request import urlopen
from  urllib.request import Request
import os

class GetSth:
    def __init__(self,url,filename):
        self.url = url
        self.filename = filename

    def get_html(self,url,filename):
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.64 Safari/537.36'}
        request=Request(url,headers=header)
        html=urlopen(request)
        with open(filename,'wb') as fobj:
            while True:
                data = html.read(1024)
                if not data:
                    break
                fobj.write(data)
        html.close()

    def get_urls(self,pic_url):
        cpatt=re.compile(pic_url)
        urllist=[]
        with open(filename) as fobj:
            for line in fobj:
                r = cpatt.search(line)
                if r:
                    urllist.append(r.group())
        return urllist

    def get_pic(self,list,imgdir):
        for url in list:
            img=os.path.join(imgdir,url.split('/')[-1])
            self.get_html(url,img)

if __name__ == '__main__':
    url="http://www.tedu.cn"
    filename="/tmp/tedu.html"
    pic_url='http://[\w/.-]+\.(jpg|png|gif)'
    gs = GetSth(url,filename)
    try:
        gs.get_html()
    except:
        pass
    list=gs.get_urls(pic_url)
    imgdir="/tmp/picture"
    if not os.path.isdir(imgdir):
        os.mkdir(imgdir)
    gs.get_pic(list,imgdir)