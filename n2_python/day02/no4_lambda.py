#!/usr/bin/env python3
# a = lambda x,y: x + y

from random import randint

def fun1(x):
    return x % 2

def fun2(x):
    return x*2 + 1

if __name__ == '__main__':
    nums = [randint(0,100) for i in range(10)]
    print(nums)
    #filter: guo lv , man zu tiao jian de guo lv diao , bu man zu de bao liu.
    a=filter(fun1,nums)
    print(type(a))
    print(list(filter(fun1,nums)))
    print(list(filter(lambda x:x%2,nums)))
    print(list(map(fun2,nums)))
    print(list(map(lambda x:x*2+1,nums)))