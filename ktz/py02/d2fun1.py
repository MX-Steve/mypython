# def foo():
#     print('in foo')
#     bar()
#
# def bar():
#     print("in bar")
#
# foo()

def get_info(name,age):
    print("%s:%s"%(name,age))

get_info(name='tom',age=12)

def func1(*args):
    print(args)

func1('a','b',11,22,33)
func1()

def add(a,b):
    return a+b

nums=[10,20]

print(add(*nums))

def func2(**kws):
    print(kws)

func2(name='tom',age=25)
func2()
a={'name':'tom','age':25}
func2(**a)