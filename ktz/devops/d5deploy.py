import os
import requests
import hashlib
import tarfile
import requests_ftp
import wget

# 该函数使用requests_ftp处理requests模块无法直接访问ftp的问题
#def rftp(url):
#    requests_ftp.monkeypatch_session()
#    s=requests.Session()
#    res=s.list(ver_url)
#    res.encoding='utf-8'
#    return res

def has_new_ver(ver_url,ver_fname):
    "检查是否有新版本True/False"
    if not os.path.isfile(ver_fname):
        return True
    r = requests.get(ver_url)
    with open(ver_fname) as fobj:
        local_ver=fobj.read()

    if r.text != local_ver:
        return True
    return False

def check_app(app_fname,app_md5_url):
    "检查的压缩包是否损坏True->完好,False->损坏"
    m=hashlib.md5()
    with open(app_fname,'rb') as fobj:
        while True:
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)
    result=m.hexdigest()
    r=requests.get(app_md5_url)
    if result==r.text.strip():
        return True

def deploy(app_fname,web_root):
    "部署应用"
    dest='/var/www/deploy'
    tar = tarfile.open(app_fname)
    tar.extractall(path=dest)
    tar.close()
    app_dir=app_fname.split('/')[-1]
    app_dir=app_dir.replace('.tar.gz','')
    app_dir=os.path.join(dest,app_dir)
    
    if os.path.exists(web_root):
        os.remove(web_root)
    os.symlink(app_dir,web_root)

if __name__=="__main__":
    ver_url="http://139.159.184.194/myweb/livever"
    ver_fname='/var/www/deploy/livever'
    if not has_new_ver(ver_url,ver_fname):
        print('未发现新版本')
        exit(1)
    r=requests.get(ver_url)
    version=r.text.strip()
    app_url='http://139.159.184.194/myweb/packages/myweb-%s.tar.gz' %version
    download_dir='/var/www/download'
    wget.download(app_url,download_dir)
    app_fname=app_url.split('/')[-1]
    app_fname=os.path.join(download_dir,app_fname)
    app_md5_url="http://139.159.184.194/myweb/packages/myweb-%s.tar.gz.md5"%version
    if not check_app(app_fname,app_md5_url):
        print("压缩包已经损坏")
        os.remove(app_fname)
        exit(2)
    with open(ver_fname,'w') as fobj:
        fobj.write(version+'\n')
    web_root='/var/www/html/nsd1903'

    deploy(app_fname,web_root)

