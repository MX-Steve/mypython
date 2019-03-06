import re
def count_patt(fname,patt):
  cpatt=re.compile(patt)
  result={}
  with open(fname,'r') as fobj:
    for line in fobj:
      m = cpatt.search(line)
      if m:
        key=m.group()
        result[key] = result.get(key,0) +1
  return result

if __name__=="__main__":
  fname="/root/a.log"
  ip="^(\d+\.){3}\d+"
  br='MSIE|Chrome|Firefox'
  print(count_patt(fname,ip))
  print(count_patt(fname,br))






#import re
#def count_patt(fname,patt):
#  cpatt=re.compile(patt)
#  result={}
#
#  with open(fname,'r') as fobj:
#    for line in fobj:
#      m = cpatt.search(line)
#      if m:
#        key=m.group()
#        result[key] = result.get(key,0) + 1
#  return result
#
#if __name__=="__main__":
#  fname="/root/a.log"
#  ip='^(\d+\.){3}\d+'
#  br='Firefox|MSIE|Chrome'
#  print(count_patt(fname,ip))
#  print(count_patt(fname,br))
#











#import re
#
#def count_patt(fname,patt):
#  cpatt=re.compile(patt)
#  result={}
#
#  with open(fname) as fobj:
#    for line in fobj:
#      m = cpatt.search(line) # 如果匹配不到，返回None
#      if m:
#        key=m.group()
#        result[key]=result.get(key,0) + 1
#  return result
#
#if __name__=="__main__":
#  fname = "/root/a.log" # nginx日志文件
#  ip = "^(\d+\.){3}\d+" # 日志开头的ip地址
#  print(count_patt(fname,ip))
#  br='Firefox|MSIE|Chrome' #日志中客户端浏览器
#  print(count_patt(fname,br))
