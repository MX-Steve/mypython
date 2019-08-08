import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.4.14',username='root',password='123456',port=22)
stdin,stdout,stderr=ssh.exec_command('id root;id john')

out=stdout.read()
err=stderr.read()

print(out.decode())
print(err.decode())
