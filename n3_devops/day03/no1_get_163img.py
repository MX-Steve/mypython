from urllib import request
import re
from os import fork


def get_file(url,fname):
    html=request.urlopen(url)
    with open(fname,'wb') as fobj:
        while True:
            data=html.read(1024)
            if not data:
                break
            fobj.write(data)

def get_urls(patt,fname,charset='utf8'):
    url_list=[]
    cpatt=re.compile(patt)
    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                url_list.append(m.group())

    return url_list

if __name__ == '__main__':
    url_163="http://www.163.com"
    fname_163="/tmp/163.html"
    get_file(url_163,fname_163)
    img_patt="(http|https)://[\w./]+\.(jpg|jpeg|gif|png)"
    ulist = get_urls(img_patt,fname_163,'GBK')
    # print(ulist)
    for img in ulist:
        imgname=re.split('/',img)[-1]
        get_file(img,"/tmp/img/"+imgname)
        # print(imgname)
    # pid=fork()
