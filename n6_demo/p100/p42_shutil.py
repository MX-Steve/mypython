import shutil

with open("/etc/passwd",'rb')as sfobj:
  with open("/tmp/mima.txt",'wb') as dfobj:
    shutil.copyfileobj(sfobj,dfobj)

shutil.copyfile("/etc/passwd","/tmp/mima2.txt") #源和目标都必须是文件
shutil.copy("/etc/passwd","/tmp") # cp /etc/passwd /tmp
shutil.copy2("/etc/passwd","/tmp") # cp -p /etc/passwd /tmp	
shutil.copytree("/etc/security","/tmp/anquan") # cp -r /etc/security /tmp,目标目录不能存在
shutil.move("/tmp/mypass","/var/tmp/")
shutil.rmtree("/tmp/anquan")
shutil.chown("/tmp/myfile",user="zhangsan",group="zhangsan")
