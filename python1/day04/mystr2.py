#!/usr/bin/env python3
# #zhuan yi zi fu: \n \r \t ...
# winpath='c:\windows\newfile'
# print(winpath)
# winpath1='c:\windows\\newfile'
# print(winpath1)
# #r'xxx': yuan shi zi fu chuan.
# winpath2=r'c:\windows\newfile'
# print(winpath2)

mystr='hello'
# #capitalize:shou zi mu da xie == title
# print(mystr.capitalize())
# print(mystr.title())
# #center: zai zhi ding kuan du zhong ju zhong
# #di er ge can shu biao shi tian chong zi fu
# print(mystr.center(50))
# print(mystr.center(50,'*'))
#count:tong ji zhi ding zi fu chu xian de zishu
#count(str,start,end) zhi ding fan wei nei
print(mystr.count('l'))
mystr="this is a dog"
print(mystr.count('is'))
print(mystr.count('is',4,100))
