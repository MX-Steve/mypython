# blist=[11,21,12,32,15]
# print(sorted(blist))
#
# alist=[1,2,3,4,5]
# # print(list(enumerate(alist)))
# # for item in enumerate(alist):
# #     print(item)
# #
# # for k,v in enumerate(alist):
# #     print("%s:%s"%(k,v))
# #
# # print(list(reversed(alist)))
#
# print(sorted('ardbqwd'))

import string
import keyword
fstr=string.ascii_letters+'_'

ostr=string.ascii_letters+string.digits+'_'

def check_ok(str):
    if keyword.iskeyword(str):
        return "%s is key word"%str
    if str[0] not in fstr:
        return 'first letter is not valid'
    for k,v in enumerate(str[1:]):
        if v not in ostr:
            return "the %s is not valid in the %s"%(k+2,str)
    return '%s is valid'%(str)

def menu():
    print("please input your str")
    while True:
        str=input('end is funished>').strip()
        if str == 'end':
            break
        print(check_ok(str))


if __name__ == '__main__':
    # menu()
    print('abc'.isidentifier())
    print('%010d'%25)
    print('97 is %c'%97) # ASCII -> letter
    print('%f aa'%5.7)
    print("%5.2f aaa"%1239995.7)