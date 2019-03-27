import requests
import json

headers={"Content-Type":"application/json-rpc"}

###############################################################

# data = {
#     "jsonrpc": "2.0",
#     "method":"apiinfo.version",
#     "params":[],
#     "id":1
# }

# data = {
#     "jsonrpc": "2.0",
#     "method":"user.login",
#     "params":{
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id":1
# }

# d8e3932b37a7a65078bda168bec8f35a

# data = {
#     "jsonrpc":'2.0',
#     "method":"host.get",
#     "params":{
#         "filter":{
#             "host": [
#                 "ecs-zabbix.novalocal"
#             ]
#         }
#     },
#     "auth":"d8e3932b37a7a65078bda168bec8f35a",
#     "id":1
# }



data = {
    "jsonrpc":'2.0',
    "method":"host.create",
    "params":{
        "host": "web1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "userip": 1,
                "ip": "192.168.1.251",
                "dns":"",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid" : "2"
            }
        ],
        "templates": [
            {
                "templateid": "1001"
            }
        ],
        "inventory_mode": 0,
        "inventory" : {
            "macaddress_a" : "01234",
            "macaddress_b" : "56789"
        }
    },
    "auth":"d8e3932b37a7a65078bda168bec8f35a",
    "id":1
}

###############################################################

url ="http://139.9.6.199/api_jsonrpc.php"
r = requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())
