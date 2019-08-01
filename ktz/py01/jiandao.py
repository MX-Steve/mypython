import random

list=['jiandao','shitou','bu']
computer=random.choice(list)
print(computer)
your=input("input your result: ")
if your == computer:
    print("pingju")
elif your=='jiandao':
    if computer == "shitou":
        print("loser")
    else:
        print("winner")
elif your=="shitou":
    if computer=="bu":
        print("loser")
    else:
        print("winner")
else:
    if computer=="jiandao":
        print("loser")
    else:
        print("winner")