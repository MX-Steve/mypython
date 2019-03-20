import re
print(re.match('f..','food'))
m=re.search('f..','seafood')
print(m.group())
n=re.findall('f..','seafood is food')
print(n)
for i in re.finditer('f..','seafood is food'):
    print(i.group())
print(re.split('-|\.','hello-world-abc.123.txt'))
print('hello world'.replace('world','china'))
print(re.sub('X','tom','hi X,nihao'))
print(re.sub('X|Y','tom','hi X,nihao Y'))
cpatt = re.compile('f..')
print(cpatt.search('seafood').group())