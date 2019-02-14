adict=dict() # {}
print(dict([('name1','tom1')]))
bdict=dict([("name","tom"),("age",28)])
print(bdict)
cdict={}.fromkeys(['zs','ls','ww'],11)
print(cdict)

for key in bdict:
  print("%s : %s" % (key,bdict[key]))

print("%(name)s : %(age)s"%bdict)

bdict['name']='tom'
bdict['email']='tom@steve.cn'

print(bdict)

del bdict['email']
print(bdict)

bdict.pop('age')
print(bdict)
bdict.clear()
print(bdict)

