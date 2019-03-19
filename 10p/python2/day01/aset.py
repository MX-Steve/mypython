# aset=set('abc')
# print(aset)
# bset=set('bcd')
# print(bset)
# print(bset-aset)
# # cset=set(['hello','world'])
# # print(cset)
# # for item in cset:
# #     print(item)
#
# print(aset | bset)
# print(aset & bset)
# print(aset - bset)
# from random import  randint
#
# alist = [randint(1,50) for i in range(20)]
# print(alist)
# print(list(set(alist)))

with open('/tmp/passwd') as fobj:
    aset = set(fobj)
with open('/tmp/passwd1') as fobj:
    bset = set(fobj)

print(bset-aset)