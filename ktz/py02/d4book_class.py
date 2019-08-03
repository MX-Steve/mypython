class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
    def __str__(self):
        return "<%s>"%self.name
    def __call__(self):
        print("<%s> is %s written"%(self.name,self.author))

if __name__ == '__main__':
    core_py=Book('python core py','wiski')
    print(core_py)
    core_py()
