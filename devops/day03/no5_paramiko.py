import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # yes
ssh.connect('192.168.1.20')
# ssh.connect('192.168.1.21',username='root',passphrase='1')
a=ssh.exec_command('id z31')
print(len(a))
print(a[1].read())  # correct : standard out
print(a[2].read())  # error : standard error
ssh.close()