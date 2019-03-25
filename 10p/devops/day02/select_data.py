import pymysql

conn=pymysql.connect(
    host="176.4.16.101",
    port=3306,
    user='root',
    passwd='123456',
    db='tedu1',
    charset='utf8'
)

cursor=conn.cursor()
# sql1="insert into departments(dep_id,dep_name) values(%s,%s)"
# result=cursor.execute(sql1,(1,'renshibu'))

sql1="select * from departments;"
# opts=[(2,'yunwei'),(3,'kaifa')]
cursor.execute(sql1)
result=cursor.fetchone()
print(result)
print("*"*30)
result=cursor.fetchmany(2)
print(result)
print("*"*30)
result=cursor.fetchall()
print(result)



conn.commit()
cursor.close()
conn.close()