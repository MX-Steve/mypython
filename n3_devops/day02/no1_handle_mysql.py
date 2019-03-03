# import pymysql
#
# conn=pymysql.connect(
#     host="127.0.0.1",
#     port=3306,
#     user='root',
#     passwd='123456',
#     db='ktz',
#     charset='utf8'
# )
#
# cursor=conn.cursor()
# hr=(1,'hr')
# deps=[(2,'yunwei'),(3,'kaifa'),(4,'caiwu')]
# insert1="insert into departments values(%s,%s)"
# cursor.execute(insert1,hr)
# cursor.executemany(insert1,deps)
# conn.commit()
# cursor.close()
# conn.close()

import pymysql

conn=pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    passwd='123456',
    db='ktz',
    charset='utf8'
)

cursor=conn.cursor()
caiwu=(4,'caiwu')
sql1="insert into departments values(%s,%s)"
cursor.execute(sql1,caiwu)
conn.commit()
cursor.close()
conn.close()