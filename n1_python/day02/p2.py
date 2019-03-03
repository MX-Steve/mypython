#!/usr/bin/env python3

adict={'name':"bob",'age':28,'school':'tarena'}

import random
all_choice = ['jian','shi','bu']
you=input("chu:")
win=[("jian","bu"),('shi',"jian"),("bu","shi")]
if (you,random.choice(all_choice)) in win:
    print("you win")
else:
    print("you lose")


# import random
# num=random.randint(1,100)
# answer=int(input("num:1-100"))
# if answer < num:
#     print("small")
# elif answer > num:
#     print("big")
# else:
#     print("ok")
# print(num)

# n=1
# while n<=9:
#     m=9
#     while m>=n:
#         print(n,"*",m,"=",m*n,end="  ")
#         m-=1
#     n+=1
#     print()

# n=1
# while n <=9:
#     m=1
#     while m <=n:
#         # print(m,n,end='  ')
#         print(m,"*",n,"=",m*n,end="  ")
#         m+=1
#     n+=1
#     print()


# num=0
# while num <=100:
#     num+=1
#     if num %2 ==1 :
#         continue
#     print(num,end=' ')
# print()
#
# n=1
# while n <=100:
#     print(n,end='  ')
#     if n >=30:
#         break
#     n+=1
# print()

# while True:
#     name = input("your name:")
#     if name == "tom":
#         break
#     print(name)

# a=1
# while a<=20:
#     print(a,end="  ")
#     a+=2
# print()

# a=1
# while a<=20:
#     print(a,end='  ')
#     a+=1
# print()

# x=3
# y=4
# smaller=x if x< y else y
# print(smaller)