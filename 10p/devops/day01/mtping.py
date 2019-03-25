import subprocess
import threading

def ping(host):
    rc=subprocess.call(
        "ping -c2 %s &>/dev/null"%host,
        shell=True
    )
    if rc == 0:
        print("\033[32m %s up\033[0m"%host)
    else:
        print("\033[31m %s down\033[0m"%host)

if __name__ == '__main__':
    ips=['176.4.13.%s'%i for i in range(1,255)]
    for ip in ips:
        t = threading.Thread(target=ping,args=(ip,))
        t.start()