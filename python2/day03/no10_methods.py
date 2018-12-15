# from datetime import datetime
#
# class MyClass:
#     def hello(self):
#         print("hello world")
#
#     @staticmethod  # jing tai fang fa zhi jie diao yong , wu xu shi li
#     def welcome():
#         print("ni hao")
#
#     @classmethod # lei fang fa
#     def greet(cls):
#         print("how are you?")
#
# if __name__ == '__main__':
#     # MyClass.hello() # bao cuo , bu neng zhi jie diao yong , xu yao tong guo shi li diao yong
#     MyClass.welcome()
#     MyClass.greet()

# 方法：静态方法，类方法，这两种无需创建实例，可以直接使用
# ]# 魔法方法：init , str , call
# init :  初始化实例属性
# str : 创建对象后，打印实例对象，返回指定字符串，而不是class类
# call : 创建对象后，可以像调用函数一样调用该方法，模拟函数的行为

class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def hello(cls):
        print("Hello world!!!")

    @staticmethod
    def greet():
        print("ni hao!")

    def __str__(self):
        return "<%s>"%self.name

    def __call__(self, *args, **kwargs):
        print("%s is %s years old"%(self.name,self.age))

class Man(People):
    def __init__(self,name,age,school):
        # self.people = People(self,name,age)
        self.school=school

    def Car(self):
        print("This is my Car!")

class Girl(People):
    pass

if __name__ == '__main__':
    People.hello()
    People.greet()
    lisi = Man('lisi',25,'xian')
    lisi.Car()
    # print(lisi.name)
    print(lisi.school)
    p=People('lisi',28)
    print(p)
    p()