#!/usr/bin/env python

# string / list / atuple / adist
#for
# for ch in 'abcd':
#     print(ch,end='  ')

# alist={'name':"tom","age":28,"school":"tarena"}
# for i in alist:
#     print(i,alist[i])
# print(i)
#
# for i in [1,2,3,4,5]:
#     print(i,end="  ")

# for i in range(1,101):
#     if i % 10 != 0:
#         print(i,end="  ")
#     else:
#         print(i)

# fibs=[0,1]
# fibs.append(1)
# fibs.append(2)
# fibs.append(3)
# fibs.append(4)
# fibs.append(5)
# print(fibs)
# n=int(input("num:"))
# for i in range(n-2):
#     fibs.append(fibs[-1]+fibs[-2])
# print(fibs)

# # 99
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"*",i,"=",j*i,end="  ")
#     print()

# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

# print(list(range(1,101,2)))
# print(list(range(100,0,-2)))

# # 99
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%dx%d=%d"%(j,i,j*i),end="  ")
#     print()

# list=[]
# for i in range(1,21):
#     list.append(i)
# print(list)
# # liebiaojiexi
# print([i for i in range(1,21)])
# print([i**2 for i in range(1,21)])
# print([i for i in range(1,21,2)])
# print([i for i in range(2,21,2)])

# # open a file
# fangwenmoshi
# r: w: a:
#r
# fobj=open('/root/a.cnf')
# print(fobj)

# fobj=open('hello.py','r')
# data=fobj.read()
# print(data)
# data=fobj.read()
# print(data)
# fobj.close()

# f=open('/tmp/passwd')
# f.read(5)
# data=f.readline()
# print(data)
# data=f.readline()
# data=f.readlines()

# f.close()
# w
# f = open('hello.txt','w')
# f.write('hello world')
# f.write('nihao')
# f.close()

# data=['new line\n','2nd line\n','3rd line']
# f=open('hello.txt','w')
# f.writelines(data)
# f.close()

# with open('hello.txt') as obj:
#     data=obj.readline()
#     print(data)
#
# with open('hello.txt') as obj:
#     while True:
#         data=obj.readline()
#         print(data,end='')
#         if data =='':
#             break

# with open('/tmp/passwd') as f:
#     print(f.tell())
#     f.read(100)
#     print(f.tell())

# with open('/tmp/passwd') as f:
#     print(f.tell())
#     f.seek(0,2)
#     print(f.tell())

# with open('/tmp/passwd') as f:
#     print(f.readline())
#     f.seek(0,0)
#     print(f.readline())
# #seek: 0:start,1:now,2:end
# +: duxiemoshi
# b: erjinzhi

# with open("/tmp/passwd") as f:
#     for line in f:
#         print(line,end='')




print()