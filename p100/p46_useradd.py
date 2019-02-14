import subprocess
import sys
from p37_randpass import gen_pass

def useradd(username,passwd,fname):
  data="""user infomation
%s: %s
"""
  subprocess.call('useradd %s'%username,shell=True)
  subprocess.call('echo %s | passwd --stdin %s'%(passwd,username),shell=True)
  with open(fname,'a') as fobj:
    fobj.write(data%(username,passwd))

if __name__=="__main__":
  username=sys.argv[1]
  passwd=gen_pass(8)
  useradd(username,passwd,'/tmp/user.txt')

























#import subprocess
#import sys
#import p37_randpass
#
#def adduser(username,passwd,fname):
#  data="""user information:
#%s: %s
#"""
#  subprocess.call("useradd %s"%username,shell=True)
#  subprocess.call('echo %s | passwd --stdin %s'%(passwd,username),shell=True)
#  with open(fname,'a') as fobj:
#    fobj.write(data%(username,passwd))
#
#if __name__=="__main__":
#  username=sys.argv[1]
#  passwd=p37_randpass.gen_pass()
#  adduser(username,passwd,'/tmp/user.txt')
