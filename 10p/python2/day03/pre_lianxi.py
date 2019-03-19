import time

def timeit(func):
    def todo():
        start = time.time()
        func()
        end = time.time()
        print("total time: ",(end-start))
    return todo

@timeit
def func1():
    print("func1 start")
    time.sleep(3)
    print("func1 end")

if __name__ == '__main__':
    # start = time.time()
    # func1()
    # end = time.time()
    # print("total time: ",(end-start))
    func1()