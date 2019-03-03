class A:
    def __init__(self,name,age):
        self.name=name
        self.age = age

    def say(self):
        print("%s is %s years old"%(self.name,self.age))

    def __call__(self, *args, **kwargs):
        print("aaa")
    def __str__(self):
        return "xxxx"

if __name__ == '__main__':
    # A('lis',28)
    lisi=A('lisi',28)
    print(lisi.name)
    lisi.say()
    lisi()
    print(lisi)