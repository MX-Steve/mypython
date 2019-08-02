# import datetime
from datetime import  datetime,timedelta
# print(datetime.now())
# t1=datetime.now()
# print(t1.date(),t1.day)
# t2=datetime.strftime(t1,'%Y-%m-%d %H:%m:%s')
# print(t2)
# t3=datetime.strptime('2018-07-08 20:00:02', '%Y-%m-%d %H:%M:%S')
# print(t3.date())
# t4=datetime(2019,8,9)
# print(t4)

dt=timedelta(days=100,hours=4)
t=datetime.now()
print(t-dt)
print(t+dt)
