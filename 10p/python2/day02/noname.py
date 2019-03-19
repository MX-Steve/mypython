from random import randint
def add(x,y):
    return x+y

def func1(num):
    return num % 2 # 0->false;1->true

if __name__ == '__main__':
    # cmds={'+':lambda x,y: x+y,'-':lambda x,y: x-y}
    # print(cmds['+'](10,5))
    # print(cmds['-'](10,5))
    alist=[randint(0,100) for i in range(20)]
    print(alist)
    # filter -> true = save; false = remove
    blist=filter(func1,alist)
    print(list(blist))
    result2 = list(filter(lambda num:num %2 , alist))
    result2.sort()
    print(result2)
    result3 = list(map(lambda num: num*2,[randint(0,100) for i in range(10)]))
    print(list(result3))