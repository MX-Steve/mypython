import requests
import json

url="http://139.9.6.199/api_jsonrpc.php"
headers={"Content-Type":"application/json-rpc"}

data = {
    "jsonrpc" : "2.0",
    "method" : "host.get",
    "params" : {
        "output" : ["hostid","host"],
        "selectInTerfaces":["interfaceid","ip"]
    },
    "auth":"d8e3932b37a7a65078bda168bec8f35a",
    "id":1
}

r = requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())