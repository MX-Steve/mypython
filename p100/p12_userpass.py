import getpass

username=input("请输入用户名：")
password=getpass.getpass("请输入密码：")

if username=="bob" and password=="123":
  print("welcom")
else:
  print("username or password error!")
