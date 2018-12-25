import requests
from  urllib.request import urlopen
import os
import hashlib


def get_pack_name(version):
    "fan hui xia zai de ruan jian bao url"
    version_url="http://192.168.1.21/deploy/%s_version" %version
    ver=requests.get(version_url).text.strip()
    pack_url="http://192.168.1.21/deploy/packages/wpress_%s.tar.gz"%ver
    return pack_url


def download(url):
    "yong yu xia zai ruan jian bao, fan hui jue dui lu jing"
    # data = requests.get(url)
    # with open('wpress_1.0.tar.gz','wb') as fobj:
    #     fobj.write(data)
    html = urlopen(url)
    fname=url.split('/')[-1]
    fname = os.path.join('/var/tmp/', fname)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)
    html.close()
    return fname

def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

def check_package(fname):
    "jiao yan ruan jian bao shi fou wan hao, zheng que fan hui true , fou ze fan hui false"
    md5_w=requests.get('http://192.168.1.21/deploy/live_version').text.strip()
    md5_n=check_md5(fname)
    if md5_n == md5_w:
        return True
    else:
        return False



def deploy(fname):
    "jiang xia zai de ruan jian bao bu shu dao web fu wu qi"

if __name__ == '__main__':
    prompt="""(0) live version 
(1) last version
choice(0|1)"""
    version = input(prompt)
    if version == '0':
        version = "live"
    elif version == '1':
        version = 'last'
    url = get_pack_name(version)
    fname = download(url)
    fileok = check_package(fname)
    if fileok:
        deploy(fname)
    else:
        print("download again please!")
