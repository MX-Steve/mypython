import os

# os , shutil , getpass , subprocess , string , random , sys

print(os.getcwd())
print(os.listdir('/tmp'))
# os.mkdir('/tmp/aaa')
# os.makedirs('/tmp/bbb/aaa')
os.chdir('/tmp/aaa')
print(os.listdir())
# os.mknod('a.txt')
# os.symlink('/etc/hosts','zhuji')
# os.chmod('a.txt',0o644)
# os.rename('a.txt','b.txt')
# os.rmdir('/tmp/bbb')
# os.unlink('zhuji')
# os.remove('b.txt')