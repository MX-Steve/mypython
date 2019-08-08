import requests
import json
import pprint

url='http://139.159.184.194/api_jsonrpc.php'
headers={'Content-Type':"application/json-rpc"}
####################################################
data1={
    "jsonrpc": "2.0",
    "method": "apiinfo.version",
    "params": [],
    "id": 1
    }

####################################################
# token
data2 = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
       "user": "Admin",
       "password": "zabbix"
    },
    "id": 1
   }
# token : 668842271f577272a68b0f95f944d74d
####################################################
data3={
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
       "output": "extend",
       "filter": {
          "host": [
             "Zabbix server",
             "web1",
             "web2"
          ]
      }
    },
    "auth": "668842271f577272a68b0f95f944d74d",
    "id": 1
}

####################################################
# 10255  web2
data4={
    "jsonrpc": "2.0",
    "method": "host.delete",
    "params": [
        "10255"
    ],
    "auth": "668842271f577272a68b0f95f944d74d",
    "id": 1
}
####################################################
data5={
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        "filter": {
           "name": [
               "Linux servers",
               "web"
            ]
        }
   },
   "auth": "668842271f577272a68b0f95f944d74d",
   "id": 1
  }
# web groupid: 15
####################################################
data6={
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": "extend",
        "filter": {
             "host": [
                  "Template OS Linux"
             ]
         }
    },
    "auth": "668842271f577272a68b0f95f944d74d",
    "id": 1
 }
 # Template OS Linux: 10001
####################################################
data={
    "jsonrpc": "2.0",
    "method": "host.create",
       "params": {
          "host": "web2",
          "interfaces": [
             {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.12",
                "dns": "",
                "port": "10050"
             }
          ],
          "groups": [
             {
                "groupid": "15"
                                                                                                                  }
          ],
          "templates": [
             {
               "templateid": "10001"
             }
          ],
          "inventory_mode": 0,
          "inventory": {
             "macaddress_a": "01234",
             "macaddress_b": "56768"
          }
     },
     "auth": "668842271f577272a68b0f95f944d74d",
     "id": 1
 }
####################################################
r=requests.post(url,headers=headers,data=json.dumps(data))
print(pprint.pprint(r.json()))
