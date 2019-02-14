alist=[1,2,3,'bb','alice']
alist[0]=10
print(alist)
alist[1:3]=[20,30]
print(alist)
alist[2:2]=[22,24,26,28]
print(alist)
alist.remove(24) # 如果有多个24，只会删除第一个
print(alist.index('bb'))
blist=alist.copy() # blist=alist[:]
alist.insert(1,15) #在下标为1的地方插入15
alist.pop() # pop last one
alist.pop(2) # 弹出下标为2的
alist.pop(alist.index('bb'))
print(alist)
alist.sort()
print(alist)
alist.reverse()
print(alist)
print(alist.count(20)) # 统计20在列表中出现的次数
alist.clear() # 清空列表
print(alist)
alist.append('new')
print(alist)
alist.extend('new')
print(alist)
alist.extend(['hello','world'])
print(alist)
