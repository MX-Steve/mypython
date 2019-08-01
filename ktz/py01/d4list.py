from random import randint

alist=[randint(0,100) for i in range(10)]
print(alist[0])
print(alist[0:3])
print(alist)
alist[2:2]=[10,20]
print(alist)
alist.append(30)
print(alist)
alist.extend([100,200])
print(alist)
alist.remove(100)
print(alist)
alist.pop()
print(alist)
blist=alist.copy()
print(blist)
alist.clear()
print(blist)