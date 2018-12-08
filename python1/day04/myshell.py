#!/usr/bin/env python3
#shutil module
import shutil
#copyfileobj(fsrc,fdst) jie shou wen jian dui xiang
# shutil.copyfileobj(open('/etc/passwd','rb'),open('/tmp/mima.txt','wb'))
#copyfil(src,dst) wen jian lu jin
shutil.copyfile('/etc/passwd','/tmp/mima')