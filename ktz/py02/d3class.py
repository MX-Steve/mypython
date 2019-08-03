class Warrior:
    def __init__(self,name,weapon):
        self.name=name
        self.weapon=weapon

    def say(self,words):
        print("I'm %s,%s"%(self.name,words))
    


if __name__ == '__main__':
    gy=Warrior('guanyu','qinglong')
    gy.say('guowuguan')