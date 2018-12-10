#!/usr/bin/env python3
#shutil module
import shutil
#copy a file to another
#copyfileobj(fsrc,fdst) jie shou wen jian dui xiang
# shutil.copyfileobj(open('/etc/passwd','rb'),open('/tmp/mima.txt','wb'))
#copyfil(src,dst) wen jian lu jin
# shutil.copyfile('/etc/passwd','/tmp/mima')
#copy di er ge can shu ke yi shi mu lu
# shutil.copy('/etc/shadow','/tmp/')
#copy2
# shutil.copy2("/etc/hosts",'/tmp/')
#move a file to another
# shutil.move('/mypython/python1/passwd','/var/tmp')
#copy a mulu
# shutil.copytree('/etc/yum.repos.d/','/tmp/myyum')
# shutil.copytree('/etc/yum.repos.d/','/tmp/myyum') #di er ci bao cuo , dst bu neng cun zai!
# remove a tree
# shutil.rmtree('/tmp/myyum') # bu cun zai , ze bao cuo!

#fu zhi quan xian
#copymode zhi fu zhi quan xian , jiang shadow quan xian fu zhi gei mima.
# shutil.copymode("/etc/shadow",'/tmp/mima')
## stat /etc/passwd fuzhiyuanshuju
# shutil.copystat('/etc/shadow','/tmp/mima')
#chown : shutil.chown(file,user='',group='')
# shutil.chown('/tmp/mima',user='lisi',group='ntp')