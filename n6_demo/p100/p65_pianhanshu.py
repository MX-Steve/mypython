#偏函数可以理解为，将现有函数的某些参数固定下来，构成一个新函数，新函数调用就不用写那么多参数了
from functools import partial
def foo(a,b,c,d,e):
  return a+b+c+d+e

if __name__=="__main__":
  print(foo(10,20,30,40,5))
  print(foo(10,20,30,40,15))
  print(foo(10,20,30,40,25))
  print(foo(10,20,30,40,35))
  add = partial(foo,a=10,b=20,c=30,d=40)
  print(add(e=45))
  print(add(e=55))
