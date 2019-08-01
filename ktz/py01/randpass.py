# import random
#
# def getpass(n=8):
#     str=''
#     alls='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
#     for i in range(n):
#         str+=random.choice(alls)
#     return str
#
#
# if __name__ == '__main__':
#     print(getpass())
#     print(getpass(4))

from random import choice
from string import ascii_letters,digits

def getpass(n=8):
    str=""
    alls=ascii_letters+digits
    for i in range(n):
        str+=choice(alls)
    return str

if __name__ == '__main__':
    print(getpass())
    print(getpass(4))