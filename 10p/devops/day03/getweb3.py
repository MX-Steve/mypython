from urllib.request import urlopen
import sys
from urllib.error import HTTPError

def get_web(url,fname):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        if e.code == 403:
            print("quan xian bei ju jue")
        elif e.code == 404:
            print("not found")
        return
    with open(fname,'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)
    html.close()

if __name__ == '__main__':
    get_web(sys.argv[1],sys.argv[2])