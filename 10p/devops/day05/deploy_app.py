"""
has_new_ver() panduan shibushi you xinbanben
check_app() jiancha wanzhengxin
deploy() bushu yuanjian
"""
import os
import requests
import wget
import hashlib
import  tarfile

def has_new_ver(ver_url,ver_fname):
    if not os.path.isfile(ver_fname):
        return True
    with open(ver_fname) as fobj:
        app_ver=fobj.read()
    r = requests.get(ver_url)
    if app_ver != r.text:
        return True
    return False

def check_app(app_fname,app_md5_url):
    r = requests.get(app_md5_url)
    remote_md5 = r.text.strip()
    m = hashlib.md5()
    with open(app_fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    if remote_md5 == m.hexdigest():
        return True
    return False


def deploy(app_fname):
    deploy_dir = "/var/www/deploy"
    os.chdir(deploy_dir)
    tar = tarfile.open(app_fname,'r:gz')
    tar.extractall()
    tar.close()

    app_path = os.path.basename(app_fname)
    app_path = app_path.replace('.tar.gz','')
    app_path = os.path.join(deploy_dir, app_path)

    link = "/var/www/html/nsd1810"
    if os.path.exists(link):
        os.unlink(link)
    os.symlink(app_path,link)
    # deploy_app = ''



if __name__ == '__main__':
    ver_url = "http://192.168.4.254/deploy/livever"
    ver_fname = "/var/www/deploy/livever"
    if not has_new_ver(ver_url,ver_fname):
        print(" no new version")
        exit()
    r= requests.get(ver_url)
    app_ver = r.text.strip()
    app_url="http://192.168.4.254/deploy/packages/myweb-%s.tar.gz" % app_ver
    download_dir="/var/www/deploy"
    wget.download(app_url,download_dir)

    app_fname = "/var/www/download/myweb-%s.tar.gz" % app_ver
    app_md5_url=app_url + ".md5"
    if not check_app(app_fname,app_md5_url):
        print("download error")
        exit(1)

    with open(ver_fname,'w') as fobj:
        fobj.write(r.text)

    deploy(app_fname)