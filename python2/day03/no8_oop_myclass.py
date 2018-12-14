class A:
    def foo(self):
        print("ni hao")

class B:
    def bar(self):
        print("hello")

class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def pstar(self):
        print("*"* 30)


if __name__ == '__main__':
    c=C('lisi',18)
    c.foo()
    c.bar()
    c.pstar()