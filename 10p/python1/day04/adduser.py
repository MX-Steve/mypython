#!/usr/bin/env python3
"create user and passwd it"
import subprocess
from string import  ascii_letters, digits
import random
all_c=ascii_letters+digits

def passwd_gen(n=8):
    result=''
    for i in range(n):
        result+=random.choice(all_c)
    return result

def createuser(user,passwd):
    result=subprocess.run(
        'useradd %s'%user,
        shell=True)
    if result.returncode:
        print("username already exists!")
        return
    subprocess.run(
        'echo %s | passwd --stdin %s'%(passwd,user),
        shell=True
    )
    with open('/tmp/u.txt','a') as fobj:
        fobj.write('%s : %s\n'%(user,passwd))


def menu():
    u=input('input your name:')
    p=passwd_gen(8)
    createuser(u,p)

if __name__ == '__main__':
    menu()