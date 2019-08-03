print(("192.168.1.%s"%i for i in range(1,255)))

ips=("192.168.1.%s"%i for i in range(1,255))
# for i in ips:
#     print(i)

def mygen():
    yield 100
    a=10+20
    yield a
    yield 300

mg=mygen()
for n in mg:
    print(n)