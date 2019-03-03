import re

# print(re.match('f..','food')) # cong kai tou pi pei : match
# print(re.match('f..','seafood'))
#
# print(re.search('f..','food'))
# m=re.search('f..','seafood')# pi pei nei rong di yi ge : search, pi pei ting zhi
# print(m.group()) # fan hui pi pei dao de nei rong:group
#
# print(re.findall('f..','seafood is food')) # fan hui lie biao : findall
# print(re.finditer('f..','seafood is food')) # fan hui die dai qi :finditer
# for m in re.finditer('f..','seafood is food'):
#     print(m.group())

# str1='food'
# str2='seafood is food'
#
# print(re.match('f..',str1))
# print(re.match('f..',str2))
# m=re.match('f..',str1)
# print(m.group())

# #]# re.split(a,b) #使用a进行切割b
# str3='hello-world.tar.gz'
# obj1=re.split('\.|\-',str3)
# print(obj1)
#
# ## re.sub(x,b,z) #将字符串z里的x，替换成b
# str4='Hi, X \nHello X'
# print(re.sub('X','lisi',str4))
# # 在匹配量很大的时候，先将模式进行编译，可以提升效率
# patt=re.compile('f..')
# m=patt.search('seafood')
# print(m.group())
# print(patt.findall('seafood is feed'))

str5="/etc/sysconfig/network-script/ifcfg-eth0"
print(re.split('\/',str5))