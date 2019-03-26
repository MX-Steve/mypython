import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='176.4.16.101',username='root',password='daneiyunzhijia')
a = ssh.exec_command('ls /home/')
print(len(a))     # a[0] -> input ; a[1] -> out ; a[2] -> error
# print(a[1].read())
# print(a[2].read())
out = a[1].read()
err=a[2].read()
print(out.decode('utf8'))