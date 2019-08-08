#!/root/ktz/bin/python

import paramiko
import sys
import os
import getpass
import threading

def rcmd(host,user='root',passwd=None,port=22,command=None):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=user,password=passwd,port=port)
    stdin,stdout,stderr = ssh.exec_command(command)
    out=stdout.read()
    err=stderr.read()
    if err:
        print("\033[31;1m[%s] ERROR\n%s\033[0m"%(host,err.decode()))
    if out:
        print("[%s] OUT\n%s"%(host,out.decode()))

if __name__=="__main__":
    if len(sys.argv) !=3:
        print("usage:%s ipfile 'command'" % sys.argv[0])
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file:%s'%sys.argv[1])
        exit(2)
    ipfile=sys.argv[1]
    command=sys.argv[2]
    password=getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            t=threading.Thread(target=rcmd,args=(ip,),kwargs={'passwd':password,'command':command})
            t.start() # rcmd(*args,**kwargs)
