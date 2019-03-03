#集合相当于无值的的字典，所以也用{}表示
print(set(['a','bc','e']))
myset = set('hello')
print(len(myset))
for ch in myset:
  print(ch)

aset = set('abc')
bset = set('cde')
print(aset & bset) #交集
print(aset | bset) #并集
print(aset.union(bset)) #并集
print(aset - bset) # 差集
print(aset.difference(bset)) # 差集
aset.add('new')
print(aset)
aset.update(['aaa','bbb'])
print(aset)
aset.remove('bbb')
print(aset)
cset=set('abcde')
dset=set('bcd')
print(cset.issuperset(dset)) # cset是dset的超集吗？
print(dset.issubset(cset))  # dset是cset的子集吗？
