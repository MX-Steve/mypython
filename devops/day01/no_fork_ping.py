import os
import subprocess

# rc=subprocess.call('ping -c2 192.168.1.254 &>/dev/null',shell=True)
# # print(rc)
# if rc==0:
#     print("up")
# else:
#     print('down')

# def ping(ip):
#     rc=subprocess.call("ping -c2 %s &>/dev/null"%ip,shell=True)
#     if rc==0:
#         subprocess.call("echo %s >>/mypython/devops/test/hosts.txt"%ip,shell=True)
#         # print(ip+"ok")
#     # else:
#         # print(ip+"down")
#
#
# if __name__ == '__main__':
#     for ip in ['176.4.16.%s'%(num) for num in range(1,254)]:
#         pid=os.fork()
#         if not pid:
#             ping(ip)
#             exit()

def ping(host):
    result=subprocess.call(
        "ping -c2 %s &>/dev/null"%host,
        shell=True
    )
    if result == 0:
        result = subprocess.call(
            "echo %s >>/mypython/devops/test/hosts1.txt" % host,
            shell=True
        )

if __name__ == '__main__':
    for host in ['176.4.15.%s'%(str(num)) for num in range(1,254)]:
        pid=os.fork()
        if not pid:
            ping(host)
            exit()