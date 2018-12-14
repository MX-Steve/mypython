class MyClass:
    def hello(self):
        print("hello world")

    @staticmethod  # jing tai fang fa zhi jie diao yong , wu xu shi li
    def welcome():
        print("ni hao")

    @classmethod # lei fang fa
    def greet(cls):
        print("how are you?")

if __name__ == '__main__':
    # MyClass.hello() # bao cuo , bu neng zhi jie diao yong , xu yao tong guo shi li diao yong
    MyClass.welcome()
    MyClass.greet()