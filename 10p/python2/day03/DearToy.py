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



class Mage:
    def __init__(self,name,weapon):
        self.name=name
        self.weapon=weapon
    def speak(self,words):
        print("i am %s,i have %s,%s"%(self.name,self.weapon,words))

if __name__ == '__main__':
    m1=Mage("hamlet",'saobao')
    m1.speak('hahahehe')






    