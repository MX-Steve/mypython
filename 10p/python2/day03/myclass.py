class A:
    def hello(self):
        print("A: hello")
    def foo(self):
        print("A: foo")

class B:
    def greet(self):
        print("B: how are you?")
    def foo(self):
        print("B: foo")

class C(B,A):
    pass

if __name__ == '__main__':
    c1=C()
    c1.greet()
    c1.hello()
    c1.foo()