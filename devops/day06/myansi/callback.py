def foo(fun, *args):
    print("processing")
    fun(*args)

def loop(num):
    for i in range(num):
        print(i)

if __name__ == '__main__':
    foo(loop, 10)