import requests

url = 'http://176.4.13.138/polls/2/vote'

data = {
    'choice_id':'11'
}
for i in range(100):
    r = requests.post(url,data=data)