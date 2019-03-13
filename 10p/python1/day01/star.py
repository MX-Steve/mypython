# print('ok')
# alist=['tom','jerry',10,20,[1,2,3]]
# alist.append(200)
# print(alist)
# alist.insert(0,100)
# print(alist)
# for i in alist:
#     print(i)

# f = open('/tmp/passwd','rb')
# print(f.tell())
# f.read(5)
# print(f.tell())
# print(f.readline())
# f.seek(0,0)
# print(f.readline())

src='/bin/ls'
dst='/tmp/list'
with open(src,'rb') as fobj:
    with open(dst,'wb') as dobj:
        data=fobj.read()
        dobj.write(data)