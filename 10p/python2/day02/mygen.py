def mygen():
    yield "hello world!"
    a = 10 + 20
    yield a
    yield [10,20,30]

if __name__ == '__main__':
    mg=mygen()
    print(mg.__next__())
    print(mg.__next__())
    print(mg.__next__())
    # print(mg.__next__())