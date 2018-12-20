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
delete1="delete from departments where dep_id=%s"
cursor.execute(delete1,(4,))
conn.commit()
cursor.close()
conn.close()