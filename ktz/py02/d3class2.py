class A:
    def func1(self):
        print("A func")
    def func3(self):
        print("A func3")

class B:
    def func2(self):
        print("B func")
    def func3(self):
        print("B func3")

class C(A,B):
    pass

if __name__ == '__main__':
    c=C()
    c.func2()
    c.func1()
    c.func3()