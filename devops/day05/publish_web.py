
def get_pack_name(version):
    "fan hui xia zai de ruan jian bao url"

    pass

def download(url):
    "yong yu xia zai ruan jian bao, fan hui jue dui lu jing"

def check_package(fname):
    "jiao yan ruan jian bao shi fou wan hao, zheng que fan hui true , fou ze fan hui false"

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
