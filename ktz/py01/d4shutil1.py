import  shutil

# f1=open("/bin/ls",'rb')
# f2=open('/tmp/ll','wb')
# shutil.copyfileobj(f1,f2)
# f1.close()
# f1.close()

# shutil.copyfile('/bin/ls','/tmp/ls1')
# shutil.copy('/bin/ls','/tmp/ls2')
# shutil.copy2('/bin/ls','/tmp/ls3')
# shutil.move('/tmp/ls3','/opt/')
# shutil.copytree('/etc/security','/tmp/security')
# shutil.rmtree('/tmp/security')

# import os
# os.remove('/opt/ls3')
# shutil.chown('/tmp/ls2',user='root',group='wheel')

import subprocess
# subprocess.run('ls')
# subprocess.run(['ls','/home'])
# subprocess.run('ls ~' , shell=True)
# rc=subprocess.run('ping -c2 192.168.1.2 &>/dev/null',shell=True)
# print(rc.returncode)

# rc=subprocess.run('ls /home',shell=True)
# rc=subprocess.run('id root; id john',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# print(rc.stderr)
# print(rc.stdout)
# print(rc.stdout.decode()) # bytes  -->  str

a,b=(10,20)
a,b=b,a
print(a)
print(b)

import keyword

print(keyword.kwlist)
print(keyword.iskeyword('is'))