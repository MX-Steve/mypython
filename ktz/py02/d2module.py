# import sys
# print(sys.path)

import hashlib

m=hashlib.md5(b'123456')
print(m.hexdigest())
with open('/etc/passwd','rb') as fobj:
    data=fobj.read()
n=hashlib.md5(data)
print(n.hexdigest())

m1=hashlib.md5()
m1.update(b'12')
m1.update(b'34')
m1.update(b'56')
print(m1.hexdigest())