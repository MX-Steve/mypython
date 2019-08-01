import random

dict={"0":'jiandao',"1":"shitou","2":"bu"}
list=['jiandao','shitou','bu']
wins=[('jiandao','bu'),('shitou','jiandao'),('bu','shitou')]
yn=0
cn=0
while True:
    computer=random.choice(list)
    your=input("input your result:")
    if your==computer:
        print("pingju")
    elif (your,computer) in wins:
        yn+=1
    else:
        cn+=1
    print("computer: "+computer)
    if yn >=2 or cn >=2:
        break
if yn == 2:
    print("\033[32;41;5myou win\033[0m")
else:
    print("\033[33;41;5myou lose\033[0m")
