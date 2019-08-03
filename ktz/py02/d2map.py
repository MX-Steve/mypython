from random import randint

nums=[randint(1,100) for i in range(10)]

print(nums)
print(list(map(lambda x:2*x+1,nums)))
