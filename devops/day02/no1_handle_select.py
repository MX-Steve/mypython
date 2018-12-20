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
query1="select * from departments order by dep_id"
cursor.execute(query1)
result=cursor.fetchone()
print(result)
print("-"*30)
result=cursor.fetchmany(2)
print(result)
print('-'*30)
cursor.scroll(0,mode="absolute")
result=cursor.fetchall()
print(result)