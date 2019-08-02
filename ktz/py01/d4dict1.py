adict={'name':'tom','age':20}
print('name' in adict)
for key in adict:
    print(key,adict[key])

print('%(name)s: %(age)s' % adict)

adict[(1,2)]=10
print(adict)
print(adict.items())
for key,val in adict.items():
    print(key,val)

print(adict.keys())
print(adict.values())
adict.update({'qq':'2102227265','phone':17267678971})
print(adict)

adict.popitem()
print(adict)
adict.pop('name')
print(adict)

print(adict.get('age'))
print(adict.get('age1',28))