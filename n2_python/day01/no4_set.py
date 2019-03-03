#!/usr/bin/env python3
"set is like a adict without value, it is wu xu de"
# b={'a','b','c'}
# print(b)
# a=['123','b','sdfe']
# print(set(a))
# c=set(a)
# print(b & c)
# print(b | c)
# print(b - c)
# c.add('greet')
# c.update(['ni','hao'])
# c.remove('ni')
#
# print(b.intersection(c))  # b & c
# print(b.union(c))         # b | c
# print(b.difference(c))    # b - c
#
# print(c)
############################################################################
# cha yi de nei rong cun zai yi ge wen jian zhong
# : pan duan bu tong , bing jiang bu tong de nei rong cun zai wen jian zhong
with open('/etc/passwd') as fobj:
    aset=set(fobj)
with open('/tmp/mima.txt') as fobj:
    bset=set(fobj)

with open('/root/newfile', 'w') as fobj:
    fobj.writelines(bset-aset)