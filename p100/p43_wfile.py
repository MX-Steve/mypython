import os
def get_fname():
  while True:
    fname=input("请输入文件名：")
    if not os.path.isfile(fname):
      break
    print("文件已经存在")
  return fname

def get_content():
  contents=[]
  print("请输入文件内容，输入end表示结束")
  while True:
    content=input("> ").strip()
    if content == "end":
      break
    contents.append(content)
  return contents

def wfile(fname,content):
  with open(fname,'w') as fobj:
    for i in content:
      fobj.write(i)

if __name__ == "__main__":
  fname=get_fname()
  content=get_content()
  content=['%s\n'%line for line in content]
  wfile(fname,content)
















#import os
#
#def get_fname():
#  while True:
#    fname = input('filename:')
#    if not os.path.exists(fname):
#      break
#    print('%s already exists. Try again'%fname)
#  return fname
#
#def get_content():
#  content =[]
#  print('输入数据，输入end结束')
#  while True:
#    line = input('> ')
#    if line == 'end':
#      break
#    content.append(line)
#
#  return content
#
#def wfile(fname,content):
#  with open(fname,'w') as fobj:
#    fobj.writelines(content)
#
#
#if __name__=="__main__":
#  fname=get_fname()
#  content=get_content()
#  content=['%s\n' % line for line in content]
#  wfile(fname,content)
