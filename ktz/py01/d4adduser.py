import sys
import random
import string
import subprocess

alls=string.digits+string.ascii_letters+"_"

def getpass(n=8):
    str=''
    for i in range(n):
        str+=random.choice(alls)
    return str

def add_user(username,userpass,fname):
    while True:
        rc=subprocess.run('id %s &>/dev/null'%username,shell=True)
        if rc.returncode:
            break
        print("user name already exists")
    subprocess.run('useradd %s'%username,shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s'%(userpass,username),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    with open(fname,'w') as fobj:
        fobj.write("%-10s%-8s"%(username,userpass))

if __name__ == '__main__':
    username=sys.argv[1]
    passwd=getpass(4)
    fname='/tmp/users'
    add_user(username,passwd,fname)