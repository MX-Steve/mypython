import random

# def add(a,b):
#     return a+b
#
# def reduce(a,b):
#     return a-b

def show_main():
    opts={'+':lambda a,b:a+b,"-":lambda a,b:a-b}
    Prompt="""continue?[y/n]>"""
    while True:
        try:
            your=input(Prompt).strip()[0]
        except:
            break
        if your == 'n':
            break
        if your in 'yY':
            nums=[random.randint(1,101) for i in range(2)]
            nums.sort(reverse=True)
            opt=random.choice('+-')
            # print("%s%s%s=?"%(nums[0],opt,nums[1]))
            answer=opts[opt](*nums)
            n=0
            while n < 3:
                try:
                    your=int(input("%s%s%s="%(nums[0],opt,nums[1])))
                except:
                    continue
                n+=1
                if your == answer:
                    print("you are very clever!")
                    break
                print("the wrong number!")
            else:
                print("the answer is %s"%answer)


if __name__ == '__main__':
    show_main()