zhan=[]
def input_zhan():
    try:
        say=input("sth to zhan: ")
    except (KeyboardInterrupt,EOFError):
        return
    zhan.append(say)

def output_zhan():
    print("sth out zhan:")
    if len(zhan) == 0:
        print("none")
    else:
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
        # KeyboardInterrupt --> ctrl+c , EOFError
        try:
            your=input(prompt).strip()
        except (KeyboardInterrupt,EOFError):
            # print("bye...")
            # break
            your='3'

        if your[0] not in '0123':
            continue
        elif your == '3':
            print("\nbye...")
            break
        opts[your]()


if __name__ == '__main__':
    main()