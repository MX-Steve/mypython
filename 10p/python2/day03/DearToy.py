# class BearToy:
#     def __init__(self,name,color,size):
#         self.name=name
#         self.color=color
#         self.size=size
#
#     def sing(self,geci):
#         print("i am %s , %s lalala..."%(self.name,geci))
#
# if __name__ == '__main__':
#     bear1=BearToy('xiongda','brown','large')
#     bear2=BearToy('xionger','white','middle')
#     print(bear1.name)
#     print(bear2.size)
#     bear2.sing('xixihaha')


class Weapon:
    def __init__(self,name,strength):
        self.name=name
        self.strength=strength


# class Mage:
#     def __init__(self,name,weapon_name,weapon_strength):
#         self.name=name
#         self.weapon=Weapon(weapon_name,weapon_strength)
#     def speak(self,words):
#         print("i am %s,i have %s,%s"%(self.name,self.weapon,words))
#     def move(self):
#         print("i can fly.")

class Mage:
    def __init__(self,name,weapon):
        self.name=name
        self.weapon=weapon
    def speak(self,words):
        print("i am %s,i have %s,%s"%(self.name,self.weapon,words))
    def move(self):
        print("i can fly.")


class Wizard(Mage):
    pass
    # super(Wizard,self).__init__(name,cloth)


class Sorceress(Mage):
    pass

if __name__ == '__main__':
    harry = Wizard('hamlet','saoba')
    herm = Sorceress('rouce','nvsaoba')
    harry.move()
    herm.move()
    # m1=Mage("hamlet",'saobao',1000)
    # m1.speak('hahahehe')
    # print(m1.weapon.name,m1.weapon.strength)
    # m2=Mage('sunwukong','jinggubang',200)
    # print(m2.weapon.name,m2.weapon.strength)




