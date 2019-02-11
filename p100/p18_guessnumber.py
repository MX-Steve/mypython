import random

num=random.randint(1,10)
running=True

while running:
  answer=int(input("请输入："))
  if answer > num:
    print("大了")
  elif answer < num:
    print("小了")
  else:
    print("猜对了")
    running=False
