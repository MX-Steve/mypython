#!/usr/bin/env python3
"exam is very good!"

import random

def add(x,y):
    return x + y

def sub(x,y):
    return x - y


def exam():
    "+- suan fa"
    n=0
    jian = random.choice("+-")
    # type1
    # num1 = random.randint(0, 100)
    # num2 = random.randint(0, 100)
    # if num2 > num1:
    #     num1, num2 = num2, num1
    # if jian == '+':
    #     answer = num1 + num2
    # else:
    #     answer = num1 - num2
    # type2
    nums=[random.randint[1,100] for i in range(2)]
    nums.sort(reverse=True)
    if jian == '+':
        answer = nums[0]+nums[1]
    else:
        answer = nums[0]-nums[1]
    while True:

        # print("%s %s %s=?"%(num1,jian,num2))
        print("%s %s %s=?"%(nums[0],jian,nums[1]))
        yours=int(input("-->"))
        if yours == answer:
            print("you are right!")
            break
        n+=1
        if n>=3:
            print("answer is %s"%answer)

def main():
    while True:
        exam()
        yn=input("continue(y/n)").strip()[0]
        if yn in ['n','N']:
            break
if __name__ == '__main__':
    main()