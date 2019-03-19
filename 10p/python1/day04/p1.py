# from random import choice
# from string import  ascii_letters, digits
#
# def randpass(n=8):
#     # all_cs="1234567890qwertyuiopasdfghjklzxcvbnmQWETRYUIOPASDFGHJKLZXCVBNM"
#     all_cs=ascii_letters+digits
#     result = ''
#     for i in range(n):
#         result+=choice(all_cs)
#     return  result
# if __name__ == '__main__':
#     n=int(input('qingshuru:'))
#     print(randpass(n))

# import shutil
# # shutil.copy('/etc/hosts','/tmp/zj')
# # shutil.copy2('/etc/passwd','/tmp')
# # shutil.copytree('/etc/security','/tmp/anquan')
# shutil.rmtree('/tmp/anquan')
# import os
# os.remove('/tmp/zj')
#
# a , b = 10, 20
# a,b = b,a
# print(a,b)


import keyword

print(keyword.kwlist)
