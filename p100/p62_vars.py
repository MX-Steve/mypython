x=10 # 全局变量从定义开始到程序结束，一直可见可用

def foo():
  print(x)

foo()

def bar():
  x=20 # 此处的x是局部变量，将全局变量遮盖住，不会影响全局变量的值
  print(x)

bar()
print(x) # x->10

def aaa():
  global x  # 在局部引用全局变量
  x = 100
  print(x) # 100

aaa()

print(x)  # 100
