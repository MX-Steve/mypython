import hashlib
import sys

def check_md5(fname):
  m = hashlib.md5()
  with open(fname,'rb') as fobj:
    while True:
      data = fobj.read(1024)
      if not data:
        break
      m.update(data)
  return m.hexdigest()
    

if __name__=="__main__":
  print(check_md5(sys.argv[1]))















#import hashlib
#import sys
#
#def check_md5(fname):
#  m = hashlib.md5()
#  with open(fname,'rb') as fobj:
#    while True:
#      data=fobj.read(4096)
#      if not data:
#        break
#      m.update(data)
#  return m.hexdigest()
#
#if __name__=="__main__":
#  print(check_md5(sys.argv[1]))












#import hashlib
#import sys
#
#def check_md5(fname):
#  m = hashlib.md5()
#
#  with open(fname, 'rb') as fobj:
#    while True:
#      data = fobj.read(4096)
#      if not data:
#        break
#      m.update(data)
#  return m.hexdigest()
#
#if __name__=="__main__":
#  print(check_md5(sys.argv[1])) # python3 check_md5.py /etc/passwd
