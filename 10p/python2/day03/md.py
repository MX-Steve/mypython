import hashlib
m = hashlib.md5(b'123456')
# print(m.hexdigest())
# hash : one way encrypt,the same thing,the same result.
# http://www.cmd5.com

m = hashlib.md5()
m.update(b'123')
m.update(b'456')
print(m.hexdigest())
m = hashlib.md5(b'123456')
print(m.hexdigest())