
import pymysql

conn=pymysql.connect(
    host='192.168.4.14',
    port=3306,
    user='lihan',
    passwd='123456',
    db='nsd1903',
    charset='utf8'
)

cursor=conn.cursor()

insert_dep="INSERT INTO department values(%s,%s)"
# hr=(1,'renshi')
# ops=(2,'yunwei')
# dev=(3,'kaifa')
# qa=(4,'ceshi')
# deps=[ops,dev,qa]
# cursor.execute(insert_dep,hr)
# cursor.executemany(insert_dep,deps)

# delete_dep="delete from department where dep_name=%s"
# cursor.execute(delete_dep,('renshi',))

# update_dep="UPDATE department SET dep_name=%s WHERE dep_name=%s"
# cursor.execute(update_dep,('gaojikaifa','kaifa'))

# market=(5,'shichang')
# finance=(6,'caiwu')
# sales=(7,'xiaoshou')
# cursor.executemany(insert_dep,(market,finance,sales))

# query_dep="SELECT * FROM department"
# cursor.execute(query_dep)
# result1=cursor.fetchone()
# print(result1)
# print("*"*40)
# result2=cursor.fetchmany(2)
# print(result2)
# print("*"*40)
# result3=cursor.fetchall()
# print(result3)
# print("*"*40)

query_dep="SELECT * FROM department"
cursor.execute(query_dep)
cursor.scroll(3,mode='absolute')
result=cursor.fetchone()
print(result)
print("*"*40)
cursor.scroll(1)
result2=cursor.fetchone()
print(result2)
print("*"*40)


conn.commit()

cursor.close()
conn.close()