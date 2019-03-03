#!/usr/bin/env python3
#dict
# print(dict([('name','bob'),("age",25)]))
adict={"name":"bob","age":25}
# print("bob" in adict)
# print("name" in adict)
# print(len(adict))
# for key in adict:
#     print("%s: %s"%(key,adict[key]))
#
# print("%(name)s: %(age)s" % adict)
# adict['school']='tarena'
# print(adict)
# adict['email']='ktz@tedu.cn'
# print(adict)
print(adict.get('name'))
print(adict.get('qq','123456'))
print(adict.get('name','tom'))
print(adict.keys())
print(adict.values())
print(adict.items())
adict.pop('age')
print(adict)
bdict=adict.copy()
cdict=adict
print(id(bdict))
print(id(adict))
print(id(cdict))
adict.update({"name":"tom","age":29})
print(adict)