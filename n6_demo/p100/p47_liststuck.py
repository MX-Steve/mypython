stack=[]

def push_it():
  item = input('item to push: ')
  stack.append(item)

def pop_it():
  if stack:  
    print("from stack popped %s"%(stack.pop()))
  else:
    print("stack中无数据")

def view_it():
  print(stack)

def view_menu():
  cmds={'0':push_it,'1':pop_it,'2':view_it}
  prompt="""(0) push it
(1) pop it
(2) view it
(3) exit
please input your choice(0|1|2|3):"""
  while True:
    choice=input(prompt).strip()[0] # strip()去除两端空白，再取下标为0的一个字符
    if choice not in '0123':
      print("Invalid input")
      continue
    if choice == '3':
      break
    cmds[choice]()

if __name__=="__main__":
  view_menu()
