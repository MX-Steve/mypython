#!/usr/bin/env python3
# #san zhong chuan can fang shi
# print("%d"%(3))
# print("%f"%(3.14))
# print("%f"%3.15)
# msg='my name is {}'.format('bob')
# print(msg)

# msg1='my name is {0[0]}, i am {0[1]} yesars old'.format(['bob',23])
# print(msg1)

# # {:[tian chong zi fu][dui qi fang shi <^>][kuan du]}
# msg='{:-^20}'.format('hello')
# print(msg)
# msg1='{:*>20}'.format('hello')
# print(msg1)
# msg2='{:-<20}'.format('hello')
# print(msg2)

#lian xi 1
def get_content():
    msgs=[]
    while True:
        msg=input("your msg>")
        if msg == 'exit':
            break
        msg="+"+'{: ^48}'.format(msg)+"+"
        msgs.append(msg)
    print("+" + "*" * 48 + "+")
    for ch in msgs:
        print(ch)
    print("+"+"*"*48+"+")

if __name__ == '__main__':
    content=get_content()