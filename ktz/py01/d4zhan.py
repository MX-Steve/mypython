zhan=[]
def input_zhan():
    say=input("sth to zhan: ")
    zhan.append(say)

def output_zhan():
    print("sth out zhan:")
    zhan.pop()

def show_zhan():
    print(zhan)

def main():
    prompt="""please choice one:>
0> input_zhan
1> output_zhan
2> show_zhan
3> quit"""
    opts={'0':input_zhan,'1':output_zhan,'2':show_zhan}
    while True:
        your=input(prompt).strip()
        if your[0] not in '0123':
            continue
        elif your == '3':
            print("bye...")
            break
        opts[your]()

    pass

if __name__ == '__main__':
    main()