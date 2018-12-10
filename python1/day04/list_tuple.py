#!/usr/bin/env python3
alist=[1,2,3,4,5]
# alist[-1]=10
# print(alist)
#
# #append
# alist.append(11)
# alist.append([5,6]) # yi ge yuan su

alist.extend([4,5,6]) #da san lie biao
alist.insert(0,0)
# alist.insert(1,'abc')
# alist.insert(-1,'aaa') # zui hou yi ge zhi qian
# alist.sort()
alist.reverse()

print(alist.index(6)) # de dao index zhi
# print(alist.index(1000)) # cun zai cai ke yi
alist.pop()

print(alist)