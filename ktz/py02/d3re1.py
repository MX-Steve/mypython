#sys, os , string , getpass , shutil , re , pickle , time , datetime , random , functools

import re
# print(re.match('f..','food'))  # match from begin
# print(re.match('f..','seafood'))
m=re.match('f..','food')
# print(m.group())
m1=re.search('f..','food') # search from one , wherever
m2=re.search('f..','seafood is food')
m3=re.findall('f..','seafood is food')
m4=re.finditer('f..','seafood is food')
# print(m1.group())
# print(m2.group())
# print(m3)
# print(m4)
# for m in m4:
#     print(m.group())

a=re.split(' |\.','hello greet welcome.ni.hao')
# print(a)
b=re.sub('X','bob','Hi X, ni hao X')
# print(b)

c=re.sub('X','tom',"""hi X:
how are you ?
i miss you X""")
# print(c)

cpatt=re.compile('f..')
m=cpatt.search('seafood')
# print(m.group())
# print(cpatt.findall('seafood is food'))
d=cpatt.finditer('seafood is food !')
# for i in d:
#     print(i.group())

# pprint , sys , os , getpass , subprocess , random , date , datetime , shutil , re , functools , string , collections , pickle