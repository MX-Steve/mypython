# zi lei ji cheng fu lei

class Bear:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sing(self):
        print("i am %s"%self.name)

class NewBear(Bear):
    def __init__(self,name,age,date):
        # self.name = name
        # self.age = age
        # Bear.__init__(self,name,age)
        super(NewBear, self).__init__(name,age)
        self.date = date
    def run(self):
        print("i can run")

if __name__ == '__main__':
    big = NewBear('lisi',25,'2018-05-18')
    big.sing()
    big.run()