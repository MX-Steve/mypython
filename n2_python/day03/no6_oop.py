class Country:
    def __init__(self,name,city):
        self.name = name
        self.city = city

class Bear:
    def __init__(self,name,age,cname,city):
        self.name = name
        self.age = age
        self.country = Country(cname,city)
    def sing(self):
        print("i am %s"%self.name)

if __name__ == '__main__':
    lisi = Bear('lisi',25,'china','nanjing')
    print(lisi.name)
    print(lisi.age)
    lisi.sing()
    print(lisi.country.name)
    print(lisi.country.city)