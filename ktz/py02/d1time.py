import time

# print(time.ctime())
# print(time.time())
# print(time.localtime())
# t=time.localtime()
# print(t.tm_year)
# # time.sleep(3)
# # print('123')
# print(time.strftime('%Y%m%d %H:%M:%S'))
# print(time.strptime('2019-07-09 20:00:00','%Y-%m-%d %H:%M:%S'))

# get log content;
t1 = time.strptime('2019-05-06 01:00:00','%Y-%m-%d %H:%M:%S')
t2 = time.strptime('2019-05-06 05:00:00','%Y-%m-%d %H:%M:%S')
logfile='web.log'
with open(logfile) as fobj:
    for line in fobj:
        t = time.strptime(line[:19],'%Y-%m-%d %H:%M:%S')
        if t > t2:
            break
        if t1 <= t <= t2:
            print(line,end='')