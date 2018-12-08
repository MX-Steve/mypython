#!/usr/bin/env python3
# src_obj=open("/bin/ls",'rb')
# dst_obj=open("/root/ls",'wb')
# # 4096
# while True:
#     data=src_obj.readline(4096)
#     #if data == ''
#     if not data:
#         break
#     dst_obj.write(data)
# dst_obj.close()
# src_obj.close()

# # second
# src_obj=open("/bin/ls",'rb')
# dst_obj=open('/root/ls','wb')
# while True:
#     data=src_obj.read(4096)
#     if not data:
#         break
#     dst_obj.write(data)
# src_obj.close()
# dst_obj.close()

# # third
# with open("/bin/ls",'rb') as src:
#     while True:
#         data=src.read(4096)
#         with open('/tmp/ls','wb') as dst:
#             dst.write(data)
#             if not data:
#                 break

# #function
# # type: def function(): 'xxx' fun_suit
# def foo():
#     print("hello world")
#
# foo()

# #fun2: han shu nei de bian liang , diao yong zhi hou jiu hui bei shan chu!
# #mei you fan hui zhi , fan hui none
# def foo():
#     res=3+4
#     return res
# print(foo())

# # #fun3: can shu / chuan can
# def foo(uname):
#     print(uname)
# foo('lisi')
# uname='zhangsan'
# foo(uname)
def fib(num):
    fibs=[0,1]
    for i in range(num-2):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
print(fib(8))
print(fib(10))