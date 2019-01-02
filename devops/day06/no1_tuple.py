# from collections import namedtuple
# user = namedtuple('user',['name','age'])
# bob = user('Bob', 24)
# print(bob[0])
# print(bob[1])
# print(bob.name,bob.age)
from collections import namedtuple
mb = namedtuple('mobile',['name','price'])
sx = mb('sanxing',2500)
print(sx.name,sx.price)