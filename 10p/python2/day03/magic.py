class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __str__(self):
        return "<%s>  %s"%(self.title,self.author)

    def __call__(self, *args, **kwargs):
        print("<%s>"%self.title)

if __name__ == '__main__':
    core_py=Book(' ')
    print(core_py)
    core_py()