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
# def fib(num):
#     fibs=[0,1]
#     for i in range(num-2):
#         fibs.append(fibs[-1]+fibs[-2])
#     return fibs
# print(fib(8))
# print(fib(10))
# def jiji(num):
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             print("%dX%d=%d"%(j,i,j*i),end="  ")
#         print()
# jiji(8)
# jiji(16)

# # #fun4
# def copy_file(src,dst):
#     with open(src,'rb') as src_obj:
#         while True:
#             data=src_obj.read(4096)
#             if not data:
#                 break
#             with open(dst,'wb') as dst_obj:
#                 dst_obj.write(data)
# copy_file('/etc/passwd','/tmp/passwd')

#fun5
import sys
# def copy_file():
#     with open(sys.argv[1],'rb') as src_obj:
#         while True:
#             data=src_obj.read(4096)
#             if not data:
#                 break
#             with open(sys.argv[2],'wb') as dst_obj:
#                 dst_obj.write(data)
# copy_file()

# def foo():
#     print(sys.argv)
#     print(sys.argv[1])
#     print(sys.argv[2])
# foo()

# # fun6: mo ren can shu zhi
# def pstar(num=5):
#     print("*"*num)
# pstar()
# pstar(30)