import random
num=random.randint(1,10)
counter=0

while counter <5:
  answer=int(input("请输入："))
  if answer > num:
    print("\033[33;1m大了\033[0m")
  elif answer < num:
    print("\033[33;1m小了\033[0m")
  else:
    print("\033[32;1m对了\033[0m")
    break
  counter+=1
else:
  print("the number is:",num)
