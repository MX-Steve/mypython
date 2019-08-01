'''
hi
pstar
'''
from random import randint,choice
import getpass as gp

hi='hello world'
def pstar(n=30):
    print("*"*n)

if __name__ == '__main__':
    y=gp.getpass()
    print(hi)
    pstar()
    print(randint(10,20))
    print(choice('abcd'))