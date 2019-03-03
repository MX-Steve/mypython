import random
all_choices=["剪刀","石头","布"]
win_list=[["剪刀","布"],["石头","剪刀"],["布","石头"]]
prompt="""[0]剪刀
[1]石头
[2]布
"""
cwin=0
pwin=0
while pwin <2 and cwin<2:
  computer=random.choice(all_choices)
  yours=all_choices[int(input(prompt))]
  print("Y:%s,C:%s"%(yours,computer))
  if yours==computer:
    print("平局")
  if [yours,computer] in win_list:
    print("你赢了")
    pwin+=1
  else:
    print("你输了")
    cwin+=1


