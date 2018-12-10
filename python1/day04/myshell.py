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
shutil.move('/mypython/python1/passwd','/var/tmp')