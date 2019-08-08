import json

adict={'name':'tom','age':20}
jdata=json.dumps(adict)
print(type(jdata))

bdict=json.loads(jdata)
print(bdict)
