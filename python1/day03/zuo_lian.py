#!/usr/bin/env python3
# action1
# import random
# all_choice=['jian','shi','bu']
# win=[['jian','bu'],['shi','jian'],['bu','shi']]
#
#
# prompt="""
# 0:jian
# 1:shi
# 2:bu
# please:
# """

# if [player,computer] in win:
#     print("you win!")
# else:
#     print("you lose!")

# if player == computer:
#     print("ping")
# elif [player,computer]in win:
#     print("you win")
# else:
#     print("you lose")

# action2
import random
all_choice=['jian','shi','bu']
win=[['jian','bu'],['shi','jian'],['bu','shi']]


prompt="""
0:jian
1:shi
2:bu
please:
"""
p=0
c=0
while p<2 and c<2:
    computer = random.choice(all_choice)
    player = all_choice[int(input(prompt))]
    if player == computer:
        print("ping")
        continue
    elif [player,computer]in win:
        print("you win")
        p+=1
    else:
        print("you lose")
        c+=1
if p==2:
    print("you win")
else:
    print("you lose")

