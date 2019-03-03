class Book:
    def __init__(self,title,author):
        self.title=title
        self.author = author

    def __str__(self):
        return "<%s>"%self.title

    def __call__(self, *args, **kwargs):
        print("<%s> is written by %s" %(self.title,self.author))

if __name__ == '__main__':
    core_py=Book('python core process', 'wesley')
    print(core_py) #diao yong str fang fa
    core_py() #diao yong call fang fa