# f=open('/tmp/hosts','w')
# f.write('hello world\n')
# f.close()

# os , sys , getpass , random , subprocess , pickle , string , random , shutil

import  pickle

shopping_list=['apple','banana','orage']

with open('/tmp/shop.data','wb') as fobj:
    pickle.dump(shopping_list,fobj)

with open('/tmp/shop.data','rb') as fobj:
    list=pickle.load(fobj)

print(list)
print(type(list))

# os , sys , shutil , getpass , subprocess , pickle , string , random , date , datetime ,