class Weapon:
    def __init__(self,wname,strength):
        self.wname=wname
        self.strength=strength

class Warrior:
    def __init__(self,name,weapon):
        self.name=name
        self.weapon=weapon

    def say(self,words):
        print("I'm %s,%s"%(self.name,words))

    def show_me(self):
        print("I'm %s , i am a warrior, i use %s "%(self.name,self.weapon.wname))



if __name__ == '__main__':
    # gy=Warrior('guanyu','qinglong')
    # gy.say('guowuguan')
    # gy.show_me()
    blade=Weapon('qinglong',100)
    gy=Warrior('guanyu',blade)
    gy.show_me()
    cz=Weapon('jinggubang',100)
    wk=Warrior('sunwukong',cz)
    wk.show_me()