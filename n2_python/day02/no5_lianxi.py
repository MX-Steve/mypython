#!/usr/bin/env python3

# ju bu bian liang , ju bu shi yong.

x=10

def foo():
    print(x)

def foo1():
    x='hello'
    print(x)

def bar():
    y=2
    print(y)

def foo2():
    global x  # sheng ming shi yong quan ju bian liang
    x = 'nihao'

# print(x)
# # foo()
# # foo1()
# # bar()
# foo2()
# print(x)

y=10

def bar1():
    print(y)
    # y=20

bar1()