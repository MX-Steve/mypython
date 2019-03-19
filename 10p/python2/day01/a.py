a={'user':'lisi'}
print(a)
print(a.get('age',20))
print(a.keys())
for key in a.keys():
    print(key,a.get(key))

for key in a:
    print(key,a[key])

print(a.values())