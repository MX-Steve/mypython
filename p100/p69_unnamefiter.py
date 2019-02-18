from random import randint

def func1(x):
    return x %2

if __name__=="__main__":
    alist=[randint(1,100) for i in range(10)]
    print(alist)
    # filter 要求第一个参数是函数，该函数必须返回true或false
    # 执行时把alist的每一项作为func1的参数，返回真留下，否则过滤掉
    # filter函数的参数又是函数，称为高阶函数
    result = filter(func1,alist) # 不适用匿名函数
    print(list(result))
    result2 = filter(lambda x: x%2,alist)  # 使用匿名函数，不适用常规函数
    print(list(result2))
    result3 = filter(lambda x:x%2==0,alist)
    print(list(result3))
