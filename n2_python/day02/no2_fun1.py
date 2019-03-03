#!usr/bin/env python3
# function :
"""
    nei bu han shu wai mian bu ke yong
    qian ding yi han shu , zai ying yong han shu

"""
# def set_info(name,age):
#     print("%s is %s years old" % (name,age))
#
# set_info('lisi',20)
# set_info('lisi',age=20)
# set_info(age=20,name='lisi')


# def mytest(*args):
#     print(args)  # * dai biao yuan zu
#
# mytest()
# mytest(1)
# mytest('tom',12,'schol')
#
# def mytest2(**kwargs):
#     print(kwargs) # ** dai biao zi dian
#
# mytest2()
# mytest2(name='lisi')
# mytest2(name='lisi',age=26)

def mytest(*args):
    print(args)  # * dai biao yuan zu
a1=['lisi',25]
mytest(*a1) # * jiang lie biao chai kai

def mytest2(**kwargs):
    print(kwargs) # ** dai biao zi dian
b1={"name":"zs","age":28}
mytest2(**b1)
