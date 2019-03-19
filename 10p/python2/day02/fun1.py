def f1(*args):
    print(args)

def f2(**args):
    print(args)

if __name__ == '__main__':
    f1()
    f1('a','b','c')
    f1('a','b')
    f2()
    f2(a='b',b='c')
    a=['aaa','bbb','ccc']
    b={'name':'lisi','age':28}
    f1(*a)
    f2(**b)