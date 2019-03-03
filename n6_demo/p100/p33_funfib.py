def fib(num):
  fib=[0,1]
  for i in range(num-len(fib)):
    fib.append(fib[-1]+fib[-2])
  print(fib)
fib(3)
fib(5)
fib(10) 
