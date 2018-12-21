from urllib import request

def get_file(url,fname):
    html=request.urlopen(url)
    with open(fname,'wb') as fobj:
        while True:
            data=html.read(1024)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    url="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3581792254,1787772481&fm=173&app=25&f=JPEG?w=218&h=146&s=DBACB7475B8662D2062E5B6D0300E068"
    fname="/tmp/a.jpeg"
    get_file(url,fname)