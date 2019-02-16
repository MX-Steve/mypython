import time

t=time.localtime() # 返回当前时间的九元组
print(t)
print(time.gmtime()) # 返回格林威治0时区当前时间的九元组
print(time.mktime(t)) # 把九元组转换成时间戳
time.sleep(1)
print(time.asctime())
print(time.ctime()) # 返回当前时间，参数是时间戳，常用
print(time.strftime("%Y-%m-%d")) # 常用
print(time.strptime("2018-08-08","%Y-%m-%d")) #返回九元组时间格式
print(time.strftime("%H:%M:%S"))
from datetime import datetime
from datetime import timedelta
print(datetime.today()) # 返回当前时间的datetime对象
print(datetime.now()) # 同上， 可以用时区作参数
dt=datetime.today()
print(datetime.ctime(dt))
print(datetime.strftime(dt,"%Y%m%d"))

days = timedelta(days=90,hours=3)
dt2=dt+days
print(dt2.year)
print(dt2.month)
print(dt2.day)
print(dt2.hour)
