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

# update1="update departments set dep_name='renliziyuanbu' where dep_name='renshibu'"
# cursor.execute(update1)

delete1="delete from departments where dep_id=%s"
cursor.execute(delete1,3)

conn.commit()
cursor.close()
conn.close()