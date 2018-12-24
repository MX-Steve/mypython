import requests

r = requests.get('http://127.0.0.1/')
print(r.text)

# p = requests.get('http://tts.tmooc.cn/ttsPage/LINUX/NSDTN201801/DEVOPS/DAY04/CASE/01/index.files/image006.png')
p = requests.get('https://www.baidu.com/img/xinshouye_ef8bb3d1d46a8b05760b91e24624b839.png')
with open('/tmp/ttt.img', 'wb') as fobj:
    fobj.write(p.content)
# eog /tmp/ttt.img

r1 = requests.get('http://www.weather.com.cn/data/sk/101010100.html')
print(r1.json())
print(r1.encoding)
r1.encoding='utf8'
print(r1.json())