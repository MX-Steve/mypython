import re
data="my phone is 18262629999"
m=re.search('.+?(\d+)',data)
print(m.groups())
print(m.group(1))
n=re.search('(.+?)(\d+)',data)
print(m.group(1))