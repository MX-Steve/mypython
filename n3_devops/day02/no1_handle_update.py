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
upate1="update departments set dep_name=%s where dep_name=%s"
data=('HRB','hr')
cursor.execute(upate1,data)
conn.commit()
cursor.close()