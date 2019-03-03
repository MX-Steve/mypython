import paramiko
import sys
import os
import getpass
import threading  # qi dong duo xian cheng

def rcmd(host,username,password,cmd):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=username,password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdout=stdout.read()
    stderr=stderr.read()
    if stdout:
        print("[%s] OUT:\n%s"%(host,stdout.decode()))
    if stderr:
        print("[%s] ERR:\n%s"%(host,stderr.decoder()))
    print("=============================")

if __name__ == '__main__':
    host='192.168.1.20'
    password='1'
    username='root'
    cmd='ls /root'
    # rcmd(host,username,password,cmd)
    # hosts=['192.168.1.20','192.168.1.21','192.168.1.61']
    # for ip in hosts:
    #     rcmd(ip,username,password,cmd)
    if len(sys.argv) !=3:
        print("Usage: %s ip file 'command'"%sys.argv[0])
        exit(1)
    ipfile=sys.argv[1]
    if not os.path.isfile(ipfile):
        print("No such file:",ipfile)
        exit(2)
    cmd=sys.argv[2]
    password = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            rcmd(ip,'root',password=password,cmd=cmd)

            # t = threading.Thread(target=rcmd, args=(ip,'root',password,cmd))
            # t.start()
