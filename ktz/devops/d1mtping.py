import os
import threading
import subprocess

def myping(host):
    result=subprocess.run(
        'ping -c2 %s &> /dev/null'%host,
        shell=True
    )
    if result.returncode==0:
        print('%s:up'%host)
    else:
        print("%s:down"%host)

if __name__=="__main__":
    ips=('176.4.11.%s' % i for i in range(1,255))
    #for ip in ips:
    #    retval = os.fork()
    #    if not retval:
    #        myping(ip)
    #        exit()
    for ip in ips:
        t = threading.Thread(target=myping,args=(ip,))
        t.start()
