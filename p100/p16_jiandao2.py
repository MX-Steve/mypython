import random
all_choices=["剪刀","石头","布"]
win_list=[["剪刀","布"],["石头","剪刀"],["布","石头"]]
prompt="""请出拳：
[0]剪刀
[1]石头
[2]布
"""
computer=random.choice(all_choices)
yours=all_choices[int(input(prompt))]
if yours==computer:
  print("\033[31;1m平局\033[0m")
elif [yours,computer] in win_list:
  print("\033[32;1m你赢了\033[0m")
else:
  print("\033[33;1m你输了\033[0m")
