from random import randint , choice

def exam():
  nums=[randint(1,10) for i in range(2)]
  nums.sort(reverse=True)
  opt=choice('+-*')
  cmds={'+':lambda x,y: x+y, '-':lambda x,y: x-y,'*':lambda x,y:x*y}
  prompt="%s%s%s="%(nums[0],opt,nums[1])
  result=cmds[opt](*nums)
  tries=0
  while tries < 3:
    try:
      answer=float(input(prompt))
    except:
      continue
    if answer==result:
      print('ok')
      break
    else:
      print('error')
      tries+=1
  else:
    print("%s%s"%(prompt,result))

if __name__=="__main__":
  while True:
    exam()
    try:
      yn=input('Continue(y/n)?').strip()[0]
    except:
      print('Continue(y/n)?')
      continue
    if yn in 'nN':
      break

