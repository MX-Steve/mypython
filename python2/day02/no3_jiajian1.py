#!/usr/bin/env python3
"exam is very good!"

import random


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def exam():
    "+- suan fa"
    n = 0
    cmds = {'+':add,'-':sub}
    op = random.choice("+-")
    nums = [random.randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    answer = cmds[op](*nums)
    while True:

        # print("%s %s %s=?"%(num1,jian,num2))
        print("%s %s %s=?" % (nums[0], op, nums[1]))
        yours = int(input("-->"))
        if yours == answer:
            print("you are right!")
            break
        n += 1
        if n >= 3:
            print("answer is %s" % answer)
            break


def main():
    while True:
        exam()
        yn = input("continue(y/n)").strip()[0]
        if yn in ['n', 'N']:
            break


if __name__ == '__main__':
    main()