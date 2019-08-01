# import random
#
# num=random.randint(1,100)
# running=True
#
# while running:
#     answer = int(input('guess(1-100): '))
#     if answer > num:
#         print("bigger")
#     elif answer < num:
#         print("smaller")
#     else:
#         print("right")
#         running=False


import random

num=random.randint(1,100)
count=0

while count<4:
    count+=1
    answer = int(input('guess(1-100): '))
    if answer > num:
        print("bigger")
    elif answer < num:
        print("smaller")
    else:
        print("right")
        break
else:
    print("answer is %s"%(num))