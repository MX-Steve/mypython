from random import  randint

alist=[randint(1,100) for i in range(10)]

def func1(x):
    return True if  x % 2 == 0 else False

print(list(filter(func1,alist)))
print(list(filter(lambda x: True if x % 2 == 0 else False, alist)))
print(list(filter(lambda x: True if x % 2 else False, alist)))