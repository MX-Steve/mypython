# fs=frozenset('abc')
# s1=set('abc')
# print(fs)
# print(s1)
# s2=set(['aaa','bbb','ccc'])
# print(s2)
# print(set('hello'))
#
# for i in s2:
#     print(i)
#
# print(len(s2))
# print(set('hello'))
# s=''
# a=list(set('hello'))
# a.sort()
# for i in a:
#     s+=i
# print(s)
#
# aset=set('abc')
# bset=set('bcd')
# print(aset&bset)
# print(aset|bset)
# print(aset-bset)
# print(bset-aset)
# aset.add('e')
# print(aset)
# aset.update('new')
# print(aset)
# aset.update(['new1','new2'])
# print(aset)
# aset.remove('new1')
# print(aset)
#
# s1=set('abcde')
# s2=set('bc')
# print(s1.issuperset(s2))
# print(s2.issubset(s1))
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))

from random import randint

num_list = [randint(1,20) for i in range(1,100)]
print(num_list)
num_list=list(set(num_list))
print(num_list)