def func(n):
  if n==1:
    return n
  return n*func(n-1)

if __name__=="__main__":
  print(func(5))
  print(func(6))






#def func(n):
#  if n == 1:
#    return n
#  return n*func(n-1)
#
#if __name__=="__main__":
#  print(func(3))
#  print(func(5))
