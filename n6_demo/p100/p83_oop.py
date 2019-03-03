class BearToy:
  def __init__(self, nm, color, size):
    """__init__在实例化时自动执行，实例本身作为第一个参数传递给self，self只是习惯用的名字，不是必须使用
    """
    self.name= nm
    self.color=color
    self.size=size

  def sing(self):
    print('lalala...')

  def speak(self):
    print("My name is %s"% self.name)

if __name__=="__main__":
  tidy=BearToy('Tidy','white','large')
  print(tidy.color)
  print(tidy.size)
  tidy.sing()
  tidy.speak()
