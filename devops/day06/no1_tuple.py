from collections import namedtuple
user = namedtuple('user',['name','age'])
bob = user('Bob', 24)
print(bob[0])
print(bob[1])
print(bob.name,bob.age)