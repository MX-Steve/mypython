import random

num=random.randint(1,10)

answer=int(input("请输入数字："))

if answer > num:
  print("大了")
elif answer < num:
  print("小了")
else:
  print("猜对了")

print("the number:",num)
