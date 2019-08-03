x=10

def func1():
    print(x)

# func1()

def func2():
    y=100
    print(y)

# func2()

def func3():
    x=15
    print(x)

# func3()
# print(x)

def func4():
    global x
    x='abc'
    print(x)

# func4()
# print(x)\

def func5():
    print(len('abc'))

# func5()

# print(int('1010',base=2))
# print(int('1010'))

from functools import partial

int2 = partial(int,base=2)
print(int2('1010'))

# os , sys , getpass , random , functools , subprocess , shutil , time , datetime , pickle

def add(a,b,c,d,e):
    return a+b+c+d+e

print(add(10,20,30,40,50))

add1=partial(add,10,20,30,40)
print(add1(100))
print(add1(200))
print(add1(300))

# os , sys , randpass , getpass , subprocess , string , shutil, pickle , date , datetime , functools