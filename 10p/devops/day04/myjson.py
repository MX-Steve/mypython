import json
src={"name":'bob',"age":20}
print(json.dumps(src))
data = json.dumps(src)
print(type(data))
dst = json.loads(data)
print(type(dst))

