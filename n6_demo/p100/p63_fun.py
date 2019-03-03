def get_age(name,age):
  print("%s is %s years old"%(name,age))

get_age('tom',24) #参数按顺序传递
get_age(24,'tom') #没有语法错误，但是语义不对
get_age(age=25,name='bo')
# get_age() #Error, 少参数
# get_age('bob',25,100) # Error,多参数
# get_age(age=25,'bob') #语法错误
# get_age(25,name='bob') #错误，参数按顺序传递，name得到多个值
get_age('bob',age=25)
