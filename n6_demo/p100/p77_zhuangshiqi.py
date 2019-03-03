def color(func):
  def red():
    return '\033[31;1m%s\033[0m' % func()
  return red

def hello():
  return 'Hello World!'

@color
def welcome():
  return "Hello China"

if __name__=="__main__":
  hello=color(hello)
  print(hello())
  print(welcome())
