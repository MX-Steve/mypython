from random import randint

alist=list() #[]
print(list('hello'))
print(list((1,2,3,4))) # () => []
astr=str() # ''
print(str(10)) # 10 => '10'
print(str(['a','b','c','d'])) # [] => ""
atuple=tuple() # ()
print(tuple('hello')) #'' => ()
num_list=[randint(1,100) for i in range(10)]
print(num_list)
print(max(num_list))
print(min(num_list))
