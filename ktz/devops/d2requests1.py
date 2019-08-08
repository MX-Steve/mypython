import requests
#url="http://www.kuaidi100.com/query"
#params={'type':'youzhengguonei','postid':'9893442769997'}
#r=requests.get(url,params=params)
#print(r.json())

url="http://www.jianshu.com"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.64 Safari/537.36'}
r=requests.get(url,headers=headers)
print(r.text)
