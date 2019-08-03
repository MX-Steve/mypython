# def jiecheng(n):
#     if n == 1:
#         return 1
#     return n*jiecheng(n-1)
#
# print(jiecheng(2))
# print(jiecheng(3))
# print(jiecheng(4))
# print(jiecheng(5))
#
# s=1
# for i in range(1,6):
#     s*=i
# print(s)
from random import randint

alist=[randint(1,100) for i in range(10)]

def quit_sort(alist):
    if len(alist) < 2:
        return alist
    mid=alist[0]
    smaller=[]
    larger=[]
    for i in alist[1:]:
        if mid >=i:
            smaller.append(i)
        else:
            larger.append(i)
    return quit_sort(smaller)+[mid]+quit_sort(larger)

print(alist)
print(quit_sort(alist))