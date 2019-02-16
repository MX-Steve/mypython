adict=dict([('name','tom'),('age',28)])
print(len(adict))
print(hash(10))
print(adict.keys())
print(adict.values())
print(adict.items())
print(adict.get('name'))
print(adict.get('qq')) # 不存在，返回none
print(adict.get('qq','not found')) # 不存在，返回指定的内容
print(adict.get('age','not found'))
adict.update({'phone':'18262629870'})
print(adict)
