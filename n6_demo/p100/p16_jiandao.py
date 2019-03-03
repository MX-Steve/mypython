import random
all_choices=["剪刀","石头","布"]
computer=random.choice(all_choices)
prompt="""请：
剪刀
石头
布
"""
player= input(prompt)
wins=[["剪刀","布"],["石头","剪刀"],["布","石头"]]
print("computer :",computer)
if player==computer:
  print("平局")
elif [player,computer] in wins:
  print("你赢了")
else:
  print("你输了")

