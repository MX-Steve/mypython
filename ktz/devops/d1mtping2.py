import os
import threading
import subprocess

class Ping:
    def __init__(self,host):
        self.host=host

    def __call__(self):
        result=subprocess.run(
            'ping -c2 %s &> /dev/null'%self.host,
            shell=True
        )
        if result.returncode==0:
            print('%s:up'%self.host)
        else:
            print("%s:down"%self.host)

if __name__=="__main__":
    ips=('176.4.11.%s' % i for i in range(1,255))
    #for ip in ips:
    #    retval = os.fork()
    #    if not retval:
    #        myping(ip)
    #        exit()
    for ip in ips:
        t = threading.Thread(target=Ping(ip))
        t.start() #target() 相当于直接调用实例，call方法可以允许你直接调用实例
