from random import randint,choice

def add(x,y):
  return x+y

def sub(x,y):
  return x-y

def plus(x,y):
  return x*y

def redu(x,y):
  return x/y

def exam():
  nums=[randint(1,10) for i in range(2)]
  nums.sort(reverse=True)
  opt=choice('+-*/')
  cmds={'+':add,'-':sub,'*':plus,'/':redu}
  prompt="%s%s%s="%(nums[0],opt,nums[1])
  result=cmds[opt](*nums)
  tries=0
  while tries <3:
    try:
      answer=int(input(prompt))
    except:
      continue
    if answer==result:
      print('\033[32mgood!\033[0m')
      break
    else:
      print('\033[31merror!\033[0m')
      tries+=1
  else:
    print("%s%s"%(prompt,result))
if __name__=="__main__":
  while True:
    exam()
    try:
      yn=input('Continue(y/n)?').strip()[0]
    except IndexError:
      continue
    except (KeyboardInterrupt,EOFError):
      print()
      yn='n'
    if yn in 'nN':
      break





















#from random import randint , choice
#
#def add(x,y):
#  return x + y
#
#def sub(x,y):
#  return x - y
#
#def exam():
#  cmds={'+':add,'-':sub}
#  nums=[randint(1,100) for i in range(2)]
#  nums.sort(reverse=True)
#  op = choice('+-')
#  result = cmds[op](*nums)
#  prompt="%s%s%s="%(nums[0],op,nums[1])
#  tries=0
#
#  while tries<3:
#    try:
#      answer=int(input(prompt))
#    except:
#      continue
#
#    if answer == result:
#      print('very good')
#      break
#    else:
#      print('wrong answer')
#      tries+=1
#  else:
#    print("%s%s"%(prompt,result))
#
#if __name__=="__main__":
#  while True:
#    exam()
#    try:
#      yn = input('Continue(y/n)?').strip()[0]
#    except IndexError:
#      continue
#    except (KeyboardInterrupt,EOFError):
#      print()
#      yn = 'n'
#    if yn in 'nN':
#      break
