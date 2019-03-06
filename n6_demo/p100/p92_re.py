import re

m = re.match('f..','food') # 匹配到返回对象
#print(m)
#print(re.match('f..','seafood')) # 匹配不到返回None
m.group()
re.findall('f..','seafood is food') # 返回所有匹配组成的列表
result = re.finditer('f..','seafood is food') # 返回匹配对象组成的迭代器
for m in result:
  print(m.group())

# 使用abc，替换f..匹配到的字符
re.sub('f..','abc','fish is food')
# 用.和-切割后面字符串
re.split('\.|\-','hello-world.tar.gz')

patt = re.compile('f..') # 先把要匹配的模式编译，提升效率
m = patt.search('seafood')
m.group()
