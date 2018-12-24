import requests
import json

url="http://139.9.6.199/api_jsonrpc.php"
headers = {'Content-Type':"application/json-rpc"}



data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid", "host"],
        "selectInterfaces": ["interfaceid", "ip"]
    },
    "auth": "6c7e82c22a3233e17d2ddfa491df9526",
    "id": 1
}
r = requests.post(url,headers=headers, data=json.dumps(data))
print(r.json())