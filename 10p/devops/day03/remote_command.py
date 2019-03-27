import paramiko
import pickle
import threading


def remote_com(hosts,user,passwd,cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hosts,username=user,password=passwd)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    out = stdout.read()
    err=stderr.read()
    if out:
        print("[%s] OUT:\n%s"%(hosts,out.decode('utf8')))
    if err:
        print("[%s] ERROR: \n%s"%(hosts,err.decode('utf8')))

if __name__ == '__main__':
    # remote_com()
    # hosts=[
    #     {"host": '176.4.16.101',"user":  "root","passwd":  "daneiyunzhijia"},
    #     {"host": '176.4.13.5', "user": "root", "passwd": "Taren1"},
    #     {"host": '176.4.13.4', "user": "root", "passwd": "Taren1"},
    # ]
    # with open("user.txt",'wb') as fobj:
    #     # pickle.dumps(hosts,fobj)
    #     pickle.dump(hosts,fobj)
    cmd='id z3'
    with  open('user.txt','rb') as fobj:
        hs = pickle.load(fobj)
        for line in hs:
            t = threading.Thread(target=remote_com,args=(line['host'],line['user'],line['passwd'],cmd))
            t.start()
            # remote_com(line['host'],line['user'],line['passwd'],cmd)