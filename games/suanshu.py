#!/usr/bin/env python3
import kuang
import random
import jindutiao

def plus():
    prompt="""
输入 0: 退出>    
"""
    count=0
    err=0
    while True:
        print(prompt)
        num1=random.randint(1,100)
        num2=random.randint(1,100)
        answer=num1+num2
        try:
            yours=int(input("%s+%s=___;结果:>"%(num1,num2)))
        except ( EOFError,ValueError):
            print("\033[31m别瞎输入，正常点！\033[0m")
        except (ZeroDivisionError,KeyboardInterrupt):
            print("\033[31m不做个题，还想走？\033[0m")
        else:
		
            if err >=2:
                print("\033[31m小子，智商不行呀，太危险了，不能给你用!\033[0m")
                jindutiao.jdt()
            if yours == 0:
                if count >=1:
                    msg=["不错","下次再来哦!"]
                    kuang.win(msg)
                    # print("\033[32m不错，下次再来哦!\033[0m")
                    exit(1)
                else:
                    print("\033[31m小子，先至少回答对一道题，才能使用我的电脑哦！\033[0m")
            elif yours == answer:
                count+=1
                msg = ["不错"]
                kuang.win(msg)
            else:
                err+=1
                print("\033[31m你的答案不对呀\033[0m")

def menu():
    prompt="""[-------------使用须知--------------]
凡是用我的电脑的，必须智商够硬，否则请离开，如果挑战，做错3题也必须离开
0 : 离开
1 : 挑战
come on : >"""
    yours=input(prompt)
    if yours == "0":
        jindutiao.jdt()
    else:
        plus()
if __name__ == '__main__':
    menu()
