import pickle
import datetime
import os


def cost(zhangdan,qian):
    with open(qian,'rb') as fobj:
        total=pickle.load(fobj)
    money=int(input("cost: "))
    content=input("content: ")
    now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    left=total-money
    with open(qian,'wb') as fobj:
        pickle.dump(left,fobj)
    with open(zhangdan,'rb') as fobj:
        list=pickle.load(fobj)
    #list.append('%-15s%-15s%-15s%-15s%s'%(now,0,money,content,left))
    list.append([now,0,money,content,left])

    with open(zhangdan,'wb') as fobj:
        pickle.dump(list,fobj)

def save(zhangdan,qian):
    with open(qian,'rb') as fobj:
        total=pickle.load(fobj)
    money = int(input("cost: "))
    content = input("content: ")
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    left = total + money
    with open(qian,'wb') as fobj:
        pickle.dump(left,fobj)
    with open(zhangdan,'rb') as fobj:
        list=pickle.load(fobj)
    #list.append('%-15s%-15s%-15s%-15s%s'%(now,money,0,content,left))
    list.append([now,money,0,content,left])
    with open(zhangdan, 'wb') as fobj:
        pickle.dump(list, fobj)

def show(zhangdan,qian):
    with open(zhangdan,'rb') as fobj:
        list=pickle.load(fobj)
    for i in list:
        print('%-25s%-15s%-15s%-15s%s'%(i[0],i[1],i[2],i[3],i[4]))
    with open(qian,'rb') as fobj:
        total=pickle.load(fobj)
    print("left money > ",total)

def main():
    prompt="""please choice one: 
0> cost
1> save
2> show
3> quit"""
    opts={"0":cost,"1":save,"2":show}
    zhangdan = '/tmp/zhang.data'
    qian = '/tmp/money.data'
    if not os.path.exists(qian):
        with open(qian,'wb') as fobj:
            pickle.dump(10000,fobj)
    if not os.path.exists(zhangdan):
        with open(zhangdan,'wb') as fobj:
            list=[["time","save","cost","content","left"]]
            pickle.dump(list,fobj)
    while True:
        try:
            your=input(prompt).strip()
        except:
            your = '3'

        if your not in '0123':
            continue
        if your == '3':
            print("\nBye...")
            break
        opts[your](zhangdan,qian)


if __name__ == '__main__':
    main()