import os
import subprocess
def ping(host):
    rc=subprocess.call('ping -c2 %s &>/dev/null'%host,shell=True)
    if rc==0:
        print("%s up"%host)
    else:
        print("\033[32m%s down\033[0m"%host)

if __name__ == '__main__':
    ips=['176.4.13.%s'%i for i in range(1,255)]
    for ip in ips:
        pid=os.fork()
        if not pid:
            ping(ip)
            exit()
