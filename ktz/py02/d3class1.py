class Role:
    def __init__(self,name,weapon):
        self.name=name
        self.weapon=weapon
    def say(self,words):
        print("I'm saying:'%s'"%words)
    def run(self):
        print("i'm running")


class Warrior(Role):
    def __init__(self,name,gender,weapon):
        super(Warrior,self).__init__(name,weapon)
        # Role.__init__(self, name, weapon)
        self.gender=gender


    def show_me(self):
        print("I'm %s , i am a warrior "%(self.name))



if __name__ == '__main__':
    # gy=Warrior('guanyu','qinglong')
    # gy.say('guowuguan')
    # gy.show_me()
    wk=Warrior('sunwukong','nan','jinggubang')
    wk.show_me()
    wk.say('guowuguan,zhanliujiang')
