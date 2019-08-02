s1='123@#hello%$world100'
slist=[]
for ch in s1:
    if ch.isalpha():
        slist.append(ch)
print(slist)
print(''.join(slist))
print(''.join([i for i in s1 if i.isalpha()]))