import os

print(os.path.abspath('.'))
print(os.path.split('/tmp/a.txt'))
print(os.path.dirname('/tmp/a.txt'))
print(os.path.basename('/tmp/a.txt'))
print(os.path.join('/tmp/demo','abc.txt'))
print(os.path.isdir('/tmp'))
print(os.path.isfile('/tmp'))
print(os.path.islink('/etc/passwd'))
print(os.path.ismount('/'))
print(os.path.exists('/etc'))
